==============================
Oprava čtečky čárových kódů
==============================

Odoo Barcode podporuje tři hlavní typy skenovačů čárových kódů: skenery připojené k počítači prostřednictvím USB, bezdrátové skenery a
mobilní počítačové skener. Při konfiguraci každého typu skeneru se mohou objevit běžné problémy, v nichž
Skenery nefungují tak, jak mají, a Odoo vrací chyby zařízením.

Přečtěte si níže uvedené sekce k identifikaci obecných a specifických problémů s zařízením.
druhy skenerů.

Obecné otázky
==============

Podívejte se na následující části, kde najdete nejčastější problémy s běžnými skenerovými zařízeními.

Pro problémy týkající se konkrétních zařízení odkazujte na :ref:`skenery Androidu
V sekci „Nastavení čárového kódu“ pro mobilní počítačové skenery nebo v části :ref:`Bez obrazovky
část „Skenery (kódy, nastavení, bezdrátové skenery)“ pro USB a Bluetooth skenery.

Čárový kód nelze přečíst
----------------------

Jedním z běžných problémů, který se může vyskytnout při používání čárových kódů, je chyba způsobená
není čitelný.

Může se to stát z následujících důvodů:

- Čárový kód je poškozený.
- Zařízení nemůže přečíst požadovaný typ čárového kódu (některé skenery dokáží číst pouze dvourozměrné čárové kódy).
- Kód, který je skenován, se zobrazuje na obrazovce. Některé skener nepodporují tuto funkci a kódy
Musí být vytisknuta, aby mohla být skenována. Nejčastěji se jedná o čárové kódy typu 1D.
- Zařízení nemá baterii nebo je poškozené. Abyste tento problém vyloučili, postupujte podle návodu na odstraňování závad
V následujících částech.

Odoo vrací chybu čárového kódu
--------------------------

Všechny typy čteček čárových kódů mají své vlastní „jazyky“, které ovlivňují, jakým způsobem vygenerují výstup
údaje o čárovém kódu do aplikace Odoo Barcode. V některých případech může způsobit, že aplikace Odoo Barcode vrací čárový kód
chyba při skenování. Může jít například o následující příčiny:

- K počítači je připojen jiný klávesnicový rozložení než u čtečky kódů.
Vypněte zařízení a ujistěte se, že je nakonfigurováno stejným klávesovým rozložením.

Příkladem je například nastavení počítače pro použití klávesnice FR-BE. V takovém případě by měl snímač
FR-BE klávesy. Stejná logika platí, pokud používáte tablet místo počítače.

Pro více informací o konfiguraci klávesových zkratek se podívejte na stránku :doc:`Nastavení čtečky
dokumentace k hardwaru.
- Pro mobilní počítačové skener (například zařízení Zebra) může skenér interpretovat
čárový kód jinak než bylo zamýšleno. K tomu může sloužit skenování testovacího čárového kódu, abyste viděli, jak skener
dekóduje čárový kód.

.._čárový kód/nastavení/Android skener:

Androidové skenery
================

Nejnovější modely čteček čárových kódů s Androidem a prohlížečem Google by měly fungovat s Odoo.
Vzhledem k široké nabídce modelů a konfigurací je však doporučeno nejprve vyzkoušet
kompatibilita s Odoo.

Produktová řada Zebra je doporučena; konkrétně model **Zebra TC21 (WiFi-only)** a **Zebra
TC26 (Wi-Fi / mobilní).

.. viz též:
„Hardware kompatibilní s Odoo Inventory & Barcode <https://www.odoo.com/app/inventory-hardware>“

Aplikace čárového kódu neposkytuje zpětnou vazbu
----------------------------------

Výchozí nastavení aplikací pro skenování čárových kódů v systému Android je předběžné zpracování čárového kódu a následně odeslání celé zprávy. Od Odoo
Kód Barcode neumí číst tento typ výstupu, nastavení pro každý typ skeneru musí být
správně nakonfigurovaný.

Odoo Barcode očekává, že skener funguje jako analogová klávesnice a tak pouze detekuje *klávesu
události*. Viz následující části pro konfiguraci nastavení pro nejpopulárnější zařízení.

Zebra TC21/TC26
---------------

Při používání snímačů značky Zebra zkontrolujte následující nastavení klávesnice, aby se předešlo chybám.

Začněte na domovské obrazovce skenovače Zebra a vyberte aplikaci DataWedge (aplikace je
jejichž ikona je ve tvaru „(světle modrá čárovka)“.

Na stránce „Profily DataWedge“ vyberte možnost profilu pro přístup k snímači značky Zebra.
Nastavení.

Jakmile si vyberete profil, přejděte dolů na možnost „Výstup z klávesnice“ a ujistěte se, že
Volba „Zapnout/vypnout zadávání klávesových zkratek“ je nastavena na „Povoleno“.

.. obrázek: zařízení/zařízení-zebra-nastavení.png
:align:center
:alt:Zobrazit možnost klávesové zkratky v aplikaci DataWedge pro skenery Zebra.

Jakmile je tato možnost zapnutá, přejděte zpět na stránku s nastavením profilu a přejděte do
V části „Zpracování stisknutí klávesnice“. Poté otevřete podnabídku „Možnosti zpracování stisku klávesy“.
Zkontrolujte, zda je zaškrtnutá možnost „Přenášet znaky jako události“.

.. důležité::
V poli „Odeslat znaky jako událost“ musí být zaškrtnuto na skeneru Zebra.
Odoo **není schopna rozpoznat skenované čárové kódy.

Jakmile jsou provedeny výše uvedené kroky, proveďte testovací skenování, abyste si ověřili, že je skener Zebra funkční.
účelově.

MUNBYN zařízení s operačním systémem Android
----------------------

Při používání skenerů MUNBYN pro systém Android zajistěte následující konfigurace, abyste se vyhnuli chybám.

Na domovské obrazovce zařízení klikněte na položku :menuselection:`App Settings`. Na následující stránce najděte
sekci „Režim procesu“ a vyberte „Klávesové vstupy“.

.. obrázek: zařízení_problémy/zařízení-problémy-munbyn-režim-procesu.png
:align:center
:alt:Sekce procesního režimu na stránce nastavení aplikace skeneru MUNBYN.

.. tip::
Vybraný režim zpracování *Data* řídí, jak jsou data zpracovávána po přečtení čárového kódu.

*Vstup pomocí klávesnice* vkládá čísla do oblasti kurzoru stejně jako vstupová data na klávesnici.
klávesnice s analogovým ovládáním.

Po provedení výše uvedených kroků proveďte testovací skenování, abyste si ověřili, že je skener MUNBYN pro Android
funguje tak, jak má.

.. varování: Proč není po úspěšném skenu v aplikaci zobrazená žádná data?

Při skenování čárového kódu může být vydán zvukový signál, který ukazuje úspěšný sken, ale není to
datové výstupy v aplikaci.

Pro vyřešení této chyby nastavte způsob výstupu na „klávesový analog“ v aplikaci „Skener“.
zařízení.

Na domovské obrazovce zařízení klikněte na :menuselection:`Skenování - Nastavení`.
:guilabel:`Nastavení“ stránku a klikněte na „Výstupní režim“. Vznikne okno s výběrem
různé možnosti výstupu pro uživatele. Vyberte klávesnici, pak klikněte
:guilabel:`OK“.

.... obrázek: zařízení/zařízení-problémy-režim-výstupu-přepínače.png
:align:center
:alt:Pop-up okno s výstupním režimem na skeneru MUNBYN.

Zpět ke spuštěnému programu a klikněte nejprve na dialogové okno pro vstup.
skenování. Nakonec proveďte kontrolní sken, abyste se ujistili, že skener MUNBYN pro Android funguje tak, jak má.
bylo zamýšleno.

Datalogic zařízení s operačním systémem Android
-------------------------

Při používání skenerů Datalogic s operačním systémem Android zkontrolujte následující konfigurace, abyste zabránili
chyby.

Pro zobrazení a konfiguraci všech nastavení skeneru použijte aplikaci Settings na zařízení s operačním systémem Android od společnosti Datalogic.
zařízení. V nabídce aplikací vyberte:menuselection:`Nastavení --> Systém --> Skener
Nastavení.

Z výsledného seznamu nastavení vyberte položku „Výřez“. V nabídce zvolte pod položkou
V části „Klávesnice“ zkontrolujte, jestli je zapnutá funkce „Povolit klávesnici“.
aktivován.

Poté v sekci „Klávesnice“ najděte „Zadávání klávesnicového rozhraní“.
možností vstupu. Výchozím nastavením je „Vložení textu“.

.. obrázek: zařízení/zařízení-problémy-výčepní-pult.png
:align:center
:alt:Nastavení štítku na snímači Datalogic.

Klikněte na „Režim vstupu klávesnice“, a změňte nastavení na „Tlačítko“.
Tím se zajistí, že skenované čárové kódy budou převedeny na stisknutí kláves, nikoli vpraveny
do pole s textem.

.. obrázek: zařízení/zařízení-zjišťování problémů-klávesnice-vstupní blok.png
:align:center
:alt:Výběr režimu vstupu klávesnicového zásuvníku na skeneru Datalogic.

Jakmile jsou splněny všechny tyto kroky, proveďte testovací skenování, abyste se ujistili, že je datalogický skener na Androidu
funguje tak, jak má.

.. _čárový kód/nastavení/snímače bez displeje:

Bezobrazovkové skener
===================

Bezobrazovkové skenerové snímače jsou zařízení na čtení kódů, která nemají obrazovky. Patří sem např. USB skener
a bezdrátové skenery.

.. důležité::
Odoo podporuje většinu USB a Bluetooth čteček čárových kódů, protože všechny z nich simulují klávesnici.
ověřit, zda je skener kompatibilní se specifickým klávesnicovým rozložením (nebo lze jej konfigurovat tak, aby
(viz seznam kompatibilního hardwaru společnosti Odoo).
<https://www.odoo.com/documentation/10/inventory/hardware/>.

NETUM zařízení
-------------

Výchozí uživatelská příručka skenovacího zařízení čárových kódů NETUM zobrazuje pouze konfiguraci francouzské klávesnice.
použijte klávesnici belgickou, naskenujte kód níže:

.. obrázek: zařízení/zařízení-opravy-problémů-Belgie-FR-klíč.png
:align:center
:alt:Belgický klíč kódovaný čárovým kódem.

Jakmile je kód naskenován, ujistěte se, že má skenovač správnou konfiguraci klávesnice.
A funguje, jak má.

.. viz též:
   - :doc:`../setup/hardware`
   - :doc:`../setup/software`
