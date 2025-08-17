==========================
Trasy a pravidla tlačení/táhnutí
==========================

Modul „Trasy“ v Odoo řídí pohyb produktů mezi různými místy, ať už se jedná o interní nebo
vnější, používající pravidla tlaku a tahu. Jakmile jsou nastaveny, tyto pravidla pomáhají automatizovat logistiku produktů
pohyb založený na specifických podmínkách.

.. viz též:
   - „Tutoriály Odoo: trasy <https://www.youtube.com/watch?v=qkhDUezyZuc>“
   - :doc:`Standardní trasy v Odoo <../daily_operations>`

.. poznámka::
Cesty jsou aplikovatelné na produkty, kategorie produktů, způsoby dopravy, balení.
<sklad/správa produktů/balení s trasou>, a na řádku prodejního příkazu.

O trasách a termínech
============================

V obecném skladu jsou příjmový můstek, kontrolní oblast kvality, skladovací prostory.
pracovníci v těchto oblastech pracují na výrobním procesu od začátku až do konce.
produkty procházejí jednotlivými místy, každé místo spouští produktů určený způsob.
pravidla.

.. obrázek: použít_cesty/vzorek_skladu.png
:align:center
:alt: Pohled na sklad s kontrolou kvality.

V tomto případě vozidla dodavatelů vyloží palety objednaných výrobků na přijímací molo.
Poté zkontrolujte produkty v oblasti příjmu. Podle trasy a pravidel se některé produkty
Tyto výrobky jsou odeslány do kontrolní oblasti kvality (například produkty, které tvoří součást používaných komponentů).
výrobním procesem), zatímco jiné jsou přímo uloženy na svých odpovídajících místech.

.. obrázek: použít_cesty/přidat_k_pravidlu_vzor.png
:align:center
:alt: Pohled na běžný tlak při přijímání produktů.

Tady je příklad plnění objednávek. Ráno se vybírají všechny položky pro všechny objednávky
musí být připraveny během dne. Tyto předměty jsou vybrány z skladových míst a přemístěny na
připravené k expedici. Pak se objednávky zabalí do příslušných
Krabice a pásy přepravníky je dopraví k odbavovacímu můstku, kde jsou připravené k dodání zákazníkům.

.. obrázek: použít_trasy/vytažení_zákona_příklad.png
:align:center
:alt: Pohled na obecný tah z pravidla při přípravě dodávek.

Pravidla tlaku
----------

Pravidla nákupu se používají k tomu, aby zboží bylo ihned po příjezdu do skladovacího místa dodáno.
konkrétní místo určení.

.. poznámka::
Pravidla push mohou být spuštěna pouze tehdy, pokud neexistují žádné pravidla pull, která již vygenerovala
převody produktů.

V jednokrokové cestě přijímání faktur (<receipts_delivery_one_step>) s použitím jediného pravidla pro tlačení.
produkt přijde do skladu, může se automaticky převést na *Sklad
Lokalita. Různé pravidla pro tlačení mohou být aplikována na různé produkty, což umožňuje přizpůsobení
skladovací místa.

.. obrázek: použít_trasy/přidat_pravidlo.png
:align:center
:alt: Pravidlo pro příjem v jednom kroku.

Přesunout pravidlo pro trasu „Příjem v jednom kroku“.

Pro více informací o konfiguraci pravidel přeskočte na část :ref:`Konfigurace pravidel
<Inventura/Přijetí a výdej/Nastavení pravidel>.

Pravidla tahu
----------

Pravidla táhnou produkty na požadované místo, například prodejní objednávku nebo potřebu doplnit zásoby.
<../../sklady/dodavky/pravidla-pro-naskladnění>.

Pravidla tahu fungují od místa poptávky zpět. Například v případě dvoufázového doručení
Dvoufázovém procesu přepravy zboží od skladu k výrobě.
Před předáním zákazníkovi se vytvoří převod z
Dodání výrobku zákazníkovi. Pokud je produkt nenalezen na „Výstupu“, jiná pravidla tahového systému vytvoří převod
od *Sklad* k *Výstupu*. Skladníci pak zpracovávají tyto převody v opačném pořadí:
vybírání a následné odesílání.

.. obrázek:: use_routes/pull-rule.png
:align:center
:alt: Příklad tahu pravidla.

Vytáhněte pravidla pro trasu „Dodání ve dvou krocích“.

Pro více informací o konfiguraci pravidel přeskočte na část :ref:`Konfigurace pravidel
<Inventura/Přijetí a výdej/Nastavení pravidel>.

..._použití tras/pravidla tras:

Konfigurace
=============

Odoo vám pomůže spravovat pokročilé trasy, protože jsou to soubory pravidel „Tlač“ a „Vytáhnout“.
konfigurace jako například:

- Řídit výrobní řetězce produktů.
- Spravovat výchozí umístění pro každý produkt.
- Definujte trasy v skladu podle obchodních potřeb, například kontroly kvality.
pozáruční servis nebo vrácení zboží od dodavatele.
- Zjednodušte správu pronájmu tím, že budete automaticky generovat návratové pohyby pro zapůjčené produkty.

Nejprve otevřete aplikaci „Sklad“ (Guilabel) a přejděte do
V nabídce „Nastavení“ vyberte možnost „Sklad“. Pak v sekci „Sklad“ zapněte
Klikněte na „Uložit“ a poté na „Další kroky“.

.. obrázek: použít_cesty/vícekrokové_cesty_vlastnosti.png
:align:center
:alt:Aktivujte funkci vícefázových tras v Odoo Inventuře.

.. poznámka::
Funkce „Uložiště“ je automaticky aktivována s
:guilabel:`Multistepové trasy“

Jakmile je tento první krok dokončen, může uživatel používat přednastavené trasy dodávané s Odoo.
Mohou vytvářet vlastní trasy.

Přednastavené trasy
---------------------

Pro přístup k přednastaveným trasám Odoo zvolte v menu: „Sklad --> Konfigurace -->
Skladovny“. Pak otevřete formulář „Konfigurace skladu“ v záložce „Nastavení skladu“, kde uživatel
může zobrazit přednastavené trasy skladu pro příchozí zásilky.
:guilabel:`Odeslané zásilky“.

.. obrázek: use_routes/example-preconfigured-warehouse.png
:align:center
:alt:Sklad v Odoo Inventories přednastavený.

Některé pokročilejší trasy, jako například „pick-pack-ship“, jsou také k dispozici. Uživatel si může vybrat
nejvhodnější trasu pro své podnikání. Jakmile jsou přijaté zásilky a
:guilabel:`Výchozí trasy“ jsou nastavené, přejděte na „Skladové zásoby – Konfigurace“.
--> Cesty k zobrazení konkrétních tras, které vygeneroval Odoo.

.. obrázek: use_routes/preconfigured-routes.png
:align:center
:alt: Přehled všech přednastavených tras, které nabízí Odoo.

Na stránce „Trasy“ klikněte na trasu, abyste otevřeli formulář trasy. V formuláři trasy je
Uživatel může zobrazit, které oblasti trasa platí. Uživatel také může nastavit trasu
pouze na konkrétní společnost. To je užitečné v prostředí více společností, protože
Příkladem je například to, že uživatel může mít firmu a sklad v zemi A a druhou firmu a sklad ve
Země B.

.. viz též:
:ref:`Použitelné na obalech <inventory/product_management/packaging-route>`

.. obrázek: použít_cesty/cesty-příklad.png
:align:center
:alt: Příklad trasy, která se vztahuje na kategorie produktů a sklady.

Na konci trasy je možné zobrazit specifické „Pravidla“ pro tuto trasu.
Každá pravidlo má akci, zdrojové umístění a
:guilabel:`Místo určení“.

.. obrázek: použít_trasy/pravidla-příklad.png
:align:center
:alt:Příklad pravidel s akcemi tlačit a táhnout v Odoo Inventuře.

Nastavení tras
-------------

Chcete-li vytvořit vlastní trasu, přejděte na: „Sklad --> Konfigurace --> Trasy“ a klikněte
Vytvořit“. Následně vyberte místa, kde se tato trasa bude zobrazovat. Trasa může být
použitelná na kombinovaných místech.

.. obrázek: použít_cesty/pokročilé_cesty.png
:align:center
:alt: Pohled na trasu skladování, balení a dodání.

Každé místo má jiný chování, proto je důležité označit pouze užitečné políčka a přizpůsobit každé
upravte trasu podle toho. Pak konfigurujte pravidla trasy.

Pokud je trasa aplikovatelná na produktovou kategorii, trasu stále musíte nastavit ručně v
Kategorie produktů vytvoříte tak, že se přesunete na: Menu --> Sklad --> Konfigurace --> Produkty
Kategorie. Pak vyberte kategorii produktu a otevřete formulář. Poté klikněte na „Upravit“
V sekci „Doprava“ nastavte „Trasy“.

Při aplikaci trasy na produktovou kategorii se použijí všechny nastavené pravidla v trase
všechny produkty v dané kategorii. To může být užitečné, pokud firma používá model drop shipping
pro všechny produkty z dané kategorie.

.. obrázek: použít_trasy/trasy-logistické-sekce.png
:align:center
:alt: Pohled na trasu aplikovanou kategorií „vše“.

Také sklady jsou na tom podobně. Pokud se trasa vztahuje na :guilabel:`Sklady`, všechny
přesuny v rámci vybraného skladu, které splňují podmínky pravidel trasy
Poté bude následovat tento směr.

.. obrázek: použít_trasy/vztahující se na sklad.png
:align:center
:alt: Zobrazení nabídky skladu při výběru vhodného na skladě.

Pokud je cesta použitelná na řádcích objednávek, je to zhruba opak.
cestu je nutné vybrat ručně při vytváření cenové nabídky. To se hodí, pokud některé produkty procházejí
různé trasy.

Pamatujte na zapnutí viditelnosti sloupce „Trasa“ v citaci a objednávce.
Pak lze trasu vybrat na každé řádku objednávky/prodejního příkazu.

.. obrázek:use_routes/add-routes-to-sales-lines.png
:align:center
:alt:Pohled na nabídku, která umožňuje přidávat nové řádky do objednávek prodeje.

Nakonec jsou tu trasy, které se dají aplikovat na produkty. Ty fungují víceméně jako produkt
kategorií: Jakmile je vybrána kategorie, musí být trasa ručně nastavena v produktovém formuláři.

Chcete-li nastavit trasu na produkt, přejděte do sekce „Sklad --> Zboží --> Zboží“ a vyberte
požadovaný produkt. Poté přejděte na záložku „Sklad“ a pod záložkou „Operace“
v části „Způsoby“, vyberte možnost „Trasy“.

.. obrázek: použít trasy/na produktu.png
:align:center
:alt: Pohled na produktový formulář, kde je nutné vybrat trasu.

.. důležité::
Na trase musí být nastaveny pravidla, aby trasa fungovala.

… inventarizaci, přijímání a konfiguraci pravidel:

Pravidla
~~~~~

Pravidla jsou definována v sekci „Trasa“ na formuláři. Nejprve přejděte do sekce „Nastavení“:
--> Vyberte trasu a otevřete požadovanou trasu. Následně klikněte na tlačítko „Upravit“ a v
V sekci „Pravidla“ klikněte na „Přidat řádek“.

.. obrázek: use_routes/add-new-rules.png
:align:center
:alt:Pohled na nabídku pravidel, kde lze přidat nová pravidla.

K dispozici jsou různé pravidla, která spouští různé akce. Pokud nabízí Odoo *Push* a *Pull* pravidla, ostatní jsou
Je k dispozici také každá pravidlo má :guilabel:`Akci`:

- :guilabel:`Vytažení z“: tato pravidla se spouští potřebou produktu v konkrétní lokalitě.
Potřeba může vzniknout z potvrzení objednávky nebo z výroby, která vyžaduje
určité složky. Když se potřeba objeví v cílovém místě, Odoo vygeneruje výdejku.
Splnit tuto potřebu.
- :guilabel:`Přesun na“: tato pravidla se spustí při příchodu některých produktů do definovaného zdroje
místo. V případě přesunu produktů do zdrojového místa generuje Odoo výdejní listy.
přepravit tyto produkty na místo určení.
- :guilabel:`Táhnout a tlačit“: Tato pravidlo umožňuje generovat výběry v obou situacích
vysvětleno výše. To znamená, že když jsou požadovány určité produkty na konkrétním místě, je nutné provést převod
vznikla z předchozí lokality, aby tuto potřebu uspokojila. Tím vytváří potřebu na předchozí
místo a vyvolá se pravidlo k jeho splnění. Jakmile je druhá potřeba uspokojena, produkty
Jsou převezeny na místo určení a všechny potřeby jsou uspokojeny.
- :guilabel:`Koupit“: když jsou produkty potřeba na místě určení, je vytvořen požadavek na nabídku.
vytvořené, aby tuto potřebu uspokojily.
- :guilabel:`Výroba“: když jsou produkty potřeba v původní lokalitě, je vydán výrobní příkaz
Je vytvářen, aby vyhověl potřebám.

.. obrázek: použít trasy/přetáhnout z pravidla skladu do balení.png
:align:center
:alt: Přehled pravidla „Pull From“, které vytváří převod mezi zásobami a balením
zóna.

Operační typ musí být také definován v pravidle, což určuje, jaký druh skladování
Vzniká z pravidla.

Pokud je nastavení pravidla :guilabel:`Action` na :guilabel:`Pull From“ nebo :guilabel:`Pull & Push“,
:guilabel:„Zdroj“ musí být nastaven. Zdroj definuje, co se stane při
Zdroj:

- :guilabel:`Odebrat z skladu“: produkty jsou odebírány ze skladových zásob zdroje
lokalita.
- :guilabel:`Zapnout jinou pravidlo“: Systém se pokusí najít skladovou pravidla, která by produkty přivedly na
zdrojové umístění. Ignoruje se dostupný zásoby.
- „Vybrat z skladu, pokud není k dispozici, spustit jiný pravidlo“: produkty jsou vybírány
zpracování objednávky a pokud je na skladě dost zboží, tak se objednávka zpracuje.
zjistit pravidlo, které by produkty přeneslo na zdrojové místo.

Příklad průtoku
============

V tomto příkladu použijme vlastní cestu Pick-Pack-Ship, abychom vyzkoušeli plný tok s pokročilým
vlastní trasa.

Nejprve rychlý pohled na pravidla trasy a jejich dodavatele. Jsou tři pravidla, všechna
„Vytažení z“ pravidel. „Dodavatelské metody“ pro každé pravidlo jsou následující:

- :guilabel:`Vybrat z skladu“: Když jsou produkty potřeba v :guilabel:`Zóně balení a skladování“, provede se výběr.
(výrobní přesuny z :guilabel:`WH/Stock“ do :guilabel:`WH/Packing Zone“) jsou vytvářeny
:guilabel:`WH/Stock“ k naplnění potřeby.
- „Spouštění dalšího pravidla“: Když jsou produkty potřeba v „Výrobě / Výstupu“, pak se balí
(interní přesuny z :guilabel:`WH/Balicí zóna“ do :guilabel:`WH/Výstup“) jsou vytvářeny
:guilabel:`WH/Balicí zóna“ k vyplnění potřeby.
- „Spouštění jiného pravidla“: Když jsou produkty potřeba v „Partner
Výrobní objednávky vytváříme z položek „Místa / Zákazníci“ a „Dodací listy“.
potřeba.

.. obrázek: použít trasy/přepravní přehled.png
:align:center
:alt: Přehled všech přeprav vytvořených pomocí trasy „pick-pack-ship“.

To znamená, že když zákazník objedná produkty s nastavenou trasou „vybrat – zabalit – odeslat“,
je vytvořen dodací příkaz k vyřízení objednávky.

.. obrázek: použít trasy/operaci přesunu.png
:align:center
:alt: Pohled na operace vytvořené tahem z převodu.

.. poznámka::
Pokud je zdrojovým dokumentem pro více převodů stejný prodejní doklad, stav není stejný.
Pokud je předchozí přenos v seznamu ve stavu „Čeká na další operaci“, pak bude nový přenos
Ještě není hotovo.

.. obrázek: použít_cesty/čekací_stavy.png
:align:center
:alt: Pohled na různé stavy převodů v průběhu procesu.

Pro přípravu expedičního listu jsou v výstupní oblasti potřebné balené produkty, takže
požaduje se přesun z pásu balení.

.. obrázek:: use_routes/detailed-operations-2.png
:align:center
:alt: Pohled na podrobné operace při přesunu mezi zónou balení a výstupem.

Samozřejmě, že balicí zóna potřebuje produkty připravené k zabalení. Proto je nutné provést vnitropodnikový přesun
požadovány na sklad a zaměstnanci si mohou zboží ze skladu vyzvednout.

.. obrázek: použít trasy/podrobné operace převodu.png
:align:center
:alt: Pohled na podrobné operace při přesunu mezi skladovou a balicí zónou.

Jak uvedeno v úvodu dokumentace, poslední krok procesu (pro tento
(trasy, dodacího příkazu) je první spouštěna, která pak spouští další pravidla až do chvíle, kdy
dosáhnout prvního kroku procesu (tady převodu ze skladu do balení)
plocha) je nyní připravena k zpracování tak, aby zákazník obdržel objednané zboží.

V tomto případě je produkt dodán zákazníkovi až ve chvíli, kdy jsou všechny podmínky splněny.
Převody jsou hotové.

.. obrázek: použít trasy/přepravní stav.png
:align:center
:alt:Zobrazení stavu převodů po dokončení trasy.
