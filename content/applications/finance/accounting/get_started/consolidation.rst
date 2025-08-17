=============
Konsolidační fáze
=============

Konsolidace umožňuje sloučit finanční údaje z více nezávislých společností, každé s
vlastní knihy do jednotného pohledu, který poskytuje „spravedlivý obraz“ celkového zdraví skupiny.

Pomáhá vytvářet jasný a komplexní pohled na finanční výkonnost skupiny tím, že spojuje data
z více firem.

.. poznámka::
Konsolidace společností zahrnuje **právně samostatné subjekty**, zatímco :ref:`pobočky
<obecné/firmy/pobočky> jsou **pododděleními** jediné právnické osoby, které často sdílejí
zásobami centrály (časopisy, daně, účetnictví, daňové pozice) a nejsou soustředěny v
Stejně jako oni.

... nástroje pro konsolidaci:

Nástroje pro konsolidaci
===================

Kombinací několika nástrojů se podaří postavit finanční
Konsolidace:

..._konzolidační_účetní_mapování:

#**Mapování účtů:** Podobné účty z různých společností lze seskupit dohromady.
umožňuje Odoo správně je sloučit v konsolidačních zprávách. Pro přidání účtů se přihlaste
:menuselection:`Účetnictví -> Konfigurace -> Skladová kniha“. Klikněte na „Zobrazit“
na účetní lince. V záložce :guilabel:`Mapování` zadejte kód v příslušné společnosti
:guilabel:`Kód“ slouží k přiřazení účtu.

.... obrázek: konsolidace/mapování více společností.png
:alt: Mapování různých kódů na různé společnosti.

...... poznámka: :ref:`Import mapování účtu <consolidation_import_account_mapping> nebo sloučení stávajících
účty používající nástroj pro sloučení :ref:`<consolidation_merge_tool>` mohou proces zjednodušit.

Když se více účtů z jedné společnosti převede na jeden účet v jiné společnosti, pak
je možné seskupit více účtů do jediné řádky v účetní závěrce jiného podniku.
:ref:`skupinami podle <customize-reports/lines-group-by> účetního kódu (account_code)`
než identifikátor účtu („account_id“).

.. poznámka::
Některé zprávy, například :ref:`zisk a ztráta <účetnictví/hospodářské výsledky/zisk-a-ztráta>`
do různých sekcí podle typu účtu. Když tyto zprávy skupíme podle typu účtu
kód, oddělení sekcí jsou zachována, ale v rámci každé sekce je skupinování účtů
je respektován.

...... příklad::
Belgická společnost je mateřskou společností s dceřinou společností, Americkou společností. Americká společnost má
pět příjmů:

      - Prodej výrobků v hodnotě 400 000 Kč - domácí trh
      - Prodej produktů - mezinárodní
      - 410000 Prodej služeb - Konzultace
      - 420 000 USD ročních příjmů z předplatného
      - Přepravní a manipulační příjem 430000

Všechny pět účtů příjmů USA odpovídají jedinému účtu příjmů (účet 700000 Příjmy).
Belgická společnost.

Pro zveřejnění výkazu zisku a ztráty belgické společnosti, který obsahoval jednu řádku pro všechny americké společnosti.
Společnost zahrnuje do svých konsolidovaných účetních výkazů příjmy společnosti s jediným účtem v Belgii.
pět účtů příjmů z americké společnosti musí být přiřazeno k účtu 700000 belgické společnosti.
Výnosový účet a řádky výkazu musí být:ref:`skupinovány podle
<sestavit zprávy/řádky podle skupin účtů>.

......_konzolidaci_víceúčetních_výkazů:

#**Součet účtů:** Účty jsou základem procesu konsolidace. Jsou buď:

   - *Běžné účetní knihy:* Každá společnost v rozsahu konsolidace má svůj vlastní standardní účetnictví
účetní kniha, kde jsou zaznamenány všechny běžné denní transakce. Vynechává společnost
konsolidační účetní knihy.

   - *Víceúčetní kniha pro konsolidaci:* Společnost, která provádí skutečnou konsolidaci, má
speciální víceúčetní knihou, která zahrnuje všechny konsolidační úpravy ostatních společností.
časopisy (takové, které nejsou vedeny ve svých vlastních knihách). To umožňuje zobrazit celkový dopad
z celé řady úprav.

Vytvořit nový účetní deník můžete v menu „Účetnictví -> Konfigurace -> Víceúčetních knih“
a stiskněte tlačítko „Nový“. Zadejte název, vyberte společnost, ke které je účetní kniha spojena
Nejprve je třeba určit, které tituly se mají vedení účtů vyhnout.

......_konzolidační_soubor_výběru_společnosti:

#**Výběr více společností:** Konsolidovaný pohled lze zobrazit pomocí výběru více společností
selektor. Vybrat koncernovou společnost jako aktuální a udělat z ostatních
společnosti viditelné v selektoru jsou zobrazeny všechny položky z konsolidačního
pohledu společnosti.

.... obrázek: konsolidace/multi_company_selector.png
:alt:Vybrat hlavní společnost a aktivovat ostatní.

......_konzolidaci_horizontálních skupin:

#**Horizontální skupiny:** Nástroje pro zpracování dat v Odoo umožňují kombinovat více účetních knih a používat
horizontální skupiny, které zobrazují konsolidovaný výsledek hospodaření nebo výkaz zisku a
společnost přispívá k celkovým konzolidačním číslům.

Pro vytvoření horizontální skupiny postupujte podle těchto kroků:

      - Aktivujte režim pro vývojáře.
      - Přejděte na položku „Účetnictví“ -> „Konfigurace“ -> „Svislé skupiny“ a klikněte
:guilabel:`Nový“.
      - Přidejte „Skupina“ a vyberte „Zprávy“, kde je horizontální skupina
Může být použita.
      - V sloupci „Pole“ klikněte na tlačítko „Přidat řádek“.
      - V okně Vytvořit pravidla přidejte pole a vytvořte nové
Pak klikněte na tlačítko „Uložit a zavřít“.

.. obrázek: konsolidace/horizontální skupiny.png
:alt:Používání horizontálních skupin k zobrazení přispění každé společnosti.

.... důležité::
Když se otevře finanční výkaz, obvykle je nastaven na zákonný pohled, který používá společnost.
běžný účetní deník (včetně jeho konsolidační úpravy). Pro celkový obraz konsolidace je nutné
**zajistěte, aby byl vybrán víceúčetní záznam**, který zahrnuje všechny konsolidační úpravy.

......_konzolidační_měnový_převod:

#**Kumulativní přepočet cizích měn:** Konsolidaci společností s různými měnami
Odoo se stará o překlad.

   - *Účty vlastního kapitálu:* Použijte historickou směnnou hodnotu.

   - *Zisk a ztráta (P&L):* Využijte průměrnou směnnou sazbu.

   - *Výkaz zisku a ztráty (kromě vlastního kapitálu):* použijte konečnou směnnou sazbu.

.... důležité::
Použité sazby jsou aktuálně zvolené společnosti.

... nástroj pro sloučení souborů.

Sloučení účtů
===============

Účty lze sloučit, aby se snížil počet účtů a aby byly standardizovány napříč společnostmi.
je nepovinný, konsolidaci lze provést i bez něj.

Pro použití nástroje pro sloučení vyberte všechny společnosti s účtem, který má být sloučen.
výběr společnosti v pravém horním rohu obrazovky.

.. obrázek: sloučení/nástroj pro výběr společností při slučování účtů.png
:alt:Vybrat všechny společnosti, které mají účty k sloučení.

Pak přejděte na: „Účetnictví“ -> „Konfigurace“ -> „Skladová kniha“.
účty sloučit. Vyberte v nabídce „Akce“ možnost „Sloučit“.
účty“.

V okně „Sloučit účty“ zapněte možnost „Skupiny podle jména?“, pokud je to nutné.
Klikněte na tlačítko „Sloučit“.

Vybrané účty jsou pak sloučeny do jednoho společného účtu, který je přístupný všem vybraným uživatelům.
firmy, jako by účet vytvořily přímo pro sdílení.

... nástroj pro sloučení/rozdělení:

Smazání účtu
=================

Účty lze také oddělit, pokud je třeba.

.. varování:

Poznámka: Odpojení účtů **neodpojí chatovací okna uživatelů z těchto účtů**. Jakmile jsou spojeny,
Historie změn je trvale sloučena.

Pro oddělení účtů vyberte společnost s společným účtem v seznamu společností na horním panelu.
v pravém rohu obrazovky. Poté přejděte na: „Účetnictví“ -> „Nastavení“ -> „Zobrazení
Zvolte účet, ze kterého chcete data odebrat a klikněte na ikonu „Nastavení“ v pravém horním rohu.
vyberte možnost „Nespojovat účty“.

V okně potvrzení se zobrazí varování Odoo s výčtem účtů.
být rozdělen.

.. obrázek: sloučení/nástroj pro potvrzení rozdělených účtů/potvrzovací průvodce.png
:alt:Průvodce potvrzením pro nástroj Sdílené účty - Odpojení.

Klikněte na „Odpojit“. Nový účet pro každou společnost bude vytvořen z původního.
Společný účet.

..._konzolidaci_importu_účetní_mapování:

Import mapování
================

Pro import mapování účtů vyberte všechny související společnosti v seznamu firem.
v pravém horním rohu obrazovky a přejděte na: „Účetnictví“ -> „Konfigurace“ -> „Diagram“.
Účty.

Nejprve vyberte pole k exportu, zvolte účty a klikněte na ikonku
Tlačítko „Akce“ a vyberte možnost „Export“. Poté v poli „Export dat“
okno, přidejte pole „Kódování/Kód“, „Kódování/Společnost“ a
Pole „Externí identifikátor“ pomocí ikony „+“ a klikněte na „Export“. Jinak
Toto pole je povinné.

Druhým krokem je přepracování v tabulce, kde se do každé společnosti na požadovaných účtech zadá požadovaný kód.

Třetí, k importu souboru (formát xlsx nebo csv) do Odoo klepněte na tlačítko „Import“ a v
V sekci „Importní tabulka účtů“ klikněte na „Import CoA“.
Klikněte na tlačítko „Importovat účetní soubor“ nebo „Nahrát datový soubor“.
Poté klikněte na tlačítko „Import“.

Konečně se kódy nyní vztahují na mapovací společnost pro každou společnost.
