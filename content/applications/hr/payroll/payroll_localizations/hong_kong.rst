=========
Hongkong
=========

.. payroll/l10n_hk/payroll:

.. důležité::
Zajistěte, aby modul „Mzdy v Hong Kongu“ („l10n_hk_hr_payroll“) byl nainstalován před
řízení.

... payroll/l10n_hk/create_employees:

Vytvářejte zaměstnance
================

Přejděte do aplikace „Zaměstnanci“ a klikněte na „Nový“. Poté nastavte následující
pole:

- Pod záložkou „Informace o práci“

  - :guilabel:`Práce“: musí být vybrán „Standardní pracovní doba 40 hodin týdně“.

- V záložce „Soukromé informace“

  - :guilabel:`Příjmení, Jméno, Čínské jméno`: jméno zaměstnance.
  - :guilabel:`Soukromá adresa“): adresa zaměstnance.
  - :guilabel:`Číslo účtu v bance“: číslo účtu zaměstnance.
  - :guilabel:`Současná nájemní smlouva“: záznamy o pronájmu zaměstnance (pokud se na nájem platí daň).
  - :guilabel:`Typ Autopay“: :guilabel:`BBAN“, :guilabel:`SVID“, :guilabel:`EMAL“, atd.
  - :guilabel:`Referenční číslo Autopay“: referenční číslo pro automatické platby.
  - :guilabel:`Číslo identifikace“: HKID zaměstnance.
  - :guilabel:`Pohlaví“: pohlaví zaměstnance.

.. důležité::
Pro účet :guilabel:`Bank Account Number` by měl být nastaven jako :guilabel:`Trusted
před dalším zpracováním.

Pro dosažení tohoto cíle klikněte na tlačítko s pravým směrem vedle pole „Číslo bankovního účtu“.
Nastavte :guilabel:`Send Money“ na :guilabel:`Trusted“ kliknutím na přepínač.

.. poznámka::
Přiřadit položku k aktuálnímu pronájmu, vyberte v seznamu „Historie“.
Poté klikněte na tlačítko „New“. Vyplňte potřebné údaje a uložte záznam o pronájmu.
uložením záznamu a smlouvy o pronájmu se zobrazí stav (vpravo nahoře):
a může být nastaven na :guilabel:`Běžný režim“.

- Pod záložkou „Nastavení HR“:

  - Vyberte možnost „Dobrovolná práce“ nebo „Pouze povinné“.
Příspěvek“, „S fixním %VC“ nebo „Kapacita 5 % VC“.
  - :guilabel:`Účet MPF Manulife“: číslo účtu, pokud je k dispozici.

.. _payroll/l10n_hk/manage_contracts:

Správa smluv
================

Jakmile je nový zaměstnanec vytvořen, klikněte na tlačítko „Smlouvy“
záznam zaměstnance nebo přejděte na: „Menu sekce: Zaměstnanci aplikace -> Zaměstnanci -> Smlouvy“.

.. poznámka::
Jeden smluvní vztah může být aktivní pro jednoho zaměstnance, ale zaměstnanec může být přiřazen
smlouvy v průběhu zaměstnání.

K uzavření smlouvy je potřeba splnit následující podmínky:

- :guilabel:`Typ struktury mzdy“: nastavte na „CAP57: Zaměstnanec v Hongkongu“.
- :guilabel:`Datum zahájení pracovního poměru“: datum nástupu do zaměstnání.
- :guilabel:`Plán práce“: nastavit na „Standardní pracovní dobu 40 hodin týdně“ (z karty zaměstnance).
- :guilabel:`Zdroj vstupu do práce“: vyberte buď „Rozvrh směn“, „Pracovní docházky“.
nebo :guilabel:`Plánování“. Tento prvek určuje, jak se pracovní záznamy započítávají v
pracovní smlouva, mzda a výplatní páska.

  - :guilabel:„Plán práce“: pracovní záznamy se generují automaticky na základě
pracovní doba zaměstnance.
  - :guilabel:`Přítomnost“: práce jsou generovány na základě zaznamenaného období přítomnosti
v záložce *Přítomnosti*.
  - :guilabel:`Plánování“: pracovní vstupy jsou generovány pouze z plánovaných směn.

- Pod záložkou „Informace o mzdě“

  - :guilabel:`Druh mzdy“: vyberte „Pevnou mzdu“ pro zaměstnance na plný úvazek nebo částečný úvazek.
:guilabel:`Mzda za hodinu“ pro zaměstnance, kteří jsou placeni hodinovou mzdou.
  - :guilabel:`Plánované platby“: frekvence vystavení výplatních pásek.
  - :guilabel:'Mzda': 'Měsíční' nebo 'Hodinová', podle toho, jaká je
Typ.
  - :guilabel:`Předplatné Internetu“: tento je **volitelný** prvek, který poskytuje další informace o internetovém připojení
přidat k současnému platu další platbu.

.. důležité::
Časové listy neovlivňují vstupy práce v Odoo.

Jakmile je vše nastaveno, změňte stav smlouvy na „V provozu“ kliknutím na
Tlačítko „Spustit“ v pravém horním rohu stránky.

.. obrázek: hong_kong/hk-smlouva.png
:alt: Smlouva o zaměstnání v Hongkongu.

... _payroll/l10n_hk/running_payslips:

Vytvořit výplatní pásky
=================

Jakmile jsou zaměstnanci a jejich smlouvy nakonfigurovány, mohou být vytvořeny výplatní pásky v modulu *Mzdy*.
aplikace

Odoo nabízí čtyři různé platové struktury podle nařízení CAP57:

#:guilabel:`Měsíční plat zaměstnanců CAP57“: zpracování měsíčního platu zaměstnanců.
#:guilabel:`Platba v náhradě výpovědi“: zpracování konečné platby při ukončení smlouvy
používajíc :abbr:`ADW (Průměrný denní plat)“.
#:guilabel:`Platba za dlouholetou službu CAP57“: platí pro zaměstnance s více než pětiletou praxí
služby po ukončení smlouvy.
#:guilabel:`CAP57: Odstupné“: platí pro zaměstnance s více než dvouletou službou
v případě ukončení smlouvy.

Před spuštěním výplatních pásek lze účty použité v pravidle o mzdě upravit kliknutím na
:menu-vyber->„Mzdy“ --> „Nastavení“ --> „Pravidla“.

.. obrázek: hong_kong/hk-salary-rules.png
:alt:Hongkongské pravidla pro výplaty.

Odoo může vytvářet výplatní pásky dvěma způsoby: buď prostřednictvím :ref:`batch <payroll/l10n_hk/batch_payslips>`, nebo
:ref:`příslušného zaměstnance <payroll/l10n_hk/employee_payslips>“.

.. _payroll/l10n_hk/batch_payslips:

Množstevní výplatní pásky
--------------

Tento způsob vytváření výplatních pásek se používá pro opakující se platby, protože více zaměstnancům
je možné spravovat najednou. Přejděte na: „Mzdy“ – „Pracovní smlouvy“ – „Sklady“.

#Klikněte na „Nový“.
#Zadejte „Název sady“ (např. „2024 – 1.“) a „Období“ (např. „01/01/2024“).
   `01/31/2024`).
#Klepněte na tlačítko „Vytvořit výplatní pásky“.
#Vyberte, jaký typ struktury mzdy chcete použít pro tento soubor. Filtr oddělení umožňuje
pouze na určitý okruh zaměstnanců.
#Klikněte na tlačítko „Vytvořit“.
#Vytvoří se automaticky tlačítko „Mzdy“.

Dále klikněte na tlačítko „Vytvořit návrh záznamu“ pro vytvoření návrhu zápisu zaznamenaného v
:guilabel:`Další informace“ v každém výplatním lístku. V okně „Potvrzení“ se objeví
:guilabel:„Opravdu chcete pokračovat?“. Klikněte na tlačítko :guilabel:„OK“ a vytvořte záznamy.

... _payroll/l10n_hk/individual_payslips:

Individuální výplatní pásky
-------------------

Přejděte na:menu: „Mzdy“ --> „Mzdové listy“ --> „Všechny mzdové listy“.

Tento způsob vytváření výplatních pásek se běžně používá k řešení jednorázových plateb (například
„CAP57: Platební náhrada za výpověď“, „CAP57: Odměna za dlouholetou službu“ nebo
:guilabel:`Částka odstupného“).

#Klikněte na „Nový“.
#Vyberte zaměstnance. Když je vybrán, vyplní se smlouva
automaticky.
#Přidejte platbu s názvem „Období“.
#Vyberte platbu: guilabel:"struktura" (např. "CAP57: měsíční plat zaměstnanců").
#V záložce „Práce a vstupy“ se automaticky počítají pracovní dny/hodiny a dovolené.
listy, které jsou aplikovatelné.
#Můžete přidat další položky výplatního listu (např. :guilabel:`Provize“).
:guilabel:`Odpočty“) pod záložkou „Jiné vstupy“.
#Klikněte na tlačítko „Výpočetní list“. Toto tlačítko aktualizuje
záložku „Výpočet mzdy“.

.. poznámka::
Pokud byl záznam o práci zaměstnance změněn, klikněte na ikonu :icon:`fa-cog` :guilabel:`(gear)`
Poté klikněte na tlačítko „Znovu vypočítat celý list“ a aktualizujte mzdu.
Tabulka „Vstupy“.

Karta „Splatnost“ zobrazuje podrobné rozdělení výpočtu na základě
platy stanovené pro každý typ struktury.

#:guilabel:`Příspěvek na nájemné“: částka vypočítaná z aktivní nájmové knihy zaměstnance.
#:guilabel:`Mzda v základu“: částka základní mzdy poskytnutá (po odečtení nájemného).
#:guilabel:`713 Gross`: nevyčerpaná částka po započtení *Provize*, *Přístup k internetu*
*Vrácení peněz*, *Zpětné platby*, *Odečty z platu*, atd.
#:guilabel:`MPF Gross“: čistá částka po odečtení dalších příspěvků
příspěvek na živobytí, slevy a roční platba.
#:guilabel:`Povinný příspěvek zaměstnance“: Příspěvek na důchodové pojištění ze strany zaměstnavatele.
#:guilabel:`Povinný příspěvek zaměstnavatele“: Příspěvek na důchodové pojištění od zaměstnavatele.
#:guilabel:`Gross“: čistá částka z MPF po odečtení odvodů do MPF.
#:guilabel:`Mzda čistá“: konečná částka, která má být zaměstnanci vyplacena.

.. důležité::
Do první měsíce se neplatí příspěvky z MPF. Přispívají oba, zaměstnanec i zaměstnavatel
začíná v druhém měsíci.

.. obrázek: hong_kong/hk-salary-computation.png
:alt: Výpočet mzdy v Hongkongu.

Pod záložkou „Další vstupy“ v záložce „Práce a vstupy“ je
další typy manuálního vstupu:

- :guilabel:`Zpětná platba“: do této kategorie lze zahrnout i příplatek za práci navíc.
- :guilabel:`Komise“: v tomto poli lze ručně zadat výši komise za období.
- :guilabel:`Paušální srážka“: paušální daň z celého výplatního listu.
- :guilabel:`Globální úhrada“: jednorázová úhrada celé mzdy.
- :guilabel:`Provize za doporučení“: další odměna, která je nabízena za jakoukoli formu obchodního doporučení.
- :guilabel:`Denní mzda“: převzít hodnotu :abbr:`ADW (Průměrná denní mzda)“, která se používá pro
zanechává výpočet.
- :guilabel:`Pronájemné: Pokud je zadáno, pronajaté bydlení se nezapočítává do aktuálního
pracovní smlouva, mzda a výplatní páska.
- :guilabel:`Průměrná měsíční mzda na míru“: aby se použila průměrná měsíční mzda
příspěvek na dovolenou (platí pouze pro výplatní pásky vytvořené v prosinci).
- :guilabel:`Doba výpovědi (měsíců)`: pouze pro :guilabel:`CAP57: Výplata v náhradě
základní mzdy společnosti Notice. Výchozí výplatou je měsíční plat.
:guilabel:`Počet“ pole v sekci „Další vstupy“ k nastavení jiného upozornění
doba trvání.

Po připravení výplatních pásek klikněte na „Výpočetní list“, následovaný „Zpracovat náčrt“.
vstupu vytvořit návrh záznamu do deníku, který je uveden v záložce „Další informace“ na výplatním lístku.

Platit zaměstnancům
=============

Jakmile jsou návrhy účetních záznamů zveřejněny, mohou společnosti nyní vyplatit zaměstnancům jejich mzdy. Uživatelé
vyberte si mezi dvěma různými způsoby platby:

- Z účtu zaměstnance (v aplikaci „Mzdy“ -> „Příjmy“ -> „Všechny příjmy“) se zobrazí
Při zadání záznamu o výplatě se objeví tlačítko „Registrace platby“. Po kliknutí na něj se spustí
Stejně jako: „Zaplacení faktur dodavatelům“ (viz: „Dokumentace: Zaplacení faktur dodavatelům“). Vyberte požadovanou banku
pak později vyrovnat platbu s příslušným výpisem z účtu.
- Pro hromadné platby (:menuselection:`Mzdy - aplikace --> Mzdy --> Hromadné platby“), jakmile je vytvořen návrh na účetní knihu
Pokud jsou položky z objednávky potvrzeny, klikněte na tlačítko „Zaplatit“
:vstup, pak vytvořte platbu v aplikaci *Účetnictví*.
a vyrovnat se s ní podle toho.

Příjmy a návštěvnost
===========================

Konfigurovat smlouvu pro zaměstnance placeného hodinovou mzdou pomocí aplikace *Pracovní doby*.
sledování, navigovat na:menu-selection:„Mzdy - aplikace“ --> „Smlouvy“ --> „Smlouvy“.
Vytvořte novou smlouvu. Důležité je si zapamatovat, že při vytváření smlouvy musí být nastavené
„Zdroj vstupu do práce“ jako „Přítomnost“, a „Druh mzdy“ jako
:guilabel:`Mzda za hodinu“.

Zaznamenat hodiny odpracované zaměstnancem pomocí aplikace *Přítomnost*:

#Přejděte na: menu-selection: `Návštěvnost aplikace`.
#Zaměstnanec může vstupovat a odcházet pomocí režimu kiosku a čas bude automaticky zaznamenán.
#V aplikaci „Mzdy“ v části „Zaměstnanci“ zkontrolujte záznamy o odpracovaných hodinách vygenerované z
:menu_selecce:`Mzdy - aplikace --> Vstupy do práce --> Vstupy do práce`.
#Poté vytvořte výplatní pásky a zpracujte platby.

.. obrázek: hong_kong/hk-attendance-work-entry.png
:alt: Pracovní vstup do Hongkongu.

.. obrázek: hong_kong/hk-attendance-payslip.png
:alt: Pracovní smlouva v Hongkongu.

Čas volna s platem
=====================

Typy vstupu do práce a typy volna jsou plně integrovány mezi aplikacemi
Aplikace pro výplatu mezd. Existuje několik typů dovolené a pracovního vstupu, které jsou specifické pro
Hongkongu, které se nainstalují automaticky společně s modulem *Mzdy v Hongkongu*.

Přejděte na :menuselection:`Mzdy --> Konfigurace --> Druhy pracovních vstupů“ a klikněte na :guilabel:`Nový“.

Při nastavení typu záznamu o práci je třeba zvážit dvě zaškrtávací políčka:

- :guilabel:`Použijte 713“: Zahrňte tento typ do výpočtu 713.
- :guilabel:`Neplněná mzda“: 80 % z :abbr:`ADW (Průměrný denní plat)“.

.. obrázek: hong_kong/hk-work-entry-type.png
:alt: Typ vstupu do práce v Hongkongu.

.. viz též:
:ref:`Vytváření a konfigurace pracovních vstupů <účetnictví/pracovní vstupy>`

Porozumění zákonu č. 713
===========================

Modul Hong Kong – Mzdy je v souladu s vyhláškou č. 713, která se týká
:zkr.:„Spočítání průměrného denního platu“ k zajištění spravedlivé odměny pro zaměstnance.

ADW výpočet je následující:

.. obrázek: hong_kong/hk-adw.png
:alt:Formule ADW z Hongkongu.

:abbr.: ADW (Průměrný denní plat) je celkový plat za 12měsíční období, odečteny jsou platy za
neplatná částka dělená počtem kalendářních dnů v 12měsíčním období odečtených od dní neplatného platu.

.. poznámka::
Pro č. 418 neexistuje automatické přidělování práv na volno v souvislosti s
zaměstnanci. Jakmile jsou splněny všechny požadavky, ručně přidělte dovolenou pomocí funkce
Aplikace Off*.

.. poznámka::
Před generováním výplatních pásek zkontrolujte stavy:guilabel:"Dokončeno", abyste ověřili výsledek.

.. seznam tabulkový::
:hlavičkové řádky: 1

   * – Období
     - Dny
     - Mzda
     - Komise
     - Total
     - ADW
     - Zůstatek
   * Jan
     - 31
     - $20200
     - $0
     - $20200
     - $651.61 ($20200/31)
     - N/A
   * Feb
     - 28
     - $20200
     - $5000
     - $25200
     - $769.49 ($45400/59)
     - N/A
   * -Mar (Jednodenní dovolená)
     - 31
     - $20324.33
     - $0
     - $20324.33
     - $730.27 ($65724.33/90)
     - $769.49
   * – Apr (1 den 80% nemocenské)
     - 30
     - $20117.56
     - $0
     -
     -
     - $584.22 ($730.27*0.8)

.. příklad::
Níže je příklad, který demonstruje logiku 713.

   - **Jan**: Vytvořte výplatní pásku s měsíčním platem 20200 $.
Je vždy vypočítávána na základě posledních 12 měsíců.
   - Únor: Vytvořte podobný výplatní lístek, ale přidejte do něj jiný typ vstupu
:guilabel:`Komise“.
   - **Mar**: Podat žádost o jednu plnou mzdu za dovolenou v březnu.
doposud byla vypočítávána na základě :abbr:`ADW (Průměrný denní plat)“.

.. obrázek:: hong_kong/hk-march-713.png
:alt:Hongkong, březen 2013.

   - **Duben**: Požádejte o jednodenní neplatovou dovolenou v dubnu. Protože se jedná o neplatovou dovolenou,
:zkratka ADW (průměrný denní plat) se počítá podle tohoto vzorce.

....... obrázek:: hong_kong/hk-apr-713.png
:alt:Hongkong, duben 2013.

.. poznámka::
Hodnota :abbr:`ADW (Průměrný denní plat)` se počítá v zadní části a není viditelná.
uživatel.

.. viz též:
   - „Nařízení HK 713 <https://www.labour.gov.hk/eng/public/wcp/ConciseGuide/Appendix1.pdf>“
   - „Nařízení HK 418 <https://www.workstem.com/hk/en/blog/418-regulations/>“

Vytvářet zprávy
================

Před vytvořením níže uvedených zpráv nastavte následující v aplikaci „Nastavení“:
Mzdy.

V sekci „Účetnictví“ nastavte následující:

- Zaškrtněte políčko „Mzdy HSBC Autopay“.

  - :guilabel:`Typ automatického placení“: nastavte na „Příjem z H2H“.
  - Vyberte bankovní účet, který chcete použít.

V sekci „HK Lokální“ nastavte následující:

- :guilabel:`Název zaměstnavatele se zobrazuje na výkazech“
- :guilabel:`Číslo spisového materiálu zaměstnavatele“
- :guilabel:`Manulife MPF Scheme“

.. obrázek: hong_kong/hk-report-setup.png
:alt: Nastavení mzdy v Hongkongu.

Zpráva IRD
----------

Všechny čtyři zprávy IRD jsou k dispozici:

- :guilabel:`IR 56B“: daňový přiznání zaměstnavatele k odvodům a důchodovým pojištěním.
- :guilabel:`IR56E“: oznámení o zahájení zaměstnání.
- :guilabel:`IR56F`: oznámení o ukončení pracovního poměru (zůstávající v HK).
- :guilabel:`IR56G“: oznámení o ukončení pracovního poměru (odcházíte z Hongkongu trvale).

Přejděte na položku „Mzdy“ -> „Zprávy“, vyberte jednu z možností „IR56B/E/F/G
Možnosti listu:

#Klikněte na „Nový“.
#Vyplňte potřebné informace pro zprávu o IRD.
#Klikněte na tlačítko „Obyvatelé“ a zobrazí se tlačítko „Zaměstnanci“.
#Stav „Zaměstnanecké prohlášení“ má stav „Návrh“ a byl změněn na
:guilabel:`Vytvořený PDF“ stav, jakmile se spustí plán.
#Jakmile je PDF vygenerováno, lze si stáhnout formulář IRD.

.. obrázek: hong_kong/hk-ir56b.png
:alt:Hongkongská zpráva IR56B.

.. poznámka::
Akce s názvem „Mzdy: Vytvořit PDF“ je naplánovaná a lze ji spustit ručně. Její nastavení
výchozí nastavení, které generuje PDF měsíčně.

Manulife MPF list
------------------

Přejděte na: „Mzdy a platby --> Zprávy --> List Manulife MPF“.

#Klikněte na „Nový“.
#Vyberte příslušné pole „Rok“, „Měsíc“ a „Číslo“.
#Klikněte na „Vytvořit soubor XLSX“.
#*. Soubor Manulife MPF XLSX je pak vytvořen a k dispozici ke stažení.*

.. obrázek: hong_kong/hk-manulife-sheet.png
:alt:Hongkongská Manuvie.

.. poznámka::
Odoo se nebude dále věnovat vývoji reportů pro dalšího správce fondu, protože brzy bude
eMPF, který zřídila místní samospráva.

.. viz též:
„eMPF <https://www.mpfa.org.hk/en/empf/overview>“

HSBC AutoPay Report
-------------------

Pokud je vybrána metoda platby v sérii HSBC Autopay, klikněte na tlačítko „Vytvořit HSBC Autopay
Report, vyplňte povinná pole:

.. obrázek: hong_kong/hk-generate-autopay.png
:alt: Hongkongská aplikace pro automatické platby HSBC.

Vytváří formát souboru .apc, který lze nahrát na portál HSCB k dalšímu zpracování.
