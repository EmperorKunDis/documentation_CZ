==================================
Správa BOM pro varianty produktů
==================================

Odoo umožňuje používat jeden nákladový list (BoM) pro více variant stejného produktu.
Souhrnný seznam materiálů pro výrobek s variantami ušetří čas tím, že zabrání
potřebu řídit více BoMů (seznamy materiálů).

Aktivujte varianty produktů
=========================

Aby se spustil funkční prvek variant produktů, přejděte do aplikace „Sklad“ na záložku:
Konfigurace --> Nastavení“, a pak v sekci „Produkty“ klikněte na
zaškrtávací políčko pro zapnutí možnosti Varianty. Poté klikněte na tlačítko Uložit a aplikovat změny.
scénář.

Pro více informací o konfiguraci variant produktu se podívejte na stránku :doc:`varianty produktů
<https://www.shoptet.cz/návody/objednávky-a-fakturace/dodací-podmínky/> dokumentaci.

.. obrázek: product_variants/product-variants-variants-settings.png
:align:center
:alt: Vybrat možnost „Varianty“ v nastavení aplikace Sklad.

Vytvořte vlastní atributy produktu
================================

Jakmile je aktivována funkce variant produktů, vytvořte a upravte atributy produktu na
Stránka „Atributy“.

Stránka „Atributy“ je přístupná buď z nabídky „Inventář aplikace“ nebo z nabídky „Inventář aplikace -->
Konfigurace --> Nastavení“ kliknutím na tlačítko „Atributy“, nebo kliknutím
:menu:„Aplikace pro inventář --> Konfigurace --> Atributy“.

Jakmile se ocitnete na stránce „Atributy“, buď klikněte do existujícího atributu nebo klikněte
Kliknutím na tlačítko „Vytvořit“ se zobrazí nový prázdný formulář pro
upravit atribut. Pro existující atribut klikněte na tlačítko „Upravit“ v jeho formuláři.
změny.

Přidělte atributu jméno v poli „Název“ a vyberte kategorii z pole „Kategorie“.
položky nabídky. Pak vyberte požadované možnosti vedle položky :guilabel:`Typ zobrazení`.
Vyberte pole „Režim vytváření variant“ a poté klikněte
:guilabel:`Přidejte řádek“ pod záložkou „Hodnota atributu“, abyste mohli přidat novou hodnotu.

..tip:
Na řádku „Hodnota“ je zaškrtávací políčko „Je vlastní hodnota“. Pokud je vybráno,
Toto hodnota bude uznána jako vlastní hodnota, která umožňuje zákazníkům zadat speciální
požadavky na úpravu při objednávání vlastní verze produktu.

Příklad:
.... obrázek: produktove-varianty/produktove-varianty-atribut.png
:srovnání: do středu
:alt: Konfigurační obrazovka pro atributy produktové varianty.

Jakmile jsou do seznamu přidány všechny požadované hodnoty, klikněte na tlačítko „Uložit“ a uložte nový
atribut.

.._produktové varianty/přidat produktovou variantu:

Přidejte varianty produktu na formulář produktu
========================================

Vytvořené atributy lze aplikovat na konkrétní variantu určitého produktu.
varianty produktu, přejděte na stránku s formulářem takto:
Produkty --> Produkty. Chcete-li změnit produkt, klikněte na tlačítko „Upravit“. Pak klikněte na
:guilabel:`Varianty“ záložka.

Pod nadpisem „Atribut“ klikněte na „Přidat řádek“, abyste přidali nový atribut.
Vyberte si jeden z nabízených možností ze seznamu.

Poté klikněte na položku „Hodnoty“ pod nadpisem „Guide Labels“ a vyberte z nabídky.
existující hodnoty. Klikněte na každou požadovanou hodnotu a opakujte tento proces pro všechny další
atributy, které by měl produkt obsahovat.

Jakmile je hotovo, klikněte na tlačítko „Uložit“ pro uložení změn.

.. obrázek: product_variants/product-variants-product-form.png
:align:center
:alt:Tabulka s variantami produktu, hodnotami a atributy.

..tip:
:zkratka:Produkty s více variantami, které vyrábíme ve vlastních dílnách
Pokud nejsou nastaveny pravidla pro přeskupení s hodnotou 0,0 nebo pokud není nastavena trasa doplňování,
*Dodání na objednávku (MTO)*

Použijte komponenty BoM u variant produktů
========================================

Poté vytvořte nový seznam materiálů (BoM) nebo upravte stávající, přejděte na
Vyberte položku „Výroba“ -> „Produkty“ -> „Součástky“. Pak klikněte
:guilabel:`Vytvořit“ otevře nové okno „Seznamy materiálů“, které je možné konfigurovat od začátku.

Přidejte produkt do seznamu položek BoM (seznam materiálů) kliknutím na rozbalovací nabídku v
Vyberte pole „Produkt“ a vyberte požadovaný produkt.

Pak přidejte komponenty kliknutím na „Přidat řádek“ pod sekcí „Komponenta“.
kartě „Komponenty“ a zvolte požadované komponenty ze seznamu.

Zvolte požadované hodnoty v poli „Množství“ a „Jednotka měření“.
sloupce. Pak vyberte požadované hodnoty v sloupci „Aplikovat na varianty“.

.. poznámka::
Možnost „Použití na varianty produktů“ k přiřazení komponent ke konkrétním variantám produktu.
:abbr:`Seznam materiálů (bill of materials)“ je dostupný pouze po aktivaci nastavení „Varianty“.
z aplikace „Soupis“. Pokud je pole „Aplikovat na varianty“ vyplněno,
nejsou hned viditelné, aktivujte je z nabídky dalších možností (tři tečky, pro přístup k
vpravo od hlavičkové řádky.

.. obrázek: product_variants/product-variants-apply-on-variants.png
:align:center
:alt:"Aplikovat na varianty" možnost v nabídce dalších možností.

Každý komponent může být přiřazen k více variantám. Komponenty bez specifikovaných variant se použijí
V každé variantě produktu. Stejný princip platí i při konfiguraci operací a
Případně i odpady.

Při definování varianty :abbr:`BoMs (seznam materiálu pro výrobu)` pomocí přiřazení komponent je
V hlavním oddíle seznamu položek „BoM“ by měl být uveden
zůstat prázdné. Toto pole se používá jen při vytváření :abbr:`BoM (seznamu materiálů)“.
Pro konkrétní variantu produktu.

Když jsou všechny požadované konfigurace provedeny v seznamu součástek (BoM), klikněte
:guilabel:`Uložit“ na vrcholu formuláře pro uložení změn.

..tip:
Pro součásti, které se vztahují pouze na konkrétní varianty, zvolte operace, ke kterým
by mělo být využito. Pokud sloupec „Využití v operaci“ není hned viditelný,
viditelné, aktivujte je z nabídky dalších možností (trojúhelníková ikona vpravo od
hlavičkové řádky).

Prodávat a vyrábět varianty produktů BoM
=============================================

Prodej a výroba variant produktů na objednávku podle seznamu materiálů (BOM):
:menuvolba:Prodejní aplikace --> Vytvořit``

Prodat variantu produktu BoM
---------------------------

Jakmile se dostanete na prázdný formulář „Citace“, klikněte na vybranou možnost vedle položky „Zákazník“
pole pro přidání zákazníka.

Poté v záložce „Řádky objednávky“ klikněte na „Přidat produkt“ a vyberte
Dříve vytvořený produkt s variantami z nabídky.
Tím se zobrazí okno „Nastavit produkt“.

V okně s náhledem klikněte na požadované atributy a konfigurujte správnou variantu.
produkt k výrobě. Pak klikněte na zelené ikonky „+“ nebo „–“ vedle čísla 1
změnit množství k prodeji a výrobě, pokud je to požadováno.

.. obrázek: product_variants/product-variants-variant-popup.png
:align:center
:alt:Nastavte dialogové okno pro výběr atributů produktu.

Jakmile jsou všechny parametry vybrány, klikněte na tlačítko „Přidat“. To změní okno na
druhé okno „Nastavení“, kde se v případě dostupnosti volitelných produktů zobrazí.
byly vytvořeny již dříve.

Jakmile budete připraveni, klikněte na tlačítko „Potvrdit“ v okně.

Poté klikněte na tlačítko „Uložit“ pro uložení všech změn a potvrďte je v horní části okna.
Formulář „Citace“ k vytvoření a potvrzení nové objednávky.

Varianta výrobku BoM
----------------------------------

Jakmile je potvrzena objednávka na prodej, objeví se tlačítko „Výroba“ v
v horní části formuláře „Prodejní objednávka“ (SO). Klikněte na tlačítko „Výroba“ chytré klávesnice.
otevřete formulář „Výrobní objednávka“.

Na tomto formuláři pod záložkou „Komponenty“ je potřeba vybrat vhodné komponenty pro zvolený
varianty jsou uvedeny. A podle variant se budou lišit i složky.
povinné nebo nepovinné kroky operace, přejděte na záložku „Pracovní příkazy“.

Pro vstup do obrazovky pracovního příkazu ve formátu tabletu klikněte na ikonku tabletu vedle
a řádit, dokud se požadovaná operace neuskuteční.

Z pohledu na tablet klikněte na tlačítko „Ukončit“ a postupujte podle pokynů pro dokončení
operační kroky.

Alternativně klikněte na tlačítko „Zadat jako hotové“ v horní části formuláře pro výrobní objednávku.
Dokončit objednávku.

.. obrázek: product_variants/product-variants-manufacturing-order.png
:align:center
:alt: Výrobní objednávka na variantu produktu BoM.

Poté se vraťte na stránku s objednávkami SO přes navigační lištu nahoře na stránce.

Nyní, když je produkt vyrobený, klikněte na tlačítko „Dodání“
produkt zákazníkovi. V dialogovém okně „Přijetí zásilky“ klikněte na tlačítko „Zkontrolovat“.
Poté klikněte na tlačítko „Aplikovat“ a produkt dodáte.

Pro dokončení prodeje se vraťte na SO (objednávku) přes „kroky“
nahoru na stránku a pak klikněte na tlačítko „Vytvořit fakturu“ a poté na „Vytvořit
Znovu fakturovat zákazníkovi objednávku.
