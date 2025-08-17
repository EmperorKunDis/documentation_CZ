==================
Kategorie skladování
==================

Kategorie skladování se používá s pravidly pro ukládání zboží (viz dokument Putaway Rules), jako další atribut umístění
automaticky navrhovat optimální skladovací prostory pro produkty.

Postupujte podle těchto kroků, abyste dokončili nastavení:

#:ref:`Zapněte funkci Kategorie skladu <inventory/routes/enable-storage-categories>`
#:ref:`Vytvořte kategorii skladování <inventory/routes/define-storage> s konkrétními omezeními
#Přidělte kategorie skladům (viz inventory/routes/assign-location).
#Přidejte kategorie skladování jako atribut do pravidla „umístit“.


.. viz též:
:doc:`uklidit“

.. poznámka::
Přiřazení kategorií skladovým místům říká Odoo, že se jedná o specifická místa.
požadavky, jako je například teplota nebo dostupnost. Poté Odoo hodnotí tyto lokality na základě
definovanou kapacitu a doporučí nejvhodnější na přepravním listu skladu.
..._inventář/cesty/povolit kategorie skladu:

Konfigurace
=============

Pro povolení kategorií skladu přejděte do: „Inventář aplikace --> Konfigurace --> Nastavení“.
Poté v sekci „Sklad“ zkontrolujte „Uložení“ a
Funkce „Složené trasy“ je zapnuta.

Poté aktivujte funkci „Kategorie úložiště“ a nakonec klikněte na „Uložit“.

.. obrázek: skladovací kategorie/povolit kategorie.png
:align:center
:alt:Zobrazit funkci Kategorie úložiště.

... inventář/cesty/definovat skladování:

Určete kategorii skladování
=======================

Kategorie skladování s konkrétními omezeními **musí být vytvořena** před jejím použitím
míst, aby bylo možné vybrat optimální skladovací místo.

Pro vytvoření kategorie skladu přejděte na: „Inventář aplikace --> Konfigurace --> Sklad
Kategorie, a klikněte na tlačítko Vytvořit.

V poli „Kategorie úložiště“ zadejte název kategorie.
pole.

Možnosti jsou k dispozici pro omezení kapacity podle hmotnosti, produktu a typu balení.

.. poznámka::
Maximální hmotnost může být spojena s kapacitou balení nebo produktu (např. maximálně 100 kusů).
produkty o celkové hmotnosti dvou set kilogramů.

Zatímco je možné omezit kapacitu podle produktu a druhu balení na stejném místě, může
je praktičtější ukládat věci v různých množstvích na různých místech, jak je vidět na obrázku.
příkladu: :ref:`kapacitou balíčkem <inventory/routes/set-capacity-package>`.

Záložka „Nové produkty“ definuje, kdy je lokalita považována za dostupnou pro ukládání nových výrobků.
produkt:

- Pokud je položka prázdná, může se do ní přidat pouze produkt.
- Pokud jsou produkty stejné“: Produkt se může přidat pouze tehdy, pokud je stejný produkt
Jsou tam už teď.
- :guilabel:`Povolit smíšené produkty“: v této lokalitě může být uloženo několik různých produktů
Ve stejnou dobu.

.. tip::
Když je kliknuté tlačítko „Místo“, zobrazí se ikona s názvem „Uložiště“ a ukazuje, které skladovací místa patří do dané kategorie.
Byl přidělen.

Kapacita v hmotnosti
------------------

Ve formuláři kategorie skladu (:menuselection:`Sklad --> Konfigurace --> Sklad
Kategorie“), nastavte maximální hmotnost produktu v poli „Maximální váha“. Tento limit se vztahuje
do každé lokalitě přiřazené této kategorii skladování.

Kapacita podle produktu
-------------------

V záložce „Kapacita podle produktu“ klikněte na tlačítko „Přidat řádek“, zadejte
jejich kapacitu v poli „Kapacita“.

.. příklad::
Zajistěte, aby bylo vždy uloženo maximálně pět „Velkých skříní“ a dvě „Pracovní desky s pravým výhledem“.
jediném skladovém místě, uvedením těchto množství v záložce „Kapacita produktu“.
v podobě zásobníkového formuláře.

.... obrázek::storage_category/kapacita-podle-produktu.png
:align:center
:alt:Zobrazit kategorii skladu omezenou počtem produktů.

... inventář/trasy/nastavit kapacitu balíčku:

Kapacita balíčkem
-------------------

Pro společnosti používající balíčky podle :doc:`balíčků <../../product_management/configure/package>“ se stává
možné zajistit kontrolu skladovacích kapacit v reálném čase podle druhu balení (např. palety, bedny,
krabice, atd.

.. důležité::
Zapněte funkci „Pakety“ v sekci „Nastavení“ aplikace Inventář.
Nastavení zobrazit kartu „Kapacita balení“.

.. příklad::
Vytvořte pravidla pro skladování palet s vysokou frekvencí, vytvořením skladovacího prostoru „Vysoká frekvence palet“
kategorie.

V záložce „Kapacita balíčku“ zadejte počet balíčků pro určené místo.
:guilabel:`Druh balení“, nastavte maximální počet „palet“ na „2,00“.

.. obrázek::kategorie_ukladiště/ukládání.png
:align:center
:alt: Vytvořte kategorii ukládání na stránce.

... inventář/trasy/přiřazení umístění:

Přiřaďte k místu
==================

Jakmile je kategorie uložení vytvořena, přiřaďte ji k místu. Vyhledejte místo přes
:menu:„Aplikace skladu“ -> „Konfigurace“ -> „Místa“, vyberte požadované místo.
Poté vyberte vytvořenou kategorii v poli „Kategorie úložiště“ .

.. příklad::
Přidělte kategorii skladování „Vysokofrekvenční palety“ (která omezuje množství palet na jakékoliv místo).
do dvou palet) do podložky „WH/Sklad/palety/PAL 1“.

.... obrázek: kategorie_ukladiště/kategorie_umisťování_ukládání.png
:align:center
:alt:Když je vytvořena kategorie skladu, může být propojena s místem ve skladu.

.. inventář/cesty/vlastnost nastavení skladování:

Pravidlo odsunu
============

S kategorií „Skladování“ (viz inventory/routes/define-storage) a s kategorií „Lokalita“ (viz inventory/routes/define-location).
<inventar/routy/přidělit místo> a vytvořte pravidlo pro ukládání zboží podle návodu
do položky menu:Inventarizace aplikace --> Konfigurace --> Pravidla pro ukládání.

Klikněte na tlačítko „Vytvořit“ a vytvořte pravidlo pro ukládání zboží. V poli „Má kategorii“
položku nového pravidla pro ukládání, vyberte kategorii skladu.

.. příklad::
Pokračujme v příkladu výše. Kategorie skladování „Vysokofrekvenční palety“ je přiřazena k
pravidlo pro ukládání, které nasměruje palety limonády do míst s „vysokofrekvenčními paletami“.
Kategorie skladu: přidělené jim v souvislosti s trasami (viz inventář/trasy/přidělit lokalitu).

.. obrázek: kategorie-skladu/chytře-uklidit.png
:align:center
:alt:Kategorie skladování používané v různých pravidlech pro ukládání.

Příklad použití: omezení kapacity balení
===================================

Omezit kapacitu skladovacího místa konkrétním počtem balíčků:
kategorii s kapacitou balíčku menší než inventory/routes/set-capacity-package.

Pokračujme v příkladu výše. Kategorie skladování „Vysokofrekvenční palety“ je přiřazena k
Lokality „PAL1“ a „PAL2“.

Poté se nastaví pravidla pro skladování („pravidla skladování“), takže jakákoliv paleta přijatá
Sklad je určen k uložení na lokalitách „PAL1“ a „PAL2“.

V závislosti na počtu palet skladovaných v každém ze skladů se jedna paleta
Pokud je přijata plechovka s citronádou, následují tyto scénáře:

- Pokud jsou pole PAL1 a PAL2 prázdná, paleta je přesměrována na WH/Sklad/Palety/PAL1.
- Pokud je pole PAL1 plné, paleta se přesměruje na WH/Sklad/Palety/PAL2.
- Když jsou pole „PAL1“ a „PAL2“ plná, paleta je přesměrována na „WH/Sklad/Palety“.

