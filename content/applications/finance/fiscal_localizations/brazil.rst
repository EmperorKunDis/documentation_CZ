======
Brazílie
======

.. |IAP| nahradit za: zkratka: `IAP (In-app-purchase)`
.. |API| nahradit za: zkratku: API (aplikační rozhraní)
.. |SO| nahradit za:: :abbr:`SO (Prodejní objednávka)`

.. viz též:
Užitečné zdroje pro brazilskou lokalizaci včetně materiálů a videí k zaškolení:

   - Seznam úkolů pro nové uživatele
<https://docs.google.com/document/d/e/2PACX-1vSNYTYVnR_BzvQKL3kn5YdVzPjjHc-WHw_U3udk5tz_dJXo69woj9QrTMinH_siyOX2rLGjvspvc8AF/pub>_.
   - „Seznam videí YouTube – Brazílie (lokalizace)
<https://www.youtube.com/watch?v=u8Uz5_-x01c&list=PL1-aSABtP6ADqexw4YNCbKPmpFggajxlX&index=2>.
   - Seznam videí na YouTube - Návody v portugalštině pro Odoo
<https://www.youtube.com/watch?v=04_5YxNiXzM&list=PL1-aSABtP6ACGOW2UREePGjHQ2Bgdy-UZ&index=3>.
   - Dokumentace o zákonnosti a souladu s předpisy v Brazílii


... /lokalizace/brazil/moduly:

Moduly
=======

Následující moduly související s brazilskou lokalizací jsou k dispozici:

.. seznam tabulkový::
:hlavičkové řádky: 1
:šířky: 25 25 50

   * Jméno
     - Technické označení
     - Popis
   * -- Brazilský účetnictví
     - „l10n_br“
     - Brazilský: fiskální balíček pro místní úřady (<fiscal_localizations/packages>)
Brazilský účetní systém, daně, daňový přiznání, fiskální pozice a dokumenty.
typy identifikace.
   * -- Brazil - Účetní zprávy --
     - „l10n_br_reporty“
     - Účetní zprávy pro Brazílii.
   * – :guilabel:"AvaTax Brazil", :guilabel:"Avatax Brazil Sale" a :guilabel:"Test SOs for
Brazilský Avatax
     - „l10n_br_avatax“, „l10n_br_avatax_sale“ a „l10n_br_test_avatax_sale“.
     - Výpočet DPH pomocí Avalary.
   * :- guilabel:Brazilská účetní EDI
     - „l10n_br_edi“
     - Provádí elektronické fakturace prostřednictvím Avataxu.
   * :- guilabel:Prodám brazilskou účetní EDI
     - „l10n_br_edi_sale“
     - Přidá několik polí do prodejních objednávek, která se přenášejí na fakturu.
   * --:guilabel:`Brazilská účetní elektronická výměna dat pro POS“
     - „l10n_br_edi_pos“
     - Provádí elektronické fakturace prostřednictvím Avataxu na pokladnách.
   * :- guilabel:„Brazilské účetnictví pro elektronickou obchodní výměnu“
     - „l10n_br_edi_webové_stránky_prodej“
     - Umožňuje výpočet daně a elektronickou výměnu dat pro uživatele e-commerce.
   * --:guilabel:`Účetnictví v Brazílii pro skladování“
     - l10n_br_edi_stock
     - Dodatečně doplňuje informace o dodání do NF-e.
   * --:guilabel:Brazílie - Prodej webových stránek
     - „l10n_br_web_prodej“
     - Umožňuje výpočet daně a elektronickou výměnu dat pro uživatele e-commerce.
   * Brazílie - Sale
     - „l10n_br_sales“
     - Prodáváme modifikace pro Brazílii
   * :- guilabel:"Brazílie - Předplatné"
     - l10n_br_sale_subscription
     - Prodej předplatného pro Brazílii

.. poznámka::
Jádro modulů lokální verze je nainstalováno automaticky s lokálním nastavením. Ostatní mohou
je nutné je ručně nainstalovat:doc:`</applications/general/apps_modules>`.

.._lokalizace/brazil/loc-recenze:

Přehled lokalizace
=====================

Brazilská lokalizace zajišťuje soulad s brazilským daňovým a účetním systémem.
směrnice. Obsahuje nástroje pro správu daní, fiskální pozice, výkaznictví a předdefinované
účetní kniha přizpůsobená brazilským standardům.

Brazilské balíčky lokalizace poskytují následující klíčové funkce, které zajišťují soulad s
lokální daňové a účetní předpisy:

- :ref:`Účetní kniha <lokality/brazil/účetní kniha>“: předdefinovaná struktura
podle brazilských účetních standardů
- :ref:`Daně <localizations/brazil/taxes>“: přednastavené sazby daní včetně DPH.
nulové sazby, a volitelné možnosti.
- :doc:`Mzdy </applications/hr/mzdy>`
- :doc:`Zprávy o účetnictví <../accounting/reporting>`

... /lokalizace/brazil/účetní kniha:

Klasifikační schéma
-----------------

V rozvaze (viz dokumentace v části „Účetní kniha“), jsou účty
automaticky na své odpovídající daně a výchozí účet splatný.
příjmových polí.

.. poznámka::
Brazilský systém účetnictví je založen na SPED CoA, který poskytuje základ pro nezbytnou
účty.

... /lokalizace/brazil/daně:

Daně
-----

Daňové záznamy jsou automaticky vytvářeny a konfigurovány při instalaci
Brazilská lokalizace. Avalara používá některé z nich k výpočtu daně z prodeje nebo faktur.

Daň z přidané hodnoty za služby se musí ručně přidat a nakonfigurovat, protože sazba se může lišit v závislosti na
Město, kde je služba nabízena.

.. důležité::
NFS-e nelze vydat na služební poplatky, které byly založeny ručně.
<lokalizace/brazil/fakturace-online>, vypočítává daň pomocí Avalary.

.. varování:
Nebuďte na daních lakomí, protože slouží k výpočtu daně AvaTax. Pokud je smažete, Odoo vytvoří
jejich znovu při použití v faktuře nebo SO, kde se počítají daně pomocí AvaTax.
musí být v nastavení daně změněn v záložce „Definice“ pod položkou
v sekci „Výdej faktur“ a „Výdej vrácených peněz“.

..._lokalizace/brazil/firma-a-kontakty:

Společnost a kontakty
====================

Pro využití všech funkcí této fiskální lokalizace je nutné mít v
:doc:`údaje o společnosti </odborne/obecne/spolecnosti/>“

- :label:Jméno
- :guilabel:`Adresa“ přidat „Město“, „Stát“, „PSČ“
:guilabel:`Země“

  - Do pole „Ulice“ zadejte název ulice, číslo popisné a případně další adresu.
informace.
  - Do pole „Ulice 2“ zadejte čtvrť.

- :guilabel:`Číslo identifikace“: :guilabel:`CNPJ“ nebo :guilabel:`CPF“
- :guilabel:`Daňové identifikační číslo“: spojené s typem identifikace
- :guilabel:`IE“: Státní registrace
- :guilabel:`IM“:Městská registrace
- :guilabel:`Kód SUFRAMA“: Úřad pro volný obchodní zónu v Manaus - pokud je to nutné
- :guilabel:`Telefon“
- :guilabel:`E-mail“

Vyberte záložku „Prodej a nákup“ a v sekci „Daňové informace“ nastavte hodnotu „Fiskální informace“.

   - Přidejte položku „Daňová pozice“ pro AvaTax Brazil.
   - :guilabel:`Daňový režim“: Federální daňový režim
   - :guilabel:`ICMS daňový subjekt“: ukazuje na :guilabel:`ICMS režim“, :guilabel:`Výjimku“.
nebo :guilabel:`Nepoplatník“
   - :guilabel:`Hlavní oborová činnost“

Nastavte následující doplňkové pole:

   - Přidejte položku „Daňová pozice“ pro AvaTax Brazil.
   - :guilabel:`Podrobnosti o COFINS“: :guilabel:`Daňová, nezdanitelná, daňová se sazbou 0 %, osvobozená
Zastaveno
   - :guilabel:`Podrobnosti PIS“ :guilabel:"Daňový, nezdanitelný, daňový sazbou 0 %, osvobozený
Zastaveno
   - :guilabel:`Daňového subjektu“ pokud společnost podléhá DPH nebo ne

.. tip::
Pokud se jedná o zjednodušený režim, musíte nastavit sazbu ICMS. Pro to přejděte na
:menu:"Účetnictví --> Konfigurace --> Nastavení", posuňte se dolů na položku :guilabel:"Daně"
části a nastavte pole „Dodatečný poplatek“ a „Nákupní daň“.
:guilabel:`Výchozí daně“ sekce.

Ta samá konfigurace se vztahuje i na příslušný formulář pro kontakt:
s integrací AvaTax.

.. poznámka::
Vyberte možnost „Společnost“ pro kontakt s daňovým identifikačním číslem (CNPJ) nebo
:guilabel:`Osoba“ pro kontakt s CPF.

... /lokalizace/brazil/avatax-account:

Integrace Avataxu
==================

.. poznámka::
   - Ujistěte se, že nainstalujete :ref:`instalaci <general/install> AvaTax Brazil“ (l10n_br_avatax)
modul.
   - Odoo je certifikovaným partnerem společnosti Avalara v Brazílii.
   - :doc:`Integrace Avalary AvaTax <../accounting/taxes/avatax>` využívá :doc:`Nákupy v aplikaci
(IAPs) k výpočtu daní a správě elektronických dokumentů
(např. :ref:`NF-e <lokality/brazil/faktura-za-zboží>`, :ref:`NFS-e
<lokalizace/brazil/fakturace-elektronických-dokumentů>‘. Každá akce spotřebovává kredity z účtu IAP.
rovnováha <https://iap.odoo.com/iap/in-app-services/819> na počátku. Nové databáze obdrží
500 volných kreditů.

Pro výpočet DPH a zpracování elektronických faktur jsou potřeba následující konfigurace
Jaké jsou potřeba?

- :ref:`Společnost <lokalizace/brazil/spolecnost-a-kontakty>`
- :ref:`Kontakty <lokalizace/brazil/firma-a-kontakty>`
- :ref:`Konfigurace AvaTaxu<localizations/brazil/avatax-credentials>“.
- :ref:`Digitální certifikát A1 <lokalizace/brazil/certificate-upload>“
- :ref:`Daňová mapa <lokalizace/brazil/daňové-pozice>`
- :ref:`Produkty <lokalizace/brazil/produkty>`

... /lokalizace/brazil/avatax-konfigurace:

Konfigurace
-------------

..._lokalizace/brazil/avatax-credentials:

Kvalifikace
~~~~~~~~~~~

:ref:`Zapněte AvaTax v Odoo <účetnictví/avatax/přihlašovací údaje>“ a v „AvaTax Brazílie“.
sekci, přidejte e-mailovou adresu administrátora portálu AvaTax v poli :guilabel:`AvaTax Portal
Zadejte e-mailovou adresu a klikněte na ikonu „fa-plug“ s popiskem „Vytvořit účet“.

.. varování:
Při testování nebo vytváření produkce: guilabel:AvaTax Portal Email
sandbox nebo produkční databáze, použijte skutečnou e-mailovou adresu, protože je potřebná k :ref:`připojení
Avalara (účetnictví/Avatax/předpoklady) a nastavte certifikáty, zda chcete testovat nebo používat
na výrobu.

V Brazílii existují dvě různé verze portálu Avalara.

   - Pro testování: https://portal.sandbox.avalarabrasil.com.br/
   - Jeden pro výrobu: https://portal.avalarabrasil.com.br/

Při vytváření účtu z Odoo vyberte správnou verzi. Kromě toho e-mail, který používáte k přihlášení do
otevřít účet nelze použít k založení dalšího účtu. Uchovejte si :guilabel:`ID API`.
:guilabel:`API klíč“ při vytváření účtu z Odoa.

.... obrázek:brazil/transfer-api-credentials.png
:alt:Přenos přihlašovacích údajů k API.

Po vytvoření účtu z Odoo se přihlaste na portál Avalara a nastavte heslo:

#Přihlaste se na portál „Avalara“ (https://portal.avalarabrasil.com.br/Login/).
#Klikněte na „Můj první přístup“.
#Přidejte e-mailovou adresu používanou v Odoo k vytvoření účtu Avalara/AvaTax a klikněte
:guilabel:`Požádat o heslo“.
#Následně obdržíte e-mail s tokenem a odkazem pro vytvoření hesla. Klikněte na tento odkaz
a vložte token, který chcete přidělit heslu.

.. tip::
Pokud používáte AvaTax v Odoo jen pro výpočet daně, nastavíte heslo nebo přístup do
Portál Avalara je zbytečný. Elektronické fakturace ale vyžadují přístup k
AvaTax je potřeba a certifikát musí být nahrán.
<lokalizace/brazilie/vložení certifikátu>.

.. poznámka::
|API| přístupové údaje lze předat. Tato možnost by měla být používána jen tehdy, pokud uživatelský účet existuje.
Bylo vytvořeno v jiném instanci Odoo a musí být znovu použito.

... /lokalizace/brazil/certifikát-nahrání:

Nahrání certifikátu A1
~~~~~~~~~~~~~~~~~~~~~

Pro vystavování elektronických faktur je nutné nahrát certifikát na portál AvaTax.
<https://portal.avalarabrasil.com.br/Login>.

Certifikát bude v Odoo synchronizován, dokud nebude mít externí identifikační číslo.
Portál AvaTax shoduje bez speciálních znaků s číslem CNPJ a identifikací
číslo (CNPJ) v Odoo odpovídá číslu (CNPJ) v AvaTax.

.. důležité::
Některé městské části vyžadují, aby byl certifikát propojen s portálem města před vystavením
NFS z Odoo.

Pokud se zobrazí chybová hláška města, která říká: guilabel:"Certifikát není propojený
Pro uživatele je nutné tento proces provést v městském portálu.

... /brazil/fiscal-positions:

Fiskální pozice
~~~~~~~~~~~~~~~~

Pro nastavení automatické daňové mapy (Avalara Brazil) viz:
<účetnictví/avatax/daňové pozice>`, zapněte „Detekovat automaticky“ a
Možnosti „Používat rozhraní AvaTax Brazil API“.

.. viz též:
:doc:`Daňová pozice <../účetnictví/daně/daňová_pozice>`

.. /lokalizace/brazil/produkty:

Produkty
~~~~~~~~

Pro použití integrace AvaTax na prodejních objednávkách a fakturách zadejte následující informace do
:guilabel:„Prodej“ v kartě produktu pod sekcí „Účetnictví“.
jakým způsobem bude produkt využíván.

..._lokalizace/brazil/faktura-za-zboží:

Elektronické faktury na dodávky zboží (NF-e)
***************************

.. důležité::
:ref:`Integrace Avalara <lokalizace/brazil/avatax-account>` funguje na základě kreditu.
systém, kde každá interakce s Avalarou spotřebovává jednu kreditní jednotku. Níže jsou uvedeny hlavní
operace spotřebující kredit:

**Aplikace pro obchodníky**

   - Daňové výpočty v cenových nabídkách a objednávkách na prodej.

**Účetní aplikace**

   - Daňové výpočty na fakturách.
   - Elektronická podání faktur (NF-e nebo NFS-e).

**Přechodné operace**: (za každý krok se platí zvlášť)

   - :ref:`Pravopisná oprava (Carta de Correcção) <localizations/brazil/pravopisna-oprava>`
   - :ref:`Zrušení faktury <lokalizace/brazil/zruseni-faktury>`
   - :ref:`Vrácení peněz přes fakturu <localizations/brazil/credit-notes>`
   - :ref:`Prodáváme doplňkové faktury kreditními poznámkami <lokalizace/brazil/credit-notes>`
   - :ref:`Neplatnost rozsahu čísla faktury <localizations/brazil/invoice-number-invalidation>`
   - Další daňová ověření.

.. poznámka::
Pokud se daně vypočítávají v aplikaci **Prodej** a následně je faktura vystavena v
**Účetní aplikace**, kde se výpočet provádí dvakrát a spotřebovává dva kredity.

.. příklad::
| **Potvrzení objednávky**
|:icon:`fa-arrow-down` 1 kredit (daňová výpočet)
| **Vystavená faktura**
|:icon:`fa-arrow-down` 1 kredit (daňová výpočet)
| **Potvrzená a odeslaná faktura**
| :icon:`fa-arrow-down` 1 kredit (daňová kalkulace) + 1 kredit (odeslat fakturu)
| **Celkem: 4 kredity**

- :guilabel:`CEST kód“: daňový klasifikační kód, který identifikuje zboží a výrobky podléhající dani
náhradní plnění podle pravidel ICMS a pomáhá určit příslušnou daňovou úpravu.
pro konkrétní položky. Použitelnost výrobku pro tento požadavek lze ověřit v
  https://www.codigocest.com.br/.
- :guilabel:`Kód produktů společného nomenklaturu Mercosuru“: Mercosur Common Nomenclature Product Code
- :guilabel:`Země původu“: původ produktu, který může být zahraniční nebo domácí, mezi jinými
možné varianty v závislosti na konkrétním případu použití
- :guilabel:`SPED Fiskální produkt typu“: fiskální produktový typ podle tabulky v seznamu SPED
- :guilabel:`Účel použití“: účel použití tohoto produktu

.. poznámka::
Odoo automaticky vytvoří tři produkty, které se použijí pro náklady na dopravu spojené s
přepravu, pojistku a další náklady.
a jsou již nakonfigurované. Pokud je potřeba vytvořit další, zkopírujte a použijte stejnou konfiguraci:

   - :guilabel:`Produkt“ :guilabel:"Služba"
   - :guilabel:`Druh přepravních nákladů“: „Pojištění“, „Přeprava“ nebo
:guilabel:`Další náklady“

..._lokalizace/brazil/služby-elektronických-faktur:

Elektronické faktury za služby (NFS-e)
*******************************

.. důležité::
:ref:`Integrace Avalara <lokalizace/brazil/avatax-account>` funguje na základě kreditu.
systém, kde každá interakce s Avalarou spotřebovává jednu kreditní jednotku. Níže jsou uvedeny hlavní
operace spotřebující kredit:

**Aplikace pro obchodníky**

   - Daňové výpočty v cenových nabídkách a objednávkách na prodej.

**Účetní aplikace**

   - Daňové výpočty na fakturách.
   - Elektronická podání faktur (NF-e nebo NFS-e).
   - Kontrola stavu faktury (za každou kontrolu je odečten 1 kredit).

**Přechodné operace**: (za každý krok se platí zvlášť)

   - :ref:`Pravopisná oprava (Carta de Correcção) <localizations/brazil/pravopisna-oprava>`
   - :ref:`Zrušení faktury <lokalizace/brazil/zruseni-faktury>`
   - :ref:`Vrácení peněz přes fakturu <localizations/brazil/credit-notes>`
   - :ref:`Prodáváme doplňkové faktury kreditními poznámkami <lokalizace/brazil/credit-notes>`
   - :ref:`Neplatnost rozsahu čísla faktury <localizations/brazil/invoice-number-invalidation>`
   - Další daňová ověření.

.. poznámka::
Pokud se daně vypočítávají v aplikaci **Prodej** a faktura je později vystavena v
**Účetní aplikace**, kde se výpočet provádí dvakrát a spotřebovává dva kredity.

.. příklad::
| **Potvrzení objednávky**
|:icon:`fa-arrow-down` 1 kredit (daňová výpočet)
| **Vystavená faktura**
|:icon:`fa-arrow-down` 1 kredit (daňová výpočet)
| **Potvrzená a odeslaná faktura**
| :icon:`fa-arrow-down` 1 kredit (daňová kalkulace) + 1 kredit (odeslat fakturu)
| **Celkem: 4 kredity**

- :guilabel:`Kód produktů společného nomenklaturu Mercosuru“: Mercosur Common Nomenclature Product Code
- :guilabel:`Účel použití“: účel použití tohoto produktu
- :guilabel:`Země původu služby“: Místní kód služeb, kde je poskytovatel registrován
- :guilabel:`Pracovní úkoly“: zaškrtávací políčko pro výběr služby, která zahrnuje práci
- :guilabel:`Druh dopravních nákladů“: typ dopravních nákladů, který chcete vybrat
- :guilabel:`Služby“: Městský kód služby, kde bude služba poskytována; pokud není kód
Přidává se také pole „Země původu služby“ a bude používáno pole „Země původu služby“.

..._lokalizace/brazil/daňová kalkulace:

Daňová výpočet
---------------

.. viz též:
:ref:`Výpočet daně <účetnictví/avatax/vypocet-dane>`

..._lokalizace/brazil/daňové výpočty:

Daňové výpočty v cenových nabídkách a objednávkách
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Zapněte automatické vypočítání daní z cenové nabídky nebo objednávky pomocí AvaTaxu.
jeden z následujících způsobů:

- **Potvrzení citace**
Potvrďte nabídku jako objednávku.
- **Ruční spoušť**
Klikněte na položku „Vypočítat daně pomocí AvaTax“.
- **Představení**
Klikněte na tlačítko „Náhled“.
- **E-mailová nabídka / objednávka**
Odeslat cenovou nabídku nebo objednávku zákazníkovi e-mailem.
- **Přístup k online cenám**
Když zákazník přistupuje k cenové nabídce online (přes portál View), vytvoří se
spustil.

..._lokalizace/brazil/daňové výpočty a faktury:

Daňové výpočty na fakturách
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Zapněte automatické vypočítání daní z faktury zákazníka pomocí AvaTaxu v kterémkoliv
následujícími způsoby:

- **Ruční spoušť**
Klikněte na položku „Vypočítat daně pomocí AvaTax“.
- **Představení**
Klikněte na tlačítko „Náhled“.
- **Přístup k online fakturám**
Když zákazník otevře fakturu online (přes portál View), spustí se |API| volání.

.. poznámka::
Vlastnost „Daňová pozice“ musí být nastavena na „Automatické mapování daní (Avalara Brazílie)“.
Tyto kroky vedou ke snadnému výpočtu daní automaticky.

.. viz též:
:doc:`Daňová pozice (daňové a účetní mapování) <../accounting/taxes/fiscal_positions>`

... /lokalizace/brazilsko/účetnictví:

Účetnictví
==========

..._lokalizace/brazil/elektronické dokumenty:

Elektronické dokumenty
--------------------

... /lokalizace/brazil/časopisy/:

Konfigurace
~~~~~~~~~~~~~

Každá sériová čísla je spojena se specifickým rozsahem čísel pro elektronické faktury.
číslo série na prodejním deníku, přejděte do: „Účetnictví“ -> „Konfigurace“ -> „Deníky“.
a nastavte ji do pole „Série“. Pokud je potřeba více sérií, vytvořte nový prodejní deník
musí být vytvořeny a každé sérii musí být přiřazen nový číslo série.

Zapněte možnost „Používat dokumenty?“; pole „Série“ se bude zobrazovat
pokud je vybrána možnost „Používat dokumenty?“ v záznamníku.

Při vystavování elektronických a neelektronických faktur se pole „Typ“ vybírá z dokumentu.
typ použitý při vystavení faktury.

.. poznámka::
Při vytváření účetního deníku zajistěte pole „Dedikovaná sledovací poznámka“ ve
:guilabel:`Účetní informace“ je nezaškrtnutá, stejně jako v Brazílii, mezi sekcemi
faktury, kreditní a debetní doklady jsou sdíleny podle sériového čísla, což znamená podle deníku.

..._lokalizace/brazil/faktury pro zákazníky:

Faktury zákazníků
~~~~~~~~~~~~~~~~~

Pro zpracování elektronické faktury za zboží (NF-e) nebo služby (NFS-e) musí být faktura potvrzena.
A daň musí být vypočítána společností Avalara, do následujících polí se musí zadat:

- :guilabel:`Zákazník“, s veškerými informacemi o zákaznících
- :guilabel:`Způsob platby: Brazílie“: Uveďte očekávaný způsob platby.
- :guilabel:`Dokumentový typ“: Vyberte „(55) Elektronická faktura (NF-e)“ nebo „(SE)
Elektronická faktura Národní finanční správy (NFS-e`).

:guilabel:„Další informace“ záložka:

- :guilabel:`Daňová pozice“ nastavena na „Automatické mapování daní (Avalara Brazílie)“.

Některé nepovinné pole závisí na povaze transakce. Tyto položky v :guilabel:`Ostatní
Ve většině případů nebudou chybovat ani prázdné položky „Info“.
státu při podání faktury:

- :guilabel:`Model přepravy nákladu“ určuje, jakým způsobem budou zboží plánovány přepravovat – domácí.
- :guilabel:`Přepravce Brazílie“ určuje, kdo přepravu provádí.

Poté klikněte na tlačítko „Odeslat“. V okně „Tisk a odeslání“ klikněte na „Zpracovat“.
elektronickou fakturu a další možnosti, například „Stáhnout“ nebo „E-mail“. Nakonec klikněte
:guilabel:`Odeslat“ k zpracování faktury s vládou.

.. poznámka::
Všechny položky faktury používané k vystavení elektronické faktury jsou také dostupné na
objednávka na prodej, pokud je třeba. Při vytváření první faktury se pole „Číslo dokladu“ zobrazí
zobrazena a přidělena jako první číslo, které bude používáno v pořadí pro další faktury.

..._lokalizace/brazil/platební poznámky:

Kreditní poznámky
~~~~~~~~~~~~

Pokud je potřeba zboží vrátit, lze vytvořit fakturu.
<účetnictví/vystavení kreditní faktury> a předloženy vládě ke schválení.

.. poznámka::
Kreditní poznámky jsou k dispozici pouze pro elektronické faktury na zboží (NF-e).

..._lokalizace/brazil/platební poznámky:

Debetní poznámky
~~~~~~~~~~~

Pokud je potřeba doplnit další informace nebo hodnoty, které nebyly přesně uvedeny v
Originální faktura musí být opravena, vydá se :ref:`pohledávka
<účetnictví/kreditní poznámky/vystavení debetní poznámky>.

.. poznámka::
   - Debetní poznámky jsou dostupné pouze pro elektronické faktury za zboží (NF-e).
   - Do daňového dokladu lze zahrnout pouze produkty uvedené na původní faktuře.
změny lze provést na jednotkové ceně nebo množství produktu, ale produkty **nelze** přidat.
záporný doklad. Účelem tohoto dokumentu je pouze vyjádření částky, která se má přičíst na účet
originální faktura za stejné nebo méně produktů.

..._lokalizace/brazil/faktura-zruseni:

Zrušení faktury
~~~~~~~~~~~~~~~~~~~~

Elektronické faktury, které stát ověřil, lze zrušit.

.. poznámka::
Zkontrolujte, zda elektronická faktura ještě není v lhůtě pro odstoupení, která se může lišit.
podle právních předpisů každého státu.

... /lokalizace/brazil/e-faktura-zboží-nf-e:

Elektronické faktury na dodávky zboží (NF-e)
***************************

Pro zrušení elektronické faktury za dodávku (NF-e) v Odoo klikněte na „Požadavek na zrušení“ a přidejte
Zrušení: důvod v poli „Důvod“ na vyskakovacím okně. Tento důvod pro zrušení je odeslán
Zákazníkovi emailem, zaškrtněte políčko „E-mail“.

.. poznámka::
Jedná se o elektronické zrušení, což znamená, že Odoo pošle žádost vládě
zrušit NF-e. Pak se spotřebuje jedno IAP kredity, protože dojde ke zprávě API.

... /lokalizace/brazil/e-fakturační služby-nf-e:

Elektronické faktury za služby (NFS-e)
*******************************

Pro zrušení elektronické faktury za služby (faktura NFS-e) v Odoo klikněte na tlačítko „Požadavek na zrušení“.
elektronický zrušení proces v tomto případě, protože ne každé město má tuto službu k dispozici.
Uživatel musí tento NFS-e ručně zrušit na webových stránkách města. Jakmile je tento krok dokončen, může
požádat o zrušení v Odoo, což bude fakturu zrušit.

... /lokalizace/brazil/opravni-dopis:

Dopis s opravou
~~~~~~~~~~~~~~~~~

Korekční dopis může být vytvořen a propojen s elektronickou fakturou za zboží (NF-e), kterou
vláda schválila.

V Odoo klikněte na „Opravný list“ a přidejte důvod „Oprava“.
pop-up. K odeslání důvodu k opravě zákazníkovi emailem zapněte :guilabel:`E-mail`.
zaškrtávací políčko.

.. poznámka::
Korektury jsou dostupné pouze pro elektronické faktury za zboží (NF-e).

..._lokalizace/brazil/fakturační číslo:

Zrušení rozsahu čísla faktury
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Soubor pořadí, které je přiřazeno k prodejním deníkům, může zrušit vláda v případě
nejsou v současné době využívány a nebudou využívány ani v budoucnu.
Vyberte položku „Účetnictví“ -> „Konfigurace“ -> „Deníky“, otevřete deník a klikněte na
ikonu „Kolečko“ (ikona „Nástroj“) a vyberte možnost „Zneplatnit číslo“.
Vyberte kartu „Nastavení rozsahu čísla“ a zadejte počáteční číslo.
:guilabel:`Konec čísla“ rozsahu, který má být zrušen, a vložte hodnotu pro zrušení
:guilabel:`Důvod“.

.. poznámka::
   - Zrušení rozsahu čísel faktur je k dispozici pouze pro elektronické faktury za zboží (NF-e).
   - Kniha záznamů časopisu uchovává protokol o zrušených číslech spolu s souborem XML.

... /lokalizace/brazil/faktury dodavatelů:

Faktury dodavatelů
------------

Při přijetí faktury od dodavatele zašifrujte fakturu v Odoo tím, že k ní přidáte všechny obchodní
informace a stejné brazilsky specifické informace zaznamenané na fakturách pro zákazníky.
<lokalizace/brazil/elektronické dokumenty>.

Tyto brazilské specifické pole jsou:

- :guilabel:`Způsob platby: Brazílie“: Uveďte očekávaný způsob platby.
- :guilabel:`Dokumentový typ“: používá výrobce
- :label_guid:Číslo faktury od dodavatele
- :guilabel:`Model přepravy“: **Specifický pro NF-e** jakým způsobem budou zboží přepravovány – vnitrostátně
- :guilabel:`Dodavatel Brazílie“: **specifický pro NF-e**, který zajišťuje přepravu.

... /br/pos:

Pokladna s technologií NFC
===================

NFC-e je právní dokument, který podporuje prodej zboží nebo zboží konečnému zákazníkovi.
elektronického daňového dokladu, tzv. NF-e (<localizations/brazil/e-invoice-goods-nf-e>).
vydávána v formátu XML a má pomocný dokument známý jako „Souhrn NFC-e“ (*NFC-e Summary*).
Elektronický dokument lze vystavit prostřednictvím **Odoo PointofSale**.

Jeho právní platnost je zaručena digitálními podpisy a SEFAZ každého brazilského státu.
Tajemnice financí.

.. důležité::
:ref:`Integrace Avalara <lokalizace/brazil/avatax-account> funguje na kreditní bázi
systému. Každá operace, která zahrnuje komunikaci s Avalarou, spotřebuje jeden kredit.
následující operace v aplikaci POS jsou předmětem úvěru
spotřeba:

   - Daňové přiznání při prodeji
   - Vydávání elektronických faktur (NFC-e)

.. poznámka::
Každý krok je účtován zvlášť. Například výpočet daní a vystavení faktury za
stejná transakce typu POS spotřebuje dvě kreditní body.

.. viz též:
:doc:`Prodejní místo <../../sales/point_of_sale>`

.._lokalizace/brazil/pos-konfigurace:

Konfigurace
-------------

:ref:`Nainstalujte <general/install> Brazilian Accounting EDI for POS` („l10nbr_edi_pos“)
modul a ujistěte se, že aktivujete:doc:`AvaTax <../accounting/taxes/avatax>“.

... /lokalizace/brazil/pos-csc-detail:

Podrobnosti o společnosti CSC
-----------

Přejděte do sekce „Účetnictví“ - „Konfigurace“ - „Nastavení“ a posuňte se na položku „Danie“.
sekci Nastavení NFC-e. V sekci Nastavení NFC-e zadejte následující údaje pro DPH (daňový subjekt)
Políčka pro zadání bezpečnostního kódu:

- :guilabel:`ID CSC“: Identifikátor bezpečnosti daňového poplatníka je buď „ID CSC“ nebo „Token CSC“.
kód, který může mít od 1 do 6 číslic a je k dispozici na oficiálních stránkách státu
Ministerstvo financí (SEFAZ).
- :guilabel:Číslo CSC: Číslo CSC je kód o maximálně 36 znaků, který zná pouze vy a
Finančnímu odboru je známo. Slouží k generování QR kódu NFC-e a zajišťuje
autenticitu DANFE.

.. poznámka::
Informace potřebné pro tyto položky lze získat prostřednictvím webových stránek SEFAZ každé
Brazilské státní podniky účetním společnosti.

..._lokalizace/brazil/pos-produkt:

Konfigurace produktu
---------------------

Přejděte na příslušný produktový formulář v POS, pak
konfigurovat produkt „Brazilské účetnictví“
pole.

.._lokalizace/brazil/pos-shop-konfigurace:

Prodejní místo
-------------

Přejděte na „Prodejní místo“ - „Konfigurace“ - „Nastavení“ a ujistěte se, že jsou nastaveny
Pokladna je vybrána v horní části obrazovky (v konfiguraci pokladny).
Poté přejděte do sekce „Účetnictví“ a nakonfigurujte „Brazilské EDI“.
pole:

- :guilabel:`Série“
- :guilabel:`Další číslo“: další NFC-e číslo v pořadí k vydání, například pokud
Poslední číslo vydané SEFAZ je „100“, *další číslo* bude „101“.

... /lokalizace/brazil/pracovní postupy:

Průběh práce
--------

..._lokalizace/brazil/generovat-nfc-e:

Vytvoření NFC-e
~~~~~~~~~~~~~~~~~~~

Pro vytvoření NFC-e postupujte takto:

#Otevřete příslušný obchod s prodejem a uskutečněte prodej.
#Zkontrolujte platbu a vypočítejte daně, vydávejte NFC-e. Platný NFC-e se zobrazuje na pravé straně
straně obrazovky.

.. obrázek:brazil/l10n-br-nfce-úspěšně-vydané.png
:alt:Úspěšná platba pomocí technologie NFC v obchodním místě.

.. poznámka::
Je také možné vydat NFC-e, které zákazníka identifikuje podle jeho CPF/CNPJ.
takže klikněte na ikonu „uživatel“ (guilabel:„Zákazník“) nebo vyhledejte zákazníka nebo vytvořte nového.

Následující pole jsou povinná pro vydání identifikované karty CPF/CNPJ:

   - :label:Jméno
   - Město a stát, odkud je faktura vystavena
   - :guilabel:`CPF/CNPJ“

#Klikněte na tlačítko „Přijmout“. NFC-e se objeví a zvýrazní číslo klienta na tiskárně.
#Klikněte na tlačítko „Tisk“ nebo „Odeslat e-mailem“, abyste fakturu doručili zákazníkovi.

..._lokalizace/brazil/nfc-e-print:

Tisk jízdenky NFC-e
~~~~~~~~~~~~~~~~~~

Po vytvoření a ověření NFC-e podle příkazu :ref:`<localizations/brazil/generate-nfc-e>` klikněte
:guilabel:`Tisknout“ pro doručení faktury.

.. poznámka::
Funkce Odoo NFC-e je kompatibilní s jakýmkoliv termotiskárnou a nevyžaduje žádné :doc:`Odoo
IoT box <../obecne/iot>.

... /lokalizace/brazil/objednat-s-chybou-NFC-E:

Opětovné vydání PoS s chybou NFC-E
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pokud se vrátí chybová hlášení z NFC-e, postupujte podle následujících kroků:

#Opravte chybu.
#Znovu vydat NFC-e kliknutím na ikonu „fa-bars“ a výběrem
:guilabel:`Objednávky“.
#Filtrujte seznam, zobrazte pouze objednávky s poplatkem a klikněte na „Podrobnosti“. Chyba
Vyobrazení.
#Klikněte na tlačítko „Odeslat NFC“.

.. poznámka::
Pokud je chyba opravena a sezení PoS ukončeno, Odoo zaznamená daňovou korekci.
chvilkové šeptání souvisejícího záznamu v deníku. Záznam o objednávce ukazuje, že
V tomto případě je nutné provést znovu zpracování NFC e.

.. obrázek:brazil/l10n-br-order-error-screen.png
:alt: Formulář pro zobrazení objednávky na prodejním místě.

..._lokalizace/brazil/nfc-e-vraceni-a-zruseni:

NFC-e vrací peníze a ruší rezervace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`Vrácení peněz lze provést přímo v Odoo <pos/refund>`, ale zrušení objednávky musí být provedena
na oficiálním portále vlády.

Když je proces dokončen, vytvoří se schválená návratová NF-e, což znamená, že **předchozí NFC-e
zrušené**.

.. obrázek:brazil/l10n-br-return-succeed.png
:alt:Vrácení zboží schválené NF-e

.. důležité::
SEFAZ umožňuje zrušení NFC-e pouze do **30 minut** od vydání na SEFAZ.
webové stránky. Po uplynutí této doby musí být vrácení peněz provedeno ručně spolu s vydáním
*Vrácení zboží NF-e*.
