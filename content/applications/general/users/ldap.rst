===================
Autentizace pomocí LDAP
===================

Pro konfiguraci autentizace pomocí protokolu LDAP (Lightweight Directory Access Protocol):

#Otevřete aplikaci Nastavení, posuňte se dolů do části „Souhrn“ a zapněte
:guilabel:`Přihlášení přes LDAP“.
#Klikněte na tlačítko „Uložit“ a poté se vraťte do sekce „Spojení“ a klikněte
:guilabel:`LDAP server“.
#V seznamu „Nastavení serveru LDAP“ klikněte na „Nový“, vyberte požadovanou možnost a poté stiskněte tlačítko „OK“.
společnost ve výběrovém seznamu.
#V sekci „Informace o serveru“ zadejte IP adresu a port serveru.
:guilabel:`adresa LDAP serveru“ a „port LDAP serveru“, v příslušném pořadí.
#.Zapněte možnost „Používat TLS“ a požádejte o zabezpečené šifrování SSL/TLS při připojování k LDAP
server, pokud je na něm povolen protokol StartTLS.
#V sekci „Přihlášení“ zadejte ID a heslo účtu použitého k
serveru v polích :guilabel:`LDAP binddn` a :guilabel:`LDAP password`,
respektive. Pokud pole necháte prázdná, server bude provádět dotaz na anonymní bázi.
#V sekci „Parametr procesu“ zadejte:

   - jméno LDAP serveru v poli :guilabel:`LDAP základna“ s formátem LDAP
(např. „dc=example,dc=com“);
   - „uid=“ v poli filtru LDAP.

#V sekci „Informace o uživateli“ v části „Nastavení účtu“:

   - Zapněte možnost „Vytvořit uživatele“ při prvním přihlášení, aby se vytvořila uživatelská profilová stránka v Odoo
pomocí LDAP.
   - Vyberte šablonu uživatele, která má být použita pro vytvoření nových profilů uživatelů. Pokud žádná šablona
Pokud je vybrán administrátorský profil, použije se profil správce.

.. poznámka::
Při použití služby Microsoft Active Directory (AD) pro ověřování pomocí protokolu LDAP se uživatelé mohou setkat s problémem přihlášení
i přes použití platných přihlašovacích údajů vytvořit nový parametr systému k deaktivaci sledování odkazů
v klientu LDAP:

    #:ref:`Zapněte vývojářský režim. <developer-mode>“
    #Přejděte do sekce „Nastavení“ – „Technické“ – „Systémové parametry“ a klikněte
:label:`Nový`.
    #Vyplňte pole:

       - :guilabel:`Klíč“: „auth_ldap.disable_chase_ref“
       - :label:Hodnota: „Pravda“
