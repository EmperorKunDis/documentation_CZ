Zobrazit obsah
:ukrýt obsah:

============
Termíny
============

Aplikace pro objednávání schůzek společnosti Odoo je aplikací pro samoobslužné objednávání, která usnadňuje proces rezervování.
schůzky, konzultace nebo služby. Společně s aplikacemi pro podnikání společnosti Odoo umožňuje
automatizaci plánování schůzek, snížení manuální koordinace a poskytnutí hladkého
zkušenost pro klienty. Termíny lze propojit s kalendářem, příležitostmi v CRM a zaměstnanci.
a více, což z něj činí ideální nástroj pro služební podniky hledající efektivitu a
organizace.

Konfigurace
=============

Aplikace **Objednávky** umožňuje nové termíny objednávek podle dostupnosti
uživatelé nebo dostupnost zdrojů, jako jsou například místnosti pro schůzky či sedací plochy.
Zdroje nebo spravovat stávající zdroje, přejděte na:
--> Zdroje“. To otevře seznam dostupných zdrojů v databázi i s jejich
individuální kapacita.

... termíny a zdroje:

Zdroje
---------

Klikněte na „Nový“ pro vytvoření nového zdroje. V prázdném záznamu zadejte název
nový zdroj. V poli „Kapacita“ zadejte maximální počet lidí, které zdroj
může ubytovat. Poté potvrďte časové pásmo pro tuto zdrojovou položku.

Pokud chcete, vyberte jeden nebo více položek z nabídky „Související zdroj“.
označuje jeden nebo více zdrojů, které lze použít v kombinaci k vyřešení větší poptávky.

.. důležité:
Pouze „propojené zdroje“ se používají při použití funkce automatického přiřazení (viz :ref:`<appointments/configure>`)
:guilabel:`Metoda přiřazení“.

Nakonec přidejte popis pro tuto zdrojovou položku pomocí :guilabel:`Description`.

.. poznámka::
Obsah záložky „Popis“ je viditelný zákazníkům při rezervaci.
objednání online.

..._objednávky/konfigurovat:

Konfigurace typu objednávky
==============================

Před zadáním termínu je nutné vytvořit typ schůzky. Přejděte na
Vyberte v nabídce aplikace „Termíny“ položku „Nový“. V novém prázdném záznamu
Vložte název schůzky, pak nastavte dobu trvání pro tento typ schůzky.

Dále nastavte „Čas před rezervací“. To je minimální doba mezi tím, kdy si zákazník objedná
termín lze rezervovat a kdy začít s rezervací. Pokud je nastaveno
Předem je nutné si rezervovat termín alespoň hodinu předem.

Příklad:
Vytvoříme typ rezervace pro „Tenisové kurty“, s hodnotou „Doba trvání“ 1 hodina.
a čas před rezervací 1 hodina. V 14:00 se pokusí zákazník zarezervovat
termín na stejný den v 14:45 hodin. První volná kapacita je od 16:00 hodin.

.. obrázek: objednávky/příklad předběžné rezervace.png
:alt: Příklad kalendáře rezervací s volnými termíny.

Vyberte „Časový okno“:

- Vyberte možnost „K dispozici nyní“ a umožněte zákazníkům okamžitě si zarezervovat termín.
:guilabel:`Do X dnů do budoucna“ pole k definování, jak daleko dopředu mohou zákazníci plánovat
termíny. Například pokud je zadáno číslo „14“, zákazníci nemohou objednávat termíny dříve než 14 dní dopředu.
od aktuální doby.
- Vyberte možnost „V rámci datového rozsahu“ pro omezení rezervací na určitý rozsah dnů.
Vyberte tuto možnost a klikněte do políčka „Od“ a „Do“, použijte kalendář.
okno s nastavením data a časového rozsahu.

Aktualizujte pole „Povolit zrušení“ na omezení doby před objednáním.
kde si zákazník může zrušit objednávku. Pokud je tato funkce zapnutá, zákazníci nebudou moci své objednávky zrušit
určeném časovém období.

.. poznámka::
Pokud se zákazník pokusí zrušit v daném časovém limitu, obdrží chybové hlášení.
kontaktní informace. Pokud se jedná o zdroj, jsou kontaktní údaje pro uživatele
a tento typ schůzky vytvořil. Pokud je schůzka pro uživatele, kontaktní údaje jsou pro
uživatel, s nímž se schůzka týká.

.... obrázek:: objednání/zrušení-objednávky.png
:alt: Příklad zprávy, kterou zákazník vidí při zrušení.

Dále určete, zda je tento typ schůzky založen na uživatelích nebo
Vyberte příslušný tlačítko „Zdroje“ a pokud je založeno na uživatelích, vyberte
Jeden nebo více uživatelů v rozevíracím seznamu. Pokud je založen na :ref:`zdrojích
<termíny/zdroje>“, vyberte jeden nebo více „Zdrojů“ v seznamu.

..tip:
Uživatelsky definované typy schůzek lze používat k plánování prodejních schůzek a ukázek.
pohovory o přijetí do zaměstnání.

Pomocí typů objednávek na základě zdrojů lze naplánovat čas v konkrétních místnostech nebo prostorách.

Vybráním položky „Zdroje“ v poli „Dostupnost“ se zobrazí
Možnost „Spravovat kapacity“. Pokud je vybrána, termín rezervace omezuje počet účastníků
na základě kapacity vybraných zdrojů.

Vyberte metodu přiřazení pomocí příslušného tlačítka rádia:

 - :guilabel:`Vybrat uživatele nebo zdroj, pak čas“: zákazníci vybírají z dostupných
Vyberte uživatele nebo zdroj, pak vyberte volný časový úsek.
 - Vyberte čas poté uživatele nebo zdroj“: zákazníci si vybírají datum a čas, pak zvolí
seznam dostupných uživatelů/zdrojů.
 - :guilabel:`Vyberte čas, pak automaticky přiřadit“: zákazníci si vyberou časový interval a jsou jim automaticky přiřazeni.
přiřazen uživateli nebo zdroji.

Kalendář
------------

Karta „Rozvrh“ se používá k určení, kdy má být tento typ schůzky dostupný.
Nastavení definují časové úseky, které se zobrazují na stránce s rezervací.

Klikněte na tlačítko „Přidat časový úsek“ pro vytvoření nového časového rámce. Vyberte den v týdnu z
:guilabel:Každé rozbalovací menu, pak aktualizovat časy v poli :guilabel:Od a :guilabel:Do
políčka. Klikněte na ikonu „odpadkový koš“ (trash) pro odstranění položky. Můžete také vybrat více položek.
Je možné ji zahrnout do jediného dne.

..tip:
Pokud by měl být termín k dispozici v určitých časech, například když uživatelé jdou na oběd,
Zahrnují časové úseky před a po.

.... obrázek: schůzky/kalendář-karta.png
:alt: Příklad záložky Plán v objednávce.

Karta Možnosti
-----------

Karta „Možnosti“ slouží k přizpůsobení zobrazení pro tuto schůzku.
Jako nastavení oznámení pro zákazníky a uživatele.

Pole „Zobrazení v předním panelu“ určuje, jak se termín zobrazí na webových stránkách.
zákazníkům. Vyberte tlačítko „Zobrazit obrázky“ a zveřejněte výchozí obrázky
uživatele nebo zdroje pro tuto schůzku na webu.

Pole „Časové pásmo“ a „Lokalita“ se automaticky vyplní pro zdroj
Termíny podle umístění zdroje. U uživatelských termínů je
V poli „Místo“ je výchozí hodnotou „Online schůzka“, s odkazem na „Video konferenci“.
je automaticky vygenerovaný. Pokud se nejedná o online schůzku, zvolte jinou možnost v
:guilabel:`Lokalita“ pole.

Zatrhněte políčko „Potvrzení ručně“ a vyžádejte si schválení před přijetím schůzky.
Pokud je tato funkce zapnutá, časový úsek pro objednání se stále považuje za rezervovaný, dokud nebude
potvrzeno nebo zamítnuto. Nechte tento prázdný, aby se automaticky přijímaly schůzky vytvořené z této
termínu.

Funkce „Vytvořit příležitost“ (<appointments/create-opps>) přidává příležitost do
Pro každou plánovanou schůzku aplikace CRM, která je přiřazena konkrétnímu uživateli. Zaškrtněte
zaškrtněte políčko „Vytvořit příležitosti“.

.. důležité:
Toto pole je viditelné pouze v případě, že je nainstalována aplikace CRM na databázi.

Pole „Upomínky“ se používá k nastavení způsobu kontaktování zákazníků před
Čas objednání. Vyberte jednu nebo více možností z roletky podle komunikačního kanálu
A časový rámec.

Zatrhněte políčko „Povolit hosty“ a zákazníkům umožněte přidat další hosty.
Při registraci na termín.

...objednávky/dotazy:

Karta otázek
-------------

Karta „Dotazy“ může být použita k tomu, aby zákazníci poskytli další informace, zatímco
objednávají se na konzultaci. Klikněte na tlačítko „Přidat otázku“ pro přidání nové otázky.

V okně „Vytvořit otázky“ zadejte „Otázku“, pak vyberte
:guilabel:`Typ odpovědi“.

Zatrhněte políčko „Odpověď je povinná“ a zákazníci budou muset odpovědět na tuto otázku před
mohou si zarezervovat termín. Klikněte na tlačítko „Uložit a nový“ pro přidání další otázky nebo
:guilabel:`Uložit a zavřít“ po dokončení.

Karta Zprávy
------------

Karta „Zprávy“ slouží k poskytování dodatečných informací zákazníkům.
v souvislosti s touto formou jmenování.

.. důležité:
Obsah v záložce „Zprávy“ je viditelný pro zákazníky a návštěvníky webu.

Do pole „Základní zpráva“ vložte stručný popis typu schůzky.
může obsahovat téma schůzky, program jednání nebo seznámení s uživateli
odpovědný za schůzku.

Po provedení rezervace se zákazníkovi zobrazí „Doplněk o potvrzení“.
schůzku. Zde můžete uvést další informace, které by měl zákazník vědět. To může zahrnovat
informace o parkování, poslední minuty nebo další pokyny.

Zveřejnění termínu
=========================

Když je termín připravený k zveřejnění, klikněte na tlačítko „Přejít na web“ v horní části.
zaznamenané hodnoty. Pak přetáhněte ikonu „Zapnuto“ na
:icon:`fa-toggle-on` :guilabel:`Zveřejněno“.

.. toctree::


appointments/vytvorit-misto
