"""Public team and portfolio contract for both locales."""
from pathlib import Path
import re
import unittest
from test_branding import Elements

ROOT = Path(__file__).resolve().parents[1]
HOMES = ('index.html', 'en/index.html')
PAGES = (*HOMES, 'privacidad/index.html', 'en/privacy/index.html')


class ContentTests(unittest.TestCase):
    def test_two_named_humans_lead_the_studio_in_both_languages(self):
        for path in HOMES:
            with self.subTest(page=path):
                source = (ROOT / path).read_text()
                for class_name in ('hero__intro', 'hero__facts', 'studio__statement', 'team-ledger', 'team__body'):
                    match = re.search(r'<[^>]+class="' + class_name + r'"[^>]*>(.*?)</(?:div|dl)>', source, re.S)
                    assert match is not None, class_name
                    section = match.group(1)
                    self.assertIn('Omar', section)
                    self.assertIn('Manny', section)
                self.assertIn('Dos humanos.' if path == 'index.html' else 'Two humans.', source)
                self.assertIn('Omar pone el contexto, el gusto y la última palabra.' if path == 'index.html' else 'Omar brings the context, the taste, and the final call.', source)
        for path in PAGES:
            with self.subTest(page=path):
                source = (ROOT / path).read_text()
                self.assertNotRegex(source.lower(), r'\bun humano\b|\bone human\b|\bel humano\b|\bthe human\b')

    def test_three_projects_link_to_their_public_sites(self):
        expected = ['https://factucat.com/', 'https://librochiquito.com/', 'https://rangosalud.com']
        for path in HOMES:
            with self.subTest(page=path):
                source = (ROOT / path).read_text()
                stages = re.findall(r'<article class="product-stage\b.*?</article>', source, re.S)
                self.assertEqual(len(stages), 3)
                for stage, url in zip(stages, expected):
                    links = [attrs for tag, attrs in Elements(stage).elements if tag == 'a']
                    self.assertEqual(len(links), 1)
                    self.assertEqual(links[0]['href'], url)
                    self.assertEqual(links[0]['target'], '_blank')
                    self.assertEqual(set(links[0]['rel'].split()), {'noopener', 'noreferrer'})
                self.assertIn('Conocer Rango' if path == 'index.html' else 'Meet Rango', stages[2])
                self.assertFalse(re.search(r'dos productos|two products|las dos ideas|the two ideas|two distinct product', source, re.I))
        for path in PAGES:
            with self.subTest(footer=path):
                source = (ROOT / path).read_text().split('<footer', 1)[1]
                self.assertIn('href="https://rangosalud.com"', source)


if __name__ == '__main__':
    unittest.main()
