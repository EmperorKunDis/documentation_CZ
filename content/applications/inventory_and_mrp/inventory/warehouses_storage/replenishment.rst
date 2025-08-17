
:ukrýt stránku obsahující obsah:

=============
Dodávky
=============

.. |MTO| nahradit za: zkratka: `MTO (Make to Order)`
.. |PO| nahradit za: :abbr:`PO (Příkaz k nákupu)`
.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`
.. |POs| nahradit za: zkratka: `POs (Purchase Orders)`
.. |MOs| nahradit za:: :abbr:`MOs (Výrobní objednávky)`
.. |SO| nahradit za: :abbr:`SO (Prodejní objednávka)`

Na sklad lze v Odoo doplnit třemi způsoby: podle pravidel *reordering rules*, nebo podle principu *make to order* (MTO).
trasy nebo použít *hlavní výrobní plán* (MPS).

Každý mechanismus doplňování vyvolává vytvoření nebo navrhnutí nákupního příkazu (PO).
výrobní objednávka (MO) s nejlepším výběrem podle obchodního procesu.

.. karty::

......karta: Řádky pro přeskupení
:target: doplnění / pravidla pro opětovné objednávání
:tag: Doporučeno


Automaticky navrhovat nebo vytvářet PO nebo MO, když zásoby klesnou pod minimální úroveň.

... karta: MTO
:target: doplnění/MTO
:tag:Začátečníkům přívětivé

Automaticky vytvářet faktury nebo dodací listy, když jsou potvrzeny objednávky na prodej.

... karta: MPS
:target: /manufacturing/workflows/use_mps

Spravujte dlouhodobé zásoby na základě vstupních prodejních předpovědí prostřednictvím panelu.

Strategie doplňování
========================

Zpráva o doplňování zásob a pravidla pro objednávání
-----------------------------------------

Pravidla přeskupení jsou pravidla, která lze nastavit tak, aby se udržovala minimální zásoba. Často
konfigurované tak, aby podporovaly výrobní nebo prodejní požadavky. Když zásoby klesnou na nebo pod
minimální úroveň, kterou Odoo vytváří (nebo navrhuje) nákupní nebo výrobní objednávku k doplnění zásob.
na maximální úroveň.

Při použití automatických pravidel pro opětovné objednávání Odoo vytvoří novou objednávku. Při použití manuálních pravidel Odoo navrhne
objednávky na doplnění zásob. Podrobné pokyny naleznete v souboru :doc:`report_replenishment
<dodání/zpráva> a :doc:`pravidla doplňování <dodání/reordering_rules>.

Hlavní body zahrnují:

- :ref:`Pravidla automatického přeřazování zásob <skladové zásoby/automatické přeřazování>“: Automaticky vytvářet
|POs| nebo |MOs| při poklesu pod minimální úroveň. To je pohodlné, ale méně přesné.
flexibilní.
- [:ref:`Pravidla ručního přeřazování skladů <inventory/warehouses_storage/manual-rr>“]: Vytváření návrhů
zprávu o doplňování pro kontrolu uživatele, která umožňuje provádět úpravy a objednávky v sériích
termíny.
- „Logika just-in-time“: Strategie doplňování zásob
jen takové, které jsou nezbytné k prevenci přebytku zásob.

.. viz také:
   - :doc:`dodávky/pravidla pro doplňování zásob“
   - :doc:`dodávka/zpráva

.. inventář/správa/produkty/strategie:

Na zakázku
-------------

Strategie MTO znamená, že nákup nebo výroba jsou spouštěny pouze po obdržení objednávky na prodej.
bylo potvrzeno. Tato strategie je doporučena v případě produktů na míru a poptávky
nepředvídatelné, omezená kapacita skladu a když jsou produkty cenné a zároveň levné
poptávka. V takových případech se nevyplatí mít skladové zásoby.

Oproti produktům doplňovaným pomocí pravidel pro opětovné objednávání je v Odoo automaticky spojena objednávka s
|PO| nebo |MO| vygenerované trasou MTO.

Další rozdíl mezi pravidly pro přesuny a |MTO| je v tom, že s |MTO| generuje Odoo návrh |PO| nebo
Po potvrzení |SO| se okamžitě vytvoří návrh |PO| nebo
Pokud předpovězená zásoba klesne pod stanovenou minimální hodnotu, bude zadáno MO.

Dále je také automaticky přidávána kvantita k položkám |PO| nebo |MO| podle změny předpovědi.
Pokud je tedy potvrzena jen PO nebo MO,

Trasa MTO je nejlepší strategií doplňování pro produkty, které jsou upravené a/nebo
Produkty, které nejsou skladem.

.. viz také:
:doc:`dodavatelské řetězce/MTO`

Hlavní výrobní plán
--------------------------

:abbr:`MPS (Master Production Schedule)` je panel, na kterém jsou zobrazeny produkty a jejich předpokládané
do systému se zadávají množství. Na základě potvrzených výrobních a nákupních objednávek
doporučuje objednat nebo vyrobit.

Toto je užitečný manuální nástroj pro sledování množství. Abbreviation: MPS (Master Production Schedule)
Schéma (Schedule) „v žádném případě“ nemělo být použito společně s pravidly přeskupování, protože automatizovaný proces
Přerušuje manuální způsob doplňování zásob.

.. viz také:
:doc:`../procesy/pouziti-mps`

.. toctree::
:tituly:

doplnění/množství
pravidla pro doplňování a obnovu zásob
replnění/zpráva
dodávky/doba dodání
sklady zásob
