..._frontend/komponenty:

==============
Součástky sovy
==============

Odoo JavaScriptový rámec používá vlastní komponentovou knihovnu nazvanou Owl.
je deklarativní komponentový systém inspirovaný Vue a React. Komponenty
jsou definovány pomocí :doc:`QWeb šablon <qweb>`, doplněných některými OWL
konkrétními pokyny. Oficiální
Dokumentace „Sova“ (<https://github.com/odoo/owl/blob/master/doc/readme.md>).
obsahuje kompletní odkazovou stránku a návod.

.. důležité:

Přestože kód najdeme v modulu web, je udržován samostatně.
samostatný GitHub repozitář. Každá změna v Owlu by tedy měla být provedena
přes požadavek na aktualizaci v repozitáři https://github.com/odoo/owl.

.. poznámka::
Aktuálně všechny verze Odoo (od verze 14) používají stejnou verzi Owlu.

Použití komponent Owl
====================

„Soubor dokumentace pro Owla“_ již podrobně popisuje rámec Owl, takže
Stránka bude obsahovat pouze informace specifické pro Odoo. Ale nejprve se podíváme na to, jak
může vytvořit jednoduchou složku v Odoo.

... kódový blok: JavaScript

import { Komponenta, XML, použítStav } z '@odoo/owl';

klas MyComponent prodlouží třídu Component
statická šablona = XML
<div t-on-click="zvýšit">
<t t-esc="state.value">
</div>
        `;

setup() {
tento.state = useState({ hodnota: 1 });
        }

increment() {
this.state.value++;
        }
    }

Toto je příklad, který ukazuje, že Owl je k dispozici jako knihovna v globálním prostoru jmen
„sova“: může být použita jako většina knihoven v Odoo. Poznámka:
definovali zde šablonu jako statickou vlastnost, ale bez použití „static“
klíčové slovo, které není dostupné v některých prohlížečích (kód JavaScriptu Odoo by měl
musí být v souladu s ECMAScriptem 2019).

Definujeme zde šablonu v JavaScriptovém kódu pomocí XML.
pomocníkem. Je však užitečný pouze pro zahájení práce. Ve skutečnosti
Odoo by měl být definován v XML souboru, takže může být přeložen. V tom případě
komponenta by měla definovat pouze název šablony.

V praxi by mělo být většina komponent definována dvěma nebo třemi soubory, které jsou umístěny na stejném místě.
místo: soubor JavaScriptu (my_component.js), šablonový soubor (my_component.xml)
a volitelně soubor s příponou .sass (.css) („my_component.sass“). Tyto soubory by měly
Pak se přidá do nějakého balíčku aktiv, a pak se o něj postará webový rámec.
načítání souborů JavaScriptu a CSS a načítání šablon do Owla.

Takto by měla být definována komponenta výše:

... kódový blok: JavaScript

import { Component, useState } od „@odoo/owl“;

klas MyComponent prodlouží třídu Component
statický šablona = "myaddon.MyComponent";

        ...
    }

A šablona je nyní umístěna v příslušném souboru XML:

... blok kódu::xml


<šablony xml:space="preserve">

<t t-name="myaddon.MyComponent">
<div t-on-click="increment">
<t t-esc="stát.hodnota"/>
</div>


</šablony>

.. poznámka::

Názvy šablon by měly následovat konvenci „addon_name.ComponentName“.


.. viz též:
    - „Repozitář sovy <https://github.com/odoo/owl>“

... _frontend/owl/best-practices:

Nejlepší postupy
==============

Prvně je třeba říct, že komponenty jsou třídy, takže mají konstruktor. Ale konstruktory
Jsou speciální metody v JavaScriptu, které nelze nijak převzít.
je občas užitečný vodítko pro Odoo. Musíme se ujistit, že žádný komponent
v Odoo se přímo používá metoda konstruktoru. Komponenty by měly používat
Metoda setup:

... kódový blok: JavaScript

    // correct:
klas MyComponent prodlouží třídu Component
setup() {
            // initialize component here
        }
    }

    // incorrect. Do not do that!
třída NeplatnýKomponent rozšiřuje třídu Komponent.
constructor(parent, props) {
            // initialize component here
        }
    }

Další dobrou praxí je používat konzistentní konvenci pro názvy šablon:
`addon_name.ComponentName`, což zabraňuje kolizi názvů mezi odoo doplňky.

Seznam použité literatury
==============

Webový klient Odoo je postaven na komponentech „Owl“ (https://github.com/odoo/owl).
Pro usnadnění práce poskytuje rámec Odoo v JavaScriptu sadu obecných
komponenty, které lze znovu použít v některých běžných situacích, jako jsou například rozbalovací nabídky.
zaškrtávací políčka nebo datumové vybrané pole. Tato stránka vysvětluje, jak používat tyto obecné komponenty.

.. seznam tabulkový::
:šířky: 30 70
:hlavičky: 1

   * -Technické jméno
     - Stručný popis
   * :-:ref:<frontend/owl/actionswiper>
     - komponentu pro přejetí prstem, která provádí akce při dotyku
   * – :ref:`Tlačítko <frontend/owl/button>`
     - jednoduchý komponent se zaškrtávací políčko s názvem vedle něj
   * – :ref:`Barvová seznam <frontend/owl/colorlist>`
     - seznam barev, ze kterých si můžete vybrat
   * – :ref:`Kapitola <frontend/owl/dropdown>`
     - položkový seznam
   * - :ref:`Notebook <frontend/owl/notebook>`
     - komponenta pro přepínání mezi stránkami pomocí záložek
   * :-:ref:`Pager <frontend/pager>`
     - malý komponent k ovládání stránkování
   * -- :ref:`<frontend/select_menu>`
     - komponentu pro výběr z různých možností.
   * :-:ref:`Seznam štítků <frontend/tags_list>`
     - seznam štítků zobrazených v kulatých pilulkách

..._frontend/owl/actionswiper:

ActionSwiper
------------

Lokalita
~~~~~~~~

@web/jádro/akce_swiper/akce_swiper

Popis
~~~~~~~~~~~

Tento komponent může provádět akce, když se prvek přejezdí.
horizontálně. Svírač obaluje cílový prvek, aby k němu přidal akce.
Akce se spustí, jakmile uživatel uvolní posuvník
její šířky.

... blok kódu::xml


<SomeElement/>


Nejjednodušší způsob použití komponenty je přidat ji kolem cílového prvku
v šabloně XML uvedené výše. Ale někdy můžete chtít rozšířit existující prvek
a nechce si vzít šablonu. Je možné jenom to.

Pokud chcete prodloužit chování stávajícího prvku, musíte umístit prvek
Vnitřní část je možné obalit přímo. Dále lze kód podmíněně doplnit o proměnné, které umožňují řídit chování při
je možné, že se jedná o interaktivní prvek, jeho animace a minimální část, kterou je třeba přejet, aby bylo provedeno akce.

Komponentu lze použít k snadnému interakci s záznamy, zprávami, položkami v seznamech a mnohým dalším.

.. obrázek: owl_components/actionswiper.png
:šířka: 400 px
:alt: Příklad použití ActionSwiper


Následující příklad vytvoří základní komponentu ActionSwiper.
Tady je možné sledovat obsah v obou směrech.

... blok kódu::xml

<ActionSwiper
onRightSwipe="
      {
akce: '() => Odstranit položku',
ikonka: 'fa-smazat',
pozadí: 'bg-danger',
      }"
onLeftSwipe="
      {
akce: '() => Hvězdný výrobek',
ikonka: 'fa-hvězda',
pozadí: 'bg-varování',
      }"
  >

Přepínatelný prvek



.. poznámka: Akce jsou převráceny při použití jazyků zleva doprava (zprava doleva).

Props
~~~~~

.. seznam tabulkový::
:šířky: 20 20 60
:hlavičkové řádky: 1

    * - Jméno
      - Typ
      - Popis
    * – „animacePriHodu“
      - „Booleovská“
      - volitelná logická hodnota, která určuje, zda je během přejetí přítomen efekt překladu.
    * – „animaceTyp“
      - „Řetězec“
      - volitelná animace, která se používá po skončení přejetí („návrat“ nebo „před sebou“)
    * – „onLeftSwipe“
      - „Objekt“
      - Pokud je přítomen, lze jej posunout na levé straně.
    * – „onRightSwipe“
      - „Objekt“
      - Pokud je přítomen, lze akční lištu posunout vpravo
    * – „poměr vzdálenosti“
      - „Číslo“
      - volitelné minimální poměr šířky, které musí být přejeto pro provedení akce

Můžete používat oba „onLeftSwipe“ a „onRightSwipe“ vlastnosti zároveň.

Použité „objekty“ pro vlevo/vpravo musí obsahovat:

    - „akci“, která je volatelná funkce sloužící jako zpětná vazba.
Jakmile je přejetí dokončeno v daném směru, tato akce
Je prováděn.
    - „ikon“ je třída ikon, obvykle používaná k zobrazení akce.
Musí jít o řetězec.
    - Barva „bgColor“ slouží k dekorování akce.
může být jedním z následujících „kontextových barev bootstrapu“
<https://getbootstrap.com/docs/3.3/components/#available-variations>`_ („nebezpečí“,
„info“, „sekundární“, „úspěch“ nebo „varování“.

Tyto hodnoty musí být definovány, aby se určily chování a vizuální vzhled.
uživatele.

Příklad: Rozšíření stávajících komponent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V následujícím příkladu můžete použít „xpath“ k vytvoření nového prvku.
v komponentě ActionSwiper. Zde byl přidán swiper pro označení
zpráva, kterou si přečtete v e-mailu.

... blok kódu::xml

<xpath expr="//*[hasClass('o_Message')]" position="after">
<ActionSwiper
onRightSwipe="pokud je zařízení mobilní a zpráva potřebuje akci,
        {
akce: () => zobrazitZprávu.zpráva.označitČtenou()
ikonou „fa-check-circle“.
pozadí: 'bg-úspěch',
}:undefined
    />


<xpath expr="//*[@class='o_Message']" position="move"/>


.._frontend/owl/checkbox:

Checkbox
--------

Lokalita
~~~~~~~~

@web/jádro/checkBox/checkBox

Popis
~~~~~~~~~~~

Jedná se o jednoduchý součástkový prvek s textovým popiskem vedle něj.
spojené s štítkem: zaškrtávací políčko se zapíná a vypíná při kliknutí na štítek.

... blok kódu::xml


Nějaký text


Props
~~~~~

.. seznam tabulkový::
:šířky: 20 20 60
:hlavičkové řádky: 1

    * - Jméno
      - Typ
      - Popis
    * – „hodnota“
      - Pravda nebo nepravda
      - Pokud je tvrzení pravdivé, zaškrtávací políčko je vyznačeno, jinak není.
    * – „invalidní“
      - Pravda nebo nepravda
      - Pokud je tato informace pravdivá, zaškrtávací políčko je deaktivováno, jinak aktivní.

... /frontend/owl/colorlist:

ColorList
---------

Lokalita
~~~~~~~~

@web/jádro/barvový seznam/barvový seznam

Popis
~~~~~~~~~~~

Komponenta ColorList vám umožňuje vybrat si barvu z předdefinovaného seznamu. Výchozí hodnotou je aktuální
vybrané barvě a není rozšiřitelný, dokud nejsou přítomny „canToggle“ vlastnosti. Různé vlastnosti mohou změnit jeho
chování, vždy seznam rozšiřovat nebo jej nechat fungovat jako přepínač po kliknutí, aby byl zobrazen seznam
Výchozí barvy, dokud není vybrána.

Props
~~~~~

.. seznam tabulkový::
:šířky: 20 20 60
:hlavičkové řádky: 1

    * - Jméno
      - Typ
      - Popis
    * – „může se přepnout“
      - Pravda nebo nepravda
      - volitelné. Zda se při kliknutí na barvu rozbalí celý seznam barev
    * – „barvy“
      - „soubor“
      - seznam barev, které se zobrazí v komponentě. Každá barva má jedinečné ID
    * – „forceExpanded“
      - Pravda nebo nepravda
      - volitelné. Pokud je pravdivá, vždy se rozbalí
    * – „jeRozbaleno“
      - Pravda nebo nepravda
      - volitelné. Pokud je hodnota pravdivá, seznam se rozšíří o výchozí položky
    * – onColorSelected
      - Funkce
      - zpětná volba, která se spustí po výběru barvy
    * – barva
      - „číslo“
      - volitelné. Barva, která je vybrána

Barvy identifikátorů jsou následující:

.. seznam tabulkový::
:hlavičkové řádky: 1

    * – Id
      - Barva
    * - `0`
      - „Žádné barvy“
    * - `1`
      - „Červená“
    * - `2`
      - „Oranžová“
    * - `3`
      - „Žlutá“
    * - `4`
      - „Světle modrá“
    * - `5`
      - „Tmavě fialová“
    * - `6`
      - „Lososová růžová“
    * - `7`
      - „Středně modrá“
    * - `8`
      - „Tmavě modrá“
    * - `9`
      - „Fuchsiová“
    * - `12`
      - „Zelená“
    * - `11`
      - „Fialová“

..._frontend/owl/dropdown:

Kontextová nabídka
--------

Lokalita
~~~~~~~~

@web/core/dropdown/dropdown a @web/core/dropdown/dropdown_item

Popis
~~~~~~~~~~~

Dropdown vám umožní zobrazit nabídku s seznamem položek, když je přepínač
kliknutím na ně. Můžou být kombinovány s DropdownItems, aby se vyvolaly zpětné volání
a zavřít nabídku, když jsou vybrané položky.

Přímočaré ovladače jsou překvapivě složitými komponentami, jejich seznam funkcí je
Provádí se následovně:

- Při kliknutí se zobrazí seznam položek
- Blízko na vnější kliku
- Volání funkce při výběru položek
- Možnost uzavřít seznam položek při výběru položky
- SIY: stylujte si sami
- Podpora podnadpisů, až do jakéhokoliv stupně
- Konfigurovatelná klávesová zkratka pro otevření nebo uzavření vyskakovacího okna nebo výběr položky v něm
- Navigace klávesnicí (klávesy šipky nahoru a dolů, tabulátor, shift + tab, domovská klávesa, koncová klávesa, klávesa pro vstup a klávesa pro únik)
- Přesouvat se, když je stránka posunuta nebo změněna velikost
- Chytrá volba směru, kterým se má otevřít (směr zleva doprava je automaticky vyřešen).
- Přímé rozevírací seznamy sourozenců: když je jeden otevřený, aktivují se další na přejetí myší.

Pro správné použití komponenty <Dropdown> je potřeba vyplnit dvě
„Sloty OWL <https://github.com/odoo/owl/blob/master/doc/reference/slots.md>“:

- Výchozí „slot“: obsahuje vypínače vašeho rozbalovacího seznamu. Výchozím nastavením bude
bude připojen k tomuto prvku, aby se otevřel a zavřel.
- Slot „obsah“: obsahuje prvky samotného rozbalovacího menu a je zobrazen uvnitř poppoveru.
Pokud chcete, můžete do této položky vložit nějaké „DropdownItem“, což se zobrazí jako rozbalovací nabídka.
Otevřené okno se automaticky uzavře, pokud je vybrána některá z položek.

... blok kódu::xml

<Výběr>
<!--Obsah „výchozího“ slotu je komponenta, která se stává aktivní při najetí kurzoru-->
<button class="my-btn" type="button">
Klikněte na mě a zobrazí se vám rozbalovací nabídka.


<!--Slot „content“ se zobrazuje uvnitř nabídky, která se objevuje vedle tlačítka.
<t t-set-slot="content">
<DropdownItem selected="true" onSelected="selectItem1">Název položky menu 1</DropdownItem>
<DropdownItem selected="true" onSelected="selectItem2">Název položky menu 2</DropdownItem>



Dropdown Props
~~~~~~~~~~~~~~

.. seznam tabulkový::
:šířky: 20 20 60
:hlavičkové řádky: 1

    * - Jméno
      - Typ
      - Popis
    * – „menuClass“
      - „Řetězec“
      - Povinná třída přidána do nabídky v rozevíracím seznamu
    * – „invalidní“
      - „Booleovská“
      - Volitelné, pokud je pravdivé, deaktivuje vybavení a uživatel již není schopen jej otevřít. (Výchozí hodnota: „false“)
    * – „položky“
      - Array
      - Volitelný seznam položek, které mají být zobrazeny jako DropdownItems v nabídce.
    * „- pozice“
      - „Řetězec“
      - Volitelně definuje požadovanou pozici otevření nabídky. Automaticky se používá směr zleva doprava. Musí jít o platný :ref:`hook <frontend/hooks/useposition>` pro umístění. (Výchozí: `bottom-start`)
    * – před otevřením
      - „Funkce“
      - Volitelná funkce, která se volá před otevřením. Může být asynchronní.
    * – „onOpened“
      - „Funkce“
      - Volitelná funkce, která se volá hned po otevření.
    * – onStateChanged
      - „Funkce“
      - Volitelná funkce, která se volá po otevření nebo zavření (předává jako jediný parametr booleovou hodnotu, která reprezentuje, jestli je rozbalovací nabídka otevřená či ne).
    * „stát“
      - „Objekt“
      - Volitelný objekt s vlastnostmi open(), close() a isOpen, který umožňuje ruční kontrolu otevření a zavření rozbalovací nabídky.
    * – „Manuál“
      - „Booleovská“
      - Volitelně, pokud je hodnota true, komponent Dropdown nebude přidávat události kliknutí na tlačítko. To umožňuje větší kontrolu nad tím, kdy se dropdown otevře (to by mělo být používáno společně s hodnotou prop).
    * – „navigační možnosti“
      - „Booleovská“
      - Volitelně přepíše možnosti navigace z rolovací nabídky (viz web/core/navigation/navigation).
    * – `holdOnHover`
      - „Booleovská“
      - Pokud je tato možnost nastavena na hodnotu „pravda“, zůstane nabídka v pozici, když myš přejede nad ní, což vytváří lepší UX při změně obsahu nabídky.
    * – „menuRef“
      - „Funkce“
      - Volitelné, umožňuje získat odkaz na menu vybraného seznamu položek (vyžaduje funkci vrácenou z metody useChildRef).

Vlastnosti DropdownItem
~~~~~~~~~~~~~~~~~~

.. seznam tabulkový::
:šířky: 20 20 60
:hlavičkové řádky: 1

    * - Jméno
      - Typ
      - Popis
    * „třída“
      - „Řetězec“ nebo „objekt“.
      - Volitelná hodnota přidávaná k základnímu třídě (podporuje jak řetězce, tak i „notaci klasifikace OWL <https://github.com/odoo/owl/blob/master/doc/reference/templates.md#dynamic-class-attribute>“).
    * — onSelected
      - „Funkce“
      - Volitelná funkce, která se volá při výběru položky v rolovacím seznamu.
    * – „zavírací režim“
      - „žádný“ | „nejblíže“ | „všechny“
      - Volitelně, kontrola, které rodičovské položky by měly být zavřeny při výběru položky:
„Žádné“: vybraný seznam nezavře, „Nejbližší“: zavřou se rodičovské seznamy, „Všechny“: všechny podřízené seznamy se uzavřou (výchozí hodnota: „Všechny“)
    * - `attrs`
      - „Objekt“
      - Volitelný objekt reprezentující atributy přidávané k kořenovému prvku.

.. důležité:
Při psaní vlastního CSS pro vaše komponenty nezapomeňte na to, že položky nabídky nejsou vedle tlačítka
ale uvnitř přehrávače, na spodní části dokumentu. Proto použijte vlastnosti menuClass a class k tomu, abyste mohli
snadno napsat své selektory. (Toto kouzlo DOM nám umožnilo vyhnout se mnoha problémům s přesahem.)


Násobený výběr
~~~~~~~~~~~~~~~

Dropdown může být vnořený, k tomu stačí vložit nové komponenty Dropdown do obsahového slotu rodičovského Dropdownu.
když se otevře rolovací menu, dětská rolovací menu se automaticky otevřou při přejetí myší.

Výchozí nastavení je takové, že výběr položky z nabídky se uzavře celé rozbalovací menu.

Příklad:

Toto je příklad toho, jak lze vytvořit podmenu pro soubory s podmenu pro nové soubory.

... kódový blok :: XML

<Dropdown>
<tlačítko>Soubor</tlačítko>
<t t-set-slot="content">
<DropdownItem onSelected="() => this.onItemSelected('soubor-uložit')">Uložit</DropdownItem>
<DropdownItem vlastnost="selected" funkce="() => this.onItemSelected('soubor-otevřít')">Otevřít</DropdownItem>

<Výběr>
<tlačítko>Nový</tlačítko>
<t t-set-slot="content">
<DropdownItem vlastnost="selected" na výběr="() => this.onItemSelected('soubor-nový-dokument')">Dokument</DropdownItem>
<DropdownItem vlastnost="selected" funkce="() => this.onItemSelected('soubor-nový-sešit')">Sešit</DropdownItem>


</t>


V následujícím příkladu voláme šablonu k zobrazení stromovité struktury.

... kódový blok :: XML

<t t-name="addon.MainTemplate">

<t t-call="addon.RecursiveDropdown">
<t t-set="name" t-value="Hlavní menu" />
<t t-set="items" t-value="stát.menuItems" />
</t>
</div>


<t t-name="addon.RecursiveDropdown">
<Výběr>
<tlačítko t-esc="jméno"></tlačítko>
<t t-set-slot="content">
<t t-foreach="items" t-as="item" t-key="item.id">

<!--Pokud tento prvek nemá žádné dítě, udělte mu atribut <DropdownItem/>.-->
<Výběr položek t-pokud-ne-děti-stromu-item.childrenTree.length "t-při-vybrání-() => this.onItemSelected(item)" t-výjimka="item.name"/>

<!-- Jinak: volat šablonu aktuálního výběru. -->
<t t-else="" t-call="addon.RecursiveDropdown">
<t t-set="jméno" t-value="item.jméno" />
<t t-set="items" t-value="item.dětiStrom" />


</t>
</Dropdown>


Kontrolované rozbalení
~~~~~~~~~~~~~~~~~~~

Pokud je potřeba, můžete také otevřít nebo zavřít rozbalovací nabídku pomocí kódu. K tomu musíte použít funkci
s vlastností stavu, která se jmenuje useDropdownState, vrátí objekt s metodami open a close (a také s getterem isOpen).
Předmět předávejte do vlastnosti „stát“ vybraného dropdownu a volání příslušných funkcí by mělo nyní otevřít.
Zavřete si rozbalovací nabídku.

Můžete také nastavit „manuální“ na hodnotu „pravda“, pokud nechcete, aby se vám přidávaly výchozí ukazatele myši.

Příklad:

Následující příklad ukazuje vyskakovací okno, které se otevře automaticky při připojení a má pouze 50% šanci
zavření při stisknutí tlačítka uvnitř.

... kódový blok::javascript

import { Komponenta, naPřipojení } z "@odoo/owl";
import { Dropdown } z "@web/jádro/dropdown/dropdown";
import { DropdownItem } z "@web/jádro/dropdown/dropdown_item";
import { useDropdownState } z "@web/jádro/dropdown/dropdown_hooky";

klas MyComponent prodlouží třídu Component

statické komponenty = { Dropdown, DropdownItem };
statická šablona = XML
<Dropdown stav="toto.dropdown">
<div>Moje rozbalovací nabídka</div>

<t t-set-slot="content">
<tlačítko t-při-kliknutí="() => tento.můžeZavřít()">Zavřít to!<tlačítko>


      `;

setup() {
tento.dropdown = použít stav záložky ();

onMounted(() => {
tento.seznam.otevřít();
        });
      }

můžeZavřít()
pokud (Math.random() > 0,5) {
tento.dropdown.zavřít();
        }
      }
    }

Skupina rozbalovacího seznamu
~~~~~~~~~~~~~

**Lokalita:** `web/core/dropdown/dropdown_group`

Můžete použít komponentu DropdownGroup k tomu, aby se Dropdowny sdílely jednou skupinou. To znamená, že když
Jeden z těchto seznamů je otevřený, ostatní se automaticky otevřou při najetí myší, aniž by
nutnost kliknutí.

Pro toto je buď nutné všechny Dropdowny obklopit jedním DropdownGroupem nebo je obklopit
Skupiny Dropdowns s identickým klíčem group.

Příklad:
V níže uvedeném příkladu budou všechny vyskakovací okna sdílet stejnou skupinu:

... kódový blok :: XML

<SkupinaNáhledů>
<Dropdown>...</Dropdown>
<Dropdown>...</Dropdown>
<Dropdown>...</Dropdown>


V následujícím vzorku se pouze první, druhý a čtvrtý výběr nacházejí ve stejné skupině:

... kódový blok :: XML

<Skupina rozbalovacího seznamu skupina="'my-group'"
<Dropdown>...</Dropdown>
<Dropdown>...</Dropdown>


<DropdownGroup group="'moje-druhá-skupina'"
<Dropdown>...</Dropdown>


<Skupina rozbalovacího seznamu skupina="'my-group'"
<Dropdown>...</Dropdown>


..._frontend/owl/notebook:

Notebook
--------

Lokalita
~~~~~~~~

@web/jádro/poznámkový blok/poznámkový blok

Popis
~~~~~~~~~~~

Notebook je navržen tak, aby zobrazoval více stránek v záložkovém rozhraní. Záložky mohou být umístěny
nahoře u prvku pro zobrazení vodorovně nebo vlevo pro svislé uspořádání.

Existují dvě cesty, jak definovat stránky vašeho Notebooku, buď pomocí slotů,
nebo přesným předáním „propů“.

Stránku lze deaktivovat pomocí atributu isDisabled, který se nastavuje přímo na uzlu slot.
V prohlášení stránky, pokud se notebook používá s „stránkami“ jako vlastnostmi. Jakmile je tato funkce zakázána
odpovídající záložka je šedivá a neaktivní.

Props
~~~~~

.. seznam tabulkový::
:šířky: 20 20 60
:hlavičkové řádky: 1

    * - Jméno
      - Typ
      - Popis
    * – „zátěže“
      - „objekt“
      - volitelné. Povolte navigaci k prvkům uvnitř záložek, které nejsou vidět.
    * – „class“
      - „smyčka“
      - volitelné. Název třídy, který je nastaven na kořenovém prvku komponenty.
    * – „defaultní stránka“
      - „smyčka“
      - volitelné. Stránka s ID zobrazovaná výchozím nastavením.
    * – ikony
      - „soubor“
      - volitelný. Seznam ikon používaných v záložkách.
    * – „orientace“
      - „smyčka“
      - volitelné. Směr záložek je buď „svislý“ nebo „vodorovný“.
    * – onPageUpdate
      - Funkce
      - volitelný. Vykonává se jednou, když stránka změní obsah.
    * „stránky“
      - „soubor“
      - volitelné. Obsahuje seznam stránek, které mají být vyplněny z šablony.

Příklad:

První přístup spočívá v umístění stránek do slotů komponenty.

... kódový blok :: XML

<Notebook orientace="'vertikální'"
<t t-set-slot="page_1" title="„Stránka 1“" isVisible="true">
<h1>Můj první web</h1>
<p>Je čas vytvářet komponenty sovy. Četli jste dokumentaci?</p>
</t>
<t t-set-slot="page_2" title="Druhá stránka" isVisible="true">

</t>
</Notebook>

Další způsob definování stránek je prostřednictvím props. To může být užitečné, pokud některé stránky sdílejí
stejnou strukturu. Nejdříve vytvořte komponentu pro každý šablonový soubor, který můžete používat.

... kódový blok::javascript

import { Komponenta, xml } z "@odoo/owl";
import { Notebook } z "@web/jádro/notebook/notebook";

class MyTemplateComponent extends Component {
statická šablona = XML
<h1 t-esc="props.title" />
<p t-esc="props.text" />
        `;
      }

class MyComponent extends Component {
statická šablona = XML
<Notebook defaultPage="'stránka 2'" pages="stránky" />
        `;

dostupnostStránek()
return [
            {
Komponenta: MyTemplateComponent
název:„Stránka 1“,
props: {
název: „Můj první web“,
text:„Tato stránka není viditelná“.
              },
            },
            {
Komponenta: MyTemplateComponent
id: „stránka 2“,
název: „Stránka 2“,
props: {
titulek: „Moje druhá stránka“,
text:„Jste na správném místě!“
              },
            },
          ]
        }
      }

Oba příklady jsou zde ukázány.

.. obrázek:: notebook.png
:šířka: 400 px
:alt:Příklady s vertikální a horizontální orientací
:synchronizace: střed


..._frontend/pager:

Pager
-----

Lokalita
~~~~~~~~

@web/jádro/paginace/paginace

Popis
~~~~~~~~~~~

Pager je malý komponent k ovládání stránek. Stránka se definuje pomocí offsetu a limitu (velikost stránky). Zobrazuje aktuální stránku a celkový počet prvků, například „9-12 / 20“. V předchozím příkladu je offset 8, limit 4 a celkový počet 20. Má dvě tlačítka („Předchozí“ a „Další“) pro navigaci mezi stránkami.

.. poznámka::
Paginátor lze používat kdekoli, ale jeho hlavní využití je v ovládacím panelu. Chcete-li manipulovat s paginátorem ovládacího panelu, podívejte se na :ref:`příkaz <frontend/hooks/usepager>`

... blok kódu::xml



Props
~~~~~

.. seznam tabulkový::
:šířky: 20 20 60
:hlavičkové řádky: 1

    * - Jméno
      - Typ
      - Popis
    * – „výška“
      - „číslo“
      - Index prvního prvek stránky. Začíná na 0, ale zobrazuje se „offset + 1“.
    * „- limit“
      - „číslo“
      - Velikost stránky. Součet hodnot offset a limit odpovídá indexu posledního prvku na stránce.
    * „celkem“
      - „číslo“
      - Počet prvků, které stránka může obsahovat.
    * – „onUpdate“
      - Funkce
      - Funkce, která se volá při změně stránky pomocí pageru. Tato funkce může být asynchronní, ale zatímco bude tato funkce spouštěna, pager nelze upravovat.
    * – editovatelnost
      - Pravda nebo nepravda
      - Umožňuje kliknout na aktuální stránku a upravit ji („pravda“ výchozí hodnotou).
    * – s klíčem přístupu
      - Pravda nebo nepravda
      - Přidá klíčové slovo „p“ na tlačítko předchozí stránky a „n“ na tlačítko další stránky („true“ výchozí hodnotou).

.. _frontend/select_menu:

Vyberte si
----------

Lokalita
~~~~~~~~

@web/jádro/vyber-menu/vyber-menu

Popis
~~~~~~~~~~~

Tento komponent můžete používat v případě, kdy chcete dělat více než s nativním prvkem „select“. Můžete si definovat svůj vlastní šablonu pro možnosti, což umožňuje vyhledávání.
mezi vašimi možnostmi nebo je můžete seskupit do podsekcí.

.. poznámka::
Přednostně používejte původní HTML tag select, který poskytuje výchozí přístupnost a lepší uživatelské rozhraní na mobilních zařízeních.
Tento komponent je navržen tak, aby se používal pro složitější případy použití a překonal omezení prvku nativního.

Props
~~~~~

.. seznam tabulkový::
:šířky: 20 20 60
:hlavičkové řádky: 1

    * - Jméno
      - Typ
      - Popis
    * „volby“
      - „soubor“
      - volitelný. Seznam možností, které se mají zobrazovat v rolovacím seznamu.
    * „třída“
      - „smyčka“
      - volitelné. Název třídy nastavený na kořenovém SelectMenu komponentu.
    * „Skupiny“
      - „soubor“
      - volitelné. Seznam skupin, které obsahují volby, které se mají zobrazovat v rolovacím menu.
    * – multiSelect
      - Pravda nebo nepravda
      - volitelné. Povolte vícenásobnou volbu. Když je povolená vícenásobná volba, vybrané hodnoty se zobrazují jako :ref:`tag <frontend/tags_list>` v SelectMenu inputu.
    * – „tlačítko“
      - „smyčka“
      - volitelný. Název třídy nastavený na tlačítku pro přepínání.
    * „Povinné“
      - Pravda nebo nepravda
      - volitelný. Zda je možné vybranou hodnotu odstranit.
    * – „vyhledatelné“
      - Pravda nebo nepravda
      - volitelné. Zda je vidět vyhledávací pole v rozbalovacím seznamu.
    * „Vyhledávací pole“
      - „smyčka“
      - volitelné. Zobrazovaný text jako náhrada za vyhledávací pole.
    * – „hodnota“
      - „jakákoliv“
      - volitelné. Vybraná aktuální hodnota. Může být z jakéhokoliv typu.
    * – onSelect
      - Funkce
      - volitelný. Volání zpětného volání prováděné při výběru možnosti.

Tvar volby je následující:

    - Hodnota „value“ je skutečná hodnota volby. Obvykle jde o technický řetězec, ale může být libovolného typu.
    - „Štítek“ je zobrazený text spojený s volbou. Tento obvykle bývá přívětivější a překládaný „řetězec“.

Tvar skupiny je následující:

    - „volby“ je seznam „volby“, které mají být zobrazeny pro tuto skupinu.
    - „Štítek“ je zobrazený text spojený s skupinou. Jde o „řetězec“, který se zobrazí na horním okraji skupiny.

Příklad:

V následujícím příkladu bude SelectMenu zobrazovat čtyři možnosti. Jedna z nich je na vrcholu seznamu.
protože k němu žádné skupiny nejsou přiřazeny, ale ostatní jsou odděleny štítkem své skupiny.

... kódový blok::javascript

import { Komponenta, xml } z "@odoo/owl";
import { SelectMenu } z "@web/jádro/select_menu/select_menu";

class MyComponent extends Component {
statická šablona = XML
<VyberMenu
volby="volby"
groups="groups"
hodnota="'hodnota_2'"
          />
        `;

get choices():
return [
              {
hodnota: "hodnota_1",
label:„První hodnota“
              }
          ]
        }
getGroups() {
return [
            {
label: „Skupina A“,
volby:
                    {
hodnota: "hodnota_2",
label: „Druhý význam“
                    },
                    {
value: "hodnota_3",
label: „Třetí hodnota“
                    }
                ]
            },
            {
label: „Skupina B“,
volby:
                    {
hodnota: "hodnota_4"
label:„Čtvrtá hodnota“
                    }
                ]
            }
          ]
        }
      }

Můžete také přizpůsobit vzhled tlačítka a nastavit vlastní šablonu pro volby pomocí příslušného komponentu „slot“.

... kódový blok :: XML

<Vyberte
volby="volby"
skupiny="skupiny"
hodnota="hodnota_2"
      >
Zvolte si!
<t t-set-slot="volba" t-slot-scope="volba">
<span class="coolClass" t-esc="'👉 ' + choice.data.label + ' 👈'" />
</t>
</Vybermenu>

.... obrázek:owl_components/select_menu.png
:šířka: 400 px
:alt: Příklad použití a přizpůsobení SelectMenu
:synchronizace: střed

Při použití SelectMenu s více výběry musí být vlastnost value nastavena na pole obsahující hodnoty vybraných možností.

.... obrázek:owl_components/select_menu_multiSelect.png
:šířka: 350 pixelů
:alt:Příklad použití SelectMenu s více výběry
:synchronizace: střed

Pro pokročilejší použití lze upravit spodní část nabídky pomocí vlastnosti slotu `bottomArea`, kde si můžeme zvolit, že budeme zobrazovat
tlačítko s odpovídajícím nastaveným hodnotou v poli pro vyhledávání.

... kódový blok :: XML

<Vyberte
volby="volby"
      >
<span class="select_menu_test">Vyberte něco</span>
<t t-set-slot="spodní oblast" t-slot-scope="select">
<div t-if="select.data.searchValue">

Vytvořte tento článek "<i t-esc="select.data.searchValue" />"
</tlačítko>
</div>

</Vybermenu>

.... obrázek:owl_components/select_menu_bottomArea.png
:šířka: 400 px
:alt: Příklad přizpůsobení spodní části SelectMenu
:synchronizace: střed

.. _frontend/tagy_seznam:

Štítky
--------

Lokalita
~~~~~~~~

@web/jádro/tagy/tagy

Popis
~~~~~~~~~~~

Tento komponent může zobrazit seznam štítků ve tvaru kuliček. Tyto štítky buď jen obsahují několik hodnot, nebo jsou upravitelné a umožňují odstranění položek.
Možné je omezit počet zobrazených položek pomocí vlastnosti „itemsVisible“. Pokud seznam je delší než tento limit, počet dalších položek
ukázané v kruhu vedle posledního štítku.

Props
~~~~~

.. seznam tabulkový::
:šířky: 20 20 60
:hlavičkové řádky: 1

    * - Jméno
      - Typ
      - Popis
    * – „zobrazit štítek“
      - Pravda nebo nepravda
      - volitelné. Zda se štítek zobrazuje jako nálepka.
    * – „zobrazit“
      - Pravda nebo nepravda
      - volitelné. Zda se bude s textem nebo bez něj zobrazovat štítek.
    * – „zobrazené položky“
      - „číslo“
      - volitelný. Maximální počet viditelných štítků v seznamu.
    * – „tagy“
      - „soubor“
      - seznam prvků tagu předaných komponentě.

Tvar tagu je následující:

    - „colorIndex“ je volitelný identifikátor barvy.
    - „ikon“ je volitelný ikonový obrázek, který se zobrazuje před zobrazovaným textem.
    - „id“ je jedinečný identifikátor značky.
    - „img“ je volitelná obrázková značka, která se zobrazuje v kruhu před zobrazovaným textem.
    - „onClick“ je volitelná funkce, kterou lze přidat do prvku. Tato funkce umožňuje rodičovskému prvku vykonávat jakékoliv funkce podle toho, který prvek byl kliknutý.
    - Funkce onDelete je volitelná a může být předána prvku. Tato funkce umožňuje odstranění položky ze seznamu štítků a musí být zpracována rodičovským prvkem.
    - „text“ je zobrazený řetězec „stringu“, který je spojen s tímto značkovým jménem.

Příklad:

V další ukázce se používá komponenta TagsList k zobrazení více štítků.
Je na vývojáři, aby se postaral o to, co se stane, když je tlačítko stisknuto nebo kliknuté tlačítko smazání.

... kódový blok::javascript

import { Komponenta, xml } z "@odoo/owl";
import { Seznam štítků } z "@web/jádro/tags_list/tags_list";

třída Parent je dědičná od komponenty.
statické šablona = XML`<TagsList tags="tagy"/>`;
statické součásti = { SeznamTagů };

setup() {
tags: [
id: "tag1",
text: „Země“
          }, {
barva: 1,
id: „tag2“,
text: „Vítr“,
onDelete: () => {...}
          }, {
barva: 2
id: „tag3“,
text: „Oheň“,
onclick: () => {...}
onDelete: () => {...}
          }];
        }
      }

Podle atributů, které jsou danému tagu přiřazeny, se jejich vzhled a chování liší.

.. obrázek::owl_components/tags_list.png
:šířka: 350 pixelů
:alt:Příklady TagListu s různými vlastnostmi a atributy
:synchronizace: střed
