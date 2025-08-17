=============================
Aktualizace a přizpůsobení databáze
=============================

Aktualizace na novou verzi Odoo může být náročná, zejména pokud pracujete s databází.
obsahuje vlastní moduly. Tato stránka má za cíl vysvětlit technický proces aktualizace
databáze s přizpůsobitelnými moduly. Viz: „Dokumentace k upgradu“
na návod, jak upgradovat databázi bez vlastních modulů.

Zvažujeme modul na míru, který je jakýmkoliv modulem, který rozšiřuje standardní kód Odoo a nebyl
Vytvořené pomocí aplikace Studio. Před aktualizací takového modulu nebo před požadavkem na jeho aktualizaci je
Podívejte se na :ref:`upgrade-sla`, abyste zjistili, kdo za ním stojí.

Při práci na tom, co nazýváme „upgrade na míru“, myslete na cíle
upgrade:

#Zůstaňte podporováni
#. Získejte nejnovější funkce
#Užívejte si zlepšení výkonu.
#Snížit technický dluh.
#Využijte zlepšení bezpečnosti

S každou novou verzí Odoa dochází k úpravám. Tyto změny mohou ovlivnit moduly, které
byly vyvinuty. To je důvod, proč se aktualizuje databáze obsahující
Moduly vyžadují další kroky, aby bylo možné upgradovat zdrojový kód.

Tady jsou kroky, které je třeba udělat při upgradu databází s vlastními úpravami:

#:ref:`Zastavte vývoj a vyzvěte je k úpravám <upgrade_custom/stop_developments>“.
#:ref:`Požádejte o aktualizaci databáze <upgrade_custom/request_upgrade>.
#:ref:`Vytvořte modul, který je možné nainstalovat na prázdnou databázi <upgrade_custom/empty_database>“.
#:ref:`Uveďte, že váš modul je instalovatelný na aktualizované databázi <upgrade_custom/upgraded_database>.
#.:ref: Testování je nutné provádět důkladně a před nasazením do praxe by mělo proběhnout i zkoušení.
#:ref:`Aktualizovat databázi produkce <upgrade_custom/production>.

.._upgrade_custom/stop_developments:

Krok 1: zastavte vývoj
=============================

Zahájení upgradu vyžaduje závazek a zdroje pro vývoj. Pokud se bude dál vyvíjet
Při každé změně budou muset být tyto funkce znovu upgradovány a testovány.
Proto doporučujeme úplné zamrznutí kódu při spouštění procesu upgradu.
Samozřejmě se tato doporučení netýkají oprav chyb.

Jakmile vývoj skončí, je dobrým zvykem posoudit dosažené pokroky a porovnat
s funkcemi, které byly mezi vaší aktuální verzí a verzí, na kterou cílíte, zavedeny.
Zapracujte na všech možných výzvách a najděte funkční náhrady. Odstraňování duplicit
mezi vašimi vývojovými moduly a standardní verzí Odoo dojde k usnadnění procesu upgradu.
a snižovat technický dluh.

.. poznámka::
Ve změnách mezi verzemi najdete informace v Release notes.
<https://odoo.com/page/release-notes>.

.._upgrade_custom/request_upgrade:

Krok 2: Požádejte o aktualizaci databáze
====================================

Jakmile se vývoj zastaví pro moduly na míru a implementované funkce
Pokud byla vyzvána k odstranění zbytečných funkcí a kódu, další krok je požádat o aktualizaci testu
databáze. K tomu postupujte podle kroků uvedených v :ref:`upgrade-request-test`, dle toho, jaký
typ hostingu vaší databáze.

Účelem této fáze není začít pracovat s vlastními moduly v aktualizované databázi.
Aby bylo zajištěno, že proces upgradu běží hladce a aby byla dodána testovací databáze
správně. Pokud tomu tak není a požadavek na upgradování selže, žádejte o pomoc prostřednictvím
stránku „Pomoc při migraci“ (<https://odoo.com/help?stage=migration>), kde si vyberete možnost
testování upgradu.

.. upgrade_custom/empty_database:

Krok 3: Vyprázdnění databáze
======================

Před prací na aktualizované testovací databázi doporučujeme provést funkčnost vlastních vývojů na
prázdná databáze cílové verze vašeho upgradu. To zajistí, že personalizace
je kompatibilní s novou verzí Odoo a umožňuje analyzovat chování a interakci s novou
funkce a zaručuje, že nebudou způsobovat žádné problémy při aktualizaci databáze.

Použití vlastních modulů také pomáhá zabránit chybám a změnám.
konfigurace, která mohou být v produkčním systému přítomny (např. úpravy studií).
přizpůsobené webové stránky, šablony e-mailů nebo překlady). Nejsou vrozeně spojeny s
vlastní moduly, které mohou vyvolat nechtěné problémy v průběhu procesu upgradu.

Pokud chcete, aby vlastní moduly fungovaly na prázdné databázi, doporučujeme postupovat následovně:

#:ref:`upgrade_custom/empty_database/modules_installable`
#:ref:`upgrade_custom/empty_database/test_fixes`
#:ref:`upgrade_custom/empty_database/clean_code`
#:ref:`Dokončení testů úspěšně <upgrade_custom/empty_database/standard_test>“

.. _upgrade_custom/prázdná databáze/moduly nainstalovatelné:

Umožnit instalaci vlastních modulů
-------------------------------

Prvním krokem je udělat moduly na míru instalovatelné v nové verzi Odoo.
To znamená, že je nutné zajistit, aby během instalace nebyly žádné stopy ani varování.
Pro tento účel nainstalujte v prázdné databázi nové verze Odoa jeden po druhém moduly na míru a
opravit stopy a varování, které z toho vznikají.

Tento proces pomůže odhalit problémy během instalace modulů, například:

- Nesprávné závislosti modulu.
- Změna syntaxe: deklarace aktiv, aktualizace OWL, atributy.
- Odkazy na standardní pole, modely a pohledy, které již neexistují nebo byly přejmenovány.
- XPath, které byly přesunuty nebo odstraněny z pohledu.
- Metody přejmenované nebo odstraněné.
- ...

... upgrade_custom/prázdná databáze/test_opravy:

Test a opravy
--------------

Jakmile nejsou žádné další zpětné sledování při instalaci modulů, je třeba je otestovat.
I když jsou moduly pro uživatele instalovatelné na prázdné databázi, neznamená to, že je
žádné chyby při jejich provádění. Proto doporučujeme pečlivě otestovat všechny
přizpůsobení, aby vše fungovalo tak, jak má.

Tento proces pomůže odhalit další problémy, které nebyly zjištěny během instalace modulu.
A mohou být detekovány pouze v průběhu běhu. Například zastaralé volání standardního Pythonu nebo OWL
funkce, neexistující odkazy na standardní pole atd.

Doporučujeme otestovat všechny možnosti nastavení, zejména následující prvky:

- Názory
- Šablony e-mailů
- Zprávy
- Akce serveru a automatické akce
- Změny v běžných pracovních postupech
- Pole vypočítaná v aplikaci

Doporučujeme také psát automatické testy, abyste ušetřili čas při opakování testů a zvýšili
testovací pokrytí a zajistit, aby změny a opravy, které byly zavedeny, nezpůsobily narušení stávajících toků.
Pokud jsou v již implementovaných testech nějaké funkce, ujistěte se, že byly aktualizovány na novou verzi.
Vývojáři přidali novou verzi a úspěšně spustili aplikaci, opravili všechny problémy, které mohly být přítomné.

.. upgrade_custom/empty_database/clean_code:

Uklidněte kód
--------------

V této fázi upgradu doporučujeme také vyčistit kód co nejvíce.
Mezi ně patří:

- Odstraňte zbytečný a nepotřebný kód.
- Odebrat funkce, které jsou nyní součástí standardu Odoo, jak je popsáno v

- Komentáře k čistému kódu odstraňte, pokud už nejsou potřeba.
- Pokud je potřeba, přeorganizujte kód (funkce, pole, pohledy, zprávy atd.).

.. upgrade_custom/prázdná databáze/standardní test:

Standardní testy
--------------

Jakmile jsou splněny předchozí kroky, doporučujeme provést všechna běžná testování spojená s
závislosti na modulu vlastní konfigurace projdou.
Standardní testy zajišťují ověření logiky kódu a zabraňují poškozování dat.
Pomohou vám identifikovat chyby nebo nežádoucí chování předtím, než se pustíte do práce na databázi.

V případě, že dojde k neúspěšnému provedení standardních testů, navrhujeme zkontrolovat důvody jejich selhání:

- Přizpůsobení změní standardní práci: přizpůsobte si standardní test své pracovní rutině.
- Nastavení nezohledňuje zvláštní průtok: přizpůsobte si nastavení, aby bylo zajištěno
je vhodný pro všechny standardní pracovní postupy.


... upgrade_custom/upgraded_database:

Krok č. 4: Aktualizovaná databáze
=========================

Jakmile jsou moduly zvyku instalovatelné a fungující v prázdné databázi, je čas
přidělejte jim práci na :ref:`zvýšené databázi <upgrade-request-test>`.

Aby se u nové verze funkce vlastního kódu zcela bezchybně fungovala, postupujte takto:

- :ref:`upgrade_custom/upgraded_database/migrate_data`
- :ref:`upgrade_custom/upgraded_database/test_custom`

... upgrade_custom/upgraded_database/migrate_data:

Migrujte data
----------------

Při aktualizaci vlastních modulů můžete muset použít skripty pro aktualizaci.
„<../reference/upgrades/upgrade_scripts>“ odrážejí změny v zdrojovém kódu.
odpovídající data. Kromě upgradovacích skriptů můžete také využít
:doc:`../reference/upgrades/upgrade_utils` a funkce pomocné.

- Každá technická data, která byla přejmenována během upgradu vlastního kódu (modely, pole,
(externí identifikátory) by měly být přejmenovány pomocí upgrade skriptů, aby se zabránilo ztrátě dat během
modul pro aktualizaci. Viz také metoda :meth:`rename_field`, :meth:`rename_model`, :meth:`rename_xmlid`.
- Data ze standardních modelů odstraněná z zdrojového kódu novější verze Odoo.
databáze během standardního procesu upgradu může být nutné obnovit ze staré tabulky modelu
pokud ještě přetrvává.

...... příklad::
Pole vlastní pro model „sales.subscription“ nejsou automaticky migrována z Odoo 15 do
Odoo 16 (když byl model sloučen do „sale.order“). V tomto případě lze použít SQL dotaz.
provedené na skriptu upgradu, který přesouvá data z jedné tabulky do druhé.
že všechny sloupce/pole musí již existovat, takže zvažte provedení v „po“ skriptu (viz
:ref:`upgrade-scripts/fáze`).

... spoiler::

... kódový blok: Python

def migrace(cr, verze):
cr.execute("
                  """
UPDATE objednávka_prodeje
SET vlastní pole = ss.vlastní pole
FROM sale_subscription ss
WHERE ss.new_sales_order_id = so.id
                  """
               )

Podrobnější informace najdete v dokumentaci na téma :doc:`../reference/upgrades/upgrade_scripts`.

Upgrade skripty mohou být také použity k:

- Zkrátit dobu zpracování aktualizace. Například uložit hodnotu vypočítaných pole
na modelech s nadměrným počtem záznamů pomocí dotazů SQL.
- V případě, že se změnila výpočetní metoda hodnoty pole, je nutné jej znovu vypočítat.
:metoda: recompute_fields.
- Odinstalujte nechtěné vlastní moduly. Podívejte se také na metodu :meth:`remove_module`.
- Opravte chybné údaje nebo špatně nakonfigurované nastavení.

Spouštění a testování skriptů pro aktualizaci
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. záložky::

...... skupina-tab::Odoo Online

Instalace vlastních modulů, které obsahují soubory Pythonu, není na Odoo Online povolena.
databáze nelze na této platformě spouštět upgrade skripty.

...... skupina-tab:: Odoo.sh

Jak je uvedeno v záložce „Odoo.sh“ na stránce :ref:`upgrade-request-test`, Odoo.sh je integrováno s
upgradovat platformu.

Jakmile je větvení na „Aktualizace při zadání“ nastaveno, každá aktualizace se provede při každém
Pokud je na větvi nainstalován upgrade, je obnoven zálohovaný systém a všechny moduly jsou aktualizovány.
Tato aktualizace zahrnuje provedení upgrade skriptů.

Kromě samotného upgradu databáze je součástí i provedení upgrade skriptů.
aktualizace vlastních modulů prováděná platformou při obnovení databáze.

......skupina-tab::On-premise

Jakmile obdržíte aktualizovanou zálohu databáze z „Platformy pro upgrade“,
<https://upgrade.odoo.com>`, nasadit databázi a aktualizovat všechny moduly.
vyvoláním příkazu :doc:`odoo-bin </developer/reference/cli> ve skriptovacím jazyce Shell.
Pro aktualizaci vlastních modulů použijte možnost:
--update <moduly>.

...............důležité::
Jak je uvedeno v dokumentaci CLI (:doc:`CLI dokumentace </developer/reference/cli>`), použité příkazy
volání CLI závisí na tom, jak jste nainstalovali Odoo.

.. upgrade_custom/upgraded_database/test_custom:

Otestujte vlastní moduly
-----------------------

Aby fungovaly v nové databázi správně, musí mít
musí být také testovány, což pomáhá zajistit jak standardní, tak i uživatelská data uložená v databázi.
je konzistentní a nic nebylo ztraceno během procesu upgradu.

Pozor na:

- Zobrazení nefunguje: Během upgradu se zobrazení s obsahem, který způsobuje problémy, odstraní.
znefunkčněno. Informace o znefunkčněných pohledech najdete v zprávě o upgradu. Tento pohled je nutné
aby se znovu aktivoval (nebo odstranil, pokud už není potřeba). Doporučujeme použití
upgrade skripty.
- Modul „Data“ nebyl aktualizován: Vlastní záznamy, které mají
„noupdate“ vlajka se při aktualizaci modulu ve staré databázi neaktualizuje. Pro vlastní
dat, která je nutné aktualizovat kvůli změnám v nové verzi, doporučujeme použít upgrade
:meth:`update_record_from_xml`

.. upgrade_custom/testing_rehearsal:

Krok 5: Testování a zkoušení
=============================

Pokud jsou vylepšené moduly funkční v nové databázi, je důležité provést další
kola testování, aby se zjistilo, jak je databáze použitelná a zda nebyly nalezeny nějaké problémy.
v předchozích testech nebyly zaznamenány. Další informace o testování aktualizované databáze najdete na
:ref:`upgrade-testing“.

Jak je uvedeno v části :ref:`upgrade-production`, oba standardní skripty pro upgradování a vaše databáze
neustále se vyvíjí, proto je vhodné požadovat nové aktualizované testy
databáze a zajistit, aby proces upgradu byl stále úspěšný.

Kromě toho si udělejte plnohodnotnou zkoušku procesu aktualizace den předtím, než provedete samotnou aktualizaci.
databáze produkce, aby se během upgradu vyhnula nežádoucímu chování a detekovala jakýkoliv problém.
mohlo dojít s migrovanými daty.

... upgrade_custom/production:

Krok 6: Zvýšení produkce
==========================

Jakmile budete mít jistotu ohledně upgradu produkčního databázového serveru, postupujte podle popsaného procesu na
:ref:`upgrade-production`, podle typu hostingu vaší databáze.
