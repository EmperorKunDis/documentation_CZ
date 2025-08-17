
..._odoosh-gettingstarted-builds:

======
Staví
======

Přehled
========

V Odoo.sh je považován za sestavení databáze nahrávající Odoo server
(`odoo/odoo <https://github.com/odoo/odoo>`_ & `odoo/enterprise
<https://github.com/odoo/enterprise>`_) běžící na konkrétním revidovaném repozitáři vašeho projektu
kontejnerizované prostředí. Jeho účelem je otestovat chování serveru a databáze
a s těmito změnami.

.. obrázek:: builds/interface-builds.png
:align:center

V tomto pohledu představuje řádek větev a buňka v řádku vývojovou větve této věty.

Většinou se budovy vytvářejí po tlačení na větve vašeho repozitáře Githubu.
Vznikají i při jiných operacích.
například importování databáze na Odoo.sh nebo požádání o přepracování větve projektu.

Stavbu považujeme za úspěšnou, pokud při jejím vytváření nevyskočí žádné chyby nebo varování.
Úspěšné sestavení je označeno zeleně.

Stav se považuje za neúspěšný, pokud během jeho vytváření dojde k chybám.
Nebylo-li sestavení úspěšné, je vyznačeno červenou barvou.

Pokud se během vytváření zobrazí varování, ale nejsou žádné chyby, tak je stav sestavení považován za téměř
úspěšné. Je zvýrazněno žlutě, aby vývojáři informovali o tom, že byly vysunuty varování.

Sestavení ne vždy vytváří databázi od nuly. Například při přidávání změny na
výrobní větve, takže nová verze začne spouštět server a zkusí načíst
současnou databázi výroby na něm. Pokud se neobjeví žádné chyby, staví se za úspěšné a
Jinak by se jí nepodařilo.

Stáže
======

Produkce
----------

První sestavení produkční větve vytváří databázi od nuly.
Pokud je tato verze úspěšná, pak se tento databázový server považuje za produkční databázi vašeho projektu.

Od té doby se budou na výrobní větvi vytvářet nové sestavení, která se pokusí nahrát databázi
pomocí serveru s novou verzí.

Pokud je sestavení úspěšné nebo obsahuje varování, ale žádné chyby, bude nyní produkční databáze spouštěna
tento sestavený produkt a revize spojená se sestaveným produktem.

Pokud se sestavení nepodaří načíst nebo aktualizovat databázi, pak je použito předchozí úspěšné sestavení.
databáze, takže databáze bude spouštěna na serveru s předchozím
úspěšná revize.

Výroba, která běží produkční databázi, je vždy první ve výčtu verzí. Pokud se nějaká verze
nefunguje, je umístěna za stávajícím během produkčního databáze.

Režie
-------

Staging vytváří duplikát produkční databáze.
a pokusit se nahradit tuto kopii s revizemi větví pro testování.

Každý pokus o novou revizi na pracovním větvení vyvolává nové sestavení.
databáze výroby. Databáze nejsou mezi budovami stejného větvení znovu používány, což zajišťuje:

* Provedení se používají databáze, které jsou blízko tomu, co v produkci vidíte.
vaše testy s daty zastaralými.

* Můžete si hrát s databází hry tak dlouho, jak chcete, a pak požádat o
obnovit, když chcete znovu spustit s novou kopií produkce.

Přesto to znamená, že pokud provedete konfigurační změny v testovacích databázích a ne
použít je při výrobě, nebudou se předávat na další sestavení stejného větvení.

Rozvoj
-----------

Vývojové sestavení vytváří nové databáze, načítá ukázková data a spouští jednotkové testy.

Konstrukce bude považována za neúspěšnou a označena červenou barvou, pokud se v průběhu instalace zobrazí chyba.
Jejich účelem je upozornit na chybu, pokud k ní dojde.

Pokud všechny testy projdou a nebude žádný problém, bude se stav považovat za úspěšný.

Podle seznamu modulů k instalaci a otestování může vývojová verze trvat až hodinu.
buď připraveni. Je to kvůli velkému množství testů, které jsou v základní sadě modulů Odoo.

Vlastnosti
========

Výrobní odvětví se vždy objeví jako první a ostatní odvětví jsou seřazena podle posledního
Vytvořené větve. Můžete filtrovat větve.

.. obrázek: build/interface-builds-branches.png
:align:center

Pro každou větev můžete přistupovat k poslednímu sestavení pomocí odkazu „Připojit“ a skočit na
branch code pomocí odkazu na GitHub. Pro ostatní než výrobní větve můžete vytvořit nový
budova, která bude používat nejnovější verzi větve pomocí odkazu *přestavit*. Poslední odkaz je
nejsou k dispozici, pokud je již v procesu sestavení pro daný větev.

.. obrázek: builds/interface-builds-build.png
:align:center

Pro každou sestavení můžete zobrazit změny v revizi pomocí tlačítka s ikonou GitHubu.
Připojit se k databázi projektu jako správce pomocí tlačítka Připojení.
databáze s jiným uživatelem pomocí tlačítka Connect as v nabídce Connect
tlačítko.

... _odoosh-gettingstarted-builds-download-dump:

.. obrázek: builds/interface-builds-build-dropdown.png
:align:center

... _odoosh-gettingstarted-builds-dropdown-menu:

V rozbalovacím menu pro stavbu je k dispozici stejné funkce jako v :ref:`přehledu verzí.
<odoosh-gettingstarted-branches-tabs>:*Záznamy*, *Webová konzole*, *Editor*, *Vyjíždějící e-maily*.
mít možnost stáhnout si zálohu databáze sestavení.*
