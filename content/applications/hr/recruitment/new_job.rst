=============
Pracovní pozice
=============

V aplikaci pro nábor zaměstnanců Odoo jsou všechny pracovní pozice zobrazeny na výchozím panelu.
Aplikace pro nábor zaměstnanců, která obsahuje jak aktivní, tak i neaktivní pozice.

Každá pracovní pozice je zobrazena na samostatné kartě Kanban. Pokud je pracovní pozice aktivní a
kandidáti se mohou přihlásit; v pravém horním rohu karty se objeví banner s nápisem „Zveřejněno“.

Zobrazte seznam podaných žádostí o zaměstnání kliknutím na jakoukoli pracovní pozici.

.. obrázek: new_job/jobs.png
:alt:Hlavní pohled na aplikaci pro nábor zaměstnanců, který zobrazuje všechny pracovní pozice.

.._pracovní pozice/vytvořit pracovní pozici:

Vytvořit novou pracovní pozici
=========================

Vytvoření nové pracovní pozice z hlavního panelu v aplikaci **Nábor zaměstnanců** provedete kliknutím na
tlačítko „Nové“ v pravém horním rohu a okno s názvem „Vytvořit pracovní pozici“.
se objevuje.

Nejprve zadejte název pozice (např. „Obchodní manažer“, „Mechaničtí inženýři“).
Inženýr,“ atd.) v oboru.

Dále zadejte e-mailovou adresu aplikace tím, že do pole napíšete první polovinu e-mailové adresy.
první pole, pak vyberte druhou polovinu e-mailu pomocí výběrového seznamu v druhém poli.
Uchazeči mohou poslat životopis na konkrétní e-mailovou adresu a Odoo vytvoří žádost.
je automaticky přiděleno.

Když je vše hotovo, klikněte na tlačítko „Vytvořit“ nebo „Zrušit“.
tlačítko pro jeho smazání.

.. obrázek: new_job/position.png
:alt: Vytvořit novou pracovní pozici.

Jakmile je pracovní pozice vytvořena, zobrazí se jako karta ve formátu Kanban na hlavní obrazovce.
Dashboard aplikace pro nábor zaměstnanců.

.._nástup do nového zaměstnání/změna pracovního místa/edit:

Upravte novou pracovní pozici
-----------------------

Po vytvoření pracovní pozice je čas zadat podrobnosti o pozici. Klikněte na
Ikona „fa-ellipsis-v“ v horním pravém rohu příslušného
kartu s několika možnostmi a pak klikněte na „Nastavení“ pro editaci podrobností.

.. obrázek: new_job/edit-job.png
:alt:Upravte kartu pracovního místa.

.. poznámka::
V pravém horním rohu karty je tlačítko, které umožňuje zveřejnit pracovní pozici na webu.
Pozice je zveřejněna, vidíte zelené tlačítko „Zveřejněno“. Pokud pozice nebyla zveřejněna,
ještě není zveřejněno, objeví se šedé tlačítko „Nepublikováno“. Klikněte na něj pro zveřejnění
nebo zveřejnit nebo nezveřejnit pracovní místo.

Karta náboru
~~~~~~~~~~~~~~~

Vše podstatné o pracovním místě je uvedeno v záložce „Nabídka práce“.

Žádný z polí není povinný, ale je důležité konfigurovat a naplnit
:guilabel:„Oddělení“, „Místo pracovní pozice“ a „Typ zaměstnání“.
:guilabel:„Shrnutí pozice“ a „Poznámky k pozici“, protože jsou všechny viditelné pro potenciální uchazeče na webu.

.. poznámka::
Některá pole uvedená níže nemusí být zobrazena v závislosti na konfiguraci databáze a dalších
nainstalované aplikace.

Pole lze vyplnit následovně:

- Vyberte příslušný oddělení pro danou pracovní pozici.
webové stránky.
- :guilabel:`Lokalita práce“: Vyberte fyzickou adresu pro pracovní pozici. Pokud je pracovní pozice vzdálená,
Zanechte pole prázdné. Toto je viditelné na webu.
- :guilabel:'Průmysl': Vyberte odvětví, do kterého patří pracovní pozice.
odpovídá oborům, které najdete na pracovních portálech. Odoo přichází s 86 přednastavenými odvětvími.
Není doporučeno přidávat novou oblast, protože může skrýt pracovní pozici při některém vyhledávání.
různé pracovní portály.
- :guilabel:`E-mailová adresa aliasu“: Zadejte e-mailovou adresu, na kterou se uchazeči mohou posílat svůj životopis.
emailem, Odoo automaticky vytvoří žádost o něj. Pokud byl při vytváření
přiřazení pracovní pozice, do pole se vloží hodnota.
- :guilabel:`Typ zaměstnání“: vyberte typ pozice pomocí rolovací nabídky.
Výchozí možnosti jsou: „Trvalé“, „Dobrovolné“ a „Sezónní“.
:guilabel:`Plný úvazek“, :guilabel:`Studenti“, :guilabel:`Učňovské vzdělávání“,
:guilabel:`Bakalářská práce“, :guilabel:`Zákonem stanovené“ a :guilabel:`Pracovník“.
lokalizace, mohou být dostupné další možnosti. Ty jsou viditelné na webu.
- :guilabel:`Rozvrh směn“: Vyberte rozvrh směn pro pracovní pozici. Odoo nabízí jeden
pracovní režim výchozí, :guilabel:`Standardní 40 hodin týdně“, ale všechny pracovní režimy v
Databáze je k dispozici.
- :guilabel:`Rozsah platu“: Zadejte oba nejnižší a nejvyšší plat nabízený na danou pozici
dva pole. Pak nastavte poslední pole na časový rámec pro platovou hladinu. Výchozí
Možnosti jsou: :guilabel:`Hodina`, :guilabel:`Den`, :guilabel:`Týden`, :guilabel:`Dvoutýdenní interval`,
:guilabel:`Měsíc“ a :guilabel:`Rok“.
- :guilabel:`Očekávané dovednosti“: Vyberte všechny požadované dovednosti pro danou pracovní pozici pomocí
nabídce. Představené dovednosti jsou: nastaveny v aplikaci Zaměstnanci
<zaměstnanci/vzdělání>.
- :guilabel:`Společnost“: Vyberte společnost, pro kterou je práce určená. Toto pole se objeví pouze v případě, že používáte
multifirmový databázový systém.
- :guilabel:`Datum zahájení mise“: Pomocí kalendáře vyberte datum začátku pracovního místa.
Pokud je pracovní pozice dočasná a má konkrétní datum ukončení, zadejte datum ukončení v druhém poli.
- :guilabel:`Počet zaměstnanců, které chcete najmout na tuto pozici.“
- :guilabel:`Webová stránka“: Vyberte webovou stránku, na které je pracovní místo zveřejněno.
- :guilabel:`Personalista“: vyberte osobu odpovědnou za nábor do této pozice.
- :guilabel:`Pozadí interviewéru“: Vyberte, kdo má provádět rozhovory. Může jich být více.
Vybrané.
- :guilabel:`Forma rozhovoru“: vyberte si :ref:`Rozhovor <recruitment/interview>“.
k vyplnění před pohovorem.
- :guilabel:`Šablona smlouvy“: Vyberte šablonu smlouvy, která se má použít při nabídce práce.
kandidátka.

.. obrázek: new_job/recruitment-tab.png
:alt:Podrobnosti o pracovním místě v záložce Nabídka práce.

Karta shrnutí o zaměstnání
~~~~~~~~~~~~~~~

Do pole „Popis práce“ vložte popis pracovní pozice. Tento popis je viditelný na
webová stránka.

.. obrázek: new_job/job-summary.png
:alt:Shrnutí pozice v záložce Shrnutí.

Informace o aplikaci
~~~~~~~~~~~~~~~~~~~~

V části „Podrobnosti o procesu“ v záložce „Informace o aplikaci“ se nachází informace
je zveřejněn online na pracovní pozici. Tímto způsobem se uchazeči dozví o časovém harmonogramu a krocích
pro náborový proces, takže vědí, kdy se mohou těšit na odpověď.

Následující pole jsou vyplněna automaticky, ale lze je upravit podle harmonogramu náboru.
z obchodu:

- :guilabel:`Čas na odpověď“: Zadejte počet dní před kontaktováním uchazeče.
:guilabel:`Dva dny otevřených dveří` tento prvek vždy automaticky vyplní.
- :label_guid:'Proces': Zadejte různé fáze, které kandidát prochází během náboru
procesu. Výchozí nastavení zobrazuje dvě fáze procesu: „1 Telefonní hovor“ a „1
Onsite interview.
- :guilabel:`Dny k získání nabídky“: Zadejte počet dní před tím, než se uchazeč může očekávat
přihlásit se po skončení výběrového řízení. Výchozí hodnota je:guilabel:`4 Days after Interview`.

.. obrázek: new_job/app-info.png
:alt: Do záložky s nabídkou práce zadejte podrobnosti o pracovní pozici.

.. poznámka::
Sekce „Podrobnosti procesu“ je textovým polem. Všechny odpovědi se zadávají ručně, nikoliv pomocí
Vybírat lze z roletky. Text se na webu zobrazuje přesně tak, jak je zadán.
tento záložce.

.. _případně pohovor:

Vytvořit dotazník
---------------------

Formulář interview je používán k určení, zda uchazeč odpovídá požadavkům na pracovní pozici.
formy mohou být tak specifické nebo obecné, jak si přejete, a mohou se objevit v podobě certifikátu, zkoušky
nebo obecný dotazník. Formuláře pro pohovor stanoví tým náboru.

Před vytvořením dotazníku ověřte správné nastavení. Přejděte na
V nabídce „Nástroje“ vyberte možnost „Zaměstnanecká aplikace“, v následujícím okně
v sekci „Náborový proces“, zkontrolujte, zda je zaškrtnuto pole „Odeslat dotazník pohovoru“.
Zapnuto.

Přestože v Odoo nejsou žádné přednastavené formuláře, musí být všechny dotazníky vytvořeny.
Přihlášku vyplňte odkazem na záložku „Nabídka práce“ v záložce „Pracovní pozice“.
poličku „Forma rozhovoru“, zadejte název nové formy rozhovoru.
pod záznamem se nachází několik možností: :guilabel:`Vytvořit (název formuláře pro rozhovor)`
:guilabel:'Hledat více...' a :guilabel:'Vytvořit a upravit...'. Klikněte na :guilabel:'Vytvořit a upravit...'
a objeví se okno s názvem „Vytvořit formulář pro rozhovor“.

.. obrázek: new_job/prázdný formulář pro pohovor.png
:alt:Pop-up okno prázdného dotazníku.

.. poznámka::
Volba „Hledat více ...“ se objeví pouze tehdy, pokud existují již nějaké dotazníky.
Vytvořeno. Pokud neexistují žádné dotazníky, jedinou možností je vytvoření nového dotazníku.
„Vytvořit a upravit...“, „Název“ a „:guilabel:“.

Pokračujte v vyplňování dotazníku, který se objeví jako okno s výzvou k účasti na průzkumu. Pro konkrétní pokyny
jak vytvořit průzkum, podívejte se na: `survey essentials <../../marketing/surveys/create>`.
dokument, který poskytuje krok za krokem pokyny pro vytváření a konfiguraci průzkumu.
