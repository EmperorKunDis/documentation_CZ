================================
Synchronizace kalendáře v aplikaci Outlook
================================

Synchronizace kalendáře uživatele Outlook s Odoo je užitečná pro sledování úkolů a
termíny v rámci všech souvisejících aplikací.

.. viz též:
   - :doc:`../../obecne/uzivatele/azure`
   - :doc:`../../obecne/komunikace_e-mailem/azure_oauth`

Nastavení Microsoftu Azure
=====================

Pro synchronizaci kalendáře Outlook s kalendářem v Odoo je potřeba mít účet Microsoft Azure.
Vytvoření účtu je pro uživatele zdarma, kteří nikdy předtím nevyzkoušeli nebo za něj neplatili službu Azure.
informace a zobrazit možnosti účtu na webu Azure.
<https://azure.microsoft.com/en-us/free/?WT.mc_id=A261C142F>

Sledujte dokumentaci společnosti Microsoft (<https://docs.microsoft.com/en-us/azure/active-directory/)
vytvořit nový účet>_ na to, jak vytvořit Microsoft Entra ID (dříve nazývanou
Microsoftu *Azure Active Directory (Azure AD)*). Jedná se o rozhraní API pro správu a registraci
Aplikace společnosti Microsoft.

Uživatelé existujícího systému Microsoftu *Entra ID* by se měli přihlásit na portál vývojářů Microsoft Azure.
<https://portal.azure.com/#home>. Následně vyberte položku „Zobrazit“ pod sekcí
:guilabel:`Správa identit Microsoft Entra“.

Přihláška do rejstříku
--------------------

Po přihlášení pomocí Microsoftu *Entra ID* je třeba „registrovat aplikaci
<https://docs.microsoft.com/cs-cz/azure/active-directory/develop/quickstart-register-app>.

Pro vytvoření aplikace klikněte na tlačítko „+ Přidat“ v horním menu. Vyberte si z nabídky
menu, vyberte: guilabel:"Registrace aplikace".

.. obrázek: outlook/app-register.png
:align:center
:alt:Stránka správy služby Microsoftu Azure s vyznačeným odkazem na + Přidat a registraci aplikace.

Zadejte jedinečný název pro aplikaci, ke které se připojujete.

Vybrat vhodný typ podporovaného účtu je zásadní, jinak se k němu nebude možné připojit.
aplikace nebude fungovat. Uživatelé, kteří chtějí propojit svůj kalendář Outlook s Odoo, by měli vybrat
:guilabel:`Účty v jakémkoliv organizačním adresáři (v jakémkoliv adresáři Microsoft Entra ID)
Multitenant) a osobní účty Microsoftu (např. Skype, Xbox)
druhy účtů.

Při konfiguraci :guilabel:`Redirect URI` zvolte možnost :guilabel:`Web“ z prvního
rozbalovací nabídku. Poté zadejte adresu databáze Odoo (URL), následovanou
„/microsoft_account/authentication“.

Příklad:
Zadejte adresu https://yourdbname.odoo.com/microsoft_account/authentication pro :guilabel:`Redirection
URI. Změňte „yourdbname.odoo.com“ na URL (jednotný odkazový zdroj).

..tip:
Zajistěte, aby URL (Uniform Resource Locator) (doména) použitá v URI byla
stejná doména jako je nastavená v systémovém parametru web.base.url.

Přihlaste se k webovému adresáři pomocí aktivace režimu vývojáře (viz Developer Mode) a přejděte na
:menu:Nastavení aplikace --> Hlavní nabídka technického menu --> Parametry --> Systém
Parametry“. Pak vyberte z seznamu klíčů v části „Systémové parametry“
stránka.

.. obrázek: outlook/azure-register-application.png
:align:center
:alt:Nastavení „Podporovaného typu účtu“ a „Přesměrovacího URI“ v portálu Microsoft Entra ID.

Pro více informací o omezeních a limitech URIs se podívejte na stránku Redirect URI
omezení a omezení
<https://docs.microsoft.com/en-us/azure/active-directory/develop/reply-url> stránku.

Na stránce registrace aplikace klikněte na tlačítko „Registrovat“ a dokončete
registrace aplikace. Vytvoří se hodnota :guilabel:`Application (client) ID`, která je potřebná k přihlášení do systému.
je potřeba později v části :ref:`outlook_calendar/odoo_setup`.

.. obrázek: outlook/app-client-id.png
:align:center
:alt:V sekci „Základní informace“ nově vytvořené aplikace je zvýrazněno ID klienta.
aplikace.

Vytvořit tajný klíč klienta
--------------------

Druhý kredit, který je potřeba pro dokončení synchronizace kalendáře Microsoft Outlook,
*Tajný klíč klienta*. Uživatelé **musí** přidat tajný klíč klienta, protože to umožňuje Odoo ověřit
Sám o sobě, bez jakéhokoliv zásahu ze strany uživatele. Certifikáty jsou volitelné.

Chcete-li přidat tajný klíč klienta, vyberte v levém menu položku „Soubory certifikátů a tajného klíče“. Pak klikněte
:guilabel:`+ Nový tajný klíč klienta“ vytvořit nový tajný klíč klienta.

.. obrázek: outlook/client-secret.png
:align:center
:alt: Nová stránka s certifikáty a tajnými klíči, kde je nově možnost zobrazit tajné klíče
zvýrazněny.

Poté zadejte „Popis“ a vyberte datum expirace klientského tajného klíče.
K dispozici jsou následující možnosti: :guilabel:`90 dní (3 měsíce)“, :guilabel:`365 dní (12 měsíců)“.
„545 dní (18 měsíců)“, „730 dní (24 měsíců)“ nebo „Vlastní“.
Možnost „Vlastní“ umožňuje správci nastavit hodnotu „Začátek“ a „Konec“.
datum.

Nakonec klikněte na tlačítko „Přidat“ v poli „Přidat tajný klíč“.

..tip:
Odstraňování nesynchronizovaných položek může být obtížné, proto Odoo doporučuje nastavit maximální povolenou hodnotu.
datum vypršení platnosti klientského tajného klíče (24 měsíců nebo vlastní hodnota)
co nejdříve znovu synchronizovat.

Zkopírujte hodnotu :guilabel:`Value`, kterou pak použijete v další části.

.. varování:
Hodnoty tajného klíče nelze zobrazit, s výjimkou okamžiku jeho vytvoření. Ujistěte se, že si hodnotu
sekret, když byl vytvořen před opuštěním stránky.

... _outlook_calendar/odoo_setup:

Konfigurace v Odoo
=====================

V databázi Odoo přejděte na: „Kalendářová aplikace -> Konfigurace -> Nastavení“ a zaškrtněte
zaškrtávací políčko vedle nastavení „Kalendář Outlook“. Pamatujte, že klikněte na „Uložit“
zavést změny.

.. obrázek: outlook/outlook-calendar-setting.png
:alt:Nastavení „Outlook Calendar“ v Odoo.

V portálu Microsoftu Azure zkopírujte v sekci „Přehled“ aplikace.
„ID aplikace (klienta)“ a vložte ji do
:guilabel:`ID klienta“ pole v Odoo.

.. obrázek: outlook/client-id.png
:align:center
:alt:„ID klienta“ v portálu Microsoft Azure.

Zkopírujte již získané hodnoty „:guilabel:Value“ (Client Secret Value) a vložte je do
:guilabel:`Tajné heslo klienta“ v Odoo.

.. obrázek: outlook/client-secret-value.png
:align:center
:alt: Token „Client Secret“ k zkopírování ze systému Microsoft do Odoo.

V poslední fázi přejděte na stránku „Nastavení“ v menu „Odoo“ a klikněte na tlačítko „Uložit“.

..._outlook/sync:

Synchronizace s Outlookem
=================

.. varování:

Odoo doporučuje, aby se synchronizace kalendáře Outlooku testovala na testovací databázi a
před pokusem o synchronizaci ověřit e-mailovou adresu (která není používána pro žádné jiné účely).
požadovaný kalendář Outlooku s databází uživatele.

Pokud uživatel má v kalendáři Odoo nějaké minulé, současné nebo budoucí události před synchronizací
Kalendář v aplikaci Outlook bude při synchronizaci považovat události převedené z kalendáře Odoo za
nové události, které vyvolají odeslání e-mailové notifikace z aplikace Outlook všem účastníkům akce.

aby se e-maily neposílaly všem účastníkům minulých, současných i budoucích akcí.
musí přidat události z kalendáře Odoo do kalendáře Outlook před prvním nesouladem.
odstranit události z Odoo a poté spustit synchronizaci.

I po synchronizaci kalendáře Odoo s kalendářem Outlook se vám stále může dostat e-mail.
oznámení všem účastníkům události při každé editaci (vytvoření, smazání) události
nearchivovány (nebo datum nebo čas změněn) bez výjimky. To je omezení, které nelze obejít.
vyřešeny z naší strany.

Ve zkratce, jakmile uživatel synchronizuje svůj kalendář v aplikaci Outlook s kalendářem Odoo:

   - Vytvoření události v Odoo způsobí, že Outlook pošle pozvánku všem účastníkům akce.
   - Smazání události v Odoo způsobí, že Outlook pošle všem účastníkům zrušení.
   - Při obnovení události v Odoo vyzve Outlook všechny účastníky k potvrzení jejich účasti.
   - Ukládání události do Odoo způsobí, že Outlook pošle všem účastníkům zrušení.
   - Přidání kontaktu do události způsobí, že Outlook pošle pozvánku všem účastníkům akce.
   - Odstranění kontaktu z události způsobí, že Outlook pošle všem účastníkům události oznámení o zrušení.

Synchronizujte kalendář Odoo a Outlook
------------------------------

V databázi Odoo otevřete modul Kalendář a klikněte na tlačítko „Synchronizace s Outlookem“.
vpravo na stránce pod měsíčním kalendářem.

.. obrázek: outlook/outlook-sync-button.png
:align:center
:alt:Tlačítko pro synchronizaci s aplikací Outlook v kalendáři Odoo.

Synchronizace je dvoustranný proces, což znamená, že události jsou v obou účtech sladěny.
(*Outlook* a Odoo). Stránka přesměruje na stránku přihlášení Microsoftu a uživatel je požádán o přihlášení
pokud ještě nejsou přihlášené. Nakonec klikněte na
:guilabel:`Přijmout“.

.. obrázek: outlook/accept-terms.png
:align:center
:alt:Autorizační proces na stránce Microsoft Outlook OAuth.

.. poznámka::
Všichni uživatelé, kteří chtějí používat synchronizaci, jednoduše musí:
Outlook <outlook/sync>. Konfigurace účtu Microsoftu Azure se provádí jen jednou, a to
Microsoft *ID Entra* uživatelů klientských identifikátorů a tajemství je jedinečné a pomáhá uživateli spravovat
konkrétní případ služeb cloudu společnosti Microsoft pro vnitřní i externí uživatele.

.. viz též:
   - :doc:`../../obecne/integracie/emailove-pluginy/outlook`
   - :doc:`google`

Zjišťování problémů s synchronizací
=================

Může dojít k situaci, kdy účet Microsoft Outlook Calendar nebude synchronizován s Odoo správně.
Problémy s synchronizací lze vidět v databázových logech.

V těchto případech je potřeba účet vyřešit. Reset může být proveden pomocí
Tlačítko „Obnovit účet“, které lze přistupovat kliknutím na nabídku „Nastavení
aplikace --> Správa uživatelů. Pak vyberte uživatele, jehož kalendář chcete upravit a klikněte na
:guilabel:`Kalendář“ záložka.

.. obrázek: outlook/outlook-reset.png
:align:center
:alt:Zvýrazněné tlačítko resetu v kalendáři uživatele.

Dále klikněte na tlačítko „Znovu nastavit účet“ pod správným kalendářem.

Obnovení nastavení
-------------

Pro řešení problémů s synchronizací kalendáře Microsoft Outlook jsou k dispozici následující možnosti obnovení nastavení:
Odoo:

.. obrázek: reset-calendar.png
:align:center
:alt: Možnosti obnovení kalendáře v Odoo.

:guilabel:`Uživatelské stávající události“:

 - :guilabel:Nechat vše beze změn“: žádné změny událostí.
 - :guilabel:`Smazat z aktuálního kalendáře Microsoft“: smažte události ze *Microsoft
Kalendář v aplikaci Outlook*.
 - :guilabel:`Smazat z Odoo“: smažte události ze schránky Odoo.
 - :guilabel:`Smazat z obou“: smažte události ze všech kalendářů Microsoft Outlook a Odoo
kalendář.

:guilabel:`Další synchronizace“:

 - :guilabel:`Synchronizovat pouze nové události“: synchronizovat nové události v kalendáři Microsoft Outlook a/nebo
Kalendář Odoo.
 - :guilabel:`Synchronizovat všechny existující události“: synchronizovat všechny události v kalendáři Microsoft Outlook
a/nebo kalendářem Odoo.

Po výběru možnosti klikněte na tlačítko „Potvrdit“ a poté upravte události uživatele a kalendář.
synchronizace.

