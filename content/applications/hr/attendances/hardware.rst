========
Hardware
========

Zaměstnanci, kteří nejsou uživateli databáze a nemají tedy přístup
Aplikace „Přítomnost“ musí zaměstnanci při příchodu do práce používat kiosky. Následující jsou fyzické
požadavky na zřízení stánku.

Kioskové zařízení
=============

Kiosek je samoobslužná stanice, kde zaměstnanci mohou:
<attendance/kioskový vstup> s buďto štítkem <attendance/hardware/badges>, nebo
:ref: „klíčenka RFID <attendance/hardware/rfid>“. Tyto zařízení jsou obvykle vyhrazena jako kiosky
jenže jako kiosk lze nastavit jakýkoliv přístroj s prohlížečem.

Kiosek se používá pro navádění na webovou stránku, která je uvedena v konfiguraci
sekci „Návštěvy“ aplikace Attendances.

Kiosky jsou vybaveny jedním z následujících zařízení:

- Laptop nebo stolní počítač
- Tablet
- Mobilní telefon (Android nebo iOS)

.. tip::
Dotykové obrazovky jsou snadno použitelné a tablety i mobilní telefony zabírají méně místa. Proto je většina
Zvažte použití menšího zařízení s dotykovým displejem jako informačního kiosku.

Doporučuje se umístit stánek na bezpečný stojan nebo jej pevně připevnit ke zdi.

...přítomnost/hardware/štíty:

Štítky
======

Značky jsou způsobem, jakým zaměstnanci mohou rychle přihlásit a odhlásit se z kiosku, protože značky jsou skenovány
Kamera v kiosku identifikuje zaměstnance.

Chcete-li vytvořit štítek, nejprve přejděte do aplikace „Zaměstnanci“ pomocí odkazu „Employees“. Následně klikněte na
Potřebujete kartu zaměstnance pro otevření formuláře pro zaměstnance, pak klikněte na záložku „Nastavení“.

V sekci „Účast/Prodej/Výroba“ je podnadpisem „Štítek“.
„ID“ pole. Pokud je pole prázdné, klikněte na „Vytvořit“ v konci pole „Špatný identifikátor“.
linie a pole se automaticky vyplní novým číslem identifikačního štítku. Pak klikněte
:guilabel:`Tisk štítku“ na konci čísla identifikačního štítku, abyste vytvořili soubor ve formátu PDF s tímto štítkem.

Pokud je na formuláři uživatelů již číslo identifikačního štítku, nebude k dispozici tlačítko „Vytvořit“.
tlačítko, pouze tlačítko „Tisk štítku“.

Zaměstnanecká karta obsahuje fotografii zaměstnance, jeho jméno, pozici ve firmě, loga společnosti a čárový kód.
, který lze naskenovat na přepážce při příjezdu i odjezdu.

Štítky lze vytisknout na jakémkoliv termo nebo inkoustovém tiskárně pro zaměstnance.

.. obrázek::hardware/badge.png
:alt:Štítek pro zaměstnance, který vznikl z aplikace Zaměstnanci.

.. poznámka::
Kartičky nejsou nutné, protože zaměstnanci se mohou identifikovat na kiosku ručně.

Čtečky čárových kódů
----------------

Při použití štítků k přihlášení a odhlášení musí být skenován čárový kód, aby bylo možné identifikovat zaměstnance.
Můžete to udělat pomocí kamery na kiosku, pokud je dostupná na zařízení.

Pokud není kamera dostupná na zařízení kiosku, musí se použít externí čtečka čárových kódů.
snímat čipy.

Kiosky pracují s většinou USB čteček čárových kódů. Podporovány jsou také bezdrátové čtečky čárových kódů přes Bluetooth.
Pokud chcete zařízení bez portů USB nebo pokud chcete bezdrátový přenos.

Postupujte podle pokynů výrobce na čárovém kódu skeneru, abyste správně připojili čárový kód.
snímač do zařízení na prodejním místě.

.. tip::
Pokud je čtečka čárových kódů připojena přímo k počítači, musí být konfigurována.
<../../inventory_and_mrp/barcode/setup/hardware> pro použití klávesnice počítače.

.. poznámka::
IoT box není nutný k použití čtečky čárových kódů.

…přítomnost/hardware/RFID:

Čtečky klíčenek s RFID čipem
====================

Místo použití „špatného“ štítku (:ref:`<attendance/hardware/badges>`) mohou zaměstnanci skenovat osobní RFID
klíčenka s čtečkou RFID k ověření příchodu a odchodu z práce.

Pro použití této metody je nutné zakoupit oba RFID klíčenky a čtečku RFID.
vpřed a vzad. Postupujte podle pokynů výrobce při instalaci čtečky RFID a nastavení RFID klíče
FOB.

.. poznámka::
IoT box není **nutný** pro používání klíčů s čipem.
