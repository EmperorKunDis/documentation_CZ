==========================
Vytvořte a odešlete nabídky
==========================

Jakmile se kvalifikovaný kontakt promění v příležitost, další krok je vytvoření a dodání
citace. Tento proces lze snadno zvládnout pomocí aplikace CRM v Odoo.

Vytvořit novou nabídku
======================

Pro vytvoření nové nabídky otevřete aplikaci CRM, zobrazte Pipeline
stránka na hlavním panelu CRM.

Zde klikněte na jakoukoli příležitost otevřít ji. Zkontrolujte existující informace a aktualizujte je.
pokud je třeba.

.. poznámka::
Pokud již byla vytvořena nabídka pro tuto příležitost, najdete ji kliknutím na
:tlačítko „Citace“ v horní části formuláře. Počet existujících citací je
jsou uvedeny i v seznamu chytrých tlačítek.

V horním levém rohu formuláře klikněte na tlačítko „Nová nabídka“.

.. obrázek: send_quotes/send-quotes-new-button.png
:align:center
:alt: Kvalifikovaný formulář s tlačítkem Nová nabídka zvýrazněným.

.. důležité:
Aplikace **Prodej** musí být nainstalována, aby se mohl použít tlačítko „Nové cenové nabídky“.
Vyskytnout se.

.. důležité:
Pole „Zákazník“ je na formuláři příležitosti **nepovinné**.

Informace o zákazníkovi však musí být přidány nebo propojeny před odesláním nabídky.
:guilabel:"Zákazník" pole na příležitosti je prázdné, kliknutím na :guilabel:"Nová
Tlačítko „Citace“ otevře okno s následujícími možnostmi:

   - :guilabel:`Vytvořit nového zákazníka“ vytváří nový záznam zákazníka s použitím všech dostupných
informace uvedené v přihlášce.
   - :guilabel:`Odkaz na existujícího zákazníka“: otevře se pole s názvy již existujících zákazníků.
Vyberte jméno, které spojí tuto novou citátu s již existujícím zákaznickým záznamem.
   - :guilabel:`Nepřipojujte se k zákazníkovi“: citace nebude s žádným zákazníkem spojena.
nejsou provedeny žádné změny v zákaznických informacích.

Jakmile tento odkaz kliknete, objeví se vám nová objednávka. Zkontrolujte informace na horní polovině
a aktualizovat všechny chybějící nebo nesprávné položky:

- :guilabel:`Zákazník“: společnost nebo kontakt, pro kterého byla tato nabídka vytvořena.
- :guilabel:`Zdroj“: pokud zákazník přišel na vaši firmu díky nějakému jinému zákazníkovi nebo kontaktu, vyberte ho z
vyskakovací nabídka v tomto poli.
- :guilabel:`Adresa faktury“: fyzická adresa, na kterou by měl být vystaven fakturační doklad.
- :guilabel:`Adresa doručení“: fyzická adresa, na kterou by měly být dodány všechny produkty.
- :guilabel:`Šablona citace“: pokud je k dispozici, vyberte přednastavenou šablonu „citace“.
Vyberte pole „<../../sales/sales_quotations/quote_template>“ z této oblasti.
- :guilabel:`Platnost do“: datum, kdy se tato citace již nebude považovat za platnou.
- :guilabel:`Datum citace“: datum vytvoření návrhu/odeslané objednávky, datum potvrzení potvrzené objednávky
pořadí objednávek. Poznámka: Toto pole je viditelné pouze v režimu vývojáře (režimu ladění).
</aplikace/obecné/rozvojářský režim> je aktivní.
- :guilabel:`Opakující se plán“: pokud je tato citace pro opakující se produkt nebo předplatné, vyberte
opakované konfiguraci plánu, která se má použít.
- :guilabel:`Ceník“: vyberte ceník, který se má na tento objednávkový formulář aplikovat.
- :guilabel:`Platební podmínky“: vyberte příslušné platební podmínky pro tuto nabídku.

.. obrázek: send_quotes/send-quotes-new-quote.png
:align:center
:alt: Kvalifikovaný formulář s tlačítkem Nová nabídka zvýrazněným.

..tip:
V poli `Expirace` se automaticky vyplní podle data vytvoření.
Citaci a výchozí platnost.

Aktualizovat výchozí časový rámec platnosti lze přes menu „Prodejní aplikace -->
Konfigurace --> Nastavení --> Cenové nabídky a objednávky“ a aktualizujte „Výchozí cenovou nabídku“.
V poli Platnost zadejte hodnotu 0, pokud chcete vypnout automatické vypršení platnosti.

Po provedení požadovaných změn klikněte na tlačítko :guilabel:`Uložit`.

Při použití šablony cenové nabídky je datum vypršení platnosti založeno na :guilabel:`Nabídce.
V poli „Platnost“ šablony. Chcete-li změnit způsob výpočtu platnosti na šabloně, přejděte do
:menu:„Prodejní aplikace --> Konfigurace --> Objednávky --> Šablony objednávek“.

Pak klikněte na šablonu, abyste ji otevřeli, a aktualizujte číslo v poli „Platnost cenové nabídky“
pole.

Řádky objednávek
-----------

Po aktualizaci informací o zákazníkovi, platbě a termínu na nové cenové nabídce
Tabulka „Řádky objednávky“ může být aktualizována s odpovídajícími informacemi o produktu.

Pro provedení této akce klikněte na tlačítko „Přidat produkt“ v záložce „Řádky objednávky“.

Poté zadejte název položky do pole :guilabel:`Produkt`, abyste mohli vyhledávat produkty.
katalog. Poté vyberte produkt z nabídky nebo vytvořte nový výběrem
Vytvořit nebo Vytvořit a upravit.

Po výběru produktu aktualizujte množství, pokud je třeba. Zkontrolujte informace v
zbývající pole.

K odstranění řádku z citace klikněte na ikonu „Odpadkový koš“ .

Pro uspořádání produktů do sekcí klikněte na „Přidat sekci“ a zadejte název sekce.
Pak klikněte na ikonu „OI-Draggable“ vlevo od názvu a přetáhněte ji
Přesuňte sekci na vhodné místo a přesuňte každý produkt stejným způsobem, abyste jej dokončili.
Organizace řádků s cenovými nabídkami.

.. obrázek: send_quotes/product-sections.png
:align:center
:alt:Kategorie se používají k vytváření samostatných položek na řádcích objednávky cenových nabídek.

Katalog produktů
~~~~~~~~~~~~~~~

Chcete-li rychle přidat do nabídky mnoho produktů, klikněte na tlačítko :guilabel:`Katalog`, abyste otevřeli
Katalog produktů.

Všechny produkty v databázi jsou uvedeny jako karty a mohou být seřazeny v levém panelu podle
„Kategorie produktů“ a „Atributy“.

.. obrázek: send_quotes/product-catalog.png
:align:center
:alt:Katalog produktů zobrazuje všechny produkty jako karty.

Chcete-li přidat produkt, klikněte na tlačítko „Přidat“ v kartě produktu vedle ikonky „fa-shopping-cart“.
Nastavte množství položky pomocí ikonky „+“ nebo „–“.
:guilabel:`(odčitatel)` nebo zadat počet v číselném poli mezi dvěma tlačítky.
K odstranění položky klikněte na tlačítko „Odstranit“ v detailu produktu vedle ikonky „Smazat“.

.. obrázek: send_quotes/set-quantity.png
:align:center
:alt: Modré tlačítko „Přidat“ a „Odebrat“ se používají k nastavení množství položky.

Jakmile jsou všechny množství produktů nastaveny, klikněte na tlačítko „Zpět do nabídky“ a vrátíte se zpět
citace. Výrobky, které byly vybrány v katalogu produktů, se nyní zobrazují na záložce „Řádky objednávky“.

Předběžná kalkulace a odeslání nabídky
==========================

Kliknutím na tlačítko „Náhled“ zobrazíte náhled citace tak, jak ji zákazník uvidí.
Tím se otevře náhled v portálu pro zákazníky.

Po prohlédnutí zákaznického náhledu klikněte na tlačítko „Návrat do režimu úprav“
citace v administraci.

Když je citace připravena k doručení zákazníkovi, klikněte na tlačítko „Odeslat e-mailem“.

Provedením takového kroku se otevře okno s přednastaveným e-mailovým sdělením. Informace z nabídky
včetně kontaktních údajů, celkové ceny a názvu nabídky se importují z
citát.

Přílohou e-mailu je soubor ve formátu PDF s citací.

.. poznámka::
Přednastavený vzor se používá k vytvoření e-mailové zprávy. Chcete-li změnit šablonu, klikněte na
vnitřní odkaz na pravé straně pole „Nahrát šablonu“, které se nachází na spodku stránky.
okno s e-mailovou zprávou.

K výběru nového šablonového souboru vyberte možnost z rozevírací nabídky „Nahrát šablonu“.

Pokračujte v provedení všech potřebných změn e-mailu a pak klikněte na tlačítko „Odeslat“. Kopie
zpráva je přidána do záznamu „Chat“.

Po odeslání citační nabídky se aktualizuje tlačítko „Nabídka“ v původní příležitosti.
s novým počtem. Tento citát i všechny ostatní citáty lze získat prostřednictvím této chytré
tlačítko v horní části příležitosti v aplikaci CRM*.

Každá citace připojená k příležitosti, která byla potvrzena a tedy převedena na
objednávky na prodej budou odečteny z počtu uvedeného v tlačítku „Nabídka“.
Výše prodejní objednávky se zobrazí v tlačítku „Objednávky“ umístěném na
stejné ovládací panely.

Označte příležitost, kterou jste vyhráli nebo prohráli.
===============================

Aby byl přehled o potrubí aktuální a správný, je třeba identifikovat příležitosti jako „vyhrané“
nebo ztratil zákazníka, který odpověděl na nabídku.

Pro označení příležitosti jako „získané“ nebo „ztratěné“ se vraťte k příležitosti pomocí chlebových zbytků
v horním levém rohu citace. Nebo přejděte na:
a klikněte na správnou příležitost, abyste ji otevřeli.

V horní části formuláře klikněte na tlačítko „Za“ nebo „Proti“.

Pokud je příležitost označena jako vyhraná, do záznamu se přidá zelené pásmo s nápisem „Vyhrál“.
byla přesunuta do fáze „Vyhráno“.

Označení příležitosti jako „ztratěné“ prostřednictvím tlačítka „Ztracené“ otevře tlačítko „Ztracené“.
okně s tlačítkem pro zadání „zapomenutého důvodu“.

V poli „Ztracený důvod“ vyberte existující ztracený důvod. Pokud žádný neexistuje
důvod je k dispozici, vytvořte nový zadáním do pole „Ztracený důvod“
kliknutím na tlačítko „Vytvořit“.

..tip:
Nejlepší praxí je pokusit se používat přednastavené hodnoty :guilabel:`Ztracený důvod`, co nejvíce.
možné nebo omezit vytváření nových hodnot pouze na vedoucí prodejního týmu. Použitím konzistentních hodnot
pro tento parametr bude analýza potrubí jednodušší a přesnější při filtrování na
:guilabel:`Ztracený důvod“ parametr.

Pro nastavení nových hodnot do pole, přejděte na: „CRM --> Konfigurace --> Ztracené
Důvody, a klikněte na oba políčka „Nový“ a „Uložit“, pokud chcete přidat novou položku do seznamu.
seznam.

Poznámky a komentáře lze přidat do pole „Závěrečná poznámka“ (viz guilabel).

Po zadání všech požadovaných informací v okně „Ztracený kus“ stiskněte
:guilabel:`Označit jako ztracené“.

Po kliknutí na tlačítko „Ztracený“ se okno zavře a Odoo se vrátí do
možnost vytvořit novou červenou šipku „Ztracený“ v horním pravém rohu
o příležitosti.

Jakmile je příležitost označena jako „ztratila“, není již brána v potaz a odstraněna z
plynovod.

Chcete-li zobrazit ztracenou příležitost v potrubí, klikněte na ikonu „svislý šipek“
v pravé části vyhledávací lišty a zvolte buď „Ztraceno“ nebo „Archivováno“.
padající nabídka.

.. důležité:
Při označení příležitosti jako „ztratil“ se považuje za „archivovanou“, ale upozorňujeme, že
aby se příležitost zahrnula do hlášení jako „ztratila“, musí být specificky
označeny jako „ztratil se“, nikoli „archivováno“.
