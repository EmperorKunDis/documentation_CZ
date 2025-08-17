=====================
Upravte typ zobrazení
=====================

Podklasifikovat existující pohled
=========================

Předpokládejme, že potřebujeme vytvořit vlastní verzi obecného pohledu. Například kanbanový pohled s nějakými
Další pás s widgety na horní liště (pro zobrazení konkrétních informací). V tom případě je
Je možné provést v několika krocích:

#Přidejte do kanbanového řídícího prvku/zobrazení/modelu a zaregistrujte jej v registru pohledu.

... kódový blok::js
:předmět: :soubor:`custom_kanban_controller.js

import {KanbanController} z "@web/views/kanban/kanban_controller";
import { kanbanView } z "@web/views/kanban/kanban_view";
import { registry } z "@web/core/registry";

      // the controller usually contains the Layout and the renderer.
class CustomKanbanController : KanbanController
statický šablonový vzorec = "my_module.CustomKanbanView";

          // Your logic here, override or insert new methods...
          // if you override setup(), don't forget to call super.setup()
      }

exportní konstanta customKanbanView je
...kanbanView, // obsahuje výchozí renderer/controller/model
Controller: CustomKanbanController
      };

      // Register it to the views registry
registry.kategorie("views").přidat("custom_kanban", customKanbanView);

V našem vlastním kanbanu jsme definovali nový šablonový model. Můžeme buď dědit stávající kanban controller
šablonu a přidat naše šablonové díly nebo můžeme definovat úplně novou šablonu.

... kódový blok :: XML
:popisek: :soubor:`custom_kanban_controller.xml`


<šablony>
<t t-name="my_module.CustomKanbanView" t-inherit="web.KanbanView">
<xpath expr="//Layout" position="před">

Ahoj světe!

</xpath>



#Použijte pohled s atributem `js_class` v archu.

... kódový blok :: XML

<kanban class="custom_kanban">
<šablony>
<t t-name="kanban-box">
<!--Váš komentář-->
</t>

</kanban>

Možností pro rozšíření pohledu je nepřeberné množství. My jsme pouze rozšířili ovládací panel
tady si můžete také přidat nové tlačítko, upravit způsob zobrazení záznamů nebo
upravit nabídku, stejně jako rozšířit další komponenty, například model a šablonu tlačítka.

Vytvořte nový pohled od nuly
==============================

Vytváření nového pohledu je pokročilé téma, které tento průvodce pouze zásadně nastiňuje.

#Vytvořte ovládací prvek.

Hlavní úlohou kontroléra je usnadnit koordinaci mezi různými komponentami.
jako renderer, model nebo layout.

... kódový blok::js
:caption: :file:`krasny_controller.js

import { Layout } z "@web/hledání/layout";
import { useService } z "@web/core/utils/hooks";
import {Component, onWillStart, useState} z "@odoo/owl";

export třída BeautifulController prodlouží třídu Component následujícím způsobem:
statický šablonový soubor = „my_module.View“;
statické komponenty = { Layout };

setup() {
tento.orm = použít službu ("orm");

              // The controller create the model and make it reactive so whenever this.model is
              // accessed and edited then it'll cause a rerendering
tento.model = useState(
nové tento.props.Model(
tento.orm
tento.vlastnosti.modelRes
tento.vlastnosti.pole
tento.vlastnosti.archInfo
this.props.doména
                  )
              );

onWillStart(() => {
očekávejte, až se model načte.
              });
          }
      }

Šablona Controller zobrazuje ovládací panel s Layoutem a také
renderer.

... kódový blok :: XML
:předpis: :soubor:`krasny_controller.xml`


<šablony xml:space="preserve">
<t t-name="my_module.View">
<Layout zobrazení="props.display" třída="'h-100 overflow-auto'"

</Layout>



#Vytvořte renderer.

Hlavním úkolem rendereru je vytvořit vizuální reprezentaci dat pomocí renderování.
pohled, který zahrnuje záznamy.

... kódový blok::js
:caption: :file:`krasny_renderer.js

import { Komponenta } z "@odoo/owl";
export třída BeautifulRenderer prodlouží třídu Component následujícím způsobem:
statický vzorový šablonový řetězec = „my_module.Renderer“;
      }

... kódový blok :: XML
:předpis: :soubor:`krasne_renderer.xml`


<šablony xml:space="preserve">
<t t-name="renderer.MyModuleRenderer">
<t t-esc="props.propsYouWant"/>
<t t-foreach="props.records" t-as="record" t-key="record.id">
                  // Show records
</t>



#Vytvořte si vlastní model.

Role modelu je získávat a spravovat veškerá potřebná data v pohledu.

... kódový blok::js
:caption: :file:`krasna_modelka.js

import {KeepLast} z "@web/core/utils/concurrency";

export třída KrasnáModelka {
constructor(orm, resModel, pole, archInfo, doména) {
tento.orm = orm;
tento.resModel = resModel;
              // We can access arch information parsed by the beautiful arch parser
const { poleZArcheologickéInformace } = archInfo;
tento.poleZArchivu = poleZArchivu;
tento.pole = pole;
tento.doména = doména;
tento.keepLast = nový KeepLast();
          }

async load() {
              // The keeplast protect against concurrency call
const { délka, záznamy } = čekat na tento.doplnit poslední
tento.orm.webSearchRead(toto.resModel, tento.doména, [toto.pole z archivu], {})
              );
tento.záznamy = záznamy;
tento.délkaZáznamů = délka;
          }
      }

....... poznámka::

Pro pokročilé případy je možné místo vytváření modelu od nuly použít existující.
„Relacionální model“, který používají další pohledy.

#Vytvořte archivní parsovací nástroj.

Role archového parsování je převést pohled na arch do formátu, který umožňuje přístup k informacím.

... kódový blok::js
:předpis: :soubor:`krasna-arka-parsovatel.js

import { XMLParser } z "@web/jádro/utils/xml";

exportní třída BeautifulArchParser prodloužuje třídu XMLParser následujícím způsobem:
parse(arch) {
const xmlDokument = tento.parseXML(souboru).
const poleOdArchivu = xmlDokument.getAttribute("poleOdArchivu");
return {
pole z archivu
              };
          }
      }

#Vytvořte pohled a spojte všechny dílky dohromady, pak registrujte pohled v pohledech
registr.

... kódový blok::js
:popisek: :soubor: `krásný výhled.js

import { registry } z "@web/core/registry";
import {Krásný Controller} z „./krasny_controller“;
import { ParserKrásnéArchitektury } z „./beautiful_arch_parser“;
import { ModelBeautiful } z "./krasna_modelka";
import { KrasavecRenderovacíEngine } z „./krasavec_renderovací_engine“;

exportní konstantou je nádherný výhled,
typ: „krásná“,
display_name: „Krásná“,
ikona: „fa fa-picture-o“, // ikona, která se zobrazí v panelu Layout
multiRecord: true,
Controller: KrasnyController
ArchParser:KrásnýArchParser
Model: BeautifulModel
renderer: Krasavec

props(generické vlastnosti, pohled) {
const { ArchParser } = view;
const { arch } = props;
const archInfo = nový ArchParser().parse(arch);

return {
...obecné vlastnosti
Model: view.Model
Renderer: view.Renderer
archinfo
              };
          },
      };

registry.kategorie("views").přidat("krásný výhled", krásný výhled);

#Zde vyhlásit pohled na záznamy v architektuře.

... kódový blok :: XML

      ...
<záznam id="můj krásný výhled" typu="ir.ui.view">
<field name="název">my_view</field>
<položka jméno="model">my_model</položka>
<položka jméno="arch" typ="xml">
<krásné pole z archu res.partner/>
</p>
</záznam>
      ...
