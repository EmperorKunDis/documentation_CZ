
================
Manifest modulu
================



.. odkaz/modul/manifest:

Manifest
========

Manifestový soubor slouží k prohlášení balíčku Pythonu jako modulu Odoo
a specifikovat metadatové informace o modulu.

Jedná se o soubor s názvem „__manifest__.py“ a obsahuje pouze jeden příkaz v jazyce Python.
slovníku, kde každý klíč označuje modul metadat.

::

    {
„Název“: „Modul“,
"verze": "1.0",
'závisí na základu': ['base']
'autor': "Autorské jméno",
'kategorie': 'Kategorie',
"popis": """
Popis
        """,
        # Data jsou vždy načtena při instalaci.
'data': [
'views/mymodule_view.xml',
        ],
        # soubor dat obsahující volitelná vzorová data
"demo": [
‚demo/demo_data.xml‘,
        ],
    }

K dispozici jsou následující pole manifestu:

„jméno“ („str“, povinné)
čitelný název modulu
„verze“ („str“)
verze modulu by měla splňovat pravidla „semantického verzování“
„popis“ („str“)
rozšířený popis modulu v reStrukturovaném textu
„autor“ („str“)
jméno autora modulu
„webová stránka“ („str“)
URL webové stránky autora modulu
„licence“ („str“, výchozí hodnoty: „LGPL-3“)
licenci na distribuci modulu.
Možné hodnoty:

    * „GPL-2“
    * „GPL-2 nebo novější verze“
    * „GPL 3“
    * „GPL verze 3 nebo novější“
    * „AGPL-3“
    * „LGPL-3“
    * „Další licence schválená OSI“
    * „OEEL-1“ („Odoo Enterprise Edition License v1.0“)
    * „OPL-1“ („Odoo Proprietary License verze 1.0“)
    * „Jiné vlastní“

„kategorie“ („str“, výchozí hodnota: „Nezařazeno“)
kategorie třídění v Odoo, hrubá obchodní doména modulu.

Přestože je doporučeno používat „stávající kategorie“, pole je
volné a neznámé kategorie vytváříme na lince. Kategorie
hierarchie lze vytvořit pomocí oddělovače „/“, například „Foo / Bar“
Vytvoří kategorii „Foo“, kategorii „Bar“ jako podkategorii této kategorie.
„Foo“ a nastaví „Bar“ jako kategorii modulu.
„záleží“ („list(str)“)
Moduly Odoo, které musí být načteny před tímto modulem, ať už kvůli tomu, že
modul využívá funkce, které vytvoří, nebo protože mění zdroje, které
definovat.

Při instalaci modulu se nainstalují všechny jeho závislosti předtím.
stejně jako před naložením modulu se načítají i závislosti.

.. poznámka::
Modul „base“ je vždy nainstalován ve všech instancích Odoo.
Ale stále je potřeba ji uvést jako závislost, aby se vaše modul aktualizoval, když se aktualizuje „base“.

„data“ („list(str)“)
Seznam datových souborů, které musí být vždy nainstalovány nebo aktualizovány.
modul. Seznam cest od kořenového adresáře modulu
„demo“ („list(str)“)
Seznam datových souborů, které jsou nainstalovány nebo aktualizovány pouze v *demonstraci
režim*
„auto_install“ („bool“ nebo „list(str)“, výchozí hodnota: „False“)
Pokud je „True“, tento modul bude automaticky nainstalován, pokud jsou všechny jeho
jsou nainstalovány závislosti.

Je obecně používáno pro „synchronizační moduly“, které implementují synergickou integraci
mezi dvěma jinak nezávislými moduly.

Například „sale_crm“ závisí na obou proměnných „sale“ a „crm“ a je nastaveno
„auto_instal“. Když jsou nainstalovány oba moduly „sale“ a „crm“,
automaticky přidává do objednávek sledování prodejních kampaní bez
„prodej“ nebo „CRM“, které jsou si vědomy jeden druhého.

Pokud je to seznam, musí obsahovat podmnožinu závislostí. Tento modul bude automaticky zahrnut do
jsou nainstalovány, jakmile jsou nainstalovány všechny závislosti v podmnožině. Zbývající
budou nainstalovány automaticky i všechny závislosti. Pokud je seznam prázdný, tento modul
vždy automaticky nainstalovány bez ohledu na jejich závislosti a tyto budou instalovány jako
dobře.

„externí závislosti“ („dict(key=list(str))“)
Složka obsahující slovník s binárními a/nebo Pythonovými závislostmi.

Pro závislosti na Pythonu je nutné definovat klíč „python“.
seznam slovníků a seznam modulů Python, které mají být importovány.
k němu.

Pro binární závislosti musí být definován klíč „bin“.
k němu by měly být přiřazeny slovník a seznam názvů binárních spustitelných souborů.

Modul se nenainstaluje, pokud buď nebude instalován modul Python.
v hostitelském stroji nebo není nalezena binární verze.
proměnná prostředí PATH hostitelského stroje.
„aplikace“ („bool“, výchozí hodnota: „False“)
Zda modul lze považovat za plnohodnotnou aplikaci
(„Pravda“) nebo je pouze technickou součástí („Falešně“), která poskytuje nějaké
dostatečně velký, aby se do něj vešla celá aplikace.
„aktiva“ („slovo“)
Definice, jak se načítají všechny statické soubory v různých balících aktiv.
Podrobnější informace o tom, jak vytvářet aktiva, najdete na stránce :ref:`aktiva <reference/assets>`.
popisovat balíčky.
„instalovatelný“ („bool“, výchozí hodnota „True“)
Zda uživatel má mít možnost instalovat modul z webového rozhraní nebo ne.
„správce“ („str“)
Osoba nebo subjekt odpovědný za údržbu tohoto modulu, pokud není uvedeno jinak.
Je předpokládáno, že autor je udržovatel.
„Před inicializací“, „Po inicializaci“ a „Odinstalování“ („str“)
Háčky pro instalaci/odinstalaci modulu, jejich hodnota by měla být
Řetězec reprezentující název funkce definované uvnitř modulu.
„__init__.py“.

„pre_init_hook“ bere jako jediný parametr ukazatel, tato funkce je
provedené před instalací modulu.

„post_init_hook“ přijímá jako argument kurzor a registr.
funkce se spustí ihned po instalaci modulu.

„uninstall_hook“ přijímá jako argument ukazatel a registr.
funkce se spustí po odinstalování modulu.

Tyto háčky by měly být používány jen tehdy, když je potřeba nastavit nebo uklidit modul.
je buď extrémně obtížné nebo nemožné prostřednictvím API.
„aktivní“ („bool“)
Zastaralé. Nahrazeno „auto_install“.

...semantické verze: https://semver.org
... existující kategorie: {GITHUB_PATH}/odoo/addons/base/data/ir_module_category_data.xml
