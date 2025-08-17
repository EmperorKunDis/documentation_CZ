Zobrazit obsah

=========
Recepce
=========

Aplikace **Odoo Frontdesk** poskytuje způsob, jak se návštěvníci mohou při příchodu do budovy zaregistrovat.
místo a informovat o svém příjezdu osobu, se kterou se setkají. Dále mohou požádat
Naplněný nápoj, který jim přinesou, zatímco čekají.

Tato aplikace je ideální pro firmy, které nemají na recepci zaměstnance.
nebo bez určeného prostoru pro čekání hostů a návštěvníků.

Konfigurace
=============

Prvním nastavením v aplikaci Frontdesk je stanice, následovaná nápojem.
volitelných nabídek.

.._recepce/stanice:

Stanice
--------

V aplikaci Frontdesk společnosti Odoo lze stanici chápat jako jakoukoliv lokalitu, kde se může někdo nacházet.
Přihlásit se a čekat na zaměstnance. To je obvykle nějaká forma čekárny, například recepce.
na stanici je stánek, kde se návštěvníci registrují.

Při instalaci aplikace Frontdesk je nutné alespoň jednu stanici konfigurovat.
Počet stanic, které lze vytvořit a nakonfigurovat, není omezen.

Pro vytvoření stanice přejděte do části „Aplikace pro front desk“ -> „Konfigurace“ -> „Stanice“.
Klikněte na položku „Nový“. Po kliknutí se zobrazí prázdná přední část.

Do formuláře zadejte následující informace:

- :guilabel:`Název pokladny“: zadejte název pro konkrétní místo pokladny. Tento by měl být krátký
a jednoznačné, například „Pokladna“ nebo „Hlavní haly“. Tento údaj je nutný k tomu, aby
vytvořit stanici.
- :guilabel:`Odpovědné osoby“: vyberte osobu (nebo osoby), které jsou upozorněny, když se návštěvník přihlásí
použitím konkrétního pokladního pultu. Můžete zadat více možností. Toto pole je povinné,
aby vytvořili stanici.
- :guilabel:URL kiosku: Toto pole se automaticky vyplní po uložení předpokladu, pokud je alespoň
V poli „Jméno recepce“ a „Odpovědné osoby“ musí být vyplněna pole. Chcete-li data uložit ručně, klikněte
:ikonu „fa-cloud-upload“ v horní části formuláře.

Jakmile je URL uloženo, vytvoří se v poli „Kiosková URL“ :guilabel:. Tato URL je jedním ze způsobů, jak
Při přístupu na recepční kiosk.

Chcete-li se do kiosku dostat, klikněte na tlačítko „Kopírovat“ v konci URL a přejděte na danou stránku.
URL v prohlížeči. Tato adresa otevře stránku přihlašovacího formuláře konkrétní stanice.

.....tip:
Chcete-li k formuláři přidat obrázek nebo fotografii, přejeďte kurzorem nad :guilabel:`(fotoaparát s plusem)`
ikona v pravém horním rohu formuláře, která odhalí ikonu „Peněženka“ (Edit).

Klikněte na ikonu :icon:`fa-pencil` :guilabel:`(Upravit)` pro otevření souborového manažera, který vám umožní navigovat do
obrázku nebo fotografie, pak klikněte na tlačítko „Otevřít“ a vyberte jej.

Vybraná fotografie stanice se zobrazuje jako pozadí pro stojan s informacemi o stanici.

Karta Možnosti
~~~~~~~~~~~

.. _frontdesk/host:

- :guilabel:`Vybraný host“: pokud návštěvník navštíví schůzku, tato možnost umožňuje návštěvníkovi
vybrat pořadatele schůzky ze seznamu předložených uživatelů a oznámit tuto skutečnost tomuto jednotlivci. Když je zapnuté
Pokud se zobrazí další pole, viz níže uvedené podrobnosti.
- :guilabel:`Přihlašování hostů“: pokud je požadována další informace při příjezdu hosta
zapnout tuto možnost a vybrat, které z následujících jsou potřebné:

  - :guilabel:`E-mailová adresa“: vyberte, zda je e-mailová adresa hosta :guilabel:`Povinná“.
:guilabel:`Volitelné“, nebo pokud informace nebyly vůbec požadovány (:guilabel:`Nic“).
  - :guilabel:`Telefon“: vyberte, zda je telefonní číslo hosta :guilabel:`Povinné“.
:guilabel:`Volitelné“, nebo pokud informace nebyly vůbec požadovány (:guilabel:`Nic“).
  - :guilabel:`Organizace“: vyberte, zda je organizace hosta :guilabel:`Povinná“,
:guilabel:`Volitelné“, nebo pokud informace nebyly vůbec požadovány (:guilabel:`Nic“).

- Vyberte barvu kiosku. Vyberte buď „Světlý“ nebo
:guilabel:"Tmavý". Vybraní "Světlý" zobrazí na terminálu šedou barvu.
Porovnejte s výběrem „Tma“, který zobrazuje tmavě šedý a černý pozadí.
- :guilabel:'Samoobslužný příjezd': zapněte tuto možnost, abyste na kiosku zobrazili čárový kód pro odbavení. Čárový
Kód umožňuje hostům přihlásit se do hotelu pomocí mobilního zařízení místo použití pokladny.
Je vhodný pro rušné kiosky s více hosty, kteří se mohou přihlásit kdykoliv.
- :guilabel:"Nabídnout nápoje": zapněte tuto možnost, pokud chcete hostům nabídnout nápoj při příchodu. Pokud
Pokud je povolena, je nutné konfigurovat nabízené nápoje, viz
výběr nápojů, který se objeví po zapnutí této možnosti. Jakmile budete mít všechny nápoje vybrány,
Vyberte si každý nápoj, který chcete nabídnout, pomocí rozbalovacího seznamu.

.. poznámka::
Následující možnosti jsou viditelné pouze v záložce „Možnosti“ pokud je vybrána volba „Vyberte hostitele“.
volba „<frontdesk/host>“ je povolena.

- :guilabel:'Oznámit e-mailem': zapněte tuto možnost, abyste měli odesláno e-mail na osobu, kterou host
přihlášení. Když je povoleno, objeví se pod ním pole pro e-mailový vzor.
výchozí šablona e-mailu „Přední pokladna“ vybrána.

Chcete-li změnit výchozí e-mailový vzor, klikněte na rozbalovací nabídku v poli „Vzor e-mailu“.
Vyberte pole a poté vyberte jiný e-mailový šablonu.

Pro změnu aktuálně vybraného šablony klikněte na ikonku :icon:`oi-arrow-right` :guilabel:`(Interní
na konci řádku a upravte šablonu.
- :guilabel:`Oznámit SMS“: zapněte tuto možnost, abyste měli odesláno SMS (textové) zprávy na osobu
hosta při příjezdu. Když je zapnutá, objeví se pod ní pole pro :guilabel:`SMS šablonu`.
s výchozím šablonou „SMS Frontdesk“.

Chcete-li změnit výchozí šablonu pro SMS, klikněte na rozbalovací nabídku v poli „Šablona SMS“.
pole a vyberte jiný vzor SMS zprávy.

Pro změnu aktuálně vybraného šablony klikněte na ikonku :icon:`oi-arrow-right` :guilabel:`(Interní
linka) na konci řádku a provést libovolné úpravy obsahu šablony.
SMS zpráva může mít maximálně 242 znaků, což se vejde do čtyř SMS zpráv (UNICODE).
- „Upozornit pomocí diskuze“: tato volba je vypnuta výchozím nastavením, pokud je aktivována možnost „Upozornit pomocí e-mailu“.
Vybraná možnost „Výběr“ je aktivní. Tato volba otevře okno zprávy aplikace „Diskuse“.
osobu, se kterou host přijel na ubytování.

Když je zapnuto, zobrazí se výchozí zpráva pro osobu, kterou navštěvuje host.
Aplikace **musí být nainstalována**, aby tato možnost fungovala.

.. poznámka::
*Diskutovat* je nainstalován výchozí nastavením při vytváření databáze Odoo a nepočítá se do
účetní. Pokud aplikace *Discuss* nebyla záměrně odinstalována,
:guilabel:`Upozornění pomocí diskuze“ funguje.

.. příklad::
Výchozí formát zprávy pro možnost „Oznámit pomocí diskuze“ je: (Přístupová stanice).
Check-in: (Jméno hosta) (Telefonní číslo hosta) (Název organizace) se setká s (Jméno zaměstnance).

Příkladem, jak by se to mohlo objevit v zprávě **Discuss**, je například: „Hlavní halová recepce: John Doe
(555-555-5555) (Inc. Odoo) se setkat s Markem Demem.

.. obrázek: frontdesk/station-form.png
:alt:Přístupový bod s vyplněnou frontdeskovou stanicí.

Karta vedlejší zprávy
~~~~~~~~~~~~~~~~

Zadejte libovolný text, který se má zobrazit na pokladně stanice po příchodu hosta, například
vítací pozdrav nebo případně potřebné instrukce. Text se zobrazí na potvrzující stránce,
v pravé části obrazovky po dokončení procesu přijetí hosta.

.. _recepce/nápoje:

Nápoje
------

Po vytvoření stanice je další krok konfigurace nápojů, které chcete návštěvníkům nabídnout.

.. poznámka::
Tento krok není nutný ani požadovaný pro správnou funkci aplikace Frontdesk a je možné jej přeskočit.
Pokud hostům nabízíte nápoje, musí být konfigurována.

Chcete-li přidat možnost nápoje, přejděte na: `Frontdesk app --> Konfigurace --> Nápoje`.
Klikněte na tlačítko „Nový“. To odhalí prázdnou kartu pro konfiguraci nápoje.

Do příslušného políčka v záznamní kartě nápoje zadejte následující údaje:

- :guilabel:`Název nápoje“: Zadejte název možnosti nápoje do tohoto pole. Toto pole je povinné.
- :guilabel:`Osoby, které mají být informovány“: vyberte z nabídky v tomto poli osobu, která má být informována
zde vyberete nápoj, který si přejete objednat. Do pole můžete zadat více lidí. Toto pole je povinné.
- :guilabel:'Sekvence': do pole zadejte číselnou hodnotu, která ukazuje na místo v seznamu nápoje
možností, čím nižší je číslo, tím výše se nápoj v seznamu objeví.
se objeví. Například zadáním čísla 1 by se nápoj umístil na první pozici v seznamu a
Vyskytují se na začátku sekvence.

.. tip::
Chcete-li přidat obrázek k nápoji, přejeďte kurzorem nad ikonou „(fotoaparát s plusem)“
v pravém horním rohu formuláře, aby se zobrazila ikona „Pen“ (Upravit).

Klikněte na ikonu „Penál“ (Edit) pro otevření souborového manažera, přejděte do složky s dokumenty
Pokud chcete vybrat požadované obrázky nebo fotografie, klikněte na tlačítko „Otevřít“ a vyberte je.

Nyní vybraný obrázek zobrazuje pole pro obrázek a nastavuje jej jako obrázek nápoje.

.. obrázek:: frontdesk/espresso.png
:alt:Forma na kávu s vyplněnými informacemi pro espresso.

Dashboard stanice
=================

.. tip::
Chcete-li přidat obrázek k nápoji, přejeďte kurzorem nad ikonou „(fotoaparát s plusem)“
v pravém horním rohu formuláře, aby se zobrazila ikona „Pen“ (Upravit).

Klikněte na ikonu „Penál“ (Edit) pro otevření souborového manažera, přejděte do složky s dokumenty
Pokud chcete vybrat požadované obrázky nebo fotografie, klikněte na tlačítko „Otevřít“ a vyberte je.

Nyní vybraný obrázek zobrazuje pole pro obrázek a nastavuje jej jako obrázek nápoje.

.. _recepce/pult:

Prodejní místo
===========

Nastavte každý stánek pro použití po konfiguraci různých stanic. Doporučuje se používat
přidělený zařízení pro každou recepci, například tablet.

Dostanete se na stánek jedním ze dvou způsobů:

- Přejděte na hlavní panel aplikace Frontdesk a klikněte na tlačítko „Otevřená recepce“.
tlačítko na požadované stanici. Kiosek se otevře v novém záložce prohlížeče.
- Přejděte na: „Nástroje pro správu fronty --> Konfigurace --> Stanice“ a klikněte na
pak klikněte na tlačítko „kopírovat“ v konci adresy „kiosku“.
a vložte odkaz do nového okna prohlížeče.

.. důležité::
Jednou je přístup na recepci získán buď pomocí tlačítka „Otevřená recepce“ nebo
:guilabel:"URL kiosku", uživatel je automaticky odhlášen z databáze na konkrétním
zařízení.

To je bezpečnostní opatření, které má zabránit neoprávněnému přístupu do databáze.

Reportáž
=========

Aplikace **Frontdesk** má k dispozici dva reporty: „Návštěvníci“ a
:guilabel:`Nápoje“.

Pro přístup k jednomu z těchto reportů přejděte na: „Frontdesk app -> Reporting“.
zobrazit rozbalovací nabídku s možnostmi: „Návštěvníci“ a „Nápoje“.

Zpráva o návštěvnosti zobrazuje počet návštěvníků za měsíc v aktuálním roce.
:guilabel:`Nápoje“ ukazuje, kolik celkových požadavků bylo na každý nápoj.

Stejně jako u všech reportů v Odoo lze filtry a skupiny upravit tak, aby zobrazovaly jiné metriky.

.. viz též:
   - :doc:`frontdesk/visitors

..toctree::


frontdesk/návštěvníci
