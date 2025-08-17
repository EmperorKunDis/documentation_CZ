
:ukrýt stránku obsahující obsah:

===================
Rezervační metody
===================

Společnosti, které prodávají a dodávají zboží zákazníkům, musí zajistit, aby vždy měly skladové zásoby.
Aby mohli dodávat produkty včas, když jsou nové objednávky potvrzeny.

V Odoo lze tento problém vyřešit pomocí metod rezervace. Metody rezervace řídí způsob, jakým jsou produkty
dodací objednávka (DO) by měla obsahovat rezervace pro dodání, které zajistí, že jsou rezervovány
správné časy pro správné objednávky.

V Odoo existují tři různé způsoby rezervace: „Při potvrzení“, „Ručně“ a „Dříve“.
datum plánované události.

.. záložky::

....... tab:Při křtu

Reservace produktů **pouze** v případě potvrzení objednávky na prodej a **pokud je již skladová zásoba
dostupné.

.. tab:: Ručně

Jakmile je potvrzená cena, musí být dostupnost produktu kontrolována ručně a požadované množství
množství musí být rezervováno ručně.

.. tab::Před plánovaným datem

Můžete si vybrat konkrétní počet dnů, což je maximální počet dnů předtím, než
termínu, kdy by měly být rezervované produkty dodány.

Konfigurace
=============

Metody rezervace jsou nastaveny na jednotlivých typů operací. Chcete-li konfigurovat metody rezervace, přejděte do
Vyberte aplikaci „Správa zásob“ -> Konfigurace -> Typy operací. Pak vyberte požadovaný
typ operace. Nebo vytvořte novou kliknutím na tlačítko „Nový“.

Ve formuláři typu operace vyhledejte položku „Způsob rezervace“ v záložce „Obecné“.
možnost a vybrat způsob provedení této operace.

.. obrázek: rezervační metody/rezervační metody - operace typ pole.png
:align:center
:alt: pole rezervace na formuláři pro objednávku dodání.

..tip:
Pokud je zvolen způsob rezervace „Dříve než termín“, vytvoří se nová
:guilabel:`Rezervace před plánovaným datem“ se objeví pod tímto polem. Z tohoto pole získáte číslo
:guilabel:`dny předtím“ a :guilabel:`dny předtím, když je hvězdička“ lze změnit z výchozího
   `0`.

Změna hodnoty :guilabel:`dny předem` mění maximální počet dnů před plánovaným termínem.
datum, kdy by měly být rezervovány produkty.

Změna hodnoty `days before when starred` změní maximální počet dní před zobrazením.
Aby se vyhnul nedorozuměním, měl by si rezervovat datum, kdy byly zveřejněny (oblíbené) převody produktů.

...... obrázek: rezervační metody/rezervační metody-před plánovaným datem.png
:srovnání: do středu
:alt:Rezervace před termínem s vybraným předtermínovým způsobem rezervace.

Povinné aplikace
=====================

Dvě požadované aplikace, které **musí být** nainstalovány:ref:`<general/install>`, aby bylo možné rezervovat
Metody jsou aplikace Sales a Inventory.

.. poznámka::
Kromě dodacích objednávek lze rezervační metody použít také pro výrobní objednávky.
*dodavatel doplňkových služeb*, objednávky na *opravy* a *vnitřní převody*, pokud je to požadováno.
aby se tato funkce zapnula, nastavte další možnosti:

   - **Pro výrobní objednávky:** Nainstalujte aplikaci *Výroba* přes
:aplikace „Aplikace“, najděte aplikaci Manufacturing a klikněte na ni.
:guilabel:`Instalace“.
   - **Pro dodavatele doplňkových materiálů:** Přejděte na: menu: `Výroba --> Konfigurace
--> Nastavení a v sekci Operace zapnout Subdodavatelské práce.
Pak klikněte na tlačítko :guilabel:`Uložit“.
   - **Pro opravy:** Nainstalujte aplikaci „Opravy“ přes menu „Aplikace“.
aplikace, najít aplikaci Repairs a kliknout na „Instalovat“.
   - **Pro vnitřní převody:**Přejděte na: :menuselection:`Skladová aplikace --> Konfigurace -->
Nastavení“, a pod sekcí „Sklad“ zapněte „Skladovací místa“.
Pak klikněte na tlačítko :guilabel:`Uložit“.

Jakmile jsou tyto aplikace nainstalovány, nejsou zapotřebí žádné další funkce z nastavení.
rezervační metody fungovat. Budou k dispozici výchozím nastavením pro některé typy operací a
je možné zobrazit a změnit po kliknutí na:
Operační typy“ a poté kliknutím na konkrétní operační typ.

.. poznámka::
Když je změněn typ operace na „Pokladní doklad“,
:guilabel:`Typ operace“ formuláři, rezervace není k dispozici.

.. obrázek: rezervační metody/rezervační metody operace typ menu.png
:align:center
:alt:Zobrazení typů operací v podnabídce Konfigurace aplikace Sklad.

.. viz také:
   - :doc:`rezervační_metody/potvrzení`
   - :doc:`rezervační metody/ručně“
   - :doc:`rezervační_metody/před_plánovaným_datem“

.. toctree::
:tituly:

rezervační metody/potvrzení
rezervace/ručně
reservation_methods/před_plánovaným datem
