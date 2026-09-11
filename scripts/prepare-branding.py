"""Regenerate branding with Pillow; preserve approved originals without redrawing."""
import argparse
from pathlib import Path
import shutil
from PIL import Image, IcoImagePlugin

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / 'assets/brand'
ORIGINALS = BRAND / 'originals'
NAMES = ['DNI-estudio-indie-transparente.png', 'DNI-isotipo-transparente.png', 'DNI-favicon.ico']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', type=Path, default=ORIGINALS)
    args = parser.parse_args()
    # Validate all inputs before copying or generating any output.
    for name in NAMES:
        with Image.open(args.source_dir / name) as source:
            source.verify()
    ORIGINALS.mkdir(parents=True, exist_ok=True)
    for name in NAMES:
        source = args.source_dir / name
        destination = ORIGINALS / name
        if source.resolve() != destination.resolve():
            if destination.exists() and source.read_bytes() != destination.read_bytes():
                raise FileExistsError(f'Refusing to replace approved original: {name}')
            shutil.copy2(source, destination)
    image = Image.open(ORIGINALS / NAMES[0]).convert('RGBA')
    bounds = image.getchannel('A').getbbox()
    image.crop(bounds).save(BRAND / 'dni-indie-v1.png', optimize=True)
    icon = Image.open(ORIGINALS / NAMES[2])
    assert isinstance(icon, IcoImagePlugin.IcoImageFile)
    print('Approved ICO sizes:', sorted(icon.ico.sizes()))
    png = icon.ico.getimage((32, 32)).convert('RGBA')
    png.save(BRAND / 'dni-icon-32-v1.png', optimize=True)
    white = Image.new('RGBA', png.size, 'white')
    white.putalpha(png.getchannel('A'))
    white.save(BRAND / 'dni-icon-dark-32-v1.png', optimize=True)
    isotipo = Image.open(ORIGINALS / NAMES[1]).convert('RGBA')
    isotipo.resize((180, 180), Image.Resampling.LANCZOS).save(BRAND / 'dni-apple-touch-180-v1.png', optimize=True)
    for destination in [BRAND / 'dni-favicon-v1.ico', ROOT / 'favicon.ico']:
        shutil.copy2(ORIGINALS / NAMES[2], destination)
    print('Logo: lossless crop', bounds, '->', image.crop(bounds).size)
    print('PNG/touch icons generated; ICO copies preserve exact approved bytes.')


if __name__ == '__main__':
    main()
