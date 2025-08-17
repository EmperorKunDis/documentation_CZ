=======================
Omezit přístup k datům
=======================

.. důležité:
Tento návod je pokračováním návodu :doc:`server_framework_101`. Ujistěte se, že jste si přečetli
dokončil ji a použijte modul „majetek“, který jste postavili, jako základ pro cvičení v této
návod.

Dosud jsme se převážně zabývali implementací užitečných funkcí.
Ve většině podnikatelských scénářů se však bezpečnost stává problémem:
v současné době

* Každý zaměstnanec (což je co „group_user“ znamená) může vytvářet, číst
aktualizovat nebo smazat vlastnosti, typy vlastností a štítky vlastností.
* Pokud je nainstalován „účet majetku“, pak mohou interagovat pouze agenti povolení k tomu.
S fakturací lze potvrdit prodej, což je nutné k vytvoření
faktura <návody/serverový-rámec-101/13_jiný-modul/vytvořit>.

Ale:

* Nechceme, aby třetí strany mohly přímo přistupovat k nemovitostem.
* Nemusí být všichni naši zaměstnanci makléři nemovitostí (např. administrativní pracovníci).
(personál, správci nemovitostí...), nechceme, aby o nich věděli lidé, kteří
dostupných nemovitostí.
* Makléři nemají potřebu ani právo rozhodovat o tom, jaké typy nemovitostí nebo tagy jsou
*k dispozici*.
* Makléři mohou mít exkluzivní nemovitosti, my nechceme jednoho makléře
aby mohl spravovat exkluzivy jiných.
* Všichni makléři nemovitostí by měli být schopni potvrdit prodej nemovitosti.
může spravovat, ale nechceme, aby mohly platit nebo označit jako zaplacené
jakýkoliv fakturu v systému.

.. poznámka::

Možná bychom s některými nebo dokonce většinou z nich mohli být spokojeni pro malé podniky.

Protože je pro uživatele snazší vypnout zbytečná bezpečnostní pravidla než
Je lepší být opatrný a vytvořit je z ničeho.
a omezit přístup: uživatelé mohou kdykoli povolit přístup, pokud je to nutné nebo vhodné.

Skupiny
======

.. viz též:

Dokumentace k této problematice je dostupná v sekci :ref:`Bezpečnostní
odkazu <reference/security>.

:dokument: „/přispívání/rozvoj/směrnice kódování“ popisuje formát a
umístění hlavních datových polí.

.. varování: **Cíl**

V závěru této části

    - Můžeme zaměstnance udělat realitními makléři nebo správci nemovitostí.
    - Uživatel „admin“ je správce nemovitosti.
    - Máme nového zaměstnance, který nemá přístup k fakturaci
nebo správy.

Přidělit každému zaměstnanci individuální bezpečnostní pravidla by nebylo praktické.
je čas na změnu, která by spojila bezpečnostní pravidla s uživateli. Tyto skupiny odpovídají
do rolí, které lze přiřadit zaměstnancům.

Pro většinu aplikací Odoo je dobrým základem mít uživatele a
*manažerské* role (nebo správce): manažer může změnit konfiguraci
aplikace a celé její používání, zatímco uživatel může klidně
použít aplikaci [#appuser]_.

Tento základ je pro nás dostačující:

* Realitní makléři si mohou systém konfigurovat (spravovat dostupné typy a
i dohlížet na každou nemovitost v prodejním procesu.
* Makléři mohou spravovat nemovitosti ve své péči nebo nemovitosti.
které nejsou v péči konkrétního agenta.

Odoo je založen na datech, takže skupina je jen záznamem
„res.groups“ model. Obvykle jsou součástí modulu „master data
<definice modulu>, která je definována v jednom z datových souborů modulu.

Jednoduchý příklad najdete zde <https://github.com/odoo/odoo/blob/532c083cbbe0ee6e7a940e2bdc9c677bd56b62fa/addons/hr/security/hr_security.xml#L9-L14>.

..cvičení::

    #Vytvořte soubor „security.xml“ v příslušné složce a přidejte jej do souboru „__manifest__.py“.

    #Pokud již tak neučinil, přidejte do souboru „__manifest__.py“ pole „kategorie“ s hodnotou „Nemovitosti/Makléř“.

    #Přidejte záznam vytvářející skupinu s ID „estate_group_user“ a názvem „Agent“.
a kategorie „Základní modul - Kategorie realitního makléře“.

    #Pod ní přidejte záznam vytvářející skupinu s ID „správce nemovitosti“.
jméno „Manager“ a kategorii „base.module_category_real_estate_brokerage“.
Skupina „správce skupiny“ musí obsahovat uživatele „uživatel skupiny“.

.. poznámka::

Kde se vzala ta kategorie? Je to modulová kategorie.
V tomto případě jsme použili kategorii s ID „base.modul_kategorie_realitní kancelář“.
která byla automaticky vygenerována pomocí Odoa na základě hodnoty v poli „kategorie“ ve souboru __manifest__.py modulu.
Na stránkách také najdete seznam.
`Výchozí kategorie modulů <https://github.com/odoo/odoo/blob/71da80deb044852a2af6b111d695f94aad7803ac/odoo/addons/base/data/ir_module_category_data.xml>`_.
Provozovatelé e-shopů tak mohou využívat například funkci automatického vytváření objednávek nebo možnost přizpůsobit si fakturační údaje.

.......tip::

Protože jsme změnili soubory dat, pamatujte na restartování Odoa a aktualizaci
modul s příkazem „-u state“.

Pokud se přesunete do nastavení „Spravovat uživatele“ a otevřete
„Admin“ uživatel („Mitchell Admin“) by měl vidět novou sekci:

.. obrázek:: restrict_data_access/groups.png

Uživatelské jméno správce nastavte na „Manažer nemovitostí“.

..cvičení::

Přes webové rozhraní vytvořte nového uživatele pouze s rolí „realitní makléř“.
přístup. Uživatel by neměl mít žádný přístup na fakturaci nebo správu.

Přihlášení s novým uživatelem proveďte v soukromém okně nebo záložce (nezapomeňte nastavit
(a heslo), jako makléř byste měl vidět jen nemovitosti.
aplikace a možná i aplikace Diskuse (chat):

..... obrázek:: restrict_data_access/agent.png

Přístupová práva
=============

.. viz také: Dokumentace k tématu je dostupná na
:ref:`reference/security/acl`.

.. varování: **Cíl**

V závěru této části

    - Ti, kteří nejsou alespoň makléři, se na to nikdy nedostanou.
aplikace pro nemovitosti.
    - Makléři nemohou aktualizovat typy nebo tagy nemovitostí.

Práva přístupu byly poprvé představeny v :doc:`server_framework_101/04_securityintro`.

Přístupová práva jsou způsob, jak dát uživatelům přístup k modelům prostřednictvím skupin: asociovat
přístup do skupiny, pak bude mít přístup všechny uživatele této skupiny.

Například nechceme, aby si makléři mohli měnit vlastnosti nemovitosti.
jsou k dispozici typy, takže bychom je nepropojili s uživatelskou skupinou.

Přístupová práva mohou dát přístup, ale nemohou jej odebrat: když je
ověřené, systém zkontroluje, zda je uživateli přiděleno *jakékoliv* oprávnění
(prostřednictvím jakékoli skupiny) poskytuje přístup.

====== ====== ==== ====== ======
skupina vytvořit přečíst aktualizovat smazat
------ ------ ---- ------ ------
A           X      X
B                X
C                      X
====== ====== ==== ====== ======

Uživatel s oprávněními skupin A a C bude moci provádět všechny operace, kromě odstranění objektu.
Zatímco uživatelé s oprávněním B a C budou moci číst a aktualizovat soubor, ale nebudou mít právo vytvářet nebo mazat jej.

.. poznámka::

    * Skupina přístupových práv může být vynechána, což znamená, že se aplikují ACL.
každému uživateli, je to užitečná ale riziková záloha, protože v závislosti na
aplikace nainstalovaná na zařízení může umožnit i nezaregistrovaným uživatelům přístup k modelu.
    * Pokud se na uživatele nevztahuje žádný přístupový právo, nebude mu přístup umožněn
(výchozí odepření).
    * Pokud se odkazuje na model, ke kterému uživatel nemá přístup.
nemá podmenu, který uživatel vidí, nebude zobrazeno.

.. cvičení: Aktualizujte soubor oprávnění přístupu na:

    * Dávejte plný přístup ke všem objektům do skupiny správce nemovitostí.
    * Uživatelům (zaměstnancům realitní kanceláře) udělte přístup jen na typy a štítky.
    * Nikomu nedávejte právo majetek smazat.
    * Zkontrolujte, zda uživatelský agenti nemohou měnit typy nebo tagy,
majetek, ale jinak mohou vytvářet nebo aktualizovat
vlastnosti.

.... varování::

Nezapomeňte přiřadit každému záznamu „ir.model.access“ jiný identifikátor XID
Pokud ano, pak se vám data přepíší navzájem.

Uživatel „demo“ nebyl jmenován makléřem nebo manažerem, takže
neuvidí ani reálnou nabídku nemovitosti. Použijte soukromé záložky nebo okno
zjistit, zda je tomu tak (uživatel „demo“ má heslo „demo“).

Rekordní pravidla
============

.. viz také: Dokumentace k tématu je dostupná na
:ref:`reference/bezpecnost/pravidla`.

.. varování: **Cíl**

Na konci této části nebudou agenti moci vidět vlastnosti.
výhradně pro své kolegy, ale manažeři budou stále moci vidět
vše.

Přístupová práva mohou umožnit přístup k celému modelu, ale často potřebujeme
konkrétněji: zatímco agenti mohou interagovat s vlastnostmi obecně, nemusí
chtějí, aby je aktualizovali nebo dokonce viděli nemovitosti spravované jedním z jejich kolegů.

Rekordní pravidla přesně stanoví, jakým způsobem mohou být data zveřejněna nebo zamítnuta.
individuální rekordy:

... blok kódu::xml

<záznam id="pravidlo_id" typ="ir.rule">
<políčko name="název">Popis role pravidla</políčko>
<položka jméno="model_id" odkaz="model_to_manage"/>
<pole jméno="perm_read" hodnota="False"/>
<pole název="skupiny" hodnota="[Komandní odkaz na skupinu uživatelů (base.group_user)]" />
<políčko jméno="doména_povinnost">
"|", ("user_id", "=", uživatel.id)
('user_id', '==', False)
]</field>
</záznam>

Reference na :ref:`orm/domains` řídí přístup k záznamům: pokud je záznam v pořádku,
Pokud ano, je přístup povolen, jinak je přístup zamítnut.

..tip:

Protože pravidla bývají spíš komplikovaná a nejsou vytvářena ve velkém množství, jsou
Obvykle se vytváří ve formátu XML, nikoli ve formátu CSV používaném pro přístupová práva.

Pravidlo výše:

* Pouze pro „vytvořit“, „aktualizovat“ (napsat) a „odstranit“ (odpojit).
operace: zde chceme, aby každý zaměstnanec mohl vidět záznamy ostatních uživatelů
Ale aktualizovat záznam může pouze autor / přiřazený uživatel.
* Je tedy „ne globální“ (viz odkaz na bezpečnostní pravidla), takže můžeme poskytnout
příkladně pro manažery.
* Povolí operace pokud je nastaven aktuální uživatel („user.id“).
nebo je přiděleno na záznamu nebo pokud záznam nemá žádného uživatele.

.. poznámka::

Pokud není definována žádná pravidla pro model nebo operaci, pak
operace je povolena (výchozí povolené), což může mít zvláštní účinky
pokud nejsou nastaveny přístupová práva správně (jsou příliš dovolující).

..cvičení::

Definujte pravidlo, které omezuje agenty na možnost vidět nebo upravovat
nemovitosti bez realitního makléře nebo nemovitosti, na které je realitní makléř.

Možná chcete vytvořit druhého uživatele pro realitní makléře nebo vytvořit několik
vlastnosti, které spravuje prodejce nebo jiný uživatel.

Zkontrolujte, zda váš správce nemovitostí stále vidí všechny nemovitosti.
Nebo proč ne? Vzpomeňte si:

Skupina „správce skupiny“ musí obsahovat uživatele „uživatel skupiny“.

Překročení bezpečnostních opatření
=================

Obcházení bezpečnostních opatření
------------------

.. varování: **Cíl**

Při konci této části by měli být agenti schopni potvrdit prodej nemovitostí.
bez nutnosti přístupu k fakturaci.

Pokud se jako makléř pokusíte nemovitost označit za „prodanou“, měli byste dostat
chyba přístupu:

.. obrázek:: odeprived-access-to-data/error.png

K tomu dochází proto, že funkce „estate_account“ se pokouší vytvořit fakturu během
proces, ale vytváření faktury vyžaduje oprávnění k celému řízení fakturace.

Chceme, aby agenti mohli potvrdit prodej bez plné fakturace.
přístup, který znamená, že musíme obejít běžné bezpečnostní kontroly v rámci systému Odoo.
vytvořit fakturu, ačkoliv aktuální uživatel nemá oprávnění
To udělejte.

Existují dvě hlavní cesty k obcházení stávajících bezpečnostních kontrol v Odoo, a to
záměrně nebo jako vedlejší účinek:

* Metoda „sudo()“ vytvoří nový záznamový set v režimu „sudo“, což ignoruje
všechna práva přístupu a pravidla záznamů (i když jsou pečlivě zakódované kontroly skupin a uživatelů)
Stále platí, že může.
* Vykonávání neošetřených dotazů na databázi obchází přístupová práva a pravidla záznamu.
to je vedlejší účinek obcházení ORM samotného.

..cvičení::

Aktualizujte „estate_account“ tak, aby při vytváření obcházely přístupová práva a pravidla
fakturu.

.. nebezpečí::

Tyto vlastnosti by měly být obecně vyhýbány a používané s maximální opatrností.
po kontrole, že aktuální uživatel a operace mají oprávnění
obejít běžné ověřování přístupových práv.

Operace prováděné v takovém režimu by měly být založeny na co nejmenším množství
a měli by ho co nejvíce ověřit.

Programově kontrolovat bezpečnost
----------------------------------

.. varování: **Cíl**

Na konci této části by měla být vytvoření faktury odolná
k bezpečnostním otázkám, ať už se jedná o změnu „majetku“.

V Odoo se ověřují přístupová práva a pravidla záznamů pouze při provádění dat
přístup přes ORM* např. vytváření, čtení, vyhledávání, zápis nebo odpojení
záznamem metodami ORM. Jinými metodami se nemusí kontrolovat žádné
druhu přístupových práv.

V předchozím kroku jsme obešli pravidla pro vytváření faktur
v „akční_prodáno“. Tento obchvat může využít každý uživatel bez jakýchkoliv oprávnění
právo, které se kontroluje:

- Před vytvořením „estate_account“ přidejte tisk do „action_sold“.
účetní doklad (vytvoření účetního dokladu přistupuje k vlastnosti, tedy spouští
(např. kontrola ACL).

print("dosáhlo ".center(100, "="))

V protokolu Odoo byste měli vidět „dosáhl“ a následně chybu přístupu.

.. nebezpečí: Jen proto, že už jste v Pythonovém kódu, neznamená to, že máte přístup
pravidlo nebo právo bylo či bude zkontrolováno.

*Nyní* jsou přístupy implicitně kontrolovány při přistupování k datům na „sám“
i volání „super()“ (které dělá totéž a aktualizuje „self“).
vyvolávání chyb při přístupu a zrušení transakce „odstraněním“ našeho
faktura.

Pokud se však v budoucnu změní, nebo přidáme vedlejší účinky metody
(např. ohlášení prodeje na úřad) nebo se do programu dostane
„majetek“, … by bylo možné, aby neagentní osoby spouštěly operace.
neměli mít přístup k.

Proto při provádění operací nezahrnujících CRUD nebo při oprávněném obejití
ORM nebo bezpečnostní vrstva, nebo když spouští jiné vedlejší účinky, je
je důležité provádět *explicitní bezpečnostní kontroly*.

Explicitní kontrola zabezpečení může být prováděna:

* Zkontrolovat, kdo je aktuální uživatel („self.env.user“) a porovnat jejich hodnoty
konkrétní modely nebo záznamy.
* Zkontrolovat, zda uživatel má kódované skupiny povolit nebo zakázat.
operace („self.env.user.has_group“).
* Při volání funkce „check_access(operations)“ na objektu RecordSet se ověřuje, že
aktuální uživatel může provádět operaci na každém záznamu v sadě.
Jako speciální případ se kontroluje prázdný záznamový set.
Uživatel má určitá oprávnění k provádění operací na modelech obecně.

..cvičení::

Před vytvořením faktury použijte funkci „check_access“ k ověření, že aktuální
uživatel může aktualizovat vlastnost, za kterou je faktura.

Spusťte znovu skript obchvatu a zkontrolujte, že chyba nastane před tiskem.

... _tutorials/restrict_data_access/multicompany:

Společná bezpečnost více firem
======================

.. viz též:

:ref:`reference/jak_na_to/firma` pro přehled o více společnostech.
všeobecně a :ref:`pravidla pro více společností <jak_na_to/firmy/bezpecnost>
V tomto směru zejména.

Dokumentace obecných pravidel je opět k dispozici na
:ref:`reference/bezpecnost/pravidla`.

.. varování: **Cíl**

V závěru této části by měli mít agenti přístup pouze k nemovitostem
agentury (nebo agentur).

Pro nějaký důvod bychom mohli potřebovat řídit naše nemovitosti
Jako v případě více firem bychom mohli mít velmi samostatné agentury,
franchisingová struktura nebo více značek (možná díky akvizici jiných)
realitní činnosti), které zůstávají právně nebo finančně oddělené od jednoho
další.

Odoo lze použít k řízení více společností v rámci jednoho systému.
Skutečné zpracování je na individuálních modulech: Odoo samo poskytuje nástroje
řešení záležitosti společností závislých polí a pravidel pro více společnosti.
A právě o tom budeme mluvit.

Chceme, aby různé agentury byly „odděleny“ od sebe, s vlastními nemovitostmi
přidružené k určité agentuře a uživatelům (zda jsou to agenti nebo manažeři) pouze
zobrazit vlastnosti spojené s jejich agenturou.

Jak už bylo řečeno, protože je založen na nejednoduchých datech, je pro uživatele snazší
povolit pravidla, než je zpřísňovat. Proto smysl dává
relativně silnější bezpečnostní model.

Pravidla pro více společností jsou prostě záznamová pravidla založená na „company_ids“.
„company_id“ pole:

* „company_ids“ jsou všechny společnosti, ke kterým má aktuální uživatel přístup
* „company_id“ je aktuální společnost (ta, se kterou uživatel pracuje v současné době).
pracujících v/pro).

Pravidla pro více společností budou většinou používat původní, tj. zkontrolovat, jestli záznam
spojené s jednou z firem, ke kterým má uživatel přístup:

... blok kódu::xml

<záznam typu "ir.rule" s ID "hr_appraisal_plan_comp_rule">
<pole název="název">Hodnotící plán pro více společností</pole>
<vlastnost jméno="model_id" odkaz="model_hr_appraisal_plan"/>
<políčko jméno="doména_povinnost">
'|', ('firma_id', '==', False),
('company_id', 'in', company_ids)
]</field>
</záznam>

.. nebezpečí::

Pravidla pro více společností jsou obvykle :ref:`globální <reference/security/rules/global>`.
Pokud ne, hrozí vysoké riziko, že dodatečná pravidla umožní obejít.
multikomoditní pravidla.

..cvičení::

    * Přidejte pole „company_id“ do tabulky „estate.property“, mělo by být povinné
(nechceme bezagentní vlastnosti) a měly by se nastavit na současnou hodnotu.
současná společnost uživatele.
    * Založit novou společnost s novým realitním makléřem v této společnosti.
    * Ředitel by měl být členem obou společností.
    * Starý agent by měl být členem pouze staré společnosti.
    * Vytvořte několik vlastností pro každou společnost (buď použijte výběr společnosti
jako manažer nebo používat agenty. Vypněte výchozího prodejce, aby se předešlo
spouštěním *takovéhoto* pravidla.
    * Všichni agenti vidí všechny společnosti, což není žádoucí, přidejte záznam
pravidlo omezující tento způsob chování.

Pozor: pamatujte na aktualizaci modulu, když změníte jeho model.
data

Viditelnost ≠ bezpečnost
======================

.. varování: **Cíl**

Na konci této části by neměli vidět nastavení makléři.
nabídku nemovitostí aplikace, ale stále by měl být schopen nastavit
druh nemovitosti nebo tagy.

Konkrétní modely Odoo lze přímo spojit s skupinami (nebo společnostmi, nebo
uživatelů. Důležité je zjistit, jestli tento vztah není *bezpečnostní*
nebo funkci *viditelnosti* před použitím:

* Funkce „viditelnost“ znamená, že uživatel může stále přistupovat ke modelu nebo záznamu.
jinak buď jinou částí rozhraní nebo :doc:`výkonem
připojení k serveru pomocí RPC <../reference/external_api>. V takovém případě se může stát, že
Ve webovém rozhraní je v některých kontextech viditelný.
* Funkce „Bezpečnost“ znamená, že uživatel nemůže přistupovat k záznamům, polím nebo operacím.

Například:

* Skupiny na poli „vzorec“ (Python) jsou bezpečnostní funkcí. Uživatelé mimo
Skupina nebude moci pole získat ani o něm vůbec vědět.

Příklad: v akcích serveru „jen uživatelé systému mohou vidět nebo aktualizovat kód Pythonu“
<https://github.com/odoo/odoo/blob/7058e338a980268df1c502b8b2860bdd8be9f727/odoo/addons/base/models/ir_actions.py#L414-L417>.
* Skupiny na prvku zobrazení (v XML) jsou viditelnostním prvkem, uživatelé mimo
Skupina nebude moci vidět prvek nebo jeho obsah v podobě.
jinak s tímto objektem (včetně pole) nebudou moci interagovat.

Příklad: „Jen manažeři mají okamžitý filtr, který jim umožňuje vidět dovolenou svých týmů.“
<https://github.com/odoo/odoo/blob/8e19904bcaff8300803a7b596c02ec45fcf36ae6/addons/hr_holidays/report/hr_leave_reports.xml#L16>.
* Skupiny v nabídkách a akcích jsou viditelné prvky, nabídka nebo akce se
nebude v rozhraní zobrazena, ale nebrání přímé interakci
s podkladovým předmětem.

Příklad: „Jen správci systému mohou vidět nabídku nastavení e-learningu
<https://github.com/odoo/odoo/blob/ff828a3e0c5386dc54e6a46fd71de9272ef3b691/addons/website_slides/views/website_slides_menu_views.xml#L64-L69>.

..cvičení::

Makléři nemohou přidávat typy nemovitostí nebo štítky, ale mohou je vidět.
možnosti z vlastností formuláře, když jej vytváříte.

Nastavení jen přidává do jejich rozhraní šum, takže je nechte vypnuté.
viditelné pro manažery.

Přestože nemá přístup do nabídky typů a tagů vlastností.
agent může stále přistupovat k podkladovým objektům, protože je stále možné vybrat
tagy nebo typ, který lze nastavit na jejich vlastnosti.

... [#app] Aplikace Odoo je skupina souvisejících modulů pokrývajících obchodní
plocha nebo pole, obvykle složená z základního modulu a několika dalších.
rozšíření na základě těchto prvků o další možnosti nebo specifické funkce a vytvořit propojení
do dalších obchodních odvětví.

.. [#appuser] Pro aplikace, které by používali většina nebo všichni zaměstnanci,
uživatelská role „aplikace“ by mohla být zrušena a její
schopnosti, které jsou zaměstnancům přiznané přímo, např. obecně všem
zaměstnanci mohou podávat výdaje nebo si vzít dovolenou.
