=========
Intrastat
=========

Intrastat je systém sběru dat a výroby statistik pro zboží obchodované mezi členskými státy Evropské unie.
státy. Shromažďuje údaje o:

- Obchodní transakce s věcmi určenými k použití, spotřebě, investici nebo prodeji včetně vlastnického práva
převod.
- Přeprava zboží bez převodu vlastnického práva (například stěhování zásob nebo přesunutí zboží)
před nebo po výrobě či zpracování, a také po údržbě nebo opravě).
- Vrácení zboží.

.. poznámka::
I když se systém Intrastat nadále používá, termín Intrastat již není užíván.
legislativní akt <http://data.europa.eu/eli/reg/2019/2152/2022-01-01>
*statistiky o obchodu s výrobky mezi členskými státy EU*.

.. viz též:
Eurostat Statistika vysvětlena - Slovník: Intrastat
<https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Heslo:Intrastat>

.. intrastat/obecné nastavení:

Obecná konfigurace
=====================

Zapněte hlášení Intrastatu v sekci „Účetnictví“ -> „Konfigurace“ -> „Nastavení“.
V sekci „Faktury zákazníkům“ zaškrtněte políčko „Intrastat“ a pak
:guilabel:`Uložit“.

.._intrakódy:

Výchozí transakční kódy: faktura a vrácení peněz
---------------------------------------------

Můžete nastavit výchozí kód transakce (:ref:`<intrastat/transaction-code>`):
fakturační a vrácené transakce. Pod položkou „Účetnictví -> Konfigurace -> Nastavení“
Vyberte „Nastavení výchozího kódu transakce faktury“ a/nebo „Nastavení výchozího kódu transakce vrácené platby“.
Kód a poté „Uložit“. Kód se automaticky nastaví na všech příslušných řádcích faktury.

.. _intrastat/kód regionu:

Kód oblasti
-----------

Regionální kód se používá jen v belgických společnostech. V nastavení účtu pod položkou „Účetnictví“ ->
Konfigurace --> Nastavení“, vyberte „Firma Intrastatní oblast“
a pak stiskněte tlačítko „Uložit“.

.. tip::
Pokud máte sklady v různých regionech, můžete definovat kód oblasti na
úroveň každého skladu namísto toho. Chcete-li tak učinit, přejděte na:
Skladové prostory“, vyberte skladovou jednotku, nastavte její „Intrastatní oblast“ a pak „Uložit“.

.. obrázek:: intrastat/sklad-region.png
:align:center
:alt:Přidání oblasti Intrastatu k skladu

.._intrakot:

Konfigurace produktu
=====================

Všechny produkty musí být správně konfigurovány, aby byly zahrnuty v hlášení Intrastat.

.. intrastat/kód komodity:

Komoditní kód
--------------

Komoditní kódy jsou mezinárodně uznávané referenční čísla používané k třídění zboží podle
jejich **přirozenosti**. Intrastat používá „Systém společného jmenovitého katalogu <https://taxation-customs.ec.europa.eu/customs-4/calculation-customs-duties/customs-tariff/combined-nomenclature_en>“.

Chcete-li přidat kód zboží, přejděte na: „Účetnictví --> Zákazníci --> Produkty“ a vyberte
produktu. V záložce „Účetnictví“ nastavte komoditní kód produktu.

.. viz též:
„Národní banka Belgie – Kódy komodit intrastatu“


.._intrakot:

Množství: hmotnost a jednotka doplňující
---------------------------------------

Podle druhu zboží je nutné uvést buď hmotnost výrobku v
kilogramů (bez obalu) nebo doplňkové jednotky produktu, například metr čtvereční („m2“).
zboží („p/st“), litrů („l“) nebo gramů („g“).

Chcete-li přidat hmotnost nebo jednotku doplňkovou, přejděte na:
Produktů a vyberte produkt. V záložce „Účetnictví“ podle druhu zboží
kódový soubor, buď vyplňte hodnotu produktu „Hmotnost“ nebo jeho „Doplňkové jednotky“.

.. intrastat/země původu:

Země původu
-----------------

Chcete-li přidat zemi původu produktu, přejděte na: „Účetnictví - zákazníci - produkty“.
a vyberte produkt. V záložce „Účetnictví“ nastavte „Země původu“.

.. _intrakstat/faktura-pokladní doklad-konfigurace:

Konfigurace faktur a zálohových faktur
================================

Jakmile jsou produkty správně nakonfigurovány, musí být na fakturách a účtech nastaveny některé další možnosti.
Vytváříte.

.._intrakód:

Transakční kód
----------------

Transakční kódy slouží k identifikaci povahy transakce.
Může být nastaven pro transakce faktury a vrácení platby.

Pro nastavení transakčního kódu na řádku faktury vytvořte fakturu nebo účet, klikněte na sloupce
tlačítko výběru, zaškrtněte „Intrastat“ a použijte nově přidanou sloupec „Intrastat“.
vybrat kód transakce.

.. obrázek: intrastat/intrastat-sloupec.png
:align:center
:alt:Přidání sloupce Intrastatu do faktury nebo daňového dokladu

.. viz též:
„Národní banka Belgie – Intrastat: Přeshraniční obchod od ledna 2022
<https://www.nbb.be/dokumenty/dd/one-gate/data/nové_druhy_transakcí_2022_cs.pdf>

.._intrakot:

Partnerský stát
---------------

Partnerem je země dodavatele pro faktury a země zákazníka pro
faktur. Automaticky se doplní podle země, kterou je v kontaktu nastavená.
pole.

Pokud chcete upravit informace o zemi partnera ručně, vytvořte fakturu nebo zálohovou fakturu. Klikněte na „Další informace“.
tabu a vyberte položku „Země Intrastatu“.

.. intrastat/dopravní kód:

Dopravní kód
--------------

Dopravní kód identifikuje předpokládaný způsob přepravy zboží (doručení nebo
přepravu).

Přidat dopravní kód, vytvořit fakturu nebo daňový doklad, přejít na záložku „Další informace“
a vyberte „Dopravní režim Intrastatu“.

.. intrastatní hodnota:

Hodnota zboží
------------------

Hodnota zboží je nezdaněná část celkové ceny (cena x
Kód položky faktury (výše).

.._intrakotace/partner:

Konfigurace partnera
=====================

Dva poli z kontaktního formuláře partnera jsou použity s Intrastatem: :guilabel:`DPH“ a
„Země“. Zemi lze ručně nastavit na
faktura nebo účet.

Vytvořit hlášení Intrastatu
=============================

Vytvořte zprávu kliknutím na: „Účetnictví“ → „Zprávy“ → „Auditní zprávy“.
Intrastat report. Je automaticky vypočítána na základě :ref:`výchozí konfigurace
<intraSTAT/obecné konfigurace> a informace nalezené na :ref:`produktech
<intraSTAT/produktová konfigurace>`, :ref:"faktury a daňové doklady
<intrastat/faktura-záloha-konfigurace> a :ref:`dodavatelé <intrastat/dodavatel>.

Exportujte zprávu jako soubor PDF, XLSX nebo XML a nahrajte ji na svou právní správu.

Každá řádka hlášení odkazuje na jednu řádku faktury a obsahuje následující informace:

- Číslo faktury nebo účtu.
- Systém, který je kód automaticky generovaný podle toho, zda se jedná o fakturu
(dodací list) nebo faktura (příjezd).
- „Země <intrastat/partner-country>“, což je země dodavatele pro příjezdy a
země zákazníka pro zasílání.
- :ref:`Kód transakce <intrastat/transaction-code>“
- Pokud je vaše společnost umístěna v Belgii: „Kód oblasti“
- „Kód komodity“ (viz „Komoditní kód <intrastat/commodity-code>“);
- „Země původu“ (viz „Původní země“);
- :ref:`Partner DPH <intrastat/partner>`;
- „Pravidla pro přepravu <intrastat/transport-code>“
- :doc:`Kód Incotermu <../customer_invoices/incoterms>`;
- Hmotnost (v intrastatu)
- :ref:`Dodatečné jednotky <intrastat/množství>“
- Hodnota <intrastat/value>, která je vždy vyjádřena v eurech, i když původní faktura byla v jiné měně.
účet byl veden v jiné měně.
