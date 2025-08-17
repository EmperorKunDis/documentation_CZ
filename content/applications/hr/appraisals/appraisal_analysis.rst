==================
Analýza hodnocení
==================

Aplikace „Ocenění“ má schopnost hlásit všechna ocenění v systému, včetně
hodnocení minulosti, současnosti a budoucnosti a jejich příslušné postavení. Tato zpráva pomáhá manažerům
sledovat plánované hodnocení a identifikovat jakékoliv pozdní nebo nepotvrzené hodnocení.

Pro přístup k zprávě „Analýza hodnocení“ přejděte na: menu:„Ocenění aplikace –> Zprávy
--> Analýza hodnocení“.

Na stránce „Analýza hodnocení“ se zobrazí report s přehledem všech hodnocení.
databáze v grafu výchozího typu. Hodnocení jsou seskupena podle měsíce:
:guilabel:`Oddělení“.

Zobrazení podle stavu
==============

Další způsob pohledu na zprávu „Analýza hodnocení“ je v Ganttově grafu, který poskytuje vizuální
informace o stavu odhadce.

Přejděte na:menu:Appraisals app --> Reporting --> Appraisal Analysis“ a klikněte na
Ikona „úkoly“ v pravém horním rohu, pod ní zobrazuje současný stav projektu.
rok, dělený podle oddělení, s aktuálním měsícem zvýrazněným.

Každá položka je zvýrazněna jinou barvou, aby bylo možné zjistit její stav:

+-----------+----------------------------+------------------------------------------------+
|Barva      |Stav                       |Význam                                                  |
+===========+============================+================================================+
|Žlutá     |:guilabel:`Dokončeno`       | Hodnocení bylo dokončeno.
+-----------+----------------------------+------------------------------------------------+
|Oranžová   |:guilabel:`Potvrzení hodnocení`  |Hodnocení bylo potvrzeno, ale nebylo dokončeno. |
+-----------+----------------------------+------------------------------------------------+
|Červená  |:guilabel:`Zrušeno`  |Ocenění bylo zrušeno.
+-----------+----------------------------+------------------------------------------------+
|Šedá       |:zelená značka:Zahájit|Hodnocení bylo naplánováno, ale nebylo potvrzeno.|
+-----------+----------------------------+------------------------------------------------+

.. poznámka::
Odhad bude automaticky naplánován (zobrazí se šedě) podle své příslušnosti.
:ref:`hodnocení/hodnotící plán`.

Pro změnu zobrazeného období přepněte data v pravém horním rohu
Zprávu otevřete kliknutím na ikonku :icon:`fa-calendar` :guilabel:`Od (datum) do (datum)`
rozbalovací nabídka možností. Zobrazované možnosti jsou: guilabel:'Dnes',
:guilabel:Tento měsíc, :guilabel:Tento kvartál a :guilabel:Tento rok.

Dále lze do políčka „Od“ a „Do“ zadat rozsah dat.
spodní části seznamu a poté klikněte na „Použít“.

Kdykoli klikněte na tlačítko „Zaměřit se dnes“ (použijte ikonu „fa-crosshairs“), abyste měli přehled o tom, co je v současné době důležité.
V zobrazení uveďte dnešní datum.

Kliknutím na jakoukoli hodnotící zprávu se objeví okno s podrobnostmi o této hodnotící zprávě.
termínu hodnocení. Chcete-li zobrazit další podrobnosti, klikněte na tlačítko „Zobrazit“ a
podrobnosti se zobrazí v okně „Otevřeno“.

Výsledky vyhledávání mohou být filtrovány podle dalších kritérií, například :ref:`filtrů <search/filters> a
vyhledávací lištu v horní části stránky.

.. obrázek:hodnocení_analýza/analýza.png
:alt:Zpráva zobrazující všechny hodnocení pro Zprávu Analýzy Hodnocení.

.. _hodnocení/skupinový status:

Skupina podle stavu
===============

Pokud má společnost velké množství zaměstnanců, výchozí zpráva „Analýza hodnocení“
může zobrazit příliš mnoho informací najednou. V tomto scénáři je možné zobrazovat data podle stavu
Může být prospěšná.

Nejprve odstraňte filtry nebo skupiny z vyhledávací lišty. Poté klikněte na ikonu „fa-caret-down“
ikona „Zobrazit panel pro vyhledávání“ v pravém dolním rohu vyhledávací lišty. Klikněte na „Stav“.
v sloupci „Skupina“ v seznamu ikonek. Klikněte mimo seznam, abyste jej zavřeli.

Všechny hodnocení jsou nyní uspořádané podle stavu, v následujícím pořadí: :guilabel:`Zrušené`,
„Dokončeno“, „Zahájeno“ a „Odpověď zaslána“.

Tento pohled ukazuje, které hodnocení je třeba dokončit a kdy, stejně jako která hodnocení jsou stále
musí být potvrzeny.

.. obrázek: hodnocení_analýza/podle_stavu.png
:alt:Zpráva zobrazující všechny hodnocení, seřazené podle stavu.

Příklad použití: zobrazení jen hodnocení uživatele
=========================================

Při prohlížení zprávy „Analýza ocenění“ může ušetřit čas pouze prohlédnutí odhadů.
Přihlášený uživatel je zodpovědný za své chování a skrývá ostatní.

K zobrazení pouze těchto dat klikněte na ikonu :icon:`fa-caret-down` :guilabel:`(Povolit vyhledávací panel)“
v pravé části vyhledávací lišty, kde se zobrazí rozbalovací nabídka.

.. poznámka::
Není nutné odstraňovat výchozí skupování podle ikony „OI-Group“ a štítku „Oddělení“.
Zůstává aktivní, výsledky jsou seřazeny podle oddělení. Pokud je odstraněno, zobrazí se
seřazené abecedně.

Klikněte na „Přidat vlastní filtr“ v dolní části ikony „Filtry“.
sloupci a okno „Přidat vlastní filtr“ se objeví.

Klikněte do prvního pole a objeví se okno s různými možnostmi. Klikněte na
:icon:`fa-chevron-right` :guilabel:`(pravý směr)` ikona za slovem :guilabel:`Zaměstnanec“, pak
Přejděte dolů a klikněte na položku „Manager“. Následně nastavte střední pole na hodnotu „=“
:guilabel:`(rovno)` a nakonec klikněte na třetí pole a vyberte požadovaného uživatele ze seznamu.
pole jsou nastavená, klikněte na tlačítko „Přidat“.

.. obrázek: hodnocení_analýza/vlastní.png
:alt: Filtr přizpůsobený tak, aby se zobrazili pouze zaměstnanci uživatele.

Nyní se zobrazují pouze hodnocení, která má na starosti vybraný uživatel.
místo prohlížení všech hodnocení.

Tento report lze také seskupit podle stavu :ref:`<appraisals/group-status>`.

.. obrázek: hodnocení_analýza/uživatelské_hodnocení.png
:alt:Zpráva zobrazující pouze hodnocení, za která je uživatel odpovědný, podle stavu.

.. viz též:
   - :doc:`Odoo esenciální reportování <../../essentials/reporting>`
   - :doc:`../../základy/vyhledávání`
