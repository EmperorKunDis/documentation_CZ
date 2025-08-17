======================================
Přihlášení do služby Microsoft Azure
======================================

Funkce přihlášení pomocí Microsoft Azure OAuth je užitečná funkce, která umožňuje uživatelům Odoo přihlašovat se
do jejich databáze pomocí svého účtu Microsoft Azure.

Toto je zvláště užitečné v případě, že organizace používá prostředí Azure Workspace a chce, aby zaměstnanci
organizaci, která se připojí k Odoo pomocí svých účtů Microsoft.

.. varování:
Databáze hostované na Odoo.com by neměly používat přihlášení pomocí OAuth pro vlastníka nebo správce
databáze, protože by se tak odpojila databáze od jejich účtu na Odoo.com. Pokud je pro tento
uživatel, databáze již nebude možné kopírovat, přejmenovávat nebo jinak spravovat.
portál Odoo.com.

.. viz též:
   - :doc:`../../produktivita/kalendar/outlook`
   - :doc:`../email_communication/azure_oauth`

Konfigurace
=============

Přidání funkce přihlášení přes Microsoft vyžaduje konfiguraci na straně Microsoftu a Odoo.

Odoo Systémové parametry
---------------------

Nejprve aktivujte režim vývojáře (:ref:`vývojářský režim <developer-mode>`), a pak přejděte do nastavení
--> Technické --> Systémové parametry`.

Klikněte na tlačítko „Vytvořit“ a v novém prázdném formuláři přidejte následující systémový parametr
„auth_oauth.authorization_header“ do pole „Klíč“ a nastavte hodnotu na
„1“. Pak klikněte na „Uložit“ a dokončete.

Dashboard Microsoftu Azure
-------------------------

Vytvořte novou aplikaci
~~~~~~~~~~~~~~~~~~~~~~~~

Nyní je čas nastavit parametry systému v Odoo.
aplikace v rámci Microsoftu Azure. Chcete-li začít s novou aplikací, přejděte na
„Portál Microsoftu Azure“ (https://portal.azure.com/). Přihlášení pomocí:
Pokud máte účet Microsoft 365, přihlaste se pomocí něj. Pokud ne, přihlaste se pomocí osobního účtu Microsoft
účet“.

.. důležité::
Uživatel s administrátorskými právy k nastavení Azure musí být připojen a provést následující
konfiguračních kroků níže.

Nyní přejděte do sekce s názvem „Správa Microsoft Entra ID“ (původně Azure Active Directory).
Pokud je tento odkaz na stránce obvykle uprostřed.

Nyní klikněte na ikonu „Přidat (+)“ v horním menu a poté vyberte „Aplikace“.
registrace“ z nabídky. Na obrazovce „Registrovat aplikaci“ přejmenujte
Zadejte do pole „Název“ hodnotu „Odoo Login OAuth“ nebo podobný název.
V sekci „Podporované typy účtů“ vyberte možnost „Účty v této organizaci“.
pouze adresář organizace (adresář organizace pouze pro jednu instanci).

.. varování:
Podporované typy účtů se mohou lišit podle typu účtu Microsoft a koncového použití.
OAuth. Například: Je přihlašování určeno pro uživatele v rámci jedné organizace nebo je určeno
pro přístup do zákaznického portálu? Výše uvedená konfigurace se používá pro interní uživatele v
organizace.

Vyberte:guilabel:Pouze osobní účty Microsoftu, pokud je cílová skupina určená pro portál
uživatelé. Vyberte: guilabel:„Pouze účty v této organizační složce (pouze výchozí adresář)
„Jediný nájemce“ pokud je cílovou skupinou uživatelé firem.

V sekci „Přesměrování URL“ vyberte „Web“ jako platformu a pak zadejte
„https://<odoo base url>/auth_oauth/signin“ do pole „URL“. Základní adresa URL Odoo:
(adresa zdroje) je kanonická doména, na které se může váš instanci Odoo dostat (např.
V poli „URL“ zadejte adresu mydatabase.odoo.com (pokud je váš web hostovaný na odoo.com). Pak klikněte
:guilabel:„Registrace“ a aplikace je vytvořena.

Autorizace
~~~~~~~~~~~~~~

Upravte novou aplikaci kliknutím na položku „Autorizace“ v nabídce
levé menu po přesměrování na nastavení aplikace z předchozího kroku.

Dále se vybere typ tokenů potřebných pro ověření pomocí OAuth. Tyto nejsou
měnové tokeny, ale spíše autentizační tokeny, které jsou předávány mezi Microsoftem a Odoo.
Proto tedy za tyto tokeny neplatíte, používají se jen k ověření identity
mezi dvěma :abbr:`API (Application Programming Interface)“. Vyberte tokeny, které mají být
vydané autorizačním koncovým bodem, pokud se na obrazovce posunete dolů a zaškrtnete políčka označená jako
„Přístupové tokeny (používané pro implicitní toky)“ a „Token ID (používaný pro implicitní a
hybridní proudy.

.. obrázek:: azure/authentication-tokens.png
:align:center
:alt:Nastavení autentizace a tokeny koncových bodů.

Klikněte na tlačítko „Uložit“ a ujistěte se, že jsou tyto nastavení uloženy.

Sbírejte kredity
~~~~~~~~~~~~~~~~~~

S aplikací vytvořenou a ověřenou na portálu Microsoft Azure budou kredence
seřazeny pod sebou. Chcete-li tak učinit, klikněte na položku „Přehled“ v levém sloupci.
a zkopírujte hodnotu pole „ID aplikace (klienta)“ v okně, které se objeví. Vložte tento kredit
na poznámkový blok/poznámkový blok, protože tento přístupový kód bude použit v konfiguraci Odoo později.

Po dokončení této části klikněte na položku „Konektory“ v horním menu a pak klepněte na ikonu kopírování.
vedle pole „OAuth 2.0 autorizační bod (v2)“. Vložte tento výraz do schránky
poznámkový blok.

.. obrázek:: azure/overview-azure-app.png
:align:center
:alt:Kredence aplikace a autorizačního bodu OAuth 2.0 (verze 2).

Nastavení Odoo
----------

Posledním krokem při konfiguraci služby Microsoft Azure OAuth je nakonfigurovat některé nastavení v
Odoo. Přejděte na: menu: „Nastavení“ -> „Propojení“ -> „OAuth autentizace“ a zkontrolujte
zatrhněte políčko pro aktivaci funkce přihlášení pomocí OAuth a klikněte na tlačítko „Uložit“, aby se změny uložily.
Pak se přihlaste do databáze poté, co se načte obrazovka přihlášení.

Znovu se přesuňte na: „Nastavení -> Propojení -> Autentizace pomocí OAuth“
Klikněte na „OAuth Provider“. V horním levém rohu vyberte „New“ a pojmenujte
poskytovatel Azure.

Vložte do pole „ID aplikace (klienta)“ z předchozí sekce.
ID pole. Po dokončení vložte nový :guilabel:`OAuth 2.0 autorizační bod (v2)`
hodnotu do pole „URL autorizace“.

Do pole „URL uživatele“ vložte následující :abbr:`URL (Uniform Resource Locator)“:
„https://graph.microsoft.com/oidc/userinfo“

Do pole „Předmět“ vložte následující hodnotu: openid profile email. Následně otevřete
logo lze použít jako třídu CSS na obrazovce přihlášení zadáním následující hodnoty:
fa-okna, v poli CSS třída.

Zaškrtněte políčko vedle pole :guilabel:`Povoleno`, abyste mohli použít poskytovatele OAuth. Nakonec přidejte
„Microsoft Azure“ do pole „Text tlačítka přihlášení“. Tento text se objeví vedle
Logo Windows na stránce přihlášení.

.. obrázek: azure/odoo-provider-settings.png
:align:center
:alt:Nastavení poskytovatele v aplikaci Nastavení.

Uložte změny a dokončete nastavení ověření pomocí OAuth v Odoo.

Uživatelská zkušenost proudí
---------------------

Pro uživatele se přihlásit do systému Odoo prostřednictvím služby Microsoft Azure musí být v nastavení :menuselection:`Odoo
stránku pro obnovení hesla. Toto je jediný způsob, jak může Odoo spojit účet Microsoft Azure a
umožní uživateli přihlásit se.

.. poznámka::
Stávající uživatelé musí:ref:`změnit heslo <users/reset-password>`, aby se dostali k
:menu_selecce:"Stránka pro obnovení hesla v Odoo". Noví uživatelé musí kliknout na odkaz nového uživatele
přijatý e-mailem, pak klikněte na Microsoft Azure. Uživatelé by neměli nastavit novou
heslo.

Pro přihlášení do Odoo poprvé pomocí poskytovatele OAuth Microsoft Azure přejděte na
:menuselection:`Reset hesla Odoo“ (pomocí nového odkazu na pozvánku uživatele). Heslo lze obnovit
Stránka se zobrazí. Pak klikněte na možnost s názvem:guilabel:`Microsoft Azure`. Stránka
přesměrovat na stránku přihlášení společnosti Microsoft.

.. obrázek:: azure/odoo-login.png
:align:center
:alt:Přihlášení do aplikace Microsoft Outlook.

Zadejte e-mailovou adresu Microsoft a klikněte na „Další“. Postupujte podle pokynů, jak podepsat
do účtu. Pokud je zapnutá dvoufaktorová autentizace, pak se vám zobrazí další krok
Může být vyžadována.

.. obrázek: azure/login-next.png
:align:center
:alt:Zadejte přihlašovací údaje Microsoftu.

Poté, co se přihlásíte do účtu, bude vám stránka automaticky přesměrována na stránku s oprávněním, kde
Uživatel bude vyzván k přijetí podmínek, že aplikace Odoo bude mít přístup
informace o Microsoftu.

.. obrázek:: azure/accept-access.png
:align:center
:alt:Přijmout podmínky společnosti Microsoft pro přístup k informacím o účtu.
