Zobrazit obsah

========
Plánování
========

S Odoo Planning můžete plánovat rozvrh svého týmu a spravovat směny a zdroje.

Řízení plánování týmu přináší specifické požadavky, které se mohou lišit v závislosti na
potřeby vašeho podnikání. Následující koncepty byly zavedeny v plánování Odoo, aby tyto potřeby splnily:

Příkazy jsou přidělovány zdrojům, které mohou být buď lidé (viz plánování zaměstnanců).
(zaměstnanci) nebo :ref:`materiál <plánování/materiály>“ (např. zařízení). Zdroje jsou přiřazeny
:ref:`role <plánování/role>“, který umožňuje organizovat práci v týmu.

Jakmile je hotová počáteční konfigurace, může být provedeno plánování směn.
ručně nebo automaticky pomocí funkce „Auto Plan“ (viz plánování/otevřené směny).

Propojení aplikací Plánování a Prodej umožňuje propojit prodané služby s rolí.
přesuny v plánování. Dále je možné integraci s projektem :doc:`<project>`, díky čemuž lze přidělit
směruje zdroje a čas na konkrétní projekty.

.. viz též:
„Návody k Odoo: Plánování <https://www.odoo.com/slides/planning-60>“

... plánování/konfigurace:

Konfigurace
=============

.. plánování rolí:

Role
-----

K definování rolí, které vaše zdroje plní (např. kuchař, barman, číšník), přejděte na
Vyberte „Plánování“ -> „Konfigurace“ -> „Role“, pak klikněte na „Nový“ a vyplňte
Vyberte „Jméno“ (např. asistentka, recepční, manažer) a poté vyberte „Zdroje“.
která tuto roli zastane. Zdroje mohou být buď zaměstnanci, nebo
:ref:`Materiály <plánování/materiály>“.

.. poznámka::
   - Pokud je aplikace Prodej nainstalována ve vaší databázi, objeví se pole „Služby“.
umožňuje vám určit, které role jsou potřebné k provádění služby, takže směny budou
předána správnému člověku.
   - Při použití funkce Auto Plan se vychází z rolí.

Vlastnosti a role objektů
~~~~~~~~~~~~~~~~~~~~~~~~~

Pole vlastností umožňují přidat do formulářů aplikací Odoo vlastní pole.
Plánování zahrnuje možnost přidání vlastností majetku, které jsou spojeny s rolí, do směn.

Pro vytvoření pole vlastností přepněte na seznamový pohled z jakéhokoli kalendáře. Potom klikněte
Vyberte požadovaný přesun a v poli „Rol“ vyplňte pole
pak klikněte na ikonu ozubeného kolečka a vyberte možnost „Přidat vlastnosti“.
:doc:`Nastavte nový prvek podle svých potřeb.

.. obrázek: plánování/vlastnosti.png
:alt: Vytvoření nového pole vlastnosti v plánování.

Součástí vlastnostního pole je vztah k roli a je zahrnuta do přesunového tvaru všech provedených směn.
tímto postem.

Příklad:
Některé z použití vlastností pole role zahrnují:

   - Akreditace: pro role, které vyžadují konkrétní povolení (např. řidičský průkaz)
   - **Lokalita**: v podnicích, které působí na více místech (např. obchody nebo restaurace)
   - Jazyk: v multilingvním prostředí (např. poradenská společnost)

.. plánování zaměstnanců:

Zaměstnanci
---------

Do plánování mohou být zapojeni všichni zaměstnanci a přidělena směna.

Pro přizpůsobení nastavení plánování zaměstnance přejděte na: „Plánování“ - „Nastavení“ -
Zaměstnanci“ a vyberte zaměstnance pro kterého chcete upravit nastavení. Poté přejděte na
:guilabel:`Informace o práci“ záložka.

.. obrázek: plánování/zaměstnanci.png
:alt: Profil zaměstnance a záložka pracovní informace.

..tip:
Stejné můžete udělat i z aplikace **Zaměstnanci**, která je nainstalována výchozí verzí spolu s
Plánování.

Dvě části záložky „Informace o práci“ zaměstnance mají vliv na plánování:
„Rozvrh“ (konkrétně pole „Směny“) a „Zaměstnání“.

.. plánování a pracovní doby:

Pracovní doba
~~~~~~~~~~~~~

Při výpočtu času přiděleného na práci jsou zohledněny pracovní hodiny.
Procento se počítá pro :ref:`směny <plánování/šablony>“. Pokud je nastavené :guilabel:`Časová dotace`,
položka je nevyplněná, zaměstnanec se považuje za pracujícího na flexibilní úvazek.

Pro vytvoření individuálního záznamu „Práce na plný úvazek“ apod. pro zaměstnance pracujícího zkrácenou pracovní dobu klikněte
„Hledat více…“, pak „Nový“.

.. poznámka::
V plánování mohou být ovlivněny pracovní hodiny a přidělený čas.
**Mzdy**, pokud je smlouva zaměstnance nastavena tak, aby generovala pracovní vstupy na základě směn.

.. viz též:
:ref:`Dokumentace o pracovních směnách <payroll/working-times>`

Role plánování
~~~~~~~~~~~~~~

Jakmile má zaměstnanec jednu nebo více :guilabel:„Role“:

- Při vytváření směny pro tento zaměstnanec se použijí pouze šablony směn z vybraných rolí.
V poli se zobrazí pole.
- Když je zveřejněn rozpis směn, zaměstnanec je pouze upozorněn na volné směny pro role, které jsou
přiděleny jim.
- Při automatickém přidělování otevřených směn nebo plánování prodejních objednávek je zaměstnanec přiřazován pouze k směnám.
přidělené role.

Dále, pokud je definována výchozí role:

- Při vytváření směny pro zaměstnance je automaticky vybrána výchozí role.
- Tato role má přednost před ostatními rolí zaměstnance při automatickém přidělování volných směn.
nebo plánování objednávek.

.. poznámka::
Pokud jsou pole pro plánování rolí prázdná, nejsou v šablonách směn žádné omezení.
otevřené směny sdílené s zaměstnancem. Avšak není možné využít funkci **Automatické plánování**
pro zaměstnance bez rolí.

.._plánování/materiálu:

Materiály
---------

**Materiály** jsou zdroje, které lze přiřadit směnám a pracovním hodinám, ale nejsou zaměstnanci.
Například stavební firma může použít materiál k vytvoření směn pro sdílené stroje.
např. jeřáby, vysokozdvižné vozíky)

Stejně jako zaměstnanci mohou být materiály přiřazeny rolím a pracovní době.

.._Šablony/Plánování:

Přesun vzorců
---------------

Pro vytvoření šablony přepínání klikněte na tlačítko „Nový“ v rozvrhu, pak vyplňte
:podrobnosti o směně <plánování/vytvořit-směnu>. Chcete-li uložit směnu,
šablona, zaškrtnout: guilabel:"Uložit jako šablonu".

.. obrázek: plánování/ukládání šablony.png
:alt:Přepněte do režimu s volbou „Uložit šablonu“.

Alternativně můžete jít do: „Plánování“ - „Konfigurace“ - „Šablony směn“,
Klikněte na „Nový“. Vyplňte pole „Čas začátku“ a „Délka směny“.
Poté se vypočítá „Čas konce směny“ na základě hodin práce, přičemž
pracovní dobu i přestávky.

Příklad:
Pracovní doba zaměstnance je pondělí až pátek od 8.00 do 17.00 hodin s přestávkou na oběd mezi 12.00 a 13.00
hodin.

   - Vytvoření šablony směny s časem zahájení 9 hodin a trvání 8 hodin bude mít za následek
konečnou hodinou páté hodiny odpoledne na základě pracovní doby a jednohodinové přestávky.
   - Vytvoření šablony směny s časem zahájení 10 hodin a trvání 10 hodin bude mít za následek
konec hodiny 10.00 následujícího dne, protože společnost má zavřeno v 17.00
pracovní doba.

Dále lze pro každý vzor směny také nakonfigurovat:

- :guilabel:`Role“: propojit přesun s konkrétní rolí.
- :guilabel:`Projekt“: sledování směn, které jsou určeny k práci na projektu.

.. plánování směn:

Plánování směn
===============

Při otevření aplikace Plánování uživatelé vidí svůj vlastní rozvrh. Uživatelům s rolí administrátorů se zobrazí
„Časový rozvrh podle zdroje“, „Role“, „Projekt“ nebo „Obchodní objednávka“.
stejně jako menu pro nastavení a reporty.

.. poznámka::
V Ganttově pohledu je zobrazena harmonogram, který umožňuje upravit (přetáhnout)
změnit velikost, rozdělit a duplikovat posuny bez otevření.

.. obrázek: plán/rozpis.png
:alt: Schéma zobrazující různé vizuální prvky.

Pro označení změn v rozvrhu jsou používány následující vizuální prvky:

- **V plné barvě**: přesuny, které jsou naplánované a zveřejněné.
- **Diagonální pruhy**: přesuny, které jsou naplánované, ale ještě nebyly zveřejněny.
- Šedé pozadí: zaměstnanci na dovolené.
- **Pokročilá lišta**: aktuálně probíhající směny s přidruženými časovými listinami.
- Šedé přesuny: při kopírování směn jsou zobrazeny ve své plné barvě, zatímco
Původní směny jsou dočasně zšednuty. Barva se vrátí na plnou barvu nebo
diagonální pruhy na další aktualizaci stránky nebo odstraněním filtru.

... plánování/vytvoření směny:

Vytvořit posun
--------------

Pro vytvoření posunutí přejděte do jakéhokoliv rozvrhu, pak klikněte na „New“. V otevřeném okně zadejte
Vyplňte následující údaje:

- Šablony: Pokud existuje v databázi jedna nebo více šablon, jsou
zobrazené v horní části okna přesunutého okna. Jakmile je vybráno, šablona předvyplní
přizpůsobit se.
- :guilabel:`Zdroj“: Zdroje mohou být buď zaměstnanci nebo materiály. Pokud je pole prázdné,
Přesun je považován za :ref:`otevřený přesun <plánování/otevřené přesuny>`.
- :guilabel:`Pozice“: Vyberte roli, kterou bude přiřazený zdroj vykonávat. Toto pole je
používá se při :ref:`automatickém plánování <planning/open-shifts>`, jakmile si vyberete roli, tak
V horní části okna se zobrazí šablony spojené s ním.
- Pokud je aplikace Project nainstalována ve vaší databázi, tento prvek umožňuje
Propojení projektu s přesunem je k dispozici, takže můžete naplánovat a sledovat přesuny, které jsou určeny
pracovat na vybraném projektu.
- :guilabel:„Dodací položka“: Pokud je aplikace „Prodej“ nainstalována ve vaší databázi, tento prvek umožňuje
vám umožní propojit objednávku s pracovním směnou.
- :guilabel:`Opakovat“: Zaškrtněte políčko a nastavte pole „Opakovat každých“
podle vašich potřeb. Následující pravidla se vztahují na opakující se směny:

  - Všechny pole (např. Resource, Role, Project) jsou kopírována z
původní posun kromě data, které se přizpůsobuje podle
:guilabel:`Opakovat každý“ pole.
  - Případné opakování se plánuje, ale nebude zveřejněno.
  - Plánované směny se vytváří automaticky s šestiměsíčním předstihem.
postupně. Chcete-li změnit časové pásmo, aktivujte režim vývojáře (:ref:`<developer-mode>`), pak
přejděte na „Plánování -> Konfigurace -> Nastavení“ a upravte
:guilabel:`Opakující se posuny“.

- :guilabel:`Uložit jako šablonu“: Pokud je tato možnost zaškrtnuta, vytvoří se šablona s
Stejné: „Čas začátku a konce“, „Přidělený čas“, „Role“
a:guilabel:`Projekt“.
- :guilabel:`Poznámka zaslaná zaměstnanci“: Kliknutím na pole přidejte poznámku.
- :guilabel:`Datum“: Zvolte datum a čas své směny. To je jediné povinné pole, když
vytváří přesun.
- „Čas přidělený“: Je vypočítán na základě data a zaměstnance „Pracovní doby“.
Schéma. Podrobnější informace naleznete v části :ref:`Šablony směn <plánování/šablony>`.

Klikněte na tlačítko „Zveřejnit a uložit“ k potvrzení změny a odeslání plánu zaměstnanci.
e-mailem.

.. poznámka::
Návrh je viditelný v rozhraní pro správce a lze jej identifikovat pomocí svislých čar.
zaměstnanec je o změně směny informován až po jejím zveřejnění.

Závisí na konfiguraci účtu, zda zaměstnanci obdrží dvě různé notifikace.

   - Zaměstnanci bez uživatelských účtů jsou přesměrováni na speciální **Portál plánování**.
   - Zaměstnanci s uživatelským účtem jsou přesměrováni na pohled :guilabel:`Moje plánování`.
zadní pohled na Odoo.

..tip:
Nástroj pro **rozdělení směn** umožňuje snadno rozdělit dlouhou směnu na segmenty. K tomu stačí přejet
Klikněte na ikonu „nůžky“ (zobrazení ikony lze nastavit v nabídce Nástroje > Možnosti).

.... obrázek: plánování/přerušení směn.png
:alt: Nástroj pro rozdělení směn.

.. plánování/otevřené směny:

Otevřené směny a automatické plánování
-----------------------------

Tlačítko „Auto Plan“ umožňuje přiřadit **otevřené směny** (směny bez pracovníka).
přiřazené) a vytvářet a přiřazovat směny k prodejním objednávkám nebo projektu.

Následující vlastnosti mají vliv na plánování auta:

- Pozice: Otevřené směny jsou přidělovány pouze zdrojům (zaměstnancům nebo materiálu), které mají
přidělené roli. Není možné používat funkci „Automatické plánování“
zaměstnanec bez rolí.
- Přednostní role: Přednostní role přiřazená zdroji má přednost před ostatními rolí
které jim byly přiděleny.
- Konflikt: Zaměstnanci nebo materiál nemohou být přiřazeni na více směn najednou.
- Pracovní volno: Do výpočtu se započítává pracovní volno zaměstnanců i svátky.
- **Délka směny**: Zohledňuje se při přidělování směn zaměstnancům nebo materiálu.
nelze použít funkci „Auto Plan“ pro zaměstnance, který pracuje
:ref:`pružná pracovní doba <plánování/pracovní doby>“.
- Smlouvy: Pokud má zaměstnanec aktivní smlouvu, nebude mu přidělena směna, která spadá do
v době po skončení smlouvy.

Klikněte na tlačítko „Zveřejnit“ a potvrďte rozpis a informujte zaměstnance o plánování.

... plánování/přepínání/rozpojení:

Přesunutí směn a nezaměstnanost
---------------------------------

Dva funkce jsou k dispozici, které umožňují zaměstnancům provádět změny ve svém rozvrhu:
přepínání směn a odvolávání.

.. poznámka::
Tyto vlastnosti jsou navzájem vylučující. Přepínání směn je možné výchozí hodnotou a nelze ho
je deaktivován. Jakmile je však zapnuta funkce **Povolit nepřiřazení**, nahrazuje možnost
přepínač se posune.

Střídání směn
~~~~~~~~~~~~~~~~

Jakmile jsou směny naplánovány a zveřejněny, zaměstnanci obdrží e-mailové oznámení. Pokud je
chce změnit směnu, může kliknout na nechtěnou směnu a kliknout na „Poptat výměnu“.

Přesun zůstává přiřazen původnímu zaměstnanci, v rozvrhu je ale upozornění
Informace o tom, že zaměstnanec přeje změnit směnu, je vidět na směně.

Pozice se pak zobrazí ostatním zaměstnancům s touto rolí a ti mohou pozici přidělit.
může kliknout na tlačítko „Beru to“.

.. poznámka::
V následujících případech se použijí tyto pravidla:

   - Zobrazené směny odpovídají rolím zaměstnance.
   - Přepínání směn není k dispozici pro směny v minulosti.

Nezadání
~~~~~~~~~~~~

Aby zaměstnanci mohli odvolat své přiřazení na směnu, přejděte na
Vyberte položku „Nastavení“ v menu „Plánování“, poté zaškrtněte políčko
:guilabel:`Povolit přeřazení“. Pak zadejte maximální počet dní, po které mohou zaměstnanci
se před směnou odhlásit.

Jakmile jsou směny naplánovány a zveřejněny, zaměstnanci obdrží e-mailové oznámení. Pokud se
přidělování je povoleno, zaměstnanci mohou kliknout na tlačítko „Jsem nedostupný“ a
přechází na otevřenou směnu.

.. poznámka::
V následujících případech se použijí tyto pravidla:

   - V kalendáři zaměstnance se zobrazují pouze směny, které odpovídají jeho rolím.
   - Odvolání směn není možné pro již proběhlé směny.
