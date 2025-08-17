==================================
Využijte aktivity pro obchodní týmy
==================================

Aktivita je následná činnost spojená s záznamem v databázi Odoo. Aktivitu lze naplánovat
na jakékoli stránce databáze obsahující chatovací vlákno, kanbanový pohled, seznam nebo aktivity
pohled na aplikaci.

.. obrázek: využít_aktivity/aktivita-výhled.png
:align:center
:alt:Stručný pohled na aktivity pro kontakty a příležitosti v databázi Odoo.

Plánované aktivity pro leady a příležitosti.

Druhy aktivit
==============

Seznam přednastavených typů aktivit je k dispozici v aplikaci *CRM*. Seznam dostupných
Vyberte typy aktivit, přejděte na: `CRM aplikace --> Konfigurace --> Typy aktivit`.

.. poznámka::
Další typy aktivit jsou k dispozici v databázi a lze je využít prostřednictvím
různé aplikace. Chcete-li zobrazit kompletní seznam typů aktivit, přejděte na
:volba menu „Nastavení“, pak se posuňte do části „Diskuse“ a klikněte
:guilabel:`Druhy aktivit“.

Přednastavené typy aktivit pro aplikaci CRM jsou následující:

 - :guilabel:`E-mail“: připomínka pro chatovatele, aby prodavač poslal e-mail.
 - :guilabel:`Zavolat“: otevře odkaz na kalendář, kde obchodník může naplánovat čas pro telefonický hovor.
kontakt.
 - :guilabel:„Schůzka“: otevře kalendářový odkaz, kde může obchodník naplánovat čas pro setkání
schůzka s kontaktem.
 - :guilabel:"Co dělat": přidává obecný úkol do chatu.
 - :guilabel:`Nahrát dokument“: přidá odkaz na aktivitu, kde je možné nahrát externí dokument.
nahraný. Pozor, že aplikace „Dokumenty“ není pro využití této aktivity typu nutná.

.. poznámka::
Pokud jsou nainstalovány další aplikace, například Sales nebo Accounting, existují jiné typy aktivit.
jsou k dispozici v aplikaci CRM*.

..._crm/create-new-activity-type:

Vytvořte nový typ aktivity
--------------------------

Pro vytvoření nového typu aktivity klikněte na tlačítko „Nový“ v pravém horním rohu stránky.
forma.

Na začátek si vyberte jméno pro nový typ aktivity na horní části formuláře.

Nastavení činnosti
~~~~~~~~~~~~~~~~~

Akce
******

Záložka Akce určuje účel aktivity. Některé akce vyvolávají konkrétní chování
Po plánování aktivity.

- Pokud je vybrána možnost „Nahrát dokument“, přidá se přímo do
plánovaná aktivita v chatu.
- Pokud je vybrána volba „Telefon“ nebo „Schůzka“, uživatelé mají možnost otevřít
jejich kalendář, aby si mohli naplánovat čas pro tuto aktivitu.
- Pokud je vybrána možnost „Podpis požadavku“, do plánované aktivity se přidá odkaz.
chvilkové mluvení, které otevře okno s žádostí o podpis.

.. obrázek: využít_aktivity/akční pole.png
:align:center
:alt:Nastavení aktivity pro nový typ aktivity se zaměřením na pole Akce.

.. poznámka::
Akce dostupné pro výběr typu aktivity se liší podle aplikací, které jsou v současnosti k dispozici.
nainstalován do databáze.

Výchozí uživatel
************

Při plánování této aktivity automaticky přiřadit tuto aktivitu konkrétnímu uživateli.
Vyberte jméno z rozevíracího seznamu „Uživatelské jméno“. Pokud je pole nevyplněné,
aktivita je přiřazena uživateli, který aktivitu vytvoří.

Výchozí souhrn
***************

Pokud chcete zahrnout poznámky při vytváření této aktivity, vložte je do pole :guilabel:`Výchozí
Pole „Shrnutí“.

.. poznámka::
Informace v polích „Výchozí uživatel“ a „Popis výchozího souboru“
Je však možné je změnit před vytvořením aktivity.
plánované nebo uložené.

Další aktivita
~~~~~~~~~~~~~

Nabídnout automaticky novou aktivitu po označení aktivity jako dokončené.
Musí být nastaven parametr „Zapínání typu“.

Navrhněte další činnost
*********************

V poli „Typ řetězce“ vyberte možnost „Doporučit další činnost“. Po provedení této akce
pole pod ním se změní na: „Navrhnout“. Klikněte na pole „Navrhnout“
vybrat jakékoliv aktivity, které doporučí jako následné úkoly pro tento typ aktivity.

.. obrázek: využít_aktivity/další_aktivita.png
:align:center
:alt:Součást nového formuláře pro nový typ aktivity v části Další činnosti.

V poli „Rozvrh“ vyberte výchozí termín pro tyto aktivity.
Nastavte si požadovaný počet dnů, týdnů nebo měsíců. Pak
rozhodnout, zda by mělo nastat po datu dokončení nebo po předchozí aktivitě
termín.

Toto pole „Rozvrh“ může být změněno před plánováním aktivity.

Po dokončení všech konfigurací klikněte na tlačítko „Uložit“.

.. poznámka::
Pokud je typ řetězce nastaven na „Doporučit další činnost“ a
Pokud je v poli :guilabel:`Suggest` uvedeno nějaké činnosti, doporučení jsou zobrazena uživatelům.
pro další kroky.

.... obrázek:: využít_aktivity/navrhnout_další_aktivitu.png
:synchronizace: střed
:alt:Pop-up s rozvrhem aktivit, který se zaměřuje na doporučené aktivity.

Spustit další aktivitu
*********************

Pokud nastavíte typ řetězce na „Spouštění další aktivity“, okamžitě se spustí
další činnost, jakmile bude dokončena předchozí.

Pokud je vybrána možnost „Spouštění další aktivity“ v poli „Typ řetězce“, pole
pod ním změna na: guilabel: Trigger. Z nabídky pole guilabel: Trigger vyberte
aktivita, která by měla být spuštěna poté, co byla dokončena aktivity.

V poli „Rozvrh“ vyberte výchozí termín pro tyto aktivity.
Nastavte si požadovaný počet dnů, týdnů nebo měsíců. Pak
rozhodnout, zda by mělo nastat po datu dokončení nebo po předchozí aktivitě
termín.

Toto pole „Rozvrh“ může být změněno před plánováním aktivity.

Po dokončení všech konfigurací klikněte na tlačítko „Uložit“.

.. poznámka::
Pokud je typ aktivity nastaven na „Spouštění další aktivity“,
označení aktivity jako „Dokončeno“ spouští další aktivitu v seznamu.
:guilabel:`Způsob spouštění“ pole.

Sledování aktivit
=================

Aby byl potrubí aktuální s nejaktuálnějším pohledem na stav aktivit, jakmile
Když se s kontaktem pracuje, měla by být spojená aktivita označena jako „Dokončeno“. Tím zajistíte, že
Aktivita může být naplánována podle potřeby. Také zabraňuje zanášení potrubí nepotřebnými
předchozí činnosti.

Pipeline je nejúčinnější, pokud je aktuální a přesný v souvislosti s interakcemi, které jsou
sledování.

..._crm/aktivity:

Plány činnosti
==============

*Plány aktivit* jsou přednastavené sekvence aktivit. Když je spustíte,
aktivita v sekvenci je automaticky naplánována.

Pro vytvoření nového plánu přejděte na: „CRM aplikace -> Konfigurace -> Plán aktivit“.
Klikněte na „Nový“ v horním levém rohu stránky, abyste otevřeli prázdnou formu „Plány prodeje“.

Do pole „Název plánu“ zadejte název nového plánu. Do pole „Aktivita“ zadejte činnosti, které chcete v plánu uvést.
Vytvořte záložku „Vytvořit“ a klikněte na „Přidat činnost“, abyste přidali novou aktivitu.

Vyberte typ aktivity z roletky. Klikněte na :guilabel:`Hledat více`, abyste viděli
úplný seznam dostupných typů aktivit nebo vytvořit nový:ref:`
<crm/vytvorit-novy-tip-aktivity>.

Dále v poli „Shrnutí“ zadejte podrobnosti o specifikách aktivity.
včetně pokynů pro obchodníka nebo informací, které jsou potřebné po ukončení činnosti.
Obsah tohoto pole je součástí plánované aktivity a může být později upraven.

V poli „Přidělení“ vyberte jednu z následujících možností:

 - :guilabel:`Ptejte se při spuštění“: aktivity jsou přiřazeny uživateli, když je plán naplánován.
 - :guilabel:`Výchozí uživatel“: vždy je přiřazena konkrétnímu uživateli.

Pokud je vybrána položka „Výchozí uživatel“ v poli „Přiřazení“, zvolte uživatele v
:guilabel:Přiřazeno k

..tip:
Plány aktivit mohou obsahovat aktivity, které jsou přiřazeny výchozím uživatelům a uživatelům přiřazeným v
spuštění plánu.

.... obrázek:: využít_aktivity/vytvořit_plán_akce.png
:synchronizace: střed
:alt:Formulář plánu s naplánovanými aktivitami.

Dále nastavte časovou osu pro aktivity. Aktivity mohou být naplánované na předcházející nebo následující den.
datum plánu nebo po něm. Použijte pole „Intervál“ a „Jednotky“, abyste nastavili
termínu pro tuto aktivitu. Nakonec v poli „Spouštěč“ vyberte, zda je aktivita
Mělo by se stát před nebo po plánovaném datu.

Příklad:
Vytváří se plán aktivit pro zpracování vysoké prioritní poptávky. Konkrétně tyto poptávky by měly být
Kontaktovali jsme je rychle s tím, že schůzka byla naplánovaná do dvou dnů od prvního kontaktu.
Konfigurováno následujícími aktivitami:

   - E-mail dva dny **předem** plánovaným datem
   - Schůzka nula dní před plánovaným datem
   - Třetí citaci udělejte tři dny po plánovaném datu
   - Nahrát dokument tři dny po plánovaném datu
   - Další krok pět dní po plánovaném datu

Tímto se stanoví datum plánu jako termín k dokončení úkolů, což je cílem plánu.
V den schůzky je čas na kontaktování zákazníka a přípravu na setkání.
Datum je prodejce dostatečný čas na vytvoření nabídky, nahrání dokumentu a následné sledování.

Tyto kroky opakujte pro každou aktivitu zahrnutou v plánu.

Zahájit aktivizační plán
-----------------------

Pro spuštění plánu aktivit pro příležitost v CRM aplikaci přejděte na:
Kanbanová karta příležitosti, která umožňuje otevření.

V pravém horním rohu chatu klikněte na „Aktivita“ a otevřete „Rozvrh“.
Pop-up okno s aktivitou.

V poli „Plán“ vyberte požadovaný plán činnosti, který chcete spustit. To vytvoří
:guilabel:`Přehled plánu“, který uvádí aktivity zahrnuté v plánu. Vyberte si :guilabel:`Plán
Datum vyberte v kalendáři. To aktualizuje pole „Shrnutí plánu“ s termíny podle
intervaly nastavené v plánu aktivit.

Vyberte uživatele v poli „Přiřazeno“ (viz obrázek). Tento uživatel je přiřazen k jakémukoli aktivitě
V plánu byly nakonfigurovány s :guilabel:`Poptat při spouštění“ v poli :guilabel:`Přiřazení“.

.. obrázek: využít_aktivity/plán_aktivit.png
:align:center
:alt:Popis okna s aktivitou v plánu.

Klikněte na položku „Rozvrh“.

Podrobnosti plánu jsou přidány do hovoru a k každé aktivitě.

.. obrázek:: využít aktivity/aktivita plán chatu.png
:align:center
:alt:Diskusní vlákno příležitosti v CRM s aktivním plánem.

.. viz též:
 - :doc:`Aktivita </aplikace/základní/aktivita>`
