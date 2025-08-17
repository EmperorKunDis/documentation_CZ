=========================
Kapitola 1: Komponenty sovy
=========================

Tento kapitol představuje „framework Owl <https://github.com/odoo/owl>“, který je speciálně přizpůsobený pro použití v rámci ERP systému.
systém pro Odoo. Hlavními stavebními kameny OWL jsou „komponenty
<{OWL_PATH}/doc/reference/komponenty.md> a <{OWL_PATH}/doc/reference/šablony.md>.

V Owlu je každá část uživatelského rozhraní řízena komponentou: drží logiku a definují
šablony používané k zobrazení uživatelského rozhraní. Ve skutečnosti je komponenta reprezentována
malá třída v JavaScriptu, která je podtřídou třídy Component.

Pro začátek potřebujete běžící Odoo server a vývojové prostředí. Než se pustíte do práce
Do cvičení se ujistěte, že jste všechny kroky popsané v této
:ref:`Úvodní příručka <tutorials/discover_js_framework/setup>“.

..tip:
Pokud používáte prohlížeč Chrome, můžete si do něj nainstalovat rozšíření „Owl Devtools“.
Prodloužení poskytuje mnoho funkcí, které vám pomohou porozumět a profilovat jakýkoliv aplikační projekt Owl.

„Video: Jak používat vývojové nástroje <https://www.youtube.com/watch?v=IUyQjwnrpzM>“

V této kapitole používáme přídavné moduly „Awesome Owl“, který poskytuje zjednodušené prostředí.
obsahuje pouze sovího a několik dalších souborů. Cílem je naučit se samotnou sovu bez využití Odoo
kód pro webové klienty.

..spoiler:: Řešení

Řešení každého cvičení kapitoly jsou uložená na oficiálních návodech k Odoo.
repozitář
<https://github.com/odoo/tutorials/commits/{CURRENT_MAJOR_BRANCH}-discover-js-framework-solutions/awesome_owl>.
Je doporučeno se pokusit o řešení bez nahlížení na řešení.

Příklad: komponenta Counter
==============================

Nejprve se podíváme na jednoduchý příklad. Komponenta Counter, která je uvedena níže, je komponentou
Udržuje vnitřní číselnou hodnotu, zobrazuje ji a aktualizuje ji pokaždé, když uživatel klikne na
tlačítko.

... kódový blok::js

import { Komponenta, použítStav } z "@odoo/owl";

exportní třída Counter, která dědí z komponenty:
statický šablonový výraz = „my_module.Counter“;

setup() {
tento.state = useState({ hodnota: 0 });
       }

increment() {
tento.stavy.hodnota++;
       }
   }

Komponenta „Counter“ určuje název šablony, která reprezentuje její HTML. Je napsaná v XML
pomocí jazyka QWeb:

... blok kódu::xml

<šablony xml:space="preserve">
<t name="my_module.Counter">

<button type="button" class="btn btn-primary" onclick="increment()">Zvýšit</button>
</t>



1. Zobrazení počítadla
=======================

.. obrázek: 01_součástky/čítačka.png
:align:center

Jako první cvičení si připravíme modifikaci komponenty Playground, která se nachází v
Do adresáře „awesome_owl/static/src“ přejmenujte soubor na konter. Výsledek můžete vidět na
„/awesome_owl“ adresu v prohlížeči.


#Upravte soubor `playground.js`, aby fungoval jako počítadlo, jak je tomu v příkladu výše.
Zapomeňte na „Hřiště“ jako název třídy. Budete potřebovat použít funkci „useState hook“.
<{OWL_PATH}/doc/reference/hooks.md#usestate> tak, aby se komponent znovu zobrazila
pokaždé, když je jakýkoliv prvek státního objektu, který byl čten tímto komponentem, změněn.
#V téže složce vytvořte metodu s názvem „Increment“.
#Upravte šablonu v souboru:file:`playground.xml`, aby zobrazovala vaši proměnnou pro počítání. Použijte
„t-esc <{OWL_PATH}/doc/reference/templates.md#outputting-data>“ k výstupu dat.
#Přidejte tlačítko do šablony a zadejte příkaz t-on-click
atributem „<{OWL_PATH}/doc/reference/event_handling.md#event-handling>“ v tlačítku
Aktivovat metodu „increment“ každou chvíli, když je tlačítko klikáno.

..tip:
Javascriptové soubory stažené prohlížečem jsou zkomprimovány. Pro účely ladění je
Je snazší, když jsou soubory nekomprimované. Přepněte na režim :ref:`s aktivními
</vývojářský režim/aktivace> tak, aby soubory nebyly zmenšeny.

Toto cvičení představuje důležitou vlastnost sovy: „systém reaktivity <{OWL_PATH}/doc/reference/reactivity.md>“.
Funkce useState vytváří pro hodnotu proxy, který umožňuje Owlu sledovat, která komponenta
potřeby části státu, takže se může aktualizovat pokaždé, když dojde ke změně hodnoty. Zkuste
odstranit funkci „useState“ a zjistit, co se stane.

2. Vytažení proměnné Counter do podkomponenty
=======================================

Nyní máme logiku počítadla v komponentě „Hřiště“, ale není ji možné používat vícekrát.
podívejte se, jak vytvořit podkomponentu z ní:

#Vyjměte kód z hrací plochy komponenty Playground do nové komponenty Counter.
#Můžete to udělat v jednom souboru jako první, ale jakmile je hotovo, aktualizujte svůj kód tak, aby se
„Sčítadlo“ do své složky a souboru. Do „sčítadla“ importujte relativně z „./sčítadlo/sčítadlo“. Ujistěte se,
šablona je v samostatném souboru s názvem stejným jako šablona.
#Vložte do šablony komponenty Playground značku Counter a přidejte dvě číselníky.
hřiště.

.. obrázek: 01_součástky/dvojitý počítadlo.png
:align:center

..tip:
Řešením je konvence, že většina komponent má stejný název ve tvaru „snake case“.
jako součást. Například pokud máme komponentu TodoList, její kód by měl být v
`todo_list.js`, ´todo_list.xml´ a pokud je třeba také ´todo_list.scss´

... /tutoriály/objevte-js-framework/jednoduchá-karta/:

3. Jednoduchý komponent „Karta“
============================

Komponenty jsou opravdu nejpřirozenějším způsobem, jak rozdělit složitý uživatelský rozhraní na několik
Opakovaně použitelné části. Ale aby byly skutečně užitečné, je nutné umět komunikovat
nějaké informace mezi nimi. Podívejme se, jak může rodičovská komponenta poskytnout informace dítěti
podkomponentu pomocí atributů (nejčastěji známých jako „props <{OWL_PATH}/doc/reference/props.md>“).

Tento cvičení má za cíl vytvořit komponentu „Card“, která přijímá dvě proměnné: „title“ a „content“.
Příklad použití:

... blok kódu::xml



Následující příklad by měl vytvořit nějaký HTML pomocí Bootstrapu, který bude vypadat takto:

.. kódový blok:: html

<div třída="karta" styl="šířka: 18rem;">
<div class="card-body">
<h5 class="card-title">název mé karty</h5>

nějaký obsah
</p>



#Vytvořte komponentu „Karta“.
#Importujte ji do Playgroundu a zobrazte pár karet v jeho šabloně

.. obrázek: 01_sokol_komponenty/jednoduchý_kartáček.png
:align:center

4. Zobrazení HTML pomocí značek
=================================

Pokud jste použili „t-esc“ v předchozím cvičení, mohli byste si všimnout, že Owl automaticky uprchne
její obsah. Například pokud se pokusíte zobrazit nějaký HTML takto:
s „toto.html = '<div>nějaký obsah</div>'“
Výsledný výstup jednoduše zobrazí HTML jako řetězec.

V tomto případě je vhodné použít komponentu „Card“, která může zobrazovat jakýkoliv obsah.
umožnit uživateli zobrazit nějaký HTML. To se provádí pomocí
„t-out“ příkazu <{OWL_PATH}/doc/reference/templates.md#outputting-data>_.

Zobrazování libovolného obsahu jako HTML je však nebezpečné, může se použít k vložení škodlivého kódu.
Výchozí nastavení je takové, že Owl vždy uprchne z řetězce, pokud nebyl explicitně označen jako bezpečný pomocí atributu markup.
Funkce.

#Aktualizujte třídu Card, aby používala t-out.
#Aktualizujte hru „Hřiště“ tak, aby mohla importovat značky a používat je na některých hodnotách HTML.
#Ujistěte se, že vidíte, že normální řetězce jsou vždy uvozeny znakem zpětného lomítka, zatímco značené řetězce ne.

.. poznámka::

Direktiva t-esc může být v šablonách Owl stále používána, je o něco rychlejší než t-out.

.. obrázek: 01_sokolovské součástky/markup.png
:align:center

5. Validace vlastností
===================

Komponenta „Card“ má implicitní API. Očekává, že do svých vlastností obdrží dva řetězce: „title“.
a „obsah“. Ať si tento API více
explicitní. Můžeme přidat definici prostředků, která umožní provést krok validace v režimu vývoje
<{OWL_PATH}/doc/reference/app.md#develop-mode>. Chcete-li aktivovat vývojový režim, přejděte do
konfigurace (viz {OWL_PATH}/doc/reference/app.md#configuration>), ale je aktivována výchozím nastavením
na hřišti „Awesome Owl“).

Je dobrou praxí ověřovat vlastnosti pro každý komponent.

#Přidejte „Validace vlastností <{OWL_PATH}/doc/reference/props.md#props-validation>“ do karty
součástí.
#. Přejmenujte proměnné „title“ v šabloně pro hřiště na něco jiného a pak zkontrolujte
:guilabel:`Konzola“ v prohlížeči, kde vidíte chybu.

6. Součet dvou „Přepočítávačů“
===========================

V předchozím cvičení jsme viděli, že „vlastnosti“ mohou poskytovat informace z rodiče.
do dětského komponentu. Podívejme se nyní na způsob sdělování informací v opačném směru
směr: v této cvičení chceme zobrazit dva komponenty Counter a pod nimi součet
jejich hodnoty. Proto musí být komponenta rodičovského okna („hrací plocha“) informována o každé změně
Hodnota Counter se změní.

Toho lze dosáhnout pomocí vlastnosti „zpětné volání“ (viz dokumentace OWL):
pomůcka, která je funkcí, kterou může dítě volat zpět. Dítě si může vybrat, že zavolá
tuto funkci s jakýmkoliv argumentem. V našem případě budeme jednoduše přidávat volitelný parametr „onChange“, který bude
bude vyvolán pokaždé, když se komponenta „Čítačka“ zvyšuje.

#Přidejte ověření vlastnosti do komponenty Counter: měla by přijímat volitelnou vlastnost onChange
funkce prop
#Aktualizujte komponentu Counter tak, aby volala metodu onChange (pokud existuje), pokaždé když
Je přidána.
#. Upravte komponentu „Hřiště“ tak, aby udržovala místní hodnotu stavu („součet“), která je zpočátku
je nastaven na hodnotu 2 a zobrazuje se v jeho šabloně.
#Implementuj metodu „incrementSum“ v Playground.
#Dávejte tento metodu jako vlastnost dvěma (nebo více) podkomponentám Counter.

.. obrázek:: 01_součet_komponent/sum_counter.png
:align:center

.. důležité:

Pro callbacky je tu ale jedna drobnost: obvykle by měly být definovány metodou bind.
přípona. Podívejte se na dokumentaci v části „Použití funkcí vázání vlastností“

7. Seznam věcí k vyřízení
==============

Nyní objevme různé vlastnosti sovy tím, že vytvoříme seznam úkolů. K tomu potřebujeme dvě složky:
Komponenta „TodoList“, která zobrazí seznam komponent „TodoItem“. Seznam úkolů je
co by měl udržovat „Seznam věcí k vyřízení“.

Pro tento návod je „to do“ objekt, který obsahuje tři hodnoty: id (číslo), description
(řetězec) a vlajka „isCompleted“ (logická hodnota):

... kódový blok::js

{ id: 3, popis: „koupit mléko“, je splněno: false }

#Vytvořte komponentu TodoList a TodoItem.
#Komponenta „TodoItem“ by měla přijímat jako vlastnost „todo“ a zobrazovat jeho „id“ a „description“ v „div“.
#Prozatím je třeba zadat seznam úkolů ručně.

... kódový blok::js

      // in TodoList
tento.todo = useState([{id: 3, popis: „koupit mléko“, je splněno: false}]);

#Použijte t-foreach <{OWL_PATH}/doc/reference/templates.md#loops> k zobrazení každého úkolu v TodoItem.
#Zobrazte seznam úkolů v herním prostředí.
#Přidat ověření vlastností do třídy TodoItem.

.. obrázek: 01_součásti_sovy/seznam_úkolů.png
:align:center

..tip:
Protože komponenty TodoList a TodoItem jsou tak úzce provázané, je
dává smysl je uložit do stejné složky.

.. poznámka::
„T-foreach“ příkaz není v Owlu úplně stejný jako implementace QWeb v Pythonu:
vyžaduje unikátní hodnotu t-key, aby mohl Owl správně spojit každý prvek.

8. Použijte dynamické atributy
=========================

Zatím se v komponentě „TodoItem“ nedá vizuálně zjistit, jestli je úkol splněný nebo ne. Pojďme to napravit takto:
používáním dynamických atributů (viz „Dynamické atributy“).

#Přidejte na kořenový prvek TodoItem třídy text-muted a text-decoration-line-through.
pokud bude dokončena.
#Změňte pevně danou hodnotu „this.todos“ a zkontrolujte, zda je správně zobrazena.

I když je tento příkaz pojmenován „t-att“ (pro atribut), může být použit k nastavení hodnoty „class“ (a
vlastnosti HTML, jako je například hodnota vstupního pole).

.. obrázek: 01_součástky_sova/mute_todo.png
:align:center

..tip:

Owl vám umožní kombinovat statické hodnoty třídy s dynamickými hodnotami. Následující příklad bude fungovat tak, jak byste očekávali:

... kódový blok :: XML

<div t-class="a" t-att-class="someExpression"/>

Viz také: „Sova: Dynamické atributy třídy <{OWL_PATH}/doc/reference/templates.md#dynamic-class-attribute>“

9. Přidání úkolu
================

Tak daleko jsou naše „todo“ v seznamu pevně zakódované. Pojďme je udělat užitečnější, umožníme uživateli přidávat
A taky na seznam.

#Odstranit pevně zakódované hodnoty v komponentě TodoList:

... kódový blok::javascript

tento.todo = useState([]);

#Přidejte pole pro vstup nad seznamem úkolů s místo náhradního textu *Zadejte nový úkol*.
#Přidejte funkci zpracování události na událost keyup
pojmenované jako addTodo.
#Implementujte metodu addTodo, která zkontroluje, jestli byl stisknutý klávesový znak (:code:`ev.keyCode === 13`), a v případě
Případně vytvořte nový úkol s aktuálním obsahem vstupu jako popis a vymažte
vstup všech obsahů.
#Ujistěte se, že úkol má jedinečné ID. Může být jen počítadlo, které se každému úkolu přičítá.
#Bonusový bod: neprováděj žádné operace, pokud je vstup prázdný.


.. obrázek: 01_součástky/vytvořit_seznam.png
:align:center

.. viz též:
„Sova: Reaktivita <{OWL_PATH}/doc/reference/reactivity.md>“

Teorie: Životní cyklus komponent a háky
=====================================

Dosud jsme viděli jeden příklad funkce pro zavěšení: „použít stav“. Funkce „zavěsit <{OWL_PATH}/doc/reference/hooks.md>“
je speciální funkce, která se „zapojí“ do vnitřních částí komponenty. V případě
„useState“, vytváří propojený objekt proxy, který je spojen s aktuálním komponentem. Proto
Funkce smyčky musí být volány v metodě setup a nikdy později.


.. schéma LR

..    classDef hook naplněn:#ccf

...     podgraf „vytvoření“
.. směr TB
...:A:háček
..:B:::hook
..:M:::hook
...A[setup] --> B
...  B[naZacit] --> C(zobrazit)
..    C --> D ("připojení (v DOM)")
..    D --> M[naZvednutéKolo]
...                   konec

..     aktualizace podgrafů
.. směr TB
..:E:Hook
..:F:::hook
..:H:Hook
...      E[„(onWillUpdateProps)“] --> L(render)
..         L --> F[naPatche]
..         F --> G (patch DOM)
...     G --> H[naPatched]
...                   konec

..     destrukce podgrafu
.. směr TB
..:::háček
..:::J:::hook
...     I[onWillUnmount] --> J[onWillDestroy]
...   J --> N (odstraněno z DOMu)

...                   konec

......vytvoření --- aktualizace
..      aktualizace ---> zničení


.. obrázek: 01_sova_komponenty/komponentni-zivotni-cyklus.svg
:align:center
:šířka: 50 %


Komponenta sovy prochází mnoha fázemi: může být instancována, vykreslována.
nainstalované, aktualizované, odpojené, zničené… To je „životní cyklus komponenty“ („<{OWL_PATH}/doc/reference/component.md#lifecycle>“).
Obrázek ukazuje nejdůležitější události v životě komponenty (háčky jsou vyznačeny fialovou barvou).
Přibližně řečeno, vytvoříte komponentu, pak ji aktualizujete (možná několikrát) a poté ji zničíte.

Sýkora poskytuje řadu vestavěných funkcí „závěsů“ (viz {OWL_PATH}/doc/reference/hooks.md). Všechny z nich musí být volány
funkce setup. Například pokud chcete spustit nějaký kód při připojení komponenty, můžete použít funkci onMounted
háček:

... kódový blok: JavaScript

setup() {
onMounted(() => {
       // do something here
     });
   }

..tip:

Všechny funkce s háčky začínají slovy „use“ nebo „on“. Například: „useState“ nebo „onMounted“.


10. Zaměření vstupu
======================

Podívejme se, jak můžeme přistupovat k DOM pomocí t-ref <{OWL_PATH}/doc/reference/refs.md> a useRef
<{OWL_PATH}/doc/reference/hooks.md#userref>. Hlavní myšlenkou je, že musíte označit
cílový prvek v šabloně komponenty s atributem t-ref

... blok kódu::xml

<div t-ref="jmeno">Ahoj!</div>

Poté můžete do JavaScriptu přistupovat pomocí funkce useRef s odkazem na dokumentaci „Reference“ v části „Hooks“ („Hokey“).
Ale existuje problém, pokud o tom přemýšlíte: skutečný HTML prvek pro
komponenta neexistuje, když je komponenta vytvářena. Existuje pouze tehdy,
komponenta je nainstalována. Ale háčky musí být volány v metodě setup. Takže použijte ref
Vrátit objekt, který obsahuje klíč el (pro prvek), který je definován pouze tehdy, když
součást je namontována.

... kódový blok::js

setup() {
tento.můjRef = použítRef("nějaké jméno");
onMounted(() => {
console.log(this.myRef.el);
      });
   }


#Zaměřte se na „vstup“ z předchozího cvičení.
Komponenta „TodoList“ (pozornost věnujte tomu, že v html prvek pro zadání textu je metoda „focus“).
#Bonusový bod: extrahujte kód do speciálního „závěsu <{OWL_PATH}/doc/reference/hooks.md>“
Do nového souboru „awesome_owl/utils.js“ přidejte proměnnou „useAutofocus“.

.. obrázek: 01_součástky_autofokusu.png
:align:center

..tip:

Reference obvykle obsahují příponu „Ref“, aby bylo zřejmé, že se jedná o speciální objekty:

... kódový blok::js

tento.vstupníRef = použítRef("vstup");

11. Přepínání všech
==================

Teď přidáme novou funkci: označit úkol jako splněný. Ve skutečnosti je to složitější než se na první pohled zdá.
myslet. Vlastník státu není stejný jako komponenta, která ho zobrazuje. Takže třída
komponenta musí svému rodiči sdělit, že stav „musím udělat“ potřebuje přepnout. Jedním z klasických
Jak na to? Přidejte vlastnost callback.
<{OWL_PATH}/doc/reference/props.md#binding-function-props>_`toggleState`.

#Přidejte pole s atributem :code:`type="checkbox"` před ID úkolu, které musí
je třeba zkontrolovat, jestli je stav „isCompleted“ pravdivý.

......tip:
Orel nezavádí atributy vypočítané pomocí příkazu t-att, pokud hodnota vyjadřuje
hodnota false.

#Přidejte do vlastností callbacku props „toggleState“ do TodoItem.
#Přidejte do komponenty TodoItem událostní zpracovatele pro událost change a ujistěte se, že tato událost volá
Funkci „přepínání stavu“ s identifikátorem úkolu.
#Dokážete to!

.. obrázek: 01_sokoloviny/vypnuto.png
:align:center

12. Smazání všech
==================

Posledním krokem je umožnit uživateli smazat úkol.

#Přidejte novou vlastnost pro volání zobrazení položky „Remove Todo“ do „TodoItem“.
#Vložte do šablony komponenty TodoItem značku <span class="fa fa-remove"/>>.
#Každýkrát, když uživatel na ni klikne, by mělo volat metodu removeTodo.
#Dokážete to!

......tip:
Pokud používáte pole k ukládání seznamu úkolů, můžete použít funkci splice v JavaScriptu.
funkci pro odstranění úkolu z ní.

.. kódový blok::

   // find the index of the element to delete
const index = list.findIndex((elem) => elem.id === elemId);
pokud je index větší nebo roven nule,
         // remove the element at index from list
list.spojit(index, 1);
   }

.. obrázek:: 01_součástky/odstranit_seznam.png
:align:center

.. _tutorials/discover_js_framework/generic_card:

13. Obecný „karta“ s otvory
=============================

V předchozím cvičení jsme si vytvořili jednoduchou kartu.
jednoduchý komponent „Karta“. Ale je upřímně dost omezený. Co když chceme
Zobrazit nějaký libovolný obsah uvnitř karty, například podkomponentu?
nefunguje, protože obsah karty je popsán řetězcem.
Nicméně by bylo velmi pohodlné, kdybychom mohli popsat obsah jako šablonu.

Toto je přesně to, co systém „slotů“ („slot <{OWL_PATH}/doc/reference/slots.md>“) od sovy umožňuje
pro: umožňuje psát obecné komponenty.

Pojďme upravit komponentu Card, aby používala sloty:

#Odeberte vlastnost content.
#Použijte výchozí slot k definování těla.
#Vložte několik karet s libovolným obsahem, například komponentu Counter.
#(bonus) Přidat ověřování vlastností.

.. obrázek: 01_sokolovská_komponenta/obecný_kartový_objekt.png
:align:center

.. viz též:
„Připraveno na start: dokumentace karty <https://getbootstrap.com/docs/5.2/components/card/>“

14. Snižování obsahu karet
===========================

...TODO: Toto cvičení neukazuje žádnou novou koncepci, a proto by mělo být pravděpodobně odstraněno.

Začněme tedy přidáním funkce do komponenty Card, aby byla zajímavější:
chcete tlačítko, které by mělo možnost zobrazit nebo skrýt obsah.

#Přidejte stát do komponenty Card, abyste sledovali, zda je otevřená (výchozí nastavení) nebo ne.
#Přidejte do šablony t-if, abyste podmíněně zobrazili obsah.
#Přidejte tlačítko do hlavičky a změňte kód tak, aby se stav měnil při kliknutí na tlačítko.

.. obrázek: 01_sokolovna_komponenty/přepínač karty.png
:skalka: 90 %
:align:center
