import argparse
import os
import re
import sys
from itertools import chain
from unittest.mock import patch

import sphinxlint

import checkers


CUSTOM_RST_DIRECTIVES = [
    'card', 'cards',  # cards
    'example', 'exercise',  # custom_admonitions
    'spoiler',  # spoilers
    'tab', 'tabs', 'group-tab', 'code-tab',  # sphinx_tabs
]

ADDITIONAL_CHECKERS = [
    checkers.resource_files.check_resource_file_referenced
]


def run_additional_checks(argv=None):
    _enabled_checkers, args = sphinxlint.parse_args(argv)
    for path in chain.from_iterable(sphinxlint.walk(path, args.ignore) for path in args.paths):
        if path.startswith('content') and not path.endswith('.rst'):
            for checker in ADDITIONAL_CHECKERS:
                checker(path)


"""
Následující kontrolní programy jsou vybrány pro příkaz make test.
– před rolem závorka: Hledání rolí, které jsou před nimi uvedeny v závorce.
– bad-indent: Zkontrolujte, zda je v bloku kódu překročena mezera.
– ukončení řádku: Zkontrolovat ukončení řádku (\r).
– chybějící-dolary: Hledání příkazu, který je špatně napsaný jako komentář.
--dotdirective: Hledat příkazy s třemi tečkami místo dvou.
– horizontální tabulátor: Zkontrolujte, zda jsou v řádcích horizontální tabulátory (\t).
– hyperlink-reference-missing-backtick: Hledání chybějících závorek uvnitř hypertextového odkazu
reference.
– chybějící závorka za rolí: Hledání rolí, které nemají uzavírací závorku.
-chybějící-čárka-v-roli: Hledání chybějících čárek v rolích.
- chybějící nová řádka na konci souboru: Zkontrolujte, zda poslední řádek souboru končí novou řádkou.
-chybějící mezera po literálu: Hledání vložených literálů, které jsou následovány znakem.
-chybějící mezera po roli: Hledání rolí, které následují hned za znakem.
– chybějící-mezera-před-výchozím-rolí: Hledání chybějících mezer před výchozím rolí.
– chybějící mezera před rolí: Hledání chybějících mezer před rolí.
-chybějící mezera v odkazu: Hledání odkazů, které chybí mezeru.
-chybějící_podtržítko_po_odkazu: Hledání odkazů bez podtržítka po uzavření
zpětného uvozovky.
– python-syntax: Hledání neplatného syntaxu v příkladech Pythonu.
--role-s-dvojitými-zvratky: Hledání rolí s dvojitými závorkami.
--role-bez-závorek: Hledat role bez závorek.
– kontrola mezer na konci řádku: Zkontrolujte, zda nejsou na konci řádku mezery.
– nevyvážené inline literály oddělovače: vyhledávat nevyvážené inline literály oddělovače.
---
– všechny šachovnice definované v souborech checkers/*.

Následující kontrolní mechanismy jsou vybírány pouze pro „make review“.
– příliš dlouhá linka: Zkontrolujte délku řádku.
– brzký přerušení řádku: Zkontrolujte, zda je v textu brzy přerušení řádku.

"""
if __name__ == '__main__':
    # Upravte globální konstanty sphinxlintu, aby zahrnovaly naše vlastní direktivy a analyzovali jejich obsah.
    with patch(
        'sphinxlint.DIRECTIVES_CONTAINING_RST',
        sphinxlint.DIRECTIVES_CONTAINING_RST + CUSTOM_RST_DIRECTIVES,
    ), patch(
        'sphinxlint.DIRECTIVES_CONTAINING_RST_RE',
        '(' + '|'.join(sphinxlint.DIRECTIVES_CONTAINING_RST) + ')',
    ), patch(
        'sphinxlint.ALL_DIRECTIVES',
        '(' + '|'.join(sphinxlint.DIRECTIVES_CONTAINING_RST
            + sphinxlint.DIRECTIVES_CONTAINING_ARBITRARY_CONTENT)
            + ')',
    ), patch(
        'sphinxlint.seems_directive_re',
        re.compile(rf"^\s*(?<!\.)\.\. {sphinxlint.ALL_DIRECTIVES}([^a-z:]|:(?!:))"),
    ), patch(
        'sphinxlint.three_dot_directive_re',
        re.compile(rf'\.\.\. {sphinxlint.ALL_DIRECTIVES}::'),
    ):
        parser = argparse.ArgumentParser()
        if os.getenv('REVIEW') == '1':  # Enable checkers for `make review`.
            setattr(sphinxlint.check_line_too_long, 'enabled', True)
            setattr(checkers.rst_style.check_early_line_breaks, 'enabled', True)
            ADDITIONAL_CHECKERS.extend([
                checkers.resource_files.check_image_size,
                checkers.resource_files.check_image_color_depth,
                checkers.resource_files.check_resource_file_name,
            ])
        run_additional_checks()
        sys.exit(sphinxlint.main())
