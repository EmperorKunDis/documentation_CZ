Zobrazit obsah
:ukázat obsah:

========
Helpdesk
========

Odoo **Helpdesk** je aplikace pro zákaznickou podporu na bázi ticketů, do které lze přidat více týmů
a spravované na jednom pultu, každá s vlastními kanály pro řešení případů od zákazníků.
Trubky jsou uspořádány do přizpůsobitelných fází, které umožňují týmům sledovat, prioritizovat a řešit
zajistí rychle a efektivně vyřešení problému zákazníka.

.. _helpdesk/create-team:

Vytvořte tým podpory
======================

Pro zobrazení nebo změnu týmů **Helpdesku** přejděte na:
Tým podpory. Chcete-li vytvořit nový tým, klikněte na tlačítko „Nový“ v levém horním rohu.
přístrojová deska.

.. obrázek: helpdesk/helpdesk-teams-list.png
:alt: Pohled na stránku týmů v Odoo Helpdesk.

V prázdném formuláři týmu Helpdesku zadejte jméno nového týmu. Pak vepište
popis týmu v poli pod názvem týmu, pokud je to požadováno.
je přiřazeno k, vyberte jej z rozevírací nabídky „Společnost“.

.. důležité:
Popis týmu je zveřejněn na webových stránkách určených pro veřejnost.
<helpdesk/overview/ticket-submission>, kde zákazníci a uživatelé portálu podávají požadavky.
Popis, který je uveden v tomto poli, by neměl obsahovat žádné informace, které jsou určeny pouze pro interní potřebu.
pouze pro vlastní potřebu.

.... obrázek:helpdesk/týmová-charakteristika-webform.png
:alt: Zobrazení webové stránky týmu pomocného servisu s popisem týmu.

Viditelnost a přiřazení
-----------------------

Nastavení „Viditelnost“ mění, kteří interní uživatelé a portáloví uživatelé mají přístup do této týmu.
jejich lístky. Nastavení „Přidělení“ mění způsob, jakým uživatelé jsou přiřazováni k řešení každého lístku.

Určete viditelnost týmu
~~~~~~~~~~~~~~~~~~~~~~~~~

V sekci „Zobrazit“ vyberte jednu z následujících možností, abyste určili, kdo může
Tým a lístky na tento zápas:

- :guilabel:`Zváni interní uživatelé (soukromý přístup)`: Interní uživatelé mohou tým a lístky vidět
Následovali je, a tento přístup může být upraven na každé vstupence individuálně přidáním nebo odebráním
uživatel jako následovník. Interní uživatelé jsou považováni za „přizvané“ poté, co byli přidáni jako následovníci
na individuální vstupenku nebo na tým samotný (viz např. helpdesk/follow).
- :guilabel:`Všichni interní uživatelé (firma)“: Všichni interní uživatelé mohou přistupovat do týmu a všechny jeho
lístky.
- :guilabel:`Zváni jsou pouze portáloví uživatelé a všichni interní uživatelé (veřejně)“: Všichni interní uživatelé mohou přistupovat
tým a všechny jeho vstupenky. Uživatelé portálu mohou sledovat pouze vstupenky, které sledují.

Příklad:
Tým „Podpora zákazníků“, který by měl řešit obecné problémy s dodávkami a produkty, by měl mít
Viditelnost nastavena na:guilabel:"Zváni uživatelé portálu a všichni interní uživatelé".

Ve stejnou dobu byl zřízen tým „Financial Services“, který řeší případy související s účetnictvím nebo daněmi.
Informace by měla být viditelná pouze pro :guilabel:`Pozvané interní uživatele`.

.. varování:
Viditelnost týmu lze po prvotní konfiguraci změnit. Pokud se však tým změní
od uživatelů portálu pozvaných a všech interních uživatelů (veřejných) přístup k buď
uživatelé (soukromí) nebo pouze interní uživatelé (firma) - přístup pro portálové uživatele je odebrán
fanoušci z obou týmů a také jednotlivé vstupenky.

... pomocí helpdesku.

Sledujte všechny týmy.
~~~~~~~~~~~~~~~~~~~~~~~~~

Pokud má být uživatel informován o jakýchkoliv změnách týkajících se vstupenek na zápasy tohoto týmu, vyberte jeho jméno
z nabídky „Sledovat“ v sekci „Sledovat všechny tikety týmu“.
pole. Může být vybráno více uživatelů, kteří sledují jeden tým.

.. důležité:
Kontakty mimo tým lze vybrat v poli „Sledovatelé“. Pokud je viditelnost týmu nastavena na
nastaveno na: guilabel:„Zváni interní uživatelé (soukromý)“, sledující jsou informováni o aktualizacích
týmových vstupenek, ale nemohou je zobrazit na portálu.

Automaticky přiřazovat nové požadavky
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Když jsou vstupenky přijaty, musí být přiřazeny členovi týmu. To se provádí buď
ručně na jednotlivých vstupenkách nebo prostřednictvím Automatic Assignment.
zaškrtněte políčko „Automatické přiřazení“, abyste tuto funkci aktivovali pro celý tým.

.. obrázek: helpdesk/helpdesk-visibility-assignment.png
:alt: Zobrazení stránky nastavení týmu podpory s důrazem na automatické přiřazování v Odoo
Helpdesk.

Vyberte jednu z následujících metod přiřazování úkolů podle toho, jak by se měla pracovní zátěž rozdělit mezi
tým:

- :guilabel:„Každému uživateli je přiřazeno stejné množství lístků“: Lístky jsou přiděleny členům týmu
na základě celkového počtu vstupenek bez ohledu na počet otevřených nebo uzavřených vstupenek.
je aktuálně přidělen.
- Každý uživatel má stejný počet otevřených požadavků: Požadavky jsou přidělovány členům týmu
podle počtu otevřených případů, které jsou aktuálně přiřazeny.

.. poznámka::
Když je vybrána volba „Každému uživateli je přidělen stejný počet lístků“, celkový počet
Počet vstupenek přidělených členům týmu je stejný, ale nebere v potaz současnou
pracovní vytíženost.

Při výběru položky „Každý uživatel má stejný počet otevřených požadavků“ je zajištěno rovnoměrné
pracovní zátěž mezi členy týmu, protože bere v úvahu aktuální počet aktivních požadavků.

Poté přidejte členy týmu, kteří mají být přiřazeni ke všem lístkům pro tento tým. Nechte
pole nechat prázdné, aby se do něj zahrnuly všechny zaměstnankyně s příslušnými přiřazenými úkoly a přístupovými právy.
Nastavení uživatelského účtu.

.. důležité:
Pokud má zaměstnanec v aplikaci „Čas volna“ čerpání dovolené naplánované, není přiřazen
vstupenek během této doby. Pokud není k dispozici žádný zaměstnanec, systém se podívá dopředu až do chvíle, kdy je někdo k dispozici.
zápasu.

.. viz též:
   - :ref:`Spravovat uživatele <users/add-individual>`
   - :doc:`Přístupová práva <../obecne/uzivatele/prava_pristupu>`

Sloučit lístky
=============

Pokud se v HelpDesku najdou duplicitní lístky, mohou být sloučeny do jednoho lístku pomocí
*sjednocení* funkce.

.. důležité:
Funkce *sjednocení* je přístupná pouze v případě, že je zapnutá funkce :doc:`Čištění dat
Aplikace pro čištění dat je nainstalována na databázi.

Pro sloučení dvou nebo více lístků přejděte do :menuselection:`Aplikace Helpdesku --> Lístky --> Všechny lístky`.
Označte si karty, které chcete sloučit a zaškrtněte políčko vpravo od každé karty.
jejich. Pak klikněte na ikonu „fa-cog“ a vyberte možnost „Sloučit“.
položky nabídky. Pokud tak učiníte, otevře se nová stránka s vybranými vstupenkami a
:guilabel:`Podobnost“ hodnocení. Zde klikněte buď na :ref:`Spojení <čištění dat/souborů>“.
spojit lístky nebo: guilabel: DISCARD.

Převádějte vstupenky na příležitosti
================================

Některé lístky mohou být lépe vyřešeny prodejním týmem než podporou. V tomto případě
lístky lze převést na „příležitosti“ a přiřadit prodejnímu týmu k dalšímu zpracování.

.. důležité:
Tato funkce je k dispozici pouze tehdy, pokud je nainstalována aplikace :doc:`CRM <../sales/crm>`.

Převést lístek na příležitost. Nejprve přejděte do lístku, buď z týmového potrubí,
nebo přejděte na:menu:„Pomocná aplikace - Tikety“ a klikněte na tiket, abyste jej otevřeli.

Na vrcholu faktury klikněte na tlačítko „Převést na příležitost“.

.. poznámka::
Pokud jsou v aplikaci CRM zapnuté „příležitosti k získání“, pak při přidělení případu se otevře okno s
Převáděny na *leady* a tlačítko zobrazuje: „Převést na lead“.

Otevře se okno „Převést na příležitost“. Vyplňte nebo vyberte následující
informace o vyskakovacím okně:

- Zvolte, zda chcete vytvořit nového zákazníka nebo jej propojit s
„Stávající zákazník“ nebo „Nelinkujte na zákazníka“. Pokud je zvoleno „Linkovat na zákazníka“,
Vyberte vhodný název zákazníka ze seznamu :guilabel:`Zákazník`.

- :guilabel:`Prodejní tým“: Vyberte, který :guilabel:`Prodejní tým“ a :guilabel:`Obchodník“ se
Vzniklou příležitost je přidělována tomu, kdo ji vytvořil.

.. obrázek:helpdesk/convert-to-opp.png
:alt:Pop-up okno pro konverzi příležitosti.

Po dokončení formuláře klikněte na tlačítko „Převést na příležitost“. To vytvoří nový
možnost v aplikaci CRM. Originální požadavek je propojen s novou možností v chatovacím okně
pro dohledatelnost.

.. poznámka::
Po převodu na příležitost je lístek archivován.

.. viz též:
   - „Tutoriály Odoo: Helpdesk <https://www.odoo.com/slides/helpdesk-51>“

.. toctree::


helpdesk/přehled
helpdesk/pokročilé
