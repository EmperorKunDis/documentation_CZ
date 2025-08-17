===========
PDF zprávy
===========

S aplikací Studio můžete: „upravit stávající PDF reporty <studio/pdf-reports/edit>“ (např. faktury,
citace, atd.) nebo vytvořte nové (viz. studio/pdf-reporty/edit).

.._studia/pdf-reporty/výchozí-layout:

Výchozí rozložení
==============

Výchozí rozložení zpráv je spravováno mimo Studio. Přejděte do položky „Nastavení“ a poté
sekci „Společnosti“ hlavní stránky a klikněte na „Nastavení formátu dokumentů“.
Nastavení formátu je společnostně specifické, ale platí pro všechny zprávy.

..tip:
Můžete vidět, jak se různé nastavení projeví na uspořádání zprávy v náhledu.
v pravé části okna „Nastavení rozložení dokumentu“. Při tvorbě nebo úpravě dokumentu
reportu si můžete prohlédnout náhled zprávy kliknutím na tlačítko „Náhled“ v levém menu.
straně obrazovky.

Použijte následující nastavení:

.._studia/pdf-reporty/výchozí-formát-layout:

- :guilabel:`Přizpůsobit“: K dispozici je sedm různých rozložení:

...... záložky::

.. tab:: Světlo

.. obrázek: pdf_reporty/layout-light.png
:alt: Vzorek uspořádání světelného hlášení
:skalka: 90 %

.. tab:: Záložka

.. obrázek:: pdf_reporty/layout-boxed.png
:alt: Vzorek uspořádání zprávy v rámečku
:skalka: 90 %

... tab:: Tučný

.. obrázek:: pdf_reporty/layout-bold.png
:alt: Vzorek odvážného uspořádání zpráv
:skalka: 90 %

.. tab:: Proužkovaný

.. obrázek:: pdf_reporty/layout-striped.png
:alt: Vzorek uspořádání zpráv s pruhy
:skalka: 90 %

.. tab::Bublina

.. obrázek:: pdf_reporty/layout-bubble.png
:alt: Vzorek uspořádání bublin
:skalka: 90 %

.. tab:: Vlna

.. obrázek::pdf_reporty/layout-wave.png
:alt: Vzorek uspořádání vlnového hlášení
:skalka: 90 %

....... tab::Složka

.. obrázek:: pdf_reporty/složka_layoutu.png
:alt: Vzorek uspořádání složky
:skalka: 90 %

.._studia/pdf-reporty/výchozí-layout-předloha:

- :guilabel:`Pozadí“: Následující pozadí jsou k dispozici:

  - :guilabel:`Prázdná obrazovka“: Není zobrazeno nic.
  - :guilabel:`Demonstrativní logo“: V pozadí je zobrazeno demonstrační logo.
  - :guilabel:`Vlastní obrázek“: Nahrát vlastní pozadí.

.._studia/pdf-reporty/výchozí-formát písma:

- :guilabel:`Text`:K dispozici je osm fontů: Lato, Roboto, Open Sans, Montserrat, Oswald,
Raleway, Tajawal (podporuje arabské a latinské písmo) a Fira Mono. Přejděte na stránku „Google Fonts
webové stránky <https://fonts.google.com/>, kde si je můžete prohlédnout.

.._studio/pdf-reporty/výchozí-layout-logo:

- :guilabel:Logo společnosti: Klikněte na tlačítko „Upravit“ a nahrajte nebo změňte logo.
Přidává logo do záznamu o společnosti na modelu Company, který se nachází v
:menu:"Nastavení" a poté kliknutím na "Aktualizovat informace" v sekci "Společnosti".
části.

.._studia/pdf-reporty/výchozí-barevné schéma:

- :guilabel:`Barvy“: Změňte primární a sekundární barvy používané k strukturování zpráv.
Barvy jsou automaticky generovány podle barev loga.

.._studio/pdf-reporty/výchozí-formát-adresa:

- :guilabel:`Adresa“: Název a adresu společnosti se zobrazuje v záhlaví odkazu na
reportů <studia/pdf-reporty/hlavička-patka>. Můžete přidat více řádků textu.

.._studia/pdf-reporty/výchozí-formát-nadpisu:

- :guilabel:`Záhlaví“: Toto se zobrazuje v záhlaví :ref:`externích zpráv
<studia/pdf-reporty/hlavička-patka> pomocí světlého, pruhovaného, bublinového, vlnkového a složkového
layouty a v záhlaví externích zpráv s použitím layoutu Boxed a Bold.
Můžete přidat více řádků textu.

.._studia/pdf-reporty/výchozí-formát-patičky:

- :guilabel:`Záhlaví“: Tento text se používá v záhlaví externích zpráv
<studia/pdf-reporty/hlavička-patka>. Můžete přidat více řádků textu.
upravit zápatí pomocí reportového editoru (viz také: :ref:`editor reportů <studio/pdf-reports/edit>`).

.._studia/pdf-reporty/výchozí-layout-papír:

- :guilabel:`Formát papíru“: Toto nastavuje výchozí velikost papíru pro zprávy. Můžete vybrat
:guilabel:`A4“ (21 cm x 29,7 cm) a :guilabel:`US Letter“ (21,59 cm x 27,54 cm).
definované pro jednotlivé zprávy v poli „Formát papíru“ ve :guilabel:`Vlastnostech
:ref:`Studiu <studium/pdf-reporty/upravit-možnosti>`

...... poznámka::
Další papírové formáty mohou být k dispozici v závislosti na tom, které aplikace nebo moduly jsou nainstalovány.
například štítky pro inventář nebo nálepky pro události v aplikaci Events.

.._studia/pdf-reporty/vytvorit:

Vytváření nových PDF zpráv
========================

Vytvořit nový report pro model:
(např. objednávky na prodej) přístup k modelu, klepněte na ikonu „Studio“ (viz ikona „Povolit Studio“)
tlačítko, pak klikněte na „Zprávy“. Klikněte na „Nový“ a v otevřeném okně
Vyberte typ zprávy. Tento se používá jen k určení, co bude v hlavičce zobrazeno a
patička:

.._studia/pdf-reporty/hlavičky-patky:

- :guilabel:`Externí“:

  - Hlavička zobrazuje logo společnosti :ref:`<studio/pdf-reports/default-layout-logo>`.
:ref:`název a adresu <studia/pdf-reporty/výchozí-formát-adresa>“.
Vzory Light, Striped, Bubble, Wave a Folder.
:ref:`tagline <studio/pdf-reports/default-layout-tagline>“ se také objevuje v hlavičce.

  - V zápatí se zobrazují hodnoty nastavené v
:ref:`Záhlaví <studio/pdf-reports/default-layout-header>`, stránkový číslo a název souboru.
zprávy s použitím formátu Boxed a Bold.
:ref:`tagline <studio/pdf-reports/default-layout-tagline>“ se také objevuje v zápatí.

- :guilabel:Vnitřní: Hlavička zobrazuje aktuální datum a čas uživatele a název společnosti.
:ref:`jméno a adresu <studijní/pdf-reporty/výchozí-formát-adresa>“ a stránku.
žádný zápatí.

- :guilabel:'Prázdný': Nejsou hlavička ani patka. Klikněte do horního levého rohu
stránku pro úpravu zprávy.

Jakmile vytvoříte zprávu, můžete začít :ref:`upravovat ji <studio/pdf-reports/edit>`.

.._studia/pdf-reporty/edit:

Úprava PDF zpráv
===================

Pro přístup k dostupným zprávám o modelu se přihlaste do modelu a klikněte na
Tlačítko „Studio“ (ikona „OI Studio“) a poté klikněte na „Zprávy“. Vyberte
existující zprávu otevřít.

Alternativně můžete také otevřít Studio, kliknout na „Zprávy“ a vyhledat konkrétní
report nebo model.

.. důležité:
Je silně doporučeno **vytvořit kopii** standardního hlášení a provést změny v
duplicitní verzi. Chcete-li zkopírovat zprávu, přejeďte myší na horním pravém rohu
zprávy klikněte na ikonu „vertikální elipsa“ (:guilabel:"vertikální elipsa") a
Pak vyberte Duplikát.

.. obrázek::pdf_reporty/duplicitni_zpravy.png
:alt:Duplikace PDF zprávy

..._studia/pdf-reporty/upravit možnosti:

Možnosti
-------

Jakmile si vyberete nebo vytvoříte zprávu, můžete použít možnosti v levém panelu obrazovky
to:

- Změňte název reportu: Nový název se použije všude (ve studiu, v
:guilabel:`Tisknout“ v podmenu pod ikonou „gear“ (ikona :guilabel:`fa-cog`) ve formuláři.
(jméno souboru ve formátu PDF).
- Upravte pole „Formát papíru“: Pokud není vybrána žádná hodnota, bude použit formát definovaný v
:ref:`výchozí formát <studio/pdf-reports/default-layout-paper>`.
- :guilabel:`Zobrazit v nabídce tisku“: přidat zprávu do nabídky „Tisk“ ve formuláři.
- :guilabel:`Uložit jako přílohu na záznamu první“
V případě, že je zpráva vytvořena a následně znovu načtena, bude obsahovat původní verzi zprávy.
Je povinná pro faktury a hlavně se používá v tomto případě.
- :guilabel:`Omezení viditelnosti na skupiny“: omezit dostupnost PDF zprávy pro konkrétní
:doc:`uživatelské skupiny <../obecne/uzivatele/prava_prihlaseni>“.
- :guilabel:`Upravit zdroje“: upravovat zprávu přímo v souboru XML.
<studia/pdf-reporty/XML-editace>.
- :resetovat zprávu“: vymazat všechny změny v reportu a vrátit ho do svého původního stavu
verze.
- :guilabel:`Náhled tisku“: vygenerovat a stáhnout náhled zprávy.

.._studia/pdf-reporty/report-editor:

Šéfredaktor reportáže
-------------

Editor zprávy umožňuje upravit obsah a formátování zprávy.

..tip:
  - Můžete provést „Zrušit“ nebo „Přetočit“ změny pomocí příslušných tlačítek nebo zkratek
´CTRL‘ + ‚Z‘ a ‚CTRL‘ + ‚Y‘.

  - Změny se ukládají automaticky po opuštění zprávy nebo ručně pomocí
tlačítko „Uložit“.

  - Můžete vrátit zprávu do jejího standardního stavu kliknutím na tlačítko „Zpět“
v levém dolním rohu obrazovky.

.. důležité:
Upravování hlavičky a paty zprávy ovlivňuje všechny standardní i vlastní zprávy.

Podmíněné bloky
~~~~~~~~~~~~~~~~~~

Částečně vyplněné čtverce představují **podmíněné bloky** (*if/else* příkazy). Ty se používají k
Zobrazit obsah podle specifických podmínek. Klikněte na blok, abyste zjistili podmínky.

.. obrázek: pdf_reporty/podmíněný blok.png
:alt:Zobrazení podmínek, které se vztahují na blok.

Vyberte hodnotu, abyste viděli její odpovídající výstup a upravili ji, pokud je třeba.

.. obrázek:: pdf_reporty/podmíněný-blok-jinak.png
:alt:Zobrazení výstupu jiné podmínky.

.. poznámka::
Pozice lze upravovat pouze v XML editoru.

Další obsah
~~~~~~~~~~~~~

V zprávách existují dva typy obsahu textu:

- Statická část textu, tedy ta, která není zvýrazněna modře, lze upravovat přímo v
editor.
- Dynamický text, tedy text v modrém rámečku, který je nahrazován
:doc:`hodnoty pole </applications/studio/fields> při generování zprávy například číslo objednávky nebo
datum citace.

Můžete do zprávy přidat obsah (např. pole, seznamy, tabulky, obrázky, reklamní plochy atd.)
příkazy. Zadejte znak / a otevřete :ref:`pohon box <essentials/html_editor/commands>“, poté zadejte
Název příkazu nebo vyberte jej z seznamu.

Chcete-li do zprávy přidat statický text, vložte jej tam, kde chcete.

Pro pokročilejší změny můžete:ref:`upravit zprávu přímo v XML.
<studia/pdf-reporty/XML-editace>.

.._studia/pdf-reporty/přidat pole:

Přidej pole
***********

Přidejte pole zadáním znaku / a vyberte příkaz „Políčko“. V seznamu, který se otevře, vyberte
nebo vyhledejte pole; klikněte na pravý šipku vedle názvu pole, abyste se dostali do seznamu souvisejících.
Pokud je pole nevyplněné, zobrazí se výchozí hodnota
v záznamu a stiskněte klávesu Enter.

.. obrázek: pdf_reports/powerbox-field.png
:alt:Vyberte příbuznou oblast.

.. _studia/pdf-reporty/přidat-upravit-tabulku:

Přidat nebo upravit tabulku
*******************

V zprávách existují dva typy tabulek:

- :ref:`Statické tabulky <studio/pdf-reports/static-table>“, které se používají k zobrazení statického textu nebo polí. Pro tento typ tabulky definujete
počet sloupců a řádků při přidání tabulky.
- :ref:`Dynamické tabulky <studio/pdf-reporty/dynamicka-tabulka>“, které se používají k zobrazení dat z
:ref:`vztahová pole <studio/fields/relational-fields>“.
Pro tento typ tabulky nastavíte pouze počet sloupců při přidání tabulky. Počet řádků
Počet řádků v generovaném výstupu bude určený počtem záznamů ve spojené tabulce.
spojené s aktuálním modelem.

...... příklad::
V zprávě o prodejní objednávce se používá dynamická tabulka k zobrazení řádků objednávky souvisejících s prodejem.
Pokud objednávka obsahuje 10 řádků, tabulka v generovaném výstupu má 10 sloupců.
Pokud obsahuje dvě objednávkové řádky, má tabulka dvě sloupce.

.._studia/pdf-reporty/statické-tabulky:

Přidejte nebo upravte statickou tabulku
^^^^^^^^^^^^^^^^^^^^^^^^^^

Přidejte statickou tabulku zadáním znaku / a výběrem příkazu Tabulka. Zadejte počet
sloupce a řádky pro tabulku. Jakmile je tabulka přidána, můžete začít s jejím úpravami.

Můžete vložit, přesunout a smazat sloupce a řádky pomocí nástrojů pro práci se tabulkami. Umístěte kurzor na horní hranici
sloupce nebo vlevo od řádku, pak klikněte na fialový obdélník a vyberte možnost.

.. obrázek:: pdf_reporty/stolni-nastroje.png
:alt: Seznam dostupných možností pro úpravu struktury tabulky.

Pro změnu šířky sloupce přetáhněte hranici sloupce na požadované místo; resetujte všechny sloupce
standardní velikost pomocí volby „Vyresetovat velikost“ v nástrojích tabulky.

Přidejte pole svého výběru (:ref:`<studio/pdf-reports/add-field>`) do buňky nebo statický text.
písemně.

..tip:
Každý řádek může obsahovat text ve strukturované formě bez použití tabulky. Text do řádku lze vložit pomocí sloupců.
zadáním znaku „/“ a výběrem příslušného příkazu: „2 sloupce“, „3 sloupce“.
:guilabel:`4 sloupce“.

.._studia/pdf-reporty/dynamická tabulka:

Přidejte nebo upravte dynamickou tabulku
^^^^^^^^^^^^^^^^^^^^^^^^^^^

...... poznámka::
     - Jen vztahy typu „jedna k mnoha“ nebo „mnoho k mnoha“ mohou být zobrazeny jako dynamické tabulky.
     - Existující dynamická tabulka v základním výstupu má složitější strukturu než dynamická tabulka
doplníte sami. U takových tabulek je možné přidávat nebo mazat sloupce; není to ale možné
pohyb sloupců nebo vložení, posunutí nebo odstranění řádků.

Přidejte dynamickou tabulku stisknutím klávesy / a vyberte příkaz „Dynamická tabulka“. V seznamu
otevřete, vyberte nebo vyhledejte vztah, na kterém bude tabulka založena, a stiskněte klávesu Enter.
tabulka byla přidána a můžete začít s jejím úpravami.

Můžete vložit, přesunout nebo odstranit sloupce pomocí nástrojů pro práci s tabulkou.
:ref:`statická tabulka <studio/pdf-reports/static-table>“. Je také možné vložit statické řádky
které se objeví nad nebo pod generovanými řádky.

Přidat pole do buňky, vymazat všechny místní zástupce textu a poté přidat pole svého výběru.
<studia/pdf-reporty/přidat pole>. Dialogové okno, které se otevře, zobrazí zdrojový objekt pro
pole (např. model *Objednávkové řádky*) a seznam dostupných polí.

.. obrázek: pdf_reports/available-fields.png
:alt: Seznam dostupných polí pro model prodejních řádků.

Vyměňte štítek „Název sloupce“ za štítek své volby.

.. poznámka::
Výchozí řádek automaticky prochází obsahem pole a generuje řádky na zprávě.
pro každý hodnotový řádek (např. jeden sloupec na řádek objednávky).

Formátování
**********

Pro formátování textu v zprávě vyberte jej a poté použijte možnosti ve
:doc:`textový editor </aplikace/základní/html_editor>“.

... obrázek::pdf_reporty/textovy_editor.png
:alt: Formátovat text pomocí textového editoru.

.._studia/pdf-reporty/XML-editace:

Upravování zprávy ve formátu XML
------------------------

.. varování:
Přímo upravovat XML může vést k problémům při upgradu.
<../../../administration/upgrade>. Pokud se tak stane, jednoduše kopírujte své změny z původní
databáze do vaší aktualizované databáze.

Pro editaci zdrojového kódu zprávy klikněte na tlačítko „Upravit zdroje“ v levém panelu.

Příklady
~~~~~~~~

.. spoiler:: Upravit widget pole

Pokud chcete změnit způsob zobrazení dat ve vašem výkazu, můžete upravit výchozí hodnoty pole.
:doc:`widget </applications/studio/fields>“ ručně. V následujícím příkladu je datum objednávky
datum a čas výchozí hodnotou, zatímco jednotková cena má přesnost dvě desetinná místa.
místa.

... kódový blok :: XML
:vyzdvihnout-řádky: 2,3

<div třída="oe_struktura">
<t-field t-field-name="doc.date_order" />
<span t-field="cena_s_dph"/>
</div>

Použitím možnosti „t-options“ (v tomto případě možností „widget“) lze tyto pole upravit tak, aby zobrazovaly
jen datum a přesnost na čtyři desetinná místa, tj.:

... kódový blok :: XML
:vyzdvihnout-řádky: 2,3

<div třída="oe_struktura">
<span t-field="doc.date_order" t-options="{'widget': 'date'}"/>
<span t-field="cena_s_dph" t-options="{'widget': 'float', 'precision': 4}"/>
</div>

.. spoiler:: Podmíněné bloky

Pokud chcete zobrazit nebo skrýt obsah na základě specifických podmínek, můžete ručně přidat příkaz „pokud ano, pak ano“.
kontrolní výrazy v zprávě XML.

Příkladem může být skrytí vlastního datového řádku, pokud nejsou žádné štítky. V takovém případě lze použít t-if
atribut definující podmínku, která je pak vyhodnocena jako „pravda“ nebo „ne“. Tabulka
nebude zobrazena, pokud v citaci nejsou žádné tagy.

... kódový blok :: XML
:vyzdvihnout-řádky: 2

<!-- kořenový prvek tabulky -->
<table class="table" t-if="len(doc.tag_ids) > 0">
<!--thead = hlavička tabulky, řádek s názvy sloupců-->
<hlavička>
<!-- řádek tabulky -->
<tr>
<!-- hlavička tabulky -->
<th>ID</th>
<th>Jméno</th>
</tr>
</hlavní hlavička>
<!-- tělo tabulky, hlavní obsah -->
<tbody>
<!-- vytváříme řádek pro každý podřádkový záznam s t-foreach -->
<tr t-foreach="doc.tag_ids" t-as="tag">
<!-- pro každou řádek vypíšeme jméno a cenu jako buňky tabulky -->
<td t-out="tag.id"/>
<td t-out="tag.name"/>
</tr>

</table>

Pokud chcete zobrazit jiný blok, pokud je výsledek příkazu t-if roven False,
může specifikovat pomocí příkazu t-else. Blok t-else musí následovat přímo po bloku t-if
block v dokumentu, který není potřeba specifikovat žádnou podmínkou v t-else.
atribut. Například můžeme ukázat rychlou zprávu s vysvětlením, že nejsou žádné štítky na
citace:

... kódový blok :: XML
:vyzdvihnout-řádky: 22

<!-- kořenový prvek tabulky -->
<table class="table" t-if="len(doc.tag_ids) > 0">
<!--thead = hlavička tabulky, řádek s názvy sloupců-->
<hlavička>
<!-- řádek tabulky -->
<tr>
<!-- hlavička tabulky -->
<th>ID</th>
<th>Jméno</th>
</tr>
</hlavní hlavička>
<!-- tělo tabulky, hlavní obsah -->
<tbody>
<!-- vytváříme řádek pro každý podřádkový záznam s t-foreach -->
<tr t-foreach="doc.tag_ids" t-as="tag">
<!-- pro každou řádek vypíšeme jméno a cenu jako buňky tabulky -->
<td t-out="tag.id"/>
<td t-out="tag.name"/>
</tr>

</table>
<div class="text-muted" t-else="">Žádný značkovací prvek na tomto dokumentu nebyl zjištěn.</div>

Použitím zkratky „t-if/t-else“ si reportér všimne, že tyto části jsou
vzájemně vylučující a měly by být zobrazeny jako podmíněné bloky:

.... obrázek::pdf_reporty/xml-podmínka-pokud.png
:alt:Předzobrazení výstupu pokud jsou tagy.

Pomocí editoru můžete přepínat podmínky a zobrazovat jejich výstup:

.. obrázek:: pdf_reporty/XML-podmínka-jinak.png
:alt:Předzobrazení výstupu, pokud nejsou žádné tagy.

Pokud chcete mít více možností, můžete také použít příkaz t-elif k přidání prostředníka
podmínky. Například takto se mění název faktury na základě podmínek prodeje.
podmínky dokumentu, na němž je založen.

... kódový blok :: XML

<h2 class="mt-4">
<span t-if="env.context.get('proforma', False) nebo je_pro_forma">Faktura pro forma #</span>
<span t-elif="doc.state in ['návrh','odesláno']">Citace číslo </span>
<span t-else="">Objednávka číslo </span>
SO0000


Titul *Dodací list proforma* se používá v závislosti na některých kontextuálních podmínkách.
Pokud nejsou splněny podmínky a stav dokumentu je buď „návrh“ nebo „odeslaný“, pak
Pro tento případ se používá citace. Pokud žádný z uvedených podmínek není splněn, název hlášení je „Objednávka“.

.. spoiler::Obrázky

Pracovat s obrázky v zprávě může být náročné, protože přesná kontrola velikosti a umístění obrázku je
Chování není vždy zřejmé. Můžete do reportu vložit obrázkové pole pomocí editoru reportu
(pomocí příkazu Field, viz:ref:`Příkaz pole <studio/pdf-reports/add-field>`) a vložením do XML
Použitím příkazu t-field a doplňujících atributů t-options lze dosáhnout lepšího nastavení velikosti.
řízení pozice.

Příklad kódu, který vypíše pole „image_128“ produktu řádku
obrázek široký 64 pixelů s automaticky nastavenou výškou podle poměru stran obrazu.

... kódový blok :: XML

<span t-field="line.product_id.image_128" t-options-widget="image" t-options-width="64px"/>

Následující možnosti jsou k dispozici pro obrázkové widgety:

   - „šířka“: šířka obrázku, obvykle v pixelech nebo jednotkách CSS (například „rem“) (nechte prázdné
(pro automatické šířky).
   - „Výška“: výška obrázku, obvykle v pixelech nebo jednotkách CSS (např. „rem“) (nechte prázdné
(pro automatické nastavení výšky).
   - „třída“: CSS třídy použité v značce „img“; „Bootstrap třídy
jsou k dispozici na adrese <https://getbootstrap.com/docs/5.1/content/tables>.
   - `alt`: alternativní text obrázku
   - `style“: atribut stylu; umožňuje přehrát styly volněji než s
„Třídy Bootstrapu <https://getbootstrap.com/docs/5.1/content/tables>“.

Tyto atributy musí obsahovat řetězce, tedy text uzavřený v uvozovkách v uvozovkách, například
`t-options-width="64px"`.

....... poznámka::
Obrázekový widget nelze použít na značce img. Místo toho nastavte příkaz t-field na
uzlu „span“ (pro obsah vložený do textu) nebo uzlu „div“ (pro blokový obsah).

Například přidáme do tabulky s cenovou nabídkou sloupec s obrázkem produktu.

... kódový blok :: XML
:zvýraznit-řádky: 4,14-20

<table class="table table-sm o_main_table table-borderless mt-4">
<th styl="zobrazení jako řádkový sloupec tabulky">
<tr>
<th>Obrázek</th>
<th name="th_description" class="text-start">Popis</th>
<th>Kategorie produktu</th>
<th name="th_quantity" class="text-end">Množství</th>

      [...]
<t t-foreach="lines_to_report" t-as="line">
<t t-set="součet_doplatku" t-value="součet_doplatku + cena_doplatku_line"/>
<tr t-att-class="'bg-200 fw-bold o_line_section' pokud je typ zobrazení 'line_section', jinak 'fst-italic o_line_note' pokud je typ zobrazení 'line_note', jinak prázdné">
<t t-if="!line.display_type">
<td>
<span t-field="line.product_template_id.image_128"



                                 />




Atribut t-options-width omezuje šířku obrázku na 64 pixelů a Bootstrapové třídy
použité v t-options-class vytváří okraj s zaoblenými rohy a stínem, který připomíná miniaturu.

.. obrázek:: pdf_reporty/XML-obrazek.png
:alt:Přidat sloupec s obrázkem produktu do tabulky cenové nabídky.
