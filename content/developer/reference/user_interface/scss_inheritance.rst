================
Dědění podle zákona o dědictví
================

Přehled
========

Správa aktiv SCSS v Odoo není tak jednoduchá jako v některých jiných prostředích, ale je
Velmi účinná.

Modulárnost je klíčová. Dědění popsané dále umožňuje Odoo:

- přizpůsobit rámec Bootstrapu.
- umět pracovat s dvěma různými designy klienta (Community a Enterprise).
- zpracovávat balíčky na serverové a klientské straně samostatně (včetně vzhledu webu uživatele).
- načítat pouze nezbytné soubory.
- umět pracovat s více barevnými schématy (např. tmavý režim).

Řízení výchozích hodnot v SCSS
===========================

„Přesměrování proměnných“ je v Sassu možné, ale může vést k nekonzistentním výsledkům.
v komplexních prostředích jako je Odoo.

Příklad:

... kódový blok: scss
:caption: :file:`library.scss`

$foo: červená;

... kódový blok: scss
:předpis: :soubor: `customization_layer.scss`

$foo: modrá; //-> Nedělejte to!

Skutečně, protože proces sestavování působí na různé nezávislé balíky, přidělování
Proměnná v „špatné“ pozici může vést k nečekaným důsledkům.

SCSS nabízí několik technik, jak tyto problémy překonat
(např. „stínování“ <https://sass-lang.com/documentation/variables#shadowing>“), ale nejčastěji
Kritická procedura v Odoo je použití znaku „!default“.

Při použití vlajky „!default“ přidělí kompilátor hodnotu jenom v případě, že proměnná ještě
definováno.

Tímto způsobem je přiřazena priorita proměnným v souladu s aktivy.
pořadí načítání.

Příklad:

... kódový blok: scss
:předpis: :soubor: `customization_layer.scss`

$foo: červená !výchozí;

... kódový blok: scss
:caption: :file:`library.scss`

$foo: modrá !default; // -> Už je definovaná, řádek ignorován.
$bar: černá !default; //->Není definováno ještě, hodnota přiřazena.

... blok kódu::
:caption: :file:`component.scss`

.komponenta {
barva: $foo; // -> 'barva: červená;'
pozadí: $bar; // -> 'základní barva: černá;'
      }

.. viz též:
!default v dokumentaci SASS


Dědění systému SCSS společnosti Odoo
==============================

Následující schéma ilustruje pořadí sestavení, ve kterém se používají CSS a SCSS.
Definují se proměnné.

... blok kódu:: text

↓ [Sestava začíná]
    ⏐
↓ web.tmavý_režim
⏐    ├─ Primární proměnné
⏐    └─ Komponenty proměnných
    ⏐
↓ web._assets_primary_variables
⏐   │ └─ Hlavní proměnné (podnik)
├─ Komponenty proměnných (podnik)
⏐    ├─ Primární proměnné (komunita)
⏐    └─ Komponenty proměnných (komunita)
    ⏐
↓ web._assets_bootstrap
    ⏐
↓ web.assets_backend
    ⏐   ├─ ...
⏐    └─ Definice proměnných CSS
⏐    └─ Kontextové přizpůsobení proměnných CSS
    ⏐
●[Výsledek na obrazovce]

.. důležité:
Tento diagram je neúplný a nesouvisí s aktuální organizací balíků. Více informací najdete v
:ref:`soubory aktiv <reference/assets_bundle>“.
