Zobrazit obsah
:ukrýt stránku obsahu:

================
Prodejní faktury
================

„Prodejní cenová nabídka“ nebo „nabídka“ je dokument zaslaný zákazníkovi, který obsahuje odhadované náklady.
smluvní podmínky pro dodávku zboží nebo služeb. Jakmile jsou přijaty, může být nabídka změněna na objednávku na prodej, která
Slouží jako konečná dohoda před dodáním a fakturací.

Přehled prodejního toku
===================

Citace zapadá do širšího prodejního toku, který spojuje různé fáze interakce zákazníka
od počátečního zájmu až po zaplacení.

Typický průběh je následující:

#*. Citace*: Návrh zaslaný zákazníkovi s podrobnostmi o produktu a cenou.
#*.Objednávka k prodeji*: Vytvořená automaticky po přijetí nabídky zákazníkem a potvrzující
prodej.
#*Dodání* (pokud je k dispozici): Produkty jsou dodávány nebo služby poskytovány.
#Faktura: Konečná faktura je vystavena na základě objednávky nebo dodaných produktů/služeb.
#*.Platba*: Zákazník uhradí fakturu a dokončí tak obchodní cyklus.

Tento proud pomáhá firmám sledovat celý životní cyklus prodeje a udržet informace v souladu.
mezi aplikacemi.

V Odoo jsou cenové nabídky konfigurovány v aplikaci **Prodej**. Můžete je také vygenerovat z jiných aplikací
Jako součást prodejního procesu:

- CRM:Převést příležitosti na citaci pro další zpracování
na potenciální obchody.
- **Pomocná služba**: :doc:`Vytvoření nabídky z požadavku <../../services/helpdesk/advanced/after_sales>`
při nabídce placených služeb nebo produktů.
- Předplatné: :doc:`Nabídněte opakované služby <../subscriptions> před
zahájení automatického fakturačního cyklu.

.. karty:

....... karta: Vytvořit citaci
:target: obchodní nabídky/vytvořit nabídku

Vytvářet, konfigurovat a odesílat nabídky zákazníkům.

....... kartu:: šablony citátů
:target: obchodní nabídky/vzorová nabídka

Nastavte si šablony cenových nabídek, abyste mohli rychleji posílat přizpůsobené nabídky.

......karta:: Volitelné produkty
:target: prodejní nabídky/volitelné produkty

Nabídnout zákazníkům užitečné a související produkty, aby se zvýšily prodeje.

......karta::Online podpisy pro potvrzení objednávek
:target: prodejní nabídky/získat podpis k ověření

Každý zákazník má možnost objednávku potvrdit elektronickým podpisem přímo na prodejním dokladu.

.......karta:: Potvrzení o online platbě
:target: prodejní faktury/získat zaplaceno za ověření

Každý zákazník má možnost objednávku potvrdit prostřednictvím online platby přímo na prodejní faktuře.

...... karta:: Termíny pro citace
:target: prodejní nabídky/termín

Určete termíny pro cenové nabídky, aby zákazníci jednali včas.
uzavírání obchodních dohod.

... karta: doručování objednávek a faktur na různé adresy
:target: prodejní faktury/různé adresy

V objednávce specifikujte samostatné adresy pro dodání a fakturaci.

....... karta::Varianty produktů v cenových nabídkách a objednávkách
:target: prodejní nabídky / objednávky a varianty

Přidejte varianty produktů do prodejních objednávek, abyste mohli nabídnout další možnosti jednotlivých produktů.

......karta:: Stavěč cen v PDF
:target: obchodní nabídky/PDF nabídkový formulář

Přidejte do nabídek vlastní PDF soubory, abyste zvýšili hlavičku a design dokumentu.

Prodejní ceny v obchodních transakcích
==================================

Prodejní citaci lze považovat za klíčový krok v prodejním procesu, který spojuje mezeru mezi zákazníkem
prvotní dotaz na zboží a služby a konečná smluvní dohoda o platbě.
dodání. Cenová nabídka také poskytuje transparentnost v cenách a pomáhá oběma stranám vyjednávat a
Dokončit podmínky před závazkem.

Prodejní faktury hrají v obchodních transakcích zásadní roli tím, že definují rozsah a cenu toho, co
prodává přímo koncovému zákazníkovi. Uvádí jasná očekávání ohledně cen, dodacích lhůt, daně a
podmínky platby; a poskytnout dokumentovanou fázi, kde lze obchodní dohodu vyjednávat před
bylo dohodnuto.

Základní složky prodejního odhadu
===================================

Kvalitní nabídka by měla obsahovat následující body:

- Číslo a datum citace: Jedinečný identifikátor pro sledování a odkazování.
:doc:`datum vydání a platnosti <sales_quotations/deadline>“. V aplikaci Odoo **Sales**
Číslo citace je přiřazeno podle standardního názvu, jakmile je potvrzeno.
- Informace o zákazníkovi: jméno a kontaktní údaje zákazníka, jakož i
:doc:`fakturační a dodací adresa <objednávky/různé_adresy>“.
- Produkty a služby: Seznam položek k nákupu včetně množství
specifikace (pokud je potřeba) a cena za jednotku.
- Platební podmínky a ceník: Konfigurované dohody a
pravidla pro cenotvorbu a úhradu této konkrétní smlouvy o dodávce zboží.
- Speciální cenová nabídka: Volitelné: Slevy a slevové akce
<produkty/ceny/ceník> pro aktualizaci a/nebo změnu jednotlivých produktů.
- Celkové náklady a měna: Souhrnné celkové částky za produkt nebo službu včetně poštovného
relevantní daně.

V aplikaci pro obchodní zástupce společnosti Odoo mohou nabídky obsahovat další podrobnosti a konfigurace, které přidávají
více podrobností a informací, např. :doc:`vzory nabídek <sales_quotations/quote_template>“.
„plány předplatného“ (viz „Sales/Subscriptions“), a „jméno prodejce“.
<výrobky/vytvořit-nabídku>.

.. obrázek: sales_quotations/sales-quotation.png
:alt:Nedokončená prodejní nabídka v aplikaci Odoo **Prodej**.

.. toctree::


sales_quotes/create_quote
sales_quotes/quote_template
sales_quotes/optional_products
sales_quotes/get_signature_to_validate
sales_quotes/get_paid_to_validate
sales_quotes/term
faktury/různé adresy
sales_quotes/orders_and_variants
sales_quotations/pdf_quote_builder
