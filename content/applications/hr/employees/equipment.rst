=========
Vybavení
=========

Mnoho zaměstnanců dostává různé věci k použití během práce, jako jsou například notebooky, telefony a
tiskárny. Většina společností sleduje své vybavení, aby viděla, kdo jaké zařízení používá, a také má záznamy
důležité informace o zařízení, jako jsou sériové čísla, záruční podmínky a
historie údržby.

.. poznámka::
Pro sledování vybavení zaměstnanců je aplikace **Údržba** nutná.

.. zaměstnanci/zařízení:

Osobní vybavení zaměstnance
=============================

Výbava zaměstnance je sledována v záznamu o zaměstnanci. Chcete-li zobrazit všechny aktuálně přiřazené výrobky,
Přejděte do aplikace „Zaměstnanci“ a klikněte na požadovaný záznam zaměstnance.

Na vrcholu záznamu se objeví tlačítko s ikonou „:fa-cubes“ a štítkem „Počet vybavení“, které umožňuje
číslo ukazující, kolik, pokud ještě nějaké, položek jsou aktuálně přiděleny tomuto zaměstnanci.

Klikněte na tlačítko „Počet zařízení“ a zobrazí se všechna aktuálně používaná zařízení.
přiřazený zaměstnanci se zobrazuje v jednotlivých kartách Kanbanu.

Každá kartička Kanbanu zobrazuje na první řádce název a model zařízení, následované sériovým číslem.
pořadové číslo (pokud je k dispozici) a nakonec jméno zaměstnance. Všechny aktuální požadavky na údržbu se zobrazují
spodní část karty v červeném rámečku.

.. obrázek: vybavení/vybavení.png
:alt: Přehled všech zařízení pro zaměstnance.

.. poznámka::
Sériové číslo není potřeba při zadávání techniky.

Všechno vybavení zaměstnanců
======================

Pro zobrazení všech zařízení pro všechny zaměstnance začněte v záznamu o vybavení jednotlivce.
zaměstnanci <vybavení/zaměstnanci>“.

.. poznámka::
Nezajímá nás, kdo bude vybrán, nebo jestli má nějaké zařízení přiděleno.
Tento krok je pouze pro dosažení seznamu :guilabel:`Vybavení`.

V kanbanovém pohledu na vybavení zaměstnance odstraňte výchozí hodnotu: guilabel:Přidělený zaměstnanec
filtr v hledání. Tento přístup zobrazuje *všechno* vybavení v databázi, včetně zařízení přiřazených
jednotliví zaměstnanci a celé oddělení.

Zadejte do vyhledávacího pole a zvolte: „Zaměstnanec“ v ikoně „Skupina“
Kanbanová tabulka. Nyní je vybavení organizované podle zaměstnance.

V zobrazení KanaBan s přehledem všech záznamů o vybavení zaměstnanců lze zařízení přidělit.
kliknutím a přetažením karty vybavení na požadovaného zaměstnance, což mění vlastnictví
vybavení.

.. obrázek: vybavení/vsechny-vybaveni.png
:alt: Přehled všech strojů pro všechny zaměstnance.

Přidat vybavení do záznamu zaměstnance
===================================

Chcete-li přidat vybavení do záznamu zaměstnance, otevřete aplikaci „Zaměstnanci“, klikněte na
požadovaný záznam zaměstnance, pak klikněte na tlačítko „Chytré tlačítko“ s ikonou „Krychle“ a textem „Počet zařízení“.
na vrcholu.

Všechno vybavení, které je aktuálně přiděleno zaměstnanci, se zobrazuje na jednotlivých kartách Kanban.
zaznamenáváte vybavení, klikněte na tlačítko „Nový“ v pravém horním rohu, a poté
Formulář načítá seznam vybavení.

Vyplňte formulář pro vybavení (viz /inventory_and_mrp/maintenance/add_new_equipment).
Vybavení zaměstnance.

.. tip::
Místo vyplnění nového formuláře „Vybavení“ pro stejný předmět lze použít stávající formulář.
duplikován a poté aktualizován.

Na formuláři „Vybavení“ klikněte na ikonu „Akce“ (označení „fa-gear“)
v pravém horním rohu a poté vyberte ikony „fa-clone“ a „Duplikovat“.

Vyplněný je identický formulář s veškerými údaji kromě
:guilabel:`Sériové číslo“.

Do pole „Sériové číslo“ zadejte hodnotu a provádějte další potřebné změny.
přiřazený zaměstnanec.

.... obrázek: vybavení/vybaveni-form.png
:alt: Duplicitní vyplněný formulář s výbavou, kromě sériového čísla.
