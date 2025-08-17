========
Kolumbie
========

.. |DIAN| nahradit za: zkratka: DIAN (Národní daňová a celní správa)
.. |NIT| nahradit za: zkratka: „NIT (Identifikační číslo pro daňové účely)“

Balíček lokální kolumbijské verze Odoo poskytuje účetní, daňové a právní funkce pro databáze
v Kolumbii – jako například účetní kniha, daně a elektronické faktury. Lokální verze obsahuje
požadavky
<https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/que-requeres-para-factura-electronicamente/>
při používání vlastního softwaru Dian
<https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/como-puedes-facturar-electronicamente/>
řešení s Odoo:

- Zaregistrujte se v RUT
<http://www.dian.gov.co/tramitesservicios/tramites-y-servicios/tributarios/Paginas/RUT.aspx>
s platným číslem DIČ.
- Mít platný digitální podpisový certifikát „schválený ONAC
<https://onac.org.co/directorio-de-acreditados/>`.
- „Registrujte se a aktivujte se
<https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/proceso-de-registro-y-habilitacion-como-facturador-electronico/>
tím, že dokončí certifikační proces požadovaný Dianou.

.. viz též:
   - Pokud chcete získat více informací o tom, jak dokončit proces certifikace modulu |DIAN|, přečtěte si
následující „webovou konferenci <https://www.youtube.com/watch?v=l0G6iDc7NQA>“
   - „Chytrý návod – Lokální kolumbijská verze
<https://www.odoo.com/slides/smart-tutorial-lokalizace-kolumbie-132>`_
   - Dokumentace o zákonnosti a dodržování předpisů v Kolumbii
<../účetnictví/fakturace zákazníkům/elektronická fakturace/kolumbie>

.._lokalizace/kolumbie/konfigurace:

Konfigurace
=============

..._lokalizace/kolumbie/moduly:

Instalace modulů
--------------------

:ref:`Instalujte následující moduly, abyste získali všechny funkce kolumbijského
lokalizace:

.. seznam tabulkový::
:hlavičkové řádky: 1
:šířky: 25 25 50

   * Jméno
     - Technické označení
     - Popis
   * --:guilabel:`Účetnictví v Kolumbii“
     - l10n_co
     - Výchozí:balík fiskální lokace <fiscal_localizations/packages>. Tento modul přidává
základní účetní funkce pro lokalizaci Kolumbie: rozvaha, daně,
srážky a typ identifikačního dokladu.
   * „Daňová evidence pro Kolumbii s DIAN“
     - l10n_co_dian
     - Tento modul obsahuje funkce potřebné pro integraci s DIAN jako samostatnou
software a přidává schopnost vytvářet elektronické faktury a podpůrné dokumenty na základě
|DIAN| předpisy.
   * --:guilabel:`Účetní zprávy Kolumbie“
     - l10n_co_reportuje
     - Modul zahrnuje účetní výkazy pro zasílání certifikátů dodavatelům.
srážky z výplaty.
   * --:guilabel:Daňové doklady pro Kolumbii s Carvajalem
     - l10n_co_edit
     - Tento modul zahrnuje funkce potřebné pro integraci s Carvajalem. Přidává možnost
Vygenerovat elektronické faktury a podpůrné dokumenty na základě DIAN.
   * :- guilabel:Kolumbijská prodejna
     - l10n_co_pos
     - Tento modul obsahuje účtenky pro místní kolumbijskou lokalizaci.

..._lokalizace/kolumbie/konfigurace/firma:

Informace o společnosti
-------------------

Pro konfiguraci informací o společnosti:

#Přihlaste se do kontaktního formuláře vaší společnosti:

   - Přejděte do aplikace „Kontakty“ a vyhledejte svou společnost nebo
   - Přejděte do aplikace „Nastavení“, aktivujte režim vývojáře a
v sekci „Společnosti“, klikněte na „Aktualizovat informace“. Pak zadejte
:guilabel:`Kontaktní údaje“ pole, klikněte na název společnosti.

#Nastavte následující informace:

   - :guilabel:`Název společnosti“.
   - :guilabel:`Adresa“: Zahrnuje :guilabel:`Město“, :guilabel:`Oddělení“ a :guilabel:`PSČ“
kód.
   - Vyberte typ identifikace (NIT,
:guilabel:'Občanský průkaz', :guilabel:'Občanské rejstříky' atd.
:guilabel:`Typ identifikace“ je :guilabel:`NIT“,
:guilabel:`Číslo identifikace“ musí mít na konci „kontrolní číslici“.
předcházejícím pomlčce („-“).

#Přejděte na záložku „Prodej a nákup“ a nakonfigurujte „Daňové informace“:

   - :guilabel:`Povinnosti a odpovědnost“: Vyberte daňovou zodpovědnost společnosti.
(:guilabel:'O-13' Příspěvkový důchodce,
:guilabel:`O-23` Daňový agent, :guilabel:`O-47` Jednoduchý daňový režim
:guilabel:`R-99-PN` (neaplikuje se).
   - :guilabel:„Velký přispěvatel“: Pokud je společnost „Velkým přispěvatelem“, zapněte tuto možnost.
   - Vyberte název daně pro společnost („IVA“,
:guilabel:`INC“, :guilabel:`IVA a INC“ nebo :guilabel:"Nepoužívá se")
   - :guilabel:`Obchodní název“: Pokud společnost používá konkrétní obchodní název a je
uvedené na faktuře.

.. tip::
Data konfigurovaná v sekci „Údaje o fiskální evidenci“ jsou tisknuta na platné faktuře.
PDF zprávy.

..._lokalizace/kolumbie/einvoice-konfigurace:

Elektronické fakturační kvalifikace a prostředí DIAN
-------------------------------------------------------

Konfigurovat uživatelská přihlašovací jména, která se používají k připojení k webové službě DIAN.
V prostředí Diany přejděte na položku „Účetnictví -> Konfigurace -> Nastavení“
Přejděte dolů do sekce „Elektronické fakturace v Kolumbii“. Pak postupujte podle těchto kroků:

#Vyberte „DIAN: Bezplatná služba“ jako poskytovatele „Elektronické fakturace“.
#Nastavte pro příslušné typy dokumentů režimy operací podle :guilabel:`Operační módy`.
(*elektronické faktury* nebo *podpůrné dokumenty*) vytvářené z Odoo. Klikněte
:guilabel:`Přidat řádek“, pak vyplňte pole:

   - :guilabel:`Programový režim“: typ dokumentu, který má být vytvořen s použitím programového režimu.
   - :guilabel:`ID softwaru“: ID generované společností |DIAN| pro konkrétní režim provozu.
   - :guilabel:`Software PIN“: PIN vybraný v konfiguraci režimu provozu v DIAN
portál.
   - :guilabel:`Testovací ID`: testovací ID vygenerované společností |DIAN| po provedeném testu
režim provozu.

#Nastavte dostupné certifikáty k podepisování elektronických dokumentů. Klikněte
:guilabel:`Přidat řádek“, pak vyplňte pole:

   - :guilabel:`Název certifikátu“: název certifikátu.
   - Nahrát certifikát v PEM formátu. V poli „Soukromý klíč“
Zadejte klíč, který se objeví na obrazovce, vyberte existující soukromý klíč nebo vytvořte nový.
tak uveďte klíčové jméno a vyberte možnost „Vytvořit a upravit“. Poté v poli „Vytvořit“ zadejte
Vyberte soubor privátního klíče pomocí „Wizardu pro soukromý klíč“ a nahrajte platný soubor „Key“. Klikněte na „Uložit a zavřít“.

....... obrázek:: kolumbie/dian-kreditní karta-konfigurace.png


#. Konfigurujte prostředí DIAN, elektronické fakturace v rámci DIAN nabízí čtyři různé
|DIAN| prostředí, do kterých se můžete připojit:

   - **Demonstrátor DIANu**: Tento prostředí umožňuje otestovat elektronické fakturační procesy pomocí
demonstrativní digitální certifikát. Soubory se vytváří automaticky a nejsou odesílány
do jakéhokoli prostředí Dian. Každá interní validace může být otestována. Chcete-li ji aktivovat, zaškrtněte
zaškrtávací políčko „Demo režim“.

.. poznámka::
Zaškrtávací políčko „Demo režim“ je skryto, pokud je zaškrtnuto pole „Testování“.
je zaškrtnuto políčko „Environment“.

   - **Certifikační prostředí**: Toto prostředí je užitečné pro úspěšné složení zkoušky
proces a získat stav *Aktivní* pro fakturaci v Odoo. Aby se aktivoval, povolte oba
Vyberte možnost „Testovací prostředí“ a zaškrtněte políčko „Zahájit certifikační proces“.
   - **Testovací prostředí**: Toto prostředí umožňuje simulovat elektronické fakturační toky.
a ověřování v testovacím portálu DIAN. Aktivovat jej lze jen zapnutím :guilabel:`Test
Zaškrtnutím políčka „Environment“.
   - **Provozní prostředí**: Toto prostředí umožňuje generovat platné elektronické dokumenty.
aktivovat ji, deaktivovat obě „Testovací prostředí“ a „Aktivujte
zaškrtávací políčka v procesu certifikace.

.. důležité::
Nepoužívejte v produkčním prostředí režim demo Dian. Tento režim je určen
pouze pro testovací prostředí.

.. poznámka::
Ve vícefiremové databázi může každá společnost mít své vlastní certifikát.

.. viz též:
Pro elektronické fakturační konfigurace pomocí řešení Carvajal se podívejte na následující video:
„Elektronická fakturace – Lokace Kolumbie
<https://www.youtube.com/watch?v=bzweMwTEbfY&list=PL1-aSABtP6ABxZshems3snMjx7bj_7ZsZ&index=3>`.

..._lokalizace/kolumbie/master-data:

Hlavní data
-----------

..._lokalizace/kolumbie/kontakty:

Kontakty
~~~~~~~~

Nastavte následující pole v kontaktním formuláři:

- :guilabel:`Číslo identifikace“ (DPH): Vyberte typ čísla identifikace a zadejte
identifikační číslo. Pokud typ identifikačního čísla je :guilabel:`NIT`, pak identifikace
číslo musí obsahovat kontrolní číslice na konci, předcházející lomítku („-“).
- :ref:`Daňové informační pole <lokalizace/kolumbie/konfigurace/firma>“ v
:guilabel:`Prodej a nákup“ záložka.

.._lokalizace/kolumbie/produkty:

Produkty
~~~~~~~~

Přejděte do sekce „Účetnictví“ - „Zákazníci“ - „Produkty“ a zkontrolujte
buď pole „Kategorie UNSPSC“ (naleznete v záložce „Účetnictví“) nebo
V poli „Vnitřní odkaz“ (v záložce „Obecné informace“) je nastaven vnitřní odkaz.

..._lokalizace/kolumbie/daně:

Daně
~~~~~

Pro vytvoření nebo změnu daní přejděte na: „Účetnictví --> Konfigurace --> Daně“ a vyberte
související daň.

Pokud se v prodejních transakcích objevují produkty s daní, nastavte pole „Typ hodnoty“ na
Karta „Pokročilé možnosti“. Základní daňové typy (ICA, IVA)
Tato konfigurace se používá k zobrazení daně na
faktura.

.. obrázek: kolumbie/dian-daňový-konfigurátor.png
:alt: Specifické daňové konfigurace dle DIAN.

..._lokalizace/kolumbie/co-noviny:

Prodejní knihy
~~~~~~~~~~~~~~

Jakmile DIAN přidělí oficiální pořadí a předponu pro elektronickou fakturaci,
Prodejní deníky související s fakturami musí být aktualizovány v Odoo. Chcete-li tak učinit, přejděte na
a vyberte existující prodejní deník.
nebo vytvořit novou s tlačítkem Create.

Do prodejního deníku zadejte „Název deníku“ a „Typ“, pak nastavte
jedinečné: „Krátký kód“ v záložce „Záznamy“. Pak si nastavte následující
data v záložce „Další nastavení“:

- :guilabel:`Elektronická fakturace“: povolit UBL 2.1 (Kolumbie).
- :guilabel:`Řešení fakturace“: číslo rozhodnutí vydané společnosti prostřednictvím jejich testu
set.
- :guilabel:`Datum schválení“: datum, kdy byla rezoluce schválena.
- :guilabel:`Datum ukončení platnosti rozhodnutí“: datum, kdy vyprší platnost rozhodnutí.
- :guilabel:`Počáteční číslo faktury (minimální)`: první autorizované číslo faktury.
- :guilabel:`Rozsah číslování (maximální)“: Poslední autorizovaná faktura.
- :guilabel:`Technický klíč“: ověřovací klíč získaný ze sady testů portálu DIAN nebo jejich webové stránky
služby v případě produkčního prostředí.

Při konfiguraci databáze pro produkční prostředí
<lokalizace/kolumbie/einvoice-konfigurace>, místo ručního nastavení těchto polí
Klikněte na tlačítko „Znovu načíst konfiguraci DIAN“ pro získání informací o rozlišení DIAN.
z webové služby DIAN.

.. obrázek: kolumbie/nastavit-dian-tlačítko.png
:alt:Tlačítko pro obnovení konfigurace DIAN v denních knihách prodeje.

.. důležité::
   - Krátká adresa a rozlišení časopisu musí odpovídat těm, které obdrželi v DIAN.
z portálu testovací sady nebo z portálu MUISCA.
   - Pořadí faktur a předčíslí faktury musí být podle pokynů v článku
Při vytvoření první faktury je Odoo automaticky přiřazen předpona.
a pokračovat v řazení podle následujících faktur.

.._lokalizace/kolumbie/nákupní deníky:

Knihy nákupů
~~~~~~~~~~~~~~~~~

Jakmile DIAN přidělí oficiální sekvenci a předponu pro podpůrný dokument související s
Dodavatelské faktury a nákupní deníky spojené s jejich podklady musí být aktualizovány.
Odoo. Postup je podobný jako u konfigurace prodejních deníků
<lokalizace/kolumbie/co-noviny>.

.. viz též:
Pro více informací o podpoře dokumentů v deníku pomocí řešení Carvajal, přečtěte si
„Dokument podpory – Lokace v Kolumbii“
<https://www.youtube.com/watch?v=UmYsFcD7xzE&list=PL1-aSABtP6ABxZshems3snMjx7bj_7ZsZ&index=8>

.. _lokalizace/kolumbie/účetní kniha:

Klasifikační schéma
~~~~~~~~~~~~~~~~~

:doc:`Pokladní kniha </applications/finance/accounting/get_started/chart_of_accounts>
je nainstalován automaticky jako součást modulu lokalizace. Účty jsou přiřazeny automaticky v
dani, pohledávky a závazky. Výkaz zisku a ztráty pro Kolumbii
je založena na PUC (Plánu jednotného účetnictví).

.._lokalizace/kolumbie/práce:

Multiměnová
-------------

Oficiální směnný kurz pro Kolumbii poskytuje „Banco de la República
<http://www.dane.gov.co/EstadisticasEconomicas/>`.

Pro automatické aktualizace směnných kurzů postupujte takto:

#Přejděte na „Účetnictví“ -> „Konfigurace“ -> „Nastavení“.
#Přejděte do sekce „Měny“ a zapněte „Automatické měnové kurzy“.
#Zajistěte, aby byl vybrán služba „Banka republiky“ („[CO] Banco de la República“).
#Vyberte interval, ve kterém by měla být směnná hodnota měny automaticky aktualizována.
aktualizovány.

Hlavní průběh práce
==============

..._lokalizace/kolumbie/elektronické faktury:

Elektronické faktury
-------------------

Následující je stručný popis hlavního postupu pro elektronické faktury s kolumbijským
lokalizace:

#Uživatel vytváří fakturu.
#Odoo vytváří právní soubor XML.
#Odoo vygeneruje CUFE (Elektronický kód faktury).
#Odoo zasílá notifikaci do DIAN.
#Systém Dian ověřuje fakturu.
#Systém . |DIAN| buď fakturu přijme, nebo odmítne.
#Odoo vygeneruje fakturu ve formátu PDF s QR kódem.
#Odoo smaže přílohu (obsahující odeslaný XML soubor a výsledek validace v DIAN)
a fiskální platnou PDF do souboru :file:`.zip`.
#Uživatel pošle fakturu (soubor :file: .zip) prostřednictvím Odoo zadavateli.

.._lokalizace/kolumbie/vystavování faktur

Vytváření faktur
~~~~~~~~~~~~~~~~

.. poznámka::
Funkční průběh, který se odehrává před kontrolou faktury, **neovlivňuje** hlavní
změny, které přinesla elektronická fakturace.

Elektronické faktury jsou vytvářeny a odesílány jak DIAN, tak i zákazníkovi. Tyto dokumenty lze
může být vytvořen z objednávky nebo ručně vygenerován. Novou fakturu lze vytvořit kliknutím na
Vyberte „Účetnictví“ -> „Zákazníci“ -> „Faktury“ a vyberte možnost „Vytvořit“.
fakturační formulář, nastavte následující pole:

- :guilabel:`Zákazník`: informace o zákazníkovi.
- :guilabel:`Časopis“: časopis používaný pro elektronické faktury.
- Vyberte typ faktury: Výchozí je „Faktura“.
Je vybrán de Venta`.
- :guilabel:`Řádky faktury“: Uveďte produkty s správnými daněmi.

.. důležité::
Při vytváření prvního daňového dokladu souvisejícího s elektronickou evidencí tržeb je nutné
ručně změnit pořadí faktury na formát DIAN: „Předpona + Pořadové číslo“.

Příkladem je převod řetězce z „SETP/2024/00001“ na „SETP1“.

Po dokončení klikněte na tlačítko „Potvrdit“.

..._lokalizace/kolumbie/zaslat elektronickou fakturu:

Elektronické zasílání faktur
~~~~~~~~~~~~~~~~~~~~~~~~~~

Po potvrzení faktury klikněte
„Tisk a odeslání“. V zobrazeném průvodci si zajistěte zapnutí „DIAN“ a
zaškrtávací políčka „E-mail“ pro odeslání XML do webové služby DIAN a faktury,
Klientské daňové e-mailové adresy a klikněte na tlačítko „Tisk a odeslání“. Pak:

- Vytvoří se XML dokument.
- Vzniká Česko-ukrajinská fakulta ekonomická.
- XML zpracovává DIAN souběžně.
- Pokud je soubor přijat, zobrazí se v chatovací oblasti a e-mail klientovi s
souboru s příponou .zip.

.. obrázek: kolumbie/zip-xml-chatter-kolumbie.png
:alt:Elektronické dokumenty k dispozici v chatovacím okně.

V poli s názvem „DIAN“ se pak zobrazí následující text:

- :guilabel:`Datum podpisu“: datum a čas vytvoření souboru XML.
- :guilabel:`Stav`: Stav získaný v odpovědi DIAN. Pokud byla faktura
Pokud je odmítnuta, můžete zde vidět chybové hlášení.
- :guilabel:Testovací prostředí: Zjistit, zda dokument byl doručen na testovací server Dian
životní prostředí.
- :guilabel:`Proces certifikace“: Zjistit, zda dokument byl zaslán v rámci certifikačního procesu
proces s Dianou.
- :guilabel:`Stáhnout“: Stáhnout odeslaný XML soubor i v případě, že výsledkem bylo
byla zamítnuta.
- :guilabel:`Stáhnout připojený dokument“: Stáhnout soubor s generovaným připojeným dokumentem, který je zahrnut v
přenese klientovi soubor .zip.

.. obrázek: kolumbie/dian-tab-elektronický-dokument.png
:alt:Záznam o dokumentu EDI je k dispozici v záložce DIAN.

..._lokalizace/kolumbie/platební doklady:

Kreditní poznámky
------------

Pro vystavení kreditní faktury je třeba postupovat stejně jako u vystavení faktury.
fakturu, přejděte na: „Účetnictví“ - „Zákazníci“ - „Faktury“. Na faktuře klikněte
Vyberte položku „Přidat fakturu“, a doplňte následující informace:

- :guilabel:`Metoda úvěru“: Vyberte typ metody úvěru.

  - :guilabel:`Částečná náhrada“: Využijte tuto možnost, pokud je částka částečná.
  - :guilabel:`Úplná náhrada“: Vyberte tuto možnost, pokud je kreditní faktura v plné výši.
  - „Úplná náhrada a nový návrh faktury“: Využijte tuto možnost, pokud chcete vrátit celou částku a vystavit novou fakturu.
se samo ověřilo a zkontrolovalo s fakturou. Originální faktura byla vytvořena jako nová kopie.
návrh.

- :guilabel:`Důvod kreditní faktury“: Zadejte důvod pro vystavení kreditní faktury.
- :guilabel:`Datum obratu“: Vyberte, zda chcete pro účetní záznam o kreditním dokladu konkrétní datum nebo
datum záznamu v deníku.
- Vyberte konkrétní časopis: Vyberte časopis pro účetní záznam nebo nechte pole prázdné, pokud
chcete použít stejný deník jako u původní faktury.
- :guilabel:`Datum vrácení peněz“: Pokud jste vybrali konkrétní datum, zvolte datum pro vrácení peněz.

Jakmile bude recenze provedena, klikněte na tlačítko „Zrušit“.

..._lokalizace/kolumbie/hotovostní poznámky:

Debetní poznámky
-----------

Pro vystavení záporného dokladu je postup podobný jako u kreditního dokladu.
Fakturu najdete v sekci „Účetnictví“ - „Zákazníci“ - „Faktury“. Na faktuře klikněte na
Tlačítko „Přidat poznámku k úhradě“ a zadejte následující informace:

- :guilabel:`Důvod“: Zadejte důvod pro vystavení poznámky k účtu.
- Vyberte konkrétní možnosti.
- :guilabel:`Kopírovat řádky“: Vyberte tuto možnost, pokud potřebujete zadat fakturu s identickým číslem.
řádky faktury.
- :guilabel:`Použít konkrétní deník“: Vyberte tiskárnu pro fakturu nebo nechte pole prázdné
pokud chcete použít stejný deník jako v původní faktuře.

Když je hotovo, klikněte na tlačítko „Vytvořit debetní poznámku“.

... _lokalizace/kolumbie/podpora:

Podpora faktur od dodavatelů
---------------------------------

S hlavními daty, přihlašovacími údaji a nákupním deníkem nakonfigurovaným pro podporu dokumentů souvisejících s
faktur od dodavatelů můžete začít používat podporující dokumenty.

Podklady pro fakturaci dodavatelů mohou být vytvořeny z vaší objednávky nebo ručně. Přejděte na
Vyberte položku „Účetnictví“ -> „Dodavatelé“ -> „Faktury“ a vyplňte následující údaje:

- :guilabel:Dodavatel: Zadejte informace o dodavateli.
- :guilabel:`Datum faktury“: Vyberte datum faktury.
- :guilabel:`Časopis“: Vyberte časopis pro podporu dokumentů souvisejících s fakturami dodavatelů.
- :guilabel:`Fakturované řádky“: Uveďte produkty s správnými daněmi.

Jakmile bude tato část prohlížena, klikněte na tlačítko „Potvrdit“. Po potvrzení vytvoříme soubor XML a
byla automaticky zaslána na adresu Carvajala.

..._lokalizace/kolumbie/obecné chyby:

Nejčastější chyby
-------------

Nejčastější chyby při validování XML souborů jsou způsobené chybějícími „master dat
<lokalizace/kolumbie/master-data>. V takovém případě se zobrazí chybová hláška o ověření.
odeslání bylo zablokováno.

Pokud byla faktura odeslána a nastavena jako *Odmítnuto* v DIANu, jsou chybové hlášky viditelné
kliknutím na ikonu „Info kruh“ vedle položky „Stav“.
pole v záložce „DIAN“. Použitím zjištěných chybových kódů je možné provést
řešení, které je třeba aplikovat před opětovným zasláním.

.. obrázek: /kolumbie/chybová_zpráva_odmítnuté_faktury.png
:alt: Příklad chybových hlášení na odmítnutých fakturách.

Po opravě hlavních dat nebo jiných problémů je možné XML znovu zpracovat.
Takže podle zasílání elektronických faktur:
proudění.

..._lokalizace/kolumbie/zprávy:

Finanční výkazy
=================

..._lokalizace/kolumbie/certifikat-ica:

ICA retention certificate
-------------------------------

Tento dokument je certifikací dodavatelům za srážky, které byly provedeny pro kolumbijskou průmyslovou
Daň z přidané hodnoty (DPH). Zpráva je k dispozici pod názvem: „Účetnictví --> Hlášení --->
Výpověď z Kolumbie --> Certifikát o udržení v ICA.

Klikněte na ikonu „fa-cog“ (kolečko) pro zobrazení možností stáhnout soubor ve formátu Excel.
a:kopírovat do dokumentů.

.. obrázek: kolumbie/zadržení-ica-dian.png
:alt: Záznam o udržení v ICA v účetnictví Odoo.

... _lokalizace/kolumbie/doklad-o-dph:

Doklad o zadržení DPH
-------------------------------

Tento výstup vystavuje certifikát o částce sražené od dodavatelů na DPH.
je k dispozici pod položkou „Účetnictví“ -> „Zprávy“ -> „Kolumbijské výkazy“ -> „Certifikát“.
Daň z přidané hodnoty.

Klikněte na ikonu „fa-cog“ (kolečko) pro zobrazení možností stáhnout soubor ve formátu Excel.
a:kopírovat do dokumentů.

.. obrázek: kolumbie/retencni-dph-dian.png
:alt: Daňový doklad o přijetí v Odoo účetnictví.

..._lokalizace/kolumbie/certifikát o zdroji:

Zpětná retence
-------------------------------------

Tento certifikát vystavuje partnerovi za sraženou daň z příjmů ze svého podílu.
je možné najít pod položkou „Účetnictví“ -> „Vykazování“ -> „Kolumbijské výkazy“ -> „Certifikát o
Zadržení v prameni.

Klikněte na ikonu „fa-cog“ (kolečko) pro zobrazení možností stáhnout soubor ve formátu Excel.
a:kopírovat do dokumentů.

.. obrázek: kolumbie/zadržení zdroje diana.png
:alt: Zpráva o držení hotovosti v Odoo účetnictví.
