===================
Pokročilé plány telefonních čísel
===================

Obvykle mají firmy každý den velké množství příchozích hovorů, ale mnoho z nich nechce, aby jejich týmy
odpovídat na hovory 24 hodin denně, 7 dní v týdnu.

Použitím pokročilých funkcí plánu volání společnosti AxiVo lze proces automatizovat a nastavit směrování
pro všechny scénáře. Tímto způsobem zákazníci nikdy nečekají nebo se nenudí, protože nemohou
se nikým nekontaktovat.

Použitím pokročilých prvků v telefonních plánech mohou společnosti automatizovat směrování hovorů pro určité
dny nebo časy, jako jsou například firemní svátky. Firmy mohou také umožnit volajícím zadat přípony
a přeposílají se automaticky pomocí digitální recepce. Tímto způsobem je
Administrativní tým nemusí být k dispozici nepřetržitě.

Je zde možnost směrovat hovory podle toho, odkud jsou volající na světě.
Takže maximalizují efektivitu.

.. důležité:
Více informací o základních telefonních plánech a jak je doplnit najdete na :doc:`dial_plan_basics`.

.. varování:
Používání doplňku pro kontrolu pravopisu v prohlížeči může bránit použití vizuálního editoru v plánech volání.
nepoužívat překladač s konzolí pro správu Axivox.

Pokročilé prvky
=================

V plánech Axivox (jak je popsáno v :doc:`dial_plan_basics`) jsou dvě pokročilé funkce, které
Může být použita.

- :guilabel:`Záznam‘: funkce záznamu je zapnutá (vyžaduje změnu plánu, zapnuto v Axivox
(Nastavení).
- :guilabel:`Označení volajícího“: nahraďte označení volajícího číslem nebo libovolným textem.

Chcete-li přidat jeden z těchto prvků, přejděte na stránku „Dial plány“, která je v nabídce
levé menu „Konzole pro správu Axivoxu <https://manage.axivox.com>“.

Dále klikněte na tlačítko „Vizuální editor“ vedle požadovaného plánu volání pro jeho úpravy.
Začněte kliknutím na tlačítko „Nový prvek“ v horní liště a poté vyberte požadovaný prvek.
:guilabel:`Přidat“.

.. obrázek: dial_plan_advanced/visual-editor.png
:align:center
:alt:Vizuální editor plánu pro telefonní ústřednu v Axivoxu s prvky přidání a operátora zvýrazněnými.

Pro více informací navštivte:ref:`voip/axivox/dial_plans`.

.. důležité:
Element Record zaznamenává hovory, které prochází touto částí a vyžaduje
další změna v plánu Axivox.

Pro nahrávání na Axivox přejděte do nastavení v Axivox management console.
Pak přejděte na záložku „Nahrávání“ a pod ní najdete možnost „Záznam“.
stránky. Z nabídky vyberte možnost „Aktivní“ a nahrávání začněte
Použitím prvku :guilabel:`Record` v telefonním plánu.

..tip:
Pokud není k dispozici a nelze změnit položka „Nahrávání“ v nabídce, poraďte se s
AxiVox tuto funkci umožňuje.

Element :guilabel:`Zobrazit volajícího“ umožňuje nahradit zobrazení čísla volajícího na úrovni nižší.
routování.

Při přidání prvku :guilabel:`Caller ID` do plánu volání a kliknutí na něj pro konfiguraci
Vyberte si jednu z nich.

První je pole „Volací jméno“ s možností zadání libovolného textu místo čísla volajícího.
Druhou možností je volba „Změnit číslo volajícího na číslo volaného“. Tato volba nahradí
identifikátor volajícího s :guilabel:`Číslo v síti“.

..tip:
Společnost může chtít použít prvek „Zobrazované číslo“ (Caller ID) k nahrazení prvku „Příchozí hovor“ (Incoming
číslo, takže zaměstnanci nebo externí převody nemohou vidět číslo a informace je uchována
soukromé.

Základní prvky routování
======================

Základní prvky routingu v plánech Axivox poskytují směrování na základě rozšíření. To lze provést
Přidat buď hvězdičku Menu*, která spojuje číselné volání s akcí, nebo použít hvězdičku Digital*.
Recepční automaticky směruje nebo poslouchá prodloužení podle klíčového vstupu z
volající.

Hlavní rozdíl mezi těmito prvky spočívá v tom, že digitální recepční **nepotřebuje k práci**
je přednastavena číselně s akcemi. Namísto toho funguje jako virtuální recepční.

- :guilabel:`Nápověda“: přidat telefonní seznam s nastavenými akcemi (ne
terminalu. Například funkce volání na číslo by mohla obsahovat prvek, kde kliknutím na „2“
přesměruje volajícího na prvek spojený s číslem 2 v menu.
- :guilabel:`Digitální recepční“: připojte virtuálního operátora, který bude poslouchat telefonní čísla.

Chcete-li přidat jeden z těchto prvků, přejděte na stránku „Dial plány“, která je v nabídce
levé straně „Konzole pro správu Axivoxu“ <https://manage.axivox.com>. Následně klikněte na
Tlačítko „Editor zobrazení“ vedle plánu volání, abyste mohli upravit plán volání. Poté otevřete
Vyberte nový prvek v seznamu „New element“ a klikněte na „Přidat“.

Pro více informací navštivte:ref:`voip/axivox/dial_plans`.

Scénář digitální recepční
-----------------------------

Prvek *Digitální recepční* je funkcí, která přesně směruje volajícího na určité telefonní číslo.
plánu na základě rozšíření, které zadáte pomocí klávesnice.

Nastavte digitální recepční, abyste nemuseli mít tým nebo živého recepčního na telefonu.
vždy. Díky tomuto prvku se nyní hovory dostanou na cílové číslo, aniž by prošly skutečným operátorem
přerušovat.

Po přidání prvku „Digitální recepční“ do plánu volání je nutné propojit příslušný
koncových bodů a klikněte na prvek dvakrát, abyste nastavili časový limit
Pop-up okno s názvem „Recepční“.

Velikost časového limitu lze nastavit v pětiminutových intervalech od 5 do 60 sekund.

.. důležité:
Element „Digitální recepční“ (Digital Receptionist) **vyžaduje** prvek „Spustit soubor“ (Play a file).
na obou stranách, aby vysvětlily, co má uživatel udělat, a kdy je zadáno špatné prodloužení.

Příklad:
Při přizpůsobení dialplánu v okně „Editor dialplánu“ (viz :guilabel:`Dialplan Editor`) přidejte
:guilabel:`MENU“ prvku s :guilabel:`Pozdravnou zprávou“, která by mohla číst například takto: „Stiskněte hvězdu pro
„zavolejte na příslušnou linku“.

Pak na položce Menu přidáme pro volbu * (hvězdička) odkaz.
:guilabel:`Spustit soubor“ prvek, který přehrává :guilabel:`Audiovzkaz“, který říká „Zadejte
„prodloužení osoby, kterou se snažíte kontaktovat“.

Po prvním prvcích „Spustit soubor“ přidejte „Digitální recepční“.
element, následovaný dalším:guilabel:„Spustit soubor“ elementem, který říká „Toto není platný
rozšíření.

Toto poslední pole slouží k uzavření smyčky, pokud volající nezadá správnou příponu.

Konečně tento poslední prvek „Spustit soubor“ je vrácen zpět do menu.
prvek.

.... obrázek:dial_plan_advanced/receptionist.png
:synchronizace: střed
:alt:Výstižný příklad digitální recepční.

.. důležité:
Elementy telefonního plánu lze konfigurovat kliknutím na ně a výběrem různých funkcí
AxiVox jim tento konzolový systém představil.

Příkladem je třeba audio vzkaz. Ten se musí udělat a pak vybrat.
:guilabel:`Spustit soubor“ nebo „Nápověda“.

Pro více informací se podívejte na tuto dokumentaci:ref:`voip/axivox/audio_messages`.

Pokročilé prvky směrování
=========================

Pokročilé směrovací prvky automaticky přesměrují hovory, jakmile jsou přijaty na příchozí linku.
číslo (y). Toto lze nastavit pomocí geolokace, bílého seznamu nebo proměnných času. Hovory
před jejich konečným cílem procházejí filtrem a jsou směrovány podle nastaveného
variabilní(é).

Následující jsou pokročilé prvky směrování:

- :guilabel:`Zpracovatel událostí“: vytvořte filtr hovorů, který směruje provoz podle polohy
identifikace volajícího.
- :guilabel:`Seznam přístupů“: vytvořte seznam přístupu s přednostním oprávněním pro VIP zákazníky.
- :guilabel:`Časová podmínka“: vytvořte časové podmínky pro směrování příchozího provozu kolem svátků.
jiné citlivé časové úseky.

..tip:
Whitelisting je technický pojem používaný k vytvoření seznamu povolených čísel. Naopak
blacklistování se používá k vytvoření seznamu zakázaných čísel.

Chcete-li přidat jeden z těchto prvků, přejděte na stránku „Dial plány“, která je v nabídce
levé straně „Konzole pro správu Axivoxu“ <https://manage.axivox.com>. Následně klikněte na
Tlačítko „Editor zobrazení“ vedle plánu volání, abyste mohli upravit plán volání. Poté otevřete
Vyberte nový prvek v seznamu „Nový prvek“ a klikněte na „Přidat“.
informace naleznete na adrese:

Scénář dispečera
-------------------

Element Dispatcher je funkcí telefonní ústředny, která směruje hovory podle regionu nebo geolokace.
Většinou je prvek :guilabel:`Dispatcher` v plánu spojen s prvkem :guilabel:`Start`.
prvek, který filtruje nebo snímá hovory, jakmile přichází do příchozího čísla.

Klikněte na položku Dispatcher v okně Dialplan Editor.
její konfiguraci.

Tento prvek kontroluje čísla (přesměrována přes tento prvek) podle pravidel regulárních výrazů.
pravidlo, klikněte na tlačítko „Přidat řádek“ v dolní části panelu „Zasílatel“.
Pop-up okno.

Pak pod tlačítkem „Jméno“ zadejte jméno, které bude sloužit k identifikaci této výrazné vlastnosti.
název, který se objevuje v prvku :guilabel:`Dispatcher` na zobrazené telefonní síti
Pop-up okno Dialplan Editor.

Do pole „Vzor“ zadejte kód země nebo oblasti, kterou používá Axivox.
a pro příchozí hovory. To je zejména užitečné, pokud by společnost chtěla filtrovat
jejich zákazníky do určitých front nebo uživatele podle polohy zákazníka.

Pro specifikaci všech čísel za určitým kódem země nebo oblasti zahrňte do textu po zemi znak „\d+“.
kód nebo kód země + telefonní předčíslí.

.. obrázek: dial_plan_advanced/dispatcher.png
:align:center
:alt:Panel konfigurace dispečera s názvem, pravidlem a přidanou řádkou zvýrazněnou.

Příklad:
  - „02\d+“: ověřuje čísla začínající „02“
  - „00\d+“: platí pro všechna čísla začínající na „00“.
  - „0052\d+“ ověřuje všechna čísla začínající na „0052“ (mezinárodní kód země Mexiko).
  - „001716\\d+“: ověřuje všechna čísla začínající „001716“ (kód země USA + Západní New York
kód oblasti

..tip:
Regulární výraz (zkráceně „regex“ nebo „regexp“) je někdy označován jako „racionální“.
„výraz“ je sekvence znaků, která určuje shodnost s textem. Jinými slovy
přiřazení čísla do daného rozsahu.

Pokud jsou požadované konfigurace dokončeny na okně „Zasílač“ (pop-up), ujistěte se, že
Klikněte na tlačítko „Uložit“.

Při tom se objeví :guilabel:`Dispatcher` s různými trasami.
konfigurovat podle zadaných regulárních výrazů.

Připojte tyto trasy k jakémukoliv :guilabel:`Nový prvek` v okně :guilabel:`Editor dialplánu“.

Výchozí cestou je „Neznámá“ cesta, která se zobrazuje na prvku „Řídicí panel“.
po nastavení alespoň jednoho výrazu regulárního.

Hovory následují tento směr, pokud jejich číslo neodpovídá žádnému zadanému výrazu
na elementu Dispatcher.

.. obrázek: dial_plan_advanced/dispatcher-element.png
:align:center
:alt: Základní telefonní plán s vyznačeným prvkem operátora.

Scénář časové podmínky
-----------------------

Pokud se do plánu přidá prvek „Časová podmínka“, má jednoduchou hodnotu „Pravda“.
a:guilabel:Pravda routing.

Po přidání prvku časového omezení do plánu telefonní ústředny klikněte na něj dvakrát pro jeho konfiguraci
proměnné. „hodina“, „den v týdnu“ a „den v měsíci“.
Všechny hodnoty mohou být konfigurovány.

Pokud čas, kdy volající kontaktuje příchozí číslo, odpovídá nastaveným podmínkám, pak
Pokud je zvolená cesta „pravdivá“, bude se po ní pokračovat, jinak se bude pokračovat po cestě „nepravdivé“.

Příklad:
Pro společnost, která je každoročně uzavřena kvůli americkému svátku nezávislosti (4. července),
Následující časové podmínky by měly být nastaveny:

   - :guilabel:`hodina/minuta“ - „0:0 až 23:59“
   - :guilabel:`Den v týdnu“ – „Všechny na všechny“
   - :guilabel:`Den v měsíci“ - „Od 4 do 4“
   - :label:Měsíc - Červenec

Prvek časové podmínky :guilabel: je zvlášť užitečný pro svátky, víkendy a nastavení
směny. Když se volající dostane na místo, kde může být pomocný, buď
osobě nebo do hlasové schránky, což snižuje zbytečné čekání a odmítnutí hovorů.

.. obrázek:: dial_plan_advanced/time-condition.png
:align:center
:alt:Časové podmínky nastavené v plánu volání na Axivoxu. Časová podmínka je zvýrazněna.

.. důležité:
Chcete-li nastavit časové pásmo, ve kterém bude fungovat podmínka času, přejděte na
„Správce Axivo Management Console <https://manage.axivox.com>“ a klikněte na „Nastavení“.
v levém menu. Poté nastavte časové pásmo pomocí druhého pole zespodu,
kliknutím na vybraný položku z nabídky.

Scénář seznamu přístupů
--------------------

Element Access List v dial plánu umožňuje směrování určitých čísel a zakazuje
popírá jiné čísla.

Po přidání prvku Access List do plánu volání jej lze nakonfigurovat
dvojitým kliknutím na prvek přímo v okně „Editor dialplánu“.

Vyskytnou se dvě pole, do kterých lze vložit regulární výrazy na základě tlačítek „Povolit“ a „Zakázat“.
políčka okna Access List.

Příklad:
Pro velmi důležitého zákazníka mohou být čísla nastavena v poli :guilabel:`Povolit`,
Příchozí hovory mohou být přesměrovány přímo na manažery.

..tip:
Regulární výraz (zkráceně „rex“ nebo „rexp“) je někdy také označován jako
„racionální výraz“, je sekvence znaků, která určuje shodnost vzorce v textu.

.. obrázek:dial_plan_advanced/access-config.png
:align:center
:alt: Konfigurace seznamu přístupu s vyznačenými poli povoleno/zakázáno.

Příklad:
   - „200-299“: ověřuje čísla od „200 do 299“.
   - „02\d*“: platí pro všechna čísla začínající na „02“
   - „0017165551212“ ověřuje číslo („0017165551212“)

Po nastavení políčka :guilabel:`Allow` a :guilabel:`Deny` s regulárními výrazy nebo čísly
Klikněte na tlačítko „Uložit“ v okně „Seznam přístupu“.

Pak na seznamu přístupových listů v plánu volání existují tři cesty (nebo trasy).
Propojit s dalšími kroky.

Neznámé hovory lze přesměrovat na běžnou nabídku volání pomocí vložení prvku Menu.
Připojit ji k cestě Unknown. :guilabel:`Refused` volání lze směrovat na
:guilabel:„Zavěsit“ prvek. Nakonec mohou být „autorizovaní“ volající odesláni na konkrétní
přídavek nebo fronta.

.. obrázek: dial_plan_advanced/access-list.png
:align:center
:alt:Zvýrazněný příklad dial plánu s přístupovým seznamem.

Přepínače
========

Element „Přepínač“ v Axivoxu je jednoduchá aktivní/neaktivní akce pro přepínání trasy.

Tyto mohou být rychle aktivovány nebo vybrány, což umožňuje rychlé změny trasy bez nutnosti měnit
dílčí plán.

Alternativní trasy lze nakonfigurovat tak, aby v případě potřeby byly okamžitě přepnuty. To by
pro novou dostupnost nebo pro přizpůsobení provozu z jakéhokoliv důvodu.

Axivox umožňuje jednoduché zapnutí/vypnutí a víceřadý přepínač s několika možnostmi volby.
od.

- :guilabel:`Přepínač“: manuální ovládání zapnutí/vypnutí, které může směrovat provoz podle toho, zda je otevřený
buď otevřené (on), nebo uzavřené (off).
- :guilabel:„Multiswitch“: mechanismus pro vytváření cest a jejich zapínání a vypínání, který umožňuje odvádět
přijaté hovory.

Základní přepínač
------------

Pole „Vybrat“ lze nastavit v „Konzoli pro správu Axivo <https://manage.axivox.com>“
Navigace do sekce „Přepínače“ v levém menu. Pro vytvoření nového přepínače klikněte na „Vytvořit
Přepněte na panel „Vypínače“ (viz obrázek), nastavte jméno pro něj a klikněte
:guilabel:`Uložit“.

Poté přepněte požadovaný přepínač na buď „Zapnuto“ nebo „Vypnuto“,
Sloupec „Stát“ na panelu „Přepínače“.

Toto stav :guilabel:`On` / :guilabel:`Off“ automaticky směruje provoz v telefonním plánu, ve kterém
Tento přepínač je nastavený.

Provoz se přepne na trasu „Aktivní“ při zapnutí vypínače.
Provoz hovorů se přepne na trasu :guilabel:`Inactive`, když je v :guilabel:`Off` stisknuto
přepínač.

Změny lze provádět na letišti. Ujistěte se, že kliknutím na tlačítko „Použít změny“ uvedete změny do praxe.
jejich.

Přidejte přepínač do telefonního plánu
~~~~~~~~~~~~~~~~~~~~~~~~~

Přidat do telefonního plánu :guilabel:`Switch` lze pomocí Axivox Management Console.
<https://manage.axivox.com> a v levém menu klikněte na položku „Telefonní plány“. Pak
:guilabel:`Editor zobrazení“ vedle požadovaného plánu volání, aby se otevřel „Editor plánu volání“.
Pop-up okno.

Vyberte z rozevírací nabídky „Nový prvek“ možnost „Přepínač“ a pak klikněte
:guilabel:Přidat“. Dvojklikem na prvek můžete dále konfigurovat :guilabel:„Přepínač“

.. obrázek:dial_plan_advanced/switch.png
:align:center
:alt:Nastavení telefonní ústředny s aktivními a neaktivními trasami zvýrazněnými.

Multiswitch
------------

V Axivoxu je „multi-switch“ prvkem takový přepínač, kde lze konfigurovat více cest a přepínat mezi nimi.
mezi.

Pro konfiguraci a nastavení prvku Multi-Switch přejděte do Axivox management console
Poté klikněte na položku „Přepínače“ v levém menu.

Přepněte na kartu „Více přepínačů“ a vytvořte nebo nastavte přednastavený
:guilabel:`Současné přepínače“ prvek.

Chcete-li vytvořit nový :guilabel:`Multiswitch`, klikněte na :guilabel:`New` a poté zadejte
Název pro prvek a pak zadejte „Volitelné“. Zadejte jednu
:guilabel:`Volitelné položky na řádku“; nezapomeňte, že duplicitní záznamy se nevyhodnocují.

Pamatujte na kliknutí tlačítka „Uložit“.

Pro výběr státu v Multi-Switch klikněte na rozbalovací nabídku vedle
Název „Multiswitch“, pod záložkou „Multiswitch“ v
Panel „Přepínače“.

Zvolený stát je cestou, kterou se v telefonní předvolbě následuje. Zvolený stát
může být upraveno na lince, stačí kliknout na „Použít změny“.

Přidejte vícenásobný přepínač do plánu telefonního čísla
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chcete-li do plánu přidat prvek :guilabel:`Multi-Switch`, přejděte na Axivox management console
<https://manage.axivox.com> a v levém menu klikněte na položku „Telefonní plány“.

Vyberte nebo vytvořte telefonní plán. Pak klikněte na „Editor zobrazení“ u požadovaného telefonního plánu.

Na okně „Editor dialplánu“, které se objeví, klikněte na „Nový prvek“.
položce „Vyberte“ a vyberte možnost „Multiswitch“. Pak klikněte na „Přidat“ a dvojklikem na
prvek, který lze dále konfigurovat pomocí prvku :guilabel:`Switch`.

.. obrázek: dial_plan_advanced/multi-switch.png
:align:center
:alt: Konfigurace více přepínačů v telefonní ústředně s vybranou cestou zvýrazněnou.
