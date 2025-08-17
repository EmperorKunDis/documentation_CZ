========================
Sledování času na výrobní ploše
========================

.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`
.. |MOs| nahradit za:: :abbr:`MOs (Výrobní objednávky)`

Přihlášením do modulu Odoo Shop Floor jako „obsluha“ mohou zaměstnanci sledovat množství
Času, který stráví na každém pracovním příkazu.

Odoo sleduje čas potřebný k dokončení každé objednávky i čas strávený každým operátorem.
Na každém pracovním příkazu.

Přihlášení operátora
================

Přihlásit se do modulu Shop Floor jako obsluha, přihlaste se k databázi Odoo a otevřete
:menuselection:`Modul Shop floor“ a profil zaměstnance, který je přihlášen do databáze
je automaticky přihlášen jako operátor.

Všichni aktivní operátoři jsou uvedeni v levém panelu operátorů. Panel můžete
je možné otevřít nebo zavřít kliknutím na tlačítko „Zobrazit / skrýt panel“ (bílý čtverec s černou sloupcovou hlavicí).
tlačítko v pravém horním rohu modulu.

.. obrázek: shop_floor_tracking/operator-panel.png
:align:center
:alt: Panel operátora v modulu Výroba s tlačítkem pro zobrazení/skrytí nad ním.

Přihlaste se do obchodu jako jiný zaměstnanec kliknutím na tlačítko „+ Přidat operátora“ v
spodní části panelu. To otevře okno „Vybrat zaměstnance“, které obsahuje
každý zaměstnanec, který se do modulu může přihlásit.

Klikněte na konkrétního zaměstnance, abyste se přihlásili pomocí jeho profilu. Pokud není potřeba heslo k přihlášení
Pokud je tento zaměstnanec uživatelem profilu, bude se automaticky podepisovat.

Pokud je vyžadován PIN kód, zobrazí se okno „Heslo?“ s číselnou klávesnicí.
Kód můžete zadat na numerické klávesnici a poté kliknout na tlačítko „Potvrdit“.
Přihlaste se do modulu Shop Floor*.

.. obrázek: shop_floor_tracking/pin-code.png
:align:center
:alt:Okno „Heslo?“, které slouží k zadání operátorského PIN kódu.

.. poznámka::
Každému zaměstnanci lze nastavit vlastní kód PIN, který musí být při každém přihlášení zadán.
modul Shop Floor, zaevidovat nebo vyskladnit v režimu Kiosk v aplikaci Attendance.
se přihlásit jako pokladní v aplikaci Point of Sale.

Chcete-li nastavit zaměstnanecký PIN, přejděte do aplikace „Zaměstnanci“ a vyberte konkrétního zaměstnance.
zaměstnance. Na spodní části formuláře pro zaměstnance klikněte na záložku :guilabel:`Nastavení HR`,
Zadejte číselný kód do pole „PIN“.

Jakmile je zaměstnanec přihlášen do modulu, jeho jméno se zobrazí na obslužném panelu spolu s
každý další zaměstnanec, který se přihlásil. Panel může zobrazovat více zaměstnanců, ale pouze jeden
Zaměstnanec může být aktivní v jakémkoliv okamžiku na jediném instanci modulu Shop Floor.

Klikněte na jméno zaměstnance, aby se profil aktivoval. Aktivní zaměstnanec je zvýrazněný
modře, zatímco jména zaměstnanců, kteří jsou podepsaní, ale neaktivní, jsou vybledlá.

K odhlášení konkrétního zaměstnance z modulu klikněte na tlačítko vedle
jejich jméno na ovládacím panelu.

Doba trvání prací na kolejích
=========================

Chcete-li sledovat čas strávený prací na objednávce, začněte výběrem zaměstnance, který ji zpracovává.
přístrojová deska.

Poté přejděte na stránku pracovního centra, kde má být práce prováděna.
Toho lze dosáhnout výběrem pracovního centra z horní navigace v modulu Shop Floor nebo
kliknutím na název pracoviště v kartě výrobního příkazu (VPO).
je součástí.

Na stránce pracovního centra najděte kartu pro objednávku práce. Jakmile začne pracovat, klikněte na
hlavičku objednávky práce, aby se začalo měřit doba trvání jejího provedení. Tato doba
zobrazené na hlavičce karty pracovního příkazu, která sleduje celkový čas strávený
v rámci pracovního úkolu všemi zaměstnanci.

.. obrázek: shop_floor_tracking/work-order-timer.png
:align:center
:alt:Pracovní karta s aktivním časovačem.

Dále se na ovládacím panelu objevuje číslo pracovního příkazu pod názvem
zaměstnanci pracující na něm, společně s druhým časoměřičem, který sleduje množství času, které zaměstnanec
za práci na objednávce. Tento časový údaj pouze odráží práci vykonanou v rámci aktuální
pracovní úvazek, i když zaměstnanec dříve pracoval na příkazu k práci.

Zaměstnanci mohou pracovat na více zakázkách současně a sledovat čas strávený na každé z nich.
Referenční číslo každé pracovní objednávky, která je v daném okamžiku zpracovávána, se zobrazuje pod jménem zaměstnance.
s časovačem.

.. obrázek: shop_floor_tracking/employee-timer.png
:align:center
:alt:Zaměstnanecká karta v ovládacím panelu s dvěma časovači pracovních úkolů.

Zastavit časovač na kartě pracovního příkazu a odstranit pracovní příkaz pod jménem zaměstnance.
Druhý klik na hlavičku v ovládacím panelu.

Jakmile je objednávka dokončena, klikněte na tlačítko „Uzavřeno“ v dolní části
pracovní kartička, která způsobuje, že se karta ztrácí. Pokud je časovač stále aktivní, zastaví se
karta zmizí úplně.

Zobrazení doby trvání pracovního úkolu
========================

Pro zobrazení doby trvání pracovního příkazu přejděte na: „Výrobní aplikace“ → „Operace“.
Vyberte „Výrobní objednávky“ a poté vyberte |MO|.

Zobrazit a vybrat |MOs|, které byly dokončeny a označené jako *Dokončeno*: odstraňte štítek „Co dělat“.
filtr z vyhledávací lišty pomocí tlačítka „X“
pravé straně filtru.

Na stránce pro |MO| klikněte na záložku „Pracovní příkazy“ a zobrazí se vám seznam všech pracovních příkazů.
zahrnuty v MO. Čas na dokončení každé objednávky je zobrazen v
Sloupec „Skutečná doba“.

Skutečná doba je celková doba, kterou pracovníci strávili na zakázce.
na ní pracovaly. Zahrnuje dobu zaznamenanou v modulu Shop Floor a také dobu zaznamenanou na
:guilabel:„Pracovní příkazy“ vlastního |MO|.
