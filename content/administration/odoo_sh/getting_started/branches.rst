========
Banky
========

Přehled
========

Zobrazení větví vám poskytne přehled o různých větvích vašeho repozitáře.

.. obrázek: branches/interface-branches.png
:align:center

... _odoosh-gettingstarted-branches-stages:

Stáže
======

Odoo.sh nabízí tři různé fáze pro vaše pobočky: výrobu, testování a vývoj.

Můžete změnit fázi větve tím, že ji přetáhnete do části názvu fáze.

.. obrázek: větve/rozhraní-větve-staging-change.png
:align:center

... scénické zpracování:

Produkce
----------

Toto je větve, která drží kód, na kterém běží vaše produkční databáze.
Může být pouze jedna výrobní větev.

Když do této větve nově přidáte závazný kód,
Vaše produkční servery jsou aktualizovány kódem nové revize a poté znovu spuštěny.

Pokud vaše změny vyžadují aktualizaci modulu (například změna v zobrazení formuláře),
a chcete, aby se automaticky spouštěl.
Zvýšit číslo verze modulu v jeho manifestu (*__manifest__.py*).
Platforma pak zajistí, aby aktualizace proběhla v čase, kdy
Bude dočasně nedostupná z důvodu údržby.


Tento způsob je ekvivalentem upgradu modulu prostřednictvím nabídky Aplikace.
nebo přes příkazový řádek pomocí
:doc:`příkazovou řádku </developer/reference/cli>“.

Pokud změny v závazku zabrání obnovení serveru,
nebo pokud selže aktualizace modulů
server se automaticky vrátí k předchozí úspěšné verzi kódu.
databáze je vrácena do stavu před aktualizací.
Stále máte přístup k protokolu o neúspěšném updatu, takže můžete problém vyřešit.

Demoverze nejsou nahrány, protože se nepoužívají v produkčním databázi.
Jednotkové testy se neprovádějí, protože by zvýšily nedostupnost produkce.
databáze během aktualizace.

Partneři používající testovací projekty by měli být vědomi, že jejich výrobní větve a všechny větve přípravy
automaticky se vrátí do vývojového stádia po 30 dnech.

Režie
-------

Branchy pro testování se používají k ověření nových funkcí s produkčními daty bez ohrožení
skutečnou výrobní databázi s testovacími záznamy. Vytvoří databáze, které jsou neutrální
duplikát kopie produkční databáze.

Zneškodnění zahrnuje:

* Zakázání plánovaných akcí. Pokud chcete zjistit, jak fungují, můžete je spustit ručně nebo
je znovu aktivovat. Uvědomte si, že platforma bude tyto notifikace méně často spouštět, pokud nikdo nebude používat
databáze, aby se ušetřily zdroje.
* Zablokování odchozích e-mailů pomocí mailcatcheru.
:ref:`přístup k e-mailům, které jste poslali<odoosh-gettingstarted-branches-tabs-mails>`.
Protože databáze je k dispozici, nemusíte se starat o zaslání testovacích e-mailů svým kontaktům.
* Nastavit platební a dopravce do režimu testovacího módu.
* Zakázání služeb IAP

Nejnovější databáze bude uchovávána navždy, starší verze z téže větve mohou být vymazány
aby se na ně dostalo nové dřevo. Bude platit tři měsíce a poté budete očekáváni k obnově větve.
Pokud do těchto databází provádíte konfigurační nebo zobrazovací změny, ujistěte se, že je dokumentujete nebo píšete přímo.
V modulích větve pomocí souborů dat XML s přesměrováním výchozí konfigurace nebo pohledů.

Jednotlivé testy se neprovádějí, protože v Odoo aktuálně závisí na demodatových datech, které zatím není možné načíst.
výrobní databáze. V budoucnu, pokud bude Odoo podporovat spouštění jednotek bez demodat
Odoo.sh pak zváží spuštění testů na databázích pro vývojáře.

Rozvoj
-----------

Vývojové větve vytvářejí nové databáze pomocí ukázkových dat, aby mohly spustit jednotkové testy.
Nainstalované moduly jsou ty, které obsahují vaše větve. Můžete změnit tento seznam modulů
nainstalovat do vašich nastavení projektu (viz odoosh-gettingstarted-settings-modules-installation).

Když do jedné z těchto větví přidáte nový příspěvek,
spustí se nový server s databází vytvořenou od začátku a novým revizním stromem.
Demo dat je načteno a testy jednotek se provádějí automaticky.
Tím se ověřuje, že vaše změny nepoškodí žádné z funkcí testovaných nimi. Pokud chcete, můžete
Vypnout testy nebo povolit konkrétní testy s vlastním tagem v nastavení „větve“
<odoosh-gettingstarted-branches-tabs-settings>.

Podobně jako větve staging jsou e-maily zachyceny poštovním krysařem,
Plánované akce nejsou spuštěny, dokud není databáze používána.

Databáze vytvořené pro vývojové větve mají žít zhruba tři dny.
Poté jsou automaticky vymazány a místo jim budou přiděleny nové databáze bez předchozího upozornění.

..._odoosh-gettingstarted-branches-mergingbranches:

Spojení větví
---------------------

Můžete snadno sloučit své větve tím, že je přetáhnete do sebe.

.. obrázek:: interface-branches-merge.png
:align:center

Pokud chcete otestovat změny svých vývojových větví s produkčními daty
Můžete buď:

* sloučit vývojovou větev do vaší testovací větve přetažením na požadovanou testovací větev.
* Přetáhněte vývojovou větev na název sekce pro testování, aby se z ní stal testovací větvený vývoj.

Když jsou vaše poslední změny připraveny k nasazení.
můžete přetáhnout svou testovací větev na produkční větev
sloučit a nasadit do produkce vaše nejnovější funkce.

Pokud jste odvážní.
Můžete sloučit své vývojové větve do svého produkčního větvení.
To znamená, že přeskočíte ověření změn pomocí dat produkce prostřednictvím větve pro testování.

Můžete sloučit své vývojové větve do sebe a své testovací větve do sebe.

Pokud chcete, můžete přímo na svém pracovním stanovišti použít příkaz :code:`git merge`, abyste sloučili své větve.
Odoo.sh bude informován, když do vašich větví budou nové verze pushnuty.

Sloučení vývojového větve do produkční větve slučuje pouze zdrojový kód: Konfigurační změny, které jste provedli ve
stagingová databáze není předána do produkční databáze.

Pokud chcete otestovat změny konfigurace v testovacích verzích a aplikovat je do produkce, musíte buď:

* Psaní změn konfigurace do souborů dat XML
překrývání výchozí konfigurace nebo pohledů větví.
a poté zvýšit verzi vašeho modulu v jeho manifestu (*__manifest__.py*). To spustí aktualizaci modulu.
při sloučení vaší testovací větve do produkční větve.
Toto je nejlepší praxe pro lepší škálovatelnost vašich projektů, protože budete používat funkce verze s Git
aby bylo možné sledovat všechny změny konfigurace a tím pádem i všechny změny provedené v systému.
* Přeneste je ručně ze své testovací databáze do produkční databáze pomocí kopírování a vkládání.

... _odoosh-gettingstarted-branches-tabs:

Karty
====

Historie
-------

Přehled historie vaší pobočky:

* Zprávy o zavedení a jejich autorů
* Různé události spojené s platformou, jako jsou změny scény, importy databází nebo obnovení záloh.

.. obrázek: branches/interface-branches-history.png
:align:center

V pravém horním rohu je zobrazen stav každé události.
Může poskytnout informace o probíhající operaci na databázi (instalace, aktualizace, záloha importu, ...)
nebo jeho výsledek (zpětná vazba testů, úspěšný dovoz zálohy, ...).
Pokud je operace úspěšná, můžete se do databáze přihlásit pomocí tlačítka Connect*.

... _odoosh-gettingstarted-branches-tabs-mails:

E-maily
-----

Tato záložka obsahuje schránku na e-maily, která zobrazuje přehled odeslaných e-mailů z vaší databáze.
Mailcatcher je k dispozici pro vaše vývojářské účely a
stává se, že e-maily vaší produkční databáze jsou skutečně odeslány místo toho, aby byly zachyceny.

.. obrázek:: větve/interface-větve-pošty.png
:align:center
:scale: 50 %

Shell
-----

Přístup k vašemu kontejneru pomocí skořápky. Můžete provádět základní příkazy Linuxu (například :code:`ls` a :code:`top`).
a otevřít skořápku na vaši databázi zadáním příkazu :code:`psql`.

.. obrázek: branches/interface-branches-shell.png
:align:center

Můžete otevřít více záložek a přetáhnout je na požadované místo, abyste si uspořádali rozvržení stránky podle svého.
Například vedle sebe.

.. Poznámka:
Dlouhodobé běhové instance nejsou zaručeny. Neaktivní shell může být
může být kdykoli odpojen, aby se uvolnily zdroje.

Editor
------

Online integrovaný vývojový prostředí pro úpravu zdrojového kódu.
Můžete také otevřít terminály, konzoly Pythonu a dokonce i konzoly Odoo Shell.

.. obrázek: interface-branches-editor.png
:align:center

Můžete otevřít více záložek a přetáhnout je na požadované místo, abyste si uspořádali rozvržení stránky podle svého.
Například vedle sebe.

Monitorování
----------

Tento odkaz obsahuje různé sledovací metriky aktuální verze.

.. obrázek:: větve/monitoring-větví.png
:align:center

Můžete zvětšit, změnit časové rozpětí nebo vybrat konkrétní metriku pro každý graf.
Na grafech vám pomohou s přiřazením změn k budovám (import databáze, git push, atd...).

... _odoosh/logs:

Logy
----

Zkontrolovat záznamy o vašem serveru.

.. obrázek: branches/interface-branches-logs.png
:align:center

K dispozici jsou různé logy:

* soubor instalace: Logy databáze. V rozvojové větvi jsou zahrnuté i logy testů.
* pip.log: Logy instalace závislostí v Pythonu.
* odoo.log: Protokoly běžícího serveru.
* update.log: Logy aktualizací databáze.
* pg_long_query.log: Logy dotazů PostgreSQL, které trvají neobvykle dlouho.

Pokud se do protokolu přidají nové řádky, zobrazí se automaticky.
Pokud se posunete dolů, prohlížeč bude automaticky posouvat každou novou řádku.

Stahování protokolů můžete přerušit kliknutím na příslušné tlačítko v pravém horním rohu zobrazení.
Stahování je automaticky zastaveno po 5 minutách. Můžete jej znovu spustit pomocí tlačítka Play.

... odoo_sh_branches_backups:

Zálohy
-------

Seznam dostupných záloh ke stažení a obnovení, možnost provést ruční zálohu a import
databáze.

.. obrázek: větve/interfaces-vzpěry-zálohy.png
:align:center

Odoo.sh provádí denní zálohy produkční databáze. Uchovává 7 denních, 4 týdenních a 3 měsíčních záloh.
Každá záloha obsahuje databázový export, úložiště souborů (přílohy, binární pole), protokoly a relace.

Stanice a vývojové databáze nejsou zálohovány.
Nicméně máte možnost obnovit zálohu produkční databáze ve svých testovacích větvích.
testovacích účelů nebo ruční obnovu dat, která byla omylem smazána z produkční databáze.

Seznam obsahuje zálohy uchovávané na serveru, kde je hostována vaše produkční databáze.
Tento server uchovává pouze jeden měsíc záloh: 7 denních a 4 týdenních záloh.

Dedikované servery pro zálohování uchovávají stejné zálohy jako i tři další měsíční zálohy.
Chcete-li obnovit nebo stáhnout jedno z těchto měsíčních záloh, kontaktujte nás na adrese https://www.odoo.com/help/.

Pokud spojíte komit aktualizující verzi jednoho nebo více modulů (v souboru `__manifest__.py`) nebo jejich odkazované python
závislosti (v souboru requirements.txt), pak provede zálohu automaticky (označené jako Update v seznamu).
Jakmile bude instalován nový balíček, nebo dokonce samotná databáze.
změnila s aktualizací modulu, která následovala. V těchto dvou případech provádíme zálohu, protože může dojít k potenciálnímu
zničit věci.

Pokud se sloučí pouze nějaký komit, který mění jen kód bez změn uvedených výše, pak se žádné zálohy nedělá.
Odoo.sh, protože ani kontejner, ani databáze nejsou upraveny, takže platforma považuje tento postup za bezpečný. Samozřejmě
pokud chcete získat ještě větší jistotu, můžete si zálohu udělat ručně předtím, než provedete velké změny ve zdrojích produkce.
něco se pokazí (manuální zálohy jsou k dispozici asi týden). Pro zamezení zneužívání je omezen počet manuálních záloh
až 5 denně.

Funkce „Import databáze“ přijímá archivy databází ve formátu poskytnutém:

* standardní správce databází Odoo.

* Odoo správce online databází.
* tlačítko pro stahování zálohy z obrazovky Odoo.sh Backup na této záložce *.Backups*.
* tlačítko pro stažení zálohy na stránce s výstupy projektu v sekci :ref:`Sestavení <odoosh-gettingstarted-builds>`.

... odoo_sh/upgrade:

Upgrade
-------

Pro produkci a provozní složky platí pro oprávněné projekty.

.. viz též:
:doc:`Dokumentace k upgradu <../../upgrade>`

..._odoosh-gettingstarted-branches-tabs-settings:

Nastavení
--------

Zde najdete několik nastavení, která se vztahují pouze na aktuálně vybranou větev.

.. obrázek: větve/rozhraní-větve-nastavení.jpg
:align:center

Chování po novém zavázání

Pro vývojové a testovací větve můžete změnit chování větve po přijetí nové
zavázat se. Výchozí vývojová větev vytvoří novou sestaveninu a testovací větev aktualizuje
předchozí verze (viz část :ref:`Produkční fáze <stage_production>`). To je zejména užitečné
Pokud funkce, kterou pracujete na, vyžaduje konkrétní nastavení nebo konfiguraci, abyste se vyhnuli
je nutné ji znovu nastavit ručně při každém připojení. Pokud zvolíte nové sestavení pro vývojovou větev,
Vytvořit novou kopii z výrobní verze každý, když je pushnutá změna.
při návratu ze scénování do vývoje bude nastaveno „Nic nedělat“.

**Instalace modulů**

Zvolte moduly, které se mají automaticky instalovat do vývojových verzí.

.. obrázek: branches/interface-settings-modulesinstallation.png
:align:center

* *Nainstalovat pouze mé moduly* nainstaluje do větve pouze moduly z této větve. Je to výchozí volba.
Výjimku tvoří podmoduly, viz :ref:`podmoduly <odoosh-advanced-submodules>`.
* *Úplná instalace (všechny moduly)* nainstaluje moduly větve a moduly zahrnuté ve submodulech
a všechny standardní moduly Odoo. Při plném spuštění je deaktivována sada testů.
* *Nainstalovat seznam modulů* nainstaluje do systému moduly uvedené v zadaném vstupu pod touto volbou.
Jména jsou technický název modulů a musí být oddělena čárkou.

Pokud jsou testy povoleny, balíček standardních modulů Odoo může trvat až hodinu.
Toto nastavení se vztahuje pouze na vývojové sestavení.
Staging vytváří duplicitní produkční sestavení a pouze produkční sestavení instaluje základ.


**Sada testů**

Pro vývojové větve můžete zvolit, jestli chcete nebo nechcete aktivovat testovací sadu. Je zapnutá výchozí hodnotou.
Při zapnutém testovacím balíčku můžete omezit jejich počet specifikacíí testových značek:
<vývojář/odkaz/testování/výběr>.

**Verze Odoo**

Pokud chcete otestovat aktualizovaný kód nebo vyvíjet pro větve vývoje, můžete změnit verzi Odoo.
funkce, zatímco je vaše produkční databáze v procesu aktualizace na novější verzi.

Dále máte dvě možnosti ohledně aktualizace kódu pro každou verzi.

* Můžete si vybrat, zda chcete automaticky těžit z nejnovějších oprav chyb, bezpečnostních a výkonnostních problémů.
Zdroje vašeho Odoo serveru budou aktualizovány každý týden. To je možnost „Nejnovější“.
* Můžete si vybrat, že budou zdroje Odoo připojeny k určité verzi výběrem z seznamu
datum. Změny budou platné po dobu 3 měsíců, poté vyprší a na Vás bude zaslána zpráva e-mailem.
přiblížení se datumu a pokud později nebudete nic dělat, budete automaticky nastaveni na
nejnovější verze.

**Vlastní domény**

Zde můžete konfigurovat další domény pro vybranou pobočku. Je možné přidat i jiné
Domény ve tvaru *<název firmy>.odoo.com* nebo vlastní domény, pro které musíte:

* vlastnit nebo zakoupit doménu.
* přidat doménu do seznamu.
* ve správci doménových jmen vašeho registrátora.
Nastavte doménové jméno s „CNAME“ záznamem nastaveným na vaši produkční databázi.

Příklad: Např. pro přiřazení *www.mycompany.com* k databázi *mycompany.odoo.com*:

* v Odoo.sh přidejte do vlastních domén projektu *www.mycompany.com*.
* ve vašem správci doménových jmen (např. *godaddy.com*, *gandi.net*, *ovh.com*)
konfigurujte webové stránky www.mycompany.com s „CNAME“ záznamem, jehož hodnotou je mycompany.odoo.com.

Nebude přijatá doména bez koncovky (*mycompany.com*):

* Mohou být konfigurovány pouze pomocí záznamů „A“.
* „A“ záznamy přijímají pouze hodnotu IP adres.
* IP adresa vaší databáze se může změnit po upgradu, hardwarovém selhání nebo
Vaše touha uchovávat databázi v jiném státě nebo kontinentu.

Proto by mohly najednou přestat fungovat domény bez obsahu, pokud dojde ke změně IP adresy.

Pokud byste chtěli, aby oba názvy *mycompany.com* a *www.mycompany.com* fungovaly s vaší databází,
Přesměrování z prvního na druhý je mezi
„Nejlepší postupy SEO <https://support.google.com/webmasters/answer/7451184?hl=cs>“
(Viz *Poskytnout jednu verzi URL, která umožní získat dokument*)
aby byl jediný doménový název. Můžete tedy nastavit, aby se všechny stránky s názvem *mycompany.com* automaticky přesměrovaly na www.mycompany.com.
Většina správců domén má možnost tento přesměrování konfigurovat, což je obecně nazýváno jako přesměrování na webu.

**HTTPS/SSL**

Pokud je přesměrování správně nastaveno, bude si platforma automaticky vytvářet certifikát SSL.
„Let’s Encrypt“ <https://letsencrypt.org/about/> a do hodiny bude váš web
přístupný přes protokol HTTPS.

Na platformě Odoo.sh zatím není možné si vytvářet vlastní certifikáty SSL.
Zvažujeme tuto funkci, pokud bude poptávka dostatečná.


*Soulad se standardem SPF a DKIM*

Pokud doména vašich uživatelů používá SPF (Sender Policy Framework) nebo DKIM
(DomainKeys Identified Mail), nezapomeňte autorizovat Odoo jako odesílací server ve vašem doménovém jménu
Nastavení, které zvyšuje doručitelnost vašich odchozích e-mailů. Postup nastavení
v dokumentaci o :ref:`SPF <email-domain-spf>` a :ref:`DKIM
<email-domain-dkim>.

.. Varování:
Pokud zapomenete na konfiguraci SPF nebo DKIM, aby autorizovaly Odoo jako odesílatele, může to vést k
doručování vašich e-mailů do složky Spam ve schránce kontaktů.

Shell příkazy
==============

V pravém horním rohu obrazovky jsou k dispozici různé příkazy pro skořápku.

.. obrázek:: interface-branches-shellcommands.png
:align:center

Každý příkaz lze zkopírovat do schránky, aby se dal použít v terminálu.
a některé z nich lze spustit přímo ze služby Odoo.sh kliknutím na tlačítko „Spustit“
V takovém případě se zobrazí vyskakovací okno, ve kterém uživatel definuje případné proměnné.
např. „<URL>“, „<PATH>“ atd.

Klon
-----

Stáhněte si repozitář Git.

.. kódový blok: bash

$ git clone --recursive-submodules --branch master git@github.com:odoo/odoo.git

Klonuje repozitář *odoo/odoo*.

* :kód: --recursive-submodules: Stáhne podmoduly vašeho repozitáře. Podmoduly obsažené v podmodulích jsou stahovány také.
* :kód: --branch: zkontroluje konkrétní větev repozitáře, v tomto případě *master*.

Tlačítko „Spustit“ pro tuto příkazovou řádku není k dispozici, protože je určená pro použití na vašich strojích.

Fork
----

Vytvořit novou větev na základě aktuální větve.

.. kódový blok: bash

$ git checkout -b feature-1 master

Vytvoří novou větev s názvem *feature-1* na základě větve *master* a pak ji zkontroluje.

.. kódový blok: bash

$ git push -u origin feature-1

Nahrává novou větev s názvem *feature-1* do vašeho vzdáleného repozitáře.

Sloučení
-----

Sloučit aktuální větev do jiné větve.

.. kódový blok: bash

$ git merge staging-1

Sloučí větve *staging-1* do aktuální větve.

.. kódový blok: bash

$ git push -u origin master

Nahrává změny, které právě provedl větvený kořenový adresář na vašem vzdáleném repozitáři.

SSH
---

Nastavení
~~~~~

Pokud chcete používat SSH, musíte si nastavit profil SSH veřejného klíče (pokud ještě není nastavený).
Postupujte takto:

#Vytvořit nový klíč SSH
<https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key>
#Kopírujte klíč SSH do schránky
<https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account>
(pouze krok 1)
#Vložte zkopírovaný obsah do profilu SSH klíčů a stiskněte „Přidat“.

...... obrázek: branches/SSH-key-pasting.png
:align:center

#Klíč by se měl objevit pod tímto textem.

.... obrázek:: větve/SSH-klíč-zobrazení.png
:align:center

Připojení
~~~~~~~~~~

Pro připojení k vašim sestavením pomocí ssh použijte následující příkaz v terminálu:

.. kódový blok: bash

$ ssh <build_id>@<doména>

Krátkou zkratku pro tento příkaz najdete v horním pravém rohu v záložce SSH.

.. obrázek: branches/SSH-panel.png
:align:center

Pokud máte na projektu správná oprávnění:
získáte přístup SSH k sestavení.

.. Poznámka:
Dlouhodobé spojení SSH nejsou zaručeny. Neaktivní spojení budou
Je odpojen, aby se uvolnily zdroje.

Podmodul
---------

Přidejte větve z jiného repozitáře do vaší aktuální větev jako *podsložku*.

*Podmoduly* umožňují používat moduly z jiných repozitářů v projektu.

Podmoduly jsou podrobně popsány v kapitole
:ref:`Podmoduly <odoosh-advanced-submodules> této dokumentace.

.. kódový blok: bash

$ git submodule add -b master <URL> <PATH>

Přidá větvení *master* repozitáře *<URL>* jako podmodul pod cestou *<PATH>* ve vašem aktuálním větvení.

.. kódový blok: bash

$ git commit -a

Připojí všechny vaše současné změny.

.. kódový blok: bash

$ git push -u origin master

Nahrává změny, které právě provedl větvený kořenový adresář na vašem vzdáleném repozitáři.

Smazat
------

Odeberte větev z vašeho repozitáře.

.. kódový blok: bash

$ git push origin :master

Smaže větve ve vašem vzdáleném repozitáři.

.. kódový blok: bash

$ git branch -D master

Smaže větve ve vašem lokálním repozitáři.
