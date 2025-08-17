==================
Příslušenství k mzdě
==================

Přídělek je část mzdy, která se přímo z výplatní pásky strhne na určitý účel.
ať už dobrovolné nebo povinné.

Když je srážka dobrovolná, obvykle se považuje za srážku. Když je srážka
soudně nařízené nebo dobrovolné se někdy označují jako „přikázání mzdy“. Ve verzi Odoo jsou
se všemi nazývají „příděly“.

Zaměstnanci mohou být také pravidelně odměňováni z příslušných mezd.
Jako odměna rozdělená do několika částí.

.. _pracovní smlouva/platové připojení/druhy:

Druhy srážek ze mzdy
=======================

Pro zobrazení aktuálně konfigurovaných typů příloh k mzdě přejděte na:
Konfigurace --> Druhy připojení k platům“. Výchozí typy připojení k platům jsou:
„Přidělení mzdy“, „Přidělování mzdy“ a „Výživné“.

Každý typ přílohy zobrazuje název přílohy,
Kód používaný při výpočtu mzdy, zaškrtávací políčko pro uvedení informace o tom, zda je :guilabel:
Datum ukončení a zda je toto datum specifické pro danou zemi (nebo univerzální).

.. obrázek:salary_attachments/attachment-types.png
:alt: Výchozí typy příloh k mzdovým výplatám.

Vytvořit nové typy příloh k platům
----------------------------------

.. nebezpečí::
Při instalaci aplikace **Mzdy** je přednastavená výchozí příloha mzdového listu.
typy jsou spojeny s různými pravidly, která se váží k různým platovým strukturám.
instalovaný balíček :ref:`lokalizace <fiscal_localizations/packages>`.

Není doporučeno měnit nebo upravovat žádnou z přednastavených příloh pro výpočet mzdy.
typu, zejména pokud byl dříve použit na výplatních páskách v databázi.
mohou ovlivnit různá pravidla pro výpočet mzdy a zabránit vytvoření mezd.

Nový typ přílohy mzdy lze vytvořit, ale měli byste tak učinit jen tehdy, pokud to je nezbytně nutné.
je nezbytné. Typ přílohy mzdy musí být propojen s pravidlem výplaty, aby byl považován za
v účetnictví mzdy.

Chcete-li vytvořit nový typ platby, klikněte na tlačítko „Nový“ a vyplňte
Formulář „Druhy připojení k platu“ se načte. Zadejte nové jméno pro plat.
druh přílohy do odpovídajícího pole. Poté zadejte kód platby, který se používá v mzdě
pravidla pro výpočet mzdy. Nakonec zaškrtněte políčko „Žádný konec“ pokud se jedná o přílohu
nevyprší.

Pokud je v databázi více společností s pobočkami ve více zemích, pak pole „Země“
je také k dispozici na formuláři „Druhy připojených platů“. Vyberte zemi, ke které se připojení
použijte nebo nechte prázdné, pokud je univerzální.

.. /pracovní list/vytvořit:

Vytvořte přílohu k mzdě
==========================

Všechny srážky ze mzdy musí být nastaveny zvlášť pro každého zaměstnance a pro každý typ platu.
příloha. Pro zobrazení aktuálně konfigurovaných příloh k mzdě přejděte na: `
app --> Smlouvy --> Přílohy k platu.

Všechny přílohy k platu se zobrazují v výchozím seznamovém pohledu a ukazují jméno
:guilabel:'Zaměstnanci', :guilabel:'Popis', příloha 'Mzda' a typ přílohy
„Měsíční částka“, „Datum zahájení“ a aktuální „Stav“.

Pro vytvoření nové přílohy mzdy klikněte na tlačítko „Nový“ v pravém horním rohu,
Vyplňte následující informace na formuláři:

- :guilabel:`Zaměstnanci“: Vyberte požadované zaměstnance z nabídky. Může jich být více
Mohou být uvedeny v tomto poli.
- :guilabel:`Popis“: Zadejte krátký popis přílohy s platem.
- :guilabel:`Typ mzdy“: Vyberte konkrétní typ přílohy mezd z rozevírací nabídky.
<platová/příloha k mzdě/druhy>.
- :guilabel:`Datum nástupu“: Vyberte datum, od kterého se má platit příloha
je v platnosti.
- :guilabel:`Odhadovaný konec“: Tento údaj je **neupravitelný** a **pouze se zobrazuje po
:guilabel:`Měsíční částka“ je vyplněna. Toto pole představuje odhadovaný termín, kdy bude zaměstnanci vyplacena mzda
Příloha se doplní. Datum dneška se do pole vkládá automaticky. Pak už stačí jen
Pokud je pole „Celková částka“ vyplněno, tento datum se aktualizuje.
- :guilabel:`Dokumenty“: Pokud je potřeba nějaké dokumentace, například soudní příkaz, klikněte na
:tlačítko „Nahrát soubor“ a otevře se okno pro práci s dokumenty. Vyberte požadovaný dokument
je připojit k příloze mzdy. Přílohu lze připojit pouze jednou.
- :guilabel:`Měsíční částka“: Zadejte do pole částku, kterou každý měsíc odečtete z výplaty.
- :guilabel:`Celková částka“: Toto pole se zobrazí pouze v případě, že je typ připojení mzdy
<platová pásma/přílohy k platům/druhy> nemá žádný termín konce (volba „Žádné datum“).
**nezaškrtnuto.**

.. obrázek: platove_prilohy/platova-priloha-vzor.png
:alt:Příloha s plně vyplněným formulářem mzdy.

Pokud se při vyplňování údajů o mzdě zobrazí pole pro uložení souboru, po vytvoření výplatní pásky
připojení k jednotlivému zaměstnanci není nutné žádné další kroky podnikat.

Pokud chcete vytvořit více mezd pro více zaměstnanců na jednom formuláři mzdy, po
Formulář vyplníte a klikněte na tlačítko „Vytvořit individuální přílohy“. Tímto způsobem vytvoříte
samostatné přílohy mzdy pro každého zaměstnance uvedeného v poli „Zaměstnanci“.

Po vytvoření samostatných příloh k platu se obrazovka vrátí na :guilabel:`Plat
Přílohový panel, ale s filtrem „Popis“ a obsahem vyplněným popisem
vyplnila v příloze k platu. Všechny přílohy k platu mají stav
„Běh“, protože jsou aktuálně aktivní. Zrušte filtr v poli vyhledávání, abyste viděli
Výchozí nastavení: panel Salary Attachment v celé jeho šíři.

Spravovat přílohy k platu
=========================

Přílohy k mzdě mají tři stavy: *běží*, *dokončeno* nebo *zrušeno*; pro zobrazení
Aktuální stav všech srážek ze mzdy, přejděte na: „Mzdy a personalistika“ --> „Smlouvy“.
-->Přílohy k platu“.

Všechny přílohy mzdy se zobrazují v pořadí, ve kterém byly nakonfigurovány. Chcete-li zobrazit přílohy
určité metriky, například „Stav“ nebo „Typ“, klikněte na název sloupce
seřadit podle konkrétní sloupce.

Dokončené srážky ze mzdy
----------------------------

Když je vytvořena příkaz k srážkám ze mzdy, má stav :guilabel:`Spouštěcí`. Jakmile jsou
připojení je dokončeno (*Celková částka*) zadaná v přihlašovacím formuláři pro platové připojení
Pokud je platba (v případě platby převodem na účet) provedena v plné výši, automaticky se stav změní na
*Dokončeno* a zaměstnanec už nemá peníze odebrány z budoucích výplat.

Pokud je splněna srážka ze mzdy, ale automaticky se nezmění na „Dokončeno“,
Záznam lze ručně aktualizovat. Chcete-li změnit stav, otevřete
navigace na:menu-selecetion:Mzdy - Smlouvy - Přílohy k mzdě.

Klikněte na záznam pro aktualizaci a zobrazí se podrobné okno „Příloha mzdy“.
individuální záznam „Příloha mzdy“, klikněte na tlačítko „Označit jako dokončené“.
v horním levém rohu a stav se změní na „Dokončeno“.

.. příklad::
Následující příklad ukazuje, kdy může být manažer mezd nucen ručně změnit plat.
připojení z aktivního stavu do stavu hotového.

Rose Smithová má soudní příkaz k výplatě náhrady škody, kde je povinna zaplatit
$ 3 000. Vytvoří se příkaz k úhradě, který každý měsíc odečte z výplaty Roseové 250 $.
směřovat k vyrovnání s obyvateli.

Roseová po šesti měsících zaplatila z platu 1 500 $. Získala zpět daňové odpočty a používá
peníze na úhradu zbývající části soudního vyrovnání. Po odeslání příslušné
dokument pro mzdového účetního, který ukazuje, že se platba vyrovnala v plné výši.
manažerka ručně změní stav svého přílohy s výplatou na „Dokončené“.

Zrušte srážky ze mzdy
-------------------------

Každé srážky ze mzdy lze kdykoliv zrušit. K zrušení srážek ze mzdy klikněte na
individuální záznam o připojení z hlavního panelu „Příloha mzdy“ k otevření
zaznamenána. Z rekordu „Příloha mzdy“ klikněte na tlačítko „Zrušit“, abyste zrušili
příloha k platu a přestat si nechat strhávat peníze z budoucích výplat.

.. viz též:
:doc:`priznak_platu“
