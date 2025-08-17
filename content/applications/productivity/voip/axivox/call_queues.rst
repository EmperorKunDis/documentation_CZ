===========
Fronty na telefonu
===========

Fronta volajících organizuje a směruje příchozí hovory, když jsou všichni agenti zaneprázdnění, a umisťuje je na čekací lince.
v pořadí, v jakém volali. Tento systém pomáhá lépe spravovat velké množství hovorů a zajišťuje férovost
rozdělení zátěže a poskytuje více předvídatelný zážitek jak pro volající, tak i pro agenty.

Tento dokument vysvětluje, jak nastavit parametry fronty hovorů a přihlásit se do fronty z aplikace Odoo.
databáze.

.. viz též:
:ref:`Nastavení hudby na drátě <voip/axivox/music_on_hold>`

Přidejte frontu
===========

Chcete-li přidat frontu volání v Axivox, přejděte na „Konzoli pro správu Axivox“.
<http://www.axivo.cz/cs/klient-axivo/ke-stazeni/>. V levém menu klikněte na položku „Fronty“. Následně klikněte
:guilabel:`Přidejte frontu“. Zde nastavíte frontu hovorů.

- :guilabel:`Název volací fronty`: Název fronty pro zpracování hovorů. Povinný údaj.
- :guilabel:`Vnitřní rozšíření“: Agenti mohou volajícího přepojit na tuto službu. Povinný údaj.
- :guilabel:`Strategie“: Jak jsou hovory směrovány. Zvolte možnost, která nejlépe odpovídá společnosti
požadavky na tuto frontu hovorů:

  - :guilabel:`Volat všechny dostupné agenty“: Hovor je odeslán každému agenta.
  - :guilabel:`Volá se uživateli, který telefonní hovor přijal nejdéle“: Hovor je odeslán
agent s nejdelší dobou nečinnosti.
  - :guilabel:`Volá agentovi, který má nejméně hovorů“: Volání je odesláno agentovi
měl nejmenší počet hovorů v časovém okně.
  - :guilabel:`Volat náhodný agenta“: Hovor je přijat náhodným agnetem.
  - „Přeposílat hovory na jednotlivé agenty“: Hovor je přesměrován na dalšího agenta, který byl předem určen.
tento příkaz je uložen a po každém volání se nevymaže.
  - :guilabel:`Zavolat operátory postupně, začínáme od prvního v seznamu“:
odeslány na další agenta v určitém pořadí. Toto pořadí se pamatuje a pořadí se neresetuje
po každém volání.

- :guilabel:`Délka čekání v sekundách“: Jak dlouho může zákazník čekat ve frontě
přepojení na hlasovou schránku nebo konkrétního agenta.
- :guilabel:`Délka hovoru u operátora“: Jak dlouho zazvoní telefonní ústředna
před tím, než se hovor přesune na další krok v telefonní síti. Více informací o :doc:`telefonních plánech
<základy_telefonní_sítě>.
- :guilabel:`Statické agenti“: Agenti ve frontě, kteří přijímají hovory bez přihlášení.
- :guilabel:`Dynamické agenty“: Agenti, kteří se musí přihlásit do fronty a přijmout hovor z ní.

.. viz též:
   - :ref:`voip/axivox/hudba-na-drátě“
   - :doc:`dial_plan_basics“
   - :doc:`dial_plan_advanced“

Agentská spojení
================

Agenti mají tři způsoby, jak se připojit do fronty na telefonní hovor:

- Statické agenti se automaticky propojí.

  - Statické agenti jsou vždy přihlášeni do fronty hovorů.

- Manažeři přihlásí konkrétní agenty přes „Axivox management console“ <https://manage.axivox.com>.
- Agent se připojuje do fronty v Odoo prostřednictvím **VoIP** widgetu.

Připojte se do fronty přes Axivox
-----------------------------------

Jakmile je nastavená fronta hovorů a změny se aplikují, manažer může přihlásit do Axivoxu.
konzoli pro správu (https://manage.axivox.com) a připojit dynamické agenty do fronty ručně.

Pro připojení agenta klikněte na záložku „Fronty“, která se nachází v levém menu. Po kliknutí se otevře
Dashboard „Fronty“ s několika různými sloupci uvedenými v názvu:

- :guilabel:`Jméno“: jméno fronty.
- :guilabel:`Dlouhé číslo“: číslo, které je potřeba vytočit k dosažení fronty.
- :guilabel:`Připojení agentů“: číslo, na které se dynamičtí agenti mohou přihlásit do fronty.
- :guilabel:`Agent disconnection“: číslo, které je potřeba zadat pro odhlášení dynamických agentů ze fronty.
- :guilabel:`Spojené agenty“: jména agentů spojených s frontou.

Na panelu „Fronty“ jsou k dispozici také následující tlačítka:

- :guilabel:`Připojit agenta“: ručně připojte agenta k frontě.
- :guilabel:`Zpráva“: spustit zprávu o frontě.
- :guilabel:`Smazat“: smažte frontu.
- :edit: změnit nastavení fronty.

Když jsou agenti připojeni do fronty nebo živí s klientem, zobrazují se pod
Sloupec „Spojené agenty“.

Pokud jsou statické agenty, vždy se zobrazí jako připojené.

Připojte agenta kliknutím na oranžový tlačítko s nápisem „Připojit agenta“. Pak vyberte
jméno požadovaného agenta z roletky a klikněte na tlačítko „Připojit“.

Pro ruční odhlášení dynamického agenta z fronty volání přejděte na Axivox Management Console.
<http://www.axivox.com>`, v levém menu klikněte na položku „Fronty“. Pak klikněte na
Zelené tlačítko „Obnovit“ v horní části sloupce „Připojená zařízení“.
Klikněte na červené tlačítko „Odpojit“ a okamžitě se odpojí. To lze
Pomáhá v situacích, kdy agenti zapomenou na konci dne se odhlásit.

.. obrázek: call_queues/call-queue.png
:alt:Zeleně zvýrazněná sloupec s volajícími, kteří jsou připojeni a tlačítko pro spojení a hlášení.
zvýrazněny.

Zpráva
~~~~~~

Klikněte na tlačítko „Hlášení“ pro otevření stránky s hlášením o čekací lince, která zobrazuje aktivity v čekárně.
Zpráva obsahuje informace o tom, kdo a kdy se připojil, stejně jako jaké hovory byly vyřízeny frontou.
Tato informace je zobrazena na samostatné stránce „Zpráva o frontě“.

Datum vzniku zprávy nastavte do pole „Období“. Chcete-li vybrat konkrétní datumový rozsah, použijte
Události“ a „Od“ a „Do“. Informace lze uspořádat podle „Události
:type` (popisované níže) a :guilabel:`Call ID“.

Zobrazit zprávu kliknutím na tlačítko „Použít“.

Každý zpráva může být exportován do souboru CSV (soubor oddělených čárkami) pro další použití.
Analýza, kterou provedete pomocí tlačítka Export do CSV.

Při kliknutí na pole „Typ události“ se zobrazí vyskakovací okno s následujícími
možnosti:

- :guilabel:„Zavěsil“
- :guilabel:`Agent se připojuje“
- :guilabel:`Agent se odpojuje“
- :guilabel:`Hovor byl ukončen (operátor zavěsil)“
- :guilabel:`Hovor byl ukončen (volající zavěsil)“
- :guilabel:„Hovor je připojen k operátorovi.“
- :guilabel:`Někdo se chystá do fronty“
- :guilabel:`Volající opustí frontu (žádný operátor není připojen).“
- :guilabel:„Volající opustí frontu (časový limit)“
- :guilabel:Nikdo neodpovídá
- „Nikdo neodpovídá, volající zavěsí“
- :guilabel:`Převod“
- :guilabel:`Přesměrování bez interakce s operátorem“ (při přepojení hovoru na operátora bez interakce s ním)

Každá nebo všechny z třinácti možností lze vybrat ze seznamu „Typ události“.
Kliknutím na tlačítko „Zkontrolovat vše“ se vyberou všechny dostupné možnosti z roletky.
Kliknutím na „Odškrtnout vše“ odstraníte všechny výběry z roletky.

K výběru konkrétního typu události klikněte na požadovanou možnost v rozevíracím seznamu.

.. obrázek: call_queues/report.png
:alt:Zpráva o frontě s výsledkem, typem události a obdobím zvýrazněným.

Připojte se do fronty na Odoo
------------------------

Dynamičtí agenti mohou manuálně připojit se na hlasovou frontu Axivo z **VoIP** widgetu v Odoo, jakmile
Aplikace VoIP je pro každého uživatele nastavena v Odoo.

Pro přístup k widgetu VoIP v Odoo klepněte na ikonu :icon:`oi-voip` :guilabel:`(VoIP)` .
v horním pravém rohu obrazovky v libovolné databázi Odoo.

.. viz též:
   - :doc:`axivox_config`
   - :doc:`/voip_widget`

Pro připojení agenta do fronty hovorů zavolejte na číslo „Připojení agenta“ a poté
Stiskněte zelené tlačítko „volání“ :icon:`fa-phone` :guilabel:`(telefon)` v **voip** widgetu. Potom
Agent slyší krátkou zprávu o délce dvou sekund, která ukazuje, že je přihlášený.
automaticky skončí.

Pro zobrazení spojených agentů v pořadníku hovorů přejděte na Axivox Management Console.
<https://manage.axivox.com>_ a klikněte na záložku „Fronty“.

Poté klikněte na zelený tlačítko „Obnovit“ v horní části seznamu „Propojených agentů“.
sloupci. Všechny agenty, statické nebo dynamické, které jsou nyní připojeny k frontě se zobrazují v sloupci
Přímo vedle fronty, do které jsou přihlášeni.

Pro odhlášení z fronty otevřete widget VoIP a vytočte číslo :guilabel:`Odpojení agenta`.
číslo a poté stiskněte zelenou tlačítko „volání“ :icon:`fa-phone` :guilabel:`(telefon)` ikonu. Operátor
odpojena z fronty po krátké dvousekundové zprávě.
