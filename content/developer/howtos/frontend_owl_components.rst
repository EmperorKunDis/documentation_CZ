============================================
Použijte komponenty Owl na portálu a webových stránkách
============================================

V tomto článku se dozvíte, jak můžete využít komponenty Owl na portálu.
a webové stránky.

Přehled
========

Chcete-li používat komponenty Owl na webu nebo portálu, budete muset udělat několik věcí:

- Vytvořte svůj komponent Owl a zaregistrujte jej v registru public_components
- Přidejte tento komponent do balíčku webových aktivit v předním portálu
- Přidejte značku <owl-component> na webovou stránku nebo portál, abyste mohli použít komponentu

1. Vytváření komponenty Sova
=============================

Abychom si věci usnadnili, začněme s velmi jednoduchým komponentem, který jen zobrazuje
„Ahoj světe.“ To nám řekne na první pohled, jestli máme správně nakonfigurované prostředí.

Nejprve vytvořte šablonu ve složce :file:`/your_module/static/src/portal_component/your_component.xml`.

... blok kódu::xml


<šablony xml:space="preserve">
<t t-name="Váš modul.Váš komponent">
Ahoj světe!
</t>
</šablony>

Poté vytvořte soubor JavaScriptu pro tento komponent v adresáři: / vašeho modulu / statické / zdroje / portálový komponent / váš komponent.js
a přidejte ji do registru veřejných komponent:

... kódový blok::js

import { Komponenta } z "@odoo/owl";
import { registry } z "@web/jádro/registry"

export třída YourComponent prodlouží třídu Component následujícím způsobem:
statická šablona = "Váš modul.Vaše komponenta";
statické props = {};
    }

registry.category("public_components").add("your_module.YourComponent", YourComponent);


.. viz též:
:ref:`Soubor s odkazy na komponenty <frontend/components>.


2. Přidání vašeho komponentu do balíčku webových aktivit v přední části
============================================================

Balíček webových aktivit front-endu je balíček aktiv, který používá portál a
webové stránky, budete chtít přidat kód komponenty do této knihovny, aby byla veřejností
Služba komponent může najít vaši součást a namontovat ji. V manifestu modulu
V sekci aktiv přidejte položku web.assets_frontend a do ní vložte komponentu
soubory:

.. kódový blok:: py

    {
        # ...
"aktiva": {
'web.assets_frontend': [
'your_module/static/src/portal_component/**/*'
            ],
        }
    }

.. viz též:
:ref:`Manifest modulu <reference/module/manifest>.

3. Přidání značky <owl-component> na stránku
============================================

Nyní potřebujeme vložit značku <owl-component>, která bude sloužit jako cílová značka pro komponentu
Je třeba ji namontovat. Pro ilustraci přidáme přímo do portálu
domovská stránka s XPath v souboru: / vašeho modulu / views / templates.xml.

... blok kódu::xml


<odoo>

<xpath expr="//*[hasclass('o_portal_my_home')]" position="before">

</xpath>



Nezapomeňte přidat tento soubor do sekce dat v balíčku vašich aktiv.

.. kódový blok:: py

    {
        # ...
'data': [
'views/šablony.xml',
        ]
    }

A je hotovo. Pokud se na hlavní stránce portálu objeví zpráva
„Ahoj světe!“ na vrcholu stránky.

Pozor na
=================

Komponenty sovy jsou zcela vykreslené v JavaScriptu prohlížečem. To může způsobit
některé problémy:

- Posun obsahu
- Horší indexace vyhledávačů

Proto byste měli používat komponenty Owl pouze na portálu a webových stránkách
Specifické příklady použití uvedené níže.

Posun obsahu
------------

Když se stránka na počátku zobrazí s obsahem a ten poté posune („posunuje“).
V rámci stránky se tento jev označuje jako layout shift. Při používání komponent Owl
portál nebo webová stránka zobrazí všechny HTML soubory, které obklopují komponentu Owl.
serveru a je první věcí, která se zobrazí uživateli. Když
začne běžet, sova vám nainstaluje součástku, což pravděpodobně způsobí okolní
elementy, které se pohybují na stránce. To může způsobit špatnou uživatelskou zkušenost: uživatel vidí
prvek na stránce, který se zobrazil jako první a s nímž chtějí interagovat.
Takže pohybují kurzorem nebo prstem nad tímto prvkem. Když se chystají kliknout,
součást sovy je namontována a pohybová jednotka se přesune na místo, které chce ovládat.
Klikají na aplikaci Owl namísto toho.

To může být frustrující zkušenost, takže byste se měli při navrhování svého
stránce, na které se komponent Owl nepohne s prvky. To lze dosáhnout
různými způsoby, například tím, že je umístíte pod všechny ostatní existující prvky a ne
jiných interaktivních prvků v okolí nebo vyhrazené pevné místo pro komponentu Owl.
pomocí CSS.


.. viz též:
„Kumulativní posun vzhledu na web.dev <https://web.dev/articles/cls>“


Horší indexace vyhledávačů
---------------------------------

Při budování indexu obsahu webu využívají vyhledávače tzv. webové sklízecí roboty
vyhledávat stránky a analyzovat jejich obsah, aby tyto stránky zobrazily.
výsledky vyhledávání. Moderní vyhledávače jsou obecně schopny spouštět JavaScript
kód a měly by být obecně schopny zobrazit a indexovat obsah vygenerovaný v JavaScriptu.
Mohou se zpožděním indexovat obsah a trestat stránku v hledaných výsledcích.

Protože většina vyhledávačů nezveřejňuje přesný způsob, jakým prochází a indexují
webových stránek není vždy snadné určit rozsah dopadu klientského renderování
může mít na vaše hodnocení vyhledávačů vliv. Ačkoli je nepravděpodobné, že by vám pomohlo nebo poškodilo váš SEO
strategii, měli byste používat komponenty Owl jen tehdy, když přidávají skutečnou hodnotu.
serverové straně.

Kdy použít komponenty Owl na portálu a webové stránce
====================================================

Jak bylo v předchozích kapitolách uvedeno, používání komponenty Owl může mírně snižovat výkon.
zkušenosti, pokud nejste opatrní, a mohou také ztížit vaše SEO. Takže když byste měli
používat komponenty Owl v těchto místech? Zde jsou nějaké obecné pokyny.

Když se o SEO nezajímáte
-----------------------------

Pokud stránka nemůže být indexována vyhledávači kvůli tomu, že není veřejně dostupná
např. cokoli v uživatelském portálu, výkonnost SEO není problémem, protože vyhledávače
na tyto stránky stejně nemůžete přistupovat. Existují také věci, které nechcete nebo
se zajímat o indexování například pokud chcete mít stránku, na které si uživatel může vybrat datum
a čas pro schůzku, pravděpodobně nechcete, aby vyhledávače indexovaly data
na které je možné si domluvit termín v určitém čase.

Když potřebujete silnou interakci
----------------------------------

Rozhodnutí používat Owla je kompromisem mezi výše zmíněnými nevýhodami
a úsilí, které vám Owl ušetří tím, že je snadné vytvářet interaktivní uživatelské rozhraní.
zkušeností. Hlavním důvodem pro použití Owla je, pokud chcete vytvořit rozhraní, které
může reagovat v reálném čase na vstupy uživatele bez nutnosti obnovit stránku. Pokud
pokud chcete uživateli hlavně ukázat statickou stránku, neměli byste používat Owla.
komponenta.
