========
Nastavení
========

Přehled
========

Nastavení umožňuje spravovat konfiguraci vašeho projektu.

.. obrázek: nastavení/předvolby-rozhraní.png
:align:center

Název projektu
============

Název vašeho projektu.

.. obrázek: nastavení/rozhraní-nastaveni-projektname.png
:align:center

Toto určuje adresu, kterou použijete k přístupu ke své produkční databázi.

Jméno vašich sestavení a vývojových verzí je odvozeno z názvu této složky a přiřazeno
automaticky. Při změně názvu projektu se však použije nový název pouze u budoucích sestavení.

..._odoosh-gettingstarted-settings-collaborators:

Spolupracovníci
=============

Spravujte uživatele GitHub, kteří mohou přistupovat ke svému projektu.

.. obrázek: nastavení/předvolby-rozhraní-spolupracovníci.png
:align:center

Existují tři úrovně uživatelů:

- :guilabel:`Administrátor“: má přístup ke všem funkcím projektu Odoo.sh.

- :guilabel:`Tester`: má přístup k databázím *Staging* a *Development* a jejich nástrojům.
Tato role je pro uživatele, kteří provádějí testování přijatelnosti. Tester může pracovat s kopiemi
výrobní data, ale nemohou se dostat k výrobní databázi prostřednictvím nástrojů Odoo.sh.

- :guilabel:`Vývojář“: má přístup pouze k databázím a nástrojům pro vývojáře.
role je pro vývojáře, kteří navrhují změny v kódu, ale nemají přístup do produkce.
a nasazování databází prostřednictvím nástrojů Odoo.sh.

.. seznam tabulkový::
:hlavičkové řádky: 1
:šířky: auto

   * -
     -
     - Developer
     - Tester
     - Admin
   * -Vývoj
     - Historie
     - |zelená|
     - |zelená|
     - |zelená|
   * -
     - Připojení na jeden klik
     - |zelená|
     - |zelená|
     - |zelená|
   * -
     - Logy
     - |zelená|
     - |zelená|
     - |zelená|
   * -
     - Shell/SSH
     - |zelená|
     - |zelená|
     - |zelená|
   * -
     - E-maily
     - |zelená|
     - |zelená|
     - |zelená|
   * -
     - Nastavení
     - |zelená|
     - |zelená|
     - |zelená|
   * - Režie
     - Historie
     - |zelená|
     - |zelená|
     - |zelená|
   * -
     - Připojení na jeden klik
     -
     - |zelená|
     - |zelená|
   * -
     - Logy
     -
     - |zelená|
     - |zelená|
   * -
     - Shell/SSH
     -
     - |zelená|
     - |zelená|
   * -
     - E-maily
     -
     - |zelená|
     - |zelená|
   * -
     - Monitorování
     -
     - |zelená|
     - |zelená|
   * -
     - Zálohy
     -
     -
     - |zelená|
   * -
     - Upgrade
     -
     - |zelená|
     - |zelená|
   * -
     - Nastavení
     -
     - |zelená|
     - |zelená|
   * -Produkce
     - Historie
     - |zelená|
     - |zelená|
     - |zelená|
   * -
     - Připojení na jeden klik
     -
     -
     - |zelená|
   * -
     - Logy
     -
     -
     - |zelená|
   * -
     - Shell/SSH
     -
     -
     - |zelená|
   * -
     - E-maily
     -
     -
     - |zelená|
   * -
     - Monitorování
     -
     -
     - |zelená|
   * -
     - Zálohy
     -
     -
     - |zelená|
   * -
     - Upgrade
     -
     -
     - |zelená|
   * -
     - Nastavení
     -
     -
     - |zelená|
   * – Stav
     -
     - |zelená|
     - |zelená|
     - |zelená|
   * - Nastavení
     -
     -
     -
     - |zelená|

.. varování:
Tyto role se vztahují pouze na používání Odoo.sh. Je důležité, aby byly uživatelské role
attributionu v repozitáři na GitHubu. Prosím, odkazujte se na dokumentaci k GitHubu.
`Správa pravidla ochrany větve <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule>`_
pro podrobné pokyny.

.. |zelená| neupravený:: html



.. |červená| neupravený:: html

<span class="text-danger" style="font-size: 32px; line-height: 0.5">●</span>

.. |červená| syrová:: html

<span class="text-danger" style="font-size: 32px; line-height: 0.5">●</span>

Přístup veřejnosti
=============

Umožněte veřejnosti přístup k vývojovým verzím.

.. obrázek: nastavení/rozhraní-nastaveni-veřejné.png
:align:center

Pokud je tato možnost aktivována, zobrazí se stránka Sestavení veřejně a návštěvníci si mohou prohlédnout protokoly vývojových sestavení.

Výroba a montáž jsou vyloučeny, návštěvníci mohou vidět pouze jejich stav.

..._odoosh-gettingstarted-settings-modules-installation:

Stavy závazků na GitHubu
======================

Tato možnost umožňuje Odoo.shu posílat stavy závazků do vašeho repozitáře na GitHub při každém spouštění.
vytvořen nebo aktualizován. Používá k tomu token GitHubu s oprávněním pro přidávání stavů komitů.
repozitář. Sledujte dokumentaci GitHubu o osobních přístupových tokenech <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>_.
pro pokyny k vytvoření vašeho.

.. poznámka::
GitHub má **jemně nastavené osobní tokeny** s datem vypršení platnosti, které budou zablokovány.
neaktualizovat stav závazku. Můžete kdykoli nahradit token na Odoo.sh.

Stavy závazků, které jsou vytlačeny na GitHub, mohou mít následující kontexty:

- :guilabel:`ci/odoo.sh (dev)`: stav vývojové verze
- :guilabel:`ci/odoo.sh (staging)`: stav stážního sestavení
- :guilabel:`ci/odoo.sh (production)`: stav produkční verze
- :guilabel:`ci/odoo.sh (test_ci)`: Testování tokenu z nastavení stránky bude spouštět test
stav posledního závazku vašeho repozitáře

Vlastní domény
==============

Pro konfiguraci dalších domén se podívejte na příslušnou záložku nastavení:
<odoosh-gettingstarted-branches-tabs-settings>.

..._odoosh-gettingstarted-settings-submodules:

Submoduly
==========

Nastavte klíče pro nasazení soukromých repozitářů, které používáte
jako podmoduly ve vašich větvích, aby Odoo.sh mohl stáhnout je.

.. varování:
Tyto nastavení jsou vyžadována pouze pro soukromé repozitáře. Pokud hledáte, jak tyto nastavení nastavit,
zvyšte své podmoduly, návod je k dispozici v kapitole :ref:`Podmoduly
těchto dokumentací.

.. obrázek: nastavení/předvolby-rozhraní-podmoduly.png
:align:center

Pokud je repozitář soukromý, není možné veřejně stahovat jeho větve a revize.
Proto je potřeba nakonfigurovat nasazovací klíč pro Odoo.sh
Takže vzdálený Git server nám umožňuje stahovat revize naší platformy.
soukromé repozitáře.

Pro konfiguraci klíče pro soukromý repozitář postupujte následovně:

* V poli „URL“ vložte SSH URL soukromého podrepositáře a klikněte na tlačítko *Přidat*.

  * např. *git@github.com:uživatelské jméno/repozitář.git*
  * Může být jiný gitový server než GitHub, například Bitbucket, GitLab nebo dokonce vlastní samo-hostovaný.
server

* zkopírujte veřejný klíč.

  * Měl by vypadat takto: *ssh-rsa nějaké ... náhodné ... znaky ... zde ... ==*

* Ve nastavení soukromé podskupiny přidejte veřejný klíč mezi nasazovací klíče.

  * Github.com: :menuselection:`Nastavení --> Klíče pro nasazení --> Přidat klíč k nasazení“
  * Bitbucket.com: „Nastavení“ -> „Přístupové klávesy“ -> „Přidat klíč“
  * Gitlab.com: „Nastavení“ → „Soubor“ → „Deploy Keys“
  * Soukromé klíče: přidejte klíč do souboru autorizovaných klíčů uživatele git v adresáři .ssh

Velikost úložiště
============

Tato část ukazuje velikost úložiště, které vaše projekt využívá.

.. obrázek: nastavení/předvolby-uložení.png
:align:center

Velikost úložiště se vypočítává následovně:

* velikost databáze PostgreSQL

* velikost diskových souborů dostupných ve vašem kontejneru: databáze, uložiště relací...

.. varování:
Pokud chcete analyzovat využití disku, můžete spustit nástroj ncdu.
v Web Shellu, viz <https://dev.yorhel.nl/ncdu/man>.

Pokud velikost vaší produkční databáze přesáhne to, co je v rámci vašeho předplatného k dispozici,
bude automaticky synchronizován s ním.

Dělníci v databázi
================

Zde lze konfigurovat další pracovníky databáze, kteří pomohou zvýšit zatížení vaší
databáze produkce je schopna zpracovat. Pokud přidáte víc, bude automaticky synchronizováno
s předplatným.

.. obrázek: nastavení/předvolby-rozhraní-dělníků.png
:align:center

.. Varování:
Přidáním více pracovníků se problém výkonnosti nevyřeší zázračně. Jen umožní serveru
aby bylo možné zpracovat více spojení najednou. Pokud jsou některé operace neobvykle pomalé, je
pravděpodobně problém s kódem, pokud není způsobený vašimi vlastními úpravami můžete otevřít požadavek.
„tady <https://www.odoo.com/help>“.

Branchování
================

Přídavné větve pro vývoj a testování umožňují vyvíjet a testovat více funkcí najednou. Pokud
Přidejte více a bude automaticky synchronizováno s vaší předplatbou.

.. obrázek: nastavení/rozhraní-nastavení-vývojových-větví.png
:align:center

Aktivace
==========

Zobrazuje stav aktivace projektu. Můžete změnit aktivační kód projektu, pokud
nebyla nutná.

.. obrázek: nastavení/přístupové údaje-aktivace.png
:align:center
