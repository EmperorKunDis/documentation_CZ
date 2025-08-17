
=================
Upravte pole
=================

Podklasifikovat existující pole
====================================

Pojďme si ukázat příklad, kdy chceme rozšířit třídu BooleanField, abychom vytvořili nový booleovský prvek.
Zobrazí „Pozdě!“ v červeném písmu, pokud je zaškrtávací políčko vyplněno.

#Vytvořte nový komponent widgetu, který bude dědit požadovaný komponent.

... kódový blok::javascript
:předmět: :soubor: `late_order_boolean_field.js`

import { registry } z "@web/core/registry";
import { Pole s logickým typem } z "@web/views/pole/logické pole";
import { Komponenta, xml } z "@odoo/owl";

třída LateOrderBooleanField je podtřídou třídy BooleanField
statický šablonový parametr = "my_module.LateOrderBooleanField";
      }

#Vytvořte šablonu pole.

Komponenta používá nový šablonový soubor s názvem my_module.LateOrderBooleanField. Vytvořte jej tak, že
dědí aktuální šablonu pole typu Boolean.

... kódový blok :: XML
:podpis: :soubor:`pozdní_objednávka_logická_pole.xml


<šablony xml:space="preserve">
<t t-name="my_module.LateOrderBooleanField" t-inherit="web.BooleanField">
<checkbox expr="//checkbox" position="after">
<span t-if="props.value" class="text-danger">Pozdě!</span>
</xpath>



#Zaregistrujte součást do pole registru polí.

... blok kódu::
:předmět: :soubor: `late_order_boolean_field.js`

registry.kategorie("pole").přidat("pozdní_logická", LateOrderBooleanField);

#Přidejte widget do zobrazení archivu jako atribut pole.

... kódový blok :: XML

<položka jméno="nějaké pole" widget="pozdní booleovská hodnota"/>

Vytvořte nový komponent pole
============================

Předpokládejme, že chceme vytvořit pole, které zobrazí jednoduchý text červeně.

#Vytvořte nový komponent Owl, který bude reprezentovat náš nový prvek.

... kódový blok::js
:předpis: :soubor: `my_text_field.js

import { standardní pole vlastností } z "@web/výhledy/pole/standardní pole vlastností";
import { Komponenta, xml } z "@odoo/owl";
import { registry } z "@web/core/registry";

export třída MyTextField prodlouží třídu Komponenta následovně:
statický šablona = xml
<input t-att-id="props.id" třída="text-danger" t-att-value="props.value" vlastnost="onchange" onChange.bind="onChange" />
         `;
statické props = {...standardní pole vlastností};
statické podporované typy jsou "char".

         /**
         * @param {boolean} nováHodnota
         */
onChange(newValue) {
tento.props.aktualizovat(nový hodnota);
         }
      }

Do importovaného pole „standardní položky“ jsou zahrnuty standardní vlastnosti, které předává „Zobrazení“, například
funkci „aktualizace“ pro aktualizaci hodnoty, typ pole v modelu,
„const“ boolovou hodnotu a další.

#Ve stejném souboru registrujte komponentu do pole registrů.

... kódový blok::js
:předpis: :soubor: `my_text_field.js

registry.category("fields").add("my_text_field", MyTextField);

Toto mapuje název widgetu v archivu na jeho skutečnou součást.

#Přidejte widget do zobrazení archivu jako atribut pole.

... kódový blok :: XML

<položka jméno="nějaké pole" widget="můj textový prvek"/>
