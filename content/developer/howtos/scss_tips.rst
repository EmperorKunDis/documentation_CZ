===============================
Napište tenký, snadno udržovatelný CSS
===============================

Existuje mnoho způsobů, jak zjednodušit a zúžit SCSS. Prvním krokem je zjistit, jestli existuje vlastní kód
nebyla potřebná vůbec.

Webový klient Odoo je navržen jako modulární, což znamená, že (případně všechny) třídy mohou být
sdílené mezi pohledy. Před vytvořením nové třídy se ujistěte, že neexistuje žádný
třída nebo HTML značka, která přesně dělá, co hledáte.

Navíc Odoo využívá framework Bootstrap.
<https://getbootstrap.com/docs/5.1/getting-started/introduction/>`_ (Bootstrap), jedna z nejkomplexnějších
K dispozici jsou rámce CSS. Rámec byl upraven tak, aby odpovídal designu Odoo (včetně
komunitní a podnikové verze, což znamená, že můžete používat jakoukoli třídu BS přímo v Odoo.
dosáhnout vizuálního výsledku, který je v souladu s naším uživatelským rozhraním.

.. varování:
   - Skutečnost, že třída dosáhne požadovaného vizuálního výsledku, neznamená nutně, že je
správnou volbou. Buďte si vědomi tříd vyvolávajících chování v JavaScriptu, např.
   - Buďte opatrní při výběru tříd. Použití třídy „tlačítko“ na titulek není pouze
Semanticky špatně může vést i k migračním problémům a vizuálním nesouladům.

Následující části popisují tipy, jak odstranit řádky SCSS **když je použití vlastního kódu jedinou možností.
go***.

... _tutorials/scss_tips/browser_defaults:

Výchozí nastavení prohlížeče
================

Výchozí nastavení každého prohlížeče říká, že obsah by měl být zobrazen pomocí šablony stylu uživatelského agenta.
Nesoulad mezi prohlížeči. Některá z těchto pravidel jsou překryta „Bootstrap Reboot
<https://getbootstrap.com/docs/5.1/content/reboot/>`.

V této fázi byly všechny „příslušné pro konkrétní prohlížeč“ pravidla odstraněna, ale velká část
pravidla definující základní informace o uspořádání je udržováno (nebo posíleno pomocí *Rebootu* pro konzistenci
důvodů).

Můžete se na ně spolehnout.

Příklad:

Použití vlastnosti display: block; na elementu div je obvykle zbytečné.

... blok kódu:: css

div.element {
zobrazení: blok;
         /* not needed 99% of the time */
      }

Příklad:

V tomto případě můžete zvážit přepnutí značky HTML namísto přidání nové pravidlo CSS.

... blok kódu:: css

span.element {
zobrazení: blok;
         /* replace <span> with <div> instead
aby výchozí hodnota byla „zobrazeno: blok“
      }

Tady je seznam obecných pravidel:

.. seznam tabulkový::
:hlavičky: 1

   * Tag/Atribut
     - Výpovědi
   * <div>, <section>, <header>, <footer> ...
     - „zobrazit: blok“
   * <span>, <a>, <em>, <b>...
     - „inline“
   * <button/>, <label/>, <output/>...
     - „inline-block“
   * – ``, „
     - „vertical-align: middle“
   * 
     - „kurzor: ukazatel;“
   * 
     - | `":before {content: otevřený citát}`
| `":after {content: zavřený citát}`
   * - ...
     - ...

.. viz též:
„Bootstrap Reboot na GitHubu
<https://github.com/twbs/bootstrap/blob/1a6fdfae6b/sass/_reboot.scss>`_

... _tutorials/scss_tips/html_tags:

HTML tagy
=========

Možná to zní jako klišé, ale nejjednodušší a nejpřesnější způsob, jak udělat text vypadat jako nadpis
použít nadpisový tag („<h1>“, „<h2>“ atd.). Kromě pravidel pro resetování stylů většina značek nese dekorativní
styly definované v Odoo.

.. první třídy: bglight
Příklad:

......container:: varování varování-nebezpečí

Ne

... záložky::

... kódová tabulka:: HTML XML


Ahoj, tady je někdo.



Já jsem titulek.


...:: CSS SCSS

.o_module_custom_title {
zobrazení: blok;
font-size: 120%;
font-weight: 700;
animace: 1s lineární 1s mycustomAnimation;
            }

.o_module_custom_subtitle {
zobrazení: blok;
font-size: 12px;
font-weight: 700;
animace: 2s lineární, 1s mycustomAnimation;
            }

... kontejner:: varování varování-úspěch

      Do

... záložky::

... kódová tabulka:: HTML XML

<h5 třída="o_modul_vlastní_nadpis">
Ahoj, tady je někdo.
</h5>

<div class="o_module_custom_subtitle">
<b><small>Jsem titulek.</small></b>
</div>

...:: CSS SCSS

.o_module_custom_title {
animace: 1s lineární 1s mycustomAnimation;
            }

.o_module_custom_subtitle {
animace: 2s lineární, 1s mycustomAnimation;
            }

.. poznámka::
Kromě snížení množství kódu přináší modulární design (použití tříd, značek, mixinů...)
Zajišťuje konzistentní vizuální výsledek a snadno udržovatelný kód.

Pokud se změní design titulů Odoo, budou tyto změny aplikovány v
také prvku „o_module_custom_title“, protože používá značku <h5>.

... /návody/css-tipy/utility-třídy:

Utilitární třídy
===============

Naše rámec definuje mnoho užitečných tříd, které pokrývají téměř všechny
layoutu, designu nebo interakce. Jednoduchá skutečnost, že třída už existuje, je důvodem k jejímu použití místo
vlastní CSS, pokud je to možné.

Pojďme si ukázat příklad „position-relative“.

... kódový blok:: CSS

pozice-relativní {
pozice: relativní !důležité;
   }

Od té doby, co je definována třída utilit, každá CSS řádka s deklarací „position: relative“
**možná** zbytečný.

Odoo staví na základních třídách Bootstrapu.
<https://getbootstrap.com/docs/5.1/utilities/background/>`_ stack a definuje vlastní pomocí
„API Bootstrap <https://getbootstrap.com/docs/5.1/utilities/api/>“.

.. viz též:
   - „Utility třídy Bootstrapu <https://getbootstrap.com/docs/5.1/utilities/api/>“
   - „Odoo Custom Utilities na GitHubu


... _tutorials/scss_tips/utility_classes/downside:

Zpracování utility tříd
----------------------------------

Nevýhodou tříd s užitečnými funkcemi je potenciální nedostatek čitelnosti.

Příklad:

... blok kódu:: html

<komponenta t-attf-class="d-flex border px-lg-2 card
{{props.readonly ? 'o_myComponent_disabled' : ''}}
karta d-lg-block pozice-absolutní {{vlastnosti.aktivní?
"o_myComponent_active": ""}

Pro řešení problému můžete kombinovat různé přístupy:

- V atributu Qweb používejte třídy jen pro přepínání *na lince*.
- použijte nové řádky pro každý atribut.
- řazení tříd podle konvence „[názov odoo komponenty] [název bootstrap komponenty] [pořadí deklarace v css souboru]“.

Příklad:

... blok kódu:: html

<komponenta
t-att-class="
o_myComponent_disabled: props.readOnly,
o_myComponent_active: props.active
         }"
"class":"myComponent card pozice-absolutní flexibilní d-flex d-lg-blokový hrana px-3 px-lg-2"
      />

.. viz též:
:ref:`Pořadí vlastností CSS <contributing/coding_guidelines/scss/properties_order>`
