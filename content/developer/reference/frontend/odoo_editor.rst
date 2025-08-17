===========
Odoo Editor
===========

Editor Odoo je vlastní bohatý textový editor společnosti Odoo. Jeho zdrojové kódy lze najít na
Složka s editorem odoo
<{GITHUB_PATH}/addons/web_editor/static/src/js/editor/odoo-editor>.

Powerbox
========

Powerbox je uživatelské rozhraní, které obsahuje
:ref:`příkazy <odkaz/přední-panel/odoo-editor/powerbox/příkazy>“
do kategorií:ref:`<reference/frontend/odoo_editor/powerbox/category>“.
objeví se při zadávání znaku / v editoru. Příkazy lze filtrovat po
uživatel zadává text a pohybuje se klávesami šipkami.

.. obrázek: odoo_editor/powerbox.png
:align:center
:alt: Po zadání „/“ se otevřel Powerbox.

Upravit Powerbox
----------------------

Každý čas se má spustit pouze jeden Powerbox a tuto práci dělá
sám redaktor. Jeho instanci Powerboxu lze najít v jeho instanci powerbox
proměnná.
Pro změnu obsahu a možností Powerboxu změňte parametry předané
editor před jeho instancováním.

.. důležité:
Nikdy nesnažte se vytvořit vlastní Powerbox. Vždy používejte editor, který je k dispozici.
případě.

Příklad:
Předpokládejme, že chceme přidat novou příkazovou řádku „Dokument“ do Powerboxu.
„Masová pošta“. Chceme ji přidat do nové kategorie s názvem
„Dokumentace“ a chceme ji mít na vrcholu Powerboxu.

`Masová pošta´ ‚rozšiřuje

třída Wysiwyg v rámci webového editoru
<{GITHUB_PATH}/addons/web_editor/static/src/js/wysiwyg/wysiwyg.js>`, které
v metodě start() inicializuje editor.
Metoda se jmenuje _getPowerboxOptions a je velmi pohodlná.
aby přidaly naše nové příkazy.

Pokud funkce „masová pošta“ již předdefinuje metodu „_getPowerboxOptions“, tak nemá smysl ji přidávat.
naše nové příkazy k němu:

... kódový blok :: JavaScript

_getPowerboxOptions: function () {
const options = this._super();
          // (existing code before the return statement)
options.kategorie.push({
jméno: _t('Dokumentace'),
priorita: 300,
          });
options.příkazy.push({
jméno: _t('Dokument'),
kategorie: _t('Dokumentace'),
popis: _t("Přidejte tento text do dokumentace k e-mailu"),
fontawesome: 'fa-book',
priorita: 1, // Toto je totiž jediná příkaz v kategorii.
          });
vrací se možnosti.
      }

...... důležité::
Pro umožnění názvů a popisů vašich příkazů a
kategorie, které chcete přeložit, ujistěte se, že je obalíte funkcí _t.

.......tip::
Aby nedocházelo k nekontrolovatelnému eskalování, nepoužívejte náhodná čísla.
priorit: podívejte se, které priority již existují a vyberte si své.
hodnotu odpovídající tomu, jak byste ji nastavili pro z-index.

Otevření vlastního powerboxu
-------------------------

Je možné otevřít Powerbox s vlastním nastavením kategorií.
příkazů, přeskočí všechny předchozí příkazy. K tomu zavolejte metodu
Powerbox a předáte mu své vlastní příkazy a kategorie.

.. obrázek: odoo_editor/powerbox-custom.png
:align:center
:alt:Powerbox otevřel s vlastními kategoriemi a příkazy, když jsem do něj vložil
URL obrázku.

Příklad:
Potřebujeme aktuální verzi Powerboxu, která se nachází v
aktuálním redaktorem. Třída Wysiwyg
<{GITHUB_PATH}/addons/web_editor/static/src/js/wysiwyg/wysiwyg.js>`,
najde jako "toto.odooEditor.powerbox".

Teď otevřít s naším vlastním „Dokument“ příkazem v našem vlastním
Kategorie „Dokumentace“

... kódový blok :: JavaScript

tento.editorOdoo.otevřít (
          [{
jméno: _t('Dokument'),
kategorie: _t('Dokumentace'),
popis: _t("Přidejte tento text do dokumentace k e-mailu"),
fontawesome: 'fa-book',
priorita: 1, // Toto je totiž jediná příkaz v kategorii.
          }],
          [{
jméno: _t('Dokumentace'),
priorita: 300,
          }]
      );

Filtry příkazů
------------------

Existují tři způsoby filtrování příkazů:

#Ve filtru „powerboxFilters“.
:ref:`Možnost Powerboxu <reference/frontend/odoo_editor/powerbox/options>.
#. Prostřednictvím určitého
:ref:`příkazu <odoo_editor_powerbox_command>
položka „je vypnutá“.
#Uživatel může filtrovat příkazy jednoduše tím, že po otevření
Powerbox. Ten bude hledat shodu s názvy kategorií a
příkazy.

.. obrázek: odoo_editor/powerbox-filtered.png
:align:center
:alt:Příkazová skříňka s filtrací příkazů pomocí slova „hlava“.

Reference
---------

.. odkaz na editor Odoo

Kategorie
~~~~~~~~

.. seznam tabulkový::
:šířky: 20 20 60
:hlavičkové řádky: 1

    * - Jméno
      - Typ
      - Popis
    * – „jméno“
      - „smyčka“
      - název kategorie
    * – „Priorita“
      - „číslo“
      - používá se k určení prioritní kategorie: vyšší priorita má
Vyšší priorita je v kategoriích, které jsou výše v Powerboxu.
jsou seřazeny abecedně.

.. poznámka::
Pokud existují kategorie se stejným názvem, budou seskupeny do
Jedním z nich bude právě tento, jeho prioritou bude ta definovaná v kategorii verze
Byl vyhlášený poslední.

.. odkaz na editor Odoo:

Příkaz
~~~~~~~

.. seznam tabulkový::
:šířky: 20 20 60
:hlavičkové řádky: 1

    * - Jméno
      - Typ
      - Popis
    * – „jméno“
      - „smyčka“
      - název příkazu
    * „kategorie“
      - „smyčka“
      - název kategorie, do které patří příkaz
    * Popis
      - „smyčka“
      - krátký popis příkazu
    * - `fontawesome`
      - „smyčka“
      - název fontu Awesome, který bude sloužit jako ikona příkazu
    * – „Priorita“
      - „číslo“
      - používá se k zadání příkazu: je zobrazen příkaz s vyšší prioritou
Vyšší do Powerboxu (příkazy s stejnou prioritou jsou seřazeny
abecedně
    * – „callback“
      - „funkce“ („() => void“)
      - funkce, která se spustí při vyzvednutí příkazu (může být asynchronní)
    * – isDisabled (volitelné)
      - „funkce“ („() => void“)
      - funkce, která v určitých podmínkách příkaz deaktivuje (pokud
Pokud je hodnota vrácena jako „pravda“, bude příkaz zakázán.

.. poznámka::
Pokud příkaz odkazuje na kategorii, která ještě neexistuje, taková kategorie
Bude vytvořen a připojen na konec Powerboxu.

.. odkaz na editor Odoo:

Možnosti
~~~~~~~

Následující možnosti lze předat editoru Odoo, který je poté předán
Příklad PowerBoxu:

.. seznam tabulkový::
:šířky: 20 20 60
:hlavičkové řádky: 1

    * - Jméno
      - Typ
      - Popis
    * „povely“
      - „soubor příkazů“
      - příkazy, které se přidávají k výchozím hodnotám definovaným v editoru
    * – „kategorie“
      - „soubor kategorií“
      - kategorie, které je možné přidat k výchozí kategorii definované redaktorem
    * – „powerboxFilters“
      - „soubor funkcí“ („příkazy => příkazy“)
      - funkce používané k filtrování zobrazovaných příkazů v Powerboxu
    * – `getContextFromParentRect`
      - `funkce` (`=> DOMRect`)
      - funkce, která vrací DOMRect předka editoru (může
může být užitečné, pokud je editor v rámci stránky.
