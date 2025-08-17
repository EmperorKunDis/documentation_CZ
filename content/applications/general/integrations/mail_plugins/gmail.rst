============
Plug-in pro Gmail
============

Plug-in *Gmail* integruje databázi Odoo s poštovní schránkou Gmailu, takže uživatelé mohou sledovat všechny
jejich práci mezi Gmailem a Odoo bez ztráty informací.

Uživatelé Odoo Online
=================

Pro databáze hostované na Odoo Online (nebo Odoo.sh) postupujte podle níže uvedených kroků, abyste nakonfigurovali Gmail
Plug-in.

Nainstalujte doplněk Gmail
------------------------

Nejprve se přihlaste do účtu Gmailu, ke kterému chcete Odoo připojit.

V e-mailové schránce Gmail klikněte na ikonu plusu v pravém panelu pro získání doplňků.
panel není vidět, klikněte na šipku v pravém dolním rohu schránky pro jeho zobrazení.

.. obrázek: gmail/gmail-side-panel.png
:align:center
:alt: Plus symbol na straně panelu poštovní schránky v Gmailu.

Poté vyhledejte „Odoo“ a najděte „Odoo Inbox Addin“.

.. obrázek: gmail/google-workspace-marketplace.png
:align:center
:alt:Odoo Inbox Addin na Google Workspace Marketplace.

Nebo se rovnou přesuňte na stránku Odoo Inbox Addin v Google Workspace Marketplace.
<https://workspace.google.com/marketplace/app/odoo_inbox_addin/873497133275>

Jakmile je doplněk nalezený, klikněte na tlačítko „Instalovat“ a poté na „Pokračovat“, abyste mohli začít
instalace.

Dále vyberte Gmail účet, ke kterému chcete připojit Odoo a pak klikněte na tlačítko „Povolit“.
Odoo přístup k vašemu účtu Google. Google poté zobrazí okno s potvrzením, že
montáž byla úspěšná.

Nastavte databázi Odoo
---------------------------

Funkci „Plug-in Mail“ je nutné v databázi Odoo zapnout, aby bylo možné používat Gmail.
Plugin. Chcete-li tuto funkci zapnout, přejděte na: „Nastavení“ -> „Obecné nastavení“.
V sekci „Spojení“ aktivujte „Plug-in pro e-mail“, a pak klikněte
:guilabel:`Uložit“.

.. obrázek: gmail/mail-plugin-settings.png
:align:center
:alt:Funkce Připojení k e-mailu v nastavení.

Nastavte poštovní schránku Gmail
-------------------------

V hlavní schránce Gmailu je nyní vidět modrá ikona Odoo v pravém panelu. Klikněte na Odoo
ikonu pro otevření okna s doplňkem Odoo. Pak klikněte na jakoukoliv e-mailovou zprávu v doručené poště.
V okně rozšíření zvolte možnost „Povolit přístup“ a udělte Odoo přístup k vašemu e-mailu v Gmailu.

.. obrázek: gmail/autorizace-přístupu.png
:align:center
:alt:Tlačítko Povolit přístup v pravém sloupci panelu s doplňky Odoo.

Dále klikněte na tlačítko „Přihlásit se“ a zadejte adresu databáze Odoo, kterou chcete použít.
Připojte se k doručené poště Gmail a přihlaste se do databáze.

.. poznámka::
Použijte obecnou adresu URL databáze, nikoliv konkrétní adresu URL stránky v databázi.
například použijte „https://mojefirma.odoo.com“, nikoli
„https://mojefirma.odoo.com/web#cids=1&action=menu“.

Konečně klikněte na tlačítko „Povolit“ a umožněte Gmailu přístup do databáze Odoo. Prohlížeč poté zobrazí
Zpráva „Úspěch!“ a poté okno zavřete. V e-mailové schránce Gmailu a databázi Odoo
spojené.

Uživatelé Odoo On-Premise
=====================

Pro databáze hostované na serverech jiných než Odoo Online (nebo Odoo.sh) postupujte podle následujících kroků:
Nastavit plugin Gmail.

.. poznámka::
Google vyžaduje od tvůrců doplňků seznam URL.
které lze použít v akcích a přesměrováních spuštěných rozšířením. Toto chrání uživatele před
zajištění například toho, aby se doplněk neodkazoval na škodlivé webové stránky.
„Google Apps Script <https://developers.google.com/apps-script/manifest/allowlist-url>“.)

Odoo může pouze zobrazit doménu „odoo.com“ a ne každý unikátní server zákazníků, který je umístěn v prostředí na místě.
doméně, zákazníci na vlastním serveru nemohou nainstalovat rozšíření Gmail z Google Workspace
Marketplace.

Nainstalujte doplněk Gmail
------------------------

Nejprve se přihlaste do „GitHub repozitáře <https://github.com/odoo/mail-client-extensions>“ pro
Odoo Mail Plugins. Nyní klikněte na zelené tlačítko „Kód“. Poté klikněte
:guilabel:`Stáhnout ZIP“ ke stažení souborů pluginu do počítače uživatele.

.. obrázek: gmail/gh-download-zip.png
:align:center
:alt:Stáhněte si archiv ZIP z repozitáře Githubu pro Mail Plugins.

Otevřete soubor ZIP na počítači. Pak přejděte do složky:
gmail --> src --> views“, a otevřete soubor „login.ts“ pomocí libovolného softwaru pro úpravu textů.
například Notepad (Windows), TextEdit (Mac) nebo Visual Studio Code.

Odeberte následující tři řádky textu z souboru `login.ts`:

.. kódový blok::

pokud (!/^https:\/\/([^\/?]*\.)?odoo\.com(\/|$)/.test(validatedUrl)) {
return notify("URL musí být poddoménou odoo.com");
   }

Tímto se odstraní omezení domény „odoo.com“ z programu Gmail Plugin.

Dále se v souboru ZIP přesuňte do složky :menuselection:`mail-client-extensions-master --> gmail` a otevřete
souboru s názvem :guilabel:`appsscript.json`. V sekci :guilabel:`urlFetchWhitelist` nahraďte všechny
odkaz na „odoo.com“ s unikátním doménovým jménem zákazníka Odoo.

Poté otevřete soubor s názvem :guilabel:`README.md`, který je umístěn v stejné složce jako :guilabel:`gmail`.
návod v souboru README.md, jak nahrát soubory pluginu do projektu Google.

.. poznámka::
Počítač musí umět spouštět příkazy Linuxu, aby mohl následovat pokyny v
:guilabel:`README.md“ souboru.

Poté sdílejte projekt Google s účtem Gmail, který chcete propojit s Odoo.
Poté klikněte na tlačítko „Zveřejnit“ a „Vyvinout ze šablony“. Nakonec klikněte
:guilabel:`Nainstalujte doplněk“ k instalaci doplňku Gmail.

Nastavte databázi Odoo
---------------------------

Funkci „Plug-in Mail“ je nutné v databázi Odoo zapnout, aby bylo možné používat Gmail.
Plugin. Chcete-li tuto funkci zapnout, přejděte na: „Nastavení“ -> „Obecné nastavení“.
V sekci „Spojení“ aktivujte „Plugin pro e-mail“, a pak klikněte na „Uložit“.

.. obrázek: gmail/mail-plugin-settings.png
:align:center
:alt:Funkce Připojení k e-mailu v nastavení.

Nastavte poštovní schránku Gmail
-------------------------

V hlavní schránce Gmailu je nyní vidět modrá ikona Odoo v pravém panelu. Klikněte na Odoo
ikonu pro otevření okna s doplňkem Odoo. Pak klikněte na jakoukoliv e-mailovou zprávu v doručené poště.
V okně rozšíření zvolte možnost „Povolit přístup“ a udělte Odoo přístup k vašemu e-mailu v Gmailu.

.. obrázek: gmail/autorizace-přístupu.png
:align:center
:alt:Tlačítko Povolit přístup v pravém sloupci panelu s doplňky Odoo.

Dále klikněte na tlačítko „Přihlásit se“ a zadejte adresu databáze Odoo, kterou chcete použít.
Připojte se k doručené poště Gmail a přihlaste se do databáze.

.. poznámka::
Použijte obecnou adresu URL databáze, nikoliv konkrétní adresu URL stránky v databázi.
například použijte „https://mojefirma.odoo.com“, nikoli
„https://mojefirma.odoo.com/web#cids=1&action=menu“.

Konečně klikněte na tlačítko „Povolit“ a umožněte Gmailu přístup do databáze Odoo. Prohlížeč poté zobrazí
Zpráva „Úspěch!“ a poté okno zavřete. V e-mailové schránce Gmailu a databázi Odoo
spojené.
