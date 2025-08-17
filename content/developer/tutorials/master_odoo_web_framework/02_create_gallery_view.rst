================================
Kapitola 2: Vytvořte galerijní pohled
================================

Podívejme se, jak vytvořit nový pohled úplně od začátku. Ve skutečnosti není
je těžké provést, ale neexistují žádné skutečně užitečné zdroje na to, jak to udělat. Poznámka: většina situací
Mělo by být vyřešeno buď upravením stávajícího pohledu nebo s pomocí klientské akce.

Pro tento úkol předpokládejme, že chceme vytvořit pohled „galerie“, což je pohled, který umožňuje
Jsme soubor záznamů, které obsahují obrazové pole.

Za tímto problémem stojí určitě kanbanový pohled, ale to znamená, že není možné
mít naše normální kanbanové zobrazení a galerii v jednom kroku.

Vytvořme galerii. Každá galerie bude definována atributem image_field v jejím
arch:

... blok kódu::xml

<gallery field="some_field"/>

Pro dokončení úkolů v této kapitole budete potřebovat nainstalovat rozšíření awesome_gallery.
Doplněk obsahuje potřebné soubory serveru, které umožňují přidat nový pohled.

.. varování: Cíl

.... obrázek: 02_vytvorit_galerie_prihled_prehled.png
:synchronizace: střed

..spoiler:: Řešení

Řešení každé úlohy kapitoly jsou uveřejněna na
„oficiální repozitář návodů k použití Odoo
<https://github.com/odoo/tutorials/commits/{CURRENT_MAJOR_BRANCH}-master-odoo-web-framework-solutions/awesome_gallery>.

1. Vytvořte pozdrav světu
==========================

Prvním krokem je vytvoření implementace JavaScriptu s jednoduchým komponentem.

#Vytvořte soubory „gallery_view.js“, „gallery_controller.js“ a „gallery_controller.xml“.
„static/src“.
#Implementujte jednoduchou složku „Hello World“ do souboru `gallery_controller.js`.
#Ve skriptu gallery_view.js dovolejte kontrolér, vytvořte objekt zobrazení a registrujte jej v
zobrazit záznamy pod názvem „galerie“.

...... příklad::
Níže je příklad definice objektu View:

... kódový blok::js

import { registry } z "@web/jádro/registry";
import { MůjKontroler } z "./můj_kontroler";

export const myView = {
typ: "můj pohled",
display_name: „Můj pohled“,
ikona: „oi oi-view-list“,
multirekord: true,
Controller: MůjController
         };

registry.category("views").add("my_controller", myView);

#Přidejte „galerie“ jako jeden z typů pohledu v akci „Kontakty“.
#Ujistěte se, že můžete vidět svou složenku „Hello World“ při přepínání na galerii.

.. obrázek: 02_create_gallery_view/view_button.png
:align:center

.. obrázek: 02_vytvorit_galerie_zobrazeni/nove_zobrazeni.png
:align:center

2. Použijte komponentu Layout
===========================

Dosud naše galerie vypadá jinak než obvyklý pohled. Použijme tedy komponentu Layout.
Mají stejné funkce jako ostatní pohledy.

#Importujte komponentu Layout a přidejte ji do složky components v GalleryController.
#Aktualizujte šablonu tak, aby používala Layout. Potřebuje vlastnost display, kterou naleznete
`props.display`.

.. obrázek: 02_vytvorit_galerie_zobrazeni/layout.png
:align:center

3. Rozložte archeologické nálezy.
=================

Prozatím naše galerie není moc užitečná. Začněme tedy čtením informací obsažených v
oblouk pohledu.

Proces rozpoznávání arků se obvykle provádí pomocí třídy ArchParser, která je specifická pro každý pohled.
dědí z obecné třídy XML parseru.

Příklad:

Zde je příklad, jak by mohl vypadat parser architektury:

... kódový blok::js

exportní třída MyCustomArchParser
parse(xmlDoc) {
const myAttribute = xmlDoc.getAttribute("my_attribute")
return {
mojeAtribut
             }
          }
      }

#Vytvořte třídu ArchParser v samostatném souboru.
#Použijte ji k přečtení informací o poli obrázku.
#Aktualizujte kód zobrazení galerie, aby se přidaly do vlastností obdržených od kontroleru.

.. poznámka::
Je možná trochu přehnané takhle to řešit, protože vlastně potřebujeme jen číst jednu
atribut z oblouku, ale je to návrh, který se používá v každém jiném pohledu na odoo, protože
nám umožňuje vyjmout nějaké předběžné zpracování z kontroleru.

.. viz též:
„Příklad: grafický parsovač archů


4. Nahrát nějaká data
=================

Nyní získáme nějaká reálná data ze serveru. Pro tento účel musíme použít metodu webSearchRead() z ORM
služby.

Příklad:

Tady je příklad funkce webSearchRead, která získává záznamy ze schématu:

... kódový blok::js

const { délka, záznamy } = this.orm.webSearchRead(tento.model, doména, {
specifikace:
[tohoto pole]: {}.
:{},
          },
kontext: {
bin_size: true,
          }
      })

#Přidejte metodu loadImages(doména) do GalleryControlleru. Ta by měla provádět
„webSearchRead“ volání služby orm pro získání záznamů odpovídajících doméně.
použít obrázek získaný v propsu.
#Pokud jste bin_size nezahrnuli do kontextu volání, obdržíte pole obrazu.
je kódováno pomocí Base64. Ujistěte se, že zadáváte bin_size v kontextu, abyste dostali velikost obrázku
pole. Obrázek zveřejníme později.
#Upravte metodu setup tak, aby volala tuto metodu v onWillStart a onWillUpdateProps.
háčky.
#Upravte šablonu, aby zobrazovala ID a velikost každého obrázku uvnitř výchozího slotu
komponenta Layout.

.. poznámka::
Následující cvičení se bude zabývat přesunem načítacího kódu do vhodného modelu.

.. obrázek: 02_vytvorit_galerie_zobrazeni/galerie_dat.png
:align:center

5. Zjednodušte řešení problémů s konkurencí
================================

Naše kódy zatím nejsou vůči souběžnosti odolné. Pokud se změní doména dvakrát, vyvolá to
„načíst obrázky (doména)“ dvakrát. Máme tak dva požadavky, které mohou dorazit v různý čas.
na různé faktory. Odpověď na první požadavek přichází až poté, co dostanete odpověď
Druhá žádost povede k nesourodému stavu.

Primitiv „KeepLast“ z Odoo tento problém vyřeší. Spravuje seznam úkolů a pouze
Udržuje poslední úkol aktivní.

#Importujte funkci KeepLast z souboru: @web/core/utils/concurrency.
#Vytvořte objekt KeepLast v modelu.
#Přidejte volání webSearchRead do KeepLast, aby se vyřešil pouze poslední výsledek.

.. viz též:
`Příklad: použití KeepLast <https://github.com/odoo/odoo/blob/ebf646b44f747567ff8788c884f7f18dffd453e0/addons/web/static/src/core/model_field_selector/model_field_selector_popover.js#L164>`

6. Restrukturalizovat kód
==================

Skutečné pohledy jsou trochu více organizované. To může být přehnané v tomto případě, ale je to zamýšleno
se naučit strukturovat kód v Odoo. Dále bude lépe škálovat s měnícími se požadavky.

#Přesuňte všechny kód modelu do vlastní třídy GalleryModel.
#Přesuňte všechny kódy renderování do komponenty GalleryRenderer.
#Importujte třídu GalleryModel a GalleryRenderer do GalleryController, aby to fungovalo.

7. Dokončete výhled
===========================

Pokud chcete rozšířit pohled, můžete do galerie přidat objekt s vlastním pohledem a upravit ho podle svého.
Problém je v tom, že zatím není možné definovat vlastní model nebo renderer, protože
je vložen přímo do ovladače.

#Importujte soubor s názvem „GalleryView“ a v něm importujte třídy „GalleryModel“ a „GalleryRenderer“.
#Přidejte klíč „model“ a „renderer“ do objektu galerie a přiřaďte je k „GalleryModel“.
a „Galerie renderer“. Přidejte do kontroleru vlastnosti „Model“ a „Renderer“.
#Odeberte pevně vložený import do kontroleru a získávejte je ze vlastností.
#. Použijte součástku t
<https://github.com/odoo/owl/blob/master/doc/reference/component.md#dynamic-sub-components>
mohou mít dynamické podkomponenty.

.. poznámka::

Takto by se mohl nyní někdo rozšířit pohled do galerie změnou rendereru:

... kódový blok::js

import { registry } z "@web/core/registry";
import { galerieView } z "@awesome_gallery/galerie_view";
import { GalerieRenderovací služba } z "@awesome_gallery/gallery_renderovací služba";

export třída MyExtendedGalleryRenderer prodlouží třídu GalleryRenderer následovně:
statický šablonový vzorec = "my_module.MyExtendedGalleryRenderer";
setup() {
super.setup();
console.log("můj galerie renderer rozšíření");
         }
      }

registry.kategorie("views").přidat("my_gallery", {
...galerie,
Renderér: MyExtendedGalleryRenderer
      });

8. Zobrazit obrázky
=================

Aktualizovat renderer tak, aby zobrazoval obrázky pěkně, pokud je pole nastaveno. Pokud je pole
prázdný, místo něj zobrazit prázdnou krabici.

..tip:

Je zde ovladač, který umožňuje získat obrázek ze záznamu. Můžete tento ovladač použít
část odkazu, který bude použit k vytvoření odkazu:

... kódový blok::js

import { url } z "@web/jádro/utils/url";
const url = url("/web/image", {
model: resModel
id: obrázek_id
pole: obrázek
         });

.. obrázek: 02_vytvorit_galerie_pohled/trikot_obrazek.png
:align:center

9. Přepněte se do formulářového zobrazení po kliknutí
===============================

Aktualizujte renderer, aby reagoval na kliknutí na obrázek a přepnul se do zobrazení formuláře. Můžete použít
Funkce „přepnout na pohled“ z akční služby.

.. viz též:
„Kód: Funkce přepínání pohledu <https://github.com/odoo/odoo/blob/db2092d8d389fdd285f54e9b34a5a99cc9523d27/addons/web/static/src/webclient/actions/action_service.js#L1064>“

10. Přidejte volitelný nástroj tipu
===========================

Je užitečné mít nějaké další informace při najetí myší.

#Aktualizujte kód tak, aby umožnil volitelné další atributy na archeologických nálezech.

... kódový blok :: XML

<gallery image_field="nějaké_pole" tooltip_field="jinaké_pole"/>

#Při najetí myší zobrazit obsah položky nástroje. To by mělo fungovat, pokud je pole
pole typu char, pole číslo nebo pole mnoho k jednomu.
vložte řetězec do atributu data-tooltip prvku.
#Aktualizujte galerii zákazníků, aby se v ní zobrazovala položka s názvem „Zákazník“ jako nápověda.

.. obrázek: 02_vytvorit_galerie_zobrazeni/obrazovek_nastaveni.png
:align:center
:scale: 50 %

.. viz též:
„Příklad: použití t-att-data-tooltip <https://github.com/odoo/odoo/blob/145fe958c212ddef9fab56a232c8b2d3db635c8e/addons/survey/static/src/views/widgets/survey_question_trigger/survey_question_trigger.xml#L8>“

11. Přidat stránkování
==================

Přidejme do ovládacího panelu stránkování a spravujme všechna stránková čísla jako v normálním pohledu na Odoo.

.. obrázek: 02_vytvorit_galerie_zobrazeni/paginace.png
:align:center

.. viz též:
   - „Kód: Použití funkce pager hooku <{GITHUB_PATH}/addons/web/static/src/search/pager_hook.js>“
   - Příklad: použijte pager v kontroloři listu <https://github.com/odoo/odoo/blob/48ef812a635f70571b395f82ffdb2969ce99da9e/addons/web/static/src/views/list/list_controller.js#L109-L128>

12.  Souhlas s názory
=====================

Dosud máme hezký a užitečný pohled. Ale ve skutečnosti bychom mohli mít problémy s uživateli, kteří nám budou posílat chybné informace.
kódování „archu“ jejich galerie: v současné době je to pouze neuspořádaný kousek XML.

Přidáme nějakou validaci. V Odoo lze popsat XML dokumenty pomocí souboru RN
„(soubor Relax NG)“, a poté byl ověřen.

#Přidejte soubor RNG, který popisuje aktuální gramatiku:

   - Povinný atribut „image_field“.
   - Volitelný atribut: `tooltip_field`.

#Přidejte nějaký kód, který by zajistil, že všechny pohledy budou ověřeny proti tomuto souboru náhodného generátoru čísel.
#Zatímco jsme u toho, můžeme se ujistit, že pole „obrázek“ a „nástrojová lišta“ jsou pole
současný model.

Ověření souboru s náhodným číslem není snadné, protože zde je ukázka k pomoci:

... kódový blok:: python

   # *-*- kódování: UTF-8 *-*-
import logging
import os

importujeme modul lxml

od odoo.loglevels import ustr
od odoo.tools import misc, view_validation

_logger = logging.getLogger(__name__)

_validátor_názvu_výhledu = None

@view_validation.validace('vizitka')
def schéma_výběr (arch, **klauzule):
"Zkontrolujte galerijní pohled na jeho schéma.

:typ: arch: etree._Element
         """
globální validátor názvu vzhledu

pokud je _viewname_validator None:
s open(os.path.join('modulename', 'rng', 'viewname.rng'), "rb") as f:
_viewname_validator = etree.RelaxNG(etree.parse(f))

pokud je arch validován v rámci metody viewname_validator.validate():
vrátí True

za chybu v validátoru názvu pohledu:
_logger.error(ustr(chyba))
vrací hodnotu False

.. viz též:
`Příklad: RNG soubor grafického zobrazení <https://github.com/odoo/odoo/blob/70942e4cfb7a8993904b4d142e3b1749a40db806/odoo/addons/base/rng/graph_view.rng>`_.

13. Nahrání obrázku
======================

Naše galerie neumožňuje uživatelům nahrávat obrázky. Přidejme tuto funkci.

#Přidejte tlačítko na každé obrázce pomocí komponenty FileUploader.
#Komponenta FileUploader přijímá vlastnost onUploaded, která se volá při uživatelském
nahraje obrázek. Ujistěte se, že voláte metodu webSave z služby ORM, aby byl nahrán nový obrázek.
#Možná jste si všimli, že obrázek se nahraje, ale nebude znovu vykreslen prohlížečem.
To je proto, že obrázek odkaz nezměnil a prohlížeč si jej tedy znovu stáhnout nemusel.
do obrázku URL zaznamenává datum psaní.
#Ujistěte se, že kliknutím na tlačítko pro nahrání nevyvoláte přepnutí na jiný pohled.

.. obrázek: 02_vytvorit_galerie_zobrazeni/nahrat_obraz.png
:align:center
:scale: 50 %

.. viz též:

   - „Příklad: použití FileUploader <https://github.com/odoo/odoo/blob/7710c3331ebd22f8396870bd0731f8c1152d9c41/addons/mail/static/src/web/activity/activity.xml#L48-L52>“
   - `Odoo: webSave definition <https://github.com/odoo/odoo/blob/ebd538a1942c532bcf1c9deeab3c25efe23b6893/addons/web/static/src/core/orm_service.js#L312>`_

14. Vylepšený šablonový nástroj tipů
=============================

Prozatím můžeme specifikovat pouze pole pro nápovědu. Co ale když chceme umožnit psát konkrétní
šablona pro něj?

Příklad:

Toto je příklad galerie s archeologickým pohledem, který by měl fungovat po této cvičení.

... kódový blok :: XML

<zaznamenání id="kontakty_galerie_výhled" model="ir.ui.view">
<políčko name="název">awesome_gallery.orders.gallery</políčko>
<field name="model">res.partner</field>
<položka jméno="arch" typ="xml">
<gallery image_field="image_1920" tooltip_field="name">
<field name="email"/> <!-- Udělte modelu najevo, že se má e-mail získat -->
<field name="jméno" />  <!--Specifikujte modelu, že se má získat jméno-->
<vlastní šablona pro nástrojovou lištu>

<p class="m-0">E-mail: <field name="email"/></p>
</nástrojovém šabloně>
</galerie>
</field>
</záznam>

#Změňte galerii obrazů ve vzhledu „partner“ v souboru:
arch v příkladu výše. Nemusíte se bát, pokud neprojde kontrolou RNG.
#Změnit galerii rng validátor, aby přijal novou strukturu archivu.

......tip:

Můžete použít tento kousek skriptu pro ověření šablony nástrojového tipu

... kódový blok::xml

<rng:define name="návod-vložení-šablona">
<rng:element name="nástrojová šablona">
<rng:zeroOrMore>


</rng:nulaIle>
</rng:element>
</rng:definice>

<rng:define name="kdokoliv">
<rng:element>
<rng:jmenoNikoho/>
<rng:zeroOrMore>
<rng:volba>

<rng:jmenoNikoho/>
</rng:attribut>


</rng:volba>
</rng:nulaIle>
</rng:element>
</rng:definice>
#Architektura parsování by měla rozpoznat pole a šablonu nástrojového panelu. Do importu přidejte
:soubor: web/core/utils/xml a použijte jej k parsování názvu pole a šablony pro nápovědu.
#Ujistěte se, že model volá metodu webSearchRead a zahrne do ní pole vybrané pomocí metody parseFieldNames.
specifikace.
#Výkonnostní vrstva (nebo jakákoliv podvrstva, kterou jste pro ni vytvořili) by měla přijímat vykreslené nástrojové tipy.
šablona. Tuto šablonu upravte tak, aby se v ní nahradilo tagu <field> tagem <t t-esc="x">
prvek.

......tip:

Šablona je objektem typu Element, takže lze s ní pracovat jako se značkou HTML.

#. Registrujte šablonu do Owlu pomocí funkce xml z modulu @odoo/owl.
#Použijte funkci „připojit nástrojovou lištu“ z souboru @web/core/tooltip/tooltip_hook.
nástrojové lišty. Tato funkce přijímá jako argument šablonu Owl a proměnnou, kterou potřebuje
šablona.

.. obrázek: 02_vytvorit_galerie_zobrazeni/pokrocile_nastaveni.png
:align:center
:scale: 50 %

.. viz též:

   - Příklad: použití nástroje tooltip v Kaban <https://github.com/odoo/odoo/blob/0e6481f359e2e4dd4f5b5147a1754bb3cca57311/addons/web/static/src/views/kanban/kanban_record.js#L189-L192>
   - Příklad: použití visitXML <https://github.com/odoo/odoo/blob/48ef812a635f70571b395f82ffdb2969ce99da9e/addons/web/static/src/views/list/list_arch_parser.js#L19>
   - „Sova: Vložené šablony s funkcí pomocí XML <https://github.com/odoo/owl/blob/master/doc/reference/templates.md#inline-templates>“
