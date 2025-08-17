==================
Prodat vstupenky na akci
==================

Odoo Events poskytuje uživatelům možnost vytvářet vlastní vstupenky na akce (a ceny za ně)
v různých cenových relacích.

Díky tomu mohou prodávat vstupenky na akce dvěma způsoby: prostřednictvím standardních objednávek a
online prostřednictvím integrovaného webu.

Odoo také usnadňuje proces nákupu vstupenek, protože nabízí mnoho platebních možností.

..tip:
Chcete-li se dozvědět více o tom, jak vytvářet vlastní vstupenky (a cenové hladiny) pro události, podívejte se na
:ref:`vytváření událostí“ dokumentace.

Konfigurace
=============

Pro prodej vstupenek na akce prostřednictvím Odoo je třeba nejprve zapnout některé nastavení.

Nejprve přejděte na: „Aplikace událostí - Konfigurace - Nastavení“.
v sekci „Registrace“ jsou dvě různá nastavení: „Vstupenky“ a
:guilabel:`Online prodej vstupenek“.

Nastavení „Vstupenky“ umožňuje uživatelům prodávat vstupenky na události s běžnými prodejními objednávkami.

Nastavení „Online prodej vstupenek“ umožňuje uživatelům prodávat vstupenky na akce online prostřednictvím svých
integrovaný web Odoo.

Aby se aktivovala nastavení, zaškrtněte políčko vedle požadované funkce a klikněte
:guilabel:Uložit“ pro dokončení procesu.

.. poznámka::
Pokud tyto možnosti nejsou povoleny, bude k dispozici výchozí tlačítko „Registrovat“
návštěvníky interagovat a získat bezplatné registrace na akci.

.. obrázek:: sell_tickets/events-settings-tickets.png
:align:center
:alt: Zobrazení stránky nastavení pro události v Odoo.

S těmito nastaveními zapnutými vám Odoo automaticky vytvoří nový produktový typ s názvem „Vstupenka“.
která je dostupná na každém produktu. Odoo také vytváří tři produkty pro registraci účastníků akcí (s
Položka „Produkt“ nastavená na „Vstupenka na událost“) lze používat nebo upravovat pro vstupenky na akce.

.. důležité:
Při vytváření nového produktu pro registraci na akci musí být nastaven typ produktu na *Akce*.
Tiket na produktu v poli Forma, aby byl vybrán v sloupci Produkt pod
záložka „Vstupenky“ na formuláři akce.

.... obrázek: sell_tickets/events-tickets-registration-product.png
:synchronizace: střed
:alt: Pohled na událost s vyznačeným sloupcem produktů pod záložkou vstupenek v Odoo.

.. poznámka::
Každý akce s prodanými vstupenkami obsahuje tlačítko „Prodej“ se symbolem dolaru :icon:`fa-dollar`
vrcholu události, kde jsou přiděleny příslušné prodejní objednávky spojené s těmito prodeji vstupenek.
bude k dispozici.

.... obrázek: sell_tickets/events-sales-smartbutton.png
:synchronizace: střed
:alt: Pohled na formu události a tlačítko chytrého prodeje v aplikaci Odoo Events.

Kliknutím na ikonu „fa-dollar“ se zobrazí samostatná stránka s přehledem prodejů.
všechnu prodejní objednávku (standardní i on-line) související s prodanými vstupenkami na
konkrétní událost.

Prodávejte vstupenky na akce s aplikací Sales
=====================================

Pro prodej vstupenek s objednávkami začněte tím, že se přesunete do aplikace „Prodej“.
Poté klikněte na tlačítko „New“ pro otevření nového formuláře s nabídkou.

Po vyplnění horní části formuláře vhodnou informací o zákazníkovi klikněte
V záložce „Dodací lístky“ klikněte na tlačítko „Přidat produkt“. Poté v záložce „Produkt“
sloupec, vyberte (nebo vytvořte) produkt registrace na akci nakonfigurovaný s jeho :guilabel:`Produktovým
Typ nastavený na „Vstupenka“ v produktovém formuláři.

Jakmile je vybrán produkt pro registraci na akci, zobrazí se okno
se objevuje.

.. obrázek: sell_tickets/configure-event-popup.png
:align:center
:alt:Standardní okno „Nastavení události“, které se objeví při objednávce vstupenek na akci.

V okně „Nastavit událost“ vyberte událost, ke které se tento nákup vstupenek váže.
vztahující se k události v poli „Událost“ vyskakovacího menu. Pak v poli „Vstupenka na událost“
příkazové nabídce vyberte, jaké vstupenky chcete koupit.
Pozice, které byly pro danou událost konfigurovány.

Když jsou všechny požadované konfigurace dokončeny, klikněte na tlačítko „OK“. To uživatele vrátí
objednávka s produktem registrace na akci nyní přítomným v poli :guilabel:`Objednávka
Tabulka Line. Uživatel může pokračovat v potvrzení a uzavření prodeje podle obvyklého procesu.

..tip:
Chcete-li znovu otevřít okno „Nastavení události“, přejeďte kurzorem nad názvem produktu registrace na akci.
v záložce „Řádky objednávky“ a klikněte na ikonu „pravítko“ (pravítko).

Prodávejte vstupenky na akce přes aplikaci Webové stránky
==========================================

Když se návštěvník dostane na stránku registrace akce na webu, může kliknout na
Klikněte na tlačítko „Registrace“ pro nákup vstupenky na akci.

.. poznámka::
Pokud návštěvník není již na stránce registračního formuláře webu akce, kliknutím
:guilabel:"Registrace" v podmenu webu akce je přesměruje na správné místo.
stránce registrace. Zde mohou kliknout na tlačítko „Registrovat“ a zahájit proces vytvoření lístku.
nákupní proces.

Pokud jsou pro událost nastaveny různé cenové úrovně vstupenek, návštěvník je předložen
Pop-up okno „Vstupenky“.

.. obrázek: sell_tickets/tickets-popup.png
:align:center
:alt:Okno s registračními údaji, které se objeví na webu akce po kliknutí na tlačítko „Registrovat“.

Od zde si návštěvníci vyberou, jaký druh vstupenky by chtěli zakoupit, včetně počtu kusů.
pomocí numerického rozbalovacího seznamu k dispozici napravo od jejich požadovaných vstupenek.
návštěvník pak klikne na tlačítko „Registrovat“.

Poté se zobrazí okno „Účastníci“, které obsahuje všechny otázky, na které jste odpověděli.
Konfigurována v záložce „Otázky“ přihláškového formuláře pro tento konkrétní turnaj.

.. obrázek: sell_tickets/attendees-popup.png
:align:center
:alt:Pop-up okno, které se objeví na webu akce po kliknutí na tlačítko „OK“.

Pokud se kupují více vstupenek najednou, každá má své číslo.
registrační formulář s otázkami stejnými jako v předchozím registračním formuláři. Pokud je však nějaká otázka nakonfigurována
S nastavením „Položit jednou za objednávku“ se tato otázka ptá jen jednou – a **ne** každou
účastník objednávky v pořadí.

Po zadání všech potřebných informací může návštěvník kliknout na tlačítko „Pokračovat do platby“.
tlačítko. Kliknutím na něj se návštěvník dostane nejprve na stránku potvrzení o platbě, následovanou
Konfirmační stránka platby, kde mohou využít jakýkoliv z konfigurovaných způsobů platby.
do databáze pro dokončení objednávky.

Poté, co je nákup dokončen na přední straně webu, následuje objednávka prodeje.
je okamžitě přístupný v administraci databáze.

.. viz též:
:doc:`vytvářet události“
