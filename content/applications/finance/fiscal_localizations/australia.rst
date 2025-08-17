=========
Australie
=========

Moduly
=======

.. seznam tabulkový::
:šířky: 25 25 50
:hlavičkové řádky: 1

   * Jméno
     - Technické označení
     - Popis
   * Australie - Účetnictví
     - l10n_au
     - Modul účetnictví pro australskou lokalizaci.
je nainstalován automaticky, když se instaluje balíček pro daňové účetnictví Austrálie.
<fiskální lokality/balíčky> je vybrána. Tento modul také nainstaluje :ref:`ABA kreditní
Modul přenosu <australia/aba>.
   * Australské zprávy - účetnictví
     - „l10n_au_reports“
     - Přidává také roční zprávu o zdanitelných platbách (TPAR) a roční zprávu o podnikání
Zpráva o aktivitách (BAS) <australia/bas>. Je automaticky nainstalována při instalaci
:guilabel:`Austrálie“ :ref:`daňové balíčky pro místní úpravu <fiscal_localizations/packages>“.
vybrány.
   * Australie - mzdy
     - „l10n_au_hr_mzdy“
     - Modul základní mzdy pro australskou lokalizaci.
   * Australie - Mzdy a účetnictví
     - „l10n_au_hr_mzdy“
     - Obsahuje potřebné účetní informace pro australské pravidla výplaty mezd a je nainstalován
automaticky, pokud je zapnutá volba „Účetní záznamy“ v sekci „Mzdy“.
   * --:guilabel:Mzdy Employment Hero
     - „l10n_employment_hero“
     - Synchronizuje všechny platby od :ref:`Employment Hero <payroll/l10n_au/employment-hero>`.
s účetními záznamy v Odoo.

.. _australia/accounting:

Účetnictví
==========

Daň z přidané hodnoty
-------------

V Austrálii je standardní sazba DPH 10 %, ale existují různé sazby a
Existují výjimky pro určité druhy zboží a služeb.

.. obrázek: australia/default-taxes.png
:alt:Výchozí sazby DPH

.. poznámka::
Daň z příjmu ovlivňuje:

Daňová mapa
~~~~~~~~~~~

V australské lokalizaci jsou názvy daní součástí samotné sazby daně.
názvosloví. Navzdory vysokému počtu daňových položek definovaných v Odoo
Jejich sazby jsou často podobné (0 % nebo 10 %).

DPH z prodeje
***************

Další sazby DPH dostupné v Odoo jsou uvedeny níže.

.. seznam tabulkový::
:šířky: 20 50 30
:hlavičkové řádky: 1

   * -Jméno GST
     - Popis
     - Štítek na fakturách
   * - DPH ve výši 10 %
     - GST prodej
     - 10 % DPH
   * – 0 % EX
     - GST Free na prodej do zahraničí
     - Nulová daň z přidané hodnoty
   * 0 % F
     - Prodej bez DPH
     - Za výhru neplatíte žádnou daň
   * – 0 % INP
     - Vstupem zdaněné prodeje
     - Nulové procento DPH z prodeje
   * – 100 % Adj
     - Toto je pro nastavení, částky mohou být upraveny tak, aby vyhovovaly vašim potřebám.
     - Daňové úpravy (Prodej)

GST daně z nákupu
******************

Další daň z přidané hodnoty dostupná v Odoo je uvedena níže.

.. seznam tabulkový::
:šířky: 20 50 30
:hlavičkové řádky: 1

   * -Jméno GST
     - Popis
     - Štítek na fakturách
   * - DPH ve výši 10 %
     - Nákupy GST
     - 10 % DPH
   * – 10 % C
     - Kapitálové výdaje
     - Nákupy s kapitálem v hodnotě 10 %
   * – 10 % INP
     - Nákupy pro výdajové účely
     - Nákupy s DPH pro výstupní daňově uznatelné tržby
   * – 10 % PRIV
     - Nákupy pro soukromé použití nebo neodpočitatelné
     - Nákupy pro soukromé účely ve výši 10 %
   * 0 % F
     - Nákupy bez DPH
     - Nulová daň z přidané hodnoty
   * – 0 % TPS
     - Nákup (Daně z dovozu) – Daň zaplacená zvlášť
     - Nulová sazba DPH, platí zvlášť
   * – 100 % JEN
     - DPH pouze na dovoz
     - DPH pouze na dovoz
   * – 100 % Adj
     - Daňové úpravy (Nákupy)
     - Daňové úpravy (Nákupy)
   * – 100 % DGST
     - Zpožděná daň z přidané hodnoty
     - 100 % DGST
   * - Bez ABN
     - Daň sražená pro partnery bez ABN
     - Daň z příjmu pro neplátce DPH
   * PAYGW - W3
     - Jiné částky sražené (včetně jakékoliv částky uvedené v poli W2 nebo W4)
     - Jiné částky sražené na dani (W3)

Varianty
^^^^^^^^

Podniky z některých oborů musí hlásit platby, které poskytly svým dodavatelům.
služby v průběhu finančního roku. Odoo kombinuje použití daně a fiskálních pozic pro vykazování
Tyto platby jsou zaznamenány na :ref:`TPAR <australia/tpar>“.
závazky, dvě varianty hlavní daně z přidané hodnoty jsou v Odoo k dispozici, ale jsou neaktivní.
výchozí.

.. příklad::

Pro daň z přidané hodnoty ve výši 10 % jsou možné tyto varianty:

...... seznamová tabulka::
:šířky: 20 40 20 20
:hlavičkové řádky: 1

      * -Daňové označení
        - Popis
        - Zprávy se dotkly
        - Výchozí stav
      * - DPH ve výši 10 %
        - Výchozí daň z přidané hodnoty ve výši 10 %
        - BAS
        - Aktivní
      * - 10 % DPH TPAR
        - Varianta DPH pro dodavatele s ABN
        - | BAS
|TPAR
        - Neaktivní
      * – 10 % DPH TPAR bez IČ
        - Varianta daně TPAR, pokud dodavatel neposkytl ABN
        - | BAS
|TPAR
        - Neaktivní

Odložená DPH
~~~~~~~~~~~~

Odoo umožňuje společnostem, které využívají „Dodatečný daňový režim zboží a služeb (DGST)“ <https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/rules-for-specific-transactions/international-transactions/deferred-gst?=redirected_deferredGSTscheme>
automatizovat své odložené přirážky DPH.

Konfigurace
*************

Je doporučeno:

- Přejděte do sekce „Účetnictví“ -> „Konfigurace“ -> „Nastavení“ a nastavte „Daňové přiznání“.
Periodicita: měsíčně (BAS měsíčně).
- Vytvořte nový deník, kam uložit všechny odložené položky DPH.
--> Konfigurace --> Záznamy --> Nový“ a vybrat „Různé“.
:guilabel:`Typ` při konfiguraci.

Výchozí daně (100 % DGST, neaktivní výchozí hodnotou) a účet (*21340 Deferred GST Liability*).
jsou k dispozici pro australské společnosti. Zapněte daňovou sazbu přechodem na:
Konfigurace --> Daně. Hledat podle názvu „100 % DPH“ (odstranit výchozí filtr, pokud je přítomen).
(povinné) a klikněte na tlačítko „Aktivovat“ přepínače.

Proud
****

1. Dodávky zboží: objednávka a faktura dodavatele
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Při dovozu zboží ze zahraničí lze nyní odložit povinnost platit DPH pro firmy podléhající DPH
schémat. V objednávce zvolte daň 0 % TPS (daň zaplacená zvlášť).
relevantní řádky objednávky.

.. obrázek: australia/dgst-po-tax.png
:alt:Nastavení sazby DPH na nákupní objednávce

2. Záznam zůstatku DGST na výkazu BAS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Když australská daňová služba (ATO) obdrží elektronickou zprávu o souhrnném dluhu za
systému integrovaného nákladu (ICS), zůstatku DPH odloženém v předchozím měsíci
bude k dispozici na portálu BAS australské daňové správy.

.. důležité::
Odoo zatím automaticky z ATO nevybírá stav DGST, je nutné vložit ručně.
musí být vytvořená pohledávka v Odoo. Doporučujeme použít nový účetní deník pro tento účel
protože odklad bude opakovaný.

Přejděte na záložku „Účetnictví“ -> „Výpisy z účtu“ -> „Nový“. V prvním řádku položky výpisu přidejte
účet „Závazky z DPH“ (21340) a zůstatek neuhrazené DPH.
:guilabel:`Kredit“. Vraťme se k příkladu uvedenému výše, přičemž kreditujeme 2 000 dolarů a ukládáme si.

.. obrázek:: australia/dgst-balance-credit.png
:alt:Vytvoření záznamu s účtem DGST

Vytváří se automaticky vyvažovaná linie a v zápisech správně přiřazují hodnoty.
BAS: „Dani“. Sekce *G11*, *G18*, *7A*, a pouze jsou aktualizovány správně.

.. obrázek: australia/dgst-tax-grids.png
:alt:Účetní záznam s automatickým vyrovnáním a zdaněním v BAS

Po zveřejnění záznamu v deníku se ve zprávě BAS zobrazují správné hodnoty pro každou část.
s odpočtem DGST.

Zprávy
-------

.. _australia/bas:

Oznámení o podnikání (BAS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hlášení BAS je kritickou povinností pro podniky, které jsou zaregistrovány na DPH.
Austrálie. Služba BAS slouží k podávání a odvádění různých daní na ATO. S funkcí BAS v Odoo můžete
Podniky mohou hlásit následující:

- GST
- Srážková daň sražená při výplatě
- DGST

Přejděte na stránku „Účetnictví“ a klikněte na odkaz „Zpráva z účetnictví (AU)“.
sekci „Další operace“.

.. obrázek: australia/bas-report.png
:alt: Příklad zprávy BAS

Základní a daňové částky se vybírají z přednastavené sítě daní (**sazebníku**), která je v systému předdefinována.
Daňový rastr lze také ručně nastavit pro jakýkoliv další speciální případ použití DPH (např. víno).
daň z rovného příjmu) a po jejím nastavení systém automaticky vloží do účetnictví
položky do správné daňové kategorie. To zajišťuje, že zpráva o BAS bude přesná a odráží skutečnost.
Hospodářské činnosti podniku.

.. obrázek: australia/gst-grids.png
:alt: Příklad sítě GST

Kromě části DPH zahrnuje účetní výkaz BAS také složky zálohy na daň z příjmu fyzických osob (W1 až
*W5*, pak „Shrnutí, část 4“). Toto propojení zajišťuje, že všechny srážky z mezd jsou
Daňové odvody jsou přesně zaznamenány a odráženy v hlášení.

.. obrázek:: australia/payg.png
:alt:Příklad srážkové daně a souhrnné vyúčtování BAS

Modul obsahuje v sobě zabudované pravidla, která usnadňují automatické výpočty daní pro typy
W1 až W5. Pro podrobný návod a více informací o výpočtu těchto
daně, viz část :ref:`Mzdy <payroll/l10n_au/payroll>“.

Závěr
*******

Když je čas podat daňové přiznání u ATO, klikněte na „Závěrečný zápis“. Daňové přiznání
doba lze nastavit pod položkou „Účetnictví“ - „Konfigurace“ - „Nastavení“ - „Daň
Časový interval vrácení. Startovací datum časového intervalu vrácení lze také definovat na výstupu
sám o sobě přes tlačítko období (:icon:`fa-calendar` *období* *rok*).

.. viz též:
:doc:`Závěrka za rok <../accounting/reporting/year_end>`

.. poznámka::
Odoo používá čtvrtletí kalendáře namísto australských fiskálních čtvrtletí, což znamená *červenec až
Září je v Odoo Q3.

Před prvním uzavřením vstupu je výchozí účet pro platbu DPH **GST payable account** a **GST
je nutné nastavit pohledávku, objeví se oznámení a uživatele přesměruje na skupiny daní.
konfigurace.

.. obrázek: australia/bas-accounts.png
:alt:Zpráva o daňových skupinách

Jakmile jsou zřízeny účty pro odvedenou DPH a přijatou DPH, BAS vygeneruje přesný
automaticky uzavřený záznam o účetním období, který vyrovnává zůstatek DPH s částkou DPH vyrovnanou.
účet.

Záporný zůstatek DPH na účtu přijaté a vydané je vyrovnán s daní vyrovnanou,
daňová skupina. Výše platby nebo příjmu od ATO lze vyrovnat proti bance
Prohlášení.

.. obrázek: australia/bas-taxes.png
:alt:Zpráva o zaplacení daně

.. důležité::
Zpráva BAS není předložena přímo do ATO, Odoo vám pomůže automaticky vypočítat
potřebné hodnoty v každé sekci s možností provedení kontroly, abyste lépe porozuměli
je za nimi historie. Firmy si mohou tyto hodnoty zkopírovat a vložit na portál ATO.
<https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/how-to-lodge-your-bas>

... australie/tpar:

Roční zpráva o zdanitelných platbách (TPAR)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Odoo umožňuje firmám hlásit platby, které byly provedeny dodavatelům nebo poddodavatelům během finančního roku.
roku. Tento údaj je získán vytvořením **TPARu**. Pokud nejste si jisti, že vaše firma potřebuje tento dokument,
viz stránku „ATO TPAR <https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/taxable-payments-annual-report>“.

Přejděte na záložku „Účetnictví“ - „Zprávy“ - „Daňové odvody“.
Roční zprávy (TPAR).

Konfigurace
*************

Nejprve je nutné přiřadit fiskální pozice svým dodavatelům před tím, než jim zaúčtujete aktualizaci.
TPAR. Chcete-li tak učinit, přejděte na: „Účetnictví“ - „Dodavatelé“ - „Dodavatelé“, vyberte dodavatele.
a nastavte pod záložkou „Nákupy a prodeje“ položku „Daňová pozice“.

... obrázek: australia/tpar-fiscal-positions.png
:alt:Fiskální pozice dodavatele

Na základě zvolené fiskální pozice se na dodavatele aplikuje správné zdanění.
faktury.

.. obrázek: australia/tpar-vendor-bill-tax.png
:alt:DPH dodavatele

TPAR obsahuje následující informace od dodavatelů:

- :label:ABN
- :guilabel:`Celková daň z přidané hodnoty“ (celková daň z přidané hodnoty)
- :guilabel:`Zaplaceno“ (výše částky se zobrazí po označení faktury dodavatele jako zaplacené).
- „Daň sražená“ (zobrazí se, pokud je dodavatel zaregistrován na fiskální pozici s nastavením „
:guilabel:`TPAR bez ABN`)

TPAR lze exportovat do několika formátů: PDF, XLSX a TPAR.

.. australská/výplata:

Příkaz k převodu
-----------------

Příkaz k úhradě je dokument používaný jako důkaz o zaplacení obchodní firmě. V Odoo lze
přístupná po kliknutí na:menu:Účetnictví -> Dodavatelé -> Platby, výběrem platby (platb)
a kliknutím na tlačítko „Tisk - Potvrzení o přijetí platby“.

.. obrázek: australia/transfer.png
:alt: Příklad zprávy o zaslání

..._australia/peppol:

Elektronické fakturace
-----------

Peppol
~~~~~~

Odoo je v souladu s požadavky „Peppol“ v Austrálii
<http://www.peppol.cz/jak-to-funguje/zeme/australie/>_ . Založte své zákazníky a dodavatele
Přejděte do sekce „Účetnictví“ -> „Zákazníci“ nebo „Dodavatelé“.
Výběrem jednoho z nich, kliknutím na záložku „Účetnictví“ a konfigurací
„Elektronické fakturace“ v sekci „Nastavení“.

.. obrázek: australia/partner-einvoicing.png
:alt:Nastavení elektronické fakturace pro dodavatele

.. důležité::
Potvrzení faktury nebo kreditní zprávy pro partnery na síti Peppol stáhne
souladu s XML, který lze ručně nahrát do vaší sítě Peppol. Odoo je v současné době
proces stát se přístupovým bodem pro oblast ANZ.

..._australie/aba:

ABA podává žádost o hromadné platby
----------------------------

Soubor ABA je digitální formát vyvinutý Australskou bankovní asociací.
<http://www.ausbanking.org.au/>_ je určen pro podnikatele, kteří chtějí provádět hromadné platby
pracuje s jedním souborem, který je nahrán z jejich podnikového softwaru.

Hlavním výhodou používání souborů ABA je zlepšení efektivity plateb a shody.
Dosáhla se sjednocením mnoha plateb do jednoho souboru pro hromadné zpracování, které lze
podané všem australským bankám.

Konfigurace
~~~~~~~~~~~~~

Skládané platby
**************

Přejděte na „Účetnictví > Konfigurace > Nastavení“ a zapněte „Blok
Platby.

Bankovní časopis
************

Přejděte na položku „Účetnictví“ – „Konfigurace“ – „Deníky“ a vyberte „Banka“.
Journal. Zadejte číslo účtu, klikněte na „Vytvořit a upravit…“ a vyplňte
následujících polích:

- :guilabel:`Banka“
- :guilabel:`BSB“
- :guilabel:`Majitel účtu“

Poté zapněte přepínač „Poslat peníze“ a klikněte na „Uložit a zavřít“.

.. poznámka::
Použití pole :guilabel:`Měna“ je nepovinné.

Vraťte se na záložku „Záznamy v deníku“ a do pole pod nadpisem „ABA“ zadejte následující údaje.
část:

- :guilabel:`BSB“: do tohoto pole se vkládá kód BSB z účtu.
- :guilabel:„Kód finanční instituce“: oficiální zkratka banky (např.
„WBC“ (pro Westpac).
- :guilabel:`Jméno uživatele“: šestimístné číslo, které vám poskytne vaše banka. Kontaktujte svou banku nebo zkontrolujte
její webové stránky, pokud o nich nevíte.
- :guilabel:`Identifikační číslo APCA“: šestimístné číslo, které vám poskytne vaše banka. Kontaktujte svou banku nebo
Zkontrolujte její webové stránky, pokud o ní nevíte.
- :guilabel:`Zahrnout transakci s vyrovnáváním zůstatku“: Vybráním této možnosti se přidá další
„samostatně vyvážený“ transakční soubor na konec souboru ABA, který některé banky vyžadují.

Bankovní účty zákazníků a dodavatelů
*************************************

Přejděte na položku „Účetnictví“ – „Zákazníci“ nebo „Účetnictví“ – „Zákazníci“.
Dodavatelé --> Dodavatelé a vyberte zákazníka nebo dodavatele. Otevřete záložku „Účetnictví“ a
V sekci „Účty“ klikněte na tlačítko „Přidat řádek“, abyste vyplnili jejich:

- :guilabel:`Číslo účtu“
- :guilabel:`Banka“
- :guilabel:`BSB“
- :guilabel:`Majitel účtu“

Poté zapněte přepínač „Poslat peníze“ a klikněte na „Uložit a zavřít“.

Vytváření souboru ABA
~~~~~~~~~~~~~~~~~~~~~~

Pro vytvoření souboru ABA je potřeba vystavit fakturu dodavateli, potvrdit ji a zajistit, aby měl dodavatel přístup k bankovnictví.
informace je správně nastavená.

Poté klikněte na položku „Zaplatit“ v faktuře dodavatele a vyberte následující pole:

- :guilabel:`Časopis“: :guilabel:`Banka“
- :guilabel:`Způsob platby“: :guilabel:"Převod z účtu ABA"
- :guilabel:`Číslo účtu příjemce“: číslo bankovního účtu dodavatele

Jakmile jsou platby vytvořeny, přejděte na: „Účetnictví“ - „Dodavatelé“ - „Platby“, vyberte
zaplacené částky a klikněte na tlačítko „Vytvořit Batch“. Zkontrolujte všechny informace.
Vyberte a potvrďte „Validovat“. Jakmile je soubor ABA ověřen, je k dispozici v chatu.
vpravo.

Po nahrání souboru do portálu vaší banky se vám zobrazí transakční řádek ABA.
v příštím kole zpracování transakcí. Budete muset provést kontrolu proti souboru transakcí
Platba** v Odoo.

Oborové specifikace
==========================

Starshipit - přepravní služba
-------------------

Starshipit je operátor přepravních služeb, který usnadňuje integraci australských a oceánských přepravců.
kurýři s Odoo. Podívejte se na dokumentaci k Starshipit
<../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/starshipit_shipping> pro
podrobné informace.

.. viz též:
„Webinář o řešení Odoo pro firmy <https://www.youtube.com/watch?v=TcDWnoYLXWg>“

... _australia/buynow_paylater:

Nákup nyní, zaplaťte později
----------------------------

„Kup teď, zaplať později“ je oblíbená platební metoda pro eshopy v Austrálii.
řešení je k dispozici prostřednictvím „Stripe <https://stripe.com/en-au/payments/payment-methods>“ a
„AsiaPay <https://www.asiapay.com.au/payment.html#option>“.

.. viz též:
   - :doc:`Platební služba Stripe <../payment_providers/stripe>`
   - :doc:`Platební brána AsiaPay <../payment_providers/asiapay>`

POS terminály
-------------

Pro zřízení přímého spojení mezi Odoo a terminálem POS v Austrálii je nutné zaplatit pomocí služby **Stripe**.
je nutný terminál. Odoo podporuje platební řešení **EFTPOS** v Austrálii.

.. poznámka::
Je nutné poznamenat, že platební terminál Stripe není pro používání Odoo jako hlavního systému POS nezbytný.
Jedna z nich spočívá v tom, že pokladní musí částku konečné platby ručně vyplnit na terminálu.

.. viz též:
   - :doc:`Platební služba Stripe <../payment_providers/stripe>`
   - :doc:`Platební terminál Stripe <../../sales/point_of_sale/payment_methods/terminals/stripe>`
   - „Dokumentace k terminálu Stripe.com <https://stripe.com/docs/terminal>“
