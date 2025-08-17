=======================================================
Připojte Microsoft Office 365 k Odoo pomocí Azure OAuth
=======================================================

Odoo je kompatibilní s Microsoft Azure OAuth pro Microsoft 365. Pro odesílání a přijímání
Zabezpečené e-maily z vlastní domény lze nastavit během několika minut.
Azure platformě a na zadní straně databáze Odoo. Tato konfigurace funguje s buď
osobní e-mailová adresa nebo adresa vytvořená na základě vlastního doménového jména.

.. viz též:
„Microsoft Learn: Registrace aplikace v Microsoft Identity Platform
<https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app>`_

.. viz též:
   - :doc:`/aplikace/obecné/uživatelé/azure`
   - :doc:`/aplikace/produktivita/kalendář/outlook`

Nastavení v portálu Microsoft Azure
===============================

Vytvořte novou aplikaci
------------------------

Chcete-li začít, přejděte na portál Microsoftu Azure (https://portal.azure.com/). Přihlásit se můžete
:guilabel:`Microsoft Outlook Office 365“ účet, pokud existuje, jinak se přihlaste pomocí
osobní:účet Microsoft. Uživatel s administrátorskými právy k nastavení Azure
musíte se připojit a provést následující konfiguraci. Poté přejděte do části
označené jako „Spravovat identitu Microsoft Entra“ (dříve Azure Active Directory).

Nyní klikněte na tlačítko „Přidat (+)“ v horním menu a poté vyberte „Aplikace“.
registrace“. Na obrazovce „Registrovat aplikaci“ přejmenujte :guilabel:„Název“ na
„Odoo“ nebo něco rozpoznatelného. V sekci „Podporované typy účtů“ vyberte
:guilabel:`Účty v jakémkoliv organizačním adresáři (Ve kterémkoliv adresáři Microsoft Entra ID - Multitenant)
a osobní účty společnosti Microsoft (např. Skype, Xbox).

V sekci „Přesměrování URL“ vyberte „Web“ jako platformu a pak zadejte
„https://<web base url>/microsoft_outlook/confirm“ do pole „URL“. Hodnota proměnné
závisí na použitém URL pro přihlášení do databáze.

.. poznámka::
Dokumentace o :ref:`webové adrese základní úrovně <domain-name/web-base-url>` vysvětluje, jak zmrazit
je také možné přidat různé odkazové adresy na aplikaci Microsoft.

Po přidání URL do pole se aplikace zaregistruje a vytvoří se.

Povolení API
---------------

Dalším krokem je nastavení oprávnění pro API. Odoo bude potřebovat konkrétní oprávnění API, aby mohlo
schopnost číst (IMAP) a odesílat (SMTP) e-maily v nastavení Microsoftu 365. Nejprve klikněte na
:guilabel:`Povolení API“ odkaz, který se nachází v levém menu. Poté klikněte na „(+).
Přidejte tlačítko „Dovolit“ a vyberte Microsoft Graph pod „Často používané“.
Microsoft API“. Poté vyberte možnost „Přidělená oprávnění“.

Vyhledejte následující: guilabel: Delegované oprávnění a klikněte
Přidejte oprávnění pro každé z nich:

- :guilabel:`SMTP.Send“
- :guilabel:`IMAP.AccessAsUser.Všechny“

.. poznámka::
Povolení `User.Read` bude přidáno automaticky.

.. obrázek:: azure_oauth/permissions.png
:align:center
:alt:Povolení pro integraci Odoo se nachází pod Microsoft Graph.

Přiřaďte uživatele a skupiny
=======================

Po přidání oprávnění API se vraťte na stránku „Přehled“.
:guilabel:`Aplikace“ v horní části levého sloupce nabídek.

Nyní přidejte uživatele do této aplikace. V seznamu „Základní“ pod nadpisem
odkaz označený:guilabel:`Správa aplikace v místním adresáři“ nebo poslední možnost na spodku
pravé straně stolu.

.. obrázek:: azure_oauth/managed-application.png
:align:center
:alt:Přidejte uživatele a skupiny kliknutím na odkaz „Správa aplikace v místním adresáři“ pro
vytvořil aplikaci.

V levém sloupci vyberte položku „Uživatelé a skupiny“. Poté klikněte na „(+) Přidat
Uživatel/Skupina. Podle účtu buď skupina nebo uživatel
přidána nebo jen :guilabel:`Uživatelé“. Soukromé účty umožní pouze přístup pro :guilabel:`Uživatele“
přidán.

V seznamu uživatelů nebo skupin klikněte na „Žádný zvolený“ a přidejte uživatele
nebo skupina uživatelů, kteří budou odesílat e-maily z účtu Microsoft v Odoo.
Přidejte uživatele/skupiny, klikněte na „Vybrat“ a poté na „Přiřadit“.
aplikace.

Vytvořte přihlašovací údaje
------------------

Nyní je potřeba vytvořit přihlašovací údaje pro instalaci Odoo.
Mezi ně patří např. „ID klienta“ a „tajný klíč“.
Klientské ID lze zkopírovat na stránce „Přehled“ aplikace.
V poli „Klientské ID“ nebo „ID aplikace“ je uvedeno pod „Název zobrazení“.
v přehledu aplikace „Základní funkce“.

.. obrázek:: azure_oauth/application-id.png
:align:center
:alt:ID aplikace/klienta se nachází v přehledu aplikace.

Dále je potřeba získat hodnotu tajného klíče klienta. K tomuto účelu je nutno kliknout na
V levém sloupci zvolte „Soubory certifikátů a tajné klíče“ a poté vyberte „Tajný klíč klienta“.
musí být vytvořen. Chcete-li to provést, klikněte na tlačítko „(+). Nový klíč klienta“.

V pravém okně se objeví tlačítko s názvem „Přidat klientské tajné“. Pod
:guilabel:`Popis`, zadejte „Odoo Fetchmail“ nebo něco rozpoznatelného a pak nastavte
:guilabel:`datum vypršení platnosti“.

.. důležité::
Pokud je třeba vytvořit nový kód, musí být vygenerován a nakonfigurován.
vyprší. V takovém případě může dojít k přerušení služby, a proto by měl být datum vypršení
a posunout na nejvzdálenější možný termín.

Poté klikněte na tlačítko „Přidat“, když jsou tyto dvě hodnoty zadány. Pak se objeví pole pro „Hodnota tajného klíče“.
a vytvoří se „Tajné ID“. Je důležité zkopírovat hodnotu „Hodnoty“ nebo
:guilabel:`Hodnota tajného klíče“ do poznámkového bloku, protože se za chvíli stane šifrovanou.
Klíčová značka „Tajné ID“ není potřebná.

.. obrázek:: azure_oauth/secretvalue.png
:align:center
:alt: Hodnota tajného klientského klíče nebo hodnota v přihlašovacích údajích aplikace.

Po provedení těchto kroků by měly být následující položky připraveny k nastavení v Odoo:

- ID klienta (případně ID aplikace)
- Tajný klíč klienta (:guilabel:`Hodnota“ nebo „Tajný klíč klienta“)

Toto dokončuje nastavení na straně portálu Microsoft Azure.

Nastavení v Odoo
=============

Zadejte přihlašovací údaje do aplikace Microsoft Outlook
-----------------------------------

Nejprve otevřete databázi Odoo a přejděte do modulu :guilabel:`Aplikace`. Pak odstraňte
Vyhledejte v nabídce aplikací a zadejte „Outlook“. Poté nainstalujte modul
přezdívka: „Microsoft Outlook“.

Poté přejděte na „Nastavení -> Obecné nastavení“ a pod položkou „Diskuse“
sekci, zkontrolujte, jestli je zaškrtnutá políčka pro :guilabel:`Vlastní e-mailové servery`. To obsadí
nová možnost v poli „Kredence Outlooku“.

Uložte svůj pokrok.

Poté zkopírujte a vložte :guilabel:`ID klienta“ (Aplikační ID) a :guilabel:`Tajný klíč
(Hodnota tajného klíče) do příslušných polí a poté stiskněte tlačítko „Uložit“.

.. obrázek: azure_oauth/outlookcreds.png
:align:center
:alt:Kreditní údaje v obecných nastaveních Odoo.

Nastavit odchozí e-mailový server
-------------------------------

Na stránce „Obecné nastavení“ pod položkou „Vlastní e-mailové servery“
Klikněte na odkaz „Výchozí servery pro odesílání e-mailů“ a nakonfigurujte svůj účet Microsoft.

Poté vytvořte nový e-mailový server a zaškrtněte políčko „Outlook“. Následně vyplňte
:guilabel:`Jméno“ (může být cokoli) a e-mailový účet Microsoftu :guilabel:`Uživatelské jméno“.

Pokud pole „Od filtru“ je prázdné, zadejte buď doménu nebo e-mailovou adresu.
<email-outbound-unique-address>.

Poté klikněte na „Připojit svůj účet Outlook“.

Otevře se nové okno od společnosti Microsoft, ve kterém je třeba dokončit autorizační proces. Vyberte
vhodné e-mailové adresy, které se konfigurují v Odoo.

.. obrázek:: azure_oauth/verify-outlook.png
:align:center
:alt:Stránka s povolením přístupu mezi nově vytvořenou aplikací a Odoo.

Poté přepněte na „Ano“ a potvrďte.
stránka se vrátí zpět do nově nakonfigurovaného pole „Výchozí poštovní server“ v Odoo.
konfigurace automaticky načítá token v Odoo a štítek s
Ve zprávě se objeví zelené „Outlook Token Valid“.

.. obrázek:: azure_oauth/outlook-token.png
:align:center
:alt: Indikátor platného tokenu pro aplikaci Microsoft Outlook.

Konečně klikněte na tlačítko „Ověřit připojení“ a potvrzení by mělo být zobrazeno.
nyní mohou bezpečně a bezpečně odesílat e-maily prostřednictvím aplikace Microsoft Outlook s ověřením OAuth.

... _azure_oauth/notifikace:

Konfigurace s jedním odchozím poštovním servery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Konfigurace jediného výstupního serveru je nejjednodušší konfigurací, která je dostupná pro Microsoft Azure
a nevyžaduje rozsáhlé přístupové práva uživatelů v databázi.

Obecná e-mailová adresa by se používala k odesílání e-mailů všem uživatelům v databázi. Například
Může být strukturováno s „upozorněními“ (aliasem „upozornění@příklad.cz“) nebo „kontaktem“ (aliasem „kontakt@příklad.cz“).
(např. „contact@example.com“). Tuto adresu je nutné nastavit jako filtr pro odesílatele na serveru.
Toto adresní pole musí také odpovídat klíčové kombinaci {mail.default.from}@{mail.catchall.domain}.
parametry systému.

.. viz též:
Navštivte stránku s návodem k použití filtru v e-mailovém odesílání.
informace.

.. poznámka::
Systémové parametry lze zobrazit aktivací režimu vývojáře v
:menu: „Nastavení“ --> „Technické“ --> „Parametry“ --> „Systémové parametry“.

Při použití této konfigurace bude každá odeslaná e-mailová zpráva obsahovat adresu
konfigurovanou schránku „upozornění“. Je však třeba poznamenat, že jméno odesílatele
jejich e-mailová adresa se změní:

.. obrázek: azure_oauth/from-name-remain.png
:align:center
:alt:Jméno odesílatele z reálného e-mailu.

.. příklad::
Konfigurace jediného odchozího poštovního serveru:

   - Server pro odchozí poštu **username** (přihlašovací jméno) = `notifications@example.com`
   - Server odchozí pošty: guilabel:FROM Filtering = notifications@example.com
   - Parametr systému „mail.catchall.domain“ je nastaven na „example.com“.
   - V systémových parametrech je nastaveno „mail.default.from“ na hodnotu „notifications“.

Uživatelsky specifická (více uživatelů) konfigurace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kromě univerzálního e-mailového serveru lze pro uživatele nastavit i individuální e-mailový server.
databáze. Tyto e-mailové adresy musí být nastaveny jako filtr „Odesílatel“ na každé jednotlivé
server pro tuto konfiguraci fungovat.

Tato konfigurace je ze dvou možných konfigurací Microsoftu Azure tím obtížnějším.
vyžaduje, aby všichni uživatelé s nastavenými e-mailovými servery měli přístup k nastavení.
spojení s e-mailovým serverem.

Nastavení
*****

Každý uživatel by měl mít vlastní e-mailový server nastavený. Filtr „Odesílatel“ by měl být nastaven na
Aby se z daného serveru odesílal pouze e-mail uživatele. V jiných slovy, aby byl odeslán pouze e-mail
adresa, která odpovídá sadě guilabel: FROM Filtering, může používat tento server.

.. viz též:
Navštivte stránku s návodem k použití filtru v e-mailovém odesílání.
informace.

Musí být nastaven záložní server, který umožňuje odesílání
:guilabel:`upozornění“. Filtr „Od“ pro tento server by měl mít hodnotu
`{mail.default.from}@{mail.catchall.domain}`

.. poznámka::
Systémové parametry lze zobrazit aktivací režimu vývojáře v
:menu: „Nastavení“ --> „Technické“ --> „Parametry“ --> „Systémové parametry“.

.. důležité::
Konfigurace pro tento transakční e-mailový server může fungovat vedle odchozího masového mailingu.
e-mailový server. Filtr „Od“ pro masovou poštu může zůstat prázdný.
Ale je třeba ji přidat do nastavení aplikace Email Marketing.

......viz také::
Pro více informací o nastavení poštovního serveru pro masovou poštu navštivte
:ref:`e-mailová adresa vlastní domény - SMTP server`.

.. příklad::
Konfigurace víceúčelového SMTP serveru pro odchozí poštu:

   - Uživatelská schránka číslo 1
      - Server pro odchozí poštu #1 **username** (přihlašovací jméno) = `john@example.com`
      - Server odchozí pošty číslo 1: guilabel:FROM Filtering = john@example.com
   - Uživatel #2 - schránka
      - Server pro odchozí poštu číslo 2 **username** (přihlašovací jméno) = „jane@example.com“
      - Server pro odchozí poštu #2: guilabel:FROM Filtering = jane@example.com
   - Poštovní schránka pro oznámení
      - Server pro odchozí poštu číslo 3 **username** (přihlašovací jméno) = `notifications@example.com`
      - Server pro odchozí poštu #3: guilabel:FROM Filtering = notifications@example.com
   - Parametry systému
      - Parametr systému „mail.catchall.domain“ je nastaven na „example.com“.
      - V systémových parametrech je nastaveno „mail.default.from“ na hodnotu „notifications“.

Nastavení příchozího e-mailového serveru
-------------------------------

Příchozí e-mailový účet by měl být konfigurován podobně jako odchozí e-mailový účet.
do položky „Příchozí poštovní servery“ v menu „Technické nastavení“ a „Vytvořit“.
nová konfigurace. Zkontrolujte nebo vyberte tlačítko vedle položky:guilabel:"OAuth autentizace Outlooku"
zadejte uživatelské jméno Microsoftu Outlook. Klikněte na tlačítko „Připojit svůj účet Microsoft
účet. Odoo uvede: „Token Outlook valid“ a nyní „Ověřit a potvrdit“.
účet, který je připravený na příjem e-mailů do databáze Odoo.
