Zobrazit obsah

========================
Účetnictví a fakturace
========================

Odoo Fakturace je samostatná aplikace, která vám umožní vytvářet faktury, odesílat je zákazníkům a spravovat
platby. Dále také zpracovává toky spojené s fakturami od dodavatelů. Na druhou stranu aplikace Účetnictví je
komplexní účetní řešení, které umožňuje stejné akce a zahrnuje další funkce, jako
jako standardní finanční zprávy, vyrovnání účtů, rozpočty, správa aktiv a další.

.. viz též:
„Návody k Odoo: Účetnictví <https://www.odoo.com/slides/accounting-19>“

.. karty:

......karta: Začínáme
:target: účetnictví/začínáme
:velké:

Základní pojmy účetnictví a založení vašeho účetnictví

...... karta:Daně
:target: účetnictví/daně

Daně, fiskální pozice a integrace

...... karta: Faktury pro zákazníky
:target: účetnictví/faktury zákazníkům

Faktury zákazníků, platební podmínky a elektronická fakturace

....... karta: Faktury dodavatele
:target:účetnictví/faktury od dodavatelů

Faktury dodavatelů, majetek a digitalizace faktur (OCR)

......karta: Platební metody
:target: účetnictví / platby

Faktury a platby faktur (on-line, šeky, sestavy), kontrola plateb faktur

....... karta:Bankovní a hotovostní účty
:target: účetnictví / banka

Synchronizace bankovních účtů, vyrovnání a pokladny

......karta: Zprávy
:target: účetnictví/reporting

Hlášení, vykazování a analytické účetnictví

..účetnictví/dvojí účtování:

Dvojí účetnictví
========================

Odoo automaticky vytváří všechny podkladové účetní záznamy pro všechny účetní transakce (např.
faktury zákazníků, dodavatelské faktury, objednávky z prodejny, výdaje, ocenění zásob apod.

Odoo používá systém dvojího účetnictví, kdy každá položka potřebuje odpovídající protislužbu.
protistrana v jiném účtu, z jednoho účtu odečteno a na druhý připsáno.
Zajišťuje, aby všechny transakce byly zaznamenány přesně a konzistentně a aby účty
Vždy musíte vyvážit.

.. viz též:
:doc:`Příručka účetnictví <accounting/get_started/cheat_sheet>`

...účetnictví/účtování - hotovostní:

Metoda účtování a metoda hotovostního pohybu
======================

Oba způsoby účtování jsou v Odoo podporovány, což umožňuje zobrazit příjmy a
v okamžiku, kdy se transakce uskuteční (metoda přičítání), nebo v okamžiku, kdy je platba provedena či přijata.
na základě hotovosti.

.. viz též:
:doc:`Účetnictví na základě hotovosti <účetnictví/daně/hotovostní báze>`

..účetnictví / více společností:

Společnost s více subjekty
=============

:doc:`Může být spravováno více společností v rámci jednoho
databáze. Každá společnost má svůj vlastní „účetní výkaz
<účetnictví/zahájení/rozvaha>“, ale „:ref: účty mohou být sdílené
<souhrnné účty>, což je užitečné při zobrazování souhrnných výkazů. Uživatelé mohou zobrazit
záznamy a zprávy od více společností najednou, ale může pracovat pouze na jedné společnosti.
účetnictví v čase.

.. viz též:
   - :doc:`Společnost s více subjekty </aplikace/obecné/firmy/multisubjektní-firma>`
   - :ref:`Transakce mezi společnostmi <obecné/multicompany/transakce mezi společnostmi>`

..účetnictví/měna:

Multiměnová prostředí
==========================

Multiměnový účetní systém s automatizovaným
směnný kurz pro usnadnění mezinárodních transakcí je k dispozici v Odoo. Každá transakce je zaznamenaná
v měně společnosti; pro transakce v jiné měně ukládá Odoo obě
hodnota v měně společnosti a hodnota transakce v měně. Odoo generuje měnu
zisk a ztrátu po vyrovnání položek v účetním deníku.

.. viz též:
:doc:`Správa banky v cizí měně <účetnictví/banka/cizí_měna>`

...účetnictví/pobočky:

Banky
========

Rodiče: společnosti a jejich pobočky
<obec/firmy/odvětví> lze spravovat v jedné databázi, která běží na sdíleném
účetní a reportingové pravidla, včetně následujících:

- Účetní kniha mateřské společnosti
hlavní měna (účetnictví/základy/multiměnový účet), a daně (účetnictví/daně)
Vztahuje se na všechny pobočky.
- Branchy si mohou spravovat své vlastní specializované časopisy a související záznamy.
- Mateřská společnost spravuje společný :ref:`daňový období <roční konec/daňové roky>`, takže její
:ref:`zámky a datum uzavření <datum-konec-roku/zamknout-vsechno-datum> platí pro všechny pobočky.
Banky mohou stanovit dřívější datum uzavření účtu, pokud je to nutné.
- Mateřská společnost má přístup ke všem zprávám o účetnictví a fakturám.
<účetnictví/faktury zákazníkům>, „faktury dodavatelů“ <účetnictví/dodavatelské faktury> atd.
Každá větev může vidět pouze svá vlastní data.

.. poznámka::
Paket pro daňovou lokalizaci :doc:`<fiscal_localizations>` je nastaven na mateřskou společnost.

.. varování:
Přidáním pobočky do společnosti umožníte:
<../obecne/firmy/multifirma>.

Pro více informací se podívejte na stránku „Ceník Odoo“ <https://www.odoo.com/pricing-plan>.
kontaktujte svého manažera účtu Odoo.

..účetnictví/odvětví/hospodářské výsledky:

Reportáž
---------

Společnost zahájila konzolidaci účetních operací všech poboček prostřednictvím centrální
výhledu, například výsledovce nebo rozvahy.

..účetnictví/odštěpný závod/DPH:

DPH
---

Každá společnost a pobočka musí být konfigurována s vlastními právními informacemi, včetně DPH.
v případě, že je to možné. Podle struktury mohou pobočky sdílet DIČ mateřské společnosti nebo
mají své vlastní, čímž se zvyšuje počet společných nebo samostatných :doc:`daňových přiznání
<účetnictví/výkaznictví/daňové přiznání>.

Toto flexibilní nastavení umožňuje uživatelům vytvářet individuální zprávy a daňová přiznání pro každou entitu.
nebyla nutná.

...účetnictví/mezinárodní standardy:

Mezinárodní standardy
=======================

Odoo Accounting podporuje více než 100 zemí a poskytuje standardizované funkce a mechanismy.
použitelné ve všech regionech. Do modulů je zahrnuta i specifická účetní legislativa pro daný stát
Nařízení. Fiskální lokace <fiskalni_lokalizace> se zabývají regionálními požadavky, jako
jako účetní knihy, daně nebo jakékoliv jiné právní povinnosti.

...účetnictví/příjmy a výdaje:

Závazky a pohledávky
===============================

Výchozí účet je určen pro příjmy a další účet pro výdaje.
placené položky. Protože transakce jsou spojeny s kontakty, je možné vygenerovat zprávu podle
zákazník, dodavatel nebo subdodavatel.

Výkaz Partner Ledger zobrazuje stav účtů klientů a dodavatelů. Chcete-li se do něj dostat, přejděte na
:menu „Účetnictví -> Vykazování -> Účetní kniha partnera“.

...účetnictví/reporting:

Reportáž
=========

Následující finanční zprávy jsou k dispozici a aktualizovány v
v reálném čase:

+-----------------------------------------------+
|Finanční výkazy|
+============+==================================+
|Výrok  |Výsledovka
|            +----------------------------------+
|Profit a ztráta|Profit and loss
|            +----------------------------------+
|  Výkaz cash flow   |Výkaz o peněžních tocích
|            +----------------------------------+
|Výkonná zpráva|Výkonné shrnutí
|            +----------------------------------+
|             |Daňové přiznání                   |
|            +----------------------------------+
|             |Prodejní list EU                   |
+------------+----------------------------------+
|Audit       |Účetní kniha                          |
|            +----------------------------------+
|Trial balance|
|            +----------------------------------+
|             |Audit časopisu                   |
|            +----------------------------------+
|Intrastatní hlášení|Intrastat report
|            +----------------------------------+
|             |Kontrolní kniha                      |
+------------+----------------------------------+
|Partner     |Účet partnera                      |
|            +----------------------------------+
|Aktiva|Zaúčtované faktury                       |
|            +----------------------------------+
|Aktuální dluh  |Aktivní splatná částka           |
+------------+----------------------------------+
|Management | Analýza faktur
|            +----------------------------------+
|Analytický report|
|            +----------------------------------+
|Auditní stopa|Auditní stopa
|            +----------------------------------+
|Budgetní zpráva|
|            +----------------------------------+
|Nepočítané měnové zisky/ztráty|
|            +----------------------------------+
|            |Zálohované příjmy          |
|            +----------------------------------+
|Deferované výdaje|Deferované výdaje
|            +----------------------------------+
|Depreciační     |Schéma depreciace             |
|            +----------------------------------+
|Nesplněné výdaje|Nepovolené výdaje
|            +----------------------------------+
|            |Analýza úvěrů                    |
|            +----------------------------------+
|Produktové marže|
|            +----------------------------------+
|            |1099 hlášení                     |
+------------+----------------------------------+

.. tip::
:doc:`Vytvářejte a přizpůsobujte zprávy <účetnictví/zprávy/vlastní zpráva> s motorem pro vytváření zpráv Odoo.“

...účetnictví/daňový výkaz:

Daňové přiznání
----------

V přehledu o dani z příjmu se v Odoo počítají všechny účetní transakce za
Specifický daňový období a používá tyto součty k výpočtu daňové povinnosti.

.. poznámka::
V závislosti na lokalizaci země může být vygenerován XML soubor s daňovým přiznáním.
nahrazena na příslušný daňový portál.

.._účetnictví/synchronizace s bankou:

Synchronizace bank
====================

Synchronizační systém banky je přímo propojen s bankovními institucemi a automaticky
importovat všechny transakce do databáze. To dává přehled o pohybu peněz bez nutnosti zadávání
do internetového bankovnictví nebo čekat na papírové výpisy z účtu.

.. viz též:
:doc:`Synchronizace bankovního účtu <účetnictví/banka/bankovní-synchronizace>`

.. účetnictví / inventarizační ocenění:

Ocenění zásob
===================

Oba periodické (ruční) i trvalé (automatizované) způsoby ocenění zásob jsou v Odoo podporovány.
Dostupné metody jsou standardní cena, průměrná cena, LIFO (poslední vstup, první výstup) a
:zkr. „FIFO (první vstup, první výstup)“.

.. viz též:
:doc:`../inventar-und-mrp/Inventar/Produktverwaltung/Inventarisierungswertberechnung/Inventarisierungswertberechnung_konfigurieren`

.. _účetnictví/zůstatková hodnota:

Zůstatková hodnota
=================

Zůstatková hodnota je část příjmů, která zůstává ve firmě. Odoo vypočítá aktuální roční
Zisky v reálném čase, takže není potřeba roční účetní kniha nebo převod. Zisk
A ztráta je automaticky uvedena v rozvaze.

.. viz též:
:doc:`Příručka účetnictví <accounting/get_started/cheat_sheet>`

…účetnictví a správce majetku:

Fiduciáři
===========

Režim „Účetní firmy“ lze aktivovat kliknutím na „Účetnictví ->
Konfigurace --> Nastavení“. Když je zapnutá:

- Všechny dokumenty mají možnost upravit pořadí položek.
- V poli „Celkem (včetně DPH)“ se zobrazuje hodnota, která umožňuje rychlejší a kontrolované kódování automatizací.
vytvoření řádku s tím správným účtem a daní;
- V poli „Datum faktury“ je předvyplněno datum vystavení faktury.
- Možnost „Rychlého kódování“ je dostupná pro faktury zákazníků a dodavatelské faktury.

.._přístupová práva účetního/účetní:

Přístupová práva účetního
========================

Přidat účetního jako nového uživatele
a nakonfigurujte příslušná práva přístupu podle :doc:`dokumentace
V sekci „Účetnictví“ v položce „Přístupová práva uživatelů“ klikněte na tlačítko
Finanční údaje společnosti:

- Vyberte „Účetnictví“ a poté vyberte „Účetní“.
- :guilabel:`Banka“: Povolit ověření bankovního účtu.

.. Poznámka:
Přidání účetního jako nového uživatele v sekci :doc:`Odoo Online <../../administration/odoo_online>
je zdarma, pokud účetní má v Odoo registrovaný stejný e-mail jako ten, který používáte.
jsou uvedeny pro společnost.
:doc:`Odoo On-premise <../../administration/on_premise>“ může být spojeno s dalšími poplatky za každou
další uživatel. Ceny naleznete na
„Ceník Odoo“ <https://www.odoo.com/pricing-plan>.

V případě více společností nastavte vhodný přístup podle :ref:`přístupů k uživatelům <users/multi-companies>`.

..toctree::


účetnictví/začínáme
účetnictví/daně
účetnictví / faktury zákazníkům
účetnictví/faktury dodavatelů
účetnictví / platby
účetnictví/banka
účetnictví/hospodářské výsledky
