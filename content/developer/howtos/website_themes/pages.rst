=====
Stránky
=====

V této kapitole se dozvíte, jak deklarovat statické stránky.

... /webové-šablony/stránky/výchozí/:

Stránky výchozí
=============

V Odoo jsou webové stránky dodávány s několika výchozími statickými stránkami (Domovská stránka, Kontaktujte nás, 404, ...). Tyto stránky jsou vytvářeny
takto.

... blok kódu::xml
:caption: `/web/data/web_data.xml`

<šablona id="webová stránka.domovská stránka" jméno="Domů">
<t t-call="web.layout">
<t t-set="pageName" t-value="'domovská stránka'"/></t>
<div id="wrap" třída="oe_struktura oe_prázdná" />
</t>


Každá výchozí stránka je šablona s vlastním obsahem uloženým do záznamu. Proto
:ref:`Stránky vytvořené na míru se nacházejí uvnitř záznamu <webové šablony/stránky/téma stránek>“.

Znaky v uvozovkách „<t-call='website.layout'>“ mají několik proměnných, které lze nastavit:

Definujte metatitulek.

... blok kódu::xml

<t t-set="přidat titulek">Můj název stránky</t>

..tip:
Tady se hodnota neukládá do atributu t-value nebo t-valuef.
Toto je pro účely překladu. Obsah hodnoty t-value nebo t-valuef není explicitně uveden.
exportován pro překlad. Kromě toho je napsaný v XML, což znamená, že mezi otevírací značkou
a ukončovací značka je považována za přeložitelnou v podstatě automaticky.

...... příklad::
**Dobrý příklad:**

... kódový blok::xml

<t t-set="přidatitulek">Můj titulek</t>

**Špatný příklad:**

... kódový blok::xml

<t t-set="přidatititul" t-valuef="Můj titulek"/>

Definujte meta popisky.

... blok kódu::xml

Toto je popis stránky, který se zobrazí ve vyhledávačích.
Motory.</t>

Přidejte do stránky třídu CSS.

... blok kódu::xml

<t t-set="pageName" t-valuef="..."/>

Skryj hlavičku.

... blok kódu::xml



Skryjte zápatí.

... blok kódu::xml



Pokud je potřeba, vypněte výchozí stránky.

... blok kódu::xml
:caption: „/webové stránky/vzduchotěsné/data/stránky/domov.xml“

<záznam id="webová stránka.domovská stránka" typu="ir.ui.view">
<field name="active" eval="false"/>
</záznam>

... blok kódu::xml
:caption:"/web/airproof/data/stranky/kontakt.xml"

<záznam id="kontaktujte nás" typu="ir.ui.view">
<field name="active" eval="false"/>
</záznam>

Alternativně nahraďte výchozí obsah těchto stránek pomocí XPath.

... blok kódu::xml
:caption: „/webové stránky/vzduchotěsnost/stránky/404.xml“

<šablona ID="404" zdědila ID ze šablony http_routing.404">
<xpath expr="//*[@id='wrap']" position="replace">
<t t-set="additional_title" t-value="'Stránka nenalezena'" />

<div id="wrap" třída="oe_struktura">
<!-- Obsah -->

</xpath>


.. viz též:
   - :doc:`Dokumentace Odoo o SEO <../../../applications/websites/website/pages/seo>`

... /webové-šablony/stránky/téma stránek:

Stránky s tématem
===========

Můžete přidat na svůj web kolik chcete stránek. Namísto definování šablony vytvořte
stránkový objekt.

**Prohlášení**

... blok kódu::xml
:komentář: „/webové_prostředí_vzduchotěsné/data/stránky/o-nás.xml“

<odoo noupdate="1">

<pole name="name">O nás</pole>
<vlastnost jméno="je publikována" hodnota="Pravda"/>
<položka jméno="klíč">webová stránka proti pronikání vody, o nás</položka>
<field name="url">/o-nas</field>
<pole název="webová stránka" hodnota="1"/>
<položka typu="qweb" />
<položka jméno="arch" typ="xml">


<div id="wrap" class="oe_structure">


</t>
</t>
</položka>



.. varování: více webů a „webová ID“

V kontextu modulu je vytvořený záznam k dispozici, pokud není jinak nastaveno, na každé webové stránce.
dostupné v databázi. Je lepší specifikovat ID webu, na kterém je příspěvek publikován.
Stránka bude vyhledatelná.

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * – Hřiště
     - Popis
   * - jméno
     - Název stránky (čitelný pro člověka).
   * - je_zveřejněna
     - Určete, zda je stránka publikovaná (viditelná pro návštěvníky).
   * – klíč
     - Hodnota klíče (musí být jedinečná).
   * - url
     - Relativní cesta, kde je stránka dostupná.
   * – typ
     - Typ zobrazení
   * Arch
     - Zobrazit architekturu (markup vaší stránky)

S využitím značky „<t t-call="website.layout">“ používáte výchozí šablonu stránky Odoo se svým kódem.

... /webové-šablony/stránky/téma-stránek/noupdate:

Atribut „noupdate“
--------------------

Toto atributy zabraňuje přepsání dat. Může být buď přidán na tag „data“, který obalí nějaká
záznamy, které mají být chráněny, nebo na „odoo“ tag, který má chránit všechny záznamy v souboru.

Zabezpečte všechny záznamy v souboru:

... blok kódu::xml


<odoo noupdate="1">
<záznam id="menu_firma" model="web.menu">
<!-- pole -->
</záznam>
<záznam id="menu_faq" typu="website.menu">
<!-- pole -->
</záznam>


Chránit konkrétní záznamy v souboru:

... blok kódu::xml



<záznam id="menu_firma" model="web.menu">
<!-- pole -->
</záznam>

<data noupdate="1">

<!-- Položky -->
</záznam>
<záznam id="menu_legal" model="web.menu">
<!-- Položky -->
</záznam>
</datum>


**Případ použití**

Do modulu byly vytvořeny několik statických stránek, tato byla umístěna na databázi
A uživatelé si některé stránky aktualizovali. Některé chyby je nutné opravit na
statické stránky a zároveň zabránit ztrátě změn provedených uživatelem.

**Problém**

Pokud dojde k aktualizaci modulu v databázi, každý záznam vyhlášený v modulu přepíše
takové, které jsou v databázi i když uživatel změnil některé z nich.

**Řešení**

Zahrnutím záznamu (nebo všech zaznamenaných záznamů v souboru) do značky
tag, který je při instalaci prvního modulu vytvořen, ale není aktualizován po instalaci dalšího modulu.
aktualizace.

.. spoiler::Co se stane, pokud byl záznam ručně smazán (např. položka v menu)?

Systém zjistí, že záznam neexistuje a vytvoří jej znovu.

..spoiler::Je tento postup platný jen pro statické záznamy stránek?

Ano, samozřejmě. Je technicky použitelný pro všechny typy záznamů.

... /webové-šablony/stránky/témata stránek/přebal/

Překryv hlavičky
--------------

Zadní pozadí hlavičky udělejte průhledné a vložte ji nad obsah stránky.

... blok kódu::xml

<pole název="přebal" hodnota="true"/>

.. obrázek: stránky/přebal.png
:alt: Překryv hlavičky

.. poznámka::
Pro vytvoření obsahu statické stránky použijte způsob práce Odoo, abyste zůstali
editovatelné pomocí Webového editoru. Prosím, zvažte, že Odoo využívá rámec Bootstrap (verze 5.1.3).

Najděte dostupné třídy a komponenty:

   - „Příručka pro Bootstrap <https://getbootstrap.com/docs/5.3/examples/cheatsheet/>“
   - „Dokumentace Bootstrapu <https://getbootstrap.com/docs/5.3/getting-started/introduction/>“

.._webové šablony/stránky/šablony stránek / šablony stránek:

Šablony stránek
--------------

Vytvořte předdefinované statické šablony stránek dostupné z okna Nová stránka.

**Prohlášení**

Šablony stránek musí být definovány v souboru __manifest__.py modulu prostřednictvím
:file:`new_page_templates.php` a :file:`new_page_template_templates.xml`:

... kódový blok:: python
:caption: `/webová_vrstva_vzduchotěsná/__manifest__.py
:zvýraznit-řádky: 11,16-19

   {
„název“: „Airproof Theme“,
'popis': '...'
'kategorie': 'Webové stránky/Šablona',
"verze": "{BRANCH}.0.0",
'autor': '...'
'licence': '...',
'závisí na webu': ['webová stránka']
"data": [
         # ...
'views/nový_stránkový_šablonový_vzorec.xml'
      ],
"aktiva": {
         # ...
      },
"nové šablony stránek":
"vzduchotěsné": {
'FAQ': ['s_airproof_text_block_h1', 's_title', 's_faq_collapse', 's_call_to_action']
      }
   }

**Šablony**

Pak musíte vytvořit šablonu pomocí konkrétního názvu podle hierarchie
souboru __manifest__.py. V tomto případě je název nová stránka s sekcí proti vlhkosti FAQ.
Konstrukční prvky, které tento šablona označuje, jsou přesně stejné jako standardní konstrukce s výjimkou
První, který byl upraven „na lince“.

Vytvořte nový instanci standardního bloku textu (důležitá je vlastnost primary). Použijte nějaké
adaptace:

... blok kódu::xml



<xpath expr="//div[contains-class('container')]|//div[contains-class('o_container_small')]" position="replace">
<div class="container s_allow_columns">
<h1 class="display-1">Často kladené otázky – Pomoc</h1>




Pro každý blok stránky vytvořte instanci (upravenou nebo ne):

... blok kódu::xml





Poté vytvořte svůj šablonový soubor s nějakým „t-snippet-call“ uvnitř obálky, jak je popsáno výše:

... blok kódu::xml


<šablona id="nová-stránka-s-otázkami-airproof-faq" jméno="Airproof - Nový vzhled otázek a odpovědí">
<div id="wrap">
<t t-snippet-call="web_vzduchotěsný.nový_stránkový_šablonový_vzduchotěsný_FAQ_s_textovým_blokem_nadpisem_1"/>
<t t-snippet-call="web_vzduchotěsnost.nový_stránkový_šablonový_vzduchotěsnost_faq_s_nadpisem"/>
<t t-snippet-call="web_vzduchotěsné.nový_stránkový_šablonový_vzduchotěsný_faq_s_faq_rozbaleným">

</div>


Jakmile je vytvořen šablona stránky, vytvořte si vlastní skupinu a přidejte ji do stávajících. Níže najdete seznam
Existující skupiny:

... blok kódu::xml
:caption: `/web/vzory/novy_stranicky_vzor_vzorov.xml`

<template id="nová stránka - skupiny">
<div id="basic">Basic</div>
<div id="about">O nás</div>
<div id="landing">Stránky pro přistání</div>
<div id="gallery">Galerie</div>
<div id="sluzby">Služby</div>
<div id="cena">Plány cen</div>
<div id="team">Tým</div>


Pokud chcete, můžete přidat vlastní skupiny do seznamu:

... blok kódu::xml


<šablona id="nová stránka - skupiny" dědí id="webová stránka - nová stránka - skupiny" jméno="Airproof - Nová stránka - Skupiny">
<xpath expr="//div[@id='custom']" position="after">
<div id="airproof">Airproof</div>



.. obrázek: stránky/nový-šablonový-vzhled.png
:šířka: 520
:alt: Seznam existujících šablon statických stránek

.. viz též:
`Pokračujte tím, že upravíte základní stavební bloky vlastního šablonového souboru <https://github.com/odoo/odoo/blob/64971a0b1b2f8c063def5846f6029d5bb3a574cd/addons/website/views/new_page_template_templates.xml#L38>`_.
