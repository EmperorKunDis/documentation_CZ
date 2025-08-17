========================
Kreditní poznámky a vrácení peněz
========================

Kreditní nebo debetní poznámka je dokument zaslaný zákazníkovi s informací, že
byli přičteny nebo odečteny určité částky.

Kreditní poznámka může být vystavena z několika důvodů, například:

 - chyba na faktuře
 - vrácení zboží nebo odmítnutí služeb
 - doručené zboží je poškozené

Debetní poznámky jsou méně časté, ale nejčastěji se používají k sledování dluhů vůči zákazníkům nebo
dodavatelé kvůli změnám potvrzených fakturách zákazníkům nebo dodavatelským fakturám.

.. poznámka::
Vydání kreditní nebo debetní poznámky je jediným legálním způsobem zrušení, vrácení nebo změny
potvrzenou fakturu. Ujistěte se, že **zaregistrujete platbu** poté, co vám bude peníze vráceny zpět
zákazníkovi a ověřit
:doc:`vrací </applications/sales/sales/products_prices/returns>` pokud jde o skladovatelný produkt.
vráceny.

...účetnictví/daňové doklady/vystavení daňového dokladu:

Vystavit zákazníkovi kreditní fakturu
============================

Většinou se kreditní poznámky vytváří přímo z odpovídajících faktur.
Přejděte na položku „Účetnictví“ -> „Zákazníci“ -> „Faktury“, otevřete příslušnou fakturu.
a klikněte na položku „Zápočet“.

V okně „Poznámka k úvěru“ zadejte důvod, který se objeví na faktuře.
Aktualizujte pole „Časopis“ a „Datum obratu“, pokud je to nutné.
Je dvě možnosti:

- Klikněte na tlačítko „Odmítnout“ a otevřete si návrh faktury s přesnými údaji z objednávky.
originální faktura. Aktualizujte položky „Produkt“ a „Množství“ a klikněte
:guilabel:`Potvrdit“. Tato možnost umožňuje částečnou úhradu nebo změnu kreditní poznámky.
- Klikněte na tlačítko „Zpět a vytvořit fakturu“ pro vytvoření kreditní poznámky, ověřit ji automaticky
připojit k němu fakturu související, otevřít nový návrh faktury s předvyplněnými údaji přesným.
podrobnosti z původní faktury.

Vytvoření účetního dokladu od nuly proveďte v menu:Účetnictví --> Zákazníci --> Kredit
Zadejte poznámku, klikněte na tlačítko „Nový“ a vyplňování úvěrové poznámky probíhá stejným způsobem jako vyplňování
fakturu:ref:`<účetnictví/faktura/vytvoření>`.

.. poznámka::
Řetězec kreditní poznámky začíná písmenem R a je následován číslem souvisejícího dokumentu (např.
RINV/2025/0004 je spojen s fakturou INV/2025/0004.

...účetnictví/kreditní poznámky/vystavení debetní poznámky:

Vystavte zákazníkovi fakturu.
===========================

Vytvoření faktury provedete v menu: „Účetnictví“ - "Zákazníci" - "Faktury".
Tyto kroky:

#Vyberte požadované faktury, klikněte na ikonu „Nástroje“ a vyberte
:guilabel:`Vytvořit debetní poznámku“.
#V okně „Vytvoření debetní poznámky“ vyplňte důvod a aktualizujte
:guilabel:`Použijte pole pro specifický účet“ a „Datum poznámky o debetu“ pouze v případě potřeby.
#Zapněte možnost „Kopírovat řádky“ a poté klikněte na tlačítko „Vytvořit
„Debetní poznámka“.
#V poznámce k úhradě aktualizujte položky „Produkt“ a „Množství“ a klikněte
:guilabel:`Potvrdit“.

.. tip::
Chcete-li vytvořit fakturu z pohledu formuláře objednávky, klikněte na ikonu „Ozubené kolo“
ikonu a vyberte: guilabel: Debetní poznámka.

..účetnictví, kreditní poznámky, záznamy o vrácení peněz od dodavatele:

Zaznamenat vrácení peněz od dodavatele
======================

Vrácení peněz od dodavatele nebo vystavení kreditní faktury se zaznamenává stejně jako:ref:`faktura
<účetnictví/faktury/vystavit fakturu>

Pro zaznamenání vrácení peněz nebo účtování kreditu od příslušného dodavatele přejděte na
:menu „Účetnictví“ -> „Dodavatelé“ -> „Faktury“, otevřete příslušnou fakturu dodavatele a klikněte
:guilabel:`Poznámka k účtu“.

Pro nahrání zadávejte do políčka „Účetnictví > Přijaté platby > Vrácení“ a klikněte na
:label:Nový.

...účetnictví/poznámky k úhradě/záznam o poznámce k úhradě:

Zaznamenat fakturu dodavatele
==========================

Debetní poznámky od dodavatelů jsou zaznamenávány stejně: ref>:debetní poznámky jsou vydávány zákazníkům
<účetnictví/kreditní poznámky/vystavení debetní poznámky>.

Pro zaznamenání pohledávky přejděte do sekce „Účetnictví“ -> „Dodavatelé“ -> „Faktury“.
požadovaný doklad. Klikněte na ikonu „fa-cog“ a vyberte možnost „Vytvořit účetní dopis“.

.. tip::
Chcete-li vytvořit fakturu dodavatele z pohledu formuláře Faktura odběratele, klikněte na ikonu :icon:`fa-cog`.
ikona „Převod zůstatku“ a vyberte „Dodací list“.

..účetnictví/daňové doklady/doklady o kreditu:

Deník
===============

Vytvoření poznámky o úhradě z faktury vede k **zrušení vstupu**, který vyrovnává
dokumenty z původní faktury.

.. příklad::
Účetní záznam o vystavení faktury:

.... obrázek: credit_notes/dokumenty_faktury.png
:alt:Účetní záznam o faktuře

Záznam z účetního deníku, který byl vytvořen pro obrácení původní faktury:

...... obrázek: credit_notes/záznamy-z-deníku-poznámka-o-úhradě.png
:alt: Záznam v deníku kreditních poznámek opakuje záznam z deníku faktur
