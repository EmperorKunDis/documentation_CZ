===================================
Vytvořte samostatnou aplikaci Owl
===================================

Pro jakýkoliv důvod můžete chtít mít samostatnou aplikaci Owl, která není součástí
webový klient. Příkladem v Odoo je aplikace pro samoobslužné objednávky, která umožňuje zákazníkům objednávat
jídlo z telefonu. V této kapitole se dozvíme, co je potřeba k tomu, aby něco takového šlo udělat.

Přehled
========

Pro samostatnou aplikaci Owl je potřeba několik věcí:

- kořenový komponent pro aplikaci
- soubor aktiv, který obsahuje nastavení.
- QWebový pohled, který volá aktivační balíček
- kontrolor, který zobrazuje pohled

1. Kořenový komponent
=================

Abychom si věci usnadnili, začněme s velmi jednoduchým komponentem, který jen zobrazuje
„Ahoj světe.“ To nám řekne na první pohled, jestli máme správně nakonfigurované prostředí.

Nejprve vytvořte šablonu v souboru: /your_module/static/src/standalone_app/root.xml

... blok kódu::xml


<šablony xml:space="preserve">
<t t-name="Váš_modul.Kořen">
Ahoj světe!
</t>
</šablony>

Poté vytvořte soubor JavaScriptu pro tento komponent v adresáři: ` / vaše_modul/ statické / src / standalone_app / root.js`.

... kódový blok::js

import { Komponenta } z "@odoo/owl";

export třída Root prodlouží třídu Komponenta následovně:
statická šablona = „your_module.Root“;
statické props = {};
    }

Je obecně dobrý nápad mít nastavení aplikace, které komponentu nainstaluje, oddělené.
souboru. Vytvořte soubor JavaScriptu, který bude aplikaci umísťovat do: ` / vašeho_modulu/statické/src/samostatná_aplikace/app.js`.

... kódový blok::js

import { kdyžBudePřipravený } z "@odoo/owl";
import { připojit komponentu } z "@web/env";
import { Root } z „./root“;

když je připraveno (=>), připevníme komponentu kořenového elementu na tělo dokumentu.

Funkce „mountComponent“ se postará o vytvoření aplikace Owl a její konfiguraci.
správně: vytvoří prostředí, spustí služby <frontend/services>, zajistí
aplikace je přeložena a umožňuje aplikaci přistupovat k šablonám ve vašem balíčku aktiv.
Věci.

.. viz též:
:ref:`Soubor s odkazy na komponenty <frontend/components>.


2. Vytvoření balíčku aktiv obsahující naše kódy
================================================

V manifestu vašeho modulu vytvořte nový :ref:`soubor aktiv<reference/assets_bundle>“.
Měl by obsahovat balíček „web._assets_core“, který obsahuje JavaScript Odoo.
rámec a základní knihovny, které potřebuje (například Owl a luxon), po kterých můžete
glob, který přidá všechny soubory aplikace do balíčku.

.. kódový blok:: py
:zvýrazněte-řádky: 9-10

    {
        # ...
"aktiva": {
"your_module.assets_standalone_app": [
('zahrnout', '_web.asset_helper')
'web/statické/před-proměnné.scss'
'web/statické/lib/bootstrap/scss/_proměnné.scss',
(‚include‘, ‚web._assets_bootstrap‘)
('include', '_web.assets.core')
'your_module/statické/zdrojové/samostatná aplikace/**/*'
            ],
        }
    }

Další řádky jsou balíčky a soubory saskritu, které jsou potřeba k tomu, aby Bootstrap fungoval.
povinné, protože komponenty webového rámce používají třídy pro stylizování z bootstrapu.
layout.

.. upozornění:
Ujistěte se, že soubory pro samostatnou aplikaci jsou přidány pouze do této sady, pokud již
mít definici pro web.assets_backend nebo web.assets_frontend a mají globy, pak
jistě, že tyto globy neodpovídají souborům pro vaši samostatnou aplikaci, jinak by se spouštěcí kód
Vaše aplikace bude konfliktovat s již existujícím spouštěcím kódem v těchto balíčcích.

.. viz též:
:ref:`Manifest modulu <reference/module/manifest>.

3. XML pohled, který volá aktivační balíček
========================================

Nyní, když jsme vytvořili naši sadu aktiv, musíme vytvořit
:ref:`QWeb výhled <reference/view_architectures/qweb>“ využívající tento balíček aktiv.

... blok kódu::xml


<odoo>
<template id="vase-modul.samostatna-aplikace">

<hlavička>
<script type="text/javascript">
var odoo = {
csrf_token: "<t t-nocache='Token CSRF musí být vždy aktuální.' t-esc='request.csrf_token(None)'" />
debug: "<t t-out="debug"/>",
__session_info__: <t t-esc="json.dumps(session_info)"/>
                        };


</hlavička>





Tento šablona dělá pouze dvě věci: inicializuje globální proměnnou odoo a poté volá aktivační funkce.
balíček, který jsme právě definovali. Inicializace globální proměnné „odoo“ je nezbytná. Tato proměnná
Měl by obsahovat následující:

- CSRF token, který je v mnoha případech nutný pro interakci s HTTP kontrolerem.
- Hodnota pro ladění, která se používá na mnoha místech k přidání dalšího záznamu nebo kontroly vhodné pro vývojáře.
- __sesní informace__, které obsahují informace ze serveru, které jsou vždy potřebné a pro které
chceme provést další požadavek. Více v následujícím odstavci.

4. Kontroler, který zobrazuje pohled
===================================

Nyní máme pohled, ale musíme jej zpřístupnit uživateli. Pro tento účel vytvoříme
:ref:`httpový kontroler <reference/controllers>`, který tuto stránku vykreslí a vrátí ji uživateli.

.. kódový blok:: py

od odoo.http import požadavek, trasa, kontroler

třída YourController(Controller):
@route("/vaše_modul/samostatná aplikace", autentizace="veřejné")
def standalone_app(self):
vraťte požadavek na renderování
'your_module.standalone_app'
                {
'session_info': požadavek.env['ir.http'].get_frontend_session_info()
                }
            )

Pozorujte, jak předáváme šablonu „session_info“. Získáváme ji z funkce „get_frontend_session_info“
metoda a nakonec bude obsahovat informace používané webovým rámcem, jako je například aktuální
uživatelské ID přihlášeného uživatele, verze serveru, edice Odoo atd.

V tomto bodě byste měli otevřít v prohlížeči adresu URL /your_module/standalone_app.
uvidíte prázdnou stránku s textem „Ahoj světe“. V tomto bodě můžete začít psát skutečný kód.
kód pro vaši aplikaci.
