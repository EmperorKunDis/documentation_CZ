=======================
Elektronické cenovky
=======================

Elektronické cenovky umožňují zobrazovat informace o produktech, jako jsou například ceny a čárové kódy.
poličky a synchronizovat je vzdáleně z back-endu. To odstraňuje potřebu tisknout nové štítky
Při změně informací o produktu.

.. obrázek: elektronické_štítky/elektronický_štítek.png
:alt: elektronická etiketa od Priceru

.. poznámka::
Odoo používá elektronické cenovky od Priceru.

Konfigurace
=============

Instalace priceru
------------

#Kontaktujte společnost Pricer <https://www.pricer.com/contact> a vytvořte si svůj Pricer
účet.
#Vytvořte své obchody: jeden pricerový obchod odpovídá jednomu fyzickému obchodu.
#. Připojte k obchodu Pricer takové množství přijímačů, které je potřeba.
#Vytvořte následující proměnné, abyste mohli sdílet informace o produktech mezi vaším systémem Odoo a
Pricer. Tyto proměnné fungují jako vložky na štítku.

   - `itemId`: tento parametr obsahuje jedinečné interní identifikátory, které jsou přiřazeny každému produktu.
   - `itemName`: skutečný název produktu
   - „cena“: prodejní cena produktu včetně příslušných daní
   - „prezentace“: název šablony používaný v Priceru pro zobrazení informací o produktu na
štítek
   - „měna“: měna vaší společnosti (např. USD, EUR)
   - „čárový kód“: číslo čárového kódu spojené s každým produktem

.... důležité::
Název proměnných musí být v databázi Pricer stejný.

#Vytvořte šablonu s názvem „NORMAL“. Tato šablona se používá k zobrazení informací na vašem digitálním
tagy.

Jakmile máte svůj účet, obchody, proměnné a šablonu nakonfigurované v Priceru, můžete pokračovat s
nastavení databáze Odoo.

.. důležité:
Účet spojený s vaším obchodem Pricer musí mít přístup k odesílání požadavků na Pricer.

Nastavení Odoo
----------

Jako předpoklad je nutné aktivovat modul POS Pricer.
název: pos_pricer) má všechny potřebné funkce pro používání elektronických tagů Pricer.

.. obrázek: elektronické_etikety/cenač_modul.png
:alt:Instalace modulu POS Pricer z Apps

Jakmile modul aktivujete, nakonfigurujte si své cenové sklady a připojte je k
:ref:`Pricer tagy <pricer_tags/tags>“ s vašimi produkty.

.. _cena_tagy/obchody:

Pricery
~~~~~~~~~~~~~

Stejně jako v případě konfigurace Pricer je nutné pro každou fyzickou lokalitu vytvořit jeden obchodník.
Pro toto nastavení přejděte na: „Prodejní místo“ - „Nastavení“ - „Pricer Stores“, klikněte
„Nový“ a vyplňte řádek požadovanými informacemi:

- :guilabel:`Název obchodu“: můžete dát jakýkoliv název, který se vám líbí.
- :guilabel:`Název nájemce Pricera`: jméno vašeho účtu v Pricer, obvykle následované
- `country_code`, který je dodáván společností Pricer.
- :guilabel:`Pricer Login“: přihlašovací údaje k vašemu účtu Pricer.
- :guilabel:`Heslo k účtu Pricer“: heslo vašeho účtu Pricer.
- :guilabel:`ID obchodu Pricer“: ID obchodu Pricer, který je definován na vašem Pricer
databáze.

.. obrázek: elektronické_štítky/pricer-obchod-nastavení.png
:alt: Konfigurace cenového terminálu

.. poznámka::
   - Kolonka „Štítky cen“ je automaticky aktualizována, když se štítek přiřadí k
produktu.
   - Sloupec „Poslední aktualizace“ a sloupec „Stav poslední aktualizace“ jsou aktualizovány
automaticky při aktualizaci tagů.

.. _cena_tagů/tagy:

Pricery
~~~~~~~~~~~

Pro zobrazení konkrétních informací o produktu je nutné spojit etiketu s
produktu. Chcete-li tak učinit, postupujte následovně:

#Otevřete produktové formuláře kliknutím na: Menu Selection: Point of Sale --> Products --> Products
kliknutím na tlačítko „New“ nebo výběrem existujícího produktu.

....... poznámka::
Pokud vytváříte nový produkt, nakonfigurujte ho a uložte před přidáním štítku cenovky.

#. Vyberte záložku „Prodej“, posuňte se do části „Cenotvorba“ a vyberte
odpovídající :guilabel:`Pricer Store“.

.... obrázek: elektronické_štítky/cenovka-produkt.png
:alt:Propojení tagů cenovkovače s produktem
:skalka: 75 %

#Zadejte hodnotu do pole „ID štítků cen“ přetažením ID štítku z etikety.
a skenováním jeho čárového kódu.

....... poznámka::
ID štítků Pricer jsou tvořeny písmenem následovaným 16 číslicemi.

..tip:
   - Doporučujeme použít čtečku čárových kódů, aby se urychlil proces kódování.
   - Při prvním nastavení cenového systému Pricer s Odoo se doporučuje konfigurovat pouze
nejprve jeden produkt. Než budete konfigurovat další produkty, ujistěte se, že můžete zobrazit jejich informace
na etiketě Pricer.

Nyní, když máte produkt spojený s etiketou Pricer, můžeme poslat informace o něm do Priceru.

Praktické využití
---------------------

Odoo automaticky pošle žádost o synchronizaci štítků každých 12 hodin, pokud provedete jakoukoliv změnu.
modifikace:

   - Název produktu, cena, čárový kód nebo zákaznická daň
   - Měna
   - Obchod s asociací Pricer nebo štítky Pricer

Aby se aktualizace spustila, aktivujte režim vývojáře (:ref:`vývojářský režim <developer-mode>`). Pak:

#Přejděte na „Prodejní místo –> Konfigurace –> Cenovka“.
#Vyberte požadovanou prodejnu.
#Klikněte na tlačítko „Aktualizovat štítky“ a aktualizujte všechny štítky, které byly ovlivněny změnami.

   - Název produktu, cena, čárový kód nebo zákaznická daň
   - Měna
   - Obchod s asociací Pricer nebo štítky Pricer

Alternativně klikněte na tlačítko „Aktualizovat všechny štítky“ a přinutit tak aktualizaci každého štítku.
zda došlo ke změně.

.. obrázek: elektronické_štítky/aktualizace_všeho.png
:alt:Aktualizovat všechny tagy Pricer

Pokud Pricer zpracoval a přijal požadavek, stavový proužek zobrazí:guilabel:`Aktualizace
úspěšně odeslána na Pricer“. Pokud dojde k nějaké chybě, zobrazí se hláška o chybě.

.. varování:
Pokud požadavek na Pricer selže, Odoo stále považuje za aktuální produkt.
V takovém případě doporučujeme nutit aktualizaci všech značek.

Slevové etikety
---------------

Pro zobrazení slevového štítku na Pricer Tag je nutné propojit seznam cen:doc:`<pricelists>`.
variant produktu spojená s tímto štítkem.

Pro to je potřeba otevřít formulář produktové varianty:

#Přejděte na: „Prodejní místo“ - „Produkty“ - „Varianty produktů“.
#Vyberte produkt, na který chcete uplatnit slevu.

Poté nastavte požadovanou cenovou nabídku:

#Přejděte na záložku „Obecné informace“.
#Vyberte ceník v poli „Prodejní ceník“ (Guilabel: Price List Sales).

Jakmile je stanovena cenová nabídka, pole „Prodávaná cena“ se objeví a zobrazí „Prodejní cenu“.
Sleva uplatněna.

.. obrázek: elektronické_štítky/pricer-prodejní-ceník.png
:alt:Připojení cenového seznamu k produktové variantě

Po aktualizaci elektronických štítků by měl na elektronickém štítku vystupovat „PROMO“ tag.
zobrazuje jak původní cenu s přeškrtnutím, tak i slevu.

.. poznámka::
   - V současné době jsou k dispozici ceníky slev na nákup více jednotek nebo ceny odvozené
z jiných ceníků nejsou podporovány.
   - Přiřazení cenového lístku produktové variantě ovlivňuje pouze zobrazení elektronického štítku při skenování.
Při prodeji se slevou na místě nebude automaticky aplikovat sleva.

.. viz též:
:doc:`slevy“
