==============================
Nepřetržitý proces zlepšování produktu
==============================

.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`
.. |MOs| nahradí za: zkratku: `MOs (Manufacturing Orders)`
.. |BoM| nahradit za: :abbr:`BoM (Seznam materiálů pro výrobu)“
.. |ECO| nahradit za: zkratku: `ECO (Engineering Change Order)`
.. |QCP| nahradit za :: abbr: QCP (kontrolní bod kvality)
.. |PLM| nahradit za: zkratku `PLM (Produktový životní cyklus)`
.. |BoMs| nahradí: :abbr:`BoMs (Seznamy materiálů)`

„Nepřetržitý zlepšování“ je obecný filozofický přístup, který má pomoci jednotlivcům i organizacím
neustále se zlepšovat a vylepšovat svou práci.

Existuje mnoho různých metodologií, které spadají pod křídlo kontinuálního
zlepšení. Patří mezi ně např. Kaizen, šest sigmů a Lean. I když konkrétní kroky
Každá metoda je jiná, jejich cíl zůstává stejný: implementovat proces, který umožňuje zlepšení.
trvalý cíl, nikoli jednorázový úspěch.

Níže uvedené části obsahují podrobnosti o tom, jak lze použít Odoo k implementaci čtyř obecných kroků.
k mnoha z nejpopulárnějších kontinuálních metod zlepšování s odkazy na dokumentaci o
konfigurovat potřebné funkce. Poslední část popisuje, jak konkrétní společnost může nakonfigurovat
Odoo implementace v rámci jejich organizace.

#:ref:`výroba/průběh práce/ci-identifikace“
#:ref:`výroba/práce/ci-suggest
#:ref:`výroba/průběh práce/CI implementace
#:ref:`výroba/průběh práce/CI review“

.. důležité:
Kontinuální zlepšování není jednotná metodika. Většina strategií však obsahuje
mezi čtyřmi až šesti kroky, aby byla implementace provedena správně, je nutné vyvinout systém přizpůsobený
specifické potřeby každé společnosti.

Toto není omezení, ale spíše výhodou, protože metodika je dostatečně flexibilní.
adaptovat téměř na jakýkoliv případ použití. Odoo se tímto způsobem velmi dobře přizpůsobuje této flexibilitě, protože lze
je konfigurován tak, aby vyhovoval téměř jakémukoli pracovnímu postupu.

Proto je důležité si uvědomit, že obsah níže uvedený poskytuje pouze příklady toho, jak Odoo
Mohou být použity, ale měly by se spíše brát jako vodítko než konkrétní bod.
a je třeba ji dodržovat.

... výrobu/průběh práce/ci-identifikovat

Identifikujte problémy
=================

Než se začne s vylepšováním, je nutné určit, kde je potřeba vylepšení.
kde se hraje o identifikaci problémů. Dvě z nejlepších aplikací pro identifikaci problémů s
Produkty nebo procesy jsou Helpdesk a Quality.

Helpdesk
--------

Aplikace Helpdesk je užitečná pro získávání zpětné vazby od mimoorganizačních subjektů, například od
klienty nebo zákazníky. To se dosáhne implementací jednoho (nebo více) z následujících postupů:
:doc:`příjem lístků <../../../services/helpdesk/overview/receiving_tickets>“, včetně e-mailu
aliasů, živých chatech a formulářích na webu.

Takto mohou zákazníci podávat zpětnou vazbu na problémy, které jsou následně vyhodnoceny.
člen týmu helpdesku. V závislosti na výsledku
recenzi může člen týmu rozhodnout o dalším postupu, který zajistí, aby se problém vyřešil. To může
vytvořit „upozornění na kvalitu“ (dokument: doc: quality_alerts).

Kvalita
-------

Aplikace Quality je užitečná pro získávání zpětné vazby zevnitř organizace, například od
zaměstnanci.

Jedním ze způsobů, jak toho dosáhnout, je zřídit kontrolní bod kvality.
<../../kvalita/kvalitní řízení/kontrolní body kvality> (KP), který se používá automaticky
Vytvářet kontroly kvality v pravidelných intervalech, které zaměstnance vyzývají ke kontrole a potvrzení kvality.
produktu.

Pokud se nějaký problém najde, může pak zaměstnanec vytvořit „upozornění na kvalitu“
k oznámení týmu kvality. Kvalitní upozornění mohou také
mělo být vytvořeno nezávisle na QCP, pokud zaměstnanec zjistí problém bez
aby si zkontrolovali, jestli je vše v pořádku. To je skvělý způsob, jak mohou zaměstnanci zákaznického servisu upozornit na kvalitu
tým, který se zabývá problémem, o kterém zákazník informoval prostřednictvím lístku.

... výrobu/průběh práce/ci-suggest:

Navrhněte vylepšení
====================

Jakmile je problém identifikován, následuje navržení řešení.
Stejně jako při identifikaci problémů je aplikace Quality také užitečná pro navrhování zlepšení.
Další možností je aplikace PLM (*Produktový životní cyklus*), která umožňuje tento účel splnit také.

Kvalita
-------

Když vytváříte upozornění na kvalitu (:doc:`<../../quality/quality_management/quality_alerts>`) za účelem
předat kvalitě, tj. :guilabel:`Korektivní opatření“
Karty „Preventivní kroky“ mohou být použity k poskytnutí zpětné vazby o tom, jak lze problém vyřešit.
adresováno.

Karta „Opravná opatření“ se používá k navržení způsobu, jakým lze napravit položky ovlivněné
například „Zajistěte šrouby na sedadle pevněji, aby se nehýbalo“.

Karta Preventivní kroky se používá pro navržení způsobu, jak zabránit problému.
se vyskytují v budoucnu. Například „Nebuďte s utahováním šroubů příliš drsní, jinak se
vykastrovaný.

Kvalitní tým, který hlásku kontroluje, vidí tyto navržené kroky a může je zohlednit.
Při rozhodování, jak se k problému postavit.

PLM
---

Aplikace PLM se používá k řízení životního cyklu produktu od jeho uvedení na trh až po každou
úspěšné verze. Je proto užitečný pro testování nápadů na zlepšení produktu.

Použitím :doc:`změn v projektu <../../plm/manage_changes/engineering_change_orders>`
manažerské týmy mohou vytvářet nové iterace produktů |BoMs| a přidávat nebo odebírat konkrétní komponenty.
nebo operace, pokud je to nutné. Výrobky vytvořené pomocí těchto |BoMů| procházejí procesem kontroly
aby potvrdila účinnost změn.

... výrobu/procesy/CI implementace:

Zavádějte strategie
====================

Realizace strategií zahrnuje implementaci navržených řešení z kroku „Navrhněte vylepšení“.
do akce. Aplikace PLM během této fáze stále zůstává užitečná, protože lze konfigurovat tak, aby
Aktualizace BoM. Aplikace Field Service může také využívat některé společnosti k zlepšení
výrobky, které již byly prodány zákazníkům.

PLM
---

Jakmile změny v BoM projdou správným procesem schvalování, mohou být schváleny a
aktualizovaná |BoM| byla uvedena do provozu. Toho je dosaženo tak, že se konfiguruje jedna ze zkoušek |ECO|
:použít změny provedené na BoM a aktualizovat BoM.
se uvolní pro nové |MOs|.

Produkt BoM může být nadále aktualizován podle potřeby.
Funkce aplikace |PLM| pro správu změn a verzování umožňují snadnou správu
všechny verze daného BoM.

Služba v terénu
-------------

Aplikace PLM je skvělý způsob jak provádět změny v produktové |BoM|. Tyto změny však mají vliv pouze na
výrobky vyrobené pomocí nového |BoM|. Pokud se již výrobku s vadou prodal zákazníkovi
Může být nutné opravit (nebo aktualizovat) tento produkt.

V takovém případě lze aplikaci Field Service použít k plánování :doc:`terénních zásahů.
<../../../services/field_service/creating_tasks>. Tyto zásahy umožňují službě
technici (nebo jiní zaměstnanci) byli posláni na místo zákazníka, aby se pokusili vyřešit problém s
produkt.

... výrobu/práce/CI recenze:

Zpětná kontrola
==============

Zpětná vazba je místem, kde se projevuje „neustálý“ prvek neustálého zlepšování, protože
umožňuje organizacím hodnotit rozhodnutí učiněná v předchozích krocích.
Zpět k začátku procesu, aby se předešlo dalším problémům.
identifikovány a řešeny.

Toto znamená, že by měly být opět používány aplikace Helpdesk a Quality pro přijímání zákaznických
zpětná vazba od zaměstnanců. Další aplikace, která se může hodit na tomto stupni, je aplikace *Připomínky*.

Průzkumy
-------

Po implementaci změn do produktu nebo procesu může být chytré oslovit zákazníky s jejich
zpětnou vazbu přímo, namísto čekání na jejich vlastní iniciativu. To může přinést
světlý zpětný feedback, který by zákazníci jinak možná přehlédli.

Jedním z nejlepších způsobů, jak toho dosáhnout, je prostřednictvím dotazníků:
Aplikace vytváří průzkumy a odesílá je zákazníkům, kteří obdrží aktualizovaný produkt, což zvyšuje
možnost získat relevantní zpětnou vazbu na produkt.

... varování: Příklad pracovního postupu: zlepšení produktu věšák
:class: alert alert-success

Společnost *Wood Hut* je výrobcem kvalitních dřevěných produktů. Snaží se vyrábět pouze kvalitní produkty
v nejvyšší kvalitě a vždy hledají způsoby, jak zlepšit produkty.
prodávat i s procesy, které k jejich vytvoření používají.

Wood Hut používá platformu Odoo k řízení všech prvků výroby, dodání a
procesy spokojenosti zákazníků. Vytvořili vlastní proces zlepšování produktu, který
zahrnuje aplikace Helpdesk, Kvalita, PLM a Výroba.

Jedním z nejoblíbenějších produktů dřevařství Wood Hut je věšák na kabáty. Je vyrobený ze 100% dubového dřeva a
Zákazníci ho popisují jako „stylový a elegantní“. Nicméně nedávné zákaznické zpětné vazby o kabátu
Rack přinesl pozornost kvalitativním problémům, které vyžadují revizi současného způsobu výroby.
procesu.

Proces revize produktu začíná, když tým zákaznického servisu obdrží požadavek v
Aplikace helpdesku od zákaznice, která má problémy s věšákem na kabáty, který si zakoupila.
Abigail Petersonová zjistila, že její věšák na kabáty padne, když je na něm více než pět kabátů.
To je velký problém, protože věšák má dost háčků na šest kabátů.

.... obrázek: kontinuální zlepšování/helpdesk-ticket.png
:synchronizace: střed
:alt:Tiket podpory ohledně problému s věšákem.

Marc, zaměstnanec zákaznického servisu přiřazený k otevření požadavku na technickou podporu, otevírá aplikaci Quality.
Vytváří novou výstrahu kvality. Označuje tým pro kontrolu kvality a přiřazuje Julii Andersonové
zodpovědný za vydání varování.

Julie si přečte upozornění a poradí se svým týmem o nejlepším postupu. Rozhodnou
že je nutné přezkoumat produkt BoM, aby se problém neopakoval.
budoucnost, kterou Julie poznamenává v záložce „Korektivní opatření“ kupodivu v upozornění na kvalitu.

...... obrázek:: kontinuální zlepšování/kvalitní upozornění.png
:synchronizace: střed
:alt:Kvalitní výstraha vytvořená ohledně problému s produktem věšáků.

Pak Julie poslala zprávu produktovému inženýrovi Joemu Kazanovi v chatu kvalitního upozornění, aby se na problém podíval.
jeho pozornost. Joe otevře aplikaci PLM a vytvoří nový ECO s poznámkou o problému s
příborníku, navrhuje změnu v produktu |BoM|.

.. obrázek:: kontinuální_zlepšování/eko.png
:synchronizace: střed
:alt:ECO vytvořené k aktualizaci produktu BoM na věšák.

Joe klikne na tlačítko „Začátek revize“ a poté na tlačítko „Revize“, aby se otevřela
druhou verzí věšáku |BoM|. Tento |BoM| vznikl současně s |ECO| a zůstává
Archivují se, dokud nejsou schváleny.

Joe po nějakém testování zjistí, že přidání kovové podpěry do věšáku na oblečení zesílí
jejími zásahy, takže kabáty mohou viset na ramínku a nepadnout. Aktualizuje také |BoM|
zahrnout podpěrnou tyč jako jeden z komponentů a přidat další operaci, aby se ujistil, že je
je nainstalován během výroby. Nakonec zanechává v chatu
|EKO|, aby o tom informoval svého manažera Jose a mohl ho připravit na recenzi.

.... obrázek:: kontinuální_zlepšování/bom.png
:synchronizace: střed
:alt:Přepínač na oblečení BoM, aktualizovaný pro přidání dalšího komponentu a funkce.

Jose zkoumá změny a potvrzuje, že jsou účinným způsobem řešení problému
s věšákem na kabáty. Přesouvá |ECO| do fáze schválené, což dělá z verze dvě
věšák na kabáty |BoM| aktuální verze.

Nyní každýkrát, když se vytvoří |MO| k výrobě věšáku, je aktualizovaný |BoM| automaticky
Vybraný návrh byl vybrán a společnost Wood Hut začala vyrábět zlepšenou věšákovou stěnu, na základě zpětné vazby od zákazníků se potvrdilo, že
Nová verze problém vyřešila.

Wood Hut využívá platformu Odoo pro implementaci procesu zlepšování produktů od začátku až do konce.
Protože základní prvky tohoto procesu (zpětná vazba od zákazníků, kontrola kvality atd.)
Je neustále funkční a lze ji použít k neustálému aktualizování produktů a procesů.
