================
Google překladač
================

Pomocí Google Translate lze přeložit uživatelsky vytvořený text v chatu Odoo.

Google API konzole
==================

Většina nastavení pro integraci Google Translate do Odoo je prováděna prostřednictvím služby Google API
konzole*. Po dokončení následujících procesů je vytvořen klíč API, který se zadává do Odoo.

.. viz též:
„Nastavení služby Google Translate na Googlu <https://cloud.google.com/translate/docs/setup>“

Vytvořte nový projekt
--------------------

Chcete-li začít, přejděte na stránku „Google API Console <https://console.developers.google.com>“. Pak se
s účtem Google Workspace (pokud existuje). Pokud ne, přihlaste se pomocí osobního účtu Gmail
(toto by mělo odpovídat e-mailové adrese, ke které je připojen fakturační účet).

Poté klikněte na „Vytvořit projekt“ v pravém dolním rohu obrazovky pro udělení souhlasu s OAuth.

.. tip::
Pokud máte v Google API Console existující projekty, klikněte na rozevírací nabídku vedle
:guilabel:`Google Cloud“ ikona a vyskočí okno. Nyní klikněte na „New Project“.
v horním pravém rohu okna přesahujícího.

Na obrazovce „Nová projektová stránka“ přejmenujte „Jméno projektu“ na „Odoo Translate“.
Procházejte a vyhledejte „Lokalitu“. Nastavte „Lokalitu“ jako *Google Workspace
organizace. Pokud je použit osobní účet Gmailu, nechte pole „Lokalita“
:guilabel:Žádné organizace.

.. obrázek: google_translate/novy-projekt.png
:align:center
:alt:Název a umístění projektu pro službu Google OAuth.

Klikněte na tlačítko „Vytvořit“ pro dokončení této fáze.

Knihovna API
-----------

Poté je třeba nainstalovat do projektu nově vytvořeného službu Cloud Translation API.
Klikněte na položku „Knihovna“ v levém menu. Pak vyhledejte pojem „Cloud Translation API“, a
klikněte na výsledek. Tento by měl být označen jako „Google Enterprise API“ s názvem: guilabel: Cloud Translation
API.

Klikněte na tlačítko „Povolit“ a nainstalujte knihovnu do tohoto projektu.

.. důležité::
Používání služby Google Translate vyžaduje platný účet.
<https://účet.google.com/>`.

Jakmile je účet nastavený u společnosti Google a knihovna je zapnutá, klikněte na tlačítko „Spravovat“.
dokončit konfiguraci na API.

Vytvořte přihlašovací údaje
------------------

Nyní, když je projekt nastavený a funkce „Cloud Translation API“ aktivována, musí být přístupové údaje
včetně API klíče.

Pro zahájení procesu klikněte na položku „Přihlašovací údaje“ v levém sloupci nabídky.

Poté klikněte na tlačítko „Vytvořit přihlašovací údaje“ v horním menu a vyberte možnost „API klíč“.
kliknutím na tlačítko „Přidat do košíku“.

.. obrázek: google_translate/api-key.png
:align:center
:alt:Vytvořte klíč v konzoli služby Google API.

Zkopírujte klíč API pro použití v další části.

.. důležité::
Pro zabezpečení může být omezeno používání klíče API.

Chcete-li to udělat, přejděte na stránku omezení API kliknutím na tlačítko „Upravit klíč API“ v okně
okno nebo kliknutím na seznam klíčů API v části „Kreditní údaje“. Zde je možné zadat klíč
omezení lze nastavit. To zahrnuje nastavení aplikace tak, aby se omezilo používání klíče API.
a zda tento klíč může volat jakoukoli API.

Je doporučeno, aby API pro překlad Odoo *Translate* bylo omezeno pouze na požadavky z **jediného**
konfigurovanou databázi Odoo a k aplikaci pro překlad do cloudu.

Přidat omezení webu je možné kliknutím na položku Webové stránky pod položkou Vyberte, jaké typy obsahu chcete blokovat.
„Omezení aplikace“. Pak zadejte adresu databáze Google Translate.
použít kliknutím na tlačítko „Přidat“. Nakonec přidejte :abbr:`URL (Uniform Resource Locator)“
a klikněte na tlačítko :guilabel:`Hotovo`.

Pro omezení použití klíče na vybranou aplikaci nejprve vyberte možnost „Omezit klíč“ pod položkou
:guilabel:`Omezení API“ a poté vyberte z roletky API, které chcete omezit.
nakonfigurované (API pro překlad do cloudu).

.. tip::
   - Uložte klíč API: zkopírujte klíč API a uložte ho na bezpečném místě.
   - API klíč nikdy nezveřejňujte a v kódu na straně klienta ho nesmí být vidět.

Konfigurace Odoo
==================

Pro přístup k integraci v Odoo přejděte na: „Nastavení aplikace“ -> „Diskuse“.
sekci. Zadejte klíč API do pole označeného:guilabel:'Překlad zprávy'. Pak
Uložte nastavení a můžete používat Google Překladač v jakémkoliv chatu.
databáze.

.. obrázek: google_translate/odoo-config.png
:align:center
:alt: Konfigurace klíče API z Google API Console.

Přeložte šeptání
=================

Pro překlad uživatelského textu do jiného jazyka klikněte na ikonu „… (tři tečky)“ v nabídce
právo na chatu. Pak vyberte: guilabel:"Přeložit". Obsah přeloží do
Jazyk nastavený na preference uživatele.

.. obrázek:: google_translate/google-translate.png
:align:center
:alt:Přítomnost služby Google Translate v chatovací místnosti databáze Odoo.

.. viz též:
:ref:`instalace jazyka
