===============================
Účinnost celkového vybavení
===============================

.. |MO| nahradit za: zkratka: `MO (manufacturing order)`
.. |OEE| nahradit za: zkratku `OEE (overall equipment effectiveness)`
.. |BoM| nahradit za: :abbr:`BoM (Seznam materiálů pro výrobu)“

V aplikaci Manufacturing v Odoo je „overall equipment effectiveness“ (OEE) reprezentováno množstvím času
Výrobní centrum je plně produktivní. Hodnota OEE se zobrazuje jako procento celkového času, který pracovník stráví na výrobním centru.
centrum je aktivní.

Plně produktivní čas je považován za dobu, kdy je pracoviště v provozu **a**
pracovat s pracovními příkazy, které nevyčerpaly svou *očekávanou dobu trvání*.

|OEE| pomáhá výrobním týmům porozumět efektivitě pracovišť a příčinám
zastavení výroby.

.. důležité::
Protože OEE sleduje produktivitu pracoviště, musí být zapnutá funkce pracovišť.
v nastavení aplikace Manufacturing.

Pro toto nastavení přejděte na: „Výroba -> Konfigurace -> Nastavení“ a zaškrtněte
zaškrtávací políčko vedle :guilabel:`Dodacích objednávek“, pod nadpisem :guilabel:`Provoz“. Pak
klikněte na tlačítko „Uložit“.

Účinnost standardů
====================

Pro přesné zobrazení procenta plně produktivního času na pracovišti je nutné
centrum musí být správně nakonfigurováno s odpovídajícími produktivními ukazateli, včetně práce
*účinnosti času*, *kapacitě* a *cíli OEE*.

Úspora času
---------------

Časová efektivita představuje efektivitu pracovního centra při zpracování objednávek.
v procentech. Hodnota časové efektivity 100 % znamená, že pracovní centrum
Proces zpracovává objednávky v rychlosti očekávané doby trvání, jak je uvedeno na BoM produktu. Hodnota
menší než nebo větší než 100 % znamená, že pracoviště zpracovává objednávky na práci pomaleji nebo rychleji
než je očekávaná doba operace, tj.

Pro nastavení účinnosti práce na pracovišti přejděte do:
Konfigurace --> Střediska, vyberte středisko. V poli :guilabel:`Obecné informace
v poli „Účinnost času“ zadejte číselnou hodnotu.

Příklad:
Výroba produktu „židle“ vyžaduje dvě operace: „řez“ a „sestavení“.
|BoM| uvádí očekávanou dobu trvání každé operace v délce 30 minut.

Operace řezání se provádí na pracovišti centra účinnosti *řezací stanice*, které má vysokou
hodnota 50 %. To znamená, že doba trvání operace je dvojnásobná, celkem tedy
hodinu.

Sestavovací operace se provádí na pracovišti montážní linky, kde je stanoven čas
účinností 200 %. To znamená, že doba trvání operace se snížila na polovinu.
15 minut.

Kapacita
--------

Kapacita představuje, kolik jednotek výrobku lze vyrábět současně na pracovišti.
Doba trvání pracovních úkolů pro více jednotek se zvyšuje nebo snižuje v závislosti na tom, kolik jednotek je zapotřebí k práci.
centrum zvládne.

Pro nastavení kapacity pracovního centra přejděte na:
Konfigurace --> Střediska, vyberte středisko. V poli :guilabel:`Obecné informace
tabulku, zadejte číselnou hodnotu do pole „Kapacita“.

Příklad:
Strojová stanice typu *vrtací* má kapacitu jednoho kusu. Pro 10 kusů je potvrzena |MO|
*křeslo*, produkt vyrobený pomocí vrtací stanice.

Protože je desetkrát více jednotek k výrobě než kolik může pracovní středisko zpracovat najednou,
Provozní doba je desetkrát delší než uvedená doba na produktu.

cílový index efektivnosti
------------

Cílem je, aby se využilo co nejvíce času pracovního centra.
produktivní čas. Zobrazuje se jako procento a měl by být nastaven pouze na „100 %“.

Pro stanovení cíle OEE pro pracovní centrum přejděte na:
Konfigurace --> Nastavení --> Střediska práce, vyberte středisko. V poli :guilabel:`Obecné
V poli „Informace“ zadejte číselnou hodnotu menší než 100,00 v poli „Cílová OEE“.

Výpočet OEE
=================

Hodnota OEE je vyjádřena jako procentní hodnota mezi nulou a 100 %. Hodnota znázorňuje množství
čas, kdy je pracoviště plně produktivní. Zbývající čas znamená množství času, kdy
centrum práce nebylo v plném provozu. To se může stát z mnoha důvodů.
včetně *snížené rychlosti*, *dostupnosti materiálu* a *poruchy zařízení*.

Plně produktivní čas
---------------------

Pro pracoviště je plně produktivní, pokud dokáže přijímat zakázky, mít
komponenty potřebné k zpracování objednávek a fungovat v očekávaném časovém rozmezí
objednávku, kterou zpracovává.

Příklad:
Ve výrobním středisku sestavení není blokována a dostává se mu objednávka na sestavení kola.
K dispozici jsou potřebné součástky, takže výroba začne hned po tom, co budou vybrány.
dodán do pracovního centra. Práce má očekávanou délku 30 minut a je
Dokončeno za 27 minut. Všechny tyto hodiny jsou považovány za plně produktivní.

Snížená rychlost
-------------

Když pracovní centrum funguje v omezeném režimu, znamená to, že zpracovává objednávku práce.
překročila svou očekávanou délku. I když pracoviště může být v provozu, není to považováno za
plně produktivní čas.

Příklad:
Stanice pro řezání obdrží příkaz k vyřezání desek na stůl. Očekávaný
Délka pracovního úkolu je 15 minut. Celkově trvá dokončení pracovního úkolu 18 minut.
Ředitelství práce je považováno za provozující se v omezeném režimu během tří minut.
která přesáhla očekávanou dobu trvání.

Dostupnost materiálu
---------------------

Dostupnost materiálu se týká situací, kdy je pracoviště schopno přijmout objednávku na práci, ale
Nezbytné součástky nejsou k dispozici. To může nastat z důvodu, že součástky nemají skladem.
nebo jsou vyhrazeny pro jiný řád.

Příklad:
Výroba lavičky vyžaduje 20 kusů dřeva. Potvrzení výrobního příkazu (MO)
za deset kusů lavic, ale kvůli nedostatku dřeva se výroba nezahájí.
Výrobní čas, který je potřeba na získání dřeva, se započítává jako doba nedostupnosti materiálu.

Závada zařízení
-----------------

Závada na zařízení znamená jakýkoliv časový úsek, kdy pracovní centrum není použitelné kvůli údržbě.
problémy s vybavením. Tyto problémy mohou být způsobeny poruchami nebo uzavřením pracovního centra
pro plánovanou údržbu. V těchto případech lze pracovní centrum zablokovat pomocí
:doc:`žádost o údržbu <../../maintenance/maintenance_requests>“.

Příklad:
Ve výrobním centru se zasekne vrták na *vrtací stanici*, což způsobí, že pracoviště bude nefunkční.
Vytvoří se požadavek na údržbu k opravě vrtačky a pracoviště bude blokováno pro přijímání dalších objednávek.
objednávky. Oprava vrtačky a znovu zprovoznění pracoviště trvá dvě hodiny.
Doba trvání dvou hodin je zaznamenána jako doba výpadku zařízení.

Reportování o výkonnosti strojů
===============

Pro zobrazení metrik výrobního procesu pro každé pracoviště klikněte na: menu „Aplikace pro výrobu
--> Zprávy o výrobě --> Celkový účinnostní index. Tato stránka zobrazuje metriky pro každé pracoviště
s daty o efektivitě výroby.

Alternativně můžete zobrazit metriky pro jednotlivé pracoviště v
Vyberte položku „Výrobní aplikace“ -> „Konfigurace“ -> „Střediska“, vyberte středisko.
klikněte na tlačítko „Chytrý“ s ikonou „Pie chart“ a zaškrtněte políčko „OEE“.

Výchozí stránka s hlavním přehledem ukazuje data v grafu sloupcovém, zatímco stránka pro konkrétní
V pracovním centru se zobrazuje v grafu sloupcovém. Pro výběr jiného typu grafu na buď stránce klikněte
:icon:`fa-bar-chart` :guilabel:`(bar chart)`, :icon:`fa-line-chart` :guilabel:`(line chart)` nebo
Tlačítko „Pie Chart“ nad zobrazeným grafem.

Data OEE lze také zobrazit v přehledu sloupců nebo seznamu s každým záznamem.
kliknutím na ikonu :icon:`oi-view-pivot` nebo :icon:`oi-view-list`
tlačítka „Zobrazit“ v pravém horním rohu stránky.

.. obrázek: oee/oee-report.png
:align:center
:alt:Dashboard zprávy o OEE.
