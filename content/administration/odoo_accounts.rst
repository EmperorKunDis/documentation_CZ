=================
Účty na odoo.com
=================

Tento dokument popisuje, jak upravit a spravovat účet na webu odoo.com včetně přidání klienta.
databáze, smazání účtu, obnovení hesla a zapnutí dvoufaktorového ověřování.

Přidělte uživatelům přístup k databázi
==============================

Databáze může být propojena s účtem na Odoo.com, který vytvořil jiný uživatel Odoo.com.
Tím se databáze zobrazí v části „Moje databáze“ účtu.
Klientský účet na webu Odoo.com musí být v databázi přidán jako uživatel.

Nejprve se přihlaste do účtu Odoo.com, který vytvořil databázi klientů. V hlavním rozhraní Odoo
databáze a přejděte do aplikace „Nastavení“, kde klikněte na položku „Správa uživatelů“.
:guilabel:`Uživatelé“ části. Klikněte na tlačítko „Nový“, zadejte jméno do
Jméno uživatele do pole „Jméno“ a poté zadejte e-mailovou adresu použitou při registraci požadovaného
Účet na odoo.com v poli „E-mail“. Vraťte se zpět do políčka „Nastavení“ pomocí
kousky chleba, a v okně se objeví upozornění s titulkem „Zvání uživatelů“ a varováním
Přidáním dalších uživatelů se zvýší cena předplatného.

Klikněte na tlačítko „Potvrdit“ a seznam uživatelů se zobrazí. Přihlášení proběhne automaticky.
na e-mailovou adresu. Jakmile je potvrzena, databáze klientů se nyní zobrazuje v části **Moje databáze**
stránka cílového účtu Odoo.com.

..tip:
Chcete-li poskytnout tomuto uživateli plný přístup do databáze, nastavte pole :guilabel:`Dashboard`.
hlavičku „Produktivita“ na „Admin“. Poté nastavte
:guilabel:`Administrace“ pole pod hlavičkou :guilabel:`Administrace“.
:guilabel:`Nastavení“.

Smazat účet na webu odoo.com
=======================

Chcete-li smazat účet na webu Odoo.com, začněte kliknutím na profilový obrázek v pravém horním rohu
(které je zobrazeno uživatelským jménem a ikonou) se objeví rozbalovací nabídka. Vyberte
„Můj účet na Odoo.com“, který odhaluje uživatelský portál.

Z uživatelského portálu se dostanete k možnosti smazání přes:
Upravit nastavení zabezpečení - Smazat účet“. Můžete se k němu také dostat přes
„https://www.odoo.com/my/home <https://www.odoo.com/my/home>“.

.. nebezpečí:
Smazání účtu v Odoo je nevratné. Při provádění této akce buďte opatrní, protože odoo.com
Účet je **nevratně** smazán, jakmile byl odstraněn.

Po kliknutí na tlačítko „Smazat účet“ se objeví okno s žádostí o
potvrzení o smazání účtu.

.. obrázek: odoo_accounts/delete-account.png

:alt:Kliknutím na tlačítko Smazat účet se otevře okno, které potvrzuje změnu.

Pro potvrzení smazání zadejte heslo a přihlašovací jméno účtu.
odstraněna. Poté klikněte na tlačítko „Smazat účet“ pro potvrzení smazání.

... _odoocom/change_password:

Změna hesla k účtu na odoo.com
================================

Nejprve se přihlaste do uživatelského účtu na webu www.odoo.com z webové stránky www.odoo.com
přihlášení. Po přihlášení se přesuňte do pravého horního rohu obrazovky a klikněte na :guilabel:`▼
(svislá šipka) vedle ikony profilu. Pak vyberte možnost „Můj účet“ a portál
objeví se panel nástrojů.

Pro změnu hesla na webu Odoo.com klikněte na odkaz „Upravit nastavení zabezpečení“ pod
V sekci „Zabezpečení účtu“ proveďte potřebné změny a zadejte aktuální
:guilabel:`Heslo“, :guilabel:`Nové heslo“ a ověřte nové heslo. Nakonec klikněte na
Klikněte na „Změnit heslo“ a dokončete změnu hesla.

.. poznámka::
Pokud by zákazník chtěl změnit přihlašovací jméno, kontaktujte podporu Odoa zde
<https://www.odoo.com/help>.

.. poznámka::
Uživatelské heslo pro Odoo.com a portál zůstává oddělené i když se jedná o stejný e-mail.
používány.

Přidejte dvoufaktorovou autentizaci
=============================

Chcete-li přidat dvoufaktorové ověření, přihlásit se do účtu uživatele na webu Odoo.com z stránky přihlášení na webu Odoo.com.
Po přihlášení se přesuňte do pravého horního rohu obrazovky a klikněte na tlačítko :guilabel:`▼ (dolů
ikonu lukovice vedle ikony profilu. Pak vyberte „Můj účet“ a portál
objeví se panel nástrojů.

Pokud by uživatel chtěl zapnout dvoufaktorovou autentizaci (2FA) pro přístup k Odoo.com, klikněte na
:guilabel:`Upravit nastavení zabezpečení“ odkaz pod sekcí „Bezpečnost účtu“.

Klikněte na „Povolit dvoufaktorové ověření“ a zapněte si „2FA (dvoufázové ověření)“.
Potvrďte současné heslo v poli „Heslo“ a klikněte na tlačítko
na políčko „Potvrzení hesla“. Následně aktivujte dvoufaktorové ověřování
a:zkratka: 2FA (dvoufaktorová autentizace) aplikace (Google Authenticator, Authy atd.) pomocí skenování
:guilabel:`QR kód“ nebo zadáním „Kontrolního kódu“.

Poté klikněte na tlačítko „Zapnout dvoufázové ověření“ a dokončete nastavení.

.. poznámka::
Pod záložkou „Můj účet“ mohou uživatelé služby Odoo také přistupovat k následujícímu:

   - :guilabel:Dashboard partnera
   - :guilabel:`Moje služby v rámci aplikace“
   - :guilabel:`Můj přehled aplikací“
