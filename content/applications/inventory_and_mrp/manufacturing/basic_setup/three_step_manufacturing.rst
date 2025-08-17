========================
Třístupňové zpracování
========================

... výroba/výrobní management/dvoufázová výroba
.. |BOM| nahradit za: zkratka: `BoM (Bill of Materials)`
.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`

Odoo *Manufacturing* umožňuje uživatelům vyrábět produkty pomocí jednoho, dvou nebo tří kroků.
třístupňová výroba, Odoo vytváří převod komponentů, výrobní objednávku (MO) a
sklad dokončených výrobků, přenosy a aktualizace zásob podle počtu součástek
a vznikly hotové výrobky.

..tip:
Počet kroků použitých při výrobě je nastaven na úrovni skladu, což umožňuje každému
sklad, použijte jiný počet kroků. Chcete-li změnit počet kroků pro konkrétní
skladu začněte tím, že se přesunete na: „Sklad --> Konfigurace --> Sklady“.
a poté vyberte sklad z obrazovky :guilabel:`Skladové prostory`.

Na kartě „Konfigurace skladu“ najděte v poli „Způsob výroby“ volbu „Výroba“.
pole a vyberte jednu ze tří možností: „Výroba (1 krok)“, „Odebrat“ nebo „Upravit“.
komponenty a pak je vyrobit (2 kroky)“, nebo „Vyberte komponenty, vyrobte je a pak
skladovat produkty (3 kroky).

.... obrázek: třístupňová výroba/výrobní typ.png
:srovnání: do středu
:alt: Políčko pro vstup do rádiového vysílání na stránce konfigurace skladu.

.. důležité::
Produkty musí být správně nakonfigurovány, než mohou být vytvořeny v Odoo. Pro podrobnosti o tom, jak
pro více informací se podívejte na dokumentaci k nastavení výrobku.
<výroba/správa/konfigurace výrobku>.

Vytvořit výrobní objednávku
==========================

Chcete-li vytvořit výrobek pomocí Odoo Manufacturing, začněte tím, že se přesunete na
:menuselection:`Výroba -> Provoz -> Výrobní objednávky“ a pak klikněte
:guilabel:`New` vytvořit nový |MO|.

V novém |MO| vyberte produkt, který chcete vytvořit z nabídky „Produkty“ v rozevíracím seznamu.
:guilabel:`Seznam materiálů“ pole automaticky vyplní s asociovaným seznamem materiálů (BoM).

Pokud je pro produkt vytvořeno více než jedno BOM, konkrétní BOM lze vybrat v
:guilabel:„Seznam materiálů“ pole a pole „Produkt“ se automaticky vyplní
související produkt.

Po výběru BOM se zobrazí karty „Součásti“ a „Dodávky“.
automaticky doplnit komponenty a operace uvedené na BOM. Pokud jsou k dispozici další komponenty nebo
Pro konfiguraci |MO| jsou potřebné operace, přidejte je do :guilabel:`Komponenty`.
Klikněte na „Přidat řádek“ v záložce „Dodací lístky“.

Konečně klikněte na tlačítko „Potvrdit“ pro potvrzení |MO|.

Přenos komponent procesu vybírání
================================

Po potvrzení třístupňového |MO| se v horní části obrazovky zobrazí tlačítko „Převody“.
stránku. Klikněte na ni, abyste byli přesměrováni na stránku „Převody“ pro |MO|. Na této stránce jsou uvedeny dva
převody: *WH/PC/XXXXX* (přenos komponent,) a *WH/SFP/XXXXX* (skladování dokončených součástek).
přenos produktů).

Vyberte: guilabel: `WH/PC/XXXXX`, abyste otevřeli přenos komponent pro |MO|. Tento přenos je
slouží k sledování pohybu komponent od skladovacích míst ke skladovacímu místu
Kde se používají k výrobě produktu.

Po přesunutí komponent do jejich skladovacího místa klikněte na tlačítko „Přijmout“.
výše převodu, následovaná tlačítkem „Použít“ na okně „Okamžitý převod?“.
okno, které se objeví. Tímto způsobem je přenos označen jako „Dokončeno“ a aktualizuje počty zásob
odrážet množství přenesených součástek.

Nakonec se vraťte na stránku MO kliknutím na „breadcrumb“ s názvem WH/MO/XXXXX nahoře.
stránka.

.. obrázek: třístupňová výroba/pšeničná mouka.png
:align:center
:alt:Výrobní objednávka chleba přesouvá komponenty na paletě.

Dodací objednávka procesního výrobce
===========================

MO se zpracovává dokončením všech pracovních úkolů uvedených pod jeho štítkem „Pracovní úkoly“.
tabulku. Toho lze dosáhnout přímo na samotné |MO| nebo z pohledu pracovního příkazu.

Základní průběh
--------------

Pro dokončení pracovních příkazů od MO začněte tím, že se přesunete na :menuselection:`Výroba
→ Výrobní operace → Zadání výroby“ a poté vyberte zadání výroby.

Na stránce „Úkoly“ vyberte záložku „Úkoly“. Jakmile začne pracovat první úkol
které ještě není dokončeno, klikněte na tlačítko „Začít“ pro příslušný pracovní úkol.
Poté začne časovač, který sleduje dobu trvání práce na zakázku.

.. obrázek: třístupňová výroba/start-button-2.png
:align:center
:alt:Tlačítko pro vytvoření pracovního příkazu na výrobním příkazu.

Když je objednávka dokončena, klikněte na tlačítko „Dokončeno“ pro danou objednávku.
Tento proces je stejný pro každý pracovní příkaz uvedený na záložce „Pracovní příkazy“.

.. obrázek: třístupňová výroba/dokončeno.png
:align:center
:alt:Tlačítko hotovo pro práce na výrobním příkazu.

Po dokončení všech pracovních příkazů klikněte na tlačítko „Vyrobit vše“ nahoře na obrazovce.
označte políčko |MO| jako „Dokončeno“ a zaregistrujte vyrobený produkt do zásob.

Práce na výrobní lince
-------------------

Pro dokončení pracovních příkazů pro |MO| pomocí modulu *Podlaha výroby* začněte tím, že se přesunete na
Vyberte „Výroba“ -> „Provoz“ -> „Objednávky výroby“, a poté vyberte |MO|.

Na stránce MO klikněte na záložku „Pracovní příkazy“ a poté vyberte tlačítko „↗️ (čtverec)“.
s šípem vycházejícím z ní) na řádku první pracovní objednávky, která má být zpracována.
otevře okno s informacemi o práci a možnostmi zpracování.
pořádku.

V okně s náhledem vyberte tlačítko „Otevřít výrobní plochu“ v horním levém rohu okna.
otevřít modul Shop Floor.

.. obrázek: třístupňová výroba/tlačítko na podlaze.png
:align:center
:alt:Tlačítko pro otevřenou výrobní plochu v příkazu k výrobě.

Při přímém přístupu z konkrétní objednávky v rámci |MO| je výchozí stránkou
pro pracoviště, kde se bude práce objednávat. Stránka zobrazuje kartu pro
dokument s pracovním příkazem, který zobrazuje číslo |MO|, produkt a počet kusů, které mají být vyrobeny.
kroky potřebné k dokončení pracovního příkazu.

.. obrázek: třístupňové výrobní procesy/dodací karta.png
:align:center
:alt:Příkaz k práci na stránce pracovního centra v modulu Výroba.

Dokončení práce se provádí kliknutím na každý bod uvedený v jejím pořadí.
na krok a podle pokynů uvedených v okně s upozorněním, které se objeví. Jakmile je
Dokončeno, klikněte na tlačítko „Další“ a pokračujte do dalšího kroku (pokud je vyžadován).

Alternativně lze krok pracovního příkazu dokončit kliknutím na zaškrtávací políčko vpravo.
stránce karty s pracovním příkazem. Při použití této metody je automaticky
označeno jako dokončené, aniž by se objevilo okno s upozorněním.

Posledním krokem na pracovní objednávce je položka „Zaregistruj výrobu“. Tento krok se používá k registraci
Počet vyrobených jednotek produktu. Pokud je počet vyrobených stejný jako počet
MO vzniklo pro, klikněte na tlačítko „Jednotky“ vedle řádku.
automaticky zaregistruje tuto skutečnost jako počet vyrobených kusů.

Pokud je třeba zadat jiný počet, klikněte na krok „Registrace výroby“
přechodné okno. Zadejte počet vyrobených jednotek do pole „Jednotky“ a pak klikněte
:guilabel:`Přidat číslo do seznamu“ a zaregistrujte si ho.

.. poznámka::
Krok „Výroba záznamu“ se na kartě objednávky objevuje vždy. Musí být dokončen, aby mohl být
První pracovní příkaz zpracovaný. Po provedení se zobrazí jako již dokončený.
každou zbývající objednávku v MO.

Po dokončení všech kroků pro objednávku práce se na zápatí objednávky objeví tlačítko
kartu. Pokud ještě musí být dokončeny další pracovní úkoly, aby mohl být |MO| uzavřen, tlačítko se nazývá
:guilabel:`Označit jako hotové“. Pokud nejsou další pracovní příkazy k dokončení, tlačítko je označeno
:guilabel:`Zavřít výrobu“.

Kliknutím na tlačítko „Zadat jako hotové“ se karta práce zmenší a zmizí.
úplně, stav pracovního příkazu je na |MO| označen jako *Dokončeno*, a
je zobrazen v modulu *Prodejní plocha*, na stránce pracoviště, kde je konfigurován.
Provedena. Další pracovní příkazy lze zpracovat podle pokynů uvedených v tomto
§

Kliknutím na tlačítko „Zavřít výrobu“ se karta objednávky práce zmenšuje a po zmizení
V poli MO je uvedeno hodnocení *Dokončeno* a do pole Jednotky produktu jsou zadány jednotky, které byly vyrobeny.
Inventarizaci.

Po kliknutí na tlačítko „Ukončit výrobu“ nebo „Zadat dokončené“, se každé tlačítko nahradí
Tlačítko „Zpět“. Klikněte na tlačítko „Zpět“ předtím, než se karta objednávky práce zcela vybije.
aby se pracovní příkaz neuzavřel.

..tip:
Tento oddíl popisuje základní postup zpracování |MO| v modulu Shop Floor.
Pro podrobnější vysvětlení modulu a všech jeho funkcí se podívejte na odkaz :ref:`Shop Floor
přehled dokumentace pro výrobu a podlahové plochy (shop floor).

Dokončení přenosu hotového výrobku
=================================

Po dokončení |MO| se vraťte na stránku „Převody“ objednávky kliknutím na
Tlačítko „Převody“ v horní části objednávky. Tentokrát vyberte možnost „WH/SFP/XXXXX“.
otevřít sklad s hotovými výrobky a provést převod zboží do této položky, což se používá k sledování pohybu hotových výrobků.
výrobky z místa jejich výroby na místo, kde jsou skladovány.

Po přesunu hotových výrobků do skladovacího místa klikněte na tlačítko „Zkontrolovat“.
výše převodu, následovaná tlačítkem „Použít“ v okně „Okamžitý převod?“.
okno, které se objeví. Tímto způsobem je přenos označen jako „Dokončeno“ a aktualizuje počty zásob
odrážejí množství hotových výrobků převedených na druhou stranu.
