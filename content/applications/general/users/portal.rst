=============
Přístup do portálu
=============

.. _portal/hlavní:

Přístup do portálu je poskytován uživatelům, kteří potřebují možnost zobrazit určité dokumenty nebo informace.
Odoo databáze.

Mezi běžné případy použití portálu patří umožnění zákazníkům číst nebo zobrazovat libovolný obsah.
v následujících modulůch v Odoo:

- leads/příležitosti
- cenové nabídky, objednávky
- objednávky na nákup
- faktury a účty
- projekty
- úkoly
- evidence pracovní doby
- lístky
- podpisy
- předplatné

.. poznámka::
Uživatelé portálu mají pouze čtenářský přístup a nebudou moci upravovat žádné dokumenty v
databáze.

.._portál/přístup:

Dát zákazníkům přístup do portálu
==================================

Na hlavní obrazovce aplikace Odoo vyberte modul Kontakty. Pokud kontakt ještě nebyl vytvořen,
vytvořené v databázi, klikněte na tlačítko „Vytvořit“, zadejte podrobnosti o kontaktu
a pak klikněte na „Uložit“. Jinak vyberte existující kontakt a pak klikněte na
:guilabel:`Akce“ v horní části centra obrazovky.

.. obrázek: portál/přístup-k-portálu-pro-poskytovatele-dotací.png
:align:center
:alt:Použijte aplikaci Kontakty k udělení přístupu do portálu uživatelům.

Vyberte možnost „Povolit přístup k portálu“. V okně se objeví tři pole:

- :guilabel:`Kontakt“: zaznamenané jméno kontaktu v databázi Odoo
- :guilabel:`E-mailová adresa“: e-mailová adresa kontaktu, kterou použije při přihlašování do portálu
- :guilabel:`V portálu“: zda uživatel má přístup do portálu

Pro udělení přístupu do portálu nejprve zadejte kontaktní e-mailovou adresu, kterou bude uživatel používat k přihlášení.
Portál. Poté zaškrtněte políčko pod sloupcem „V Portálu“. Volitelně můžete do pole přidat text.
zprávu, kterou kontakt obdrží. Pak klikněte na tlačítko „Přijmout“ a proces dokončete.

.. obrázek: portál/přidat-kontakt-do-portálu.png
:align:center
:alt:Do pole E-mailová adresa a odpovídajícího zaškrtávacího políčka pro kontakt je nutné vyplnit e-mailovou adresu.
zaslání pozvánky na portál.

Na zadanou e-mailovou adresu bude zaslán e-mail s informací, že kontakt je nyní portálem
uživatel pro tuto databázi Odoo.

.. tip::
Pokud chcete umožnit přístup k portálu více uživatelům najednou, přejděte na kontakt firmy, pak klikněte
:menu „Akce“ -> „Přidat přístup do portálu“ pro zobrazení seznamu všech souvisejících společností.
kontakty. Zkontrolujte políčko pod sloupcem „V portálu“ u všech kontaktů, které potřebují
Přihlaste se do portálu a klikněte na „Aplikovat“.

.. poznámka::
Přístup do portálu může být kdykoliv zrušen tím, že se přejde na kontakt a klikne
:menuvolba:`Akce --> Povolit přístup k portálu“, a poté odškrtnutím zaškrtávacího políčka pod
:guilabel:`Ve sloupci Portál“ a kliknutím na „Použít“.

.. _portal/prihlaseni:

Změnit uživatelské jméno portálu
======================

Přihlášení k portálu může uživatel změnit, pokud chce, a to kdykoliv
v databázi s právy administrátora. Následující postup popisuje potřebné kroky
změnit přihlašovací údaje uživatele portálu.

.. viz též:
:ref:`Více informací o nastavení přístupových práv naleznete v dokumentaci


Nejprve přejděte do aplikace „Nastavení“ a poté pod položkou „Filtry“ vyberte
„Uživatelé portálu“ nebo vyberte „Přidat vlastní filtr“ a nastavte následující
Konfigurace: „Skupiny“ > „Obsaženo“ > „Portál“. Po provedení této volby
Vyhledejte (a otevřete) portálového uživatele, který chcete upravit.

Dále klikněte na tlačítko „Upravit“ (pokud je nutné) a do pole „E-mailová adresa“ vložte
pokračovat v provedení všech potřebných změn ve sloupci. Sloupec „E-mailová adresa“ se používá k
Přihlásit se do portálu Odoo.

.. poznámka::
Změna e-mailové adresy nebo hesla změní pouze uživatelské jméno zákazníka.
portál login.

Chcete-li změnit kontaktní e-mailovou adresu, musí se tato změna provést na šabloně kontaktu.
*Kontakty*. Klienti mohou změnit svůj e-mail přímo v portálu
ale heslo nelze změnit. :ref:`Viz změna informací o zákazníkovi <portal/custinfo>.`

Změny v zákaznickém portálu
=======================

Klient může chtít změnit své kontaktní údaje.
heslo nebo bezpečnostní informace připojené k účtu portálu. Toto lze provést
z jejich portálu. Následující proces je, jak může zákazník změnit své kontaktní údaje
informace.

... _portal/custinfo:

Změna údajů zákazníka
--------------------

Nejprve zadejte uživatelské jméno a heslo (přihlášení) do databáze portálu.
účet. Po úspěšném přihlášení se zobrazí portálový panel. Dokumenty portálu
v seznamu nainstalovaných aplikací Odoo se objeví počet každé z nich.

.. viz též:
:ref:`Dokumentace přístupu do portálu <portal/main>`.

Dále přejděte do horního pravého rohu portálu a klikněte na tlačítko „Upravit“.
do sekce „Podrobnosti“. Poté změňte příslušné informace a klikněte
:guilabel:`Potvrdit“.

Změnit heslo
---------------

Nejprve zadejte uživatelské jméno a heslo (přihlášení) do databáze portálu.
účet. Po úspěšném přihlášení se zobrazí portálový panel.

Pokud by zákazník chtěl změnit heslo pro přístup do portálu, klikněte na tlačítko „Upravit
Odkaz „Nastavení zabezpečení“ pod sekcí „Bezpečnost účtu“. Pak proveďte potřebné změny.
změnit heslo, zadáním aktuálního hesla, nového hesla a ověření nového
heslo. Nakonec klikněte na „Změnit heslo“ a změnu hesla dokončete.

.. poznámka::
Pokud by zákazník chtěl změnit přihlašovací údaje, jak je uvedeno výše, kontaktujte databázi Odoo
:ref:`Viz dokumentaci výše o změně uživatelského jména portálu <portal/login>.“

.. poznámka::
Hesla uživatelů portálu a uživatelů služby Odoo.com zůstávají oddělená, i když mají stejnou e-mailovou adresu.
používány.

Přidejte dvoufaktorovou autentizaci
-----------------------------

Nejprve zadejte uživatelské jméno a heslo (přihlášení) do databáze portálu.
účet. Po úspěšném přihlášení se zobrazí portálový panel.

Pokud by zákazník chtěl zapnout dvoufaktorovou autentizaci (2FA) pro přístup do portálu, klikněte na
odkaz „Upravit nastavení zabezpečení“ pod sekcí „Zabezpečení účtu“.

Klikněte na „Povolit dvoufázové ověření“ a zapněte dvoufaktorové ověřování.
ověření). Zadejte aktuální heslo portálu do pole „Heslo“ a pak klikněte
na položku „Potvrzení hesla“. Následně aktivujte dvoufaktorové ověřování (2FA) v
Aplikace pro dvoufaktorovou autentizaci (zkráceně 2FA) (např. Google Authenticator nebo Authy), pomocí skenování
Vložení QR kódu nebo zadání ověřovacího kódu.

Konečně klikněte na tlačítko „Zapnout dvoufázové ověření“ a dokončete nastavení.

..._uživatelský portál platby metodami:

Změnit údaje o platbě
-------------------

Nejprve zadejte uživatelské jméno a heslo (přihlášení) do databáze portálu.
účet. Po úspěšném přihlášení se zobrazí portálový panel.

Pokud zákazník chce spravovat způsoby platby, přejděte na stránku „Spravovat způsob platby“.
Zvolte metodu v nabídce na pravé straně a přidejte novou platební informaci a vyberte možnost „Přidat“.
novou kartu.
