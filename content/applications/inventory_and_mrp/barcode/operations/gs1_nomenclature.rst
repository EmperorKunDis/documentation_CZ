========================
Nomenklatura čárových kódů GS1
========================

..._čárový kód/operaci/GS1:

.. |AI| nahradit za: zkratka: `A.I. (Application Identifier)`
.. |EAN| nahradit za: zkratku: EAN (Global Trade Item Number)
.. |GTINy| nahradit za: :abbr:`GTINy (globální čísla položek obchodu)`


„Nomenklatura GS1 <https://www.gs1us.org/>“ sdružuje různá data o produktech a dodavatelském řetězci do
jediný čárový kód. Odoo přijímá „globální obchodní čísla“
<https://www.gs1.org/standards/get-barcodes>_(GTIN), zakoupené podniky, aby umožnily globální
dodávky, prodej a produktové listy v oblasti elektronického obchodu.

Nastavte systém GS1 tak, aby skenoval čárové kódy uzavřených krabic a identifikoval klíčové produkty
informace jako například GTIN, číslo šarže, informace o množství a další.

.. důležité::
|EANy| jsou jedinečné identifikační kódy výrobku, které **musí být zakoupeny u společnosti GS1
<https://www.gs1.org/standards/get-barcodes>_ pro použití čárových kódů GS1.

.. viz též:
   - „Všechny čárové kódy GS1 <https://www.gs1.org/standards/barcodes/application-identifiers>“
   - :ref:`Výchozí pravidla GS1 Odoa <barcode/operations/default-gs1-nomenclature-list>“
   - :ref:`Proč mi nefunguje čárový kód? <barcode/operations/troubleshooting>`

.. _čárový kód/operaci/nastavení čárového kódu:

Zavedení čárového kódu pro označení
===========================

Pro použití systému GS1 navigujte do aplikace „Skladové zásoby“ - „Nastavení“
Nastavení“. Pak pod položkou „Čárový kód“ zaškrtněte políčko „Skenovač čárových kódů“.
Dále vyberte položku „Barcode Nomenclature --> Default GS1 Nomenclature“ z výchozího
nominální možnosti čárového kódu.

.. obrázek: gs1_nomenclature/setup-gs1-nomenclature.png
:align:center
:alt: Vyberte GS1 z roletky a klikněte na externí odkaz, abyste viděli seznam pravidel GS1.

Seznam GS1 pravidel a štítků, které Odoo podporuje zcela automaticky, je přístupný kliknutím na
ikonu „➡️ (šipka)“ vedle výběru „Nomenklatura čárových kódů“.

V okně „Otevřená nomenklatura“ zobrazte a upravujte názvy pravidel společnosti GS1.
v Odoo. Tabulka obsahuje všechny informace, které lze skenováním čárového kódu GS1 zkomprimovat.
spolu s odpovídajícím :guilabel: „Štítkový vzor“.

.. tip::
Po nastavení GS1 jako čárového kódu se zobrazí nabídka :menuselection:`Čárové kódy`.
Nastavení lze také zobrazit skrytým menu, které se objeví po zapnutí :ref:`rozvojového
režimu vývojáře (developer-mode). Jakmile je zapnutý, přejděte do aplikace „Vybavení“ pomocí příkazu
Konfigurace --> Menu „Čárové kódy“ a nakonec vyberte: guilabel:„Výchozí GS1
Nomenklatura.

..._barcode/operace/vytvorit-GS1-kod:

Využijte v Odoo kódy GS1
========================

Pro identifikaci produktů pomocí čárových kódů GS1 v Odoo získávají podniky „unikátní GTIN
<https://www.gs1.org/standards/get-barcodes>“ jako mezinárodně rozpoznatelný identifikátor výrobku
koupené od společnosti GS1. Tento GTIN je spojen s konkrétními produktovými detaily podle předpisů společnosti GS1
*vzor čárového kódu*. Skladba čísel a písmen vzoru čárového kódu musí odpovídat normám GS1
konvence pro přesné interpretaci globálními systémy po celou dobu dodavatelského řetězce.

Každý čárový kód začíná dvou až čtyřmístným identifikátorem aplikace.
<http://www.gs1.org/standards/barcodes/application-identifiers>“ (AI). Tento požadovaný předpon
univerzálně ukazuje, jaký druh informací obsahuje čárový kód. Odoo dodržuje pravidla společnosti GS1
identifikační údaje, které jsou podrobně popsány v seznamu standardních pravidel GS1.
<čárový kód/operační/výchozí GS1 nomenklatura>. Včetně relevantního |AI| z seznamu
umožňuje Odoo správně interpretovat štítky GS1. Většina štítkových vzorů má pevný počet znaků
požadavky, například čísla a sériová čísla, mají proměnnou délku.

.. tip::
Pro pružné délky čárových kódů, které nejsou umístěny na konci GS1 čárového kódu, použijte FNC1.
separátor (\`\\x1D\`) k ukončení čárového kódu.

Příklad: Vzor čárového kódu pro sériové číslo je dlouhý 20 znaků. Namísto vytváření
20ti znakový čárový kód s pořadovým číslem, například „LOT00000000000000001“, použijte oddělovač FNC1
kratší: „LOT001\x1D“.

Viz seznam GS1 názvů produktů v souboru :ref:`<barcode/operations/default-gs1-nomenclature-list>`.
kompletní seznam všech vzorů čárových kódů a pravidel, které je třeba dodržovat. Jinak se podívejte na odkaz:
Dokumentace k používání GS1 <barcode/operations/gs1_usage> pro konkrétní příklady kombinování GTIN s produktem
informace a konfigurace práce s dokumenty.

.. viz též:
   - :ref:`Průběh sériových čísel <barcode/operations/gs1-lots>`
   - :ref:`Nepřevoditelné množství <barcode/operations/quantity-ex>`

.._čárový kód/akce/vytvořit nové pravidlo:

Vytvořte pravidla
------------

GS1 pravidla jsou specifický formát informací obsažených v čárovém kódu začínající znakem |AI|
obsahující definovanou délku znaků. Skenování GS1 čárových kódů ze seznamu :ref:`výchozího
<barcode/operations/default-gs1-nomenclature-list> automaticky vyplní odpovídající údaje v Odoo
databáze.

Přidání pravidel čárového kódu GS1 do Odoo zajišťuje přesné interpretaci jedinečných neobvyklých čárových kódů GS1.
formáty.

Pro to začněte zapínat režim vývojáře a přejděte na
:guilabel:`Štítky produktů“ v seznamu:menuselection:„Aplikace skladu --> Konfigurace -->
Čárový kód Nomenklatury“. Pak vyberte položku „Výchozí nomenklatura GS1“.

Na stránce „Výchozí klasifikace GS1“ vyberte v dolní části „Přidat řádek“.
tabulka, která otevírá okno pro vytvoření nového pravidla. Vnitřně se používá pole „Název pravidla“
identifikovat, co barcode znamená. Barcode:guilabel:Typy jsou různé klasifikace
informací, které lze systémem pochopit (např. produkt, množství, datum spotřeby).
balíček, kupon). Sekvence:guilabel:reprezentuje prioritu pravidla, což znamená
Čím nižší hodnota, tím vyšší je pravidlo na tabulce. Odoo sleduje sekvenční řazení
tento stůl a použije první pravidlo, které odpovídá sekvenci.
Pattern je způsob, jakým systém rozpoznává sekvenci písmen nebo čísel.
informace o produktu.

Po vyplnění informací klikněte na tlačítko „Uložit a nový“ pro vytvoření dalšího pravidla nebo
Klikněte na tlačítko „Uložit a zavřít“ pro uložení a návrat k tabulce pravidel.

... čárový kód / operace / řešení problémů

Řešení problémů s čárovými kódy
=======================

Odolnost kódu GS1 je obtížná. Zde jsou některé kontroly, které můžete zkusit, když se vám nechce pracovat s kódy
nefungují tak, jak by měly:

#Zajistěte, aby nastavení „Název štítku“ bylo nastaveno na hodnotu „Výchozí GS1
„Nomenklatura“. Přeskočte na část nastavení „Nomenklatury“
viz příslušný odkaz v části „Nastavení čárového kódu“.
#Zajistěte, aby byly ve Vašem systému Odoo zapnuty pole pro skenování čárového kódu. Například, abyste mohli naskenovat čárový kód
obsahující čísla a sériová čísla, ujistěte se, že je zapnutá funkce „Čísla a sériová čísla“
je zapnuto v nastavení Odoo a na produktu
</barcode/operations/lot-setup-on-product>.
#Odstraňte znaky interpunkce, jako jsou závorky „()“ nebo závorky „[]“, mezi :abbr:„A.I. (Aplikace
Identifikátor a čárový kód, které jsou obvykle používány pro lepší čitelnost v příkladech.
a neměla by být zahrnuta do finálního čárového kódu. Pro více informací o vytváření čárových kódů GS1
podívejte se na: „Tento oddíl“ (odkaz).
#Pokud jediný čárový kód obsahuje více kódovaných polí, Odoo vyžaduje uvedení všech pravidel.
- názvosloví čárového kódu pro Odoo, aby čtečku uměla číst čárový kód.
<barcode/operations/create-new-rules> popisuje, jak přidat nová pravidla do barcode nomenklatury.

#.Testovali jsme čárové kódy s více poli kódu, po jednom, abychom zjistili, které pole je
způsobující problém.

...... příklad::
Při testování čárového kódu obsahujícího GTIN, šaržové číslo a počet kusů začněte skenováním
|EAN| sám o sobě. Pak zkuste ověřit |EAN| s číslem šarže a nakonec zkuste skenovat celý
čárový kód.

#Po diagnostice je pole zakódované a neznámá. Přidat nová pravidla
</barcode/operations/create-new-rules> do seznamu výchozích pravidel Odoa, aby rozpoznal GS1 kódy.
jedinečné specifikace.

.... důležité::
Zatímco nový položkový kód bude čten, informace se nebude vázat na existující pole v Odoo
bez úprav vývojáře. Přidání nových pravidel je však nezbytné pro zajištění zbytku
jsou správně interpretovány pole čárového kódu.

... _čárový kód / operace / výchozí GS1 nomenklatura seznam:

Seznam GS1
=====================

Tabulka níže obsahuje seznam výchozích pravidel GS1 společnosti Odoo. Znaky čárového kódu jsou psány v
výrazy. Prvních tři pravidla vyžadují „kontrolní číslo“.
<https://www.gs1.org/services/check-digit-calculator>_ jako poslední znak.

+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
|Název pravidla||Typ||Vzor čárového kódu||Typ obsahu GS1||Odoo pole||
+=========================================+=============+==============================+====================+=======================+
|Sériové číslo kontejneru na přepravu | Balík       | (00)(\\d{18})           | Numerický identifikátor |Název balíku         |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
| Celosvětové číslo položky obchodu (GTIN) | Jednotka      | (01)(\\d{14})              | Numerický identifikátor | :guilabel:`Čárový kód` |
|                                                |Produkt      |                             |                   |Pole na produktovém formuláři
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
|Kódy obsažených obchodních položek          | Jednotka      | (02)(\\d{14})            |Numerický identifikátor | Obal             |
|                                                |Produkt     |                               |                   |                      |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
Přepravit na/doručit do světa                  |Destinace|(410)(\\d{13})              |Numerický identifikátor |Destinace            |
|místo                                     | místo         |                             |                   | místo               |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
|Loď/Dodání pro dopravu vpřed           |Destinace  |(413)(\\d{13})          |Numerický identifikátor |Zdrojová lokalita      |
|                                                |místo        |                             |                   |                      |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
Identifikace fyzické polohy                  | Poloha       |(414)(\\d{13})                |Numerický identifikátor|Poloha             |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
|Číslo šarže nebo číslo výrobní série | Šarže       | (10)          |Alfanumerický název  | Šarže             |
|                                                |            |([!%"-/0-9:-?A-Z_a-z]{0,20}) |                      |                     |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
| Sériové číslo                            | Los         | (21)                         | Alfa-numerický název | Sériové číslo       |
|                                                |            |([!%"-/0-9:-?A-Z_a-z]{0,20}) |                      |                     |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
|Datum balení (RRMMDD)                | Balení      | (13)(\\d{6})                | Datum              | Datum balení         |
|                                                |Datum       |                               |                   |                      |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
Datum spotřeby (RRMMDD)                | Datum spotřeby |(15)(číslo 6)                 | Datum              | Datum spotřeby       |
|                                                |Datum       |                               |                   |                      |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
|Datum vypršení platnosti (RRMMDD)          |Vypršení platnosti |(17)(dvoumístné číslo)|Datum              |Datum vypršení platnosti |
|                                                |Datum       |                               |                   |                      |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
Počet položek                              | Počet     | (30)(0-8)           | Měření             | Jednotky: Jednotky  |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
Počet obchodních položek                     | Množství   | (37)(\\d{0,8})              | Jednotka měření  | Množství v jednotkách
|                                                |            |                               |                     | kontejnery (AI 02)   |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
|Hmotnost netto: kilogramy (kg)          | Množství     |(310[0-5])(\\d{6})           | Jednotka           |Množství v kg           |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
|Délka v metrech (m)                          |Počet       |(311[0-5])(\\d{6})           |Měření           |Kusy v m             |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
| Celkový objem: litry (l)             | Množství   |(315[0-5])(\\d{6})          | Jednotka         |Množství v l           |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
| Celkový objem: metrů krychlových (m³)  | Množství   |(316[0-5])(\\d{6})                 | Jednotka           | Množství v m³      |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
|Délka v palcích (v palcích)              |Množství     |(321[0-5])(\\d{6})          |Měření             |Množství v palcích      |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
Hmotnost/objem: unce (oz)                   | Množství     |(357[0-5])(\\d{6})          |Měření         |Kusy v uncích           |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
| Celková objemná hmotnost: stopa krychlová (ft³) | Množství    |(365[0-5])(\\d{6})           | Jednotka       |Množství v ft³     |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
|Typ obalu                                    |Obaly       |(91)               |Názvy alfanumerické |Typ balení           |
|                                               |Typ          |([!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_a-z]{0,90})|                   |                     |
+-----------------------------------------+-------------+------------------------------+--------------------+-----------------------+
