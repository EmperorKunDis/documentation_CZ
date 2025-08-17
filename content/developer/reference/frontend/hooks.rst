.. _frontend/hooks:

=====
Háčky
=====

„Háčky sovy“ jsou uvedeny na stránce „Reference“ v dokumentaci „Owl hooks <https://github.com/odoo/owl/blob/master/doc/reference/hooks.md>“.
cestu k faktorizaci kódu, i když závisí na životním cyklu nějaké složky. Většina háčků
Owl poskytuje informace o životním cyklu komponenty, ale některé z nich (např.
`použít komponentu <https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#usecomponent>`_
poskytnout způsob, jak vytvářet konkrétní háčky.

Pomocí těchto háčků lze vytvořit mnoho přizpůsobených háčků, které pomáhají řešit
konkrétní problém nebo usnadnit některé běžné úkoly. Zbytek této stránky
dokumentuje seznam háčků poskytovaných webovým rámcem Odoo.

.. seznam tabulkový::
:šířky: 30 70
:hlavičky: 1

   * - Jméno
     - Stručný popis
   * :-:použít aktiva <frontend/hooks/useassets>
     - nabídnout aktivum
   * – :ref:`používat automatické ostření <frontend/hooks/useAutofocus>`
     - automaticky zaostřit na prvek, který je odkazován autofokusem
   * – :ref:`použítBus <frontend/hooks/usebus>`
     - přihlásit se a odhlásit z autobusu
   * :-:použít pager
     - Zobrazit stránku ovládacího panelu pro zobrazení pohledu.
   * – :ref:`použít pozici <frontend/hooks/useposition>“
     - umístit prvek vzhledem k cíli
   * – :ref:`používat kontrolu pravopisu <frontend/hooks/useSpellCheck>`
     - zapnout kontrolu pravopisu na soustředění pro vstup nebo textové pole

..._frontend/hooks/useassets:

použít aktiva
=========

Lokalita
--------

@web/jádro/aktiva

Popis
-----------

Podívejte se na část o :ref:`příspěvku s názvem „Lazy Loading Assets“ <frontend/assets/lazy_loading>
více informací.


..._frontend/hooks/useAutofocus:

použítAutofokus
============

Lokalita
--------

@web/core/utils/hooks

Popis
-----------

Zaměřit prvek, který je odkazován pomocí t-ref="autofocus", v aktuálním komponentu.
jakmile se objeví v DOM a pokud nebyla zobrazena předtím.

... kódový blok: JavaScript

import { useAutofocus } z "@web/core/utils/hooks";

třída Comp {
setup() {
tento.vstupní odkaz = použít automatické zaostření ();
      }
statický šablonový řetězec = "Comp";
    }

... blok kódu::xml

<t t-name="Společnost">
<input t-ref="auto_fokus" typ="text"/>


API
---

..js:function:: použít automatické ostření

:vrací odkaz na prvek.

.._frontend/hooks/usebus:

useBus
======

Lokalita
--------

@web/core/utils/hooks

Popis
-----------

Přidejte a vymažte událostní slyšenou na autobusu. Tento háček zajišťuje, že
Posluchač je správně vyčištěn, když se komponenta odpojí.

... kódový blok: JavaScript

import { useBus } z "@web/core/utils/hooks";

public class MyComponent
setup() {
použijBus(tento.env.bus, „nějaký-událost“, (event) => {
console.log(událost);
        });
      }
    }

API
---

..js:funkce: použít autobus (autobus, událostní jméno, zpětná volání)

:param EventBus bus: cílový eventbus
:param  string  eventName: jméno události, kterou chceme sledovat
:param funkce callback: callback posluchače

..._frontend/hooks/usepager:

použijtePage
========

Lokalita
--------

@web/hledani/pager_hook

Popis
-----------

Zobrazte sekci „Páger“ ovládacího panelu pohledu. Tento krok správně nastaví proměnné prostředí, aby poskytly parametry pro páger.

... kódový blok: JavaScript

import { usePager } z "@web/search/pager_hook";

třída CustomView {
setup() {
const state = useState({
offset: 0,
limit: 80
celkem: 50
        });
použijte pager(=> {
return {
offset: tento.stát.offset,
limit: tento.stát.limit
celkem: tento.stav.celkem
onUpdate: (novýStav) => {
Object.assign(toto.stát, novýStát);
            },
          };
        });
      }
    }

API
---

...js:function::usePager(getPagerProps)

:param funkce getPagerProps: funkce, která vrací hodnoty pageru.

.._frontend/hooks/useposition:

usePosition
===========

Lokalita
--------

@web/jádro/položka_hooku

Popis
-----------

Pomáhá při umisťování HTML elementu (tj. „popup“) vzhledem k jinému
HTMLElement (vzorec „odkaz“). Tento háček zajišťuje, že se pozice aktualizuje při
okno se změní velikost nebo posune.

... kódový blok: JavaScript

import { usePosition } z "@web/core/position_hook";
import { Komponenta, XML } z "@odoo/owl";

class MyPopover extends Component {
statická šablona = XML
<div t-ref="popper">
Jsem na krásném háku!
</div>
      `;

setup() {
        // Here, the reference is the target props, which is an HTMLElement
použít pozici (tento.props.target);
      }
    }

.. důležité:
Uveďte svůj prvek „popup“ pomocí příkazu „t-ref <https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#useref>“.

API
---

..js:funkce: použít pozici (odkaz, možnosti)

:param reference: cílový HTML prvek, od něhož se má pozice vypočítat
:typ odkazu: HTML prvek nebo funkce, která vrací HTML prvek
:param Options options: možnosti umístění (viz tabulka níže)

.. seznam tabulkový::
:šířky: 20 20 60
:hlavičky: 1

   * – možnost
     - Typ
     - Popis
   * „poper“
     - string
     - toto je „vazba na referenci <https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#useref>“ pro prvek, který se bude posouvat.
Výchozí hodnota je „popper“.
   * „kontejner“
     - HTMLElement
     - kontejner, ze kterého se očekává, že nebude přetékat.
dochází k přetečení, zkoušejí se další pozice poperů až do
je nalezena přebytečná značka. (výchozí: značka `
   * „- margin“
     - číslo
     - přidává mezery mezi pop-up a referenčními prvky (výchozí hodnota: 0)
   * „- pozice“
     - Směr[-variant]
     - žádané umístění. Jedná se o řetězec, který obsahuje jeden objekt Direction a jeden
Varianta oddělená znakem „-“.
„Směr“ může být například „nahoru“, „dolů“, „vpravo“ nebo „vlevo“.
„Varianta“ může být například „začátek“, „střed“, „konec“ nebo „pasuje“.
Varianta může být vynechána (výchozí varianta je „middle“).
Varianta „fit“ znamená, že by měl mít stejnou šířku nebo výšku jako popper.
podle zvolené směru.
Příklady platných pozic: „vpravo nahoře“, „vlevo doleva“, „vpravo uprostřed“.
„levá“, „dolní“. (Výchozí pozice: „dole“)
   * – `onPositioned`
     - (element: HTMLElement, pozice: Pozicování řešení) => prázdné
     - volání, které se spustí pokaždé, když dojde k určení polohy.
(např. na komponentu nainstalované/opravené, procházení dokumentu, změnu velikosti okna ...).
Může být použito například pro dynamické formátování podle současné pozice.
„Posílení pozice“ je objekt, který má následující typ:
{ směr: Směr, varianta: Varianta, top: číslo, left: číslo }.

Příklad:

... kódový blok::javascript

import { Komponenta, xml, použítRef } z "@odoo/owl";
import { usePosition } z "@web/jádro/položka_výstupu";

třída DropMenu prodlouží třídu Komponenta
statická šablona = XML
<toggler ref="toggler">Zobrazit menu</toggler>
<div t-ref="menu">
<t t-slot="default">
Toto je výchozí obsah menu.


        `;

setup() {
const toggler = useRef("toggler");
použít pozici (
=> toggler.element
            {
popper: "menu",
pozice: "vlevo nahoře"
onPositioned: (el, { směr, varianta }) => {
el.classList.add(`dm-${směr}`); // -> „dm-nahoru“ „dm-vpravo“ „dm-dolů“ „dm-vlevo“
el.styl.barva = variant === "prostředek" ? "červená" : "modrá";
              },
            },
          );
        }
      }

..._frontend/hooks/useSpellCheck:

použít kontrolu pravopisu
=============

Lokalita
--------

@web/core/utils/hooks

Popis
-----------

Aktivujte kontrolu pravopisu na vstup nebo textovém poli při získání soustředění pomocí t-ref="spellcheck"
současný komponent. Tento stav je pak odstraněn při přechodu do nezaostřeného režimu, stejně jako červený obrys, který
Zlepšuje čitelnost obsahu.

Hák může být také použit na jakýkoliv HTML prvek s atributem „contenteditable“.
Spellcheck zcela na prvky, které mohou být aktivovány háčkem, a explicitně nastavte
Přidat atribut „spellcheck“ s hodnotou „false“ na prvek.

Příklad:

V následujícím příkladu bude kontrola pravopisu zapnuta na prvním vstupu, tedy textovém poli.
div s atributem „contenteditable=“true“.

... kódový blok::javascript

import { useSpellCheck } z "@web/core/utils/hooks";

třída Comp {
setup() {
tento.jednoduchýOdkaz = použít kontrolu pravopisu();
tento.vlastníRef = použít kontrolu pravopisu (refName: „vlastní“);
tento.nodeRef = použijte kontrolu pravopisu (refName: „obal“);
         }
statický šablona = "Comp";
       }

... kódový blok :: XML

<t t-name="Společnost">
<input t-ref="spellcheck" type="text"/>
<textarea t-ref="vlastní_textová_oblast"/>
<div t-ref="container">
<input type="text" spellcheck="false"/>
<div editovatelný="true"/>

</t>

API
---

..js:funkce: použít kontrolu pravopisu ([možnosti])

:param Options options: možnosti kontroly pravopisu (viz tabulka níže)

.. seznam tabulkový::
:šířky: 20 20 60
:hlavičky: 1

   * – možnost
     - Typ
     - Popis
   * „refName“
     - string
     - to je odkaz na „příručku <{OWL_PATH}/doc/reference/hooks.md#useref>“ pro prvek, který bude
zapnutý kontrolní režim.
