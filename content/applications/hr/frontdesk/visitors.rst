========
Návštěvníci
========

V aplikaci **Odoo Frontdesk** se jako návštěvník označuje každý nezaměstnanec (např. opravář).
kandidát na pracovní místo, auditor atd. Návštěvníků lze evidovat pro účely bezpečnosti,
zajištění přesného záznamu o tom, kdo je na pozemku.

.. _frontdesk/list:

Seznam návštěvníků
============

Pro zobrazení seznamu všech návštěvníků, kteří jsou na recepci, přejděte do aplikace Frontdesk:
Návštěvníci.

.. poznámka::
Výchozí nastavení filtrů „Plánované nebo Zkontrolované“ a „Dnes“ se zobrazuje v
:guilabel:`Hledat ...“ lišta.

Všechny návštěvníky je možné zobrazit v seznamovém pohledu s těmito detaily, které byly při kontrole vyplněny


- :guilabel:`Jméno hosta“: jméno hosta.
- :guilabel:`Návštěvní společnost“: společnost, kterou host reprezentuje.
- :guilabel:`Telefon“: telefonní číslo hosta.
- :guilabel:`Nápoje“\*: nápoj, který si host objednal.
- :guilabel:`Host“: koho host čeká.
- :guilabel:`Check-in“: datum a čas příjezdu hosta.
- :guilabel:`Checkout“\*: datum a čas odjezdu hosta. V výchozím nastavení se zobrazují pouze hosté
s :guilabel:`Zkontrolováno“ nebo :guilabel:`Plánováno“ jsou viditelné. Hosté s odjezdem
Časy jsou viditelné pouze tehdy, když je odstraněn filtr „Dnes“.
- :label_guid:`Délka pobytu hosta“: doba, po kterou byl host ubytován.
- :guilabel:`Stanice“: místo, kde se host ubytoval.
- :guilabel:`Stav“: stav hosta. Možnosti jsou :guilabel:`Přihlášen“,

- :guilabel:`E-mailová adresa hosta“\*: e-mailová adresa hosta.
- :guilabel:`Společnost`\*: společnost, kterou host navštíví. Tento prvek je k dispozici pouze v případě
databáze více společností.

*Tyto pole nejsou viditelná ve výchozím seznamu návštěvníků. Ty musí být povoleny pomocí
ikonu „Nastavení“ v pravém horním rohu
list.

Vpravo od nadpisů sloupců na stránce „Návštěvníci“ je nezařazený
sloupci, kde lze aktualizovat stav hosta.

Když host odchází, klikněte na tlačítko „Odhlásit se“ dostupné v záložce :guilabel:`Check out`,
a zaznamenat datum a čas, kdy opustili místo.

Pokud se na místě objeví očekávaný host, který nepřišel do hotelu přes **Check-in** kiosk, může být
z této seznamu, kliknutím na tlačítko „Zkontrolovat“ dostupné pod štítkem „Datum a čas zkontrolování“.
Kdy dorazili.

Kromě sloupce s nezařazeným stavem se objeví tlačítko „Nápoj podáván“ (drink served), ale pouze v případě, že
K určitému návštěvníkovi byl přinesen nápoj.

Když je nápoj připravený, klikněte na tlačítko „Nápoj připraven“ a označte nápoj.
je doručena hostovi a po kliknutí zmizí.

Na konci řádku se objeví tlačítko „Vytisknout štítek“ pro návštěvníky, kteří jsou v plánu.
**jenom**. Klikněte na tlačítko, abyste si stáhli soubor PDF s návštěvnickou kartičkou. Na kartičce je
datum a čas příjezdu návštěvníka, jméno a firma návštěvníka, koho navštívil, a
logo společnosti, kterou navštíví.

.. poznámka::
Štítek v PDF formátu lze vytisknout na samolepicí etikety pro návštěvníky nebo na papír, který
je nutné je umístit do plastového štítku.

.. obrázek: návštěvníci/návštěvníci.png
:alt: Celý seznam návštěvníků, kteří jsou v současné době na místě s vyznačenými nápoji, které budou podávat.

Pokud není vidět žádná sloupec nebo pokud je viditelný sloupec preferován skrytý, klikněte na
:ikona: „Nastavení“ (adjust settings) ikona, která se nachází na konci horního řádku.
Tím se zobrazí rozbalovací nabídka s možnostmi sloupců, které je třeba zapnout nebo vypnout.
Ikona „(zobrazit)“ ukazuje, že sloupec je viditelný.

.. _frontdesk/planned:

Plánovaní návštěvníci
================

Když se očekávají hosté, jako jsou uchazeči o práci, úředníci nebo noví dodavatelé, může být
Pro návštěvníky je užitečné zadat informace o sobě předem. Když se návštěvníci dostanou na místo, mohou využít
Možnost „Rychlého přihlášení“ na kiosku namísto zadávání všech informací ručně při
příjezd.

Vstupte do aplikace Frontdesk a vytvořte plánovaného hosta s očekávanými informacemi.

Pro vytvoření plánovaného hosta přejděte do aplikace Frontdesk na kartu „Návštěvníci“ a klikněte
:guilabel:`Nový“. Poté zadejte stejné informace jako jakákoliv jiná osoba v seznamu návštěvníků
formulář hosta, který se objeví. Jedinými povinnými poli jsou jméno návštěvníka a
:guilabel:`Nádraží“, na které se očekává příjezd.

.. důležité::
Pokud je host připraven dopředu, musí být zapsán ze seznamu.
:guilabel:"Návštěvníci" stránka v aplikaci Frontdesk (:menuselection:"Aplikace Frontdesk --->
Pokud se plánovaný host přihlásí na pokladně, je zaregistrován samostatně.
plánovaný vstup hosta a jejich plánovaný vstup hosta zůstává uveden jako :guilabel:`Plánovaný`.

Status „Plánovaný“ u plánovaného hosta se mění pouze na „Přihlášen“, pokud
jsou kontrolovány uvnitř seznamu návštěvníků aplikace (:guilabel:`Visitors`).

Pokud hosté zaregistrují svůj příjezd na automatu, ujistěte se, že všechny záznamy jsou aktuální, a seznam hostů
že v současné době jsou na místě správně zadané údaje. Ujistěte se, že při příjezdu a odjezdu vyplníte správná data.
Proto se návštěvní seznam správně zobrazuje, kdo je v tuto chvíli na pozemku.

Zajistěte, aby plánovaní hosté byli informováni o tom, že se **nemají** přihlásit na pokladně, pokud jsou
byl ohlášen jako plánovaný host s předstihem.

Počet návštěvníků
============

Registrace návštěvníků
----------------

Když se návštěvník dostaví na místo, přistupuje ke :ref:`přístroji pro frontdesk <frontdesk/kiosk>`.
Klikněte na tlačítko „Přihlásit se“. Návštěvníkovi je zobrazeno, co bylo pro něj nastaveno.
Konkrétní stanici Frontdesk. Pokud je požadována jakákoli informace, pole zobrazí červenou
hvězdička (*). Návštěvník musí vyplnit požadované informace, aby se mohl zaregistrovat.

Po zadání všech informací klikne návštěvník na tlačítko „Přihlášení“.

.. poznámka::
V průběhu celého procesu odbavení se může po dobu deseti vteřin nic nedělat. Kiosk se vrátí na
hlavní přivítací obrazovka.

Plánované návštěvy
~~~~~~~~~~~~~~~~~~~~~~~~

Když se plánovaný návštěvník:ref:`<frontdesk/planned>` dostaví na zařízení, nejprve se obrátí na
:ref:`Přístupový kiosk <frontdesk/kiosk>`, pokud je naplánovaný návštěvník na daný den.
Vpravo od kiosku se objeví panel „Rychlé přihlášení“, který vás požádá o „Jste
Jeden z nich?“ Pod otázkou je seznam všech návštěvníků, kteří mají přijet tento den.

Klikněte na příslušné jméno v seznamu a zkontrolujte svůj příjezd.

Nápoje
------

Pokud by byly nápoje nakonfigurovány pro stanici, po stisknutí tlačítka „Zkontrolovat zůstatek“
Potvrzující obrazovka se načítá spolu s otázkou: „Chcete něco k pití?“

Návštěvník může vybrat buď „Ano, prosím“, nebo „Ne, děkuji“.

Pokud vyberou „Ano prosím“, objeví se obrazovka s výběrem nápojů a přednastavené
seznamuje s nabídkou a návštěvník pak vybrané zboží označí nebo pokud nechce nic,
Mohou klepnout na tlačítko „Nic, děkuji“ v dolní části obrazovky.

Pokud byl vybrán nápoj, zobrazí se:guilabel:`Děkuji za registraci! Nápoj je na cestě.
objeví se zpráva.

Oznámení
-------------

Jakmile se návštěvník zaregistruje, může navštívit osobu, kterou chce navštívit, a další uživatele.
které jsou nastaveny tak, aby se oznámily při příjezdu na přepážku, jsou upozorněny.
e-mailem, SMS zprávou, chatek „Diskuse“ nebo kombinací těchto tří možností.

Pokud návštěvník požádal o nápoj, uživatelé konfigurovaní jako :guilabel:`Lidé, kteří mají být upozorněni`,
Oznámení o přijetí nápoje se zobrazují v aplikaci *Discuss*. Zpráva je:
:guilabel:`(Jméno návštěvníka) právě zkontroloval/a vstup na místo. Požadoval/a (Název nápoje).“

Jakmile nápoj doručí hostovi, je za něj zodpovědný ten, kdo ho přinesl.
pro označení dodání nápoje.

Zaúčtovat nápoj znamená přejít na: „Aplikace Frontdesk --> Stations“ a vybrat
požadovanou kartu stanice s názvem „Nápoje“.

Otevře se seznam všech návštěvníků, kteří jsou na stanici zaregistrováni a čekají na nápoj.
tlačítko „Nápoj podaný“ na konci řádku pro návštěvníka, který byl obsloužen.
je označen jako čekající na nápoj, návštěvník se z tabulky vymaže.

Vyčkejte prosím
---------

Jakmile návštěvník dokončí své obchodní záležitosti a opustí prostory, je důležité zkontrolovat
Je třeba je vybavit přesnými záznamovými systémy.

Pro správné vyřízení návštěvníků přejděte na: „Aplikace Frontdesk --> Stanice“ a zvolte
Potřebnou kartu stanice s názvem „Nápoje“ (#) Nápoje. Po otevření se zobrazí seznam všech
návštěvníků, kteří jsou nyní zaregistrováni na této stanici.

Klikněte na tlačítko „Zkontrolovat“ poblíž konce řádku pro návštěvníka, který odešel. Jakmile
je označen jako vypůjčený, návštěvník se zobrazí na seznamu.

.. důležité::
Návštěvníci se neodepisují sami, když odejdou. Pro uživatele Frontdesku je důležité
aby si mohli zaznamenávat návštěvníky pro přesné účetnictví.

Vždy mějte přesný seznam osob, které jsou na pozemku v daný čas. To je důležité pro
zabezpečení a v případě nouze.
