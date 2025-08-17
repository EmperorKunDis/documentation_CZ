===========================================
Správa účtu v cizí měně
===========================================

V Odoo jsou všechny transakce zaznamenány v měně společnosti a reporty jsou
na základě výchozí měny. Když máte účet v cizí měně, za každou
transakce, Odoo ukládá dvě hodnoty:

-  Debet/kredit v měně společnosti;
-  Debet/kredit v měně účtu.

Směnné kurzy jsou aktualizovány automaticky pomocí webových služeb bankovní instituce.
výchozí nastavení používá služby Evropské centrální banky, ale existují i další možnosti.

Konfigurace
=============

Aktivujte více měn
-------------------------

Chcete-li pracovat s více měnami, přejděte na: „Účetnictví > Konfigurace > Nastavení“.
-->Měny a kliknutím na „Více měn“. Pod „Rozdíl při směně“
vstupy v:, poskytněte:GuideLabel:Journal, GuideLabel:Gain Account, GuideLabel:Loss Account
a poté klikněte na tlačítko „Uložit“.

Nastavte měny
--------------------

Jakmile je Odoo nakonfigurováno pro podporu více měn, jsou vytvořeny všechny měny, ale
je nutné aktivovat. Chcete-li aktivovat nové měny, klikněte na: guilabel:"Aktivujte jiné měny"
pod položkou „Mnoho měn“ nebo přejděte na „Účetnictví -> Konfigurace“.
Účetnictví: měny“.

Když jsou měny aktivovány, můžete si vybrat, zda chcete **automatizovat** aktualizaci kurzů nebo ne.
je na **ručním** nastavení. Pro aktualizaci sazby se vrátíte do :menuselection:`Účetnictví -->
Konfigurace --> Nastavení --> Měny, zkontrolovat položku „Automatické měnové kurzy“, nastavit
Vyberte si požadovanou frekvenci a klikněte na „Uložit“. Můžete také
možnost vybrat službu, ze které chcete získat směnné kurzy.

Klikněte na tlačítko „Aktualizovat nyní“ (:guilabel:„⏬“) vedle pole „Další běh“.
kurzy měn ručně.

Vytvořte si nový účet v bance
-------------------------

V účetním programu přejděte na: „Účetnictví“ -> „Konfigurace“ -> „Deníky“.
Vytvořte nový. Zadejte název „Journal Name“ a nastavte typ na „Bank“.
Kartě „Záznamy“ zadejte krátký kód, měnu a nakonec stiskněte
pole „Bankovní účet“ pro vytvoření nového bankovního účtu. V okně s informacemi o účtu
vytvoření, zadání názvu, kódu (např. 550007), nastavení typu na „Banky a hotovost“, nastavení měny
a uložit. Když se vrátíte na stránku s účtem, klikněte na pole „Číslo účtu“ a
V okně s upozorněním vyplňte číslo účtu, banku a
Ušetřit.

.. obrázek: cizí měna/cizí noviny.png
:align:center
:alt: Příklad vytvořeného bankovního výpisu.

Při vytvoření účetní knihy se účet automaticky propojí s účetní knihou.
je umístěn pod položkou „Účetnictví“ -> „Nastavení“ -> „Účetnictví: Skladová kniha“.

Faktura dodavatele v cizí měně
=================================

Pro platbu v cizí měně jednoduše vyberte měnu vedle položky „Deník“.
pokladní doklady a zaevidovat platbu. Odoo automaticky vytvoří a zaúčtuje převod měny nebo
ztrátu jako nový záznam.

.. obrázek: cizí měna/výpis z účtu v cizí měně.png
:align:center
:alt:Jak nastavit měnu faktury.

.. poznámka::
Pozor, můžete platit i v cizí měně. V takovém případě je automaticky převedena na měnu účtu.
Převádí mezi oběma měnami.

Zpráva o neuskutečněných ziscích a ztrátách v měnách
=======================================

Tento výpis shrnuje všechny nevypořádané částky v cizí měně na vašem účtu.
Umožňuje upravit vstup nebo nastavit směnný kurz ručně. Chcete-li zobrazit tento výkaz, přejděte na
:menuselection:`Zprávy --> Vedení účetnictví: Neuskutečněné zisky a ztráty z měnových kurzů“. Zde máte
přístup ke všem otevřeným položkám na vašem **rozvahovém účtu**.

.. obrázek: cizí měna/zisk a ztráta.png
:align:center
:alt: Pohled na deník Neuskutečněných zisků a ztrát.

Pokud chcete používat jiný kurz než ten, který je nastaven v položce
Konfigurace --> Nastavení --> Měny“, klikněte na tlačítko „Směnné kurzy“ a změňte
sazba cizích měn v zprávě.

.. obrázek: cizí měna/směnný kurz.png
:align:center
:alt: Nastavení kurzů pro manuální změnu.

Při ručním nastavení směnných kurzů se zobrazí žluté upozornění, které vám umožní obnovit původní hodnotu.
Sazba Odoo. Klikněte na tlačítko:guilabel:`Resetovat sazbu Odoo`.

.. obrázek: cizí měna/výchozí sazby.png
:align:center
:alt:Banner k obnovení Odoo sazeb.

Aby se aktualizovala vaše rovnováha s částkou v poli „upravení“,
Klikněte na tlačítko „Zadání úpravy“. V okně se zobrazí výběr
„Deník“, „Příjmový účet“ a „Výdajový účet“ k výpočtu.
zpracovat **neuskutečněné zisky a ztráty**.

Datum zprávy můžete nastavit v poli „Datum“. Odoo automaticky obrátí
vytvoření rezervace na datum, které je uvedeno v poli „Datum obratu“.

Jakmile je příspěvek zveřejněn, sloupec „Upravení“ by měl ukazovat hodnotu 0,00, což znamená, že všechny **neuskutečněné
Zisk nebo ztráta byla upravena.

.. obrázek: cizí měna/převod na cizí měnu.png
:align:center
:alt:Zpráva o neuskutečněných ziscích a ztrátách v důsledku měnové politiky se upraví.
