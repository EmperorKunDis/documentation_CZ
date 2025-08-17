========================================
Připojte Gmail k Odoo pomocí služby Google OAuth
========================================

Odoo je kompatibilní s ověřováním přes Google pro Gmail. Chcete-li odesílat zabezpečené e-maily ze svého vlastního
doménu je potřeba jen nakonfigurovat několik nastavení na platformě Google Workspace.
i na zadní straně databáze Odoo. Tato konfigurace funguje buď pomocí osobního
e-mailová adresa nebo adresa vytvořená na základě vlastního doménového jména.

.. tip::
Pro více informací navštivte dokumentaci Google
<https://support.google.com/cloud/answer/6158849>

.. viz též:
   - :/aplikace/obecné/uživatelé/google
   - :doc:`/aplikace/produktivita/kalendář/google`

Nastavení v Google
===============

Vytvořte nový projekt
--------------------

Chcete-li začít, navštivte „Google API Console <https://console.developers.google.com>“. Přihlaste se
s vaším účtem Google Workspace (pokud ho máte), jinak se přihlaste pomocí svého osobního e-mailu na Gmail
účet (toto by mělo odpovídat e-mailové adrese, kterou chcete v Odoo nakonfigurovat).

Po kliknutí na tlačítko „Vytvořit projekt“, které se nachází v pravém horním rohu obrazovky, zadejte následující údaje.
souhlasí s obrazovkou. Pokud uživatel vytvořil projekt v této službě, zobrazí se obrazovka „Nový
Možnost „Projekt“ se nachází v pravém horním rohu pod volbou „Vybrat projekt“.
menu.

Na obrazovce „Nové projekty“ přejmenujte :guilabel:`Jméno projektu“ na „Odoo“.
Procházejte a vyhledejte „Lokalitu“. Nastavte „Lokalitu“ jako *Google Workspace
organizace. Pokud používáte osobní účet Gmailu, pak nechte pole „Lokalita“ prázdné
:guilabel:Žádné organizace.

.. obrázek: google_oauth/new-project.png
:align:center
:alt:Název a umístění projektu pro službu Google OAuth.

Klikněte na tlačítko „Vytvořit“ pro dokončení této fáze.

OAuth souhlas s obrazovkou
--------------------

Pokud se stránka neodklikne na volby „Typ uživatele“, klikněte na „OAuth
Souhlasím v levém menu.

V seznamu možností „Typ uživatele“ vyberte příslušný typ uživatele a pak klikněte na
:guilabel:`Vytvořit znovu“, což nakonec vyvolá dialog „Upravit registraci aplikace“.
stránka.

.. varování:
*Osobní* účty Gmail jsou povoleny pouze jako typ uživatele **Externí**, což znamená, že Google může
Je třeba získat schválení nebo přidat do nich *Scopes*. Používání účtu Google Workspace však
umožňuje používat uživatelské typy **Interní**.

Zároveň je třeba poznamenat, že když je připojení k API v režimu testování *Externí*, pak žádné schválení
je nutné od Googlu. V testovacím režimu je omezení počtu uživatelů na 100.

Editace registrace aplikace
---------------------

Nyní konfigurujeme registraci aplikace projektu.

V kroku „Souhlas s OAuth“ vyplňte do sekce „Informace o aplikaci“
Do pole „Název aplikace“ zadejte „Odoo“. Vyberte e-mailovou adresu organizace pod
:guilabel:`Podpora uživatelů“ pole e-mailu.

Dále klikněte na tlačítko „Přidat doménu“ pod položkou „Doména aplikace -> Autorizované domény“.
zadat „odoo.com“.

Poté v sekci Kontaktní údaje vývojáře zadejte organizační údaje.
e-mailová adresa. Google používá tuto e-mailovou adresu k oznámení organizace o jakýchkoli změnách ve vašem
projektu.

Poté klikněte na tlačítko „Uložit a pokračovat“. Pak přeskočte stránku „Sady“
Přejděte na konec a klikněte na „Uložit a pokračovat“.

Pokud chcete pokračovat v testovacím režimu (Externí), přidejte e-mailové adresy, které jsou nastavené pod
Krok „Uživatelé k testování“, kliknutím na „Přidat uživatele“ a poté na „Uložit“.
Pokračovat“. V seznamu registrací aplikace se zobrazí souhrnná informace o registraci.

Nakonec se přesuňte na konec a klikněte na „Zpět do dashboardu“
projektu.

Vytvořte přihlašovací údaje
------------------

Nyní, když je projekt nastavený, by měly být vytvořeny přihlašovací údaje, které zahrnují
*Klientské tajné heslo*. Nejprve klikněte na položku „Přihlašovací údaje“ v levém sloupci nabídky.

Poté klikněte na položku „Vytvořit přihlašovací údaje“ v horním menu a vyberte možnost „ID OAuth klienta“.
z rozbalovací nabídky.

- V poli „Typ aplikace“ vyberte možnost „Webová aplikace“ z rozevírací nabídky.
- Do pole „Název“ zadejte Odoo.
- Pod štítkem „Povolené přesměrovací adresy“ klikněte na tlačítko „Přidat adresu“ a
Pak zadejte do pole „URI 1“ URL adresu https://vaše_db_název.odoo.com/google_gmail/potvrzení.
Ujistěte se, že nahradíte část URL *yourdbname* skutečným názvem databáze Odoo.
- Dále klikněte na tlačítko „Vytvořit“ a vygenerujete klíč OAuth „ID klienta“ a „Klientský klíč“.
„Tajné“. Nakonec zkopírujte každý vygenerovaný hodnotu pro pozdější použití při konfiguraci v Odoo a pak
navigovat do databáze Odoo.

.. obrázek: google_oauth/client-credentials.png
:align:center
:alt:Klientské ID a klientský tajný klíč pro službu Google OAuth.

Nastavení v Odoo
=============

Přihlaste se pomocí přihlašovacích údajů Googlu
------------------------

Nejprve otevřete Odoo a přejděte do modulu :guilabel:`Apps`. Poté odstraňte :guilabel:`Apps`.
filtr z vyhledávací lišty a vepište „Google“. Nainstalujte modul s názvem :guilabel:„Google
Gmail.

Poté přejděte na „Nastavení -> Obecné nastavení“ a pod položkou „Diskuse“
sekci, zkontrolujte, že je zaškrtnuté pole pro :guilabel:`Vlastní e-mailové servery“ nebo :guilabel:"Externí
Zkontroluje se server. To vytvoří novou možnost pro :guilabel:`Přihlašovací údaje Gmailu“ nebo :guilabel:`Používat
Gmail Sever“. Poté zkopírujte příslušné hodnoty do pole „Klientské ID“
:guilabel:`Tajné heslo klienta“ a stiskněte tlačítko „Uložit“.

Nastavit odchozí e-mailový server
-------------------------------

Pro konfiguraci externího účtu na Gmailu se vraťte nahoru do části „Vlastní e-mailové servery“
a pak klikněte na odkaz „Výchozí e-mailové servery“.

.. obrázek: google_oauth/outgoing-servers.png
:align:center
:alt:Nastavení odchozích e-mailových serverů v Odoo.

Poté klikněte na „Nový“ nebo „Vytvořit“, abyste vytvořili nový e-mailový server, a vyplňte
Název, popis a e-mailovou adresu (pokud je vyžadována).

Dále klikněte na „Ověření přístupu pomocí Gmailu“ nebo „Gmail“ (pod
Přihlaste se (v části „Přihlášení“ nebo „Připojení“) a nakonec klikněte na
:guilabel:`Připojte svůj účet Gmail“.

Otevře se nové okno s názvem „Google“ a vyberte
vhodné e-mailové adresy, které se konfigurují v Odoo.

Pokud je e-mailová adresa osobní účet, pak se objeví další krok, takže klikněte
:guilabel:`Pokračovat“ a umožnit ověření a propojení účtu Gmail s Odoo.

Poté přepněte na „Pokračovat“ nebo
:guilabel:`Povolit“. Poté se stránka vrátí na nově nakonfigurovanou odchozí poštu
server v Odoo. Konfigurace automaticky načte token do Odoo a přidá štítek
Ve zeleném se objeví „Gmail Token Valid“.

.. obrázek: google_oauth/green-token.png
:align:center
:alt:Nastavení odchozích e-mailových serverů v Odoo.

Poté klikněte na „Ověřit připojení“. Potvrzení by mělo být zobrazeno.
mohou nyní bezpečně a zabezpečeně odesílat e-maily prostřednictvím služby Google pomocí ověření OAuth.

Často kladené otázky o službě Google OAuth
================

Výroba vs. testování a publikace stavu
---------------------------------------

Vybrat „Produkce“ jako „Stav vydání“ (namísto
zobrazí následující varovný vzkaz:

.. obrázek:: google_oauth/published-status.png
:align:center
:alt:OAuth je omezen na 100 citlivých přihlášení.

Chcete-li tento upozornění opravit, přejděte na stránku „Google API Platform
<https://console.cloud.google.com/apis/credentials/consent>`. Pokud je stav publikační služby
:guilabel:Ve výrobě, klikněte na :guilabel:Zpět do testování a opravte problém.

Žádný testovací uživatel nepřidán
-------------------

Pokud se do souhlasu s OAuth nepřidají žádní testovací uživatelé, pak bude chybová zpráva „přístup odepřen“
Obyvat.

.. obrázek:: google_oauth/403-error.png
:align:center
:alt: Chyba přístupu odepřen.

Chybu lze opravit návratem na obrazovku „Souhlas s OAuth“ pod „API a služby“.
Přidejte služby a přidejte uživatele testu do aplikace. Přidejte e-mail, který jste nastavili v Odoo.

Modul Gmail nebyl aktualizován
------------------------

Pokud modul Google Gmail v Odoo nebyl aktualizován na nejnovější verzi, pak
Chybová hláška „Zakázáno“ se objeví.

.. obrázek:: google_oauth/forbidden-error.png
:align:center
:alt:Zakázáno, nemáte oprávnění přistupovat k požadované službě.

Chybu lze opravit v modulu „Aplikace“ a vymazáním hledaných výrazů. Pak
Hledejte „Gmail“ nebo „Google“ a aktualizujte modul „Google Gmail“. Nakonec klikněte
na tři tečky v pravém horním rohu modulu a vyberte Upgrade.

Typ aplikace
----------------

Při vytváření přihlašovacích údajů (OAuth *Client ID* a *Client Secret*) je-li zvoleno:
Vybrán pro typ aplikace, objeví se chyba autorizace.

.. obrázek: google_oauth/error-400.png
:align:center
:alt:Chyba 400 - Odkaz na přesměrování neodpovídá.

Chybu lze opravit tak, že se smažou již vytvořené přihlašovací údaje a vytvoří se nové přihlašovací údaje, při jejichž tvorbě je vybrána
Vyberte „Webová aplikace“ pro typ aplikace a pak pod „Autorizované
přesměrovat URIs, klikněte na tlačítko „Přidat URI“ a zadejte:
„https://yourdbname.odoo.com/google_gmail/confirm“ do pole, vždy s nahrazením *yourdbname*.
v adrese URL s názvem databáze Odoo.
