
.._nastavení/aktualizace:

==============
Opravy chyb
==============

Úvod
============

Aby mohl využívat nejnovější vylepšení, opravy zabezpečení, opravy chyb a
výkonnostní nárůst, může být třeba aktualizovat instalaci Odoo v určitých intervalech.

Tento průvodce se používá pouze v případě, že používáte Odoo na svém vlastním serveru.
Pokud používáte některou z řešení Odoo v cloudu, aktualizace se provádějí automaticky za Vás.

Terminologie okolo aktualizací softwaru je často matoucí, takže zde jsou některé základní
definice:

Aktualizace (instalace Odoo)
Označuje proces získání nejnovější verze zdrojového kódu.
Váš aktuální balíček Odoo. Například aktualizace vašeho Odoo Enterprise 13.0 na
nejnovější verze.
Toto nezpůsobuje žádné změny v obsahu databáze Odoo.
může být odstraněna opětovným nainstalováním předchozí verze zdrojového kódu.

Aktualizace (databáze Odoo)
Označuje složitý proces zpracování dat, kdy struktura a obsah vašich
Databáze je trvale upravena, aby byla kompatibilní s novou verzí Odoo.
Tato operace je nevratná a obvykle se provádí pomocí Odoo.
„služba upgradu databáze“ (<https://upgrade.odoo.com>), kterou si můžete vybrat, když se rozhodnete
přejít na novější verzi Odoo.
Historicky se tento proces také nazýval „migrací“, protože zahrnuje přesun dat
v rámci databáze, i když může být na stejném fyzickém místě
Po upgradu.

Tato stránka popisuje typické kroky potřebné k aktualizaci instalačního balíku Odoo na nejnovější verzi.
verze. Pokud chcete získat další informace o aktualizaci databáze, navštivte
„Stránka upgrade Odoo <https://upgrade.odoo.com>“ místo toho.


V kostce
=============

Aktualizace Odoo je provedena jednoduše přeinstalováním nejnovější verze vaší Odoo.
Edice na vrcholu vaší aktuální instalace. Tímto způsobem budou vaše data uložena bez jakýchkoliv změn.
pokud neodinstalujete PostgreSQL (databázový motor, který je součástí Odoo).

Hlavním zdrojem pro aktualizaci je logicky náš návod na instalaci:
A tím vysvětluje běžné způsoby instalace.

Aktualizace je také nejlépe prováděna osobou, která původně systém Odoo nasadila.
Protože postup je velmi podobný.

.. poznámka: Vždy doporučujeme stáhnout nejnovější verzi Odoa.
použitím ručního aplikování oprav, jako jsou bezpečnostní opravy, které přicházejí s bezpečnostním
Advokátní poradenství.
Patche jsou hlavně určeny pro instalace, které jsou silně upravené, nebo pro
technici, kteří dávají přednost aplikaci minimálních změn dočasně při testování
kompletní aktualizace.


Krok 1: Stáhněte si aktualizovanou verzi Odoo
========================================

Střední stahovací stránka je https://www.odoo.com/page/download. Pokud uvidíte odkaz „Koupit“,
Stáhněte si Odoo Enterprise, ujistěte se, že jste přihlášeni na Odoo.com stejným přihlašovacím údajem jako je
spojené s vaším předplatným Odoo Enterprise.

Alternativně můžete použít jedinečný odkaz ke stažení, který byl součástí vaší licence Odoo Enterprise.
potvrzení o nákupu e-mailem.

.. poznámka: Stahování aktualizované verze není nutné, pokud jste aplikaci instalovali přes GitHub (viz níže).


Krok 2: Vytvořte zálohu databáze
======================================

Aktualizační postup je poměrně bezpečný a neměl by měnit vaše data. Nicméně vždy je lepší být obezřetný
celkový zálohovaný soubor databáze před provedením jakéhokoliv změn na vaší instalaci a uložit jej někam.
na jiném počítači.

Pokud jste databázi nesmazali, můžete ji obnovit pomocí nástroje pro správu databází (viz :ref:`tady <security>`, proč byste to měli udělat).
můžete si stáhnout zálohu své databáze (odkaz na konci obrazovky výběru databáze).
databáze. Pokud jste ji deaktivovali, použijte stejný postup jako pro vaše obvyklé zálohy.


Krok 3: Nainstalujte aktualizovanou verzi
===================================

Vyberte metodu, která odpovídá vaší aktuální instalaci:


Instalace balíčků
-------------------

Pokud jste nainstalovali Odoo pomocí instalačního balíčku stáhnutého z našich webových stránek (doporučený způsob),
Aktualizace je velmi jednoduchá.
Stačí si stáhnout instalační balíček odpovídající vašemu systému (viz krok 1).
a nainstalujte si ho na svůj server. Aktualizace se provádějí každý den a obsahují nejnovější opravy zabezpečení.
Většinou stačí pouze dvojitým kliknutím na balík nainstalovat jej nad současnou instalaci.
Po instalaci balíčku je nutné ukončit službu Odoo nebo restartovat server.
A máte hotovo.

Zdroj instalace (tarbal)
------------------------

Pokud jste původně nainstalovali Odoo s verzí „tarball“ (archiv zdrojového kódu), máte
nahradit instalační adresář novější verzí. Nejprve stáhnout nejnovější balíček ve formátu tar
z webu www.odoo.com. Aktualizují se denně a obsahují nejnovější opravy zabezpečení (viz krok 1).
Po stažení balíčku jej rozbalte do dočasného umístění na vašem serveru.

Získáte složku označenou verzí zdrojového kódu, například „odoo-13.0+e.20190719“.
obsahuje složku „odoo.egg-info“ a skutečný zdrojový kód složky „odoo“ (pro verzi Odoo 10
a později „openerp“ pro starší verze.
Můžete ignorovat složku odoo.egg-info. Najděte složku, kde je nainstalována vaše současná instalace
a nahraďte ji složkou „odoo“ nebo „openerp“, která je v archivu, který právě extrahujete.

Ujistěte se, že máte stejnou strukturu složek, například novou složku „addons“, která je součástí zdrojového kódu
a měla by se dostat přesně na stejnou cestu, jaká byla předtím. Dále je třeba sledovat konfiguraci
soubory, které jste možná ručně zkopírovali nebo upravili v původním adresáři a přesuňte je do
nový adresář.
Poté znovu spusťte službu Odoo nebo restartujte stroj a je hotovo.

Zdroj instalace (GitHub)
-----------------------

Pokud jste původně nainstalovali Odoo s plným klonem repozitářů na GitHubu,
Proces aktualizace vyžaduje stáhnout nejnovější zdrojový kód pomocí git.
Přejděte do adresáře každé repozitáře (hlavní repozitář Odoo a Enterprise
úložiště) a spusťte následující příkazy:

git fetch
git rebase --autostash

Poslední příkaz může narazit na konflikt zdrojového kódu, pokud jste místně upravili zdrojový kód Odoo.
Chybová hláška vám poskytne seznam souborů s konflikty a budete je muset vyřešit.
konflikty ručně, tj. editací a rozhodnutím o tom, která část kódu zůstane.

Alternativně můžete jednoduše vyhodit všechny konfliktní změny a vrátit se k oficiální verzi.
verzi můžete použít následující příkaz:

git reset --hard

Konečně obnovte službu Odoo nebo resetujte počítač a měli byste být hotovi.


Docker
------

Prosím, podívejte se na dokumentaci „Docker image“ (<https://hub.docker.com/_/odoo/>_).
Specifické pokyny k aktualizaci.
