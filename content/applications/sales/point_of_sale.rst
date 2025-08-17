Zobrazit obsah
:ukázat obsah:

=============
Místo prodeje
=============

S aplikací **Odoo Point of Sale** můžete snadno spravovat své obchody a restaurace. Aplikace funguje na jakémkoliv zařízení s
webový prohlížeč, i když jste dočasně offline. Pohyby produktů jsou automaticky zaznamenávány v
Vaše zásoby, získáte reálné statistiky a vaše data jsou konsolidována v rámci všech obchodů.

.. viz též:
   - „Návody k Odoo: Návody k pokladně <https://www.odoo.com/slides/point-of-sale-28>“
   - :doc:`Dokumentace k IoT boxům </aplikace/obecné/iot>`

.._pos/session-start:

Zahájit sezení
===============

Ve svém **POS dashboardu** klikněte na „Nový účet“ a v poli „Otevřené hotovosti“
Obrazovka „Kontrola“, klikněte na „Zahájit sezení“ nebo na „Pokračovat“.
Prodej, pokud je seance již otevřená.

.. poznámka::
:dokument:„Ve stejném sezení může být přihlášen více uživatelů <point_of_sale/employee_login>“
Ve stejný čas. Avšak jednu sezení lze otevřít pouze na jednom prohlížeči.

.. _prodej:

Prodat produkty
=============

Klikněte na produkty a přidejte je do košíku. Chcete-li změnit množství, klikněte na „Qty“
Do políčka zadejte počet produktů pomocí klávesnice. Chcete-li přidat slevu nebo upravit produkt
**cena**, klikněte na příslušné pole :guilabel:`% Discount“ nebo „Cena“ a zadejte částky.

Jakmile je objednávka dokončena, pokračujte na stránku „Zaplacení“ kliknutím na tlačítko „Platba“.
Zadejte způsob platby, částku a klikněte na „Potvrdit“. Klikněte
„Nový pořádek“ a přesunout se k dalšímu zákazníkovi.

.. obrázek: point_of_sale/pos-interface.png
:alt: rozhraní pro relace s terminálem.

..tip:
   - Můžete používat jak „,“ tak „.“ jako oddělovač desetinných čísel na klávesnici.
   - Výchozí volbou je „Hotovost“, pokud částku zadáte bez výběru způsobu platby.

.. poznámka::
Systém může načíst pouze omezený počet produktů pro účinné otevření. Klikněte
:guilabel:`Hledat více“ pokud požadovaný produkt není automaticky načten.

.._pos/zákazníci:

Sestavte zákazníky
=============

Registrace zákazníka je nutná k tomu, aby se mu přičítaly věrnostní body a udělovaly se jí odměny.
<prodejní místo/cenotvorba/věrnostní program>“, automaticky se aplikuje cenový výpis
<prodejní místo/cenotvorba/ceníky>“, nebo „vytvořit a vytisknout fakturu
<faktury/>.

Můžete vytvořit zákazníka z otevřené pokladny pomocí kliknutí na
Vyberte „Zákazník – Vytvořit“ a vyplňte kontaktní údaje. Můžete také vytvořit
zadat požadavek na zadní straně, přejděte do: `Nástroje prodeje --> Objednávky --> Zákazníci`.
Klikněte na „New“ a pak vyplňte informace a uložte.

Chcete-li při objednávce nastavit zákazníka, přejděte na seznam zákazníků kliknutím na „Zákazník“
POS rozhraní. Můžete si také zvolit zákazníka na platebním obrazovce kliknutím
:label_customer:

.._pos/customer-notes:

Poznámky zákazníka
==============

Můžete přidat poznámky zákazníka k určitému produktu přímo z otevřené :ref:`ses
<pos/session-start>. Například poskytnout tipy na úklid a údržbu. Mohou být také použity
sledovat specifickou poptávku zákazníka, například pokud si zákazník nepřeje, aby mu produkt sestavili.

Pro to vyberte produkt a klikněte na tlačítko „Poznámka zákazníka“ v bloku. To otevře okno
okno, ve kterém můžete přidávat nebo upravovat obsah poznámky.

.. poznámka::
Poznámky k produktu z importované objednávky ze SO <point_of_sale/shop/sales_order> se zobrazují
stejně v košíku.

.. obrázek: bod_prodeje/poznámky_klienta.png
:alt: Tlačítko poznámky zákazníka a poznámky k produktům v košíku

Poznámky zákazníků se objevují na fakturách a účtech podobně jako v košíku.
v sekci související produkt.

.. obrázek: point_of_sale/notes-receipt.png
:alt: Faktura pro zákazníka s poznámkami od SO a funkce poznámky k faktuře

.. _pos/vrácení:

Vrácení a vracení zboží
==========================

Pro vrácení peněz za zboží, které bylo vráceno, postupujte takto:

#:ref:`Zahájit sezení <pos/session-start>“ z **přístupového bodu POS**.
#Klikněte na „Akce“, pak na „Zrušit“ a vyberte příslušnou
pořádku.
#Vyberte položky, použijte klávesnici k nastavení množství vrácené částky a pak klikněte na tlačítko „Vrácení“.
#Klikněte na položku „Platba“ a vyberte vhodný způsob vrácení peněz.
#Klikněte na tlačítko „Potvrdit“ a vytiskněte pokladní doklad, pokud je potřeba.
#Klikněte na tlačítko „Nový pořad“ a pokračujte s dalším zákazníkem.

..tip:
   - Seřadit seznam objednávek podle :guilabel:`Číslo objednávky“, :guilabel:`Číslo faktury“
:guilabel:`Datum“ nebo „Zákazník“, zadejte hodnotu do vyhledávacího pole a vyberte
z nabídky filtrů.
   - Pokud je celková částka záporná, přidáním dárkové karty do košíku se automaticky upraví
dárkovou kartu v hodnotě odpovídající této částce.

.. poznámka::
Alternativně lze vrácení peněz provést výběrem zboží vráceného zpět ze skladu.
sezení a nastavit záporné množství rovné počtu položek vrácených zpět. Chcete-li tak učinit, klikněte
:guilabel:'Množství' a :guilabel:'Přidat/Odebrat', a aktualizovat množství podle toho.

Jakmile je platba vrácena, Odoo vygeneruje požadovanou fakturu.
originální fakturu nebo dodací list a částečně nebo úplně zrušit tento dokument.

.. _pos/kasa:

Vedoucí pokladny
========================

Chcete-li přidat nebo odebrat hotovost z pokladny, klikněte na ikonu menu v pravém horním rohu vašeho
obrazovka a :guilabel:`Příjem/Výdej“.

.. obrázek: bod_prodeje/tlačítko_menu.png
:alt:Drobná nabídka pro ukončení pokladního režimu, přístup do zázemí, vložit nebo vybrat hotovost či kontrolovat
objednávky

K tomu se otevře okno s možnostmi „Vložit“ nebo „Vybrat“.
Vyplňte částku a důvod a klikněte na „Potvrdit“.

.._pos/session-close:

Uzavřete sezení na pokladně.
=====================

Pro ukončení sezení klikněte na ikonu menu v pravém horním rohu obrazovky.
:guilabel:`Ukončit relace“.

Tím se otevře okno „Kontrola uzavření“. Zde můžete získat
různé informace:

- počet objednávek a celkový objem uskutečněných obchodů za sezení.
- Očekávané částky rozdělené podle způsobu platby.

Než okno zavřete, spočítejte si hotovost pomocí ikony kalkulačky. To způsobí otevření
okno, které počítá celkovou částku v pokladně podle počtu mincí a bankovek.
a ručně přidána. Poté klikněte na tlačítko „Potvrdit“ nebo „Zrušit“, abyste okno zavřeli.
Výpočetní částka je nastavena v sloupci „Počítaná“, a podrobnosti o penězích jsou
v sekci „Poznámky“.

.. obrázek:point_of_sale/uzavírací kontrola.png
:alt:Jak ukončit sezení na pokladně.

Jakmile máte hotovo s kontrolou částek, klikněte na tlačítko „Uzavření relace“ a vraťte se zpět.
dashboard POS.

.. poznámka::
   - Chcete-li se dostat na Backend bez ukončení relace, klikněte na položku „Backend“ v nabídce.
menu.
   - Pro zrušení klikněte na tlačítko „Zavřít“ v okně s upozorněním.
   - V závislosti na vašem nastavení můžete být omezeni v uzavření seance pouze tehdy, pokud je očekávaný hotovostní zisk
Příjem je roven počítané hotovosti. Zavřít jej lze kliknutím na tlačítko „OK“ v
:guilabel:`Rozdíl plateb“ obrazovka.

..tip:
   - Je silně doporučeno uzavřít každodenní sezení POS na konci dne.
   - Pro zobrazení všech předchozích objednávek přejděte na: „Obchodní místo - Objednávky“.
Sessions'.

..._pos/analytics:

Analýza
=========

Jakmile ukončíte a zveřejníte sezení POS <pos/session-close>, přistupujte k podrobnému hlášení.
zpracovat všechny aktivity jednání, včetně toho, kdo zahájil jednání a kdo se o konkrétní záležitost staral.
objednávek. Pro přístup k zprávě o jednání:

#Klikněte na ikonu „vertikální elipsa“ ([:guilabel:`fa-ellipsis-v`]).
#Klikněte na „Záznamy“ pod záložkou „Výstup“.
#Z této obrazovky můžete vidět všechny sezení a kdo je zahájil pod
:guilabel:`Otevřeno“ sloupec.
#Vyberte transakci, abyste získali podrobné informace o této transakci.
#Klikněte na tlačítko „Objednávky“ v levém menu. Zobrazí se seznam všech objednávek, které byly během této doby zadány.
jednání.
#Z této perspektivy lze získat následující informace:

   - :guilabel:`Objednávka číslo`
   - Datum objednávky, viz guilabel:Date.
   - Místo prodeje, kde byla objednávka zadána.
   - :guilabel:`Číslo faktury“.
   - :guilabel:`Zákazník“.
   - Zaměstnanec, který tento nákup objednal.
   - Výše zaplacené částky celkem.
   - Příkaz: Status.

Pro zobrazení všech objednávek bez ohledu na relace klikněte na tlačítko vertikální elipsy.
:guilabel:`⋮“ na platební kartě a vyberte „Objednávky“ v sekci „Zobrazit“.

.. toctree::


konfigurace prodejního místa
point of sale/pos hardware
point_of_sale/prihlaseni-zamestnance
prodejní místa/faktury a daňové doklady
prodejní místo/příprava
point of sale/self order
point_of_sale/kombinace
point of sale/shop
bod prodeje/restaurace
cena na prodejně
point_of_sale/platební metody
point of sale/marketing založený na POS
point of sale/online food delivery
point of sale/reporting
