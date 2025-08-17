============
Náklady na dopravu
============

.. |RfQ| nahradit za: zkratku `RfQ (Request for Quotation)`
.. |PO| nahradit za: abbr: PO (příkaz k nákupu)
.. |FIFO| nahradit: zkratka: FIFO (První do první ven)
.. |AVCO| nahradit za: zkratka: `AVCO (Průměrná cenotvorba)`

Při dodání produktů zákazníkům je poštovné součástí celkové ceny produktu nebo zásilky.
včetně všech nákladů spojených s dodáním zboží.

V Odoo se používá funkce „Dodatečné náklady“ k zohlednění dalších nákladů při výpočtu
hodnota produktu. To zahrnuje náklady na dopravu, pojištění, celní poplatky, daně a
a další poplatky.

Konfigurace
=============

Chcete-li přidat náklady na dopravu k produktům, musí být nejprve zapnutá funkce „Náklady na dopravu“.
vlastnost, přejděte na:menu:„Aplikace skladu“ -> „Konfigurace“ -> „Nastavení“, a posuňte se dolů
sekci „Ocenění“.

Zaškrtněte políčko vedle možnosti „Náklady na dopravu“ a klikněte na tlačítko „Uložit“, abyste uložili
změny.

Když stránka znovu načte, objeví se pod políčkem „Příchozí pošta“ pole „Výchozí doručená pošta“.
Náklady jsou uvedeny v sekci „Ocenění“.

Klikněte na položku „Výchozí účetní kniha“ a zobrazí se seznam účetních knih. Vyberte
jehož účetní záznamy týkající se nákladů spojených s přistáními by měly být zaznamenány.

.. obrázek:landed_costs/integrating-landed-costs-enabled-setting.png
:alt:Funkce Náklady na dopravu a výchozí pole pro účetní knihu v nastavení skladu.

Vytvořte produkt s přepravními náklady
==========================

Pro poplatky, které jsou přičítány jako náklady na dopravu, lze vytvořit produkt s náklady na dopravu.
Odoo. Tímto způsobem lze rychle přidat položku k faktuře dodavatele jako daňový doklad.
a nebylo by nutné je ručně zadávat při každém vystavení nové faktury od dodavatele.

Pro tento účel vytvořte nový produkt kliknutím na: „Inventář aplikace --> Produkty -->
Produkty“ a klikněte na „Nový“.

Přidělte produktu nákladů na dopravu název v poli „Název produktu“ (tj. „Doprava mezinárodní“)
Dodání“). V poli „Typ produktu“ klikněte na seznam a vyberte
„Služba“ jako „Druh produktu“.

.. důležité::
Prodávající musí mít v případě „vstupních“ produktů nastavenou hodnotu :guilabel:`Product Type` na :guilabel:`Service“.

Klikněte na záložku „Nákup“ a zaškrtněte políčko vedle „Je přímá cena“.
sekci „Faktury dodavatele“. Jakmile je zaškrtnuto, objeví se nové pole „Základní metoda rozdělování“
se nachází pod ním, což vyvolá výběr. Po kliknutí na tento seznam se zobrazí následující možnosti:

- :guilabel:`Rovnoměrně rozložené náklady“: rozdělí náklady rovnoměrně mezi všechny produkty uvedené na faktuře, bez ohledu
z množství každého.
- :guilabel:`Podle množství“: rozděluje náklady mezi jednotlivé kusy všech produktů na faktuře.
- :guilabel:„Podle aktuální ceny“ rozděluje náklady podle ceny jednotky produktu, takže
Výrobek s vyšší cenou dostane větší podíl na celkových nákladech.
- :guilabel:'Podle váhy': rozděluje náklady podle hmotnosti produktů v dokladu.
- :guilabel:`Podle objemu“: rozděluje náklady podle množství produktů v dokladu.

.. obrázek: landed_costs/integrating-landed-costs-landed-cost-product.png
:alt:Je v poli Základní náklady na službu a výchozí metoda rozdělení produktu typu služby.

Při vytváření nových faktur od dodavatelů lze tento produkt přidat jako položku na faktuře jako náklad na dopravu.

.. důležité::
Při aplikaci celkových nákladů na fakturu dodavatele musí produkty v původním |PO| **musí být** součástí
*Kategorie produktu* s metodou ocenění buď |AVCO| nebo |FIFO| a způsob oceňování
může být buď manuální (použití inventarizační hodnoty) nebo automatická (použití hodnoty z obchodního účetnictví).
<výpočet hodnoty zásob>.

Vytvořte objednávku k nákupu
=====================

Navigujte na:menu-selection:Koupit aplikaci --> Nová“ pro vytvoření nové žádosti o nabídku (RfQ).
Zadejte pole „Dodavatel“, přidejte dodavatele pro objednávání produktů. Pak klikněte na „Přidat
„Produkty“, pod záložkou „Produkty“ a přidejte produkty do RfQ.

Jakmile je objednávka připravena, klikněte na tlačítko „Potvrdit objednávku“ a poté na „Doručení“.
Produkty poté, co byly produkty přijaty, následuje: „Potvrdit“.

Vytvořit fakturu dodavateli
------------------

Jakmile dodavatel splní |PO| a zašle fakturu, lze vytvořit dodavatelskou fakturu z |PO|
Odoo.

Přejděte do nabídky „Nákup aplikace“ a klikněte na PO, pro které chcete vystavit fakturu.
je třeba vytvořit. Poté klikněte na „Vytvořit fakturu“. To otevře novou
stádiu návrhu.

V poli „Datum faktury“ klikněte na řádek, abyste otevřeli kalendářové menu.
datum, kdy by měla být tato návrhová vyhláška vydána.

Poté klikněte na záložku „Dodací položky“ a pod záložkou „Přidat řádek“ vyberte možnost „Vybrat z rozevírací nabídky“.
v poli „Produkt“ nabídku v seznamu produktů, které byly dříve vytvořeny. Klikněte
ikonu „Ikona cloud s šipkou“ (Cloud s šipkou) pro ruční uložení a aktualizaci
návrh zákona.

.. obrázek: landed_costs/integrating-landed-costs-checkboxes.png
:alt:Zatržítka sloupců „Náklady na dopravu“ pro produkt a náklady na dopravu.

V sloupci „Dodací náklady“ je uvedená cena produktu, který byl objednán od dodavatele.
zaškrtnuté políčko „Zemní náklady“ a zaškrtnout políčko „Nakoupený produkt“. Toto rozlišuje zemní
z ostatních nákladů uvedených na faktuře.

Dále se na vrchní části formuláře objeví tlačítko „Vytvořit náklady“.

.. obrázek:landed_costs/integrating-landed-costs-create-button.png
:alt:Vytvořit tlačítko „Náklady na dodání“ v faktuře od dodavatele.

Připočtěte náklady na dopravu
===============

Jakmile je k faktuře dodavatele přičtena poštovná, klikněte na tlačítko „Vytvořit náklady spojené s dopravou“ v horní části
faktura dodavatele.

Provedením takového kroku se automaticky vytvoří záznam o nákladech na dopravu s předvyplněným nákladem na dopravu.
produktová řada v záložce „Další náklady“.

V poli „Základní náklady“ klikněte na „Převody“ a vyberte
Která přenesenou nákladovost vlastní.

.. obrázek:landed_costs/integrating-landed-costs-transfers-menu.png
:alt:Formulář přistupné ceny s vybraným převodem faktury.

.. tip::
Kromě vytváření nákladů na pozemek přímo z faktury dodavatele lze také vytvořit záznamy o nákladech na pozemek.
vytvořit přejítím na:menu-selection:Inventář aplikace --> Provoz --> Náklady na pozemek
kliknutím na tlačítko „Nový“.

Po zadání výběru ze seznamu „Převody“ klikněte na „Vypočítat“.
(v dolní části formuláře pod položkou „Celkem“).

Klikněte na záložku „Změny ocenění“ a zobrazí se dopad nákladů spojených s přepravou.
Sloupec „Původní hodnota“ uvádí původní cenu PO a sloupec „Doplňková
Sloupec „Dodací cena“ zobrazuje dodací cenu a sloupec „Nová hodnota“ zobrazuje součet
dva, celkové náklady na projektu |PO|.

Jakmile je vše připraveno, klikněte na tlačítko „Zkontrolovat“ a zadanou položku přidejte do účetní knihy.

To způsobí, že se na horním okraji formuláře objeví tlačítko „Ocenění“. Klikněte
Tlačítko „Ocenění“ otevře stránku s oceněním produktů.
Aktualizovaná ocenění uvedena.

.. poznámka::
Pro zobrazení tlačítka „Ocenění“ při ověření produktu musí být
:guilabel:`Produktový typ“ **musí být nastaven na** :guilabel:`Skladovatelný“.

Pro zobrazení hodnoty každého produktu včetně nákladů na dopravu přejděte na
:menuvolba:„Skladové zásoby -> Hlášení - > Ocenění“.

.. poznámka::
Každá účetní položka vzniklá pro náklady na dodavatele lze zobrazit v části *Účetnictví*.
aplikace.

Pro zobrazení těchto záznamů přejděte do sekce „Účetnictví“ v aplikaci „Účetnictví“.
„Záznamy v deníku“ a najít správnou položku podle čísla (tj. „PBNK1/2024/XXXXX“).

Klikněte do záznamu v deníku, abyste viděli „Záznamy v deníku“ a další informace o
vstup.

.... obrázek:: náklady na přistání/zahrnutí nákladů na přistání do účetní záznamu.png
:alt:Formulář záznamu pro přepočet nákladů na pozemek vytvořený z faktury dodavatele.
