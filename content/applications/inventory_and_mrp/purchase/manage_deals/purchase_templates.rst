==================
Nákup šablon
==================

.. |Pts| nahradit:: Nákup šablon
.. |pt| nahradit: vložit šablonu
.. |RFQ| nahradit za: zkratku: RFQ (žádost o nabídku)
.. |RFQs| nahradí za: :abbr:`RFQs (žádosti o nabídku)“

„Nákupní šablony“ jsou typem smlouvy, který umožňuje opakované vytváření požadavků na
cenové nabídky pro opakované nákupy. Produkty pak lze přidat a změnit jejich množství.
podle potřeby. |Pts| lze použít pro více dodavatelů, což šetří čas a zjednodušuje proces poptávky.

Výjimkou jsou „plošné objednávky“, které se liší od „objednávek na přikrývku“ v tom, že „objednávka na přikrývku“ je velká objednávka
na několik dodávek, proto musí být všechny RFQ pro stejného dodavatele. PT mohou být
je kopírována pro více dodavatelů a může přenášet kvantity, což je užitečné při časté
objednávek.

Konfigurace
-------------

Nejprve přejděte na: „Koupit aplikaci -> Konfigurace -> Nastavení“. Pod
V sekci „Objednávky“ zaškrtněte políčko „Kupní smlouvy“. Klikněte
:guilabel:`Uložit“ k uložení změn.

.. obrázek: zakoupit šablony/smlouvy o nákupu - nastavení.png
:alt: Kupní smlouvy v aplikaci Nákup.

Vytvořit nový vzor
---------------------

Navigujte na :menuselection:`Koupit aplikaci --> Objednávky --> Kupní smlouvy“ a klikněte na :guilabel:`Nový“.

Z rozevírací nabídky vyberte „Dodavatele“.

..tip:
Chcete-li tento vzor používat s více dodavateli, nechte pole „Dodavatel“ prázdné.
prázdné.

V poli „Typ smlouvy“ vyberte možnost „Šablona kupní smlouvy“.

Přesvědčte se, že informace v ostatních polích jsou správné, případně je aktualizujte.

Na záložce „Produkty“ klikněte na „Přidat řádek“, vyberte požadovaný produkt.
Aktualizujte pole „Množství“ a nastavte cenu za jednotku.

.. důležité:
Při přidávání produktů do nové objednávky nejsou použity předchozí ceny.
automaticky přidány do produktových řad. Ceny **musí** být ručně přiřazeny, a to
změnou hodnoty v sloupci „Cena za jednotku“ na dohodnutou cenu s uvedeným
V opačném případě zůstane cena na nule.

Po přidání všech potřebných produktů klikněte na tlačítko „Potvrdit“.

Vytvořte novou poptávku z nákupního šablony
=========================================

Po potvrzení poptávky lze nové nabídky vytvářet přímo z poptávkového formuláře.
Tento formulář je předvyplněn informacemi na základě pravidel nastavených v tomto formuláři. Dále
citace jsou automaticky propojeny s tímto |pt| tvarem přes ikonu :icon:`fa-list-alt`.
tlačítko „RFQs/Objednávky“ v horní části formuláře.

Chcete-li vytvořit novou nabídku, klikněte na tlačítko „Nový“
Citace. To otevře novou |RFQ|, která je předvyplněná správnými informacemi v závislosti na
Nastavení na formuláři |pt|.

Pokud nebyl na |pt| identifikován dodavatel, vyberte si z nabídky v seznamu :guilabel:`Dodavatele`.
Přidání produktů do RFQ lze provést kliknutím na tlačítko „Přidat produkt“ v sekci „Produkty“.
tabulka. Chcete-li produkt odstranit, klikněte na ikonu „Odpadkový koš“ v pravém dolním rohu
produktová řada.

V nové podobě RFQ klikněte na tlačítko „Odeslat e-mailem“ a vytvořte a odešlete e-mail uvedeným
prodejce. Klikněte na tlačítko „Tisk nabídky“ pro generování tisknutelné verze PDF nabídky nebo klikněte na „Připraveno“,
Klikněte na tlačítko „Potvrdit objednávku“ pro potvrzení nákupní objednávky.

Po potvrzení objednávky se vraťte zpět na stránku s chlebem pomocí „kousků“ (breadcrumbs).
Tlačítko „RFQs/Objednávky“ bylo aktualizováno tak, aby zobrazovalo potvrzenou objednávku.

.. obrázek:: kupni_vzory/rfq-smart-button.png
:alt:Chytrý tlačítko RFQ na nákupním šabloně.
