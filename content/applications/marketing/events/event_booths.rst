============
Stánky s programem
============

Aplikace Odoo Events umožňuje uživatelům vytvářet stánky na akcích a prodávat své zboží.
Dostupnost a správu rezervací.

Konfigurace
=============

Pro vytváření, prodej a správu stánků na akcích je nutné využít funkci
aktivován.

Pro toto nastavení přejděte na: „Aplikace události --> Konfigurace --> Nastavení“ a zaškrtněte
Zatrhněte zaškrtávací políčko „Správa kabin“ a pak stiskněte tlačítko „Uložit“.

.. obrázek: event_booths/booth-management-settings.png
:align:center
:alt: Nastavení správy Booth v aplikaci Odoo Events.

.. důležité:
Při zapnuté možnosti „Správa kabin“ se vytvoří nový produktový typ.
<../../inventar-und-mrp/Inventar/Produktverwaltung/Konfigurieren/Typ> se zobrazí na všech
produktové formy: Event Booth.

To je důležité, protože každý vytvořený stánek **musí být přiřazen kategorie Booth**.
respektující stánek a každá kategorie stánku **musí** mít přiřazen produkt Event Booth.
k němu.

Kategorie boxů
================

Při zapnuté funkci Booth Management v aplikaci Events je možné vybrat kategorii stánku.
je v nabídce „Konfigurace“.

Přejděte na stránku „Dashboard kategorie stánků“ v aplikaci „Akce“.
Konfigurace --> Kategorie stánků“, což odhalí seznam všech vytvořených kategorií stánků.

.. obrázek: event_booths/kategorie-stánku.png
:align:center
:alt:Stránka kategorie v aplikaci Odoo Events.

Na stránce kategorie stánku je uvedeno následující informace o každé kategorii stánku:

- :guilabel:`Název kategorie stánku“: název kategorie stánku.
- :guilabel:`Vytvořit sponzora“: pokud je zaškrtnuto, při rezervaci této kategorie stánku se vytváří
uživatel.
- :guilabel:Produkt: produkt Event Booth spojený s konkrétním typem stánku.
- :guilabel:`Cena za místo“: cena za stánek v dané kategorii.

Když se na pravé straně objeví ikonka nastavení
při kliknutí na nadpis sloupce se zobrazí další možnosti sloupců v podobě rozbalovací nabídky.
položka rozbalovací nabídky, zaškrtněte políčko vedle :guilabel:`Stupeň sponzora` a/nebo :guilabel:`Typ sponzora`.
ukázat tyto sloupce na stránce „Kategorie stánku“.

Chcete-li upravit existující kategorii stánku, vyberte ji z seznamu a pokračujte v provádění požadovaných změn.
změny v kategorii událostí.

Vytvořit kategorii stánku
---------------------

Pro vytvoření kategorie stánku z stránky „Kategorie stánků“ klikněte na „Nový“.
tlačítko v horním levém rohu, které odhalí prázdnou kategorii pro stánek.

.. obrázek: event_booths/booth-category-form.png
:align:center
:alt: Typická kategorie stánku v aplikaci Odoo Events.

Začněte zadáním názvu kategorie stánku do pole nahoře vpravo s názvem „Kategorie stánku“.
Povinné pole.

Přidat k dané kategorii stánku příslušný obrázek (například ukázkovou fotografii, jak stánek vypadá).
klikněte na ikonu „fa-pencil“ (pravítko), která se objeví, když kurzor přejede nad
místo kamery v pravém horním rohu kategorie boxu. Po kliknutí se přesune na
Nahrajte požadovanou fotografii do formuláře kategorie fotokiosku (pokud je třeba).

V sekci „Podrobnosti o boxu“ uživatelé **musí** přiřadit produkt.
kategorii a musí mít nastavený produkt typ Event Booth na formuláři produktu.

A přestože je na výrobku Event Booth uvedena cena, můžete si zvolit vlastní.
:guilabel:`Cena“ pro tuto kategorii stánku v poli níže.

V sekci „Podpora“ je možnost zaškrtnout políčko „Vytvořit podporovatele“.
když je objednána kabina patřící do této kategorie, vytvoří se uživatel jako
oficiálním sponzorem akce.

Když je zaškrtnuto políčko „Vytvořit sponzora“, objeví se pod ním další dva pole:
:guilabel:`Úroveň sponzora“ a „Typ sponzora“.

.. poznámka::
:guilabel:`Úroveň sponzora“ a :guilabel:"Typ sponzora" jsou pouze pro rozlišení různých
rozlišení sponzorů. Například pokud je sponzor připojen k společnosti vícekrát
let, získají vyšší úroveň (např. *Zlatou* úroveň), která jim poskytuje
Okamžitá důvěryhodnost a prestiž. Naopak nový sponzor by byl naopak považován za relativně mladého.
a nižší úroveň (např. *Bronzová* úroveň), která odpovídá jeho vlastní důvěryhodnosti a postavení.

Vyberte požadovanou úroveň sponzorství z pole „Sponsor Level“.

..tip:
Chcete-li upravit stávající úroveň sponzora, vyberte ji z rozevíracího pole a pak klikněte
ikonu „fa-arrow-right“ (pravý směrový ukazatel) na konci řádku.
Takže se otevře nová stránka s názvem „Úrovně sponzorství“ a „Stylu lišty“.
Může být změněn, pokud je třeba.

Uživatelé mohou také vytvořit nový „úroveň Sponsora“, zadáním názvu nové úrovně.
klikněte na „Vytvořit a upravit…“ v rozevíracím seznamu, který se zobrazí.

.. poznámka::
V tomto případě kliknutím na položku „Vytvořit“ v rozevírací nabídce, která se zobrazila, vytvoříte
sponzorský úrovni, ale nevyžaduje okamžitě od uživatele další konfiguraci.
:guilabel:`Vytvořit úroveň sponzora“ okno.

Tím se zobrazí okno „Vytvořit úroveň sponzora“.

.. obrázek: event_booths/create-sponsor-level-popup.png
:align:center
:alt:Okno pro vytvoření úrovně sponzora, které se objeví ve výchozím nastavení při otevření aplikace Odoo Events.

Z této okamžité zprávy potvrďte nově vytvořený úroveň sponzora a rozhodněte se o tom, jakou úroveň
pokud je k dispozici, by měl být použit styl :guilabel:`Ribbon Style`. Styl :guilabel:`Ribbon Style“
v tomto seznamu jsou následující možnosti: „Žádný řetízek“, „Zlatý“ a „Stříbrný“.
a:guilabel:'Bronz'.

Pokud je vybrán jeden z nich, objeví se vám na události s názvem „Ribbon Style“ a jménem sponzora.
webové stránky.

V sekci „Podrobnosti o stánku“ pod sekcemi (:guilabel:`Booth Details“ a
„Zakázka“, je v ní záložka „Popis“. Do této záložky zadejte
jakákoliv důležitá informace týkající se kategorie stánku, která by byla pro potenciální
stánek kupujícího musí vědět o něm (např. plocha stánku, případné vybavení, velikost obrazovky atd.)

Přidejte stánek na akci
=====================

Chcete-li přidat stánek na událost, přejděte do existujícího formuláře pro událost pomocí odkazu „Události“.
Aplikace „Události“ a vyberte požadovanou událost z panelu „Události“. Nebo klikněte
:guilabel:`Nový“ pro otevření prázdného formuláře události.

Klikněte na tlačítko „Stánky“ v sekci pro konkrétní akci.
chytře umístěný tlačítko v horní části stránky.

Stránka „Booths“ je zobrazena v kanbanovém pohledu, výchozí stav má dvě různé fáze:
„K dispozici“ a „Nedostupné“.

.. poznámka::
Stránka „Stánky“ akce je také viditelná v :icon:`oi-view-list`.
:guilabel:`Seznam“ Zobrazení, :icon:`fa-area-chart“ Zobrazení grafu a :icon:`oi-view-pivot“
:guilabel:`Výhled Pivot“ a všechny jsou dostupné prostřednictvím jejich ikon v pravém horním rohu
stránky Booths.

Stánky, které jsou k dispozici v sekci `Dostupné`, je možné stále zakoupit.
akci. Stánky vystavené na scéně :guilabel:`Není k dispozici` jsou již prodané a
jsou již nedostupné.

Pro úpravu jakéhokoliv stánku je potřeba kliknout na požadovaný stánek z stránky :guilabel:`Stánky`,
Pokračujte v případných změnách z kabiny. Nebo vytvořte novou, kliknutím na
:guilabel:'Nové' tlačítko v pravém horním rohu, které odhalí prázdný stánek.

Boothová forma
----------

Formulář pro stánek v Odoo Events umožňuje uživatelům upravovat a konfigurovat stánky na různé
různými způsoby.

.. obrázek: event_booths/booth-form.png
:align:center
:alt: Běžný stánek ve verzi aplikace Odoo Events.

Začněte psaním názvu pro stánek, což je **povinné pole**.

Poté přidejte do stánku pole „Kategorie stánku“ (viz guilabel:Booth Category). To je povinný údaj.

..tip:
Novou kategorii boxu lze vytvořit z tohoto pole, pokud do něj napíšete název.
novou kategorii a poté klikněte na položku „Vytvořit a upravit…“ z rozevírací nabídky.
Provedením takového kroku se zobrazí okno „Vytvoření kategorie stánku“, které obsahuje všechny standardní pole.
nalezené na společném formuláři kategorie stánku.

Základní kliknutí na položku „Vytvořit“ z rozevírací nabídky vám vytvoří kategorii, ale
neukazuje okno „Vytvoření kategorie stánku“. Kategorii byste si museli vytvořit sami.
může být později upravena na stránce „Kategorie Booth“ (:menuselection:`Aplikace události --> Konfigurace
--> Kategorie stánků.

Při výběru již existujícího pole „Kategorie kabinky“ se zobrazí dvě další pole, která nelze měnit.
zobrazit: „Produkt“ a „Cena“. Oba pole představují své odpovídající výběry.
pro konkrétní kategorii stánku.

Když si někdo pronajme stánek na webu akce, následný nájemce se musí zaregistrovat.
Pole na formuláři se automaticky vyplní podle informací poskytnutých kupujícím během
online transakce. Bojler se automaticky změní ze stavu *Volný* na
Není k dispozici.

Pokud však pronájem stánku probíhá jiným způsobem (např. osobně, prostřednictvím objednávky prodeje),
atd.), :guilabel:'Nájemce', :guilabel:'Jméno nájemce', :guilabel:'E-mail nájemce' a
V polích „Telefon pronajímatele“ lze zadávat ručně.

Stav stánku (:guilabel:`Dostupný“ nebo :guilabel:`Nedostupný“) lze také změnit
ručně, buď kliknutím na příslušný stav ze seznamu stavů uvedeného v rámečku formuláře pro hlasování.
nebo přetažením a ponecháním požadovaného stánku na příslušnou scénu prostřednictvím stránky Booths.
Kanban pohled.

Prodávejte stánky na akce
=================

S konfigurovanými stánky na události vytvořenými prostřednictvím událostí specifických stránek pro stánky (Booths) představuje Odoo
na webu události prostřednictvím odkazu na událost „Získat stánek“ v podnadpisu.

Chcete-li se dostat na stránku „Zarezervuj si stánek“ na webu akce, otevřete aplikaci „Akce“ a
Vyberte požadovanou událost na panelu „Události“ a z událostního formuláře klikněte na
Klikněte na tlačítko „Přejít na webovou stránku“ a budete přesměrováni na webové stránky události, které byly vytvořeny pomocí Odoo.

Pokud se v podnadpisu události nezobrazuje nabídka „Získat stánek“ (s možností :guilabel:`Get A Booth`),
Webové stránky události existují dvě možnosti, jak se zobrazí.

Na webu akce klikněte na tlačítko „Upravit“ a vstupte do režimu úprav.
v pravém horním rohu. Pak klikněte do záložky „Nastavení“ vzniklého panelu webových stránek.
nástroje pro návrh.

V záložce „Nastavení“ klikněte na přepínač pro „Podmenu (konkrétní)“.
Klikněte na tlačítko „Uložit“. To zobrazí podnadpis události s různými možnostmi.

Alternativně zadejte :doc:`Režim ladění <../../general/developer_mode>` a otevřete konkrétní událost.
v aplikaci *Události*.

Ve formuláři události se při zapnutém režimu ladění objeví pole s možnostmi podnadpisů. Zatrhněte
zaškrtávací políčko „Webový podmenu“, aby se na webu akce zobrazilo podmenu.
Provedením takového kroku se automaticky zaškrtne každý další související políčko.

V tomto bodě pokračujte v výběru možností, které chcete udržet na podnadpisu události. V tomto případě
Zkontrolujte, zda je zaškrtnutá políčka „Registrace na stánku“.

Odtud klikněte na podnadpis „Získat stánek“ v nabídce možností události. To odhalí
stránce „Získat stánek“, kde jsou všechny konfigurované stánky založené na
forma události.

.. obrázek: event_booths/get-a-booth-page.png
:align:center
:alt:Běžná stránka s informacemi o stánku na webu akce prostřednictvím aplikace Odoo Events.

Od zde může návštěvník vybrat požadovanou variantu stánku a poté „Lokalita“. Následně
kliknutím na tlačítko „Rezervuj si stůl“ v dolní části stránky „Zarezervujte si stůl“.
Stránka Boothové.

Tím se zobrazí stránka „Kontaktní údaje“, kde vyplňují buďto „Kontaktní údaje“
nebo „Podrobnosti o sponzorech“, v závislosti na tom, jak byl stánek konfigurován ve formuláři akce.
Údaje na tomto formuláři se liší v závislosti na tom, zda je určen pro základní kontakt nebo sponzora akce.

.. poznámka::
Pokud je v dané bance zaškrtnuto políčko „Vytvořit sponzora“, tato stránka se zobrazí jako „Sponzor
Podrobnosti*

Tato stránka s podrobnostmi o pronajímateli se používá k automatickému vyplnění informací týkajících se pronajímatele.
informace o stánku v záložce „Akce“ aplikace *Event*.

Po zadání potřebných informací klikne návštěvník na tlačítko „Pokračovat“.
Vyplňte údaje o platbě na konci stránky a pokračujte v běžném procesu dokončení objednávky.

Pokud je platba potvrzena, vybraná místo se automaticky přesune do stavu *Nedostupné*.
stánek na stránce s událostí v aplikaci Events (přístupná přes Booths)
chytře umístěný tlačítko na události (event form)).

Dále jsou poskytnuty informace o *sponzorovi* (pokud je k dispozici) a informace o *objednávce*.
přístupné z konkrétního události prostřednictvím jejich příslušných chytrých tlačítek, které se objeví na horní liště.
v podobě.

.. poznámka::
Klikněte na tlačítko „sponzoři“ a upravte případně potřebné informace o sponzorech.

.. viz též:
   - :doc:`create_events“
   - :doc:`prodávat lístky“
