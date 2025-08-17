
... _odoosh-advanced-submodules:

==========
Podmoduly
==========

Přehled
========

„Součástí“ git repozitáře („submodule“) umožňuje integraci jiných projektů v Gitu
do kódu bez nutnosti kopírovat celý jejich kód.

Skutečně můžete vlastní moduly záviset na modulech z jiných repozitářů.
Co se týče Odoa, tato funkce vám umožňuje přidávat moduly z jiných repozitářů do větví vašeho repozitáře.
Přidávání těchto závislostí do vašeho větvení pomocí podmodulů usnadňuje nasazení vašeho kódu a serverů.
Můžete si tedy klonovat své vlastní repozitáře a zároveň i repozitáře přidané jako podmoduly, současně.

Kromě toho můžete vybrat větvení repozitáře přidané jako podsložka.
A máte kontrolu nad tím, jaké revize chcete.
Je na vás, zda chcete připnout podmodul k určité verzi a kdy chcete aktualizovat
na novější verzi.

V Odoo.sh vám moduly podsložek umožňují používat a záviset na modulech dostupných v jiných repozitářích.
Platforma zjistí, že jste do svých větví přidali moduly prostřednictvím podmodulů.
a přidat je do cesty pro doplňky automaticky, abyste je mohli nainstalovat do svých databází.

Pokud do svých větví přidáte soukromé repozitáře jako podmoduly
Potřebujete nakonfigurovat klíč nasazení ve svém projektu Odoo.sh a v nastavení repozitáře.
Pokud ne, pak Odoo.sh nebude moci stahovat soubory.
Postup je podrobně popsán v kapitole „Nastavení > Moduly <odoosh-gettingstarted-settings-modules>“.

Přidání podmodulu
==================

S Odoo.sh (jednoduché)
---------------------

.. varování::
Aktuálně není možné přidat soukromé repozitáře tímto způsobem. I tak však
to udělejte takhle:

Ve větvích projektu na Odoo.sh vyberte větve, do kterých chcete přidat podmoduly.

V pravém horním rohu klikněte na tlačítko „Modul“ a poté na „Spustit“.

.. obrázek: submodules/advanced-submodules-button.png


Zobrazí se dialog s formulářem. Do políček zadejte následující údaje:

* URL repozitáře: SSH URL adresa repozitáře.
* Branch: Vyberte pobočku, kterou chcete použít.
* Cesta: Složka, do které chcete tento podmodul větve přidat.

.. obrázek: submodules/advanced-submodules-dialog.png


Na GitHubu získáte URL repozitáře pomocí tlačítka „Zkopírovat nebo stáhnout“ u repozitáře. Ujistěte se, že používáte „SSH“.

.. obrázek: submodules/advanced-submodules-github-sshurl.png


... _odoosh-advanced-submodules-withgit:

S Gitem (pokročilé)
-------------------

V terminálu v adresáři složky, kde je vaše repozitář zkopírován.
Zkontrolujte větvení, ve kterém chcete přidat podmodul:

... kódový blok:: bash

$ git checkout <branch>

Pak přidejte podmodul pomocí příkazu níže:

... kódový blok:: bash

$ git submodule add -b <branch> <git@yourprovider.com>:<uživatelské jméno>/<název repozitáře>.git <cesta>

Vyměnit

* *git@yourprovider.com:username/repository.git* jako SSH URL adresu repozitáře, který chcete přidat jako podsložku
* *<větve>* pro větve, které chcete použít v nadřazeném repozitáři.
* *<path>* do složky, kam chcete tento podsložkový modul přidat.

Zavolej a přidej své změny:

... kódový blok:: bash

$ git commit -a a git push -u <remote> <branch>

Vyměnit

* <vzdálené> repozitářem, na který chcete své změny poslat. Pro běžný Git je to repozitář *origin*.
* <větve> větví, na které chcete své změny přidat.
Nejspíš jste v prvním kroku použili příkaz :code:`git checkout`.

Můžete si přečíst dokumentaci „git-scm.com <https://git-scm.com/book/en/v2/Git-Tools-Submodules>“
pro více informací o podsložkách Git.
Příkladem je například aktualizace podsložek na nejnovější verzi.
Můžete sledovat kapitolu.
„Stahování změn z upstreamu <https://git-scm.com/book/en/v2/Git-Tools-Submodules#_pulling_in_upstream_changes_from_the_submodule_remote>“.

Ignorujte moduly
==============

Pokud přidáváte repozitář s mnoha moduly, můžete chtít některé z nich ignorovat v případě, že existují
které se nainstalují automaticky. Chcete-li tak učinit, můžete před svou složkou s podmoduly přidat znak :code:“.“. Platforma
Ignorujte tuto složku a ručně vyberte své moduly vytvořením symbolických odkazů na ně z jiné složky.
