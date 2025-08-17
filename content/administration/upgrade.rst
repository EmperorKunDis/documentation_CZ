=======
Upgrade
=======

Aktualizace zahrnuje přesun databáze ze starší verze na novější podporovanou verzi (např. z
Odoo 16.0 do Odoo 18.0). Důležité je pravidelné upgradování, protože každá verze nabízí nové funkce a
opravy chyb, bezpečnostní opravy. Používání verze podporované dokumentací :doc:`<supported_versions>` je
doporučeno. Každá hlavní verze je podporována po dobu tří let.

Při aktualizaci databáze záleží na typu hostingu a verzi použitého Odoa, zda je tato aktualizace **povinná**.

.. záložky::

...... skupina-tab::Odoo Online

      - Pokud je databáze na **větší verzi** (např. 16.0, 17.0, 18.0), je nutné provést aktualizaci
každé dva roky.
      - Pokud je databáze na **menší verzi** (např. 17.1, 17.2, 17.4), je nutné provést upgrad
několik týdnů po vydání další verze. Menší verze jsou obvykle vydávány každé
Dva měsíce.

... skupina-tab:: Odoo.sh

Po třech letech podpory budete mít další dva roky na dokončení
aktualizace. Budete upozorněni, když bude nutná aktualizace.

.. obrázek: upgrade/odoo-sh-message.png
:alt:Pop-up „nepodporovaná verze“ na Odoo.sh.

...... skupina-tab:: Na místě

Můžete zůstat na stejné verzi po neomezeně dlouhou dobu, i když není doporučována.
Menší je rozdíl mezi verzemi, tím snadnější by mělo být upgradování.

.. spoiler::Automatické aktualizace: proces Rolling Release společnosti Odoo Online

O několik týdnů předem vám přijde oznámení ve vaší databázi, že je nutné provést povinnou aktualizaci.
je automaticky provedeno. Máte kontrolu nad procesem, dokud termín není splněn.
Dosáhla.

.... obrázek: upgrade/rr-upgrade-message.png
:alt:Výzva k upgradu na horním pravém okraji databáze

Konkrétně tým pro upgrady společnosti Odoo provádí tichý testovací upgrade každé databáze, která by měla být
upgradována. Pokud je test úspěšný a trvá méně než 20 minut, můžete spustit
upgrade databáze. Pokud test nevyjde, můžete zkusit upgradovat pomocí manažera databází
<https://www.odoo.com/my/databases>.

Pokud vás někdo pozve k aktualizaci, je doporučeno požádat o :ref:`aktualizovaný test
Nejprve vytvořte databázi upgrade-request-test a věnujte čas testování :ref:`upgradu <upgrade-testing>`.

Pokud nebudou před uplynutím lhůty pro aktualizaci provedeny žádné kroky, dojde automaticky k upgradu na další verzi.
stanovený termín.

Aktualizace nezahrnuje:

  - Snížení na předchozí verzi Odoo
  - Přechod mezi edicemi („na místě/komunita-do-podnikání“)
Enterprise
  - :ref:`Změna typu hostingu <hosting/change-solution>“ (např. z on-premise na Odoo Online)
  - Migrace z jiného ERP na Odoo

.. varování:
Pokud obsahuje databáze vlastní moduly, nemůže být aktualizována, dokud nebude verze vašich vlastních
moduly je k dispozici pro cílovou verzi Odoo. Pro zákazníky, kteří si udržují vlastní modifikované
moduly doporučujeme paralelizovat procesem: požádejte o upgrade databáze.
<upgrade-request-test> a zároveň upgradujte zdrojový kód vašeho vlastního
moduly </rozvojáři/jak-na-to/aktualizace-vlastní-databáze>.

... upgrade-nutshell:

Upgrade v kostce
=======================

#Požádejte o aktualizaci databáze pro testování (viz:ref:`získání aktualizované databáze
</upgrade-request-test>
#Pokud je to možné, aktualizujte zdrojový kód vašeho vlastního modulu na kompatibilitu s novou
verze Odoo (viz :doc:`/cs/developer/howtos/upgrade_custom_db`).
#Zkontrolovat aktualizovanou databázi.
<testovací-verze>).
#. Pokud narazíte na nějaký problém při testování, napište o tom do Odoa prostřednictvím stránky „Podpora“.
vybrat „Případ související s budoucí aktualizací (testuji aktualizaci)“
<https://www.odoo.com/help?stage=migration>.
#Všechny problémy musí být vyřešeny a uživatel by měl mít jistotu, že aktualizovaná databáze
bez problémů provozujete hlavní databázi, naplánujte aktualizaci produkční databáze.
#Požádejte o aktualizaci produkční databáze, která bude po dobu jejího provádění nedostupná.
dokončit proces (viz odkaz na „aktualizaci výrobní databáze“).
#. Pokud narazíte na nějaký problém při upgradu na Odoo, navštivte stránku „Podpora“ a
vybrat „Případ související s mým upgradem (produkce)“
<https://www.odoo.com/help?stage=post_upgrade>.

.._žádost o upgradu test:

Získání aktualizované databáze testů
===================================

„Stránka upgrade <https://upgrade.odoo.com>“ je hlavní platformou pro žádost o aktualizaci
databáze. V závislosti na typu hostingu však můžete upgradovat přímo z příkazové řádky
(na místě), databázový správce Odoo Online „https://www.odoo.com/my/databases“ nebo vaše
„Projekt Odoo.sh <https://www.odoo.sh/project>“.

.. poznámka::
Platforma Upgrade se řídí stejnou politikou ochrany osobních údajů, jakou má Odoo.
jiných služeb Odoo.com. Navštivte stránku „Obecného nařízení o ochraně osobních údajů“
<https://www.odoo.com/gdpr>

.. záložky::

...... skupina-tab::Odoo Online

Online databáze Odoo lze ručně aktualizovat pomocí nástroje „správce databází“.
<https://www.odoo.com/my/databases>.

Správce databáze zobrazuje všechny databáze spojené s uživatelským účtem.
nebude u nejnovější verze Odoo zobrazena vedle jejich jména ikona šipky v kruhu.
ukazující, že je lze vylepšit.

.. obrázek:: upgrade/databases-page.png
:alt: Správce databáze s tlačítkem pro aktualizaci vedle názvu databáze.

Klikněte na ikonu v podobě šipky v kruhu pro spuštění procesu upgradu. V okně zadejte:

      - Verzi Odoo, kterou chcete upgradovat, obvykle nejnovější verzi.
      - E-mailová adresa, na kterou by měl být odeslán odkaz ke stažení aktualizované databáze
      - Účel upgradu, který je automaticky nastaven na „Test“,
vaše první požadavek na upgrad

.. obrázek: upgrade/upgrade-popup.png
:alt:Okno „Aktualizace databáze“.

Při upgradu je vedle názvu databáze zobrazen štítek :guilabel:`Upgrade in progress`.
dokončení. Jakmile proces úspěšně dokončí, obdržíte e-mail s odkazem na aktualizovaný
databáze je zaslána na uvedenou adresu. Databáze lze také získat přímo ze stránky databáze
klikněte na šipku dolů před názvem databáze.

.. obrázek: upgrade/access-upgraded-db.png
:alt: Kliknutím na šipku v menu se zobrazí aktualizovaná databáze testů.

... skupina-tab:: Odoo.sh

Odoo.sh je integrováno s platformou pro aktualizace, aby bylo možné zjednodušit proces upgradu.

.. obrázek: upgrade/odoo-sh-staging.png
:alt:Projekt Odoo.sh a záložky

Poté je poslána nejnovější denní záloha výroby na platformu Upgrade.

Jakmile je hotová platforma pro aktualizaci, aktualizuje zálohu a nahraje ji na větve.
vloženy do speciálního režimu: pokaždé, když je **přepnutí na novou verzi** provedeno na větvi,
proběhne aktualizace operačního systému a všech vlastních modulů.
vám umožní otestovat vaše vlastní moduly na čisté kopii databáze, která byla aktualizována.
:Soubor s postupem upgradu lze nalézt ve vašem nově aktualizovaném vývojovém prostředí pomocí procházení
:`~/logs/upgrade.log`.

... důležité::
V databázích, kde jsou nainstalovány vlastní moduly, musí být zdrojový kód aktuální.
cílovou verzi Odoo před upgradem lze provést. Pokud nejsou žádné, může být
V režimu „aktualizace závazku“ se přeskočí a aktualizovaná databáze bude postavena hned po
Přenesen z upgradovací platformy a vypnut režim upgradu.

Podrobnější informace najdete na stránce :doc:`/developer/howtos/upgrade_custom_db`.

...... skupina-tab:: Na místě

Standardní proces upgradu lze zahájit vstupem následujícího příkazového řádku na
stroj, na kterém je databáze uložena:

... kódový blok: konzole

$ python <(curl -s https://upgrade.odoo.com/upgrade) test -d <vaše databáze> -t <verze cílového systému>

.. poznámka::
Toto příkaz má nějaké požadavky na prostředí, ve kterém běží:

         - Některé externí příkazy musí poskytnout operační systém a obvykle se nacházejí v
jakýkoliv linuxový distributor (včetně WSL). Pokud se objeví chyba, bude zobrazeno upozornění.
Tyto jsou chybějící.
         - Uživatel systému, který spouští příkaz, musí být nakonfigurován s přístupem k
databáze. Prosím, obraťte se na dokumentaci PostgreSQL o prostředí klienta
<https://www.postgresql.org/docs/current/libpq-envars.html> nebo heslo klienta
souboru <https://www.postgresql.org/docs/current/libpq-pgpass.html> pro tento požadavek.
         - Skript musí být schopen dosáhnout jednoho nebo více serverů upgradovací platformy
a na TCP portu 443 i na libovolném TCP portu v rozsahu mezi 32768 a 60999.
Toto může být v rozporu s vaším omezujícím firewall a bude potřeba přidat výjimku
do konfigurace firewallu.

Pro zobrazení obecného návodu a hlavních příkazů lze použít tento příkaz:

... kódový blok: konzole

$ python <(curl -s https://upgrade.odoo.com/upgrade) --help

Poptat aktualizaci databáze lze také na stránce Upgrade.
<https://upgrade.odoo.com>.

... důležité::
V databázích, kde jsou nainstalovány vlastní moduly, musí být zdrojový kód aktuální.
před upgradováním je třeba provést aktualizaci na cílovou verzi Odoo.
:doc:`/developera/jak-na-to/aktualizace-vlastniho-databazi` pro další informace.

.. poznámka::
         - Z bezpečnostních důvodů může stahovat pouze osoba, která požadavek na aktualizaci podala.
         - Pro účely ukládání je kopie databáze předložena bez souborového systému k upgradu
Server nebyl aktualizován, protože databáze byla vylepšena.
         - Před obnovením aktualizované databáze musí být její úložiště sloučeno s produkcí
filovém skladu, aby bylo možné provádět testy za stejných podmínek jako v nové
verze.
         - Aktualizovaná databáze obsahuje:

           - Soubor „dump.sql“, který obsahuje databázi, která byla aktualizována
           - Soubor „filestore“, který obsahuje soubory extrahované z databázových záznamů
přílohy (jestliže existují), a nové soubory s otevřeným standardem Odoo z cílového Odoo.
verze (např. nové obrázky, ikony, loga platebních poskytovatelů atd.).
To je složka, která se má sloučit s produkčními daty
aby získal plnou verzi upgradovaného souborového systému.

.. poznámka::
Pokud chcete upgradovat vícekrát, můžete požádat o více testovacích databází.

.. poznámka::
Když je požadavek na upgradu dokončen, připojí se k úspěšnému upgradu zpráva o upgradu.
e-mail a stává se dostupným v aplikaci Diskuse pro uživatele, kteří jsou členy „Administrátorů“.
   / Settings" group. This report provides important information about the changes introduced by
nová verze.

..._testování upgradu:

Testování nové verze databáze
=======================================

Je nezbytné otestovat aktualizovanou databázi, abyste se nemohli dostat do situace, kdy
denní činnost změnou názoru, chování nebo varovným hlášením po upgradu
živě.

.. poznámka::
Testovací databáze jsou deaktivovány a některé funkce jsou vypnuty, aby se zabránilo tomu, že by mohly ovlivnit
databáze produkce:

   #V plánovaných akcích není nic aktivní.
   #Výchozí servery jsou vypnuty archivací stávajících serverů a přidáním falešného.
   #Provozovatelé platebních služeb a přepravci jsou vráceni do testovacího prostředí.
   #Synchronizace s bankou je vypnutá. Pokud chcete zkusit synchronizaci, kontaktujte prosím
poskytovatele bankovního synchronizačního nástroje pro získání přihlašovacích údajů do testovacího prostředí.

Testování co nejvíce firemních procesů je silně doporučeno, aby se zjistilo, že jsou
fungovat správně a seznámit se s novou verzí.

.. varování: Seznam základních kontrol

   - Existují názory, které jsou v testovací databázi deaktivované, ale ve výrobní databázi aktivní?
databáze?
   - Zobrazují se vaše obvyklé názory správně?
   - Je správně generován váš report (faktura, objednávka apod.)?
   - Fungují vaše webové stránky správně?
   - Můžete vytvářet a upravovat záznamy (objednávky, faktury, nákupy, uživatelé, kontakty)?
společnosti, apod.
   - Je něco špatně s vašimi šablonami e-mailů?
   - Je nějaký problém s uloženými překlady?
   - Vaše filtry vyhledávání jsou stále přítomny?
   - Můžete si svá data exportovat?

..spoiler::Příklad end-to-end testování

   - Vybrat náhodný produkt ve vašem katalogu produktů a porovnat jeho testovací a výrobní data s
ověřit, že je vše stejné (kategorie produktu, prodejní cena, nákupní cena, dodavatel, účty,
trasy, atd.
   - Koupit tento produkt (Nákupní aplikace).
   - Potvrzení přijetí tohoto produktu (Aplikace skladu).
   - Zkontrolovat, zda je cesta k produktu stejná ve vaší produkční databázi
(Aplikace pro inventář).
   - Prodávat tento produkt (Aplikaci pro prodej) náhodným zákazníkům.
   - Otevřete databázi zákazníků (aplikace Kontakty), vyberte zákazníka (nebo společnost) a zkontrolujte
své data.
   - Dodávka produktu (Aplikace Inventura).
   - Zkontrolovat, zda je trasa pro dodání produktu stejná jako ve vaší databázi výroby.
(Aplikace pro inventář).
   - Potvrzení zákaznického faktury (Aplikace Fakturace nebo Účetnictví).
   - Přičítání faktury (vystavení kreditní poznámky) a kontrola, zda se chová jako ve vaší výrobě
databáze.
   - Kontrola výsledků reportů (Aplikace účetnictví).
   - Náhodně kontrolujte své daně, měny, účty a fiskální rok (Aplikace pro účetnictví).
   - Vytvoření objednávky na webu (aplikace v e-shopu od výběru zboží až po
procesu vyzvednutí a zkontrolovat, zda se chová všechno tak, jak by mělo v produkční databázi.

Tento seznam není **úplný**. Rozšířte příklad na ostatní aplikace podle vašeho používání Odoo.

Pokud narazíte na problém při testování své aktualizované databáze testů, můžete požádat o pomoc
Odoo by se měl vydat na stránku „Podpora“ a vybrat „Problém související s budoucí aktualizací (Jsem)
testování aktualizace)“ <https://www.odoo.com/help?stage=migration>. V každém případě je nutné
v případě, že narazíte na nějaký problém při testování, je nutné jej vyřešit před upgradem produkčního systému.
databáze.

Můžete narazit na významné rozdíly mezi běžnými pohledy, funkcemi, poli a modely.
testování. Tyto změny nelze na případové bázi vracet zpět. Nicméně pokud dojde k nějaké změně
pokud nová verze narušuje vaše úpravy, je za to zodpovědný udržovatel vaší úpravy
modul, který by ho učinil kompatibilním s novou verzí Odoo.

.. tip::
Nezapomeňte si zkontrolovat:

   - Propojení s externím softwarem (EDI, API atd.).
   - Procesy mezi různými aplikacemi (prodej přes internet s e-commerce, konverze vedení klienta až do
objednávka, dodání zboží apod.
   - Export dat
   - Automatické akce
   - Akce serveru v nabídce akcí na formulářích a také při výběru více záznamů
zobrazení seznamu

.._upgrade-production:

Aktualizace databáze produkce
=================================

Jakmile jsou dokončeny testy a vy jste si jisti, že upgrade
databáze může být použita jako hlavní databáze bez problémů, je čas naplánovat den spuštění.

Váš produkční server bude nedostupný během jeho upgradu. Proto doporučujeme naplánovat
v době, kdy je používání databáze minimální.

Jakmile se standardní skripty pro aktualizaci a databáze neustále vyvíjejí, je také doporučeno
často požadovat další aktualizovanou databázi testů, aby se zajistilo, že proces aktualizace stále
úspěšný, zejména pokud trvá dlouho dokončit.**Plně nacvičený proces upgradu
den před aktualizací produkčního databáze je také doporučený.

.. důležité::
Pokud se do výroby pustíte bez předchozích testů, může vám to způsobit:

   - Uživatelé, kteří se neumí přizpůsobit změnám a novým funkcím
   - Ztráta obchodních příležitostí (např. nemožnost ověřit akci)
   - Špatný zákaznický zážitek (např. e-shop, který nefunguje správně)

Proces aktualizace produkčního databáze je podobný jako u testovacího databáze, ale s
pár výjimek.

.. záložky::

...... skupina-tab::Odoo Online

Proces je podobný jako v případě získání upgradované databáze testů.
</upgrade-request-test>, s výjimkou možnosti účelu, která musí být nastavena na
místo :guilabel:`Testování“ použít :guilabel:`Výroba“.

.. varování::
Jakmile bude požadováno upgradování, databáze nebude dostupná až do doby upgradu.
Když je proces dokončený, nelze vrátit se zpět k předchozí verzi.
verze.

... skupina-tab:: Odoo.sh

Proces je podobný jako při získání aktualizované testovací databáze:
větve :guilabel:`Produkce`.

.. obrázek:: upgrade/odoo-sh-prod.png
:alt: Pohled z nabídky Upgrade

Proces je spuštěn, jakmile se udělá nový commit na větvi.
umožňuje synchronizaci procesu upgradu s nasazením vlastních modulů.
aktualizovaný zdrojový kód.
Pokud neexistují žádné vlastní moduly, proces upgradu je spuštěn okamžitě.

... důležité::
Databáze je nefunkční po celou dobu procesu. Pokud se něco pokazí, platfor
Automaticky se vrací zpět na původní verzi, což je stejné jako u běžných aktualizací. V případě úspěchu
vytvoří zálohu databáze před upgradem.

Aby bylo možné dokončit celý proces upgradu, musí být aktualizace vašich vlastních modulů úspěšná.
Ujistěte se, že stav vašeho testovacího upgradu je :guilabel:`úspěšný`, než jej zkusíte v
výrobu. Další informace o tom, jak upgradovat vaše vlastní moduly, najdete na
:doc:`/rozvoj/jak-na-to/aktualizace-vlastniho-databaze`.

...... skupina-tab:: Na místě

Příkaz k přechodu databáze do produkčního režimu je podobný jako příkaz k přechodu na testovací verzi.
databáze s výjimkou argumentu test, který musí být nahrazen produkcí:

... kódový blok: konzole

$ python <(curl -s https://upgrade.odoo.com/upgrade) production -d <vaše databáze> -t <verze cílového systému>

Žádost o aktualizaci produkčního databáze lze podat také prostřednictvím stránky „Aktualizace“
<https://upgrade.odoo.com>.

Jakmile je databáze nahrána, jakákoliv změna ve vaší produkční databázi **nebude**
bude přítomna na vaší aktualizované databázi, proto doporučujeme ji nepoužívat při aktualizaci
procesu.

... důležité::
Když požádáte o aktualizaci databáze pro produkční účely, kopie je předložena bez
a filestore. Proto musí být nový databázový filestore sloučen s produkčním.
souborového uložiště před nasazením nové verze.

Pokud máte problém s produkčním databázovým serverem, můžete požádat o pomoc společnost Odoo prostřednictvím
na stránku „Pomoc“ a vybrat „Problém s aktualizací (produkce)“.
<https://www.odoo.com/help?stage=post_upgrade>

.. upgrade-sla:

Smlouva o úrovni služeb (SLA)
=============================

S verzí Odoo Enterprise je upgrade databáze na nejnovější verzi Odoa zdarma, včetně
jakoukoli podporu, která je potřebná k nápravě případných rozdílů v aktualizované databázi.

Informace o službách upgradu zahrnutých v licenci Enterprise najdete na
„Smlouva o předplatném Odoo Enterprise <upgrade>“. Tato část však jasně vysvětluje, že
služby, které můžete očekávat.

.. upgrade-sla-pokryta:

Upgrade služeb pokrytých SLA
-----------------------------------

Databáze hostované na cloudech Odoo (Odoo Online a Odoo.sh) nebo vlastními prostředky (On-Premise)
mít k dispozici služby upgradu vždy:

- výrazné vylepšení všech základních aplikací;
- aktualizaci všech **vlastních úprav vytvořených pomocí aplikace Studio**, dokud je Studio stále
je nainstalovaná a odpovídající předplatné stále aktivní.
- upgrade všech **vývojů a úprav pokrývaných servisním poplatkem za úpravy
předplatné**.

Upgrade služeb je omezen na technickou konverzi a adaptaci databáze (standard
moduly a data) aby bylo možné provést aktualizaci na verzi, která je cílem upgradu.

.._upgrade-sla-nejsou-pojisteny:

Služby upgrade, které nejsou pokryty smlouvou o úrovni služeb
---------------------------------------

Následující služby související s upgradem nejsou zahrnuty:

- čištění předchozích dat a konfigurací při upgradech.
- upgrade doplňkových modulů, které nejsou pokryty servisní smlouvou
v rámci vlastních nebo třetích stran, včetně partnerů společnosti Odoo.
- školení o nových funkcionalitách a pracovních postupech vylepšené verze.

.. viz též:
   - :doc:`Dokumentace Odoo.sh <odoo_sh>`
   - :doc:`Podporované verze Odoo <supported_versions>`
