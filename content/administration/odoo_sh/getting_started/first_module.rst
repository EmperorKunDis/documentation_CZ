=================
První modul
=================

Přehled
========

Tato kapitola vám pomůže vytvořit první modul Odoo a nasadit jej do projektu Odoo.sh.

Tento návod vyžaduje, abyste vytvořili projekt na Odoo.sh (viz odoo.sh/gettingstarted/create).
znáte URL svého repozitáře na GitHubu.

Přednáška vysvětluje základní používání Git a GitHubu.

Předpokládá se následující:

* ~/src je adresář, ve kterém jsou umístěny Git repozitáře související s vašimi projekty Odoo.
* *odoo* je uživatel na GitHubu.
* *odoo-addons* je repozitář na GitHubu.
* *feature-1* je název vývojové větve.
* *master* je název výrobní větve.
* *my_module* je název modulu.

Tyto hodnoty nahraďte libovolnými hodnotami.

Vytvořte vývojovou větev
=============================

Odoo.sh
------------

V rozhraní větví:

* stiskněte tlačítko „+“ vedle fáze vývoje.
* Vyberte větvení *master* ve výběru *Fork*.
* V poli „Komu“ zadejte „*feature-1*“.

|obr1|  |obr2|

.. |obrázek1| obrázek: první modul/prvnímodul-rozvoj+.png
:šířka: 45 %

.. |obrázek2| obrázek:: první modul/prvnímodul-rozvojové větve.png
:šířka: 45 %

Jakmile je sestavení vytvořeno, můžete přistupovat k editoru a procházet složku ~/src/user*, abyste se dostali
do kódu vaší vývojové větve.

.. obrázek: první modul/prvnímodul-rozvojový editor.png
:align:center

.. obrázek: první modul/první modul - vývojářské rozhraní editoru.png
:align:center

Z počítače
------------------

Zkopírujte svůj repozitář na GitHub do počítače:

.. kódový blok: bash

$ mkdir ~/src
$ cd ~/src
$ git clone https://github.com/odoo/odoo-addons.git
$ cd ~/src/odoo-addons

Vytvořte novou větev:

.. kódový blok: bash

$ git checkout -b feature-1 master

Vytvořit modulovou strukturu
===========================

Skladba modulu
----------------------

Pokud není nutné, skládací konstrukce zabraňuje zdlouhavé práci s nastavením základní struktury modulu Odoo.
Nový modul můžete nainstalovat pomocí spustitelného souboru *odoo-bin*.

Z editoru Odoo.sh v terminálu:

.. kódový blok: bash

$ odoo-bin scaffold my_modul ~/zdroje/uživatel

Anebo z počítače, pokud máte nainstalovanou instalaci Odoo:

.. kódový blok: bash

$ ./odoo-bin scaffold my_modul ~/odoo-addons/

Pokud nechcete řešit instalaci Odoa na svůj počítač,
Můžete si také stáhnout šablonu struktury modulu:
která nahradí všechny výskyty *my_module* jménem, které si zvolíte.

Následující struktura bude vytvořena:

::

my_module
└── __init__.py
└──__manifest__.py
├── controllers
│   └── __init__.py
├── __init__.py
└── demo
│   └── demo.xml
├── models
│   └── __init__.py
├── __init__.py
└── security
├─────────────────────────────────────────────────────────
└── views
└── templates.xml
└── views.xml

.. varování:

Nebraňte se používat speciální znaky jinak než podtržením (_).
hyfena (-). Toto jméno se používá pro třídy vašeho modulu v Pythonu a mít třídy s názvem
s jinými speciálními znaky než podtržením není v Pythonu platné.

Komentář z textu souborů odstraňte:

* *models/models.py*
příklad modelu s jeho poli.
* *pohledy/pohledy.xml*
stromové a formulářové zobrazení s nabídkami pro jejich otevření.
* *demo/demo.xml*.
demonstrátorské záznamy pro výše uvedený příklad modelu
* *kontrolory/kontrolory.py*
příklad implementace některých tras.
* *views/templates.xml*.
dva příklady výhledů QWeb používaných nadřazenými kontroléry tras.
* *manifest.py*,
manifest modulu včetně například jeho názvu, popisu a datových souborů k načtení.
Potřebujete jen odkomentovat soubor se seznamem kontroly přístupu:

....... kódový blok:: python

    # „bezpečnost/ir.model.access.csv“,

Ručně
--------

Pokud chcete vytvořit strukturu modulu ručně
Můžete sledovat návod /developer/tutorials/server_framework_101, abyste pochopili
struktura modulu a obsah každého souboru.

Vytlačte vývojovou větev
===========================

Změny nastavte k přijetí

.. kódový blok: bash

$ git add my_module

Uložte změny

.. kódový blok: bash

$ git commit -m "Můj první modul"

Přidejte své změny do svého vzdáleného repozitáře

Z terminálu pro editaci Odoo.sh:

.. kódový blok: bash

$ git push https HEAD:feature-1

Výše uvedené příkazy jsou vysvětleny v části
:ref:`Přidejte a převeďte své změny
<odoosh-gettingstarted-online-editor-push>
:ref:`Online editor <odoosh-gettingstarted-online-editor>`
kapitola.
Zahrnuje vysvětlení, že budete vyzváni k zadání svého uživatelského jména a
heslo a co dělat, když používáte dvoufaktorové ověření.

Anebo z počítačového terminálu:

.. kódový blok: bash

$ git push -u origin feature-1

Pro první tah musíte specifikovat pouze *-u origin feature-1*.
Od té doby můžete své budoucí změny snadno posílat z počítače prostřednictvím

.. kódový blok: bash

$ git push

Otestujte svůj modul
================

Váš větvený projekt by měl být viditelný ve vašich vývojových verzích.

.. obrázek: první modul/první modul - testovací větev.png


V zobrazení větví projektu
Kliknutím na název své větve v levém navigačním panelu se dostanete k jeho historii.

.. obrázek: první modul/prvnímodul-test-branch-history.png


Zde vidíte změny, které právě provedli, včetně komentáře, který jste nastavili.
Jakmile bude databáze připravena, můžete se k ní dostat klepnutím na tlačítko *Připojit*.

.. obrázek: první modul/prvnímodul-test-databáze.png


Pokud je váš projekt Odoo.sh nakonfigurován tak, aby automaticky nainstaloval vaši modulu
Přímý přístup k němu najdete mezi databázovými aplikacemi. Jinak bude dostupný v aplikacích pro
instalace.

Poté můžete s modulem pohrát, vytvářet nová data a testovat funkce a tlačítka.

Test s výrobními daty
=============================

Pro tento krok potřebujete produkční databázi. Pokud ji nemáte, můžete si ji vytvořit.

Jakmile si otestujete modul v vývojovém sestavení se zkušebními daty a budete věřit, že je připravený,
Můžete si to otestovat na vývojovém větvení, které používáte pro produkční data.

Můžete buď:

* Vytvořte svou vývojovou větev jako testovací větev tím, že ji přetáhnete na část *testování*.
titul.

.... obrázek: první modul/první modul - test - vývojové prostředí - staging.png
:synchronizace: střed

* Sloučit ji do existujícího testovacího větve, přetažením na daný testovací větvi.

.... obrázek: první modul/prvnímodul-test-develop-staging.png
:synchronizace: střed

Můžete také použít příkaz :code:`git merge`, abyste své větve sloučili.

Tím vytvoří nový stavěcí sestavení, které bude duplikovat produkční databázi a umožní její provoz.
pomocí serveru aktualizovaného s nejnovějšími změnami vaší větve.

.. obrázek: první modul/první modul - test sloučení do staging.png
:align:center

Když je databáze připravena, můžete se k ní dostat pomocí tlačítka *Připojit*.

..._odoosh-gettingstarted-firstmodule-productiondata-install:

Nainstalujte svůj modul
-------------------

Váš modul se nainstaluje automaticky, musíte jej však nainstalovat z nabídky aplikací.
Účelem stavového sestavení je otestovat chování vašich změn, jak by se projevily na vašem
výroby a na vaší výrobě byste si nepřáli, aby se do vašeho modulu automaticky instaloval
na poptávku.

Váš modul nemusí být přímo v aplikacích k instalaci, musíte aktualizovat své aplikace.
seznam první:

* Aktivujte režim vývojáře:ref:`<developer-mode>
* V nabídce aplikací klikněte na tlačítko *Aktualizovat seznam aplikací*.
* V dialogovém okně klikněte na tlačítko Update.

.... obrázek: první modul/prvnímodul-test-aktualizace seznamu aplikací.png
:align:center

Vaše modul pak bude v seznamu dostupných aplikací.

.. obrázek: první modul/první modul test mymodul v aplikaci.png


Uvedení do provozu
====================

Jakmile otestujete svůj modul v testovací větev s vašimi produkčními daty
a pokud si myslíte, že je připravená k produkci, můžete sloučit své větve s produkční verzí.

Přetáhněte svou větvičku s testovací verzí na výrobní verzi.

.. obrázek: první modul/prvnímodul-test-součástka-spojená-ve výrobě.png


Můžete také použít příkaz :code:`git merge`, abyste své větve sloučili.

Tím se sloučí nejnovější změny větve pro testování do produkční větve.
A aktualizujte svůj produkční server těmito nejnovějšími změnami.

.. obrázek: první modul/prvnímodul-test-sloučený v produkci.png


Když je databáze připravena, můžete se k ní dostat pomocí tlačítka *Připojit*.

Nainstalujte svůj modul
-------------------

Váš modul se nainstaluje automaticky.
Musíte si ji nainstalovat ručně, jak je vysvětleno v
:ref: „Návod k instalaci vašeho modulu do testovacích databází“
<odoosh-gettingstarted-firstmodule-productiondata-install>.

Přidejte změnu
============

Tato část vysvětluje, jak přidat změnu do vašeho modulu pomocí nového pole ve třídě a nasazení
it.

Z editoru Odoo.sh
 * procházejte do složky s modulem *~/src/user/my_module*.
 * Poté otevřete soubor *models/models.py*.

Anebo z počítače.
 * Použijte svůj oblíbený souborový prohlížeč k procházení složky modulu.
*~/src/odoo-addons/můj_modul*
 * potom otevřete soubor *models/models.py* v editoru svého výběru
např. Atom, Sublime Text, PyCharm, vim, ...

Poté, co popisovali pole

... kódový blok::python

popis = pole.Text

Přidejte pole datum a čas.

... kódový blok::python

start_datum = pole.DatumVČasu('Start time', výchozí hodnota je lambda sebe: pole.DatumVČasu.nyní)

Poté otevřete soubor views/views.xml.

Po

.. kódový blok::xml

<pole hodnota2/>

Přidej

.. kódový blok::xml

<pole název="start_datetime"/>

Tyto změny mění strukturu databáze přidáním sloupce do tabulky.
a upravit pohled uložený v databázi.

Pro použití v již existujících databázích, jako je například vaše produkční databáze.
Tyto změny vyžadují aktualizaci modulu.

Pokud chcete, aby aktualizace byla prováděna automaticky prostřednictvím platformy Odoo.sh při každém odeslání
Váš update zvyšuje verzi vašeho modulu v jeho manifestu.

Otevřete modulový manifest __manifest.py__*.

Vyměnit

... kódový blok::python

„verze“: „0.1“,

s

... kódový blok::python

"verze": "0.2",

Platforma detekuje změnu verze a spustí aktualizaci modulu na novou.
revize nasazení.

Přejděte do složky s Gitem.

Pak z terminálu Odoo.sh:

.. kódový blok: bash

$ cd ~/src/user/

Anebo z počítačového terminálu:

.. kódový blok: bash

$ cd ~/src/odoo-addons/

Poté připravte své změny k zavedení

.. kódový blok: bash

$ git add my_module

Uložte změny

.. kódový blok: bash

$ git commit -m "Přidání pole start_datetime do modelu my_module.my_module"

Uložte změny:

Z terminálu Odoo.sh:

.. kódový blok: bash

$ git push https HEAD:feature-1

Anebo z počítačového terminálu:

.. kódový blok: bash

$ git push

Platforma pak vytvoří novou verzi pro větev *feature-1*.

.. obrázek: první modul/prvnímodul-test-addachange-build.png
:align:center

Jakmile otestujete své změny, můžete je sloučit do produkční větve, například takto:
přetažením větve na produkční větev v rozhraní Odoo.sh.
verze modulu v seznamu, bude automaticky aktualizován modul a váš nový prvek
bude k dispozici přímo. Jinak můžete manuálně aktualizovat modul v seznamu aplikací.

Použijte externí knihovnu Pythonu
==============================

Pokud chcete použít externí knihovnu Pythonu, která není součástí výchozího instalace
Můžete definovat soubor s názvem *requirements.txt*, který obsahuje seznam externích knihoven, které vaše moduly vyžadují.

.. poznámka::
   - Není možné nainstalovat nebo upgradovat systémové balíčky na databázi Odoo.sh (např. apt
Pokud je však splněna určitá podmínka, může být balíček považován za instalaci.
To platí také pro moduly Pythonu vyžadující systémové balíčky k jejich kompilaci.
**třetí strany Odoo moduly**.
   - **Rozšíření PostgreSQL** nejsou na Odoo.sh podporovány.
   - Pro více informací navštivte naši „často kladené otázky“ <https://www.odoo.sh/faq#install_dependencies>.

Platforma použije tento soubor k automatické instalaci knihoven Python vašeho projektu.

Tato funkce je vysvětlena v této části pomocí knihovny Unidecode.
Přidejte do vašeho modulu knihovnu _<http://pypi.python.org/pypi/Unidecode>_.

Vytvořte soubor *requirements.txt* v kořenovém adresáři vašeho repozitáře

Ve správci souborů Odoo.sh vytvořte a otevřete soubor ~/src/user/requirements.txt.

Nebo z počítače vytvořte a otevřete soubor ~/src/odoo-addons/requirements.txt.

Přidej

... blok kódu:: text

unidecode

Pak použijte knihovnu ve vašem modulu například k odstranění akcentů z písmen v názvu.
oblast vašeho modelu.

Otevřete soubor *models/models.py*.

Před

... kódový blok::python

od odoo importujeme modely, pole a API

Přidej

... kódový blok::python

odkaz na knihovnu unidecode

Po

... kódový blok::python

start_datum = pole.DatumVČasu('Start time', výchozí hodnota je lambda sebe: pole.DatumVČasu.nyní)

Přidej

... kódový blok::python

@ApiModel
def __init__(self, values):
pokud je v hodnotách klíč „name“
values['jméno'] = unidecode(values['jméno'])
return super(modul, sebe).vytvořit(hodnoty)

def write(self, hodnoty):
pokud je v hodnotách klíč „name“
values['jméno'] = unidecode(values['jméno'])
return super(modul, sebe).write(hodnoty)

Přidání závislosti na Python vyžaduje zvýšení verze modulu pro instalaci platforem.

Upravte modulový manifest *__manifest.py*

Vyměnit

... kódový blok::python

"verze": "0.2",

s

... kódový blok::python

"verze": "0.3",

Zobrazte a zavřete změny:

.. kódový blok: bash

$ git add requirements.txt
$ git add my_module
$ git commit -m "Vložení [IMP] modulu my_module: automaticky odstraňuje speciální znaky v poli názvu modulu my_module.my_module"

Poté proveďte změny a potvrďte je.

V terminálu Odoo.sh:

.. kódový blok: bash

$ git push https HEAD:feature-1

V počítačovém terminálu:

.. kódový blok: bash

$ git push
