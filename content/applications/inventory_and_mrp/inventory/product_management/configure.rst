Zobrazit obsah

.. |UoM| nahradit za: zkratka: `UoM (jednotka měření)`
.. |UoMs| nahradit: zkratka `UoMs (jednotky měření)`


=================
Nastavit produkt
=================

Skupinu produktů v Odoo lze dále definovat pomocí:

- Jednotky měření (UoM) <configure/uom>: standardní množství pro specifikaci množství produktů
(např. metry, yardy, kilogramy) umožňuje automatickou konverzi mezi měrnými systémy.
Odoo, například centimetry na nohy.

  - *Příklad: Koupit metrážový materiál, ale obdržet ho v yardách od dodavatele.*

- :doc:`configure/package`: Fyzický kontejner používaný k seskupení produktů bez ohledu na
zda jsou stejné nebo odlišné.

  - *Příklad: Krabice s různými předměty k dodání nebo skladovací krabice dvou set knoflíků
regál.*

- :doc:`konfigurace/balení“: seskupuje stejné produkty, aby je bylo možné nakoupit nebo prodat
určité množství.

  - *Příklad: Přeplněné plechovky limonády v balení po šesti, dvanácti nebo dvaceti čtyřech kusech.*

Srovnání
==========

Tento tabulkový přehled poskytuje podrobnou srovnávací tabulku jednotek měření, balení a obalů, aby pomohl
Podniky hodnotí, která z nich nejlépe vyhovuje jejich požadavkům.

.. seznam tabulkový::
:hlavičkové řádky: 1
:prázdné sloupky: 1

   * - Feature
     - Jednotka měření
     - Balíčky
     - Obaly
   * Účel
     - Standardizovaná měření pro jednotky produktů (například cm, lb, L)
     - Sleduje konkrétní fyzickou nádobu a její obsah
     - Skupiny předmětů dohromady pro snadnější správu (např. balení po 6, 12 nebo 24 kusech).
   * - Jednotnost výrobku
     - Definované na produkt, uložené jako jedna |UoM| v databázi
     - Povoluje smíšené výrobky
     - Téže produkty, jen levněji
   * -Flexibilní
     - Převod mezi jednotkami měření dodavatele a zákazníka
     - Mohou být do nádoby přidány nebo odebrány předměty
     - Množství je pevně stanoveno (např. vždy šest, dvanáct nebo dvacet čtyři kusů).
   * - Komplexnost
     - Nejjednodušší pro převody jednotek
     - Komplexnější kvůli sledování zásob na úrovni kontejneru
     - Jednodušší, vhodné pro homogenní skupiny výrobků
   * -Sledování zásob
     - Sleduje množství produktů na skladě v konkrétním měřítku definovaném pro daný produkt
forma
     - Sledování polohy a obsahu balíčku v skladu
     - Sledované trasy měly k dispozici pouze souhrnné údaje, nikoliv informace o konkrétních položkách.
   * – Hladké fungování čárových kódů
     - Není k dispozici
     - Požaduje skenování balíku i jednotlivých položek při přijetí. (I když je jich 30)
položky v balíčku) může umožnit :ref:`Přesun celého balíčku
funkci „Přesunout celý balíček“ k aktualizaci obsahu balení.
poloha předmětů při přesouvání balíčku
     - Při skenování čárového kódu na obalu se automaticky zaznamenají všechny jednotky, které jsou v balení (např. 1 balení = 12
jednotek
   * - Hledání produktu
     - Není k dispozici
     - Při skenování čárového kódu produktu se zjistí jeho obvyklé skladové místo v databázi Odoo
     - Čárový kód označuje skladovanou množinu, nikoliv místo skladování
   * - Jedinečné čárové kódy
     - Není k dispozici
     - Jedinečné čárové kódy pro jednotlivé balíky (např. paleta číslo 12).
     - Čárové kódy nastavené na úrovni balení (např. pro šestikus)
   * -Opakovatelnost
     - Nepoužitelné
     - Může být jednorázové nebo opakovaně použitelné a konfigurovatelné pomocí :ref:`Používání balíčku
pole „<skladové zásoby/sklady a skladování/shluk balení>“
     - Pouze jednorázové
   * – Hmotnost kontejneru
     - Nepoužitelné
     - Hmotnost kontejneru je zahrnuta do pole *Dopravní hmotnost* balíčku.
(:menu_selection:'Inventář aplikace-->Produkty-->Balíčky')
     - Hmotnost kontejneru je definována v nastavení typu balení
   * - Sledování sériových čísel
     - Požaduje manuální nastavení sledování |UoMs| pomocí lotů (viz případová studie
(podrobnosti viz inventář/správa produktů/skupiny a jednotky měření).
     - Pouze pro produkty v uzavřeném obalu
     - Platí pro oba produkty i jejich obal.
   * - Vlastní trasy
     - Nelze nastavit
     - Nelze nastavit
     - Dráhy mohou definovat konkrétní cesty skladu pro určitý typ balení.

Příklady použití
=========

Po porovnání různých funkcí zvažte, jak tyto podniky, s různými zásobami
správy a logistických procesů se k rozhodnutí dostaly.

Palety s předměty zabalenými v obalu
--------------------------------

Sklad přijímá dodávky mýdla uspořádaného na fyzických paletách po 96 kusech.
Palety se používají pro vnitropodnikové přepravy a prodávají se také samostatně jako jednotky.
Při určitém druhu dodání musí být váha palet zahrnuta do celkové hmotnosti zásilky.
Dále je potřeba paletu označit čárovým kódem pro snadnější sledování a počet jednotlivých
Mýdla musí být zahrnuta do inventury při přijetí palet.

Po vyhodnocení různých možností se ukázalo, že nejvhodnějším řešením je balení produktu.
umožňuje přiřadit čárový kód paletě, která je označena jako „paleta typu“, obsahující 96 mýdel.
Tento čárový kód zefektivňuje procesy automatickým registracím skupinového množství.
Mezi rozdíly patří:

- **Omezení sledování skladu**: Odoo sleduje pouze celkové množství, nikoliv počet
balení. Například pokud je přijato paletové balení s množstvím 12 a 24 kusů, Odoo zaznamenává
množství, nikoliv podrobnosti o paletě.
- **Kódy na obalech jsou typově specifické, ne jedinečné**: Kódy reprezentují typ balení (např.
„paleta s 96 mýdly“) nejednoznačně identifikují jednotlivé palety, například paletu číslo 1 nebo
Paleta číslo 2.

Získávejte informace o produktu pomocí čárového kódu
-----------------------------------------

Uživatel aplikace Odoo očekává, že aplikace Barcode zobrazí obvyklé skladové místo produktu.
snímání čárového kódu na kontejneru.

Nejvhodnější je „Balíčky“. Když je zapnutá vhodná konfigurace
<skladové zásoby/balení/zobrazit balíček>, při skenování štítku zobrazí obsah balení
aplikace **Čárový kód**.

Balíčky představují fyzické kontejnery, které umožňují detailní sledování položek, které obsahují.
Skenování balíčku umožňuje vidět jeho obsah a usnadňuje operace, jako je například inventarizace.
pohybuje.

... inventář/správa produktů/skladové položky a jednotky měření:

Sledovat různé jednotky měření v skladu
-------------------------------------------

Distributor ovocných šťáv sleduje více |UoMs| pro své operace:

- Ovoce se nakupuje v tunách.
- Džus se vyrábí a skladuje v kilogramech.
- Malé vzorky jsou uchovávány v gramů pro testování receptu.

Nejvhodnější jednotkou měření byl „Ton“. Odoo automaticky převádí tuny na kilogramy během
fakturami. Firma však sleduje v databázi pouze jednu jednotku měření na produkt, a proto používá
čísla losů pro rozlišení |UoMs|:

- LOT1: Gramy (g)
- LOT2: Kilo (kg)

Pro převod mezi partiemi je nutné provést manuální úpravy zásob, například odebrat 1 kg.
LOT2 přidá 1 000 g k LOT1. I když funkční, tento postup může být časově náročný a náchylný
chyby.

..toctree::


konfigurovat/typ
konfigurovat/uom
konfigurovat/balíček
konfigurace/balení

