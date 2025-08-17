from pathlib import Path

from PIL import Image
import sphinxlint


MAX_IMAGE_SIZES = {  # in bytes
    '.png': 505000,
    '.gif': 2100000,
}
MODE_TO_BPP = {
    '1': 1, 'L': 8, 'P': 8, 'RGB': 24, 'RGBA': 32, 'CMYK': 32, 'YCbCr': 24, 'I': 32, 'F': 32
}


def log_error(file, line, msg, checker_name):
    """ Log an error in sphinx-lint's log format to ease the processing of linting errors on Runbot.
    """
    print(f"{file}:{line or 0}: {msg} ({checker_name})")


def check_image_size(file):
    """Zkontrolujte, zda jsou obrázky menší než maximální velikost souboru povolená pro jejich příponu."""
    file_path = Path(file)
    file_size = file_path.stat().st_size
    max_size = MAX_IMAGE_SIZES.get(file_path.suffix)
    if max_size and file_size > max_size:
        log_error(
            file_path,
            0,
            f"the file has a size of {round(file_size / 10**6, 2)} MB, larger than the maximum"
            f" allowed size of {round(max_size / 10**6, 2)} MB; compress it with pngquant",
            'image-size',
        )

def check_image_color_depth(file):
    """Zkontrolujte, zda jsou obrázky ve formátu PNG komprimovány na 8 bitů s pomocí programu PNGQuant."""
    file_path = Path(file)
    if file_path.suffix.lower() == '.png':
        data = Image.open(file)
        bpp = MODE_TO_BPP[data.mode]
        if bpp > 8:
            log_error(
                file_path,
                0,
                f"the file has a color depth of {bpp} instead of 8; compress it with pngquant",
                'image-color-depth'
            )

def check_resource_file_name(file_path):
    """Zkontrolujte, zda jsou názvy souborů zdrojů uvedeny pomocí podtržítka a ne podtržítkem."""
    if '_' in file_path.split('/')[-1]:
        log_error(
            file_path,
            0,
            "the resource file should have hyphens rather than underscores",
            'resource-file-name'
        )

def check_resource_file_referenced(file, options=None):
    """Zkontrolujte, zda jsou zdrojové soubory odkazovány v alespoň jednom souboru RST."""
    resource_file = Path(file)
    resource_folder = resource_file.parent
    rst_file = resource_folder.with_suffix('.rst')
    if rst_file.exists():
        if resource_file.name not in rst_file.read_text():
            log_error(
                file,
                0,
                f"the resource file is not referenced in {rst_file}",
                "resource-file-referenced",
            )
    else:
        log_error(
            rst_file,
            0,
            f"resource folder name '{resource_folder.name}' does not match an rst file name.",
            'resource-folder-match',
        )

@sphinxlint.checker('')
def check_file_extensions(file, lines, options=None):
    """Zkontrolujte, zda neexistuje soubor bez přípony."""
    yield 0, "the file does not have an extension"
