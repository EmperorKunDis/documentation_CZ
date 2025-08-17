===============================
Kapitola 1: Vytvořte hru Clicker
===============================

Pro tento projekt spolu vytvoříme „klikací hru“ (viz https://cs.wikipedia.org/wiki/Inkrementální_hra).
integrované s Odoo. Cílem hry je získat co nejvíce kliknutí.
automatizovat systém. Zajímavá část je, že budeme používat uživatelské rozhraní Odoo jako naši hřiště.
Například některé bonusy schováme v náhodných částech webového klienta.

Abychom se mohli pustit do práce, potřebujeme běžící server Odoo a vývojové prostředí.
Do cvičení se ujistěte, že jste všechny kroky popsané v této
:ref:`Úvodní příručka <tutorials/master_odoo_web_framework/setup>“.

.. varování: Cíl

.... obrázek: 01_build_clicker_game/final.png
:synchronizace: střed

..spoiler:: Řešení

Řešení každé úlohy kapitoly jsou uveřejněna na
„oficiální repozitář návodů k použití Odoo
<https://github.com/odoo/tutorials/commits/{CURRENT_MAJOR_BRANCH}-master-odoo-web-framework-solutions/awesome_clicker>.


1. Vytvořte položku v systémovém tray
========================

Chceme začít zobrazovat počítadlo v systémovém tlačítku.

#Vytvořte soubor „clicker_systray_item.js“ (a „xml“) s komponentou „Hello World“ pro Owla.
#Zaregistrujte ji do registru systému a ujistěte se, že je viditelná.
#Aktualizujte obsah položky tak, aby zobrazoval následující řetězec: „Počet kliknutí: 0“.
Přidejte tlačítko na pravé straně, které zvýší hodnotu.

.. obrázek: 01_build_clicker_game/systray.png
:align:center

A hle, máme úplně funkční klikací hru.

.. viz též:

   - :ref:`Dokumentace k registru systray <frontend/registries/systray>
   - Příklad: přidání položky systému do registru
<https://github.com/odoo/odoo/blob/c4fb9c92d7826ddbc183d38b867ca4446b2fb709/addons/web/static/src/webclient/user_menu/user_menu.js#L41-L42>

2. Počítat externí kliknutí
========================

No, aby se nám to nezdálo, že ještě moc zábavy to není. Takže přidáme novou vlastnost: chceme všechny kliknutí
uživatelské rozhraní počítá, takže uživatel má motivaci používat Odoo co nejvíce! Ale samozřejmě
Záměrné kliknutí na hlavní počítadlo by mělo být stále více.

#Použijte funkci useExternalListener k poslechu všech kliknutí na dokument.body.
#Každý z těchto kliknutí by měl zvýšit hodnotu kontrolky o jedna.
#Změnit kód tak, aby každý klik na čítač zvýšil hodnotu o 10
#Ujistěte se, že kliknutím na čítač nezvýšíte hodnotu o 11!
#Další výzva: zajistit, aby externí posluchač zachytil události, abychom se nemuseli
Nebude vám chybět ani jedno kliknutí.

.. viz též:

   - Dokumentace k používání externího posluchače v Owlu <https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#useexternallistener>
   - „Stránka MDN o zachycení události <https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#event_capture>“


3. Vytvořte akci klienta
=========================

Současná uživatelská rozhraní je poměrně malé: jedná se pouze o položku v systémovém trayi. Jistě potřebujeme
více prostoru pro zobrazení více našich her. Proto vytvořme akci klienta. Akce klienta
je hlavní akcí spravovanou webovým klientem, která zobrazuje komponentu.

#Vytvořte soubor „client_action.js“ (a „xml“) s komponentou „Hello World“.
#Zaregistrujte tuto akci klienta v registru akcí pod názvem „awesome_clicker.client_action“.
#Přidejte tlačítko do systémové lišty s textem „Otevřít“. Když na něj kliknete, mělo by se otevřít
akci klienta „awesome_clicker.client_action“ (použijte službu akce, aby jste to udělali).
#Abychom nezpůsobili zaměstnancům rušení práce, dáváme přednost akci klienta otevřít v okně přesvědčování.
Spíš než v plném režimu, otevřete ji pomocí metody doAction.

......tip:

Můžete použít „target: 'new'“ v metodě doAction k otevření akce v okně přesunu:

... kódový blok::js

         {
typ: „ir.actions.client“,
značka: „Awesome Clicker - akce klienta“,
cíl: „nový“,
jméno: „Klikr“
         }

.. obrázek: 01_build_clicker_game/client_action.png
:align:center

.. viz též:

   - :ref:`Jak vytvořit klientskou akci <jakto/javascript_client_action>`

4. Stát převést na službu
==============================

Naše klientská akce je zatím jen „hello world“ komponenta. Chceme ji použít k zobrazení stavu hry, ale
Tato funkce je v současné době dostupná pouze ve složce Systray. To znamená, že musíme změnit
umístění našeho státu, aby byl dostupný pro všechny jeho složky. To je ideální případ použití služeb.

#Vytvořte soubor „clicker_service.js“ s odpovídajícím službami.
#Tato služba by měla exportovat reaktivní hodnotu (počet kliknutí) a několik funkcí pro její aktualizaci:

... kódový blok::js

const state = reaktivní objekt s vlastnostmi kliknutí:
         ...
return {
stát
increment(inc) {
stát.kliky += inc
            }
         };

#Přistupujte k stavu v položce systému i v akci klienta (nezapomeňte použít stav).
položku systému Windows pro odstranění vlastního lokálního stavu a použití jejich. Dále můžete odstranit tlačítko „+10 kliknutí“.
#Zobrazte stav v akci klienta a přidejte tlačítko „+ 10“ do ní.

.. obrázek: 01_build_clicker_game/increment_button.png
:align:center

.. viz též:

   - :ref:`Stručný popis služeb <návody/objevte-js-framework/služby>`

5. Použijte vlastní háček
====================

Teď je každá část kódu, která bude potřebovat naše služby, nucena do svého zdrojového kódu zahrnout příkaz
„useState“. Protože je poměrně častá, použijme si vlastní funkci. Je také užitečné více zdůraznit
„klikání“ a méně důrazu na „službu“.

#Exportujte funkci „useClicker“ jako háček.
#Aktualizujte všechny aktuální použití služby kliknutím na nový háček:

... kódový blok::js

tento.klikací zařízení = použít klikací zařízení();

.. viz též:

   - „Dokumentace o háčcích: <https://github.com/odoo/owl/blob/master/doc/reference/hooks.md>“

6. Zobrazenou hodnotu lidštěte
===============================

V budoucnu budeme zobrazovat velké číslo, takže se na to připravme. Existuje funkce „humanNumber“, která
formátovat čísla tak, aby byly snadněji pochopitelné: například číslo 1234 by mohlo být formátováno jako 1.2k

#. Použijte ho k zobrazení našich počítadel (v položce systému a v akci klienta).
#Vytvořte komponentu ClickValue, která zobrazí hodnotu.

....... poznámka::

Orel umožňuje komponentu, která obsahuje jen textové uzly!

.. obrázek: 01_build_clicker_game/humanized_number.png
:align:center

.. viz též:

   - „definice funkce počtu lidí <https://github.com/odoo/odoo/blob/c638913df191dfcc5547f90b8b899e7738c386f1/addons/web/static/src/core/utils/numbers.js#L119>“

7. Přidejte nástrojovou lištu v komponentě ClickValue
==========================================

S funkcí „humanNumber“ jsme ve skutečnosti přišli o nějakou přesnost na našem rozhraní. Podívejme se na reálné číslo
jako nápovědu.

#Nástrojová lišta potřebuje HTML prvek. Změňte hodnotu ClickValue na vložení hodnoty do tagu <span/>
#Přidejte dynamický atribut „data-tooltip“, abyste zobrazili přesný výsledek.

.. obrázek: 01_build_clicker_game/humanized_tooltip.png
:align:center

.. viz též:

   - „Dokumentace v nástrojové liště <https://github.com/odoo/odoo/blob/c638913df191dfcc5547f90b8b899e7738c386f1/addons/web/static/src/core/tooltip/tooltip_service.js#L17>“

8. Kupte si ClickBoty
================

Abychom hru ještě více zatraktivnili, pokud se hráč poprvé dostal na 1000 kliknutí,
Otevře novou funkci: hráč si může koupit roboty za 1000 kliknutí. Tyto roboti vygenerují 10 kliků.
každých deset sekund.

#Přidejte do stavu číslo úrovně. To je číslo, které se bude zvyšovat při dosažení některých milníků.
otevřít nové funkce
#Přidejte do stavu číslo clickBots, které představuje počet robotů zakoupených v daném měsíci.
#. Upravte akci klienta, aby zobrazila počet kliknutí botů (pouze pokud je „level“ větší nebo roven 1), s tlačítkem „Koupit“.
tlačítko, které je aktivní, pokud „kliknutí“ je větší než 1000. Tlačítko „Koupit“ by mělo počet kliků zvýšit o jedna.
#Nastavte intervál služby na 10 sekund, který bude každých 10 sekund zvyšovat počet kliknutí o hodnotu clickBots.
#Ujistěte se, že tlačítko Koupit je deaktivováno, pokud hráč nemá dostatek kliknutí.

.. obrázek: 01_build_clicker_game/clickbot.png
:align:center

9. Refaktorovat na třídový model
============================

Současný kód je napsán trochu funkcionálně. Ale abychom tak mohli učinit, musíme vyexportovat stav a všechny jeho
aktualizovat funkce v našem objektu kliknutí. Jak se projekt rozrůstá, může to být stále složitější.
jednodušší je oddělit naši logiku od služby do třídy.

#Vytvořte soubor „clicker_model“, který exportuje reaktivní třídu. Přesuňte všechny funkce stavu a aktualizace do
službu do modelu.

......tip:

Můžete třídu ClickerModel rozšířit o třídu Reactive.
:soubor:`@web/core/utils/reactive`. Třída Reactive zabalí model do reaktivního proxy.

#Změňte službu klikání tak, aby instancovala a exportovala třídu modelu klikání.

.. viz též:

   - „Příklad podtřídy Reactive <https://github.com/odoo/odoo/blob/c638913df191dfcc5547f90b8b899e7738c386f1/addons/web/static/src/model/relational_model/datapoint.js#L32>“

10. Informovat, když je dosažen určitý cíl
======================================

Nemáme mnoho zpětné vazby, že by se něco změnilo, když jsme dosáhli 1000 kliknutí. Použijme tedy službu „efekt“
dát tuto informaci jasně najevo. Problém je v tom, že náš klikací model nemá přístup ke službám.
Dále chceme udržet co nejvíce UI záležitost mimo model. Takže můžeme zkoumat nové strategie
pro komunikaci: autobusy pro přepravu osob.

#Aktualizujte model kliku na instanci autobusu a spustit událost „MILESTONE_1k“ při dosažení 1000 kliknutí.
poprvé.
#Změňte službu kliknutí na poslech stejné události v modelovém autobusu.
#Pokud se tak stane, použijte službu „efekt“ k zobrazení duhy muže.
#Přidejte nějaký text, který vysvětluje, že uživatel může nyní kupovat clickbots.

.. obrázek: 01_build_clicker_game/milestone.png
:align:center

.. viz též:

   - Dokumentace k „sovím“ událostem na „busu událostí“ <https://github.com/odoo/owl/blob/master/doc/reference/utils.md#eventbus>
   - :ref:`Dokumentace k efektu služby <frontend/services/effect>`

11. Přidejte BigBoty
===============

Jasně, potřebujeme způsob, jak dát hráčům více možností. Pojďme přidat nový typ klikacího robota: „BigBoty“.
Ty jsou prostě silnější: poskytují každých 10 sekund 10s, ale stojí 5000 kliknutí.

#Zvýšit úroveň na 2, když dosáhne hodnoty 5000.
#Aktualizujte stát, abyste mohli sledovat velké boty
#Velké roboty by měly být dostupné na úrovni „>= 2“
#Zobrazte odpovídající informace v akci klienta.

..tip:

Pokud potřebujete v šabloně použít tagy „<“ nebo „>“, buďte obezřetní, protože mohou být chápány jako JavaScriptové výrazy.
XML parser. Chcete-li tento problém vyřešit, můžete použít jeden z speciálních aliasů: „gt“, „gte“, „lt“ nebo „lte“. Podrobnější informace najdete v
`Stránka dokumentace Owl o výrazech šablon <https://github.com/odoo/owl/blob/master/doc/reference/templates.md#expression-evaluation>.

... obrázek: 01_build_clicker_game/bigbot.png
:align:center

12. Přidejte nový zdroj: sílu
=====================================

Nyní přidáme další bod měření - nový typ zdroje: mocnářské násobitelé. To je číslo
který lze zvýšit na hodnotu „>= 3“ a násobí akci botů (takže místo toho, aby poskytoval
Kliknutí, klikboti nyní poskytují „množičské“ kliknutí.

#. zvyšovat úroveň, když dosáhne hodnoty 100k (takže by měla být 3).
#Aktualizovat stav, abychom mohli sledovat energii (výchozí hodnota je 1).
#změnit boty tak, aby používali tento počet jako násobek.
#Aktualizovat uživatelské rozhraní, aby zobrazovalo a umožňovalo koupit novou úroveň výkonu (náklady: 50k).

... obrázek: 01_build_clicker_game/bigbot.png
:align:center

13. Definujte nějaké náhodné odměny
==============================

Chceme, aby uživatel občas získal bonusy a odměňoval je pomocí Odoo.

#Definujte seznam odměn v souboru click_rewards.js. Odměna je objekt s:
   - Popisová řetězcová hodnota.
   - funkci „aplikovat“, která přijímá stav hry jako argument a může jej měnit.
   - číslo „minLevel“ (volitelné), které popisuje, na jakém úrovni odemknutí je bonus k dispozici.
   - Číslo „maxLevel“ (volitelné), které popisuje úroveň odemknutí, při níž se bonus již nezobrazuje.

Příklad:

... kódový blok::js

exportní konstantou jsou odměny, které jsou [
         {
popis: „Získat klikacího robota“,
apply(klikr) {
clicker.zvýšit(1);
            },
maxLevel: 3,
         },
         {
popis: „Získejte 10 kliknutí robotem“,
apply(klikr) {
clicker.zvýšit(10);
            },
minLevel: 3
maxLevel: 4,
         },
         {
popis: „Zvýšit sílu robota!“,
apply(klikr) {
clicker.multiclicks += 1;
            },
minLevel: 3
         },
      ];

Můžete přidat cokoliv, co chcete!

#Definujte funkci getReward, která vybere náhodný odměnu z seznamu odměn, které odpovídají
aktuální úroveň odemknutí.
#Vyjměte kód, který vybírá náhodně z pole v funkci „vybrat“, kterou můžete přesunout do jiného souboru utils.js.

14. Nastavte odměnu při otevření formuláře
=============================================

#Opravte formulářový kontroler. Každý formulářový kontroler by měl při vytváření náhodně rozhodnout (s 1 % pravděpodobností).
pokud by měl být udělen odměna.
#Pokud je odpověď ano, zavolejte metodu getReward na modelu.
#Tento způsob by měl vybrat odměnu, poslat oznámení s tlačítkem „Vyzvednout“, které bude
Pak se odměna aplikuje a nakonec by měl otevřít klientskou akci „klikání“.

.. obrázek: 01_build_clicker_game/reward.png
:align:center

.. viz též:

   - :ref:`Dokumentace o opravě třídy <frontend/patching_class>`
   - „Definice funkce patch <https://github.com/odoo/odoo/blob/c638913df191dfcc5547f90b8b899e7738c386f1/addons/web/static/src/core/utils/patch.js#L71>“
   - „Příklad opravy třídy <https://github.com/odoo/odoo/blob/c638913df191dfcc5547f90b8b899e7738c386f1/addons/pos_mercury/static/src/app/screens/receipt_screen/receipt_screen.js#L6>“

15. Přidejte příkazy do nabídky příkazů
===================================

#Přidejte příkaz „Otevřít hru Clicker“ do nabídky příkazů.
#Přidejte další příkaz: „Koupit klikacího robota“.

.. obrázek: 01_build_clicker_game/command_palette.png
:align:center

.. viz též:

   - „Příklad použití registru poskytovatelů příkazů <https://github.com/odoo/odoo/blob/c638913df191dfcc5547f90b8b899e7738c386f1/addons/web/static/src/core/debug/debug_providers.js#L10>“

16. Přidejte další zdroj: stromy
===================================

Je čas představit úplně nový typ zdrojů. Tady je jeden, který by neměl být příliš kontroverzní: stromy.
Nyní umožníme uživatelům vysazovat (sklízet?) ovocné stromy. Strom vyjde na 1 milion kliknutí, ale bude nám poskytovat
jablka nebo třešně.

#Aktualizujte stát na sledování různých druhů stromů (jabloně, třešně) a jejich plodů.
#Přidejte funkci, která vypočítá celkový počet stromů a plodů.
#Definujte nový stupeň odemčení na „kliknutí >= 1 000 000“.
#Aktualizovat uživatelské rozhraní klienta tak, aby zobrazoval počet stromů a plodin a také umožňoval jejich nákup.
#Zvyšte počet plodů o jedno každých 30 sekund pro každý strom.

.. obrázek: 01_build_clicker_game/trees.png
:align:center

17. Využijte rozbalovací nabídku pro položku systému
============================================

Hra se začíná zlepšovat. V systémovém trayi ale zatím vidíme jen celkový počet kliknutí.
chceme vidět více informací: celkový počet stromů a plodin. Dále by bylo užitečné mít rychlý
přístup k některým příkazům a další informace. Použijme rozbalovací nabídku!

#Zástupce v systémovém tácu nahraďte rozbalovacím seznamem.
#Měl by zobrazovat počty kliknutí, stromů a plodin s pěknými ikonami.
#Kliknutím na něj by se měl otevřít rolovací seznam, který zobrazí podrobnější informace: každý druh stromů
a ovoce.
#Dále několik položek s některými příkazy: otevřít hru na kliknutí, koupit clickera, ...

... obrázek: 01_build_clicker_game/dropdown.png
:align:center

18. Použijte komponentu Notebook
============================

Nyní sledujeme mnohem více informací. Pojďme zlepšit uživatelské rozhraní tím, že budeme organizovat informace
a objevuje se v různých záložkách s komponentou „Notebook“:

#Použijte komponentu Notebook.
#Všechny „klikací“ prvky by měly být zobrazeny v jednom záložce.
#Všechny „stromy/plody“ by měly být zobrazeny v jiném záložce.

.. obrázek: 01_build_clicker_game/notebook.png
:align:center

.. viz též:

   - :ref:`Odoo: Dokumentace k komponentě Notebook <frontend/owl/notebook>`
   - „Sova: Dokumentace o slotu <https://github.com/odoo/owl/blob/master/doc/reference/slots.md>“
   - „Testy součásti notebooku <https://github.com/odoo/odoo/blob/c638913df191dfcc5547f90b8b899e7738c386f1/addons/web/static/tests/core/notebook_tests.js#L27>“

19.  Přetrvávání stavu hry
===========================

Určitě jste si všimli velké chyby v naší hře: je nestabilní. Každou chvíli, kdy uživatel zavře
okno prohlížeče. To opravíme. Použijeme místní úložiště, abychom udrželi stav.

#Importujte „prohlížeč“ z souboru: @web/core/browser/browser, abyste mohli přistupovat k místní paměti.
#Serializovat stav každých 10 sekund (v stejném intervalu kódu) a ukládat jej do místního úložiště.
#Když je spuštěna služba „klikání“, měla by se načíst stav ze místního úložiště (pokud existuje) nebo zahájit inicializaci.
Jinak.

20. Zavést státní migrační systém
====================================

Jakmile nějaký stav existuje někde, objeví se nový problém: co když aktualizujete svůj kód, takže tvar stavu
změnami a uživatel otevře svůj prohlížeč s nastavením, které bylo vytvořeno starou verzí? Vítejte ve světě
migrační otázky!

Je pravděpodobně moudré řešit problém včas. To, co zde uděláme, je přidat číslo verze ke stavu a zavést
systém automatického aktualizování států, pokud není aktuální.

#Přidejte verzi stavu.
#Definujte prázdný seznam migrací. Migrace je objekt s číslem verze „fromVersion“, číslem verze „toVersion“ a funkcí „apply“.
#Každýkrát, když kód načte stav z místního úložiště, by měl ověřit verzi. Pokud je stav nesprávný
Pokud je aktuální, měla by provést všechny potřebné migrace.

21. Přidejte další druh stromů
=============================

Abychom otestovali naši migrační systém, přidáme nový druh stromů: broskvoně.

#Přidejte višňovníky.
#Zvýšit číslo verze státu.
#Definujte migraci.

.. obrázek: 01_build_clicker_game/broskvoně.png
:align:center
