Zobrazit obsah

==================
Integrace Avataxu
==================

Software pro správu daní společnosti Avalara s názvem *AvaTax* je založen na cloudu. Propojením *AvaTax* s Odoo lze dosáhnout reálného času
a daňové výpočty specifické pro daný region při prodeji, nákupu a fakturaci položek v Odoo.*AvaTax*
Daňový výpočet je podporován pro každou zemi, která je uvedena v seznamu OSN, včetně mezinárodních hranic.
transakcí.

.. důležité::
*AvaTax* je k dispozici pouze pro integraci do databází/firem, které mají pobočky v
Spojené státy, Kanada a Brazílie. To znamená, že fiskální pozice/země databáze může být pouze
bude nastaven na Spojené státy, Kanadu nebo Brazílii. Pro více informací se podívejte sem
dokumentace: :ref:`účetnictví/avatax/daňový stát`.

Systém AvaTax bere v úvahu daňové sazby podle místa pobytu pro každý stát, okres a město.
Přesnost převodu peněz tím, že se budete snažit dodržovat zákony, pravidla, hranice právních území a zvláštní
okolností (např. daňové prázdniny a výjimky z produktů). Firmy, které integrují *AvaTax*
může udržovat kontrolu nad výpočty daní vlastními silami s pomocí této jednoduché :abbr:`API (aplikace
integrovaný rozhraní programování).

.. důležité::
Některé omezení existuje v Odoo při používání AvaTaxu pro výpočet daně:

   - AvaTax používá výchozí adresu společnosti. Chcete-li použít skladovou adresu, zapněte: doc:`Povolit
Nastavení aplikace POS „Pošlete později“ (Ship Later).
   - Daň z přidané hodnoty se nepodporuje. To zahrnuje daně z tabáku a elektronických cigaret, palivové daně a další
konkrétní odvětví.

.. viz též:
Podpora společnosti Avalara: „O AvaTaxu“
<https://community.avalara.com/support/s/document-item?language=cs>

Nainstalujte si Avatax
================

Pro nastavení *AvaTax* je potřeba účet u společnosti Avalara. Pokud takový účet dosud nebyl založen,
připojit se k Avalaru a zakoupit licenci: „Avalar: Pojďme si promluvit
<https://www.avalara.com/us/en/get-started.html>.

.. tip::
Při nastavení účtu si poznamenejte hodnotu *AvaTax* :guilabel:`Account ID`. Budete ji potřebovat při
:ref:`Nastavení Odoo <účetnictví/avatax/přihlašovací údaje>“. V Odoo je toto číslo :guilabel:`API
ID.

Pak vytvořte základní profil společnosti
<https://www.odoo.com/r/2k0>

Vytvořte základní firemní profil
----------------------------

Sbírejte podstatné informace o vašem podnikání pro další krok: místa, kde se vybírá daň.
prodávané produkty a služby (a jejich prodejní místa) a osvobození od daně z přidané hodnoty, pokud je aplikovatelné.
Sledujte dokumentaci společnosti Avalara, jak vytvořit základní profil společnosti:

#„Přidat informace o společnosti
<https://www.odoo.com/r/XZDW>.
#„Řekněte nám, kde společnost vybírá a platí daně
<https://www.odoo.com/r/E6g>.
#„Zkontrolovat jurisdikce a aktivovat společnost
<https://www.odoo.com/r/NIy>.
#„Přidejte další pobočky společnosti pro umístění souborů
<https://www.odoo.com/r/GF4>.
#„Přidejte tržiště do firemního profilu
<https://www.odoo.com/r/QA5>.

... /účetnictví/avatax/vytvořit_kreditní údaje Avalara:

Připojte se k AvaTaxu
-----------------

Po vytvoření základního profilu společnosti v Avalaru se připojte k *AvaTaxu*. Tento krok propojí Odoo a
AvaTax obousměrně.

Přejděte buď do „pískoviště“ (https://sandbox.admin.avalara.com/), nebo do produkčního prostředí
<https://admin.avalara.com/>_ prostředí. To bude záviset na typu účtu Avalara, který používáte.
chce začlenit.

.. viz též:
„Testovací prostředí versus produkční prostředí v Avalaru
<https://knowledge.avalara.com/bundle/fzc1692293626742/page/sandbox-vs-production.html>.

Přihlaste se a vytvořte „Klíč licence“. Přejděte na „Nastavení -> Licence a API“
Klepněte na tlačítko „Vytvořit licenční klíč“.

.. důležité::
Přihlášení do aplikace se zobrazí varování „Pokud je vaše obchodní aplikace propojena s řešením Avalara,
Připojení bude přerušeno, dokud neaktualizujete aplikaci novým licenčním klíčem. Tato akce není možná
se musí zrušit.

Vytvoření nového licenčního klíče přerušuje spojení s existujícími aplikacemi pro podnikání, které používají AvaTax.
integrace. Ujistěte se, že tyto aplikace aktualizujete s novým klíčem licence.

Pokud se jedná o první integraci aplikačního rozhraní.
s AvaTaxem a Odoo, pak klikněte na „Vytvořit klíč licence“.

Pokud je tato klíčová licence navíc, ujistěte se, že předchozí spojení může být přerušeno.
Pro každý z účtů Avalara Sandbox a Production je možné používat jen jeden licenční klíč.

.. varování:
Zkopírujte klíč do bezpečného místa. Je silně doporučeno zálohovat licenční klíč.
budoucí odkaz. Tento klíč **nemůže být získán po opuštění této obrazovky**.

...účetnictví/avatax/konfigurace Odoo:

Konfigurace Odoo
==================

Před použitím AvaTaxu je nutné provést několik dalších konfigurací v Odoo, aby bylo možné provádět výpočty daní.
Jsou vyrobeny přesně.

Zkontrolujte, zda databáze Odoo obsahuje potřebná data. Země se nejprve nastaví v databázi
určuje daňovou pozici a pomáhá AvaTaxu při výpočtu přesných sazeb daně.

.. účetnictví / avatax / daňové země:

Daňový stát
--------------

Chcete-li nastavit „Daňový stát“, přejděte do sekce „Účetní aplikace“ - „Konfigurace“.
--> Nastavení.

.. viz též:
:doc:`../../daňové lokality“

V sekci „Daně“ nastavte vlastnost „Daňový stát“ na „Spojené státy“.
Států“, „Kanada“ nebo „Brazílie“. Pak klikněte na „Uložit“.

Nastavení společnosti
----------------

Všechny společnosti, které podnikají na databázi Odoo, by měly mít uvedenou plnou a kompletní adresu.
Nastavení. Přejděte do aplikace „Nastavení“ a pod položkou „Firmy“.
sekci, zkontrolujte, že je v databázi pouze jedna společnost. Klikněte na tlačítko „Aktualizovat informace“.
otevřít samostatnou stránku pro aktualizaci údajů o společnosti.

Pokud je v databázi více společností, klikněte na tlačítko „Správa společností“.
nahrát seznam firem, ze kterých si můžete vybrat. Aktualizovat informace o konkrétní firmě kliknutím na ni.
soukromá společnost.

Administrátoři databází by měli zajistit, aby se v poli „Ulice...“ a „Ulice2...“ objevily následující hodnoty.
Všechny pole „Město“, „Stát“, „PSČ“ a „Země“ jsou aktualizovány pro
Společnostem.

Tím se zajistí přesné výpočty daně a hladký průběh roční účetní operace.

.. viz též:
   - :doc:`/obecne/spolky`
   - :doc:`../začínáme“

Instalace modulu
-------------------

Následně se ujistěte, že modul Odoo AvaTax je nainstalován. Pro provedení této operace přejděte na
:menu-vyber:Aplikace. V poli :guilabel:Hledat... zadejte avatax a stiskněte
Stiskněte klávesu „Enter“. Následující výsledky se zobrazí:

.. seznam tabulkový::
:hlavičkové řádky: 1
:šířky: 25 25 50

   * Jméno
     - Technické označení
     - Popis
   * :- guilabel:Avatax
     - „účet_s_avatary“
     - Výchozí modul AvaTax. Tento modul přidává základní funkce pro výpočet daně, které jsou součástí aplikace AvaTax.
   * -- :guilabel:`Avatax pro lokalizaci“
     - „account_avatax_geolokalizace“
     - Modul zahrnuje funkce, které jsou potřebné pro integraci *AvaTaxu* do systému geolokace.
v Odoo.
   * -- :guilabel:Avatax pro SO
     - „účet_pro_dani_z_přidané_hodnoty“
     - Zahrnuje informace potřebné k výpočtu daní z prodejů v Odoo.
   * --:guilabel:`Daňový software Avatax pro sklad“
     - „účet_avatax_dph“
     - Zahrnuje výpočet daně v Odoo Inventory.
   * :-:guilabel:`Most mezi Amazonem a Avataxem“
     - `prodej_amazon_avatax`
     - Zahrnuje funkce pro výpočet daní mezi Amazonem a Odoo.
   * :- guilabel:Avatax Brazil
     - l10n_br_avatax
     - Zahrnuje informace pro výpočet daně v brazilské lokalizaci.
   * – :guilabel:Avatax Brazílie pro služby
     - l10n_br_avatax_services
     - Tento modul obsahuje požadované funkce pro výpočet daně z přidané hodnoty za služby v Brazílii.
lokalizace.
   * --:guilabel:`Prodej služeb v Brazílii společností Avatax“
     - „l10n_br_edi_sale_services“
     - Tento modul obsahuje požadované funkce pro výpočet daně z přidané hodnoty při prodeji služeb.
lokalizace pro Brazílii, která zahrnuje elektronickou výměnu dat (EDI).
   * --:guilabel:`Testování SO pro brazilskou AvaTax“
     - „l10n_br_test_avatax_sale“
     - Tento modul obsahuje požadované funkce pro testování objednávek v brazilské lokalizaci.

Klikněte na tlačítko „Instalovat“ v modulu označeném jako Avatax: account_avatax.
Provedením této operace se nainstalují následující moduly:

- :guilabel:`Avatax“: „účet_avatax“
- :label:Avatax pro SO: účet avatax_prodej
- :guilabel:`Avatax pro sklad“: „účet Avatax sklad“

Pokud bude nutné použít AvaTax pro geolokalizaci nebo s Amazon Connectorem, pak je nainstalujte.
moduly jednotlivě kliknutím na „Instalovat“ v „Avatax pro lokalizaci zeměpisné polohy“.
a „Most Amazon/Avatax“.

.. viz též:
Pro lokální specifické pokyny k dani *AvaTax* se podívejte na následující dokumentaci:
<https://www.phpbb.com/documentation/> dokumentace:

   - :doc:`../../fiscal_localizations/brazil`
   - :doc:`../../fiscal_localizations/united_states`

...účetnictví/Avatax/přihlašovací údaje:

Nastavení Odoo AvaTax
--------------------

Pro integraci s AvaTax API do Odoo přejděte na
:menuselection:`Účetnictví aplikace“ -> „Konfigurace“ -> „Nastavení“. V poli :guilabel:`AvaTax“
V sekci „Dani“ jsou umístěny pole pro konfiguraci AvaTaxu.
Do systému se zadávají přihlašovací údaje.

Nejprve zaškrtněte políčko vedle možnosti AvaTax, abyste aktivovali AvaTax.
databáze. Tento způsob je rychlý a pohodlný pro aktivaci a deaktivaci výpočtu daně *AvaTax*.
Odoo databáze.

.. obrázek: avatax/avatax-konfigurační nastavení.png
:align:center
:alt: Konfigurace nastavení AvaTax

... účetnictví/avatax/požadavky:

Předpoklady
~~~~~~~~~~~~~

Nejprve vyberte prostředí :guilabel:`Environment`, ve kterém chce společnost používat *AvaTax*.
nebo buď „Testovací prostor“ nebo „Provoz“.

.. viz též:
Pro pomoc při určení, ve kterém prostředí *AvaTaxu* se má používat (buď v prostředí pro produkci nebo
:guilabel:`Testovací prostředí“ navštivte stránku „Testovací prostředí versus produkční prostředí“.
<https://knowledge.avalara.com/bundle/fzc1692293626742/page/sandbox-vs-production.html>.

Kvalifikace
~~~~~~~~~~~

Nyní se mohou zadat přihlašovací údaje. Hodnotu „*AvaTax*“ :guilabel:„ID účtu“ je nutné vyplnit
„ID API“ a „Klíč licence“ by měly být vyplněny v poli „API“.
Klíčové slovo.

.. důležité::
ID účtu lze najít přihlášením do portálu AvaTax (sandbox)
<https://sandbox.admin.avalara.com/> nebo <https://admin.avalara.com/>) a v
v pravém horním rohu klikněte na počáteční písmena uživatele a :guilabel:`Účet`.
:guilabel:`ID účtu“ je uvedena jako první.

Chcete-li získat klíč licence, podívejte se na tuto dokumentaci:
:ref:`účetnictví/avatax/vytvořit_kreditní_kartu_avalara`.

Do pole „Firma“ zadejte kód společnosti Avalara pro danou firmu.
konfigurována. Pokud není nastavena, interpretuje společnost Avalara tento parametr jako „VÝCHODNÍ“.
je přístupný v portálu pro správu Avalara.

Nejdříve se přihlaste do portálu AvaTax („Sandbox“ https://sandbox.admin.avalara.com/ nebo „Production“ https://production.admin.avalara.com/).
Pak přejděte na „Nastavení“ a „Správa společností“.
Hodnota „Kód společnosti“ se nachází v řádku „Společnost“
Sloupec „Kód společnosti“.

.. obrázek: avatax/sidlo.png
:align:center
:alt:Zvýrazněný kód společnosti Avatax na stránce s podrobnostmi o společnosti.

Možnosti transakce
~~~~~~~~~~~~~~~~~~~

V nastavení Odoo *AvaTax* existují dvě transakční konfigurace, které lze nakonfigurovat:
:guilabel:`Používejte UPC“ a „Provádějte transakce“.

Pokud je zaškrtnutá políčka vedle :guilabel:`UPC`, transakce budou používat univerzální kód
Kódy (UPC) namísto vlastních definovaných kódů od společnosti Avalara. Konzultujte s daňovým poradcem (CPA).
pro konkrétní pokyny.

Pokud je zaškrtnuta políčka „Provádět transakce“, pak se transakce v Odoo
databáze bude zpřístupněna pro reportování v AvaTaxu.

Kontrola adresy
~~~~~~~~~~~~~~~~~~

Funkce „Kontrola adresy“ zajišťuje, že je nastaven nejaktuálnější poštovní standard
na kontakt v Odoo. To je důležité pro přesné výpočty daní pro zákazníky.

.. důležité::
Pouze pro partnery a zákazníky v Severní Americe funguje funkce „Kontrola adresy“.

Dále zaškrtněte políčko vedle pole „Kontrola adresy“ (viz obrázek).

.. důležité::
Pro přesné výpočty daně je nejlepší praxí zadat kompletní adresu kontaktů.
uloženy v databázi. Avšak funkce *AvaTax* může stále fungovat tím, že implementuje pokus o nejlepší snahu
pouze „Země“, „Stát“ a „PSČ“. Tyto jsou
tři povinné položky.

Uložte nastavení, aby se konfigurace zavedla.

.. tip::
Manuálně: Vyberte možnost „Zkontrolovat“ a přejděte do aplikace „Kontakty“.
výběrem kontaktu. Nyní, když byl modul *AvaTax* nakonfigurován na databázi, může uživatel
:guilabel:`Potvrdit“ tlačítko se zobrazí přímo pod :guilabel:`Adresa“.

Klikněte na tlačítko „Potvrdit“ a v okně se objeví pole s názvem „Adresa potvrzená“.
:guilabel:`Původní adresa“ je uvedena. Pokud je „Ověřená adresa“ správnou adresou pro zasílání
adresu pro daňové účely, klikněte na tlačítko „Uložit ověřené“.

.. obrázek: avatax/validate-address.png
:align:center
:alt: Vyskakovací okno pro ověření adresy v Odoo s tlačítkem „Uložit ověřenou“ a „Ověřeno
„Adresa“ vyznačena.

.. varování:
Všechny dosud zadané adresy kontaktů v databázi Odoo budou muset být ověřeny
použitím manuálního ověřovacího procesu popsaného výše. Adresy nejsou automaticky ověřovány, pokud
Při výpočtu daně se však objeví pouze v případě, že byly již dříve zadány.

Test připojení
~~~~~~~~~~~~~~~

Po zadání všech výše uvedených informací do konfigurace AvaTax v Odoo klikněte na tlačítko „Test
připojení. To zajišťuje, že jsou správné :guilabel:ID API a :guilabel:klíč API.
Odoo se propojí s API aplikace AvaTax.

Synchronizační parametry
~~~~~~~~~~~~~~~

Po dokončení konfigurace a nastavení sekce *AvaTax* klikněte na tlačítko „Synchronizovat“.
Parametry tlačítko. Tato akce synchronizuje výjimky z AvaTaxu.

.. účetnictví/avatax/daňové pozice:

Fiskální pozice
---------------

Dále přejděte na: „Účetnictví aplikace“ -> „Konfigurace“ -> „Účetnictví: Daňová evidence“.
Pozice. Automatické mapování daní je uvedeno pod názvem „Pozice“.
(AvaTax`). Klikněte na něj, abyste otevřeli stránku konfigurace daňového postavení AvaTaxu.

Zde zkontrolujte zaškrtnutí políčka „Použít API AvaTax“.

Volitelně zaškrtněte políčko vedle pole s názvem: guilabel:Detect automatically.
pokud bude tato volba zaškrtnuta, pak se automaticky aplikuje tento :guilabel:`Daňový postoj`.
transakce v Odoo.

Povolení volby „Detekovat automaticky“ také umožňuje konkrétní parametry, například „DPH“.
vyžadováno`, :guilabel:`Daňové identifikační číslo cizince`, :guilabel:`Skupina zemí`,
V poli „Stát“ nebo „PSČ“ se objeví možnosti „Státy“ a „Poštovní směrovací číslo“. Vyplněním těchto parametrů se filtruje
:guilabel:`Daňová pozice“ používání. Nechat je prázdné zajistí, že všechny výpočty budou prováděny pomocí
:guilabel:`Daňová pozice“.

.. varování:
Pokud by nebyla zaškrtnuta políčka „Detekovat automaticky“, každý zákazník bude muset
měli nastavenou položku „Daňová pozice“ na záložce „Prodej a nákup“.
záznam kontaktu. Chcete-li tak učinit, přejděte na: „Prodejní aplikace --> Objednávky --> Kontakty“.
:menu_selecetion:Kontakty aplikace --> Kontakty. Pak vyberte zákazníka nebo kontakt, ke kterému chcete nastavit fiskální
na své místo.

Zvolte záložku „Prodej a nákup“ (Guilabel) a přejděte dolů do sekce s označením
:guilabel:`Daňová pozice“. Zadejte hodnotu do pole :guilabel:`Daňová pozice“
pro zákazníka.

.. viz též:
:doc:`fiskální pozice“

Účty Avatax
~~~~~~~~~~~~~~~

Po výběru možnosti zaškrtávacího políčka „Používat AvaTax API“ se zobrazí nová záložka
zobrazí se dvě různá nastavení.

První nastavení je „Účet faktury AvaTax“, zatímco druhé je „AvaTax
Návratový účet“. Ujistěte se, že oba účty jsou nastaveny tak, aby vám usnadnily ukládání záznamů na konci roku. Konzultujte
certifikovaný účetní pro konkrétní rady ohledně nastavení obou účtů.

Klikněte na tlačítko „Uložit“ pro zavedení změn.

Daňová mapa
-----------

Integrace AvaTax je dostupná na prodejních fakturách a daňových dokladech s zahrnutou AvaTax daní.
položka.

.. tip::
Dále je k dispozici záložka „Mapování daní“ a „Mapování účtů“.
:guilabel:`Automatické mapování daní (AvaTax)` daňovou pozici, kde lze také nastavit mapování pro produkty.
může být konfigurována. Chcete-li přistupovat k položkám „Daňové pozice“, přejděte na záložku „Účetnictví“
--> Konfigurace --> Účetnictví: Daňové pozice`.

Mapování kategorií produktů
~~~~~~~~~~~~~~~~~~~~~~~~

Před použitím integrace zadejte do kategorií produktů :guilabel:`kategorii Avataxu`.
Přejděte na:menu-selection: „Skladové aplikace -> Konfigurace -> Kategorie produktů“. Vyberte
kategorii produktu, do které se má přidat :guilabel:`AvaTax Category`. Do kategorie :guilabel:`AvaTax Category`
Vyberte pole, kategorii z nabídky nebo „Hledat více ...“ pro otevření kompletního
seznam možností.

.. obrázek: avatax/avatax-kategorie.png
:align:center
:alt:Specifikujte kategorii AvaTaxu na produktech.

Mapování produktů
~~~~~~~~~~~~~~~

Kategorie mohou být nastaveny také na jednotlivé produkty. Chcete-li nastavit kategorii Avatax
Kategorie „Navigace“ -> „Aplikace Inventář“ --> „Produkty“ --> „Produkt“. Vyberte produkt
Přidat kategorii Avatax. Pod záložkou „Obecné informace“
pravicově extremistické, je pole s názvem „Kategorie Avatax“. Nakonec klikněte na seznam
menu a vyberte kategorii nebo zadejte „Hledat více ...“ pro nalezení té, která není uvedena.

.. poznámka::
Pokud je pro produkt i jeho kategorii nastaveno pole :guilabel:`AvaTax Category`, pak bude
:guilabel:`Kategorie AvaTax“ má přednost.

.. obrázek: avatax/override-avatax-product-category.png
:align:center
:alt:Přeskočit kategorie produktů, pokud je potřeba.

.. důležité::
Vytvoření kategorie AvaTax na produktu nebo v kategorii produktů by mělo být
Pro každý produkt nebo kategorii produktů, podle zvolené trasy.

.. viz též:
   - :doc:`fiskální pozice“
   - :doc:`avatax/avatax_use`
   - :doc:`avatax/avalara_portal`
   - Daňová souladnost v USA: Video Avatax elearning


..toctree::


avatax/avatax_use
avatax/avalara_portal
