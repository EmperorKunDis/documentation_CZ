======
Poplachy
======

V aplikaci *Příjemce* lze zveřejnit zprávu, tzv. „upozornění“.
horní část panelu, kde se uživatelé mohou dozvědět důležité informace.

Poplachy zůstávají na hlavním panelu *Přesměrování* po dobu, kterou je možné nastavit v
individuální upozornění.

.. obrázek: varování/varovani.png
:align:center
:alt: Nad fotografií uživatele se objeví dvě výstražná upozornění.

Vytvořit upozornění
===============

Vytvářet upozornění mohou pouze uživatelé s oprávněním „Administrátor“ pro aplikaci „Nábor“.
Pro přidání nové výstrahy přejděte do aplikace „Příkazy“ – „Konfigurace“ – „Výstrahy“.

Klikněte na tlačítko „Nový“ pro otevření prázdného formuláře varování. Vyplňte následující informace v tomto formuláři:

- :guilabel:`Datum od“: datum, kdy se upozornění zobrazí. Na tento den je upozornění viditelné na
dashboard.
- :guilabel:`Datum ukončení“: datum, kdy uplyne lhůta pro zobrazení varování. Po tomto datu se varování skryje.
- :guilabel:Společnost: tato pole vyplňuje aktuální společnost, výchozí hodnotou je. Chcete-li změnit společnost
upozornění se zobrazí pro, vyberte požadovanou společnost ze seznamu v tomto
pole.

Pokud tento pole zůstane prázdné, upozornění bude viditelné pro všechny uživatele s přístupem k položce *Reference*.
aplikace.

Pokud je uvedena společnost, zobrazí se pouze uživatelé v této společnosti (kteří také mají přístup k položce *Zakázky*).
(viz upozornění). Toto pole se zobrazuje pouze v případě, že je databáze více společností.
- Zadejte text pro upozornění: Tento text se zobrazí uvnitř pásu s upozorněním.
hlavní přehled *Příkazy*.
- :guilabel:"Po kliknutí": Upozornění má tři možnosti, vyberte si příslušný přepínač vedle
požadované výběru. Možnosti jsou:

  - :guilabel:"Není kliknutí": varování zobrazuje pouze text, nikoliv odkaz na kliknutí.
  - :guilabel:"Přejít na všechny pracovní nabídky": upozornění obsahuje odkaz, který vás přesměruje na
webová stránka s aktuálními pracovními pozicemi.
  - :guilabel:"Uveďte URL": varování obsahuje odkaz na konkrétní URL, který se otevře po kliknutí.
Naviguje na tuto adresu URL. Když je vybrána, objeví se pod ní pole pro zadání :guilabel:`URL`.
Klikněte na položku „URL“. Do pole vložte požadovanou adresu URL.

.. obrázek: varovani/varovani-formular.png
:align:center
:alt:Formulář s upozorněním, který je úplně vyplněný a všechny volby jsou zadány.

Zrušit upozornění
================

Je možné odhlásit se z oznámení, pokud uživatel nechce vidět konkrétní upozornění znovu.

K odstranění upozornění klikněte na ikonu :icon:`fa-times` :guilabel:`(odstranit)` v pravém horním rohu
upozornění na odstranění upozornění z palubní desky.

Tím se zamezí tomu, aby se upozornění znovu neobjevilo, i když je otevřena aplikace *Příkazy*.
první v nové sezóně.
