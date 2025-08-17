================
Vytvářejte otázky
================

V Odoo *Survey* je tvorba a přizpůsobení dotazníků klíčová pro vytváření a
přizpůsobit průzkumy (<../surveys/create>).

Naštěstí Odoo nabízí mnoho způsobů konfigurace přizpůsobených otázek pro jakýkoliv průzkum.

Chcete-li zobrazit seznam všech otázek vytvořených v databázi, přejděte na
:menuselection:`Průzkumy aplikace --> Otázky a odpovědi --> Otázky“. Tam mohou uživatelé zobrazit a upravovat
jakýkoliv dotaz z jakéhokoliv průzkumu.

V aplikaci *Odoo Surveys* je ale pouze jedno místo, kde lze dotazníkové otázky zadávat.
vytvořit. K tomu je potřeba se přesunout na formulář s průzkumem pomocí tlačítka „New“ v aplikaci „Průzkumy“.
Vyberte si z již existujících průzkumů, které jsou na stránce „Průzkumy“ („Surveys app
--> Ankety

Karta otázek
=============

V průzkumném dotazníku mohou uživatelé zobrazit, přistupovat k, přidávat nebo mazat otázky (a sekce).
:guilabel:`Dotazy“ záložka.

V záložce „Otázky“ jsou dvě sloupce: „Název“ (tj.
otázka) a :guilabel:`Typ otázky“.

Pokud je zapnutá volba „Náhodně podle oddílu“ v záložce „Možnosti“,
v dotazníku se objeví sloupec s názvem „Vybrané náhodně“
:guilabel:`Dotazy“ záložka.

Zobrazit sloupec „Povinná odpověď“ na záložce „Otázky“, který ukazuje
klikněte na ikonu „(volitelné sloupce)“
vlevo od názvu sloupce.

.. obrázek: otázky/slider-složka-povinné-odpovědi.png
:align:center
:alt:Výběr z roletky s možností povinné odpovědi v průzkumech Odoo.

Vytvářejte sekce
---------------

*Sekce* rozděluje průzkum na organizované části, aby vizuálně seskupila podobné otázky.
společně. Chcete-li vytvořit sekci, klikněte na tlačítko „Přidat sekci“ v dolní části stránky
Kartě „Otázky“, zadejte požadovaný název sekce, pak buď
Stiskněte klávesu Enter nebo klikněte pryč.

Ve sloupci otázek je čára oddělující sekce zobrazena šedou barvou.

Pak můžete přetáhnout požadované otázky pod sekci nebo přetáhnout titulek sekce na horní část.
(tj. před) požadovanými otázkami v průzkumu, aby se vyplnil oddíl
konkrétní otázky, které se tématu sekce týkají.

Pokud je zapnutá volba „Náhodně podle oddílu“ v záložce „Možnosti“,
při dotazníku se zobrazí číslo „1“ na řádku oddělujícím části, pod nadpisem „:guilabel:#
Kolonka „Vybrané náhodně“.

To znamená, že každý účastník bude vybrán náhodně z jedné otázky ze sekce.
vyplňovat anketu a přeskočit všechny ostatní otázky z vybrané sekce.
Zvolte číslo, vyberte požadovanou hodnotu a vložte ji do jeho políčka. Poté stiskněte
Stiskněte klávesu Enter nebo klikněte pryč.

Vytvářejte otázky
================

Pro vytvoření otázek dotazníku klikněte na tlačítko „Přidat otázku“ v sekci „Otázky“.
tab.

Kliknutím na tlačítko „Přidat otázku“ se otevře okno „Vytvoření oddílů a otázek“.
okně, ve kterém lze vytvořit průzkumnou otázku.

.. důležité:
Pro vytvoření sekcí a podsekcí je nutné zadat název průzkumu.
se zobrazí okno s otázkami. Pokud není pro průzkum zadán titulek, objeví se chybové okno.
V pravém horním rohu se zobrazí zpráva s instrukcemi pro uživatele, aby zadali název průzkumu.

Když jsou všechny požadované konfigurace dokončeny, klikněte na tlačítko „Uložit a zavřít“
dotaz a vraťte se na formulář průzkumu nebo :guilabel:`Uložit & Nový`` pro uložení otázky a vytvoření
nový okamžitě v novém okně s názvem „Vytvoření sekcí a otázek“.

Klikněte na tlačítko „Vyhodit“ a celý dotaz vyhoďte.

Vytvořit okno pro vkládání sekcí a otázek
-------------------------------------------

.. obrázek: otázky/vytvořit-oddíly-otázek-popup.png
:align:center
:alt:Formulář Přidat sekce a otázky v aplikaci Odoo Survey.

V okně „Vytvoření sekcí a otázek“ začněte psát otázku.
políčko „Dotaz“, které se nachází v horní části okna.

Poté vyberte požadovaný typ otázky. Před zobrazením každého typu otázky je k dispozici náhled
vpravo od pole „Typ otázky“, když je vybrán „Typ otázky“.

Vyberte jednu z následujících možností:

- :guilabel:`Výběr více možností: pouze jedna odpověď“: otázka s výběrem více možností, kde je pouze jedna správná odpověď
Je povoleno.
- :guilabel:`Výběr více možností: více odpovědí povoleno“: otázka s výběrem více možností, kde je více
Odpověď je povolena.
- :guilabel:`Textová pole s více řádky“: otevřená otázka, kde mohou účastníci zadat
víceřádkový odpovědní formulář.
- :guilabel:`Textová pole s jednou řádkou“: otevřená otázka, kde účastníci mohou zadat pouze jednu
lineární odezva.
- :guilabel:„Číselná hodnota“: otázka na číslo, kde účastníci musí zadat číslo.
Odpověď.
- :guilabel:`Datum“: otázka s datem, kde účastníci musí zadat datum (rok-měsíc-den).
Odpověď.
- :guilabel:`Datum“: otázka s datem, kde účastníci musí zadat jak datum, tak i čas
(rok-měsíc-den, hodina-minuta-sekunda) jako odpověď.
- :guilabel:`Matice“: vícečetná otázka s více možnostmi odpovědí v tabulkovém uspořádání
účastníci jsou prezentováni různými otázkami na každé řádce a různými možnostmi odpovědí.
každé sloupci.

.. poznámka::
Různé funkce se zobrazují v záložce „Odpovědi“ a „Možnosti“, podle toho,
vybraný typ otázky.

Nicméně vždy zůstává stejná záložka „Popis“, bez ohledu na otázku
typ zvolený.

Jakmile je vybrán typ otázky, jsou k dispozici tři možné záložky s informacemi
může být přizpůsoben pro otázku. Tyto zahrnují záložku „Odpovědi“ (pokud je to vhodné pro
vybrat položku „Typ otázky“ (viz obrázek), záložku „Popis“ a záložku „Možnosti“.

Každá záložka nabízí různé funkce v závislosti na tom, jaký typ otázky byl zvolen.
vybrané.

Karty odpovědí
~~~~~~~~~~~

Karta „Odpovědi“ se zobrazí pouze tehdy, pokud je vybrán typ otázky, který
odpovědi pro účastníka.

Pokud je však vyžadován vlastní odpovědní formulář pro odpověď na zvolený typ otázky, například
například „Textová pole s více řádky“. Nebo pokud odpověď na otázku je typu
Je-li číslo, datum nebo datum a čas, pak se vůbec nezobrazí záložka „Odpovědi“.

Pokud je vybrán typ otázky „Single Line Text Box“,
:guilabel:'Odpovědi' záložka zůstává, i když poskytuje pouze dvě možnosti zaškrtnutí: :guilabel:'Vstup
musí být e-mail a uložit jako přezdívku uživatele“.

.. obrázek: otázky/jednoduchá odpověď.png
:align:center
:alt:Odpovědní políčko typu jednoduchý text v aplikaci Odoo Surveys.

Pokud je zapnutá možnost „Vstup musí být e-mail“, zobrazí se nové pole s názvem „Uložit jako uživatele“.
Zobrazí se e-mailová adresa. Pokud je zaškrtnuté políčko, pak Odoo uloží odpověď účastníka na konkrétní otázku
jako e-mailovou adresu.

Pokud je zapnutá možnost „Uložit odpověď jako uživatelské jméno“, Odoo uloží odpověď účastníka jako
jeho přezdívka.

Pro všechny ostatní platné možnosti otázky typu „Question Type“ s odpověďmi na
účastníkovi se zobrazí stejná záložka „Odpovědi“.

.. obrázek: otázky/možnosti odpovědí.png
:align:center
:alt:Odpovědní tabulka s vybranou možností z více možností v Odoo Surveys.

Zde mohou uživatelé přidat možnosti odpovědí kliknutím na tlačítko „Přidat řádek“ a zadáním
různé možnosti odpovědí na tuto otázku. Pak stiskněte klávesu Enter a zafixujte tak svou odpověď
možnost a okamžitě přidat další. Nebo jednoduše zablokovat odpověď.

Zadané odpovědi se zobrazují v sloupci „Možnosti“ v záložce „Odpovědi“.

Pokud je v sekci „Možnosti“ dotazníku zapnutá některá z možností „Hodnocení“,
Kolonky „Vyhodnocení“ a „Skóre“ se zobrazují vedle kolonky „Volby“.
sloupce.

Chcete-li označit odpověď jako správnou, zaškrtněte políčko pod sloupcem „Správná“.
přesně tuto otázku. Pokud je nastaveno, že
:guilabel:`Typ otázky“, v sloupci :guilabel:`Odpovědi“ může být více odpovědí označeno jako
:guilabel:`Korektní“.

V sloupci „Skóre“ vyznačte počet bodů (pokud nějaké), které by měly být uděleny za
účastníkem za zadání konkrétního odpovědi. Je možné zadat zápornou částku jako
:guilabel:`Skóre“ odebrat body za špatnou odpověď.

Možnost nahrát k odpovědím příslušný obrázek je dostupná na
otázka v řádku pod obrázkem, kliknutím na „Nahrát svůj soubor“
Nahrát požadovanou fotografii.

K odstranění jakékoliv možnosti odpovědi klikněte na ikonu 🗑️ v pravém rohu.
otázky.

Výjimkou je, pokud je zvolená možnost „Matrix“ a „Otázka“.
Typ. Pokud je vybrán tento typ, zůstane v záložce „Odpovědi“ obvyklý
V sekci „Volby“ je sekce „Sloupce“. To proto, že
Možnost Matrix poskytuje odpovědní tabulku, kterou mohou účastníci vyplnit.

.. obrázek: otázky/matrix-odpověď-tabulka.png
:align:center
:alt:Odpovědní tabulka s vybraným typem otázky ve formě matice v aplikaci Odoo Surveys.

Karta popisu
~~~~~~~~~~~~~~~

V záložce „Popis“ okna „Vytvořit sekce a otázky“ je
aby poskytoval jakékoli druhy pokynů, instrukcí nebo jiného doplňkového materiálu
považuje za nezbytné, aby účastníci odpověděli na otázku nebo pochopili její význam.

Vložení popisu není povinné.

Karta Možnosti
~~~~~~~~~~~

V záložce „Možnosti“ okna „Vytvořit sekci a otázku“ je
Existují čtyři dostupné sekce: :guilabel:`Odpovědi`, :guilabel:`Podmínky“, :guilabel:`Pokud
Zobrazit“, a „Živé seance“.

Odpovědi
***************

.. poznámka::
Položky v sekci „Odpovědi“ v záložce „Možnosti“ v dialogovém okně pro vytváření
Pop-up okno sekcí a otázek se liší podle vybraného typu otázky.
a celkově: „Možnosti“ nakonfigurované na průzkumném formuláři.

Typy otázek s více možnostmi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pokud je vybraný typ otázky buď „Výběr více možností: jen jedna odpověď“ nebo
„Výběr více možností: více odpovědí povoleno“, je zde „Zobrazit pole komentářů“
je k dispozici v sekci „Odpovědi“.

Pokud je povoleno, objeví se další dvě pole: „Komentář“ a „Komentář je“.
Odpověď.

.. obrázek: otázky/více možností tabulka.png
:align:center
:alt:Odpovědní část záložky možností při výběru typu otázky s více odpověďmi.

Do pole „Komentář zprávy“ zadejte vodicí zprávu, která pomůže účastníkům vědět, co
(např. „Pokud jiný, uveďte prosím“).

Pokud je zapnutá volba „Komentář je odpověď“, Odoo bere komentovaného účastníka jako odpovídajícího.
Odpověď jako odpověď a ne jen komentář ke otázce. To je nejlépe využitelné ve výzkumných dotaznících
kde není povolena možnost skórování.

Typ otázky s více řádky a textovým polem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pokud je vybraný typ otázky :guilabel:`Multiple Lines Text Box“,
V sekci „Odpovědi“ v části „Možnosti“ se zobrazí pole „Zástupný symbol“.
tab.

.. obrázek: otázky/víceřádkové-umístění.png
:align:center
:alt: Pole pro nahrazení při výběru možnosti víceřádkového pole v průzkumech Odoo.

Do pole „Zástupný text“ zadejte vodítko pro účastníky, které jim pomůže pochopit, co mají dělat.
by měli psát do pole „Víceřádkový text“ předloženého jim.

Typy otázek Jednoduchý textový box, Číselná hodnota, Datum a čas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pokud je vybraný typ otázky „Jednolineární textová pole“, pak „Číselné pole“.
Hodnota“, „Datum“ nebo „Čas“, dvě možnosti se zobrazí v „Odpovědi“.
sekci záložky „Možnosti“: „Zkontrolovat vstup“ a „Výchozí hodnota“.

Pokud je zapnuta možnost „Zkontrolovat vstup“, objeví se pod tímto dvě další pole:
:guilabel:`Minimální a maximální limity“ a „Chyba ověření“.

.. obrázek: otázky/jednoduché-ověření-vstupu.png
:align:center
:alt:Odpovědi v sekci odpovědí při výběru jednoduchého řádkového pole.

Do pole „Minimální a maximální limity“ zadejte minimální a maximální povolené množství.
Ta konkrétní otázka.

V poli „Chyba ověření“ zadejte vlastní zprávu, kterou Odoo zobrazí při odpovědi
Je neplatná.

Do pole „Zástupný text“ zadejte vodítko pro účastníky, které jim pomůže pochopit, co mají dělat.
by měli psát do pole „Víceřádkový text“ předloženého jim.

Omezení
*******************

V sekci „Omezení“ v záložce „Možnosti“ je stejný obsah bez ohledu na
vybrat „Typ otázky“.

.. obrázek: otázky/omezení-sekce.png
:align:center
:alt:Karta Možnosti v sekci Omezení v aplikaci Odoo Surveys.

V sekci „Povinné odpovědi“ je k dispozici pouze jedna možnost: „Odpověď vyžadována“.

Pokud je zapnuto „Odpověď povinná“, znamená to, že konkrétní otázka vyžaduje odpověď.
od účastníka předtím, než může pokračovat. Kromě toho, když je zapnuté pole „Povinná odpověď“,
které odhaluje další pole: „Chybová zpráva“.

Do pole „Chybová zpráva“ vložte vlastní chybovou hlášku, která by měla účastníka vyzvat k
Odpovědět na tuto otázku.

Sekce Podmíněné zobrazení
***************************

:guilabel:`Podmíněné zobrazení“ znamená, že otázka se **jenom** zobrazí, pokud je splněna podmínka
Odpověď byla vybrána v předchozích otázkách (tj. např. guilabel:Vyvolání odpovědí).

.. poznámka::
V části „Podmíněné zobrazení“ v záložce „Možnosti“ není k dispozici.
při náhodném výběru otázek.

V sekci „Podmíněné zobrazení“ je pouze jedno pole: „Spouštěcí podmínky“.
Odpovědi.

.. obrázek: otázky/podmíněné zobrazení sekce.png
:align:center
:alt:Karta možností v aplikaci Odoo Survey s sekcí Podmíněné zobrazení.

V poli „Způsoby spouštění odpovědí“ vyberte konkrétní odpovědi z předchozích otázek.
Vyvolá tuto otázku. Může být vybrán více odpovědí. Nechte pole prázdné, pokud
otázka by měla být vždy zobrazena.

Sekce Živé vystoupení
*********************

Možnosti v sekci „Živé relace“ na záložce „Možnosti“ jsou **pouze**
Podpořené průzkumy *Live Session*.

V sekci „Živé relace“ je k dispozici pouze jedna možnost: „Dotaz
Časový limit“.

.. obrázek: otázky/živé sekce.png
:align:center
:alt:Sekce Živé sezení v záložce Možnosti aplikace Odoo Průzkumy.

Při zapnuté volbě „Časový limit otázky“ určete, jak dlouho (v
:guilabel:'sekundy') musí odpovědět na otázku během ankety v reálném čase.

.. poznámka::
Barvy použité v průzkumu jsou přímo spojeny s barvami, které se používají pro téma webových stránek.
<../../weby/weby/web_design/theme>.
