=========
Incoterms
=========

:zkr. „Incoterms“ jsou standardizované obchodní podmínky používané v
mezinárodní transakce, které definují práva a povinnosti kupujících a prodávajících.
zavádí povinnosti související s dodáním zboží, přechodem rizik a
dělení nákladů mezi účastníky obchodu. Incoterms specifikují důležité podrobnosti, například
místě přechodu rizika a nákladů z prodávajícího na kupujícího.
doprava, pojištění, celní odbavení a další související aspekty transakce.

.. poznámka::
Výchozí nastavení obsahuje všechny 11 Incoterms v Odoo:

   - **EXW**: Ex works
   - **FCA**: Zdarma k přepravě
   - **FAS**: Volný po boku lodi
   - FOB: Zdarma na palubě
   - **CFR**: Cena a náklady na dopravu
   - **CIF**: Cena, pojištění a přeprava
   - **CPT**: Doprava zaplacena do
   - *CIP* - doprava a pojištění proti všem rizikům
   - **DPH**: Doručeno na místo bez nakládky
   - **DAP**: Dodáno na místě
   - **DAP**: Dodáno, clo zaplaceno

.. viz též:
   - :doc:`../reporting/intrastat`
   - :doc:`/faktury-zakaznikum`
   - :doc:`../faktury_dodavatelů`

.. _incotermy/faktury:

Určete Incoterm
==================

Pro ruční definici Incoterms vytvořte fakturu nebo účet a klikněte na záložku „Další informace“.
vyberte :guilabel:`Incoterms“.

Místo podle INCOTERMS
-----------------

Na faktuře nebo zálohové faktuře lze přidat místo, které je pro zvolené obchodní podmínky významné.
v poli „Další informace“ v záložce „Místo dodání“.

.. příklad::
Pokud je zvolený kód Incotermu „CIF“ (Cena, pojištění, přeprava), pak se může jednat o
cílový přístav, kam budou zboží doručeny.

.. _incotermy/výchozí:

Výchozí konfigurace obchodních podmínek Incoterms
==============================

Můžete nastavit výchozí pravidlo pro Incoterm, které bude automaticky vyplňovat pole Incoterm na všech nových
vytvářely faktury a zálohové faktury. Pod položkou „Účetnictví / Fakturace“ -> „Konfigurace“ ->
Nastavení“ a v sekci „Faktury zákazníkům“ vyberte příslušný obchodní termín.
:guilabel:`Výchozí obchodní podmínky“ pole.
