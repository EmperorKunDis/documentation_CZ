================
Schválit výdaje
================

V Odoo není možné schvalovat faktury jen tak někomu, ale pouze uživatelům s potřebnými právy (nebo
povolení) může. To znamená, že uživatel **musí** mít alespoň oprávnění „Schváleno týmem“.
Aplikace „Náklady“. Zaměstnanci s potřebnými právy mohou prohlížet výdajové zprávy, schvalovat nebo zamítat.
a poskytnout zpětnou vazbu díky integrovanému komunikačnímu nástroji.

Pro více informací se podívejte na dokumentaci práv k přístupu <applications/general/users>.
o správě uživatelů a jejich oprávnění.

Zobrazit výdajové zprávy
====================

Uživatelé, kteří mohou schvalovat výdajové zprávy, obvykle manažeři, snadno vidí všechny výdaje.
k nim mají přístupová práva. Přejděte na: „Nákladový účet --> Nákladové zprávy“, abyste se mohli podívat
dashboardu „Všechny zprávy“.

Seznam všech faktur s stavem buď :guilabel:`K předložení“, :guilabel:`Předložené“.
:guilabel:Schváleno“, „Předáno“ nebo „Dokončeno“ se zobrazí. Výdajové požadavky s tímto stavem
Výchozí je skrytý stav „Odmítnuto“.

.. obrázek: schvalit_výdaje/seznam_zpráv_o_výdajích.png
:align:center
:alt: Zprávy k ověření se nacházejí na stránce Zprávy k schválení.

Schválit výdajovou fakturu
=======================

Zprávy o výdajích lze schvalovat dvěma způsoby: :ref:`individuálně <expenses/individual>` nebo :ref:`ve
větší než náklady na jednoho uživatele.

.. důležité::
Schváleny mohou být pouze hlášení s stavem „Předloženo“.

Je doporučeno zobrazit pouze hlášení s označením „Odeslané“ zaškrtnutím políčka vedle
filtr „Předložené“ v levém sloupci pod záložkou „Stav“.

Pokud je zpráva **nepřijatelná**, tlačítko „Schválit zprávu“ **nefunguje**.
objeví se na stránce „Všechny zprávy“.

... výdaje/osobní:

Schválit jednotlivé zprávy
--------------------------

Pro schválení jednotlivého výkazu přejděte na: „Náklady aplikace - Výkazy nákladů“
Klikněte na konkrétní zprávu, abyste viděli formulář pro tuto zprávu.

Zde jsou představeny několik možností: „Schválit“, „Odmítnout“ a
:reset_to_draft:

Klikněte na tlačítko „Schválit“ k schválení zprávy.

..._náklady/více:

Schválit více zpráv
------------------------

Pro schválení více výdajových zpráv najednou přejděte nejprve do aplikace „Výdaje“:
Zobrazit výdajové zprávy - seznam všech výdajových zpráv. Vyberte požadované výdajové zprávy k schválení zaškrtnutím
Zaškrtněte políčko vedle každého hlášení schválené nebo zaškrtněte políčko vedle
Vyberte všechny zprávy v seznamu klepnutím na titulek sloupce „Zaměstnanec“.

Poté klikněte na tlačítko „Schválit zprávu“.

.. obrázek: schvalit-výdaje/schvalit-zprávu.png
:align:center
:alt: Schválit více zpráv zaškrtnutím políček vedle každé z nich.

.. tip::
Pro správce týmů je možné zobrazit všechny výdajové faktury pouze pro členy jejich týmu.

Pro toto klikněte na stránce „Všechny zprávy“ na ikonu „fa-caret-down“.
:guilabel:`(směrový šipek)“ vpravo od vyhledávací lišty a poté klikněte na „Moje tým“.
:icon:`fa-filter` :guilabel:`Filtry“

Tato funkce zobrazuje všechny reporty pouze pro tým manažera.

...... obrázek: schvalit-výdaje/moje-tým-filtr.png
:align:center
:alt: Vyberte filtr My Team.

Odmítnout výdajové hlášení
======================

Výdajové faktury mohou být zamítnuty pouze na jednotlivých výdajových fakturách a ne
:guilabel:`Všechny zprávy“ panelu. Chcete-li otevřít individuální výkaz nákladů, přejděte na
:menuselection:`Náklady aplikace --> Nákladové zprávy“, pak klikněte na konkrétní nákladovou zprávu
zobrazit zprávu.

Pokud je potřeba další informace (například chybějící faktura), sdělte všechny nezbytné údaje.
v poznámkovém bloku v hlášení. Na jednotlivé výdajové faktuře klikněte
Klikněte na tlačítko „Odeslat zprávu“ pro otevření okna s textem zprávy.

Napište zprávu, označte správné lidi a klikněte na tlačítko „Odeslat“
:guilabel:`Odeslat“. Zpráva je zveřejněna v chatu a označené osoby jsou upozorněny.
e-mail.

.. poznámka::
Jen lidé, kteří jsou „sledováni“ konkrétním příspěvkem, mohou být označeni v zprávě.
klikněte na ikonu :icon:`fa-user-o` :guilabel:`(uživatel)`
o výdajovém hlášení.

.... obrázek::approve_expenses/chatter.png
:align:center
:alt:Posílejte zprávy do chatu.

Zamítnout fakturu klikněte na tlačítko „Odmítnout“ a poté na „Odmítnout výdaje“.
zobrazí se okno s krátkým vysvětlením důvodu odmítnutí pod :guilabel:`DŮVOD K ODMÍTNUTÍ
V poli „Náklady“ klikněte na tlačítko „Odmítnout“.

.. obrázek: schvalit-výdaje/odmítnout-výdaj.png
:align:center
:alt:Posílejte zprávy v chatovacím okně.

Jakmile je vyúčtování zamítnuto, stav se změní na „Zamítnuto“ a jediný tlačítko
v levém horním rohu je: guilabel:"Zpět do návrhu".
