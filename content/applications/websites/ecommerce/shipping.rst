========
Dodání
========

Odoo eCommerce umožňuje nastavit různé způsoby doručení, díky čemuž si zákazníci mohou vybrat
jejich preferovanou možností při :doc:`checkoutu <checkout>“. Tyto metody zahrnují :ref:`externí poskytovatele
<ecommerce/dodání/externí poskytovatel>`, :ref:"vlastní možnosti <ecommerce/dodání/vlastní metoda>"
například paušální nebo bezplatné poštovné, místní dopravci přes
:doc:`Sendcloud </aplikace/skladování a řízení výroby/obsluha skladu/konfigurace/zaslání přes Sendcloud“
nebo:ref:`Na základě pravidel <inventory/shipping/rules>`,
:ref:`výdej v obchodě<ecommerce/doprava/vydej-v-obchode>.

.._ecommerce/dodavatel-sluzeb:

Součástí je integrace externích poskytovatelů
=============================

Pro doručení produktů můžete propojit svou databázi s externími dopravci.
</aplikace/skladové hospodářství/příjem a výdej/konfigurace/třetí dopravce>
např. :doc:`FedEx </applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/fedex>
:doc:`UPS </applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/ups_credentials>`,
nebo:doc:`DHL </aplikace/skladování a řízení výroby/příjem a expedice/konfigurace/dhl_credentials>.
Připojovací modul spojuje tyto poskytovatele a automatizuje :doc:`sledování štítků.
</přílohy/skladové zásoby a řízení výroby/Sklad/Přijetí a expedice/Konfigurace štítků> a expedici.
procesy.

Chcete-li povolit třetí stranu pro doručení, přejděte na: „Webové stránky --> Konfigurace -->
Nastavení“, posuňte se do části „Doručení“ a vyberte požadovaného dopravce.
a stiskněte tlačítko „Uložit“.

Přejděte na:menu:Website --> Konfigurace --> Způsoby doručení a vyberte způsob doručení
v seznamu k:ref:`konfigurovat <inventar/versand/lieferungsart-konfigurieren>“.

.. viz též:
   - Dopravci třetích stran

   - :doc:`Gelato </applications/sales/sales/gelato>`

.. důležité:
Pole pro definování dalších poplatků musí být vyplněno **v třetích stranách dodání
účet poskytovatele**, i když nemáte v plánu účtovat zákazníkům žádný další poplatek. Pokud ne
Pokud chcete aplikovat poplatek, zadejte hodnotu 0. Pokud pole necháte prázdné, nemůžete nastavit cenu dopravy.
Vypočítána a zákazníkovi je nabídnuta možnost zvolit si jiný způsob doručení.

Margin dodací sazby
-----------------------

Přidat další poplatek k základnímu tarifu dopravy (například na pokrytí dodatečných nákladů) se můžete přihlásit do
dopravce a nastavte požadovanou částku v příslušném poli. Přepravní koncovka získá tuto
a zahrnuje ji do konečné ceny při placení. Kontaktujte svého dopravce pro další pomoc
s touto konfigurací.

Alternativně zadejte do účtu třetí strany číslo 0 a pak nastavte poplatek v Odoo.
Pro to je potřeba se přesunout na stránku požadovaného způsobu dopravy.
„Nastavení způsobu dodání“ a zadejte marži v položce „Marže“.
na poli „Sazba“ přidat procento k nákladům na dopravu a/nebo „Přirážka“.
pole, do kterého se přičte pevná částka.

.. důležité:
Pole pro definování dalších poplatků nesmí být prázdné ve třetích stranách.
účet poskytovatele.

..._ecommerce/doprava/vlastní metoda:

Vlastní způsob doručení
======================

Musí se vytvořit specifické způsoby doručení, například:

- integrovat kurýrní společnosti přes Sendcloud

- konfigurovat konkrétní pravidla (např. poskytovat dopravu zdarma při objednávce nad určitou částku).
konkrétní poskytovatel služeb.
- konfigurovat dopravu „Pevná cena“ nebo dopravu „Založenou na
Pravidla (<inventory/shipping/rules>).

Pro vytvoření vlastní metody doručení přejděte na: „Webové stránky --> Konfigurace --> Dodání“
Metody, klikněte na „Nový“ a vyplňte pole :ref:`vlastnosti
<Inventura/Přijetí a odeslání/Dodací metody – podrobnosti>.

V poli „Dodavatel“ vyberte „Na základě pravidel“ nebo
:ref:`Fixní cena <sklad/dodání/fix>“.

..tip:
Při :ref:`konfiguraci <inventory/shipping_receiving/configure-delivery-method> dodací metody
Metoda, kterou můžete použít, je:

   - Omezte jej na konkrétní webovou stránku:
vybráním v poli „Webová stránka“.
   - Klikněte na tlačítko „Testovací prostředí“ a přepněte se do
:guilabel:`Provozní prostředí“. Pak klikněte na :guilabel:`Nepublikované“ a poté na :guilabel:`Zveřejnit“
způsob doručení a umožnit jej návštěvníkům webových stránek.
   - Použijte záložku „Dostupnost“ k definování podmínek
<Inventar/Versand und Empfang/Verfügbarkeit> pro způsob dodání založený na objednávce.
obsah nebo cíl.

..._elektronického obchodování, dopravy a vyzvednutí v kamenné prodejně:

Klikni a vyzvedni
===============

Pokud chcete zákazníkům umožnit rezervovat produkty online a platit/vyzvedávat je v kamenných prodejnách, postupujte podle těchto kroků:

#Přejděte na: menu: „Webová stránka“ --> „Konfigurace“ --> „Nastavení“.
#.Přejděte do sekce „Dodání“ a zapněte možnost „Klikni a vyzvedni“.
:guilabel:`Uložit“.
#Klikněte na ikonu „fa-arrow-right“ a zvolte možnost „Nastavení míst pro vyzvednutí“.
<Inventar/Versand und Empfang/Konfigurieren des Versandverfahrens> a zkontrolujte, že je
:guilabel:`Provozovatel“ pole je nastaveno na „Vyzvednutí v obchodě“.
#V záložce „Prodejny“ klikněte na „Přidat řádek“ a vyberte sklad(y), kde
Zákazníci si mohou vyzvednout své objednávky.
#Jakmile je vše nastaveno, klikněte na tlačítko „Nepublikovat“ a změňte stav na
:guilabel:`Zveřejnit“ a zpřístupnit zákazníkům zvolený způsob doručení.

.. poznámka::
   - Když je produkt skladem, zobrazí se na stránce výrobku :doc:`lokalizátor.
na stránkách „Produkty“ a „Dokumentace“ pro způsob platby „Vyzvednutí“. Když si zákazník vybere způsob platby „Vyzvednutí“, nemůže zvolit místo vyzvednutí.
pokud je zboží na daném místě vyprodané.
Volba „<ecommerce/products/stock-management>“ pro vyprodané produkty není podporována.
   - Pokud je možnost „Zobrazit dostupné množství“ aktivní pro
produktu mohou zákazníci vidět skladové zásoby dostupné pro každé skladování na daném místě.
výběr na stránce produktu.
   - Každému skladu musí být přidělen **úplný adresní údaj**, aby bylo možné zobrazit jeho umístění s přesností.
zákazníkům. Neúplné adresy brání zobrazení skladu.
   - Možnost vyzvednutí na prodejně není k dispozici u služeb.
