===================
Šablony citací
===================

Opakovaně použitelné šablony cenových nabídek lze vytvořit v aplikaci **Prodej** společnosti Odoo pro běžné produkty nebo služby.

Pomocí těchto šablon lze citace přizpůsobit a odeslat zákazníkům rychleji.
bez nutnosti vytvářet nové nabídky od nuly při každém obchodním jednání.

Konfigurace
=============

Pro použití šablony citace začněte aktivací nastavení v aplikaci „Prodej“:
Konfigurace --> Nastavení“, a přejděte na záhlaví „Citace & Objednávky“.

Pod nadpisem zaškrtněte políčko „Šablony citací“. To zpřístupní nové
v poli „Výchozí šablona“, ve které lze zvolit výchozí šablonu citačního formátu.
kliknutím na tlačítko „Přidat do košíku“.

.. obrázek: quote_template/citace-vzory-nastavení.png
:alt:Jak zapnout šablony citačních znaků v prodejním modulu Odoo.

Při aktivování funkce „Šablona citace“ se zobrazí interní ikonka
Níže se zobrazí odkaz na šablonu citace.

Po kliknutí na tento odkaz se zobrazí stránka „Šablony citací“, ze které lze šablony
vytvářeny, zobrazovány a upravovány.

Před odchodem z stránky „Nastavení“ nezapomeňte kliknout na tlačítko „Uložit“.
uložit všechny změny provedené v průběhu sezení.

.. prodeje, zasílání nabídek a vytváření šablon:

Vytvořit šablony cenových nabídek
==========================

Pro vytvoření šablony cenového návrhu klikněte na odkaz „Šablona cenového návrhu“
Nastavení stránky po zapnutí šablon cen nebo přejděte na
V nabídce „Prodejní aplikace“ -> „Konfigurace“ -> „Šablony cenových nabídek“. Oba možnosti odhalují
stránce „Šablony citací“, kde lze vytvářet, zobrazovat a upravovat šablony citací.

.. obrázek: citace_šablona/citátových šablon stránka.png
:alt:Stránka šablon citací v aplikaci prodeje Odoo.

Pro vytvoření nového šablony citačního formátu klikněte na tlačítko „Nový“, které se nachází v pravém horním rohu.
rohu. To odhalí prázdný vzor citace, který lze upravit podle potřeby.

.. obrázek: citaci_vzor/prázdný_citát.png
:alt: Vytvořte nový vzor pro cenovou nabídku na Odoo Sales.

Začněte vložením názvu šablony do pole :guilabel:`Šablona citace`.

V poli „Platnost citace“ pak vyberte, na jak dlouho je platný vzorový formulář.
zůstane platná nebo zanechá pole na výchozí hodnotu „0“, aby šablona zůstala platná
neomezeně.

Dále v poli „Potvrzení“ klikněte na prázdný seznam a vyberte
přednastavený e-mailový vzor, který bude odeslán zákazníkům po potvrzení objednávky.

..tip:
Chcete-li vytvořit nový e-mailový šablonu přímo z pole „Potvrzení“ (viz obrázek), začněte
Při psaní názvu nového e-mailového šablonu do pole a výběru buďto: :guilabel:`Vytvořit` nebo
z nabídky, která se objeví.

Vybráním položky „Vytvořit“ vytvoříte e-mailový šablonu, kterou můžete později upravit.

Vybráním položky „Vytvořit a upravit…“ vytvoříte e-mailový šablonu a vyberete možnost „Vytvořit
Pop-up okno potvrzení e-mailu se zobrazí, ve kterém lze upravit šablonu e-mailu.
ihned konfigurovat.

.... obrázek::quote_template/create-confirmation-mail-popup.png
:alt:Vytvořit okno s potvrzením e-mailu z formuláře nabídky v Odoo Sales.

Po dokončení všech úprav klikněte na tlačítko :guilabel:`Uložit a zavřít`, abyste uložili šablonu e-mailu.
a vrátit se zpět do citace.

Pokud pracujete v prostředí více společností, použijte pole :guilabel:`Společnost`, abyste určili, ke které
tento vzor citačního odkazu se na tuto společnost vztahuje.

Pokud je časopis nastaven v poli „Fakturační deník“ na hodnotu „Výdejky“, všechny objednávky s tímto šablonou
Vystaví fakturu do zvoleného deníku. Pokud v tomto poli není vyplněn žádný deník, bude se použít
použije se nejnižší sekvence.

Pokud jsou aktivovány funkce „Elektronická podepsání“ a/nebo „Elektronické platby“,
Nastavení (v menu aplikace Prodej --> Nastavení), kde je možné
na formulářích smluvních cenových nabídek.

Zaškrtněte políčko vedle:guilabel:„Online podpis“ a požádejte zákazníka o vytvoření online podpisu.
potvrdit objednávku.

Zatrhněte políčko vedle :guilabel:„Online platba“ a požádejte zákazníka o online platbu.
potvrdit objednávku. Když je zaškrtnuté pole „Online platba“, objeví se nové procentní pole,
Kde se může zadat konkrétní procento platby.

Obě možnosti „Online podpis“ a „Online platba“ lze zapnout.
současně, v takovém případě musí zákazník poskytnout **obojí** - podpis i platbu.
potvrdit objednávku.

Tabulka řádků
---------

V záložce „Čáry“ lze produkty přidat do šablony nabídky kliknutím
„Přidat produkt“, uspořádané kliknutím na „Přidat sekci“ (a přetahováním/přesouváním
nadpisů), a dále s dalšími informacemi na vlastní uvážení (např. podrobnosti o záruce).
Poznámky (např. termíny) kliknutím na tlačítko „Přidat poznámku“.

Chcete-li přidat produkt do šablony nabídky, klikněte na tlačítko „Přidat produkt“ v části „Řádky“.
tabulku šablony pro citaci. To odhalí prázdné pole v sloupci „Produkt“.

Když na něj kliknete, objeví se vám seznam existujících produktů v databázi. Vyberte si požadovaný
produkt z nabídky vybrat a přidat ho do šablony cenového návrhu.

Pokud požadovaný produkt není na první pohled viditelný, zadejte název požadovaného produktu do
V poli „Produkt“ a možnost se objeví v rozevíracím seznamu. Produkty lze také najít
kliknutím na „Hledat více ...“ v rozbalovacím seznamu.

..tip:
Je možné přidat produkty související s akcí (stánky a registrace) do šablon nabídek.
Klikněte na pole „Produkt“, zadejte „Událost“ a vyberte požadovanou událost.
výrobky související s událostí z rozevírací nabídky níže.

.. poznámka::
Když je produkt přidán do šablony cenové nabídky, výchozí hodnota :guilabel:`Množství` je 1, ale
to lze kdykoli upravit.

Poté přetáhněte a vraťte produkt na požadovanou pozici pomocí ikony „šest čtverců“.
umístěné v levém sloupci vedle položky.

Chcete-li přidat sekci, která slouží jako nadpis k uspořádání řádků objednávky, klikněte
V položce „Dodatečné informace“ v záložce „Záznamy“. Po kliknutí se objeví prázdné pole.
Do které se požadované jméno oddělení zadává. Po zadání názvu stiskněte
zabezpečit sekci.

Poté přetáhněte a vraťte sekci do požadované polohy pomocí ikony oi-apps.
Ikona „(šest čtverců)“ umístěná vlevo od položky.

Přidat poznámku, která se pro zákazníka zobrazí jako součást citační smlouvy, klikněte
V záložce „Linky“ klikněte na tlačítko „Přidat poznámku“. Zobrazí se prázdné pole, do kterého můžete
požadovanou notu lze napsat. Jakmile je nota zadána, klikněte pryč, abyste si ji uložili.

Poté přetáhněte a vraťte poznámku na požadovanou pozici pomocí ikony „OI Apps“
:guilabel:`(šest čtverců)` ikonu.

Chcete-li odstranit jakýkoli řádek v záložce „Řádky“ (produkt, sekce a/nebo poznámka), klikněte na
:icon:`fa-trash` :guilabel:`(smazat záznam)` ikona na konci řádku.

Volitelné produkty
---------------------

Používání „volitelných produktů“ je marketingová strategie, která zahrnuje křížové prodeje.
s hlavním produktem. Cílem je nabídnout zákazníkům užitečné a související produkty, což může vést
Výrazně vyšší prodej.

Příklad:
Pokud zákazník chce koupit auto, má možnost si objednat masážní sedadla.
přidat k autu další produkt nebo nabídku ignorovat a auto si koupit samostatně.

Volitelné produkty se zobrazují jako část na konci objednávky nebo stránky e-shopu.
Mohou je ihned přidat do svých on-line objednávek sami, pokud si to přejí.

.. obrázek: citace_šablony/nepovinné_produkty_na_objednávce.png
:alt:Dodatečné produkty, které se objevují na typické objednávce s Odoo Sales.

V záložce „Volitelné produkty“ přidejte pro každý křížený produkt řádek.
s původními položkami v záložce Lines, pokud je to možné.

Kliknutím na tlačítko „Přidat řádek“ se zobrazí prázdné pole v sloupci „Produkt“.

Po kliknutí se zobrazí nabídka produktů ze databáze. Vyberte požadovaný produkt
z nabídky rozbalovacího seznamu přidat ho jako volitelný produkt do šablony cenové nabídky.

K odstranění jakéhokoliv řádku v záložce „Volitelné produkty“ klikněte na ikonu
:guilabel:`(odstranit záznam)` ikonu.

.. poznámka::
Volitelné produkty nejsou **povinné** pro vytvoření šablony nabídky.

Soubor podmínek a pravidel
----------------------

Karta „Podmínky a podmínky“ umožňuje přidat podmínky a podmínky.
vzor smlouvy. Chcete-li přidat podmínky a ustanovení, zadejte požadované podmínky a ustanovení do tohoto pole.

.. viz též:
:doc:`../../../finance/účetnictví/fakturace/obchodní podmínky`

.. poznámka::
Podmínky a smlouvy nejsou **povinné** pro vytvoření šablony nabídky.

Použijte šablony citací
=======================

Při vytváření nabídky (v menu „Prodejní aplikace“ -> „Nový“) vyberte přednastavený šablonu
pole „Šablona citace“.

.. poznámka::
Řazení šablon v poli „Šablona citace“ je určeno pořadím
z šablon v formuláři Cenové nabídky. Pořadí cenových nabídek ve formuláři Cenová nabídka
Formulář šablon neovlivňuje nic jiného.

Pro zobrazení toho, co uvidí zákazník, klikněte na tlačítko „Náhled“ v horní části stránky.
podívat se, jak vypadá šablona citace na webu prostřednictvím zákazníka Odoo.
portál.

.. obrázek:quote_template/citáty-šablony-návrh.png
:alt:Předběžný náhled cenové nabídky v Odoo Sales.

Po dokončení všech bloků a konfigurací klikněte na tlačítko :guilabel:`Uložit`, abyste uložili
konfigurace.

Modrý praporek umístěný v horní části náhledu šablony citace lze použít k rychlému návratu.
Ikona „Přejít zpět do režimu editačního okna“ (viz obrázek). Když ji kliknete, vrátí se vám aplikace Odoo do režimu editace.
formulář v zadní části aplikace Sales.

Masivní zrušení cenových nabídek/objednávek
===================================

Zrušte více cenových nabídek (nebo objednávek) kliknutím na „Prodejní aplikace“ v hlavním menu.
Pokyny -> Cenová nabídka - Dashboard, výchozí zobrazení v seznamovém pohledu. Pak na levé straně
v tabulce zaškrtněte políčka u citací, které chcete zrušit.

..tip:
Vyberte všechny záznamy v tabulce zaškrtnutím políčka nad hlavičkou sloupce v levém horním rohu.
tabulku; celkový počet vybraných položek se zobrazuje na vrcholu stránky.

Pak s vybranými požadovanými citacemi (nebo objednávkami na prodej) zobrazenými v seznamovém
Stránka „Citace“ klikněte na tlačítko „Akce“ ikony „fa-cog“
kliknutím na tlačítko „Přidat do košíku“.

Vyberte možnost z rozbalovací nabídky: „Zrušit cenové nabídky“.

.. obrázek:quote_template/zrušit-citace.png
:alt:Možnost Zrušit citace v nabídce Akce na kartě Prodej aplikace Odoo.

.. poznámka::
Toto můžete udělat pro jakýkoliv účet v jakékoliv fázi, i když je potvrzen jako prodej.
pořádku.

Při výběru možnosti „Zrušit nabídky“ se zobrazí „Zrušit nabídky“.
objeví se okno s potvrzením. K dokončení zrušení klikněte na tlačítko „Zrušit“.
tlačítko „citace“.

.. poznámka::
Při pokusu o zrušení objednávky předplatného se objeví chybová hláška.
který má fakturu.

.. viz též:
   - :doc:`get_signature_to_validate“
   - :doc:`get_paid_to_validate“
