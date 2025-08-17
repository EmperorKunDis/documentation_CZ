=================
Předpověď
=================

.. |SO| nahradit za: :abbr:`SO (objednávka na prodej)`
.. |SOs| nahradí za: :abbr:`SOs (objednávky na prodej)`
.. |RFQ| nahrazuje: zkratka: RFQ (požadavky na nabídku)
.. |POs| nahradit za: zkratka: `POs (objednávky na nákup)`
.. |PO| nahradit za: :abbr:`PO (objednávka na nákup)`
.. |MO| nahradit za: zkratka: `MO (manufacturing order)`
.. |MOs| nahradit za: zkratka: `MOs (manufacturing orders)`

Prognóza zásob v inventáři poskytuje aktuální pohled na předpokládané úrovně zásob, což pomáhá
Podniky mohou efektivně spravovat své zásoby. Tento výkaz je užitečný pro plánování a rozhodování.
výrobě, zajištění zásob pro nadcházející prodeje, výrobě a doplňování zásob.

.. důležité::
Předpovědní zpráva je k dispozici pouze u produktů, kde se sleduje zásoba, obvykle
je označován jako „produkt skladovatelný“.

Orientace v předpovědním výkazu
==============================

Prognóza je dostupná v sekci **Sklad**, **Nákup**, **Výroba** a
Aplikace pro **prodej**.

Chcete-li získat přehled o předpovědích, klikněte na tlačítko „Předpověď“
formě produktu. Alternativně lze zprávu otevřít také ze zakázky na prodej nebo nákup
kliknutím na ikonu „fa-area-chart“ vedle produktu a poté
výběrem ikony „OI-ARROW-RIGHT“ a poté výběrem možnosti „Zobrazit předpověď“.

.. obrázek: předpověď/so-predpoved.png
:alt:Objednávka s ikonou předpovědního výkazu zvýrazněnou.

Předpovědní výstup se skládá z grafu a tabulky. Graf vizualizuje pohyb cen.
Postupně se zobrazuje následující informace:

- :guilabel:`Na skladě“: aktuální zásoba fyzicky dostupná v skladu.
- :guilabel:`Příchozí“: množství očekávané z potvrzených objednávek nebo výrobních objednávek.
- :guilabel:`Výstupní“: množství vyhrazené pro objednávky nebo jiné výstupní operace.
- :guilabel:`Prognóza“: předpokládané zásoby na základě potvrzených a plánovaných operací.

.. obrázek: předpověď/předpovědní graf.png
:alt: Příklad grafu na předpovědi počasí.

Tabulka poskytuje podrobné metriky týkající se operací, včetně:

- :guilabel:`Dodávka“: Zobrazuje rezervované množství, zejména u vícekrokových operací.
- :guilabel:`Datum přijetí“: Datum přijetí položek.
- :guilabel:`Jednotky“: Počet jednotek zapojených do každé operace.
- :guilabel:`Použito pro“: Operace, ke které je akcie přidělena.
- :guilabel:`Datum dodání“: Datum, kdy se předpokládá pohyb zásob.
- :guilabel:`Očekávaný stav zásob“: Očekávané skladové zásoby.
- :guilabel:`Predikované s Pending“: Aktualizovaná skladová hodnota včetně pohybů zboží
bylo zváženo.

Rezervace a odstranění rezervace produktů
------------------------------

Uživatelé mohou přímo z předpovědního reportu rezervovat nebo odřazovat produkty, což zajišťuje skladové zásoby.
Alokace odpovídá potřebám provozu.

.. obrázek:: předpověď/tabulka-s-předpovědí.png
:alt: Podrobná část výstupu z předpovědního modelu, která ukazuje doplňování zásob a rezervy.

.. viz také:
:doc:`../objednavky/vyskladnuti/rezervační-metody`

Dodat produkty
------------------

Klikněte na tlačítko „Dodat“ v horní části zprávy, abyste otevřeli „Produkt“.
Replenish Pop-Up. Zde lze produkty doplňovat prostřednictvím nákupních objednávek od dodavatelů nebo
vyrobené. Vyberte „Množství“, „Přednostní trasa“ a „Dodavatel“.
před kliknutím na tlačítko „Potvrdit“.

Prognóza výroby
----------------------

Pro zobrazení dostupnosti výrobků klikněte na:
tlačítko. To zobrazuje předpokládané zásoby surovin a ukazuje, kolik je očekáváno
pro výrobní objednávky v budoucnu.

Prognóza výroby identifikuje nedostatek komponentů předtím, než se dostanou k výrobě
časové osy a pomáhá synchronizovat výrobní činnosti s poptávkou zákazníků.

.. obrázek: předpověď výroby/výrobní předpověď.png
:alt: Příklad výrobního předpovědního hlášení.

Aktualizace množství
---------------

Chcete-li ručně aktualizovat množství produktu, klikněte na tlačítko „Aktualizovat množství“. To otevře
Pop-up „Změnit množství produktu“. Zkontrolujte, zda je správně vybrána varianta produktu.
V poli „Produkt“ zadejte příslušnou hodnotu a v poli „Nový počet na skladě“
Klikněte na tlačítko „Použít“, když budete hotovi. Zpráva se poté aktualizuje, aby odrážela nový produkt.
množství.

Rezervace s více kroky
======================

Rezervované množství pro vícefázové příchozí a odchozí zásilky je uvedeno v
Sloupec „Dodávka“ v tabulce zprávy.

„Sklad v přepravě“ znamená produkty, které byly přijaty, ale jsou ve stádiu přepravy na jejich místo určení.
místo vstupu nebo kontroly kvality. „Volné zásoby ve výrobě“ odkazuje na dostupné produkty
přijaté na vstupním místě, ale ještě nezařazené do zásob.

Operace ovlivňující předpověď
========================================

Prognóza je ovlivněna různými operacemi, které mají na zásoby různý dopad.
Termíny dodání, plánované termíny výroby a očekávané datumy doručení všechny ovlivňují
Prognóza zásob.

Nabídky na dodání zboží (RFQ) okamžitě neovlivňují předpověď, protože produkty jsou
potvrzeno pro doplnění. |POs| však ovlivňují zprávu, protože produkty jsou očekávané.
přijít po potvrzení |PO|.

Potvrzeno |SOs| sníží předpovězený stav zásob a upraví zprávu podle plánované dodávky
datum. Potvrzené výrobní objednávky (MO) ovlivňují předpokládaný sklad zásob jak pro suroviny, tak
hotové výrobky.

Příklady použití
=========

Negativní množství
-----------------

Negativní předpovězená kvantita ukazuje, že poptávka převyšuje dostupné a
dostupný zásobní materiál v daném čase. To může nastat, pokud SO nebo MO vyžaduje více
než je aktuálně k dispozici nebo očekáváno, nebo kvůli zpoždění v dodávkách nebo výrobě.
procesu.

Ať už je příčina jakákoliv, když se na předpovědi zobrazí záporné číslo, slouží to jako
varování včas, které umožňuje firmám podniknout preventivní kroky. To může zahrnovat:

- Prioritizace konkrétních objednávek na prodej nebo výrobu.
- Upravit nákupní strategie, aby se urychlily objednávky.
- Spravujte očekávání zákazníků tím, že jim předem sdělíte možnost zpoždění.

.. obrázek: předpověď/množství.png
:alt: Příklad výstupu předpovědi s negativním množstvím.

Splité objednávky
------------

V následujícím příkladu je aktuálně nedostatek produktu „Skříň s dvířky“.
vyřídit více objednávek. Aktuální zásoby jsou rezervovány pro dodání.
„WH/OUT/00011“ a zbytek byl rozdělen mezi oba objednávky. Zbylý sklad je
očekává se s „WH/IN/00004“. Jakmile jsou přijaty, oddělují se od zbytku
objednávky.

.. obrázek: předpověď/předpověď-případ-použití.png
:alt:Příklad grafu předpovědi, který ukazuje rozdělení dodávky pro objednávku.

Pozdní příjem
------------

Dodací stůl lze použít k určení, zda příchozí dodávka dorazí včas.
vyřídit objednávku. Například je zobrazena s datem dodání dnes pro
pět krabic na kabely. Aktuální množství je nulové. Potvrzeno bylo „A“ (počet přijatých zásilek),
Očekávaný příjezd za tři dny.

Výpočet pro dnešek ukazuje hodnotu „-5“, protože potvrzená poptávka činí pět, ale aktuální
Zboží je na skladě nulové. Od doby, kdy byl vystaven doklad o přijetí zboží (datum obdržení), uplynulo více než 30 dní.
Dodávka je zpožděná.

Toto může být znamení k tomu, aby se současná dodávka uskutečnila co nejdříve, pokud je to možné, nebo aby byla přesunuta na jiný termín.
termínu dodání pro SO.
