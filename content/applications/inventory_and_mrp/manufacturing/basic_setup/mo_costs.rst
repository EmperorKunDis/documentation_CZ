=========================
Náklady na výrobní objednávku
=========================

.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`
.. |MOs| nahradit za:: :abbr:`MOs (Výrobní objednávky)`
.. |POs| nahradit za: zkratka: `POs (Purchase Orders)`
.. |BoM| nahradit za: :abbr:`BoM (Seznam materiálů pro výrobu)“
.. |BoMs| nahradit za: :abbr:`BoMs (Seznamy materiálů)`

Schopnost přesně spočítat náklady na výrobu produktu je kritická při určování
ziskovosti výrobku. Aplikace **Manufacturing** společnosti Odoo usnadňuje tento výpočet automaticky
vypočítat náklady na dokončení každé výrobní objednávky (MO) a průměrnou produkci.
náklady na výrobek vycházející z všech dokončených |MOs|.

.. důležité::
Odoo aplikace pro výrobu rozlišuje mezi skutečnou cenou a náklady na výrobní proces (MO).

MO stojí za to, kolik by mělo stát dokončení MO na základě
konfigurace skladby výrobku (BOM) včetně nákladů.
množství komponent, ale také náklady na dokončení potřebných operací.

Skutečná cena představuje, kolik stojí dokončení |MO|. Faktory, které ovlivňují skutečnou cenu, jsou
způsobit skutečnou cenu lišit od nákladů MO. Například operace může trvat déle než
kompletnější než se předpokládalo, může být potřeba většího množství součástek, než bylo uvedeno na
|BoM| nebo cena komponentů se může během výroby změnit.

Konfigurace nákladů
==================

Odoo počítá náklady na materiál podle konfigurace BoM použitého k výrobě produktu.
výpočet zahrnuje náklady a množství komponentů a operací uvedených na seznamu BoM.
kromě provozních nákladů pracovišť, kde se tyto operace provádí.
mzda, kterou dostává každý zaměstnanec pracující na operaci.

Náklady na komponenty
--------------

Kalkulace nákladů na komponenty je automatická podle průměrné ceny nákupu komponenty.
všechny objednávky (PO). Chcete-li zobrazit náklady na komponentu, přejděte do aplikace „Sklad“:
Výrobky --> Výrobky“ a vyberte složkový výrobek. Cena se zobrazí v
V poli „Cena“ na kartě „Obecné informace“ v produktovém formuláři komponenty.

Náklady na komponentu lze nastavit ručně kliknutím na pole :guilabel:`Cena`.
produktové podobě součásti a zadání hodnoty. Nicméně jakékoliv budoucí |POs| pro součást
přepsat ručně zadanou hodnotu, vrátit pole „Náklady“ zpět na automaticky vypočítané
Výpočetní hodnota.

... výroba/množstevní náklady/náklady na pracoviště:

Náklady na pracovní centrum
----------------

Pro nastavení nákladů na provoz konkrétního pracoviště přejděte do nabídky:
Vyberte „Konfigurace“ – „Zaměstnání“, vyberte pracoviště.

Pro stanovení nákladů na provoz pracoviště za hodinu zadejte hodnotu do políčka :guilabel:`per
pole „Práce“ vedle sekce „Mzda za hodinu“ na pracovišti.
:guilabel:`Obecné informace“ záložka.

Pro nastavení hodinové sazby každého zaměstnance, který pracuje na pracovišti, zadejte hodnotu v
:guilabel:`na zaměstnance“ pole vedle sekce „Náklady na hodinu“.
kartě „Obecné informace“ v záložce centra. Například pokud je zadána hodnota
:guilabel:`za zaměstnance“ pole, stojí 25 dolarů za hodinu pro každého zaměstnance pracujícího v práci
centrum.

.. důležité::
Hodnota zadaná do pole :guilabel:`na zaměstnance` se používá pouze k výpočtu nákladů na |MO|.
která je odhadovaná cena dokončení |MO|.

Skutečná cena dokončení MO je reprezentována skutečnou cenou. Namísto použití
hodnota zadaná do pole „na zaměstnance“ a skutečná cena je vypočítána na základě hodinové sazby.
náklady na zaměstnance.

Příklad: Pokud je náklady na jednoho zaměstnance v pracovním centru $50.00, pak může být
s hodinovou sazbou 60 dolarů dokončuje tam pracovní objednávku, MO (předběžná) cena je
Výpočet na základě nákladů 50 USD za hodinu je použit pro výpočet skutečných nákladů, které jsou vypočítány z nákladů 60 USD za hodinu.

Podívejte se na část o nákladech na zaměstnance níže v části :ref:`<manufacturing/mo-costs/employee-cost>`.
jak nastavit cenu pro konkrétní zaměstnance.

.. výroba/náklady na materiál/mzdy zaměstnanců:

Náklady na zaměstnance
-------------

Chcete-li nastavit hodinovou sazbu pro konkrétního zaměstnance, přejděte do aplikace „Zaměstnanci“ a
Vyberte zaměstnance. Na kartě „Nastavení“ formuláře pro zaměstnance zadejte
hodinová sazba zaměstnance v poli „Mzda za hodinu“ v nastavení aplikace
§

.. důležité::
Podrobněji viz část „Náklady na pracoviště“ v kapitole :ref:`„Náklady na výrobu“ <manufacturing/mo-costs/work-center-cost>
V horní části se používá hodnota zadaná do pole „Mzda za hodinu“ na formuláři zaměstnance.
výpočet skutečných nákladů na |MO|. Odhadované náklady na |MO|, označované jako náklady na |MO|,
Výpočet je proveden na základě ceny za zaměstnance, která byla nastavena v kartě pracoviště.

Konfigurace BoM
-------------------

Konfigurace BoM tak, aby Odoo mohl přesně vypočítat náklady na MOs, které používají, vyžaduje dvě
kroky. Nejprve musí být přidány komponenty a zadána požadovaná množství. Druhý krok
musí být uvedeny i pracoviště, na kterých jsou prováděny.

Začněte tím, že se přesunete na: „Výroba -> Produkty -> Seznamy materiálů“.
Vyberte si |BoM| nebo vytvořte nový kliknutím na „Nový“.

V sekci „Součástky“ formuláře BoM přidejte každou součástku kliknutím na „Přidat
linie“, vyberte komponentu z rozevírací nabídky v sloupci „Komponenta“ a
Zadáním množství do sloupce „Množství“.

V záložce „Operace“ klikněte na tlačítko „Přidat řádek“, abyste otevřeli
Popisky v okně „Vytvořit operace“. Do textového pole zadejte název operace.
:guilabel:`Operace“ pole.

Vyberte pracovní centrum, kde se operace provádí. Poté přidejte
:guilabel:`Délka výchozího časového limitu“, což je odhadovaná doba, po kterou trvá provedení operace.

Výchozí hodnota pole „Délka“ je nastavena na „Délku určit ručně“,
To znamená, že číslo zadané do pole „Výchozí délka“ v poli „Název“ je vždy používáno jako
Doba trvání operace.

Vybráním políčka „Spočítat na základě sledovaného času“ způsobí Odoo automatické počítání
:guilabel:`Doba trvání výchozího nastavení“ na základě určitého počtu objednávek, který je nastaven v
Záznamy o průběhu prací na základě pole „Datum zahájení“.
Používá se místo něj pole „Výchozí doba“.

Hodinová cena provozu pracovního centra a doba jeho fungování jsou použity k
Vypočítat náklady na operaci.

Konečně klikněte na tlačítko „Uložit a zavřít“ pro přidání operace do BoM a zavřete
Okno „Vytvořit operace“. Místo toho můžete kliknout na „Uložit a nový“ pro přidání
operace pro BoM a otevřít prázdné okno „Vytvořit operace“ s možností přidat další
operace.

.. viz také:
Pro kompletní přehled konfigurace |BoM| se podívejte na dokumentaci k tématu :doc:`billů materiálu
<konfigurace_faktury>.

Přehled MO
=============

Každý MO má stránku s přehledem, která obsahuje různé informace o MO včetně
Výrobní náklady a skutečné výrobní náklady. Chcete-li zobrazit přehled pro |MO|, přejděte na:
Aplikace „Operace“ – „Výrobní objednávky“, vyberte |MO| a pak klikněte na ikonu :icon:`fa-bars`.
:guilabel:`Přehled“ chytrý tlačítko na horní části |MO|.

Obě metody |MO| i skutečná cena zohledňují náklady na komponenty a jejich množství.
náklady na dokončení každé objednávky. Na přehledové stránce je uveden sloupec pro každý z těchto hodnot,
součet těchto položek uvedených na konci sloupců „Skutečná cena“ a „Náklady na výrobu“.

Před zahájením práce na MO se v polích „Náklady projektu“ a „Skutečné náklady“ zobrazuje
stejné náklady. To je odhadovaná cena dokončení |MO|.

Jakmile se však začne pracovat, hodnoty v sloupci „Skutečné náklady“ mohou začít lišit.
hodnotami v sloupci „Náklady na MO“ (viz guilabel:„Náklady na MO“). Tento krok se provede, pokud je jiná hodnota
než bylo uvedeno v MO, délka pracovního úkolu je jiná než očekávaná nebo
hodinová mzda zaměstnance, který provádí pracovní příkaz, se liší od mzdy zaměstnance nastavené na práci
centrum.

Jakmile je |MO| dokončeno kliknutím na tlačítko „Vyrobit vše“, hodnoty ve
Aktualizovat sloupec „Skutečná cena“ tak, aby odpovídal sloupci „Předběžná cena“.

.. obrázek: mo_costs/overview.png
:align:center
:alt:Stránka s přehledem MO.

Průměrná výrobní cena
==========================

Kromě ceny každého jednotlivého |MO| pro výrobek sleduje Odoo také průměrnou cenu
Výroba produktu s přihlédnutím k nákladům na každou dokončenou jednotku.
Přejděte na: „Nastavení aplikace Inventor --> Zboží --> Zboží“ a vyberte produkt.

Náklady na výrobu produktu jsou zobrazeny za jednotku měření v poli :guilabel:`Cena`.
pole v záložce „Obecné informace“. Hodnota se bude dále aktualizovat podle
Náklady na další MO jsou započítány do průměrné ceny.

Vpravo od pole „Náklady“ je tlačítko „Spočítat cenu z BOM“, které
je k dispozici pouze pro produkty s alespoň jedním BoM. Kliknutím na tlačítko se vrátíte do výchozího nastavení ceny
produktu k očekávané ceně, která bere v úvahu pouze komponenty a operace uvedené na
BoM.

.. důležité::

Věnujte pozornost tomu, že kliknutím na tlačítko „Spočítat cenu z BoM“ se nezapne trvalá cena.
cena stále aktualizuje podle průměru ceny BoM a skutečné ceny jakéhokoliv budoucího
|MOs|

... varování: Příklad pracovního postupu: výrobní náklady
:class: alert alert-success

Golfový výrobce Fairway Fields vyrábí širokou škálu golfových produktů, včetně
v interiéru. Vytvořili si pro něj BoM (Bill of Materials), takže v Odoo se automaticky
pro každý odpaliště |MO| vypočítá výrobní náklady.

Podle BoM existují dvě složky:

   - Jeden kus zeleného filcu, který stojí 20 $.
   - Jeden kus gumové podložky, která stojí 30 dolarů.

BOM také uvádí čtyři operace, všechny z nich se provádějí na stanici montáže 1.
Má hodinovou provozní cenu 30 $. Následující operace jsou zahrnuty v této ceně:

   - *Střih vlněného plátna*: výchozí doba trvání sedm minut za celkovou cenu 3,50 $.
   - *Odřezaná guma*: standardní doba trvání pěti minut za celkovou cenu 2,50 $.
   - Přilepte podložku k vlněnému materiálu“: výchozí doba trvání 15 minut za celkovou cenu 7,50 $.
   - *Vyřízněte díry*: výchozí doba tři minuty za celkovou cenu 1,50 $.

Veškeré komponenty potřebné k výrobě jednoho hracího plánu stály 50 dolarů a operace
Požadované náklady činily 15 USD, celkové výrobní náklady byly 65 USD. Tento náklad je zahrnut v
:guilabel:`Cena‘ pole na formuláři produktu pro hrací plochu.

Fairway Fields potvrzuje |MO| pro jedno odpaliště. Před zahájením výroby je nutné vystavit |MO|
přehled uvádí náklady ve výši $65,00 v obou položkách :guilabel:`MO Cost` a :guilabel:`Real Cost`.
pole.

.... obrázek: mo_costs/přehled-dříve.png
:srovnání: do středu
:alt:Stránka webu MO s přehledem jednoho odpaliště před zahájením výroby.

Výroba začíná a operace trvají o deset minut déle než bylo plánováno.
Výrobní doba čtyřiceti minut. Toto odchylení od BoM je zaznamenáno v MO.
přehled, který nyní uvádí „skutečnou cenu“ 70 $.

.. obrázek: mo_costs/přehled-během.png
:srovnání: do středu
:alt:Stránka s přehledem výroby jednoho odpaliště, během produkce.

Jakmile je výroba dokončena a |MO| je označen jako *Dokončeno*, přehled |MO| se aktualizuje.
opět, aby hodnoty v sloupcích „Skutečná cena“ a „Náklady na výrobu“ odpovídaly.
zobrazující hodnotu 70 $.

Na stránce produktu odpaliště se nyní v poli „Cena“ zobrazuje cena 67,50 $.
průměr z původní ceny 65,00 USD a skutečné ceny 70,00 USD ze zdroje |MO|.
