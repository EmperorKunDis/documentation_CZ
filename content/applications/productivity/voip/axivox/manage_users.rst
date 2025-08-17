======================
Správa uživatelů v Axivoxu
======================

Správa uživatelů VoIP je důležitou součástí nastavení
:zkratka „VoIP (hlasová služba přes internetový protokol)“ v databázi Odoo. Každý uživatel Axivox má jedinečné jméno
telefonní číslo a případně i rozšíření, a hlasovou schránku. Díky tomu se na ně lze dovolat různými způsoby
Praktické způsoby.

Uživatelé Axivox jsou uspořádáni v jednoduchém a přehledném způsobem na konzole Axivox, takže
Administrátor může uživatele snadno a rychle spravovat.

.. poznámka::
Tato dokumentace popisuje, jak vše nakonfigurovat pomocí poskytovatele Axivox.
V závislosti na zvoleném poskytovateli VoIP mohou být procesy pro správu uživatelů různé.

Přehled
========

Začněte v konzole pro správu Axivox na adrese https://manage.axivox.com
<https://manage.axivox.com>`. Přihlásit se s příslušnými přihlašovacími údaji administrátora.

.. poznámka::
Akce v konzole pro správu Axivox **musí být** uloženy dvakrát, aby se změny zobrazily.
přijít v platnost. Chcete-li uložit změny, klikněte na tlačítko „Uložit“ v okně s individuálním nastavením.
Pak klikněte na tlačítko „Aplikovat změny“ v pravém horním rohu.
konzoly.

.. _voip/axivox/incoming_number:

Příchozí hovory
----------------

Vstupní čísla jsou všechna čísla, za která společnost platí, aby mohla přijímat hovory.

Klikněte na položku „Příchozí hovory“ v levém menu správy Axivox.
konzoli. To odhalí stránku „Příchozí čísla“, kde jsou všechna příchozí čísla
včetně jejich :guilabel:`Destinace“ a informací o SMS.

:guilabel:`Destinace` určuje akci, kterou se má provést nebo cestu, kterou musí volající následovat.
volání na uvedené číslo.

Chcete-li upravit cíl, klikněte na tlačítko „Upravit“ vpravo od
Změnit příchozí číslo. Pak se zobrazí stránka pro úpravu čísla, na které je
Můžete změnit typ cílového zařízení pro hlasové volání.

Možnosti, které jsou k dispozici v rozevíracím seznamu „Druh hlasového volání“, jsou
následuje:

- :guilabel:`Není nakonfigurována“
- :guilabel:`Doplnění“
- :guilabel:`Telefonní plán
- :guilabel:`Hlasová pošta“
- :guilabel:`Zavěsit telefon“
- :guilabel:`Konference“

Podle výběru v rozevíracím seznamu „Druh cílového hovoru“ se
Druhým krokem je naplnění dalšího rozbalovací nabídky s možnostmi konfigurace.
Dále se zobrazují další pole na základě výběru v poli :guilabel:`Destinace
Vyberte možnost „Hlasová hovor“.

Jakmile jsou požadované konfigurace dokončeny, klikněte na tlačítko „Uložit“ a poté na „Použít“.
změny v pravém horním rohu a poté je uplatnit.

Noví uživatelé
=========

Každý zaměstnanec společnosti, který používá VoIP (Voice over Internet Protocol), potřebuje uživatele Axivox
účet spojený s nimi.

Pro zobrazení stávajících uživatelů v konzole pro správu Axivox klikněte na položku „Uživatelé“ v nabídce
vlevo od konzole. Každý uživatel má :guilabel:`Číslo`, :guilabel:`Jméno` a možnost
:guilabel:„Hlasová pošta“, a „Číslo volajícího“ specifikované.

Pro vytvoření nového uživatele v konzoli Axivox klikněte na tlačítko „Přidat uživatele“ a zobrazí se „Nový
uživatelské formuláře. Následující záložky jsou k dispozici pro konfiguraci nového uživatele:

- :guilabel:`Obecné“: zde lze nastavit základní informace včetně přípony uživatele.
- :guilabel:`Přeposílání“: vnitřní přeposílání na signály „neodpovídá“ nebo „zaneprázdněn“.
- :guilabel:`Sleduj mě“: externí konfigurace směrování.
- :guilabel:`Klíče“: nastavte klávesové zkratky ve VoIP systému.
- :guilabel:`identifikátory SIP“: „uživatelské jméno a heslo pro protokol Session Initiation Protocol“
konfigurace zvenčí.
- :guilabel:`Povolení“: nastavte přístupová práva uživatelů v konzole pro správu Axivox.

Obecné nastavení
-----------

Na kartě „Obecné“ formuláře pro nového uživatele je v sekci „Doplnění“
pole, zadejte jedinečnou pro každého uživatele příponu. Toto je číslo, které interní uživatelé volají
dosáhnout konkrétního zaměstnance.

Do pole :guilabel:`Jméno` zadejte jméno zaměstnance.

Dále vyplňte pole „E-mail uživatele“. Platná e-mailová adresa pro
zde by měl být uveden zaměstnanec, který e-maily obchodního charakteru přijímá.

Do pole „GSM číslo“ zadejte alternativní telefonní číslo, na kterém se uživatel může dovolat.
Ujistěte se, že zadáte kód země.

.. poznámka::
Kód země je kódem, který umožňuje přístup do telefonního systému požadované země.
zeměpisný kód se volá jako první před cílovým číslem. Každá země na světě má svůj vlastní
specifický kód země.

Pro seznam všech zemí s kompletními kódy navštivte: https://countrycode.org
<https://countrycode.org>.

.. obrázek: manage_users/general-tab.png
:align:center
:alt: Vzhled obecného panelu v konzole pro správu Axivox.

V poli „Zanechat zprávu“ vyberte buď možnost „Ano“ nebo „Ne“.
kliknutím na tlačítko „Přidat do košíku“.

V poli „Adresář“ má správce možnost nechat pole prázdné, pokud se rozhodne
změnit nebo vybrat z nabídky „Výchozí“. Využívá se
v prvku funkce „Digitální recepční“ v telefonní ústředně.

Na spodní části záložky „Obecné“ jsou dvě samostatná pole s výběrovými políčky.

První možností je:guilabel:„Tento uživatel může přijímat hovory současně“. Po výběru
Tato možnost umožňuje přijímat hovory během jiného hovoru.

Druhá možnost „Tento uživatel musí přihlásit, aby mohl volat“ nabízí možnost umožnit mu
je pro uživatele povinné přihlášení.

.. poznámka::
Pokud společnost používá fyzické IP telefony na stolech a chce, aby její zaměstnanci mohli přihlásit
z jakéhokoliv telefonu nebo stolu v kanceláři by vybrali:guilabel:'Tento uživatel
„Pokud se chcete přihlásit, musíte zavolat.“

Jakmile jsou požadované konfigurace dokončeny, klikněte na tlačítko „Uložit“ a poté na „Použít“.
v pravém horním rohu.

.. _voip/axivox/přeposílání_tab:

Karta Přeposlání
---------------

Pod záložkou „Přeposílání“ v novém uživatelském formuláři může společnost rozhodnout, jaké
pokud někdo volá uživatele a hovor není přijat.

.. důležité:
Přeposílání je zakázáno, pokud je zapnuta možnost „Sleduj mě“.

Příkladem může být pole „Předání při nedostupnosti“, kde je tlačítko „Přidat“
Po výběru cíle se zobrazí možnost přidat konkrétního uživatele nebo telefonní číslo. Po
Při zadání cíle lze konkrétní časový úsek vybrat posunutím
:guilabel:`sekundová lišta“ na požadovanou dobu trvání zvonění.

Další destinace lze přidat s různými časy vyzvánění.

.. poznámka::
Časové okno může být rozloženo do několika částí, takže hovor bude přeposlán na další uživatele po prvním uživateli.
nepřijmout hovor. Možnost „Odeslat do schránky jako poslední možnost“ je k dispozici
správci, pokud by se Destinace nezachytila.

V poli „Přeposílání v případě přetížení“ může správce zaškrtnout „Přidat cílovou adresu“.
Když je kliknou, mohou pak nastavit cíl (uživatele) a časový rámec. Pokud
původní uživatelské VoIP (Voice over Internet Protocol) rozšíření nebo vstupní číslo je obsazené.
hovor je přepojen na cílové číslo.

.. obrázek: manage_users/forwardings-tab.png
:align:center
:alt: Spravovat přeposílání hovorů na různé uživatele nebo telefonní čísla v záložce Přeposílání.

Když jsou požadované konfigurace hotové, klikněte na tlačítko :guilabel:`Uložit`, pak klikněte na tlačítko :guilabel:`Použít
změny v pravém horním rohu stránky.

Sleduj mě
-------------

Když je zvolena možnost „Sleduj mě“, v záložce „Sleduj mě“ se objeví
Formulář „Nový uživatel“, nelze provést přesměrování.

Pokud je vybrána možnost „Sleduj mě“, tlačítko „Přidej cíl“
může být použito k přidání uživatelů nebo telefonního čísla do původního účtu uživatele.
takže tyto přidané čísla zazní, když je hovor přijat.

Po zadání cíle lze určit konkrétní časový rámec posunutím
:guilabel:`Vteřiny na obrazovce“ na požadovanou dobu trvání zvuku. Kromě toho lze přidat další :guilabel:`Země“
s různými časy vyzvánění.

.. poznámka::
Původní číslo uživatele VoIP (Voice over Internet Protocol) nezvoní.
Tuto možnost vyberte. Můžete také nastavit časové rozestupy, takže hovor bude přeposlán na jiného uživatele
po prvním nezvednutém hovoru.

.. obrázek: manage_users/follow-me-tab.png
:align:center
:alt: Můžete volat na různé telefonní číslo nebo jiného uživatele z karty „Follow me“.

.. důležité:
Aplikace Odoo nebo jiný klient SIP (Session Initiation Protocol) umožňuje
pro současné vyzvánění uživatelské linky nebo příchozího čísla. Další informace naleznete na
dokumentaci o integraci VoIP do mobilních zařízení.

Jakmile jsou všechny požadované konfigurace dokončeny, klikněte na tlačítko „Uložit“ a potom na tlačítko „Použít“.
v pravém horním rohu.

Klávesová zkratka
--------

Pod záložkou „Klíče“ v dialogovém okně pro nového uživatele lze provádět akce rychlého volání.
je možné je nakonfigurovat. K dispozici jsou i pokročilejší možnosti.

Následující možnosti jsou k dispozici pro nastavení na hodnoty 1 až 20.

Tyto akce lze nastavit na každé číslo:

- :guilabel:'Není konfigurováno': výchozí akce, která je nic.
- :guilabel:„BLF (busy lamp fields)“: tato akce zobrazuje stav telefonů ostatních uživatelů, kteří jsou připojeni.
do telefonního systému Axivox. Tento je primárně používán na stolním telefonu.
- :guilabel:Rychlý hovor“: Tato akce umožňuje rychlé volání na externí číslo.
- :guilabel:`Linka“: tato akce umožňuje uživateli zavolat jinému uživateli.
- :guilabel:`Přepínání hovorů“: tato akce umožňuje přecházet mezi hovory z telefonní ústředny.
- :guilabel:„Odpověď“: tato akce umožňuje uživateli přijmout hovor z telefonní ústředny.

.. obrázek:: manage_users/user-keys.png
:align:center
:alt: Spravovat stránku uživatele s vyznačenou záložkou Klíče a vybraným seznamem klávesových zkratek čísla 2.
zvýrazněte)

Jakmile jsou všechny požadované konfigurace dokončeny, klikněte na tlačítko „Uložit“ a poté klikněte
V horním pravém rohu klikněte na „Použít změny“.

.. důležité:
Mnoho z předchozích možností má také sekundární volby, které lze použít k propojení
uživatel nebo externí telefonní číslo. Tyto položky **musí být vyplněny v souvislosti s počátečním
akce.

.. poznámka::
V poli „Počet klíčů“ lze změnit hodnotu zadáním požadovaného čísla.
pole „Počet klíčů“, které se nachází na horním panelu záložky „Klíče“.
:guilabel:`Nový uživatel“ formulář.

Karta identifikátorů SIP
-------------------

*SIP* (Session Initiation Protocol) umožňuje volat a přijímat hovory.
přes internetové připojení. V záložce „Identifikátory SIP“ v novém uživateli
formulář obsahuje přihlašovací údaje potřebné k konfiguraci uživatelů Axivox v Odoo a/nebo jiném :abbr:`SIP
mobilní klient Session Initiation Protocol).

.. viz též:
Podívejte se na dokumentaci k konfiguraci Axivoxu pomocí SIP identifikátorů:

   - :doc:`Používejte služby VoIP v Odoo s Axivoxem <axivox_config>`
   - :doc:`AxiVox Mobile Integrations <../devices_integrations>`

V záložce „Identifikátory SIP“ je pole „Uživatelské jméno SIP“ reprezentuje uživatele.
informace zadaná do pole „Doplňující informace“ pod záložkou „Obecné“.

Záznam o doméně je přidán do systému zástupcem společnosti Axivox.

Hodnota v poli :guilabel:`SIP Password` je pro každého uživatele Axivo jedinečná. Tato hodnota se používá
přihlásit se do Axivo na Odoo a pro všechny mobilní klienty SIP (Session Initiation Protocol).

.. obrázek: manage_users/sip-identifiers-tab.png
:align:center
:alt:Důležité přihlašovací údaje používané pro externí konfigurace hlasových služeb Axivox.

Hodnota uvedená v poli „Adresa proxy serveru“ obvykle bývá:
„pabx.axivox.com“, ale může být změněna společností Axivox, proto si zkontrolujte :guilabel: „SIP
Zaškrtněte políčko pro nejlepší hodnotu.

Když jsou všechny požadované konfigurace hotové, klikněte na tlačítko :guilabel:`Uložit`, pak klikněte na tlačítko :guilabel:`Použít
v pravém horním rohu.

Karta oprávnění
---------------

Pod záložkou „Povolení“ v novém uživatelském formuláři je pole „Uživatelské jméno“
Do pole „Heslo“ lze zadat heslo pro uživatele.

Pod těmito poli mohou být uživatelům portálu Axivox udělena následující oprávnění:

- :guilabel:`Přístup do uživatelského portálu“
- :label:Zákaznický servis
- :guilabel:`Přístup správce“
- :guilabel:`Telefonní správa“
- :guilabel:`Správa uživatelských skupin“
- :guilabel:`Správa telefonních čísel“
- :guilabel:`Správa telefonního plánu“
- :guilabel:`Správa skupin pro vyzvednutí zboží“
- :guilabel:`Správa přepínačů“
- :guilabel:`Správa konferencí“
- :label:`Řízení fronty“
- :guilabel:`Správa hlasových zpráv“
- :guilabel:`Správa zvukových zpráv“
- :guilabel:`Správa hudby na čekání“
- :guilabel:`Správa adresářů“
- :guilabel:`Seznam hovorů“
- :guilabel:`Seznam připojených uživatelů“
- :guilabel:`Globální nastavení“
- :guilabel:`Použít změny tlačítko“
- :guilabel:`Stáhnout fakturu“
- :guilabel:`Podrobnosti faktury“
- :guilabel:`Správa černé listiny“
- :guilabel:`Správa účastníků konference“

Přihlaste se do portálu uživatele Axivox.
V záložce „Povolení“ zkopírujte uživatelské jméno a vložte správné
:guilabel:`Heslo“ pro uživatele. Minimální délka hesla je 8 znaků
heslo.

.. poznámka::
Tyto jsou stejné oprávnění udělené správcům Axivoxu, které se zobrazují v nabídce
v levém panelu správy v Axivoxu. Pokud je vybrána volba „Ne“, nebo
:guilabel:`Není přístup“, pak tato možnost nabídky nebude pro uživatele k dispozici.

Jakmile jsou všechny požadované konfigurace dokončeny, klikněte na tlačítko „Uložit“ a poté klikněte
V horním pravém rohu klikněte na „Použít změny“.

Po dokončení nastavení pro nového uživatele lze vytvořit :ref:`voip/axivox/incoming_number`.

.. obrázek: manage_users/user-permissions.png
:align:center
:alt: Spravovat stránku uživatele s vyznačenou záložkou Povolení, včetně prvního povolení
vyznačeny jako nevybrané.

.. _voip/axivox/user_groups:

Uživatelské skupiny
===========

Skupina uživatelů je seskupením uživatelů Axivox, které lze propojit s frontou call centra.
schopnost.

Chcete-li začít používat uživatelské skupiny, přejděte na adresu „https://manage.axivox.com <https://manage.axivox.com>“.

Pak se přihlaste s příslušnými administrátorskými přístupovými údaji. V levém menu najeďte myší na Axivox
administrativní panel, klikněte na „Skupiny uživatelů“.

Chcete-li přidat uživatelskou skupinu z stránky „Uživatelské skupiny“, klikněte na „Přidat skupinu“.

Pak zadejte název skupiny do pole :guilabel:`Jméno`. Pak přidejte člena
Skupinu vyhledáte zadáním prvních pár písmen uživatelova jména do pole :guilabel:`Členové`.
Uživatelé se vybírají v rozevíracím seznamu pod položkou pole. Pak stačí kliknout na požadovaného uživatele a jsou
přidán do uživatelské skupiny.

Tento postup opakujte, pokud chcete přidat další uživatele do skupiny.

Jakmile jsou všechny požadované konfigurace dokončeny, klikněte na tlačítko „Uložit“ a potom na tlačítko „Použít“.
v pravém horním rohu.
