======
Stáže
======

Fáze jsou používány k organizování procesu Helpdesku a sledování pokroku v případech. Fáze
jsou přizpůsobitelné a lze je přejmenovat tak, aby vyhovovaly potřebám každého týmu.

Vytvořte nebo upravte fáze
=======================

.. důležité:
:ref:`Rozvojový režim <developer-mode> musí být aktivován, abyste se dostali do nabídky stádií.
aktivovat režim vývojáře, přejděte do nastavení aplikace „Nastavení“ – „Obecné“ – „Vývojářské nástroje“.
„Nástroje“ a klikněte na „Zapnout vývojářský režim“.

Pro zobrazení nebo úpravu fází **Helpdesku** přejděte do: „Aplikace Helpdesk > Konfigurace“.
Stáže.

Výchozí seznam na stránce „Stadia“ zobrazuje stadia, která jsou aktuálně k dispozici.
Aplikace Helpdesk. Jsou seřazeny podle pořadí, v jakém se objevují v řešení.

Pro změnu pořadí fází klikněte na ikonu „OI-Draggable“ (přesunutelná).
vlevo od jména na jevišti a přetáhněte ji na požadované místo v seznamu.

.. obrázek: stages/stages-list-buttons.png
:alt:Pohled na stránku s pořadím etap, který zdůrazňuje tlačítka pro změnu pořadí etap.
se v seznamu objeví.

..tip:
změňte pořadí fází na kanbanovém výhledu toku práce týmu **Helpdesku**, přetahováním.
odstraňováním jednotlivých sloupců.

Pro vytvoření nové scény klikněte na tlačítko „Nový“ v horním levém rohu seznamu scén.
odhaluje prázdnou scénu.

Vyberte název pro novou fázi.

.. obrázek: stages/new-stage-details.png
:alt: Zobrazení stránky nastavení scény v Odoo Helpdesku.

Přidejte šablony e-mailů a SMS do fází
=====================================

Při přidání šablony e-mailu do fáze je automaticky odeslán přednastavený e-mail.
Zákazníkovi v okamžiku, kdy se jím prodaný lístek dostal na určité místo ve frontě. Podobně jako
:guilabel:`Šablona SMS“ vyvolá přednastavený textový SMS zprávu, která je odeslána zákazníkovi.

.. důležité:
Služba zasílání krátkých textových zpráv je :doc:`In-App Purchase (IAP) </applications/essentials/in_app_purchase/>`.
služba, která vyžaduje předplacené kredity pro svou funkci. Viz „FAQ ohledně cen SMS“.
Více informací naleznete na adrese <https://iap-services.odoo.com/iap/sms/pricing>.

Pro výběr existujícího šablony e-mailu vyberte ji z pole „Šablona e-mailu“. Po
Vyberte šablonu a klikněte na ikonku :icon:`oi-arrow-right` :guilabel:`(right arrow)` vpravo.
do pole pro úpravy vybraného šablony.

Pro vytvoření nového šablony z této formuláře klikněte na pole a zadejte název pro novou šablonu.
Vyberte možnost „Vytvořit a upravit“ z rozevírací nabídky, která se objeví, a vyplňte formulář.
podrobnosti.

Postupujte stejným způsobem při výběru, úpravě nebo vytváření šablony SMS.

.. obrázek: stages/sms-template.png
:alt: Zobrazení stránky nastavení šablony SMS v Odoo Helpdesku.

.. viz též:
:doc:`/aplikace/obecné/firmy/vzor-e-mailu“

Skládejte scénu
============

Základní stavy jsou v kanbanovém pohledu na karty dashboardu zobrazené.
Tikety (:menuselection:`Pomocná aplikace - Helpdesk app --> Tikety --> Můj tiket`) nebo :guilabel:`Všechny tikety“
(:menu_selection:"Pomocná aplikace -> Tikety -> Všechny tikety").

Lístky v neotevřené scéně jsou vidět v potrubí pod názvem scény a jsou považovány za
*otevřený*.

Stanice lze nakonfigurovat tak, aby byly složené v kartovém pohledu stránky s tikety.

Jména složených scén jsou stále viditelná, ale vstupenky na pódium skryté.

Pro skládání scénáře zaškrtněte políčko „Skládaný v kanbanu“ na kartě „Scény“.

.. varování:
Tikety, které dosáhnou fáze „zavřené“, jsou považovány za uzavřené. Zavřít tiket před dokončením práce
dokončení může vést k problémům s hlášením a komunikací. Toto nastavení by mělo být používáno
povoleny pro fáze, které jsou považovány za fázi uzavření.

Dočasně složit pódium
------------------------

V kanbanovém pohledu na průběh řešení lze fáze dočasně složit.

Zobrazte konkrétní týmovou frontu, když se přesunete na: „Aplikace Helpdesk“ a klikněte na
Kanban kartu týmu.

Zaškrtněte položku „Nastavení“ v horním rohu obrazovky a klikněte na ikonu
Klikněte na ikonu „Převodovka“ (gear), která se objeví, a vyberte možnost „Sklápění“.

.. obrázek: stages/fold-stage-kanban.png
:alt:Kanbanový pohled na stupeň podpory s vyznačenou možností dočasného skládání.

.. důležité:
Manuální skládání scénáře z pohledu Kanban je dočasné a **neuzavírá**
jeviště.

Přidělte fáze týmu
=======================

Vyberte možnost v poli „Týmy Helpdesku“ na formuláři „Etapy“.
Může být vybrána jedna týmová skupina, protože stejná fáze může být přiřazena více týmům.
