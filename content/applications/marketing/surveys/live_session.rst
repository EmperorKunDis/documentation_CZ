====================
Ankety v reálném čase
====================

S aplikací *Odoo Surveys* mohou uživatelé zlepšit prezentace a ukázky produktů.
s funkcí *Živá seance*.

*Živá sekce* funguje stejně jako normální anketa, ale s moderátorem nebo hostitelem.
předkládá otázky účastníkům, zveřejňuje jejich odpovědi v reálném čase a řídí rychlost
průzkumu.

V průzkumech v reálném čase se účastníci připojí ke zkušenosti s průzkumem prostřednictvím vlastního URL adresy a přihlásí se.
s možností zadání hesla. Když začne průzkum, uvádí jeden dotaz za druhým.

Pak se diváci zúčastněných vzdělávacích institucí přihlásí s odpovědí buď na svém počítači nebo mobilním zařízení.
a po shromáždění odpovědí se moderátor všechny odpovědi účastníků zobrazí v reálném čase.
času, s výsledky každé odpovědi zobrazenými v grafu sloupců.

.. obrázek: live_session/live-session-concept-sample.png
:align:center
:alt: Zpracovaný koncept, jak vypadá výsledek otázky a odpovědi z živé seance v aplikaci Odoo Survey.

Vytvořit anketu živého průzkumu
==========================

Pro vytvoření průzkumu typu „Živý přenos“ začněte otevřením aplikace „Průzkumy“.
Přejděte na panel „Průzkumy“ a klikněte na tlačítko „Nový“, abyste zobrazili prázdnou formu pro vyplnění dotazníků.

Jedna z možností dotazníku (GuildLabel: „Dotazník“, „Živá seance“)
„Hodnocení“ nebo „Vlastní“, které jsou zobrazeny jako tlačítka v horní části dotazníku.
lze použít k vytvoření živého setu.

Vybráním možnosti „Živá anketa“ se však proces zjednoduší.
protože Odoo automaticky vybírá optimální nastavení a možnosti pro průzkum *Živé sezení*.
je vybrána.

.. důležité:
Pokud je v nabídce „Možnosti“ zaškrtnuto pole „Je certifikát“, zobrazí se na kartě „Možnosti“
Soubor dat z průzkumu nelze použít jako soubor dat ze živé seance.

Po výběru požadované možnosti „Vyplnit dotazník“ pokračujte na stránku :doc:`vytvoření průzkumu
<../surveys/create>` s otázkami a sekcemi <../surveys/questions>.

Při vytváření otázek pro anketu *Živé sezení* otevřete záložku „Možnosti“.
Vyvolat dialogové okno „Vytvořit sekce a otázky“, abyste zobrazili dialogové okno „Živé
Sekce Session s jedinou dostupnou funkcí: :guilabel:`Limit otázek“.

Pokud je zapnutá možnost „Časový limit otázky“, objeví se vedle ní nové pole, do kterého
Uživatel **musí** zadat požadovaný časový úsek (v sekundách), ve kterém má odpovídat
otázka.

.. obrázek: live_session/question-time-limit-option.png
:align:center
:alt:Časový limit pro otázky v aplikaci Odoo Surveys.

Karta Možnosti
-----------

Po vytvoření otázek pro anketu *Živé sezení* otevřete možnosti:
tabulku dotazníku pro další konfiguraci průzkumu.

Karta „Možnosti“ je rozdělena do čtyř sekcí: „Otázky“, „Čas“, „Pozice“ a „Zobrazení“.
Scoring“, „Účastníci“ a „Živá sekce“.

Otázky
~~~~~~~~~~~~~~~~~

Ať už je zvolena jakákoliv možnost v poli „Paginace“, průzkum *Živá seance*
*jenom* zobrazuje „Jedna stránka na otázku“ a bude se vždy automaticky přepínat do této volby.
Když je kliknutá tlačítko „Vytvořit živou seanci“, oficiálně začíná anketa s názvem „Živá seance“.

.. poznámka::
V poli „Stránkování“ je vybrána volba „Jedna stránka na otázku“.
výchozí a nejsou zde žádné další možnosti v sekci „Dotazy“.
:guilabel:`Živá seance“ tlačítko je vybráno.

Možnosti „Zobrazit postup“ a „Výběr otázky“ jsou stále funkční.
aktivní možnosti pro průzkumy v reálném čase, pokud si je přejete, ale nejsou **povinné**.

Ale funkce „Povolit roaming“ **není k dispozici** během průzkumu v reálném čase.
jakýkoliv, protože moderátor má kontrolu nad průzkumem a účastníci nemají žádnou kontrolu nad tím
otázku, nebo když ji uvidí.

Sekce čas a skóre
~~~~~~~~~~~~~~~~~~~~~~

Možnost „Časový limit pro průzkum“ je **nevztahuje se na živé průzkumy**.
tato možnost se ani nezobrazuje v části „Čas a skóre“ pod záložkou „Možnosti“.
Pokud je vybrána možnost tlačítka rádia „Živé hlasování“.

.. poznámka::
Zatímco možnost „Časové omezení průzkumu“ není pro živé průzkumy platná, každý
Zaškrtnutím políčka „Použít vlastní časový limit otázky“ může být otázka přidána s vlastním časovým limitem, který lze nastavit v záložce „Možnosti“.
pop-up okno s otázkami. Tyto časové limity pro konkrétní otázky fungují pouze u průzkumů typu „Živá seance“.

Pokud je to požadováno, může být použitá možnost „Hodnocení“ a následně „Požadované hodnocení (%)“.
k dispozici pro průzkumy typu „Živá seance“.

Pokud je však zapnutá možnost „Je certifikace“, pak průzkum nelze použít jako
*Živá anketa* průzkumu. Možnost „Je certifikace“ se v
V sekci „Čas a skóre“ v záložce „Možnosti“ pokud je aktivní „Živý přenos“.
je vybrána možnost typu průzkumu s tlačítkem.

Součásti účastníků
~~~~~~~~~~~~~~~~~~~~

V poli „Způsob přístupu“ je nastavené možnosti „Kdokoli, kdo má odkaz“.
anonymní průzkum je používán jako živá seance. Možnost „Kdokoli s odkazem“ **nemůže být**
změněno, pokud je vybrána možnost tlačítka rádia „Živé sezení“.

Možnost „Povinné přihlášení“ je k dispozici pro průzkumy typu „Živá seance“.
Pokud je vybrána možnost „Typ průzkumu: Živé hlasování“, obvykle se používá :guilabel:`Omezení
Pole pokusů se nezobrazí, pokud je zapnuto pole „Požadované přihlášení“.
Účastníci sezení mohou dotazník vyplnit jen jednou, protože moderátor je provede celým procesem.

Součástí je také sekce Live Session.
~~~~~~~~~~~~~~~~~~~~

Funkce pole „Kód sezení“ umožňuje uživatelům vytvářet jedinečné kódy pro účastníky, aby je mohli používat.
, abyste se dostali do průzkumu „Živé sezení“. Kód může být jakýmkoliv kombinovaným
písmena, číslice a symboly.

Záložka „Kód relace“ je **nepovinná**, nicméně je vítaná, protože přidává
úrovně exkluzivity průzkumu a bez :guilabel:`Session Code` se zobrazuje
následující pole „Odkaz na sezení“ se stává mnohem složitější.

.. důležité:
Pokud se nezadá kód session, účastníci mohou průzkumu přistupovat prostřednictvím
:guilabel:`Sessions Link“ bez potřeby hostitele a základní prvky živého
Ztrácí se tzv. session*, protože pak je průzkum jen obyčejným dotazníkem bez živého časování.
výsledky.

S kódem :guilabel:`Session Code` je v nezměnitelném poli :guilabel:`Session Link` URL
zjednodušený a končí kódem „Session Code“, který předchází řetězci /s/.

Příklad:
Pokud byl zadán kód „1212“ jako :guilabel:`Session Code`, URL v :guilabel:`Session
pole "Odkaz" začíná základní adresou databáze (např. „sample-database.odoo.com“), následuje
podpisem: „/s/1212“.

Takže kolektivně by tento vzorec měl být:
„sample-database.odoo.com/s/1212“.

..tip:
Pokud uživatel odesílá celou adresu URL Session Link – Session
„Kód“ a všichni účastníci by nemuseli zadávat kód, protože už byl zadán.
pro ně. Toto plné propojení umísťuje účastníka do virtuální čekárny, kde jednoduše
musíte čekat, až se oficiálně spustí anketa *Živá debata*.

Pokud uživatel odesílá URL nástroje Session Link - *s výjimkou* Session Code
na konci (tj. celé URL včetně „…/s/“), účastníci byli přesměrováni na stránku
v nichž by museli zadat konkrétní kód Session, aby se dostali do
*Živá seance*.

Pokud je zapnutá možnost „Body“, máte možnost „Odměnit rychlost“.
Odpovědi jsou k dispozici také u průzkumů s živou seancí.

Zahájení živého průzkumu
==========================

Jakmile jsou všechny otázky a konfigurace dokončeny, uživatelé mohou kliknout na tlačítko „Vytvořit živý
Tlačítko „Session“ v horní části dotazníku. To otevře nové záložky prohlížeče na stránce *Session
Manager*

Když je kliknutá tlačítko „Vytvořit živou relaci“ a začala se *živá relace*,
Na dotazníku se objeví nový tlačítko „Správce otevřených relací“, které otevře nové okno prohlížeče.
tlačítko do *Správce relací*. Pokud uživatelé začali *Živou relaci*, tento odkaz je přesměruje na
otázka nebo část, na které se aktuálně nachází živá lekce.

Dále se na formuláři průzkumu objeví tlačítko „Ukončit živou relaci“. Po stisknutí tohoto tlačítka
kliknete na tlačítko „Pokračovat“, anketu Live Session ukončíte.

Správcem živé ankety je moderátor a ten také ovládá *Session Manager*.
obvykle promítané na projektor nebo obrazovku, takže účastníci mohou společně sledovat otázky
a reálné odpovědi, protože moderátor je s nimi během celé *živé seance* v kontaktu.

.. poznámka::
Účastník může odpovídat na otázky z počítače nebo mobilního zařízení.
Výsledky a reálné odpovědi lze vidět pouze na Session Manager.

Začátek *Správce relací* zobrazuje název průzkumu *Živé relace*, odkaz potřebný k
připojit se k němu a počítadlo „Čekáme na účastníky ...“, které se zaplní, jakmile se dostanou účastníci.
*Živá anketa*.

Jakmile se do ankety Live Session zapojí požadovaný počet respondentů, moderátor
Klikněte na tlačítko „Spustit“ v pravé části okna Session Manager.
*Živá sekce*.

.. poznámka::
Pokud začíná anketa sekcí na formuláři ankety, tento titulek se objeví v
*Správce relací* a účastníků průzkumu upozorňuje na „Vyplňte pozorně“.
„Hostující obrazovka do dalšího dotazu“. Tato zpráva se zobrazuje pokaždé, když se objevuje nadpis části.
během živého vysílání.

Když se objeví první otázka v průzkumu, zobrazí se otázka nad
Prázdná grafická osa s možnými odpověďmi na ose x. Účastníci vidí
otázku a výběr možných odpovědí na svém počítači nebo mobilním zařízení.

Jak se účastníci hlasování vyjadřují, postupová lišta v horním levém rohu *Session
Manager, doplňuje. Takto moderátoři pořadu Live Session vědí, že se každý účastník připojil
podali své odpovědi.

Pak, když se shromáždí požadovaný počet odpovědí, moderátor
kliknutím na tlačítko „Zobrazit výsledky“ v pravé části Session Manageru odhalí
Sběrné reálně v reálném čase odpovědi na grafu.

Hostitel/moderátor se pak cítí, že účastníci dostali dostatek času na sledování živého přenosu.
výsledky pomocí obyvatelné grafické osy mohou kliknout na tlačítko „Zobrazit správnou odpověď“
v pravé části okna Session Manager. To umožňuje vybrat správnou odpověď, pokud existuje
Označeny zeleně. Chybné odpovědi jsou zvýrazněny červeně.

Když moderátor pocítí, že účastníci dostali dostatek času na to, aby si vstřebali správné a
Nesprávné odpovědi lze zobrazit pomocí sloupcového grafu na Session Manageru.
Klikněte na tlačítko „Další“ a přejděte k další části dotazníku.

Opakujte tento proces, dokud nebude průzkum dokončený.

.. viz též:
   - :doc:`vytvořit“
   - :doc:`otázky“
   - :doc:`skórování“
