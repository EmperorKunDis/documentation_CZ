=========================
Modelové, modulární a aplikační systémy
=========================

Model určuje logickou strukturu databáze a způsob ukládání, organizace a
manipulované. Jinými slovy, model je tabulka informací, která může být propojena s dalšími tabulkami.
Model obvykle představuje podnikatelský koncept, jako je objednávka prodeje, kontakt nebo produkt.

Moduly a aplikace obsahují různé prvky, jako jsou modely, pohledy, datové soubory, webové kontroly a
statická data z webu.

.. poznámka::
Všechny aplikace jsou moduly. Větší samostatné moduly se obvykle označují jako aplikace, zatímco ostatní
Moduly obvykle slouží jako doplňky k těmto aplikacím.

.._studio/model-moduly-aplikace/navrhované funkce:

Navrhované funkce
==================

Při vytváření nového modelu nebo aplikace s pomocí Studio můžete zvolit až 14 rychlostních funkcí.
vytváření procesu. Tyto funkce slouží k seskupování polí, výchozích nastavení a pohledů, které jsou obvykle
společně poskytují nějakou základní funkci. Většina z nich může být později přidána.
Ale přidáním je od začátku proces tvorby modelu mnohem snazší. Kromě toho
V některých případech se vlastnosti doplňují, aby byly užitečnější.

Příklad:
Vytvoření modelu s :ref:`studio/models-modules-apps/suggested-features/picture`.
:ref:`studio/models-modules-apps/suggested-features/pipeline-stages` funkcí povolí
obrázek v rozložení karet ve výhledu :ref:`Kanban <studio/views/multiple-records/kanban>`.

.... obrázek:: modelů/modulů/aplikací/obrázky/příprava-snímku-kanban.png
:synchronizace: střed
:alt:Kombinace obrázku a potrubí na kartě Kanban

.._studio/modely/součásti/navrhované funkce/Kontaktní údaje:

Kontaktní údaje
---------------

Vybráním položky „Kontaktní údaje“ se přidává do :ref:`Přehledu formulářů <studio/views/general/form>“.
:ref:`Mnoho k jednomu pole <studio/fields/relational-fields-many2one> spojené s modelem *Kontakt*
dvě z jeho :ref:`Souvisejících polí <studio/fields/relational-fields-related-field>“: :guilabel:`Telefon
a:guilabel:E-mail. Do pole:guilabel:Kontakt je také přidán pohled:ref:Seznam
<studia/zobrazení/více záznamů/seznam>, a také zobrazení mapy <studia/zobrazení/více záznamů/mapa>.
je aktivována.

Příklad:

.... obrázek:: modelů/moduly/aplikace/kontakt.png
:synchronizace: střed
:alt:Kontaktní údaje se zobrazují na formuláři

.._studia/modely/aplikace/navrhované funkce/přiřazení uživatele:

Přiřazení uživatele
---------------

Vybráním položky „Přiřazení uživatele“ se do zobrazení formuláře přidá
:ref:`Mnoho k jednomu pole <studia/pole/vztahová-pole-many2one>`, které je spojené s modelem *Kontakt*.
následujících:guilabel:Doména: Share User není nastavený, aby se zobrazily pouze interní
Uživatelé. Dále je k zobrazení uživatele použit widget :guilabel:`many2one_avatar_user`.
avatara. Pole „Zodpovědný“ je také přidáno do seznamového pohledu
<studia/zobrazení/více záznamů/seznam>.

Příklad:

..... obrázek: models_modules_apps/user-assignment.png
:synchronizace: střed
:alt:Funkce přiřazení uživatele na formuláři

.._studio/modely/přílohy/navrhované funkce/datumní kalendář:

Datum a kalendář
---------------

Vybráním položky „Datum a kalendář“ se přidává do zobrazení Formulářů (viz studio/views/general/form)
Datumové pole (viz studio/fields/simple-fields-date) a aktivuje kalendářový výhled.
<studia/zobrazení/časová osa/kalendář>.

..._studio/model-moduly-aplikace/navrhované funkce/datumový rozsah Ganttova diagramu:

Datum a Gantt
------------------

Vybráním „Datový rozsah a Gantt“ se přidává do :ref:`Zobrazení formulářů <studio/views/general/form>“.
dva pole typu „Datum“ vedle sebe: jedno k nastavení začátku
datum a druhé nastavit datum ukončení, pomocí widgetu „daterange“ a aktivovat
:ref:`Ganttovský pohled <studio/views/timeline/gantt>“.

..._studio/models-modules-apps/suggested-features/pipeline-stages:

Fáze trubky
---------------

Vybráním položky „Stavy potrubí“ aktivujete :ref:`Kanbanovou
<studia/zobrazení/více záznamů/kanban>`, přidává několik polí, například :ref:`Důležitost
a „Stav Kanban“ a tři fáze:
„Nový“, „Ve výrobě“ a „Dokončeno“. Vedle toho je na stránce také „Přístupový panel stavu sestavy“
a pole „Stav Kanbanu“ jsou přidány do zobrazení formuláře.
<studia/zobrazení/všeobecné/formulář>. K pole :guilabel:`Barva“ je přidáno pole :ref:`Seznam
<studia/zobrazení/více záznamů/seznam>.

.. poznámka::
Případně lze později přidat funkci :guilabel:`Pipeline stages`.

.._studio/model/moduly/návrhy funkcí/tagy:

Štítky
----

Vybráním položky Tags se přidává do :ref:`studio/views/general/form`.
:ref:`Studio/Zobrazení/Více záznamů/Seznam“ zobrazuje :ref:`Tagové pole
<studia/pole/vztahová pole - tagy>“, vytvoříme model „Tag“ s přednastavenými právy přístupu
procesu.

.._studio/model-moduly-aplikace/navrhované funkce/obrázek:

Foto
-------

Vybráním položky „Obraz“ se do horního pravého rohu Formulářového pohledu přidává
<studia/výhledy/obecné/formulář> a pole obrázku: <studia/pole/jednoduché-pole-obrázek>.

.. poznámka::
:guilabel:`Obrázek´ lze přidat v pozdější fázi.

..._studia/modely/součásti aplikací/navržené funkce/řádky:

Rozměry
-----

Vybráním položky „Řádky“ se do formuláře vloží pole „Řádky“.
pole <studia/pole/vztahová pole/řádky> v komponentě :guilabel:`Tab`.

.._studio/models-modules-apps/suggested-features/notes:

Poznámky
-----

Vybráním položky „Poznámka“ se do zobrazení formuláře vloží pole pro :ref:`HTML
pole s názvem „Studia / pole / jednoduchá pole - HTML“ na celou šířku formuláře.

.._studio/models-modules-apps/suggested-features/monetary-value:

Hodnota v penězích
--------------

Vybráním položky Monetární hodnota se přidává do :ref:`studia/zobrazení/univerzální/formulář`.
:ref:`Studio/Viditelnost/Mnoho záznamů/Seznam“ a :ref:`Položka Monetární pole
<studia/pole/jednoduché-pole-měnové>. Grafy jsou k dispozici na
Aktivní jsou také „pivtové“ pohledy, viz např. studio/views/reporting/pivot.

.. poznámka::
Do pole „Měna“ je přidáno a skryto z pohledu uživatele.

.._studio/models-modules-apps/suggested-features/company:

Společnost
-------

Vybráním :guilabel:`Společnost` se přidává do :ref:`studia/views/obecné/formulář`.
:ref:`studio/views/multiple-records/list` zobrazuje :ref:`Many2One pole
vztahující se k modelu *Společnost*.

.. poznámka::
To je užitečné pouze v případě, že pracujete ve více společnostech.

.._studio/model-moduly-aplikace/navrhované funkce/vlastní řazení:

Vlastní třídění
--------------

Vybráním položky „Vlastní řazení“ přidáte do seznamu :ref:`zobrazení
„Studio / Zobrazení / Několik záznamů / Seznam“ a ikona „Táhni a přetahuj“, abyste mohli ručně upravit pořadí záznamů.

Příklad:

.. obrázek:: views/list-drag-handle.png
:synchronizace: střed
:alt:Možnost vlastního řazení na seznamovém pohledu

..._studio/modely/příslušenství/navrhované funkce/hovořit:

Chatování
-------

Vybráním položky „Chat“ přidáte do :ref:`Form view <studio/views/general/form>“.
funkce (posílání zpráv, poznámky a plánování aktivit).

.. poznámka::
Později lze přidat funkci „Chatter“.

Příklad:

.... obrázek: models_modules_apps/chatter.png
:synchronizace: střed
:alt:Chatovací funkce na formuláři

.._studio/models-modules-apps/suggested-features/archivace:

Archivace
---------

Vybráním položky „Archivace“ se přidá do formuláře :ref:`studio/views/general/form`.
:ref:`studio/views/multiple-records/list` zobrazuje akci :guilabel:`Archiv“ a skrývá archivované
záznamy z vyhledávání a prohlížení výsledků vypisovaných automaticky.

.._studio/export-import:

Exportní a dovozové úpravy
================================

Když provedete jakoukoli úpravu pomocí studia, vytvoří se nový modul s názvem „studio_customization“.
do vaší databáze. Můžete tento modul exportovat jako soubor ZIP pomocí :guilabel:`Studio Exportu`.
funkci. Modul pak lze do jiného databáze Odoo importovat. To může být užitečné například v případě
například při instalaci nového modulu nebo pro účely školení.

.. poznámka::
Export a importování těchto úprav je možné provádět takto, namísto použití standardního Odoo
exportu a importu funkcí (viz export_import_data) znamená, že se data dostanou do
logickým způsobem. Například pokud modul obsahuje zákazníky a objednávky, zákazníci jsou
Vytvořte je jako první, protože jsou nezbytné pro vytváření objednávek na prodej.

.._studio/export-import/export:

Exportní přizpůsobení
---------------------

Pro exportování přizpůsobení klikněte na tlačítko „Studio“ v hlavním
Odoo dashboard, pak „Export“, poté buď:

- stáhnout všechny nastavení studia kliknutím na tlačítko „Export“; nebo
- Vyberte, která data chcete exportovat kliknutím na: Konfigurace dat a ukázkových dat pro export
<studio/export-import/export/configure>.

..._studio/export-import/export/konfigurace:

Nastavte údaje pro export
~~~~~~~~~~~~~~~~~~~~~~~~

Pro výběr konkrétních modelů k exportu klepněte na tlačítko „Nový“ v okně „Export Studio“.
Pak začněte psát název požadovaného modelu nebo vyberte z nabídky.

..tip:
Klikněte na tlačítko „Preset“ pro zobrazení seznamu všech modelů ve vaší databázi, které obsahují záznamy.
byly upraveny pomocí Studio a všechny vlastní modely vytvořené pomocí Studio. Chcete-li nakonfigurovat jeden z těchto
vývozní modely klikněte na model a otevřete jej pro provedení požadovaných změn.

Zaškrtněte následující možnosti, pokud jsou pro vás relevantní:

- :guilabel:`Demo`: pokud by měly exportované záznamy být považovány za ukázkové při importu.
- :guilabel:`Přílohy“: pokud se mají přílohy související s exportovanými záznamy zahrnout do
export.
- :guilabel:`Aktualizovatelné“: pokud by měly být exportovaná data aktualizována při aktualizaci modulu.

Pokud je třeba, upravte pole „Doména“ pomocí znaku :guilabel:, abyste určili, které záznamy v modelu by měly být
Exportovat. Klikněte na tlačítko „Upravit doménu“ nebo „fa-caret-right“.
Poté klikněte na „Upravit filtr“ a „Upravit doménu“, jak je vhodné.
povinné změny.

Po nastavení modelu pro export klikněte na tlačítko „Export Studio“ a vrátíte se zpět na hlavní obrazovku.
Pro stažení archivu s přizpůsobením pro všechny uvedené modely klikněte na tlačítko „Export“.

.. poznámka::
Není nutné vybírat jeden nebo více modelů, protože všechny uvedené modely budou zahrnuty v
exportu. K odstranění modelu z exportu vyberte jej a klikněte na ikonku „nastavení“
pak tlačítko „Akce“ a poté ikonu „fa-trash-o“ a „Smazat“.

V okně Studio Export:

- nezaškrtávejte políčka, aby se exportovaly pouze změny provedené v aplikaci Studio.
- Zatrhněte políčko „Zahrnout data“ pro zahrnutí dat ze vybraných modelů do výstupu.
- Zatrhněte políčko „Vložit ukázkové údaje“ a vložte do výběru modely, které mají vyznačené
jako ukázkové datové soubory. Vybráním této možnosti se vybere také položka „Zahrnout data“.

Klikněte na tlačítko „Export“ a stáhněte si soubor ZIP.

.. obrázek: models_modules_apps/studio-export.png
:alt:Volba exportu obou datových sad

.._studio/export-import/import:

Importované úpravy
---------------------

.. varování:
Před importem se ujistěte, že cílová databáze je na stejné verzi Odoo a obsahuje
stejné aplikace a moduly jako zdrojová databáze. Studio neobsahuje podkladové moduly
závislosti na exportovaném modulu.

Pro dovoz a instalaci vlastních nastavení studia do jiné databáze Odoo:

#Připojte se k cílové databázi.
#Klikněte na tlačítko „Studio“ v hlavním panelu Odoo.
:guilabel:`Dodavatel“.
#Nahrát exportovaný soubor ZIP. Pokud chcete importovat ukázková data, zaškrtněte políčko „Importovat ukázkové data“.
#Klikněte na tlačítko „Instalovat“.
