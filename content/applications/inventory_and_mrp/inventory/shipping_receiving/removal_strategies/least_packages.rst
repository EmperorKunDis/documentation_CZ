======================
Nejmenší počet odstraněných balíků
======================

Strategie „Nejmenší počet balíčků“ splňuje požadavek otevření nejmenšího počtu balíčků.
Ta je ideální pro udržování organizovaného skladu bez nutnosti otevírat více krabic.

.. viz také:
   - :doc:`O odstraňovacích strategiích <../removal_strategies>`
   - „Návody k Odoo: Nejmenší balíčky <https://www.odoo.com/slides/slide/5477/share>“

Chcete-li pochopit, jak funguje strategie odstranění, zvažte následující příklad skladu
Uchovává mouku v balení po 100 kg.

Aby se minimalizovala vlhkost a/nebo aby se zabránilo tomu, aby se do otevřených balení dostali škůdci, je nejlepší odstranit co nejméně obalů.
Strategie se používá k výběru z jednoho otevřeného balení.

... skladové zásoby/sklady/množství balení:

Příklad:
Balík mouky o hmotnosti 100 kilogramů se po vyřízení několika objednávek sníží na 54 kilogramů.
dalších balení o hmotnosti 100 kg skladem.

   #Když je objednáno 14 kilogramů mouky, zvolí se balení o hmotnosti 54 kilogramů.
   #Když je objednáno více než 54 kilogramů mouky, používá se neotevřená krabice o hmotnosti 100 kilogramů.
splnit objednávku. Přitom dočasně vznikají dvě otevřená balení, ale tyto otevřená balení
V následujícím vyskladnění jsou tyto položky prioritizovány.

Průběh práce
========

Při nejméně odstraňovacím balíčku je použito nejmenšího počtu balíčků k vyřízení objednávky.

.. důležité::
Funkce balení (viz část „Soubor balení“ v kapitole „Skladování a inventarizace“) **musí být** zapnutá, aby bylo možné používat
tato strategie.

Pojďme se podívat na příklad s produktem „Mouka“. Produkt má vlastnost „jednotky“ nastavenou na hodnotu
V poli Měření je nastaveno hodnota kg. Produkt se skladuje v baleních
„100 kg“, zbyl jeden balíček o „54 kg“. Kategorie produktu: guilabel:„Síla
Strategie odstranění je nastavena na: „Nejmenší balíčky“.

.. viz také:
   - :ref:`Strategie odstranění položek v kategorii produktů <Inventář/Skladování a sklady/Odstranění konfigurace>“

..tip:
Pro zjištění skladové zásoby produktu přejděte na kartu produktu a klikněte na tlačítko :guilabel:`Na
Tlačítko „Hands-free“.

.... obrázek:: nejmenších_balení/na_ruce_mouka.png
:srovnání: do středu
:alt:Zobrazení skladových zásob v každé krabici.

Vytvořte objednávku na dodání osmi set kilogramů mouky pomocí odkazu
do aplikace „Prodej“ a vytvořit novou nabídku. Po kliknutí na „Potvrdit“,
je vytvořen dodací příkaz.

V poli „Množství“ objednávky dodání se zobrazí automaticky vybrané množství.
podle odstranění strategie.

Pro více informací o tom, kde byly jednotky vybrány, zvolte :guilabel:`⦙≣ (seznam bodů)
ikonou umístěnou v pravém dolním rohu. Kliknutím na ni se otevře okno „Přesun do skladu“.
ukázat, jak byly vybrané položky odstraněny podle strategie odstraňování.

V okně „Přesun otevřeného skladu“ se v poli „Odebrat z“ zobrazí
požadované množství je vybráno. Protože objednávka požadovala osmdesát
kilogramů, což převyšuje množství v otevřeném balení „54 kg“ a neotevřeném balení „100
kg je vybrána.

.. obrázek: nejmenší_balíčky/nejmenší-balíček.png
:align:center
:alt:Zobrazte, který balíček byl vybrán v poli *Vyberte z*.
