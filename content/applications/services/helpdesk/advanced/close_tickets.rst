=============
Zavřít lístky
=============

Po dokončení práce na lístku v aplikaci Helpdesk existuje několik způsobů, jak může být
zavřené. Ruční uzavírání vyřešených případů udržuje frontu v aktuálním stavu, zatímco automatické uzavírání
neaktivní lístky zabraňují zbytečným problémům s blokováním. Umožňuje zákazníkům uzavřít své vlastní lístky
snižuje zmatky kolem otázky, jestli je problém vyřešený nebo ne. To vede k
kapacitu pro podporu týmů a vyšší spokojenost zákazníků.

Zavřít vyřešené případy ručně
=============================

Jakmile se pracuje na lístku, je převeden do další fáze v potrubí. Když je problém vyřešen
je vyřešen, je přesunut do fáze *zavřeno*, což znamená, že je problém vyřešen.

Pro skládání scény přejděte na panel „Pomoc“ a klikněte na tým, abyste otevřeli
trubka. Zvolte hlavu fáze a pak klikněte na ikonu „nástroje“
je umístěn v pravém horním rohu sloupce Kanban dané fáze.

.. obrázek: close_tickets/uzavření-úpravy-stádia-nástroje.png
:alt: Pohled na plochu pomocného panelu s vyznačeným ikonou ozubeného kola a možností upravit stav.

.. varování:
Kliknutím na ikonu ozubeného kola se zobrazí možnost „Sbalit“ scénu. Tato volba scénu skládá.
stáhnout na chvíli zobrazení KanaBanu, což **neznamená uzavření problémů v tiketech**
přechodná, neustále nenafukovací střídačku. Pokud je potřeba střídačku nafouknout, tak se vstupenky
Pokud je případ uzavřen, pokračujte dále podle níže uvedených kroků.

Vyberte položku z nabídky „Upravit“. To otevře nastavení scény. Zatrhněte
zaškrtávací políčko s názvem „Složené v Kanbanu“ a pak „Uložit a zavřít“, abyste potvrdili
změn. Nyní jsou lístky uzavřeny, jakmile dosáhnou této fáze složení.

.. obrázek:: close_tickets/closing-folded-setting.png
:alt:Stránka s nastavením scény.

Automaticky uzavírat neaktivní požadavky
====================================

Tikety, které nebyly aktivní po určitou dobu, mohou být automaticky uzavřeny. V tomto případě
Jsou přesunuty na skládací pódium.

Přejděte na stránku nastavení týmu kliknutím na: Menu seznamu: Pomocníci --> Konfigurace --> Pomocníci
V sekci „Týmy“ aktivujte „Automatické uzavírání“.

Pokud je v zobrazení Kanban složená pouze jedna fáze týmu, je výchozím výběrem
Pole „Přesun na stupeň“. Pokud tým má více složených stupňů, je zobrazen
První v řadě je výchozí hodnota pro tento prvek. Pokud není žádný stupeň složený, výchozí volba je
poslední část potrubí.

Pole „Po dnech nečinnosti“ má výchozí hodnotu 7, ale lze ji upravit podle potřeby.

.. varování:
pole „Po dnech nečinnosti“ **nebere v potaz pracovní kalendář
při sledování doby, po kterou je lístek neaktivní.

Pokud by měly být použity jen některé fáze pro sledování dnů nečinnosti, mohou být přidány do
Do pole „Ve fázích“.

Příklad:
Týmová řešení jsou vytvářena ve třech fázích:

   - „Nový“
   - „Ve vývoji“
   - „Zpětná vazba od zákazníků“
   - „Zavřeno“

Tikety mohou zůstat v :guilabel:`Stadiu zpětné vazby zákazníků“, protože jakmile je problém vyřešený,
Zákazníci nemusí reagovat okamžitě. V takovém případě lze tikety automaticky uzavřít.
Pokud však jde o lístky v :guilabel:`New“ a :guilabel:`In Progress“, mohou zůstat neaktivní.
z důvodu problémů s přidělením nebo zátěží. Zavření těchto požadavků automaticky by vedlo k problémům
nebylo vyřešeno.

Proto by byly nastaveny takto:\:

   - :guilabel:`Automatické uzavření“: *zatrženo*
   - :guilabel:`Přesun na stupeň“: „Vyřešeno“
   - :guilabel:`Po 7 dnech nečinnosti“
   - :guilabel:`Ve fázích“: „Zpětná vazba od zákazníků“

.. obrázek:: close_tickets/closing-automatic-settings-example.png
:alt: Příklad nastavení automatického zavírání.

Umožněte zákazníkům uzavřít vlastní požadavky
==========================================

Povolení nastavení „Zavření zákazníkem“ umožňuje zákazníkům zavírat vlastní požadavky.
Když se rozhodnou, že jejich problém je vyřešený.

Začněte tím, že se přesunete na: `Helpdesk --> Konfigurace --> Týmy helpdesku` a vyberte
týmu. Na stránce nastavení týmu přejděte do sekce „Samoobsluha“ a zaškrtněte
zaškrtávací políčko pro:guilabel:"Zavření zákazníkem".

.. obrázek:: close_tickets/uzavření-na-zadání-klienta.png
:alt:Nastavení uzavření případu v Odoo Helpdesku.

Po zapnutí nastavení zavření lístku je k dispozici tlačítko „Zavřít lístek“.
zákazníci, když si prohlíží své lístky skrze zákaznický portál.

.. obrázek: close_tickets/closing-customer-view.png
:alt:Zákaznický pohled na uzavření lístku v Odoo Helpdesku.

.. poznámka::
Zákazníci si mohou zobrazit své vstupenky kliknutím na odkaz „Zobrazit vstupenku“
obdržíte e-mailem. Odkaz je součástí šablony „Potvrzení o přijetí žádosti“, která
je přidán do první fáze týmu automaticky. Tento odkaz nevyžaduje, aby zákazník měl
přístup do portálu, kde si mohou prohlédnout nebo odpovědět na své stížnosti.

Klienti s přístupem k portálu :doc:`<../../../general/users/portal>` mohou své údaje zobrazit.
vstupenky pod položkou „Můj účet“ --> „Vstupenky“.
