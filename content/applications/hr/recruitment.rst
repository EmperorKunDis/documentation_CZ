Zobrazit obsah

===========
Personální agentura
===========

Odoo udržuje všechny uchazeče o práci organizované s přednastaveným postupem kroků a fází, které musí každý
Uchazeč projde každým kolem, které má své specifické kroky, které je potřeba provést. Ty začínají
například domluvit si telefonický rozhovor, pohovor nebo zaslat pracovní nabídku.
Je označována jako „proud žádostí“.

Když se uchazeč hlásí na pracovní pozici, v Odoo je automaticky vytvořená karta „Uchazeč“.
Aplikace pro nábor zaměstnanců na konkrétní pracovní pozici. Kandidát se tak postupně dostává
pracovní procesu, tým pro nábor pohybuje svou kartu z jedné fáze do další.

:ref:`Fáze může být konfigurována tak, aby e-mail byl automaticky odeslán
výstupu pomocí předdefinovaného šablonového vzoru ihned po vstupu karty do fáze.
automatické e-maily jsou definovány na každé fázi v procesu žádosti.

Tento dokument popisuje standardní konfiguraci Odoo, ale může být upravena podle potřeby.
vyhovovat jakémukoli procesu náboru.

.. poznámka::
Stupně se vztahují na všechny pracovní pozice, pokud není :ref:`označeno jako specifické pro danou práci.
<rekrutace/upravit-fáze>  Změny v fázích (např. přidání nebo odstranění) se týkají všech
pozice, pokud není explicitně rozsahována.

.._zaměstnávání/ nastavení:

Nastavení
========

Před vytvořením pracovní pozice v Odoo nastavte potřebné parametry pro **Personalistiku**
aplikace. Pro zobrazení a úpravu nastavení přejděte do: „Nabídka práce --> Konfigurace
→ Nastavení“. Po provedení jakýchkoliv změn klikněte na tlačítko „Uložit“ v pravém horním rohu
uložit všechny změny.

Inzerát na pracovní pozici
-----------

V sekci „Pozice“ aplikace pro nábor zaměstnanců je dvou konfigurací.
umožňuje zveřejnění pracovních nabídek na webových stránkách společnosti a externích pracovních portálech.

Pokud má být pracovní pozice zveřejněna na webových stránkách společnosti, povolte :guilabel:`Online Posting`.
volba.

.. poznámka::
Funkce „Online Posting“ je k dispozici pouze v případě, že je aktivní funkce „Website“ (viz dokument „Webové stránky“).
Aplikace je také nainstalována.

Aplikace **Nabídka práce** umožňuje zveřejnit pracovní pozice přímo na pracovním portálu. K tomu je potřeba kliknout
Klikněte na ikonu „Vybrat pracovní portál“ a pokud není vyžadováno
je již nainstalována. Klikněte na tlačítko „Instalovat“ v příslušném modulu a poté se přihlaste do hlavního Odoo
dashboard se načte po úspěšné instalaci.

Otevřete aplikaci **Nábor** a přejděte do sekce:
Nastavení“. Zadané údaje o pracovním místě jsou uvedeny. Vyplňte pole „Uživatelské jméno“ a
:guilabel:`Heslo“ pro pracovní nabídku. Po provedení jakýchkoliv změn klikněte na tlačítko „Uložit“.

.. poznámka::
V současné době je jedinou pracovní nabídkou integrovanou s Odoo Monster.com.

Proces
-------

V části „Proces“ nastavení je uvedeno, co může a nemůže databáze dělat.
během náborového procesu.

Vyplnit dotazník
~~~~~~~~~~~~~~~~~~~~~

Odoo je schopno zaslat dotazník uchazeči, aby získal více informací o něm.
Průzkumy lze považovat za zkoušky nebo dotazníky a mohou být upraveny různými způsoby.
poskytnout týmu náboru cenné informace o uchazečích

Zapněte možnost „Odeslat dotazník pohovoru“ a odešlete dotazníky uchazečům. Jakmile je zapnete,
Ikona „fa-arrow-right“ se objeví a po kliknutí na ni se zobrazí
:icon:`fa-arrow-right` :guilabel:`Anketa“ odkaz na seznam všech vytvořených
průzkumy.

Seznam zahrnuje všechny průzkumy vytvořené v databázi, nejen ty použité v
Aplikace pro nábor zaměstnanců. Pokud nebyly vytvořeny žádné průzkumy, seznam průzkumů zobrazí :guilabel:`Žádné
Zpráva „Průzkum zjištěn“ a nabízí možnosti vytvoření průzkumu ze několika předkonfigurovaných průzkumů
šablony.

.. viz též:
:doc:`vytvořit/upravit průzkumy <../marketing/surveys/create>`

.. poznámka::
Povolení možnosti „Odeslat dotazník“ vám nainstaluje aplikaci **Dotazníky**.
Pokud jsou nastavení uložena, tak se aplikace nainstaluje.

Konfigurátor platových balíčků
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Při zaslání nabídky uchazeči lze nastavit datum vypršení platnosti nabídky. Zadejte číslo
kolik dní platí nabídka v poli :guilabel:`days`. Po stanoveném počtu dnů
pokud žadatel nabídku nepřijme, je již neplatná.

..._prijem-cv-zobrazeni

Zobrazení životopisu
~~~~~~~~~~~~~~

Když uchazeči podají žádost, jedním z výchozích povinných polí je životopis, nebo zkratka CV.
Životopis. Všechny životopisy jsou uloženy v aplikaci Dokumenty a jsou dostupné na
Karta žadatele.

Životopis může být zobrazen na žádosti o zaměstnání, kterou je možné prohlédnout kliknutím na
Životopis se zobrazuje v pravém dolním rohu obrazovky. Pokud tato možnost není povolena,
Životopis je přístupný prostřednictvím odkazu v chatovací oblasti, kde musí být kliknutý na rozšíření a zobrazení.
stáhnout.

Zapněte možnost „Zobrazit životopis“ (viz guilabel:Résumé Display), aby se životopis zobrazoval na kartě uchazeče o zaměstnání.
a kromě odkazu na dokument také náhled životopisu vpravo vedle
karta žadatele.

.. poznámka::
Pro zobrazení životopisu na pravé straně okna prohlížeče musí být otevřen v plném rozlišení.
webový prohlížeč zabírá celou obrazovku.

Pokud je okno prohlížeče nastaveno na menší velikost než celou šířku obrazovky (ne
v plném rozlišení), pak se životopis nezobrazuje vpravo, ale životopis se zobrazí
:guilabel:`Soubory“ části chatu pod kartou uchazeče.

.. obrázek: nábor/cv-zobrazení.png
:alt:Životopis uchazeče na jeho kartě, který se nachází vpravo.

Nákupy v aplikaci
----------------

Sekce „Nákupy v aplikaci“ pod položkou „Nastavení“ se týká předmětů, které
požadované kredity pro použití, jako například:abbr: SMS (služba krátkých zpráv) a digitalizace.
životopisy.

.. viz též:
:doc:`Ceník a často kladené otázky <../marketing/sms_marketing/pricing_and_faq>`

Odeslat SMS
~~~~~~~~

Textové zprávy lze zasílat uchazečům přímo přes aplikaci **Nabídka práce**.
Tato funkce vyžaduje kredity pro použití. Klikněte na ikonu „fa-arrow-right“ a zobrazí se okno „Spravovat službu a zakoupit
Vnitřní odkaz na kredity a postupujte podle návodu :doc:`jak si zakoupit kredity
<../marketing/sms_marketing/cenik_a_otazky_a_odpovedi>.

.._rekruitering/cv-ocr:

Digitální přepis (OCR)
~~~~~~~~~~~~~~~~~~~~~~~~~

Když je žádost podána jakýmkoliv z dostupných způsobů, například prostřednictvím online žádosti
podání žádosti, zaslání životopisu na pracovní pozici nebo vytvoření záznamu uchazeče přímo
z databáze je možné mít Odoo vyčíst jméno, telefonní číslo a e-mailovou adresu uchazeče.
adresu z životopisu a vyplnit údaje uchazeče. Pro to je zapotřebí aktivovat :guilabel:`Životopis
Možnost digitální transformace (OCR).

Když je zapnutá, objeví se další možnosti. Klikněte na příslušný tlačítko s rádiem a vyberte jednu z
následující možnosti:

- :guilabel:"Nedigitalizovat": tato možnost vypíná digitální převod životopisu.
- „Digitalizace na vyžádání“: tato možnost digitalizuje pouze životopisy, které jsou požadovány.
:guilabel:`Digitalizovat dokumenty“ tlačítko se zobrazí na kartě uchazeče. Po klepnutí se životopis
je vyfocen a karta žadatele je aktualizována.
- Možnost „Automaticky digitalizovat“: tato možnost automaticky digitalizuje všechny životopisy, když jsou
podána.

Pod těmito možnostmi jsou dvě další odkazy. Klikněte na ikonu „fa-arrow-right“ a poté na „Spravovat
Odkaz na nákup kreditů pro digitalizaci životopisu v rámci služby Service & Buy Credits. Klikněte
:icon:`fa-arrow-right` :guilabel:`Zobrazit moje služby“ vnitřní odkaz na zobrazení seznamu všech aktuálních
služby a jejich zůstatky na účtech.

Pro více informací o digitalizaci dokumentů a :abbr:`IAP (in-app purchases)` se podívejte na
Dokumentace k nákupům v aplikaci (IAP):

.. poznámka::
Volba „Nedigitalizuj“ může na první pohled vypadat jako zbytečná, ale má své důvody.
Deaktivace možnosti „Digitální přepis (OCR)“ odinstaluje modul.
:guilabel:"Nedigitalizujte" udrží modul nainstalovaný, ale neaktivní - umožňuje tak uživateli
později znovu zapnout digitální přenos bez nutnosti opět instalovat modul.

Kanbanový pohled
===========

Pro přístup k zobrazení Kanban pro pracovní pozici se přihlaste do hlavního aplikace „Nábor“
přístrojová deska, která je výchozí pohled při otevření aplikace. Všechny pracovní pozice se zobrazují na
hlavní panel. Klikněte na tlačítko „Nové žádosti“ (#) na kartě pracovního místa
přejít do kanbanového pohledu na všechny uchazeče o tuto konkrétní pracovní pozici.

.. obrázek: nábor/tlačítko nové uchazeče.png
:alt:Hlavní pohled na kartu pracovního místa s tlačítkem pro zobrazení nových přihlášek.

V rámci žádosti o práci se objevují fáze Kanbanu s vyplněnými uchazeči.
odpovídající sloupce, které ukazují, jakou fázi aktuálně procházejí. V Odoo jsou šest výchozích fází
konfigurováno:

- :ref:`Nový <rekru/novy>`
- :ref:`Prvotní kvalifikace <rekruitování/prvotní-kvalifikace>`
- :ref:`První pohovor <recruitment/first-interview>`
- :ref:`Druhé pohovor <rekru/druhe-pohovor>`
- :doc:`Návrh smlouvy <nabídka práce/pracovních pozic>`
- :ref:`Smlouva podepsána <nabídka práce/pracovní pozice/smlouva podepsána>`

Poslední sloupec, který je ve výchozím nastavení zobrazený skrytě, má název „Smlouva podepsána“ a
karty uchazečů jsou skryty. Chcete-li rozložit stojan a zobrazit kartu uchazeče
pro tuto sloupec klikněte na tenhle tenký šedivý sloupec, který říká jméno a sloupec.
rozšiřuje se a odhalují se uchazeči.

.. obrázek: náborové fáze.png
:alt:Rozbalte sloupec v kanbanovém zobrazení kliknutím na něj.

Každá fáze má pod názvem fáze barevný pruh, který poskytuje informace o stavu.
žadatele v dané fázi žádosti. Stavy barev jsou:

- „Zelená“ značka: žadatel je připraven pokročit do další fáze.
- :guilabel:`Červená“: uchazeč je zablokován v dalším postupu.
- :guilabel:Šedá“: žadatel ještě není připravený ani v současné fázi a
byli vyloučeni z další fáze.

Stav karty se nastavuje ručně. Chcete-li zvolit stav, klikněte na malé kolečko v
v levém dolním rohu žádosti o kartu. V okně se stavem se objeví okno s výběrem stavu. Klikněte na požadovaný stav
žadatel. Aktualizuje se ikona stavu i statusová lišta.

.. obrázek: nábor/status-doty.png
:alt:Stav aplikační karty a stavová lišta.

.. tip::
Název pro tři stavy („Ve výrobě“, „Připraveno k další fázi“ a „Zastaveno“)
:ref:`může být upravena <nastavení/upravit-fáze>`, pokud je třeba.

..._rekrutace/upravit fáze:

Upravte fáze
================

Stupně lze upravit, přidat nebo odstranit tak, aby odpovídaly konkrétním krokům v procesu náboru zaměstnanců ve firmě.

Nový stupeň
---------

Pro vytvoření nové fáze klikněte na ikonu „+“ vedle položky „Fáze“ a zobrazí se nový sloupec. Do něj zadejte
Název nové etapy do pole „Název scény“ a potom klikněte na „Přidat“.
objeví se nová sloupec a další nový stupeň je k dispozici pro vytvoření. Pokud nejsou potřeba žádné nové stupně, klikněte
kdekoli na obrazovce, abyste opustili novou fázi tvorby.

.. obrázek:recruitment/add-column.png
:alt: Plus pro přidání nové sloupce do stupňů Kanbanu.

..._přijímání zaměstnanců/změna fází:

Změnit scénu
------------

Změnit nastavení scény. Přejděte na jméno scény a zobrazí se ikonka „fa-cog“
V horním pravém rohu scény se objeví ikona „Nastavení“ ( ). Klikněte na
Klikněte na ikonu „Nastavení“ (vlevo dole) a zobrazí se nabídka. Pak klikněte na „Upravit“.
volba. Zobrazí se formulář „Upravit: (Stadium)“. Změňte si v něm cokoliv podle svého a
Klikněte na tlačítko „Uložit a zavřít“.

.. obrázek:recruitment/gear.png
:alt:Ikona převodovky se objeví při najetí myší nad názvem sloupce a zobrazí se v něm ikonou
se zobrazí po kliknutí.

...případně v režimu editace.

Editace formátu souboru
~~~~~~~~~~~~~~~

Formulář „Edit: (Stage)“ je místo, kde se nastavují parametry scény. Jedinou povinnou položkou
pole je :guilabel:`Jméno pódia`.

K vyplnění nebo změně jsou potřeba tyto pole:

- :guilabel:`Název scény“: Zadejte název pro scénu.
- :guilabel:`Šablona e-mailu“: Vyberte šablonu e-mailu ze seznamu. Pokud chcete
Vybraný šablonu se aktivuje při vstupu žádosti do fáze uchazeče a automaticky je odeslána e-mailová zpráva.
žadatel použil vybraný vzor.
- :guilabel:`Složené v Kanbanu“: Zaškrtněte políčko, abyste měli stupeň skrytý (skládaný) na všech stránkách.
v výchozím zobrazení.
- :guilabel:Přijatá fáze: Zaškrtněte políčko, pokud tato fáze ukazuje, že se uchazeč uchází o místo.
Když se karta uchazeče dostane do této fáze, na kartě se zobrazí vlaječka „Přijat“ ve vrchní části.
v pravém rohu. Pokud je tato políčka zaškrtnuta, používá se tento krok k určení data pronájmu.
žadatel.
- :guilabel:`Specifická pro pozici“: Pokud se tato fáze vztahuje pouze na určité pracovní pozice, vyberte „Pozice“
z nabídky volby. Můžete vybrat více pracovních pozic.
- :guilabel:`Zobrazit v odkazech“: Zaškrtněte políčko, pokud chcete tento krok vidět v seznamu *Odkazů*.
aplikace a umožňuje získat body za doporučení, když se někdo dostane na tuto úroveň.
Pokud je aktivní, objeví se pole „Body“. Zadejte počet bodů za doporučení.
Při vstupu do této fáze dostane zaměstnanec odměnu. **Referraly** musí být nainstalovány na
aby mohli tuto možnost využívat.
- :guilabel:`Bodů“: Pokud je zapnutá volba „Zobrazit v odkazech“, zadejte
počet bodů, které zaměstnanec získá, když se uchazeč dostane do této fáze.
- :guilabel:„Nápověda“: Existují tři přednastavené stavy nápovědy (barevné kruhy).
každého uchazeče o kartu a ukazují její stav. Tyto barvy jsou zobrazeny na horním okraji každé fáze
aby odrážely postavení uchazečů v dané fázi. Název štítku lze měnit,
Ale samotná štítka (barva) nemůže. Výchozí názvy a štítky jsou: :guilabel:`In Progress`
(šedá), :guilabel:`Blokovaná“ (červená) a :guilabel:`Připravená pro další fázi“ (zelená).
- :guilabel:`Poznámky k požadavkům“: Zadejte vnitřní poznámky pro tento krok, které popisují jakékoli požadavky na
na jeviště.

Smazat krok
------------

Pokud už není potřeba nějaká fáze, je možné ji smazat. Chcete-li odstranit fázi, přejděte na její název
přejděte na kartu „Nastavení“ (viz ikona v pravém horním rohu).
Klikněte na tlačítko „Nastavení“ (ikona „fa-cog“) a poté vyberte možnost „Smazat“.
Vyskytne se okno varování s dotazem „Opravdu chcete tento soubor smazat?“.
Tuto sloupec? Klikněte na tlačítko „Smazat“ pro odstranění sloupce.

.. důležité::
Pokud jsou v současné době uchazeči ve fázi, která je odstraňována, zobrazí se chyba při pokusu o
smazat stupeň. Záznamy v současné době na stupni potřebují buď smazání, archivace nebo
Přesunutí na jiný stupeň před smazáním stavu.

Šablony e-mailů
===============

Pro komunikaci s uchazečem má Odoo několik přednastavených e-mailových šablon.
Přednastavené e-mailové šablony a kdy je použít jsou následující:

- Šablona „Přijetí žádosti o zaměstnání“: tato šablona se používá k informování uchazeče
vědí, že jejich žádost byla přijata. Tato e-mailová zpráva je automaticky odeslána poté, co žadatel
je v nové fázi.
- Šablona „Nábor: Zajímavost“ se používá k tomu, aby uchazeč o práci věděl, že jejich
Životopis se trefil do oka personalistovi, který již vybral mezi telefonáty.
telefonický rozhovor nebo pohovor.
- Šablona „Nábor: Nezajímá mě“ se používá, když uchazeč
komunikuje, že již nejsou o pozici zájemci a děkuje za jejich čas.
a úvahy.
- Šablona: „Nábor: Odmítnuto“: tato šablona se používá v případě, že uchazeč již není ve výběru.
byli do funkce zváni.
- Šablona „Nabídka práce: Zajistit pohovor“ se používá k tomu, aby uchazeč věděl, že
Prošli přijímacími zkouškami a brzy budou kontaktováni.
zajistit si pohovor s personalistou. Toto e-mailové oznámení je automaticky odesláno, jakmile se uchazeč
v kvalifikačním kole.

.. poznámka::
Šablony e-mailů lze vytvářet, upravovat a mazat podle potřeby firmy.
Informace o šablonách e-mailů najdete v dokumentu :doc:`../obecne/spolky/email_template`.

Chcete-li ručně odeslat e-mail, klikněte na tlačítko „Odeslat zprávu“. Zobrazí se textové pole,
a e-mailovou adresu žadatele.

.. obrázek: nábor/kompozice.png
:alt:Odeslat e-mail z chatu.

Klikněte na ikonu „fa-expand“ v pravém dolním rohu
:guilabel:„Odeslat zprávu“ v chatovací oblasti. Zobrazí se okno „Sestavit e-mail“,
Pole „Odesílatel“ a „Předmět“ jsou předvyplněná. Do pole pro e-mailovou adresu se zadává
V poli „Předmět“ je uvedeno „(Název pracovní pozice)“, v těle zprávy je
výchozí hodnota je prázdná.

Použít přednastavený e-mailový šablonu, klikněte na ikonu „fa-ellipsis-v“ (vertikální
tlačítko „Elipsis“ v dolní části okna. Vyberte e-mailový šablonu, kterou chcete použít z rozevírací nabídky
menu.

Přednastavené e-mailové šablony mohou obsahovat dynamické položky, takže se do nich bude moci vložit jedinečné informace.
obydlené v e-mailu pro osobnější zprávu adresovanou uchazeči. Několik přednastavených e-mailů
Vybrat si můžete z předdefinovaných šablon. Podle vybrané šablony se upraví e-mailová hlavička nebo
může se měnit.

.. poznámka::
Pouze e-mailové šablony, které jsou pro daný model nakonfigurované, se načítají. Jinak
přednastavené v Odoo, ale pokud nejsou konfigurovány pro aplikaci náboru, pak
se v seznamu dostupných šablon nezobrazí.

Pokud je potřeba připojit přílohy, klikněte na tlačítko s ikonou „papírů“
v dolní části okna. Přejděte do složky s přílohou a klikněte na tlačítko „Otevřít“.
připojit ho. Chcete-li odstranit přílohu, klikněte na ikonu „fa-close“ (smazat)
právo na srážku.

Pokud je třeba provést změny v e-mailu, upravte jeho tělo. Pokud by měly být
Uložená na později, e-mail může být uložen jako nový vzor. Klikněte na
Tlačítko „:icon:`fa-ellipsis-v` :guilabel:`(vertikální elipsa)“ v dolní části okna a vyberte
Uložit jako šablonu. Následně jsou nabídnuty dvě možnosti buď přepsat existující šablonu nebo
Vytvořte nový šablonu. Klikněte na existující název šablony, abyste přepsali tuto šablonu nebo klikněte
:guilabel:`Uložit jako šablonu“ pro uložení nové šablony. V okně „Vytvořit e-mailovou šablonu“
okno se načítá. Zadejte název šablony do pole „Název šablony“ a klikněte
:guilabel:`Uložit“.

K odeslání e-mailu klikněte na tlačítko „Odeslat“ a e-mail bude zaslán uchazeči. E-mail se poté
Ve chatu se objevuje.

.. obrázek: rekrutace/odeslání dotazníku.png
:alt:Odešlete uchazeči dotazník, který se také nazývá formulář pro pohovor.
přednastavený šablonu.

.. viz též:
   - :doc:`pracovní příležitosti/nové zaměstnání“
   - :doc:`rekrutace/přidat nové uchazeče“
   - :doc:`rekrutace/organizace-pohovoru“
   - :doc:`nabídka pracovních pozic“
   - :doc:`prijimani-odmitani-kandidatu``
   - :doc:`rekrutace/analýza uchazečů“
   - :doc:`nabor/analýza zdrojů“
   - :doc:`recruitment/time_in_stage`
   - :doc:`nabor/výkon týmu“

..toctree::


pracovní příležitosti
nábor/příliv nových zaměstnanců
rekruitování/přijímání nových uchazečů
rekrutace/organizování pohovorů
rekruiter/nabídka pracovních pozic
přijímání/odmítnutí uchazeče
nábor/analýza uchazečů
rekrutace/analýza zdrojů
recruitment/doba v oblasti
recruitment/týmová výkonnost
