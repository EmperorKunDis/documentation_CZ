import os
import re
import shutil
import sys
from pathlib import Path

import docutils
import sphinx
from pygments.lexers import JsonLexer, XmlLexer
from sphinx.ext import graphviz
from sphinx.util import logging

_logger = logging.getLogger(__name__)


#=== Obecné konfigurace ===

# Základní informace o projektu.
project = 'Odoo'
copyright = 'Odoo S.A.'

# „verze“ je informace o verzi projektu, který dokumentuje, nahrazuje znak „|verze|“.
# Používá se také v různých dalších místech dokumentace staveb.
# „release“ je plná verze včetně alfa/beta/rc tagů. Má nahradit „|release|“.
version = release = '18.0'

# Název „current_branch“ je technický název pro aktuální větev.
# Příklad: saas-15.4 -> saas-15.4; 12.0 -> 12.0, master -> master (*).
current_branch = version
# „current_version“ je verze Odoo spojená s aktuálním větvením.
# Příklad: saas-15.4 -> 15.4; 12.0 -> 12; master -> master (*).
current_version = current_branch.replace('saas-', '').replace('.0', '')
# Název „current_major_branch“ označuje větvení před aktuálním větvením.
# Příklad: saas-15.4 -> 15.0; 12.0 -> 12.0; master -> master (*).
current_major_branch = re.sub(r'\.\d', '.0', current_branch.replace('saas-', ''))
# „current_major_version“ je verze Odoa, která je spojena s aktuální hlavní větví.
# Příklad: saas-15.4 -> 15; 12.0 -> 12; master -> master (*).
current_major_version = current_major_branch.replace('.0', '')
# (*): Nezáleží nám na mistrovi.

# Minimální verze Sphinx, která je potřebná k vytvoření dokumentace.
needs_sphinx = '3.0.0'

# Výchozí jazyk, ve kterém je dokumentace napsaná. Je nastaven na hodnotu None, protože Sphinx
# považuje za jazyk, který neznamená „en“.
language = None

# Přípona zdrojových souborů.
source_suffix = '.rst'

# Hlavní dokument sestavy.
master_doc = 'index'

# Seznam vzorců, které se vztahují na zdrojový adresář, které odpovídají souborům a složkám, které je třeba ignorovat.
# hledání zdrojových souborů.
exclude_patterns = [
    'locale',
    'README.*',
    'bin', 'include', 'lib',
    'odoo',
]

# Textová role, která se používá, pokud není specifikována žádná role. Např.: „příklad“.
# Používáme „literální“ výchozí roli pro kompatibilitu s Markdownem: „foo“ chová jako „``foo``“.
# Podívejte se na https://docutils.sourceforge.io/docs/ref/rst/roles.html#standard-roles pro další role.
default_role = 'literal'


# Zda se měly zmenšené obrázky vkládat do značky odkazu nebo ne.
html_scaled_image_link = False

# Pokud je to pravda, bude k textu odkazu na funkci atd. připojen závoreček
add_function_parentheses = True

#=== Konfigurace rozšíření ===

source_read_replace_vals = {
    'BRANCH': current_branch,
    'CURRENT_BRANCH': current_branch,
    'CURRENT_VERSION': current_version,
    'CURRENT_MAJOR_BRANCH': current_major_branch,
    'CURRENT_MAJOR_VERSION': current_major_version,
    'GITHUB_PATH': f'https://github.com/odoo/odoo/blob/{version}',
    'GITHUB_ENT_PATH': f'https://github.com/odoo/enterprise/blob/{version}',
    'GITHUB_TUTO_PATH': f'https://github.com/odoo/tutorials/blob/{current_major_branch}',
    'OWL_PATH': f'https://github.com/odoo/owl/blob/master',
}

# Přidejte adresář s příponou do PYTHONPATH
extension_dir = Path('extensions')
sys.path.insert(0, str(extension_dir.absolute()))

# Vyhledejte adresář zdrojů Odoo, abyste zjistili, zda by měl být použit autodoc na dev doc.
odoo_sources_candidate_dirs = (Path('odoo'), Path('../odoo'))
odoo_sources_dirs = [
    d for d in odoo_sources_candidate_dirs if d.is_dir() and (d / 'odoo-bin').exists()
]
odoo_dir_in_path = False

if not odoo_sources_dirs:
    _logger.warning(
        "Could not find Odoo sources directory in neither of the following folders:\n"
        "%(dir_list)s\n"
        "The 'Developer' documentation will be built but autodoc directives will be skipped.\n"
        "In order to fully build the 'Developer' documentation, clone the repository with "
        "`git clone https://github.com/odoo/odoo` or create a symbolic link.",
        {'dir_list': '\n'.join([f'\t- {d.resolve()}' for d in odoo_sources_candidate_dirs])},
    )
else:
    if (3, 6) < sys.version_info < (3, 7):
        # Pro běh odoo je potřeba Python 3.7, ale verze s monkeypatchem je kompatibilní i se starší verzí 3.6.
        sys.version_info = (3, 7, 0)
    odoo_dir = odoo_sources_dirs[0].resolve()
    source_read_replace_vals['ODOO_RELPATH'] = '/../' + str(odoo_sources_dirs[0])
    sys.path.insert(0, str(odoo_dir))
    import odoo.addons
    odoo.addons.__path__.append(str(odoo_dir) + '/addons')
    from odoo import release as odoo_release  # Don't collide with Sphinx's 'release' config option
    odoo_version = '.'.join(str(s) for s in odoo_release.version_info[:2]).replace('~', '-')  # Change saas~XX.Y to saas-XX.Y
    odoo_version = 'master' if 'alpha' in odoo_release.version else odoo_version
    if release != odoo_version:
        _logger.warning(
            "Found Odoo sources in %(directory)s but with version '%(odoo_version)s' incompatible "
            "with documentation version '%(doc_version)s'.\n"
            "The 'Developer' documentation will be built but autodoc directives will be skipped.\n"
            "In order to fully build the 'Developer' documentation, checkout the matching branch"
            " with `cd odoo && git checkout %(doc_version)s`.",
            {'directory': odoo_dir, 'odoo_version': odoo_version, 'doc_version': version},
        )
    else:
        _logger.info(
            "Found Odoo sources in %(directory)s matching documentation version '%(version)s'.",
            {'directory': odoo_dir, 'version': release},
        )
        odoo_dir_in_path = True

if odoo_dir_in_path:
    upgrade_util_dir = next(filter(Path.exists, [Path('upgrade-util'), Path('../upgrade-util')]), None)
    if not upgrade_util_dir:
        _logger.warning(
            "Could not find Upgrade Utils sources directory in `upgrade_util`.\n"
            "The developer documentation will be built but autodoc directives will be skipped.\n"
            "In order to fully build the 'Developer' documentation, clone the repository with "
            "`git clone https://github.com/odoo/upgrade-util` or create a symbolic link."
        )
        odoo_dir_in_path = False
    else:
        _logger.info(
            "Found Upgrade Util sources in %(directory)s",
            {'directory': upgrade_util_dir.resolve()},
        )
        from odoo import upgrade
        upgrade.__path__.append(str((upgrade_util_dir / 'src').resolve()))

# Mapování mezi modely odoo, které se týkají hlavních dat a prohlášení
# dat, které se používají k odkazování uživatelů na dostupné xml_id při zadávání hodnot
# pole s příponou autodoc_field.
model_references = {
    'account.account.type': 'addons/account/data/data_account_type.xml',
    'res.country': 'odoo/addons/base/data/res_country_data.xml',
    'res.currency': 'odoo/addons/base/data/res_currency_data.xml',
}

# Sfinga jako rozšíření používat, jako názvy modulů.
# Mohou být rozšíření dodávaná s Sfingou (jmenovaná „sphinx.ext.*“) nebo vlastní.
extensions = [
    # Odkazy na zdroje v jiných projektech (použité při tvorbě odkazového dokumentu)
    'sphinx.ext.intersphinx',

    # Podpořte speciální příkazy pro seznam úkolů
    'sphinx.ext.todo',

    # Přizpůsobený motiv Odoo
    'odoo_theme',

    # Integrace videí z YouTube a Vimea (youtube, vimeo příkazy)
    'embedded_video',

    'custom_admonitions',

    # Generátor přesměrování
    'redirects',

    # Obsahové záložky
    'sphinx_tabs.tabs',

    # Karty
    'cards',

    # Spoilery
    'spoilers',

    # Podivná logika doménových jmen používaná v stránkách s archivem
    'html_domain',
]

if odoo_dir_in_path:
    # Vytváření odkazů na GitHub
    extensions += [
        'sphinx.ext.linkcode',
        'github_link',
        # Přeložit Pythonové dokumentace (directive autodoc, automodule, autoattribute)
        'sphinx.ext.autodoc',
        'autodoc_field',
    ]
else:
    extensions += [
        'autodoc_placeholder',
    ]
extensions.append('sphinx.ext.graphviz' if shutil.which('dot') else 'graphviz_placeholder')

todo_include_todos = False

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', '../invs/python.inv'),
    # Zdá se, že místní inventáře jsou vztahovány k zdrojové složce?
    'werkzeug': ('https://werkzeug.palletsprojects.com/', '../invs/werkzeug.inv'),
}

github_user = 'odoo'
github_project = 'documentation'

locale_dirs = ['../locale/']
templates_path = ['../extensions']

# vlastní funkci docname_to_domain, která rozděluje překlady aplikací do podadresářů
sphinx.transforms.i18n.docname_to_domain = (
    sphinx.util.i18n.docname_to_domain
) = lambda docname, compact: docname.split('/')[1 if docname.startswith('applications/') else 0]

# Štítky používané v přepínači verzí, které ukazují verze poskytované s konfigurací `versions`.
# volitelné. Pokud je poskytnutá verze neoznačená, použije se řetězec verze jako označení.
versions_names = {
    'master': "Master",
    'saas-18.4': "Odoo 18.4",
    'saas-18.3': "Odoo 18.3",
    'saas-18.2': "Odoo 18.2",
    'saas-18.1': "Odoo 18.1",
    '18.0': "Odoo 18",
    'saas-17.4': "Odoo 17.4",
    '17.0': "Odoo 17",
    '16.0': "Odoo 16",
}

# Jazyky, které jsou k dispozici v přepínači jazyků a které jsou uvedeny v souboru
# konfigurační možnost. Pokud kód jazyka neobsahuje žádný název, používá se jako název jeho velká písmena.
languages_names = {
    'de': 'DE',
    'en': 'EN',
    'es': 'ES',
    'es_419': 'ES (LATAM)',
    'fr': 'FR',
    'id': 'ID',
    'it': 'IT',
    'ja': 'JA',
    'ko': 'KR',
    'nl': 'NL',
    'pt_BR': 'PT',
    'ro': 'RO',
    'sv': 'SV',
    'th': 'TH',
    'uk': 'UA',
    'vi': 'VI',
    'zh_CN': 'ZH (CN)',
    'zh_TW': 'ZH (TW)'
}

# Adresář, ve kterém jsou uvedeny soubory s pravidly přesměrování používanými rozšířením „přesměrování“.
redirects_dir = 'redirects/'

sphinx_tabs_disable_tab_closing = True
sphinx_tabs_disable_css_loading = True

# Objednávka zboží na Autodoc
autodoc_member_order = 'bysource'

#===Možnosti výstupu v HTML===

html_theme = 'odoo_theme'

# Název stylu syntaxe zvýraznění, který se má použít.
# Podívejte se na soubor extensions/odoo_theme/pygments_override.py
pygments_style = 'odoo'

# Cesty s vlastními tématy, které se týkají této složky.
html_theme_path = ['extensions']

# Název obrázku (ve statické cestě), který se má použít jako ikona pro dokumentaci.
# Tento soubor by měl být ikonou systému Windows (.ico), která má velikost 16×16 nebo 32×32 pixelů.
html_favicon = os.path.join(html_theme_path[0], html_theme, 'static', 'img', 'favicon.ico')

# Cesty obsahující vlastní statické soubory vzhledem k této složce.
# Jsou kopií statických souborů vložených do kódu, takže soubor s názvem „default.css“ přepsává
# vložený „default.css“.
html_static_path = ['static']
html_permalinks = True

# Další soubory JavaScriptu a CSS, které lze importovat pomocí metadat „custom-js“ a „custom-css“.
# Seznamy jsou prázdné, protože soubory jsou specifikovány v rozšířeních/motivech.
html_js_files = []
html_css_files = []

# Možnost parseru PHP, aby nevyžadoval <?php
highlight_options = {
  'php': {'startinline': True},
}

#===Možnosti výstupu do formátu TeX===

latex_elements = {
    # Velikost papíru (papír formátu „dopis“ nebo „A4“).
    'papersize': 'a4paper',

    # Další věci do předmluvy LaTeXu.
    'preamble': r'\usepackage{odoo}',
    'tableofcontents': '',  # no TOC

    # Vygenerovat ručně v dokumentech LaTeX
    'releasename': release,
}

latex_additional_files = ['static/latex/odoo.sty']

# Seskupení dokumentového stromu do souborů TeX. Seznam dvojic:
# (zdrojový soubor, název cílového souboru, titulek, autor, třída dokumentu [jak udělat, návod nebo vlastní třída]).
latex_documents = [
    ('legal/terms/enterprise_tex', 'odoo_enterprise_agreement.tex',
     'Odoo Enterprise Subscription Agreement', '', 'howto'),
    ('legal/terms/partnership_tex',
     'odoo_partnership_agreement.tex', 'Odoo Partnership Agreement', '', 'howto'),
    ('legal/terms/terms_of_sale',
     'terms_of_sale.tex', 'Odoo Terms of Sale', '', 'howto'),

    ('legal/terms/i18n/enterprise_tex_fr', 'odoo_enterprise_agreement_fr.tex',
     "Contrat d'Abonnement Odoo Enterprise", '', 'howto'),
    ('legal/terms/i18n/partnership_tex_fr',
     'odoo_partnership_agreement_fr.tex', 'Contrat de Partenariat Odoo', '', 'howto'),
    ('legal/terms/i18n/terms_of_sale_fr', 'terms_of_sale_fr.tex',
     'Conditions Générales de Vente Odoo', '', 'howto'),

    ('legal/terms/i18n/enterprise_tex_nl', 'odoo_enterprise_agreement_nl.tex',
     'Odoo Enterprise Abonnementsovereenkomst', '', 'howto'),

    ('legal/terms/i18n/enterprise_tex_de', 'odoo_enterprise_agreement_de.tex',
     'Odoo Enterprise Abonnementsvertrag', '', 'howto'),
    ('legal/terms/i18n/terms_of_sale_de', 'terms_of_sale_de.tex',
     'Allgemeine Verkaufsbedingungen Odoo', '', 'howto'),

    ('legal/terms/i18n/enterprise_tex_es', 'odoo_enterprise_agreement_es.tex',
     'Acuerdo de suscripción de Odoo Enterprise', '', 'howto'),
    ('legal/terms/i18n/partnership_tex_es',
     'odoo_partnership_agreement_es.tex', 'Acuerdo de Colaboración de Odoo', '', 'howto'),
    ('legal/terms/i18n/terms_of_sale_es', 'terms_of_sale_es.tex',
     'Términos Generales de Venta Odoo', '', 'howto'),

    ('legal/terms/i18n/enterprise_tex_pt_BR', 'odoo_enterprise_agreement_pt_BR.tex',
     'Contrato de Assinatura do Odoo Enterprise', '', 'howto'),
    ('legal/terms/i18n/terms_of_sale_pt_BR', 'terms_of_sale_pt_BR.tex',
     'Termos Gerais de Venda Odoo', '', 'howto'),
]

# Seznam jazyků, které mají právní překlady (včetně angličtiny). Klíče musí být
# „jazyky_názvy“. Tyto překlady budou mít odkaz na jejich verze právních
# smlouvy namísto výchozího anglického. Hlavní právní dokumenty nejsou součástí
# překlady, které mají právní platnost.
legal_translations = ['de', 'es', 'fr', 'nl', 'pt_BR']

# Název obrázku (ve vztahu k této složce).
latex_logo = 'static/img/odoo_logo.png'

# Pokud je to pravda, zobrazte po kliknutí na externí odkaz adresu URL.
latex_show_urls = 'True'

# https://github.com/sphinx-doc/sphinx/issues/4054#issuecomment-329097229
def source_read_replace(app, docname, source):
    """Substitute parts of strings with computed values.

Protože náhrada RST není všude funkční, tj. v příkazech
musíme mít možnost zadat tyto hodnoty při čtení zdrojů.
Toto je použitím konfigurace source_read_replace_vals, která přiřazuje jméno jeho hodnotě
náhradní text. Tento bude hledat jméno obklopené závorkami v zdroji.

Jeho účelem je být spojen s událostí „source-read“.
    """
    result = source[0]
    for key in app.config.source_read_replace_vals:
        result = result.replace(f"{{{key}}}", app.config.source_read_replace_vals[key])
    source[0] = result

def upgrade_util_signature_rewrite(app, domain, objtype, contentnode):
    # Stejně jako u funkcí nebo tříd odoo.upgrade.util, ale pouze s nastavením add_module_names=False
    signature = contentnode.parent[0]
    if objtype == 'function' and signature.astext().startswith('odoo.upgrade.util.'):
        # <odoo.upgrade.util.modules>, <moduly nainstalované>, <(cr, *moduly)>
        signature.pop(0)
    if objtype == 'class' and signature.astext().startswith('class odoo.upgrade.util.'):
        # <třída>, <odoo.upgrade.util.pg.>, <PGRegexp>
        signature.pop(1)

def setup(app):
    # Vytvořte všechny alternativní URL pro každý dokument
    app.add_config_value('project_root', None, 'env')
    app.add_config_value('canonical_version', None, 'env')
    app.add_config_value('versions', None, 'env')
    app.add_config_value('languages', None, 'env')
    app.add_config_value('is_remote_build', None, 'env')  # Whether the build is remotely deployed
    app.add_config_value('source_read_replace_vals', {}, 'env')
    app.connect('source-read', source_read_replace)
    app.connect('object-description-transform', upgrade_util_signature_rewrite)
    # TODO po přesunu na verzi >= v7.2.5 nahradit místní proměnné i v souborech, které jsou zahrnuty.
    #  Podívejte se na https://github.com/sphinx-doc/sphinx/commit/ff1831
    #  app.connect('include-read', zdroj_čtení_nahradit)

    app.add_lexer('json', JsonLexer)
    app.add_lexer('xml', XmlLexer)

    app.connect('html-page-context', _generate_alternate_urls)

    # Přidejte možnost „podmínky“ do příkazů, aby je ignorovaly na základě hodnot konfigurace.
    app.add_config_value('odoo_dir_in_path', None, 'env')
    def context_eval(expr):
        return eval(expr, {confval.name: confval.value for confval in app.config})

    def patch(to_patch):
        to_patch.option_spec['condition'] = context_eval
        original_run = to_patch.run
        def new_run(self):
            if not self.options.get('condition', True):
                return []
            return original_run(self)
        to_patch.run = new_run

    for to_patch in (
        sphinx.directives.code.LiteralInclude,
        docutils.parsers.rst.directives.tables.CSVTable,
    ):
        patch(to_patch)


def _generate_alternate_urls(app, pagename, templatename, context, doctree):
    """ Add keys of required alternate URLs for the current document in the rendering context.

Alternativní URL je nutné pro:
- Kanonický odkazový tag
- přepínač verze
- Přepínač jazyka a související tagy odkazů
    """

    def canonicalize():
        """ Add the canonical URL for the current document in the rendering context.

Kanonická verze je poslední vydaná verze dokumentace.
Pro daný jazyk je pro stránku kanonické kořenové slovo v tomto jazyce, aby byla internetová
Pokud někdo hledá v daném jazyce, není přesměrován na anglickou verzi stránky.

Příklad:
- /dokumentace/prodej.html -> canonical = /dokumentace/14.0/prodej.html
- /dokumentace/11.0/cs/web.html -> canonical = /dokumentace/14.0/cs/web.html
        """
        # Pokud není nastavena kanonická verze, předpokládejte, že projekt má jedinou verzi.
        canonical_version_ = app.config.canonical_version or app.config.version
        canonical_lang_ = 'en'  # Always 'en'. Don't take the value of the config option.
        context['canonical'] = build_url(version_=canonical_version_, lang_=canonical_lang_)

    def versionize():
        """ Add the pairs of (version, url) for the current document in the rendering context.

Do kontextu renderování přidává Sphinx položku „verze“.
        """
        context['version_display_name'] = versions_names.get(version, version)

        # Pokud není nastaven seznam verzí, předpokládejte, že projekt nemá alternativní verzi.
        provided_versions_ = app.config.versions and app.config.versions.split(',') or []

        # Přeložte alternativní verze do jejich zobrazovaných názvů a URL adres.
        context['alternate_versions'] = []
        for alternate_version_ in reversed(provided_versions_):  # Reverse to show latest first.
            if alternate_version_ != version:
                display_name_ = versions_names.get(alternate_version_, alternate_version_)
                context['alternate_versions'].append((display_name_, build_url(alternate_version_)))

    def localize():
        """ Add the pairs of (lang, code, url) for the current document in the rendering context.

Příklad: ('Francouzština', 'fr', 'https://.../fr_BE/...')

Do kontextu renderování se vloží klíčové slovo language, které do textu přidává Sphinx.
        """
        current_lang_ = app.config.language or 'en'
        # Nahraďte hodnotu kontextu jejím velkým písmenem („FR“ místo „fr“).
        context['language'] = languages_names.get(current_lang_, current_lang_.upper())
        context['language_code'] = current_lang_

        # Pokud seznam jazyků není nastaven, předpokládejte, že projekt nemá alternativní jazyk.
        provided_languages_ = app.config.languages and app.config.languages.split(',') or []

        # Přeložte alternativní jazyky do jejich zobrazovacích názvů a URL.
        context['alternate_languages'] = []
        for alternate_lang_ in provided_languages_:
            if alternate_lang_ != current_lang_:
                display_name_ = languages_names.get(alternate_lang_, alternate_lang_.upper())
                context['alternate_languages'].append(
                    (
                        display_name_,
                        alternate_lang_.split('_')[0] if alternate_lang_ != 'en' else 'x-default',
                        build_url(lang_=alternate_lang_),
                    )
                )

        # Dynamické generování odkazů na místně platné právní dokumenty
        context['legal_translations'] = legal_translations

    def build_url(version_=None, lang_=None):
        if app.config.is_remote_build:
            # Projekt s kořenem jako https://www.odoo.com/documentation
            root_ = app.config.project_root
        else:
            # Projekt s kořenem .../documentation/_build/html/14.0/fr
            root_ = re.sub(rf'(/{app.config.version})?(/{app.config.language})?$', '', app.outdir)
        # Pokud není nastavena kanonická verze, předpokládejte, že projekt má jedinou verzi.
        canonical_version_ = app.config.canonical_version or app.config.version
        version_ = version_ or app.config.version
        lang_ = lang_ or app.config.language or 'en'
        canonical_page_ = f'{pagename}.html'

        # Překlady právních textů mají jiný URL schéma, protože nejsou spravovány na Transifexu.
        # např. překlad z FR /terms/enterprise => /fr/terms/enterprise_fr
        if pagename.startswith('legal/terms/'):
            if lang_ in legal_translations and not pagename.endswith(f"_{lang_}"):
                # odstranit kód jazyka pro aktuální překlad, nastavit cílový
                page_ = re.sub("_[a-z]{2}$", "", pagename)
                if 'terms/i18n' not in page_:
                    page_ = page_.replace("/terms/", "/terms/i18n/")
                canonical_page_ = f'{page_}_{lang_}.html'
            elif lang_ == 'en' and pagename.endswith(tuple(f"_{l}" for l in legal_translations)):
                # odstranit kód jazyka pro aktuální překlad, odkaz na původní anglický
                page_ = re.sub("_[a-z]{2}$", "", pagename)
                canonical_page_ = f'{page_.replace("/i18n/", "/")}.html'

        if app.config.is_remote_build:
            canonical_page_ = canonical_page_.replace('index.html', '')

        return f'{root_}' \
               f'{f"/{version_}" if app.config.versions else ""}' \
               f'{f"/{lang_}" if lang_ != "en" else ""}' \
               f'/{canonical_page_}'

    canonicalize()
    versionize()
    localize()
