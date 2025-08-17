.. _frontend/js_modules:

==================
Moduly JavaScriptu
==================

Odoo podporuje tři různé typy javascriptových souborů:

- :ref:`pouze soubory JavaScriptu <frontend/modules/plain_js>“ (bez modulového systému)
- :ref:`nativní modul JavaScriptu <frontend/modules/native_js>“.
- :ref:`Moduly Odoo <frontend/modules/odoo_module>“ (s vlastním systémem modulů)

Jak je popsáno na stránce o správě aktiv,
Všechny JavaScriptové soubory jsou sloučeny dohromady a poskytnuty prohlížeči.
Poznámka: Nativní JavaScriptové soubory jsou zpracovávány serverem Odoo a převáděny na moduly Odoo.

Nyní si stručně vysvětlíme účel každého typu souboru JavaScript.
javascriptové soubory by měly být vyhrazeny pouze pro externí knihovny a několik malých
konkrétní nízké úrovně účelu. Všechny nové soubory JavaScript by měly být vytvořeny
vlastní systém modulů v JavaScriptu. Vlastní systém modulů je užitečný pouze pro staré
nepřevoditelné soubory.

.. _frontend/moduly/plain_js:

Javascriptové soubory bez obrázků
======================

Plné soubory JavaScriptu mohou obsahovat libovolný obsah. Je doporučeno používat
Styl *iife* :dfn:`immediately invoked function execution`, při psaní takového souboru:

... kódový blok: JavaScript

(function () {
    // some code here
let a = 1;
console.log(a);
  })();

Výhodou takových souborů je, že se vyhnete úniku lokálních proměnných do
globálního rozsahu.

Jasně, prosté JavaScriptové soubory neposkytují výhody modulového systému.
Je třeba si dát pozor na pořadí v balíčku (protože prohlížeč
přesně v tomto pořadí).

.. poznámka::
Ve všech externích knihovnách se v Odoo načítají pouze prosté JavaScriptové soubory.

... /frontend/moduly/nativní_js:

Nativní moduly v JavaScriptu
=========================

Javascriptový kód v Odoo používá nativní systém modulů JavaScriptu. Je to jednodušší a
přináší výhody lepšího vývojářského zážitku spolu s lepším propojením s integrovaným vývojovým prostředím.

Pojďme se podívat na následující modul umístěný v souboru :file:`web/static/src/file_a.js`:

... kódový blok: JavaScript

import {someFunction} z „./file_b“;

exportní funkce otherFunction(val) {
return nějakáFunkce(val + 3);
  }

Je velmi důležité vědět, že výchozí nastavení Odoa je takové, že soubory překládá do
„/static/src“ a „/static/tests“ do sekce „Moduly Odoo“ v části „Frontend“:
Tento soubor pak bude přeložen do modulu Odoo, který vypadá takto:

... kódový blok: JavaScript

odoo.define('@web/file_a', ['@web/file_b'], funkce (vyžadovat) {
'use strict';
__exporty = {};

const {someFunction} = require('@web/file_b');

__export.jináFunkce = funkce jináFunkce (val) {
return nějakáFunkce(val + 3);
   };

vrací se __exporty
   )};

Takže vidíte, že transformace je v podstatě přidáním „odoo.define“ na vrch
a aktualizace vývozních a dovozních prohlášení. Jedná se o systém dobrovolného vyloučení, je možný
aby překladač ignoroval soubor.

... kódový blok: JavaScript

  /** @odoo-module ignore **/
(function () {
const sum = (a, b) => a + b;
console.log(součet(1, 2));
  )();

Pozor na první řádek komentáře: popisuje, že tento soubor se má ignorovat.

V jiných složkách se soubory nekompilují automaticky, je potřeba si o kompilaci požádat. Odoo bude hledat
první řádek souboru JS a zkontrolujte, jestli obsahuje komentář s *@odoo-module* bez
tagu *ignorovat* a pokud ano, bude automaticky převeden na modul Odoo.

... kódový blok: JavaScript

  /** @odoo-module **/
exportní funkce sum(a, b) {
vrácení hodnoty a + b.
  }

Dalším důležitým bodem je, že přeložený modul má oficiální název:
*@web/soubor_a*. To je skutečný název modulu. Každý relativní import
bude také převedena. Každý soubor umístěný v Odoo doplňku
:souboru `some_addon/static/src/cesta/k/souboru.js` bude přiděleno jméno začínající
Název doplňku ve tvaru: *@some_addon/cesta/k/souboru*.

Relativní importy fungují, ale pouze pokud moduly jsou v jednom odoo doplňku. Takže představme si, že máme
struktuře souborů:

::

addons/
web/
statické
src/
file_a.js
soubor_b.js
zásoby/
statické
src/
file_c.js

Soubor :file:`file_b` může do sebe importovat soubor :file:`file_a`, například takto:

... kódový blok: JavaScript

import {něco} z „./soubor_a“;

Ale souboru `file_c` je třeba použít celé jméno:

... kódový blok: JavaScript

import {něco} z "@web/soubor-a";

Aliasované moduly
---------------

Protože moduly :ref:`Odoo <frontend/modules/odoo_module>` mají jiný vzorec pro pojmenování modulů, existuje systém, který umožňuje plynulé
přechod k novému systému. V současné době se při převodu souboru na modul (a tedy
sledovat nové pojmenování), jiné soubory, které ještě nebyly převedeny na syntaxi podobnou ES6 v projektu
nebude moci požadovat modul. Aliasy jsou zde proto, aby převedly staré názvy na nové tím, že vytvoří
malé funkce proxy. Modul lze pak volat pod svým novým i starým názvem.

Aby se takový přezdívkový název mohl použít, musí být v horním komentáři souboru napsán tento řetězec:

... kódový blok: JavaScript

  /** @odoo-module alias=web.someName**/
import { nějakáFunkce } z „./soubor_b“;

export default funkce otherFunction(val) {
return nějakáFunkce(val + 3);
  }

Poté vytvoří modul překladu také alias s požadovaným názvem:

... kódový blok: JavaScript

odoo.define('web.someName', ['@web/file_a'], function (require) {
return vyžadovat (z '@web/file_a') [Symbol.for ("default")]
  });

Výchozí chování aliasů je reexportovat hodnotu „výchozí“
Modul, který je vlastně jenom přezdívkou. To proto, že „klasické“ moduly obvykle exportují pouze jednu
hodnota, která by se používala přímo a přibližně odpovídala významu výchozí
exportu.
Je však také možné delegovat přímo a sledovat přesný
chování modulu, který je aliasovaný:

... kódový blok: JavaScript

  /** @odoo-module alias=web.someName default=0**/
import { nějakáFunkce } z „./soubor_b“;

exportní funkce otherFunction(val) {
return nějakáFunkce(val + 3);
  }

V takovém případě bude definováno jméno s přesnými hodnotami exportovanými
původní modul:

... kódový blok: JavaScript

odoo.define('web.someName', ['@web/file_a'], function (require) {
return vyžadujte ('@web/soubor_a');
  });

.. poznámka::
Jediný alias lze definovat touto metodou. Pokud byste potřebovali další, museli byste si ho vytvořit jinak.
Příklad: pokud byste chtěli tři názvy volat stejný modul, museli byste ručně přidat proxy.
Toto není dobrá praxe a mělo by se jí vyhnout, pokud neexistují žádné další možnosti.

Omezení
-----------

Pro výkonnostní důvody používá Odoo neúplný JavaScript.
parsování nativních modulů. Existuje tedy řada omezení včetně
omezeno na:

- klíčové slovo import nebo export nemůže být předcházeno nezpětnou lomítkem.
- Multiline komentář nebo řetězec nemůže začínat řádkem s importem nebo exportem.

...... kódový blok:: javascript

    // supported
import x od „xxx“;
export X;
export default X;
import x od "xxx";

    /*
     * dovoz X ...
     */

    /*
     * export X
     */


    // not supported

var a = 1;
    /*
import X ...
    */

- Když exportujete objekt, nemůže obsahovat komentář.

...... kódový blok:: javascript

      // supported
export {
a jako b
        c,
        d,
      }

export {
        a
} z „./soubor_a“


      // not supported
export {
a jako b, // komentář
        c,
        d,
      }

export {
a /* toto je komentář */
} z „./soubor_a“

- Odoo potřebuje způsob, jak zjistit, jestli modul je popsán cestou (například: . / views / form_view „).
nebo jméno (například web.FormView). Musí použít heuristiku, aby to dokázal: pokud je v názvu znak "/",
jméno se považuje za cestu. To znamená, že Odoo nepodporuje skutečně moduly s
a nezobrazuje již čárku „/“.

„Klasické“ moduly nejsou zastaralé a v současné době není žádný plán na jejich odstranění. Proto byste je měli i nadále používat
pokud narazíte na problémy s nativními moduly nebo pokud jsou omezeny limity nativních modulů. Oba styly mohou existovat vedle sebe
v rámci stejného doplňku Odoo.


... /odoo_modul:

Modulový systém Odoo
==================

Odoo definovalo malý modulový systém (soubor
:souboru „addons/web/static/src/js/boot.js“, který musí být načten jako první).
modulový systém inspirovaný společností AMD funguje na základě definice funkce „define“
na globálním objektu Odoo. Každý javascriptový modul pak definujeme voláním
funkce. V rámci Odoo frameworku je modul kus kódu, který se spustí
jakmile to bude možné. Má název a potenciálně nějaké závislosti. Když se
Poté se načte i modul. Hodnota proměnné
Modul je pak návratovým parametrem funkce definující modul.

Příklad může vypadat např. takto:

... kódový blok: JavaScript

    // in file a.js
odoo.define('modul.A', [], funkce (vyžadovat) {
„použijte přísný režim“;

var A = ...;

vrátí se hodnota A.
    });

    // in file b.js
odoo.define('modul.B', ['modul.A'], funkce (vyžadovat) {
„použijte přísný režim“;

var A = require('modul.A');

var B = ...; // něco, co zahrnuje A

vrátí se hodnota B.
    });


Pokud některé závislosti chybí nebo nejsou připraveny, pak modul jednoduše nebude
Následně se v konzoli objeví varování.

Pozor, cyklické závislosti nejsou podporovány. To dává smysl, ale znamená to, že
Je potřeba být obezřetný.

Definování modulu
-----------------

Metoda `odoo.define` má tři argumenty:

- `nazev modulu`: název javascriptového modulu. Měl by být jedinečný.
Pravidlem je, že se jméno odoo doplňku píše za specifickým
popis. Například „web.Widget“ popisuje modul definovaný v souboru „web“.
doplněk, který exportuje třídu Widget (protože první písmeno je velké).

Pokud je jméno nejedinečné, bude vyhozena výjimka a zobrazeno v
Konzole.

- „závislosti“: mělo by jít o seznam řetězců, každý z nich odpovídá
JavaScript modul. Tento popisuje závislosti, které jsou nutné k instalaci
se načíst před spuštěním modulu.

- Poslední argument je funkce, která definuje modul. Jeho návratová hodnota
hodnota je hodnota modulu, kterou lze předat do jiných modulů vyžadujících
it.

...... kódový blok:: javascript

odoo.define('modul.Něco', ['web.ajax'], funkce (vyžadovat) {
„použijte přísný režim“;

var ajax = require('web.ajax');

         // some code here
vrátit se někam.
     });

Pokud dojde k chybě, bude zobrazena v konzole (v režimu ladění):

* „Chybějící závislosti“:
Tyto moduly se na stránce nezobrazují. Je možné, že skriptování
soubor není na stránce nebo že je špatně zadaný název modulu
* „Nefunkční moduly“:
Vyhodnoceno jako chyba v JavaScriptu
* „Odmítnuté moduly“
Modul vrátí odmítnutý slib. A stejně tak i jeho závislé moduly nejsou
naplněné.
* „Odmítnuté moduly s odkazy“:
Moduly, které na odmítnutém modulu závisí
* „Nemodulované moduly“:
Moduly, které závisí na chybějícím nebo selhávajícím modulu
