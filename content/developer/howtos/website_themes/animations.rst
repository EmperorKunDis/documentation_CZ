==========
Animace
==========

Odoo používá očarující animace, které mohou vaše webové stránky oživit. Výchozí nastavení obsahuje tři
druhy animací:

- Animace vzhledu
- Animace při posouvání
- Animace na přejetí kurzorem

... /webové-tematické-motivy/animaci/vzhled:

Na vzhledu
=============

V základu můžete přidávat animace do sloupců, textových a obrázkových prvků při jejich zobrazení.
Webovému editoru. Odoo detekuje, kdy je váš prvek v záhlaví a spustí
Animace. Velký výběr animací je k dispozici:

- Zatmění
- Náraz do zdi
- Otočit se dovnitř
- Zvětšit
- …

Můžete snadno definovat animace na sloupci vlastního tématu. Potřebujete přidat dvě třídy:
„o_animate“ a „o_anim_fade_in“. Druhá třída se mění podle typu animace, kterou
chceme používat.

Přidejte třídu o_animate_both_scroll, aby se animace spustila pokaždé, když sloupec přibude na
obrazovce. Animace se spustí pouze jednou.

Měli byste také definovat přímo v atributu style animace-duration a animace-delay.
atribut.

Dále můžete přidat směr animace. Například pro animaci prvku z
dole na obrazovce přidejte třídu „o_anim_from_bottom“ a nastavte vlastnost „--wanim-intensity“ ve stylu
určit směr a intenzitu pohybu.

**Použití**

... blok kódu::xml


<h2>Podnadpis části</h2>
<p>Napište jeden nebo dva odstavce, které popisují váš produkt nebo služby.</p>


.. obrázek: animace/vzhled.png
:alt:Animace s možnostmi vzhledu

... /webové-šablony/animaci/proklik:

Na řádku
=========

Stejně jako výše uvedené, můžete přidat animace na posouvání sloupce, textu a obrázku.
při každém posunutí okna prohlížeče přes animovaný prvek.

Můžeme přidat 6 animací na efekty při posouvání:

- Fade
- Soubor
- Bounce
- Otočit
- Zvětšit
- Zvětšit

Dále můžeme nastavit také efekt „vstup“ nebo „výstup“, animovanou „směrnost“ a animace.
„intenzita“ a „oblast pro posouvání“.

**Použití**

... blok kódu::xml

<div class="col-lg-6 o_animate o_animate_on_scroll o_animate_out o_anim_fade_in o_anim_from_right" data-scroll-zone-start="50" data-scroll-zone-end="100" style="--wanim-intensity: 100;">
<h2>Podnadpis části</h2>
<p>Napište jeden nebo dva odstavce, které popisují váš produkt nebo služby.</p>


.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 30 50 50

   * – možnost
     - Atribut dat
     - Hodnotový typ
   * –Intenzita
     - --wanim-intensity
     - Čisté číslo (v CSS)
   * - Zóna pro sledování
     - „data-scroll-zone-start“
     - Čisté
   * -Konec záložního pásma
     - „data-scroll-zone-end“
     - Čisté

.. obrázek: animace/posuv.png
:alt: Animace možností pro posouvání

.. viz též:
„Webová stránka Animate
<https://github.com/odoo/odoo/blob/c272c49657e8b7865bb93e5f1dcc183cc7d44f17/addons/website/static/src/scss/website.scss#L2075>`_

.._webové šablony/animaci při přechodu myši:

Při najetí myší
========

Třetí typ animací se vztahuje pouze na obrázky a spouští se každýkrát, když přejedeme myší nad
animovaný obrázek.

Můžeme přidat šest animací na přechodovém efektu:

- Překryv
- Zvětšit
- Zvětšit
- Dolly zoom
- Představení
- Mirror Blur

**Použití**

Povolte animace na přejetí myší přidáním třídy o_animate_on_hover do značky obrázku.
definujte také typ animace v atributu data-hover-effect.

... blok kódu::xml

<img
src="..." alt="..."
"class": "img img-fluid o_we_custom_image o_animate_on_hover"
data-přechodový efekt="překrytí"
data-overlay-effect-color="rgba(0, 0, 0, 0.25)"
    />

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 30 50 50

   * – možnost
     - Atribut dat
     - Hodnotový typ
   * Animace
     - „Přechod přes efekt přejetí“
     - Struna
   * –Intenzita
     - „účinek přechodu myši“
     - Čisté
   * -Nastavení přehrávání/Barva stopy
     - „barva přechodu“
     - Hexadecimální nebo RGBA hodnota
   * -Šířka čáry
     - „datová hrana“
     - Číslo (uložené jako „px“)

.. obrázek: animace/přechod.png
:šířka: 300
:alt:Animace na přejetí myší

.. viz též:
„Možnosti přechodu myši
<https://github.com/odoo/odoo/blob/c272c49657e8b7865bb93e5f1dcc183cc7d44f17/addons/website/views/snippets/snippets.xml#L694>`_
