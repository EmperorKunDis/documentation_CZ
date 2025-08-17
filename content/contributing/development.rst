Zobrazit obsah

===========
Rozvoj
===========

.. toctree::


rozvoj/pravidla pro kódování
vývoj/git_pravidla

Pokud čtete tento text, pravděpodobně máte zájem o získání informací o tom, jak přispět k
jádro Odoo. Ať už jste sem přišli záměrně nebo náhodou, máme pro vás řešení!

.. viz též:
:doc:`Zjistěte, jak můžete přispět k Odoo <../contributing>`

Když budete připraveni, skočte do části „přispívání / vývoj / nastavení“ a začněte svou cestu.
v přispívání k vývoji Odoo.

... přispívání/vývoj/instalace:

Nastavení prostředí
=================

Níže uvedené pokyny vám pomohou připravit vaše prostředí pro provádění místních změn kódu.
a poté je poslat na GitHub. Přeskočte tento odstavec a přejděte na
:ref:`přispívání/vývoj/první přispění`, pokud jste tento krok již splnili.

#Nejprve je třeba vytvořit účet na GitHubu (<https://github.com/join>). Odoo používá GitHub k
spravovat zdrojový kód svých produktů a právě zde budete provádět změny a podávat
Je jen na nich, zda je přijmou k dalšímu posouzení.
#Vytvořte nový klíč SSH a zaregistrujte jej u svého účtu na GitHubu
<https://docs.github.com/cs/authentication/connecting-to-github-with-ssh>.
#Přejděte na adresu „github.com/odoo/odoo <https://github.com/odoo/odoo>“ a klikněte na tlačítko „Fork“.
tlačítko v pravém horním rohu pro vytvoření forku (viz. :dfn:`vaše kopie`) repozitáře na vašem
účet. Stejně tak s „github.com/odoo/enterprise <https://github.com/odoo/enterprise>“
je k dispozici, což vytváří kopii zdrojového kódu, na který můžete provádět změny bez
ovlivňující hlavní kódovou základnu. Přeskočte tento krok, pokud pracujete pro Odoo.
#... zahrnout: instalace git.rst
#Nastavte Git tak, aby identifikoval vaši osobu jako autora budoucích příspěvků. Zadejte stejné
e-mailovou adresu, kterou jste použili při registraci na GitHubu.

... kódový blok: konzole

$ git config --global user.name "Váš Příjmení"
$ git config --global user.email "your_email@example.com"

#:doc:`Nainstalujte Odoo z zdrojů <../administration/on-premise/source>. Ujistěte se, že stáhnete
zdrojové soubory přes Git s SSH.
#Nastavte Git tak, aby posílal změny na váš fork (nebo forků), nikoliv do hlavního zdrojového kódu. Pokud pracujete pro
Odoo, nastavte Git tak, aby posílal změny na společné větve vytvořené na účtu **odoo-dev**.

... záložky::

.. tab:: Propojit s vaším forkem

V následujícím příkazu nahraďte <vaše_github_účet> jménem účtu na GitHub.
na kterém jste vytvořili odnož(y).

... kódový blok: konzole

$ cd do adresáře CommunityPath
$ git remote add dev git@github.com:<vaše_github_účet>/odoo.git

Pokud máte přístup k modulu „odoo/enterprise“, nastavte také příslušný vzdálený server.

... kódový blok: konzole

$ cd /EnterprisePath
$ git remote add dev git@github.com:<vaše_github_účet>/enterprise.git

... tab:: Propojit git s odoo-dev

... kódový blok: konzole

$ cd do adresáře CommunityPath
$ git remote add dev git@github.com:odoo-dev/odoo.git
$ git remote set-url --push origin neměli byste tento repozitář pushnout

$ cd /EnterprisePath
$ git remote add dev git@github.com:odoo-dev/enterprise.git
$ git remote set-url --push origin neměli byste tento repozitář pushnout

#Takže jste připraveni na svůj první příspěvek.
<přispívání/vývoj/první příspěvek>.

... přispívání/vývoj/první příspěvek:

Učinit první příspěvek
============================

.. důležité:
   - Vývoj aplikací Odoo může být pro začátečníky náročný. Doporučujeme, abyste měli dostatek znalostí
předem sepsat malý modul. Pokud tomu tak není, vložte do projektu nějaký čas
přes návody pro vývojáře, které najdete na stránce :doc:`Výukové programy pro vývojáře </developer/tutorials>`, abyste zaplnili mezery.
   - Některé kroky v tomto průvodci vyžadují, abyste byli s Git pohodlně seznámeni. Zde jsou nějaké „návody
<https://www.atlassian.com/git/tutorials> a interaktivní trénink
<https://learngitbranching.js.org/> pokud se v nějaké části zaseknete.

Teď, když máte prostředí nastaveno, můžete začít přispívat do kódu. V terminálu
Přejděte do složky, ve které jste nainstalovali Odoo z zdrojů a postupujte podle návodu níže.

#Vyberte verzi Odoo, kterou chcete upravit. Pamatujte na příspěvky
cílení na nepodporovanou verzi Odoo (</administration/supported_versions>).
byly přijaty. Tento průvodce předpokládá, že změny se zaměřují na verzi Odoo {CURRENT_VERSION}, což odpovídá
větve {CURRENT_BRANCH}.
#Vytvořit novou větev, která začíná od větve {CURRENT_BRANCH}. Před jménem větve přidat základ
branch: „{CURRENT_BRANCH}-…“. Pokud pracujete pro Odoo, přidejte k názvu větve své jméno.
handle: {CURRENT_BRANCH}-...-xyz.

...... příklad::

... kódový blok: konzole

$ git switch -c {POČÍTAČEK} -fix-faktury

... kódový blok: konzole

$ git switch -c {ZPĚTNÁ VETKA}-opravit faktury xyz

#Pokud nebylo provedeno, podepište smlouvu o licenci GNU Affero General Public License (AGPL) pomocí příkazu _`Sign the Odoo CLA <{GITHUB_PATH}/doc/cla/sign-cla.md>`_.
Vy pracujete pro Odoo.
#Vytvořte požadované změny v kódu. Při práci na kódu dodržujte tyto pravidla:

   - Zaměřte se na konkrétní funkci nebo opravu chyby.
v jednom kroku, namísto řešení několika nezávislých změn najednou.
   - Uvědomte si, že je třeba mít „stabilní politiku“.
<https://github.com/odoo/odoo/wiki/Přispívání#co-znamená-stabilní-verze>
jinou větev než „master“.
   - Postupujte podle pokynů pro kódování v dokumentu :doc:`<development/coding_guidelines>`.
   - Pečlivě testujte své změny a napište si testy do
zajistit, aby vše fungovalo tak, jak má a nebyly žádné zpětný skoky nebo nepředvídané chování.
důsledky.

#Přidejte své změny. Napište jasný zprávu o přidání jako je popsáno v :doc:`Git guidelines
<rozvoj/git_pravidla>.

... kódový blok: konzole

$ git add .
$ git commit

#Přidejte své změny do svého větve, pro kterou jsme přidali odkaz na vzdálený server „dev“.

...... příklad::

... kódový blok: konzole

$ git push -u develop {CURRENT_BRANCH}-fix-invoices-xyz

#Otevřete na GitHubu požadavek na změnu (pull request) pro předložení svých změn k přezkoumání.

   #Přejděte na stránku s porovnáním odoo/odoo kódu <https://github.com/odoo/odoo/compare>.
stránka s porovnáním kódu odoo/enterprise
<https://github.com/odoo/enterprise/compare>, podle kterého kódu se vaše změny týkají
cíl.
   #Vyberte **{POUŽITÉ BRÁNĚ}** jako základní verzi.
   #Klikněte na: guilabel:srovnávat větve.
   #Vyberte **<vaše_github_účet>/odoo** nebo **<vaše_github_účet>/enterprise** jako hlavní
repozitář. Vyplňte místo znaku „<“ název vašeho účtu na GitHubu, který je uvedený v poli „Account“.
vytvořil odnož nebo odoo-dev, pokud pracujete pro Odoo.
   #Zkontrolujte své změny a klikněte na tlačítko „Vytvořit požadavek na převzetí“.
   #Zatrhněte políčko „Povolit úpravy od správce“. Pokud pracujete v Odoo, tento krok přeskočte.
   #Dokončete popis a klikněte na tlačítko „Vytvořit požadavek na převzetí“.

#Níže na stránce zkontrolujte stav sloučení a vyřešte případné problémy.
#Jakmile bude váš :abbr:`PR (Pull Request)` připravený k sloučení, člen týmu Odoo
je automaticky přidělen k recenzi. Pokud má recenzent nějaké otázky nebo poznámky,
Vložte je jako komentář a budete o tom informováni e-mailem. Tyto komentáře musí být vyřešeny
pro příspěvek, aby mohl být přijat.
#Jakmile jsou vaše změny schváleny, revize je sloučí a budou k dispozici všem uživatelům Odoo.
uživatelé po další aktualizaci kódu!
