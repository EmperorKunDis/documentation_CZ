Zobrazit obsah

===========
Příjmy
===========

Aplikace **Přítomnosti** společnosti Odoo funguje jako časový strojek. Zaměstnanci mohou zadávat své příchody a odchody
práce pomocí zařízení v režimu „kiosku“ (viz. Dedikované zařízení v režimu kiosku) a uživatelé
Mohou také přímo z databáze kontrolovat své nástupy a odchody do práce: ref: attendances/check-in.
Manažeři mohou kdykoliv vidět dostupné pracovníky, vytvářet zprávy o hodinách všech zaměstnanců a
získat informace o zaměstnancích, kteří pracují přesčas nebo odcházejí z práce dříve než
očekávané.

...přístupy/práva přístupu:

Práva přístupu
=============

Znalost práv přístupu je nezbytná pro orientaci v aplikaci **Přítomnosti**.

Každý uživatel v databázi může zkontrolovat příjezd a odjezd přímo z databáze bez nutnosti
přístup do aplikace Attendances. Kromě toho všichni uživatelé mohou získat přístup ke svým vlastním záznamům o docházce
z jejich zaměstnanecké karty v aplikaci **Zaměstnanci**.

Přístup k aplikaci **Attendance** a různým funkcím v ní obsaženým je
Oprávnění k přístupu.

Chcete-li zjistit, jaké přístupové právo má uživatel, přejděte do aplikace „Nastavení“ --> „Uživatelé a
Firmy --> Uživatelé a klikněte na konkrétního uživatele. V záložce „Přístupová práva“ je vidět
výchozím nastavení. Pro zobrazení nastavení přejeďte dolů do sekce „Lidé“.
Pole „Účast“ lze buď nechat prázdné nebo vybrat
:guilabel:`Administrátor`.

Pokud je zvolené možnost „Administrátor“, má uživatel plný přístup k celému
Aplikace **Přítomnosti** s omezeným přístupem. Mohou si prohlížet všechny záznamy docházky zaměstnanců.
Přejděte do aplikace a zvolte možnost „Kiosk Mode“ a přístup k všem ukazatelům výkonu.
nastavení. Pokud je pole prázdné, uživatel nemá přístup k aplikaci **Přítomnosti**.

.. poznámka::
Pokud uživatel nemá práva správce pro aplikaci „Přítomnosti“, nebude moci provést změny.
Nemohou aplikaci otevřít, i když se na hlavním panelu databáze zobrazuje.
Při pokusu o přístup k souborům se zobrazí okno chybové hlášky s textem:

„Máte nedostatečná práva k přístupu na pole „attendance_manager_id“ v zaměstnanci.
(Správce systému). Kontaktujte svého správce systému.“

Uživatelé, kteří nemohou používat aplikaci **Přítomnosti**, stále mohou :doc:`se přihlašovat a odhlašovat.
<../hr/attendance/check_in_check_out> práce v databázi pomocí ikony
:guilabel:`(červený kruh)` nebo :icon:`fa-circle` :guilabel:`(zelený kruh)`, které jsou vždy
jsou k dispozici na vrcholu databáze.

...přítomnosti/schválení:

Schvalovatelé
---------

Schvalovatel je uživatel, který byl přiřazen k prohlížení a správě záznamů o docházce zaměstnanců. Schvalovatel
obvykle manažer, ale není to nutné. Schvalovatelé bez administrátorských práv mohou přistupovat
a upravovat docházkové záznamy pouze pro zaměstnance, kterým jsou přiřazeni. To je jediný
výjimka, kdy mohou uživatelé bez administrátorských práv zobrazit záznamy v aplikaci **Přítomnosti**.

Chcete-li zjistit, kdo schvaluje přítomnost zaměstnance, přejděte na stránku „Zaměstnanci“
„Přihlášení“ a klikněte na konkrétního zaměstnance. Klikněte na záložku „Informace o práci“.
Přejděte do sekce „Schválení“ a zkontrolujte pole „Přítomnost“. Osoba
vybraný má možnost si prohlédnout docházkové záznamy zaměstnanců v aplikaci **Přítomnosti**
dashboard i v přítomnostních zprávách a provádějí změny ve svých záznamů.

Konfigurace
=============

V aplikaci **Přítomnosti** není potřeba mnoho konfigurací. Vyhodnocování, jak se zaměstnanci přihlásí a
vymezují, jak fungují stánky, a určují, jak se počítají přesčasy.
Nastavení. Přejděte do části:menuselection:Přihlášky aplikace --> Nastavení
Přejděte do nastavení.

.. poznámka::
Každý konfigurační prvek s ikonou :icon:`fa-building-o` :guilabel:`(budova)` je
konfigurace pro danou společnost. Položky bez ikony „fa-building-o“
ikona se vztahuje na všechny společnosti uložené v databázi.

...přítomnosti/režimy:

Móda
-----

- :guilabel:`Přítomnost z backendu“ :icon:`fa-building-o`: aktivujte tuto funkci, aby uživatelé
aby se mohli přímo z databáze Odoo přihlásit a odhlásit. Pokud tato funkce není aktivována, uživatelé musí používat
pult, na kterém se můžete přihlásit a odhlásit z práce.
- :guilabel:`Automatické odhlášení“ :icon:`fa-building-o`: aktivujte tuto funkci pro automatické
kontrolovat zaměstnance podle jejich pracovního rozvrhu s časovým odstupem.
- „Tolerance“: pole se zobrazí pouze tehdy, když je aktivní „Automatické odhlášení“.
:ikona „budova“ je povolena. Zadejte počet hodin, které musí uplynout
před automatickým ukončením po skončení pracovní doby zaměstnance.

.. příklad::
S aktivní možností „Automatické vyúčtování“ a nastavenou tolerancí
„Dvě hodiny“, zaměstnanec nastoupil do práce v 9:00 ráno a zapomněl se odhlásit ve 15:00.
v 19:00 hodin jsou automaticky vykázáni.

- :guilabel:`Správa absence“ :icon:`fa-building-o`: zapněte tuto funkci pro evidenci absencí
přidružené k žádosti o dovolenou nebo nemocenské.
účasti na přednášce.

Přesčasy
-----------

Tato část specifikuje, jak se přídavný čas (někdy nazývaný jako „přesčas“) počítá včetně
Jak je započítávána přidružená doba a jak není zaznamenána.

- :guilabel:`Doba trvání tolerance ve prospěch společnosti“: zadejte počet minut
**nejsou započítány do přesčasů zaměstnance. Když zaměstnanec odchází, a navíc čas
Pokud je doba strávená na pracovišti zaznamenaná pod stanovenou hodinovou minutu, přidaný čas se nezapočítává jako přesčas.
zaměstnanci.
- :guilabel:`Doba tolerance ve prospěch zaměstnance“: zadejte počet minut, které má zaměstnanec na
Zaměstnanci je poskytnuta sazba, která **neovlivňuje jejich docházku**, pokud pracují méně hodin.
jejich pracovní dobu. Když zaměstnanec odchází na konci dne a celkový čas strávený v práci je méně
než stanovené pracovní hodiny a méně než tento stanovený časový úsek, jsou **nejsou**
Penalizovány za snížený pracovní úvazek.

...... příklad::
Společnost nastaví obě pole „Dovolená“ na 15 minut a pracovní dobu
pro celou společnost jsou nastaveny od 9:00 do 17:00 hodin.

Pokud zaměstnanec přijde v 9 hodin ráno a odejde ve 14.14 hodin, pak těchto 14 minut navíc
**nebyly započítány do jejich přesčasů.

Pokud zaměstnanec přijde v 9:05 ráno a odejde v 16:55, i když celkový čas strávený na pracovišti byl
Pokud pracují o deset minut méně než jejich plný pracovní úvazek, **nejsou za to trestáni**.
nesoulad.

- :guilabel:`Ověření přesčasů“ :icon:`fa-building-o`: zaškrtněte příslušný tlačítko uvedené vedle
:guilabel:`Automaticky schváleno“ pro automatické schválení všech přidělených hodin.


- :guilabel:`Zobrazit přesčasové hodiny“: aktivujte tuto políčko, abyste viděli přesčasové hodiny
pracovníkovi při výdeji na pokladně nebo uživateli při výdeji v databázi.

.. poznámka::
Pracovní doba přesčas může být odečtena z schválené žádosti o volno.
<volno/odečíst-přesčas>.

Přehled
========

Při vstupu do aplikace **Přítomnosti** se zobrazí přehledová lišta
obsahující všechny informace o příjezdu a odjezdu uživatele. Pokud má uživatel požadované
přístupová práva nebo je schvalovatelem
Pro konkrétní zaměstnance se v příslušné části zobrazí informace o příjezdu a odjezdu.
:guilabel:`Přehled“ panelu.

Dashboard **Přítomnost** umožňuje přepínání mezi :icon:`fa-tasks` :guilabel:`(Gantt)“ a
:ikon:`oi-view-list` :guilabel:`(Seznamy)` pohledů a vybrat časový úsek k analýze. Současný čas
je automaticky zvýrazněn žlutě pro záznamy o přítomnosti v reálném čase.
Tlačítko ikony „fa-crosshairs“ se štítkem „(Focus Today)“ okamžitě vrátí panel na hlavní stránku.
dnešní datum.

.. obrázek:přístupy/souhrn.png
:alt:Přehledová tabulka s informacemi o aktuálním týdnu a dne
zvýrazněny.

.. poznámka::
Každá položka s chybou se zobrazí červeně, což znamená, že ji musí vyřešit uživatel.
správné přístupové právo a/nebo jsou schválení
pro zaměstnance s chybami.

...přítomnosti/filtry skupiny:

Filtry a skupiny
==================

Občas se mohou úředníci a manažeři potřebovat podívat na konkrétní záznamy, jako jsou všechny automatické
pokladny k určení zaměstnanců, kteří trvale zapomínají na vyúčtování nebo podle oddělení.
určit, která z týmů pracuje nejvíce přesčas.

Pro tyto případy použijte vyhledávací lištu k výběru filtrů :icon:`fa-filter` :guilabel:`Filtry`.
:icona: „Skupina“ nebo „Skupiny“, nebo obojí, abyste zobrazili požadované informace.

.. viz též:
:doc:`../základy/vyhledávání`

Vysoké hodnoty filtrů
------------------

.. seznam tabulkový::
:hlavičkové řádky: 1
:prázdné sloupky: 1
:šířky: 40 60

   * – filtr
     - Běžný případ použití
   * - Na práci
     - Před uzavřením budovy na noc ověřte zaměstnance stále přítomné na místě.
sečetli hlavy.
   * -Chyby
     - Zobrazte všechny chyby a opravte je před zpracováním výplaty.
   * –Automaticky vyčerpaná
     - Proveďte audit, abyste zjistili zaměstnance, kteří trvale zapomínají na ukončení pracovní doby.
   * Datum
     - Omezte výsledky na konkrétní období nebo okno pro kontrolu.
   * -Aktivní/archivovaní zaměstnanci
     - Přepínat mezi současnými zaměstnanci a bývalými zaměstnanci při kontrole historických dat.

Osvěžující skupinové seskupení
--------------------

.. seznam tabulkový::
:hlavičkové řádky: 1
:prázdné sloupky: 1
:šířky: 40 60

   * – Skupina podle
     - Když pomáhá
   * – zaměstnanec
     - Během jednání na 1:1 zkontrolujte individuální docházku.
   * -Oddělení
     - Srovnejte počet zaměstnanců a pracovní dobu, abyste zjistili, které týmy jsou přetíženy nebo naopak podvyživeny.
   * – Managing director
     - Určete, kam se mohou zaměstnanci obracet s dotazy týkajícími se docházky.
   * - Metoda
     - Sledujte trendy v přítomnosti, abyste mohli vyřešit problémy s hardwarovými komponentami.
   * - Datum (Den/Týden/Měsíc)
     - Identifikujte špičky nebo sezónní trendy v absenci.

...přítomnost/chyby:

Podrobnosti o docházce
======================

Odoo zaznamenává datum a místo každého příjezdu i odjezdu, přičemž pole se liší podle
metoda, kterou použil. Tyto podrobná záznamová data mohou potvrdit, kde byl zaměstnanec v průběhu pracovního dne.
Toto může být užitečné pro společnosti s hybridním rozvrhem práce, které mohou potřebovat provádět kontroly.
zajistit řádné plnění.

Podrobný záznam o docházce obsahuje následující informace:

Hlavní informace
------------

- :guilabel:`Zaměstnanec“: jméno zaměstnance.
- :guilabel:`Příchod do práce“: datum a čas, kdy zaměstnanec nastoupil na pracoviště.
- :guilabel:`Vyčistit“: datum a čas, kdy zaměstnanec odešel z práce. Tento údaj se **výhradně** objevuje v případě, že
Zaměstnanec odjel na dovolenou.
- :guilabel:`Práce odpracovaná za den“: celková doba, kterou zaměstnanec strávil na pracovišti během dne.
příjezdy a odjezdy. V hodinovém a minutovém formátu (HH:MM).
- :guilabel:`Pracoval přesčas“: schválený přesčas (zobrazí se pouze u zaměstnance, který je přítomen).
- :guilabel:`Pracovní doba navíc“: neplacené přesčasy, které byly odpracovány nad rámec očekávaného rozvrhu pracovní doby.


Podrobnosti o příjezdu a odjezdu
--------------------------

Následující informace se zobrazuje pro oba tyto pole: „Přihlášení“ a „Odhlášení“.
části.

- :guilabel:`Způsob přihlašování“: způsob podání docházky. Může být :ref:`V systémové liště <doklady/přítomnost>“,
:ref:`Kiosk <attendance/kiosk-mode-entry>`, nebo :guilabel:`Manuální“ vstup.
- :guilabel:`IP adresa“: IP adresa zařízení používaná k přihlášení nebo odhlášení.
- :guilabel:`Webový prohlížeč“: webový prohlížeč, který zaměstnanec používal k přihlášení nebo odhlášení.
- :guilabel:`Lokalizace“: město a země spojená s IP adresou počítače.
- :guilabel:`Souřadnice GPS“: konkrétní souřadnice, které uživatel zadal při přihlášení nebo odhlášení.
:ikonka:oi-arrow-right:tlačítko:Zobrazit na mapě
pod nadpisem „Souřadnice GPS“. To otevře nové záložky v prohlížeči s konkrétními souřadnicemi.
místo, které bylo uvedeno.

.. obrázek:přítomnosti/podrobnosti.png
:alt:Podrobné informace o záznamu docházky.

Chyby při docházce
=================

Záznamy obsahující chybu se zobrazují na přehledové liště v červeném provedení.
Viditelnost v pohledu Ganttových diagramů (Gantt), kde se zobrazuje červeně.
:guilabel: (Zobrazení v seznamu) je text položky zobrazen červeně.

Chyba nastane v případě, že zaměstnanec se zaregistroval, ale neodešel do 24 hodin nebo když
jedna doba odbavení přesahuje 16 hodin.

Chybu je nutné opravit změnou nebo smazáním docházkového záznamu. Kliknutím na záznam se zobrazí
přepínačem, který obsahuje podrobnosti o daném záznamu. Chcete-li upravit pole „Záznam“ a/nebo
Klikněte na pole „Check In“ nebo „Check Out“.
a v kalendáři se objeví výběr data. Klikněte na požadovaný den, pak použijte časový filtr pod kalendářem
kalendář pro výběr konkrétního času vstupu. Když jsou informace správné, klikněte
:guilabel:`Použít.“

Když jsou všechny informace v okně správné, klikněte na tlačítko „Uložit a zavřít“.
delší doba chyby, pak se záznam zobrazí šedě místo červeně.

Chcete-li smazat záznam, klikněte na červené tlačítko „Smazat“ v okně namísto
změny v zápisu.

.. viz též:
   - :doc:`přítomnost/vstupní kontrola/výstupní kontrola“
   - :doc:`přítomnost/kiosek“
   - :doc:`přítomnost/správa“
   - :doc:`přítomnost/hardware“
   - :doc:`přítomnosti/hlášení o přítomnosti“

..toctree::


příchody/odchody
návštěvnost/pult
účastníci/správci
přítomnost/hardware
přítomnost/hlášení o přítomnosti
