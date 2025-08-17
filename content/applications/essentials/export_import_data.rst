======================
Exportní a dovozní údaje
======================

.. |seznam| nahradit za: :ikonka:`oi-view-list` :guilabel:`(seznam)`
.. |akce| nahradit za: :icon:`fa-cog` :guilabel:`Akce“

V Odoo je někdy nutné exportovat nebo importovat data pro běžné reporty nebo data.
změna. Tento dokument se zabývá vývozem a dovozem dat do a z Odoo.

.. důležité::
Někdy se uživatelé setkají s chybou „časový limit“, nebo se záznam nezpracuje kvůli jeho velikosti.
Může se vyskytnout při velkých vývozech nebo v případě, že je dovozový soubor příliš velký. K obejití tohoto problému
omezení související s velikostí záznamů, zpracování vývozu nebo dovozu v menších dávkách.

... /essentials/export_import_data/export-data:

Exportní data z Odoo
=====================

Při práci s databází je někdy nutné exportovat data do samostatného souboru.
Může pomoci při reportování aktivit, i když Odoo poskytuje přesný a snadno použitelný nástroj pro reportování.
každé dostupné aplikaci.

S Odoo lze hodnoty exportovat z jakéhokoliv pole v jakémkoliv záznamu. Pro to je zapotřebí aktivovat seznamový pohled
(|seznam|) na položky, které je potřeba exportovat, pak vyberte záznamy, které chcete exportovat.
Vyberte záznam, zaškrtněte políčko vedle příslušného záznamu. Nakonec klikněte na |akce|
Pak: „Export“.

.. obrázek: export_import_data/list-view-export.png
:alt: Pohled na různé věci, které je třeba povolit nebo kliknout pro export dat.

Po kliknutí na tlačítko „Export“ se objeví okno s názvem „Export dat“, ve kterém
Několik možností pro vývoz dat:

.. obrázek:: export_import_data/export-data-overview.png
:alt:Přehled možností, které je třeba zvážit při vývozu dat v Odoo.

#S vybranou možností „Chci aktualizovat data (importovatelný výstup)“ se systém
ukazuje pouze pole, která lze importovat. To je užitečné v případě, že již existují :ref:`položky
Záznamy musí být aktualizovány (příkaz update-data). To funguje jako filtr. Ponechání zaškrtnuté položky
nezaškrtnuté, nabízí mnohem více možností pole, protože zobrazuje všechna pole, nikoli jen ta, která jsou zaškrtnuta.
Mohou být dováženy.
#Export může být proveden ve dvou formátech: „.csv“ a „.xls“. Formát „.csv“
položky jsou odděleny čárkou, zatímco soubor .xls obsahuje informace o všech listy v
soubor obsahující jak obsah, tak formátování.
#Tyto položky lze vyvážet. Klikněte na ikonu „>>“ (pravý směr) pro zobrazení
více možností podpole. Vyhledejte konkrétní pole pomocí pole pro vyhledávání „Vyhledat“.
:guilabel:`Hledat“ možnost efektivněji, klikněte na všechny :guilabel:„>> (pravé šipky)“
zobrazit všechna pole.
#Ikona „+“ slouží k přidání políček do pole „Pole“.
exportní seznam.
#. Kliknutím na šipku nahoru a dolů vlevo od vybraných polí lze přesunout
pole nahoru a dolů, změnit pořadí, v jakém jsou zobrazeny ve vyexportovaném souboru.
Přetahování a ponechání pomocí ikony „↕️ (směr nahoru/dolů)“.
#Ikona „koš“ (:guilabel:`🗑️`) se používá k odstranění políček. Klikněte na ikony „koš“ (:guilabel:`🗑️`).
klikněte na ikonu „Smazat pole“.
#Pro opakované zprávy je užitečné mít připravené přednastavení vývozu. Vyberte všechny potřebné položky a
Klikněte na nabídku šablon. Jakmile se tam dostanete, klikněte na „Nový vzor“ a zadejte
jedinečný název pro export právě vytvořený. Kliknutím na ikonu 💾 (magnetofon) uložte export.
konfigurace. Pokud se stejný seznam bude muset exportovat znovu, vyberte příslušný šablonu
Vybraný výraz byl dříve uložen z nabídky.

.. tip::
Je užitečné znát externí identifikátor pole. Například :guilabel:`Související společnost`
v exportním uživatelském rozhraní je rovno *parent_id* (externí identifikátor). To je užitečné
Protože pak se vyexportuje jenom to, co má být upraveno a znovu importováno.

... /essentials/export_import_data/import-data:

Importujte data do Odoo
=====================

Import dat do Odoo je velmi užitečný během implementace nebo v případě, kdy jsou potřeba data.
Aktualizovat v hromadném režimu lze podle následující dokumentace.
dat do databáze Odoo.

.. varování:
Do importu se vkládají trvalé záznamy a **nemohou být** odstraněny. Filtry (vytvořené) však lze použít.
případně „poslední změna“ (např. „last modified“) k identifikaci záznamů, které byly změněny nebo vytvořeny importem.

.. tip::
Aktivací režimu vývojáře se změní viditelné nastavení dovozu v levém sloupci.
menu. Vyvoláním takového menu se objeví :menuselection:`Pokročilé“ menu, které obsahuje dvě
možnosti „Sledovat historii během importu“ a „Povolit shodu s podpoli“.

....... obrázek:: export_import_data/advanced-import.png
:alt:Pokročilé možnosti importu při zapnutém vývojářském režimu.

Pokud model používá openchatter, možnost „Sledovat historii při importu“ nastaví
Předplatné a oznámení během importu jsou zapotřebí, ale zpomalují import.

Pokud je vybrána možnost „Umožnit shodu s podpoli“, pak se všechny podpole
v rámci pole se používají při importu podle :guilabel:`Odoo Field`.

... /základní informace/export/import dat/začínáme:

Začněte
-----------

Data lze importovat do jakéhokoliv objektu v Odoo pomocí buď Excelu (.xlsx) nebo CSV.
(Vícenásobný oddělovač hodnot) (.csv). To zahrnuje: kontakty, produkty, výpisy z bankovního účtu
deníky a objednávky.

Otevřete pohled na objekt, do kterého se mají importovat/naplnit data, klikněte na ikonu „fa-cog“
Ikona „Nástroje“ a výběr „Importovat záznamy“.

.. obrázek:: export_import_data/import-button.png
:alt: Zobrazení nabídky akcí s vybranou možností „Importované záznamy“.

Klikněte na ikonu „Stáhnout“ uprostřed stránky a
stáhněte si šablonu <essentials/export_import_data/adapt-a-template> a vyplňte ji
vlastními daty společnosti. Takové šablony lze do systému importovat jedním kliknutím, protože se
je již přednastavená.

Pro nahrání stáhnutého šablony nebo vlastního souboru postupujte podle pokynů uvedených níže:

#Klikněte na tlačítko „Nahrát soubor dat“ a vyberte požadovaný soubor.
#Upravte možnosti formátování podle potřeby (pouze pro soubory CSV).
#Zajistěte, aby všechny informace v poli „Soubor“ byly správně připojeny k odpovídající
:guilabel:`Odoo Field“ a bez chyb.
#Klikněte na tlačítko „Načíst soubor dat“ (volitelné).
#Klikněte na tlačítko „Test“ a ověřte, zda jsou data platná.
#Klikněte na tlačítko „Import“.

.. poznámka::
Možnosti formátování se **neobjevují** při importu souboru s vlastními daty z aplikace Excel.
typu (.xls nebo .xlsx).

... /essentials/export_import_data/adapt-a-template:

Upravte šablonu
----------------

Šablony pro import jsou k dispozici v nástroji pro import nejčastěji dovážených dat (kontaktů,
produkty, výpisy z účtu atd.) a otevřete je v jakémkoliv tabulkovém editoru (*Microsoft Office*,
*OpenOffice*, *Google Drive*, atd.

Jakmile si stáhnete šablonu, postupujte podle těchto kroků:

- Přidejte, odeberte a přesuňte sloupce tak, aby nejlépe vyhovovaly struktuře dat.
- Je silně doporučeno, aby se neodstraňoval sloupec „Externí identifikátor“ (ID).
(další část).
- Přidělejte každému záznamu jedinečné ID tím, že seřadíte pole ID v řádku :guilabel:`Externí ID`.
sloupci ID.

.. obrázek: export_import_data/dragdown.gif
:alt:Animace myši táhnoucí se dolů po sloupci ID, takže každý záznam má jedinečné ID.

.. poznámka::
Pokud je nová sloupec přidán, Odoo nemusí být schopen jej automaticky přiřadit, pokud jeho název není
doplnit pole v Odoo. Nové sloupce lze však při testování importu ručně přidat.
Vyhledejte příslušné pole v seznamovém menu.

.. obrázek:: export_import_data/field_list.png
:alt: Rozbalený seznam v prvním okně při importu do Odoo.

Pak použijte název pole v souboru importu k zajištění úspěšných budoucích importů.

.. tip::
Další užitečnou cestou, jak zjistit správné názvy sloupců pro import, je exportovat vzorek souboru
použít pole, která mají být importována. Tímto způsobem se vytvoří vzorec pro import, pokud není k dispozici šablona importu.
Jména jsou přesná.


...nutné/externí ID:

Import z jiné aplikace
-------------------------------

:guilabel:`Vnější ID“ (ID) je jedinečný identifikátor pro položku v objednávce. Můžete si ho libovolně vybrat.
z předchozího softwaru, aby se usnadnil přechod na Odoo.

Nastavení ID není při importu povinné, ale pomáhá v mnoha případech:

- „Aktualizace dovozu <essentials/update-data>“: importujte stejný soubor několikrát bez
vytváření duplicitních záznamů.
- :ref:`Pole vztahů <export_import_data/relation-fields>“.

Chcete-li znovu vytvořit vztahy mezi různými záznamy, použijte jedinečné identifikátory původních záznamů.
aplikace by měla být použita k přiřazení jejímu sloupci v Odoo s názvem „Externí identifikátor“ (ID).

Pokud se importuje další záznam, který na první odkazuje, použijte **XXX/ID** (XXX/Externí ID).
originální unikátní identifikátor. Tento záznam lze také najít podle jeho názvu.

.. varování:
Je třeba poznamenat, že konflikty nastávají v případě dvou (nebo více) záznamů se stejným *Externím ID*.

Chybí pole pro mapovací sloupec
---------------------------

Odoo se pokouší automaticky najít typ pole pro každý sloupec v importovaném souboru.
na prvních deseti řádcích souborů.

Příkladem je například sloupec obsahující pouze čísla, kde jsou pole typu *integer*.
Jsou prezentovány jako možnosti.

Toto chování může být většinou prospěšné, ale také se může stát, že selže.
Sloupce může být přiřazen k poli, které není v nabídce výchozího nastavení.

Pokud se tak stane, zkontrolujte možnost „Zobrazit pole vztahových polí (pokročilé)“, pak
seznam všech polí dostupných pro každou sloupcovou hlavu.

.. obrázek: export_import_data/field_list.png
:alt:Hledání pole, které odpovídá sloupci daně.

Změnit formát dovozu dat
-------------------------

.. poznámka::
Odoo dokáže automaticky detekovat, zda je sloupec datem, a pokusí se odhadnout formát data podle
sada nejčastěji používaných formátů dat. Tento proces může fungovat pro mnoho různých formátů dat, ale některé
datumové formáty nejsou rozpoznatelné. To může vést k záměně den/měsíc, což způsobuje
je obtížné odhadnout, která část formátu data je den, a která část měsíc.
datum, například „01-03-2016“.

Při importu souboru CSV (čárkované hodnoty) poskytuje Odoo formátování.
Možnosti.

Pro zobrazení formátu data, který Odoo našel v souboru, se podívejte na pole „Formát data“
je zobrazeno při kliknutí na možnosti pod souborovým výběrem. Pokud je tento formát nesprávný, změňte jej na
přednostní formát, který definuje formát pomocí ISO 8601.

.. důležité::
*ISO 8601* je mezinárodní norma, která pokrývá celosvětovou výměnu dat včetně
komunikace dat a informací o čase. Například formát data by měl být „YYYY-MM-DD“.
V případě data 24. července 1981 by se mělo psát jako „1981-07-24“.

.. tip::
Při importu souborů Excel (.xls, .xlsx) se zvažte použití buňky pro datum k uložení dat.
má uložené formáty dat pro zobrazení, ať už je datum v Odoo jakkoliv formátováno.
Při importu souboru CSV použijte sekci Formátování v Odoo.
vybrat sloupce pro formát data, který chcete do importu zahrnout.

Do importu přidat měnový znak
----------------------------------

Odoo plně podporuje záporné čísla s využitím závorek.
znaky měny připojené k nim. Odoo také automaticky rozpozná, jaký oddělovač tisíců a desetinných čísel je
používány. Pokud se používá měnový znak neznámý Odoo, nemusí být rozpoznán jako číslo a
importní krachy.

.. poznámka::
Při importu souboru CSV (oddělené čárkami) je v nabídce Formátování
se zobrazuje v levém sloupci. Pod těmito možnostmi je k dispozici volba
Změnil se.

Příklady podporovaných čísel (s použitím „třicet dvě tisíce“ jako čísla):

- 32.000,00
- 32000,00
- 32,000.00
- -32000.00
- (32000.00)
- $ 32.000,00
- (32000.00 €)

Příklad, který nefunguje:

- ABC 32.000,-
- $ (32.000,00)

.. důležité::
Znak `()` kolem čísla značí, že je číslo záporné.
Značka měny **musí být** umístěná uvnitř závorek, aby ji systém Odoo rozpoznal jako měnu.
záporná hodnota měny.

Nebyla správně zobrazena náhledová tabulka s importem
--------------------------------------------

Výchozí nastavení importu předzobrazení je oddělovačem položek čárka a uvnitř citaci uvozovky.
oddělovače. Pokud CSV soubor nemá tyto nastavení, upravte
Možnosti formátování (zobrazené pod záložkou „Import CSV“)
(Seznam hodnot oddělených čárkami) po výběru souboru CSV (Seznam hodnot oddělených čárkami).

.. důležité::
Pokud je soubor CSV oddělený čárkou, tak Odoo
**neodhalí oddělené buňky. Formátování souboru musí být upraveno v sešitu
aplikace. Podívejte se na následující odkaz:
oddíl.

... export_import_data/change-csv:

Změnit formát CSV ve tabulkovém procesoru
-------------------------------------------------

Při úpravě a ukládání souborů CSV (oddělené čárkami) v aplikacích pro tabulkový procesor
pro oddělovač a znak oddělující položky se používá nastavení regionu počítače. Společnost Odoo doporučuje
OpenOffice nebo LibreOffice, obě aplikace umožňují úpravu všech tří možností (od
Aplikace LibreOffice, přejděte na: „Dialóg pro uložení souboru“ --> Zatrhněte políčko „Upravit filtr
Nastavení --> Uložit.

Microsoft Excel může měnit kódování při ukládání (dialogové okno „Uložit jako“ -->
Vyberte možnost „Nástroje“ --> „Kódování“.

Rozdíl mezi ID databáze a externím ID
----------------------------------------------

Některá pole definují vztah k jinému objektu. Například země kontaktu je
odkaz na záznam objektu „Země“. Když jsou taková pole importována, musí Odoo znovu vytvořit odkazy
mezi různými záznamy. Odoo poskytuje tři mechanismy k pomoci s importem takových polí.

.. důležité::
*Jen jedno zařízení* by mělo být použito pro každé pole, které je importováno.

Příkladem je například uvedení země kontaktu. Odoo nabízí tři různé pole pro import:

- :guilabel:`Země“: název nebo kód země
- :guilabel:`Země / ID databáze“: jedinečný identifikátor záznamu v Odoo, definovaný jako ID PostgreSQL
sloupec
- „Země / Vnější identifikátor“: ID tohoto záznamu, který je odkazován v jiné aplikaci (nebo
.XML soubor, který jej importoval

Pro například pro zemi Belgii použijte jednu ze tří následujících možností importu:

- :guilabel:`Země“: „Belgie“
- :guilabel:`Stát/ID databáze“: „21“
- :guilabel:`Země/Externí identifikátor“: „base.be“

Podle potřeby společnosti použijte jednu z těchto tří metod pro odkazování záznamů v vztazích.
Je příkladem situace, kdy se používá jedno nebo druhé podle potřeby:

- Použijte :guilabel:`Země“: je to nejjednodušší způsob, pokud jsou data z :abbr:`CSV (oddělené čárkami)
soubory, které vytvořil uživatel ručně.
- Používejte :guilabel:`Země / databáze ID“: tento způsob používání je vzácný a hlavně se používá vývojáři
hlavní výhodou je nikdy nemít konflikt (může být více záznamů se stejným jménem).
ale vždy mají unikátní identifikační číslo databáze
- Použijte pole „Země/Externí identifikátor“: použijte *Externí identifikátor* při importu dat z třetích stran
aplikace.

Při použití externích identifikátorů se do systému importují soubory ve formátu CSV (oddělené čárkami)
:guilabel:`Vnější identifikátor“ (ID) slouží k definování vnějšího identifikátoru každého záznamu, který je importován.
Pak se na tento záznam odkazuje pomocí sloupců jako například „Soubor/Externí ID“.
Dva soubory CSV (oddělené čárkami) poskytují příklad produktů a jejich kategorií.

- :stáhnout:CSV soubor pro kategorie

- :stáhnout:CSV soubor pro produkty


.. export_import_data/vztahy:

Import pole vztahů
----------------------

Odoo objekt vždy souvisí s mnoha dalšími objekty (např. produkt je propojený s produktem).
kategorie, atributy, dodavatele apod.) a pak je do importovaných vztahů zahrnout.
musí být nejprve importovány z vlastního seznamu nabídky.

Toho lze dosáhnout buď použitím názvu souvisejícího záznamu nebo jeho ID v závislosti na
okolností. ID se očekává, pokud jsou dvě záznamy s stejným názvem. V takovém případě přidejte k názvu závorku „/ID“.
na konci názvu sloupce (např. u atributů produktu: „Produktové atributy / Atribut / ID“).

Možnosti více zápasů na hřištích
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pokud například máme dvě kategorie produktů s dítětem jménem „Prodávané“ (např. „Různé“.
Produkty/Prodávané“ a „Jiné produkty/Prodávané“) je ověřování zastaveno, ale data mohou být
importované. Nicméně společnost Odoo doporučuje, aby data nebyla importována, protože se vše propojí s
první kategorii „Prodejné“ v seznamu kategorií produktů („Nezařazené produkty/Prodejné“).
Odoo doporučuje upravit jednu z hodnot duplicitního produktu nebo kategorii produktu.
hierarchie.

Pokud však společnost nechce měnit konfiguraci kategorií produktů, může použít
doporučuje použít pole „Externí identifikátor“ pro pole „Kategorie“.

Importujte vztahy pole mnoho k mnohu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Štítky se oddělují čárkou bez mezer. Například pokud zákazník potřebuje
připojené k oběma tagům „Výrobce“ a „Prodejce“, pak je třeba zašifrovat jako „Výrobce,Prodejce“.
v stejném sloupci souboru CSV (oddělené hodnoty čárkou).

- :stáhnout: `CSV soubor pro výrobce a maloobchodníka <export_import_data/m2m_customers_tags.csv>`

Importujte vztahy jeden-mnoho
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pokud společnost chce dovážet prodejní objednávku s více řádky, musí být konkrétní řádek
rezervované v souboru CSV (Comma-separated Values) pro každou položku objednávky. První položka
do stejné řádky jako informace o objednávce, další řádky potřebují
doplňková řádka, který nemá žádné informace v polích souvisejících s objednávkou.

Příkladem může být soubor CSV (Comma-separated Values) s několika citáty, který lze
importované na základě ukázkových dat:

- :stáhnout:Soubor s citáty


Následující soubor CSV (Comma-separated Values) ukazuje, jak do systému zadat objednávky.
jejich příslušných řádcích objednávky:

- :stáhnout:Objednávky s příslušnými položkami objednávky


Následující soubor CSV (Comma-separated Values) ukazuje, jak do systému importovat zákazníky a jejich
Kontakt pro příslušnou oblast:

- Kontakty zákazníků a jejich příslušných kontaktů


Importovat obrázky
------------------

Importovat obrázky spolu s nahráváním :ref:`<essentials/export_import_data/get-started>
V případě souboru CSV nebo XLS postupujte podle následujících kroků:

#Přidejte názvy obrázkových souborů do příslušného sloupce s daty v tabulce.
#:ref:`Nahrát soubor dat <essentials/export_import_data/get-started> nebo jej znovu načíst
kliknutím na tlačítko „Načíst soubor dat“.
#Klikněte na tlačítko „Nahrát soubory“ pod sekcí „Soubory k importu“.
#Vyberte příslušné obrázky. Počet vybraných souborů se zobrazí vedle tlačítka.
#Klikněte na tlačítko „Test“ a ověřte, že jsou všechna data platná.
#Klikněte na „Import“. Během procesu importu provádí Odoo kontrolu souborů automaticky.
spojit nahrané obrázky s importovaným souborem dat. Pokud není shoda, je soubor dat
bez obrázku.

.. poznámka::
   - Sekce „Soubory k importu“ je aktivní, pokud má váš šablona produktu
:guilabel:`Obrázek“ sloupec s plně vyplněnými poli.
   - Název souboru s daty musí odpovídat názvu nahraného obrázku.
   - Při importu velkého množství obrázků lze specifikovat maximální velikost balíčku v megabajtech
a nastavit zpoždění, aby se systém nezatížil. Pro tento účel je zapotřebí:
vývojářský režim (viz ../obecné/rozvojový_režim`) a vyplňte pole „Maximální velikost souboru“.
pole „Počet souborů“ a pole „Časový odstup mezi jednotlivými soubory“ v poli „Soubory k importu“.
sekci. Výchozí zpoždění odpovídá limitu na volání RPC/API definovanému v části Odoo Cloud -
Zásady používání služby <https://www.odoo.com/acceptable-use>.

Doklady o dovozu zaznamenává několikrát
----------------------------

Pokud do importovaného souboru patří jedna z následujících sloupců: :guilabel:`Externí identifikátor` nebo :guilabel:`Identifikátor databáze`,
Záznamy, které již byly importovány, se upravují namísto vytváření nových. To je extrémně
je užitečná, protože umožňuje uživatelům importovat stejný soubor CSV (hranaté závorky oddělené hodnoty) několikrát.
době mezi dvěma importy udělal nějaké změny.

Odoo se postará o vytvoření nebo úpravu každého záznamu podle toho, zda je nový či nikoliv.

Tato funkce umožňuje společnosti používat nástroj pro import/export v Odoo k úpravě sady záznamů.
v tabulkovém procesoru.

Hodnota pro pole nebyla zadána
---------------------------------------

Pokud nejsou ve souboru CSV nastaveny všechna pole, Odoo přiřadí výchozí hodnotu pro každé nepovinné pole.
pole. Ale pokud jsou pole v souboru CSV nastavena na prázdné hodnoty
Odoo nastaví prázdnou hodnotu v poli namísto přiřazení výchozí hodnoty.

Export/Import různých tabulek z aplikace SQL do Odoo
--------------------------------------------------------------

Pokud je potřeba dostat data z různých tabulek, musí se mezi záznamy vytvořit nové vztahy
přidružené k různým tabulkám. Například pokud jsou do importu zahrnuty společnosti a lidé, je mezi
Každá osoba a společnost, ve které pracuje, musí být znovu vytvořena.

Pro správu vztahů mezi tabulkami použijte funkce „Externí identifikátor“ v Odoo. „Externí identifikátor“
ID záznamu je jedinečným identifikátorem tohoto záznamu v jiné aplikaci. Hodnota pole „Externí ID“ musí být
Je unikátní pro všechny záznamy všech objektů. Je dobrou praxí předcházet tomuto pole názvem
název aplikace nebo tabulky (například „Společnost 1“, „Osoba 1“ – místo „1“)

Příkladem může být databáze SQL s dvěma tabulkami, které se mají importovat: společnosti
a lidé. Každý člověk patří do jedné společnosti, takže mezi člověkem a firmou existuje
musí být znovu vytvořená práce.

Zkuste tento příklad s ukázkovým souborem databáze PostgreSQL
<export_import_data/database_import_test.sql>.

Nejprve exportujte všechny společnosti a jejich vnější identifikační číslo. V PSQL zadejte následující příkaz:

... blok kódu:: sh

>copy (select 'company_'||id as "Externí ID", company_name as "Název", 'True' as "Je společnost" from companies) do /tmp/company.csv s hlavičkou CSV;

Toto SQL příkaz vytvoří následující soubor CSV (Comma-separated Values):

... blok kódu:: text

Externí ID,Jméno,Je firma
společnost_1, Bigees, True
2,Organizace,Pravda
společnost_3,Boum,Pravda

Pro vytvoření souboru CSV (Comma-separated Values) pro osoby spojené s firmami použijte
následujícím příkazem v PSQL:

... blok kódu:: sh



Vytváří následující soubor CSV (Comma-separated Values):

... blok kódu:: text

Exteriérový identifikátor,Jméno,Je společností,Související společnost/Externí identifikátor
person_1,Fabien,False,company_1
2. osoba, Laurence, False, společnost 1
person_3,Eric,False,company_2
4.osoba, Ramsy, False, společnost 3

V tomto souboru pracují pro společnost Bigees („firma 1“) Fabien a Laurence a Eric.
pracovala pro společnost Organi. Vztah mezi lidmi a firmami se dělá přes
Vnější identifikátor společností. Vnější identifikátor je předponou tabulky, aby se předešlo
konflikt identifikátorů mezi lidmi a společnostmi („osoba_1“ a „firma_1“, kteří sdíleli stejný identifikátor 1 v
databáze původních dat).

Dva soubory vytvořené jsou připraveny k importu do Odoo bez jakýchkoliv úprav.
importovaly tyto dva soubory CSV (Comma-separated Values), jsou zde čtyři kontakty a tři
firmy (první dva kontakty jsou spojeny s první firmou). Pamatujte na první import
Společnosti a pak lidé.

... /povinné/aktualizovat data:

Aktualizace dat v Odoo
===================

Existující data lze aktualizovat v hromadném režimu pomocí importu dat, pokud je k dispozici :ref:`externí identifikátor
Zůstává konzistentní.

Připravte se na vývoz dat
-------------------

Abychom aktualizovali data pomocí importu, nejprve se musíme dostat k datům, která chceme aktualizovat, a vybrat možnost
zobrazit seznam. V levém dolním rohu seznamu zaškrtněte políčko u každého záznamu, který chcete
Aktualizujte ji a pak klikněte na |akce| a vyberte možnost :icon:`fa-upload` :guilabel:`Exportovat“ z nabídky.
menu.

V okně s názvem „Export dat“ zvolte zaškrtnutí políčka označeného jako „Chci
aktualizovat data (import/export kompatibilní). To automaticky zahrnuje *Externí identifikační číslo* do
exportu. Dále omezuje seznam polí pro export na pouze tyto pole:
které lze dovážet.

.. poznámka::
V poli „Externí identifikátor“ se **neuvádí** v seznamu „Pole k exportu“.
Pokud není ručně přidána, ale je stále součástí vývozu. Pokud je však :guilabel:`I
Pokud je zaškrtnuté políčko „Aktualizovat data (import-kompatibilní export)“, je zahrnuto do vývozu.

Vyberte požadované pole, které chcete zahrnout do vývozu pomocí možností
„Export dat“ v okně s nápovědou, pak klikněte na „Export“.

Import aktuálních dat
-------------------

Po exportu proveďte veškeré potřebné změny v datovém souboru. Když je soubor připravený, může být
:ref:`importované <essentials/export_import_data/import-data>“ stejným způsobem jako
normální dovoz dat.

.. nebezpečí::
Při aktualizaci dat je velmi důležité, aby zůstala konzistentní hodnota *Externí ID*,
Takto systém identifikuje záznam. Pokud je ID změněno nebo odstraněno, může systém přidat
duplicitní záznam namísto aktualizace stávajícího.
