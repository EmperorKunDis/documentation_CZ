====================
Spojené arabské emiráty
====================

.. |Spojené arabské emiráty| nahradit za: zkratku `Spojené arabské emiráty (United Arab Emirates)`
.. |GCC| nahradit za: zkratku: `GCC (Gulf Cooperation Council)`
.. |DEWS| nahradí: zkratka: DEWS (Program konce služby společnosti Daman Investments)
.. |EOS| nahradit za: zkratka: `EOS (Konec služby)`
.. |WPS| nahradit za: zkratka: WPS (Systém ochrany mzdy)

Konfigurace
=============

Instalujte následující moduly, abyste získali všechny funkce **Spojených arabských emirátů.
Emiráty** **Mzdy a platové účetnictví** lokalizace:

.. seznam tabulkový::
:hlavičkové řádky: 1

   * Jméno
     - Technické označení
     - Popis
   * – :guilabel:Spojené arabské emiráty – Mzdy
     - „l10n_ae_hr_mzdy“
     - Zahrnuje všechny pravidla, výpočty a struktury mezd.
   * – :guilabel:`Spojené arabské emiráty – mzdy a účetnictví“
     - „l10n_ae_hr_mzdy“
     - Zahrnuje všechny účty související s modulem mzdy.

.. viz též:
:doc:`Dokumentace o fiskální lokalizaci Spojených arabských emirátů


Zaměstnanci
=========

Nejprve nastavte obecné informace o zaměstnanci podle návodu :doc:`zaměstnanec - základní údaje <../../employees/new_employee>`,
Vyplňte následující pole v záložce „Soukromé informace“:

- :guilabel:`Národnost (země)“: Národnost zaměstnance ovlivňuje jeho výplatní pásky, ať už
Jsou to buď národní občané, nebo přistěhovalci.
- :guilabel:`Číslo identifikace“: Používá se k extrahování zprávy :ref:`WPS
<mzdy/lokalizace_AE/wps-reporty>.
- :guilabel:`Bankovní účet“: slouží k vytažení zprávy :ref:`<payroll/l10n_ae/wps-reports>“.
generovat platby pro tyto zaměstnance.

.. poznámka::
Pole „Národnost (země)“ je nutné vyplnit i v případě, že zaměstnanec pochází z |UAE|
jejich národní, protože je jiný způsob zacházení s občany zemí GCC.

Smlouvy
=========

Jakmile vytvoříte tiskopis pro zaměstnance, ujistěte se, že je zapnutý kontrakt
Kliknutím na ikonu „fa-book“ nebo přechodem do
:menu:"Zaměstnanci --> Smlouvy".

Následující smluvní informace se týkají zaměstnanců pracujících v Spojených arabských emirátech
pod záložkou „Informace o mzdě“:

- :guilabel:`Druh mzdy“: vyberte „Pevnou mzdu“ pro zaměstnance na plný úvazek nebo částečný úvazek.
:guilabel:`Mzda za hodinu“ pro zaměstnance, kteří jsou placeni za hodinu.
- :guilabel:`Plánovaná platba“: frekvence vydávání výplatních pásek.
- :guilabel:'Mzda': 'Měsíční' nebo 'Hodinová', podle toho, jaká je
Type.
- :guilabel:Příspěvek na bydlení
- :guilabel:`Příspěvek na dopravu“
- :guilabel:`Další příspěvek“

.. poznámka::
Výše příplatku uvedená v pracovní smlouvě se používá na výplatních lístcích jako příplatek.

- :guilabel:`Počet dní dovolené“: Slouží k určení počtu dnů dovolené, které má zaměstnanec
a odpovídá tomu, kolik dní dovolené zaměstnanci skutečně připadne v daném roce.
(pracovní dny navíc pro některé vnitřní důvody společnosti), konečné vypořádání konce pracovního poměru
a nevyčerpané dovolené je závislá na čísle zadaném v tomto poli.

.. poznámka::
Počet dní dovolené ovlivňuje výpočet pro neplatné dovolené.

- :guilabel:`Je aplikována DEWS?“: DIFC Employee Workplace Savings (DEWS), pokud je zaměstnanec
|Národní občan Spojených arabských emirátů| a má |Přihlášku do programu DEWS| vyplněnou, zaškrtněte tuto políčko.
- „Výpočet podle denního platu“: Určuje způsob výpočtu konce služby:

  - Tuto políčko nezaškrtávejte, pokud má být použita výchozí kalkulace. Ta vypočítá
odškodné vydělit měsíční mzdou děleno 30 a pak násobit 21.
  - Zaškrtněte tuto políčko a přímým nastavením skutečného denního platu zajistěte, aby byl
použité při výpočtu konce životnosti.

Systém odměňování a platové předpisy
==================================

Jiné vstupní pravidla
-----------------

Následující jsou různé příplatky, které lze definovat přímo na tiskopisu :doc:`mzdy.
„<../platové pásky>“ umožňuje, aby hodnoty, které jsou proti těmto vstupům nastaveny, ovlivnily |WPS|
výpočet měsíční variabilní složky mzdy pro konkrétního zaměstnance, ke kterému jsou navázány.

Pravidla, která se týkají nastavení |WPS|, jsou propojena s jinými typy vstupů a pokaždé, když
použity, jejich hodnoty se odráží v |WPS| jako měsíční variabilní složka mzdy pro konkrétního zaměstnance.

+--------------------------------------+---------------------+
|Typ                                    |Kód                  |
+--------------------------------------+---------------------+
|:Přepravní příspěvek|:CONVALLOW
+--------------------------------------+---------------------+
|:Dávka na bydlení|:Dávka na bydlení|
+--------------------------------------+---------------------+
|:guilabel:Příspěvek na léčebné výlohy|:MEDALLOW:|
+--------------------------------------+---------------------+
|:roční povolenka|:ANNUALPASSALLOW|
+--------------------------------------+---------------------+
|:guilabel:'Příplatek za přesčas'|:guilabel:'PŘÍPLATEKZAPRÉSČAS'|
+--------------------------------------+---------------------+
|:Další příspěvek|:Ostatní příspěvky|
+--------------------------------------+---------------------+
|:guilabel:`Výplata dovolené“         | `VYPLATADOVOLENÉ“   |
+--------------------------------------+---------------------+

Konec služby (EOS)
--------------------

Konec služby (EOS) poskytuje výpočet pro příspěvek, který zaměstnanec dostane na konci
jejich služby. Spouští se v okamžiku, kdy je důvod odchodu zaměstnance nastaven archivací
personální spis zaměstnance.

Existuje několik různých výpočtů v závislosti na scénáři:

#„Zaměstnanec pracoval v této společnosti méně než rok“: Zaměstnanec nedostane žádné |EOS|
příspěvek, protože nemají na něj nárok (na příspěvek mají nárok až po dokončení svého prvního
v dané firmě).
#*Zaměstnanec strávil v dané společnosti více než rok, ale méně než pět let.*: Zaměstnanec
měli nárok na odpovídající částku za **21** dní mzdy za každý rok, který v této společnosti strávili.

.. poznámka::
Existují dvě možnosti výpočtu denního platu, který se vyplácí zaměstnanci v případě nemoci.
21 dní v měsíci EOS: Buď klasickým způsobem dělením měsíčního základu na 30. Nebo
může být ručně zadána do pracovní smlouvy zaměstnance v poli „Mzda za den“.

#*Zaměstnanec strávil v této společnosti více než 5 let*: Zaměstnanec je oprávněn požadovat odpovídající
za každý rok strávený ve firmě dostali 30 dní platu. V tomto případě byli zaměstnanci vedeni k tomu, aby
Pokud se používá tento postup, zaměstnanec dostane odpovídající mzdu za jeden měsíc a stanovené
V poli „Mzdový den“ se jim vypočítá částka za den vynásobená třiceti.

.. poznámka::
Existují dva formáty tiskopisu výplatních pásek, jeden pro normální platy a druhý pro odchod do penze
pracovní smlouvy, je založena na tom, že zaměstnanec byl archivován a má důvod k odchodu nebo ne.

Konec poskytování služeb (EOS Provision)
----------------------------------------

Ustanovení o EOS stanovuje výpočet částky pro ukončení služby, která
Společnost každý měsíc odkládá na úhradu EOS, které jim bude vyplaceno jako EOS.
příspěvek.

Na rozdíl od EOS je tato platba součástí mzdy zaměstnance již od počátku pracovního poměru.

Stejně jako u EOS má i tento příspěvek dvě výpočty podle doby strávené v
Zaměstnanec v této společnosti:

- Méně než 5 let: :math:`\frac{\text{Měsíční plat}}{30}\times{\frac{21}{12}}`
- Více než 5 let: :math:`\frac{\text{Měsíční plat}}{30} \times {\frac{30}{12}}`

.. poznámka::
Tato pravidla se zaměstnanci na výplatním lístku nezobrazují a nemají vliv na jejich čistou mzdu.
Pokud je splatná, slouží pouze pro vnitřní potřebu společnosti.

Ustanovení o dovolené
-----------------------

Pravidla pro dovolenou se používají k výpočtu dovolené získané každý měsíc.
Stejně jako u ustanovení o EOS se nepočítá do celkové částky, kterou zaměstnavatel zaměstnanci vyplatí.
pro vnitřní potřeby společnosti.

Je vypočítáváno dělením celkového platu zaměstnance (celkový plat = mzda + příplatky)
30, aby získal denní mzdu. Denní mzda se pak násobí počtem dnů dovolené a
a děleno 12, aby se určil měsíční příspěvek.

.. matematika::
:class: přesahující

\text{Měsíční dovolená} = \frac{\text{Celkový plat} \times \text{Počet dní dovolené}} {30}
\div 12

Poznámka k sociálnímu pojištění
------------------------------

Počítá se z nich sociální pojištění, které je dostupné pouze pro |UAE|
národní.

Společnost přispívá zaměstnanci na jeho celkový měsíční plat ve výši 15 % v případě, že je společnost
**Abu Dhabi** a **12,5 %** pokud je společnost v **dalším emirátu**.

.. poznámka::
Měsíční plat zaměstnance = (základní mzda + všechny příplatky, které jsou na pracovní smlouvě).

Zaměstnanec přispívá na penzijní spoření **5 %** z celkového měsíčního platu a tato částka
Odečte se z výplaty.

Pravidla pro zůstatek dovolené na konci roku
------------------------------------

Pravidla pro zůstatek dovolené za rok se používají k výpočtu částky, která má být zaplacena nebo odebrána.
zaměstnanci na základě počtu dní dovolené, které zaměstnanec v daném roce zaslouží.

Čas dovolené je specifikován pomocí :guilabel:`Time Off Type
Zaškrtněte políčko „Čerpání dovolené“.

Pokud je povolena, pravidlo spočítá počet dní dovolené, které zaměstnanec zaslouží k aktuálnímu datu.
datum a odečte počet dní dovolené, která byla vyčerpána, a pokud je výsledek kladný, znamená to
Zaměstnanec má nárok na odškodnění za zbylou částku a pokud je tato částka záporná, pak
zaměstnanec je povinen vrátit rozdíl zaměstnavateli.

Pravidla o nemocenské
----------------

Pravidla o nemocenském poskytují výpočet v případě, kdy zaměstnanec je na nemocenské a rozhodne
jak by měla být mzda ovlivněna.

Zaměstnanec může mít 3 případy:

#**Plně hrazená nemocenská:** Zaměstnanec může nahrát potvrzení o dočasné pracovní neschopnosti (SLI).
mohou využít **15 dní** dovolené tohoto typu za kalendářní rok.

.......
SLI není v Odoo povinné, ale lze ho nastavit z rozhraní pro správu :ref:`druhů volna.
<volno/druhy-volna>.

#**Placená nemocenská ve výši 50 %:** Stejná jako plně hrazená, ale zaměstnanci jsou oprávněni
**30 dní** od tohoto typu dovolené. Tyto 30 dnů se počítají po prvních **15** plně zaplacených
dní.
#**Nulová placená dovolená na nemocenské:** Stejná jako plně hrazená, ale zaměstnanci jsou oprávněni čerpat **45
dnů z této dovolené. Tyto **45 dní** se počítají po prvních **15/30**
pracovní dny plně nebo částečně hrazené zaměstnavatelem.

.. důležité::
Podle pracovního zákona Spojených arabských emirátů nejsou dny 15, 30 a 45 uvedeny jako
pracovní dny nebo kalendářní dny, takže se bude odvíjet od firemních pravidel.

Výše náhrady za nemocenské dny je počítána jako
pokračuje:

.. matematika::
:class: přesahující

\frac{Počet dnů dovolené × hrubá mzda za měsíc}{30} × procento

Kde hrubá mzda je základní plat plus všechny ostatní příplatky, které jsou v pracovní smlouvě zaměstnance uvedeny.

Program ukončení služby společnosti Daman Investments (DEWS)
-------------------------------------------------

Program DEWS umožňuje vypočítat příspěvek na bydlení pro zaměstnance, kteří jsou na něj nárokováni a
chcete být zaregistrováni na něm podle své aktuální smlouvy se společností.

Je vypočítávána na základě počtu let, které zaměstnanci ve firmě strávili:

- Méně než pět let: Z mzdy zaměstnance se odečítá 5,83 % na Dews.
- **Více než 5 let:** Z BÁZE zaměstnance se odečte 8,33 % z celkové částky splatné za
tento zaměstnanec.

Neplacené volno
-------------

Nedoplatky se počítají při výpočtu částky, která bude zaměstnanci odečtena za nevyčerpanou dovolenou.
odchodu, který je vypočítán následující rovnicí:

.. matematika::
:class: přesahující

\frac{Počet dní neplacené dovolené celkem × Brutto měsíčně}{30}

Kde hrubá mzda je základní plat plus všechny ostatní příplatky, které jsou v pracovní smlouvě zaměstnance uvedeny.

Dny mimo smlouvu
--------------------

Pravidlo o dnech mimo smlouvu poskytuje výpočet počtu dnů před/po období smlouvy.
S tím, že se překrývá s dobou na výplatních páskách zaměstnance.

.. příklad::
Pracovní smlouva je uzavřena na období od 1. do 30. září, ale mzdy jsou vygenerovány za období
21., v tomto případě je označeno jako mimo smlouvu 7 dní.

Vypočítá se následujícím způsobem:

.. matematika::
:class: přesahující

\frac{Počet nevyčerpaných dovolených dnů celkem × Brutto měsíčně}

Manuální odečty
-----------------

Manuální odečty umožňují uživatelům přidávat manuální odečty, které se mají aplikovat na zaměstnance v každém výplatním listu.

Sleva a její popis se na výplatním listu uvede přímo.
ručně, stejně jako ostatní vstupy.

Čistý plat
----------

Čistá mzda ukazuje čistou částku, kterou zaměstnanec dostane na základě výplatní pásky.

Vypočítává se jako součet základu a všech slev, od kterého se odečtou všechny odečty.

.. důležité::
Pro pravidla výše je přistupováno tak, že nejdříve se získá celkový počet všech statických částek.
které jsou v smlouvě a pak odečtou částky, které se mají odečítat, jako například neuhrazené
leave, sick leave, hand-deduction, commission, etc.

Vytváření účetních záznamů z výplatních pásek
===========================================

Účty jsou spojeny s každým pravidlem výplaty jako kredit nebo debet, takže když je vytvořen návrh
Vzniklé z výplatního lístku, odpovídají částkám na účtech.

Účty je potřeba nastavit tak, aby výsledná položka byla vyvážená, jinak
V případě nerovnováhy se vyvolá varování a nebude vytvořen záznam.

Po kontrole výplatních pásek a zjištění správnosti všech částek vytvořte návrh.
vstup, buď jeden vstup pro všechny zaměstnance nebo vstup podle nastavení dle
Nastavení.

.. příklad::
Účty debetní a kreditní pro základní a příspěvkové pravidlo.

.. obrázek: Spojené arabské emiráty/účetnictví pro pravidla.png
:alt:Nastavení účetnictví pro pravidla.

Platit zaměstnancům
=============

Po zadání účetního případu nebo výplatní pásky může společnost pokračovat v platbě svých
Zaměstnanci.

V samotném výplatním termínu nebo po kliknutí na tlačítko „výplata“ se vytvoří platba.
spojené s vloženým záznamem o výplatním lístku. Stejně tak je možné provést pro více platů, pokud se jedná o jeden platební příkaz.
Provede se z jednoho nebo více platebních deníků/peněžních knih.

.. poznámka::
Jakmile bude mzda vygenerována, zaměstnanec bude moci přistupovat k výplatním páskám prostřednictvím svého portálu
uživatelé. Ti automaticky obdrží e-mail s informací, že výplatní pásky jsou nyní k dispozici.
Je možné je zhlédnout na jejich portálu.

Tiskopisy výplatních pásek
=================

Z výplatního listu se dají vytisknout dva formáty, záleží na typu výplatního listu.
Měsíční výplatní páska nebo výplatní páska „Konec služby“. Způsobuje to, že pokud zaměstnanec požaduje výplatní pásku
je vygenerován, je uložen do archivu v daném měsíci.

Hlavní zpráva
=============

Výkaz *Mistr* poskytuje podrobný přehled o výplatách zaměstnanců za určité období.
na základě výplatních pásek, které jsou vytvářeny za tuto dobu s nastavenými řádky výplatního pásku
sloupce v excelovské zprávě.

Hlavním účelem je usnadnit a zrychlit proces auditu pro personální oddělení.

Chcete-li tento report zobrazit, přejděte na: „Mzdy“ - „Zprávy“ - „Hlavní zpráva“.

... payroll/l10n_ae/wps-reports:

Zprávy o ochraně mezd (WPS)
=====================================

WPS je hlášení, které společnost musí předložit jako důkaz toho, že platila
vyplácí zaměstnancům správné částky v správných termínech. Může být vygenerován pro každý výplatní lístek nebo ve skupinách.

Před vytvořením zprávy je nutné provést následující kroky:

#Přejděte na „Mzdy“ – „Konfigurace“ – „Nastavení“ a pod položkou „UAE
V sekci Nastavení mzdy WPS nastavte následující:

   - :guilabel:`ID zaměstnavatele“: Zadejte jedinečný identifikátor pro společnost, který se používá v |WPS|
zpráva.
   - Vyberte bankovní účet nebo začněte psát, abyste mohli vytvořit
a založit nový účet.

.. důležité::
Při nastavení položky „Mzdy - bankovní účet“ se ujistěte, že dokončíte následující:

        - :guilabel:`Majitel účtu“: nastavte na společnost.
        - :guilabel:`Číslo účtu“ musí být platný IBAN.
        - :guilabel:`Banka“ musí mít nastavené „UAE Routing Code Agent ID“.
        - :guilabel:`Poslat peníze“ by mělo být zapnuté a nastaveno na „Důvěryhodné“.

#. Udělejte jedinečné identifikátory pro všechny zaměstnance, kteří jsou součástí cíle
platová složka.

V poli „Identifikační číslo“ se nachází na stránce zaměstnance pod
:guilabel:`Soukromé informace“

Jakmile je nastavení dokončeno, lze WPS vytvořit buď pro jednu mzdu nebo pro celou sadu.
pokračuje:

#Vytvářejte výplatní pásky jednotlivě nebo jako hromadně.
#Vložte návrh subjektu souvisejícího s výplatními páskami.
#Vytvořte platbu a nastavte exportní formát na „UAE WPS“.

.. poznámka::
Zpráva je v souladu s požadavky vlády ve formátu .sif.
software, který umí otevřít soubor s příponou .sif nebo jej převést do jiného formátu (.xslx).
schopností jej prohlédnout.

Výsledný soubor obsahuje následující:

#**Záznam o podrobnostech zaměstnance** (**EDR**): obsahuje informace o zaměstnancích na lince.
by mělo být jedno záznamu EDR (záznam detailů o zaměstnanci) na každého zaměstnance.
#**Variabilní plat zaměstnance** (VPS) – zahrnuje podrobnosti o variabilním platu, který zaměstnanec dostal.
na výplatním lístku. Pokud zaměstnanec nějaké má. Tyto proměnné částky se počítají od chvíle, kdy
Do výpočtu jsou použity vstupy, které se váží k platovým pravidlům (v menu „Mzdy“ -> „Konfigurace
--> Pravidla
#**Záznam o kontrole mzdy** (**SCR**): Měl by existovat pouze jeden záznam o kontrole mzdy.
pro každý soubor WPS, protože uvádí podrobnosti o zaměstnavateli a celkové částky za výplatní pásky.
