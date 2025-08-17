==================
Výkaz o přidělení
==================

.. |SO| nahradit za: :abbr:`SO (objednávka na prodej)`
.. |SOs| nahradí za: :abbr:`SOs (objednávky na prodej)`
.. |MO| nahradit za: zkratka: `MO (manufacturing order)`
.. |MOs| nahradit za: zkratka: `MOs (manufacturing orders)`
.. |RfQ| nahradit za: zkratka: RfQ (žádost o nabídku)

Při plnění objednávek na prodej (SO) nebo při nákupu komponentů pro výrobní objednávky (MO) je
někdy je nutné vybrat si jeden z nich, ať už SO nebo MO. V situacích, kdy
Nedostatek zásob na skladě k pokrytí každé poptávky SO nebo MO, což zajišťuje, že jsou produkty a komponenty
je nezbytná pro prioritní objednávky.

V Odoo Manufacturing jsou v |MOs| používány výkazové listy pro přidělování produktů konkrétním prodejcům.
pokyny |SOs| nebo součástky pro konkrétní |MOs|. To zajišťuje dostupnost produktů nebo součástek
Pro tyto objednávky a nebyly použity omylem.

Konfigurace
=============

Pro použití výkazů o přidělených zdrojích je nutné mít zapnutou funkci „Výkaz o přidělených zdrojích pro výrobní objednávky“.
zapnout. Pro přístup k této možnosti přejděte na: „Výroba -> Konfigurace -> Nastavení“.
a zaškrtněte políčko vedle :guilabel:`Zpráva o přidělení pro výrobní objednávky“. Pak klikněte
:guilabel:`Uložit“.

Pro produkty, které se prodávají, je také nutné je nakonfigurovat tak, aby mohly být zahrnuty do |SOs|.
Pro to začněte procházet: „Sklad --> Zboží --> Zboží“ a vyberte
produktu. V poli „Název produktu“ na formuláři produktu se ujistěte, že
zaškrtnout políčko „Může být prodáno“.

Přidělit produkty
=================

Pokud chcete přidělit produkty nebo komponenty z |MO| do |SO| nebo jiného |MO|, začněte
Navigace na: menu-vyber: „Výrobní aplikace“ -> „Provoz“ -> „Dodací objednávky“. Klikněte
:guilabel:`New` vytvořit nový |MO|.

V poli „Produkt“ na formuláři MO vyberte produkt a zadejte množství.
vytvořené v poli „Množství“. Nakonec klikněte na tlačítko „Potvrdit“, abyste potvrdili |MO|.

Další část procesu přidělování zásob se odvíjí podle aktuálního množství produktů, které jsou
vyráběné a zda existují SO nebo MO, které produkt vyžadují, ale
nebyly již přiděleny jednotky.

Pokud existují stávající |SOs| a |MOs|, které produkt vyžadují, **a pokud je málo jednotek
zboží skladem k vyřízení těchto objednávek, pak se použije ikona „fa-list“ s guilabel „Allocation“
Tlačítko se objeví na horní části stránky, jakmile je potvrzeno |MO|.

Pokud existují stávající SO a MO, které produkt vyžadují, **a pokud je dostatek jednotek**
zboží skladem k vyřízení těchto objednávek. Pak se použije ikona „fa-list“ s popiskem „Allocation“.
Tlačítko Smart se objeví pouze na horní části stránky po označení úkolu jako hotového kliknutím
:guilabel:`Vyrobit vše“.

.. obrázek: přidělení/tlačítko pro přidělení.png
:align:center
:alt: Chytrý tlačítko pro přidělování na začátku MO.

.. poznámka::
Pokud neexistují žádné stávající SO a MO, které by produkt vyžadovaly, pak:
:guilabel:`Alokace“ tlačítko nevyskočí ani v případě, že je úkol označen jako hotový.

Klikněte na tlačítko „Smart“ s ikonou „fa-list“ a textem „Allocation“, abyste otevřeli „MRP Reception“.
Zpráva pro MO. Tato zpráva obsahuje otevřené objednávky nebo MO podle typu
produkt vyrobený v originálním MO.

Přidělit dodacímu příkazu
--------------------------

Pokud MO obsahuje hotový výrobek, zpráva uvádí otevřené objednávky na dodání pro které
Kvůli nedostatku produktu se zatím nevyhlašují rezervace.

Příklad:
Pro výrobu tří kusů židle na šlapání je vytvořen modul MO. Kliknutím
:guilabel:`Alokace“ tlačítko na |MO| otevře zprávu o alokaci, která seznamuje s dostupnými
objednávky na dodání, které vyžadují jeden nebo více houpacích křesel.

Klikněte na tlačítko „Přidělit všechny“ vpravo vedle konkrétního objednávkového lístku, abyste přiřadili produkty pro každou
Požadované množství k vyřízení objednávky.

Příklad:
Pokud objednávka vyžaduje jednu položku o čtyřech kusech produktu a jednu položku o jednom kusu
produktu kliknutím na tlačítko „Přidělit všechny“ přiřadí pět jednotek produktu pro splnění obou
množství.

Alternativně klikněte na tlačítko „Přidělit“ vedle konkrétního množství a přidejte pouze produkty do této
množství a ne jiné v objednávce.

Příklad:
Pokud objednávka vyžaduje jednu položku o čtyřech kusech produktu a jednu položku o jednom kusu
produkt, kliknutím na tlačítko „Přiřadit“ vedle množství jednotky produktu přiřadí
tohoto množství, ale čtyřem jednotkám nebyly přiřazeny žádné produkty.

.. obrázek:allocation/product-reception-report.png
:align:center
:alt:Výkaz o příjmu pro MRP, který obsahuje hotové výrobky.

Přidělit MO
--------------

Pokud |MO| obsahuje složku, zpráva uvádí všechny otevřené |MOs| pro které je k dispozici kvantita
komponenty ještě nebyly rezervovány.

Příklad:
Výroba tří jednotek dřeva je potřeba pro výrobu komponentu.
*křeslo s pohybem* produktu. Kliknutím na tlačítko „Přídělový systém“ ve výzvě MO se otevře
zpráva o přidělení, která uvádí volné křeslo na houpačce |MOs|, které vyžadují jeden nebo více kusů dřeva.

Klikněte na tlačítko „Přiřadit všechny“ nebo „Přiřadit“ vedle konkrétního |MO|.
Přiřaďte komponenty k tomuto |MO|.

.. obrázek: rozdělení/příjem zprávy o komponentách.png
:align:center
:alt:Hlášení o příjmu pro MO obsahující součástky.

Odebrat produkty
-----------------

Po přiřazení produktů k množství v dodacím listu nebo komponenty k MO
Tlačítko „Přiřadit“ se změní na tlačítko „Odpojit“. Klikněte na „Odpojit“.
odvolat přidělené produkty z této kvantity a učinit je dostupnými pro další kvantity.

Tisk etiket
------------

Po kliknutí na tlačítko „Přidělit všechny“ nebo „Přidělit“ se zobrazí tlačítko „Tisk štítků“.
Kliknutím na tlačítko „Tisk štítku“ vpravo od buď jednoho, nebo druhého tlačítka se zobrazí možnost výběru.
Tlačítko vytvoří a stáhne dokument ve formátu PDF s jedním štítkem pro každý produkt, který byl přiřazen.
Tyto štítky slouží k označení každého produktu jako vyhrazeného pro konkrétní objednávku.

.. obrázek:: allocation/assigned-labels.png
:align:center
:alt:Štítky, které vytvoříte kliknutím na tlačítko Print Labels nebo Print Label.
