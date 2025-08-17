=================
Klasifikační schéma
=================

Kniha jízd (COA) je seznam všech účtů, které slouží k evidenci finančních
transakce v účetnictví organizace. Schéma účtování najdete pod
:menu:"Účetnictví" --> "Konfigurace" --> "Vedlejší účty".

Při procházení vašeho rozvahového účtu můžete třídit účty podle:guilabel:„Kódu“.
:guilabel:`Název účtu“ nebo „Typ“, ale další možnosti jsou k dispozici v rozevíracím seznamu.

.. obrázek: účetní_položky/vybrané.png
:alt: Tlačítko s rozbalovacím menu

.. obrázek: účetní_kniha/účetní_kniha_seřazená.png
:alt:Seskupte účty podle typu v Odoo Accounting

.._souboru účetních knih/vytvořit:

Konfigurace účtu
===========================

Země, kterou zvolíte při vytváření databáze (nebo další společnosti ve vaší databázi).
určuje, která z instalačních balíčků pro daňové lokalizace („<../../fiscal_localizations>“) je nainstalována.
výchozí nastavení. Tento balíček obsahuje standardní účetní knihu již přednastavenou podle
zákony dané země. Můžete ho používat přímo nebo podle potřeb vaší společnosti.

Pro vytvoření nového účtu přejděte na: „Účetnictví --> Konfigurace --> Skladová kniha“.
Klikněte na tlačítko „Vytvořit“ a vyplňte alespoň požadované pole.
(:guilabel:'Kód, Jméno účtu, Typ').

.. varování:
Jednou zadaná faktura nelze změnit.
Byl zveřejněn.

Kód a název
-------------

Každý účet je identifikován svým kódem a názvem, které také ukazují na
účel účtu.

.._výkaznictví/typ:

Typ
----

Přesné nastavení typu účtu je kritické, protože slouží k mnoha účelům:

- Informace o účelu a chování účtu
- Vytvářet zemi specifické právní a finanční zprávy
- Určete pravidla pro ukončení fiskálního roku
- Vytvořte úvodní záznamy

Pro konfiguraci typu účtu otevřete pole „Typ“ a vyberte
odpovídající typ z následujícího seznamu:

+---------------+--------------+-------------------------+
|Hlášení       |Kategorie      |Typy účtů            |
+===============+==============+=========================+
|Výkaz zisku a ztráty |Vlastní zdroje      |Příjmy                 |
|               |              +-------------------------+
|                  |                |Banka a hotovost      |
|               |              +-------------------------+
|                  |                |Aktiva v oběhu         |
|               |              +-------------------------+
|                  |                |Nepohyblé aktiva       |
|               |              +-------------------------+
|Předplacené služby|Časová období|Přípravné platby
|               |              +-------------------------+
|               |              | Pohyblivé věci          |
|               +--------------+-------------------------+
|------------------|Závazky       |Vyplatitelné          |
|               |              +-------------------------+
|                  |                |Kreditní karta          |
|               |              +-------------------------+
|                  |                |Aktuální závazky       |
|               |              +-------------------------+
|Nepovinné položky|Povinné položky|Ostatní závazky
|               +--------------+-------------------------+
|------------------|-Equity-----------|-Equity---------------|
|               |              +-------------------------+
|                  |                | Hodnota aktuálního zisku  |
+---------------+--------------+-------------------------+
|Zisk a ztráta|Příjem         |Příjem                   |
|               |              +-------------------------+
|Jiné příjmy|Další příjmy|
|               +--------------+-------------------------+
|---------------------------|Náklady na provoz|Náklady na provoz|
|               |              +-------------------------+
|              |              |  Amortizace             |
|               |              +-------------------------+
|                  |                | Náklady na prodej       |
+---------------+--------------+-------------------------+
|Jiné            | Jiné         | Mimo bilanci           |
+---------------+--------------+-------------------------+

Vlastní kapitál
~~~~~~

Některé typy účtů mohou automaticky vytvářet záznamy :ref:`aktiva <aktivní-automatizace>`.
Pro automatické vkládání účtů klikněte na položku „Zobrazit“ a přejděte do
:guilabel:„Automatizace“ záložka.

Máte tři možnosti pro záložku Automatizace:

#:guilabel:`Ne“: tento výchozí stav nevyvolá žádnou akci.
#:guilabel:`Vytvořit v návrhu“: pokaždé, když je transakce zaznamenána na účtu, je vytvořen záznam
Vytvořeno, ale neověřeno. Nejprve musíte vyplnit příslušný formulář.
#Vytvořit a ověřit: musíte také vybrat model „Odložené náklady“.
Při každém zadání transakce na účet vzniká záznam a je okamžitě ověřen.

Daň z přidané hodnoty
-------------

V nabídce „Zobrazení“ účtu vyberte výchozí daň.
je zvolen pro prodej nebo nákup produktu.

Štítky
----

Některé účetní zprávy vyžadují nastavení štítků na příslušných účtech. Chcete-li přidat štítek,
Klikněte na pole „Štítky“ a vyberte existující štítek nebo klikněte na tlačítko „Vytvořit“.
nový.

Skupiny účtů
--------------

Skupiny účtů jsou užitečné pro seznam více účtů jako podúčty většího účtu.
takto konzolidaci zpráv jako je **Trial Balance**. Ve výchozím nastavení se skupiny zpracovávají automaticky
na základě kódu skupiny. Například nový účet „131200“ bude součástí skupiny
„131000“. Můžete přiřadit konkrétní skupinu k účtu v poli „Skupina“ pod
:guilabel:`Zobrazit“.

Vytvořte skupiny účtů ručně
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. poznámka::
Pravidelní uživatelé by neměli potřebovat vytvářet skupiny účtů ručně. Následující část je určená pouze
určené pro vzácné a pokročilé použití.

Vytvořit novou skupinu účtů aktivujte režim vývojáře (viz developer-mode) a přejděte na
V menu „Účetnictví“ -> „Nastavení“ -> „Skupiny účtů“ vytvořte novou skupinu a zadejte
Jméno, kódové označení a název společnosti, ke kterým by měl být účet skupiny dostupný. Poznámka
musíte zadat stejný kód předčíslí v obou polích „Od“ a „Do“.

.. obrázek: účetní_účty/skupiny_účtů.png
:alt:Vytváření účetních skupin.

Pro zobrazení svého výkazu zúčtování s vašimi účetními skupinami přejděte na
:menuaccounting-->reporting-->trial balance“, pak otevřete nabídku „Možnosti“
a vyberte: guilabel:„Hierarchie a součty“.

.. obrázek: účetní_závazky/účetní_závazky_skupiny.png
:alt:Skupiny účtů v rozvaze v Odoo účetnictví

Dovolte smíření
--------------------

Některé účty, například účet vedený pro zaznamenání transakcí platebního systému, lze použít k
Soulad účetních záznamů.

Příkladem může být faktura zaplacená kreditní kartou, která se označí jako „zaplacená“ po kontrole
Je třeba ji proto nastavit tak, aby byla používána pro
s možností vyrovnání se s minulostí“.

Pro toto nastavení zkontrolujte políčko „Povolit srovnání“ v nastavení účtu.
:guilabel:`Uložit“; nebo zapněte tlačítko z pohledu účetnictví.

.. obrázek: účetní_kniha/účetní_kniha_srovnání.png
:alt:Povolit srovnání pro účty v účetním systému Odoo

... coa_shared_accounts:

Společné účty
---------------

Funkce „Sdílené účty“ umožňuje vytvoření jednoho účtu pro určitý účel.
Je zvláště užitečné pro prostředí více společností, kde
Taková účetní kniha může být použita pro různé společnosti.

Zastaralé
----------

Není možné smazat účet, pokud na něm byla zaznamenána transakce.
jejich nepoužitelností pomocí funkce **Deprecated**: zaškrtněte pole „Deprecated“ v
Nastavení účtu a stiskněte tlačítko „Uložit“.

.. viz též:
   * :doc:`cheat_sheet“
   * :doc:`../faktury/majetek`
   * :doc:`../faktury/odložené výdaje
   * :doc:`../faktury-zakaznikum/odlozeny-prijmy`
   * :doc:`/fiscal_localizations`
   * „Návody k Odoo: Účetní kniha <https://www.odoo.com/slides/slide/chart-of-accounts-6834>“
   * „Tutoriály Odoo: Aktualizujte svůj účetní deník
<https://www.odoo.com/slides/slide/aktualizujte svůj účetní rozvrh 6391>
