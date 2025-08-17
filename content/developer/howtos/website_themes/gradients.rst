=========
Gradienty
=========

V této kapitole se dozvíte, jak:

- Přidejte přechod do části nebo nadpisu.
- Přidejte vlastní barevný přechod do palety Webové stránky.

..._webové šablony/barevné přechody/standardní:

Standard
========

V základním nastavení je možné zvolit několik stupňů přímo v editoru webových stránek.
použití vlastních šablon, gradientů musí být provedeno přímo v záhlaví sekce s atributem style.

**Použití**

... blok kódu::xml

<section class="s_text_image" data-snippet="s_text_image" data-name="Text - Image" style="background-image: linear-gradient(135deg, rgb(255, 204, 51) 0%, rgb(226, 51, 255) 100%) !important;">



Pro aplikaci gradientu na text použijte značku <font> s třídou text-gradient.

... blok kódu::xml


<font class="text-gradient" style="background-image: linear-gradient(135deg, #d95f4a 0%, #4ba7e8 100%);">Subheading of Section</font>


..._webové šablony/barevné přechody/vlastní:

Obchodní zvyklost
======

Přidejte vlastní gradienci do Webové stránky. Tímto způsobem uživatel může snadno používat i bez
Manuálně je znovu vytvářet.

... blok kódu::xml
:caption: „/webové stránky_vzduchotěsné/data/sklony.xml“

<záznam id="barva-vybíráč" typu="ir.ui.view">
<políčko jméno="klíč">webová_vzduchotěsná.barvy</políčko>
<políčko jméno="název">Vlastní gradienty</políčko>
<field name="typ">qweb</field>
<položka jméno="dědictví_id" odkaz="webový editor. barvy vybírat"/>
<položka jméno="arch" typ="xml">
<xpath expr="//div[@data-name='predefined_gradients']/t[@t-set='gradients']" position="after">
<t t-set="gradients" t-value="gradients + ['linearní gradient (135 stupňů, RGB(203, 94, 238), 0%), RGB(75, 225, 236), 100%')'" />
</xpath>
</p>
</záznam>
