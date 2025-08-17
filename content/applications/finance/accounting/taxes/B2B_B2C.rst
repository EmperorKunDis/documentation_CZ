=================================================
Ceník pro obchodníky a ceník pro spotřebitele
=================================================

Při práci s koncovými zákazníky se ceny obvykle vyjadřují včetně daně z přidané hodnoty (například
největší obchodní platformou (tedy největším e-shopem). Ale když pracujete v prostředí B2B, společnosti zpravidla smlouvy o cenách vyjednávají
V ceně není započítána daň z přidané hodnoty.

Odoo zvládá obě uvedené situace bez problémů, pokud zaregistrujete ceny produktu včetně daní.
zahrnuté nebo nezahrnuté, ale nikoli obojí najednou. Pokud si nastavíte všechny ceny včetně DPH (nebo
vyloučené) můžete stále snadno vytvářet prodejní objednávky s cenami bez DPH (nebo s DPH).
To je snadné.

Toto dokumentování je pouze pro konkrétní případ, kdy potřebujete dva odkazové body.
cena (s DPH nebo bez DPH) za stejný produkt. Komplikovanost spočívá v tom, že
není symetrický vztah s cenami zahrnutými a cenami vynechanými, jak je vidět na tomto použití
případu v Belgii s daní ve výši 21 %:

-  Vaše elektronická obchodní činnost má produkt za 10 € (včetně daní).

-  Takže by to vyšlo na 8,26 eura bez DPH a daň 1,74 eura.

Ale pro stejný případ použití, pokud zaregistrujete cenu bez DPH na produktovém formuláři (8,26 €),
získat cenu včetně DPH za 9,99 €, protože:

-  **8.26€ \* 1.21 = 9.99€**

Takže záleží na tom, jak si nastavíte ceny v produktovém formuláři.
včetně DPH a bez DPH:

-  Daň z přidané hodnoty nezahrnuje: **8,26 € a 10,00 €**

-  Daň zahrnuta: **8,26 € a 9,99 €**

.. poznámka::
Pokud nakoupíte 100 kusů za 10 € včetně DPH, je to ještě horší. Dostanete: **1000 €
(včetně daně) = 826,45 € (cena) + 173,55 € (dani) **, což je velmi odlišné od ceny za
kus za 8,26 € bez DPH.

Tato dokumentace vysvětluje, jak se vypořádat s velmi specifickým případem použití, kdy potřebujete
dvě ceny (bez a s DPH) na stejném výrobku uvnitř jedné společnosti.

.. poznámka::
V oblasti financí nemáte žádné další příjmy z prodeje svého produktu za 10 € namísto 9,99 € (za jednotku).
Protože váš příjem bude stejný jako za 9,99 €, jen se zvýší daň o 1 cent.
Takže pokud provozujete elektronický obchod v Belgii, udělejte svému zákazníkovi laskavost a nastavte cenu na 9,99 EUR
místo 10 €. V případě 20 € nebo 30 € či jiných sazeb daně se nejedná o odpočet DPH.
Pokud je množství větší než 1, uděláte mi taky radost, protože pak si vše můžete vyřídit bez DPH.
Je méně chybová a snadnější pro vaše obchodníky.

Konfigurace
=============

Úvod
------------

Nejlepší způsob, jak se tomuto složitosti vyhnout je zvolit si pouze jeden způsob řízení cen a tento dodržovat.
cena bez DPH nebo cena s DPH zahrnutá. Definujte, která je výchozí uložená na
forma produktu (na základní dani související s produktem) a nechte si vypočítat ostatní.
automaticky na základě ceníku a fiskální pozice. Smlouvy s klienty vyjednávejte
takže to funguje zcela bez konfigurace a je to hotové hned po instalaci.

Pokud nemůžete a pokud skutečně vyjednáváte nějaké ceny bez DPH a
Pokud zákazníkům nabízíte ceny s DPH, musíte:

#Vždy uchovávejte výchozí cenu bez DPH na produktovém formuláři a aplikujte daň (cenu)
(výrobku).

#Vytvořit ceník s cenami včetně DPH pro konkrétní zákazníky.

#vytvořit daňovou pozici, která přepne daně zahrnuté do ceny na daně nezahrnuté do ceny.

#. přiřadí oba ceníky i fiskální pozici zákazníkům, kteří o to mají zájem
cenová nabídka a fiskální pozice

Pro účely této dokumentace použijeme výše uvedený příklad:

-   Vaše výchozí prodejní cena je 8,26 € bez DPH

-   Ale chceme ho prodávat za 275 Kč v našich obchodech nebo na e-shopu.

.. B2B, B2C / e-commerce:

e-commerce
---------

Pokud na svém webu používáte jen ceny pro B2C nebo B2B, jednoduše vyberte vhodný režim.
**Nastavení aplikace** webové stránky.

Pokud máte na jedné webové stránce obchodní i spotřebitelské ceny, prosím, sledujte tyto pokyny:

#Aktivujte režim vývojáře a přejděte do nastavení obecných.
--> Uživatelé a společnosti --> Skupiny.
#Otevřete buď „Technické/Daňové zobrazení B2B“ nebo „Technické/Daňové zobrazení B2C“.
#Pod záložkou „Uživatelé“ přidejte uživatele, kteří potřebují mít přístup ke cenovým typům. Přidejte uživatele B2C
v skupině B2C a uživatelé v B2B skupině.

Nastavení produktů
---------------------

Vaše společnost musí být nastavena tak, aby DPH nebylo zahrnuto do ceny výchozím nastavením. To je obvykle výchozí
konfiguraci, ale můžete si zkontrolovat svou **Výchozí sazbu DPH** v nabídce
Nastavení aplikace „Účetnictví“ v menu „Správa účtu“.

.. obrázek: B2B_B2C/cena_B2C_B2B01.png


Jakmile je hotovo, můžete vytvořit cenový seznam pro B2C. Můžete aktivovat funkci cenového seznamu na základě zákazníka
z nabídky: „Konfigurace -> Nastavení“ aplikace Prodej. Zvolte
možnost **různé ceny pro jednotlivé zákaznické segmenty**.

Jakmile je vše hotovo, vytvořte si z nabídky „Konfigurace“ -> „Ceník“ nový ceník pro B2C.
Dobré je také přejmenovat výchozí ceník na B2B, aby nedocházelo k záměně.

Poté vytvořte produkt za 8,26 € s DPH ve výši 21 % (definováno jako daň nezahrnutá v ceně) a nastavte
cena na tento produkt pro B2C zákazníky je 10 € z nabídky
Aplikace pro obchodní oddělení:

.. obrázek: B2B_B2C/cena_B2C_B2B02.png


Určení daňové pozice B2C
-------------------------------

V účetním programu vytvořte z této nabídky fakturační položku pro B2C:
:menu „Nastavení“ -> „Daňové pozice“. Tato daňová pozice by měla odpovídat DPH ve výši 21 %.
bez DPH (DPH je zahrnuta v ceně) s DPH 21 % (DPH je zahrnuta v ceně)

.. obrázek: B2B_B2C/cena_B2C_B2B03.png


Test vytvořením citační poznámky
============================

Vytvořte nabídku z aplikace Prodej pomocí nabídky „Prodej --> Nabídka“.
Měli byste mít následující výsledek: 8,26 € + 1,73 € = 9,99 €.

.. obrázek: B2B_B2C/cena_B2C_B2B04.png


Vytvořte nabídku, ale změňte cenový seznam na B2C a fiskální pozici na B2C.
citace, než přidáte svůj produkt. Měli byste mít očekávaný výsledek, který je celková cena
pro zákazníka: 8,26 € + 1,74 € = 10,00 €.

.. obrázek: B2B_B2C/cena_B2C_B2B05.png


Toto je očekávané chování zákazníka vašeho obchodu.

Vyhněte se změnám každé objednávky na prodej
===============================

Pokud s klientem uzavíráte smlouvu, zda daň započítáváte nebo ne, je
Můžete nastavit ceník a fiskální pozici na kartě zákazníka tak, aby se aplikovaly.
automaticky při každé prodejní transakci tohoto zákazníka.

Ceník je v záložce „Prodej a nákup“ ve formuláři zákazníka a fiskální pozice
v záložce účetnictví.

Pozor, že je tento postup náchylný k chybám: pokud nastavíte daňovou pozici s DPH zahrnutou v ceně, ale použijete
ceník, který není zahrnutý, můžete mít špatně spočítané ceny. Proto jsme
obvykle doporučují společnostem, aby pracovaly pouze s jedním referenčním cenovým modelem.
