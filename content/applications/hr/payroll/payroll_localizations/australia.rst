=========
Australie
=========

... payroll/l10n_au/payroll:

.. důležité::
Odoo aktuálně probíhá proces, který jej připravuje na splnění požadavků STP Phase 2 a SuperStream.
Oznámení bude učiněno, jakmile budou moci společnosti používat Odoo pro mzdy jako jednotnou platformu.

Nastavení zaměstnanců
====================

Nastavení zaměstnance
-----------------

Vytvořte nového zaměstnance kliknutím na „Zaměstnanci – Nový“. Přejděte do nastavení.
tabu a konfigurovat například část „Australské mzdy“ (např. zda jsou
„Nezisková organizace“, pokud získají výhodu „Osvobození od daně“.
„Stav TFN“, „Typ zaměstnance“ atd.

.. obrázek: australia/payroll-employee-settings.png
:alt:Nastavení pro zaměstnance v australské lokalizaci mzdy.

Osobní údaje zaměstnance
----------------------------

Dále je nutné poskytnout některé osobní informace zaměstnanců pro splnění požadavků na mzdy.
Výplatní pásky a zpracování důchodových plateb. Otevřete informace o zaměstnanci:
tabulku a vyplňte následující pole:

- :guilabel:`Soukromá adresa“
- :guilabel:`Soukromá e-mailová adresa“
- :guilabel:`Soukromé telefonní číslo“
- :guilabel:`Datum narození“

.. obrázek: australia/payroll-employee-private.png
:alt:Soukromá informace zaměstnance pro australskou lokalizaci mzdy.

.. poznámka::
Odoo vás bude upozorňovat na chybějící údaje v různých fázích procesu.

Super účty a fondy
------------------------

Můžete přidat podrobnosti o důchodovém pojištění nových zaměstnanců v sekci „Důchodové pojištění“ uvedené na kartě „:guilabel: Super
Karta „Účty“. Klikněte na tlačítko „Přidat řádek“ a ujistěte se, že zahrnete pole „Členem od“
datum, číslo člena a „nadstandardní fond“.

.. Tip:
Použijte pole „Účast“ pokud má být příspěvek zaměstnance rozdělen mezi více účastníků.
peníze najednou.

.. obrázek:: australia/payroll-super-account.png
:alt: Konfigurace nadstandardního fondu a účtu pro lokální platbu v Austrálii.

Vytvořte nový :guilabel:`Super Fund`, zadejte jeho název a klikněte na :guilabel:`Create and
edit... Vložte do něj:

- :guilabel:`Adresa“
- :label:ABN
- :guilabel:`Typ“ (APRA/SMSF)
- jedinečný identifikátor (pro APRA: USI, pro SMSF: ESA)
- pouze pro SMFS: guilabel:"Bankovní účet"

.. obrázek: australia/payroll-super-fund.png
:alt: Konfigurace nadřazeného fondu pro lokalizaci australských platů.

.. Tip:
Spravovat všechny nadřízené účty a fondy přes:
Super fondy“ nebo „Super účty“.

.. důležité::
Odoo aktuálně probíhá proces, který by měl zajistit jeho kompatibilitu s SuperStreamem.

Smlouvy
---------

Jakmile je zaměstnanec vytvořen, vytvořte smlouvu o pracovním poměru kliknutím na ikonku :icon:`fa-book`.
„Smlouvy“ chytrý tlačítko nebo přes „Zaměstnanci -> Zaměstnanci ->
Smlouvy.

.. poznámka::
Jeden smluvní vztah může být aktivní pro jednoho zaměstnance najednou. Zaměstnanec však může být přiřazen
smlouvy v průběhu zaměstnání.

Vytvoření pracovní smlouvy: doporučené kroky
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. obrázek: australia/payroll-contract-flow.png
:alt: Doporučené kroky pro vytvoření pracovní smlouvy.

1. Základní smluvní informace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Vyberte „Datum zahájení smlouvy“ a „Práce“ (pevná nebo flexibilní).
pracovníci na dohodu o provedení práce (casual workers).
- Zapněte možnost „Typ struktury mzdy“ na „Australský zaměstnanec“. Tato struktura
Pokrývá všechny daňové schémata ATO.

... _mzdy/l10n_au/pracovní vstup - zdroj:

- (pokud používáte aplikaci Přítomnosti nebo Plánování) Vyberte pole „Zdroj vstupu do práce“ a definujte, jak
Pracovní doba a dny jsou zaznamenány na výplatním listu zaměstnance.

  - :guilabel:`Rozvrh směn“: pracovní záznamy se automaticky generují podle zaměstnance
pracovní plán, který začíná od data vzniku smlouvy.

... příklad::
Zaměstnanec pracuje 38 hodin týdně. Smlouva začíná platit od 1. ledna a dnes je datum 16. ledna.
Uživatel vytvoří výplatní období od 14. do 20. ledna. Výpočet hodin na výplatním lístku bude
automaticky vypočítáno na 38 hodin (5 * 7,36 hodin), pokud není čerpán neplacený volno.

  - :guilabel:`Přítomnost“: pracovní plán se ignoruje a vytváří se pouze záznamy o práci.
Po zadání docházky a odchodu ze zaměstnání v aplikaci Attendance můžete docházku importovat.
  - :guilabel:`Plánování“: pracovní plány jsou ignorovány a vytvářeny z
plánování směn v aplikaci Plánování.

.. důležité::
Časové listy neovlivňují vstupy práce v Odoo. Pokud potřebujete časové listy importovat do Odoo,
je možné importovat zadáním: „Mzdy --> Vstupy do práce --> Vstupy do práce“.

2. Karta Informace o platu
~~~~~~~~~~~~~~~~~~~~~~~~~

- :guilabel:`Druh mzdy“: vyberte „Pevná mzda“ pro plný a částečný úvazek.
:guilabel:`Mzda za hodinu“ pro pracovníky na částečný úvazek. Ten umožňuje přidání :guilabel:`Část
Procento zatížení.

.. poznámka::
Pro hodinové pracovníky by měl být v poli „Mzda za hodinu“ vyloučen příplatek za přesčas.

- :guilabel:`Plnění plánu platů“: v Austrálii jsou přijímány pouze následující frekvence výplaty mzdy:
:guilabel:`Denní“, :guilabel:`Týdenní“, :guilabel:`Dvoutýdenní“
:guilabel:`Měsíční“ a :guilabel:`Čtvrtletní“.
- :guilabel:"Mzda" /*period*: přidělte mzdu smlouvě podle frekvence výplaty.
Výplatní pásky a příslušné roční a hodinové sazby se vypočtou automaticky.

3. Australský seznam
~~~~~~~~~~~~~~~~

.. obrázek: australia/pracovní smlouva v Austrálii.png
:alt:Australský dodatek smlouvy.

- :guilabel:`Obecný“

  - Pokud je to vhodné, přidejte :guilabel:`Běžnou výplatu“.
  - Pokud chcete přidat srážkové platby v BAS, zapněte možnost „Vykazování v BAS - W3“
místo W2 (viz stránka ATO o srážkové dani z příjmu).
<https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/in-detail/instructions/payg-withholding-how-to-complete-your-activity-statement-labels#W3Otheramountswithheldexcludinganyamount>
(více informací)

- :guilabel:`Odchod z pracoviště“

  - Určete, zda jsou vaši zaměstnanci vhodní pro „Náhradu mzdy“.
  - Zadejte částku, kterou chcete odečíst za zaměstnanecké dary.
  - Zadejte částku, kterou jste obětovali na místo práce (např. výhody) (výplata mzdy).
o slevě.

- :guilabel:`Velmi přínosné příspěvky“

  - Přidejte nad rámec garantované slevy „Extra vyjednaná super sleva“.
  - Přidejte položku „Další povinné super“ podle průmyslových dohod nebo pracovních smluv.

- :guilabel:`Přímé plnění“

  - „Sacrifice Salary Superannuation“ umožňuje zaměstnancům obětovat část své mzdy.
v prospěch hlášených příspěvků zaměstnavatele na důchodové pojištění (RESC).
  - :guilabel:`Sacrifice Salary for Other Benefits“ jim umožňuje obětovat část své mzdy.
směrem k jinému druhu výhody (viz stránka ATO o slevách ze mzdy).
zaměstnanci <https://www.ato.gov.au/individuals-and-families/jobs-and-employment-types/working-as-an-employee/salary-sacrificing-for-employees>
(více informací)

....... poznámka::
Od verze Odoo 18 se nebere v úvahu slevový systém pro jiné výhody.
daň z přidané hodnoty (DPH).

... /mzdy/l10n_au/prilohy k mzdě:

4. Příslušenství k mzdě
~~~~~~~~~~~~~~~~~~~~~

Pokud má zaměstnanec dostávat další opakující se platby každý měsíc, ať už do nekonečna nebo
pro určitý počet období klikněte na tlačítko „Chytré tlačítko“ s ikonou „fa-book“ a textem „Přílohy mzdy“.
v kontraktu. Vyberte typ a popis.

.. poznámka::
V Austrálii existuje kolem 32 typů opakujících se srážek ze mzdy, které jsou většinou spojeny s
příspěvky na dítě a výživné. Pro více informací navštivte webovou stránku „Kontaktujte nás <https://www.odoo.com/help>“.
Zda lze pokrýt příspěvky z vašeho odvětví.

5. Prodloužit smlouvu
~~~~~~~~~~~~~~~~~~~

.. obrázek: australia/payroll-contract-run.png
:alt: Příklad běžné smlouvy.

Jakmile jsou všechny informace doplněné, změňte stupeň smlouvy z „New“ na
:guilabel:`Běhání“.

Připravte výplatní pásky
================

Pravidelný
-------

Výplatní lístky vytvoříte kliknutím na „Mzdy“ -> „Payslips“ -> „Batches“.
:guilabel:`New“, zadejte „Název sady“, vyberte „Interval“ a klikněte
:guilabel:`Vytvořit výplatní pásky“.

.. obrázek: australia/vyplatni-listy-vytvoreni.png
:alt: Kroky k vytvoření výplatních pásek.

Zaměstnanci na platové lhůtě lze filtrovat podle :guilabel:`Oddělení` a :guilabel:`Pozice v zaměstnání`.
Počet výplatních pásek v jednom balíku není omezen. Po kliknutí
:guilabel:`Vytvořit“, za každého zaměstnance v sekci „Čeká na vygenerování“ je vytvořen jeden výplatní lístek.
Mohou být před ověřením přezkoumány a upraveny.

.. obrázek: australia/payroll-waiting-payslips.png
:alt:Výplatní pásky vytvořené ve stavu čekání.

V zobrazení výplatního listu jsou dva typy vstupů:

- „Pracovní dny“ se počítají podle „Zdroje vstupu pro pracovní dobu“, který je nastaven na zaměstnanci.
smlouva <plat/l10n_au/pracovní vstup>. :ref:`Pracovní vstupy lze konfigurovat
podle typu: docházka, přesčas.
Sobotní sazba, nedělní sazba, sazba svátku atd.
- :guilabel:`Jiné vstupy“ jsou jednotlivé platby nebo částky různých typů
<platové rozvrhy/l10n_au/jiný typ vstupu> (příspěvky, paušální platby, slevy, odměny za skončení pracovního poměru)
pracovní doba v současném platovém období nemá mnoho společného s odměňováním za přesčasy a
:ref:`dříve nakonfigurované přílohy k mzdě <payroll/l10n_au/salary-attachments>“ jsou jednoduše
opakující se jiné vstupy připojené k smlouvě.

.. obrázek: australia/platove-listy-vstupy.png
:alt: Dny práce a další položky výplatního listu.

Pod záložkou „Výpočet mzdy“ je automaticky vypočítávána pravidla pro výplatní pásky na základě
zaměstnanci, smlouvy, odpracované hodiny, jiné typy vstupů a přílohy k mzdám.

Struktura mzdy *Australský zaměstnanec* má 35 pravidel pro výpočet mezd, která automaticky vypočítávají
dynamicky zobrazit podle vstupů z výplatních pásek.

.. příklad::

.. obrázek:: australia/payroll-payslip-salary.png
:alt:Tabulka výpočtu mzdy na výplatním lístku

V následujících pravidlech se vztahují na příklad výše:

   - :guilabel:`Základní mzda“: hrubá mzda před srážkami
   - :guilabel:`Mzdy v běžném čase“: částka, kterou je třeba přičíst k procentu zaručené mzdy
aplikován
   - :guilabel:`Sacrifice celkového platu“: zahrnuje 150 dolarů, které byly obětovány na důchodové spoření
   - „Placené příspěvky na životní náklady“: zahrnuje 10 dolarů (centy za km)
(případ)
   - :guilabel:`Příjmy ze závislé činnosti“: hrubá mzda odečtena od nezdanitelných částí
   - „Srážky ze mzdy“ a „Celkové sražené částky“: částky, které mají být odečteny
daňový základ
   - :guilabel:`Mzda čistá“: čistý plat zaměstnance
   - :guilabel:'Příspěvek nad rámec superannuation': v tomto scénáři je částka obětovaná
doplňkové důchodové spoření, které zaměstnanci vyplácí navíc k garantovanému důchodovému spoření
   - „Zaručená mzda“: od 1. července 2024 se počítá jako 11,5 % z běžného platu
výše příjmů

.. poznámka::
Od verze Odoo 18 byly aktualizovány nejnovější sazby daní (2024–2025) pro všechny mzdy.
pravidla a výpočty.

Mimo cyklus
------------

V Austrálii jsou mzdy vytvořené bez sestavení považovány za *mimo cyklus*. Vytvořte je
Přejděte na: „Mzdy“ -> „Částky za mzdu“ -> „Soukromé čísla“. Stejné pravidlo platí i pro výplatní pásky.
podat žádost, ale způsob předání výplatních pásek do ATO v rámci programu Single Touch Payroll
STP je trochu jiná.

.. důležité::
Od verze Odoo 18 není doporučováno přidávat mimořádnou výplatní pásku k již existujícímu souboru.

Dokončete platby
=================

Zkontrolujte výplatní pásky
-----------------

Jakmile bude párování platových výměrů uznáno za správné, klikněte na tlačítko „Vytvořit návrh“.
Také lze provést plat za plat, a to z důvodu kontroly.

To má několik dopadů:

- Označení sady a výplatních pásek jako „Dokončeno“.
- Vytvářet návrh účetního záznamu na základě jednoho výplatního lístku nebo jeden záznam pro celou sadu podle toho, jaké máte
Nastavení mzdy. V tomto bodě účetní mohou vytvářet záznamy, které ovlivňují výsledovku a rozvahu.
report a zpráva BAS.
- Příprava podání STP (nebo mzdových dat, které budou předloženy do ATO jako součást plnění STP).
Toto musí provést uživatel s rolí STP Zodpovědný, definovaný pod
:menu_selektor:„Mzdy -> Konfigurace -> Nastavení“.
- Připravit nadstandardní příspěvkové linie jako součást plnění požadavků SuperStream.
:guilabel:`Uživatel HR Super Send` vybraný pod :menuselection:`Mzdy --> Konfigurace -->
Nastavení.

.. obrázek: australia/payroll-stp-record.png


Podání údajů o mzdách do ATO
------------------------------

.. důležité::
Odoo aktuálně prochází procesem splnění požadavků STP fáze 2 a tento krok popsal
v tabulce ještě neposílala údaje do ATO.

Podle požadavků ATO musí být podání STP pro jednu výplatu provedeno nejpozději v den výplaty.
Proto před zaplacením pošlete svá data STP na ATO. K tomu klikněte
Ve sloupci „Pokladna“ zadejte „ATO“.

Na záznamu o platbě v STP se zobrazuje několik užitečných informací:

- upozornění v případě chybějících důležitých informací.
- automaticky vygenerovanou činnost pro uživatele STP.
- souhrn výplatních pásek obsažených v této platbě, ověřitelný z tohoto pohledu.

.. obrázek: australia/payroll-stp-record.png
:alt: Příklad záznamu STP.

Jakmile je připravena zpráva o STP, klikněte na tlačítko „Předložit ATO“ a poté si přečtěte a přijměte
související podmínky a ustanovení.

Platit zaměstnancům
-------------

Jakmile je podání k ATO dokončeno, můžete pokračovat v placení svých zaměstnanců.
přiřazování plateb, pamatujte na zadání účetních záznamů souvisejících s výplatní páskou před ověřením
platba.

Ačkoliv se můžete rozhodnout platit svým zaměstnancům individuálně, doporučujeme vytvářet hromadné platby.
z vaší platové pásce. Klikněte na položku „Plat“ v příslušné platové pásce a vyberte
„Převod kreditu ABA“ jako „Způsob platby“.

.. obrázek: australia/platová-metoda-vyplaceni.png
:alt:Vybrat způsob platby pro hromadnou fakturaci.

To má dva dopady:

- Označení sady a výplatních pásek jako :guilabel:`Zaplaceno“.
- Vytvoření platby s názvem „Splátka“ spojené se splátkovým kalendářem.

.. obrázek: australia/payroll-paid-batch.png
:alt: Příklad zaplacené sady výplatních pásek.

Při přijímání výpisu z banky v Odoo můžete nyní spárovat řádky s účtem.
Platba jedním kliknutím. Platba se neprověřuje proti výplatnímu listu v hromadném souboru a všechny individuální platby jsou provedeny najednou.
Pracovní smlouva, potvrzení o zaměstnání a výplatní pásky.

.. obrázek: australia/payroll-reconciliation.png
:alt: Kroky k vyrovnání výpisu z účtu s platbou v hromadné platbě.

Dopad na účetnictví
--------------------

Podle konfigurace zaměstnance a smlouvy se při vazbě na mzdu zobrazí záznam
více či méně kompletní.

.. příklad::
Příkladem může být záznam z deníku, který vytvořil zaměstnanec Marcus Cook konfigurovaný výše.

.... obrázek: australia/výplatní účetnictví vstup.png
:alt: Příklad záznamu v deníku pro výplatní pásku

Jakmile je účet zadán, předdefinované účty ovlivní bilanci společnosti (PAYGW, mzdy a
povinností z důchodového pojištění) a výkazem o zisku a ztrátě (mzdami a náklady na důchodové pojištění).
Další změnou je aktualizace výše hrubé mzdy zaměstnance a srážkové daně v rámci hlášení BAS pro příslušný
doba (viz Tabulka daně: W1 a W2). Účty lze přizpůsobit účetnímu rozvrhu společnosti.

.. obrázek: australia/payroll-bas.png
:alt: Příklad výstupu z BAS pro paušální daň.

Jiné platové toky
===================

Placení super příspěvku
--------------------------

.. důležité::
Odoo má partnerství s centrálním depozitářem, který zpracovává jak platby za důchodové pojištění, tak i data.
převodem z účtu. V současné době probíhá proces přechodu na
v souladu s SuperStreamem a oznámení bude učiněno co nejdříve.
Příspěvky lze zpracovávat prostřednictvím řešení mzdy společnosti Odoo.

Jeden čtvrtletí (nebo častěji v přípravě na „Superúterý“)
<https://www.ato.gov.au/about-ato/new-legislation/in-detail/superannuation/payday-superannuation>
Musíte vyplácet důchodové penze zaměstnancům do jejich fondů pro státní důchody. Pro provedení této platby přejděte na
:menuvolba-->Mzdy-->Zprávy-->Přesahující příspěvky.

.. obrázek:: australia/payroll-superfile.png
:alt:Příklad nadřazeného souboru.

Při připravení platby přidejte pole pro bankovní účet, který bude použit k odeslání platby.
Klikněte na „Zamknout“, abyste zabránili přidání příspěvků z dalších výplatních pásek.
ten soubor. Namísto toho bude vytvořen nový soubor Super.

Jakmile je platba zpracována, lze ji v souboru Super sledovat a přiřadit k bance.
Prohlášení.

.. obrázek: australia/payroll-superfile-payment.png
:alt: Příklad platby za super soubor.

Odvolávání zaměstnanců
---------------------

Zaměstnanci mohou být propuštěni v menu: „Mzdy --> Zprávy --> Ukončit
Zaměstnanec.

Tyto pole je nutné vyplnit:

- :guilabel:`Datum ukončení smlouvy“: Jakmile bude platnost zrušena, tato data budou přidána do
smlouva automaticky vyprší a smlouvu označíme za „Vypršela“ v den splatnosti.
Dosáhla.
- :guilabel:`Kód ukončení“: pole, které je pro hlášení ATO povinné.
- :guilabel:`Typ ukončení“: typ ztráty zaměstnání (opravdová nebo neopravdová) ovlivňuje
výpočet nevyužitých ročních a dlouhodobých dovolených srážek.

.. obrázek: australia/payroll-termination.png
:alt:Ukončení pracovního poměru zaměstnance.

Pro přehlednost je zobrazena rovněž bilance nevyčerpaných dovolených a dlouhodobého pracovního poměru.

Potvrzením ukončení vytváří mimořádný výplatní list s štítkem :guilabel:`poslední plat“.
počítá pracovní dny do konce smlouvy a navíc nevyčerpané dovolené zaměstnance.
a dlouhodobé dovolené.

.. obrázek: australia/payroll-termination-payslip.png
:alt: Příklad mimořádné výplatní pásky zaměstnance, který byl propuštěn.

Odoo automaticky vypočítává nevyužité nároky na dovolenou podle aktuální hodinové mzdy zaměstnance.
zůstatková dovolená a zůstatek dovolené za kalendářní rok. Tyto částky však mohou být
pokud je třeba, může být ručně upraveno v tabulce „Další vstupy“.

Můžete také přidat platby za ukončení pracovního poměru (ETP) do tabulky „Další vstupy“.
obsahuje kompletní seznam vyloučených a nevyřazených ETP pro společnosti, ze kterého si mohou vybrat.

.. obrázek:: australia/payroll-termination-etp.png
:alt:Přidání odstupného.

.. poznámka::
Srážky za nevyčerpané dovolené a ETP se vypočítávají podle rozpisu ATO „Schedule 7
<https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment>
a „Příloha 11 <https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments>“
a aktualizováno k 1. červenci 2024.

.. tip::
Jakmile je zaměstnanec propuštěn a všechny podrobnosti jeho pracovního poměru vyřešeny, můžete
archivovat zaměstnance kliknutím na ikonu :icon:`fa-cog` (:guilabel:`Akce“).
:icon:`oi-archive` :guilabel:`Archiv“ v podobě formuláře zaměstnance.

Přechod z jiného softwaru pro správu projektů na Odoo
-------------------------------------------

Při přechodu z jiného softwaru s podporou STP na Odoo může být nutné zachovat kontinuitu
v hodnotách za celý rok vašich zaměstnanců. Odoo umožňuje importovat hodnoty za celý rok vašich zaměstnanců kliknutím na
„Mzdy“ -> „Konfigurace“ -> „Nastavení“ a kliknutím na „Import YTD“.
Balance“.

.. obrázek: australia/payroll-ytd-button.png
:alt:Tlačítko pro import roční bilance.

ATO by mělo uznat záznamy zaměstnanců vašeho předchozího softwaru a zachovat kontinuitu
Odoo, musíte zadat:

- :guilabel:`Předchozí identifikátor BMS“ (jedna pro každou databázi).
- :guilabel:`Předchozí číslo výplatního listu“ (jedno pro každého zaměstnance)

Pokud nemůžete najít identifikační číslo softwarového poskytovatele nebo čísla platů vašich zaměstnanců, obraťte se na svého předchozího dodavatele.

.. obrázek: australia/payroll-ytd-import.png
:alt:Import roční bilance.

Tímto získáte možnost přidat roční účetní zůstatky svých zaměstnanců v aktuálním
daňovém roce. ATO reportuje o mnoha různých typech YTD, které jsou reprezentovány číslem 13
přidružené kategorie „Mzdy“ v Odoo.

.. obrázek: australia/payroll-ytd-salary-rules.png
:alt:Pravidla pro výpočet mzdy zaměstnance.

.. příklad::
Řekněme, že zaměstnanec Marcus Cook byl převeden z jiného softwaru s podporou STP.
1. září. Marcus dostal za předchozí software dvě výplatní pásky měsíčně (za červenec a
A srpnu (August). Zde jsou roční zůstatky, které musí společnost Marca převést do Odoo:

...... seznamová tabulka::
:hlavičkové řádky: 1

      * - kategorie za celý rok
        - Zůstatek k převodu
      * -Gross (běžná návštěvnost)
        - $13,045.45
      * Gross (přes čas)
        - $1,000
      * – Placená dovolená
        - $954.55
      * - Příspěvek na praní
        - $200
      * - Celkové srážky
        - $2,956
      * -Supergarantie
        - $1,610

Pokud některé roční zůstatky musí být podrobněji vykázány na ATO, můžete použít plat.
vstupy pravidla.

.. příklad::
Příkladem může být pravidlo *Základní plat*, které může obsahovat šest vstupních proměnných a tři z nich jsou pro nás nezbytné.
Příklad: pravidelné hrubé mzdy, přesčasy a placené dovolené. Všechny se hlásí jinak.
v souhrnných číslech za celý rok.

.. obrázek:: australia/payroll-ytd-basic-rule.png
:alt:Přidání vstupů YTD

Finální roční účetní zůstatek pro Marca Cooka vypadá následovně.

.... obrázek: australia/payroll-ytd-final.png
:alt: Příklad závěrečného ročního účetnictví

Výpočet za letošní rok na výplatních páskách je proto založen na úvodním stavu zaměstnance namísto
od nuly.

Konečná úprava STP
----------------

.. důležité::
Odoo aktuálně probíhá procesem stát se součástí STP fáze 2 a finální fáze
Data popsaná níže zatím nejsou předávána ATO.

Závěr účetního období
~~~~~~~~~~~~~~~~~

Zaměstnavatelé hlásící se přes STP musí podat konečnou deklaraci nejpozději do 14. července každého roku.
Přejděte na: menu „Mzdy“ -> „Zprávy“ -> „Souhrnné zpracování“.

.. obrázek: australia/payroll-stp-eofy-finalisation.png
:alt:Ukončení pracovního poměru zaměstnance k 31. 12.

Zobrazují se jak zaměstnanci aktivní, tak i ti, kteří již nejsou v pracovním poměru.

.. obrázek: australia/payroll-stp-eofy-list.png
:alt: Seznam zaměstnanců k dokončení.

Z pohledu finálního tvaru můžete pokračovat s konečnou kontrolou všech výplatních pásek zaměstnanců.
během příslušného finančního roku. Jakmile je připraveno, klikněte na tlačítko „Odeslat do ATO“.
závěrečném prohlášení zaměstnanci uvidí změnu stavu svých platebních informací na
:guilabel:'Připraveno na daň' ve svém přehledu příjmů po skončení finančního roku.

Individuální dokončení
~~~~~~~~~~~~~~~~~~~~~~~

Odoo vám také umožňuje individuálně upravovat mzdy během roku, což se hodí například tehdy:

- Jednorázové platby jsou vyplaceny po první konečné úpravě.
- účetní uzávěrka po skončení pracovního poměru v průběhu roku.

Pokračovat v individuálním dokončení se přesune na: „Mzdy --> Zprávy --> STP
Ukončení, nezaškrtněte políčko „Deklarace konec roku“, ručně přidejte zaměstnance
Dokončit.

.. obrázek: australia/payroll-stp-individual.png
:alt: Individuální ukončení účetního období.

I když dokončíte záznam zaměstnance uprostřed finančního roku, ATO nebude
zadat do daňového přiznání zaměstnance informace až po skončení finančního roku.

Úpravy
-----------

.. důležité::
Odoo aktuálně prochází procesem přizpůsobení se STP fáze 2 a upravuje toky.
Popisované níže metody ještě neposkytují data pro ATO.

Doplnění konečného vypořádání
~~~~~~~~~~~~~~~~~~

Pokud potřebujete upravit částky za letošní rok pro zaměstnance po vyhotovení závěrečného prohlášení, je
Stále je možné odstranit u zaměstnance indikátor konečnosti. Pro provedení této akce přejděte na
V nabídce „Mzdy -> Zpracování mezd -> Uzávěrka STP“ vyberte zaměstnance a zanechte
Zatrhněte políčko „Dokončení“.

.. obrázek:: australia/payroll-stp-amend.png
:alt:Změna ročních částek zaměstnance.

Když bude hotovo, klikněte na tlačítko „Odeslat do ATO“ a zkontrolujte aktualizaci stavu u ATO.

Jakmile budou pro zaměstnance po úpravě k dispozici správné informace o výdělku za celý rok, ukončete práci s tímto zaměstnancem.
opět.

.. poznámka::
ATO očekává, že zaměstnavatelé opraví chyby do 14 dnů od jejich zjištění nebo v případě, že máte měsíční plat.
přesahující 14 dní (například měsíční) do data, kdy byste měli podat příští pravidelnou platbu
události. Změny konečného vypořádání lze provést prostřednictvím STP do pěti let po skončení
finanční rok.

Dokončování a úprava dokončení pro jednoho zaměstnance může být také užitečné při znovuobsazení
zaměstnance ve stejném finančním roce.

Úplné nahrazení souborů
~~~~~~~~~~~~~~~~~~~~~~

Zaměstnavatel může nahradit celé platby v souboru, aby nahradil poslední odeslaný výkaz.
ATO, pokud se ukáže, že obsahuje významně nepřesné údaje.

Pro toto provedení otevřete poslední podání STP a klikněte na „Vyměnit soubor“. Poté vyberte, který
Výplatní pásky je nutné obnovit zaškrtnutím políčka „Obnovení výplatního listu“.

.. obrázek: australia/payroll-stp-reset-payslips.png
:alt:Tlačítko pro nahrazení souboru.

Resetování výplatních pásek nezpůsobuje nové výplatní pásky ani nový výplatní běh, ale:

- Soubor výplatních pásek se vrátí zpět na stav „Zaplaceno“ nebo „Dokončeno“ a změní se na „Potvrzeno“.
- Stav výplatních pásek se vrátí na hodnotu „Návrh“.
- Ve správných výplatních páskách zůstane zaplaceno a vyrovnáno s původní platbou.
- Vytvoří se nová STP podání, které nahradí staré. Pro účely sledovatelnosti je zachováno původní
Příspěvek STP není smazán, ale je označen jako nahrazený.

Nejprve opravte chyby v nových výplatních páskách a vytvořte jejich návrh. Jakmile je hotovo, zadejte
ATO se znovu objevuje v souboru výplatních pásek, aby zpracoval plnou náhradu souboru.

.. obrázek: australia/payroll-stp-resubmit.png
:alt:Opětovné odeslání platového výměru.

Když bude hotovo, podávejte platby znovu na ATO. Prosím, zkontrolujte, že jde o plnou náhradu souborů.
pouze jako poslední možnost k opravě většího množství chybných údajů. Kdykoli je to možné, ATO
doporučuje opravit chybnou výplatní pásku podáním opravy v rámci dalšího vyúčtování
nebo prostřednictvím události aktualizace.

Dále není možné podat druhou plnou náhradu stejného souboru.
plné nahrazení souboru lze provést pouze jednou za 24 hodin.

Sčítání nulových hodnot za celý rok
~~~~~~~~~~~~~~~~~~~

Pokud dojde k pololetní změně několika klíčových identifikátorů, musí být hodnoty za první část roku nastaveny na nulu a poté
repostoval s aktualizovaným klíčovým identifikátorem.

Pro následujících **identifikátorů společností** musí být všichni zaměstnanci vymazáni:

- ABN
- Kód pobočky
- BMS ID

Pro následujících **identifikátorů zaměstnance** mohou být pouze jednotliví zaměstnanci vymazáni:

- TFN
- Číslo účtu na mzdovém listu

#Před aktualizací klíčových identifikátorů vytvořte novou žádost o STP přejděte na
:menuvolba:`Mzdy --> Zprávy --> Jednoduché zpracování mezd“ a:

   - Změňte :guilabel:`Typ podání“ na :guilabel:`Aktualizace“.
   - Zatrhněte políčko „Nulový výstup za celý rok“.
   - Klikněte na tlačítko „Přidat řádek“ pro specifikaci zaměstnanců.
   - Klikněte na tlačítko „Předložit ATO“.

.... obrázek: australia/payroll-stp-zero-out.png
:alt:Vytvoření nového podání STP, které vymaže hodnoty za celý rok.

#Jakmile je hotovo, upravte klíčové identifikátory tak, aby odpovídaly změněným informacím.

#Začněte v menu „Mzdy“ -> „Reporting“ -> „Single Touch Payroll“.
podat nové :guilabel:`Aktualizace“, tentokrát bez zaškrtnutí políčka „Nulovat roční údaje“.
To ATO oznámí, že dosud zaznamenané roční účetní zůstatky se mají upravit na novou hodnotu.
klíčové identifikátory.

Pracovní listy propojují s dalšími aplikacemi
===========================

Čas na odpočinek
--------

Aplikace „Čas volna“ je v Odoo nativně integrována s aplikací mzdy.
Různé typy výplatních pásek budou obsahovat záznamy o práci na základě konceptu „vstupů do práce“.

Přejděte na:menu: „Čas volna“ - „Konfigurace“ - „Druhy času volna“, a pro každý typ nastavte
dva pole pod sekcí :guilabel:`Mzdy“:

- „Typ vstupu do práce“: definuje, který typ vstupu do práce by měl být vybrán na „Vykonané práci“.
Dny v platovém výměru.
- :guilabel:`Nedoplacená dovolená“: vyberte mezi „Rok“, „Dlouhá služba“ nebo

V případě dovolené tohoto typu se nebude zobrazovat jako nárok při ukončení pracovního poměru.
listy typu :guilabel:`Roční“ budou zahrnovat náklady na odměňování zaměstnanců, pokud jsou kvalifikovaní.
it.

.. obrázek: australia/payroll-time-off.png
:alt: Konfigurace typů dovolené.

Náklady
--------

Aplikace pro evidenci výdajů je také nativně integrována s aplikací **Mzdy**
aplikace v Odoo. Nejprve přejděte na: „Náklady“ - „Konfigurace“ - „Nastavení“ a zapněte
:guilabel:`Vrácení peněz v potvrzení o výplatě“.

Když zaměstnanec na vašem platovém výměru podá žádost o proplacení schválených výdajů, můžete mu tyto náklady vrátit.
a to dvěma způsoby:

- Pokud chcete náklady vrátit mimo platovou periodu, klikněte na tlačítko „Vytvořit záznamy o pohybech“.
Zaplacení musí být provedeno ručně.
- Pokud je náklad hrazen jako součást další výplaty, klikněte na tlačítko „Zaúčtovat v příštím platovém období“.
„Pracovní smlouva“ namísto „výplatní pásky“.

.. obrázek: australia/plat-a-náklady-na-cestování-vyrovnají.png
:alt:Dva způsoby, jak se vypořádat s výdaji.

Po přidání výdaje do dalšího výplatního listu najdete v poli „Další vstupy“
tabulka. Tento typ vstupu je pak počítán jako přirážka k čisté mzdě.

.. obrázek: australia/platove-vydaje-vyplatni-list.png
:alt:Vrácení nákladů na výplatním lístku.

Po zaplacení zaměstnanci se v účetním deníku zaznamená položka související s náhradou zaměstnance.
automaticky se shoduje s fakturou dodavatele nákladů.

.. obrázek:: australia/payroll-expenses-journal.png
:alt:Příslušný záznam z účetní knihy zaměstnance, který se týká vrácení jeho výdajů.

Pokročilé konfigurace
=======================

.. _platová/l10n_au/další typy vstupů:

Jiné typy vstupů
-----------------

Další typy vstupů získáte přechodem na:
Typy vstupů“. Je zde celkem 63 dalších typů vstupu, které se týkají Austrálie. My nedoporučujeme používat
další jako součást vašeho systému mzdy, protože nelze použít v rámci STP. Můžete
archivovat nebo smazat je.

Na každém vstupním typu jsou důležitá následující pole:

- Třída PaymentType rozděluje vstupní typy do šesti kategorií:

  #:dodatečný příjem zaměstnancům navíc k platu
příplatky. Některé z nich jsou stanoveny současnými cenovými předpisy: praní, doprava atd.

.. důležité::
„Kontaktujte nás <https://www.odoo.com/help>“ pokud plánujete používat slevy, které se liší
sazby odpočtu (například „centy za kilometr“ nebo „cestovní náhrady“) a zjistit, zda Odoo
V současné době pokrývá vaši obchodní případ.

.. poznámka::
        - Od verze Odoo 18 existují některé příplatky, například:guilabel:`Praní: Příplatek pro schválený
uniformy jsou spravovány dvěma dalšími vstupy: jedním pro ubytování částky zaplacené do ATO
limitu a druhý pro uložení částky převyšující limit ATO.
aby Odoo vypočítalo správně PAYGW.
        - Některé podniky mohou vyžadovat převedení odpisu z „Otevřená“ na
:guilabel:`Mzdy a platby“ podle zaměstnance. V tomto případě musíte duplikovat a
přepracovat existující jiný typ vstupu. Například: guilabel:Work-Related
Nepožadovaná částka je v základním nastavení označena jako OTE.

  #:guilabel:`Odpočet“: odvody do odborového svazu a výživné jsou považovány za odpočty.
  #:guilabel:`ETP“: platby za ukončení pracovního poměru. Ty buď nejsou zahrnuty, nebo
nevyjmuté (viz „Stránka ATO o zdanění složek ETP <https://www.ato.gov.au/individuals-and-families/jobs-and-employment-types/working-as-an-employee/leaving-your-job/employment-termination-payments-for-employees/how-etp-components-are-taxed>“).
  #:guilabel:`Odejít“: další vstupy související s odchodem, které nejsou spojené se zvoleným obdobím
(jednorázová platba, vyplácení dovolené za službu, nevyčerpané dovolené atd.)
  #:guilabel:'Paušální částka': návrat do práce a paušální částka E (na zpětnou platbu) spadají pod tento
kategorie.
  #:guilabel:`Jiné“: jiné platby s vlastním specifickým logikem.

- Příznak :guilabel:PAYGW Treatment ovlivňuje způsob, jakým Odoo sráží daň pro tento vstupní typ:
:guilabel:"Běžný", :guilabel:"Žádné srážky z příjmu" a :guilabel:"Pouze přebytek" (pro
(příspěvky).
- :guilabel:`Důchodové zacházení“: :guilabel:`OTE“, :guilabel:`Mzda a mzdy“
:guilabel:`Není plat a mzda“.
- :guilabel:`Kód STP“: viditelný pouze v režimu pro vývojáře (:ref:`vývojářský režim <developer-mode>`), tento prvek ukazuje
Odoo jak hlásit hrubou hodnotu této platby na ATO. My nedoporučujeme měnit
hodnota pole, pokud byla nastavena výchozí hodnota.

Skupování jiných typů vstupu podle :guilabel:`Způsobu platby` může pomoci pochopit rozdíly
scénáře, ve kterých tyto vstupy mohou být použity.

.. obrázek: australia/payroll-and-other-input-types.png
:alt: Jiná vstupní pole, která jsou seskupena podle typu platby.

... _payroll/l10n_au/work-entry-types:

Typy vstupů do práce
----------------

*Typ záznamu práce* je typ docházky zaměstnanců (např. docházka, placené volno, přesčas,
atd.) a několik pracovních typů vstupu je v každé australské databázi vytvořeno automaticky.

.. obrázek: australia/payroll-work-entry-types.png
:alt: Výchozí typy pracovních vstupů pro australskou lokalizaci.

Před použitím řešení mzdy společnosti Odoo pro Austrálii je doporučeno zmenšit typy vstupů práce na
Ponechte si pouze ty, které potřebujete, kliknutím na: „Mzdy“ - „Konfigurace“ - „Vstup do práce“.
Typy

Pro každý typ nastavte následující pole pro Austrálii:

- :guilabel:`Je to OT“: určuje, zda je čas strávený v této kategorii považován za běžný
příjmy, což znamená, že se bude aplikovat sazba garance důchodového pojištění (např. pravidelná docházka)
placené volno, atd.
- :guilabel:`Sazba pokuty“: používá se k určení procenta sankce, která se vztahuje na dobu strávenou
v této kategorii. Důležité je, abyste si nastavili sazbu pokuty, která se vztahuje na vaši zemi
nebo podle druhu práce (např. sazba za sobotu, neděli, přesčas atd.)
- :guilabel:`Kód STP“: viditelný pouze v režimu pro vývojáře (:ref:`vývojářský režim <developer-mode>`), tento prvek ukazuje
Odoo, jak hlásit strávený čas v této kategorii na ATO. My nedoporučujeme měnit
hodnota pole, pokud byla nastavena výchozí hodnota.

.. obrázek: australia/pracovní smlouva/typ pracovního vstupu/konfigurace.png
:alt: Konfigurace pracovního typu vstupu.

Aktuální omezení
===================

Od verze Odoo 18 nejsou doporučovány společnosti k používání aplikace Payroll pro následující obchodní aktivity
povodí:

- Zdroje příjmů: Příjem ze zahraniční práce
- Daňová kategorie: herci a umělci
- Oznámení o úmrtí
- Zprávní povinnosti pro WPN (místo ABN)
- Příspěvky s proměnlivou sazbou odvodu (např. příspěvek za každý ujetý kilometr)
*cestovní náhrady*)

„Kontaktujte nás <https://www.odoo.com/help>“ pokud chcete zjistit, zda Odoo splňuje vaše požadavky
požadavky na mzdy v Austrálii.

... _payroll/l10n_au/employment-hero:

Spojení s aplikací Employment Hero
===========================

Pokud vaše firma již funguje s aplikací Employment Hero, můžete použít tento konektor jako
alternativní řešení mzdového účetnictví. Modul Employment Hero synchronizuje záznamy o platbách do účetnictví
(např. výdaje, sociální odvody, závazky, daně) automaticky ze systému Employment Hero do Odoo.
Mzdová agenda je stále vedená v Employment Hero, Odoo jen eviduje účetní doklady.

Konfigurace
-------------

#:ref:`Nainstalujte modul mzdy Employment Hero („l10n_employment_hero“).
#Konfigurujte službu Employment Hero API přejděte na: „Účetní -> Konfigurace ->
Nastavení“. Po zaškrtnutí položky „Zapnout Employment Hero“ se zobrazí další pole.
Zaškrtnutí položky „Integrace“.

.. obrázek:: australia/payroll-employment-hero-settings.png
:alt:Povolení integrace aplikace Employment Hero.

   - Najděte klíč API v sekci „Můj účet“ na stránce Employment Hero
platforma.

.. obrázek:: australia/payroll-employment-hero-api-key.png
:alt:Hledání klíče API pro aplikaci Employment Hero v sekci Moje účty.

   - V poli „URL mzdy“ je předvyplněno „https://keypay.yourpayroll.com.au“.

.... varování:
Nepřepisujte předvyplněnou hodnotu „URL mzdy“.

   - Najděte ID podniku v adrese URL Employment Hero (např. 189241).

.. obrázek:: australia/payroll-employment-hero-business-id.png
:alt:Nalezení identifikátoru podniku Employment Hero v adrese URL.

   - Vyberte jakýkoliv účetní deník jako :guilabel:`Mzdový deník`, do kterého budete vkládat záznamy o výplatách.

#Konfigurace daně se provádí v menu: „Účetnictví“ - „Nastavení“ - „Daně“. Vytvořte
potřebné daně pro výplatní pásky od Employment Hero. Zadejte daňový kód z Employment
Hrdina v poli „Daňový bonus pro zaměstnavatele“.

API vysvětleno
-----------------

API synchronizuje záznamy z knihy pracovních úkolů v aplikaci Employment Hero s Odoo a nechává je ve stavu návrhu.
reference zahrnuje identifikační číslo platové složenky od společnosti Employment Hero v uvozovkách, aby byl pro uživatele snadno dostupný.
stejný záznam v aplikaci Employment Hero a Odoo.

.. obrázek: australia/payroll-employment-hero-journal.png
:alt:Příspěvky na blogu Employment Hero v Odoo.

Synchronizace se provádí automaticky jednou za týden. Záznamy lze získat i ručně
Přejděte na: „Účetnictví“ -> „Konfigurace“ -> „Nastavení“ a v
Klikněte na „Nahrát platové výplaty ručně“.

Výplatní lístky společnosti Employment Hero fungují také na principu dvojího účetnictví. Účty používané
Nastavení mzdy je definováno v sekci Nastavení platů.

.. obrázek: australia/payroll-employment-hero-accounts.png
:alt:Hledání účtů Employment Hero.

Pro aplikaci API fungovat musíte vytvořit stejné účty jako výchozí účty vašich zaměstnanců.
Hero Business (stejný název a stejné číslo) v Odoo. Musíte také zvolit správnou variantu účtu
v Odoo vytvářet přesné finanční výkazy.
