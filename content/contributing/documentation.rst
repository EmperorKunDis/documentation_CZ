Zobrazit obsah

=============
Dokumentace
=============

.. toctree::


dokumentace/pravidla obsahu
dokumentace/rst_pravidla

Tento úvodní průvodce vám pomůže získat potřebné nástroje a znalosti, abyste mohli přispět k
dokumentace.

Přečtěte si úvod do jazyka reStructed Text: :ref:`<contributing/documentation/rst-intro>`.
Pokud jste s ním nebyli seznámeni. Pak je dvě možnosti, jak začít přispívat do
dokumentace:

- Pro menší změny, jako je například přidání odstavce nebo oprava překlepu, doporučujeme používat
GitHub rozhraní**. To je nejjednodušší a nejsnadnější způsob, jak změny podat, a je vhodné pro
neprogramátory. Přeskočte přímo na :ref:`příspěvky/dokumentace/první příspěvek`.
část, kde se můžete pustit do práce.
- Pro složitější změny, například přidání nové stránky, je nutné **použít Git** a pracovat
z místní kopie dokumentace. Postupujte podle pokynů v
:ref:`contributing/documentation/setup`, abyste připravili své prostředí.

.. viz též:
:doc:`Zjistěte, jak můžete přispět k Odoo <../contributing>`

..._přispívání/dokumentace/rst-intro:

reStrukturovaný text (RST)
======================

Dokumentace je napsaná v **reStrukturovaném textu** (RST), což je „lehký značkovací jazyk
<https://cs.wikipedia.org/wiki/Lehký_značkovací_jazyk> tvořená z běžného textu doplněná
s značkami, které umožňují vkládat nadpisy, obrázky, poznámky a podobně.
(reStrukturovaný text) je snadno použitelný i pro ty, kteří s ním nejsou obeznámeni.

.. důležité:
Buďte si vědomi našich :doc:`pravidel pro obsah <documentation/content_guidelines>“.
:doc:`Doporučení RST <documentation/rst_guidelines>“ při psaní dokumentace. To zajišťuje
aby dokumentace zůstala konzistentní a aby tým Odoo mohl schválit změny.

... přispívání, dokumentaci a instalaci:

Nastavení prostředí
=================

Následující pokyny vám pomohou připravit vaše prostředí pro provádění místních změn
dokumentace a poté je vložit na GitHub. Přeskočte tento oddíl a přejděte na
:ref:`přispívání/dokumentace/první příspěvek`, pokud jste tento krok již vykonali nebo chcete
udělat změny z rozhraní Githubu.

#Nejprve „vytvořte účet na GitHubu <https://github.com/join>“. Odoo používá GitHub k řízení
Zdrojový kód svých produktů a zde budete předkládat své změny.
#Vytvořte nový klíč SSH a zaregistrujte jej u svého účtu na GitHubu
<https://docs.github.com/cs/authentication/connecting-to-github-with-ssh>.
#Navštivte „github.com/odoo/documentation <https://github.com/odoo/documentation>“ a klikněte na
:guilabel:`Tlačítko Fork“ v pravém horním rohu, abyste mohli vytvořit svou vlastní kopii (:dfn:„vlastní verzi“)
repozitář na vašem účtu. To vytvoří kopii zdrojového kódu, ke kterému můžete provádět změny
bez ovlivnění hlavního kódu. Tento krok vynechejte, pokud pracujete pro Odoo.
#... zahrnout: instalace git.rst
#Nastavte Git tak, aby identifikoval vaši osobu jako autora budoucích příspěvků. Zadejte stejné
e-mailovou adresu, kterou jste použili při registraci na GitHubu.

... kódový blok: konzole

$ git config --global user.name "Váš Příjmení"
$ git config --global user.email "your_email@example.com"

#Klonujte zdroje pomocí Git a přejděte do místního repozitáře.

... kódový blok: konzole

$ git clone git@github.com:odoo/documentation.git
$ cd dokumentace

#Nastavte Git tak, aby posílal změny do vašeho forků místo hlavní kódu. V příkazech
Níže nahraďte <vaše_github_účet> názvem účtu na GitHubu, který jste vytvořili.
fork. Pokud pracujete v Odoo, tento krok přeskočte.

... kódový blok: konzole

$ git remote add dev git@github.com:<vaše_github_účet>/dokumentace.git

#Konfigurujte Git tak, aby spolupráce mezi autory z různých systémů byla snadnější.

... záložky::

.. skupina-tab:: Linux a macOS

... kódový blok: konzole

$ git config --global core.autocrlf input
$ git config commit.template `pwd`/commit_template.txt

.. skupina-tab:: Windows

... kódový blok: konzole

$ git config --global core.autocrlf true
$ git config commit.template "%CD%"/commit_template.txt

#Nainstalujte nejnovější verzi Pythonu <https://wiki.python.org/moin/BeginnersGuide/Download>
a pip <https://pip.pypa.io/en/stable/installation/>
#Nainstalujte závislosti na dokumentaci pomocí pipu.

... kódový blok: konzole

$ pip install -r požadavky.txt

Zkontrolujte, zda je adresář instalace závislostí na Pythonu součástí systému.
proměnná PATH.

... záložky::

.. skupina-tab:: Linux a macOS

Sledujte „návod k aktualizaci proměnné PATH na Linuxu a macOS
<https://unix.stackexchange.com/a/26059>_ s instalací Pythonu
závislosti (výchozí cesta: ~/.local/bin).

.. skupina-tab:: Windows

Sledujte „Návod k aktualizaci proměnné PATH na Windows“
<https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/>
s instalací závislostí na Pythonu.

#Nainstalujte si make.

... záložky::

... skupina-tab:: Linux

... kódový blok: konzole

$ sudo apt instalovat make -y

.. skupina-tab: macOS

Sledujte „návod k instalaci Make na macOS <https://formulae.brew.sh/formula/make>“

.. skupina-tab:: Windows

Sledujte návod na instalaci Make na Windows
<https://www.technewstoday.com/instalace-a-použití-make-v-oknech>

#„Nainstalujte pngquant <https://pngquant.org/>“.
#Jste připraveni na svůj první příspěvek.
<contributing/documentation/first-contribution> s Gitem.

… přispívání/dokumentace/první příspěvek:

Přispívat k dokumentaci
=================================

.. záložky::

...... záložka: Přispívejte z rozhraní Github

      #Nejprve „vytvořte účet na GitHubu <https://github.com/join>“. Odoo používá GitHub k řízení
zdrojový kód svých produktů a zde budete předkládat své změny.
      #Zkontrolujte, že procházíte dokumentací ve verzi, kterou chcete změnit.
Verzi lze vybrat z nabídky v horním menu.
      #Přejděte na stránku, kterou chcete změnit, a klikněte na tlačítko „Upravit v Githubu“.
v pravém horním rohu stránky.
      #Klikněte na tlačítko „Vytvořit vlastní repozitář“ („fork“).
kopie) repozitáře na vašem účtu. To vytvoří kopii kódu, ke kterému máte přístup.
Pokud pracujete v Odoo, tento krok přeskočte.

.. obrázek: dokumentace/fork-repository.png
:skalka: 60 %

      #Provedené změny uveďte do souladu s obsahem článku:
<dokumentace/pravidla-obsahu> a :doc:`RST <dokumentace/pravidla-pro-RST>
doporučení.

... tip::
Klikněte na tlačítko „Náhled změn“ pro zobrazení vašeho příspěvku v podrobnějším pohledu.
čitelném formátu. Buďte si vědomi, že náhled není schopen zpracovat všechny značky
Přesně tak. Například poznámky a tipy jsou zobrazeny jako prostý text.

      #Přejděte na konec stránky a vyplňte malý formulář, abyste navrhli své změny.
první textový box, napište velmi stručný popis svých změn. Například „Oprava překlepu“
nebo „Přidat dokumentaci k fakturaci prodejních objednávek.“ V druhém textovém poli vysvětlete *proč*.
Pokud navrhujete tyto změny, pak klikněte na tlačítko :guilabel:`Navrhnout změnu`.

.. obrázek: dokumentace/navrhni-zmeny.png
:skalka: 60 %

      #Zkontrolujte své změny a klikněte na tlačítko „Vytvořit požadavek na převzetí“.
      #Zatrhněte políčko „Umožnit úpravy od správce“. Pokud pracujete pro
Odoo.
      #Zkontrolujte shrnutí, které jste napsali o svých změnách, a klikněte na tlačítko Vytvořit.
tlačítko „Přidat požadavek na aktualizaci“ znovu.
      #Níže na stránce zkontrolujte stav sloučení a vyřešte případné problémy.
      #Jakmile bude váš :abbr:`PR (Pull Request)` připravený k sloučení, člen týmu Odoo
Pokud má recenzent nějaké otázky nebo připomínky, budou automaticky přiřazeny k přezkoumání.
Vložte je jako komentář a budete upozorněni e-mailem. Tyto komentáře musí být vyřešeny
aby se příspěvek mohl vyplatit.

      #Jakmile jsou vaše změny schváleny, recenzent je sloučí a ty se zobrazí na webu.
den.

.......:Přispívejte pomocí Git

...............důležité::
Některé kroky v tomto průvodci vyžadují pohodlí s Gitem. Zde jsou nějaké „návody
<https://www.atlassian.com/git/tutorials> a interaktivní trénink
<https://naučsegitbranching.js.org/>, pokud se v některém bodě zaseknete.

Nyní, když máte prostředí nastavené, můžete začít přispívat do dokumentace.
terminalu a přejděte do složky, kde jste zkopírovali zdrojové kódy, a následujte pokyny níže.

      #Vyberte verzi dokumentace, do které chcete provádět změny.
že příspěvky, které cílí na nepodporovanou verzi Odoo
</správa/podporované-verze> nejsou přijímány. Tento průvodce předpokládá, že změny
cílí na dokumentaci Odoo {CURRENT_VERSION}, což odpovídá větvi
"{ZÁKLADNÍ BRANCH}"
      #Vytvořte novou větev, která začíná od větve {CURRENT_BRANCH}. Před jméno větve přidejte
základní větev: '{CURRENT_BRANCH}-...'. Pokud pracujete pro Odoo, přidejte k názvu větve své jméno.
Odoo handle: {POZNÁMKA}.

... příklad::

... kódový blok: konzole

$ git checkout -c {CURRENT_BRANCH}-explain-pricelists

... kódový blok: konzole

$ git checkout -c {CURRENT_BRANCH}-vysvetlit-ceniky-xyz

      #Provedené změny uveďte do souladu s obsahem článku:
<dokumentace/pravidla-obsahu> a :doc:`RST <dokumentace/pravidla-pro-RST>
doporučení.
      #Souborů PNG, které byly přidány nebo upraveny.

... kódový blok: konzole

$ pngquant cesta/k/obrazu.png
$ mv cesta/k/obrazu-fs8.png cesta/k/obrazu.png

      #Napište řádek „přesměrování“.
<https://github.com/odoo/documentation/tree/{BRANCH}/redirects/MANUAL.md> pro každý RST
soubor, který byl přejmenován.
      #Postavte dokumentaci pomocí příkazu make. Pak otevřete soubor _build/index.html v prohlížeči.
prohlížeč, abyste mohli dokumentaci s vašimi změnami procházet.

... tip::
Použijte příkaz :command:`make help`, abyste se dozvěděli o dalších užitečných příkazech.

      #Přidejte své změny. Napište jasný zprávu o přidání jako je popsáno v :doc:`Git guidelines
<rozvoj/git_pravidla>.

... kódový blok: konzole

$ git add .
$ git commit

      #Přidejte své změny do vaší větve, pro kterou jsme přidali název vzdáleného aliasu dev.

... příklad::

... kódový blok: konzole

$ git push -u develop {CURRENT_BRANCH}-explain-pricelists

Pokud pracujete pro Odoo, přidejte své změny přímo do hlavní repozitáře s odkazem
„původ“.

... příklad::

... kódový blok: konzole

$ git push -u origin {CURRENT_BRANCH}-vysvetlit-ceny-xyz

      #Otevřete na GitHubu požadavek na změnu (pull request) pro předložení svých změn k přezkoumání.

         #Přejděte na stránku s porovnáním kódu odoo/documentation.
<https://github.com/odoo/documentation/compare>.
         #Vyberte **{POUŽITÉ BRÁNĚ}** jako základní verzi.
         #Klikněte na: guilabel:srovnávat větve.
         #Vyberte **<vaše_github_účet>/odoo** jako hlavní repozitář.
„<vaše_github_účet>“ s názvem účtu na GitHubu, kde jste vytvořili
větve. Pokud pracujete pro Odoo, tento krok vynechte.
         #Zkontrolujte své změny a klikněte na tlačítko „Vytvořit požadavek na převzetí“.
         #Zatrhněte políčko „Umožnit úpravy od správce“. Pokud pracujete pro
Odoo.
         #Dokončete popis a klikněte na tlačítko „Vytvořit požadavek na převzetí“.

      #Níže na stránce zkontrolujte stav sloučení a vyřešte případné problémy.
      #Jakmile bude váš :abbr:`PR (Pull Request)` připravený k sloučení, člen týmu Odoo
Pokud má recenzent nějaké otázky nebo připomínky, budou automaticky přiřazeny k přezkoumání.
Vložte je jako komentář a budete upozorněni e-mailem. Tyto komentáře musí být vyřešeny
aby se příspěvek mohl vyplatit.
      #Jakmile jsou vaše změny schváleny, recenzent je sloučí a ty se zobrazí na webu.
den.
