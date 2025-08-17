==========================
Systém řízení výjezdů
==========================

Funkce „Systém řízení expedice“ v Odoo se používá k plánování a sestavování zásilek. Hlavní funkce
zahrnuje:

- Nabíjení vozidel**: Skupinové produkty pro konkrétní dopravce, přiřazení :doc:`souborů
a přepravu z výrobních linek na skladové plochy a řízení vozidel podle flotily.
kapacita. Tím se zajistí, že správné produkty budou zabaleny do vhodných nákladních vozidel pro dodání.
- „Správa flotily <../../../../hr/fleet>“: Sledování a správa kapacity vlastních vozidel
dodávkové vozy.

Konfigurace
=============

Pro používání systému pro správu pošty je nutné dokončit následující nastavení:

#:ref:`Nainstalujte aplikaci Fleet <general/install>.“
#Nastavit vozidlo: ref: kapacita (objem a hmotnost)
<Inventar/Versand und Empfang/Fahrzeugkapazität>.
#Vstupte do vozidla: doc: 'model auta (y) <../../../../hr/fleet/models>'.
#Povolit „nutné funkce“ (<inventory/shipping_receiving/inventory-features>).
**Aplikace Inventář**
#Zřídit vozidla jako prostředek pro doručení.
<sklad/přijímání a výdej/doručovací metoda pro přepravce>.
#Vytvořte místo pro přistání:ref:`<Inventář/příjem a výdej/místa pro přistání>“.

... inventarizaci, přijímání a expedici zboží, kapacitu vozidel:

Kapacita vozidla
----------------

Konfiguraci kapacity vozidla proveďte v aplikaci Fleet: Menu --> Konfigurace -->
Kategorie.

Poté klikněte na „Nový“ pro přidání nové kategorie nebo do existující kategorie pro její úpravu.
Do pole „Název“ zadejte typ vozidla (např. „Pick-up truck“, „Van“ nebo „Cargo van“).
nákladní automobil). Pak zadejte kapacitu vozidla v poli „Maximální hmotnost“ (v kilogramech) a
:guilabel:„Maximální objem“ (v metrech krychlových).


.. obrázek: odeslání/kategorie.png
:alt:Kategorie vozidel s definovanou hmotností a objemem.

.. poznámka::
Jednotky měření kapacity vozidla jsou přiřazovány na globální úrovni v
aplikace „Nastavení“, v sekci „Jednotky měření“.

.. obrázek: /odeslání/nastavení.png
:alt:Zobrazit nastavení jednotek měření.

.. viz také:
:ref:`Kategorie vozidel <fleet/categories>`


Model automobilu
---------

Konfigurace vozidla je nutná při přidávání vozidel do Odoo. Ujistěte se, že máte správné
Vyberte kategorii pro automobilový model. To automaticky aplikuje hmotnostní a objemové kapacity
na všechny vozy daného typu.

Pro konfiguraci přejděte na: „Flotila aplikace --> Konfigurace --> Modely“.

V seznamu Modelů vyberte existující model nebo v horním levém rohu klikněte na New.
vytvořit nový model. Pak nastavte příslušné pole :guilabel:`Category` na odpovídající hodnotu
kategorie vozidla.

.. viz také:
:doc:`Vytvořit vzor vozidla <../../../hr/fleet/models>`


...Inventarizace, přijímání a vydávání zboží:

Nastavení inventáře
------------------

Dále přejděte na položku „Aplikace Inventář --> Konfigurace --> Nastavení“ a zapněte požadované
funkce pro řízení odesílání.

V sekci „Provoz“ zaškrtněte políčko „Přenosy vln, skupin a šarží“.
zaškrtávací políčko pro přípravu objednávek k expedici.

V sekci „Doprava“ zaškrtněte možnosti „Způsoby doručení“ a „Odeslání“.
Zaškrtnutím políčka „Management System“ umožníte konkrétním vozidlům být nastaveny jako přepravci
<výdejní místo/příjem zásilky/způsob doručení pro přepravce>.

V sekci Sklad zatrhněte políčko „Skladovací místa“ a přiřaďte
Specifické lokality v skladu jako nakládací zóny pro dodávkové vozy.

Pak, až budou všechny konfigurace dokončeny, ujistěte se, že kliknete na tlačítko :guilabel:`Uložit“.

...Inventarizace, přijímání a dodávky pro dopravce:

Metoda doručení
---------------

Poté přiřaďte každému dodávkovému vozidlu jako dopravci konfigurací způsobu doručení.

Pro konfiguraci způsobu doručení přejděte na: „Inventář aplikace --> Konfigurace --> Doručování
Metoda. Vyberte existující způsob doručení nebo klikněte na „Nový“.

.. viz také:
:doc:`Nastavit způsob doručení <../setup_configuration>`

Do pole „Způsob doručení“ zadejte název způsobu doručení. Doporučujeme
použít identifikační údaje, například popis vozidla a registrační značku („Nákladní automobil
123-ABCDE.

Od dodavatele se očekává, že bude vše řídit interně, takže nastavte hodnotu :guilabel:`Provider` na
„Fixní cena“ nebo „Na základě pravidel“. Pro více informací o způsobu dopravy
cena je vypočítána podle článku „Metoda doručení“ v části „Konfigurace nastavení“.

Poté nastavte „Produkt pro doručení“, který je produkt, který se zobrazuje jako produkt zákazníka.
:ref:`přepravní poplatky <sklad/doručení/faktura>“ na faktuře nebo v objednávce.

Volitelně v záložce „Dostupnost“ nastavte země a státy.
nebo:guilabel:Zip prefixes, aby se omezilo rozsah místní dodávky.

.. obrázek: doručení/metoda-doručení.png
:alt: Forma dodání.

Příklad dodací metody s nastavením „Zip Prefixes“ na kód poštovní zóny v San Franciscu.

.. skladování, přijímání a odbavování:

Přístavní lokality
--------------

Každá nakládací rampa musí mít své vlastní umístění. Chcete-li vytvořit nebo konfigurovat místo pro nakládací rampy, přejděte na
:menu:„Aplikace pro inventář“ --> „Konfigurace“ --> „Místa“.

Klikněte na požadované místo, které otevře formulář „Lokalita“. V poli „Další informace“
V části „Informace“ zaškrtněte políčko „Je to místo pro připojení“.

.. obrázek: odeslání/dokovací místo.png
:alt: Konfigurace umístění.

Stránka konfigurace umístění s zaškrtnutou políčko „Je to místo Docku“.

Nakládejte si
===========

Jakmile je nastavení dokončeno, :ref:`přidělujte objednávky dopravci.
<inventarizace/přijetí a expedice/přiřazení dopravce> a :ref:`skupují je do balíků
„Vytvořit balíček“. Pak „Konfigurovat formulář pro vytváření balíčků
<Inventar/Výdej a příjem/Formulář pro vytvoření balíčku>, pokud je třeba.

Pro seskupení produktů přejděte do aplikace „Sklad --> Provoz --> Dodávky“.
zobrazuje seznam odeslaných zásilek.

.. viz také:
Protože tento článek je o konkrétním použití případu, podrobně popište každý způsob vybírání.
jejich články věnované tomuto tématu.

   - :doc:`../vybírání/balení`
   - :doc:`Vlnová sklizeň <../picking_methods/wave>`
   - :doc:`../vybírání metod/cluster`


... inventarizaci, přijímání a přiřazování dopravců:

Přidělení dopravce
------------------

Zobrazte sloupec *Nosič*, pokud není viditelný výchozí nastavením, kliknutím na
Ikona „Nastavení“ (ikona v pravém horním rohu) a zaškrtnutí
zaškrtávací políčko „Dodavatel“.

..tip:
Další užitečné sloupce, které lze zapnout, jsou :guilabel:`ZIP kód`, :guilabel:`Hmotnost pro zaslání“ a
:guilabel:`Počet přepravených zásilek“.

Vyberte objednávky dodání pro danou sérii zaškrtnutím políček v levém sloupci. Poté klikněte na
pole „Dodavatel“ v poli „Line“. V zobrazeném seznamu vyberte požadované vozidlo.
:ref:`doručovací metoda <sklad/přijímání a expedice zásilek/doručovací metoda pro přepravce>“.
Otevře se okno s názvem „Potvrzení“, které ukazuje počet objednávek přidávaných do
výběr. Klikněte na tlačítko „Potvrdit“ a dopravce bude aktualizován pro všechny vybrané záznamy.

.. obrázek: odeslání/nastavení dopravce.png
:alt:Nastavit nosič.

Dodací metoda „Nákladní automobil 1-MER-001“ je nastavena jako :guilabel:`Dopravce“ pro dvě objednávky dodání.

.. inventarizaci, přijímání a vytváření balíčků:

Vytvořit sérii
------------

Při nastavení dopravce začněte přidávat objednávky do balíčku nebo vlnového přenosu zaškrtnutím políčka.

.. poznámka::
Pokud je již objednávka dodání přiřazena k převodu zásob, přiřazení převodu zásob zde
**neaktualizovat** jej.

Poté klikněte na tlačítko „Akce“ (ikona „fa-cog“) a poté buď na „Přidat do sady“
nebo: „Přidat do vlnovky“. V okně s upozorněním zkontrolujte, že je nastaveno „Přidat“ na „A
nový převod“, pak klikněte na „Potvrdit“.

.. obrázek:: příkaz/přidat do vlny.png
:alt: Příkladová vlna.

Dodací objednávky jsou vybírány pro seskupení do vlnového přenosu.

Alternativní metoda vytváření sérií
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Další místo pro vytváření sérií je aplikace „Sklad“ (v menu vyberte položku Inventory).
Klikněte na ikonu „(tři tečky)“ v kartě „Objednávka dodání“.
Výsledné rozbalovací nabídce klikněte na „Připravit sadu“.

.. poznámka::
V rozevíracém seznamu „Správa dopravy“ najdete další nástroje pro správu vozového parku:

   - :guilabel:`Správa sérií“: otevřít seznam sérií
   - :guilabel:`Dock Dispatching“: otevřete týdenní kalendář plánovaných operací
   - :guilabel:`Balení podle trasy“:Kanbanový pohled na balení seskupená podle způsobu plnění
   - :guilabel:`Kalendář“: otevřete hodinový kalendář s plánovanými operacemi
   - :guilabel:`Statistiky“: otevřená tabulka přesunů

.. obrázek:: příprava-souboru.png
:alt:Zobrazit možnost přípravy sady z nabídky Správa přepravy.

... inventarizaci, přijímání a expedici zboží.

Forma balíčku
----------

V poli převodu vložte následující údaje:

- :guilabel:`Odpovědný“: zaměstnanec, který je přiřazen k vyskladňování. Nechte prázdné, pokud může vyskladnit *kdokoliv*
tento sběr.
- :guilabel:`Typ operace“: z rozevírací nabídky vyberte typ operaci pod kterou je
Přeprava je rozdělena do kategorií.
- :guilabel:`Datum plánované kontroly“: určuje datum, do kdy je osoba odpovědná za
dokončit převod na výstupní místo.
- :guilabel:`Místo nakládky“: vyberte místo nakládky.
- :guilabel:`Vozidlo“: vyberte vozidlo, které se automaticky vyplní :guilabel:`Kategorie vozidla“.
- „Kategorie vozidla“: zobrazte, jestli objednávka překročila kapacitu vozidla.


Příklad:
:guilabel:`Volumen´ je šedivý, protože kapacita byla vyčerpána.

.. obrázek:: dispatch/batch-form.png
:alt:Zobrazit formulář pro více položek.

Připravte se na dodávku
~~~~~~~~~~~~~~~~~~~~~~

Aby řidič mohl připravit, klikněte na tlačítko „Mapa“ v horní části seznamu nebo vlny.
zobrazit místa doručení na mapě. Vybráním konkrétního zásilkového pořadí se zobrazí jeho umístění.

.. poznámka::
Tlačítko „Mapa“ je viditelné pouze pro převody s stavem „Ve výrobě“.

.. obrázek: odeslání/mapa.png
:alt:Zobrazit mapu v Odoo s informacemi o dodávkách.

Dále použijte tlačítko „Zobrazit na mapách Googlu“ k vytvoření trasy z skladu.
do výdejních míst.

.. obrázek:: /soubor/google-map.png
:alt:Zobrazit trasu na mapě Google.

