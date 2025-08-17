=================================================
Dodání: nakupujte a prodávejte akcie bez vlastnictví
=================================================

Většinou se v skladu firmy nacházejí buď výrobky zakoupené u dodavatelů nebo
Vyrábějí se vlastními silami. Obchodníci však někdy dovolují společnostem skladovat a prodávat produkty
Ve skladu společnosti bez nutnosti zakoupit tyto položky předem. Tento způsob se nazývá
*dodávka*.

Dodání na sklad je užitečným způsobem pro dodavatele, jak zahájit nové produkty a snadno je doručit svým
zákazníky. Je také skvělý způsob, jakým si společnost uchovávající produkty (příjemce) může přivydělat
za jejich úsilí něco dostat. Přepravci si mohou za pohodlí skladování účtovat poplatek
produktů, které ve skutečnosti nevlastní.

Povolit nastavení zásilky
==============================

Pro přijímání, skladování a prodej konzignačního zboží je třeba funkci zapnout v nastavení.
to udělejte, přejděte na: „Nastavení“ -> „Konfigurace“ -> „Nastavení“, a pod
V části „Sledovatelnost“ zaškrtněte políčko vedle „Dodávka“ a klikněte na
:guilabel:`Uložit“ pro ukončení.

.. obrázek: vlastní_soubor/vlastni_soubor-povoleni-konzignace.png
:align:center
:alt:Povolení nastavení konzignace v konfiguraci skladu.

Přijmout a skladovat dodací zásoby
=====================================

S funkcí v Odoo lze nyní přijmout do skladu konzignační zásoby.
Hlavní nabídka „Sklad“ – klikněte do sekce „Příjmy“. Pak klikněte
:guilabel:`Vytvořit“.

.. poznámka::
Skladová zásoba není ve skutečnosti zakoupena od dodavatele, pouze přijata a uskladněna.
Proto se v případě přijetí zásilky nejedná o citaci ani objednávku.
takže každá přijatá faktura zboží bude začínat vytvářením ručně vystavených dokladů.

Vyberte dodavatele do pole „Odesílat od“ a poté vyberte stejného dodavatele do
zadejte do pole „Přiřadit vlastníka“.

.. důležité::
Protože produkty dodané od dodavatele budou vlastnit stejný dodavatel,
:guilabel:`Odeslat od“ a :guilabel:`Přidělit vlastníka“ musí shodovat.

Jakmile jsou nastaveny položky související s dodavatelem, vložte produkty do řádku „Produkt“ a nastavte
množství, které bude přijato do skladu pod sloupcem „Dokončeno“. Pokud je
Pokud je funkce „Jednotky měření“ zapnutá, lze změnit jednotku měření.
stejně tak. Jakmile bude přijato všechno skladové zboží, „Zkontrolujte“ fakturu.

.. obrázek: vlastní_foto/vlastni_fotografie_prijmovych_poli.png
:align:center
:alt:Soulad polí dodavatele při vytváření příjemky zásilky.

Prodat a dodat zásoby na objednávku
==================================

Jakmile je zboží přijato do skladu, může být prodáno stejně jako jakékoliv jiné.
Skladové zboží, u něhož je v kartě produktu zapnutá možnost „Může být prodáno“.

Pro vytvoření objednávky přejděte do aplikace „Prodej“ (v menu vyberte položku „Prodej“) a z
Přehled citací, klikněte na tlačítko „Vytvořit“. Vyberte zákazníka, do kterého chcete vstoupit.
:guilabel:`Zákazník“ pole.

.. poznámka::
Klient musí být odlišný od dodavatele, který mu zboží dodal.
přijatá a uskladněná dodávka v skladu.

Přidejte produkt zásilky do sloupce „Produkty“ v objednávkových liniích a nastavte
„Množství“ a vyplňte ostatní důležité informace o produktu v poli. Jakmile
citace je ukončena, klikněte na „Potvrdit“.

.. obrázek: vlastní_sklad/vlastní_sklad_objednávka_na_prodej.png
:align:center
:alt:Prodejní objednávka skladových zásob.

Jakmile je cenová nabídka potvrzena, stává se z ní objednávka na prodej. Zde mohou být produkty
dodaná kliknutím na tlačítko „Doručení“ a výběrem možnosti „Zkontrolovat“.
k ověření dodání.

Sledovatelnost a hlášení skladových zásob
===============================================

I když zásoby jsou vlastnictvím dodavatele a ne skladovací společnosti
Ve skladu se stále objeví určité položky zásilky v některých inventárních zprávách.

Pro zobrazení záznamů o inventarizaci přejděte na: „Inventář -> Zprávy“ a vyberte si zprávu.
pohled.

.. poznámka::
Protože příjemce nefyzicky vlastní zboží, které převzal, tak tyto produkty nejsou ve skladu.
v zprávě o hodnotě akcií a nemají vliv na skladové zásoby příjemce.
ocenění.

Hlášení o pohybu zboží
--------------------

Pro zobrazení všech informací o pohybech skladových zásob přejděte na „Pohyby produktů“.
přejděte na: „Skladové zásoby -> Zprávy -> Pohyb produktů“. Pro dodání
produktů je tato zpráva stejná jako u jakéhokoli jiného produktu: historie jeho
Pohyby produktů lze prohlížet; dokumenty „Dokončeno“ a „Referenční číslo“
Dostupné; a také jejich :guilabel:„Lokace“ jsou dostupné. Skladové zásoby budou
pocházejí z:guilabel:Partner Location/Vendor.

.. tip::
Chcete-li zobrazit pohyby produktu v dodávce podle vlastnictví, vyberte filtr :guilabel:`Skupina`.
Vyberte parametr „Přidat vlastní skupinu“ a poté vyberte možnost „Od majitele“.
:guilabel:`Aplikovat“ pro dokončení.

.. obrázek: vlastní_majetek/vlastni-majetek-pohyby-historie.png
:align:center
:alt:Historie pohybu skladových zásob.

.. tip::
Pro zobrazení předpokládaných jednotek skladových zásob přejděte na: „Sklad --> Zprávy -->
Prognóza zásob.

Zpráva o zásobách
--------------------

Zobrazte si přehled „Skladové zásoby“ kliknutím na „Nastavení skladu“ a poté na „Inventář“.
Zpráva o inventuře --> Zpráva o inventuře. Ze zprávy lze zjistit všechny položky skladu
Dále se zobrazují množství na jednotlivých skladech. U dodavatelských produktů se
Sloupec „Vlastník“ bude obsahovat vlastníka těchto produktů nebo původního dodavatele.
Kdo produkty dodal v první řadě.
