=====================
Dokládání faktur
=====================

Pokračující zprávy mohou být odeslány zákazníkům, pokud jsou splátky pozdě. Odoo pomáhá identifikovat pozdní platby
umožňuje plánovat a odesílat vhodná upomínání pomocí **dalších kroků**
podle počtu dní prodlení. Sledování může být zasláno různými způsoby, včetně
e-mail, pošta nebo SMS.

.. viz též:
   - `Tutoriál Odoo: Sledování plateb <https://www.youtube.com/watch?v=50qy2ygS7eM>`_
   - :doc:`/aplikace/finance/účetnictví/fakturace/splatnost faktury“

... účetnictví, sledování a konfigurace:

Konfigurace
=============

Pro konfiguraci „Další kroky“ přejděte na „Účetnictví -> Konfigurace“.
→ Následné úrovně“. V seznamu „Následné úrovně“ je několik následných úrovní a
akce jsou konfigurovány výchozím nastavením.

Pro úpravu následujícího stupně klikněte na záznam. V zobrazení formuláře upravte
:guilabel:"Popis" nebo upravte počet dní před zasláním připomínky. V
Karta „Oznámení“, vyberte možnosti „Akce“ jako „Poslat e-mail“, „Zobrazit zprávu“ apod.
Dopis (<customer_invoices/snailmail>) a odeslat SMS zprávu (<pricing/pricing_and_faq>).

.. poznámka::
Při odesílání dopisů nebo SMS zpráv v Odoo je potřeba :doc:`In-App Purchase (IAP).
</aplikace/základní/v-aplikaci/nákupy-vnitřními-kredity-nebo-tokeny>.

Při odesílání e-mailu nebo dopisu vyberte „Šablonu obsahu“.
Pro úpravu klikněte na ikonku „oi-arrow-right“ (interní odkaz směřující nahoru) vedle
V poli „Šablona obsahu“ pole „Šablona SMS“. Pokud je zapnuto, zprávy používají konkrétní šablonu SMS.
pole, které lze změnit kliknutím na ikonu „Oi-arrow-right“ (interní odkazová šipka).
ikonu.

Další možnosti lze zapnout v sekci „Možnosti“ na úrovni konkrétního sledování:

- Připomínku automaticky spustíte pomocí volby „Automatický“.
- Připomínky k fakturám, které jsou v prodlení.
- :guilabel:`Přidat příznivce“ k odkazovanému zákazníkovi a obdržíte upozornění na každou odpověď e-mailem
udělené na e-mailové upomínce.

V záložce „Aktivita“ zapněte možnost automaticky plánovat aktivity.
při spuštění další úrovně. Vyberte
Zadáte „Uživatel odpovědný za“ a „Typ aktivity“, a zadejte „Shrnutí“.

Pro přidání nového „úrovně sledování“ klikněte na „Nový“ a vyplňte pole.

.. tip::
Zadejte záporné číslo dní, kdy chcete odeslat upomínku před datem splatnosti faktury.

...účetnictví/sledování/fakturace:

Pokračování faktur
==================

.. poznámka::
Před zahájením procesu následného postupu se ujistěte, že jsou všechny transakce v bance vyrovnané.
pro faktury, které byly již zaplaceny.

Pro zobrazení všech neuhrazených faktur přejděte na: „Účetnictví“ - „Zákazníci“ - „Faktury“.
Ve zobrazení „Přehled faktur“ klikněte do vyhledávacího pole a filtrujte podle „Nedoplatky“.

...účetnictví/sledování/sledování pro jednoho zákazníka:

Pokračování pro jednoho zákazníka
---------------------------

Pro podrobné zobrazení stavu fakturace zákazníka přejděte na:
--> Zákazníci --> Zákazníci“. Otevřete formulář zákazníka a klikněte na záložku „Účetnictví“.
sekci „Sledování faktur“, klikněte na různé úrovně pro zobrazení
Stav sledování každého úrovně. Pokud je potřeba nějaké akce, klikněte na „Zpoždění“.
Faktury by měly mít podrobný seznam pohledávek.

Další možnosti nastavení jsou:

- „Poznámky“: Buď „automatické“ nebo „ruční“.
- :guilabel:`Další upozornění“: Datum, do kterého by měly být provedeny další kroky
Je automaticky nastaven při zpracování pokračujících případů a lze jej ručně upravit, pokud je třeba.
- :guilabel:`Zodpovědný“: Uživatel, který provádí následné kroky.

Klikněte na tlačítko „Odeslat“ a vyberte akci
okně „Odeslat a tisknout“:

- :guilabel:`Tisknout``
- :guilabel:`E-mail“
- :label:`SMS“
- :guilabel:`Dopisem“

Zapněte možnost „Připojit faktury“ a změňte šablonu obsahu, pokud je třeba.
Poté klikněte na tlačítko „Odeslat“ nebo „Odeslat a vytisknout“, abyste odeslali :ref:`doplňující zprávu
<účetnictví/doplňující zpráva/doplňující zpráva>.


.. viz též:
:doc:`/aplikace/základní/v-aplikaci-nákupy“

.. poznámka::
   - Kontaktní údaje na faktuře nebo v kontaktním formuláři jsou používány k zaslání upomínky.
   - Chatování uchovává plný záznam všech následných kroků.

...účetní/sledování/sledování pro všechny zákazníky:

Pokračování pro všechny zákazníky, kteří mají něco na srdci
-------------------------------------------

Po založení dalšího :ref:`doplňkového
Možností účetnictví/pokračování/další pokračování pro jednoho zákazníka, přezkoumat, které zákazníky mají
neuhrazené faktury nebo vyžadují další postup. Pro přístup k nim se přihlaste na: „Účetnictví -> Zákazníci ->
Zákazníci. V kartě „Zákazníci“ vyhledejte v poli pro vyhledávání a filtrujte podle
:guilabel:„Překročená splatnost“ nebo „Požaduje další postup“.

Pro všechny relevantní zákazníky provést další kroky, přepnout na seznamový pohled a vybrat
Zákazníci vyžadující další postup. Pak klikněte na ikonu „fa-cog“ a zvolte
„Sledování procesů“ a odeslat jim „Zprávu o pokračování“.
<účetnictví/doplňující zpráva/doplňující zpráva>.

...účetní, kontrolní a zprávy:

Zprávy
=======

...účetnictví, zpětná vazba, zákaznický výkaz:

Výpověď zákazníka
------------------

Pro získání komplexního přehledu o stavu účtu zákazníka klikněte na:guilabel:`Zákazník
Tlačítko „Smart“ na formuláři zákazníka, které odpovídá :ref:`Partner
Část zprávy o účetnictví, fakturách a partnerovi specifická pro daného zákazníka.

K odeslání zákazníkovi klikněte na tlačítko „Odeslat“, změňte e-mailový vzor, pokud je potřeba.
a klikněte na tlačítko „Tisk a odeslání“.

Pro zobrazení výpisů za více zákazníků najednou vyberte zákazníky v
Vyberte pohled „Zákazníci“, klikněte na ikonu „fa-cog“ a vyberte
:guilabel:`Otevřené výpisy z účtu“.

Klikněte na „PDF“ nebo „XLSX“, abyste vytvořili soubor PDF nebo XLSX.

...účetní/doplnění/závěrečný účet:

Doplňující zpráva
----------------

Pro získání kompletního přehledu o splatných fakturách zákazníka je nutné oddělit ty, které jsou splatné od těch,
klikněte na odkaz :ref:`Výpis pro klienta <účetnictví/sledování/vypis-pro-klienta>
Chytrý tlačítko na formuláři zákazníka. Pak klikněte na ikonu „fa-book“ a zvolte „Zákazník
Vyberte „Příloha“ a poté „Doplňující zpráva“.

Pro zobrazení pokračovacího hlášení pro všechny zákazníky najednou přejděte na:
Zprávy --> Partnerský účet. Pak klikněte na ikonu „Kniha“ a vyberte
:guilabel:`Doplňující zpráva“.

Klikněte na „PDF“ nebo „XLSX“, abyste vytvořili soubor PDF nebo XLSX.
