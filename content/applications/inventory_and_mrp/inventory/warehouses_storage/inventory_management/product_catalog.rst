===============
Katalog produktů
===============

.. |SO| nahradit za: :abbr:`SO (objednávka na prodej)`
.. |SOs| nahradí za: :abbr:`SOs (objednávky na prodej)`
.. |BoM| nahradit za: :abbr:`BoM (seznam materiálů pro výrobu)“
.. |RfQ| nahradit za: zkratka: RfQ (žádost o nabídku)

Produkt *katalog* je funkcí integrovanou s jakýmkoliv aplikací Odoo, která umožňuje uživatelům přidávat produkty nebo
komponenty objednávky. To zahrnuje **Skladování**, **Výrobu**, **Prodej**, **Nákup**
a mezi nimi i aplikace **Opravy**.

Katalog produktů lze zobrazit na první záložce nabídky, poptávky (RfQ).
objednávka nebo materiálový list (BOM) v novém okně. Katalog zobrazuje
produkty a komponenty v uživatelsky přívětivém formátu POS, ze kterých lze vybírat.
přidány do formulářů.

Produktový katalog usnadňuje vytváření nových prodejních objednávek (SO) a nákupních objednávek (PO).
výrobní objednávky (MO), materiálové listy (BOM) a další, poskytuje vizuální rozhraní
Prostřednictvím kterého lze rychle vybírat produkty a komponenty.

Využijte katalog produktů
===================

Pro použití produktového katalogu začněte vytvořením nebo otevřením nabídky, objednávky nebo seznamu materiálů
jaké produkty nebo komponenty lze přidat. Například vytvořte novou nabídku na prodej kliknutím
Vyberte aplikaci „Prodej“ a klikněte na „Nový“.

Na formuláři (citace, RfQ, objednávka, BoM) zkontrolujte, že je vybrán první záložkový list na spodní liště.
Podle konfigurované podoby může být tato záložka nazvána „Řádky objednávky“, „Součásti“
*Produkty* nebo *Díly*.

Na první prázdné řádce záložky klikněte na odkaz :guilabel:`Katalog`, abyste otevřeli katalog v novém okně.
stránka.

.. obrázek: product_catalog/catalog-button.png
:align:center
:alt:Tlačítko „Katalog“ na záložce „Dodací lístky“ objednávkového formuláře.

Katalog produktů zobrazuje kartu pro každý produkt přidávaný do Odoo. Každá karta obsahuje několik klíčových
podrobnosti o odpovídajícím produktu:

- Produktová fotografie
- Název produktu
- Cena nebo náklady na produkt v závislosti na tom, zda je kupován, prodáván nebo používán jako
komponenta
- Referenční kód (např. *DESK0005*)
- Množství skladem
- Variabilní atributy (např. *Barva: Bílá*).

.. obrázek: product_catalog/product-card.png
:align:center
:alt:Karta produktu v katalogu produktů.

Produkty lze filtrovat pomocí vyhledávacího pole v horní části stránky nebo lištou na levé straně.
stránce.

K filtrování podle typu produktů klikněte na tlačítko :icon:`fa-caret-down` :guilabel:`(svislá šipka dolů)“.
v pravé části vyhledávací lišty otevřete nabídku pro vyhledávání. V sekci Filtry vyberte
filtr „Služby“ pro zobrazení pouze produktů služeb nebo filtr „Produkty“
ukázat pouze fyzické produkty.

Při vytváření nebo konfiguraci nabídky nebo SO, konkrétně filtru „V objednávce“
je zobrazena v sekci filtrů ve vyhledávacím poli. Vyberte tento filtr, abyste viděli
produkty, které již byly přidány do formuláře.

V bočním panelu na levé straně stránky vyberte možnost z ikonky
:guilabel:`KATEGORIE PRODUKTU` sekci pro filtrování podle kategorie produktu nebo možnost v
:ikonka: `fa-th-list` :guilabel: „ATTRIBUCE“ v sekci filtru podle varianty.

.. obrázek: produkt/filtr-boční.png
:align:center
:alt:Filtr v bočním panelu katalogu produktů.

Chcete-li přidat produkt, klikněte na kartu produktu nebo klikněte na ikonku „nákupní košík“ a poté na tlačítko „Přidat“.
tlačítko v pravém dolním rohu karty. Kliknutím na něj přidáte jednotku produktu, který je
v poli v levém dolním rohu karty.

Jakmile je produkt přidán, kliknutím na kartu produktu pokračuje v přidávání jednotek daného produktu.
jednotlivé kroky.

K nastavení množství přidaného produktu klikněte na tlačítko :icon:`fa-minus` :guilabel:`(minus)`
snížit množství o jednu nebo tlačítko „+“ (plus) k jeho zvýšení
jedna.

Alternativně lze zadat konkrétní množství vybráním pole mezi
tlačítka „minus“ a „plus“ a psaní
Požadované množství.

Chcete-li produkt ze seznamu objednávky nebo BoM zcela odstranit, klikněte na ikonu
Tlačítko „Odebrat“ v pravém dolním rohu karty produktu nebo klepněte na
Klikněte na tlačítko „„:icon:`fa-minus` :guilabel:`(minus)`“ až do chvíle, než se množství sníží na nulu.

.. obrázek: produkt/přidáno.png
:align:center
:alt:Karta produktu pro produkt, který byl přidán.

Po přidání požadovaného množství každé položky se vraťte na formulář kliknutím na
:guilabel:`Zpět k [X]“ tlačítko na horní části obrazovky. Toto tlačítko se liší podle typu
tvaru (citát, BoM atd.).

.. důležité::
Výrobky se objevují v katalogu produktů a lze je přidat do objednávek i když nejsou skladem.
Je nutné potvrdit množství produktu, protože je na skladě nulový počet jednotek.
Pokud je produkt přidán do objednávky, ale ve skutečnosti není k dispozici, mohou vznikat rozdíly mezi zásobami.
