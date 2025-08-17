============================
Nomenklatura čárových kódů v základním nastavení
============================

.. |UPC| nahradit za: zkratku „UPC (Univerzální kód výrobku)“
.. |EAN| nahradit za: zkratka: `EAN (European Article Number)`
.. |EAN| nahradit za: zkratku: EAN (Global Trade Item Number)
.. |GTINy| nahradit za: :abbr:`GTINy (globální čísla položek obchodu)`

*Nomenklatury čárových kódů* definují, jak jsou čárové kódy rozpoznávány a zařazovány do kategorií. Když je
Pokud je skenován, je spojen se **prvním** pravidlem s odpovídajícím vzorcem. Syntaxe vzorku
jejichž názvy jsou uvedeny v seznamu názvů společnosti Odoo pomocí regulárního výrazu, a je úspěšně přečten čárový kód
Odoo, pokud jeho předpona a/nebo délka odpovídá definici v pravidlech čárového kódu.

Příkladem je například stanice prodeje na místě (viz. Point of Sale)
čárové kódy v evropském čísle výrobku (EAN), které začínají na „21“ a mají pět číslic
určují hmotnost a slouží k vážení produktů a generování čárového kódu s vyobrazením hmotnosti.
cena. Znak „21“ a pětimístné číslo je vzor kódu, který se používá k identifikaci kódu a může být
aby se Odoo správně vykládal na všechny druhy čárových kódů používané v podnikání.

.. poznámka::
Provozovatelé skladů také často používají aplikace **Sklad** a **Čárový kód** společnosti Odoo.

Odoo podporuje čárové kódy EAN, Univerzální produktový kód (UPC) a :doc:`GS1 <gs1_nomenclature>
formáty. Tento dokument se zaměřuje výhradně na :ref:`výchozí pravidla a vzory v Odoo
„<čárový kód/operační/výchozí nomenklatura/seznam>“, které používají kódování UPC a EAN.

.. důležité::
Pro použití čárových kódů UPC a EAN pro jednoznačnou identifikaci produktu po celé dodavatelské řadě
Tyto kódy **musí být zakoupeny u společnosti GS1 <https://www.gs1.org/standards/get-barcodes>.

V Odoo lze definovat vlastní šablony čárových kódů, které umožňují rozpoznat čárové kódy specifické pro danou společnost.
Pokud se kódy používají jen uvnitř firmy, například v rámci interních procesů, nemusí být zakoupeny.
:ref:`příkladu <barcode/operace/hmotnost-produktu>`, kde je kód zapsán v EAN
formátu.

Konfigurace
=============

Pro použití výchozího názvosloví přejděte na:
Nastavení“. V sekci „Štítkový kód“ zaškrtněte políčko „Skenování štítku“.
Tímto způsobem se do databáze nainstaluje aplikace Barcode.

Poté v poli „Kódování názvu“ zkontrolujte, že je nastaveno „Výchozí kódování“.
Vyberte požadované položky a klikněte na tlačítko „Uložit“.

.. obrázek:barcode_nomenclature/enable-nomenclature.png
:align:center
:alt:Povoleno nastavení čárového kódu s výchozím systémem klasifikace zboží.

S moduly Barcode a výběrem Default Nomenclature se zobrazí
akce s čárovými kódy pomocí |UPC| a |EAN|, podrobně popsané v seznamu standardních názvů
<čárový kód/operační/výchozí nomenklatura>“, jsou k dispozici pro použití. A výchozím nastavením je Odoo
automaticky provádí konverzi UPC / EAN.

... _čárový kód/operaci/hmotnost produktu:

Příklad: hmotnost výrobku čárový kód
===============================

Chcete-li lépe pochopit, jak je používána nomenklatura čárových kódů k identifikaci produktů v Odoo, tento příklad
kde se používají čárové kódy s hmotností produktu v formátu EAN, aby bylo možné provést:
podnikání pro automatické tisknutí čárových kódů a výpočet ceny
Použijte hmotnost předmětu.

Pro nastavení čárových kódů pro zvážené produkty se používá následující pravidlo:

.. seznam tabulkový::
:hlavičkové řádky: 1

   * -Název pravidla
     - Vzor čárového kódu
     - Soubor v Odoo
   * -Třímístné čárové kódy s hmotnostním označením
     - 21. ... {NNDD}
     - :guilabel:`Čárový kód“ pole na formuláři produktu

.. příklad::
Pro lepší pochopení vzorce čárového kódu pro vážené produkty se podívejte na čárový kód
   `2112345000008`:

   - „21“: kód, který tento produkt označuje jako zboží s váhou.
   - „12345“: pět číslic (označených „…“ v tabulce výše), které identifikují produkt.
   - „00000“: pět číslic (označených v tabulce znakem {NNDDD}) znázorňujících hmotnost
produktu. Na formuláři produktu musí být pět hodnot s váhou **nula nula nula nula nula**. První dvě číslice
jsou celočíselné hodnoty a poslední tři číslice jsou desetinná čísla. Například „13.5
v formátu {NNDDD} je 13500.
   - „8“: „kontrolní číslo <https://www.gs1.org/services/check-digit-calculator>“ pro „211234500000“.

Ve spojení tvoří tyto složky 13místný čárový kód EAN.

Pro konfiguraci čárového kódu produktu „Bolognese“ pro vážené výrobky je nutné zadat EAN
„2112345000008“ je zadáno do pole „Čárový kód“ na formuláři produktu (přístupné přes
Přejít do aplikace „Nastavení“ -> „Zboží“ -> „Zboží“ a vybrat požadované.
produktu). Dále je nastaveno pole „Jednotka měření“ na hodnotu „kg“.

.. obrázek:: barcode_nomenclature/barcode.png
:align:center
:alt:Čárový kód na formuláři produktu.

Další krok spočívá v tom, že se váží miska těstovin s hmotností 1,5 kg. Vytvoří se tak nový čárový kód pro
těstoviny podle hmotnosti: „211234501500“, které mají kontrolní číslici „2“. Nový kód
je „2112345015002“.

.. obrázek: barcode_nomenclature/weighted-barcode.png
:align:center
:alt:Vytvořený čárový kód, který zahrnuje hmotnost 1,5 kg.

Zajistěte správné skenování produktů, přejděte na: `Barcode app --> Operations`.
Dále klikněte na jakýkoliv typ operace, například „Přijaté faktury“. Pak klikněte na tlačítko „Nový“
Vytvořit návrh pohybu zásob. Skenujte čárový kód s hmotností produktu, například „2112345015002“, a pokud je
při zadání správného čárového kódu se objeví požadovaný produkt.

.. obrázek: barcode_nomenclature/barcode-scan.png
:align:center
:alt:Zobrazení úspěšně naskenovaného čárového kódu.

Vytvořte pravidla
============

.. důležité::
Přidání nových pravidel je nutné pro formáty |UPC| a |EAN|, které nejsou v Odoo ve výchozím nastavení.
listu, protože čárové kódy nelze úspěšně přečíst, pokud jsou neznámé pole.

Zatímco nová pravidla mohou být vytvořena, pole Odoo nebudou automaticky vyplněna informacemi z těchto
pravidla. „Konfigurace na míru <https://www.odoo.com/appointment/132>`_ je pro tento typ
funkčnost.

Chcete-li vytvořit pravidlo, nejprve zapněte režim vývojáře (:ref:`developer mode <developer-mode>`). Poté přejděte na
Vyberte v menu „Aplikace inventáře“ – „Konfigurace“ – „Čárové kódy“.
:guilabel:`Výchozí nomenklatura“.

Na této stránce můžete konfigurovat následující volitelná pole:

- :guilabel:`Konverze UPC/EAN“: určuje, zda se automaticky převede na čárový kód |UPC|/|EAN|
Převod se provede při shodě pravidla s jiným kódováním. Mezi možnosti patří například:
„Výchozí možnost“), „Nikdy“, „EAN-13 do UPC-A“ a „UPC-A do EAN-13“.
- :guilabel:`Je GS1 nomenklatura“: ujistěte se, že tuto políčko nezaškrtnete, protože
:guilabel:`Výchozí nomenklatura“ používá kódování |UPC| a |EAN|, nikoli GS1.

.. obrázek: barcode_nomenclature/rule-config.png
:align:center
:alt:Nastavení políček stránky s výchozím názvoslovím.

Na stránce „Výchozí nomenklatura“ klikněte na „Přidat řádek“ v dolní části.
tabulka, která otevře okno s názvem „Vytvořit pravidlo“.

Vnitřně slouží k identifikaci, co barcode znamená.

Klíčové slovo Sekvence představuje prioritu pravidla, tedy čím menší hodnota,
Čím výše je pravidlo na stole, tím větší má váhu.

Značková pole „Typ“ reprezentují různé třídění informací, které mohou být
pochopitelné systémem (např. :guilabel:`Soubor`, :guilabel:`Dávka“, :guilabel:`Místo“
:guilabel:Slevový kupón, atd.

Pole „Kódování“ určuje, jaký kód používá čárový kód. Tato pravidla se vztahují jen na
Pokud se používá tento konkrétní kódování. K dispozici jsou následující možnosti :guilabel:`Encoding`:
:guilabel:`EAN-13“, :guilabel:"EAN-8", :guilabel:"UPC-A" a :guilabel:"GS1-28".

Značková pole „Štítkový vzor“ představují způsob, jakým se písmena nebo číslice řadí.
uznávané systémem jako obsahující informace o produktu. Někdy se stává, že pokud je určité množství
počtu číslic je nutné zadat počet teček. Znak „N“ znázorňuje celá čísla a „D“
zastupují desetinná čísla.

.. příklad::
„1…“ představuje libovolný čtyřmístný počet začínající číslem 1. „NNDD“ představuje dvouciferné číslo
s dvěma desetinnými místy. Například číslo 14.25 je 1425.

Po vyplnění informací klikněte na tlačítko „Uložit a nový“ pro uložení pravidla.
neprodleně začít vytvářet další pravidlo. Nebo klikněte na tlačítko „Uložit a zavřít“ pro uložení pravidla a
vrátit se k stolu pravidel.

... _čárový kód/operační činnosti/výchozí nomenklatura:

Nomenklatura výchozího seznamu
=========================

Tabulka níže obsahuje seznam výchozích pravidel pro nomenklaturu společnosti Odoo.
napsané v regulárních výrazech.

.. seznam tabulkový::
:hlavičkové řádky: 1
:prázdné sloupky: 1

   * -Název pravidla
     - Typ
     - Kódování
     - Vzor čárového kódu
   * - Cena: 2 desetinná místa
     - Zboží s cenou
     - EAN-13
     - 23......{NNNDD}
   * - Slevové kódy
     - Sleva na produkt
     - Každý
     - 22{NN}
   * - Hmotnost včetně tří desetinných míst
     - Vážený produkt
     - EAN-13
     - 21......{NNDDD}
   * - Kódy zákazníků
     - Klient
     - Každý
     - 042
   * - Slevové kupony a dárkové poukazy
     - Slevový kupón
     - Každý
     - 043|044
   * - Pokladní s čárovými kódy
     - Pokladní
     - Každý
     - 041
   * – Kódy umístění
     - Lokalita
     - Každý
     - 414
   * - Kódy balení
     - Balíček
     - Každý
     - PACK
   * – šarže čárových kódů
     - Lot
     - Každý
     - 10
   * -Magnetická kreditní karta
     - Kreditní karta
     - Každý
     - %.*
   * - Produktové čárové kódy
     - Jednotka produktu
     - Každý
     - .*

.. poznámka::
Když je v znakovém vzoru :guilabel:`Barcode Pattern` zástupný znak „.*“, znamená to, že může obsahovat jakýkoliv počet nebo typ čárových kódů.
postavy.

.. viz též:
:doc:`gs1_nomenklatura“
