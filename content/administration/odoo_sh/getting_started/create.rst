
..._odoosh-gettingstarted-create:

===================
Vytvořte svůj projekt
===================

Nainstalujte svou platformu
====================

Přejděte na stránku „Odoo.sh“ (https://www.odoo.sh/) a klikněte na tlačítko „Deploy your platform“.

.. obrázek: vytvořit/nasadit.png
:align:center

Přihlásit se přes GitHub
===================

Přihlaste se pomocí svého účtu na GitHubu. Pokud ještě nemáte účet, klikněte na tlačítko Vytvořit účet
odkaz.

.. obrázek: vytvořit/github-signin.png
:align:center

Povolte Odoo.sh
=================

Grantujte Odoo.sh potřebné přístupy k vašemu účtu klepnutím na tlačítko *Autorizovat*.

.. obrázek: vytvořit/github-autorizace.png
:align:center

Odoo.sh v podstatě potřebuje:

* znát váš GitHub login a e-mail.
* vytvořit novou databázi v případě, že se rozhodnete začít od nuly.
* přečíst vaše stávající repozitáře včetně těch organizací, pokud si přejete
pracovat s existujícím repozitářem.
* vytvořit webhooku, který vás bude informovat o každém přidání změn.
* způsobit změny, které usnadní vaši implementaci, sloučit větve nebo přidat nové „podmoduly
Příkladem je například <https://git-scm.com/book/cs/v2/Git-Tools-Submodules>.

Přihlaste svůj projekt
===================

Zvolte, jestli chcete začít od nuly tím, že vytvoříte nový repozitář, nebo jestli chcete použít
existující repozitář.

Poté vyberte jméno nebo repozitář, který chcete použít.

Vyberte verzi Odoo, kterou chcete používat. Pokud plánujete do systému importovat existující databáze nebo
soubor aplikací, můžete si vybrat verzi podle potřeby. Pokud začínáte od nuly, použijte
poslední verze.

Zadejte své *číslo kuponu*. Toto číslo se také nazývá *referenční číslo*, *smluvní číslo* nebo
*aktivační kód*.

Měl by jít o kód vaší Enterprise předplatného, které zahrnuje Odoo.sh.

Partneři mohou použít své partnerské kódy k zahájení testovacího provozu. Pokud jejich zákazníci začnou projekt
Měli by si pořídit předplatné Enterprise, které zahrnuje i Odoo.sh a použít kód předplatného.
Vaše společnost získá zpět 50 % částky jako provizi. Kontaktujte svého obchodního zástupce nebo účetní.
manažer, aby ho získal.

Při odesílání formuláře vám může být sděleno, že vaše předplatné není platné. To znamená buď toto:

* není existující předplatné.
* Není to partnerství.
* jedná se o firemní předplatné, ale které neobsahuje Odoo.sh
* Není to partnerství ani podnikatelský účet (např. online
předplatného).

Pokud máte pochybnosti ohledně svého předplatného, obraťte se na podporu Odoo.
<https://www.odoo.com/help>

.. obrázek: vytvořit/nasadit formulář.png
:align:center

Hotovo!
=============

Můžete začít používat Odoo.sh. Váš první build je na cestě k vytvoření. Brzy budete moci
Připojte se k první databázi.

.. obrázek: vytvořit/nasadit-hotovo.png
:align:center

... _odoo_sh_import_your_database:

Importujte databázi
====================

Můžete do svého projektu na Odoo.sh importovat databázi, pokud je ve verzi podporované v :doc:`podpoře
podporované verze) v rámci systému Odoo.

Využijte své moduly v produkci
-------------------------------

Pokud používáte komunitní nebo vlastní moduly, přidejte je do větve ve svém repozitáři na GitHubu.
Databáze umístěné na online platformě Odoo.com nemají žádné vlastní moduly.
Uživatelé těchto databází tak mohou tento krok přeskočit.

Můžete strukturovat své moduly podle vlastního uvážení a Odoo.sh automaticky detekuje složky obsahující
Odoo doplňky. Například můžete umístit všechny moduly do kořenového adresáře vašeho
úložiště nebo skupiny modulů do složek podle kategorií, které si určíte (účetnictví, projekt,
...).

Pro komunitní moduly dostupné v veřejných repozitářích Git
Můžete také zvážit přidání jich pomocí :ref:`podmodulů <odoosh-advanced-submodules>“.

Pak buďto:
nebo:ref:`sloučit do vaší produkční větve<odoosh-gettingstarted-branches-mergingbranches>“.

Stáhněte si zálohu
-----------------

Databáze na místě
~~~~~~~~~~~~~~~~~~~~

Přihlaste se na adresu URL:soubor:/web/databáze/manažer a stáhněte si zálohu.

.. Varování:

Pokud nemůžete přistupovat k databázovému manažerovi, mohl být vypnutý vaším správcem systému.
Podrobnější informace naleznete v dokumentaci k bezpečnosti správce databáze.

Budete potřebovat hlavní heslo databáze serveru. Pokud jej nemáte, kontaktujte
správce systému.

.. obrázek: vytvořit/vytvořit-import-na-předplatném-zálohu.png
:align:center

Zvolte formát zálohování včetně složky s filmy.

.. obrázek: vytvořit/vytvořit-import-na-předplatné-zálohu-dialog.png


Odoo Online databáze
~~~~~~~~~~~~~~~~~~~~~

Přihlaste se do správce databází („https://accounts.odoo.com/my/databases/manage“) a stáhněte si
záloha vaší databáze.

.. obrázek: vytvořit/vytvořit-import-online-zálohu.png
:align:center

.. Varování:

Online verze (např. *saas-*) nejsou podporovány na Odoo.sh.

Nahrát zálohu
-----------------

Poté v projektu Odoo.sh ve svém produkčním oddělení v záložce „zálohy“ nahrajte zálohu.
jen co stáhnete.

.. obrázek: vytvořit/vytvořit-import-produkce.png
:align:center

Jakmile je záloha importována, můžete databázi přistupovat pomocí tlačítka „Připojit“ v historii.
pobočce.

.. obrázek:: create/create-import-production-done.png
:align:center

Zkontrolujte své odchozí e-mailové servery
---------------------------------

Služba Odoo.sh poskytuje výchozí poštovní server.
Pro jeho použití musí být v databázi zapnutý odchozí poštovní server.
Nastavení -> Technické -> Odchozí poštovní servery
Musí být aktivován režim vývojáře (<developer-mode>).

Po dokončení importu databáze jsou všechny odchozí e-mailové servery vypnuté a vy používáte Odoo.sh
e-mailový server, který je k dispozici v základní verzi.

.. varování:
Port 25 je (a bude) zavřený. Pokud chcete připojit k externímu SMTP serveru, měli byste
používat porty 465 a 587.

Zkontrolujte své naplánované akce
----------------------------

Po importu jsou všechny plánované akce deaktivovány.

Tímto způsobem se zabrání tomu, aby nově importovaná databáze provedla nějaké akce, které by mohly ovlivnit běžný provoz.
výroby, například odeslání zbývajících poštovních zásilek nebo zpracování hromadných poštovních zásilek.
synchronizace služeb třetích stran (kalendáře, soubory hostované na serveru, …)

Pokud plánujete používat importovanou databázi jako produkční, zapněte si ve schématu akcí, které potřebujete.
Můžete si zkontrolovat, co je v databázi původu povoleno a stejné akce zapnout i ve vyexportované
databáze. Předvolené akce jsou umístěny pod: menu „Nastavení -> Technické -> Automatizace
--> Plánované akce“.

Registrujte svůj předplatný
--------------------------

Při importu se vaše předplatné odpojí.

Do importované databáze se vkládají duplicitní záznamy výchozím nastavením, takže
protože můžete propojit pouze jednu databázi na jeden předplatný účet.

Pokud plánujete používat tento program ve své produkci, odpojte si starou databázi z předplatného a
registrovat nově importovanou databázi. Přečtěte si dokumentaci k registraci databází
pro další pokyny.
