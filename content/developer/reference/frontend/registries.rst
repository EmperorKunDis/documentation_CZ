..._přední části / registrace:

==========
Registry
==========

Registry jsou (pořadí) klíč/hodnotové mapy. Jsou hlavním rozšířením pro webového klienta
body: mnoho funkcí poskytovaných prostřednictvím javascriptového rámce Odoo je pouze vyhledávání
do registru, pokud potřebuje definici nějakého objektu (například pole).
názory, akce klienta nebo služby). Přizpůsobení webového klienta je pak jednoduché.
Provedené přidáním konkrétních hodnot do správného registru.

... kódový blok: JavaScript

import { Registr } z "@web/jádro/registr";

const myRegistry = new Registry();

myRegistry.add("hello","odoo");

console.log(myRegistry.get("hello"));

Užitečnou vlastností registrů je, že udržují soubor podregistru.
získané metodou „kategorie“. Pokud podregistry ještě neexistuje,
vytváří se na lince. Webový klient používá všechny registry, které jsou získány
takto z jednoho kořenového registru exportované do @web/core/registry.

... kódový blok: JavaScript

import { registry } z "@web/jádro/registry";

const poleRegistr = registr.kategorie("pole");
const služby = registru.kategorie("služby");
const viewRegistry = registru.kategorii „názory“;

Registrační API
============

...:class:Registry

Založí nový registr. Registr je totiž událostní bus, takže jeden může
Pokud je nutné, poslouchejte událost UPDATE. Seznamy jsou seřazeny podle:
:js:metoda `getAll <Registry.getAll>` vrací seznam
hodnoty seřazené podle jejich čísla pořadí.

.. metoda: add(klíč, hodnota, [možnosti])

:param  stránka klíč: klíč pro nový záznam
:param jakýkoliv parametr: hodnota pro novou položku
:param:param Object options: options
:param:boolean options.force: nepřerušit pokud klíč již existuje
:param  number  [options.sequence]: číslo řádku (používá se k uspořádání záznamů)
:vrací: Registr

Vloží hodnotu do určitého klíče. Pokud je klíč již použitý, tato metoda
Pokud není nastavena možnost „force“ na hodnotu „true“, vyvolá chybu.
Metoda „sequence“ je užitečná pro vložení hodnoty na konkrétní pozici.
A také spouští událost „Update“.

Vrací stejný registr, takže se mohou řetězit metody „add“.

.. metoda: get(klíč, výchozí hodnota)

:param  string key: klíč pro vstup
:param defaultValue: hodnota vrácená, pokud pro daný klíč neexistuje žádná položka

Vrací hodnotu odpovídající klíči, který je předán jako argument. Pokud registr
Pokud tento klíč neobsahuje, vrátí tato metoda hodnotu defaultValue, pokud byla zadána, nebo vyhodí
Jinak by se jednalo o chybu.

...... metoda:contains(key)

:param  string key: klíč pro vstup
:vrací: bool

Vrací hodnotu „pravda“, pokud je klíč v registru

.....js:metoda::getAll()

:vrací: jakýkoliv objekt

Vrací seznam všech prvků v registru, které jsou uspořádány
podle číselných řad.

...... metoda: remove(key)

:param  stránka klíč: klíč pro vstup, který má být odstraněn

Odebere z registru klíč/hodnotu páru. Tato operace vyvolá
„Aktualizace“.

...  :metoda: kategorie (podkategorie)

:param:string subkategorie: název pro podkategorii
:vrací: Registr

Vrací podkategorie spojenou s kategorií „subcategory“. Pokud neexistuje,
Pokud ještě neexistuje, vytváří se podregistry na lince.

Seznam použité literatury
==============

.. seznam tabulkový::
:šířky: 30 70
:hlavičky: 1

   * Kategorie
     - Obsah
   * -:ref:`důsledky <frontend/registries/effects>`
     - implementace pro všechny dostupné efekty
   * :-:formátování viz frontend/registry/formatters
     - utility funkce pro formátování hodnot (nejčastěji používané pro pole).
   * – :ref:`hlavní komponenty <frontend/registry/main_components>`
     - komponenty na nejvyšší úrovni
   * :-[:ref:`parsovací funkce <frontend/registries/parsers>`
     - utility funkce pro zpracování hodnot (nejčastěji používané pro pole).
   * :-: služby <frontend/registries/services>
     - všechny služby, které by měly být aktivovány
   * – systray:<frontend/registries/systray>
     - komponenty zobrazené v systémové oblasti na navigační liště
   * - :ref:`<frontend/registries/usermenu>
     - položky nabídky zobrazené v uživatelském menu (v horní části navigačního panelu).

..._frontend/registries/effects:

Efektivní registr
---------------

Registr „Efekty“ obsahuje implementace všech dostupných efektů.
Podívejte se na část o službě :ref:`efektu <frontend/services/effect_registry>
Pro více informací.

..._frontend/registry/formátování:

Formátovací registr
------------------

Registr formátorů obsahuje funkce pro formátování hodnot. Každý formátor
Má následující API:

..js:funkce:: formát(hodnota, [možnosti])

:param value: hodnota konkrétního typu nebo „false“ v případě, že není zadána žádná hodnota
:typ hodnota: T | false
:parametru Objekt options: různé možnosti
:vrací: řetězec

Formátuje hodnotu a vrací řetězec

.. viz též:
    - :ref:`Registr parsovacích modulů <frontend/registries/parsers>`

... _frontend/registry/hlavní komponenty:

Hlavní registr složek
------------------------

Hlavní komponentní registr („main_components“) je užitečný pro přidávání hlavních komponent.
komponenty v webovém klientovi. Webový klient má jako komponentu „Hlavní komponenty“
přímý potomek. Tento komponent je v podstatě živou reprezentací pořadí
seznam komponent registrovaných v hlavním rejstříku součástek.

API
... kódový blok :: text

rozhraní {
Komponenta: třída komponenty Owl
props?: libovolný
        }


Příkladem může být přidání komponenty LoadingIndicator do registru takto
tohoto:

... kódový blok: JavaScript

registry.kategorie("hlavní komponenty").přidat("Nabíječ indikátoru stavu", {
Komponenta: Indikátor načítání
   });

..._frontend/registry/parser:

Registr parserů
---------------

Registry „parsovacích funkcí“ obsahuje funkce, které slouží k parsování hodnot. Každá z těchto funkcí
Má následující API:

..js:funkce::parse(hodnota, možnosti)
:noindex:

:param value: řetězec reprezentující hodnotu
:datový typ: řetězec
:param Object options: různé možnosti (specifické pro parser)
:vrací: T hodnotu

Parsuje řetězec a vrací hodnotu. Pokud řetězec nevyjadřuje platnou hodnotu,
hodnota, pak mohou být chybové hlášky.

.. viz též:
    - :ref:`Formátovací registr <frontend/registries/formatters>`

..._frontend/registry/služby:

Registr služeb
----------------

Služební rejstřík (kategorie: „služby“) obsahuje všechny
služby, které je třeba aktivovat v Odoo.
Rámec.

... kódový blok: JavaScript

import { registry } z "@web/jádro/registry";

const myService = {
závislosti: [...]
start(soubor_prostředí, závislosti) {
            // some code here
        }
    };

registry.kategorie("služby").přidat("můjSlužba", mySlužba);

... /frontend/registries/systray:

Systray registr
----------------

Systray je zóna vpravo od navigačního panelu, která obsahuje různé malé ikony.
komponenty, které obvykle zobrazují nějakou informaci (například počet
nečtené zprávy), oznámení a/nebo umožnit uživateli interagovat s nimi.

Registry „systray“ obsahuje popis těchto systémových ikon jako objektů.
s následujícími třemi klíči:

- `Komponenta“: třída komponenty, která reprezentuje položku. Její kořenový prvek
musí být značkou <li>, jinak se nemusí správně zformátovat.
- `props (volitelné)`: vlastnosti, které by měly být přiděleny komponentě
- `isDisplayed (volitelné)`: funkce, která přijímá :ref:`env <frontend/framework/environment>
a vrací logickou hodnotu. Pokud je hodnota pravdivá, zobrazí se položka systému Windows na ploše. V opačném případě nebude zobrazena.
byla odstraněna.

Příklad:

... kódový blok: JavaScript

import { registry } z "@web/jádro/registry";

třída MySystrayItem prodlouží třídu Component
        // some component ...
    }

registry.kategorie("systray").přidat("myAddon.myItem",
Komponenta: MySystrayItem
    });


Systémová oblast registru je uspořádaná podle pořadí (s číslem „sequence“):

... kódový blok: JavaScript

const item = {
Komponenta: Systémová lišta
    };
registry.category("systray").add("myaddon.some_description", item, { pořadí: 43 });

Výchozí hodnota sekvence je 50. Pokud je zadána, bude použita
a objednat položky. Nejnižší sekvence je na pravé straně a nejvyšší
je v levém sloupci systémové lišty.

... /přední část/registry/uživatelské menu:

Registr uživatelských menu
-----------------

Registr uživatelského menu (kategorie: `user_menuitems`) obsahuje všechny položky menu.
se zobrazí při otevření nabídky uživatele (element návrhového prvku s uživatelským jménem).
vpravo nahoře).

Položky nabídky uživatele jsou definovány funkcí, která přijímá proměnnou :ref:`env <frontend/framework/environment>
a vrací objekt bez jakýchkoliv informací:

* „popis“: text položky menu
* href: (volitelně) pokud je zadáno (a je pravdivé), text položky se vloží do značky <a> s atributem href.
* `callback_on_selection`: funkce volaná při výběru položky
* `skrýt“: (volitelné): ukazuje, zda položka by měla být skryta (výchozí hodnota: „false“),
* `sekvence`: (volitelné) určuje pořadí položky mezi ostatními položkami v seznamu (výchozí hodnota: 100).

Každé otevření uživatelského menu vyvolá všechny funkce definující položky.

Příklad:

... kódový blok: JavaScript

import { registry } z "@web/jádro/registry";

registry.kategorie("user_menuitems").přidat("můj položka", (env) =>
return {
popis: "Nastavení",
callback: () => {env.služby.akční manažer.vykonat akci (3);},
skrýt: (Math.random() < 0.5)
        };
    });
