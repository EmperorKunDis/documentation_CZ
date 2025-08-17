=============================
Automatická oceňování zásob
=============================

.. |right arrow| nahradit za: :icon:`fa-arrow-right` :guilabel:`(right arrow)`

Hodnota zásob společnosti se vypočítává z hodnoty všech položek skladu, které má společnost k dispozici.
být zaznamenány v účetní knize, aby bylo možné přesně vyjádřit hodnotu společnosti.
všechny své aktiva.

Výchozí režim účtování zásob v Odoo je periodický způsob ocenění zásob (známý také jako manuální způsob ocenění zásob).
Tento způsob předpokládá, že účetní tým ručně zadává záznamy do knihy jízd na základě fyzických
výkazu majetku a skladoví zaměstnanci tráví čas spočítáním zásob. V Odoo je každé
Kategorie produktu odráží tuto skutečnost s nastavením „Metoda cenotvorby“ na „Standardní“.
„Cena“, a „Hodnota zásob“ („Zobrazit výchozí hodnoty“) nastavte na „Manuální“.

.. obrázek: inventarni-ohodnoceni-konfigurace/inventarni-ohodnoceni-polozky.png
:align:center
:alt:Základní metoda výpočtu je umístěna na kartě Kategorie produktů.

Alternativně může být použita neustále aktuální (automatická) ocenění zásob, která vytváří skutečné *záznamy v knize jízd*
Aplikace pro účetnictví, která zaznamenává každý příchod nebo odchod zásob do skladu společnosti.

Tento dokument se zaměřuje na správné nastavení automatického oceňování zásob, které je
integrovaný způsob ocenění, který zajišťuje, že záznamy v aplikaci *Účetnictví* odpovídají skladovým zásobám.
Aktualizace ocenění v aplikaci Inventář. Pro zavedení inventární ceny ve společnosti Odoo se podívejte na
do dokumentace „Používání inventarizace“.

.. varování:
Přechodem z manuální na automatickou inventarizaci může dojít ke kolizi mezi skladovými zásobami
hodnotící a účetní časopisy.

Jedna „úspěšná strategie <https://www.odoo.com/r/Kvfg>“ pro přechod na automatické oceňování:

   #Vyčistit stávající zásoby (možná s :doc:`úpravou zásob).

   #Změnit metodu ocenění zásob na Automatické.
   #. Vraťte stávající zásoby s původní peněžní hodnotou (pomocí inventarizačního zásahu).

Jakmile je získána stávající zásoba, aplikace Odoo Accounting automaticky vytvoří
záznamy z účetních knih k odpovídajícím záznamům o hodnotě zásob.

Konfigurace
=============

Pro správné nastavení automatického oceňování zásob postupujte v Odoo takto:

#:ref:`Nainstalujte aplikaci účetnictví a zapněte konkrétní nastavení
<skladové zásoby/účetnictví/založení účtů>
#.:ref:Nastavte automatické oceňování zásob na kategorie produktů
<Inventar/Lagerbestände/Bewertung nach Produktkategorie>
#:ref:`Metoda nákladového účtování <sklady/nákladové metody>“

... skladovou zásobu, sklady a účetnictví:

Nastavení účetnictví
----------------

Pro automatické oceňování zásob je potřeba nainstalovat aplikaci *Účetnictví*. Poté přejděte na
„Účetnictví“ -> „Nastavení“ -> „Předvolby“, a v položce „Sklad“.
V části „Ocenění“ zaškrtněte políčko „Automatické účtování“. Pak klikněte
:guilabel:`Uložit“.

.. poznámka::
Povolení položky „Automatické účtování“ zobrazí předtím skryté *Zásoby*.
pole v produktové kategorii.

.. obrázek: inventarni-ohodnoceni-konfigurace/auto-uctovani.png
:align:center
:alt:Automatické účtování v sekci Nastavení - Hodnota zásob.

Viz položku :ref:`Náklad <sklady/náklad> a :ref:`Zásoba
sekce „Vstupy/výstupy“ (účetní záznamy o zásobách) v dokumentaci pro podrobnosti.
konfiguraci účetních deníků zobrazených.

.. skladové zásoby, sklady a způsob ocenění podle kategorie zboží:

Nastavení kategorie produktů
----------------------

Po zapnutí inventarizačního účetnictví podle <inventory/warehouses_storage/accounting-setup> je další
prvním krokem je nastavení produktové kategorie pro automatickou inventarizaci.

Přejděte na položku „Aplikace Inventář --> Konfigurace --> Kategorie produktů“ a vyberte
požadované kategorii produktů. V sekci „Ocenění zásob“ nastavte
V poli „Hodnota zásob“ nastavte hodnotu na „Automatické“. Opakujte tento krok pro každý produkt.
kategorii, která má používat automatické ocenění zásob.

.. poznámka::
Po zapnutí automatického účtování se každá nově vytvořená vrstva skladového pohybu (SVL) bude
aktualizace hodnoty zásob vytváří účetní případ.

.. obrázek: inventarni-ohodnoceni-konfigurace/automatizovane-inventarni-ohodnoceni.png
:align:center
:alt:V poli inventarizační hodnota produktu v kategorii s různými skladovými účty.

... skladování, sklady a metody účtování:

Metoda nákladového účetnictví
==============

Po zapnutí inventarizace se vám zobrazí
Metoda pro výpočet a evidenci nákladů na zásoby je definována v kategorii produktu
Odoo.

Přejděte na: `Nastavení aplikace Inventor --> Konfigurace --> Kategorie produktů` a vyberte požadovanou
Kategorie produktů. V sekci „Ocenění zásob“ vyberte vhodný
:guilabel:`Metoda cenotvorby“:


.. záložky::

...... tab:: Standardní cena

Výchozí metoda nákladového účetnictví v Odoo. Cena produktu je manuálně definována na kartě produktu.
formě a tato cena se používá k výpočtu hodnoty. I když je nákupní cena při nákupu
Pokud je objednávka odlišná, hodnota je cena definovaná na formuláři produktu.

... seznam-tabulka::
:hlavičky: 1
:sloupek: 1

         * – Operace
           - Náklady na jednotku
           - Množství skladem
           - Vstupní hodnota
           - Hodnota zásob
         * -
           - $10
           - 0
           -
           - $0
         * - Získat 8 produktů za 10 dolarů za kus
           - $10
           - 8
           - 8 * $10
           - $80
         * - Získat 4 produkty za 16 dolarů/jednotku
           - $10
           - 12
           - 4 * $10
           - $120
         * - Dodat 10 produktů
           - $10
           - 2
           - -10 * $10
           - $20
         * - Získat 2 produkty za 9 dolarů za kus
           - $10
           - 4
           - 2 * $10
           - $40

....... tabulka: Průměrná cena (AVCO)

Výpočet hodnoty produktu na základě průměrné ceny daného produktu dělené
celkový počet dostupných zásob skladových zásob. S tímto způsobem ocenění zásob se
*dynamický* a neustále se přizpůsobuje podle ceny produktu.

... seznam-tabulka::
:hlavičky: 1
:sloupek: 1

         * – Operace
           - Náklady na jednotku
           - Množství skladem
           - Vstupní hodnota
           - Hodnota zásob
         * -
           - $0
           - 0
           -
           - $0
         * - Získat 8 produktů za 10 dolarů za kus
           - $10
           - 8
           - 8 * $10
           - $80
         * - Získat 4 produkty za 16 dolarů/jednotku
           - $12
           - 12
           - 4 * $16
           - $144
         * - Dodat 10 produktů
           - $12
           - 2
           - -10 * $12
           - $24
         * - Získat 2 produkty za 6 dolarů za kus
           - $9
           - 4
           - 2 * $6
           - $36

Jak se vypočítává jednotková cena a skladová hodnota na každém kroku?

      - Při nákupu čtyř produktů za 16 dolarů každý:

        - Hodnota zásob se vypočítává přičtením předchozí hodnoty zásob k nově příchozím.
hodnota: :math:$80 + (4 * $16) = $144`.
        - Jednotková cena se vypočítá vydělením hodnoty zásob na množství skladem:
:math:`$144/12 = $12“.

      - Při dodání deseti produktů se používá průměrná jednotková cena k výpočtu zásob
Hodnota zásob je nezávislá na ceně zakoupeného zboží. Proto hodnota zásob
:math:`$144 + (−10 * $12) = $24`.

      - Získejte dva produkty za 6 dolarů každý:

        - Hodnota zásob: :math:`$24 + (2 * $6) = $36`
        - Náklady na jednotku: :math:$36/4=9`

.. poznámka::
Když si vyberete jako metodu „Average Cost (AVCO)“, změní se
hodnota v poli Cena produktu v příslušné kategorii produktů
Vytvoří nový záznam v inventárním hodnocení, které se používá k přizpůsobení hodnoty
produktu. Cena se pak automaticky aktualizuje podle průměrného nákupního koše.
cena zásob a náklady na kumulované nákupy, které byly schváleny.
objednávky.

....... tab:: První vstup, první výstup (FIFO)

Sleduje náklady na vstupy a výstupy v reálném čase a používá skutečnou cenu.
změnit způsob ocenění. Nejstarší nákupní cena se používá jako náklad pro další
dobré prodáno, dokud nebude celý sortiment daného produktu vyprodán. Když se další skladová
v pořadí se používá aktuální cena produktu na základě hodnoty konkrétního balení.

Tento způsob je zřejmě nejspolehlivějším způsobem ocenění zásob pro různé důvody.
ale je velmi citlivá na vstupní data a lidské chyby.

... seznam-tabulka::
:hlavičky: 1
:sloupek: 1

         * – Operace
           - Náklady na jednotku
           - Množství skladem
           - Vstupní hodnota
           - Hodnota zásob
         * -
           - $0
           - 0
           -
           - $0
         * - Získat 8 produktů za 10 dolarů za kus
           - $10
           - 8
           - 8 * $10
           - $80
         * - Získat 4 produkty za 16 dolarů/jednotku
           - $12
           - 12
           - 4 * $16
           - $144
         * - Dodat 10 produktů
           - $16
           - 2
           - | -8 * $10
             | -2 * $16
           - $32
         * - Získat 2 produkty za 6 dolarů za kus
           - $11
           - 4
           - 2 * $6
           - $44

Jak se vypočítává jednotková cena a skladová hodnota na každém kroku?

      - Při nákupu čtyř produktů za 16 dolarů každý:

        - Hodnota zásob se vypočítává přičtením předchozí hodnoty zásob k příchozí
hodnota: :math:$80 + (4 * $16) = $144`.
        - Jednotková cena se vypočítá vydělením hodnoty zásob na množství skladem:
:math:`$144/12 = $12“.

         - Když bylo dodáno deset výrobků, osm jednotek bylo zakoupeno za 10 dolarů a dvě jednotky byly
Koupil jsem za 16 $.

        - Nejprve se vypočítá vstupní hodnota pomocí násobku skladových zásob a
při koupi za:math:`(-8 * 10) + (-2 * 16) = -112`.
        - Hodnota zásob se vypočítává odečtením předchozí hodnoty od aktuální.
inventarizovaná hodnota: :math:`$144 - $112 = $32`.
        - Jednotková cena se vypočítá tak, že se hodnota zásob rozdělí počtem zbývajících kusů:
:math:`$32 / 2 = $16`.

      - Při přijetí dvou produktů za 6 dolarů je hodnota zásob :math:$32 + $12 = $44. Jednotková cena
:math:`$44 / 4 = $11`.

.. varování:
Změna metody ocenění výrazně ovlivňuje hodnotu zásob. Je velmi doporučeno
Před provedením jakýchkoliv úprav zde se nejprve poraďte s účetním.

.. viz též:
:doc:`používání inventarizační metody“

Při změně metody cenování se mění i produkty skladem, které používaly
:guilabel:`Metoda standardního nákladového účetnictví“ nemění hodnotu; namísto toho existující jednotky zachovávají svou
hodnota a každý produkt, který se pohybuje, ovlivňuje průměrnou cenu a cenu produktu.
změna. Pokud je hodnota v poli „Náklady“ na formuláři produktu změněna ručně, Odoo
generuje odpovídající záznam v hlášení „Ocenění zásob“.

.. poznámka::
Je možné používat různé nastavení hodnot pro různé kategorie produktů.

... skladovací prostory, účetní typy:

Druhy účetnictví
===================

S automatickým oceněním zásob se vytváří účetní případy podle zvoleného
účetní systém: *kontinentální* nebo *anglosaský*.

.. tip::
Zkontrolujte účetní režim aktivací :ref:`developer-mode` a přejděte na
:menu_selection:`Účetní aplikace --> Konfigurace --> Nastavení“.

Pak v poli „Hledat…“ vyhledejte Anglo-saské účetnictví, abyste zjistili, zda je tato funkce k dispozici.
je zapnutý. Pokud není zapnutý, používá se účetní režim Continental.

.... obrázek:inventarni_ohodnoceni_konfigurace/anglosasky.png
:align:center
:alt:Zobrazit funkci anglosaského účetního systému.

V účetnictví podle anglosaského vzoru jsou náklady na prodej zboží (COGS) uvedeny při prodeji výrobků nebo
dodána, což znamená, že náklady na zboží jsou uvedeny pouze jako výdaj v okamžiku, kdy je zákazník fakturován.
pro výrobek.

Pro manuální metodu ocenění nastavte účet „Náklady“ na „Oceňování zásob“.
druh aktiv; pro metodu automatického ocenění nastavte účet nákladů na účet *Náklady* nebo *Náklady - odpisy*.
Výdaje na nákup materiálu a výrobní náklady (např. *Náklady na produkci*, *Náklady na prodej zboží*, atd.)

V účetnictví Continentalu je náklad na zboží uveden v okamžiku, kdy je produkt přijat do
výrobní zásobou. Proto může být účet „Náklady“ nastaven buď na „Náklady“, nebo na „Náklad“.
Výnosový typ však často bývá nastaven na účet výdajů.

Viz položku :ref:`Náklad <sklady/náklad> a :ref:`Zásoba
sekce „Vstup/výstup“ (pro detaily o konfiguraci každé)
druh účtu.

.. skladové zásoby, sklady a náklady na účet:

Pokladna
---------------

Konfigurovat účet pro náklady, který se používá při manuální i automatické ocenění zásob.
Přejděte do sekce vlastností účtu produktu, který chcete použít.
(:menu_selection:"Inventář aplikace --> Konfigurace --> Kategorie produktů"). Pak vyberte existující
z účtu z nabídky „Účet výdajů“.

Pro ověření správného účtu klikněte na ikonu |pravý směr| vedle položky
právo na účet. Poté zvolte typ účtu podle informací níže.

.. záložky::

.... skupina-tab:: Anglosaský

... záložky::

.. skupina-tab:: Automatické

V anglosaském účetnictví pro automatickou oceňovací inventuru nastavte:guilabel:`Náklady
Převést účet „Výdaje“ na účet „Náklady“. Poté klikněte na ikonu vpravo od
účet.

V okně s upozorněním vyberte položku „Náklady“ nebo „Náklady na prodej“.
v seznamu „Typ“.

... obrázek: inventarni-ohodnoceni-konfigurace/externi-odkaz.png
:synchronizace: střed
:alt:Zobrazit pole „Výdajový účet“ a ikonu externího odkazu.

.. skupina-tab:: Manuál

Pro konfiguraci účtu „Náklady“ zvolte v poli „Způsob ocenění“ možnost „Sklad“.
výběrovém poli pole. Zkontrolujte typ účtu kliknutím na
ikona a poté zajistit, aby „Typ“ byl nastaven na „Aktiva“.

.. obrázek: inventarni-ohodnoceni-konfigurace/manual-anglosasky-nacin.png
:synchronizace: střed
:alt:Zobrazit pole **Nákladový účet**.

... skupina-tab: Kontinentální

... záložky::

.. skupina-tab:: Automatické

Nastavte účet pro výdaje na hodnotu „Výdaje“ nebo „Náklady“.
typu účtu „Příjem“.

.. skupina-tab:: Manuál

Nastavte účet pro výdaje na hodnotu „Výdaje“ nebo „Náklady“.
typu účtu „Příjem“.

.. skladové zásoby:

Vstupy a výstupy z obchodování s cennými papíry (jen automatizované)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chcete-li nakonfigurovat účet „Příjem zboží“ a „Výdej zboží“, přejděte na
:menu „Inventarapp“ -> „Konfigurace“ -> „Produktové kategorie“ a vyberte požadovanou
Kategorie produktu.

V poli „Ocenění zásob“ vyberte možnost „Automatické“. Tím se nastaví
V sekci „Vlastnosti účtu“ se zobrazí následující účty:

- :guilabel:`Účet pro ocenění zásob“: pokud je na produktu zapnuta automatická inventarizace.
Tento účet bude obsahovat aktuální hodnotu produktů.
- :guilabel:„Účetní kniha“: účetní deník, do kterého se automaticky zadávají položky
změna ocenění zásob.
- :guilabel:`Účet vstupů do zásob“: protijednoduché položky pro všechny příchozí pohyby zásob.
pokud není na zdrojovém místě nastaven konkrétní účet pro hodnotu.
Toto je výchozí hodnota pro všechny produkty v dané kategorii a lze ji také nastavit přímo na
každý produkt.
- :guilabel:`Výdejová účetní kniha“: protikladové položky pro všechny výstupy zboží budou
pokud není v cílové bance nastaven konkrétní účet pro oceňování.
lokalitě. Toto je výchozí hodnota pro všechny produkty v dané kategorii a může být také nastavena
na každém výrobku.

.. záložky::

.... skupina-tab:: Anglosaský

V anglosaské účetní knize je zahrnuto vedení zásobovacího účtu a výdejového účtu.
Účty jsou nastaveny na různé účty „Vlastní zdroje“. Tímto způsobem se dodávky
produkty a fakturaci zákazníkům vyrovnává účet Výdej skladu.
výrobky a dodavatelé fakturace vyrovnávají účet „Vstupy do zásob“.

Chcete-li změnit typ účtu, klikněte na ikonu vpravo od akcií.
účet vstupu a výstupu. V okně vyberte položku:guilabel:`Současné aktiva“
:guilabel:`Typ“ vyhledávací pole.

.. obrázek:: inventory_valuation_config/account-type.png
:synchronizace: střed
:alt:Zobrazte stránku nastavení účtu, zvýrazněte pole „Typ“.

Účet „Příjem zboží“ je nastaven na „Zásoby přechodné (přijaté)“, účet „Vybraný majetek“
typu.

... skupina-tab: Kontinentální

V kontinentálním účetnictví je vstupní a výstupní zásoba zahrnuty do účtu :guilabel:`Stock Input Account`
Účty jsou nastaveny na stejný účet „Vlastní zdroje“. Tímto způsobem lze jedním účtem spravovat
musí být vyvážené, když jsou nakupovány a prodávány.

... příklad::
Vstupní a výstupní účty zásob jsou oba nastaveny na „Zásoby dočasné (přijaté)“,
:guilabel:`Současné aktiva“ typ účtu. Mohou být také nastaveny na „Zásoby v mezidobí“.
(Doručeno)“, pokud jsou účty vstupu a výstupu přiřazeny ke stejnému
účet.

.. obrázek: inventarni-ohodnoceni-konfigurace/kontinentální-skladová-účetní kniha.png
:align:center
:alt:Zobrazit účty vstupu a výstupu akcií.

Účetní závěrka
=============================

Začněte v sekci „Účetnictví“ -> „Vyhodnocení“ -> „Rozvaha“. Klikněte na
V poli „Pouze aktiva“ rozbalte nabídku a hledejte podmenu.
„Ocenění akcií“, „Akcie - přijaté“ a „Akcie - přijaté“.
„(Dodáno)“ řádky.

.. tip::
V horní části panelu klikněte na tlačítko „Za období od“ a zobrazí se účetní záznamy.
záznamy do určitého data.

.. viz též:
   - :ref:`Skladové účty a co dělají <účetnictví/sklady_a_skladování/skladové_účty>“
   - :doc:`../../../finance/účetnictví/začínáme/škola cheatů

.. obrázek: inventarni-ohodnoceni-konfigurace/stav-skladu.png
:align:center
:alt:Podrobné rozdělení hodnoty majetku naleznete v aplikaci účetnictví Odoo.

Získat podrobnější informace kliknutím na ikonu :icon:`fa-ellipsis-v` :guilabel:`(ellipsis)`
Vpravo od požadovaného časopisu. Vyberte: guilabel:„Účetní kniha“ pro zobrazení seznamu všech
zápisy do deníku, kde každá položka v seznamu má ikonu :icon:`fa-ellipsis-v` :guilabel:`(ellipsis)`
klikněte, abyste zobrazili možnost „Zobrazit záznamy“ a otevřeli si individuální záznam.
vstup.

Dále lze k vyrovnání přidat poznámky volbou
Vyplňte pole „Poznámka“ a klikněte na „Uložit“.

.. obrázek: inventarni_ohodnoceni_konfigurace/denniky.png
:align:center
:alt:Zobrazit záznamy o hodnotě akcií v seznamu.
