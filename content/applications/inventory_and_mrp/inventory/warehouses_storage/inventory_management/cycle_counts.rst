============
Počet cyklů
============

Pro většinu firem je nutné skladové zásoby spočítat jen jednou ročně. Proto se výchozí hodnota
Po provedení inventarizační úpravy v Odoo je termín dalšího inventárního záznamu
do konce letošního roku.

Některé podniky však potřebují mít vždy přesnou skladovou zásobu.
Společnosti používají metodu „počítání cyklů“ k tomu, aby udržely kritické zásoby přesné. Metoda počítání cyklů je
které společnosti evidují svůj majetek častěji v některých lokalitách, aby zajistily
Fyzické inventarizační záznamy odpovídají záznamům v inventáři.

Konfigurace
=============

V Odoo se počítá podle skladu. Proto je potřeba mít v nastavení funkce
musí být zapnuty před provedením cyklového počítání.

Pro zapnutí této funkce přejděte do sekce „Inventářová aplikace – Konfigurace – Nastavení“.
a posuňte se dolů do části „Sklad“. Pak zaškrtněte políčko vedle
Klikněte na „Uložit“.

.. obrázek: cycle_counts/cycle-counts-enabled-setting.png
:align:center
:alt:Povolení nastavení skladových míst v nastavení inventáře.

Změňte frekvenci záznamu skladových zásob podle místa
============================================

Jakmile je zapnutá funkce „Uložiště“ a vytvoříte více umístění,
skladu lze pro konkrétní místo změnit frekvenci záznamů o stavu zásob.

Pro zobrazení a úpravu polohy přejděte na: „Inventářová aplikace - Konfigurace“
Lokalit“. To odhalí stránku „Lokalit“ obsahující každou lokalitu, která je v současné době vytvořena.
a uloženy na skladě.

Na této stránce klikněte na místo, abyste zobrazili nastavení a konfigurační stránku pro dané místo.
Lokalita.

V sekci „Periodické počítání“ najděte „Četnost inventury (dny)“.
pole, které má být nastaveno na hodnotu 0 výchozího nastavení (pokud tato poloha nebyla dříve upravena).
Toto pole změňte na libovolný počet dnů požadovaný pro frekvenci sčítání.

.. obrázek: cycle_counts/cycle-counts-frequency-value.png
:align:center
:alt:Nastavení frekvence pro dané místo.

Příklad:
Místo, které potřebuje inventuru každých 30 dní, by mělo mít :guilabel:`Inventarizační
Četnost (Dny)` nastavena na hodnotu 30.

Nyní, když byla k této lokalitě aplikována inventarizace, je další plánovaný termín pro sčítání
automaticky nastavené na základě hodnoty zadané do pole „Četnost inventury (dny)“.

Sčítat zásoby podle lokalit
===========================

Pro provedení cyklického počtu pro konkrétní místo v skladu přejděte na
:menuvolba:„Aplikace inventáře -> Provoz - > Fyzická inventura“. To odhalí
stránka „Úpravy zásob“ obsahující všechny produkty, které jsou momentálně skladem, s každým produktem
vlastní řádku.

Z této stránky lze přejít na možnosti filtrů a seskupení dat (přístupné kliknutím na
Ikona „Dolů“ (ikona vpravo vedle ikony „Hledat…“) může být použita k
vybrat konkrétní lokality a provést inventarizaci.

Pro výběr konkrétního místa a zobrazení všech produktů v daném místě klikněte na tlačítko „⬇️
(svislá šipka) vedle ikony „Hledat…“ a poté v poli „Skupit podle“.
sloupec, klikněte na tlačítko „Přidat vlastní skupinu“ pro zobrazení nového seznamu.

.. obrázek: cycle_counts/cycle-counts-filter-menu.png
:align:center
:alt:Filtry a rozbalovací nabídka na stránce Změny zásob.

Vyberte položku „Místo“ z nabídky. Tím se produkty řadí do skladu
místo na stránce „Úpravy zásob“ a cyklický počet může být proveden pro všechny
v daném místě.

..tip:
Ve velkých skladech s více lokalitami a vysokým objemem produktů mohlo být snazší
hledat konkrétní požadovanou položku. K tomu je potřeba z nabídky „Změny zásob“
Stránku otevřete kliknutím na ikonu „↓“ vedle pole „Hledat…“.

Pak v sloupci Filtry klikněte na tlačítko Přidat vlastní filtr.
:guilabel:`Přidat vlastní filtr“ okno.

V prvním poli klikněte na hodnotu a z nabídky vyberte možnost:guilabel:"Lokalita".
Vyberte pole „obsahuje“ ve druhém poli a do třetího pole zadejte název
místo, které je hledáno.

Klikněte na tlačítko „Přidat“ pro zobrazení polohy na stránce.

.... obrázek: cycle_counts/cycle-counts-add-custom-filter.png
:srovnání: do středu
:alt: Přidejte okno s filtrem, ve kterém jsou vyplněny hodnoty umístění.

Změna frekvence plného sečtení zásob
=====================================

Při sčítání cyklistů se zpravidla počítá za jednotlivé lokality.
počty všech skladových položek v skladu lze také ručně změnit, aby se posunul termín
dříve, než je uvedeno datum.

Pro změnu výchozího termínu vyberte v menu volbu „Skladové aplikace - Konfigurace“.
Nastavení“. Pak v sekci „Provádění“ najděte „Den inventarizace za rok
a pole měsíce, které obsahuje vybrané pole s hodnotou „31“ pro prosinec.
výchozím nastavení.

.. obrázek: cycle_counts/cycle-counts-frequency-calendar.png
:align:center
:alt:Část frekvenčního pole v nastavení aplikace pro inventář.

Pro změnu dne klikněte na „31“ a změňte jej na den v rozmezí „1–31“, podle
požadovaný měsíc v roce.

Pak klikněte na tlačítko „Prosinec“ a zobrazí se nabídka. Vyberte
žádaný měsíc.

Klikněte na tlačítko :guilabel:`Uložit`, jakmile budou provedeny všechny potřebné změny.

.. viz také:
   - :doc:`počet produktů“
   - :doc:`use_locations“
