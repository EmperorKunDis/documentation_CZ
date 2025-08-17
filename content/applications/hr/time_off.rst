Zobrazit obsah

========
Volno
========

Aplikace Time Off společnosti Odoo slouží jako centrální místo pro všechny informace týkající se dovolené.
Tato aplikace spravuje požadavky, vyváženost, přidělování, schválení a zprávy.

Uživatelé mohou požádat o dovolenou (doc:požadovat dovolenou) a zobrazit přehled svých
žádosti a vyrovnání času volna. Manageři mohou :doc:`vyčlenit čas volna <time_off/allocations>
jednotlivci, týmy nebo celá společnost a schválit požadavky na dovolenou
<volno/spravovat-volno>“.

Podrobné zprávy o čase dovolené lze spustit, aby bylo vidět, jaký je čas dovolené a jaké druhy
používají se volnočasové benefity, lze vytvořit plán na naspoření dovolené.
Můžete nastavit svátky a volno podle času.

.. poznámka::
Pozor, všechny funkce aplikace Time Off mohou vidět pouze uživatelé s určitými přístupovými právy.

Každý uživatel má přístup do sekcí „Můj čas volna“ a „Přehled“ aplikace **Čas volna**. K ostatním
Některé části vyžadují specifické oprávnění.

Chcete-li lépe pochopit, jak ovlivňují aplikaci **Time Off** přístupová práva, podívejte se na
:dokumentu: „zaměstnanci/nový zaměstnanec“ konkrétně část o konfiguraci *práce
Informace*

.. viz též:
:doc:`../obecne/uzivatele/prava_pristupu`

Konfigurace
=============

Aby zaměstnanci mohli čerpat dovolenou a požádat o ni, musí být vytvořeny
musí být nejprve nakonfigurována různá časová volno a pak přidělena zaměstnancům (pokud je alokace povolena).
povinné).

... _volno/druhy-volna:

Druhy volna
--------------

Pro zobrazení aktuálně konfigurovaných typů dovolené přejděte na:
Konfigurace --> Druhy volna“. Volno je zobrazeno v seznamovém pohledu.

Aplikace **Time Off** je dodávána s čtyřmi přednastavenými typy dovolené:
:guilabel:'Neplacené volno', :guilabel:'Kompenzační dny' a :guilabel:'Přesčas'.
Hodiny“. Ty lze upravit podle potřeby firmy nebo použít tak, jak jsou.

Vytvořte si volno
~~~~~~~~~~~~~~~~~~~~

Chcete-li vytvořit nový typ volna, přejděte na: „Aplikace Volno --> Konfigurace --> Volno“.
Druhy volna“. Zde klikněte na tlačítko „Nový“ pro zobrazení prázdného formuláře typu volna.

Do prázdné řádky nahoře na formuláři zadejte název typu dovolené, například
„Dovolená“ nebo „Úmrtí“. Pak zadejte následující informace na formulář.

.. poznámka::
Jedinými **povinnými poli v formuláři pro čas dovolené** jsou jméno a název „Čas dovolené“.
Typ, „Užij si volno“, a „Druh volna“. Kromě toho je zde
:guilabel:`Žádosti o volno“ a „Žádosti o přidělení“ musí být v sekci
konfigurována.

Část požadavků na volno
*************************

Tato sekce určuje, jakým způsobem jsou vyřizovány žádosti o dovolenou pro tento typ dovolené.

- :guilabel:`Schválení“: vyberte, jaký konkrétní druh schválení je pro daný typ dovolené potřeba.
Možnosti jsou:

  - :guilabel:Žádné schválení není potřeba při žádosti o tento typ dovolené.
Žádost o dovolenou je automaticky schválena.
  - „Čas na dovolenou“: pouze uvedený „čas na dovolenou“
<čas dovolené/dovolená - pracovník>, který je nastaven na tomto formuláři v poli :guilabel:`Oznámený čas dovolené“
pole je povinné a musí být schváleno žádost o volno. Tato možnost je výchozí.
  - :guilabel:`Odvolací orgán zaměstnance“: pouze odvolací orgán zaměstnance pro dovolenou, který
je nastaven na záložce „Informace o práci“ v kartě zaměstnance, je
musí žádost o dovolenou schválit.
  - „Odběratel zaměstnance a pracovník odboru dovolené“: Oba zaměstnanci jsou uvedeni v poli „Specifikovaný
Čas dovolené schvaluje zaměstnanec v záložce „Zaměstnanci“ a „Čas dovolené“.
musí schválit žádost o dovolenou.

Část požadavků na přidělení
***************************

Tato sekce určuje, jak jsou požadavky na přidělování času volna pro tento typ volna zpracovávány.

- :guilabel:`Povinné přidělení“: Pokud je dovolená zaměstnancům povinná, vyberte
:guilabel:`Ano“. Pokud je možné požádat o volno bez předchozího přidělení volna,
Vyberte možnost „Bez omezení“. Pokud je vybrána možnost „Bez omezení“, následující volby nejsou k dispozici.
Vyplněný formulář musí obsahovat všechny potřebné údaje.
- Vyberte možnost „Povoleny všechny požadavky na přidělení volných dnů“ pokud zaměstnanec
mohou požádat o více dovolené, než jim bylo přiděleno.

Pokud by zaměstnanci neměli mít možnost požadovat více volna než bylo přiděleno,
Vyberte možnost „Není povoleno“.

...... příklad::
Ten den je zaměstnanci přidělen na tento konkrétní typ dovolené a
:guilabel:`Žádosti o přidělení dalších dnů volna jsou povoleny“ je zapnutá, zaměstnanec chce
dovolená na dvanáct dní. Mohou podat žádost o další dva dny, protože
:guilabel:`Požadavky na přidání dní jsou povoleny“ je zapnuto.

.. důležité::
Je důležité si uvědomit, že žádost o další dovolenou **neznamená**, že vám bude přidělen čas.
V případě, že je žádost o odklad splátek schválena.

- :guilabel:`Schválení“: Vyberte typ schválení, které je pro přidělování této konkrétní položky
pracovní volno.

  - :guilabel:Žádné schválení není potřeba při žádosti o další přidělování
typ volna. Žádost o přidělení je automaticky schválena.
  - „Čas na dovolenou“: pouze uvedený „čas na dovolenou“
<čas dovolené/dovolená - pracovník>, který je nastaven na tomto formuláři v poli :guilabel:`Oznámený čas dovolené“
pole je povinna schválit žádost o přidělení. Tato volba je vybrána výchozím nastavením.
  - :guilabel:`Odvolací orgán zaměstnance“: pouze odvolací orgán zaměstnance pro dovolenou, který
je nastaven na záložce „Informace o práci“ v kartě zaměstnance, je
je povinen schválit žádost o přidělení.
  - „Odběratel zaměstnance a pracovník odboru dovolené“: Oba zaměstnanci jsou uvedeni v poli „Specifikovaný
Čas dovolené schvaluje zaměstnanec v záložce „Zaměstnanci“ a „Čas dovolené“.
musí schválit žádost o přidělení času.


Konfigurační část
*********************

Tato část stanoví všechny ostatní podrobnosti týkající se typu dovolené s výjimkou schválení a
přidělování času na dovolenou. To zahrnuje, jakým způsobem musí být volno přiděleno (hodiny, polodny nebo dny).
zobrazení ostatním uživatelům a jak se doba volna projeví v aplikaci **Mzdová evidence**.

.. _čas volna/časový důstojník_:

- „Oznámený pracovník dovolené“: vyberte uživatele, který je oznamován a odpovědný za
schválení žádostí a přidělování času na dovolenou pro tento konkrétní typ volna.
- :guilabel:`Čas na odpočinek‘: Vyberte formát času, který žádá o dovolenou z rozevírací nabídky.
nabídka. Možnosti jsou:

  - :guilabel:`Den`: pokud je možné žádat o volno jen v celodenních intervalech (8 hodin).
  - :guilabel:Půl denní dovolená: pokud je možné žádat o volno pouze v půldenních intervalech (4 hodiny).
  - :guilabel:`Hodiny“: pokud je možné čerpat dovolenou v hodinových intervalech.

... _`volno/odečíst přesčasové hodiny`:

- :guilabel:'Odečíst přidělené hodiny': Zapněte tuto možnost, pokud se dovolená má započítat i s přidělenými hodinami.
přesčas odpracovaný zaměstnancem.

...... příklad::
Pokud zaměstnanec pracuje o dvě hodiny více za týden a požádá o pět hodin volna,
Žádost by trvala tři hodiny, protože dvě přesčasové hodiny se využívají jako první a odečítá se
z požadavku.

- :guilabel:`Svátek zahrnutý do ceny“:Zapněte tuto možnost, pokud chcete vyloučit svátky ze sazby.
žádost o dovolenou.

...... příklad::
Zaměstnanec v USA požádal o dovolenou na týden od čtvrtka 4. července.
pět dní. Od 4. července je totiž v USA svátek, takže žádost o volno bude
automaticky upraveno na čtyři dny volna místo pěti. To proto, že svátek je
jsou zahrnuty a uživatel nemusí používat své dovolené na státní svátek.

Tato možnost snižuje množství práce pro uživatele a umožňuje jim podat pouze jednu žádost o dovolenou.
celý týden místo dvou samostatných žádostí, jedné pro dny před a druhé pro dny po
v době prázdnin a další pro dny po prázdninách.

- :guilabel:`Povolit připojení podpůrných dokumentů“: Zapněte tuto možnost, aby zaměstnanec mohl
přiložit k žádosti o dovolenou přílohy. To je užitečné v situacích, kdy jsou potřeba dokumenty
například dlouhodobé pracovní neschopnosti.
- :guilabel:`Druh volna“: Vyberte typ volna z nabídky.
:guilabel:`Čas strávený prací“ nebo :guilabel:"Odpočinek“. „Čas strávený prací“ znamená dovolenou
pracovní doba se započítává na jakýkoli typ získávání pracovního času, který zaměstnanec dosahuje.
:guilabel:`Absence“ se nezapočítává do žádného typu účtování.
- :guilabel:`Společnost“: Pokud v databázi vznikne více společností a tento typ dovolené
je pouze pro jednu společnost, vyberte si společnost z roletky. Pokud tento údaj necháte prázdný,
v poli prázdné, pak se na všechny společnosti v databázi vztahuje typ volna „čas“.
databáze více společností.

Negativní část krycího oblouku
********************

Zapněte možnost „Povolit záporný limit“ (guilabel:Allow Negative Cap), pokud zaměstnanci mohou požádat o více volna, než
v současné době mají, což umožňuje negativní zůstatek. Pokud je povoleno, pak se nastaví maximální přeplatek
V tomto poli zadejte maximální počet dní s negativním časem, který je povolený.

.. příklad::
Sarah má nyní tři dny volna typu „Dovolená“. Plánuje cestu.
Požaduje pět dní dovolené.

Typ dovolené „Vacation“ má zapnutou možnost „Negative Cap Allowed“,
:guilabel:`Maximální přeplatkový limit“ je nastaven na pět.

Tyto nastavení umožňují Sarě podat žádost o pět dní dovolené typu „Vacation“.
je schválena, její dovolená bude o 2 dny (–2) v mínusu.

.. obrázek: čas_volna/čas_volna_typ_formulář_nahoře.png
:alt:V horní polovině časového rozvrhu je vyplněn typ dovolené Sick
mimo službu.

Sekce mzdy
***************

Pokud má dovolená typ vytvářet soubor:doc:`../hr/payroll/work_entries` ve **Mzdách**, vyberte
z rolovací nabídky „Druh vstupu do práce“.

Součást „Časové listy“
******************

.. poznámka::
Sekce „Časové listy“ se zobrazí pouze v případě, že uživatel je ve vývojářském režimu. Podrobnější informace naleznete na
:ref:`developer-mode` dokument pro podrobnosti o přístupu do režimu vývojáře.

Když zaměstnanec bere dovolenou a používá také časové listy, Odoo vytvoří záznamy
Aplikace pro evidenci pracovní doby. Tato část definuje, jak se zadávají.

- :guilabel:`Projekt“: Vyberte projekt, pro který se typy časových úseků zobrazují.
- :guilabel:`Úkol“: vyberte úkol, který se v záznamu o pracovní době zobrazuje pro tento typ volna.
Výchozí možnosti jsou: „Čas volna“, „Schůze“ nebo „Školení“.

Seznam možností zobrazení
**********************

- :guilabel:`Barva“: Vyberte barvu, která se má použít v aplikaci Time Off.
- :guilabel:`Obrázek na obalu“: Vyberte ikonu, která se má použít v aplikaci Dashboard v části **Čas volna**.

.. obrázek: time_off/time-off-type-form-bottom.png
:alt:Dolní polovina volného času v typu formuláře s veškerými informacemi o nemoci
mimo službu.

... _volno/získávání plánů:

Plány na nashromáždění
-------------

Čas dovolené se získává prostřednictvím plánu načerpání, což znamená, že za každý stanovený časový úsek
Pracovník pracuje (hodinu, den, týden atd.), získává nebo „získá“ určitou dobu volna.

.. příklad::
Pokud zaměstnanec získává jeden dovolený den za každou pracovní týden, vydělá si 0,2 dovolených dne
za každou hodinu práce. Na konci čtyřicetihodinové pracovní doby by měli mít jednu celou dovolenou
den (8 hodin).

Vytvořit plán účtování
~~~~~~~~~~~~~~~~~~~

Pro vytvoření nového plánu odpočinku přejděte na: „Časový výpočet“ → „Konfigurace“ → „Odpočinek“.
Plány“. Pak klikněte na tlačítko „Nový“, které odhalí prázdnou formu plánu.

Do formuláře zadejte následující informace:

- :guilabel:`Název plánu“: Zadejte název plánu.
- :guilabel:`Například: Připisovaný čas“: Vyberte datum, kdy zaměstnanec začíná připisovat dovolenou.

- :guilabel:`Čas přenesení“: Vyberte, kdy zaměstnanec získal čas již vydělaný. Možnosti
Jsou to:

  - :guilabel:Na začátku roku“: Vyberte tuto možnost, pokud se účetní záznam přepočítává k 1. lednu
příštím roce.
  - :guilabel:`Datum přidělení“: Vyberte tuto možnost, pokud se účetní záznam převádí na další měsíc ihned po datu přidělení.
přidělené zaměstnanci.
  - :guilabel:`Jiné“: Vyberte tuto možnost, pokud se žádná z ostatních dvou možností na vás nevztahuje.
vyberte datum v poli „Přenesení termínu“ pomocí dvou tlačítek s možnostmi.
meny, jedna pro den a druhá pro měsíc.

- Založeno na odpracovaném čase: Zapněte tuto možnost, pokud je získávání dovolené určováno
pracovní hodiny zaměstnance. Dny, které nejsou považovány za odpracované, nepřispívají k
plán přírůstku v Odoo.

...... příklad::
Zaměstnanci je poskytnut volno z plánu, který umožňuje připsat jeden den dovolené
za každých pět pracovních dní. Základ pro naspoření je vázán na odpracovaný čas zaměstnance
:guilabel:`Podle odpracovaného času“ zaškrtnuté, což znamená, že **jen** získávají dovolenou
pracovní dobu za pět dnů v týdnu, nikoliv celý sedmidenní týden.

Společnost zaměstnává pracovníky na plný úvazek s týdenní pracovní dobou 40 hodin. Podle plánu odpracovaných hodin by měli mít čtyři
dovolené za měsíc.

Zaměstnanec si vezme pět dní dovolené pomocí typu časového úseku:ref:`<time_off/time-off-types>`.
nastavit „Druh dovolené“ na „Nepřítomnost“. Protože plán uděluje
dovolená pouze za odpracované dny, ty pět dní se nepočítají do nároku.

Výsledkem je, že zaměstnanec získává pouze tři dny dovolené za měsíc místo čtyř.

- :guilabel:„Mílový přechod“: Toto pole je **pouze** viditelné po dosažení minimálně dvou
:ref:`pravidla <časového účtování/pravidla>“ jsou nastaveny na plánu čerpání dovolené. Tato volba určuje
při změně milníku, pokud se zaměstnanci kvalifikují na změnu v průběhu
době platnosti rozhodnout, zda zaměstnanec změní hodnoty:guilabel:"Hned" nebo
:guilabel:`Po skončení této období“ (po skončení aktuálního výplatního období).
- :guilabel:'Společnost': Toto pole se objevuje pouze v databázi více společností. Pomocí výběrového
menu vyberte společnost, pro kterou se plán účtování vztahuje. Pokud pole ponecháte prázdné, bude k dispozici
pro všechny společnosti.

.. obrázek: time_off/akumulace-plánu-formát.png
:alt:Formulář plánu účtování s vyplněnými poli.

...pracovní dobu a pravidla:

Pravidla
*****

Musí být vytvořeny pravidla, aby zaměstnanci mohli čerpat dovolenou z plánu načerpání.

Pro vytvoření nového pravidla klikněte na tlačítko „Nová metrika“ v šedém panelu „Pravidla“.
sekci a objeví se okno pro vytvoření milníku.

Vyplňte následující pole v formuláři:

... _čas dovolené/naskakování:

- :guilabel:`Nárok na dovolenou“: V této sekci zadejte parametry pro nárok na dovolenou.

Nejprve vyberte buď „Dny“ nebo „Hodiny“ pro přičítání času.
v roletce.

Dále zadejte číselnou hodnotu vybraného parametru, která se připočítává. Formát čísla
je „XX.XX“, takže lze konfigurovat i částečné dny nebo hodiny.

Nakonec vyberte, jak často se hodiny připočítávají pomocí roletky. Výchozí možnosti jsou
:guilabel:`hodinově“, :guilabel:`denně“, :guilabel:`týdně“, :guilabel:`dvakrát za měsíc“
:guilabel:`Měsíčně“, :guilabel:`Dvakrát ročně“ a :guilabel:`Rok co rok“.

Podle zvolené možnosti se mohou objevit další pole. Například pokud
:guilabel:`Dvakrát za měsíc“ je vybráno, objeví se další dva polička pro specifikaci dvou dnů v měsíci.
Každý měsíc se tento milník opakuje.
- :guilabel:`Nashromážděná doba“: Pokud je maximální množství času, který zaměstnanec může nasbírat
tento plán umožní tuto možnost.

Při zapnutí se objeví další dvě pole vedle zaškrtávacího políčka. Druhé pole je
oblasti obydlené buď :guilabel:`Dny` nebo :guilabel:`Hodiny“, které odpovídají výběru v
:ref:`Získávání pracovních dnů <čas na dovolenou/získávat>“.

Do prvního pole zadejte číselný údaj, který určuje maximální dobu, po kterou může být
připisované v uvedených intervalech.
- :guilabel:`Začněte s odpisy“: Zadejte počet a hodnotu časového období, které musí uplynout před
Zaměstnanec začíná získávat dovolenou.

Do prvního pole zadejte číselnou hodnotu, pak do druhého pole nastavte požadovanou dobu.
denní, měsíční nebo roční přírůstek.
- „Přenést“: vyberte, jak bude zacházeno s nevyčerpaným časem dovolené. Možnosti jsou buď:

  - :guilabel:`Žádné. Nastavení odpracovaného času na nulu“: Všechny nevyčerpané dny dovolené jsou ztraceny.
  - :guilabel:`Všechny nevyčerpané dny se přenesou do dalšího roku“: Všechny nevyužité dny se přenášejí do následujícího roku.
kalendářním roce.
  - :guilabel:`Přenést s maximem“: Nespotřebovaný dovolený je přenesena na další kalendářní rok.
ale existuje maximální částka. Pokud je vybrána, objeví se pole „Do“.

Zadejte maximální počet hodin nebo dní, které se mohou převést na
V následujícím roce. Časový úsek, který je předložen, se řídí tím, jakým způsobem :ref:`Pracovník získává
v části „Čas dovolené / nasčítávaný čas“.

Každá dovolená nad tento limit je ztracena.

.. důležité::
Pokud je pole „Násobení“ nastaveno na „Žádné. Celková doba se vrátí na nulu“,
Tato pravidlo přebíjí nastavení „Přenos času“ na plánu.

Pokud společnost vytvoří plán čerpání dovolené, který zaměstnancům umožní čerpat dovolenou:guilabel:Na začátku
„doba nashromáždění“ (tj. začátek roku) a nastavuje „dobu přenosu“ na
*přičítací plán* k datu 1. ledna, který umožňuje převádět nevyčerpanou dovolenou
přenastavit na následující rok.

Poté přidává do plánu odpisů pravidla a každý rok přidá pět dní dovolené.
První den v roce (jedna týdenní dovolená přidělená k 1. lednu).

Pokud je pole „Násobení“ nastaveno na „Žádné. Čas násobku se vrátí na nulu“,
:guilabel:`Vytvořit milník“ pro nevyčerpané dovolené.
Ačkoliv je na formuláři „Výpočet dovolené“ nastaveno „Přenesení času“,
:guilabel:`Na začátku roku“.

Přenesený zůstatek na pravidle má přednost před přeneseným zůstatkem na účetní plán.
formát.

- :guilabel:„Limit pro dosažení cíle“: Zaškrtněte tuto políčko, pokud chcete nastavit maximální dobu na dosažení cíle.
se každým kalendářním rokem. Zadejte celkový maximální počet hodin nebo
:guilabel:`Dny“ v průběhu roku, které zaměstnanec může nasbírat. Předložený časový úsek je určen
podle toho, jak je nastavená část „Naplnění pracovního úvazku zaměstnance“ (Time Off > Accrue).

Pokud je pole „Přenesení“ nastaveno na „Žádné. Nulová doba přenesená“,
:guilabel:`Značka milníku“ pole nevyskytuje.
- :guilabel:`Přenesení platnosti“: Zaškrtněte tuto políčko, pokud chcete nastavit časový limit na dobu, po kterou bude zaměstnanec
musí použít jakýkoli převedený čas dovolené. Nejprve nastavte druhé pole na požadovanou dobu pomocí
buď v rozevíracím seznamu „Dny“ nebo „Měsíce“.

Pak zadejte maximální počet dnů nebo měsíců, které zaměstnanec může využít
jejich převedené dovolené. Po uplynutí této lhůty se nevyužitá převedená dovolená
vypršet.

Pokud je pole „Přenesení“ nastaveno na „Žádné. Nulová doba přenesená“,
:guilabel:`Přenosná platnost“ pole nebude zobrazeno.

Jakmile je formulář vyplněn, klikněte na tlačítko „Uložit a zavřít“ pro uložení formuláře „Vytvořit milník“.
formulář a zavřít okno nebo kliknout na tlačítko „Uložit a nový“ pro uložení formuláře a vytvoření dalšího.
milník. Přidejte kolik milníků chcete.

.. příklad::
Tento krok je nastaven tak, že zaměstnanec za rok získá pět dní. Tyto dny začínají platit
každý rok, k 1. lednu.

Zaměstnanec nikdy nemůže mít více než 120 dní dovolené s touto účetní metodou. Kdykoliv
Pokud má zaměstnanec naspořeno 120 dní dovolené, přestane mu další čas naskakovat.

Dále mohou převést až 100 dní dovolené na další rok a mají tři
měsíce, aby mohl využít převedený čas.

Zaměstnanec nemůže přenést do dalšího roku více než 120 dní zúčtovaného času.
jakákoliv dovolená, která přesahuje celkový počet 120 dní.

.... obrázek:: time_off/milestone.png
:alt: Formulář s výchozími hodnotami všech políček.

.. _volno/svátky:

Svátky
---------------

Odvětví je různé v každé zemi a dokonce i ve městě. Proto neexistují žádné svátky
přednastavené v Odoo. Pro sledování veřejných nebo státních svátků a poskytování dalších dní volna
svátky zaměstnancům, konfigurace veřejných svátků v Odoo.

Je důležité nastavit veřejné svátky v Odoo, aby zaměstnanci věděli, které dny mají
a nežádejte o volno na dny, které jsou již vyhlášené jako svátky (nepracovní).
dní).

Dále jsou ve všech aplikacích zobrazeny i všechny svátky nastavené v aplikaci Time Off.
, které používají pracovní plány, například kalendář, plánování nebo výroba a další.

Odoo je integrováno s dalšími aplikacemi, které používají pracovní plány, a proto se považuje za nejlepší praxi
aby byly nakonfigurovány všechny veřejné svátky.

Vytvořit svátky
~~~~~~~~~~~~~~~~~~~~~~

Pro vytvoření veřejného svátku přejděte na: „Časový rozvrh aplikace“ --> Konfigurace --> Veřejný
Svátek. Všechny aktuálně nastavené svátky se zobrazují v výchozím pohledu na seznam.

Klikněte na tlačítko „Nový“ a nová položka se objeví na konci seznamu.

Do nové řádky zadejte následující informace:

- :label_field:Název: Zadejte název svátku.
- :label:Společnost: Pokud je databáze více společností, aktuální společnost tento údaj vyplní.
Je to výchozí hodnota, kterou nelze upravit.

.. poznámka::
Pole „Společnost“ je skryté v základním nastavení. Chcete-li zobrazit tento prvek, klikněte na
:ikona: „Nastavení“ (nastavení) v pravém horním rohu
v seznamu na konci sloupců a aktivujte výběr „Společnost“
z nabídky, která se objeví.

- :guilabel:`Datum začátku“: Vyberte datum a čas, kdy se bude svátek
Poté klikněte na ikonu „fa-check“ a potvrďte. Výchozí nastavení tohoto pole je
současným datem. Čas spuštění je nastaven podle času spuštění společnosti (podle
pracovní rozvrh (viz. :ref:`pracovní rozvrhy <plat/casove-rozvahy>`). Pokud je uživatelův počítač nastaven na
V případě jiného časového pásma se začátek akce přizpůsobí podle časového pásma společnosti.
- :guilabel:`Konec datumu“: Pomocí kalendáře vyberte datum a čas, kdy skončí dovolená.
Poté klikněte na ikonu „fa-check“ a potvrďte. Výchozí nastavení tohoto pole je „Apply“.
aktuální datum a čas je nastaven na konec pracovní doby společnosti (podle :ref:`pracovního
kalendáře (<plat/směny>). Pokud je uživatelův počítač nastavený na jinou časovou zónu,
Čas startu se upraví podle časového pásma společnosti.

...... příklad::
Společnost sídlící v San Franciscu pracuje od 9:00 do 18:00 s osmihodinovou pracovní dobou
a hodinovou přestávku na oběd.

Pro uživatele v New Yorku s nastaveným časovým pásmem pro východní standardní čas je vytvořený
Veřejné svátky začínají v 12:00 hodin a končí ve 21:00 hodin, což zahrnuje tříhodinový čas
rozdíl v časovém pásmu.

Stejně tak uživatel v Los Angeles s nastaveným časovým pásmem Pacifické standardní časové zóny
Veřejné svátky jsou v době od 9:00 do 18:00 hodin.

- :guilabel:„Směny“: Pokud má dovolená platit jen pro zaměstnance s určitým rozvrhem
zaměstnání, vyberte pracovní dobu z roletky. Pokud je pole prázdné, bude se počítat s volnem
Platí pro všechny zaměstnance.
- „Zadání práce“: Pokud používáte aplikaci „Mzdy“, tento položka definuje jaký typ práce je zaznamenán.
v seznamu položek pro výplatu (<payroll/work-entries>). Vyberte typ pracovní položky z
rozbalovací nabídka.

.. obrázek:time_off/vacation.png
:alt: Seznam svátků v konfiguračním menu.

Povinné dny
--------------

Některé společnosti mají speciální dny, kdy jsou zaměstnanci určitých oddělení nebo celého personálu povinni
přítomna a dovolená není povolena na těchto konkrétních dnech.

Tento typ dnů se v Odoo nazývá „povinné dny“. Tyto mohou být nastaveny tak, aby platily pro celou společnost.
nebo pro konkrétní oddělení či společnost. Když je nastaveno, zaměstnanci v daném oddělení nebo společnosti nebudou
podat žádost o dovolenou na tyto povinné dny.

Vytvořit povinné dny
~~~~~~~~~~~~~~~~~~~~~

V Odoo jsou povinné dny nastaveny výchozím nastavením. Chcete-li vytvořit povinný den, přejděte na
:menuaplikace-->Nastavení-->Povinné dny.

Klikněte na tlačítko „Nový“ v pravém horním rohu a do seznamu se zobrazí prázdná řádka.

Do nové řádky zadejte následující informace:

- :guilabel:`Název“: Zadejte název povinného dne.
- :guilabel:`Společnost“: Pokud je v databázi více společností viditelné, aktuální
Společnost tento údaj vyplňuje automaticky. Vyberte si firmu z nabídky.
Proč je povinný den právě pro něj.
- :guilabel:„Oddělení“: Tato sloupec je skrytý výchozím nastavením. Nejprve klikněte na
:ikona: „Nastavení“ (Další možnosti) v pravém horním rohu vedle
:guilabel:`Barva“ a pak zaškrtněte políčko vedle „Oddělení“, abyste zjistili, že
sloupek.

Dále vyberte požadované oddělení z roletky. Může jich být více.
a není omezen počet oddělení, která mohou být přidána.

Pokud je pole nevyplněno, povinný den se vztahuje na celou společnost.
- :guilabel:`Datum zahájení“: Vyberte datum, kdy začíná povinný den pomocí kalendářového vyhledávání.
- :guilabel:`Datum ukončení“: Vyberte datum konce povinného dne pomocí kalendáře.
Vytvoření jednoho povinného dne by mělo mít stejný konec jako začátek.
- :guilabel:`Barva“: Pokud chcete, vyberte si barvu z nabízených možností. Pokud žádnou barvu nevyberete
požadovanou barvu vyberte možnost „Žádná barva“, která je reprezentována bílým čtvercem s . Vybraná barva se objeví
na hlavním panelu aplikace Time Off, v kalendáři i v legendě.

.. obrázek:: time_off/mandatory.png
:alt:Sekce Povinné dny s třemi konfigurovanými dny.

Přehled
========

Pro zobrazení barevně označeného rozvrhu volna uživatele a/nebo týmu, který spravuje, přejděte na
„Čas na odpočinek“ aplikace --> Přehled. Tato nabídka zobrazuje kalendář s výchozím filtrem
„Moje tým“, v čtvrtletním pohledu.

Pro změnu zobrazovaného časového období klikněte na ikonu „kalendář“ :guilabel: (časové období)
tlačítko pro zobrazení rozbalovací nabídky. Pak vyberte buď „Dnes“, „Tento týden“ nebo
„Tento měsíc“, „Tento rok“ nebo vlastní časový úsek, abyste kalendář zobrazili
Takové pohledy.

Pro navigaci vpřed nebo vzad v čase, ve vybraném kroku (:guilabel:'Měsíc',
Týden, atd.) klikněte na ikonu „Oi-arrow-left“ (levá šipka).
:icona: „pravý směr“ (směr vpravo) tlačítka pro pohyb buď dopředu nebo dozadu.
určité množství času. Například pokud je vybrána hodnota :guilabel:`Month`, pak se šipky upraví pohled
o jeden měsíc.

Pro návrat na pohled obsahující aktuální den klikněte na ikonu „fa-crosshairs“ (Zaměření).
Tlačítko „Dnes“ v jakémkoliv okamžiku.

Členové týmu jsou uvedeni abecedně na jednotlivých řádcích a jejich žádaná dovolená je bez ohledu
(platná nebo k schválení) je viditelná v kalendáři.

Každý zaměstnanec je barevně označen. Barva zaměstnance je vybrána náhodně a neodpovídá
typ dovolené, kterou si požádali.

Stav dovolené je zobrazen barvou podrobností o žádosti, buď černou
(*ověřené*) nebo pruhované (*k schválení*).

Počet dní nebo hodin, které žádáte, je uveden na požadavku (pokud je dostatek místa).

Na spodní části kalendáře je v řádku „Celkem“ graf, který ukazuje, kolik lidí
, který je v daný den předpokládán. Číslo za každou jednotlivou čárkou znázorňuje počet
zaměstnanci, kteří jsou v těchto dnech na pracovní cestě.

Klikněte na záznam dovolené, abyste zobrazili podrobnosti pro konkrétní záznam dovolené. Celkový počet
Jednotlivé hodiny nebo dny jsou uvedeny spolu s časem začátku a konce dovolené.
Vyžádejte si volno v režimu dialogového okna kliknutím na tlačítko „Zobrazit“.

.. obrázek: time_off/overview.png
:alt: Přehled týmu uživatele s požadavky na dovolenou.

.. _volno/pracovní doba:

Reportáž
=========

Funkce hlášení umožňuje uživatelům zobrazit dovolenou pro svůj tým buď podle zaměstnance nebo typu.
volno. Tento nástroj umožňuje uživatelům vidět, kteří zaměstnanci jsou na dovolené, jak dlouho
jaké jsou údaje o převzetí a jaké druhy časových úseků se používají.

Každý zpráva může být přidán do tabulky, když buď
vizuálním pohledu na graf nebo v pohledu „Pivot“ (viz. ikona :icon:`oi-view-pivot`) a přes „Vložit do
Tlačítko „Spreadsheet“ v horním levém rohu zprávy.

.. poznámka::
Pokud je aplikace Dokumenty nainstalována, objeví se možnost přidat zprávu do tabulky.
Nikoli. Zprávu lze přidat na Dashboard.

Podle zaměstnance
-----------

Pro zobrazení seznamu žádostí o dovolenou zaměstnanců přejděte na: „Aplikace Dovolená --> Zprávy
--> zaměstnancem.

Výchozí zpráva obsahuje aktuální roční údaje ve formě seznamu, který zobrazuje všechny zaměstnance
abecedním pořadí. Každá řádka zaměstnance je sbalena výchozím nastavením. Chcete-li řádku rozbalit, klikněte na ni
na lince.

Výhled se rozšiřuje a má časové požadavky na dovolenou organizované podle typu dovolené. Klikněte na jakékoli místo v čase
přidat další řádek typu a zobrazit všechny individuální požadavky na dovolenou, které spadají pod tento typ.

Zobrazená informace zahrnuje jméno zaměstnance a počet hodin.
Požadované dny volna, :guilabel:`Datum začátku“, :guilabel:`Datum ukončení“, :guilabel:`Stav“ a
:label_guid:`Popis“.

.. obrázek: time_off/employee-report.png
:alt:Zpráva o dovolené zobrazená každým zaměstnancem v seznamovém pohledu.

Hlášení lze zobrazit i jinak. Klikněte na příslušnou možnost tlačítka
v pravém horním rohu stránky, abyste mohli zobrazit data v konkrétním pohledu. Různé možnosti jsou
:ikonka:oi-view-list:guilabel:(Seznam), nebo výchozí pohled, ikona:fa-area-chart:guilabel:(Graf)
Viditelnost tabulek pomocí zobrazení „Pivot“ nebo „Kalendář“.

Když je vybrána nějaká položka, objeví se další možnosti pro tuto konkrétní volbu.
podrobné informace o zprávách a jejich různých možnostech najdete v :doc:`reportingu
Dokumentace k „Essentials/Reporting“.

Dle typu
-------

Pro zobrazení grafu všech dovolených, seřazených podle typu dovolené, přejděte na:
aplikace --> Hlášení ---> podle typu“. Toto zobrazuje všechny žádosti o volno v grafu svislých čar.

Přejděte nad čárou, abyste viděli dobu trvání daného typu volna podle :guilabel:`Duration (Days)`.

.. obrázek:: time_off/bar-chart.png
:alt:Různé druhy dovolených a počet dní požadovaný v grafu sloupcovém. Detaily jsou
zvýrazněné červeným rámečkem.

Klikněte na čáru, abyste se dostali k podrobnému výpisu všech požadavků na dovolenou pro daný druh volna.

Každá žádost je uvedena s následujícími informacemi: „Zaměstnanec“,
:guilabel:`Počet dní“, :guilabel:`Typ požadavku“, :guilabel:`Datum zahájení“, :guilabel:`Datum ukončení“
:guilabel:`Stav“ a „Popis“.

Hlášení lze zobrazit i jinak. Klikněte na příslušnou možnost tlačítka
v pravém horním rohu stránky, abyste mohli zobrazit data takto. Různé možnosti jsou
:icon:`fa-area-chart` :guilabel:`(Graf)` (výchozí pohled), :icon:`oi-view-list`
:guilabel:`(Seznam)“, nebo :icon:`oi-view-pivot“ :guilabel:`(Sloupcový graf)“.

Když je vybrána nějaká položka, objeví se další možnosti pro tuto konkrétní volbu.
podrobné informace o zprávách a jejich různých možnostech najdete v :doc:`reporting
Dokumentace k „Essentials/Reporting“.

Rovnováha
-------

Pro zobrazení tabulky všech časových rozvrhů v průběhu času, uspořádaných podle typu volna, pak dále
Kolik dní a hodin ještě zbývá do odjezdu, zjistíte kliknutím na
:menu:„Čas volna“ --> „Zprávy“ --> „Zůstatek“.

Tato tabulka ukazuje všechny časy volna v základním přehledu. Zaměstnanci vyplňují řádky, zatímco
různé typy volna a jejich vyrovnání se objevují v sloupcích.

.. obrázek:: time_off/balance.png
:alt:Různé časové účty v tabulce sestupně.

.. viz též:
   - :doc:`time_off/allocations`
   - :doc:`odpocinek/žádost o odpočinek
   - :doc:`time_off/my_time`
   - :doc:`pracovní doba a řízení“

..toctree::


time_off/alokace
time_off/request_time_off
time_off/můj čas
time_off/management
