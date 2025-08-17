===========
Oddělení
===========

Všichni zaměstnanci v aplikaci **Zaměstnanci** patří do konkrétních oddělení ve společnosti.

..._zaměstnance/vytvořit-oddělení:

Vytvořit nové oddělení
======================

Pro vytvoření nového oddělení přejděte na: „Aplikace zaměstnanci --> Oddělení“, pak klikněte na
Klikněte na tlačítko „Nový“ v pravém horním rohu, abyste odhalili prázdnou formu oddělení.
podle informací z úředního tiskopisu:

- :guilabel:`Název oddělení`: zadejte název oddělení.
- :guilabel:`Manažer oddělení“: z roletkového menu vyberte manažera oddělení.
- Pokud je nový útvar umístěn v rámci jiného útvaru (je součástí)
Vyberte rodičovský oddělení pomocí vyhledávacího pole.
- :guilabel:`Společnost“: z roletkového menu vyberte společnost, ke které se oddělení řadí.
Tento pozemek se objevuje pouze v databázi více společností.
- :guilabel:`Barva“: vyberte barvu pro oddělení. Kliknutím na barevný box zobrazíte všechny
možnosti barev. Klikněte na barvu, kterou chcete vybrat.
- :guilabel:`Šablony hodnocení“: z rozevírací nabídky vyberte šablonu pro hodnocení
pro všechny hodnocení zaměstnanců v daném oddělení. Pokud chcete provést nové hodnocení, zadejte jméno
pro hodnocení, pak klikněte na tlačítko „Vytvořit a upravit ...“ a upravte nový formulář hodnocení.
Toto pole se zobrazí pouze v případě, že je nainstalována aplikace **Ocenění**.
- :guilabel:„Odhadová šetření“: z rozevírací nabídky vyberte výchozí průzkum pro použití
oddělení při žádosti o zpětnou vazbu od zaměstnanců daného oddělení. Výchozí možnosti jsou
:guilabel:`Formulář pro vyjádření zaměstnance“, :guilabel:`Zpětná vazba 360 stupňů“ a :guilabel:`Formulář hodnocení zaměstnance“.
Toto pole se zobrazí pouze tehdy, pokud je nainstalována aplikace „Ocenění“ a je zapnutá funkce 360 stupňů zpětné vazby.
volba je v nastavení povolena.

Po vyplnění formuláře klikněte na ikonu „Cloud Upload“
ručně uložit změny. Po uložení se zobrazí graf „Organizace oddělení“:
vpravo nahoře na kartě oddělení, která ukazuje, kde se oddělení v organizaci nachází.

.. obrázek: oddeleni/oddeleni-vzor.png
:alt: Úsek s vyplněnými všemi poli.

.. poznámka::
Formulář se ukládá automaticky při zadávání dat. Výstupní graf „Organizace oddělení“ je však
se nezobrazí, dokud není formulář ručně uložen. Pokud není formulář uložen,
:guilabel:`Organizační schéma oddělení“ je viditelné při otevření karty oddělení.
:guilabel:`Dashboard oddělení`.

.. viz též:
:doc:`../hodnocení“

Dashboardy oddělení
=====================

Pro zobrazení aktuálně nakonfigurovaných oddělení přejděte na:
Oddělení. Všechna oddělení se zobrazují v kanbanovém pohledu a jsou řazena abecedně.

Výchozí pohled pro panelu „Oddělení“ je :ref:`Kanban
<zaměstnanci/oddělení-kanban>. Výpis oddělení lze zobrazit ještě dvěma dalšími způsoby:
:ref:`seznamový pohled <zaměstnanci/oddělení-výpis> a hierarchický pohled
<zaměstnanci/organizační struktura>.

.. obrázek:: oddeleni/oddeleni.png
:alt: Zobrazení přehledu oddělení s kartami všech oddělení v zobrazení Kanban.

.._zaměstnanci/oddělení-kanban:

Kanbanový pohled
-----------

Každý oddělení má svou vlastní kartu Kanban na hlavním panelu „Oddělení“. Každá
Karta oddělení zobrazuje následující informace, pokud jsou k dispozici:

- :label_guid:Jméno oddělení: název oddělení.
- :guilabel:`Manažer`: jméno a obrázek manažera oddělení.
- :guilabel:`Společnost“: společnost, ke které patří oddělení, včetně ikony umístění.
- :guilabel:`Zaměstnanci“: počet zaměstnanců v oddělení.
- :guilabel:`Ocenění zaměstnanců“: počet ocenění zaměstnanců v oddělení.
- :guilabel:'Žádosti o volno': počet nezaplacených žádostí o dovolenou pro zaměstnance
oddělení:před schválením (viz časový odstup/správa časového odstupu). Toto se zobrazuje pouze tehdy, pokud
Jde o žádosti o schválení.
- :guilabel:`Požadavky na přidělení pracovních míst“: počet nepotvrzených žádostí o přidělení pracovního místa pro zaměstnance
oddělení:ref:`připravené k schválení <čas dovolených/správa přidělení>“. Toto se zobrazí pouze v případě, že
Jde o žádosti o schválení.
- :guilabel:`Noví uchazeči“: počet :ref:`nových uchazečů o pozici <vyhledávání/nové>
v rámci oddělení. Tento seznam se objeví pouze v případě, že jsou nové žádosti.
- :guilabel:`Zprávy o výdajích“: počet zaměstnanců v oddělení s :doc:`otevřenými výdaji
výkazů k schválení (<../../finance/expenses/approve_expenses>). Tato možnost se objeví pouze v případě, že jsou
jakékoli nezaplacené faktury, které čekají na schválení.
- :guilabel:`Nepřítomnost“: počet zaměstnanců s povolenou nepřítomností na aktuální den.
- Barva: vybraná barva pro oddělení se zobrazuje jako vertikální lišta v levém dolním rohu.
karta oddělení.

.. poznámka::
Klikněte na upozornění v kartě oddělení, například „Žádosti o volno“, abyste zobrazili seznam
pohled na požadavky o schválení pro dané oddělení

.._zaměstnanci/seznam oddělení:

Zobrazení seznamu
---------

Pro zobrazení oddělení v seznamovém pohledu klikněte na ikonu „:icon:`fa-align-justify`“ :guilabel:`(seznam)“.
v pravém horním rohu. Oddělení se zobrazují v seznamovém pohledu, který zobrazuje
:guilabel:`Název oddělení`, :guilabel:`Společnost“, :guilabel:`Ředitel“, :guilabel:`Zaměstnanci“
„Hlavní oddělení“, „Barva“ pro každé oddělení.

Oddělení jsou seřazena abecedně podle názvu oddělení, výchozím nastavením.

.. obrázek:: oddeleni/seznam.png
:alt:Zobrazení seznamu oddělení.

… zaměstnanci / hierarchie oddělení:

Stručný přehled
--------------

Pro zobrazení oddělení v hierarchickém pohledu klikněte na ikonu „fa-share-alt fa-rotate-90“.
ikona „Organizační struktura“ v pravém horním rohu. Oddělení se zobrazují podle organizační
formát grafu s nejvyšším oddělením na vrcholu (obvykle „Vedení společnosti“).
všechny ostatní podřízené oddělení. Všechna dětská oddělení podřízená prvního řádu jsou
Složené.

Každá karta oddělení zobrazuje název oddělení, manažera (a jejich
obrázku profilu), počtu zaměstnanců v oddělení a počtu dětí.
odborů.

Klikněte na tlačítko „Rozbalit“ v kartě oddělení, abyste jej rozvinuli. Jakmile je rozvinuté,
Tlačítko „Rozbalit“ se změní na tlačítko „Sbalit“. Chcete-li oddělení zavřít, klikněte
tlačítko „Sbalit“ (viz obrázek). Můžete rozbalit pouze jednu složku v řádku.

Klikněte na jakoukoli kartu oddělení, abyste otevřeli formulář pro oddělení. Klikněte na „(#) Zaměstnanci“
chytrý tlačítko, které zobrazí seznam všech zaměstnanců v daném oddělení.

.. obrázek:: hierarchie_oddeleni.png
:alt:Zobrazení hierarchie oddělení.
