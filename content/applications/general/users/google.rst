=============================
Google Sign-In Authentication
=============================

Funkce „Přihlášení pomocí Google“ je užitečná funkce, která umožňuje uživatelům Odoo přihlásit se do svého účtu.
databáze s jejich účtem na Googlu.

Je to zvláště užitečné v případě organizace používající službu Google Workspace a zaměstnanců pracujících
organizaci připojit k Odoo pomocí jejich účtu na Googlu.

.. varování:
Databáze hostované na Odoo.com by neměly používat přihlášení pomocí Oauth pro vlastníka nebo administrátora databáze.
databáze, protože by se tak odpojila databáze od jejich účtu na Odoo.com. Pokud je Oauth nastavený pro
uživatel, databáze již nebude možné kopírovat, přejmenovávat nebo jinak spravovat.
portál Odoo.com.

.. viz též:
   - :doc:`/aplikace/produktivita/kalendář/google`
   - :doc:`../email_communication/google_oauth`

... _google_sign_in/konfigurace:

Konfigurace
=============

Propojení funkce přihlášení přes Google vyžaduje konfiguraci jak na Googlu, tak i v Odoo.

.. _google_sign_in/api:

Dashboard pro aplikace Googlu
--------------------

#Přejděte na Google API Dashboard <https://console.developers.google.com/>.
#Zkontrolujte, že je otevřen správný projekt. Pokud projekt zatím neexistuje, klikněte na tlačítko „Vytvořit
Projekt“, vyplňte název projektu a další podrobnosti o společnosti a klikněte na
:guilabel:`Vytvořit“.

.... obrázek: google/nový-detail-projektu.png
:align:center
:alt:Dokončování podrobností nového projektu.

.......
Vyberte název společnosti z roletky.

.. _google-sign-in/oauth:

OAuth souhlas s obrazovkou
~~~~~~~~~~~~~~~~~~~~

#V levém postranním menu klikněte na položku:menuselection:„Souhlas s OAuth“.

.. obrázek:: google/consent-selection.png
:align:center
:alt: Rozbalovací nabídka pro výběr souhlasu s Google OAuth.

#Zvolte jednu z možností (Vnitřní/Vnější) a klikněte na
:guilabel:`Vytvořit“.

.. obrázek:: google/consent.png
:align:center
:alt: Výběr uživatelského typu v souhlasu s OAuth.

.. varování::
*Osobní* účty Gmailu mohou být pouze typem uživatele **Externího**, což znamená, že Google
může vyžadovat schválení nebo přidání rozsahu. Použitím služby Google Workspace však
účet umožňuje používat uživatelský typ **Interní**.

Dále je třeba poznamenat, že během testování režimu *Externí* není možné spojit se s API.
je nutné získat schválení od Googlu. V tomto testovacím režimu je omezen počet uživatelů na 100.

#Vyplňte požadované informace a údaje o doméně, pak klikněte na tlačítko „Uložit a pokračovat“.
#Na stránce „Zaměření“ nechte všechna pole beze změny a klikněte na „Uložit a
Pokračujte.“
#Poté pokračujte v testovacím režimu (*Externí*) a přidejte e-mailové adresy, které jsou konfigurovány.
krok „Zkušební uživatelé“ kliknutím na „Přidat uživatele“ a potom
:tlačítko „Uložit a pokračovat“. Zobrazí se shrnutí registrace aplikace.
#Nakonec se posuňte dolů a klikněte na „Přejít zpět na domovskou stránku“.

..._google-sign-in/credentials:

Kvalifikace
~~~~~~~~~~~

#V levém postranním menu klikněte na:menuselection:`Přihlašovací údaje`.

.... obrázek:: google/credentials-button.png
:align:center
:alt:Tlačítko pro zobrazení nabídky kreditů.

#Klikněte na „Vytvořit přihlašovací údaje“ a vyberte možnost „ID klienta OAuth“.

.. obrázek: google/client-id.png
:align:center
:alt: Výběr klientského ID OAuth.

#Vyberte „Webová aplikace“ jako typ aplikace. Nyní konfigurujte
stránky, na které bude Odoo přesměrován.

Pro dosažení tohoto cíle je třeba v poli „Povolené přesměrovací adresy“ zadat databázi.
doménu, která je následována /auth_oauth/signin. Například:
„https://můj-doménní-název.odoo.com/auth_oauth/signin“ a pak klikněte na „Vytvořit“.

#Nyní se zobrazí obrazovka s kódem aplikace.
a zkopírujte si „ID klienta“ pro pozdější použití, protože bude potřeba
pro konfiguraci v Odoo, která bude pokryta v následujících krocích.

..._google-sign-in/auth-odoo:

Google Authenticator v Odoo
-----------------------------

..._google-sign-in/client-id:

Získat klientské ID
~~~~~~~~~~~~~~~~~~~~~~

Jakmile jsou předchozí kroky dokončeny, na portálu Google API Dashboard se vytvoří dvě klíče:
:guilabel:`ID klienta“ a „Tajný klíč“. Zkopírujte si :guilabel:„ID klienta“.

.. obrázek: google/secret-ids.png
:align:center
:alt:Google OAuth klientské ID vytvořeno.

... _google-sign-in/odoo-activation:

Aktivace Odoo
~~~~~~~~~~~~~~~

#Přejděte do sekce „Obecné nastavení“ a aktivujte možnost „OAuth“.
„Přihlášení“.

.. poznámka::
Odoo může po této fázi uživatele vyzvat k přihlášení znovu.

#Zpět na „Obecné nastavení > Integrace > Autentizace pomocí OAuth“ a aktivujte
Vyberte a uložte. Následně se vraťte do nastavení „Obecné“.
Integration-->Google Authenticator a aktivujte výběr. Pak vyplňte
:guilabel:`ID klienta“ s klíčem z rozhraní Google API Dashboard a :guilabel:`Uložit“.

.. obrázek:: google/odoo-client-id.png
:align:center
:alt:Vyplnění klientského ID v nastavení Odoo.

.. poznámka::
Konfigurace služby Google OAuth2 lze také získat kliknutím na tlačítko :guilabel:`OAuth Provider`
pod nadpisem „Autentizace pomocí OAuth“ v sekci „Propojení“.

..._google-sign-in/login:

Přihlášení do Odoo přes Google
==========================

Pro propojení účtu Google s profilem Odoo klikněte na tlačítko „Přihlásit se pomocí Google“ při prvním přihlášení.
přihlášení do Odoo.

.... obrázek: google/první přihlášení.png
:align:center
:alt:Odhlášení s tlačítkem „Přihlásit se pomocí Google“.


Stávající uživatelé musí :ref:`změnit svůj heslo <users/reset-password>`, aby se mohli dostat k
:menuselection:'Zapomenuté heslo' stránce, zatímco noví uživatelé mohou rovnou kliknout na: 'Přihlásit se
Google, místo zvolení nového hesla.

.. viz též:
   - „Pomocí Google Cloud Platform Console – nastavení OAuth 2.0
<https://support.google.com/cloud/answer/6158849>
