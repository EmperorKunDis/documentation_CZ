=====================
Připojte se k zařízení
=====================

IoT Driver umožňuje komunikaci v reálném čase mezi jakýmkoliv modulem Odoo a jakýmkoliv zařízením.
připojený k IoT boxu. Komunikace s IoT boxem je obousměrná, takže
Klient Odoo může odesílat příkazy a přijímat informace z jakéhokoli
podporované zařízení.

Abychom přidali podporu zařízení, potřebujeme jen:

- „Sada rozhraní“, která detekuje připojená zařízení určitého typu
- Řidič, který komunikuje s jednotlivými zařízeními.

Na každém spuštění bude IoT Box nahrávat všechny rozhraní a ovladače, které mohou
být umístěn na propojeném instanci Odoo. Každá modul může obsahovat
Souborová složka iot_handlers, která bude kopírována do IoT Boxu. Struktura
Tento adresář je následující

... blok kódu:: text

vaše_modul
    ├── ...
└── iot_handlers
└── driver
│    └── DriverName.py
        │   └── ...
        │
└───interfaces
└── InterfaceName.py
            └── ...

Najít zařízení
==============

Přístroje připojené k IoT Boxu jsou detekovány prostřednictvím „Síťových rozhraní“.
Pro každý podporovaný typ připojení (USB, Bluetooth, Video)
Tiskárny, sériové porty atd.)). Rozhraní udržuje seznam detekovaných zařízení.
a přiřazuje je k správnému řidiči.

Podporované zařízení se zobrazí na domovské stránce IoT Box, kterou můžete přistupovat
a v modulu IoT propojeného instancí Odoo.

Uživatelské rozhraní
---------

Role rozhraní je udržovat seznam zařízení připojených přes
určitého typu připojení. Vytvoření nového rozhraní vyžaduje

- Rozšíření třídy „Interface“
- Nastavení atributu třídy connection_type
- Implementací metody get_devices, která by měla vrátit seznam
obsahující údaje o každém detekovaném zařízení. Tyto informace budou poskytnuty
argumenty pro konstruktory a metodu Driver.

.. poznámka::
Přiřazením atributu _loop_delay se změní interval mezi voláním
do funkce get_devices. Výchozí hodnota je 3 sekundy.

... kódový blok:: python

od odoo.addons.hw_drivers.interface import Interface

třída InterfaceName(Interface):
type_spojení = 'Typ spojení'

def get_devices(self):
return {
"device_identifier_1": {...},
                ...
            }

Řidič
------

Jakmile rozhraní získá seznam detekovaných zařízení, bude smyčkou
pro všechny řidiče, kteří mají stejný atribut „connection_type“.
testovat své „podporované“ metody na všech detekovaných zařízeních. Pokud
podporovaný způsob řidiče vrací hodnotu True, takže se zobrazí instanci tohoto řidiče.
vytvořené pro odpovídající zařízení.

.. poznámka::
„podporované“ metody řidičů jsou seřazeny podle prioritního pořadí.
Metoda dětské třídy se vždy otestuje před metodou jejího rodiče.
Tato priorita se dá upravit změnou atributu priority.
Řidič.

Vytvoření nového řidiče vyžaduje:

- Rozšíření řidiče
- Nastavení atributu třídy connection_type.
- Nastavení atributů „device_type“, „device_connection“ a „device_name“.
- Definice metody „podporovaná“

... kódový blok:: python

od odoo.addons.hw_drivers.driver import Driver

class DriverName(Driver):
type_spojení = 'Typ spojení'

def __init__(self, identifikátor, zařízení):
super(NewDriver, self).__init__(identifikátor, zařízení)
self.device_type = 'DeviceType'
self.device_connection = 'DeviceConnection'
self.device_name = "DeviceName"

@classmethod
def podporuje(klas, zařízení):
            ...

Komunikujte s zařízeními
========================

Jakmile je váš nový přístroj detekován a zobrazen v modulu IoT, další krok
je s ním komunikovat. Protože krabička má pouze místní IP adresu, můžete
je možné pouze ze stejné lokální sítě. Komunikace je proto
se dějí v prohlížeči, ve skriptovacím jazyce JavaScript.

Proces závisí na směru komunikace:
- Od prohlížeče k boxu přes „Akce“
- Z krabice do prohlížeče přes „dlouhé spojení“

Oba kanály jsou přístupné z jednoho objektu v JavaScriptu, tzv. DeviceProxy.
Instanční identifikátor je vytvořen z IP adresy IoT boxu a zařízení.

... kódový blok: JavaScript

var DeviceProxy = require('iot.DeviceProxy');

var iot_device = nový objekt DeviceProxy s následujícími parametry:
iot_ip: iot_ip
identifikátor: zařízení
    });

Akce
-------

Akce slouží k tomu, aby vybraný zařízení bylo provedeno konkrétní akci.
například pořízení fotografie, tisk účtenky atd.

.. poznámka::
Je třeba poznamenat, že na této trase nebude odesláno žádné „odpovědi“,
pouze stav požadavku. Odpověď na akci (pokud existuje) musí být
získané pomocí dlouhého pollingu.

Akci lze provést na objektu DeviceProxy.

... kódový blok: JavaScript

iot_device.akce(data);

V řidiči definujte metodu „akce“, která se spustí při volání
z modulu Odoo. Přebírá jako argument data, která uživatel zadal při volání.

... kódový blok:: python

def action(self, data):
        ...

Dlouhé pollingy
-----------

Kdykoli nějaký modul v Odoo potřebuje číst data z konkrétního zařízení, vytvoří
Posluchač identifikovaný podle IP/domény přehrávače a zařízení.
přidává funkci zpětného volání, která se má každou chvíli spustit.
změna. Zavolání funkce se provede s novými daty jako parametrem.

... kódový blok: JavaScript

iot_device.přidat posluchače (toto._onValueChange.vázaný na tento)

_onValueChange: funkce (result) {
        ...
    }

V řidiči je událost vypuštěna voláním funkce device_changed
z „event_manager“. Všechny zpětné volání nastavené na posluchači pak budou provedeny.
s parametrem self.data.

... kódový blok:: python

od odoo.addons.hw_drivers.event_manager import event_manager

class DriverName(Driver):
type_spojení = 'Typ spojení'

def metodaJmeno(self):
self.data = {
„hodnota“: 0,5
                ...
            }
event_manager.zařízení_změněno(self)
