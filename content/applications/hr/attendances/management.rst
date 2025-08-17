===========================
Odměňování přesčasů a schválení práce
===========================

Aplikace Attendance společnosti Odoo vyžaduje řízení, aby se zajistilo, že všechny zaznamenané přítomnosti
Je správné zejména pro přesčasy a neúplné směny.

..._přítomnost na zasedání / přehled:

Pohled do řídicího panelu
====================

Všechny záznamy o docházce, které vyžadují schválení, obvykle kvůli překrývajícím se pracovním vstupům nebo
Nepovolené volno je řízeno z centrálního panelu pro správu. K přístupu k němu použijte
do pole „Použít“ zadat: `Návštěvníci aplikace --> Správa`.

Dashboard Management zobrazuje pouze docházkové záznamy pro současné zaměstnance.
musí být schváleny v seznamu výchozích hodnot. To je způsobeno dvěma výchozími filtry ve vyhledávání
baru, v poli „Schválit“ a „Aktivní zaměstnanci“.

Každý záznam o účasti obsahuje následující informace:

- :guilabel:`Zaměstnanec“: jméno zaměstnance
- :guilabel:`Check In“: datum a čas, kdy zaměstnanec nastoupil do práce
- :guilabel:`Odejít“: datum a čas, kdy zaměstnanec odešel
- :guilabel:`Čas odpracovaný zaměstnancem“: počet hodin, které zaměstnanec zaznamenal
- :guilabel:`Pracoval jsem přesčas“: počet odpracovaných hodin navíc
- :guilabel:`Přesčas“: celkový přesčas
- :guilabel:`Stav přesčasů“: stav záznamu o docházce. Všechny záznamy o docházce, které
Pokud se v tomto panelu objeví nějaký úkol, bude mít stav :guilabel:`K schválení`.

.. obrázek: management/management-dashboard.png
:alt:Dashboard aplikace Účasti s přehledem požadavků na schválení.

...přítomnosti/schválit/odmítnout:

Schválení a zamítnutí
======================

Příchody mohou být schváleny nebo zamítnuty přímo z řídicího panelu.
<přítomnost/panel nástrojů>. Vpravo od každého záznamu je ikona „Zkontrolovat“ a
:icon:`fa-times` :guilabel:`Odmítnout“ tlačítka se zobrazí. Klikněte na příslušné tlačítko, abyste buď
nebo odmítnout záznam o docházce.

.. poznámka::
Při schvalování nebo zamítání docházkových záznamů z panelu :guilabel:`Management` je
nelze zobrazit podrobnosti o docházce.

Částečné schválení
-----------------

Je možné schválit část zaznamenaných hodin nad rámec normální pracovní doby, nikoli celkový počet hodin.
Pokud chcete schválit pouze část přesčasové práce, klikněte do záznamu o docházce, abyste zobrazili podrobnosti.

Klikněte do pole „Přesčas“ a zadejte počet hodin, které byly schváleny.
upravíte pole „Pracovní doba navíc“ (Guilabel:Extra Hours), pole „Práce navíc“ se zobrazí.
zobrazit rozdíl mezi poli „Práce“ a „Přesčas“.

.. poznámka::
V poli „Pracovní doba“ je celkový počet hodin, které zaměstnanec zadal (v poli „Práce odpracovaná“).
(v kombinaci s „Time“ a „Extra Hours“). Například pokud je zaměstnanec naplánován na práci
osm hodin a pět hodin přesčasu, takže čas odpracovaný je třináct hodin.
Extra hodiny jsou pět hodin. V poli „Práce odpracovaná“ nelze provádět žádné změny.

Klikněte na ikonu „Ověřit“ a potvrďte aktualizované hodiny navíc.
Částečně schválené, pole „Pracoval jsem přesčas“ zmizí stejně jako
Klikněte na tlačítko „Schválit“ a rozdíl v hodinách se zobrazí v poli „Přidat“.
Hodiny.

Jakmile jsou přesčasové hodiny částečně schváleny, stav se změní na „Schváleno“.

.. obrázek: management/record.png
:alt:Podrobný záznam o docházce.

.. důležité::
Jakmile je částečná přesčasová pracovní doba schválena, stále je možné odmítnout přesčas kliknutím
:icon:`fa-times` :guilabel:`Odmítnout“. Záznam lze upravovat tak často, jak je potřeba.

.. poznámka::
Občas může být nutné ověřit polohu zaměstnance při přihlašování.
pracovník se zaevidoval do práce je uveden na individuálním záznamu v poli „Režim“.

Políčko :guilabel:`Mode` nelze měnit, protože jen zaznamenává způsob záznamu docházky.
vytvořen.

Možné varianty jsou:

   - :label:Kiosk: zaměstnanec fyzicky zaznamenal svůj příchod nebo odchod pomocí kiosku.
zařízení. Zaměstnanec byl přítomen na stánku, aby provedl kontrolu vstupu.
   - :guilabel:Systray: zaměstnanec se přihlásil nebo odhlásil přímo z databáze
<check_in_check_out>`, podle zobrazené :guilabel:`IP adresy
docházkový záznam lze zjistit, kde se zaměstnanec nachází v době přítomnosti.
   - :guilabel:`Manuálně“: záznam byl vytvořen ručně v aplikaci **Přítomnosti**.
obvykle prováděné správou systému, aby se doplnil chybějící záznam.

Vytvářejte docházkové záznamy
=========================

Pokud je třeba, mají uživatelé s potřebnými :ref:`právy přístupu <employees/work-info-tab>
Vytvářet záznamy o docházce ručně v aplikaci **Přítomnosti**. Některé situace, kdy je to nutné, jsou
když zaměstnanci zapomenou zadat příchod a odchod do směny, protože zaměstnanci nemohou zpětně vytvářet
příchozí záznamy.

Chcete-li přidat chybějící záznam o účasti, přejděte na: „Účasti aplikace –> Přehled“. Klikněte
tlačítko „Nový“ v pravém horním rohu. V okně „Vytvořit“ zadejte
následující informace na formuláři:

- :guilabel:`Zaměstnanec“: vyberte zaměstnance, pro kterého je vytvářený záznam.
populuje pole výchozí hodnotou.
- :guilabel:`Check In“: Vyberte datum a čas příjezdu pomocí kalendáře, pak klikněte
:icon:`fa-check` :guilabel:`Použít“. Výchozí datum je vybráno a čas nastaven
na „00:00:00“.
- :guilabel:`Check Out“: vyberte datum a čas odjezdu pomocí kalendáře, pak klikněte
:icon:`fa-check` :guilabel:`Použít“. Výchozí datum a čas je vybrán.
nastaven na „00:00:00“.
- „Čas odpracovaný“: tento údaj se automaticky vyplní z rozdílu mezi
vybrat čas „Přihlášení“ a „Odhlášení“. Toto pole nelze měnit.
- :guilabel:`Přesčasové hodiny“: zadejte počet přesčasových hodin k schválení.

.. důležité::
Jakmile jsou přidány „Přesčasy“, automaticky je schválí systém.
Je možné ručně odmítnout jejich přijetí, jak je popsáno v sekci :ref:`Schválení a zamítnutí
v sekci „Přítomnost/schválení/odmítnutí“.

.. obrázek: management/nový-rekord.png
:alt:Formulář záznamu o docházce pro Doris Cole na 23. dubna 2025.
