
=======================
Lokální účetnictví
=======================

.. varování:

Tento návod předpokládá znalosti o tom, jak vytvořit modul v Odoo (viz
:doc:`../nauka/serverovy-framework-101`).


Postup instalace
======================

Při instalaci modulu „účet“ (příkazem „account <{GITHUB_PATH}/addons/account}>“) se automaticky nainstaluje lokalizační modul odpovídající kódu země společnosti.
V případě, že neexistuje žádný státní kódový soubor nebo není nalezen žádný modul pro lokalizaci, je nainstalován výchozí modul l10n_generic_coa (US) v adresáři {GITHUB_PATH}/addons/l10n_generic_coa.
Podrobnosti najdete v souboru „post init hook <{GITHUB_PATH}/addons/account/__init__.py>“.

Příkladem je instalace „l10n_ch <{GITHUB_PATH}/addons/l10n_ch>“ pokud má firma nastavené „Švýcarsko“.

Vytváření modulu pro lokalizaci
==============================

Struktura základního modulu „l10n_XX“ lze popsat následujícím souborem:

... kódový blok:: python

    {
„název“: „Země – Účetnictví“,
„verze“: „1.0.0“,
„kategorie“: „Účetnictví/Lokalizace/Účetní grafy“,
„licence“: „LGPL 3“,
„závisí“: [
„účet“.
        ],
„data“: [
„data/další_data.xml“,
„views/xxxmodel_views.xml“.
        ],
„demo“: [
„demo/demo_company.xml“.
        ]
    }

Váš pracovní strom by měl vypadat takto

... kódový blok:: bash

l10n_xx
└── data
│    └── šablona
│   │   ├── účet.účet-xx.csv
│     │   ├── účet.skupina-xx.csv
│     │     └── účet.daňová skupina xx.csv
│   └── další_data.xml
└── views
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
└── demo
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
└── models
│   ├── šablona_xx.py
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
└──__init__.py
└── __manifest__.py


V prvním souboru `models/template_xx.py` nastavíme název účetní osnovy spolu s několika základními poli.

.. viz též:
:ref:`Šablony grafů </developer/reference/standard_modules/account>`

Příklad:
„addons/l10n_be/models/template_be.py“ <{GITHUB_PATH}/addons/l10n_be/models/template_be.py>

...literalinclude:: {ODOO_RELPATH}/addons/l10n_be/models/template_be.py
:podmínka: odoo_dir_in_path
:jazyk:python
:začíná_na: _get_be_template_data
:konec-před: _get_be_reconcile_model


Kniha účetních záznamů
=================

Štítky účtu
------------

.. viz též:
:ref:`Odkazy na účty s tagy <reference/account_account_tag>`

Štítky jsou způsob, jakým účty třídit.
Představte si například, že chcete vytvořit finanční výkaz s více řádky, ale nemáte žádný způsob, jak najít pravidlo pro rozeslání účtů podle jejich „kódu“.
Řešením je použití štítků, jeden pro každou řádek zprávy, abyste filtrovali účty tak, jak chcete.

Zaškrtněte políčka v souboru „data/account_account_tag_data.xml“.

Příklad:
„addons/l10n_lt/data/template/account.account-lt.csv“

...literalinclude:: {ODOO_RELPATH}/addons/l10n_lt/data/template/account.account-lt.csv
:podmínka: odoo_dir_in_path
:jazyk: csv
:konec:účet_šablona_1201

Účty
--------

.. viz též:
   - :ref:`Reference na účty <reference/account_account>`
   - :doc:`/aplikace/finance/účetnictví/začínáme/rozvaha“

Zřejmě nemůže existovat ani :guilabel:`Skladová kniha`, takže je potřeba ji v :file:`data/account.account.template.csv` specifikovat.

Příklad:
„addons/l10n_ch/data/template/account.account-ch.csv“

..literalinclude:: {ODOO_RELPATH}/addons/l10n_ch/data/template/account.account-ch.csv
:podmínka: odoo_dir_in_path
:jazyk: csv
:konec-na: ch_coa_1171

.. varování:

    - Vyhněte se používání „asset_cash“ „account_type“!
Ve skutečnosti jsou účty a hotovostní účty vytvořeny přímo při instalaci modulu lokalizace a poté jsou propojeny s „účetním deníkem“.
    - Pro obecný případ stačí jeden účet typu platba/příjem. Musíme však definovat i účet PoS pro příjem.
    - Nezaložte příliš mnoho účtů: stačí jich 200 až 300. Ale hlavně se snažíme najít dobrou rovnováhu, kde CoA potřebuje minimální adaptaci pro většinu společností později.


Skupiny účtů
--------------

.. viz též:
:ref:`Referenční údaje o skupině účtů <reference/account_group>`

Skupiny účtů umožňují popsat hierarchickou strukturu rozvahy. Filtr je zapotřebí aktivovat v hlášení a poté, co se rozbalí do položek na výpisu, zobrazí rodiče účtu.

Práce probíhá s prefixem *start*/*end*, takže každý účet, kde se kód začíná něčím mezi *start* a *end* bude mít tento „account.group“ jako rodičovskou skupinu. Dále lze vytvářet hierarchii i pomocí nadřazených skupin účtů.


Příklad:
`addons/l10n_il/data/template/account.group-il.csv <{GITHUB_PATH}/addons/l10n_il/data/template/account.group-il.csv>`

.. csv-tabulka::
:podmínka: odoo_dir_in_path
:soubor: {ODOO_RELPATH}/addons/l10n_il/data/template/account.group-il.csv
:šířky: 20,20,20,20,20
:hlavičkové řádky: 1

Daně
-----

.. viz též:
   - :ref:`Daňové odkazy <reference/account_tax>`
   - :doc:`/aplikace/finance/účetnictví/daně/`

Přidat daně je nutné nejprve specifikovat daňové skupiny. Obvykle potřebujete jen jednu daňovou skupinu na každý daňový tarif, s výjimkou 0 %, protože často musíte odlišit osvobozené, 0 % a nepodléhající daně.
Tento model má pouze dvě povinná pole: „jméno“ a „země“. Vytvořte soubor :file:`data/template/account.tax.group-xx.csv` a zobrazte skupiny.

Příklad:
„addons/l10n_uk/data/template/account.tax.group-uk.csv“ (<{GITHUB_PATH}/addons/l10n_uk/data/template/account.tax.group-uk.csv>).


:podmínka: odoo_dir_in_path
:jazyk: csv


Nyní můžete přidat daně prostřednictvím souboru :file:`data/template/account.tax-xx.csv`. První daň, kterou definujete (kupní/prodejní) se také stane výchozí kupní/prodejní daní pro vaše produkty.


Příklad:
„addons/l10n_ae/data/template/account.tax-ae.csv“

..literalinclude::{ODÓO_RELPATH}/addons/l10n_ae/data/template/account.tax-ae.csv
:podmínka: odoo_dir_in_path
:jazyk:xml
:end-at: daň z přidané hodnoty v Ras Al Khaimě


Daňový report
----------

.. neupravený::html



Daňový přiznání se vyplňuje v aplikaci „Fakturace“ („účet“), ale je možné jej zobrazit pouze tehdy, když je nainstalována aplikace „Účetnictví“ („účet_účetní“).

.. viz též:
   - :doc:`/rozvoj/odkaz/standardní moduly/účet/účetní výkazová řádka“
   - :doc:`/aplikace/finance/účetnictví/reporting/daňové přiznání`

V předchozím odstavci jste si všimli políčka „invoice_repartition_line_ids“ nebo „refund_repartition_line_ids“ a pravděpodobně vám nic neřekly. Dobrá zpráva: nejste sami, kdo tomu nerozumí. Špatná zpráva: musíte se trochu zamyslet. Téma je komplikované. Ano:

... grafviz::účetnictví/daňový přehled.dot
:class: auto

Zjednodušeně řečeno v daňovém šablonu uvádíte ve fakturační/vratkové položce, zda se má do kterého řádku (přes pole *minus/plus_report_line_ids*) hlásit základ nebo procenta daně.
Stává se to jasné také při kontrole daňového nastavení v rozhraní Odoo (nebo při prohlížení dokumentace: „odkaz“:ref:`Tax References <reference/account_tax>`, :ref:`Tax Repartition References <reference/account_tax_repartition>`).

Takže jakmile máte správně nakonfigurované daně, už jen stačí přidat soubor :file:`data/account_tax_report_data.xml` s záznamem pro váš účet. Pro jeho považování za daňový report je nutné mu přiřadit správný identifikátor `root_report_id`.

... blok kódu::xml

<odoo>

<pole název="název">Daňový přehled</pole>
<pole název="kořenový identifikátor zprávy" odkaz="účet.generický daňový report"/>
<položka jméno="země_id" odkaz="základní.XX"/>


        ...


... následované prohlášením svých linií, jak je uvedeno v záznamu „účetní zprávy – řádek“.

Příklad:
„addons/l10n_au/data/account_tax_report_data.xml“ (cesta na Githubu: „addons/l10n_au/data/account_tax_report_data.xml“)

...literalinclude::{ODOO_RELPATH}/addons/l10n_au/data/account_tax_report_data.xml
:podmínka: odoo_dir_in_path
:jazyk:xml
:začíná: daňový výkaz
:konec-před: daňový-report-gstrpt-g3



Fiskální pozice
----------------

.. viz též:
   - :ref:`Daňová pozice <reference/account_fiscal_position>`
   - :doc:`/aplikace/finance/účetnictví/daně/daňové pozice`

Uveďte daňové pozice v souboru: `data/template/account.fiscal.position-xx.csv`.

Příklad:
`addons/l10n_es/data/template/account.fiscal.position-es_common_mainland.csv <{GITHUB_PATH}/addons/l10n_es/data/template/account.fiscal.position-es_common_mainland.csv>`

...literalinclude:: {ODOO_RELPATH}/addons/l10n_es/data/template/account.fiscal.position-es_common_mainland.csv
:podmínka: odoo_dir_in_path
:jazyk: csv
:konec-na: daňový vzor účetní záznamu PIVA 10% sp. ex

Konečné kroky
===========

Nakonec můžete přidat ukázkovou společnost, abyste snadno otestovali lokalizaci v režimu demo.

Příklad:
„addons/l10n_ch/demo/demo_company.xml“

...literalinclude::{ODoo_RELPATH}/addons/l10n_ch/demo/demo_company.xml
:podmínka: odoo_dir_in_path
:jazyk:xml
:začíná po: <odoo>
:end-before: </odoo>

Účetní výkazy
==================

.. neupravený::html



.. viz též:
:doc:`/aplikace/finance/účetnictví/reporting`

Účetní výkazy by měly být přidány pomocí samostatného modulu l10n_XX_reports, který by měl být uložen do úložiště pro firmy <{GITHUB_ENT_PATH}>_.

Základní soubor __manifest__.py pro takový modul vypadá následovně:


... kódový blok:: python

    {
„název“: „Země – Účetní zprávy“,
„kategorie“: „Účetnictví/Lokality/Zprávy“,
„verze“: „1.0.0“,
„licence“: „OEEL-1“,
„závisí“: [
"l10n_XX", "účetní zprávy"
        ],
„data“: [
„data/rozvaha.xml“.
„data/zisk_a_ztráta.xml“.
        ],
„auto_install“: True
    }


Funkční přehled finančních výkazů je zde: :doc:`/aplikace/finance/účetnictví/reporting`.

Příkladů je mnoho, např.:

* „<{GITHUB_ENT_PATH}/l10n_ch_reports/data/account_financial_html_report_data.xml>“
* `<{GITHUB_ENT_PATH}/l10n_be_reports/data/account_financial_html_report_data.xml>`

Můžete si zkontrolovat význam polí zde:

* :doc:`/rozvoj/odkaz/standardní moduly/účet/účetní výkaz
* :doc:`/rozvoj/odkaz/standardní moduly/účet/účetní výkazová řádka“

Pokud jste svému hlášení přiřadili ID „root_report_id“, je nyní k dispozici v jeho výběru varianty. Pokud ne
Stále je třeba přidat položku do nabídky. Z výhledu formuláře lze vytvořit výchozí položku
Vyberte si zprávu kliknutím na: „Akce“ → „Vytvořit položku v menu“. Poté budete potřebovat
Obnovte stránku pro její zobrazení nebo vytvořte novou sekci pro úplně nový report
v menu „Hlášení“, musíte vytvořit nový záznam typu ir.ui.menu (obvykle ve hlavním
Modul l10n_XX) a nový ir.actions.client (obvykle v novém souboru s reportovou XML).
„účet.report“ s novým „ID reportu“. Pak nastavte nové menu jako pole „parent_id“ v
akční model.

Příklad:
   * `ir.ui.menu creation <{GITHUB_PATH}/addons/l10n_be/data/menuitem_data.xml>`
   * `ir.actions.client a vytváření položek nabídky <{GITHUB_ENT_PATH}/l10n_be_reports/data/partner_vat_listing.xml>`_.
