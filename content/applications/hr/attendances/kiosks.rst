======
Budky
======

Aplikace **Odoo Attendance** umožňuje zaměstnancům zadávat docházku přímo do databáze.
nebo stánek.

Kiosek je :doc:`pouze určený zařízení <hardware> (PC, tablet nebo mobilní telefon) pro zaměstnance k použití
Při příjezdu a odjezdu.

Kiosky jsou potřeba pro zaměstnance, kteří nemají přístup do databáze.

Pouze zaměstnanci s přístupem do databáze Odoo mohou v aplikaci **Přítomnosti** zadat příchod a odchod.
A označují se jako uživatelé.

.. důležité::
Pokud zaměstnanci:ref:`přihlásí a odhlásí <attendance/kiosk-mode-entry> pomocí štítku nebo RFID
Pak je možné použít přístupný zařízení (hardware) v režimu Kiosk (viz. :doc:`Kiosk Mode <attendances/kiosk-mode>`)
Tyto metody **musí být k dispozici**, aby bylo možné je používat.

Konfigurace
=============

Pro použití kiosků v aplikaci **Přítomnosti** přejděte na:
Konfigurace. Na stránce „Nastavení“ konfigurujte sekci „Režimy“
<přítomnosti/kioskový režim> a :ref:`přítomnosti/nastavení kiosku`.

Jakmile jsou všechny požadované nastavení nakonfigurovány, klikněte na tlačítko :guilabel:`Uložit`.
Stránka „Nastavení“ k aktivování a zapnutí těchto funkcí.

...přístupy/režim kiosku:

Součástí jsou i módní doplňky.
-------------

Určete způsob, jakým zaměstnanec při použití kiosku zadává své jméno, buď hledáním v seznamu
pult ([:guiLabel:"Manuální výběr"]), skenováním čipové karty nebo klíčenky (:[:guiLabel:"Čárový kód/RFID"]).
nebo obojí.

Na stránce nastavení pomocí rozevírací nabídky pro režim kiosku
V sekci „Režimy“ vyberte požadovanou volbu z nabídky. Volby jsou
:guilabel:`Čárový kód/RFID“, „Čárový kód/RFID a ruční výběr“ nebo „Ruční výběr“.
Vybírání.

.. poznámka::
Aplikace **Barcode** **nemusí být** nainstalována, aby bylo možné používat jednu z aplikací Barcode/RFID.
nastavení.

...přítomnosti/nastavení kiosku:

Nastavení kiosku
----------------------

Různé nastavení v sekci „Nastavení kiosku“ určuje, jak zaměstnanci přihlásí.
Vyhoďte kiosky ven!

- :guilabel:`Zdroj čárového kódu“ :icon:`fa-building-o“: tato položka se objeví pouze v případě, že je aktivní jedna ze dvou
V nastavení :ref:`Kioskového režimu <attendances/kiosk-mode>` byly zvoleny možnosti „Čárový kód / RFID“.
nastavení.

Pokud je k dispozici, vyberte způsob skenování čárových kódů na pokladně pomocí jedné z možností nabídky.
Barcode lze skenovat pomocí speciálního skeneru nebo zařízením s fotoaparátem.
[:guilabel:"Přední kamera" nebo :guilabel:"Zadní kamera"].
- :guilabel:`Zobrazit čas“ :icon:`fa-building-o“: určete, kolik sekund je jedna kontrola vstupu/výstupu
Potvrzující zpráva se na obrazovce automatu zobrazuje předtím, než se vrátí na hlavní obrazovku pro odbavení.
- Zatrhněte políčko „Poznámka k identifikaci zaměstnance“: zaškrtněte toto pole, pokud chcete, aby zaměstnanci používali jedinečné PIN
aby se přihlásil. PIN je nastaven na každém jednotlivém záznamu zaměstnance. Viz téma:
dokumentace zaměstnance (employees/hr-settings) pro další informace o nastavení
PINy.
- :guilabel:`Adresa kiosku účasti`“:Odoo vytváří jedinečnou webovou adresu (URL), kterou lze použít zařízení jako
automatu bez přihlášení do databáze Odoo. Při nastavování zařízení pro kiosk se přihlaste na
přejděte na tuto jedinečnou internetovou adresu v prohlížeči, abyste se dostali do aplikačního terminálu **Přístupy**.

.. důležité::
Tyto kioskové adresy nejsou **nikterak** zabezpečeny heslem. Kdokoliv, kdo má tuto adresu, může
Přejděte na kiosk aplikace **Účasti**. Pokud je URL napadený z jakéhokoliv důvodu, jako například v případě
Při zjištění bezpečnostního problému klikněte na ikonu „Obnovit“ (vpravo nahoře) a vygenerujte novou adresu URL.
pod odkazem vytvořit novou adresu URL a aktualizovat automat na základě této změny.

Kioskový režim
==========

Přihlášení do režimu Kiosku je dostupné pouze uživatelům s konkrétními „přístupovými právy“
<přístupy/práva>.

Režim „Kiosk“ lze aktivovat dvěma způsoby:

#Navigujte do aplikace „Přítomnost“, klikněte na položku „Kiosk mode“ v horní části obrazovky.
menu. Zařízení poté vypne aplikaci Odoo a přepne do režimu Kiosk.
#Nastavte aplikaci „Přítomnost“ v sekci „Kiosky“.
V sekci Nastavení použijte odkaz v poli „URL kiosku“ na otevření *Kiosku.
Režim* na jakémkoli zařízení.

.. obrázek: stánky/stánek-url.png
:alt:URL pole v sekci nastavení aplikace Účasti.

.. důležité::
Jako bezpečnostní opatření je v režimu Kiosk následně nemožné vrátit se zpět.
databáze bez znovu přihlášení.

.. poznámka::
Vždy je možné vygenerovat novou adresu pro stánek, pokud je třeba. Klikněte na ikonku :icon:`fa-refresh`.
:guilabel:`Vytvořit novou adresu pro režim kiosku“

Pro opuštění režimu Kiosk, buď zavřete záložku v prohlížeči nebo se vrátíte na hlavní obrazovku přihlášení.
Odoo.

.._přístupy/vstup do kiosku:

Příjezd a odjezd s automatem
=============================

Štítek
-----

Pro ověření při příjezdu nebo odjezdu pomocí čipu klikněte na obrázek „Naskenovat čip“
střed kiosku.

.. obrázek: kiosky/skenovací_čip.png
:alt: Zobrazení kiosku s návštěvními známkami, které zobrazují obrázek štítku.

Poté naskenujte čárový kód na štítku pomocí metody nastavené v :ref:`Nastavení kiosku
„Návštěvnost“ nebo „Kiosky“ v části nastavení.

Jakmile je čárový kód naskenován, zaměstnanec je zaevidován nebo vyznačen jako odcházející, a poté se objeví :ref:`potvrzující zpráv
Všechny informace jsou uvedeny v poli „Přítomnost/potvrzení“.

RFID
----

Pro vstup nebo výstup použijte bezkontaktní klíčenku a skenujte ji s čtečkou RFID.

Jakmile je zaměstnanec naskenován, buď se mu otevře vstup nebo výstup, a zobrazí se potvrzující zpráva
Všechny informace jsou uvedeny v poli „Přítomnost/potvrzení“.

Ručně
--------

Uživatelé bez skenovatelného štítku nebo bezkontaktní čipové karty mohou ručně zadávat příchod a odchod na přepážce.

Klepněte na tlačítko „Přidat ručně“ vedle ikony „Uživatel“ a objeví se obrazovka.
se všemi zaměstnanci, kteří mohou být zaevidováni nebo odepsáni. Dashboard aplikace **Zaměstnanci** má stejný
zobrazení.

Klepněte na osobu pro ověření jejího příjezdu nebo odjezdu. Zobrazí se zpráva s potvrzením
Zobrazí se „Přítomnost/potvrzení“.

Pro vyhledání konkrétní osoby buď:

- Hledat: zadejte do vyhledávací lišty jméno požadované osoby. Jakmile se začne psát jméno,
Výsledky shody se zobrazují na obrazovce.
- Podle oddělení: kliknutím na požadovanou volbu v sekci Oddělení, která je umístěna v levém sloupci
obrazovce, abyste viděli pouze zaměstnance z konkrétního oddělení. Číslo na konci
Pozice uvedené v seznamu odpovídají počtu zaměstnanců daného oddělení.

PIN
~~~

Pokud byla zaškrtnuta políčka „Identifikace zaměstnaneckého čísla“ v nastavení kiosku (viz.
sekci „Návštěvní řád / Kioskové nastavení“ v konfiguračním menu je zaměstnanec vyzván k zadání
PIN při ručním příjezdu nebo odjezdu.

Po výběru zaměstnance se objeví klávesnice s zprávou. Při kontrole docházky
„Pozor, (zaměstnanec) zadejte své číslo karty pro ověření“ se objevuje nad čísly.
Vyskočí text „Pozor, (zaměstnanec) Zadejte své číslo karty pro potvrzení transakce“.

Zadejte PIN na klávesnici a pak stiskněte tlačítko „OK“. Poté je zaměstnanec ověřen.
zda je účastník přítomen nebo nepřítomen, a zobrazí se potvrzující zpráva (viz <attendance/confirmation>).

.. obrázek: kiosky/zadat-pin.png
:alt:Pop-up okno, které se objeví při zadávání PIN kódu.

…účasti/potvrzení:

Potvrzující zpráva
--------------------

Při příchodu nebo odchodu zaměstnance se zobrazí potvrzující zpráva s informacemi o příchodu nebo odchodu.
informace.

Při přihlášení se zobrazí zpráva „Vítejte“ a datum.
a čas. Pokud zaměstnanec již ten den odpracoval určitý počet hodin, zobrazí se v poli :guilabel:`Hours
Dnes: Zpráva „HH:MM“ se také objevuje a ukazuje celkový počet hodin zaznamenaných dříve.

Při odhlášení se zobrazí „Dobrou noc (Zaměstnanec)“, datum a čas odhlášení.
Vyskočí okno s textem „Dnes otevřeno od“ a pod ním pole „Hodiny dnes: hh:mm“, kde je uveden celkový počet hodin.
minut strávených na cestě za den.

Pod oběma „vítáme“ a „dovolte nám, abychom vás pozdravili“ zprávami je tlačítko s nápisem „OK“. K opuštění obrazovky
Před stanovenou dobou v kiosku stiskněte tlačítko :guilabel:`OK`.

.. obrázek: kiosky/dopis-sbohem.png
:alt:Souhrn informací o odchodu zaměstnance, včetně jeho jména a příjmení.
