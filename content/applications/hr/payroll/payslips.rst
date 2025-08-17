========
Pracovní smlouvy
========

Výplatní pásky vytváří pracovnice účtárny prostřednictvím aplikace „Mzdy“.

V nabídce hlavičky „Mzdy“ aplikace „Personalistika“ je uvedeno
tři sekce: „Platby“, „Všechny výplatní pásky“ a „Souhrnné platby“.

Tyto tři části poskytují všechny nástroje potřebné k vytvoření výplatních pásek pro zaměstnance, včetně
individuální výplatní pásky, soubor výplatních pásek nebo provizní výplatní pásky.

.. obrázek: výplatní pásky/vyplacni_pasky.png
:align:center
:alt:Výběr mzdy v modulu Mzdy.

.. platová tabulka/platová třída:

Zaplatit
======

Klikněte na položku „Mzdy“ -> „Potvrzení mzdy“ -> „Zaplatit“. Zobrazí se vám potvrzení o výplatách, které je třeba zaplatit.
zaplaceno.

.. obrázek: výplatní pásky/všechny platové pásky.png
:align:center
:alt: Zobrazit všechny platby, které je třeba zaplatit na stránce Platby k úhradě.

Každá výplatní páska obsahuje číslo referenčního účtu pro konkrétní výplatní pásku a
Jméno zaměstnance, název „série“, název společnosti a základní informace o produktu.
Mzda, hrubá mzda, čistá mzda a stav platby na výplatním lístku.

Klikněte na položku v mezdovém výpisu, abyste zobrazili podrobnosti pro tuto položku mezdového výpisu.

.. _mzdy/nový výplatní lístek:

Vytvořit nový výplatní lístek
--------------------

Nová výplatní páska může být vytvořena buď na stránce :ref:`Výplaty k zaplacení <payroll/to-pay>`, nebo
Stránka „Příjmy zaměstnanců“ (<payroll/all-payslips>).

Vytvořte novou mzdu kliknutím na tlačítko „Nový“ v pravém horním rohu.

Načte se prázdný tiskopis výplatního listu, kde lze doplnit potřebné údaje o výplatním listu.

Příkaz k výplatě
~~~~~~~~~~~~

Na prázdném tiskopisu mzdy je nutné vyplnit několik políček. Většina povinných polí se automaticky doplní
Po výběru zaměstnance.

Vyplňte následující údaje na tiskopisu výplatní pásky:

- :guilabel:`Zaměstnanec“: zadejte jméno zaměstnance nebo vyberte požadovaného zaměstnance ze seznamu
seznamem možností v tomto poli. Toto pole je povinné.

.. poznámka::
Je doporučeno vytvářet pouze mzdy pro zaměstnance, kteří jsou již v databázi.
Pokud neexistuje žádný současný záznam zaměstnance (a tedy ani pracovní smlouva), doporučujeme
vytvořit nového zaměstnance v aplikaci *Zaměstnanci* před tím, než se vytváří výplatní pásky pro
zaměstnance. Podívejte se na dokumentaci :doc:`nového zaměstnance <../employees/new_employee>`.
návod, jak přidat zaměstnance.

- :guilabel:`Období“: první den v měsíci do posledního dne aktuálního měsíce automaticky vyplní
:guilabel:`Období“ pole výchozí hodnoty. Datum lze změnit, pokud je třeba.

Chcete-li změnit datum začátku, klikněte na první datum v poli :guilabel:`Období`, které se zobrazí.
pop-up kalendář. Na tomto kalendáři použijte :guilabel:`< (menší než)` a :guilabel:`>
ikonky „větší než“ pro výběr požadovaného měsíce a pak klikněte na požadovaný den pro jeho výběr.
konkrétní datum.

Tento proces opakujte, abyste upravili datum platby v příkazu k výplatě. Tyto pole jsou **povinná**.
- :guilabel:`Smlouva“: vyberte požadovanou smlouvu pro zaměstnance z nabídky.
Vybraný zaměstnanec se zobrazí jako možnost v příslušných smlouvách.
**povinné pole**.
- :guilabel:`Skládka“: Vyberte v tomto poli nové platové pásky z vybrané skládky.
Příplatky se připočítávají k výplatní pásce.
- :guilabel:`Základní struktura“: z rozevírací nabídky vyberte typ základní struktury.
V případě vybrané smlouvy se zobrazí odpovídající struktury pro zaměstnance jako možnosti.

Pokud ještě nebyl vybrán žádný zaměstnanec a/nebo smlouva, všechny dostupné :guilabel:`struktury“ se zobrazí
seznam. Jakmile je vybrán zaměstnanec a/nebo smlouva, bude se zobrazit jakýkoli nevyhovující :guilabel:`Struktura`.
Pro tento zaměstnanec a/nebo smlouvu nejsou k dispozici žádné informace. Toto pole je **povinné**.

.. obrázek: výplatní pásky/nový platový list.png
:align:center
:alt:Všechny položky na nové mzdové listině pro únorový plat.

.. poznámka::
Typicky po výběru v poli „Zaměstnanec“ se Odoo automaticky vyplní všechny ostatní pole.
jiná požadovaná pole (kromě pole Period), ale pouze pokud je tato informace
už na formuláři zaměstnance v aplikaci *Zaměstnanci*.

.. důležité::
Pokud do automaticky vyplněných políček provádíte změny, je vhodné si zkontrolovat s
účetní oddělení, aby každá položka, která ovlivňuje aplikaci *Účetnictví*, byla správně zadaná.

.. _mzdy/vstupy pro počet odpracovaných dnů:

Karta pracovních dnů a vstupů
************************

- „Práce“: v poli „Práce“ (včetně
:guilabel:`Typ`, :guilabel:`Popis`, :guilabel:`Počet dní`, :guilabel:`Počet
Hodiny a částka se automaticky vyplní podle toho, co bylo zadáno do
:guilabel:`Období“, :guilabel:`Smlouva“ a :guilabel:`Základní struktura“ položky v tiskopisu výplatních pásek.
- :guilabel:`Další vstupy“: do této sekce lze zadat další vstupy ovlivňující výplatní pásku.
například slevy, náhrady a výdaje.

Klikněte na „Přidat řádek“ pro vytvoření záznamu v sekci „Další vstupy“.

Vyberte typ v seznamu zboží v poli „Typ“.
Poté zadejte „Popis“, pokud chcete. Nakonec zadejte částku v
:guilabel:`Počet“ pole.

.. obrázek:výplatní pásky/dny odpracované tabulka.png
:align:center
:alt: Zadané hodnoty v polích pracovních dnů a vstupů.

Tabulka výpočtu mzdy
**********************

- :guilabel:`Výpočet mzdy“: v záložce „Výpočet mzdy“ jsou automaticky vyplněny údaje
Po kliknutí na tlačítko „Výpočet“ se zobrazí mzdy, slevy a
daň z přidané hodnoty, clo atd.

.. obrázek: platovky/platove-slozenky.png
:align:center
:alt:Zaplněné pole v záložce výpočet mzdy.

Další informační záložka
**************

- :guilabel:`Název výplatního listu“: Zadejte název výplatního listu do tohoto pole. Název by měl být krátký
a popisné, například „(Jméno zaměstnance) Duben 2023“. Tento prvek je **povinný**.
- :guilabel:Společnost: vyberte společnost, na kterou se vztahuje výplatní páska pomocí rozbalovací nabídky
Pole. To je **povinné pole**.
- :guilabel:`Datum ukončení platnosti“: do pole zadejte datum, kdy je zaměstnanci vyplácena mzda.

Klikněte do pole, aby se zobrazilo okno kalendáře. Pomocí tlačítka :guilabel:`< >
Vyberte ikonu pro zobrazení kalendáře na měsíc a rok.

Pak klikněte na požadovaný den a vyberte jej.
- Do pole „Datum účtu“ zadejte datum, kdy by měla být faktura vystavena.
- :guilabel:„Mzdový deník“: pole se automaticky vyplní po výběru již existujícího
:guilabel:`Zaměstnanec“. Toto pole nelze upravit, protože je propojeno s účetnictvím.
aplikace. Toto pole je **povinné**.
- Pokud je vhodné, pole „Účetní záznam“ se automaticky vyplní po
Potvrzení výplatního lístku. Tento údaj nelze měnit.
- :guilabel:`Přidat vnitřní poznámku...“: do nového záznamu lze zadat libovolnou poznámku nebo odkaz
v tomto oboru.

.. obrázek:výplatní pásky/další informace.png
:align:center
:alt: Položky vyplněné v jiném informačním panelu.

Zpracujte novou mzdu
~~~~~~~~~~~~~~~~~~~~~~~

Po zadání všech potřebných informací o výplatní pásce klikněte na tlačítko „Vypočítat list“.
tlačítko. Po provedení takového kroku se uloží všechna data z výplatního listu a :guilabel:`Mzda
V poli „Počítání“ se automaticky vyplní informace z pracovní smlouvy nebo docházky.
dokumenty.

Pokud je třeba provést jakékoliv změny, nejdříve klikněte na tlačítko :guilabel:`Zrušit`, pak
Tlačítko „Přepnout na návrh“. Udělejte požadované změny a klikněte na tlačítko „Vypočítat list“.
tlačítko znovu a změny se zobrazí v poli „Práce“.
:guilabel:`Výpočet mzdy“ karty.

Jakmile je na formuláři platby vše správně, klikněte na tlačítko „Vytvořit návrh“
Vytvořit výplatní pásku.

Poté se zobrazí okno potvrzení s dotazem „Opravdu chcete pokračovat?“.
Klikněte na tlačítko „OK“, abyste potvrdili.

.. poznámka::
Databáze může potřebovat aktualizaci, aby se na výplatní pásce a e-mailu objevily.

K tisku výplatního listu klikněte na tlačítko „Tisk“. Chcete-li zrušit výplatní list, klikněte na
Tlačítko „Zrušit“.

.. obrázek: výplatní pásky/výplatní páska chatter.png
:align:center
:alt: Nová výplatní páska je zaslána zaměstnanci a zobrazena v chatu.

Další krok je zaslání platby zaměstnanci. Klikněte na tlačítko „Registrace platby“.
tlačítko. To vyvolává okno s formulářem, ve kterém je možné zadat požadovaný titulek „Bankovní listy“
Vyberte způsob platby z roletky. Pak klikněte na
Klikněte na tlačítko „Potvrdit“ a poté se vraťte zpět ke smlouvě.

.. důležité::
Pokud chce být zaměstnanci vyplacen výplatní páska, musí mít uvedeno číslo účtu.
Kontaktní informace. Pokud není uvedena bankovní informace, nemůže být vyplacen výplatní lístek a dojde k chybě.
Zobrazí se po kliknutí na tlačítko „Uhradit“. Informace o bankovním účtu lze najít v
záložku „Soukromá informace“ v kartě zaměstnance.
Aplikace „Zaměstnanci“. Upravte kartu zaměstnance a přidejte informace o bance, pokud je chybí.

.... obrázek: platovky/bankovnictví.png
:align:center
:alt:Bankovní údaje lze zadat do karty zaměstnance.

Odoo automaticky kontroluje informace o účtu. Pokud je chyba v seznamu zaměstnanců
bankovní účet, při chybě se objeví okno s hlášením „* Bankovní účet zaměstnance
neověřené.* Pokud se tento problém objeví, aktualizujte informace o bance zaměstnance.
:ref:`Formulář zaměstnance <employees/private-info>.

Pokud je potřeba platbu zrušit nebo vrátit zpět, klikněte na příslušný odkaz „Zrušit“ nebo
:guilabel:`Vrácení peněz“ tlačítko, které se nachází v pravém horním rohu obrazovky.

.. tip::
Než se pustíte do zpracování výplatních pásek, je nejlepší si zkontrolovat část varování v záložce Mzdy.
dashboard aplikace. Zde se objevují všechny možné problémy týkající se mzdy.

Pro zobrazení varování přejděte na: „Mzdy - Dashboard“. Varování se objeví
v levém horním rohu panelu.

.... obrázek: platovky-varovani.png
:align:center
:alt: Zobrazení panelu nástrojů aplikace Mzdy s vyznačeným varovným oknem.

Varování jsou seskupena podle typu, například „Zaměstnanci bez platné pracovní smlouvy“ nebo „Zaměstnanci bez
Číslo bankovního účtu. Klikněte na varování, abyste zobrazili všechny záznamy spojené s tímto konkrétním problémem.

Pokud nebudou varování vyřešena v průběhu zpracování výplatního lístku, mohlo by se objevit chyba.
se objevit. Chyby se zobrazí v okně s upozorněním a poskytnou podrobnosti o chybě a možnostech jejího odstranění.
jim.

... _mzdy/všechny mzdy:

Všechny výplatní pásky
============

Pro zobrazení všech výplatních pásek bez ohledu na stav přejděte do: menu „Mzdy“ --> „Výplatní pásky“ --> „Všechny“.
Pracovní smlouvy. Stránka „Mzdy zaměstnanců“ se načte a zobrazí všechny mzdy, uspořádané podle
v seznamu výchozího zobrazení vnořených položek.

Klepněte na tlačítko vedle názvu konkrétní platby, abyste zobrazili všechny výplatní lístky.
v této konkrétní sérii spolu se všemi podrobnostmi výplatních pásek.

Počet výplatních pásek v balíku je uveden v závorkách za názvem balíku.
Na pravé straně se zobrazuje pole „Stav“, které ukazuje jeden ze stavů
následujících stavových možností:

- :guilabel:Návrh: vytvoří se výplatní páska a ještě zbývá čas na úpravy, protože
Výše částek se nepočítá.
- :guilabel:Čeká se na výplatní pásku: Výpočet byl proveden a podrobnosti o mzdě jsou k dispozici v
*Výpočet mzdy* karta.
- :guilabel:`Hotovo“: mzda je vypočítaná a připravena k zaplacení.
- :guilabel:`Zaplaceno“: zaměstnanec byl zaplacen.

.. obrázek: výplatní pásky/vsechny-vyplatni-pasky.png
:align:center
:alt:Zobrazit všechny výplatní pásky uspořádané podle sérií. Klikněte na šipku, abyste rozbalili každou sérii.

Klikněte na jednotlivé výplatní pásky, abyste zobrazili podrobnosti pro tuto výplatní pásku na samostatné stránce.
kliknete na „Zobrazit všechny výplatní pásky“ a vrátíte se zpět do seznamu všech výplatních pásek.

Nová mzda lze vytvořit z stránky „Mzdové listy zaměstnanců“ kliknutím na
Tlačítko „Nový“ v pravém horním rohu, což odhalí samostatný prázdný výplatní list.
stránku. Na této prázdné stránce výplatního listu zadejte všechny potřebné informace, jak je popsáno v
:ref:`Vytvoření nové výplatní pásky <mzdy/vytvorit-novou-vyplatni-pasku>“.

Pro tisk PDF verzí výplatních pásek z stránky „Výplaty zaměstnancům“ nebo „Zaměstnanecké výplatní pásky“,
Nejprve vyberte požadované výplatní pásky zaškrtnutím jednotlivých políček vpravo od každé výplatní pásky.
tisknout. Nebo klikněte na pole vedle sloupce s názvem „Poznámka“, který
Vybere všechny viditelné výplatní pásky na stránce a pak klikněte na tlačítko :guilabel:`Tisknout`, abyste
Pracovní smlouva, potvrzení o zaměstnání a výplatní pásky.

Mzdy lze také exportovat do tabulky v Excelu. Chcete-li exportovat všechny mzdy, klikněte na
:guilabel:`⚙️ (převodovka)` ikona na konci slov :guilabel:`Mzdy zaměstnanců“ v pravém horním rohu
výběr. To zobrazí rozbalovací nabídku. Klikněte na Exportovat vše, abyste vyexportovali všechny výplatní pásky do
tabulkový procesor.

.. obrázek: výplatní pásky/export.png
:align:center
:alt:Klikněte na tlačítko Export All, abyste vytvořili všechny výplatní pásky ve formátu Excel.

Nejprve musíte vybrat platby, které chcete exportovat ze seznamu. Pak klikněte na
zaškrtávací políčko vedle každé jednotlivé výplatní pásky pro její výběr. Jakmile jsou vybrané výplatní pásky, zobrazí se chytrý
Tlačítko se objeví v horní části stránky a ukazuje počet vybraných výplatních pásek. Poté
klikněte na ikonu „Akce“ v horní části stránky a klikněte
:guilabel:`Export“.

.. obrázek: výplatní pásky/export-select.png
:align:center
:alt: Seznam zaměstnanců s třemi vybranými, které chcete exportovat.

.. poznámka::
Oba moduly *Zaplatit* a *Všechny výplatní pásky* zobrazují všechny podrobné informace o každé výplatní pásce.

Série
=======

Pro zobrazení výplatních pásek v seznamu přejděte na: „Mzdy --> Výplatní pásky --> Seznamy“.
Zobrazit všechny platové pásky, které byly vytvořeny. Tyto platové pásky jsou zobrazeny v
výpisem.

Každá částice zobrazuje datum vytvoření, datum ukončení a název.
:guilabel:`Stav“, počet výplatních pásek v balíčku (:guilabel:`Počet výplatních pásek“) a
:guilabel:`Společnost“.

.. obrázek: platovky/složky.png
:align:center
:alt: Zobrazení všech vytvořených sérií.

Vytvořit novou sérii
------------------

Vytvořit novou sadu výplatních pásek z stránky „Sady výplatních pásek“
Klepněte na tlačítko „Nový“ v nabídce
v levém horním rohu. To odhalí prázdnou sáček se složenkami na samostatné stránce.

Do nové sestavy výplatních pásek zadejte:guilabel:`Název sestavy`.

Dále vyberte rozsah dat, ke kterým se tato sada vztahuje. Klikněte na jednu z položek „Období“.
políčka a z kalendářního okna se přesuňte na
správný měsíc a klikněte na příslušný den pro oba termíny zahájení a ukončení série.

Současná společnost vyplňuje pole :guilabel:`Společnost`. Pokud pracujete v prostředí více společností
prostředí, nelze z formuláře změnit :guilabel:`Společnost`. Batch
*musí být vytvořen při přístupu do databáze požadované společnosti.*

.. obrázek: výplatní pásky/nový sestavení podrobností.png
:align:center
:alt: Zadejte podrobnosti o novém balení.

... _vyplácení mzdy/výpočet ve velkém:

Zpracovat sadu
---------------

Klikněte na jednotlivé balení, abyste zobrazili podrobnosti o daném balení na samostatné stránce.
detailní stránka, různé možnosti (tlačítka) se objevují nahoře podle stavu objednávky:

- :guilabel:`Nový“ stav: sestavy bez platných výplatních pásek mají stav
:guilabel:`Nový“. Pro tyto sady se zobrazí následující možnosti tlačítka:

.... obrázek: platové pásky/soubor_nový.png
:align:center
:alt: Batch s novým stavem, se zvýrazněnými dostupnými tlačítky.

   - Klepněte na tlačítko „Přidat výplatní pásky“ (viz obrázek).
a objeví se okno „Přidat výplatní pásky“. Pouze tyto výplatní pásky lze přidat.
do seznamu se objeví i platby, které v současné době nejsou součástí balíku.

Vyberte požadované výplatní listy zaškrtnutím políčka vedle názvu každého výplatního listu, pak
klikněte na tlačítko „Vybrat“ a přidejte je do sestavy. Jakmile jsou výplatní listy vybrané,
Pokud je přidán do seznamu, stav se změní na „potvrzeno“.

   - :guilabel:`Vytvořit výplatní pásky“: po přidání výplatních pásek do sestavy klikněte na
:tlačítko „Vytvořit výplatní pásky“ k zpracování výplatních pásek a vytvoření individuálních výplatních pásek.
databáze.

A okno „Vytvořit výplatní pásky“ se objeví. Pokud je zvolen pouze konkrétní „Mzda
Struktura a/nebo konkrétní oddělení, pro které chcete vystavit mzdy, vyberte.
z příslušných rolet. Pokud nejsou vybrány žádné platby, pak jsou ve výpisu všechny faktury.
okno s upozorněním se zpracovává jako obvykle.

Klikněte na tlačítko „Vytvořit výplatní pásky“. Kliknutím na tlačítko „Vytvořit výplatní pásky“
tlačítko se změní na tlačítko „Vytvořit návrh“ a stav se změní na
:guilabel:`Potvrzeno“.

- Stav „Potvrzeno“: Soupravy, které byly vytvořeny a obsahují výplatní pásky, ale
Pokud nebyly výplatní pásky zpracovány, mají stav „Potvrzené“. Následující dvě
Ve výběru se objevují tlačítka pro tyto sady:

.... obrázek: platovky/souhrn-potvrzeno.png
:synchronizace: střed
:alt: Batch s potvrzeným stavem, se zvýrazněnými tlačítky dostupnými pro volbu.

  - Klikněte na tlačítko „Vytvořit návrh“ (viz obrázek).
jednotlivé výplatní pásky (a soubor) a vytvořit návrh výplatních pásek. Batch má nyní
stav :guilabel:`Done`.
  - :guilabel:`Připraveno k přečtení“: pokud se během procesu zpracování někdy stane, že je potřeba vrátit se zpět do
:guilabel:`New“, klikněte na tlačítko „Přesunout do návrhu“. Tato akce **neodstraní žádné soubory**
pracovní smlouvy, které již byly přidány do balíčku.

- :guilabel:Dokončeno“ stav: soubory s potvrzenými výplatními páskami mají
:guilabel:`Hotovo“. Následující možnosti tlačítek se zobrazí pro tyto sady:

.... obrázek: payslips/batch-done.png
:synchronizace: střed
:alt: Batch s stavem hotovo, se zvýrazněnými tlačítky dostupnými pro spuštění.

  - Klikněte na tlačítko „Vytvořit zprávu o platbě“ a
:guilabel:`Vyberte bankovní deník“ okno se zobrazí. Vyberte správný bankovní deník
v roletce.

Název série se zobrazuje v poli „Jméno souboru“, ale lze jej změnit, pokud je to požadováno.
Konečně klikněte na tlačítko „Potvrdit“ a zpracujte mzdy, zaplaťte zaměstnancům.
  - :guilabel:`Označit jako zaplacené“: po vytvoření plateb pomocí :guilabel:`Vytvořit platbu
Tlačítko „Odeslat hlášení“ musí být v databázi uvedeny jako zaplacené.

Klikněte na tlačítko „Zaplatit“, a stav objednávky se změní na
:guilabel:`Placená“.
  - :guilabel:`Připraveno k přečtení“: pokud se během procesu zpracování někdy stane, že je potřeba vrátit se zpět do
:guilabel:`New“, klikněte na tlačítko „Přesunout do návrhu“. Tato akce **neodstraní žádné soubory**
pracovní smlouvy, které již byly přidány do balíčku.

- :guilabel:„Zaplaceno“: Běžné položky mají stav „Zaplaceno“.
jiná tlačítka pro zobrazení dalších možností.

.... obrázek: platovky/slozenka-placena-v-celku-2.png
:synchronizace: střed
:alt: Batch s platbou, se zvýrazněnými tlačítky.

Na stránce s podrobnostmi o výplatním pásmu jsou jednotlivé mzdy v pásmu přístupné prostřednictvím
„Mzdy“ chytrý tlačítko umístěné nad informacemi o sestavě vpravo doprostřed. Po kliknutí
Klepnutím na tlačítko „Mzdy“ se zobrazí seznam všech mzdových listů.

Použijte navigační lištu „Breadcrumb“ k návratu na stránku s podrobnostmi o jednotlivé várce nebo zpět do seznamu
všechny šarže.

Vytvořte výplatní listy s doložkou
-------------------------

Pro zaměstnance v Odoo jsou platby prováděny pomocí *pracovních smluv*.

Mzdy lze vygenerovat přímo z stránky „Sklady výplatních pásek“.
(:menu_selection:"Mzdy - aplikace --> Mzdy - výplatní pásky --> Výběry").

Nejprve vyberte požadované objednávky klepnutím na políčko vpravo od každé objednávky, pro kterou chcete provést komise.
Vytvořte výplatní pásky. Poté klikněte na tlačítko „Vytvořit výplatní pásky“ v horní části obrazovky.
stránky.

Provedením takového kroku se zobrazí okno Generovat výplatní pásky, ve kterém je potřeba
informace musí být vyplněny.

.. obrázek: platovky/podrobnosti-o-provizích.png
:align:center
:alt: Zadejte detaily o provizi.

V tomto okně klikněte na rozbalovací nabídky vedle pole „Období“ a
zobrazit kalendářové okno s výběrem požadovaného období.
Které jsou generovány na výplatních páskách. Pomocí znaků :guilabel:`< (levý)“ a :guilabel:`> (pravý)“.
ikonky šipek, přejděte na správný měsíc a klikněte na datum pro jeho výběr.

V poli „Oddělení“ vyberte požadované oddělení z roletky.

Když je vybrán konkrétní oddělení, zaměstnanci zařazení do daného oddělení se zobrazí v
:guilabel:`Zaměstnanec“

V sekci „Zaměstnanec“ zadejte pro každého zaměstnance částku provize.
pravicový sloupec. K odstranění zaměstnance klikněte na ikonu „🗑“ (směsný odpad)
linie.

Přidejte novou položku kliknutím na tlačítko „Přidat řádek“ a zadejte „Zaměstnance“ a
Vhodné: „Povinná částka“.

Klikněte na tlačítko „Nahrát soubor“ a přidejte soubor, pokud je potřeba. Kdokoliv může nahrát jakýkoliv typ souboru.
přijaté.

Jakmile jsou všechny odměny správně zadány, klikněte na tlačítko „Vytvořit mzdy“.
Vytvořit záložní platové výměry v hromadném režimu.

:ref:`Procesujte soubor <payroll/batch-process>` stejně jako obvyklý soubor, aby byl
Proces platby.
