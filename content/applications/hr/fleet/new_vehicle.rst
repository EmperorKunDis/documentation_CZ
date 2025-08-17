===============
Přidávání vozidel
===============

Aplikace **Odoo Fleet** spravuje všechny vozidla a doprovodnou dokumentaci.
údržba vozidel a záznamy o řidičích.

Při otevření aplikace `Flotila` jsou všechny vozidla uspořádána v
Panelu „Dopravní prostředky“, který je výchozí panel. Každý dopravní prostředek je zobrazen v
odpovídající fázi kanbanu na základě jejího stavu. Výchozí fáze jsou:
„Přijato“, „Registrováno“ a „Zrušeno“.

... flotila/nastavení:

Nastavení
========

Před registrací vozidel si projděte dvě nastavení flotily, která přímo ovlivňují každodenní
provoz a zaměstnanecké výhody:

- :ref:`Datum ukončení smlouvy <fleet/end-contract>“ - zasílá emailem osobu odpovědnou za
určitý počet dní před vypršením smlouvy na vozidlo, aby se nepřehlédly obnovení nebo vrácení.
- :ref:`Nový požadavek na vozidlo <fleet/request>“ - (pouze lokalizace Belgického platového systému) blokuje zaměstnance
od požadavku nového firemního vozu přes konfigurátor mzdy, až po dostupnost vozidel
Už nyní přesahuje stanovený limit a pomáhá kontrolovat výdaje na dávky.

Pro přístup do nabídky nastavení přejděte na: menuselection: Fleet app --> Konfigurace --> Nastavení.

…flotilu/konec smlouvy:

Upozornění na konec smlouvy
-----------------------

V poli „Upozornění na konec smlouvy“ je uvedeno, kolik dní před koncem vozidla
v případě podezření by měla být odeslána výstraha. Odpovědné osoby (označované jako „odpovědné osoby“):
e-mail, který jim sděluje, že smlouva na vozidlo končí za určený počet dní.
tohoto pole.

.. obrázek: new_vehicle/fleet-settings.png
:alt: Nastavení aplikace Flotila.

..flotila/odpovědná osoba:

Odpovědné osoby
~~~~~~~~~~~~~~~~~~~

Odpovědnou osobu za smlouvu zjistíte v detailu smlouvy.
je uveden pod záložkou „Zodpovědná osoba“ v sekci „Informace o smlouvě“.
obdrží upozornění.

Chcete-li otevřít smlouvu z seznamu všech smluv, přejděte na:
Všechny smlouvy se zobrazí v seznamu. Klikněte na „Smlouva“, abyste otevřeli její detail.
sekci „Informace“ smlouvy a podívejte se do části „Odpovědná osoba“, abyste zjistili, kdo
obdrží upozornění na vypršení platnosti.

Individuální smlouva se také otevře z konkrétního vozidla po najetí na
Vyberte aplikaci „Flotila“ – „Flotila“ – „Flotila“ a klikněte na konkrétní vozidlo.
formulář, klikněte na tlačítko „Smlouvy“ v horní části stránky. Smlouva spojená
Společně s vozidlem se v seznamu objeví i jednotlivé smlouvy, které lze otevřít kliknutím na konkrétní kontrakt.
Ve smlouvě je uvedená „odpovědná“ osoba.

…flotila/žádost:

Nová žádost o vozidlo (Belgický platový účet - Flotila)
---------------------------------------------

Zadejte maximální velikost flotily, kterou lze dosáhnout pomocí průvodce platbami.
celkový počet dostupných vozidel (vozidla bez přiřazeného řidiče) je roven nebo nižší než tento
limit, mohou zaměstnanci požádat o nové firemní auto. Jakmile bude počet dostupných vozidel vyšší než
Možnost požadavku je skryta.

.. příklad::
Pokud je nastaven limit pro požadavek na nové vozidlo na 20 vozidel a v garáži je 25 vozidel
dostupné, zaměstnanci nemohou požádat o nové auto a musí si vybrat z 25 již k dispozici. Pokud
Pokud by bylo k dispozici jen deset aut, mohl by zaměstnanec požádat o nové vozidlo.

.. poznámka::
Tato nastavení se zobrazí pouze tehdy, pokud je nainstalován modul Belgian Payroll Fleet.
pro belgickou lokalizaci.

Přidat vozidlo
=============

Přidat nové vozidlo do flotily z panelu „Vozidla“ kliknutím na „Nový“.
v horním levém rohu tlačítko a poté se vám načte prázdný formulář vozidla. Následně postupujte k zadání vozidla
informace o vozidle.

.._flotila/nové vozidlo/vozidlo-typ:

Pole vozidla
===================

- :guilabel:`Model‘: Z rozevírací nabídky vyberte model vozidla. Jakmile je vybrán jeden z modelů,
Pokud se vám nezobrazí žádné další pole, zadejte název modelu a
Klikněte na buď „Vytvořit model“, nebo „Vytvořit a upravit…“ pro vytvoření nového
Vytvořte a upravte detaily modelu pomocí příkazu „fleet/add-model“.
- :licence:Vyplňte registrační značku vozidla.
- :guilabel:`Štítky“: Vyberte si z nabídky nebo vepište nový štítek. Neexistuje žádné omezení
na počtu vybraných štítků.

.. obrázek: nové_vozidlo/model.png
:alt: Nová vozidla s uvedenou částí modelu.

.. poznámka::
Model je jediným povinným polem na novém formuláři vozidla.
vybrané, další pole se zobrazí na vozidle a relevantní informace automaticky zaplní
pole aplikovaná na model. Pokud některé z polí nejsou viditelné, může to naznačovat, že
žádný model nebyl vybrán.

.. flotila / nové vozidlo / nový řidič:

Řidič
------

Tato část vozidla se týká osoby, která aktuálně řídí auto.
Plánuje se změna jezdce v budoucnu?

- :guilabel:Řidič: Vyberte řidiče vozidla z roletkového seznamu. Pokud je
nebyl uveden, pak vytvořte nový řidič a upravte podrobnosti o řidiči.
<flotila/nové vozidlo/přidat řidiče>.

.. důležité::
Řidič nemusí být zaměstnancem. Při vytváření nového řidiče se řidič přidá do
aplikaci Fleet, nikoli aplikaci Employees.

Pokud je nainstalovaná aplikace **Kontakty**, jsou tam uloženy také informace o řidiči.

- :guilabel:`Karta Mobilita“: Pokud vybraný řidič má kartu mobilita (např. plynovou kartu), je uvedena
na kartu zaměstnance v aplikaci **Zaměstnanci** se automaticky připíše číslo mobilní karty.
Pokud se v tomto poli nezobrazí žádná karta mobilitní, a přesto by měla být přidána, pak je potřeba
v záznamu o zaměstnanci v aplikaci **Zaměstnanci** (záložka „Hodnocení“).
- :guilabel:`Budoucí řidič“: Pokud je známý další řidič vozidla, vyberte dalšího řidiče
z nabídky. Nebo zadejte další řidiče a klikněte buď na „Vytvořit budoucí
„Řidič“ nebo „Vytvořit a upravit…“ k :ref:`vytvoření nového budoucího řidiče a úpravy
„podrobnosti o řidiči“ (fleet/new_vehicle/add-driver).

.. poznámka::
Pokud je pole vyplněno, na formuláři vozidla se objeví tlačítko „Nastavit nový řidič“.
Klikněte na tlačítko „Použít nový ovladač“ a změňte informace o ovladači.

- :guilabel:'Plán na změnu auta': Zaškrtněte tuto políčko, pokud je aktuální řidič již přesvědčený o tom, že se bude střídat.
do jiného vozidla, ať už čekají na objednané auto, nebo pouze dočasně využívají toto.
Odešli z firmy.
- :guilabel:`Datum přidělení vozidla“: Vyberte datum, kdy bude vozidlo k dispozici.
dalším řidičem. Pokud je pole nevyplněno, znamená to, že vozidlo je aktuálně k dispozici.
a může být přidělen jinému řidiči. Pokud je obsazené, vozidlo není k dispozici
další řidič do vybraného data.
- :guilabel:`Společnost“: Vyberte společnost z rozevírací nabídky. Toto pole se objeví pouze v
multifirmový databázový systém.

.. fleet/new_vehicle/add-driver:

Vytvořte nový ovladač
~~~~~~~~~~~~~~~~~~~

Pokud řidič již v systému není, nový řidič se nejprve konfiguruje a přidává do
databáze. Nový řidič lze přidat buď z :guilabel:`Řidičů“ nebo :guilabel:`Budoucích řidičů“.
políčka na formuláři vozidla (viz. odkaz „Forma nového vozidla <fleet/new_vehicle/vehicle-form>“).

Nejprve zadejte jméno nového řidiče do pole „Řidič“ nebo „Budoucí řidič“.
Klikněte na pole „Řidič“, pak klikněte na tlačítko „Vytvořit a upravit…“. Klikněte na „Vytvořit řidiče“ nebo
Při vyvolání formuláře záleží na tom, které pole jej vyvolalo.

Formulář „Vytvořit řidiče“ a formulář „Vytvořit budoucího řidiče“ jsou totožné a
ukládané v aplikaci **Kontakty**. Konfigurujte nový kontakt podle návodu „Nastavení nového kontaktu“
klikněte na „Uložit a zavřít“.

.. poznámka::
Podle instalovaných aplikací se mohou na záložce nebo v poli zobrazit různé záhlaví.
:guilabel:`Vytvořit řidiče“ a „Vytvořit budoucího řidiče“ formuláře.

.. flotila/nový vůz/obecné informace:

Vozidlo
-------

Tato část zachycuje klíčové fyzické detaily vozidla. Vybráním existujícího modelu se může vyplnit automaticky
některé pole.

Vyplňte následující pole na formuláři:

- :guilabel:`Kategorie vozidla“: Vyberte kategorii vozidla z dostupných
možností. Pokud je nainstalována aplikace Inventář, kategorie se vztahuje na jakýkoli konfigurovaný :doc:`přepínač
systém řízení
<../../Sklad a výroba/Skladování a přijímání/Konfigurace/Dodací služby>.
- :guilabel:`Datum objednání vozidla“: Pomocí kalendáře vyberte datum, kdy bylo vozidlo objednáno.
Sledování, jak dlouho jsou vozidla v provozu, může pomoci při rozhodování o
drahé opravy nebo pomáhají rozhodnout se o výměně vozidla.
- :guilabel:`Datum registrace“: Vyberte datum, kdy bylo vozidlo
je nutné zaregistrovat. Mnoho regionů vyžaduje správnou registraci, takže je důležité sledovat termíny registrací.
je důležité.
- :guilabel:`Datum ukončení smlouvy“: Vyberte datum vypovězení nájemní smlouvy
až dojde k vypršení platnosti nebo vozidlo přestane být součástí flotily (např. prodáno, registrační značka vrácena).
- :guilabel:`VIN“: Zadejte číslo karoserie do pole. Toto je známé v některých zemích
jako identifikační číslo vozidla (VIN). Každé vozidlo má svůj jedinečný identifikátor, takže
Pokud dojde k odcizení nebo nehodě, lze vozidlo identifikovat pomocí tohoto jedinečného čísla.
- :guilabel:`Poslední počet najetých kilometrů“: Zadejte poslední známý nájezd v číselném poli.
vpravo vedle pole s číslem vyberte, jestli je na odometru kilometrů nebo mil
:guilabel:`(km)` nebo míle :guilabel:`(mi)“. Sledování počtu ujetých kilometrů je při sledování vozidla velmi důležité.
určení hodnoty vozidla pro účely daně z přidané hodnoty a následného prodeje.
- :guilabel:`Flottenmanager“: Wählen Sie den Flottenmanager aus der Dropdown-Liste oder geben Sie einen neuen
manažer flotily a klikněte buď na tlačítko „Vytvořit“ nebo „Vytvořit a upravit“.
- :guilabel:`Lokalita“: Zadejte konkrétní lokaci, kde je vozidlo obvykle umístěno.
pole. V poli by mělo být jasně uvedeno, kde se vozidlo nachází, například „Hlavní garáž“ nebo
„Stavba 2 Parkoviště“. Toto je zásadní informace pro firmy s mnoha pobočkami, kde
Ve skladech jsou uloženy vozy.

.. obrázek: nové vozidlo/nový typ vozidla.png
:alt: Nová vozidla s vyznačenou částí daně z motorových vozidel.

Karta Informace o dani
------------

V závislosti na nastavení lokalizace databáze a dalších aplikací
nainstalované, mohou být na formuláři přítomné další pole.

Následující sekce jsou výchozí a zobrazují se pro všechna vozidla bez ohledu na jiné nainstalované.
aplikace nebo nastavení lokálizace.

Fiskální politika
~~~~~~~~~

- :guilabel:'Dani za výkon vozidla': Zadejte částku, která je zdaněna podle velikosti vozidla
motor. Toto je stanoveno místními daněmi a předpisy a liší se podle lokality.
Je vhodné si ověřit správnost této hodnoty u účetního oddělení.
- :guilabel:`Sazba neuznaných výdajů“: Konfigurujte data a procenta vozidla
náklady (palivo, údržba, opotřebení atd.), které **nemohou** být odečteny z příjmů společnosti.
daňově uznatelný příjem.

Smlouva
~~~~~~~~

- :guilabel:`První smluvní datum“: Vyberte datum prvního kontraktu vozidla.
kalendářový výběr. Obvykle se jedná o den, kdy je vozidlo zakoupeno nebo pronajato.
- :guilabel:`Cena v katalogu (včetně DPH)`: Zadejte hodnotu :abbr:`MSRP (Doporučená maloobchodní cena výrobce)
cena vozidla při jeho koupi nebo pronájmu.
- :guilabel:`Hodnota nákupu“: Zadejte cenu za nákup nebo původní hodnotu pronájmu.
vozidlo.
- :guilabel:`Zůstatková hodnota vozidla“: Zadejte aktuální hodnotu vozidla.

.. poznámka::
Hodnoty uvedené výše ovlivňují účetní oddělení. Doporučujeme se na něj obrátit.
účetní oddělení pro další informace a/nebo pomoc při těchto hodnotách.

.. obrázek: nové_vozidlo/nový_dopravní_daně.png
:alt: Nová vozidla s vyznačenou částí daně z motorových vozidel.

Modelová tabulka
---------

Pokud je pro nové vozidlo již v databázi zadán model, pak se použije
Sekce „Motor“ jsou vyplněny odpovídajícími informacemi. Pokud model není
už jsou v databázi a klikněte na záložku Model, kde je potřeba nastavit
nový vůz <flotila/přidat_vůz>.

Zkontrolujte informace v záložce „Model“ a ujistěte se, že jsou správné. Například barva
informace o vozidle nebo informace o tom, zda je návěs připojený, jsou příklady běžných informací, které mohou být
aktualizace.

Poznámkový záznam
--------

Zadejte do této sekce poznámky k vozidlu.

.. obrázek: nové_vozidlo/model-tab.png
:alt: Nová vozidla s vyznačenou částí daně z motorových vozidel.

.. viz též:
   - :doc:`../flotila/modely`
   - :doc:`../flotila/servis`
   - :doc:`../flotila/nehody`
