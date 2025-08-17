==============
Zpracování objednávky
==============

Když zákazník objedná na vašem e-shopu, jsou tři typy záznamů potřebné k zpracování.
Odoo:

- :ref:`Objednávky na prodej <zpracování/prodej>“
- „Příkazy k dodání“ (viz. „Zpracování a dodání“);
- :ref:`Faktury a právní požadavky <zpracování/právo>“.

.. prodej/provoz:

Prodejní objednávky
============

Stav objednávky a platby
------------------------

Prvním krokem, když zákazník přidá produkt do košíku, je vytvoření nabídky. Objednávky
je možné spravovat buď z webu nebo aplikace Sales (e-commerce).
objednávky lze automaticky přiřadit k určitému prodejnímu týmu, pokud se přepnete na:
Konfigurace > Nastavení. V sekci „Obchod – proces objednávky“ vyberte
:guilabel:Prodejní tým nebo prodejce, který bude řešit objednávky z e-commerce.

.. obrázek: order_handling/handling-salesteam.png
:align:center
:alt:Přidělování objednávek na e-shop do prodejního týmu nebo prodejce

Objednávky najdete pod: `Website --> eCommerce --> Orders/Unpaid Orders`. Každá
objednávka prochází jiným stavem:

- **Citace**: nový produkt byl přidán do košíku, ale zákazník se ještě nezaregistroval.
procesu vyzvednutí zboží.
- **Přijato**: zákazník prošel procesem objednávky a potvrdil objednávku.
ale platba zatím nebyla potvrzena.
- Objednávka: zákazník prošel procesem objednání, potvrdil objednávku a
Pokud je platba přijata.

.. obrázek: order_handling/handling-status.png
:align:center
:alt:Stavy objednávek v e-commerce

Vozík zapomenutý na ulici
--------------

Zapomenutý košík představuje objednávku, kterou zákazník neukončil.
potvrzení objednávky. U těchto objednávek je možné odeslat e-mailovou
automaticky zákazníkovi. Chcete-li tuto funkci aktivovat, přejděte na:
Nastavení a v sekci „E-mail a marketing“ zapněte „Automaticky odeslat
nevyřízené emaily z pokladny. Jakmile je aktivní, můžete nastavit časový odstup po kterém bude
odesílání a přizpůsobení e-mailového šablonu použitého.

.. poznámka::
Pro e-maily o opuštěných košících musí zákazník buď během objednávky zadat své kontaktní údaje.
případně přihlášený, když produkt přidali do košíku.

.. _zpracování a dodání:

Dodací příkazy
===============

Průtok dodávek
-------------

Jakmile je potvrzena cenová nabídka, automaticky vznikne objednávka na dodání. Dalším krokem je
zpracovat tuto dodávku.

Balíčky pro elektronický obchod zpravidla obsahují vybrání zboží, přípravu balení a tisk štítku.
poštovní štítky a poštovné pro zákazníka. V závislosti na počtu objednávek, strategii nebo
Zdroje, tyto kroky lze považovat za jednu nebo více akcí v Odoo.

Automatický e-mail může být odeslán zákazníkovi, když stav převodu v Odoo je „hotovo“.
Zapnout funkci v nastavení
:doc:`Seznam skladových zásob </applications/inventory_and_mrp/inventory>` aplikace.

.. poznámka::
Pokud zákazníci mohou platit při vyzvednutí objednávky v obchodě nebo převodem,
Citaci nelze potvrdit a zásoby nejsou rezervovány. Objednávky musí být potvrzeny
ručně rezervovat produkty skladem.

.. viz též:
   - :doc:`../../skladové hospodářství a plánování výroby/Sklad/Příjem a výdej/Nastavení/Fakturace`
   - :doc:`../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/labels`
   - :doc:`../../inventar-und-mrp/einlagerung-und-auslagerung/konfiguration/verpacken`

Vrácení a vrácení peněz
-------------------

Zákazníci mohou objednávku vrátit pouze prostřednictvím online formuláře. Není možné vracet zboží
podle způsobu vrácení nebo typu produktu.

Platbu v plné výši lze přímo z objednávkového rozhraní odeslat zákazníkovi.
Za prvé musí být zapnutý poskytovatel plateb.

.. viz též:
   - :doc:`/aplikace/prodej/prodej/produkty-ceny/vrácení zboží
   - :doc:`/aplikace/služby/podpora/pokročilé/po prodeji“
   - :doc:`/aplikace/finance/platební-poskytovatelé`

.. _povaha/právní:

Faktura a právní požadavky
==============================

Posledním krokem při objednávce v elektronickém obchodě je vygenerování faktury a její odeslání zákazníkovi.
Podle typu podnikání (B2B nebo B2C) lze vygenerovat fakturu automaticky
(B2B) nebo na základě požadavku zákazníka (B2C). Tento proces lze automatizovat, pokud (a kdy) je k dispozici
Platba je „potvrzena“.

Pro automatické fakturaci přejděte na: `Website --> Konfigurace --> Nastavení`.
V sekci „Fakturace“ zapněte „Automatické fakturování“.
