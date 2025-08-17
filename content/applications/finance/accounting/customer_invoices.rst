Zobrazit obsah

=================
Faktury zákazníků
=================

Faktura zákazníka je dokument vystavený společností za produkty a/nebo služby prodané zákazníkovi.
zákazníkovi. Záznamy o přijatých platbách se provádějí v okamžiku, kdy jsou zákazníkům zaslány faktury. Faktura zákazníka může obsahovat
dlužné částky za dodané zboží a služby, příslušná prodejní daň, poštovné a balné
poplatky a další poplatky. Odoo podporuje více fakturačních a platebních postupů.

.. viz též:
:doc:`/aplikace/účetnictví/fakturace/přehled zákaznických faktur“

Od návrhu faktury po účetní závěrku je proces složitý a zahrnuje několik kroků.
služby byly objednány nebo dodány zákazníkovi v závislosti na zvolené fakturační politice:

- :ref:`účetnictví/vystavení faktury/vytvoření
- :ref:`účetnictví/faktura/potvrzení“
- :ref:`účetnictví/faktura/odeslání`
- :ref:`účetnictví/faktura/platba a vyrovnání`
- :ref:`účetnictví/faktura/doplnění`
- :ref:`účetnictví/faktura/reporting`

.. vytváření účetních dokladů a faktur

Vytváření faktur
================

Návrh faktury lze vytvářet přímo z dokumentů, jako jsou objednávky na prodej nebo nákup.
ručně z knihy faktur zákazníků v přehledu účetnictví.

Faktura musí obsahovat potřebné informace, aby zákazník mohl bez prodlení zaplatit za zboží.
zboží a služby. Ujistěte se, že jsou v následujících polích správně vyplněny:

- :guilabel:`Zákazník“: Když je vybrán zákazník, Odoo automaticky stáhne informace z
zákaznický záznam jako je fakturační adresa
:doc:`oblíbené způsoby platby <faktury/platební podmínky>“
:doc:`daňové pozice <daně/fiskální pozice>“, pohledávku a další položky na faktuře.
Chcete-li změnit tyto hodnoty pro tento konkrétní fakturu, upravte je přímo na faktuře.
jejich budoucí faktury, změňte hodnoty v kontaktní záznamu.
- :guilabel:`Datum faktury“: Pokud není tato hodnota nastavena ručně, je automaticky nastavená na aktuální datum.
Po potvrzení.
- :guilabel:`Datum splatnosti“ nebo :doc:`Platební podmínky <customer_invoices/payment_terms>“: K určení, kdy
Zákazník musí zaplatit fakturu.
- :guilabel:`Časopis`: Automaticky nastaveno a lze změnit, pokud je potřeba.
- Pokud je měna faktury odlišná od měny účtu,
Při zadání měny společnosti se automaticky zobrazí kurz.

V záložce „Částky faktury“:

- Klikněte na tlačítko „Přidat řádek“, pak vyhledejte a vyberte produkt.
- :guilabel:`Množství“
- :guilabel:`Cena“
- :doc:`Daně <taxes>“ (pokud je aplikovatelné).

Pro přístup do katalogu produktů a zobrazení všech položek v uspořádané podobě klikněte na: doc:`Katalog
</aplikace/skladovani-a-výroba/sklady/správa-skladu/sledování-stavu-zásob/katalog-produktů>.
Když jsou vybrány produkty a množství, klikněte na tlačítko „Zpět do faktury“.
faktura; vybrané položky z katalogu se objeví v řádcích faktury.

.. tip::
Pro zobrazení celkové částky faktury v slovesech přejděte na :menuselection:`Účetnictví -->
Konfigurace --> Nastavení a aktivujte položku „Celková částka faktury v písmenech“
volba.

Karta „Účetní položky“ zobrazuje účetní záznamy vytvořené. Další faktura
informace jako například :guilabel:`Referenční číslo zákazníka“, :guilabel:`Číslo platby“ nebo :doc:`Daňové
„Pozice daně/daňové pozice“, „Incoterms“ a další.
přidány nebo upraveny v záložce „Další informace“.

.. poznámka::
Odoo vytváří faktury nejprve ve stavu „Návrh“. Faktury ve stavu „Návrh“ nemají účetní dopad.
a účinky nebudou platné, dokud nejsou :ref:`potvrzené <účetnictví/faktura/potvrzení>`.

.. viz též:
:doc:`/aplikace/obchod/fakturace/předběžné faktury“

...účetnictví, faktura, potvrzení:

Potvrzení o přijetí faktury
====================

Klikněte na tlačítko „Potvrdit“ a stav faktury se změní na
:guilabel:„Vystaveno“ a vytvoří se záznam na základě konfigurace faktury.
potvrzení, Odoo přiřazuje každé faktuře unikátní číslo z definovaného seznamu.
<faktury zákazníků/pořadí>.

.. poznámka::
   - Jakmile je faktura potvrzena, již není možné provádět další změny. Klikněte na „Přepnout do verze návrhu“.
Změny jsou potřeba.
   - Pokud je třeba, faktury a další účetní záznamy lze uzamknout po zadání pomocí
:ref:`Zabezpečené příspěvky s funkcí <data-inalterability/restricted>“.

..účetnictví, fakturace, zasílání:

Souhlas s odesláním faktury
===============

Chcete-li nastavit preferovaný způsob odesílání faktury pro zákazníka, přejděte na
Vyberte položku „Účetnictví“ -> „Zákazníci“ -> „Zákazník“.
V kontaktním formuláři vyberte v záložce „Účetnictví“ požadovaný způsob zasílání faktur.
metoda v sekci „Faktury zákazníkům“.

.. poznámka::
Pro odesílání dopisů v Odoo je nutné použít: doc: In-App Purchase (IAP)
kredit nebo tokeny.

Chcete-li vystavit fakturu zákazníkovi, přejděte zpět do záznamu faktury a postupujte podle těchto kroků:

#Klikněte na tlačítko „Tisk a odeslání“.
#Pokud není vlastní fakturační šablona upravena,
Přesto se objeví okno „Nastavte formát dokumentu“. Nastavte formát a
klikněte na tlačítko „Pokračovat“.

.. poznámka::
      - Změna uspořádání dokumentu je možná v obecných nastaveních.
      - Přidat do faktury QR kód pro platbu v mobilní aplikaci, zapněte: guilabel:QR Code
možnost v okně „Nastavení formátu dokumentu“. Chcete-li tuto možnost upravit, přejděte
do sekce „Účetnictví -> Konfigurace -> Nastavení“ a posuňte se dolů k
v sekci „Platby zákazníků“ a zapnout/vypnout možnost „QR kódy“.

#V okně „Tisk a odeslání“:

   - Pokud byl v kontaktním formuláři vybrán preferovaný způsob odeslání faktury, je zvolen.
Výchozí je "Pouze v případě potřeby". Zvolte jiný, pokud chcete.
   - Pokud nebyl v kontaktním formuláři zvolen žádný preferovaný způsob odesílání faktury, vyberte
způsob, jakým bude faktura odeslána zákazníkovi.

#Klikněte na tlačítko „Tisk a odeslání“ v případě, že je vybrána možnost „E-mailem“, nebo klikněte
:guilabel:`Tisknout“.

...účetnictví/faktura/odesílání více faktur:

Odesílání více faktur
-------------------------

Pro odeslání a tisk více faktur přejděte na: „Účetnictví – zákazníci – Faktury“.
Vyberte je v seznamu „Faktury“ a klikněte na „Tisk a odeslání“.
Okno „Tisk a odeslání“ zobrazuje vybrané metody zasílání faktur podle preferovaného
metoda nastavení.

Do vybraných faktur se přidává poutač, který ukazuje, že jsou součástí právě probíhajícího odeslání a tisku.
výrobní šarže. To pomáhá zabránit tomu, aby se proces spustil ručně znovu, protože může trvat nějakou dobu
pro velmi vysoké objemy.

Pro kontrolu všech faktur, které ještě nebyly odeslány, přejděte na: „Účetnictví“ – „Zákazníci“.
Faktury“. V seznamu „Faktury“ klikněte do vyhledávacího pole a filtrujte podle
:guilabel:`Neposláno“.

...účetnictví, fakturace, platby a vyrovnání:

Platba a vyrovnání
==========================

V Odoo se faktura považuje za zaplacenou tehdy, když je spojena s příslušnou účetní položkou.
Souhlasí s odpovídající transakcí v bance.

.. viz též:
   - :doc:`platby“
   - :doc:`bankovní účet/srovnání“

...účetnictví, faktura, následná komunikace:

Sledování plateb
=================

Odoo nabízí nástroje pro sledování faktur, které pomáhají firmám vymáhat pohledávky od zákazníků.
Můžete nastavit různé akce pro připomenutí zákazníkům zaplacení jejich neuhrazených faktur.
jak dlouho je zákazník v prodlení. Tyto akce jsou seskupeny do úrovní sledování, které spouští
faktura je po splatnosti o určitý počet dní. Pokud máte více neuhrazených faktur,
stejný zákazník, akce se provádějí na nejpozdrženější faktuře.

..účetnictví, fakturace a reporting:

Reportáž
=========

...účetnictví, fakturace, partnerské zprávy:

Partneři reportují
---------------

...účetnictví, fakturace, partnerův účet

Partner Ledger
~~~~~~~~~~~~~~

Výkaz „Partner Ledger“ zobrazuje stav účtů zákazníků a dodavatelů. K jeho vygenerování je potřeba
Přejděte na: menu:Účetnictví -> Zprávy -> Účet partnera.

...účetnictví/faktury/zpráva o stárnutí:

Starý pohledávky
~~~~~~~~~~~~~~~

Pro přezkoumání neuhrazených faktur a jejich splatností použijte :ref:`Stáří pohledávky
<účetnictví/zpráva o hospodaření/pohledávky vymáhané soudně>“. Chcete-li se k ní dostat, přejděte na „Účetnictví“
Reportování --> Staré pohledávky.

...účetnictví, fakturace, pohledávky:

Starobní důchod
~~~~~~~~~~~~

Pro přezkoumání nedoplatků dodavatelům a jejich splatnosti použijte odkaz :ref:`Aged Payable.
<účetnictví/zprávy/staré faktury> zpráva. Chcete-li se k ní dostat, přejděte na:
Zpráva o stavu --> Staré faktury.

...účetnictví, faktury, zisk a ztráta:

Zisk a ztráta
---------------

Výkaz zisku a ztráty (anglicky Profit and Loss) uvádí podrobnosti o příjmech
a výdajů.

...účetnictví/faktury/rozvaha:

Výsledovka
-------------

:ref:`Výkaz zisku a ztráty <účetnictví/zprávy/výkaz zisku a ztráty>` shrnuje aktiva společnosti.
závazky a vlastní kapitál k určitému datu.

..toctree::


faktury-zakaznikum/prihled
faktury/adresy zákazníků
faktury pro zákazníky / platební podmínky
faktury_zákazníků/obchodní podmínky
faktury pro zákazníky/hotovostní slevy
faktury pro zákazníky / kreditní poznámky
faktury_zákazníkům/hotovostní srážka
faktury pro zákazníky / odložené příjmy
faktury_zákazníkům/elektronická fakturace
customer_invoices/sequence
customer_invoices/poštovní zásilka
faktury_pro_zákazníky/epc_qr_kód
faktury zákazníkům/INCOTERMS
