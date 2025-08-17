==============
Konfigurovatelné zprávy
==============

Odoo přichází s mocným a snadno použitelným rámcem pro reportování. Motor vám umožní vytvářet nové
výroční zprávy, jako jsou daňové přiznání, účetní výkazy a výsledovky s konkrétním členěním
layouty.

.. důležité::
Aktivujte režim vývojáře (:ref:`vývojářský režim <developer-mode>`) pro přístup k účetní zprávě
konfigurace.

Pro vytvoření nového výkazu přejděte na: „Účetnictví“ -> „Konfigurace“ -> „Výkazy“.
Zde vytvořte buď zprávu „kořenovou“ (viz Customize Reports/Root) nebo variantu (viz Customize Reports/Variant).
<sestavit-zpravy/varianty>“.

.. tip::
   - Zvažte uložení upravených zpráv jako variant zpráv, aby byly zachovány jejich kořenové zprávy.
   - Chcete-li se dostat k rozhraní pro správu existujícího hlášení z samotného hlášení, klikněte na
:icon:`fa-kolečko` :guilabel:`(kola)`

..._zpracovat zprávy/kořen:

Zdroj reportuje
============

Základní účetní závěrky lze považovat za obecné a neutrální účetní výkazy. Jsou základem pro vytváření
vytváří se místní účetní verze. Pokud v reportu není kořenový report, je považován za kořen
vlastní zprávě.

.. příklad::
Daňový výkaz pro Belgii a USA by použil stejnou základní verzi a upravil ji
Využijí ho pro své vnitrostátní předpisy.

Vytvoření položky nabídky je nutné k přístupu ke zprávě s novým kořenem. Pro otevření takové zprávy otevřete
konfigurace, klikněte na „Akce“, „Vytvořit položku v nabídce“ a obnovte stránku.
report je nyní dostupný pod:menuselection:`Účetnictví --> Zprávy“.

.. poznámka::
Případy, kdy je nutné vytvořit novou kořenovou zprávu, jsou vzácné, například pokud daňové úřady dané země
Požadují nový a specifický typ zprávy.

.. _sestavit zprávy/varianty:

Varianty
========

Varianty jsou země specifické verze kořenových zpráv a vždy se tedy vztahují k nějakému kořenu.
report. Vyberte generický (kořenový) report v poli :guilabel:`Základní report`.
při vytváření nového hlášení.

Když se otevře kořenový výkaz z nabídky „Zprávy“ v aplikaci Účetnictví, všechny jeho
varianty se zobrazují v rozevíracím seznamu variant ve výchozím nastavení v pravém horním rohu pohledu.

.. příklad::
:guilabel:`Zpráva o DPH (BE)` je varianta kořenového souboru :guilabel:`Univerzální daňová zpráva“.

.... obrázek:customize/engine-variant.png
:alt: Výběr varianty.

...účetnictví/přizpůsobit/řádky:

Rozhlasová stanice
=====

Po vytvoření zprávy (kořenové nebo variantní) je další krok naplnit ji řádky.
Nová řádka přidáte kliknutím na tlačítko „Přidat řádek“. Existující řádku upravíte kliknutím na ni samotnou
a upravit okno přesunutí. Každá řádka vyžaduje pole „Jméno“ a může obsahovat volitelné pole „Kód“.
Která umožňuje používat hodnotu řádku v rovnicích.

.. obrázek: customize/engine-lines-options.png
:alt:Možnosti motorových linií.

Výrazy
===========

Každá řádka může obsahovat jednu nebo více výrazů. Výrazy lze považovat za podproměnné.
potřebné pro zprávu o výkonnosti. Chcete-li vytvořit výraz, klikněte na „Přidat řádek“ *v rámci* řádku.
Pop-up.

Při vytváření výrazu musíte zadat :guilabel:`Label`, který se k němu bude vztahovat.
Štítek musí být jedinečný mezi výrazy každé řádky zprávy. Oba štítky :guilabel:`Počet
Do políčka „Motor“ a „Vzorec“ je také nutné zadat hodnotu. **Počítací jednotka**
Určuje, jak jsou **výraz(y)** a **podvýrazy** interpretovány. Je možné smíchat
vyjádření používající různé počítačové motory pod jednou čarou, pokud je třeba.

.. poznámka::
V závislosti na typu motoru mohou být také vyžadovány podpodmínky.

Odoo výpočetní jednotka pro doménu
------------------------------

Při použití výpočetního modelu „Odoo Domain“ je vzorec interpretován jako :ref:`Odoo
domain <odkaz/orm/domény> s cílem objektů „přesunutá položka“.

Subvzorec umožňuje definovat, jak se pohybové čáry shodující s doménou používají k výpočtu
hodnota výrazu:

„součet“
Výsledkem je součet všech zůstatků zařazených do řady pohybů, které jsou shodné.

sum_if_pos
Výsledkem je součet všech zůstatků pohybových linií, které odpovídají tomuto množství, pokud je kladné.
Pokud ano, pak je „0“.

„sum_if_neg“
Výsledek je součtem všech zůstatků pohybových řad, které byly shodné s touto hodnotou, pokud je tato hodnota záporná.
Pokud ano, pak je „0“.

`počet řádků“
Výsledkem je počet podřádků této výrazu. Pokud má rodičovský řádek :ref:`skupinu
hodnota atributu <customize-reports/lines-group-by> odpovídá počtu jedinečných
sloučení klíčů v řádcích hodnocených tahů. Jinak bude počet řádků hodnocených tahů.

.. tip::
Pro **obrácení** směru výsledku vložte před podvzorec znaménko „-“.

.. obrázek:: customize/engine-expressions.png
:alt:Výrazová linie v rámci zprávy o linii

Kalkulačka pro výpočet daně z příjmu
---------------------------

Při použití výpočetního motoru „Daně“ se obsah pole „Vzorec“
pole jsou přiřazena k daním. Pokud takové tagy neexistují při vytváření výrazu, budou
vznikla.

Když se vyhodnocuje výraz, výpočet výrazu lze zhruba vyjádřit jako: **(množství
pohybové čáry s tagem + (počet pohybových čar s tagem -).

.. příklad::
Pokud je nastavená vlastnost :guilabel:`Formula` na hodnotu tag_name, motor vyhledává značky s názvem +tag_name.
-tag_name, vytvářejí-li je potřeba. Například: dva tagy jsou shodné s
formulář. Pokud je formulář A, bude vyžadovat (+A a -A, pokud je potřeba).

Agregační výpočetní jednotka jiných vzorců
-------------------------------------------

Kalkulačka :guilabel:`Agregace ostatních vzorců` provádí aritmetické operace na
výsledky získané od jiných výrazů. Vzorce zde tvoří odkazy na výrazy
Oddělené jedním ze čtyř základních matematických operátorů (sčítání „+“, odčítání „-“, dělení
„/“, a „*“). Chcete-li odkazovat na výraz, zadejte kód jeho rodičovské řádky.
periodem . a označením výrazu (např. code.label).

Podmnožiny mohou být následující:

`pokud (výše(součet))“
Hodnota aritmetické výrazu se vrátí pouze v případě, že je větší než zadaná
pak bude výsledek roven nule.

`if_below(CURRENT(amount))“
Hodnota aritmetické výrazu se vrátí pouze v případě, že je nižší než zadaná
pak bude výsledek roven nule.

„pokud je mezi (kurz1(částka1)) a (kurz2(částka2))“
Hodnota aritmetické výrazu se vrací pouze tehdy, pokud je striktně mezi
Pokud nejsou k dispozici žádné hranice, bude vrátit se na nejbližší hranici.

`pokud_jiný_výraz_nad(LINE_CODE.EXPRESSION_LABEL, CUR(amount))“
Hodnota aritmetické výrazu se vrátí pouze v případě, že hodnota výrazu
označené poskytnutou čárkovou kótovací linií a výrazovým štítkem je větší než poskytnutá hranice.
V opačném případě bude výsledek roven nule.

„Pokud je výraz níže (LINE_CODE.EXPRESSION_LABEL, CUR(amount))“
Hodnota aritmetické výrazu se vrátí pouze v případě, že hodnota výrazu
označené poskytnutou čárkovou kótovací linií a výrazovým štítkem je nižší než poskytnutá hranice.
V opačném případě bude výsledek roven nule.

„CUR“ je zkratka měny v hranatých závorkách a „AMOUNT“ je částka vázaná na
takové měny.

Můžete také použít podvzorec cross_report, abyste vyhledali výraz v jiném hlášení.

Kalkulačka pro výpočet účtu
------------------------------------------

Výpočetní jednotka pro výpočet předpony účtu se používá k porovnání částek na účtech.
Použít předpony kódů těchto účtů jako proměnné v aritmetické rovnice.

.. příklad::
   | `21`
|Matematické výrazy mohou být i jedním předponovým slovem, jako zde.

.. příklad::
   | `21 + 10 - 5`
|Tato vzorec přidává zůstatky pohybových řádků na účtech, jejichž kód začíná číslem 21.
a „10“ a odečte zůstatek jedniček na účtech s předčíslím „5“.

Je také možné ignorovat výběr podpředpon.

.. příklad::
   | `21 + 10\\(101, 102) - 5\\(57)`
|Tato vzorec funguje stejně jako předchozí příklad, ale ignoruje předpony 101 a 102.
a „57“.

Můžete aplikovat „podfiltry“ na kredity a dluhy pomocí přípon C a D.
Pokud se případ shoduje s předponou a celkový zůstatek účtu je
Převod zůstatku na tento účet je možný pouze **kreditem/debitem**.

.. příklad::
Účet „210001“ má zůstatek -42, účet „210002“ má zůstatek 25. Vzorec
„21D“ vyhovuje pouze účtu „210002“, a proto se vrací 25. Účet „210001“ není shodný, protože nevyhovuje
Zůstatek je kredit.

Předpony výjimek lze kombinovat s příponami „C“ a „D“.

.. příklad::
| `21D + 10\\(101, 102)C - 5\\(57)`
|Tato vzorce přidávají zůstatky pohybových řádků na účtech, jejichž kód začíná číslem 21.
*pokud* je debetní („D“), a „10“, *pokud* je kreditní („C“), ale ignoruje předpony „101“, „102“ a
odečte zůstatek jedniček na účtech s předčíslím 5, přičemž ignoruje předčíslí 57.

Pro shodu s písmenem „C“ nebo „D“ v předponě a aby se nepoužilo jako přípona, použijte prázdné vyloučení „()“.

.. příklad::
| 21D\()
|Tato vzorce vyhledávají účty, jejichž kód začíná na „21D“, bez ohledu na znaménko zůstatku.

Kromě použití kódových předčíslí pro zahrnutí účtů můžete také spárovat s **účtem.
tagy**. To je zejména užitečné například v případě, že váš stát nemá standardizovanou mapu
účtů, kde by mohlo být stejné předpony použito pro různé účely v různých společnostech.

.. příklad::
|  tag(25)
|Tato vzorec vyhledává účty, jejichž spojené štítky obsahují jeden s ID 25.

Pokud je odkazovaný tag definován v datovém souboru, můžete místo ID použít XMLID.

.. příklad::
| `tag(můj_modul.můj_tag)`
|Toto vzorce vyhovuje účtům, jejichž spojené štítky zahrnují štítek označený
*my_modul.my_tag*.

Můžete používat matematické výrazy s tagy a možná je kombinovat s předponovými výběry.

.. příklad::
| `tag(my_module.my_tag) + tag(42) + 10`
|Zůstatky účtů označených jako *my_module.my_tag* budou součtem s těmi z účtů
připojené k značce s ID *42* a účtům se znakovým předčíslím „10“

Sufixy „c“ a „d“ lze použít stejným způsobem jako tagy.

.. příklad::
| `tag(my_modul.můj_tag)C`
|Tato vzorce vyhledávají účty s označením *my_module.my_tag* a zůstatkem na účtu.

Předpona vyloučení také funguje s tagy.

.. příklad::
|`tag(modul/můj_tag) (10)`
|Tato vzorce se shodují s účty, které mají značku *my_module.my_tag* a kód, který nezačíná
     `10`.

Vnější výpočetní jednotka pro hodnocení hodnot
---------------------------------

Výpočetní jednotka „Externí hodnota“ se používá k odkazování na manuální a přenesené
hodnoty**. Tyto hodnoty se neukládají pomocí „účetního pohybu“, ale s
„účet.zpráva.vnější.hodnota“. Každý z těchto objektů přímo odkazuje na výraz, který ovlivňuje.
Takže zde je potřeba udělat tak málo.

Formulace může být jednou z následujících:

„součet“
Pokud je výsledkem součet všech externích hodnot v daném období.

„nejnovější“
Pokud je výsledkem hodnota posledního externího vstupu v daném období.

Dále lze podmínky používat dvěma způsoby:

„srážka=X“
Za symbol „X“ lze vložit číslo, které instruuje k zaokrouhlení částky na X desetinných míst.

„upravitelné“
Ukazuje, že tento výraz lze upravovat ručně a zobrazí ikonu.
zpráva, která umožňuje uživateli tuto akci provést.

.. poznámka::
Manuální hodnoty se vytvářejí na základě aktuálně vybraného data ve zprávě.

Obě podvětvé lze smíchat oddělením znakem „;“.

.. příklad::
| editovatelný; přesnost na 2 desetinná místa
|Toto podvzorce ukazuje správný způsob, jak kombinovat oba chování.

Kalkulačka funkcí vlastními jazykovými konstrukcemi
-----------------------------------------

Komponenta pro výpočetní algoritmus Custom Python Function je prostředkem, který umožňuje vývojářům zavést
přizpůsobené výpočty v závislosti na konkrétním případu. Symbol „Formula“ je název
Funkci v Pythonu, kterou chcete zavolat, a :guilabel:`Subformula` je klíč k vyzvednutí
Výsledkem této funkce je slovník, který lze použít pouze v případě, že chcete využít vlastní výpočetní jednotku.
modul.

Sloupy
=======

Zprávy mohou obsahovat neomezený počet sloupců, které se zobrazují. Každý sloupec získává své hodnoty ze
vyjádření vyhlášená na liniích. Položka guilabel:expression_label ve sloupci
Označuje štítek výrazů, jejichž hodnota je zobrazena. Pokud řádek nemá žádný výraz s označením **expression**
pole, pak se v tomto sloupci nic nezobrazuje. Pokud je potřeba více sloupců, musíte
používat různé výrazové štítky.

.. obrázek: customize/engine-columns.png
:alt:Sloupce zprávy.

Při použití funkce porovnávání období, která je k dispozici pod záložkou „Možnosti“,
účetní výkaz, všechny sloupce se opakují pro každé období.

.._sestavit zprávy/řádky seskupit podle:

Skupiny linek
=============

Nepovinné skupinování je možné pomocí přidání nebo použitím existujících polí v modelu záznamu časopisu.
Pokud jsou pole vztahována a neuložená.

.. poznámka::
Skupování řádků vyžaduje, aby zpráva obsahovala výslovné řádky zprávy, které lze upravit.
Zprávy například nepodporují seskupování řádků, protože používají dynamické řádky, které jsou generovány.

Vytvořte nový položkový záznam
----------------------------------

Pro vytvoření neukládaného pole souvisejícího s položkou v modelu Journal Item nejprve přejděte na
:menu „Účetnictví“ -> „Deník položek“, a klikněte na ikonu „(chyba)“.
Klikněte na položku „Pole“ a klikněte na „Nový“, abyste vytvořili nové pole.
následujících polích:

- :guilabel:`Název pole“: technický název pole
- :guilabel:`Název pole“: název, který se má zobrazit u pole
- :guilabel:`Typ pole“: typ pole, ke kterému by mělo být tato položka vztahována
- :guilabel:`Uloženo“: Nezaškrtávejte tento prázdný řádek, protože pouze neuložené pole může být použito k seskupení
linie.
- V případě, že typ pole je „one2many“, „many2many“ nebo
:guilabel:`many2one`, vyberte model původního pole pro seskupení.
- :guilabel:`Definice souvisejícího pole“: technická cesta k poli, které chcete seskupit

...... příklad::
Pro skupinování podle týmu prodeje komerčního partnera nastavte vztahovou pole na
`move_id.team_id`.

Skupinové linky
-----------

Pro seskupení řádků přejděte na záložku „Řádky“ v požadovaném výkazu a klikněte
na lince, kterou chcete sloučit a upravte pole „Skupina podle“ na hodnotu technického názvu
Název pole, které má být použito jako klíč pro seskupení.

.. tip::
Chcete-li získat seznam všech polí modelu a jejich technických názvů, přejděte na
:menu „Účetnictví -> Položky účetní knihy“ a klikněte na ikonu „fa-bug“
ikona a poté klikněte na položku „Pole“. Technické názvy všech polí jsou uvedeny v
:guilabel:`Název pole“ sloupec.

.. viz též:
:ref:`Konsolidace podle účetního kódu <consolidation_account_mapping>`
