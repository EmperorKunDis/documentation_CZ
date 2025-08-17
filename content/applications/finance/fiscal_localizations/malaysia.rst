========
Malajsie
========

... MyTax: https://mytax.hasil.gov.my

.._malajsie/konfigurace:

Konfigurace
=============

.._malajsie/konfigurace/moduly:

Instalace modulů
--------------------

Instalujte následující moduly, abyste získali všechny funkce malajské
lokalizace:

.. seznam tabulkový::
:hlavičkové řádky: 1

   * Jméno
     - Technické označení
     - Popis
   * --label:Malajsie - Účetnictví
     - „l10n_my“
     - Tento modul zahrnuje výchozí
:ref:`daňová lokalizace <fiscal_localizations/packages>“.
   * :- guilabel:Malajsie - Účetní zprávy
     - l10n_my_reports
     - Tento modul obsahuje účetní výkazy pro Malajsii.
   * :-label:Malajsie - UBL PINT
     - „L10N_MY_UBL_PINT“
     - Tento modul obsahuje funkce potřebné pro vývoz faktur v formátu PINT.
   * --:guilabel:Malajsie - Elektronické faktury
     - „l10n_my_edi“
     - Tento modul obsahuje funkce potřebné pro integraci s MyInvois podle IRBM.
   * --:guilabel:`Malajsie - Rozšířené funkce elektronických faktur“
     - „l10n_my_edi_extended“
     - Tento modul zlepšuje funkci elektronického fakturování MyInvois přidáním správné podpory pro samo
účtování, zobrazení kódu QR MyInvois na faktuře ve formátu PDF a umožňuje lepší správu
zahraničního zákazníka DIČ.

.. _malajsie/konfigurace/firma:

Informace o společnosti
-------------------

Pro konfiguraci informací o společnosti přejděte do aplikace Kontakty, vyhledejte svoji firmu
a vyberte ji. Poté nastavte následující pole:

- :label:Jméno
- včetně města, státu a poštovního směrovacího čísla
a :guilabel:`Země“.

   - Do pole „Ulice“ zadejte název ulice, číslo popisné a případně další adresu.
informace.
   - Do pole „Ulice 2“ zadejte čtvrť.

- :guilabel:`Daňové identifikační číslo“: Daňové identifikační číslo
- :guilabel:`DSS“: číslo malajsijské daně z prodeje a služeb, pokud je aplikovatelné
- :guilabel:`TTx`: malajský turistický daňový číslo (pokud je k dispozici)
- :guilabel:`Telefon“

Správa faktur v systému MyInvois
=====================================

Portál MyInvois je platformou poskytovanou :abbr:`IRBM (Inland Revenue Board of Malaysia)`
který usnadňuje implementaci elektronických faktur pro malajské daňové poplatníky.
Odoo podporuje integraci s MyInvois, aby bylo možné odeslat faktury vytvořené v Odoo.

.. poznámka::
Pro zaslání faktur do MyInvois je nutné nainstalovat modul „Malajsie – elektronické faktury“.

..._malajsie/moje-vioz/nastavení:

Nastavení
------

.. _malajsie/moje_ivais/nastavení/registrace:

Registrace na MyInvois
~~~~~~~~~~~~~~~~~~~~~

Pro odeslání elektronické faktury do MyInvois je nejprve nutné se zaregistrovat a přihlásit do MyInvois
portál, který udělí společnosti Odoo právo vystavovat faktury jako prostředník za vaši firmu.

.. poznámka::
Pokud se přihlašujete do portálu poprvé, klikněte na tento odkaz:
MyTax, abyste se dozvěděli více o registračním procesu. Oba **testovací provoz** (:dfn:`testing
prostředí, ve kterém se funkce testují předtím, než je použijete v reálném (produkčním) prostředí.
**výroba** (dfn: „skutečné prostředí, ve kterém je možné podávat daňové doklady s přesnými údaji“)
podporují všechny prostředí.

#Přihlaste se do služby MyTax. Vyberte „Druh ID“ a odpovídající
:guilabel:`identifikační číslo“ používané k registraci digitálního certifikátu.
#Od přehledu klikněte na ikonu :icon:`fa-angle-down` :guilabel:`(angle-down)`
v pravém horním rohu a vyberte „Zobrazit profil daňového poplatníka“.
#V sekci „Zástupci“ klikněte na tlačítko „Přidat zprostředkovatele“ v pravém horním rohu.
rohu.

.... obrázek: malajsie/myinvois-add-intermediary.png
:alt:MyInvois přidá prostředníka

#Přidejte Odoo SA jako prostředníka pomocí následujících informací:

   - :guilabel:`Číslo TIN“: „C57800417080“
   - :guilabel:`BRN`: `BE0477472701`
   - :label:Jméno:

     - :guilabel:`Výroba“: „Odoo S.A.“
     - :guilabel:`Předprodukce“: „OXXX_XXXXA.“

#Povolte následující oprávnění kliknutím na ikonu :icon:`fa-toggle-on` :guilabel:`(toggle-on)`
ikonka:

   - :guilabel:`Zástupce od“
   - :guilabel:`Dokument - Odeslat“
   - :guilabel:`Dokument – Zrušit“
   - :guilabel:`Dokument - Odmítnutí požadavku“

.. poznámka::
      - Přístup může být v budoucnu odebrán, pokud bude třeba.
      - Odoo jako prostředník neukládá faktury zaslané jménem klienta na serveru
server.

#Klikněte na tlačítko „Uložit“. Stav pro společnost Odoo SA pak bude „Aktivní“.

.... obrázek:malajsie/myinvois-zprostředkovatel-aktivní.png
:alt:Stav MyInvois aktivní

.. _malajsie/moje_faktury/nastavení/odoo:

Konfigurace v Odoo
~~~~~~~~~~~~~~~~~~~~~

.. _malajsie/moje_faktury/nastavení/odoo/elektronické fakturace:

Společnost
*******

Otevřete aplikaci Nastavení, přejděte do sekce „Společnosti“ a klikněte
„Aktualizovat informace“. Ujistěte se, že je zadána „Daňové identifikační číslo“ a dokončete následující
pole v sekci E-fakturace:

   - Vyberte typ identifikace a zadejte spojený
:guilabel:`Registrační číslo“ používané k registraci digitálního certifikátu.
   - :guilabel:`Klasifikace indikátoru“: Zadejte pětimístný číselný kód, který reprezentuje
aktivity podniku.

Elektronická fakturace
********************

Přejděte na: „Účetnictví“ -> „Konfigurace“ -> „Nastavení“.
V sekci „Elektronické fakturace v Malajsii“ vyberte příslušný režim „Můj fakturační systém“.
na základě prostředí použitého pro registraci společnosti MyInvois.

Ujistěte se, že jste zaškrtli políčko „Přijmout elektronické faktury“, pak klikněte na tlačítko „Registrovat“.

.. poznámka::
Chcete-li změnit odkaz na číslo daňového identifikátoru, klikněte na tlačítko „Odhlásit se“.
změnit informace o společnosti a ujistit se, že číslo registrované na MyInvois odpovídá.
:guilabel:`Registrace“ znovu.

.. důležité::
Pro daňové poplatníky s TIN začínající „IG“ a
:zkratka „Registrace podnikání“ (ROB), kombinujte DIČ a ROB v formátu „TIN:ROB“.
pro pole „Daňové identifikační číslo“.

Chcete-li se zaregistrovat, přejděte na: „Účetnictví --> Konfigurace --> Nastavení“ a v
v sekci „Malajsijské elektronické fakturace“, klikněte na „Registrace“.
Po dokončení registrace lze z pole „Daňové identifikační číslo“ odstranit znak „:ROB“.

Navíc si nezapomeňte přihlásit do účtu „MyTax“ (<https://mytax.hasil.gov.my/>) a nastavit
:guilabel:`Typ role“ jako „Majitel podniku“.

... _malajsie/moje_faktury/nastavení/odoo/firma:

Kontakty
********

Přejděte na kontaktní formulář a vyplňte následující pole:

   - :guilabel:`Země“
   - :guilabel:`Stát“
   - :guilabel:`Telefon“
   - :guilabel:`Daňové identifikační číslo“
   - „Označení“: „Typ označení“ a odpovídající
:guilabel:`Identifikační číslo“ kontaktu zaregistrovaného na MyTax.

.._malajsie/moje-faktury/nastavení/odoo/produkt:

Produkty
********

Všechny produkty, které mají být zahrnuty do elektronických faktur, vyžadují malajsijský kód klasifikace.
Přejděte do formuláře „Produkt“ a v záložce „Obecné informace“ vyplňte
:guilabel:„Kód malajské klasifikace“ pole.

Malajský daňový typ
******************

Pro konfiguraci daně zvolte pole „Typ malajsijské daně“ v sekci „Účetnictví“ ->
Konfigurace --> Účetnictví --> Daně a otevřete v seznamu daní v poli „Daně“
pohled.

Při vystavení faktury nebo účtu je daň zahrnuta s nastavením „Malajsijského typu daně“
*Od daně osvobozeno*, důvod od daně musí být uveden v „Mých fakturách“.
tabulku před odesláním dokumentu.

.. obrázek: malajsie/důvod-osvobození-od-dph.png
:alt: Důvod osvobození od daně z přidané hodnoty MyInvois

.._malajsie/moje-vioz/proudu:

Průběh práce
--------

.._malajsie/moje-vioz/pruvodce-zasilani:

Faktury zasílejte na MyInvois
~~~~~~~~~~~~~~~~~~~~~~~~~

Faktury můžete odeslat na MyInvois až po jejich potvrzení. Klikněte
:guilabel:`Odeslat do MyInvoice“.

Faktury posílejte na MyInvois
~~~~~~~~~~~~~~~~~~~~~~

Pokud vystavíte fakturu na jméno dodavatele, je nutné ji zaslat do MyInvois.
faktura je potvrzena, klikněte na: guilabel:"Odeslat do Mého Invoice".

.. poznámka::
   - Ve „Správě faktur pro dodavatele“ („<https://preprod.myinvois.hasil.gov.my/content>“) jsou
zařazené do kategorie :guilabel:`Faktura vystavená na vlastní jméno“.

   - Pokud pole „Referenční číslo faktury“ je prázdné, použije se jako referenční číslo faktury dodavatele číslo faktury společnosti Odoo.
Číslo faktury MyInvois. Pokud je do pole „Referenční číslo“ zadáno nějaké číslo,
Reference je použita místo toho.

.. _malajsie/moje_invaze/průběh/odeslání/stav:

Stav mého účtu
***************

Aktuální stav faktury nebo účtu v systému MyInvois je zobrazen ve sloupci :guilabel:`Stav MyInvois`.
v záložce MyInvois.

 - :guilabel:„Validace v procesu“: validace probíhá na straně MyInvois. Modrá
:guilabel:`Zpracování“ také zobrazuje banner.
 - :guilabel:`Platné“: je ověřeno systémem MyInvois. :guilabel:`Číslo podání“,
:guilabel:`MyInvois“ a „Čas ověření“ jsou automaticky aktualizovány informacemi
z MyInvoice.

.. poznámka::
Odoo automaticky kontroluje a aktualizuje <../../sales/subscriptions/scheduled_actions>.
aktualizovat stav každou hodinu. Chcete-li jej aktualizovat ručně kdykoli, klikněte na tlačítko „Aktualizovat můj stav“.

.._malajsie/moje-vioz/pruvodce/zruseni:

Zrušení faktury
~~~~~~~~~~~~~~~~~~~~

Zaslané faktury lze zrušit do 72 hodin od data platnosti. V tomto případě se otevře
fakturu a klikněte na „Požadavek zrušit“. V okně „Zrušení dokumentu“
Zahrňte zrušení: guilabel:Důvod, pak klikněte na: guilabel:Aktualizovat fakturu.
Stav „Vyžádáno“ je aktualizován na stav „Zrušeno“.

Odeslat kreditní faktury do MyInvoice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Před zasláním kreditní faktury musí být původní faktura úspěšně odeslána do MyInvois.
Pokud tak neučiníte, stav kreditní poznámky se změní na „Neplatný“.

Zatímco Odoo používá jediný dokument „faktura“, MyInvois tyto faktury rozděluje do dvou
typy: „účet kreditu“ a „vrácení peněz“, podle způsobu, jakým jsou vyrovnávány.

- :guilabel:`Faktura MyInvois Credit Note“: Vytváří se při vyrovnání faktury v systému Odoo.
originální faktura.
- :guilabel:`Zálohová faktura MyInvois“: Tato zálohová faktura je vytvářena při vyrovnání zálohové faktury z Odoa.
platbu na základě nové faktury.

.. poznámka::
Pokud se kreditní poznámka vyrovnává pouze částečně před odesláním, stále je
v systému MyInvois je zařazen do kategorie „účetní poznámka“.

.. tip::
Vystavit oba typy faktury za stejný původní doklad:
    - Vytvořte dvě samostatné faktury v Odoo z původní faktury.
    - Pro fakturu MyInvois:guilabel:Refund Note: Registrujte platbu před odesláním.
    - Pro fakturu MyInvois:Při vystavení kreditní faktury se nezaregistruje platba.

.. poznámka::
Stejná logika se vztahuje na platební doklady vytvořené z faktur: pokud jsou vyrovnány s plnou platbou,
pokud se stává „Sebeúčtovanou vratkou“, pak se z kreditní poznámky stane „Vrácenka“; jinak se stává
:guilabel:`Splatná faktura“.

Odeslat pohledávky do MyInvoice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`Vystavte fakturu ze stávajícího daňového dokladu nebo faktury <účetnictví/fakturace/vystavit-fakturu-ze-stavejiciho-daneho-dokladu-nebo-faktury>`
a klikněte na „Odeslat do MyInvoice“. V MyInvoice pak vypadá jako „Dodací list“
vystavené na základě faktury nebo „Selbebilled Debit Note“ od dodavatele.

Přístup k fakturám přes QR kód
---------------------------

Pokud je dokument úspěšně odeslán do MyInvois, přidá se k jeho verzi ve formátu PDF i QR kód.
Při skenování kódu se automaticky otevře ověřený dokument v aplikaci MyInvois.

Pro stažení PDF faktury nebo účtu:

#Klikněte na ikonu „fa-cog“
#Vyberte: guilabel:"Stáhnout"
#Vyberte buď „PDF“ nebo „PDF bez platby“.

.. obrázek: malaysia/myinvois-qr-code.png
:alt:QR kód MyInvois

.. _malajsie/zaměstnanost-hlavní hrdina:

Mzdový systém Employment Hero
=======================

Pokud vaše podnikání již funguje s :doc:`Employment Hero
„<https://www.payroll-hero.com/hr/payroll/payroll_localizations/employment_hero>“, můžete použít náš konektor jako
alternativní řešení pro mzdy.

.. důležité::
Pro konfiguraci API služby Employment Hero pro **Malajsii** použijte
následující hodnotu jako :guilabel:`URL mzdy“: „https://apimy.yourpayroll.io/“.
