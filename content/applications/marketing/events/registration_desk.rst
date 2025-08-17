=================
Příjem hostů
=================

Použijte funkci „Přístup k registračnímu stolu“ v aplikaci Odoo Events, abyste udělili přístup registrovaným účastníkům akce.
a ukládat do reportovacích metrik údaje o návštěvnících.

Stránka registrace
======================

Na mobilním zařízení otevřete aplikaci „Události“ v aplikaci Odoo nebo v prohlížeči.
Klikněte na tlačítko „Pult registrace“ pro zobrazení stránky „Pult registrace“.

.. obrázek: registrační pult/registrační pult stránka.png
:align:center


Na konci položky „Přihlášení“ jsou možnosti buďto :guilabel:`Naskenovat
známka nebo: guilabel: vyberte účastníka.

Prosím, přiložte štítek.
============

Naskenujte kódy přítomné na náramcích účastníků akce, přejděte do aplikace „Akce“ a vyberte možnost
Přístup k registračnímu stolu“, vyberte možnost „Skenování štítku“.

.. důležité:
Odoo **musí mít přístup k fotoaparátu, který je používán pro možnost „Skenování čipové karty“
pracovat.

Jakmile má Odoo přístup k fotoaparátu, objeví se okno „Barcode Scanner“ s
pohledu kamery. Dále je zde přítomen také určený box pro hledáček, jehož velikost lze
ručně upraveno tak, že se použije ikonka „fa-crop“ a „(crop)“.

.. obrázek:registration_desk/barcode-scanner-window.png
:align:center
:alt:Okno skenování čárového kódu na pokladně registrace v aplikaci Odoo Events.

Když je kód na středu hledáčku, kód se snímá a
Pop-up okno „Čtečka čárových kódů“ zmizí a účastník je připuštěn do
Akce. Po naskenování kódu je zaznamenána jejich účast v aplikaci Events na platformě Odoo.

Pokud je skenovaný čárový kód neplatný, objeví se v pravém horním rohu chybové hlášení.

Vyberte účastníka
===============

Přístup k událostem můžete ručně povolit, pokud se přepnete na:
Přístup k registračnímu stolu“, a vyberte možnost „Vybrat účastníka“.

Odoo odhaluje stránku „Účastníci“, kde jsou uvedeni všichni účastníci každého události v databázi.
v výchozím nastavení v zobrazení „Kanban“ :guilabel:`Kanban`.

.. obrázek:registration_desk/attendees-page.png
:align:center
:alt:Stránka účastníků prostřednictvím registračního stolku v aplikaci Odoo Events.

Na stránce „Účastníci“ se na každé kartě účastníka zobrazí jméno tohoto člověka a událost, na které byl.
zaregistrovali se na něj, jejich spojená společnost (pokud je to vhodné) a jaký typ vstupenky si zakoupili.
(pokud je k dispozici), spolu s dvěma tlačítky: :icon:`fa-check` :guilabel:`(checkmark)`
:icon:`fa-undo` :guilabel:`(směr hodinových ručiček).

Povolit přístup k osobě, která je označena jako přítomná, stiskněte ikonu „fa-check“.
Tlačítko „Zkontrolovat“ na kartě daného účastníka.

Klikněte na tlačítko „fa-undo“ (symbol protisměrného šipky) v kartě účastníka, abyste zrušili
předchozí akce.

..tip:
Doporučuje se používat filtr specifický pro danou událost na stránce „Účastníci“ pomocí
vyhledávací lišta.

Pro toto klikněte vedle vyhledávací lišty na ikonu „sestupný řádek“ (zprava dolů).
zobrazí se rozbalovací nabídka s položkami „Filtry“, „Skupiny“ a „Oblíbené“.
možnosti.

Příkladem je například kliknutí na možnost „Událost“ v sloupci „Skupina“. Poté klikněte
odstranit rozbalovací nabídku. Odoo zobrazí stránku „Účastníci“ s
sloupce specifické pro události, které umožňují uživatelům najít konkrétní účastníky události.

.. viz též:
:doc:`../základy/vyhledávání`
