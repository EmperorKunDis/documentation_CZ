===================================================
Nainstalujte záplatu, která vypne platby faktur on-line
===================================================

Pokud jste nedávno provedli změnu v Odoo 16, můžete být upozorněni na to, že deaktivace :guilabel:`Faktura
Pokud chcete vypnout funkci bez odinstalování modulu, přejděte do nastavení „Online platba“ a deaktivujte ji.
odinstalovat moduly, postupujte podle následujících kroků pro instalaci modulu **Platba – Účet / Faktura
Online platba Patch**.

.. poznámka::
|Pokud je váš Odoo databáze vytvořena po modulu **Platba - Účet / Faktura online platby
Patch byl vydán, nemáte co dělat.
|Zkontrolujte, zda modul již není nainstalován. Přejděte do sekce „Aplikace“ a odstraňte filtr „Aplikace“.
a hledejte „účetní platba“. Pokud je modul **Platba – Účet/Faktura online platby
Patch je přítomen a označen jako nainstalovaný. Vaše databáze Odoo už je aktuální a vy
Mohou tuto funkci bez vedlejších účinků vypnout.

Aktualizujte Odoo na nejnovější verzi
=================================

Možnost vypnout nastavení „Online platba faktury“ bez vedlejších účinků
Dostupné prostřednictvím nového modulu Odoo; abyste jej mohli nainstalovat, musíte zajistit, že máte
Zdrojový kód Odoo je aktuální.

Pokud používáte Odoo na platformě Odoo.com nebo Odoo.sh, váš kód je již aktuální a můžete pokračovat
na další krok.

Pokud používáte Odoo s instalačním řešením v místě nebo prostřednictvím partnera, musíte aktualizovat svou instalaci.
podrobněji v dokumentaci na této stránce, nebo kontaktováním
Vaším integrujícím partnerem.

Aktualizovat seznam dostupných modulů
====================================

Nové moduly musí být objeveny vaším Odoo instancí, aby byly dostupné v nabídce **Aplikace**.

Pro to aktivujte režim vývojáře (:ref:`vývojářský režim <developer-mode>`), a přejděte do sekce „Aplikace“:
Aktualizovat seznam aplikací“. Přihlášení do programu vyžaduje potvrzení.

Nainstalujte modul Faktura online platba
===============================================

.. varování:
Nikdy byste neměli nainstalovat nové moduly do své produkční databáze bez předchozího testování v
duplikát nebo testovací prostředí. Pro zákazníky odoo.com lze vytvořit duplikát databáze
z stránky správy databáze. Pro uživatele Odoo.sh byste měli používat testovací nebo duplicitní
databáze. Pro uživatele v prostředí on-premises byste měli používat testovací prostředí – kontaktujte svého partnera
partnerovi pro další informace o tom, jak otestovat nový modul ve vašem konkrétním nastavení.

Modul by měl být nyní dostupný v nabídce „Aplikace“. Odstraňte filtr „Aplikace“ a
hledat „účetní platba“; modul: guilabel:„Platba – Účet / Faktura online platba“
měl být dostupný pro instalaci. Pokud nemůžete najít modul po aktualizaci seznamu
znamená, že zdrojový kód vašeho Odoo není aktuální; podívejte se na první bod této
stránka.

Jakmile modul nainstalujete, vypnutí funkce bude fungovat tak, jak má, a nebude po vás vyžadovat
Odinstalujte nainstalované aplikace nebo moduly.
