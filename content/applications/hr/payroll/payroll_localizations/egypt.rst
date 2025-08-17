=====
Egypt
=====

Egyptská verze balíčku pro zpracování mezd **Payroll** umožňuje zpracovávat mzdy v souladu s
Egyptské pracovní zákony. Vypočítává progresivní daň z příjmu, platbu sociálního pojištění zaměstnance a zaměstnavatele.
bezpečnost a základní složky platu včetně nájemného a dopravních výdajů.

Konfigurace
=============

:ref:`Instalujte následující moduly, abyste získali všechny funkce egyptského
Lokalizace systému pro mzdy a personalistiku:

.. seznam tabulkový::
:hlavičkové řádky: 1

   * Jméno
     - Technické označení
     - Popis
   * --:guilabel:Egypt - Mzdy
     - „l10n_eg_hr_mzdy“
     - Modul mzdy obsahuje všechny platové pravidla, logiku dovolené a kompenzační pravidla v souladu s
Egyptský zákon o práci.
   * --:guilabel:Egypt - Mzdy a účetnictví
     - „l10n_eg_hr_mzdy“
     - Přidává se mapování účtů související s výpočtem mzdy.

.. viz též:
:doc:`Dokumentace k egyptské daňové lokalizaci <../../../finance/fiscal_localizations/egypt>`

Egyptské pracovní smlouvy
===========================

Jakmile je zaměstnanec vytvořen v databázi (viz /employees/new_employee),
:ref:`musí být vytvořen nový kontrakt <plat/novy-kontrakt>“.

Zkontrolovat, zda uživatel má smlouvu, přejděte do aplikace **Zaměstnanci**, pak klikněte na
kartu zaměstnance. Tlačítko s ikonou „fa-book“ a štítkem „Smlouvy“ zobrazuje červený nulu
Pokud žádný kontrakt neexistuje, zobrazí se:guilabel:`Ve smlouvě od (datum začátku smlouvy)`
v zeleném.

.. poznámka::
Smlouvy lze najít také po kliknutí na :menuselection:`Zaměstnanci aplikace --> Zaměstnanci -->
Smlouvy“. Všechny smlouvy se zobrazují v přehledu, uspořádané podle stavu.

Vyplňte následující smluvní informace v záložce „Informace o mzdě“
smlouva:

- :guilabel:„Referenční částka sociálního pojištění“: Slouží jako základ pro výpočet
Sociální pojištění zaměstnance a zaměstnavatele
<platove/platove_lokalizace/socialni-pojisteni>.
- :guilabel:`Počet dní dovolené“: používá se k výpočtu :ref:`sazby pro příspěvek na
zaměstnanci <plat/mzdy_lokalizace/příplatek>.
- :guilabel:`Počet dnů“: Odpovídá počtu dnů použitých při výpočtu
zajištění výše odstupného v případě ukončení pracovního poměru zaměstnance

- :guilabel:`Počet dní celkem“: Odkazuje na počet dnů použitých k výpočtu
:ref>: „příspěvek na odchod do penze, který zaměstnanci vyplácí společnost při ukončení pracovního poměru.
<mzdy/mzdy_lokalizace/ukončení služby>.

... payroll/payroll_localizations/socialni-pojisteni:

Sociální zabezpečení
================

Pravidla sociálního pojištění spočítají výši příspěvku, který má být odveden zaměstnavatelem.
zaměstnanci do Národní organizace pro sociální zabezpečení (NOSI).
pro egyptské zaměstnance.

Zaměstnavatel přispívá na sociální pojištění zaměstnance ve výši 18,75 % z částky odpovídající referenční hodnotě pro pojistné na sociální zabezpečení.
Zaměstnanec přispívá 11 % z částky odpovídající pojistnému limitu a tato částka se
Odečtena z výplatní pásky.

.. důležité::
Základní sazba pojistného je pro každého zaměstnance stanovena ve smlouvě.

Listy
======

Pro zaměstnance pracující v Egyptě jsou k dispozici následující typy dovolené:
<plat/lokalizace/roční>, :ref:`Nemocenská <plat/lokalizace/nemoc>
„Neplacená dovolená“ (viz payroll/payroll_localizations/unpaid) a „Jiné typy dovolené“
<platová/platová_lokalizace/jiné>.

.. payroll/payroll_localizations/annual:

Pracovní volno
------------

Zaměstnanci mají nárok na 21 dní dovolené a pokud zaměstnanec potřebuje více dní,
musí být požadovány u odpovědných pracovníků v oblasti lidských zdrojů podle „Čas na dovolenou/Žádost o přidělení času“

.. důležité::
Vzhledem k tomu, že je dovolená placená, není spojena s platovým předpisem, ale objeví se v
dny odpracované na výplatním listu a v tiskopisu PDF.

.. _mzdové účetnictví/mzdy/nemocenská:

Nemocenská
----------

Existují tři případy v oblasti nemocenských dávek, kdy se zaměstnanci odečítá částka:

- „Platba v plné výši“: první třicet kalendářních dnů každého roku (platí pouze pro pracovní záznamy, ne pro mzdy
(odpočet).

**Výpočet mzdy** = (denní plat)

- :guilabel:`75 % placeno“: dalších 60 dní; pravidlo pro výplatu mezd odečítá z platu zaměstnance 25 %.

**Výpočet mzdy** = (denní plat * 0,25)

- „0 % placené“: po 90 dnech; pravidlo pro výplatu mezd odečítá 100 % mzdy zaměstnance.

**Výpočet mzdy** = (denní plat * 0,00)

... _mzdy/mzdy_lokalizace/neplacené:

Nedostatek peněz
------------

Srážky se provádějí z platu zaměstnance v závislosti na počtu nevyčerpaných dní dovolené.
Je počítáno tak, že se měsíční plat zaměstnance dělí třiceti a získá se denní plat.
Pak ještě násobit počtem dní neplaceného volna, které zaměstnanec využil.

.. _mzdy/mzdové lokalizace/jiná:

Jiné druhy dovolené
-----------------

Tyto typy volna jsou považovány za plně placené a neovlivňují výplatní pásku, ale jsou sledovány
pracovní záznamy:

- Příspěvek na mateřskou
- Pouť
- Služební volno k úmrtí

Daň z příjmu
==========

V Egyptě je zaveden progresivní systém zdanění příjmů, kdy se daňová sazba zvyšuje v závislosti na
vyšších ročních příjmových pásmech.

Daňové pásmo
------------

Podle výše ročního příjmu zaměstnance se uplatňují následující sazby:

.. seznam tabulkový::
:hlavičkové řádky: 1
:prázdné sloupky: 1

   * - Daňový základ
     - <600 tisíc
     - 600 až 699
     - 700Kč - 799Kč
     - 800Kč - 899Kč
     - 900 tisíc až 1,2 milionu
     - >1,2 M
   * - 0%
     - 1-40k
     - -
     - -
     - -
     - -
     - -
   * - 10%
     - Více než 40 až 55 tisíc
     - 1 - 55 tisíc
     - -
     - -
     - -
     - -
   * - 15%
     - Více než 55 až 70 tisíc
     - Více než 55 až 70 tisíc
     - 1 - 70 tisíc
     - -
     - -
     - -
   * - 20%
     - Více než 70 tisíc do 200 tisíc
     - Více než 70 tisíc do 200 tisíc
     - Více než 70 tisíc do 200 tisíc
     - 1 – 200 tisíc
     - -
     - -
   * - 22.5%
     - Více než 200 tisíc do 400 tisíc
     - Více než 200 tisíc do 400 tisíc
     - Více než 200 tisíc do 400 tisíc
     - Více než 200 tisíc do 400 tisíc
     - 1 - 400 tisíc
     - -
   * - 25%
     - Více než 400 tisíc
     - Více než 400 tisíc
     - Více než 400 tisíc
     - Více než 400 tisíc
     - Více než 400 tisíc
     - 1-1,2 M
   * - 27.5%
     - -
     - -
     - -
     - -
     - -
     - Více než 1,2 milionu

Výjimky
----------

Zaměstnanci jsou oprávněni k osobní výjimce ve výši 20 000 egyptských liber z hrubé mzdy.

Prodloužení
========

Podle doby dne a času, kdy je přesčas zaznamenán, se může přidat
Výše odměny zaměstnanci může být následující:

- Během pracovních dnů v době od 6 do 20 hodin je to částka 1,35 násobek hodinové mzdy zaměstnance.
- V nočních hodinách pracovního dne je částka 1,70násobek mzdy za hodinu zaměstnance.
- Ve dnech volna a o svátcích: Částka je 2,0 násobek hodinové mzdy zaměstnance.

.. poznámka::
Pracovní doba přesčas se zaznamenává přímo na výplatních páskách jako jiný vstup.

.. _mzdy/mzdové lokality/příplatky:

Provize
==========

Provize jsou částky, které zaměstnavatel vypočítává za účelem zaplacení mzdy zaměstnanci.
Pro výpočet nároku na odstupné nebo dovolenou se vychází z měsíční mzdy.

Poskytování výhod při ukončení služby
--------------------------------

Je počítáno tak, že se vydělí číslo dnů do konce služby a vynásobí 12.
výsledek za denní mzdu zaměstnance.

.. matematika::
:class: přesahující

\text{Výpočet mzdy} = \frac{\text{Počet dnů v platbě}}{12} × \frac{\text{Mzda} + \text{Dávky}}}{30}

Ustanovení o dovolené
----------------------

Je počítáno tak, že se číslo dní dovolené vydělí 12 a výsledek pak násobí denním
plat zaměstnance.

.. matematika::
:class: přesahující

\text{Výpočet mzdy} = \frac{\text{Počet dní dovolené}}{12} \times \frac{\text{Mzda} + \text{Dávky}}}{30}

... _mzdy/mzdy_lokalizace/konec služby:

Konec služby
==============

Na konci výdejního lístku pro zaměstnance je uvedeno následující
které jsou na výplatním lístku jedinečné:

Nepoužité dovolené nahradí
--------------------------

Počet volných dnů dovolené je uveden na záznamu zaměstnance a vychází z ročního
zanechat typ dávky, který je definován v nastavení mzdy. Je vypočítávána jako celkový zůstatek přidělených alokací
Ten konkrétní druh dovolené, který zaměstnanci náleží.

Toto číslo se pak násobí denním příjmem zaměstnance a přičte jako příplatek k jeho
Příjmový list.

Příspěvek na odchod do penze
----------------------

Vypočítá se vynásobením denního výdělku zaměstnance počtem dní za ukončení
služba, která je v pracovní smlouvě zaměstnance uvedena.

.. matematika::
:class: přesahující

\text{Výpočet výplaty} = \frac{\text{Mzda + příspěvky na životní náklady}} {30} × \text{Počet dnů před koncem služby}

Mimo smlouvu
===============

Dny mimo smlouvu jsou dny, které spadají do období výplatního lístku, ale nejsou v něm zahrnuty.
doba trvání pracovního poměru zaměstnance. Odpovídající částka se odečítá jako srážka z výplatní pásky.
Výpočet se provádí násobením počtu dnů mimo pracovní poměr denním výdělkem zaměstnance.

.. matematika::
:class: přesahující

\text{Výpočet mzdy} = \frac{\text Mzda + Dovolená}{\text Počet dní v měsíci} × \text{Dny mimo smlouvu}
