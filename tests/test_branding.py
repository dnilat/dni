"""Branding regression checks; run with python3 -m unittest discover -s tests -v."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ['index.html', 'en/index.html', 'privacidad/index.html', 'en/privacy/index.html']


class Elements(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.elements = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


class BrandingTests(unittest.TestCase):
    def test_each_header_uses_accessible_full_artwork_without_duplicate_text(self):
        for path in PAGES:
            with self.subTest(page=path):
                source = (ROOT / path).read_text()
                elements = Elements(source).elements
                brands = [attrs for tag, attrs in elements if tag == 'a' and attrs.get('class') == 'brand']
                self.assertEqual(len(brands), 1)
                self.assertIn('Donde Nacen las Ideas', brands[0]['aria-label'])
                logos = [attrs for tag, attrs in elements if tag == 'img' and attrs.get('class') == 'brand__logo']
                self.assertEqual(len(logos), 1, 'Header must show approved full logo artwork')
                logo = logos[0]
                self.assertEqual(logo.get('alt'), '')  # Link supplies the accessible name.
                self.assertEqual(logo.get('loading'), 'eager')
                self.assertEqual((logo.get('width'), logo.get('height')), ('1061', '682'))
                self.assertTrue((ROOT / logo['src'].lstrip('/')).is_file())
                self.assertNotIn('brand__mark', source)
                self.assertNotIn('brand__name', source)

    def test_every_route_advertises_versioned_favicon_and_touch_icons(self):
        expected = {
            '/assets/brand/dni-favicon-v1.ico': ('icon', 'image/x-icon', None),
            '/assets/brand/dni-icon-32-v1.png': ('icon', 'image/png', '32x32'),
            '/assets/brand/dni-icon-dark-32-v1.png': ('icon', 'image/png', '32x32'),
            '/assets/brand/dni-apple-touch-180-v1.png': ('apple-touch-icon', None, '180x180'),
        }
        for path in PAGES:
            with self.subTest(page=path):
                elements = Elements((ROOT / path).read_text()).elements
                icons = {attrs['href']: attrs for tag, attrs in elements if tag == 'link' and attrs.get('rel') in ('icon', 'apple-touch-icon')}
                self.assertEqual(set(icons), set(expected))
                for href, (rel, mime, sizes) in expected.items():
                    self.assertEqual(icons[href]['rel'], rel)
                    if mime:
                        self.assertEqual(icons[href].get('type'), mime)
                    if sizes:
                        self.assertEqual(icons[href].get('sizes'), sizes)
                    self.assertTrue((ROOT / href.lstrip('/')).is_file())
                self.assertEqual(icons['/assets/brand/dni-icon-dark-32-v1.png'].get('media'), '(prefers-color-scheme: dark)')
        approved = ROOT / 'assets/brand/originals/DNI-favicon.ico'
        self.assertEqual(approved.read_bytes(), (ROOT / 'assets/brand/dni-favicon-v1.ico').read_bytes())
        self.assertEqual(approved.read_bytes(), (ROOT / 'favicon.ico').read_bytes())


if __name__ == '__main__':
    unittest.main()
