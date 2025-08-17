==============
Gitové pokyny
==============

Nastavte svůj git
------------------

Podle zkušeností předků a ústní tradice se následující věci dějí takto.
cestou, jak udělat své commity užitečnějšími:

- Ujistěte se, že definujete oba uživatelské e-mail a jméno v konfiguraci vašeho lokálního git

...... kódový blok:: text

git config --global <var> <value>

- Ujistěte se, že do svého profilu na GitHubu vložíte celé jméno. Prosím, cítit se jako hvězda
a přidejte svůj tým, avatar, oblíbenou citát a tak dále :-)

Struktura zprávy o přijetí
------------------------

Zpráva o zavázání obsahuje čtyři části: značku, modul, krátký popis a plný
popis. Snažte se dodržovat preferovanou strukturu pro zprávy o přispění

... blok kódu:: text

modul [TAG]: popište svou změnu v krátké větě (ideálně méně než 50 znaků).

Dlouhá verze popisu změny včetně důvodu pro tuto změnu
nebo stručný popis novinky.

Prosím, věnujte mnohem více času tomu, PROČ se změna dělá.
než co se mění. To je obvykle snadno pochopitelné tím, že člověk danou věc skutečně přečte.
rozdíl by měl být vysvětlován pouze tehdy, pokud existují technické volby
nebo rozhodnutí, které je spojeno s tímto rozhodnutím. V takovém případě vysvětlete proč byl k tomuto rozhodnutí přistoupen.

Za závěr vzkazu uveďte odkazy na úkoly nebo chyby s čísly, PR a dalšími.
Tikety OPW v následujícím formátu:
task-123 (související s úkolem)
Opravuje chybu číslo 123 (uzavření příbuzné chyby na GitHubu).
Zavírá #123 (zavření příbuzného PR na GitHubu)
opw-123 (související s lístkem)

Název štítku a modulu
-------------------

Tagy se používají k předponě vašeho příspěvku. Měly by být jedním z následujících

- **[FIX]** pro opravy chyb: většinou používané ve stabilní verzi, ale také platné, pokud se jedná o aktuální verzi.
opravují nedávný bug ve vývojové verzi.
- **[REF]** pro refaktoring: když je funkce zásadně přepsána
- **[PŘIDAT]** pro přidávání nových modulů.
- **[REM]** pro odstranění zdrojů: odstraňování mrtvého kódu, odstraňování pohledů
odstranění modulů, ...
- **[REV]** pro obnovení závazných změn: pokud se nějaký závazný návrh nehodí nebo způsobuje problémy
obrácení je provedeno pomocí tohoto značky.
- **[MOV]** pro přesun souborů: použijte příkaz git move a nezměňte obsah přesunutého souboru
jinak by mohl GIT ztratit stopu a historii souboru; používá se také při přesunu
kód z jednoho souboru do druhého.
- **[RELEASE]** pro release komitů: nové hlavní nebo vedlejší stabilní verze;
- **[IMG]** pro vylepšení: většina změn, které byly provedeny ve vývojové verzi
jsou to nezávislé vylepšení, která jsou postupně přidávána.
- **[SRAŽIT]** pro sražené změny: používá se při předchozím přenosu oprav, ale také
hlavní závazek pro funkci, která obsahuje několik oddělených závazků.
- *[CLA]* pro podepsání licence Odoo Individual Contributor.
- **[I18N]** pro změny v překladových souborech.
- **[VYK]** pro opravy výkonu.

Po značce následuje upravený název modulu. Využijte technický název jako funkční
název se může časem změnit. Pokud je upraveno více modulů, uveďte je nebo použijte
různé to říkat moduly je přes. Pokud není skutečně potřeba nebo snadné se vyhnout
změnit kód v několika modulích ve stejném příspěvku. Chápání modulu
historie se může stát komplikovanou.

Hlavička zprávy o přijetí
---------------------

Po názvu štítku a modulu je hlavička s významným zprávou o přispění.
jsou srozumitelné a obsahují důvod změny. Nepoužívejte jednotlivá slova
například „oprava chyby“ nebo „vylepšení“. Snažte se omezit délku hlavičky na zhruba 50 znaků.
pro lepší čitelnost.

Hlavička zprávy o přijetí by měla tvořit platný větný celek, pokud se k sobě připojí
„Pokud se tento závazek uplatní, bude obsahovat následující hlavičku.“ Například „[IMP] základ: zabránit tomu, aby
„Uživatelé archivu spojení s aktivními partnery“ je správné, protože tvoří platnou větu.
„Pokud se tento závazek uplatní, bude zabráněno archivování…“

Popis zprávy o zavázání
-------------------------------

V popisu zprávy uveďte část kódu, kterou ovlivňují vaše změny.
(název modulu, knihovna, přesahující objekt, ...), popis změn.

Nejdříve vysvětlete PROČ upravujete kód. Co je důležité, pokud se někdo vrátí
Vaše závazek vydrží asi 4 desetiletí (nebo tři dny), a proto jste to udělali. Je
účel změny.

Co jste udělali, najdete v samotném commitu. Pokud byly nějaké technické volby
Je vhodné vysvětlit ji i ve zprávě o přijetí poznámky, kde uveďte proč.
Pro vývojáře Odoo R&D „PO tým mi řekl, abych to udělal“ není platným důvodem, jak se podíváte.

Vyhněte se zavádění změn, které ovlivňují více modulů najednou. Zkuste je rozdělit
do různých commitů, kde jsou ovlivněné moduly odlišné. Bude to užitečné
Pokud chceme vrátit změny v daném modulu samostatně.

Nebojte se být trochu obsáhlí. Většina lidí uvidí jen váš komitový příkaz
a soudit vše, co jste ve svém životě udělali, pouze na základě těchto pár vět.
Žádný tlak vůbec.

**Vy trávíte několik hodin, dní nebo týdnů prací na významných funkcionalitách.
čas na uklidnění a napsání jasných a srozumitelných závazků.**

Pokud jste vývojářem pro výzkum a vývoj v Odoo, měl by být důvod vaší práce.
, které jsou v současné době ve vývoji. Kompletní specifikace tvoří jádro závazku.
**Pokud pracujete na úkolu, který nemá cíl ani specifikaci, prosím
Zvažte, zda je nechat jasnější před pokračováním.

Nakonec zde jsou příklady správných zpráv o přijetí změn:

... blok kódu:: text

[REF] modely: použijte `parent_path` k implementaci `parent_store`.

Toto nahrazuje předchozí modifikovaný stromový průchod (MPTT).
pole „předek vlevo“ a „předek vpravo“ [...]

[Fix] Účet: Odstranit frenglish

  [...]

Zavírá #22793
Oprava chyby číslo 22769

[Oprava] Webová stránka: Odstraňte nevyužitý upozornění div a opravte vzhled tlačítka skupiny

Bootstrapova CSS závisí na elementu input-group-btn
prvním nebo posledním dítětem svého rodiče.
Nebylo tomu tak, protože neviditelná
a zbytečná výstraha.

.. poznámka: Využijte dlouhý popis k vysvětlení *proč*, nikoli
*co* a *jak* lze vidět v rozdílu.
