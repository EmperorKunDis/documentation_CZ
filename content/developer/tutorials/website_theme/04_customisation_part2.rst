==================================
Kapitola 4 - Změny, část II
==================================

... /tutoriály/webová-šablona/základní-úpravy-část-2/výplň-obrázku:

Vytvořte vlastní tvar pozadí
================================

Tvar je dekorativní prvek, který lze použít na pozadí nebo obrázku. Jde o soubor ve formátu SVG.
které lze animovat a přizpůsobit různými barvami.

#. Chcete-li lépe odpovídat atmosféře webu, vytvořte si vlastní pozadí ve tvaru
Klient může použít na různých blozích.

Vytvořte si vlastní tvar pomocí následujícího nastavení:

   - Prohlásit svůj tvar. Originální „tvar SVG“ najdete zde
<{GITHUB_TUTO_PATH}/website_airproof/shape-waves.svg>.
   - Nastavte základní barvu tvaru na zelenou téma a přidejte ji do seznamu dostupných.
tvarů.

.. viz též:
Podívejte se na odkazované dokumentace, jak přidat vlastní pozadí tvarů.
<webové šablony/tvary/zadání/vlastní>.

.. obrázek: 04_přizpůsobení_část2/tvar.png

..tip:
| **Bděte,** je tu past.
|Ve vašem souboru SVG musíte použít barvy z výchozí palety Odoo.
| Zde chci, aby odpovídal primární barvě 1 („#CEF8A1“). Proto musí být v souboru SVG
použijte barvu číslo 3 z výchozí palety Odoo („#3AADAA“).

..spoiler:: Řešení

Najděte řešení v našem příkladu Airproof pro:

   - deklaraci tvaru na „shapes.xml <{GITHUB_TUTO_PATH}/website_airproof/data/shapes.xml>“.
   - Přidat tvar do seznamu díky
„primární proměnná.scss
<{GITHUB_TUTO_PATH}/website_airproof/static/src/sass/primární proměnné.scss> a <{GITHUB_TUTO_PATH}/website_airproof/static/src/option.xml
<{GITHUB_TUTO_PATH}/website_airproof/views/snippets/options.xml>.

2. Na základě návrhu Airproof aplikujte tvar, který právě přidali do bloku Text-Image.
stránka:

   - Zajistěte, aby tvar byl ve správné poloze.
   - Nastavte mu barvu na světle modrou barvu motivu.

.. viz též:
Podívejte se na odkazované dokumentace, jak používat:ref:`zadní tvar.
<webové_šablony/tvar/vlastní/použít>.

.. obrázek: 04_přizpůsobení_díl2/tvarová sekce.png

..tip:
Na rozdíl od běžného tvaru Odoo, když se aplikuje na části, nahraďte web_editor
s atributem „ilustrace“ v třídě objektu.

..spoiler:: Řešení

... kódový blok :: XML
:caption: „/webová_stěna_vzduchotěsná/data/stránky/domov.xml“

<!-- Blok textu a obrázku, tvar pozadí -->

data-snippet="s_image_text" data-name="Obrázek - Text" style="barva pozadí: RGB (41, 128,
187);" data-oe-shape-data="{'shape': 'illustration/airproof/vlnky', 'colors': {'c1': '#BBE1FA'},
'flip': ['x']}">

url("/web_editor/shape/illustration/airproof/waves.svg?c2=#BBE1FA");
background-position: 100% 100%;"/>
         [...]
</odd>

... /tutoriály/webový-vzhled/základní úpravy/úvod do gradientu:

Přidejte pozadí s barevným přechodem
=========================

Použijte vlastní přechod mezi barvami modrou a fialovou na bloku „Nejnovější produkty“.
„rgb(11, 142, 230)“ na tmavě modrou „rgb(41, 128, 187)“.

.. viz též:
Podívejte se na odkazované dokumentace, jak používat :doc:`/developer/howtos/website_themes/gradients`.

..spoiler:: Řešení

... kódový blok :: XML
:caption: „/webová_stěna_vzduchotěsná/data/stránky/domov.xml“

<!-- Nejnovější produkty -->

data-scroll-background-ratio="0" data-snippet="s_parallax" data-name="Paralaxa"
background-image: linear-gradient(0deg, #2985B9 0%, #A1E6F5 100%)

         [...]
</odd>

... /tutoriály/webová-tematika/zvýraznění-a-animaci-díl-2/:

Animace
==========

Klient miluje celkový design, ale stránku považuje za trochu statickou. Zvýšit interaktivitu stránky
animace jako například „přechod do pozadí“, „otočení“, „skok“ atd., které lze aplikovat na sloupce, obrázky
texty, tlačítka...

Za pomoci vzduchotěsného návrhu oživte tyto prvky:

- text prvního slidu v karuselu.
- samolepka a fotografie dronu z první diapozitivy.
- čtyři sloupce s ikonami.

Upravte animace, aby byly plynulejší.

.. viz též:
Podrobnější informace o tom, jak používat :doc:`/developer/howtos/website_themes/animations`, naleznete v příslušné dokumentaci.

... obrázek: 04_přizpůsobení_díl 2/animace.gif

..spoiler:: Řešení

Najděte řešení v našem příkladu Airproof v souboru home.xml


... kódový blok :: XML
:caption: Animace obrázku

<img src="/web/obrazky/web_airproof.img_sticker" class="img img-plovoucí
x_sticker o_animate o_anim_rotate_in o_visible"" style="animation-delay: 0.8s;
--wanim-intensity: 30;"/>

<img src="/web/obrazky/webov%C3%A1_vzduchotěsnost.png" class="img img-fluid o_animate
o_anim_zoom_out o_visible" alt="Dron" />

... kódový blok :: XML
:komentář: Animace textu

<span class="o_animated_text o_animate o_anim_fade_in o_anim_from_bottom o_visible">One
krok

... kódový blok :: XML
:popisek: Animační sloupec


o_anim_fade_in o_animate o_anim_from_bottom o_visible" styl="z-index: 2;
rozloha: 6 / 1 / 12 / 4; --wanim-intenzita: 15">
</div>

... _návody/webová šablona/základní úpravy/formuláře:

Formy
=====

Formuláře v Odoo jsou velmi silné. Mohou posílat e-maily přímo do osobní schránky nebo integrovat
přímo s dalšími aplikacemi systému Odoo. To je skvělé, protože jedním z hlavních cílů vašeho klienta je
pozáruční servis. Proto musí být kontaktní formulář správně konfigurován.

Na základě vzduchotěsného návrhu vytvořte kontaktní stránku. Pamatujte na to, že je třeba zakázat výchozí a přidat
novou stránku odkazující na menu. Klient má následující požadavky pro kontaktní formulář:

- Pole „Jméno“ a „E-mail“.
- *Název společnosti*.
- Pole „Snížená sazba DPH“ se zobrazí pouze v případě, že je vyplněno pole „Název společnosti“.
- Všechna pole by měla být povinná, s výjimkou položky „Firma“.
- Odeslání formuláře musí vyvolat odeslání e-mailu.
- Po odeslání formuláře by mělo zůstat na kontaktní stránce viditelné „děkujeme za odeslání“.

.. viz též:
Podívejte se na odkazovanou dokumentaci, jak postupovat:

     - :ref:`deaktivovat výchozí stránky <webové šablony/stránky/výchozí>“
     - :ref:`vytvořit novou stránku <webové šablony/stránky/šablony stránek>`,
     - :ref:`přidat položku v nabídce <webové šablony/navigace/nabídka>“
     - Vytvořit formulář podle návodu <developer/howtos/website_themes/forms>.

..tip:
Pro určení správného kódu pro váš formulář:

   - Vytvořte stránku pro testování pomocí Webového editoru.
|Přetáhněte a pusťte na místo, které vás zajímá, a aplikujte správný návrh.
|Použijte kód vytvořený pomocí :guilabel:`Editor HTML/SCSS`.
   - Můžete také najít původní blokový kód v Odoo:
'odoo/addons/website/views/snippets/s_website_form.xml
<{GITHUB_PATH}/addons/website/views/snippets/s_website_form.xml>.

..spoiler:: Řešení

Řešení najdete v našem příkladu Airproof v souboru contact.xml
<{GITHUB_TUTO_PATH}/website_airproof/data/pages/kontakt.xml>.
