=========
Znalosti
=========

**Odoo Knowledge** je univerzální aplikace pro zvýšení produktivity, která umožňuje interním uživatelům obohatit
obchodní znalosti poskytováním informací, které jsou shromážděny individuálně nebo kooperativně.

Stránky, na kterých se shromažďuje obsah, se nazývají „články“. Hlavní částí článku je titulek
a tělo. Toto tělo je pole HTML obsahující text, obrázky, odkazy, záznamy z jiných modelů
šablony, atd.

.. viz též:
„Stránka produktu znalostí <https://www.odoo.com/app/knowledge>“

.. _znalosti/úpravy článků/vytvořit článek:

Tvorba článků
================

Článek můžete vytvořit od nuly nebo z přednastaveného šablonového vzoru.
je vytvářen pod jiným, původní článek je **rodičem článku**, zatímco nový se nazývá
*dítě* nebo *vnořený článek*, což naznačuje jeho podřízenou pozici. Tato struktura pomáhá organizovat
obsahem tím, že vytvoří jasné vztahy mezi příbuznými články.

Pro vytvoření složeného článku přejeďte myší nad článkem v bočním stromovém menu a klikněte na ikonu „+“
:guilabel:„(plus)“ ikonu.

Od nuly
------------

Pro vytvoření nového článku klikněte na tlačítko „Nový“ v pravém horním rohu nebo přejíždějte myší nad
Kategorie „Soukromé“ nebo „Práce“ v bočním stromu a pak klikněte na
Ikona „Plus“ (plus) ikona. Zadejte text nebo vyberte jednu z nabízených možností:

- Vyberte přednastavený šablonu a klikněte na „Nahrát šablonu“.
- :guilabel:`Vytvořit položku Kanban“: Vytvořte položky, které budete moci vizualizovat a spravovat v kanbanovém pohledu.
- :guilabel:`Vytvořit seznam položek“: Vytvořte strukturovaný seznam položek, abyste je mohli centrálně shromáždit na jednom místě.
článek.
- :guilabel:`Vytvořte kalendářní pohled na položky“: Vytvořte kalendářní pohled pro správu a sledování položek podle data.
- :guilabel:`Vytvořit článek pomocí umělé inteligence“: Vytváření obsahu na základě zadaného příkazu.

..tip:
Po napsání hlavičky klikněte nebo přejděte myší nad :guilabel:`Untitled` v horní liště.
automaticky pojmenovat článek podle nadpisu. Tato akce se neaplikuje, pokud je článek
již dříve oceněná.

Z šablony
---------------

Pro vytvoření článku podle šablony postupujte takto:

  #Klikněte na ikonu „malířské štětce“ v dolní části bočního panelu a poté vyberte šablonu.
  #Vyberte preferovaný šablonu.
  #Klikněte na tlačítko „Načíst šablonu“.

.. znalosti / články / editace článku:

Redakční úpravy
===============

Pro editaci článku vyberte jej v bočním stromu, poté upravte jeho obsah a formát pomocí
:ref:`nástrojová lišta textového editoru <knowledge/articles_editing/text-editor>“ a stiskněte klávesu
příkazů <znalosti/úprava článků/příkazy>“ a přidat obrázek „:obrázky“.
<znalosti/úprava_článků/obálka> s :ref:`titulem emodži <znalosti/úprava_článků/emoji>`.

.. znalosti/úpravy článků/textový editor:

Nástrojová lišta textového editoru
-------------------

Chcete-li upravit slovo, větu nebo odstavec, vyberte nebo klikněte na něj pro zobrazení textového editoru
nástrojovou lištu a použijte požadované formátování:

..tip:
Klikněte na ikonu „komentář“ ( ) pro přidání komentáře ke zvolenému textu.

.. znalostí / článků / příkazů:

Příkazy
--------

Zadejte znak /, abyste otevřeli :ref:`přístroj na výkon <essentials/html_editor/commands>“ a použijte příkaz.
následující příkazy jsou exkluzivní pro aplikaci Znalosti:

.. záložky::

... seznamová tabulka::
:šířky: 20 80
:hlavičkové řádky: 1
:sloupky: 1

         * – Příkaz
           - Užívání
         * --:guilabel:`Index
           - Zobrazit „vnořené články“:
dětské stránky hlavní stránky.
         * – :guilabel:`Kanban“
           - Vložte nástroj pro zobrazení kanbanu a vytvořte položky článku.
<slovo/povídání/údaje>.
         * --:guilabel:Karty položek
           - Vložte pohled na kartu a vytvořte :ref:`článek <knowledge/articles_editing/items>“.
         * :- guilabel:'Seznam položek'
           - Vložte seznam a vytvořte položky článku:ref:`<knowledge/articles_editing/items>`.
         * -- :guilabel:`Kalendář“
           - Vložte kalendářový pohled a vytvořte :ref:`článek.
<slovo/povídání/údaje>.

.. znalosti/úpravy článků/položky:

Článek
~~~~~~~~~~~~~

Článkové položky jsou aktivními stavebními bloky v článku, které umožňují přidávání, správu a
prohlížení různých organizovaných obsahů a dat.

Části článku v rámci nadřazeného článku mohou obsahovat vlastnosti
„<znalosti/úpravy článků/vlastnosti>“, které jsou sdílené pole dat ze strany rodiče, zajišťující
konzistentní informace mezi souvisejícími položkami a články.

.._znalosti/úpravy_článků/obálka:

Obrázek na obálce
--------------

Pro přidání obrázku na titulní stránku klikněte na ikonu :icon:`fa-ellipsis-v` :guilabel:`(ellipsis)` a poté
:guilabel:`Přidat obal“. Následující možnosti umožňují vybrat a vložit obrázky z různých
zdroje:

- Hledejte v databázi :doc:`Unsplash </applications/general/integrations/unsplash>“.
vhodné obrázky. Pokud je databáze a účet na Unsplash spojené, obrázek bude
Obrázek je automaticky vybírán podle názvu článku.
- :guilabel:`Přidat URL“: Vložte adresu obrázku.
- :guilabel:`Nahrát obrázek“: Nahrajte soubor do knihovny obrázků.

Pro správu obrázku na pozadí myší přejeďte nad ním a vyberte požadovanou možnost:

- :guilabel:`Nahradit obal“ a vyhledejte databázi nebo knihovnu, nebo přidejte jinou adresu URL.

- Přesuňte obrázek a upravte jeho polohu před kliknutím na „Uložit pozici“.

- :guilabel:`Odebrat obal“.

..._znalosti/úpravy_článků/emodži:

Emoji titulku
-----------

Přidat emotikon k názvu článku a nadpisu:

- Klikněte na ikonu „fa-ellipsis-v“ (zavináč) a poté klikněte na „Přidat ikonu“.
Vygenerovat náhodný emotikon. Klikněte na emotikon, abyste vybrali jiný.

- Alternativně můžete kliknout na ikonu „:icon:`fa-file-text-o` :guilabel:`(stránka)`“ vedle článku.
jméno v bočním panelu nebo horním panelu a vyberte preferovaný emotikon.

.. znalosti / články / úpravy / zobrazení:

Názory a odkazy z dalších aplikací
-------------------------------

Chcete-li do článku vložit pohled nebo odkaz na pohled, postupujte takto:

     #Přejděte do požadované aplikace a vyberte si preferovaný pohled.
     #Klikněte na ikonu „fa-cog“ a poté vyberte „Znalosti ->
Vložte obrázek do článku nebo: guilabel: Vložte odkaz do článku.
     #Vyberte článek, do kterého chcete vložit pohled nebo odkaz.

.. poznámka::
Jakmile je pohled nebo odkaz vložen,

   - Uživatelé bez přístupu k pohledu na něj v aplikaci Knowledge nemohou vidět, i když mohou získat přístup k
článek.
   - Kliknutím na vložený odkaz se zobrazí okno s názvem pohledu vedle
:ikonka_fa_clipboard (:guilabel_gui:"kopírovat"), :ikonka_fa_pencil_square_o (:guilabel_gui:"upravit") a
:ikona_fa_kladivo_rozbité(:guilabel_ikona_odstranění) ikony. Klikněte na jméno uvnitř okna, abyste otevřeli
propojený pohled.

Správa článků
==================

Znalost umožňuje správu článků, která se skládá z:
<poznatky/úprava článků/struktura>“, sdílení „<poznatky/úprava článků/sdílet>“
odstraněním (viz znalosti/úpravy článků/odstranění) a získáním
<znalosti/úprava článků/získání> je.

Základní řízení
----------------

Klikněte na ikonu „fa-ellipsis-v“ („guilabel:ellipsis“) a vyberte jednu z následujících akcí
pro základní správu článků:

- :guilabel:`Přesunout do“: Vyberte článek, který chcete přesunout pod kategorii nebo jiný článek, pak klikněte
:guilabel:`Přesunout článek“.
- :guilabel:`Zamknout obsah článku“: Zablokujte článek, aby se nedalo upravovat. Klikněte na :guilabel:`Odemknout“, abyste mohli znovu upravit.
- :guilabel:`Vytvořit kopii“: Kopie článku v sekci „Soukromé“.
- :guilabel:`Export“: Otevřete tiskárnu prohlížeče.
- :guilabel:`Odeslat do koše“: Přesunout článek do koše.

.. poznámka::
Tyto akce se vztahují pouze na :ref:`vnořené články
<knowledge/articles_editing/create-article> a :ref:`články


   - Převést do článku: Převést seznam článků na :ref:`článek

   - Převést na článek: Převést položku článku na :ref:`článek
<poznatky/clanky/vytvorit-clanek>.

..tip:
   - Přesouvejte články přímo ze sloupce stromu tahem a pádem pod jiný
článek nebo kategorii.
   - Stiskněte klávesu CTRL/CMD a poté zadejte ? pro vyhledání viditelných
články nebo za $:ref:`skryté články <knowledge/articles_editing/visibility>`.
Alternativně přejíždějte nad kategorií „Práce“ a klikněte na ikonu „Oko“.
ikona „Oko“ pro vyhledávání skrytých článků.

.. znalostí / článků / struktury:

Strukturování
-----------

Struktura bočního panelu
~~~~~~~~~~~~~~~~~

Struktura bočního panelu je hierarchická, s články rodičů a vnořenými články uspořádanými uvnitř
následujících kategoriích:

- Kategorie „Oblíbené“ zobrazuje všechny články označené jako oblíbené.
- Kategorie „Práce“ zobrazuje články přístupné všem interním uživatelům.
- Kategorie „Sdílené“ zobrazuje články, které byly sdíleny s konkrétními uživateli.
- Kategorie :guilabel:`Soukromé` zobrazuje soukromé články.

.. poznámka::
   - Chcete-li označit článek jako oblíbený a zobrazit kategorii „Oblíbené“, klikněte na
:ikonou „hvězda“ v horním pravém rohu nabídky.

Struktura článku
~~~~~~~~~~~~~~~~~

Články vložené do článku dědí přístupová práva svého rodiče.
:ref:`vlastnosti <knowledge/articles_editing/properties>` se aplikují na skupinu článků
pod stejným rodičem.

..._znalosti/úpravy_článků/sdílení:

Sdílení
-------

Sdílením článku se nastavují práva:ref:`<knowledge/articles_editing/rights>
zve :ref:`uživatele <knowledge/articles_editing/invite>`, poskytuje :ref:`on-line přístup
<znalosti/úprava článků/sdílení online>“, a určuje, zda se v :ref:`stromu na levé straně
<znalosti/úprava článků/struktura>.

Články uvedené v seznamu pod kategorií v bočním menu jsou **viditelné**. Články, které někteří uživatelé
musíte hledat v příkazovém paletě, protože mají omezené přístupové práva a jsou skryté.

.._znalosti/úpravy_článků/práva:

Nastavte přístupová práva
~~~~~~~~~~~~~~~~~~~~~~~

Klikněte na tlačítko „Sdílet“ v horním pravém rohu nabídky, abyste si mohli nastavit přístupová práva.

Výchozí přístupová práva
*********************

.. záložky::

...... seznamová tabulka::
:šířky: 20 80
:hlavičkové řádky: 1
:kolonky: 1

      * -Kulisy
        - Užívání
      * -- :guilabel:`Můžete upravit“
        - Umožněte všem uživatelům v rámci organizace upravovat článek.
      * --:guilabel:`Může číst“
        - Umožněte všem interním uživatelům číst pouze tento článek.
      * -- :guilabel:Přístup odepřen
        - Zamezte všem uživatelům přístup k článku v bočním stromu nebo vyhledávání.
nabídka příkazů.

... znalostí / článků / editaci viditelnosti:

Viditelnost
**********

.. záložky::

...... seznamová tabulka::
:šířky: 20 80
:hlavičkové řádky: 1
:kolonky: 1

      * -Kulisy
        - Užívání
      * :- guilabel:Každý
        - Článek je viditelný v bočním stromu pro všechny uživatele.
      * Členové
        - Článek je viditelný pouze v bočním stromu pro :ref:`povolané uživatele
<knowledge/articles_editing/invite>, zatímco ostatní uživatelé si jej mohou prohlédnout pomocí skrytých
vyhledávání článku stisknutím klávesové zkratky „CTRL“ / „CMD“ + „K“ a následným psaním znaku $.

.. poznámka::
   - Přednastavená oprávnění k přístupu se vztahují na všechny uživatele s interním účtem, s výjimkou pozvaných uživatelů.
Specifické přístupová práva mají přednost před výchozím nastavením.
   - Vybráním možnosti „Může upravovat“ nebo „Může číst“ v poli „Povolená práva“ přesune článek
do kategorie „Práce“ a výběrem možnosti „Žádný přístup“ se přesune do
:guilabel:`Soukromé“ kategorii, pokud není sdílena s uživatelem pozvaným na schůzku.
   - Nastavení „Viditelnost“ se vztahuje pouze na články z „Práce“.

.._znalosti/úpravy_článků/zveme:

Zveřejněte příspěvek na konkrétní uživatele
~~~~~~~~~~~~~~~~~~~~~

Povolit konkrétním interním nebo portálovým uživatelům přístup k soukromému článku nebo sdílet
Přiřaďte uživateli portálu článek s názvem „Práce“ takto:

#Klikněte na tlačítko „Sdílet“ v horním pravém rohu.
#Klikněte na tlačítko „Zvýšit“.
#Vyberte požadované oprávnění a přidejte uživatele do pole „Příjemci“.
#Klikněte na tlačítko „Zvýšit“.

.. znalosti/články/úpravy online:

Vytvořit adresu článku
~~~~~~~~~~~~~~~~~~~~

Klikněte na tlačítko „Sdílet“ a aktivujte přepínač „Sdílet na web“, abyste vytvořili odkaz.
ikonu „fa-clone“ („kopie“) pro kopírování adresy článku.

.. poznámka::
   - Pokud článek obsahuje :ref:`vložené názory <knowledge/articles_editing/views>“, uživatelé s
pokud nemohou přistupovat k vloženému obsahu, neuvidí URL.
   - Aplikace Webové stránky je nezbytná pro sdílení odkazu na článek.

.._znalosti/úpravy_článků/odstranit:

Odstranění
-------

Odstranění článku znamená jeho smazání nebo archivování.

Smazat článek
~~~~~~~~~~~~~~~~~

Vyberte článek v bočním stromu a klikněte na ikonku „:fa-ellipsis-v“ (:guilabel:„Ellipsis“)
ikonu, pak „Odeslat do koše“. Článek je po dobu 30 dnů přesunut do koše.
trvale smazané.

Pro trvalé smazání článku klikněte na tlačítko „Hledat“ v horním levém menu, vyberte článek a
a klikněte na:menu:"Akce --> Smazat --> Smazat".

.. poznámka::
Chcete-li obnovit smazaný článek, klikněte na tlačítko „Otevřít koš“ v dolní části bočního panelu.
strom, vyberte článek a klikněte na „Obnovit“. Nebo klikněte na „Hledat“
v horním levém menu. V poli pro vyhledávání klikněte na:menuselection:`Filtry --> Smazané“. Klikněte
článek, pak: „Obnovit“.

Archivovat článek
~~~~~~~~~~~~~~~~~~

Klikněte na tlačítko „Vyhledat“, vyberte článek a klikněte na „Akce > Archivovat“.
Archiv.

.. poznámka::
Chcete-li obnovit archivovaný článek, klikněte na tlačítko :guilabel:`Hledat`. V poli pro vyhledávání klikněte
:menu_selection:`Filtry --> Archivované“. Vyberte článek a přejděte na :menu_selection:`Akce -->
„Odarchivovat“.

.. znalosti/články/úpravy:

Vyhledávání
---------

Vyhledávání informací v článcích znalostní báze spočívá ve zjišťování jejich obsahu z různých aplikací Odoo nebo obnovením
Předchozí verze.

Přístup k článkům z různých aplikací
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Články znalostí jsou přístupné z formulářového pohledu :ref:`<studio/views/general/form>`.
Aplikace. Klikněte na ikonu „fa-bookmark“ v pravém horním rohu, abyste otevřeli
paletě příkazů, pak vyberte jednu z následujících metod hledání:

- :guilabel:`Hledání článku“: začněte psát text, abyste spustili semantickou vyhledávání.
identifikuje důležité informace o článku.
- „Vyhledávání pokročilé“: po zadání textu do vyhledávací lišty klikněte na „Pokročilé
„Vyhledávání“ provádí parametrický vyhledávací dotaz s možnostmi filtrování, seskupování nebo ukládání článků.

Historie verze
~~~~~~~~~~~~~~~

Chcete-li získat předchozí verzi článku, vyberte jej v bočním stromovém menu a klikněte na
Klikněte na ikonu „Historie“ (v levém horním rohu) a zobrazí se vám historie verze.
Vyberte verzi a klikněte na Restore history.

.. poznámka::
V historii verzí je v záložce „Obsah“ zobrazena vybraná verze.
:guilabel:`Srovnání“ panel zobrazuje rozdíly mezi předchozím a aktuálním článkem.
verze.

... znalostí / článků / vlastností:

Vlastnosti
==========

Vlastnosti jsou vlastní pole pro ukládání a správu informací, které mohou upravovat uživatelé s oprávněním „Může upravit“.
Přístupová práva můžete přidat do :ref:`vnořených článků
<znalosti/úprava_článků/vytvoření článku> nebo :ref:`článek
<znalosti/úprava článků/položky>.

Chcete-li přidat vlastnost, klikněte na ikonu „:icon:`fa-ellipsis-v`“ (:guilabel:`ellipsis`), pak
:menuselection:`Přidat vlastnosti --> Přidat vlastnost“, zadejte „Štítek“ a vyberte
:guilabel:`Typ pole“.

Chcete-li se dozvědět více o vlastnostech a polích typu, přejděte na :doc:`Vlastnosti
</aplikace/základní/vlastnosti/políčka/>.

.. poznámka::
  - Klikněte mimo pole vlastnosti, abyste uložili vlastnost.
  - Chcete-li odstranit vlastnost, přejděte na její název a klikněte na ikonu „fa-pencil“ („guilabel“ „pencil“)
ikona, pak klikněte na:menu-selection:"Smazat" --> "Smazat". Smazání vlastnosti je trvalé a
:Odstraněním všech vlastností se odstraní panel s vlastnostmi.

..tip:
  - Přejděte na položku vlastnosti a klikněte na ikonu „:icon:`fa-pencil`“ (:guilabel:„pencil“) pro úpravy.
nebo ikonu „OI-Draggable“ (ikona „táhlo“) pro přesun nad nebo pod jinou.
majetek.
  - Zatrhněte políčko „Zobrazit v kartách“ a zobrazte vlastnosti v pohledu na :ref:`položku článku
<znalosti/úprava článků/položky> viditelné z rodičovského článku.
  - Klikněte na ikonu „cogs“ (ikona „kolečko“) a skryjte boční panel vlastností.
a po návratu k článku se obrazovka znovu zobrazí.
