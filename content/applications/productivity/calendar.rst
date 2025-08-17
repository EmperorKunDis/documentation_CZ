Zobrazit obsah

========
Kalendář
========

Odoo **Calendar** je aplikace pro plánování, která umožňuje uživatelům integrovat firemní procesy do
jednotná správa. Kalendář se integruje s ostatními aplikacemi v ekosystému Odoo.
umožňuje uživatelům naplánovat a uspořádat schůzky, naplánovat události, plánovat hodnocení zaměstnanců.
koordinovat projekty a mnoho dalšího - vše z jednoho místa.

Při otevření aplikace Kalendář se uživatelům zobrazí přehled jejich současných schůzek.
Vybraná možnost zobrazení se objeví jako „Dnes“, „Týden“, „Měsíc“ nebo
:guilabel:`Rok“ vybíráku. Vybíracím menu „Zobrazení“ si uživatelé mohou také zapnout nebo vypnout
Zakázat zobrazování víkendů.

.. obrázek: kalendář/kalendář-přehled.png
:alt: Přehled aplikace Kalendář.

..tip:
V závislosti na zvoleném nastavení lze uživatelům umožnit kliknout na :icon:`oi-arrow-left
:ikonka: „oi-arrow-right“ :guilabel:„(levý nebo pravý směr)“ tlačítka pro přepínání mezi dny, týdny a
atd., a přepnout zpět do dnešního dne pomocí tlačítka „Dnes“.

Synchronizujte kalendáře třetích stran
--------------------------

Uživatelé mohou synchronizovat Odoo s již existujícími kalendáři Outlook.
kalendářů Google (<calendar/google>), přejděte na
Kalendářová aplikace --> Konfigurace --> Nastavení. Zde zadejte
:guilabel:„ID klienta“ a „tajný klíč“. Existuje také možnost přerušení
synchronizaci zaškrtnutím políčka nebo automatizací synchronizace nezaškrtnutím políčka.

Jakmile jsou požadované konfigurace dokončeny, ujistěte se, že kliknutím na tlačítko „Uložit“ před pokračováním potvrdíte svou volbu.

Akce vytvořené ve sloučených kalendářích se automaticky zobrazují na všech integrovaných platformách.

.. viz též:
   - :doc:`Synchronizace kalendáře Outlook s Odoo <calendar/outlook>`
   - :doc:`Synchronizace kalendáře Google s Odoo <calendar/google>`

Vytvářejte aktivity z chatu
------------------------------

Vytvořte nové schůzky kdekoliv v Odoo prostřednictvím chatu u jednotlivého záznamu, jako
v kartě příležitosti nebo úkolu v aplikaci Projects.

Z rozhovoru klikněte na tlačítko „Aktivita“. V části „Plánování aktivity“
připojte se k němu pomocí okna s náhledem, vyberte požadovaný typ aktivity (viz guilabel:Activity Type), který zobrazí tlačítka.
v závislosti na činnosti.

Aktivita s jiným harmonogramem, např. schůzka nebo „Demonstration Call“, odkaz
do aplikace Kalendář. Vyberte jednu z těchto aktivit a připojte ji k aplikaci Kalendář, pak
Navigovat zpět do aplikace lze také pomocí tlačítka „Otevřít kalendář“ nebo
„Zadat a označit jako hotové“ nebo „Hotové a naplánovat“ k uzavření aktivity.
Nyní je třeba udržet otevřené okno „Aktivita“ a vytvořit další.

.. viz též:
:doc:`Zařazujte aktivity do Odoo <../essentials/activities>`

Zorganizujte událost
-------------

Abychom události přidali do kalendáře, otevřeme aplikaci Kalendář a klikneme na cíl
datum. V okně „Nový události“ klikněte na tlačítko „Přidat název“.

.. obrázek: kalendář/kalendář-plán-události.png
:alt:V kalendáři si zarezervujte časový úsek pro událost.

Datum cíle se automaticky vyplní do pole „Začátek“. Toto můžete změnit kliknutím
do sekce datumu a vyberte datum z kalendáře. Pro vícedenní akce vyberte konec
datum ve druhém poli a pak klikněte na tlačítko „Použít“.

Zaškrtněte políčko „Veškerý den“, pokud neexistuje konkrétní čas začátku nebo konce.

U událostí s konkrétním časem začátku a konce zrušte zaškrtnutí položky „Vše denně“.
umožnit výběr času. Pokud je zaškrtávací políčko „Veškerý den“ nezaškrtnuté, zobrazí se
pole Start.

Uživatel podepsaný na schůzce se automaticky zobrazí jako první účastník. Další :guilabel:`Účastníci` lze přidat
a vytvořené odsud.

Pro virtuální schůzky zkopírujte a vložte URL do pole uvedeného níže.
:guilabel:`URL videohovoru“ nebo klikněte na ikonu „+“ v seznamu schůzek Odoo.
odkaz.

Dále buď vytvořte událost kliknutím na tlačítko „Uložit a zavřít“, nebo vyberte možnost „Více“.
Možnost dále konfigurovat událost.

..tip:
Jakmile je událost vytvořena, uživatelé mohou kliknout přímo do virtuální schůzky z kalendáře.
události, která umožňuje přístup k dalšímu nastavení.

.. obrázek: kalendář/kalendář-nový-schůzky.png
:alt: Celá událost pro nový kalendářní záznam.

V poli :guilabel:`Popis` mohou uživatelé přidat další informace a podrobnosti o
schůzky.

Klikněte na „Více možností“ a přejděte do formuláře pro schůzku, který poskytuje další
konfigurace události:

- Délka schůzky: Zadejte délku schůzky v hodinách nebo přepněte
:guilabel:`Všechny dny“ přepínač.
- :guilabel:`Opakující se“: Zaškrtněte políčko pro vytvoření opakujícího se setkání. Jakmile je vybráno,
Otevírá nové pole:

  - :guilabel:`Časová zóna“: Vyberte časovou zónu, pro kterou je tento čas určený.
  - :guilabel:`Opakování“: vyberte opakující se období této schůzky.
Pokud byl vybrán opakovaný údaj, objeví se další pole, ve kterém uživatelé mohou zadat datum následujícího výskytu.
schůzku by se měla opakovat. Například pokud je vybrána volba „Měsíčně“ jako „Opakování“.
volba, v novém poli se objeví pole pro výběr dne v měsíci.
schůzky by se měly opakovat.
  - Do: guilabel:Počet opakování:" zvolte omezený počet opakování, který by měl
opakovat se, pak je datum ukončení (datum konce) v poli „Konec“ nebo pokud by měly být schůzky
recurring :label:`Nadobro`.
- :guilabel:`Štítky“: Přidejte štítky události, například „Zákaznický setkání“ nebo „Vnitrofiremní setkání“.
mohou být vyhledávány a filtrovány v aplikaci Kalendář při organizování více událostí.
- :guilabel:„Termíny“: Připojte existující nebo nové termíny. Ty lze konfigurovat prostřednictvím
:ref:`Tlačítko „Sdílet dostupnost“ <kalendář/sdílet-dostupnost>“ z hlavního **Kalendáře**
přístrojová deska.
- :guilabel:`Soukromí“: Přepínání mezi možnostmi zobrazení, které umožňují kontrolovat, kdo může sledovat událost.
- :label:„Pořadatel“: Toto je výchozí uživatelský účet v Odoo. Zvolte nového z
buď existující uživatelé nebo vytvořit nového uživatele.
- :guilabel:`Popis“: Přidejte další informace nebo podrobnosti o schůzce.
- :guilabel:`Poznámky“: Vyberte možnosti oznámení, které chcete odeslat účastníkům. Zvolte výchozí
upozornění nebo nastavit nové upomínky.

Spolupracujte s dostupností týmů
-----------------------------------

Při plánování události pro více uživatelů v aplikaci Kalendář označte zaškrtávací políčko
Pokud chcete zobrazit dostupnost členů týmu, vyberte vedle políčka „Účastníci“ možnost
ukázat nebo skrýt jednotlivé kalendáře uživatelům zobrazeným v seznamu.

.. obrázek:: kalendář/kalendář-účastníci.png
:alt: Pohled na sekci Účastníci v aplikaci Kalendář.

..._kalendář/sdílení dostupnosti:

Sdílené dostupnosti
--------------------

Na hlavní obrazovce aplikace Kalendář klikněte na tlačítko „Sdílení dostupnosti“ v horní části.
stránky. Poté klikněte a přetáhněte myší na volné časy a data v kalendáři, abyste je mohli přidat
jako možnosti v pozvánce.

..tip:
Chcete-li vymazat zvolený časový interval, přejeďte myší nad dostupnost a klikněte na ikonu „odpadkového koše“
:guilabel:`(směsný odpad)` ikonu.

.. poznámka::
V rámci funkce „Sdílené dostupnosti“ je možné vybírat pouze časy v
Zobrazení kalendáře na den.

Jakmile si vyberete dostupnost, klikněte na tlačítko „Otevřít“ s ikonou :icon:`fa-external-link` :guilabel:
Přejděte do příslušného termínu schůzky.

.. obrázek: kalendář/kalendář-schůzka-sdílení-disponibilní-čas.png
:alt:Zobrazení dostupnosti v aplikaci Kalendář.

Na rezervační formuláři je k dispozici několik konfiguračních možností:

V poli `Plánování` nastavte minimální hodinový interval, abyste zajistili potvrzení termínů.
určité množství času předem. Například nastavte hodnotu „01:00“, aby účastníci potvrdili svou účast
nejméně hodinu před domluvenou schůzkou.

V poli „Povolit zrušení“ nastavte maximální hodinový okamžik předem
Účastníci mohou své přihlášky zrušit.

Pole „Dostupnost“ umožňuje účastníkům rezervovat „Uživatele“.
Zdroje, jako jsou například konferenční místnosti nebo stoly. Po výběru uživatelů
Vyberte položku „Zdroje“ a zadejte požadovaného uživatele nebo zdroj do pole pod ním.

V poli „Zobrazovací panel“ je možné vybrat „Žádné obrázky“ nebo
Zobrazit obrázky související s vybraným uživatelem nebo zdrojem na stránce termínu.

Pokud byl v poli „Dostupnost“ vybrán záznam „Zdroje“, uživatelé mají
možnost: „Správa kapacity“.

Zatrhněte políčko, které omezuje maximální počet lidí, kteří mohou zdroj používat současně.

Pole :guilabel:`Metoda přiřazení` umožňuje určit pořadí, v jakém se účastníci objednávají na čas.
uživatel/zdroj:

- :guilabel:`Vyberte uživatele/zdroj, pak čas“
- :guilabel:`Vyberte čas, pak uživatele nebo zdroj“

Pokud je v poli „Dostupnost“ vybráno pole „Zdroje“, třetí možnost
je k dispozici, „Vyberte čas a automaticky přiřaďte“.

Pokud chcete, můžete nastavit následující záložky:

- :ref:`kalendář/plánování schůzek“
- :ref:`kalendář/možnosti termínu`
- :ref:`kalendář/termín-dotazů
- :ref:`kalendář/zprávy o termínech schůzek

Klikněte na tlačítko „Náhled“ a zobrazí se vám, jak bude odkaz na schůzku vypadat pro účastníky.

Jakmile jsou konfigurace dokončeny, klikněte na tlačítko „Sdílet“ pro vytvoření odkazu ke sdílení.
nebo klikněte na tlačítko „Publikovat“ a zveřejněte výběr termínu v propojeném Odoo.
webové stránky.

.._kalendář/rozvrh schůzek:

Kalendář
~~~~~~~~~~~~

V záložce „Rozvrh“ formuláře pro objednání je možné spravovat časové úseky.
a časové pásma obsadit jako první volná místa.

Přidat nový časový interval můžete stisknutím tlačítka „Přidat řádek“. Vyberte prázdné místo pod
V poli „Od“ vyberte a zadejte nový cílový datum a čas.
Opakujte pod novým prázdným místem :guilabel:`To` pro výběr a vložení nového cílového data
a času.

.._kalendář/možnosti termínu:

Karta Možnosti
~~~~~~~~~~~

Karta „Možnosti“ nabízí další konfigurace:

- :guilabel:`Webová stránka“: Uveďte, na které webové stránce bude tato pozvánka zveřejněna.
- :guilabel:`Časové pásmo“: Toto se vypne na časové pásmo společnosti vybrané v aplikaci „Nastavení“.
Chcete-li změnit časové pásmo, vyberte požadovanou možnost z roletky.
- :guilabel:`Lokalita“: Vyberte nebo vytvořte novou lokalitu z nabídky. Pokud je toto pole
Pokud je místnost prázdná, jedná se o on-line schůzku.
- Vyberte z „Odoo Diskuse“ nebo „Google Meet“.
zahrnout do pozvánky na schůzi odkaz na videokonferenci nebo nechat prázdné, aby se zabránilo
vytváření odkazu na schůzku.
- „Potvrzení ručně“: Zobrazuje se pouze v případě, že byla vybrána položka „Zdroje“.
:guilabel:`Dostupnost‘ pole. Zatrhněte zaškrtávací políčko a zadejte maximální procento
celkovou kapacitu vybraných zdrojů, což vyžaduje manuální potvrzení k dokončení
schůzku.
- „Předem zaplacená platba“: Zatrhněte políčko, pokud chcete požadovat od uživatelů platbu před potvrzením jejich
rezervace. Po zaškrtnutí se objeví odkaz na :icon:`oi-arrow-right` :guilabel:`Nastavení
Payment Provider, který umožňuje platby přes internet.
- „Omezení pracovní doby“: Pokud je vybrána volba „Uživatelé“,
:guilabel:`Dostupnost` pole, zaškrtněte políčko a omezte časové úseky pro schůzku na vybrané
:doc:`hodiny práce uživatelů <../hr/employees/new_employee>“.
- :guilabel:`Vytvářet příležitosti“: Když je tato volba vybrána, každý naplánovaný termín vytvoří
novou příležitost pro CRM.
- :guilabel:`Poznámky“: Přidejte nebo smažte upomínky v tomto poli. Vyberte prázdné místo
pro další možnosti.
- :guilabel:`Potvrzení e-mailu“: Zaškrtněte políčko, pokud chcete zaslat potvrzovací e-mail
přítomní na schůzce poté, co je schůze potvrzena. Vyberte si z e-mailových šablon nebo klikněte
:guilabel:`Hledat více ...“, pak :guilabel:`Nový“ pro vytvoření vlastního šablonového souboru.
- :guilabel:`E-mail s odhlášením“: Zaškrtněte políčko, pokud chcete zaslat e-mail s odhlášením.
účastníků, pokud se schůzka zruší. Vyberte si e-mailový vzor nebo klikněte
:guilabel:`Hledat více ...“, pak :guilabel:`Nový“ pro vytvoření vlastního šablonového souboru.
- :guilabel:`CC to`: Přidejte kontakty, které mají být informovány o aktualizacích schůzky do pole níže, ať už
Přítomní se účastní schůze.
- :guilabel:`Povolit hosty“: Zaškrtněte políčko, pokud chcete umožnit účastníkům pozvat hosty.

...kalendář/dotaz na termín:

Karta otázek
~~~~~~~~~~~~~

V záložce „Otázky“ přidejte otázky pro účastníka, který bude odpovídat při potvrzení své
schůzku. Klikněte na tlačítko „Přidat řádek“ pro konfiguraci „Otázky“. Pak vyberte
:guilabel:'Typ otázky', možná přidat odpověď s :guilabel:'Zástupným znakem' a vybrat, jestli je
Odpověď je vyžadována.

Chcete-li se naučit vytvářet komplexnější dotazníky, přejděte do aplikace **Správa dotazníků**
dokumentace o vytváření a konfiguraci otázek pro sběr dat
<../marketing/surveys/questions>.

... kalendář/zprávy o termínech:

Karta Zprávy
~~~~~~~~~~~~

V poli „Zpráva o zahájení“ v záložce „Zprávy“ přidejte další
informace, která se objevuje na pozvánce.

Informace přidávaná do pole „Další zpráva o potvrzení“ se objeví až po uskutečnění schůzky.
potvrzeno.

.. toctree::


kalendář/outlook
kalendář/google
