Zobrazit obsah

=========
Příspěvky
=========

Aplikace **Reference** společnosti Odoo je centrálním místem, kde se shromažďují všechny informace o doporučeních.
doma - od bodů získaných, spolupracovníků najatých a odměn vybraných. Uživatelé mohou doporučit lidi, které
pro pracovní pozice a poté získávat body za doporučení, jakmile lidé postoupí v
příliv nových zaměstnanců. Jakmile se nasbírá dostatek bodů za doporučení, lze je vyměnit za odměny.
Aplikace „Zaměstnanci“, „Nábor“ a „Webové stránky“ musí být nainstalovány pro aplikaci „Doporučení“.
fungovat.

Po instalaci aplikace **Referrals** je potřeba provést pouze několik konfigurací.
na odměny za doporučení (odkaz na soubor s názvem referrals/rewards); ostatní je přednastavené v Odoo Referrals.
je nainstalována.

Uživatelé s jednou z následujících rolí: „Případný uživatel“, „Důstojník“ nebo „Administrátor“.
Přístupová práva aplikace **Nabídky zaměstnání** mohou přistupovat do aplikace **Doporučení**.
Přístup s právy správce pro aplikaci „Nábor“ má přístup k
:dokumentu: „hlášení (referrals/reporting)“ a konfiguračních menu. Další informace o uživatelích a
přístupová práva se vztahují na tyto dokumenty: :doc:`../general/users`.
:doc:`../obecne/uzivatele/pristupovy-prav.

.. _přihlašování a onboarding:

Nástup do zaměstnání
==========

Když aplikaci **Referrals** otevřete poprvé, objeví se přednastavený nástroj pro přivítání uživatelů.
Tento skript se skládá ze čtyř snímků, každý z nich popisuje různé části aplikace **Referrals**.
Na horní části panelu se po celou dobu nástupu zobrazuje následující zpráva
prezentace: „Sbírejte svůj tým! Program doporučení zaměstnání“. Za touto hlavní zprávou je obrázek
A pod ním další vysvětlující text.

Každá ze slajdů obsahuje odpovídající obrázek a zprávu, která se zobrazuje po přečtení.
Každé zprávě klikněte na tlačítko „Další“ (ikona „fa-angle-right“) a přejděte na další obrázek.

Text, který se na každé snímku objevuje, zní následovně:

#:guilabel:`NO, VRAHY SE POTULUJÍ PO MĚSTĚ! POMOŽTE NÁM SLOŽIT TÝM SUPERHRDINŮ A ZACHRÁNIT
DEN!
#:guilabel:`Procházet otevřené pracovní pozice, propagovat je na sociálních sítích nebo doporučit přátelům.“
#:guilabel:`Sbírejte body a vyměňujte je za skvělé dárky ve svém obchodě.“
#:guilabel:'SOUTĚŽTE S KOLEGY, ABYSTE POSTAVILI NEJLEPŠÍ LIGU SPRAVEDLNOSTI!'

.. poznámka::
Slidey s přivítáním se zobrazí pokaždé, když je aplikace **Přátelské doporučení** otevřená, dokud nebudou všechny
slidy byly zobrazeny a tlačítko „Začněte nyní“ bylo kliknuto. Pokud se uživatelé přihlásili,
Pokud se aplikace kdykoli vypne nebo pokud tlačítko „Spustit nyní“ nebylo stisknuto,
Otevřením aplikace **Reference** se začnou znovu zobrazovat prezentační snímky.
:guilabel:`Začít teď“ tlačítko je kliknuté, onboardingové obrázky se již nezobrazí a
hlavní panel se načte, když je aplikace **Referrals** otevřena od této chvíle.

Kdykoli během procesu nástupu do zaměstnání klikněte na tlačítko „Přeskočit“ a otevřete hlavní okno **Zaměstnanec přivedl**
přístrojová deska.

.. obrázek: přihlašování/nástup do zaměstnání.png
:alt:Slide s přivítáním, na kterém jsou vidět tlačítka pro přeskočení a další.

.. poznámka::
Pokud jsou mezi uchazeči o zaměstnání nějací, které uživatel doporučil předtím, než byl otevřen seznam referencí **Referrals**
aplikace (což znamená, že se předchozí obrazovky s uvítacími informacemi neobjevily), když je tlačítko „Začni hned“
kliknutí na konci procesu onboardingu místo přechodu na hlavní panel, je :ref:`přijatý
místo toho se objeví obrazovka „Přidání zaměstnance“.

Úprava prezentačních snímků
---------------------------

Přednastavené prezentační snímky mohou být upraveny, pokud si to uživatel přeje.
Aplikace **Nábor** může upravit prezentaci při nástupu do zaměstnání. Chcete-li upravit prezentaci, přejděte na
menu: „Přidání referencí - Konfigurace - Nastavení.“ Každá řádka zobrazuje text pro
individuální prezentační snímek. Chcete-li upravit prezentační snímek, klikněte na jednotlivý řádek prezentace
přihláška na palubě tobogánu.

Udělejte jakékoliv změny v zprávě ve sloupci „Text“. Firma může být
vybrány také. Pokud je pole vyplněno, tak tato prezentace se zobrazí pouze pro tyto
konkrétní společnosti.

.. poznámka::
Pole „Firma“ se objevuje pouze v databázi více společností.

Obrázek lze také upravit. Po najetí myší na náhled obrázku v pravém horním rohu
formou ikony „Peněženka“ a „Smazat“.
zobrazit. Klikněte na ikonu „fa-pencil“ (Upravit) pro změnu obrázku. Souborový prohlížeč
okno se načítá. Přejděte na požadovanou fotografii, vyberte ji a klikněte na „Otevřít“. Nové obrázky
je zobrazena v náhledu. K odstranění obrázku klikněte na ikonu „Odstranit“
Poté vyberte nový obrázek pomocí ikony „Penál“ (Edit).

.. obrázek: přesměrování/přihlašování.png
:alt:Přípravná obrazovka pro editaci s vyznačenými hlavními poli.

Pořadí prezentací lze změnit z přihlašovací obrazovky. Klikněte na
:icon:`oi-draggable“:guilabel:"(draggable)" ikonu doleva od textu na snímku a přetáhněte snímek
na požadovanou pozici.

.. obrázek: odkazování/přijetí-přehled.png
:alt:Přihlašovací prezentace v seznamu s vyznačenými šipkami pro přetažení a pustit.

.. počet odkazů / zaměstnaných:

Pracovní doporučení
===============

Když je doporučený uchazeč zaměstnán, uživatel „roste svým týmem superhrdinů“ a přidává
avatary superhrdinů na své stránce s referencemi.

Po nástupu nového zaměstnance se při otevření aplikace **Referrals** místo hlavní obrazovky zobrazí
dashboard, načte se stránka s textem:guilabel:(JMÉNO REFERENTA) BYL PŘIJAT! Vyberte si avatar
pro nového kamaráda!“

Pod tímto sdělením jsou pět náhledů avatara k výběru. Pokud uživatel nějaký avatar má,
pokud je odkazováno na nějaký příspěvek, obrázek se ztmaví a uvede se jméno, pod kterým byl vybrán avatar
pod profilovou fotografií. Klikněte na volný avatar, abyste si jej vybrali.

Pokud od dokončení přijetí v aplikaci **Reference** bylo zaměstnáno více než jedno doporučení, po
Vybráním prvního avatara je uživatel vyzván k výběru dalšího avatara pro následné zaměstnance.
referral. Jakmile jsou vybrány všechny avatary, načte se dashboard a všechny avatary jsou nyní
viditelné. Po najetí myší na každou avatara se nad nimi zobrazí jejich jméno.

.. obrázek: odkaz na soubor avatary.png
:alt:Zaměstnaný obrazovka. Zde jsou předvedeny různé avatary k výběru, včetně již použitých.
Vybrané jsou šedivě označeny.

Změňte přátele
--------------

Avatary přátel lze upravovat stejným způsobem, jako :ref:`úrovně <referrals/levels>
upraveno. Pouze uživatelé s právy „Administrátor“ pro aplikaci **Nabídka práce** mohou provést
změny přátel. Přednastavení přátel lze vidět a upravit po kliknutí na
:menuselection:`Přesměrování aplikace --> Konfigurace --> Přátelé“. Každý přítel má svůj vlastní avatar
Sloupec „Obrázek“ panelu Dashboard a odpovídající název se zobrazí v poli „Přítel“.
Kolonka Jméno. Výchozí obrázky jsou pestrá skupina hrdinů od robotů až po psy.

Pokud chcete upravit obrázek, miniaturu, název nebo pozici přátel, klikněte na jednotlivého přítele.
otevřete formulář pro přidání doporučení. Do pole „Jméno“ zadejte jméno.
pouze pro rozlišení přátel v konfiguračním menu; jméno kamaráda není vidět
kdekoliv jinde v aplikaci **Reference**.

Pozice může být buď „Vpředu“ nebo „Vzadu“. To určuje
položka přátel vůči hrdinskému avatáři uživatele. Klikněte na příslušnou
požadované výběru a přítel se objeví buď před nebo za avatarem uživatele.
Aktivní.

Pokud si přejete, oba miniatury - „Obrázek“ a „Miniatura Dashboardu“ - můžete
upraveno. Přejděte myší nad obrázek, který chcete nahradit a zobrazí se ikonka „Penál“ :guilabel:`(Upravit)`
ikonu a :icon:`fa-trash-o` :guilabel:`(Smazat)` ikonu. Klikněte na :icon:`fa-pencil` :guilabel:`(Upravit)`
ikona a okno procházení souborů se zobrazí. Procházejte požadovaný obrázek, pak klikněte
Vyberte možnost „Otevřít“.

Zrušit všechny provedené změny kliknutím na ikonu „fa-times“ (Zrušení všech změn)
odstranit všechny změny a vrátit se k původnímu obsahu.

.. obrázek: přesměrování/edit-friend.png
:alt:Přítel v režimu pro editaci.

.. varování:
Není doporučeno upravovat obrázky. Obrázek musí mít průhledný pozadí, aby se na něj dalo kliknout.
aby se správně zobrazil. Pouze uživatelé, kteří mají znalosti o průhledných obrázcích, by měli
upravovat obrázky v aplikaci **Příkazy**.

Jakmile je obrázek změněn a přítel uložen, je **nelze vrátit zpět** na původní stav.
původní obrázek. Chcete-li se vrátit k původnímu obrázku, musí být aplikace **Reference** odinstalována a
znovuinstalováno.

.._přesměrování/úrovně:

Úrovně
======

Aplikace Referrals má přednastavené úrovně, které se odráží v uživatelově avatáru na
Dashboard s přehledem doporučení. Uživatelé mohou získávat body za doporučení potenciálních zaměstnanců a postupně se tak „proklikat“ na vyšší úroveň.
Máme pocit, že jsme v nějaké hře.

.. poznámka::
Úrovně nemají žádný vliv na výkon aplikace. Jsou používány jen pro
účelem přidání úrovní dosažených výsledků pro účastníky, kteří se mohou snažit o jejich dosažení.
uživatel.

Aktuální úroveň uživatele je zobrazena na hlavní stránce aplikace Referrals přímo
pod fotografií v závorkách „Level: #“. Kromě toho se kolem obrázku objeví barevný prstenec
fotografie uživatele, která ukazuje, kolik bodů má aktuálně uživatel a kolik dalších bodů
Musí se zlepšit. Modrá část kroužku znázorňuje body, které hráč získal.
Bílá část znázorňuje body, které ještě musí hráč získat, aby se mohl posunout na vyšší úroveň.

Upravte úrovně
-------------

Pouze uživatelé s právy :guilabel:`Administrator` pro aplikaci **Nábor zaměstnanců** mohou úrovně měnit.

.. varování:
Není doporučeno upravovat obrázky. Obrázek musí mít průhledný pozadí, aby se na něj dalo kliknout.
aby se správně zobrazil. Pouze uživatelé, kteří mají znalosti o průhledných obrázcích, by měli
upravovat obrázky v aplikaci **Příkazy**.

Jakmile je obrázek změněn a úroveň uložena, není možné vrátit se k původnímu
obrázek. Chcete-li se vrátit k původnímu obrázku, musí být aplikace **Referrals** odinstalována a
znovuinstalováno.

Přednastavené úrovně lze vidět a upravit po kliknutí na:
Konfigurace --> Úrovně“. Každý avatar se zobrazuje v sloupci „Obrázek“ a
Číslo úrovně se zobrazuje v sloupci „Název úrovně“ a výchozí obrázky jsou
Odoo hrdinové a každý další úroveň přidává další prvek do jejich avatara, jako jsou například kabáty.
Štíty.

Pro úpravu obrázku, názvu nebo bodů potřebných k dosažení daného stupně, klikněte na konkrétní stupeň.
V seznamu otevřete úroveň a pak provádějte změny.

Do pole „Název úrovně“ (nebo číslo) zadejte název nebo číslo úrovně.
Zobrazené pod fotografií uživatele na hlavní obrazovce, když dosáhnou takové úrovně.
Počet odkazů potřebných k dosažení této úrovně v poli „Povinnosti“ ve sloupci „Požadavky“.
Body potřebné k postupu jsou celkové body, které zaměstnanec za svou pracovní dobu nasbíral.
nejsou to další body z předchozí úrovně, které je třeba získat.

Pokud je to požadováno, lze také upravit obrázek. Při přejetí nad obrázkem se zobrazí
Ikona „Peněženka“ (Edit) a ikona „Odpadkový koš“ (Clear). Kliknutím
Ikona „Penál“ (Edit) se zobrazí spolu s oknem prohlížeče souborů, do kterého je potřeba přejít.
Potřebný obrázek, pak klikněte na tlačítko „Otevřít“ a vyberte jej.

Zrušit všechny provedené změny kliknutím na ikonu „fa-times“ (Zrušení všech změn)
odstranit všechny změny a vrátit se k původnímu obsahu.

.. obrázek: odkazování/úrovně.png
:alt:Úroveň forma v režimu úpravy.

Level up
--------

Jakmile se nasbírá dostatek bodů na postup o úroveň výš, objeví se kolem fotografie uživatele
celý je vyplněn modrou barvou a nad ním se objevuje velké zobrazení s nápisem:
fotografie a pod ní se objevuje text „kliknutím zvýšíš úroveň“
současné úrovni.

Klikněte na obrázek „Level Up!“, fotografii uživatele nebo text „Click to
LEVEL UP!“ pod fotografií uživatele, aby se uživatel „leveloval“. Avatar uživatele se změní na aktuální
úrovně a na obrázku se aktualizuje prstenec, který ukazuje současný počet bodů.

Levelování nevyžaduje žádné body, uživatel musí jen získat stanovený počet
požadovaných bodů.

.. obrázek: odkaz na soubor referrals/level-up.png
:alt: Pod obrázkem uživatele se zobrazí „Klikněte pro zvýšení úrovně!“ a velké „Zvýšení úrovně!“.
nad jejich obrazem.

.. poznámka::
Jakmile uživatel dosáhne nejvyššího nastaveného stupně, bude dál získávat body.
mohou být vyměněny za odměnu, ale již nemohou postupovat na vyšší úroveň. Prstenec kolem jejich fotografie
Zůstává pevně modrá.

.. viz též:
   - :doc:`referraly/sdílení pracovních pozic“
   - :doc:`odkazů/bodů“
   - :ref_reward
   - :ref-alert
   - :ref:reporting

..toctree::
přesměrování/sdílené pracovní pozice
přesměrování/bod
referraly/odměny
doporučení/upozornění
doporučení/hlášení
