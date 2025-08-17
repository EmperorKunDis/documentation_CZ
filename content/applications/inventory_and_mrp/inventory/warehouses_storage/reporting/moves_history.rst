=======================
Pohyby v historii
=======================

Ve zprávě „Historie pohybů“ v Odoo Inventories je uveden podrobný záznam o pohybech produktů.
(obsahující minulé a současné umístění), čísla pozemků a důvody přemisťování. Zprávy lze
generované pro jakýkoli časový rámec, což z něj dělá nezbytnou součást analýzy zásob a monitorování
obratu zásob a identifikovat případné rozdíly v zásobách.

.. poznámka::
Přístup k této funkci mají pouze uživatelé s :doc:`admin přístupem
<../../../obecne/uzivatele/pristupova-prava>.

Pro přístup k inventární zprávě přejděte na: „Aplikace Inventář --> Zprávy --> Historie pohybů“.

.. obrázek: moves_history/moves-history.png
:align:center
:alt: Zobrazit historii pohybů.

...Inventář/sklady/historie skladování/dokumenty o přemísťování:

Procházejte historii pohybů
=================================

V zprávě jsou sloupce označeny takto:

- :guilabel:`Datum“: datum a čas přesunu akcií.
- :guilabel:`Referenční údaj`: popis důvodu pohybu zásob nebo změny množství, například
číslo dokladu (např. „WH/IN/00012“).
- :guilabel:`Produkt“: název produktu, který je zapojen do stěhování.
- :guilabel:`Číslo šarže/série“: určuje číslo šarže nebo sérii ztraceného produktu.
Od té doby se přestěhoval.
- :guilabel:`Od“ zdrojového umístění přesunutého produktu.
- :guilabel:`Kam“: cílové místo přemístěného produktu.
- :guilabel:`Množství“: počet přepravených výrobků.
- :guilabel:`Jednotka měření produktů přepravovaných vlaky“: jednotka měření produktů přepravovaných vlaky.
- :guilabel:`Stav“: ukazuje stav pohybu, který může být :guilabel:`Dokončeno“.
:guilabel:`K dispozici“ (připraveno k použití) nebo :guilabel:`Částečně dostupné“ (neúplné
(výše potřebného množství k dokončení operace).

Možnosti vyhledávání
--------------

Použijte následující možnosti vyhledávání k přizpůsobení zprávy „Historie pohybů“ tak, aby se
Relevantní informace

.. záložky::

...... tab:: Filtry

V sekci Filtry mohou uživatelé vyhledávat mezi předdefinovanými filtry a vlastními filtry.
najít konkrétní záznamy o cenných papírech.

      - :guilabel:„Co dělat“: Zobrazují se záznamy pohybu skladových položek, které jsou v průběhu. To zahrnuje řádky s
:guilabel:`Stav“ sloupce s hodnotou „K dispozici“ nebo „Částečně k dispozici“.
      - :guilabel:`Dokončeno“: dokončené pohyby zásob s stavem „Dokončeno“.
      - :label:Příchozí: zobrazuje záznamy o pohybu na skladových místech dodavatelů.
      - :guilabel:`Odesílané“: zobrazuje pohyby záznamů do míst zákazníků včetně zákazníka
se vrátí.
      - :guilabel:`Vnitřní“: zobrazuje záznamy o přesunu věcí mezi vnitřními prostory.
      - :guilabel:'Výroba': zobrazuje záznamy o výrobě produktů virtuálně.
výroba: „Lokalita <../inventarizace/vyuziti-lokalit>.
      - :guilabel:`Datum“: vyberte tento seznam, abyste měli k dispozici různé filtry pro data a zobrazili si je.
z konkrétního měsíce, čtvrtletí nebo roku.
      - :guilabel:`Posledních 30 dní“: zobrazuje záznamy, které se staly v posledních třiceti dnech.
      - :guilabel:`Poslední tři měsíce“: zobrazuje záznamy za posledních třech měsíců.

... tab:: Skupina

Sekce „Skupina“ umožňuje uživatelům přidávat předdefinované a vlastní skupiny do
vyhledávání.

      - :guilabel:`Produkt“: seskupte záznamy podle produktu.
      - :guilabel:`Stav“: skupinová data podle tří typů stavu: :guilabel:`Dokončeno“,
:guilabel:`K dispozici“ a :guilabel:`Částečně k dispozici“.
      - :guilabel:`Datum“: skupina záznamů podle :guilabel:`Rok“, :guilabel:`Čtvrtletí“, :guilabel:`Měsíc“.
:guilabel:'Týden' nebo :guilabel:'Den'.
      - :guilabel:`Převody“: skupiny záznamů podle čísla operace, například „WH/OUT/00012“.
„WH/MO/00211“.
      - :guilabel:`Lokalita“: skupinová data podle zdroje (sloupec „Od“ v tomto
(report).
      - :guilabel:`Kategorie produktů“: Skupina záznamů podle kategorie produktu. Konfigurace probíhá v
:menu_selektor:`Skladové aplikace --> Konfigurace --> Zboží: Kategorie zboží`.
      - :guilabel:`Batch Transfer“: skupina záznamů podle :doc:`batch
<../../skladování a expedice/vybírání/metody vybírání/soubor>.

.. tab:: Oblíbené

Uložit aktuální použité filtry a skupiny, aby se stejná informace mohla snadno získat
po zavření této stránky klikněte na tlačítko „Uložit aktuální vyhledávání“.

Volitelně zaškrtněte políčko „Výchozí filtr“ a tento aktuální pohled se stane výchozím.
filtr při otevření zprávy „Historie pohybů“. Nebo zaškrtněte políčko „Sdílené“.
zaškrtávací políčko, aby se možnost vyhledávání zobrazila ostatním uživatelům.

Poté klikněte na tlačítko :guilabel:`Uložit`.

.. viz také:
:doc:`../Essentials/Search`

