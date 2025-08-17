===============
Analýza průzkumu
===============

Po vytvoření dotazníků a jejich odeslání účastníkům je pouze otázkou času, než se objeví
Odpovědi začínají přicházet. Když ano, je důležité vědět, kde a jak s nimi pracovat.
aplikace Odoo *Průzkumy*.

Naštěstí Odoo nabízí mnoho způsobů zobrazení odpovědí na průzkumy, takže uživatelé mohou snadno přistupovat a
analyzovat odpovědi na dotazníky, jakmile jsou k dispozici.

Podívejte se na výsledky
===========

Po otevření aplikace „Průzkumy“ se na hlavním panelu zobrazí seznam všech průzkumů.
v databázi a k nim příslušné informace.

Výchozí nastavení každé průzkumnické linky zobrazuje jejich počet otázek a průměrnou odpověď.
Délka a kolik účastníků má zaregistrováno nebo dokončeno
průzkum.

Je zde také ukazatel procenta, kolik účastníků :guilabel:`Prošlo` (pokud je
*Požadovaný skóre (%)* bylo nastaveno, nebo kolik účastníků se stalo „Osvědčenými“ (pokud byl
Pokud je volba „Certifikace“ nastavena.

.. poznámka::
Chcete-li se dozvědět více o různých analytických prvcích, které najdete na panelu :guilabel:`Průzkumy`,
podívejte se na dokumentaci „Základy průzkumu“ v části „Vytvoření průzkumu“.

Na panelu „Průzkumy“ je vpravo od každé průzkumnické linky zobrazené ve výchozím nastavení
v seznamovém zobrazení je tlačítko „Zobrazit výsledky“.

.. obrázek: analýza/zobrazit výsledky tlačítko.png
:align:center
:alt:Tlačítko „Zobrazit výsledky“ na hlavním panelu aplikace Odoo Surveys.

Když je kliknut na tlačítko „Zobrazit výsledky“, otevře se nová záložka v prohlížeči, která odhaluje samostatný
stránka s výsledky dotazníku a odpověďmi na něj.
a několik filtračních políček nahoře.

.. obrázek: analýza/stránka s výsledky.png
:align:center
:alt:Typická stránka výsledků průzkumu, na kterou se dostanete kliknutím na „Zobrazit výsledky“ v přehledu průzkumů Odoo.

Na horní části stránky je odkaz „Upravit průzkum“, uprostřed modré hlavičky.
banner. Když uživatel klikne na něj, aplikace Odoo vrátí uživatele zpět do formuláře dotazníku pro daný průzkum.

Pod ním je název průzkumu a jeho popis, pokud byl do něj zadán.
dotazník.

Vpravo od titulku průzkumu jsou dva rozbalovací seznamy s různými filtračními možnostmi.
Které lze použít k personalizaci a segmentaci výsledků průzkumu různými způsoby.

První filtr je nastaven na výchozí možnost „Všechny průzkumy“, což znamená
Další výsledky ukazují odpovědi a výsledky všech dotazníků, bez ohledu na to, zda
byly dokončeny nebo ne.

Když se tento rozevírací seznam rozbalí, objeví se další možnost „Dotazníky dokončené“.

.. obrázek: analýza/všechny-dotazníky-vyber.png
:align:center
:alt:Výběr „Všechny průzkumy“ se otevře na stránce s výsledky aplikace Odoo Survey.

S otevřeným rozbalovacím seznamem se na pravé straně zobrazí číslo odpovídající každému filtru.
každé možnosti.

Vpravo od této nabídky filtrů je další nabídka filtrů.
které lze použít k dalšímu přizpůsobení výsledků zobrazených na této stránce.

Tento seznam je nastaven na možnost „Prošlo a neprošlo“ (výchozí hodnota).
ukazuje výsledky a odpovědi všech účastníků, kteří tuto konkrétní část zkoušky složili nebo neprospěli.
průzkum.

.. poznámka::
Toto druhé rozbalovací menu filtračních možností se zobrazí pouze v případě, že je analyzována právě tato anketa.
Pokud je nastavená možnost „Hodnocení“ nebo pokud je zapnutá funkce „Je certifikace“.

Když je kliknut na druhé rozbalovací nabídce filtrů, objeví se další dvě možnosti:
:guilabel:`Prošlo pouze“ a „Pouze neprošlo“.

.. obrázek: analýza/přijato-nepřijato-vyber.png
:align:center
:alt:Drobná lišta „Přijato/nepřijato“ na stránce s výsledky aplikace Odoo Survey.

Každá možnost by filtrovala výsledky níže tak, že zobrazovala pouze odpovědi účastníků, kteří splnili
výzkumu nebo těm, kteří výzkum neprospěli, případně.

Přímě pod dotazníkovým titulem je tlačítko „Tisk“. Když na něj kliknete, celý
Výsledkovou stránku lze vytisknout.

Sekce „Přehled výsledků“ je pod nadpisem průzkumu, rozbalovacími nabídkami filtrů a
a tlačítko „Tisk“.

.. obrázek: analýza/přehled výsledků.png
:align:center
:alt:Sekce „Přehled výsledků“ na stránce „Zobrazit výsledky“ v aplikaci Odoo Survey.

Tato část výsledkové stránky obsahuje stručný souhrn užitečných dat týkajících se průzkumu.
metriky pro rychlou analýzu.

Analýza otázky
-----------------

Přímo pod sekcí „Přehled výsledků“ je místo, kde jsou zobrazeny výsledky a odpovědi.
se nevyskytují.

.. poznámka::
Různé sekce průzkumu, pokud byly k dispozici, se zobrazily na horní části odpovídajících stránek.
otázky na výsledkové stránce, stejně jako pro lepší organizaci.

Každá otázka z průzkumu je zde uvedena spolu s podrobným rozborem a vizualizací.
způsobu, jakým se účastníci odpověděli, pod nadpisem „Přehled výsledků“.
část.

Každá otázka je zobrazena nad odpovídajícím výsledkem. Vlevo od otázky je
:guilabel:`👀 (oko)` ikona. Když ji kliknete, Odoo skryje vizuální a datově související výsledky
odpovědi. Když je otázka kliknutá znovu, její vizuální a datová odpověď se zobrazí znovu.

Vpravo dole jsou ukazatele, kde se dá sledovat, kolik účastníků
„Odpověděl“ a „Přeskočil“.

.. obrázek: analýza/neodpovězené indikátory.png
:align:center
:alt: Indikátory Odpověděl a Přeskočil na stránce s výsledky v aplikaci Odoo Survey.

Pokud otázka vyžadovala od účastníka vlastní odpověď bez možnosti výběru z několika nabízených variant.
od zadání konkrétního čísla nebo data, například. Indikátor také ukazuje
kolik uživatelů odpovědělo na otázku:guilabel:`Korektní'.

.. obrázek: analýza/správný indikátor.png
:align:center
:alt: Příklad správného indikátoru na stránce „Zobrazit výsledky“ v aplikaci Odoo Survey.

.. poznámka::
I když není správná odpověď na otázku tohoto typu konfigurována,
:guilabel:`Korektní“ indikátor stále zobrazuje, ale ukazuje nulu.

Tento problém by nastal u otázek založených na názorech, například „Kdy je vhodná doba pro další
Prodáváte?

Pokud je pro otázku s více možnostmi správná pouze jedna odpověď, pak jsou výsledky a odpovědi
Zobrazeno grafem „Koláč“. Správná odpověď je označena symbolem „✔️
(kontrolní značka) vedle správné odpovědi v legendě nad grafem.

.. obrázek: analýza/kruhové-grafo.png
:align:center
:alt: Klasická pizzová grafika se objevuje na stránce „Zobrazit výsledky“ v aplikaci Odoo Survey.

Pokud je pro daný typ otázky více správných odpovědí (nebo žádné),
otázka, tyto výsledky a odpovědi jsou reprezentovány grafem s názvem „Bar Graph“.

.. obrázek: analýza/bar-graph-results.png
:align:center
:alt: Typická grafická osa výsledků na stránce „Zobrazit výsledky“ v aplikaci Odoo Survey.

Každá otázka s výběrem možností má kartu „Graf“ a kartu „Data“.
Výchozí je záložka grafů.

Karta „Data“ zobrazuje všechny poskytnuté odpovědi na otázku.
„Výběr uživatele“ (s procenty a hlasy) spolu s „Skóre“ každého
option.

.. obrázek: analýza/datový tabulka.png
:align:center
:alt:Typické okno „Data“ na stránce „Zobrazit výsledky“ v aplikaci Odoo Survey.

Další typy otázek, ve kterých nebyly žádné odpovědi pro účastníka k výběru,
je karta „Nejčastější“ a karta „Všechna data“.

Karta „Nejčastější“ zobrazuje „Uživatelské odpovědi“, „Četnost“ a
a skóre (pokud je k dispozici).

.. obrázek:: analýza/nejčastější_tabulka.png
:align:center
:alt:Typické „Nejčastější“ záložka na stránce výsledků v aplikaci Odoo Survey.

Karta „Všechna data“ zobrazuje seznam všech odpovědí, které byly k danému dotazu zaslány.
otázka.

.. obrázek: analýza/všechna data tabulka.png
:align:center
:alt:Typické okno „Všechna data“ na stránce „Zobrazit výsledky“ v aplikaci Odoo Survey.

Pokud je otázka vyhledávána pro účastníky, aby zadali číselnou hodnotu jako odpověď
Indikátory „Maximum“, „Minimum“ a „Průměr“ se zobrazují v pravém dolním rohu
výsledkových tabulkách.

.. obrázek: analýza/max-min-avg-indikátor.png
:align:center


Ikona filtru je také přítomna buď vpravo od sloupce „Vlastní volba“
v záložce „Data“ nebo vpravo u řádku „Uživatelská odpověď“
Karta „Všechna data“.

.. obrázek: analýza/filtr-ikonka.png
:align:center
:alt: Běžný „Filtr“ na stránce s výsledky v aplikaci Odoo Surveys.

Když je kliknut na ikonu „filtr“, Odoo vrátí uživatele zpět na začátek výsledků.
s vybraným filtrem, který zobrazuje výsledky každé otázky pro účastníky, kteří odpovědi poslali.
konkrétní odpověď na konkrétní otázku.

.. obrázek: analýza/použitá filtrace.png
:align:center
:alt:Filtr aplikace Odoo Surveys, který se používá na stránce „Zobrazit výsledky“.

Proto je třeba zveřejnit zbývající výsledky pro účastníky, kteří na danou otázku odpověděli.
stejným způsobem. Chcete-li odstranit filtr a zobrazit všechny výsledky znovu, klikněte na „Odstranit
Všechny filtry nebo klikněte na ikonu „✖️“ (X) v filtračním poli nahoře na stránce s výsledky.

Účasti
==============

Pro zobrazení souhrnného seznamu výsledků účasti na konkrétním průzkumu přejděte na
Vyberte aplikaci „Průzkum“, vyberte požadovaný průzkum z seznamu a klikněte na
:guilabel:'Účasti' chytrý tlačítko na začátku dotazníku.

.. obrázek: analýza/participace-chytré-tlačítko.png
:align:center
:alt:Tlačítko „Participace“ v horní části dotazníku v aplikaci Odoo Survey.

Tím se zobrazí samostatná stránka „Účastníci“, která ukazuje účastníky pro tuto
konkrétní průzkum spolu s shromážděním relevantních informací týkajících se každého z nich.

.. obrázek: analýza/stránka účasti - jednotlivá anketa.png
:align:center
:alt:Stránka účastníků pro jednotlivý průzkum v aplikaci Odoo Surveys.

Zde mohou uživatelé zobrazit informace týkající se konkrétních účastníků, kteří daný průzkum absolvovali.
Pokud chtějí vidět podrobnější rozdělení svých odpovědí a reakcí, mohou
klikněte na kteroukoliv osobu a Odoo zobrazí samostatnou stránku s dotazníkem dané osoby.
podrobnosti a jejich odpovědi.

.. obrázek: analýza/stránka účastníka.png
:align:center
:alt: Podrobné informace o jednotlivém účastníkovi v aplikaci Odoo Surveys.

Pro zobrazení souhrnného seznamu všech účastníků každého průzkumu v databázi přejděte na
:menuvolba:„Průzkumy aplikace“ --> „Účasti“. Zde je zobrazen každý průzkum v databázi.
Výchozí seznam sestupně. U každého průzkumu je uveden počet respondentů v závorkách.

.. obrázek: analýza/účasti-stránka-všechny-průzkumy.png
:align:center
:alt:Stránka účasti pro všechny průzkumy v aplikaci Odoo Surveys.

Když se průzkum odstraní z tohoto seznamu, kliknutím na název průzkumu se zobrazí příslušný
účastníci a s nimi spojená data k danému šetření se zobrazují na stránce.

Stránka „Účasti“ lze také zobrazit v kartovém uspořádání.

.. obrázek: analýza/stránka s přehledem účastníků v kanbanu.png
:align:center
:alt:Stránka Účastníků v kanbanovém pohledu aplikace Odoo Survey.

.. viz též:
   - :doc:`vytvořit“
   - :doc:`skórování“
