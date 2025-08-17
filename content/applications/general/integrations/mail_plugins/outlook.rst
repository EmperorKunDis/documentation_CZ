==============
Plug-in pro aplikaci Outlook
==============

Outlook umožňuje třetím stranám připojit se, aby mohly provádět databázové operace.
e-mailů. Odoo má doplněk pro Outlook, který umožňuje vytvářet příležitosti z e-mailu.
panel.

Konfigurace
=============

Outlook:Plugin pro poštu Mail musí být nakonfigurován jak v Odoo, tak i v Outlooku.

.._mail-plugin/outlook/enable-mail-plugin:

Aktivujte plugin pro e-mail
------------------

Nejprve zapněte funkci „Plugin pro e-mail“ v databázi. Přejděte na: `Nastavení --> Obecné
Nastavení -> Integrace, zapněte „Plug-in Mail“, a poté „Uložit“.

.._mail-plugin/outlook/instalace-pluginu:

Nainstalujte doplněk pro Microsoft Outlook
--------------------------

Stáhněte si následující soubor XML k jeho nahrání
později: „https://stahování.odoocdn.com/plug-iny/outlook/manifest.xml
<http://www.odoocdn.com/plugins/outlook/manifest.xml>.

Dále otevřete schránku na e-maily Outlook a vyberte libovolný e-mail. Po dokončení této operace klikněte na
Tlačítko „Další akce“ v pravém horním rohu a vyberte možnost „Stáhnout doplňky“.

.. obrázek: outlook/more-actions.png
:align:center
:alt: Další tlačítko v Outlooku

.. tip::
Pro lokálně nainstalované verze Microsoftu Outlook přejděte na položku nabídky „Přidat doplňky“
při náhledu (**ne při otevřené zprávě**). Nejprve klikněte na tlačítko :guilabel:...
(zavináč) v pravém horním rohu náhledu zprávy a poté posuňte se dolů a klikněte na
:guilabel:"Přidat doplňky".

Po této akci vyberte záložku „Moje doplňky“ v levém sloupci.

.. obrázek: outlook/my-add-ins.png
:align:center
:alt:Mé doplňky v Outlooku

Pod položkou „Vlastní doplňky“ v dolní části klikněte na „+ Přidat vlastní doplněk“.
poté na:guilabel:„Přidat ze souboru ...“

.. obrázek: outlook/custom-add-ins.png
:align:center
:alt: Vlastní doplňky v Outlooku

Pro další krok připojte soubor „manifest.xml“ stažený výše a stiskněte tlačítko :guilabel:„OK“. Následně
přečtěte si varování a klikněte na „Instalovat“.

.. obrázek: outlook/add-in-warning.png
:align:center
:alt:Varování při instalaci vlastního doplňku v aplikaci Outlook

.._mail-plugin/outlook/connect-database:

Připojte databázi
--------------------

Nyní se Outlook připojí k databázi Odoo. Nejprve otevřete e-mail v poštovní schránce Outlooku.
Klikněte na tlačítko „Další akce“ v pravém horním rohu a vyberte „Odoo pro
Outlook.

.. obrázek: outlook/odoo-for-outlook.png
:align:center
:alt:Tlačítko pro připojení doplňku Odoo pro Outlook

V pravém panelu nyní můžete vidět **Insights o společnosti**. V dolní části klikněte na
:label_guid:`Přihlásit se“.

.. obrázek: panel-login.png
:align:center
:alt:Přihlášení do databáze Odoo

.. poznámka::
Pouze omezený počet požadavků na **Insighty společnosti** (*Zpracování kontaktu*) je k dispozici.
trial databáze. Tato funkce vyžaduje předplacené kredity:ref:`<mail_plugins/pricing>`.

.. tip::
Pokud se po krátké době na panelu nic neobjeví, je možné, že prohlížeč cookies
Nastavení bránilo načítání. Pozor, že tyto nastavení se mění i v případě, když je prohlížeč ve
„Incognito“ režim.

Chybu lze vyřešit tak, že v nastavení prohlížeče povolíte vždy cookies na stránce s pluginem Odoo.

Pro prohlížeč Google Chrome změňte nastavení souborů cookie podle návodu na adrese:
„https://support.google.com/chrome/answer/95647
<https://support.google.com/chrome/answer/95647>
a přidat „stáhnout.odoo.com“ do seznamu „Stránky, které mohou vždy používat soubory cookie“.

Jakmile je tato operace dokončena, musí být znovu otevřen panel Outlook.

Nyní zadejte URL databáze Odoo a klikněte na tlačítko „Přihlásit“.

.. obrázek: outlook/enter-database-url.png
:align:center
:alt:Vložení adresy databáze Odoo

Poté klikněte na tlačítko „Povolit“ a otevřete okno s upozorněním.

.. obrázek: outlook/new-window-warning.png
:align:center
:alt:Varování před novým oknem

Pokud uživatel není přihlášen do databáze, zadejte přihlašovací údaje. Klikněte na tlačítko „Povolit“
Plug-in Outlook se připojí k databázi.

.. obrázek: outlook/odoo-permission.png
:align:center
:alt:Povolení pluginu pro Outlook připojit se k databázi

.._mail-plugin/outlook/add-shortcut:

Přidejte zkratku do pluginu
----------------------------

Výchozí nastavení aplikace Outlook umožňuje otevřít plugin z nabídky „Další akce“.
Je možné ho přidat vedle ostatních výchozích akcí.

V e-mailovém klientu Outlook klikněte na položku „Nastavení“, poté na „Zobrazit všechny nastavení“.
Nastavení.

.. obrázek: outlook/all-outlook-settings.png
:align:center
:alt: Zobrazení všech nastavení aplikace Outlook

Nyní vyberte položku „Upravit akce“ pod „Pošta“, klikněte na „Odoo pro
Outlook“ a pak „Uložit“.

.. obrázek: outlook/customize-actions.png
:align:center
:alt:Odoo pro Outlook - přizpůsobená akce

Po provedení této akce otevřete libovolnou e-mailovou zprávu a zkontrolujte, zda je zde zkratka.

.. obrázek: outlook/odoo-outlook-shortcut.png
:align:center
:alt:Odoo pro Outlook - přizpůsobená akce

Použitím doplňku
----------------

Nyní, když je doplněk nainstalován a funkční, vše, co musíte udělat k vytvoření kontaktu, je
klikněte na ikonu „O“ nebo přejděte do části „Další akce“ a klikněte na „Odoo“.
pro aplikaci Outlook“. Panel se objeví v pravé části a pod názvem „Příležitosti“
klikněte na tlačítko „New“. V novém okně se zobrazí vytvořená příležitost v databázi Odoo.
Obyvat.
