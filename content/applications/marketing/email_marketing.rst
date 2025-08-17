Zobrazit obsah

===============
Emailový marketing
===============

Aplikace Odoo *Email Marketing* poskytuje nástroje pro tahání a plošné vkládání, předpřipravené šablony a další.
interaktivní funkce pro vytváření poutavých e-mailových kampaní. Aplikace Email Marketing také poskytuje
podrobné ukazatele k měření celkové efektivity kampaně.

.. viz též:
   - Tutoriál Odoo: E-mailový marketing

   - „Zázračný list – strategie e-mailového marketingu [PDF]
<https://drive.google.com/drive/folders/1TqZfYCF-56yhUSDVyfFjkmB23RWaRBP7>

.. karty:

...... karta: Seznamy mailů
:target: marketing-e-maily/mailové seznamy

Silo kontakty do konkrétních seznamů.

.......karta: Spravovat odhlášení (černá listina)
:target: marketing-e-mailu/odhlášení

Umožněte příjemcům odhlásit se a zablokovat budoucí e-maily.

......karta: E-mailová aktivace ztracených odkazů
:target: marketing/ztráta_leadů

Ztrácí cíle s e-mailovým marketingem.

......karta: Analyzovat metriky
:target: marketing_e-mailu/analýza_metrik

Analýzou kampaní.

Dashboard pro e-mailový marketing
=========================

Po instalaci aplikace klikněte na ikonu aplikace „E-mailový marketing“ v hlavním
Odoo panel. To odhalí hlavní panel „Pošta“ v výchozím seznamovém pohledu.

.. obrázek: email_marketing/dashboard_mailingu.png
:align:center
:alt: Zobrazení hlavního panelu aplikace Odoo Email Marketing.

V poli pro vyhledávání je výchozí filtr „Moje zprávy“, který zobrazuje všechny zprávy.
související s aktuálním uživatelem. Chcete-li tento filtr odstranit, klikněte na ikonku „✖“ vedle
filtr v hledací liště. To odhalí všechny e-maily v databázi.

Informace na panelu „Poštovní zásilky“ je možné zobrazit ve čtyřech různých režimech, které jsou umístěny v
v pravém horním rohu jako samostatné ikony.

Možnosti zobrazení jsou následující:

- :ref:`Seznam <email_marketing/list-view>“ (výchozí pohled)
- :ref:`Kanban <email_marketing/kanban-view>`
- :ref:`Kalendář <e-mailový marketing/kalendar-view>`
- :ref:`Graf <email_marketing/graph-view>`

.. _email_marketing/list-view:

Zobrazení seznamu
---------

Zobrazení seznamu, které je reprezentováno ikonou „☰“ (horizontální čáry) v pravém horním rohu.
Je výchozí pohled na panelu „Poštovní zásilky“ v aplikaci „E-mailový marketing“.

V seznamovém zobrazení jsou sloupce věnované různým aspektům informací týkajících se
seznam e-mailů. Tyto sloupce jsou následující:

- :guilabel:`Datum“: datum, kdy byla e-mailová zpráva odeslána.
- :label_field:Předmět: předmět e-mailu.
- :guilabel:`Zodpovědný“: uživatel, který e-mail vytvořil, nebo uživatel, kterému byl e-mail přiřazen
e-mail
- :guilabel:`Počet odeslání“: kolikrát byla e-mailová zpráva odeslána.
- :guilabel:`Doručeno (%)“: procento odeslaných e-mailů, které byly úspěšně doručeny.
- :guilabel:`Otevřeno (%)“: procento odeslaných e-mailů, které byly otevřeny příjemci.
- :guilabel:`Kliknutí (%)“: procento odeslaných e-mailů, které byly otevřeny příjemci.
- :guilabel:`Odpověděno (%)“: procento odeslaných e-mailů, které byly odepsány příjemci.
- :guilabel:`Stav“: stav e-mailu („Návrh“, „Ve frontě“ nebo
:guilabel:`Odesláno“).

Chcete-li přidat nebo odebrat sloupce, klikněte na tlačítko „Další možnosti (dva svislé pruhy se tečkami)“.
ikonu umístěného vpravo dole od nadpisů sloupců ve zobrazení seznamu. Kliknutím na něj se objeví nabídka
dalších možností sloupců.

.. _email_marketing/kanban-view:

Kanban
-----------

Zobrazení kanbanu, reprezentované ikonou „Inverted Bar Graph“ lze získat v
v pravém horním rohu panelu „Poštovní zásilky“ v aplikaci „E-mailový marketing“.

.. obrázek: email_marketing/kanban-view.png
:align:center
:alt: Zobrazení kanbanu hlavního panelu aplikace Odoo Email Marketing.

V zobrazení kanbanu se informace o e-mailu zobrazí v různých fázích.

Stadia jsou: „Návrh“, „Ve frontě“, „Odesílání“ a „Odesláno“.

- :guilabel:Název: e-mail ještě není dokončený.
- :guilabel:`V pořadí“: e-mail bude odeslán v pozdějších termínech.
- :guilabel:`Odesílání“: e-mail je v tuto chvíli odeslán svým příjemcům.
- :guilabel:`Odesláno“: e-mail již byl odeslán svému příjemci.

V každé fázi jsou karty přetažením a ponecháním, které reprezentují emaily vytvořené/odeslané.
a stav, ve kterém se nachází, představuje aktuální stav této zprávy.

Každá karta na panelu „Poštovní zásilky“ poskytuje klíčové informace o konkrétním
e-mail.

Když kurzor přejede do horního pravého rohu karty e-mailové kampaně, zobrazí se tlačítko :guilabel:„⋮“ (tři
Výsledkem je ikona ve tvaru svislých teček). Když ji kliknete, zobrazí se malé rozbalovací menu s možností barevného označení.
e-mailu, nebo jej smazat a archivovat pro případné budoucí použití.
používání.

.. obrázek: email_marketing/trojitý-tečkový-menu.png
:align:center
:alt: Zobrazení tří teček v rozbalovacím seznamu na stránce pro e-mailový marketing Odoo.

.. _email_marketing/kalendářový pohled:

Kalendář
-------------

Kalendářový pohled je reprezentován ikonou :guilabel:`📅 (kalendář)` a lze jej zobrazit v
v pravém horním rohu panelu „Poštovní zásilky“ v aplikaci „E-mailový marketing“.

V kalendáři je zobrazen měsíční kalendář (výchozí nastavení) s daty odeslání pošty.
by měly být odeslány.

.. obrázek: email_marketing/kalendarni-vyhled.png
:align:center
:alt: Kalendářový pohled na přehled rozesílek v aplikaci E-mailová marketingová kampaň.

Aktuální datum je reprezentováno ikonou „:guilabel:`🔴 (červený kruh)“ nad datem v kalendáři.

Vpravo od kalendáře jsou možnosti filtrovat výsledky podle:guilabel:Zodpovědné osoby a/nebo
K dispozici jsou přepínače „Stav“.

..tip:
Chcete-li skrýt pravou lištu, klikněte na ikonku „(panel-right)“, která se nachází nad lištou.

V horním levém rohu nad kalendářem je možnost změnit zobrazované období.
k dispozici v rozbalovacím seznamu, který zobrazuje výchozí hodnotu „Měsíc“. Když je kliknutý,
Vyskakovací nabídka, která se objeví, zobrazí možnosti: :guilabel:`Day`, :guilabel:`Week`,
:guilabel:`Měsíc“ (výchozí hodnota), „Rok“ a „Zobrazit víkendy“ (výchozí výběr).

Kliknutím na kteroukoli z těchto možností se kalendář změní tak, aby odrážel požadovaný časový úsek.

Kliknutím na ikonu buď :guilabel:`⬅️ (levý směr)` nebo :guilabel:`➡️ (pravý směr)` změníte
kalendář do předchozího nebo budoucího času podle toho, co je kliknuté, v závislosti na zvoleném množství
časové období.

Chcete-li se vrátit k aktuálnímu datu, klikněte na tlačítko „Dnes“.

.. _email_marketing/graficky

Grafický pohled
----------

Grafický pohled, který je reprezentován ikonou „(line graph)“, lze zobrazit v pravém horním rohu.
koutku panelu „Poštovní zásilky“ v aplikaci „E-mailový marketing“.

Zatímco v grafickém zobrazení je stav e-mailů na stránce :guilabel:`Mailings`
Grafy svislých sloupců, ale jiné možnosti grafického zobrazení lze implementovat, pokud je potřeba.

.. obrázek: email_marketing/graf-zobrazeni.png
:align:center
:alt:Jak vypadá grafické zobrazení aplikace Odoo Email Marketing.

V horním levém rohu nad grafem je možné vybrat z nabídky „Měření“.
klikněte, jiná filtrační možnost se objeví pro další přizpůsobení grafických zobrazení.

Tyto možnosti nastavení jsou: „Procento A/B testování“ a „Počet“.
Výchozí.

Vpravo od nabídky „Měření“ je tlačítko „Vložit do tabulky“.
tlačítko, pokud je nainstalována aplikace Dokumenty. Po kliknutí se zobrazí okno s upozorněním
Možnost přidat graf do tabulky nebo panelu se otevře.

Vedle položky „Měření“ a tlačítka „Přidat do tabulky“ je
různé možnosti zobrazení grafu. Zleva doprava jsou tyto možnosti zobrazení grafu:
grafu) (výchozí hodnota), :guilabel: (liniový graf) a :guilabel: (kruhový graf).

.. poznámka::
Každá volba grafického zobrazení poskytuje vlastní sérii dalších možností pro zobrazení, které se objevují
vpravo od zvolené možnosti grafického výhledu.

Možnosti vyhledávání
--------------

Přestože je zvolený pohled na panelu „Pošta“ v nastavení „E-mail“
Marketingová aplikace obsahuje možnosti filtrů, seskupení a oblíbených položek.
Vždy připravený k dalšímu upravování informací, které jsou zobrazovány.

Pro přístup k těmto možnostem klikněte na ikonu „(svislá šipka)“ umístěnou napravo od
vyhledávací lištu. To odhalí seznam možností filtrování a seskupování, které jsou k dispozici.

.. obrázek: email_marketing/search-mega-menu.png
:align:center
:alt:Drobný menu s možnostmi vyhledávání aplikace pro e-mailový marketing Odoo.

Tyto možnosti poskytují různé způsoby, jak specifikovat a organizovat informace, které jsou vidět na
:guilabel:`Poštovní zásilky“ panelu.

.. záložky::

...... záložka: Filtry

Tato část rozbalovacího megamenu nabízí různé způsoby filtrování výsledků e-mailu.
jsou zobrazeny na panelu „Poštovní zásilky“ v aplikaci „E-mailový marketing“.

.. obrázek:: email_marketing/filters-dropdown.png
:align: střed
:alt: Zobrazení nabídky filtrů na panelu e-mailového marketingu v Odoo.

Možnosti jsou: :guilabel:`Můj poštovní výpis“, :guilabel:`Datum odeslání“, :guilabel:`Testování A/B“.
:guilabel:`Testování A/B“, :guilabel:`Uloženo“ a :guilabel:`Přidat vlastní filtr“.

Pokud je vybrána možnost „Vlastní filtr“, Odoo zobrazí okno s třemi
přizpůsobitelné pole pro vyplnění, abyste vytvořili vlastní filtrační pravidla pro použití v Odoo.
získat výsledky, které odpovídají konkrétnějším kritériím.

.. obrázek: email_marketing/add-custom-filter-popup.png
:align: střed
:alt:Přidat vlastní filtr do okna, které se objevuje v aplikaci Odoo Email Marketing.

...... tab:: Skupina

Tato část rozbalovacího megamenu nabízí různé způsoby, jak seskupit výsledky vyhledávání e-mailu.
jsou zobrazeny na panelu „Poštovní zásilky“ v aplikaci „E-mailový marketing“.

.. obrázek: email_marketing/group-by-dropdown.png
:align: střed
:alt: Zobrazení nabídky Skupina v aplikaci Odoo Email Marketing.

Tato část umožňuje seskupit data podle stavu zprávy nebo podle odesílatele.
:guilabel:`Odesláno“.

K dispozici je také možnost seskupit data podle :guilabel:`Datum odeslání`, které má svou vlastní
podmenu možností, ze kterých si můžete vybrat. Možnosti „Odeslaný období“ jsou „Rok“,
:guilabel:'Čtvrtletí', :guilabel:'Měsíc', :guilabel:'Týden' a :guilabel:'Den'.

Pokud žádná z výše uvedených možností „Skupit podle“ neposkytne požadované výsledky, klikněte
:guilabel:'Přidat vlastní skupinu' na konci sekce 'Skupina podle'.
Otevře se rozbalovací nabídka, kde lze vybrat vlastní kritéria a aplikovat je, čímž se zobrazí
jakýkoliv požadovaný soubor dat.



Tato část umožňuje uložit si vlastní filtry a/nebo skupiny pro budoucí použití.
Chcete-li využít tuto část, klikněte na pole „Uložit aktuální vyhledávání“, které se zobrazí.
další pole.

.. obrázek: email_marketing/favorites-dropdown.png
:align: střed
:alt:Pohled na nabídku Favorites v aplikaci Odoo Email Marketing.

Dát oblíbenému filtru nebo skupině název na prázdné řádce nad zaškrtávacími poli.
:guilabel:`Výchozí filtr“ a :guilabel:`Sdílený“.

Zatrhnutím políčka pro :guilabel:`Výchozí filtr/skupina` se tento oblíbený filtr/skupina stává výchozím.
výchozí možnost. Zaškrtnutím políčka pro :guilabel:`Sdílené soubory a složky` umožníte ostatním uživatelům vidět a používat tento
oblíbený filtr nebo skupina.

Po konfiguraci všech požadovaných možností klikněte na tlačítko :guilabel:`Uložit`, abyste uložili filtr/skupinu.
v sekci „Oblíbené“ rozsáhlého nabídacího menu.

Nastavení
========

Pro zobrazení a úpravu nastavení služby „E-mailový marketing“ přejděte do aplikace „E-mailový marketing“.
--> Konfigurace --> Nastavení.

.. obrázek: email_marketing/konfigurační nastavení.png
:align:center
:alt: Zobrazení nabídky Nastavení v aplikaci Odoo Email Marketing.

Na stránce nastavení je k dispozici čtyři funkce.

.. obrázek: email_marketing/settings.png
:align:center
:alt: Zobrazení stránky Nastavení v aplikaci Odoo E-mailový marketing.

Mezi hlavní vlastnosti patří:

- :guilabel:`Kampaně pošty“: umožňuje správu masových e-mailových kampaní.
- „Možnost černé listiny při odhlášení“: umožňuje příjemcům zablokovat sebe samotné
příští zprávy během procesu odhlášení.
- :guilabel:`Dedicated Server“: poskytuje možnost využívat oddělený, dedikovaný server
mailingy. Když je aktivní, Odoo zobrazí nové pole (a odkaz), ve kterém se konkrétní server
Musí se nastavit konfigurace, aby se mohl správně připojit k Odoo.
- :guilabel:24H Stat Mailing Reports“ umožňuje uživatelům zkontrolovat, jak dobře se poštovní kampaně vyvíjely během dne.
Po odeslání.

.. _email_marketing/vytvorit_email:

Vytvořte e-mail
===============

Pro vytvoření e-mailu otevřete aplikaci „E-mailový marketing“ a klikněte na
:guilabel:„Nový“ tlačítko v horním levém rohu stránky „Pošty“.

Kliknutím na tlačítko „Nový“ se zobrazí prázdná e-mailová zpráva.

.. obrázek: email_marketing/prázdný_detail_formuláře.png
:align:center
:alt: Zobrazení prázdného e-mailu v aplikaci Odoo Email Marketing.

V e-mailovém formuláři jsou pole pro :ref:`Předmět <email_marketing/subject>
:ref:`Adresáti <email_marketing/adresatei> e-mailu.

Pod ní jsou tři záložky: :ref:`Tělo zprávy <email_marketing/mail_body>`, :ref:`Testování A/B
<email_marketing/ab_tests>, a :ref:`Nastavení <email_marketing/settings_tab>“.

.. e-mailový marketing/předmět:

Předmět
-------

Nejprve zadejte do e-mailu :guilabel:Předmět. Předmět je viditelný v
příjemců do složky doručené pošty, takže mohou rychle vidět o co se zpráva týká.

.. poznámka::
pole „Předmět“ je povinné. E-mail nelze odeslat bez předmětu.
:guilabel:`Předmět“.

Ikona „:guilabel:“ (smějíček s plusem) v konci pole „Předmět“
reprezentují emotikony, které lze přidat do pole „Předmět“. Po kliknutí na ikonu se zobrazí
nabídka emotikon, které lze použít.

Nedaleko ikony :guilabel:`(smile s plusem)` na konci :guilabel:`Předmět
ikona je prázdná. Když ji kliknete, ikona se zlatem a
E-mail je uložen jako šablona v záložce „Tělo zprávy“ v sekci
budoucnost.

..._e-mailový marketing/odběratelé:

Příjemci
----------

Pod políčkem „Předmět“ na e-mailovém formuláři je pole „Zaslání“.
Vyberte příjemce e-mailu. Výchozí možností je
vybrané, ale kliknutím na pole se zobrazí další možnosti příjemců.

S výchozím nastavením možnosti „Seznam“ se musí zadat konkrétní seznam.
vybrané z příslušného pole seznamu „Přidružené seznamy“.

..tip:
Možné je vybrat více než jednu seznamovou službu z pole „Vyberte seznamové služby“.

Odoo pak e-mail odesílá na kontakty v daném seznamu.

.. viz též:
:doc:`email_marketing/mailing_listy`

Když je položka „Příjemci“ vybrána, objeví se pod ní další možnosti.
Každá možnost nabízí různé způsoby, jak může Odoo vytvořit cílovou skupinu pro e-mail.

.. obrázek: email_marketing/recipients-dropdown.png
:align:center
:alt: Zobrazení seznamu příjemců v aplikaci pro e-mailový marketing Odoo.

Tyto možnosti (s výjimkou výchozího :guilabel:`Mailing List`) umožňují vytvořit více
Uvedený příjemce filtru, v rovnicovém formátu, který se zobrazuje pod
V poli „Adresáti“.

Možnosti pole „Příjemci“ (kromě výchozí možnosti „Seznam e-mailů“)
Jejich seznam je následující:

- :guilabel:`Kontakt“: vázána na aplikaci *Kontakty*, zahrnuje všechny kontakty
zadané do databáze.
- :guilabel:`Registrace na akci“: je spojen s aplikací *Akce*, a poskytuje možnosti
aby komunikoval důležité informace o události s registrovanými účastníky.
akce nebo podpořit jiné cenné aktivity, jako jsou například průzkumy po akci, nákupy atd.
- :guilabel:`Přední/příležitost“: vázána na konkrétní záznamy v aplikaci CRM, která se otevře
vytváří řadu příležitostí k ovlivnění prodeje nebo nákupu.
- :guilabel:`Kontakt pro poštu“: je spojen s aplikací *E-mailová marketingová kampaň*, a zaměřuje se na
konkrétní kontakty na e-mailovou adresu, které jsou v dané aplikaci zadány a souvisejí s
a specifický seznam odběratelů. Tyto kontakty jsou také jedinečné, protože nemají vlastní
kontaktní kartu v aplikaci Kontakty. Tento seznam lze zobrazit po najetí kurzorem na
:menu_selection:`E-mailový marketing -> Seznamy e-mailů -> Kontakty na seznamu e-mailů`.
- :guilabel:„Objednávka“: vázána je na aplikaci „Prodej“ a zaměřuje se na konkrétní prodej.
objednávky v databázi.

Přidat filtr příjemce
~~~~~~~~~~~~~~~~~~~~

Každému z možností „Příjemce“ lze přidat specifičtější filtr příjemců. Vyberte si příjemce
volbou (kromě :guilabel:`Seznamovací e-mailová adresa“), a poté klikněte na :guilabel:`Upravit filtr (směřující vpravo).
ikona pod textovým polem „Příjemce“ pro zobrazení tří dalších filtračních pravidel.
formátované jako rovnice.

Je doporučeno, aby uživatelé zadali podrobné cílové kritérium pro
:guilabel:`Příjemci pole“. Obvykle nestačí jedna řádka cílení
na e-mailovou kampaň.

Zatímco možnost „Seznam odesílatelů“ je vhodná pro pole „Příjemci“,
Možnosti „Vedoucí/Příležitost“ a „Registrace události“ poskytují mnohem podrobnější informace.
kritérií cílení, které lze přidat na vrchol seznamu zdrojů semen.

Příklad:
Řekněme například, že je zvolené pole „Lead / Opportunity“ v poli „Adresáti“.
pole, uživatelé mohou přidat různá vlastní kritéria související s datem vytvoření.
:guilabel:`Stádiím“, :guilabel:`Štítky“, :guilabel:`Ztrátou důvodu“, :guilabel:`Prodejními týmy“
:guilabel:`Aktivní“ stavy, :guilabel:`Země“ a mnoho dalšího.

....... obrázek: marketing_e-mailu/podrobné_filtry_záznamů.png
:synchronizace: střed
:alt: Pohled na to, jak lze v Odoo Email Marketing upravit filtry pro příjemce.

Pro zobrazení podmenu možností v poli filtru klikněte na každé pole a vyberte požadovanou možnost.
výběr, dokud není dosaženo požadovaného uspořádání.

Počet záznamů v databázi, které odpovídají konfigurovaným pravidlům, je uveden
pod konfigurovanými filtry, v zelené barvě.

.. obrázek: email_marketing/filtr-zaznamu.png
:align:center
:alt: Pohled na nastavení filtrů příjemců v Odoo Email Marketing.

.. poznámka::
Některé možnosti podmenu v prvním poli pravidla umožňují druhou volbu, která nabízí ještě více
specifika.

Na pravé straně každého pravidla jsou tři další možnosti, které reprezentují :guilabel:`+ (plus
„Značka“, „Mapa stránek“ a „Smazat“ ikony.

- Ikona „+“ přidává novou větvičku do celkového logického cíle.
- Ikona :guilabel:`(sitemap)` přidá větvičku uzlu. Větve obsahují další dvě podúrovně.
podřízené uzly vložené pod určitý pravidlo, které poskytují ještě více specifičnosti pro
nad ním.
- Ikona „:guilabel:`🗑️ (směsný odpad)`“ smaže konkrétní uzlík (řádek) v logickém výrazu.

.._e-mailový marketing/tělo e-mailu:

Karta Tělo zprávy
-------------

V záložce „Tělo zprávy“ je k dispozici několik přednastavených šablon pro zasílání zpráv.
od.

.. obrázek: email_marketing/mail-body-templates.png
:align:center
:alt: Pohled na šablony v záložce Tělo e-mailu aplikace Odoo E-mail marketing.

Vyberte požadovaný šablonu a upravte všechny prvky jejího designu pomocí Odoo.
bloky pro stavbu webu, které se zobrazují v pravém sloupci při výběru šablony.

.. obrázek:email_marketing/template-building-blocks.png
:align:center
:alt: Pohled na bloky v záložce Tělo e-mailu aplikace Odoo E-mailový marketing.

Vlastnosti v bočním panelu, které se používají k vytváření a přizpůsobování e-mailů, jsou rozděleny do tří částí:
„Bloky“, „Přizpůsobit“ a „Navrhnout“.

Každý blok poskytuje jedinečné funkce a profesionální návrhové prvky.
blok, přetáhněte a vložte požadovaný blokový prvek do těla e-mailu, který se staví. Jakmile byl vložen,
Je možné upravit různé aspekty stavebního bloku.

..tip:
Chcete-li postavit e-mail od základu bez jakýchkoliv stavebních prvků, vyberte
:guilabel:`Plný text“ šablonu. Když je vybrána, Odoo poskytne úplně prázdnou plochu pro e-mail.
které lze upravit pomocí bohatého textového editoru na předním konci, který přijímá
přímé znaky '/'

Když do prázdného těla e-mailu zadáte znak "/", zatímco používáte :guilabel:`Plain Text`,
šablona se zobrazí nabídka různých grafických prvků, které lze použít k vytvoření
požadovaný e-mailový vzhled.

.... obrázek:: email_marketing/vzor-prázdný-svislí-zavináč.png
:synchronizace: střed
:alt: Pohled na rozbalovací nabídku v aplikaci Odoo Email Marketing.

... _email_marketing/ab_tests:

Tabulka testů A/B
-------------

Při otevření záložky „Test A/B“ na e-mailovém formuláři je k dispozici pouze jediná možnost.
je:guilabel:Povolit testování A/B. Tato volba není povinná.

Pokud je tato možnost zapnuta, příjemci jsou e-mailem kontaktováni pouze jednou za celou dobu kampaně.

Umožňuje uživateli odesílat různé verze stejné zprávy na náhodně vybrané příjemce.
zjistit účinnost různých návrhů, formátů, uspořádání obsahu a podobně – bez jakéhokoliv
Duplicitní zprávy.

Když je zaškrtnuto políčko vedle :guilabel:`Allow A/B Testing`, objeví se pole :guilabel:`on (%)
v němž uživatel určuje procento přednastavených příjemců, kteří jsou
aby tuto aktuální verzi newsletteru obdrželi jako součást testu.

.. poznámka::
V poli :guilabel:`na (%)“ je výchozí hodnotou číslo 10, ale tento údaj lze kdykoliv změnit.
čas.

Pod tím se objeví další dva políčka:

Políčko „Výběr vítěze“ nabízí seznam možností, ze kterých si uživatel může vybrat.
rozhoduje o tom, jaká kritéria by měla být použita k určení „vítězné“ verze e-mailových testů.
odesláno.

Možnosti v poli „Výběr výherce“ jsou následující:

- :guilabel:`Manuální“: umožňuje uživateli určit „vítěznou“ verzi e-mailové zprávy. Tato volba
Odebere pole „Poslat finální verzi“.
- :guilabel:`Nejvyšší otevřená míra“ (výchozí): určuje poštu s nejvyšším procentem otevření.
bude „vítěznou“ verzí.
- :guilabel:`Nejvyšší kliknutí na odkaz“: e-mail s nejvyšším proklikovým poměrem je považován za
„vítězná“ verze.
- :guilabel:`Nejvyšší odezva“: e-mail s nejvyšším počtem odpovědí je považován za
„vítězná“ verze.
- :guilabel:`Nejlepší lead“: e-mail s nejvíce generovanými kontakty je považován za „vítězný“.
verze.
- :guilabel:`Citace“: zpráva s nejvíce citacemi je určena jako
„vítězná“ verze.
- :guilabel:`Příjmy“: zásilka s nejvyšším příjmem je určena jako
„vítězná“ verze.

Pole „Odeslat konečné“ umožňuje uživatelům zvolit datum, které se používá k určení *kdy* systém Odoo
by měl určit „vítěznou“ e-mailovou zprávu a následně ji odeslat na
zbylí příjemci.

.. obrázek:email_marketing/ab-test-tab.png
:align:center
:alt: Pohled na kartu A/B testy v aplikaci Odoo E-mail marketing.

Na pravé straně těchto polí je tlačítko „Vytvořit alternativní verzi“. Když na něj kliknete,
Odoo představuje nový záložní panel „Tělo e-mailu“ pro uživatele, aby mohli vytvářet alternativní verze
e-mail na adresu test@test.

.. _e-mailový marketing/nastavení:

Karta Nastavení
------------

Možnosti, které jsou k dispozici v záložce „Nastavení“ formuláře pro odesílání e-mailů, jsou rozděleny do dvou sekcí:
„E-mailová zpráva“ a „Sledování“.

.. poznámka::
Možnosti dostupné v záložce „Nastavení“ se liší podle toho, zda je aktivní *Služba
Feature kampaní je aktivována v menu: Email marketing --> Konfigurace -->
Nastavení“. Podrobnější informace naleznete v části „E-mailový marketing“ na adrese :ref:`email_marketing/mailing-campaigns`.

Pokud není aktivována funkce „Poštovní kampaně“, je v poli „Nastavení“ na e-mailovém formuláři
obsahuje pouze text náhledu, odesílatele a příjemce.
:guilabel:`Přílohy“ a „Odpovědný“.

.. obrázek: email_marketing/nastaveni-bez-funkci.png
:align:center
:alt: Zobrazení nastavení aplikace Odoo Email Marketing bez aktivované kampaně.

Obsah e-mailu
~~~~~~~~~~~~~

- :guilabel:`Text náhledu“: umožňuje uživateli zadat náhledový text, který by měl přimět příjemce
otevřít e-mail. V většině případů se zobrazuje vedle předmětu. Pokud je prázdné, první
Při zadávání e-mailové adresy se místo názvu obce zobrazí znaky obsahu e-mailu. Možnost přidat emodži do tohoto pole
Je k dispozici také přes ikonu :guilabel:`(úsměv s plusem)`.
- :guilabel:"Odesílat od": určete e-mailovou adresu, která se zobrazí jako odesílatel tohoto konkrétního
e-mail
- :guilabel:"Odpověď": určit e-mailovou adresu, na kterou se budou všechny odpovědi zasílat
Všechny zprávy jsou odesílány.
- :guilabel:`Připojit soubor“: pokud je pro tuto zprávu potřeba nějaký konkrétní soubor (nebo bude užitečný), klikněte
klikněte na tlačítko „Přílohy“ a nahrajte požadovaný soubor (soubory).

Sledování
~~~~~~~~

- :guilabel:`Odpovědný“: určete uživatele v databázi, který bude za tento konkrétní
e-mail

.. poznámka::
Pokud je funkce „Poštovní kampaň“ aktivována, existuje další pole „Kampaň“.
je viditelný v sekci „Sledování“ pod záložkou „Nastavení“.

....... obrázek: email_marketing/settings-tab-with-campaign.png
:synchronizace: střed
:alt: Zobrazení nastavení v Odoo Email Marketing při zapnutém kampani.

Přidání pole „Kampaň“ umožňuje uživatelům přiřadit tento e-mail k určité kampani.
pokud si přejete, můžeme vám zaslat newsletter.

Pokud požadovaná kampaň není v prvním seznamu dostupná, vyberte možnost „Vyhledat“.
Více pak odhalí kompletní seznam všech kampaní v databázi.

Nebo zadejte název požadované kampaně do pole :guilabel:`Kampaň`, dokud se Odoo
Zobrazí se požadovaná kampaň v rozevíracím seznamu. Pak vyberte požadovanou kampaň.

Odeslat, naplánovat, otestovat
====================

Po dokončení odeslání můžete využít následující možnosti pomocí tlačítek umístěných v
v horním levém rohu e-mailového formuláře: „Odeslat“ (e-mailová marketingová kampaň), „Zaplánovat
<email_marketing/schedule>, a :ref:`Test <email_marketing/test>`.

.._email_marketing/odeslat:

Odeslat
----

Tlačítko „Odeslat“ odhalí okno s dotazem „Chcete rozeslat e-maily?“.

.. obrázek: email_marketing/send-popup.png
:align:center
:alt:Zobrazení okna, které se objeví po kliknutí na tlačítko pro odeslání e-mailu.

Když je tlačítko „Odeslat všem“ kliknuté, Odoo odesílá e-mail na požadovanou adresu.
Jakmile Odoo odesílá poštu, stav se změní na „Odeslané“.

.. _email_marketing/schedule:

Rozpis
--------

Tlačítko „Rozvrh“ odhalí okno „Kdy chcete svou poštu poslat?“.
okno.

.. obrázek: email_marketing/schedule-popup.png
:align:center
:alt:Výhled na okno, které se objeví po kliknutí tlačítka pro plánování v e-mailovém formuláři.

V tomto okně zvolte pole „Odeslat“ a zobrazí se kalendářové okno.

.. obrázek: email_marketing/kalendar-v-povezovacich-oknech.png
:align:center
:alt:Výhled na okno, které se objeví po kliknutí tlačítka pro plánování v e-mailovém formuláři.

V okně kalendáře vyberte budoucí datum a čas, kdy chcete, aby Odoo tuto e-mailovou zprávu odeslala.
Klikněte na tlačítko „Použít“. Když je vybrána datum a čas, klikněte na tlačítko „Zadat termín“
a stav pošty se změní na „Ve frontě“.

.. _email_marketing/test:

Test
----

Tlačítko „Zkontrolovat“ zobrazí okno „Přeposlat poštu“.

.. obrázek:email_marketing/test-popup.png
:align:center
:alt:Výhled na okno, které se objeví po kliknutí tlačítka „Odeslat“ v e-mailovém formuláři.

Do této okamžité zprávy zadejte e-mailové adresy kontaktů, kterým by měl Odoo zaslat tuto
testovací e-mail do pole „Příjemci“. Do pole můžete přidat více kontaktů, pokud
žádané.

Jakmile jsou do pole „Příjemci“ zadány všechny požadované e-mailové adresy, klikněte
tlačítko „Odeslat test“.

.. varování:
Výchozí denní limit se vztahuje na všechny e-maily odeslané prostřednictvím **všech služeb**.
aplikace**. Pokud tedy zbývají neodeslané e-maily po dosažení limitu,
Tyto zprávy se **nezasílají automaticky** následující den. Je třeba je vynutit, například
otevření e-mailu a kliknutí na „Znovu“.

... e-mailový marketing / poštovní kampaně:

Mailingové kampaně
=================

Aplikace *Email Marketing* umožňuje uživatelům vytvářet kampaně pro rozesílání e-mailů.

Chcete-li vytvářet a přizpůsobovat kampaně e-mailového marketingu, funkce *Kampaně pro rozesílání e-mailů* je
aktivované v nastavení aplikace Email Marketing. Chcete-li tak učinit, přejděte na
V nabídce „E-mailový marketing -> Konfigurace -> Nastavení“ zaškrtněte políčko vedle
„Kampaně pošty“ a klikněte na tlačítko „Uložit“.

.. obrázek: email_marketing/kampane-vlastnosti.png
:align:center
:alt: Zobrazení funkce nastavení kampaně v Odoo Email Marketingu.

Jakmile je aktivována funkce „Poštovní kampaně“, vznikne nová možnost „Kampaně“ v nabídce
je uveden v hlavičce.

Když na něj kliknete, Odoo zobrazí samostatnou stránku s názvem „Kampaně“, která obsahuje všechny e-maily.
kampaně v databázi a aktuální fáze, ve které se nachází, jsou zobrazeny v výchozím kanbanovém pohledu.

.. obrázek: email_marketing/kampane.png
:align:center
:alt: Pohled na kampaň v Odoo Email Marketing.

.. poznámka::
Tato informace je také k dispozici v seznamu, pokud na ni kliknete na :guilabel:`☰ (horizontální čáry)`
ikonu v pravém horním rohu.

Kliknutím na jakoukoli kampaň z stránky „Kampaně“ se zobrazí její formulář.

Existují dvě různé možnosti vytváření a přizpůsobování kampaní v aplikaci Email Marketing.
nebo přímo z stránky „Kampaně“ nebo prostřednictvím
:ref:`Nastavení záložky <email_marketing/campaign-settings> v e-mailovém formuláři.

.. _e-mailový marketing/kampaňová stránka:

Vytvořte kampaň (z kampaní).
---------------------------------------------

Při zapnutí funkce *Poštovní kampaně* se v hlavičce zobrazí nová možnost
aplikace Email Marketing. Kampaně lze vytvářet přímo na stránce Kampaně ve
Aplikace pro e-mail marketing.

Chcete-li tak učinit, přejděte na: „Aplikace pro e-mailový marketing -> Kampaně -> Nová“.

Kanban
~~~~~~~~~~~

Když je v kanbanovém výhledu „Nový“ kliknut na tlačítko „Kampaně“,
stránka, na které se objeví kartička Kanbanu v :guilabel:`Nový`.

.. obrázek: email_marketing/kampane-kanban-popup.png
:align:center
:alt: Pohled na kampaně v e-mailovém marketingu Odoo.

Nové karty kampaně lze také vytvořit kliknutím na tlačítko :guilabel:`+ (plus sign)` v horní části jakékoliv
Kanbanová fáze na stránce „Kampaně“.

Když se objeví nová kampaň Kanban Card, máte možnost zadat název kampaně a
:guilabel:„Zodpovědný“ a :guilabel:„Štítky“ se stávají dostupnými.

Kliknutím na tlačítko „Přidat“ přidejte kampaň do fáze Kanban.

K odstranění kampaně stačí klepnout na ikonu:guilabel:`🗑️ (koš)“.

Chcete-li kampaně upravit, klikněte na tlačítko „Upravit“, které odhalí kampaň.
formulář pro další úpravy.

.. poznámka::
Aby se kampaň mohla zobrazit v kanbanovém panelu, musí být do něj zadána.
:guilabel:`Upravit“ tlačítko, které odhalí kampaňovou formu pro další úpravy.

Zobrazení seznamu
~~~~~~~~~

Pro zobrazení seznamu kampaní na stránce „Kampaně“ klikněte na tlačítko „☰ (horizontální čáry)“.
ikonou v pravém horním rohu. To zobrazí všechny informace o kampani ve formátu seznamu.

.. obrázek: email_marketing/kampan-stranky-seznam.png
:align:center
:alt: Pohled na kampaňovou stránku v listovém zobrazení v aplikaci Odoo Email Marketing.

Pro vytvoření kampaně z stránky „Kampaně“ v seznamovém pohledu klikněte na
Tlačítko „Nový“ vám umožní zobrazit prázdnou kampaňovou stránku.

.. obrázek: e-mailový marketing/prázdný formulář kampaně.png
:align:center
:alt: Pohled na prázdný kampaňový formulář v Odoo Email Marketing.

Z této kampaně vytvoříte tři :guilabel:`Název kampaně`, :guilabel:`Odpovědný za kampaň`
Můžete přidat štítky.

V horní části formuláře jsou vidět různé chytré tlačítka s metrickými vztahy, které ukazují konkrétní
analytické údaje o kampani. Ty chytré tlačítka jsou: :guilabel:`Příjmy`
„Citace“, „Příležitosti“ a „Kliknutí“.

.. poznámka::
Jakmile je zadána a uložena kampaň s názvem „Campaign Name“, objeví se další tlačítka v horní části.
kampaň.

Ty další tlačítka jsou: „Odeslat newsletter“ a „Odeslat SMS“.

Kampaň ve formě
-------------

Na kampaně (po kliknutí na tlačítko „Upravit“ z karty Kanban nebo výběrem existující)
kampaně z karty „Kampaně“ jsou k dispozici další možnosti a metriky.

.. obrázek: email_marketing/kampanovy_formular.png
:align:center
:alt: Pohled na kampaň ve službě Odoo Email Marketing.

Na horní části formuláře jsou vidět chytré tlačítka, která zobrazují konkrétní analýzy.
kampani. Chytré tlačítka jsou: :guilabel:`Příjmy“, :guilabel:`Faktury“.
:guilabel:`Možnosti“ a „Kliknutí“.

Také jsou tlačítka pro :guilabel:`Odeslat poštu“, :guilabel:`Odeslat SMS“, :guilabel:`Přidat příspěvek“ a
:guilabel:`Přidat push“ (příchozí oznámení).

.. poznámka::
Pokud tlačítka „Odeslat poštou“ a „Odeslat SMS“ nejsou na první pohled dostupná, zadejte
a:guilabel:"Název kampaně", pak uložte (ručně nebo automaticky). To odhalí tyto
tlačítka.

Stav kampaně je možné zkontrolovat v horním pravém rohu formuláře kampaně.

.._email_marketing/kampaně:

Vytvořte e-mailovou kampaň (z nabídky Nastavení).
-------------------------------------------

Pro vytvoření nové kampaně z karty „Nastavení“ formuláře pro odesílání e-mailů klikněte na
Pole „Kampaň“ a začněte psát název nové kampaně. Pak vyberte buď
Vyberte možnost „Vytvořit [Název kampaně]“ nebo „Vytvořit a upravit…“ z nabídky.
se objevuje.

.. obrázek: email_marketing/nastaveni-mailingu.png
:align:center
:alt: Pohled na vytváření kampaně v nastavení e-mailového formuláře.

Vyberte možnost „Vytvořit“ a přidejte tuto novou kampaň do databáze. Upravte její nastavení
v budoucnu.

Vyberte možnost „Vytvořit a upravit…“ pro přidání této nové kampaně do databáze a zobrazte
Pop-up okno s názvem „Vytvořit kampaň“.

.. obrázek: email_marketing/mailing-campaign-popup.png
:align:center
:alt: Zobrazení okna s upozorněním na e-mailovou kampaň v aplikaci Odoo Email Marketing.

Zde se nová kampaň dále upravuje. Uživatelé si mohou nastavit:guilabel:Kampaň
Název, zadat „Odpovědný“ do pole „Zodpovědné osoby“ a přidat „Štítky“.

Tlačítka pro „Přidat příspěvek“ nebo „Odeslat push oznámení“ jsou také k dispozici.

Také existuje stav umístěný v pravém horním rohu okna „Vytvořit kampaň“.
okno.

Pokud jsou všechny změny připraveny k finálnímu uložení, klikněte na tlačítko „Uložit a zavřít“.
celou kampaň a klikněte na tlačítko „Smazat“.

.. viz též:
   - :doc:`email_marketing/mailing_lists`
   - :doc:`email_marketing/odhlášení“
   - :doc:`email_marketing/ztratene_leady_email`
   - :doc:`email_marketing/analyze_metrics`

.. toctree::


emailový marketing / rozesílání e-mailů
email_marketing/odhlášení
email_marketing/ztráta_kontaktů
email_marketing/analyzovat_metriky
