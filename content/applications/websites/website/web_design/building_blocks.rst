Zobrazit obsah

===============
Stavební bloky
===============

Webové stránky si můžete navrhnout tak, že budete „táhnout a pustit“ bloky.
„<website/building_blocks/add>“, pak je upravte „<website/building_blocks/edit>“ tak, aby odpovídaly vašim
obsah a grafické zpracování.

.. viz též:
„Návod k Odoo: Vytvořte si vlastní webové stránky: text a barvy <https://www.odoo.com/slides/slide/design-your-website-text-and-colors-6930?fullscreen=1>“

... _webové stránky/stavební bloky/přidat:

Přidejte blok
====================

Přidat blok na webovou stránku lze tak, že se připojíte k stránce, klikněte na „Upravit“ a
Přetáhněte a vložte požadovaný blok do příslušné polohy. Existují dva typy bloků
jsou k dispozici: „Kategorie“ a „Vnitřní obsah“.
bloky stavebních kamenů lze přidávat pouze do bloků kategorií.

Když kliknete na blok kategorie, objeví se vyskakovací okno, které vám umožní vybrat mezi několika
šablony pro každou kategorii.

..tip:
Můžete také vyhledávat konkrétní blok v okně „Vložit blok“ pomocí tlačítka
hledání.


:alt: Výběr blokování pop-up

Jakmile je kategorie umístěna, můžete přetahovat a vkládat bloky „Vnitřní obsah“
V něm. Bloky „Vnitřní obsah“ umožňují přidat prvky, jako jsou videa, obrázky
tlačítka sociálních sítí a podobně do stávajících kategorií.

.. poznámka::
Přístup k některým blokům vyžaduje instalaci příslušné aplikace nebo modulu
(např. elektronický obchod pro blok produktů).

Příklad:
Přidejte všechny své účty na sociálních sítích do jednoho místa se vnitřním obsahem:guilabel: Sociální média
blok. Přepněte přepínač vedle požadované platformy na nebo z a vložte svou adresu URL účtu.

.... obrázek: building_blocks/social-media-inner-content.png


... _webové stránky/stavební bloky/formulář:

Tvar
----

Blok Form slouží k získávání informací od návštěvníků webu a vytváření záznamů.
v případě, že je databáze dostupná.

.. obrázek: building_blocks/form-block.png
:alt: Příklad bloku formuláře

Akce
~~~~~~

Výchozí nastavení je takové, že při odeslání formuláře obsahuje e-mail informace zadané návštěvníkem
je automaticky odeslána. V závislosti na aplikacích nainstalovaných ve vaší databázi mohou být k dispozici další akce.
automaticky vytvořené záznamy se mohou stát dostupnými. Chcete-li zvolit jiný postup, klikněte
Klikněte na tlačítko „Upravit“, vyberte formulář a přejděte do záložky „Nastavení“.
:guilabel:`Akce“:

- :guilabel:`Přihlásit se k práci“ (:doc:`Nabídka pracovních míst </applications/hr/jobs>`)
- :guilabel:`Vytvořit zákazníka“ (:doc:`E-commerce <../../ecommerce>`)
- :guilabel:`Vytvořit požadavek“ (:doc:`Pomocná služba </applications/services/helpdesk>`)
- :guilabel:`Vytvořit příležitost“ (:doc:`CRM </applications/sales/crm>`)
- :guilabel:`Přihlásit se k odběru newsletteru“ (:doc:`E-mailový marketing </applications/marketing/email_marketing>`)
- Vytvořit úkol (:doc:`Projekt </applications/services/project>`)

.. obrázek: stavebni-bloky/vnitrni-obsah-editaci-formular.png
:alt:Upravit formulář, aby měnil jeho akci

Výchozí stav je takový, že po odeslání formuláře se návštěvníci přesměrují na stránku „Děkuji“. Použijte :guilabel:`URL`.
stránku, na kterou chcete uživatele odeslat. Můžete také zvolit možnost neodkazovat a ponechat
na stránce formuláře volbou „Nic“ nebo „Zobrazit zprávu“.
:guilabel:„Úspěch“

Pole
~~~~~~

Přidat nový prvek do formuláře můžete v záložce „Upravit“ kliknutím na
:guilabel:`+ pole“ tlačítko vedle sekce „Formulář“ nebo „Pole“. Chcete-li upravit
Vyberte nový (nebo jakýkoli jiný) prvek na formuláři a poté použijte možnosti dostupné v
V sekci „Pole“ karty „Nastavení“. Například můžete:

- Změňte pole :guilabel:`Typ`.

..tip:
Je také možné vybrat pole z databáze a použít data
Závisí na zvolené akci. Položky vlastností přidané do formuláře závisí na vybrané akci.
Databáze lze také použít.

.. spoiler::Klikněte zde pro náhled všech typů polí.

....... obrázek:: building_blocks/all-types-of-field.png
:alt:Všechny typy polí

Některá pole jsou vizuálně podobná, ale do nich musí být zadány specifické údaje.

- Upravte pole :guilabel:„Štítek“ a přizpůsobte jeho :guilabel:„Pozici“.
- Zapněte pole: guilabel:'Popis'. Klikněte na výchozí popis v formuláři, abyste jej upravili.
- Přidejte :guilabel:`Zástupný symbol“ nebo :guilabel:`Výchozí hodnotu“.
- Uveďte, zda pole je povinné.
- Upravte nastavení viditelnosti pole :doc:`<visibility>`.
- Přidejte animace.

Jakmile provedete požadované změny, klikněte na tlačítko :guilabel:`Uložit“.

... _webové stránky/blok/vložení kódu:

Vložit kód
----------

Vložený kód umožňuje integrovat obsah z webových stránek třetích stran do stránky, například videa
z YouTube, mapy z Google Map, příspěvky ze sociálních sítí (Instagram, Facebook) atd.

Po přidání bloku na stránku klikněte na blok, pak přejděte na záložku „Upravit“ (viz obrázek)
Klikněte na tlačítko „Upravit“ a nahraďte místní kód svým vlastním kódem pro vložení.

.. obrázek: building_blocks/embed-code-pop-up.png
:alt:Přidejte odkaz na vložený kód, který chcete označit

.. varování:
Nekopírujte a nevkládejte kód, který nerozumíte, protože by mohl ohrozit vaše data.

.. _webové stránky/bloky staveb/přesunout, vyměnit, přepnout, odstranit:

Přesunout, vyměnit nebo smazat blok
========================================

Přetáhněte modré okraje bloku, abyste zvětšili nebo zmenšili prostor na jeho vrcholu nebo dně.

Změňte pořadí bloků kliknutím na ikonu „nahoru“ (:guilabel:"chevron up") nebo
: ikonu „svislý znak“ (:guilabel:„svislý znak“) a přesouvat blok na stránce kliknutím
Ikona „:icon:`fa-arrows`“ („:guilabel:`arrows`“). Když máte více sloupců,
<webová stránka/bloky stavby>, posunout sloupec doprava nebo doleva kliknutím
:icon:`fa-chevron-left` (:guilabel:`chevron left`) nebo :icon:`fa-chevron-right`
(:guilabel:`chevron right`).

Pro smazání bloku klikněte na ikonu „koš“ (:guilabel:"trash").

.... obrázek:: building_blocks/padding-building-block.png
:alt: Rozšířit okraje bloku

..tip:
Rychle změňte kategorii bloku klepnutím na ikonu :icon:`fa-exchange` (:guilabel:`exchange`).

.. _webové stránky/bloky/upravit:

Upravit blok
=====================

Pro úpravu obsahu bloku klikněte na něj a přejděte do záložky „Upravit“.
Možnosti nastavení se liší v závislosti na typu bloku, který byl vybrán.

.. viz též:
   - :doc:`Elementy webdesignu <elements>`
   - :doc:`Dostupnost <dostupnost>`

Pozadí
----------

Pro změnu pozadí bloku vyberte blok, přejděte na záložku „Upravit“ a
a klikněte na barevný bod nebo jinou možnost „Pozadí“ . Můžete změnit
barvu nebo přidat obrázek, video a/nebo tvar. Jakmile si vyberete tvar, objeví se nové pole
umožní vám přizpůsobit tvar.

..tip:
   - Umístěte prvek (obrázek, text atd.) za nebo před jiným pomocí
:guilabel:"Odeslat dozadu" nebo :guilabel:"Přiblížit".

.. obrázek: building_blocks/move-block-position.png
:alt: změna pozice bloku

   - Pro změnu velikosti bloku klikněte a přetáhněte body na jeho okrajích tak, jak je potřeba.

.. obrázek:: adapt-block-size.png
:alt:Adaptuj velikost bloku

.. viz též:
:doc:`Obecný motiv <themes>`

Uspořádání: mřížka a sloupce
------------------------

Pro většinu bloků můžete zvolit mezi dvěma stylem uspořádání: :ref:`grid
nebo :ref:`sloupce (kolonky) <website/building_blocks/cols>“.
výchozí styl uspořádání, klikněte na blok, přejděte do záložky „Nastavení“ a nastavte
V poli „Šablona“ nastavte hodnotu na „Řádky“ nebo „Sloupce“.

... _webové stránky/stavební bloky/mřížka:

Síť
~~~~

Vyrovnávací panel Grid vám umožní přesouvat a měnit velikost obrázků nebo textu.
je možné je přetahovat a kladením na místo. Když je vybrána volba „Síť“, jsou k dispozici další možnosti
Klikněte na „Obrázek“, „Text“ nebo „Tlačítko“.

.. obrázek:: building_blocks/grid-layout.png
:alt:Při výběru sítě zvolte obrázek a pomocí táhla jej přetáhněte tam, kde je potřeba.

... _webové stránky/bloky stavebních kamenů/sloupce:

Kolony
~~~~

Volbou rozložení „Sloupce“ lze určit, kolik prvků je na řádku.
blok. Chcete-li tak učinit, vyberte blok, který chcete upravit, a klikněte na rozbalovací nabídku vedle :guilabel:`Sloupce`
pole a upravte počet. Poté můžete upravit konkrétní sloupec pomocí možností
sekci „Sloupec“ v záložce „Nastavení“.

.. poznámka::
Výchozí nastavení je takové, že na mobilních zařízeních je viditelné pouze jedno pole (sloupec) na řádku.
aby obsah zůstal snadno čitelný a přístupný na menších obrazovkách.
hodnotu, klikněte na ikonku „mobil“ (vlevo nahoře)
a přizpůsobit počet sloupců. Tvar je skrytý v mobilním zařízení výchozím nastavením.

.. _webové stránky/stavební bloky/duplikát:

Duplikovat blok
==========================

K opakování bloku klikněte na ikonu nahoře vpravo
Nastavení“ záložku. Jakmile je kopie vytvořena, nový blok se objeví na stránce pod tím původním.
originální verze.

.. _webové stránky/bloky/vlastní:

Uložte si vlastní blok
============================

Můžete si uložit vlastní blok pro jeho další použití jinde. Pro vybrání klikněte na
kartě „Nastavení“ a klikněte na ikonu „Floppy Disk“ (ikona „CD“).
Klikněte na tlačítko „Uložit a načíst“ v okně prohlížeče, abyste potvrdili uložení vašeho vlastního bloku.

Chcete-li přidat uložený blok na stránku, přejděte do záložky „Bloky“ a vytáhněte jej tam.
blok „Vlastní“ z sekce „Kategorie“. V okně, které se otevře, klikněte
požadovaný blok v kategorii „Vlastní“.

..tip:
V okně „Vložení bloku“ klikněte na ikonu „tužka“ (viz. „Upravit“) pro přejmenování bloku.
vlastní blok nebo ikonu „koš“ (label „smazat“) pro jeho smazání.

... webové stránky / stavební bloky / odkaz:

Vytvořte odkaz na určité místo.
=====================

Hypertextové odkazy na kotvu jsou hypertextové odkazy, které uživatele přesměrují na **konkrétní část** stránky.
Pokud chcete vytvořit odkaz na blok, postupujte takto:

#Klikněte na tlačítko „Upravit“ a vyberte blok, který chcete propojit.
#Klikněte na ikonu „fa-link“ (viz níže) v horním rohu záložky „Upravit“.
#Chcete-li upravit výchozí název kotvy, klikněte na tlačítko „Upravit“ v zeleném okně s hláškou.
#Změňte název kotvy a klikněte na tlačítko „Uložit a zkopírovat“.

Jakmile je kotva zachráněna, můžete ji odkázat z jakéhokoliv místa na svém webu.
webové stránky.
