Zobrazit obsah

============
Faktury dodavatelů
============

Faktury dodavatelů lze v Odoo zadávat buď **ručně** nebo **automaticky**.
:ref:`Zpráva o věkové platitelnosti <účetnictví/faktury dodavatelů/zpráva o věkové platitelnosti>“ poskytuje přehled všech
neuhrazené faktury, aby se zajistilo včasné zaplacení správných částek.

.. viz též:
   - Návod „Registrace faktury dodavatele“
   - :doc:`/aplikace/sklad a výroba/nákup/spravovat obchody/spravovat`
   - :doc:`../účetnictví/faktury zákazníkům/přijaté faktury“

...vytváření faktur pro dodavatele:

Vytváření zákona
=============

... _účetnictví/faktury dodavatelům/vytváření ručně:

Ručně
--------

Chcete-li vytvořit fakturu dodavateli ručně, přejděte na: „Účetnictví - Dodavatelé - Faktury“.
Klikněte na „Nový“.

.. tip::
Alternativně je možné vytvořit fakturu dodavateli z účetního přehledu:

   - nebo klikněte na „Nový“ v záznamu „Faktury dodavatelů“.
   - nebo klikněte na ikonu „fa-ellipsis-v“ („vertikální elipsa“)
:guilabel:`Faktury dodavatelů“ v deníku, pak „Faktura“ pod záložkou „Nový“.

.._účetnictví/faktury od dodavatelů/automatické:

Automaticky
-------------

Faktury dodavatelů mohou být automaticky vytvářeny různými způsoby:

- Emailem na e-mailovou adresu spojenou s nákupem
novinách. Pokud e-mail neobsahuje platný soubor, odesílatel obdrží automatickou odpověď
že žádný dokument nebyl přijat.
- Nahrání PDF: Chcete-li nahrát fakturu, přejděte na: „Účetnictví“ - „Dodavatelé“ - „Faktury“, pak
klikněte na tlačítko „Nahrát“.

.. poznámka::
   - Jakmile je nahrán účet, objeví se na pravé straně obrazovky dokument ve formátu PDF.
snadno vyplnit údaje o faktuře.
   - Faktury lze digitalizovat a automaticky doplňovat.
   - Služby, jako je digitalizace skenovaných nebo PDF faktur dodavatelů v Odoo vyžadují :doc:`Veškeré informace
Nakupte si kredity (IAP).

Pro automatické vystavování faktur vybraným dodavatelům přejděte na: „Účetnictví“ - „Dodavatelé“.
Vyberte příslušného dodavatele a v záložce „Účetnictví“ pod
V sekci „Automatizace“ aktualizujte pole „Automatické vystavování faktur“ na jednu z následujících možností:
následujících možností:

- :guilabel:`Vždy“
- :guilabel:Zeptejte se po třech platných ověřeních bez úprav
- :guilabel:`Nikdy“

...účetnictví/faktury dodavatelů/úplná faktura:

Dokončení úhrady faktury
===============

Ať už je faktura vytvářena ručně nebo automaticky, zkontrolujte následující pole:
vhodně vyplněno:

- :guilabel:`Dodavatel“: Odoo automaticky vyplní některé informace na základě informací z
výpis kontaktu dodavatele, předchozí objednávky a faktury.
- :guilabel:`Referenční číslo faktury od dodavatele`: Přidejte referenční číslo objednávky dodavatele.
dříve byly produkty při přijetí spárovány s:ref:`účetnictvím <účetnictví/platby/srovnání plateb>`.
- :guilabel:`Dokončení dokumentu“: Vyberte fakturu nebo nákupní objednávku, abyste dokončili dokument
automaticky. Před dokončením této položky by měla být vyplněna pole „Dodavatel“.
- :guilabel:`Datum vydání“: Vyberte datum vydání dokumentu.
- :guilabel:`Datum účetního záznamu“: Aktualizujte datum účetního záznamu dokumentu, pokud je potřeba.
- Poznámka k platbě: pole Poznámka automaticky zahrnuje platbu
Přihlášení platby je možné pouze jednou.
- :guilabel:`Příjemce banky“: Udává číslo účtu, na který bude platba připsána.
Pole je vyžadováno při platbě prostřednictvím souborů platebních příkazů (např. :ref:`NACHA
<l10n_us/ach-electronic-transfers>` a :doc:`SEPA <payments/pay_sepa>`.
- V případě platby faktury je nutné zadat datum splatnosti nebo podmínky úhrady.
- :label_guilabel:Časopis: Vyberte, do kterého časopisu se má zaznamenat faktura a v jaké měně
<začít/více měn>.

V záložce „Částky faktury“:

- Klikněte na tlačítko „Přidat řádek“, pak vyhledejte a vyberte produkt.
- :guilabel:`Množství“
- :guilabel:`Cena“
- :doc:`Daně <taxes>“ (pokud je aplikovatelné).

.. tip::
Pokud se v databázi nevyskytuje žádný produkt odpovídající položce na faktuře, klikněte
:ikonka: „zobrazit seznam“ :guilabel: (čárky) ikonu pro vstup do popisu položky na faktuře bez
připojit ho k produktu.

Pro přístup do katalogu produktů a zobrazení všech položek v uspořádané podobě klikněte na: doc:`Katalog
</aplikace/skladovani-a-výroba/sklady/správa-skladu/sledování-stavu-zásob/katalog-produktů>.
Když jsou vybrány produkty a množství, klikněte na tlačítko „Zpět do faktury“ a vrátíte se zpět
faktura dodavatele; vybrané položky z katalogu se objeví v řádcích faktury dodavatele.

.. poznámka::
Pokud dodavatel nemá zboží skladem a odesílá objednávku později, může být vystaven více faktur za stejnou objednávku.
pokud je zboží dodáno nebo vystaveny faktura, která obsahuje částku menší než celková cena objednávky.
V tomto případě může mít více faktur stejný :guilabel:`Reference k faktuře`.

...účetnictví/faktury dodavatelů/potvrzení faktury:

Potvrzení faktury
=================

Klikněte na tlačítko „Potvrdit“ po dokončení dokumentu. Stav se změní na „Odesláno“.
a na základě informací o faktuře dodavatele je vytvořen záznam v deníku. Po potvrzení je Odoo přiřazeno
Každý dodavatel má unikátní číslo z definované sekvence: doc:`<vendor_bills/sequence>“.

.. poznámka::
Jakmile je faktura dodavatele potvrzena, už ji nelze aktualizovat. Klikněte na tlačítko „Návrh“
Potřebují se změny.

.. účetnictví / faktury dodavatelů / platba faktur:

Platba a vyrovnání
==========================

Pro registraci platby klikněte na „Zaplatit“. V okně „Zaplatit“ vyberte
„Časopis“, „Způsob platby“, „Výše“ a
:guilabel:`Měna“.

Pokud je částka uhrazená za :guilabel:`Amount` nižší než celková zbývající částka na faktuře dodavatele,
Platba je částečná (účetnictví/platby/částečná platba) a je označená jako „Částka
V poli „Rozdíl“ se zobrazuje nedoplacená částka.

Pole „Záznam“ se automaticky vyplní, pokud je nastavené pole „Referenční číslo platby“.
správně na faktuře dodavatele. Pokud pole zůstane prázdné, vyberte číslo faktury dodavatele jako
reference.

Klikněte na tlačítko „Vytvořit platbu“. Zobrazí se bannery „Na účtu“ a „Částka“.
na faktuře až do chvíle, než je :doc:`vyrovnána <bank/reconciliation>` a její stav se aktualizuje na
:guilabel:`Placená reklama“.

.. viz též:
   - :doc:`platby“
   - :doc:`bankovní účet/srovnání“

... /účetnictví/faktury dodavatelů/výkaz věřitelů:

Zpráva o dluhu vůči osobám starším 75 let
===================

Pro získání přehledu o neuhrazených fakturách a jejich splatnosti přejděte na:
--> Hlášení --> Staré pohledávky“.

Klikněte na ikonu „pravý směr“ vedle dodavatele, abyste zobrazili podrobnosti.
včetně splatnosti a výše dluhu.

.. Poznámka:
Klikněte na tlačítko „PDF“ nebo „XLSX“, abyste vytvořili soubor ve formátu PDF nebo XLSX.

..toctree::


faktury dodavatelů/digitalizace faktur
faktury dodavatelů / aktiva
faktury dodavatelů / odložené výdaje
faktura od dodavatele / pořadí
