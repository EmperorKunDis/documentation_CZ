============================
Kapitola 2: Vytvořte panel nástrojů
============================

První část tohoto návodu vás seznámila s většinou nápadů Owlu. Nyní je čas naučit se
Odoo JavaScript framework v celé jeho šíři, jak jej používá webový klient.

.. graf TD
...     podgraf „Sova“
..                   C[Komponenta]
..          T[Šablona]
...           H[Hook]
..          S[Slot]
..           E[Událost]
...                   konec

...      odoo[Odoo JavaScript framework] --> Owl

.. obrázek: 02_vytvořit_dashboard/dříve_se_učilo.svg
:align:center
:šířka: 50 %

Pro začátek potřebujete běžící Odoo server a vývojové prostředí. Než se pustíte do práce
Do cvičení se ujistěte, že jste všechny kroky popsané v této
:ref:`Úvodní příručka <tutorials/discover_js_framework/setup>“. V tomto kapitole začneme
z prázdného panelu nabízeného pluginem „Awesome Dashboard“. Postupně budeme přidávat
přidávat funkce do něj, pomocí rámce pro skriptování v jazyce JavaScript Odoo.

.. varování: Cíl

.... obrázek: 02_vytvoření dashboardu/přehled 02.png
:synchronizace: střed

..spoiler:: Řešení

Řešení každé úlohy kapitoly jsou uveřejněna na
„oficiální repozitář návodů k použití Odoo
<https://github.com/odoo/tutorials/commits/{CURRENT_MAJOR_BRANCH}-discover-js-framework-solutions/awesome_dashboard>.

1. Nový layout
===============

Většina obrazovek v webovém klientu Odoo používá společný formát: ovládací panel nahoře s několika tlačítky.
a hlavní obsahová zóna pod ním, což je provedeno pomocí komponenty Layout.
<{GITHUB_PATH}/addons/web/static/src/search/layout.js>`, dostupné v @web/search/layout.

#Aktualizujte komponentu „Awesome Dashboard“ umístěnou v souboru :file:`awesome_dashboard/static/src/`.
Komponenta Layout. Můžete ji používat
:kód: {panelKontroly: {}} } pro vlastnosti display
komponenta Layout.
#Přidejte vlastnost třídy do Layoutu: „className='o_dashboard h-100'“
#Přidejte soubor dashboard.scss, ve kterém nastavíte pozadí třídy .o_dashboard na šedou barvu (nebo vaši
(oblíbená barva)

Otevřete http://localhost:8069/web a poté otevřete aplikaci Awesome Dashboard.
výsledek.

.. obrázek: 02_postavit_dashboard/nové_zobrazení.png
:align:center

.. viz též:

   - Příklad: použití Layout v akci klienta
<{GITHUB_PATH}/addons/web/static/src/webclient/actions/reports/report_action.js>
„<{GITHUB_PATH}/addons/web/static/src/webclient/actions/reports/report_action.xml>“
   - Příklad: použití Layout v kanbanovém zobrazení
<{GITHUB_PATH}/addons/web/static/src/views/kanban/kanban_controller.xml>`_

.. _tutorials/discover_js_framework/services:

Teorie: Služby
================

V praxi může být každá složka (kromě kořenové složky) kdykoliv zničena a nahrazena.
(nebo ne) s jiným komponentem. To znamená, že stav každé složky není trvalý.
Je to v pořádku ve spoustě případů, ale určitě existují situace, kdy chceme nějaká data uchovat.
Příkladem je skutečnost, že všechny zprávy v kanálu Diskuse by neměly být načítány pokaždé, když se zobrazí kanál.

Dále může dojít k tomu, že budeme psát nějaký kód, který není komponentou. Třeba něco, co
zpracovává všechny čárové kódy nebo spravuje uživatelské konfigurace (kontext apod.)

Rámec Odoo definuje myšlenku služby, která je trvalá.
kus kódu, který exportuje stát a/nebo funkce. Každá služba může být závislá na jiných službách a
komponenty mohou dovážet služby.

Následující příklad registruje jednoduchou službu, která každých pět sekund zobrazí notifikaci:

... kódový blok::js

import { registry } z "@web/jádro/registry";

const myService = {
závislosti: ["notifikace"]
start(env, { notification }) {
let counter = 1;
setInterval(() => {
notification.add(`Tik tik ${counter++}`);
           }, 5000);
       },
   };

registry.kategorie<služba>().přidat(„můjServis“, můjServis);

Služby může využívat jakýkoliv komponent. Představte si, že máme službu pro správu nějakých sdílených
stát:


... kódový blok::js

import { registry } z "@web/jádro/registry";

const sharedStateService = {
start(env) {
stav = {};
return {
getValue(key) {
návrat hodnoty stavu pro klíč.
               },
setValue(klíč, hodnota) {
stav[klíč] = hodnota;
               },
           };
       },
   };

registry.kategorii("služby").přidat("společný stav", sharedStateService);

Pak může tento postup provést jakýkoliv komponent:

... kódový blok::js

import { useService } z "@web/core/utils/hooks";

setup() {
tento.společnýStav = použít službu ("společný stav");
const hodnota = tento.sharedState.getValue("nějaký klíč");
      // do something with value
   }

2. Přidejte několik tlačítek pro rychlou navigaci
========================================

... DOKONČIT: Přidat odkaz na službu akce, jakmile bude dokumentována.

Důležitou službou poskytovanou společností Odoo je služba „akce“: může provádět
všechny typy standardních akcí definovaných v Odoo. Například takto:
komponenta může provést akci podle svého XML ID:

... kódový blok::js

import { useService } z "@web/core/utils/hooks";
   ...
setup() {
tento.akce = použít službu ("akce");
   }
openSettings() {
tato.akce.vykonat(„base_setup.action_general_configuration“);
   }
   ...

Přidejme si na ovládací panel ještě dvě tlačítka:

#Tlačítko „Zákazníci“, které otevře kartový pohled na všechny zákazníky (tato akce již
existuje, tak byste měli použít jeho XML ID
<https://github.com/odoo/odoo/blob/1f4e583ba20a01f4c44b0a4ada42c4d3bb074273/odoo/addons/base/views/res_partner_views.xml#L510>).

#Tlačítko „Vedení“, které otevře dynamickou akci na modelu crm.lead s seznamem a formulářem
zobrazení. Sledujte příklad použití služby akce

   /static/src/components/journal_dashboard_activity/journal_dashboard_activity.js#L28-L35>`_.

.. obrázek: 02_postavit_dashboard/navigační_tlačítka.png
:align:center

.. viz též:
„Kód: akce služby


3. Přidejte položku do panelu nástrojů
=======================

A teď se pustíme do obsahu.

#Vytvořte obecný komponent DashboardItem, který zobrazí svůj výchozí slot v hezkém karetním uspořádání.
Mělo by přijímat volitelný počet číslic vlastností, které mají výchozí hodnotu 1. Šířka by měla být
v pevně dané hodnotě „(18 * velikost) modulo“.
#Přidejte dvě karty do panelu nástrojů. Jednu bez velikosti a druhou s velikostí 2.

.. obrázek: 02_postavit_přístrojovou desku/přístrojová lišta.png
:align:center

.. viz též:
„Systém slotek“ (odkaz na soubor _<{OWL_PATH}/doc/reference/slots.md>_)

4. Zavolejte na server a přidejte nějaké statistiky
=======================================

Pojďme si vylepšit panel přidáním několika položek panelu, které budou zobrazovat skutečná data podnikání.
Dodatek „Awesome Dashboard“ poskytuje cestu na adrese /awesome_dashboard/statistics, která je určena
vracet zajímavé informace.

Pro volání konkrétního kontroleru potřebujeme použít funkci rpc: :ref:`<frontend/services/rpc>`.
Exportuje pouze jednu funkci, která provádí požadavek: :code:`rpc(route, parametry, nastavení)`
Základní požadavek může vypadat takto:

... kódový blok::js

import { rpc } z "@web/jádro/síť/rpc";
   // ...

setup() {
onWillStart(() => {
const výsledek = očekávaný výstup z RPC "/my/controller" s parametry a: 1, b: 2.
      })
      // ...
   }

#Aktualizujte „Přístrojovou desku“ tak, aby používala funkci „RPC“, a zavolejte trasu „Statistiky“ /awesome_dashboard/statistics.
#Zobrazte na palubní desce několik karet, které obsahují:

   - Počet nových objednávek v tomto měsíci
   - Celkový objem nových zakázek v tomto měsíci
   - Průměrná cena trička na objednávku v tomto měsíci
   - Počet zrušených objednávek v tomto měsíci
   - Průměrný čas pro objednávku od „nové“ po „odeslanou“ nebo „zrušenou“

.. obrázek: 02_postavit_dashboard/statistiky.png
:align:center

.. viz též:
„Kód: RPC: {GITHUB_PATH}/addons/web/static/src/core/network/rpc.js“

5. Vytvořit síť cache, vytvořit službu
========================================

Pokud otevřete v prohlížeči panel nástrojů a zvolíte záložku „Síť“, uvidíte, že volání
Výpočet statistiky je prováděn při každém zobrazení akce klienta, protože
Hook „onWillStart“ je volán každýkrát, když se komponenta „Dashboard“ připojí. V tomto případě však
chce se jen jednou a my potřebujeme mít nějaký stav venku z
„Přístrojová deska“. To je hezký případ použití služby!

#Registrujte a do systému importujte nový „awesome_dashboard.statistics“ službu.
#. Měl by poskytnout funkci loadStatistics, která po zavolání provede skutečnou RPC.
Vždy se vrátí stejná informace.
#Použijte funkci memoize (https://github.com/odoo/odoo/blob/1f4e583ba20a01f4c44b0a4ada42c4d3bb074273/
addons/web/static/src/core/utils/functions.js#L11>_ funkce z
@web/core/utils/functions, který umožňuje ukládat statistiky do mezipaměti.
#Tento nástroj je k dispozici v komponentě „Přístrojová deska“.
#Zkontrolujte, zda funguje tak, jak má.

.. viz též:
   - „Příklad: jednoduchá služba <{GITHUB_PATH}/addons/web/static/src/core/network/http_service.js>“
   - Příklad: služba s vazbou
<{GITHUB_PATH}/addons/web/static/src/core/user_service.js>

6. Zobrazit graf v podobě koláče
======================

Každý má rád grafy (nebo alespoň většina z nás) takže přidáme do našeho panelu také koláčový graf, který bude ukazovat
poměr prodaných triček pro každou velikost: S/M/L/XL/XXL.

Pro tuto ukázku použijeme knihovnu grafů „Chart.js <https://www.chartjs.org/>“ . Je to knihovna, která se používá
Graficky. Výchozí ale není načtený, takže buď jej přidáme do
balíček aktiv nebo jej načítat pomalu. Pomalé načítání je obvykle lepší, protože uživatelé nemusí stahovat
Kód pro grafy jsme přidali pouze tehdy, když byl potřeba.

#Vytvořte komponentu „PieChart“.
#V metodě onWillStart nahrávejte do svého projektu knihovnu Chart.js a můžete použít příkaz loadJs
<https://github.com/odoo/odoo/blob/1f4e583ba20a01f4c44b0a4ada42c4d3bb074273/
addons/web/static/src/core/assets.js#L23>funkci pro načítání
:soubor: `/web/statické/lib/Chart/Chart.js`.
#Vložte komponentu PieChart do DashboardItem, abyste zobrazili graf sloupce.
<https://www.chartjs.org/docs/2.8.0/charts/doughnut.html>_, který ukazuje
počet prodaných triček v každé velikosti (tato informace je k dispozici na
(příkaz /statistiky) a můžete použít vlastnost velikosti, aby se zobrazilo více informací.
#Komponenta „PieChart“ bude potřebovat kreslit na plátno pomocí knihovny „chart.js“.
#Dokážete to!

.. obrázek:: 02_vytvořit_dashboard/koláčový_diagram.png
:align:center
:skalka: 80 %

.. viz též:
   - Příklad: načítání souboru js při načtení stránky

addons/web/static/src/views/graph/graph_renderer.js#L57>
   - Příklad: zobrazení grafu v komponentě

addons/web/static/src/views/graph/graph_renderer.js#L618>

7. Aktualizace ze života
===================

Od té doby, co jsme přesunuli načítání dat do mezipaměti, se nikdy neaktualizuje. Ale řekněme, že
hledí na rychle se pohybující data, takže chceme obnovit (například každých 10 minut).
čerstvá data.

Toto je poměrně jednoduché zrealizovat s funkcí setTimeout nebo setInterval v statistickém systému.
Ale tady je ten záludný bod: pokud se právě zobrazuje panel nástrojů, měl by být
aktualizovány ihned.

K tomu lze použít objekt „reaktivní“: je stejný jako objekt vrácený funkcí useState.
Ale není propojena s žádným komponentem. Komponenta pak může provést „useState“ na něm, aby se přihlásila k jeho
změny.


#Aktualizujte službu statistik tak, aby se načítaly data každých 10 minut (k ověření použijte místo toho 10s!).
#Změňte ho tak, aby vracel objekt reaktivní <{OWL_PATH}/doc/reference/reactivity.md#reactive>“.
Při načítání dat by se měl aktualizovat reaktivní objekt přímo v místě.
#Komponenta „Přístrojová deska“ nyní může používat tento stav pomocí příkazu „useState“.

.. viz též:
  - `Dokumentace o reaktivitě <{OWL_PATH}/doc/reference/reactivity.md>`
  - Příklad: Použití reaktivního v rámci služby

addons/web/static/src/core/debug/profiling/profiling_service.js#L30>

8. Náhledová zobrazení stránky
=============================

Představme si, že nám na palubní desce vzniká poměrně velký a zajímavý graf.
uživatelů. V takovém případě by mohlo smysl dávat načítání panelu až po zadání
související aktiva, takže platíme pouze náklady na nahraní kódu tehdy, když ho skutečně chceme
Podívejte se na něj.

Jedním ze způsobů, jak toho dosáhnout, je použít „LazyComponent“ (z balíčku @web/core/assets) jako prostředníka.
která načte aktivační balíček před zobrazením našeho komponentu.

Příklad:

:file:`example_action.js`:

... kódový blok::javascript

exportní třída ExampleComponentLoader pro rozhraní Component
statické komponenty = { LazyComponent };
statická šablona = XML
<LazyComponent bundle="'example_module.example_assets'" Component="'ExampleComponent'" />
          `;
      }

registry.kategorii(„akce“).přidat („example_module.example_action“, „ExampleComponentLoader“);

#Přesuňte všechny aktiva panelu do podsložky:file:`/dashboard`, abyste usnadnili
přidat do balíčku.
#Vytvořte balíček aktiv „awesome_dashboard.dashboard“, který obsahuje všechny prvky
adresář /dashboard/.
#Upravte soubor dashboard.js tak, aby se zaregistroval do registru lazy_components místo akcí.
#V souboru `src/dashboard_action.js` vytvořte prostřední komponentu, která používá `LazyComponent` a
zaregistrovat ho do registru akcí.

9. Vytvoření našeho panelu s obecnými funkcemi
===============================

Dosud máme hezký pracovní panel. Ale je momentálně pevně zakódovaný v panelu
šablonu. Co když chceme přizpůsobit naše rozhraní? Možná někteří uživatelé mají jiné
potřebují a chtějí vidět jiná data.

Dalším krokem je tedy udělat naše rozhraní obecným: místo pevně zakódovaného obsahu
V šabloně může pouze procházet seznamem položek panelu. Ale pak je mnoho
Vynořují se otázky: jak zobrazit položku na panelu, jak ji registrovat, co jsou
a tak dále. Existuje mnoho různých způsobů, jak takový systém navrhnout.
s různými obchody.

Pro tento návod budeme říkat, že položka panelu je objekt s následující strukturou:

... kódový blok::js

const item = {
id: „průměrná hodnota“,
popis: „Průměrná cena trička“,
Komponenta: Standardní položka
      // size and props are optionals
velikost: 3
props: (data) => ({
název: „Průměrná cena trička na objednávku za měsíc“
hodnota: data.průměrná_kvalita
      }),
   };

Hodnota „popis“ bude později užitečná při ukázání názvu položek, které
Uživatel může přidat na svou plochu. Číslo „velikost“ je nepovinné a jednoduše popisuje
velikost položky na panelu, která se zobrazí. Nakonec funkce „props“ je nepovinná.
Pokud nebude definována, jednoduše ji předáme jako datový objekt. Pokud je ale definovaná,
sloužit k výpočtu konkrétních vlastností komponenty.

Cílem je nahradit obsah panelu následujícím kódem:

... blok kódu::xml

<t t-foreach="items" t-as="item" t-key="item.id">
<DashboardItem velikost="item.velikost || 1">
<t t-set="itemProp" t-value="item.props ? item.props(statistiky) : {'data': statistiky}"/>
<t t-component="item.Component" t-props="itemProp" />
</DashboardItem>


Pozor, výše uvedený příklad obsahuje dvě pokročilé funkce Owl: dynamické komponenty a dynamická data.

Momentálně máme dvě druhy komponent: karty s číslem a názvem a koláčové karty.
Nějaký štítek a graf.

#Vytvořte a implementujte dva komponenty: NumberCard a PieChartCard, s odpovídajícími vlastnostmi.
#Vytvořte soubor dashboard_items.js, ve kterém definujete a exportujete seznam položek pomocí NumberCard
a „PieChartCard“ pro znovu vytvoření našeho současného panelu.
#.Importujte seznam položek do našeho komponentu „Dashboard“, přidejte ho k němu a aktualizujte šablonu
použít tzv. „t-foreach“ jako je uvedeno výše.

... kódový blok::js

setup() {
tento.itemy = položky;
         }

A nyní je náš šablona přehledu univerzální!

10. Dodání rozhraní pro přizpůsobení
===================================

Obsah našeho seznamu položek je však stále pevně zakódovaný. Pojďme si tento problém vyřešit pomocí registru:

#. Namísto exportu seznamu zaregistrujte všechny prvky panelu v registru „awesome_dashboard“.
#.Importujte všechny položky registru „awesome_dashboard“ do komponenty „Dashboard“.

Dashboard je nyní snadno rozšiřitelný. Každé další doplněk Odoo, který chce zaregistrovat novou položku na
Dashboard může jen přidat do registru.

11. Přidávat a odstraňovat položky na panelu
==================================

Podívejme se, jak můžeme udělat naše rozhraní přizpůsobitelné. Pro jednoduchost si uložíme uživatele
konfiguraci panelu v místní paměti, aby byla trvalá, ale nemusíme se o ni starat.
s serverem prozatím.

Konfigurace palubní desky bude uložena jako seznam odstraněných položek s identifikátory.

#Přidejte tlačítko v ovládacím panelu s ikonou ozubeného kola, aby bylo jasné, že se jedná o tlačítko pro nastavení.
#Kliknutím na tlačítko by se měl otevřít dialog.
#V tomto dialogu chceme vidět seznam všech existujících prvků panelu, každý s vlastním zaškrtávacím políčkem.
#V zápatí by mělo být tlačítko „Použít“. Po jeho kliknutí se vytvoří seznam všech identifikátorů položek.
to nebylo zkontrolováno.
#Chceme uložit tuto hodnotu do lokálního úložiště.
#A upravit komponentu „Plocha“ tak, aby filtrovala aktuální položky odstraněním identifikátorů položek.
z konfigurace.

.. obrázek: 02_vytvořit_přístupovou_stránku/konfigurace_položek.png
:šířka: 80 %
:align:center

12. Pokračování
=================

Níže je uveden seznam několika drobných vylepšení, které můžete zkusit udělat, pokud máte čas:

#Ujistěte se, že aplikace může být „přeložena“ (s
`env._t`.
#Kliknutím na část grafu by se měl zobrazit pohled na všechny objednávky, které mají
odpovídající velikosti.
#Uložte obsah panelu uživatele na server v nastavení uživatele!
#Učiněte ji reagující: v mobilním režimu by každá karta měla zabírat 100 % šířky.

.. viz též:
   - Příklad: použití funkce env._t

addons/account/static/src/components/bills_upload/bills_upload.js#L116>
   - Kód: překladový kód v webu

addons/web/static/src/core/l10n/translation.js#L22>
