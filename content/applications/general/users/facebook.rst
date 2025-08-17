===============================
Přihlášení přes Facebook
===============================

Funkce přihlášení pomocí služby *Facebook* umožňuje uživatelům Odoo přihlásit se do databáze prostřednictvím svého účtu na
Facebookový účet.

.. nebezpečí::
Databáze uložené na Odoo.com by neměly používat přihlášení pomocí OAuth pro vlastníka nebo administrátora
databáze, protože by se tak odpojila databáze od jejich účtu na Odoo.com. Pokud je nastavené OAuth,
tohoto uživatele, databáze již nelze kopírovat, přejmenovávat nebo jinak spravovat z
Portál Odoo.com.

Meta pro vývojáře
=========================

Přejděte na stránku „Meta pro vývojáře“ (<https://developers.facebook.com/>) a přihlaste se. Klikněte na „Můj účet“.
Aplikace. Na stránce Aplikace klikněte na tlačítko Vytvořit aplikaci.

Na stránce „Příklady použití“ vyberte možnost „Přihlásit se a požádat o data uživatelů“.
Přihlašovací stránka Facebooku, pak klikněte na tlačítko „Další“.

Do pole „Přidat název aplikace“ zadejte „Odoo Login OAuth“, nebo podobný titul.

.. poznámka::
Výchozí hodnota položky „Kontaktní e-mailová adresa“ je automaticky nastavena na e-mailovou adresu, která je spojená s
Meta účet. Pokud tato e-mailová adresa není pravidelně kontrolována, může být rozumné použít jinou
e-mailová adresa.

Klikněte na „Další“. Zkontrolujte požadavky na publikaci a metainformace.
Platforma Terms“ a „Vývojářské politiky“. Pak klikněte na „Vytvořit aplikaci“.

.. důležité::
Kliknutím na tlačítko :guilabel:`Vytvořit aplikaci` může být vyžadováno zadání hesla znovu.

Upravte aplikaci
-------------

Po vytvoření nové aplikace se zobrazí stránka Dashboard s seznamem kroků, které je třeba provést.
předtím, než aplikaci můžete zveřejnit. Zde klikněte na:guilabel:`Upravit přidání Facebook
Tlačítko Přihlásit se.

.. obrázek: facebook/app-requirements.png
:align:center
:alt:Dashboard aplikací v rámci platformy pro vývojáře Meta.

Na stránce „Nastavení“ klikněte na „Možnosti“.

Do pole „Platná odkazová adresa OAuth“ zadejte „https://<odoo base
url>/auth_oauth/signin`, kde <odoo base url> je URL databáze, ke které se vztahuje.

.. příklad::
Pokud má databáze adresu URL https://example.odoo.com, pak je
„https://example.odoo.com/auth_oauth/signin“ by se zadalo do pole :guilabel:`Ověření přes
pole Redirect URI

Klikněte na tlačítko „Uložit změny“ po dokončení.

Nastavte parametry
------------------

Na nejlepší části stránky klikněte na:menu-selection:'Nastavení aplikace --> Základní nastavení'. Tato stránka obsahuje
další nastavení, které je potřeba před podáním aplikace k schválení.

Do pole „URL“ v položce „Zásady ochrany osobních údajů“ zadejte https://www.odoo.com/privacy.

.. poznámka::
„<https://www.odoo.com/privacy>“ je výchozí politika ochrany osobních údajů pro databáze hostované na Odoo.com.

Klikněte na pole „Ikona aplikace“ pro otevření okna pro nahrání souboru. Zde vyberte a nahrajte
ikonu aplikace.

Do pole „Smazání uživatelských dat“ zadejte
„https://www.odoo.com/documentation/17.0/administration/odoo_accounts.html“.

.. poznámka::
Tento dokument obsahuje pokyny, jak uživatel může smazat svůj účet v Odoo.

Nakonec klikněte na pole „Kategorie“ a vyberte „Obchod a stránky“.
kliknutím na tlačítko „Přidat do košíku“.

Klikněte na tlačítko „Uložit změny“.

.. obrázek: facebook/app-id.png
:align:center
:alt: Příklad stránky Základní nastavení v rámci platformy pro vývojáře Meta.

..._uživatelé/aplikace-id:

Získat identifikační kód aplikace
--------------

Po vytvoření a schválení aplikace vyberte a zkopírujte :guilabel:`ID aplikace` a vložte ji
informace na klipramech nebo v poznámkovém bloku, protože je budete potřebovat v dalším kroku pro dokončení nastavení.

Vydat
-------

Na levé straně stránky klikněte na tlačítko „Zveřejnit“. V závislosti na stavu připojeného
Facebookový účet, další ověření a kroky testování mohou být vyžadovány a jsou uvedeny na
stránka.

Po prohlédnutí informací klikněte na tlačítko „Zveřejnit“.

.. viz též:
Další informace o vývoji aplikací Meta, včetně dalších podrobností o stavbě
testování a příklady použití naleznete v dokumentaci pro vývojáře Meta.
<https://developers.facebook.com/docs/development>.

Nastavení Odoo
==========

Nejprve aktivujte režim vývojáře: :ref:`Režim vývojáře <developer-mode/activation>`.

Přejděte do aplikace „Nastavení“ a posuňte se dolů k položce „Spojení“.
sekci. Tam zaškrtněte políčko s názvem „OAuth Authentication“ a klikněte na „Uložit“.

.. obrázek: facebook/enable-oauth.png
:align:center
:alt:Nastavení OAuth v aplikaci Nastavení.

Pak se přihlaste do databáze poté, co se načte obrazovka přihlášení.

Po úspěšném přihlášení přejděte na: „Nastavení aplikace“ --> „Uživatelé a společnosti“.
OAuth poskytovatelů. Klikněte na: guilabel: Facebook Graph.

Do pole „Klientské ID“ zadejte :ref:`ID aplikace <users/app-id>“ z předchozího
sekci, pak zaškrtněte políčko „Povolené“.

.. obrázek:: facebook/facebook-graph.png
:align:center
:alt:Záznam o Facebook Graphu v Odoo.
