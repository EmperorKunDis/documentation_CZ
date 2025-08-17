===================
Spravovat faktury dodavatelů
===================

...výpočetní techniku, nákup, správa smluv a správa obchodů:

.. |PO| nahradit za: abbr: PO (objednávka)
.. |POs| nahradit za: zkratka: `POs (Purchase Orders)`
.. |RfQ| nahradit za: zkratku `RfQ (požadavek na nabídku)`
.. |RfQs| nahradit za: :abbr:`RfQs (žádosti o nabídku)“

„Faktura od dodavatele“ je faktura za produkty a služby, které společnost zakoupila u dodavatele.
dodavatel. Faktury dodavatele zaznamenávají pohledávky za dodavateli a mohou obsahovat částky dlužné dodavatelům
zboží a služby zakoupené, spotřební daně, přepravné a poplatky za doručení a další.

V Odoo lze vystavit fakturu dodavateli na různých místech nákupního procesu podle
V nastavení aplikace Purchase je zvolena politika *kontroly účtu*.

Politika kontroly účtů
=====================

Pro konfiguraci výchozí politiky kontroly faktur přejděte do:
Konfigurace --> Nastavení“, a posuňte se do části „Fakturace“.

Funkce „Kontrola faktur“ nabízí dvě možnosti nastavení politiky:
:guilabel:`Přijaté množství“.

Zvolená politika se stane výchozím nastavením pro všechny nové produkty vytvořené v této organizaci. Každá z těchto politik funguje takto:

- :guilabel:`Počet objednaných položek“: vytvoří fakturu od dodavatele, jakmile bude potvrzena objednávka.
Produkty a množství v objednávce slouží k vytvoření návrhu faktury.
- :guilabel:`Přijaté množství“: faktura se vystavuje až po dodání celého nebo části objednávky.
Dodávka byla přijata, produkty a množství obdržené jsou použity k vytvoření návrhu faktury.

.. obrázek: manage/manage-configuration-settings.png
:align:center
:alt: Změňte nastavení aplikace Purchase App, aby vám umožnila kontrolovat výdaje.

Jakmile vyberete politiku, klikněte na tlačítko „Uložit“ pro uložení změn.

..tip:
Pokud produkt potřebuje jiný režim kontroly než nastavení v aplikaci Purchase,
že kontrolní politika daného produktu může být převedena na kartu „Nákup“ v
produktu, a vybrat požadovanou politiku v poli „Kontrolní politika“.

.. obrázek:: manage/manage-product-form.png
:synchronizace: střed
:alt: Kontrolní politika na formuláři produktu.

Třístranné shody
--------------

Politika třístranného shody zajišťuje, že faktury dodavatelů jsou uhrazeny pouze jednou (nebo někdy), pokud je zboží vráceno.
byly přijaty objednávky na nákup (PO).

Aby se aktivovalo třístranné shodování, přejděte na: „Koupit aplikaci“ --> Konfigurace -->
Nastavení“ a posuňte se do části „Fakturace“.

Zaškrtněte políčko vedle 3-way matching a klikněte na tlačítko Save.

.. důležité:
Tato funkce „třístranného shodování“ je **pouze** určena k práci s účtem „Bill
Politika kontroly nastavena na: „Přijaté množství“.

Vytvářejte a spravujte faktury od dodavatelů na základě příjmových dokladů
==========================================

Když jsou produkty přijaty do skladu společnosti, vytváří se pro ně příjemky.
pokud zpracují přijaté množství, mohou si vybrat možnost vytvoření faktury dodavatele přímo z
formulář skladového potvrzení.

Podle nastavení může být vytváření faktur dodavatele dokončeno
různé fáze nákupního procesu.

Počet objednaných kusů
------------------

Vytvářet a spravovat dodavatelské faktury pro příjmy s nastavenou politikou „Bill Control“ na hodnotu „Povoleno
Když se podíváte na množství, nejprve přejděte do aplikace Přidat a klikněte na tlačítko Nový.
Dashboard požadavků na nabídku.

Tím se otevře nová žádost o nabídku (RfQ). Na prázdné žádosti o nabídce (RfQ) zadejte
„Dodavatel“ a klikněte na „Přidat řádek“ pod záložkou „Produkt“, abyste přidali
Na zakázku vyráběné výrobky.

V seznamu produktů vyberte produkt z rozevírací nabídky v poli „Produkt“ a
zadejte množství, které chcete objednat do pole „Množství“.

Jakmile bude objednávka připravena, klikněte na tlačítko „Potvrdit objednávku“, aby byla |RfQ| převedena na |PO|.

Poté klikněte na tlačítko „Vytvořit fakturu“ a otevře se vám „Faktura pro dodavatele“.
formulář v stavu „Návrh“ (viz gui-label:Draft). Zde přidejte datum fakturace do políčka „Datum fakturace“
pole.

Jakmile bude faktura připravena, potvrďte ji kliknutím na tlačítko „Potvrdit“ v sekci „Faktura dodavatele“.

..tip:
Protože je nastavená kontrola faktur na položky objednané v množství, lze potvrdit návrh faktury.
ještě před tím, než byly přijaty jakékoliv produkty.

Jakmile dostanete platbu, klikněte na tlačítko „Registrace platby“ v horní části faktury.
Nahrát ho.

Tím se zobrazí okno „Registrace platby“, kde je možné provést platbu.
Můžete vybrat „Záznamy“ a „Metodu platby“.

Dále v návrhu zákona: „Částka“, „Datum platby“ a „Poznámka“.
Pokud je třeba, můžete v tomto okně upravit pole „Referenční číslo“ (dfn: Reference Number).

Jakmile je hotovo, klikněte na tlačítko „Vytvořit platbu“ a dokončete vytváření faktury pro dodavatele.
Takže na formuláři RfQ se zobrazuje zelené tlačítko „Zaplaceno“.

.. obrázek: manage/manage-draft-vendor-invoice.png
:align:center
:alt:Formulář faktury dodavatele pro kontrolu objednaného množství.

Přijaté množství
-------------------

Vytvořit a spravovat faktury dodavatelů pro příjmy s nastavenou politikou kontroly účetních dokladů na hodnotu *Příjem
množství* nejprve přejděte do aplikace „Nákup“ a klikněte na „Nový“.

Tím se otevře nová tabulka s názvem „RFQ“. V poli „Dodavatel“ zadejte název dodavatele a klikněte na
:guilabel:`Přidat řádek“ pod záložkou „Produkt“ pro přidání produktů do objednávky.

V seznamu produktů vyberte produkt z rozevírací nabídky v poli „Produkt“ a
zadejte množství, které chcete objednat do pole „Množství“.

Jakmile bude objednávka připravena, klikněte na tlačítko „Potvrdit objednávku“, aby byla |RfQ| převedena na |PO|.

.. důležité:
Při použití kontrolní politiky „Přijaté množství“ je třeba kliknout na tlačítko „Vystavit fakturu“ před jakýmkoli
Při přijetí produktu se zobrazí okno chybové hlášky „Nesprávná operace“.

Pro Odoo je nutné, aby alespoň částečně byly přijaty položky zahrnuté v |PO|.
vytvoření faktury dodavatele.

.. obrázek:: manage/manage-user-error-popup.png
:synchronizace: střed
:alt:Překlep uživatele při kontrole příjmu kvantitativních omezení.

Na kartě PO klikněte na tlačítko „Přijatá faktura“ a zobrazí se vám formulář přijaté faktury.

Zde klikněte na „Potvrdit“ a zaregistrujte množství „Dostupné“.

Poté se vraťte zpět do PO a klikněte na tlačítko „Vytvořit fakturu“.

Otevře se formulář „Předběžná faktura“ v režimu „Návrh“. Zde přidejte fakturační údaje.
datum v poli „Datum faktury“. Jakmile bude připravena, potvrďte fakturu kliknutím
V horní části návrhu klikněte na „Potvrdit“.

Jakmile dostanete platbu, klikněte na tlačítko „Registrace platby“ v horní části faktury.
Nahrát ho.

Tím se zobrazí okno „Registrace platby“, kde je možné provést platbu.
Můžete vybrat „Záznamy“ a „Metodu platby“.

Dále v návrhu zákona: „Částka“, „Datum platby“ a „Poznámka“.
Pokud je třeba, můžete v tomto okně upravit pole „Referenční číslo“ (dfn: Reference Number).

Jakmile je hotovo, klikněte na tlačítko „Vytvořit platbu“ a dokončete vytváření faktury pro dodavatele.
Takže na formuláři RfQ se zobrazuje zelené tlačítko „Zaplaceno“.

Správa faktur od dodavatelů v účetnictví
=================================

Faktury dodavatelů lze vytvářet také přímo z aplikace *Účetnictví*, bez nutnosti vytvořit
objednávku na nákup.

Přejděte na položku „Účetní aplikace“ -> „Dodavatelé“ -> „Faktury“ a klikněte na „Nový“.
To odhaluje prázdný formulář „Faktura dodavatele“.

Do pole „Dodavatel“ vložte dodavatele. V záložce „Fakturační řádky“ klikněte
:guilabel:`Přidat řádek“ pro přidání produktů.

Vyberte produkt z rolovací nabídky v poli „Produkt“ a zadejte množství.
pořadí v poli „Množství“.

Vyberte datum faktury (guilabel:Bill Date) a nakonfigurujte další potřebné informace. Nakonec klikněte
Klikněte na tlačítko „Potvrdit“, abyste potvrdili fakturu.

Po potvrzení klikněte na záložku „Záznamy“ a zobrazte si záznamy o účtech.
Tyto časopisy jsou obyvatelé podle konfigurace na odpovídajícím :guilabel:`Dodavatel`.
:guilabel:Produkt“ tvarů.

Pokud je třeba, klikněte na položku „Kreditní poznámka“ a přidejte do faktury kreditní poznámku.
Může být přidán číslo faktury (reference).

Jakmile je vše připraveno, klikněte na „Registrace platby“, následované „Vytvořit platbu“ pro dokončení.
:guilabel:`Faktura dodavatele“.

..tip:
Chcete-li propojit návrh zákona s již existujícím objednávkovým lístkem, klikněte na
Před kliknutím na tlačítko „Potvrdit“ zadejte :guilabel:`Auto-Complete`, a poté vyberte možnost ze seznamu.

Faktura se automaticky doplní informacemi z vybraného |PO|.

.... obrázek: manage/manage-auto-complete.png
:synchronizace: střed
:alt:Drobná nápověda k automatickému doplňování políček v návrhu faktury od dodavatele.

Účtování v sérii
=============

Faktury dodavatelů lze zpracovávat a spravovat v sadách v aplikaci *Účetnictví*.

Přejděte na:menu-selection:'Účetní aplikace --> Dodavatelé --> Faktury'. Pak klikněte
V levém horním rohu vedle sloupce „Číslo“ a pod
Tlačítko „Nový“.

Toto vybere všechny stávající faktury dodavatele s :guilabel:`Stavem` :guilabel:`Zasláno`.
:guilabel:`Návrh“.

Klikněte na tlačítko „Tisk“ (ikonka „fa-print“) a poté vyberte faktury, které chcete vytisknout.

Klikněte na tlačítko „Registrace platby“ a vytvořte a zpracujte platbu za více faktur najednou.

.. poznámka::
Platby, jejichž :guilabel:`Stav` je uveden jako :guilabel:`Připsáno`, lze fakturovat.
sady. Platby v stádiu „Návrh“ **musí být** zadány před tím, než budou zahrnuty do
v hromadném vyúčtování.

Kliknutím na tlačítko „Registrace plateb“ se otevře okno „Registrace plateb“.
Přejděte do okna s náhledem, vyberte „Deník“, který mají faktury odeslat, a zvolte „Zaplaceno“.
Datum, vyberte způsob platby.

Můžete také z této okénka spojit platby dohromady podle skupin. Pokud
Pokud je tato volba zaškrtnuta, vytvoří se pouze jedna platba místo jedné na fakturu. Tento způsob
Zobrazí se, pokud je funkce „Skládané platby“ zapnutá v nastavení
Aplikace „Účetnictví“.

Jakmile je hotovo, klikněte na tlačítko „Vytvořit platbu“. To vytvoří seznam účetních záznamů
oddíl. Všechny záznamy v tomto seznamu jsou spojeny s příslušnými fakturami dodavatelů.

.. obrázek: manage/manage-batch-billing.png
:align:center
:alt:Okno pro platbu registrace sestav.

.. viz též:
:doc:`kontrola_faktur“
