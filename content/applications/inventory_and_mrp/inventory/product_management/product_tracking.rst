Zobrazit obsah
:skrýt obsah stránky:

================
Sledování produktů
================

„Sériové číslo“ a „číslo šarže“ jsou dvě metody, jak identifikovat a sledovat produkty v Odoo. Zatímco
podobností mezi oběma metodami existují také významné rozdíly, které ovlivňují
faktury, dodací listy a skladové záznamy.

Hvězdička obvykle označuje konkrétní dodávku zboží, které bylo přijato, je skladováno nebo bylo
Odeslané z skladu. Může se však také vztahovat na sérii výrobků vyrobených interně.
Ano, také.

„Sériové číslo“ je jedinečný identifikátor, který se přiřazuje postupně (nebo sekvence) k položce nebo
produkt, který jej odlišuje od ostatních výrobků nebo služeb.

.. viz též:
   - :doc:`produkt/sledovani-skupin-zbozi``
   - :doc:`produktové sledování/sériové číslo“

Zapněte položky a sériové čísla
============================

Pro sledování produktů pomocí čísla šarže a výrobního čísla je nutné použít funkci
Zapnuto.

Pro toto nastavení přejděte na aplikaci „Nastavení“ v nabídce „Inventář“ --> „Konfigurace“ --> „Základní nastavení“, kde se nachází
sekci „Sledovatelnost“ a zaškrtněte políčko vedle „Čísla šarží“.
Poté klikněte na tlačítko „Uložit“ pro uložení změn.

.. obrázek: produkt_sledování/nastavení_aktivace_rozdilu.png
:align:center
:alt:V nastavení skladu se nachází funkce pro sériová čísla a šarže.

Jaké jsou výhody a nevýhody lotů
================

Lot je užitečný pro produkty, které se vyrábějí nebo přijímají ve velkém množství, například oblečení.
nebo potraviny. Jejich množství je možné využít k vytvoření stop po produktu, což je zvláště užitečné při
řízení výrobku v případě jeho stažení nebo vypršení platnosti.

.. příklad::
.... obrázek: produkt_sledování/rozdíly_lokace.png
:align:center
:alt: Vytvořil položku s množstvím produktů v ní.

Výrobci přiřazují čísla šarží skupin výrobků, které mají společné vlastnosti. To může vést k
více položek sdílející stejný číslo šarže. To pomáhá identifikovat více produktů na jednom
skupina a umožňuje sledovatelnost produktů od začátku až do konce v každém kroku jejich života.
cykly.

Kdy použít sériové číslo
==========================

Cílem přiřazování sériových čísel jednotlivým výrobkům je zajistit, aby každý produkt měl svou historii.
identifikovatelné, když prochází dodavatelským řetězcem. To může být zvláště užitečné při
výrobci, kteří poskytují pozáruční servis související s prodejem a dodávkou výrobků.

.. příklad::
.... obrázek: produkt_sledování/rozdil-serii-cisel.png
:align:center
:alt: Seznam sériových čísel produktu.

Sériové číslo může obsahovat různé druhy znaků: číslice, písmena a další typografické symboly.
symboly nebo směs všech tří typů.

Sledovatelnost
============

Výrobci a společnosti mohou odkazovat na zprávy o stopě, aby viděli celý životní cyklus produktu.
produktu. Tyto zprávy obsahují důležité informace, jako například odkud pochází (a kdy) a kde byl
ukládána a komu byla zaslána.

Pro zobrazení celé trasovací historie produktu nebo pro seskupování produktů podle šarží a sériových čísel přejděte na
Vyberte v nabídce „Aplikace inventáře“ -> „Produkty“ -> „Sériová čísla“. To zobrazí
Dashboard „Sériové číslo“.

Od tady se pak zobrazují výrobky s čísly šarží nebo sériovými čísly, které jsou přiřazeny k produktům.
Mohou být také rozšířeny, aby ukázaly, které čísla nebo sériová čísla byly jim přiděleny.

Pro seskupení podle sériových čísel nebo skupin nejprve odstraňte veškeré výchozí filtry z vyhledávacího pole.
v pravém horním rohu. Pak klikněte na „Skupina podle“, vyberte možnost „Přidat vlastní skupinu“ a
zobrazí malé rozbalovací menu. V tomto malém rozbalovacím menu vyberte: „Číslo šarže / číslo výrobku“.
a klikněte na tlačítko „Použít“.

Tím se zobrazí všechny existující položky a sériové čísla a každá může být rozšířena na celý produkt.
kvantitativní hodnoty s tímto přiřazeným číslem. U jedinečných sériových čísel, která nejsou znovu používána, by
*jenom* jeden produkt na jedno sériové číslo.

.. obrázek: produkt_sledování/rozdíly_sledování.png
:align:center
:alt:Stránka s přehledem položek a číselných řad.

.. tip::
Pro další informace o konkrétním čísle sériového čísla nebo čísle položky klikněte na řádek
položka pro číslo nebo sériové číslo, které odhalí konkrétní číslo:
:guilabel:`Sériové číslo“ formulář. Z tohoto formuláře klikněte na položku „Lokalita“.
:guilabel:`Sledovatelnost“ chytré tlačítko, které zobrazí všechny položky skladu s daným číslem výrobku.
zde najdete i operace provedené s tímto číslem nebo sériovým číslem.

..toctree::


sledování produktů/sériové číslo
produktové sledování / šarže
product_tracking/přidělení
product_tracking/datumy_spotřeby

