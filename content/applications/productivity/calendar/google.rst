===============================
Synchronizace s kalendářem Google
===============================

Synchronizujte kalendář Google s Odoo, abyste viděli a spravovali schůzky z obou platforem (aktualizace se
obě směry). Tato integrace pomáhá organizovat plány, takže schůzka nikdy nepropásnete.

.. viz též:
   - :doc:`/aplikace/obecné/uživatelé/Google“
   - :doc:`/aplikace/obecné/e-mailová komunikace/Google OAuth`

Nastavení v Google
===============

Vyberte (nebo vytvořte) projekt
----------------------------

Vytvořte nový projekt služby Google API a povolte službu Google Calendar API. Nejprve přejděte na stránku „Google API
Přejděte na stránku konzole <https://console.developers.google.com> a přihlaste se ke svému účtu Google.

.. poznámka::
Pokud je to první návštěva této stránky, Google vyzve uživatele k zadání země.
Přijmout podmínky služby. Vyberte z roletky zemi a přijměte podmínky služby.
:abbr:`Podmínky služby“.

Poté klikněte na „Vybrat projekt“ a vyberte (nebo vytvořte) projekt API pro konfiguraci OAuth.
a uložte přihlašovací údaje. Klikněte na tlačítko „Nový projekt“.

.. obrázek: google/novy-api-projekt.png
:alt: Vytvořte nový projekt API, kde budou uloženy přihlašovací údaje.

Projektu API přidělejte jasný název, jako například „Synchronizace Odoo“, abyste jej mohli identifikovat. Pak klikněte na
Tlačítko „Vytvořit“.

Povolit Google kalendář API
--------------------------

Nyní klikněte na položku „Povolené služby a API“ v levém menu. Vyberte „Povolené služby
a služeb znovu, pokud se pole pro vyhledávání nezobrazí.

.. obrázek:: google/enable-apis-services.png
:alt:Zapněte služby a aplikace v projektu API.

Následně vyhledejte „Google Calendar API“ pomocí vyhledávací lišty a zvolte:
Kalendář API z výsledků vyhledávání. Klikněte na „Povolit“.

.. obrázek: google/enable-google-cal-api.png
:alt:Povolit službu Google Calendar API.

OAuth souhlas s obrazovkou
--------------------

Nyní, když byl vytvořen projekt API, je potřeba nastavit OAuth. K tomu stačí kliknout na
V levém menu vyberte „Povolení OAuth“ a pak klikněte na tlačítko „Začněte“.

.. varování:
*Osobní* účty Gmailu mohou být pouze typem uživatele **Externího**, což znamená, že Google
Potřebují schválení nebo přidání *Souborů*. Při použití účtu *Google Workspace*
umožňuje použití uživatelského typu **Interní**.

Pozor také na to, že během testování v režimu *Externí* není potřeba žádné schválení.
Je nutné zadat do Googlu. Limit uživatelů v tomto testovacím režimu je nastaven na 100 uživatelů.

Postupujte podle následujících kroků, v pořadí:

#V poli „Informace o aplikaci“ zadejte do pole „Název aplikace“ Odoo a poté stiskněte
Zadejte e-mailovou adresu do pole :guilabel:`E-mailová podpora uživatelů` a klikněte na tlačítko :guilabel:`Další`.
#Vyberte v seznamu „Slyšení“ možnost „Externí“, pak klikněte na tlačítko „Další“.
#V poli „Kontaktní údaje“ zadejte e-mail znovu a pak klikněte na „Další“.
tlačítko.
#V poli „Dokončit“ zaškrtněte pole souhlasu s „Službami Google API: Uživatel“.
Zásady.  Klikněte na tlačítko „Vytvořit“.

Autorizované nastavení domény
-----------------------

Dále musí být zobrazeny všechny domény nastavené na obrazovce souhlasu nebo v konfiguraci klienta OAuth.
registrovaný. Pro provedení takového kroku přejděte na záložku „Značení“ v levém menu.
V sekci „Autorizované domény“ klikněte na tlačítko „Přidat doménu“, abyste vytvořili pole pro
Vstupte do autorizované domény. Vyberte doménu, například „odoo.com“, pak klikněte na tlačítko :guilabel:`Uložit`.
tlačítko v dolní části stránky.

Testovací uživatelé
----------

Uživatelům musí být umožněno synchronizovat se svými osobními účty Gmailu, což je možné pouze v případě, že jsou nastaveni jako testovací uživatelé.
Nastavte testovací uživatele v levém menu pod položkou „Audience“ a klikněte na
Tlačítko „Přidat uživatele“ v sekci „Testovací uživatelé“. Zadejte libovolné e-mailové adresy uživatelů.
a klikněte na tlačítko „Uložit“.

Vytvořte přihlašovací údaje
------------------

K propojení Google Kalendáře s Odoo je potřeba obě hesla – *ID klienta* a *tajné heslo*.
poslední krok v konzoli Google. Začněte kliknutím na „Klienti“ v levém menu.
Poté klikněte na tlačítko „Vytvořit přihlašovací údaje“ a vyberte možnost „ID klienta OAuth“, po otevření
návod na vytvoření přihlašovacích údajů.

Pod položkou „Vytvořit identifikátor klienta OAuth“ vyberte „Webová aplikace“.
V poli „Typ aplikace“ zadejte hodnotu „Můj Odoo databáze“, v poli „Název“ zadejte hodnotu „My Odoo Database“.

- V sekci „Oprávněné původní JavaScripty“ klikněte na „+ Přidat URL“ a zadejte
celé URL adresy společnosti Odoo.
- Pod sekcí „Povolené přesměrovací adresy“ klikněte na „+ Přidat URL“ a zadejte
adresa URL (Uniform Resource Locator) společnosti Odoo.
„/google_account/authentication“. Nakonec klikněte na tlačítko „Vytvořit“.

.. obrázek: google/uri.png
:alt:Přidejte autorizované JavaScriptové zdroje a autorizované přesměrovací URI.

Vyskočí pole s názvem „ID klienta“ a „Tajný klíč“. Uložte si je někam v bezpečí.

Nastavení v Odoo
=============

Jakmile najdete *ID klienta* a *tajný klíč klienta*, otevřete databázi Odoo a přejděte na
Klikněte na „Nastavení“ – „Správa kalendářů“, kde najdete funkci „Google Kalendář“. Zatrhněte
zaškrtávací políčko s názvem „Google Kalendář“.

.. obrázek: google/settings-google-cal.png
:alt: Zaškrtávací políčko služby Google Kalendář v Nastavení obecných informací.

Poté zkopírujte a vložte *ID klienta* a *tajemství klienta* z Google Calendar API.
přihlašovací stránku do příslušných polí pod tlačítkem „Google Kalendář“. Pak
Klikněte na tlačítko „Uložit“.

.. poznámka::
Zaškrtněte políčko „Zastavit synchronizaci“ a dočasně zastavte přijímání událostí.
aktualizovány. To umožňuje testování a řešení problémů bez odstraňování přihlašovacích údajů nebo odinstalace
synchronizaci. Chcete-li obnovit synchronizaci, odstraňte zaškrtnutí a uložte.

Synchronizace kalendáře v Odoo
=====================

Nakonec otevřete aplikaci Kalendář v Odoo a klikněte na Google.
tlačítko pro synchronizaci kalendáře Google s Odoo.

.. obrázek:: google/sync-google.png
:alt:Klikněte na tlačítko synchronizace s Google v kalendáři Odoo, abyste spojili Google Calendar s Odoo.

.. poznámka::
Při prvním synchronizačním spojení s Google Kalendářem bude stránka odeslána na Google
Účet. Zde vyberte e-mailový účet, který má mít přístup, a poté vyberte
:guilabel:"Pokračovat" (pokud aplikace není ověřená) a nakonec vyberte :guilabel:"Pokračovat" (abyste
udělit souhlas s přenosem dat.

.. obrázek: google/trust-odoo.png
:alt:Dát Odoo oprávnění přistupovat k Google Kalendáři.

Nyní je kalendář Odoo úspěšně synchronizován s Google Kalendářem.

.. varování:
Odoo doporučuje zkontrolovat synchronizaci s kalendářem Google na testovací databázi a testovacím
e-mailová adresa (která není používána pro jiné účely) před pokusem o synchronizaci požadovaných
Google Kalendář s databází uživatele.

Jakmile uživatel synchronizuje svůj kalendář Google s kalendářem Odoo:

   - Vytvoření události v Odoo způsobí, že Google pošle pozvánku všem účastníkům akce.
   - Smazání události v Odoo způsobí, že Google pošle všem účastníkům zrušení akce.
   - Přidání kontaktu do události způsobí, že Google pošle pozvánku všem účastníkům akce.
   - Odstranění kontaktu z události způsobí, že Google pošle všem účastníkům události oznámení o zrušení.

Vytvořit událost v kalendáři Google lze bez odeslání notifikace volbou
:guilabel:`Neposílejte“ v okamžiku, kdy je požádáno o zaslání pozvánek na schůzku.

Zjišťování problémů s synchronizací
=================

Může dojít k situaci, kdy účet Google Calendar nebude synchronizován s Odoo správně. Problémy se synchronizací
Mohou být vidět v databázových logech.

V těchto případech je potřeba účet vyřešit. Reset může být proveden pomocí
Tlačítko „Obnovit účet“, které lze přistupovat kliknutím na nabídku „Nastavení
Aplikace „Správa uživatelů“. Pak vyberte uživatele, jehož kalendář chcete upravit, a klikněte na
:guilabel:`Kalendář“ záložka.

.. obrázek: google/google-reset.png
:alt:Zvýrazněné tlačítko resetu v kalendáři uživatele.

Dále klikněte na tlačítko „Znovu nastavit účet“ pod správným kalendářem.

Obnovení nastavení
-------------

Pro řešení problémů s synchronizací kalendáře Google s Odoo jsou k dispozici následující možnosti obnovení:

.. obrázek: google/reset-calendar.png
:alt:Nastavení kalendáře v Odoo.

:guilabel:`Uživatelské stávající události“:

 - :guilabel:Nechat vše beze změn“: žádné změny událostí.
 - :guilabel:`Smazat z aktuálního účtu Google Kalendář“: smažte události ze *Google
Kalendář*.
 - :guilabel:`Smazat z Odoo“: smažte události ze schránky Odoo.
 - :guilabel:`Smazat z obou“: smažte události ze všech kalendářů Google a Odoo.

:guilabel:`Další synchronizace“:

 - :guilabel:`Synchronizovat pouze nové události“: synchronizujte nové události na Google Kalendář a/nebo Odoo
kalendář.
 - :guilabel:`Synchronizovat všechny existující události“: synchronizovat všechny události na Google Kalendář a/nebo Odoo
kalendář.

Po výběru možnosti klikněte na tlačítko „Potvrdit“ a poté upravte události uživatele a kalendář.
synchronizace.

Často kladené dotazy o službě Google OAuth
================

Někdy se mohou vyskytnout konfigurační chyby a je potřeba problém řešit.
chybou. Níže jsou uvedeny nejčastější chyby, které mohou nastat při konfiguraci kalendáře Google
používat s Odoo.

Výroba versus testování stavu publikace
----------------------------------------

Vybrat „Produkce“ jako „Stav vydání“ (místo
Zobrazí následující varování:

„OAuth je omezen na 100 citlivých přihlášení do aplikace, dokud není ověřen souhlas s OAuth. To může
vyžaduje proces ověření, který může trvat několik dní.

Chcete-li tento upozornění opravit, přejděte na stránku „Google API Platform
<https://console.cloud.google.com/apis/credentials/consent>`. Pokud je stav publikování
klikněte na „Zpět do testování“.

Žádný testovací uživatel
-------------------

Pokud nejsou přidáni žádní testovací uživatelé do obrazovky souhlasu s OAuth, pak se zobrazí chyba 403:
access_denied` se vyplní.

.. obrázek: google/403-error.png
:alt: Chyba přístupu odepřen.

Chybu lze opravit návratem na obrazovku souhlasu s OAuth (viz obrázek), kde je pod položkou „APIs &
Služby“ a přidat do aplikace testovací uživatele. Přidejte e-mail, který chcete nakonfigurovat v Odoo.

Typ aplikace
----------------

Při vytváření přihlašovacích údajů (OAuth *Client ID* a *Client Secret*) je-li zvoleno pole „Desktop App“
vybrán pro typ aplikace, objeví se chyba autorizace
(:guilabel:`Chyba 400: redirect_uri_mismatch“).

.. obrázek: google/error-400.png
:alt:Chyba 400 - Odkaz na přesměrování neodpovídá.

Chybu lze opravit tak, že se odstraní stávající přihlašovací údaje a vytvoří nové přihlašovací údaje.
„Webová aplikace“ pro „Typ aplikace“.

Poté klikněte na „Přidat adresu URL“ a zadejte:
„https://yourdbname.odoo.com/google_account/authentication“ do pole, ujistěte se, že nahradíte
*vaše_odb_jméno* v adrese URL s **skutečným** názvem databáze Odoo.

..tip:
Zajistěte, aby doména (použitá v URI:)
„https://vaše-db-jméno.odoo.com/google_account/autentizace“) je stejná doména jako
je konfigurován v systémovém parametru web.base.url.

Přihlaste se k webovému adresáři pomocí aktivace režimu vývojáře (viz Developer Mode) a přejděte na
:menu:Nastavení aplikace --> Hlavní nabídka technického menu --> Parametry --> Systém
Parametry.
