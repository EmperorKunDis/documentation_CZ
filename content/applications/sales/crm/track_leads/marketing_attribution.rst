=============================
Zprávy o přičítání marketingových aktivit
=============================

Použijte aplikaci Odoo CRM k vytvoření marketingového přičítacího protokolu, který analyzuje zdroj
vede je a seskupuje tak, aby bylo možné spočítat celkový dopad marketingu na generování leadů.
přičítání, úspěšnost a další.

Dashboard analýzy kontaktů
========================

Začněte tím, že se přesunete na panel „Analýza kontaktů“ kliknutím na „Aplikaci CRM“.
--> Hlášení --> Zákazníci“.

..tip:
Zprávy lze také spustit na panelu „CRM aplikace –> Vedení“ v sekci „Pouze“, která je k dispozici.
Pokud je funkce „Leads“ aktivována na stránce „Nastavení“, bude přístupná.

Pokud se funkce Leads neaktivovala, pak:
Dashboard Pipeline může také sloužit k vytváření reportů.

Oba dashboardy obsahují potřebné filtry a kritéria pro skupinování, abyste mohli spustit přičítání.
zpráva.

.. viz též:
   - :doc:`Převádět vedené případy na příležitosti <../acquire_leads/convert>`
   - Vytváření kontaktů (viz: doc: Create Leads <../acquire_leads/email_manual>

.. obrázek: marketing_attribution/reporting-tab-and-leads.png
:align:center
:alt: Otevřete aplikaci CRM a klikněte na záložku Reporting v horní části stránky, pak klikněte na Leads.

Zobrazení grafu (ikona fa-area-chart) je zobrazováno výchozím způsobem s aktivním nebo
Neaktivní“ a „Vytvořeno: [rok aktuálního roku]“ filtry aktivní v poli „Hledat…“
baru. Grafické zobrazení ukazuje počet vytvořených leadů podle měsíců a prodejních týmů.
S každým prodejním týmem spojeným s vlastní barvou měsíce.

Přepněte na pohled do seznamu (seznam) pomocí možnosti :icon:`oi-view-list` :guilabel:`(list)` kliknutím na příslušný
ikonu umístěné v pravém horním rohu panelu, což umožňuje snadnou vizibilizaci
skupina, která je definována parametrem *Group By*.

.. obrázek: marketing_attribution/list-view-button.png
:align:center
:alt: Klikněte na tlačítko s čtyřmi horizontálními liniemi v pravém horním rohu stránky Analýza kontaktů.

Přidejte parametry UTM
==================

*Moduly sledování Urchin (UTM)* jsou malé kousky textu vložené do URL, které se používají ke sledování
návštěvníka. To zahrnuje parametry týkající se způsobu, jakým návštěvník dosáhl odkazu, jako je typ
navštívené webové stránky a/nebo marketingovou kampaň, ze které návštěva pochází.

Odoo může použít tyto UTM jako parametry v zprávě o přičítání marketingu k sledování metrik a
výkon marketingových kampaní.

Vytvořte UTM
-----------

V Odoo lze použít nástroj :doc:`sledovač odkazů <../../../websites/website/reporting/link_tracker>
vytvářet a konfigurovat UTM.

UTM kódy lze také automaticky vygenerovat pomocí :doc:`Email Marketing
<../../../marketing/email_marketing> a :doc:`Marketing Automation
<../../../marketing/marketing_automation> aplikace.

V marketingovém přičítání se používají parametry *Medium*, *Source* a *Campaign*.
sestupném pořadí pokrytí.

- *Medium* je UTM s nejširším pokrytím a používá se k identifikaci média, které bylo použito pro přístup.
linku. To může zahrnovat média jako sociální sítě, e-mail nebo cena za kliknutí (CPC).
- Zdroj je užší a slouží k identifikaci zdroje provozu. Například jméno
webové stránky, vyhledávač nebo konkrétní sociální síť.
- Kampaň je nejúzká a může sledovat konkrétní kampaně podle názvu.
zahrnovat soutěž nebo název produktu, typ prodeje atd.

Vytvářet zprávy
==============

Pro vytvoření zprávy klikněte na ikonu „fa-caret-down“ vedle
tlačítko „Hledat…“ a zobrazí se vám seznam filtračních a seskupovacích parametrů.

V levém sloupci možností vyhledávání se nachází filtry „Filtr“, které lze použít k tomu, aby se zobrazily jen
výsledky, které odpovídají filtru. Například výběr filtru :guilabel:`Vyhráno` zobrazí pouze kontakty,
Vyhrála je v přidělovacím protokolu.

:guilabel:'Skupina', nacházející se ve střední sloupci, je používána k uspořádání výsledků do skupin.
Může být použita s filtry nebo bez nich.

.. obrázek: marketing_attribution/vyhledavani-s-mnoha-možnostmi.png
:align:center
:alt: Vyberte libovolný počet filtrů a skupin v možnostech vyhledávání.

..tip:
Přiřazení více možností „Skupina“ vytváří podskupiny dle zvolené možnosti
Je vybrána první. Například výběrem „Střední“, následované „Zdroj“.
a pak: „Kampaň“, v sloupci „Skupina“ seřadí všechny výsledky *prvně* podle
médium, pak konkrétní zdroje v každém médiu a nakonec kampaně v každém zdroji.

To lze ověřit pohledem na směr a pořadí výběru v skupinovém panelu.
to se objevuje v poli „Hledat…“.

.. obrázek:: marketing_attribution/group-by.png
:align: center
:alt:Text v titulku je „Země > Město“, což znamená, že město je podskupinou země.

Příklad:
Pro užitečný první report:

    #Vyberte filtr „Aktivní“ z sloupce „Filtry“.
které jsou stále označeny jako aktivní.
    #Vyberte si z sloupce „Skupina“ (v tomto pořadí): „Zdroj“,
Následuje buď :guilabel:`Město`, nebo :guilabel:`Země“, podle toho, která skupina je více používána.
relevantní.

.. obrázek: marketing_attribution/kampaně_a_země.png
:align: center
:alt:Nyní je každá zpráva řazena podle zdroje a poté dle města nebo země.

Tento report obsahuje všechny aktivní kontakty, které jsou seřazeny nejprve podle zdroje kontaktu a poté podle
město nebo zemi, ze kterých každý kontakt pochází. Tato informace je užitečná k určení hustoty aktivních příležitostí
seřazené podle lokality.

S těmito daty lze cílit marketingové kampaně, jako jsou konference nebo billboardy.
míst s největším potenciálem příjmů. Podobně lze věnovat větší pozornost
použít na zvýšení dosahu v místech, kde existují již trvalejší reklamní kampaně.
účinné.

Exportní zprávy
==============

Abychom nastavili měřítka zprávy, začněte procházením ikonou „OI View Pivot“
„Pohled na klíčové ukazatele“ v sekci „Analýza leadů“.

Klikněte na tlačítko „Měření“ a zobrazí se dostupná měření.
výkazu. Vyberte požadované měřítko z roletky (lze vybrat více měření).
a ověřit, zda jsou v tabulce přehledu správně zobrazeny měření, filtry a skupiny.
zajišťuje, aby byla data připravena k exportu.

Pro rychlý vývoz dat do seznamu přejděte na ikonku „OI View List“
:guilabel:`(výpis)“. Klikněte na ikonu :guilabel:`Akce“ :icon:`fa-cog“ :guilabel:`(převodník)“.
je umístěna vpravo od položky „Analýza leadů“ na horním levé rohu stránky a klikněte
:icon:`fa-upload` :guilabel:`Veškeré výstupy“. Zpráva se stáhne automaticky jako soubor .xlsx.

Pro další možnosti exportu lze zprávu exportovat do aplikace Odoo *Dokumenty*.
Klikněte na ikonu „Výhled seznamem“ (seznam v podobě tabulky) na stránce Analýza kontaktů.
Klikněte na ikonu „Akce“ a poté znovu na ikonu „Nástroje“. Nyní přejděte do
:ikonka_fa-table_guilabel_Spreadsheet“ a klikněte na „ikonku_oi-view-list_guilabel_Vložení seznamu“.
spreadsheet“. V okně se zobrazí titulek „Vyberte tabulku, do které chcete vložit seznam.“

Název seznamu lze změnit pomocí pole „Jméno seznamu“, pokud si přejete. Počet položek v
Hlášení můžete nastavit s políčkem označeným „Vložit první _ záznamy seznamu“. Následně vyberte
nebo nový sešit s prázdnými buňkami nebo export do existujícího sešitu. Nakonec klikněte
tlačítko „Potvrdit“.

.. obrázek:: marketing_attribution/dokumenty-export.png
:align:center
:alt: V nabídce nastavte název, počet záznamů a umístění exportu.

Pro vývoz zprávy ve formátu .xlsx pro použití v externím tabulkovém procesoru klikněte na
:guilabel:`Akce“ :icon:`fa-cog“ :guilabel:`(převodovka)“ ikonu a vyberte „:icon:`fa-upload
Možnost „Exportovat vše“. Pokud je vyzván k výběru umístění souboru, pojmenujte jej a pak klikněte
:guilabel:`Uložit“.
