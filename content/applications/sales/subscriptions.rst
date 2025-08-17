Zobrazit obsah
:ukrýt obsah:

=============
Předplatné
=============

Aplikace Odoo **Subscriptions** je navržena tak, aby pomáhala řídit opakující se příjmy prostřednictvím předplatného.
produkty nebo služby. Podporuje automatické fakturace, správu obnovení a řízení životního cyklu zákazníků
sledování.

Předplatné lze vytvořit ručně nebo automaticky prostřednictvím online prodeje s různými možnostmi
pro opakované fakturace. Aplikace integruje s dalšími moduly Odoo, jako jsou **Fakturace**, **CRM**,
Prodej a Helpdesk pro podporu celého procesu od objednání po servis.

.. karty:

...... karta:Obnovit předplatné
:target: předplatné/obnova
:velké:

Pochopit jádro řízení aktivit pro předplatné

...... karta: Upsell a předplatné
:target: předplatné / upselling
:velké:

Nabídněte více hodnoty stávajícím zákazníkům na stejném prodejním příkazu

...... karta: Zrušit předplatné
:target: předplatné/zavření
:velké:

Upravte šablony předplatného podle různých produktových nabídek

......karta: Integrace e-commerce
:target: předplatné / e-commerce
:velké:

Nabídněte předplatné produkty prostřednictvím svého obchodu s elektronickým obchodem Odoo

.. viz též:
   - „Návody k Odoo: Předplatné <https://www.odoo.com/slides/subscription-20>“

Nastavte opakující se plány
======================

Chcete-li začít s předplatným produktů v Odoo, použijte opakující se plány (dříve známé jako
*periody opakování*) musí být nejprve nakonfigurovány.

Opakující se plány jsou časové okno, ve kterém předplatné funguje a obnoví se znovu.
Zatímco je předplatné aktivní, zákazník obdrží produkty nebo služby a může také získávat přístup k
další výhody jako třídění požadavků na podporu. Co se týče platby, pak u opakovaných plánů
určit, jak často zákazník bude účtován za udržení výhod své předplatného.

Pro konfiguraci opakujících se plánů přejděte do aplikace „Předplatné“ - „Konfigurace“.
Opakující se plány“.

Aplikace „Předplatné“ obsahuje několik běžných opakujících se plánů.
například: guilabel:„Měsíční“ a „Roční“.

Vytvořte nový opakující se plán kliknutím na tlačítko „New“ v části „Opakující se plány“.
přístrojová deska, která odhalila prázdný formulář s plánem „Jméno“, „PODROBNOSTI“
Hodnoty pole „SELF-SERVICE“ a „Pricing“ jsou specifikovány.

.. obrázek: předplatné/přístupy/prázdný formulář.png
:alt:Prázdný opakující se plán v aplikaci Odoo Subscription.

.. důležité:
Jednotka měření „Dny“ nelze použít jako jednotku měření pro účtování v rámci předplatného.
produkty. Denní opakování v Odoo je určeno pro pronájmy a **nelze** přidat
na objednávky s předplatným.

Toto omezení je zde proto, aby se zabránilo prodejním objednávkám, které by generovaly denní faktury.

SEKCE DETAIL
---------------

Po vhodném označení opakovaného plánu, například „Měsíční“, „Dvoutýdenní“
„Čtvrtletně“, atd.) přejděte do sekce „DETAILS“ formuláře a vyplňte následující
konfigurační pole:

- :guilabel:`Období účtování“: určuje období opakování plánu s opakováním. Zadejte
číslo v poli pro text a kontextualizovat kvantitu s jednotkou času ve
příslušného seznamového pole v poli „Týdny“, „Měsíce“ nebo „Roky“.
- :guilabel:`Automatické uzavření“: číselná hodnota v dnech, kde je předplatné nastaveno na uzavření
Pokud nebude platba provedena, bude účtován automaticky.

...... příklad::
Pokud je předplatné nastaveno na obnovu 1. každého měsíce, pak se automaticky:guilabel:
V hodnotě „Uzavření“ je nastaveno číslo 15, což znamená, že předplatné bude ukončeno 16.
Pokud nebude platba připsána do konce měsíce, bude účtován poplatek za opožděnou platbu.

- Možnost „Synchronizovat s datem začátku období“: možnost silně přesměrovat nové a opakující se termíny pro obnovení předplatného
podle tohoto plánu na první den, který je definován v období fakturace.
- Případné přidělení společnosti: nepovinné přiřazení, pokud databáze obsahuje :doc:`Společnost
Funkce <../general/companies/multi_company> je aktivní. Přiřazením této hodnoty se zobrazí
opakující se plán pro konkrétní lokalitu této společnosti.
- :guilabel:`Šablona e-mailu pro fakturaci“: přiřazuje konkrétní šablonu e-mailu k použití v předplatném
účetních komunikací. Výchozí přiřazení je zde „Faktura: Odeslání“, které obsahuje různé
dynamické pole, které automaticky vyplňuje konkrétní proměnné v poli „Předmět“
:guilabel:`Obsah` záložce, jako například jméno zákazníka, číslo faktury, celkový účet zaúčtovaný atd.

..tip:
Přestože je tento údaj volitelný, doporučuje se ho vyplnit, protože tento typ komunikace
plní dobré obchodní praktiky ohledně transparentnosti cen, pravidelného kontaktu se zákazníky
hlavně v souvislosti s účtováním poplatků a pomáhá budovat kontext finanční.
dokumentace kolem opakujících se příjmů.

.. obrázek:: předplatné/faktura_předplatného_e-mailový_vzor.png
:alt:Šablona e-mailu v Odoo, která se používá k zasílání faktur za předplatné zákazníkům.

Šablona e-mailu „Faktura: zaslání“ je přístupná po kliknutí na ikonku :icon:`fa-arrow-right`.
(při najetí myší): „Vnitřní odkaz“
Vyberte pole „Šablona“ v poli „Opakující se plány“ na formuláři.

SEKCE „VLASTNÍ OBJEDNÁVKA“
--------------------

Následující nepovinná pole umožňují zákazníkům provádět administrativní činnosti sami.
předplatné. Zapnutí kterékoliv z těchto možností může snížit počet požadavků na zákaznickou podporu nebo
zvýšit hodnotu zákazníka (LTV).

- :guilabel:Zavíratelné“: zaškrtnutím této možnosti dáte zákazníkům právo zavřít svůj vlastní
předplatné. Zvažte zapnutí této možnosti, abyste snížili poptávku zákaznického servisu a zlepšili
celkový zákaznický zážitek; zákazníci, kteří si mohou sami spravovat své předplatné tímto způsobem, jim pomáhají
zpříjemnit práci prodejcům a podporovatelům, snižuje pravděpodobnost negativních recenzí.

..tip:
Přestože je tato možnost obecně vhodná k zapnutí, prodejní týmy s dobrým zákaznickým servisem
Procesy odchodu mohou zvážit, že tuto možnost nezaškrtnou, aby tak donutili
interakce, která by mohla zachránit předplatné nebo jiný druh opakujících se příjmů (např.
v případě nižšího předplatného nebo nového zkušebního období s alternativním plánem.

- :guilabel:`Přidat produkty“: umožňuje zákazníkům přidávat nové produkty nebo upravovat stávající množství
k opakovaným objednávkám a tím umožňuje prodej na základě potřeb zákazníka. Když je zapnutá,
:doc:`Příležitost k upsellu <subscriptions/upselling> se vytváří v Odoo pokaždé, když zákazník
Provádí kvantitativní úpravu svých produktových řad prodejních objednávek.

- :guilabel:`Obnovení“: zapnutím této funkce mohou zákazníci ručně vytvářet „Quotace na obnovu“.
<předplatné/obnova předplatného> pro své předplatné.
- :guilabel:`Doplňkové služby“: přidání hodnot z nabídky v poli „Drop-Down Menu“ umožní zákazníkům
přepnout na jiný typ předplatného, v takovém případě je nutné získat novou cenovou nabídku nebo obnovit ji.
Vytvořený pro požadavek na změnu.

Ceník
-----------

Učiněte cenové úpravy produktu jako součást opakujícího se plánu přidáním je do
:guilabel:`Cenotvorba“ sloupec řádků objednávek. Postupně přidejte řádky s :guilabel:`Produkty“, včetně
příslušné varianty produktů, pak přiřadit cenový seznam (jestli je k dispozici).
:guilabel:`Opakující se cena“.

.. poznámka::
Pravidla cen, která jsou zde přidána, mají přednost před výchozím informacemi o cenách.
formu předplatného. Tento krok je zaměřen na slevy a podobné cenové zvýhodnění
strategie, které by zákazníky motivovaly k nákupu opakujícího se plánu.

Chytré tlačítko
-------------

V horní části formuláře pro opakující se plány jsou dvě chytré tlačítka, která vám pomohou
navigace opakujících se zdrojů příjmů připojených k plánu:

- :guilabel:„Předplatné“: zobrazuje počet aktivních předplatných objednávek, které spadají pod
pravidelný plán. Kliknutím na tlačítko se zobrazí tabulkové zobrazení s každou řádkou jako odkazem na
a příslušnou objednávku na prodej předplatného.
- :guilabel:„Předplatné“: seznam všech jednotlivých opakujících předplatných služeb, které jsou
aktivní a podrobnější. Hodnoty :guilabel:`Subscription` a :guilabel:`Customer` budou
Pokud zákazník objednal více předplatných na jedné faktuře, opakujte tento krok.

Konfigurace produktu
==========================

S opakujícími se plány nastavenými vytvořte produkt předplatného kliknutím na
:menuvolba:„Aplikace pro předplatné“ --> „Produkty“ --> „Produkty“, a klikněte na existující produkt
upravit nebo vytvořit nový klikem na „New“ pro otevření formuláře produktu předplatného.

.. poznámka::
Výchozí nastavení je již zapnuto a Odoo tak může uznat
její jako předplatné. Ujistěte se, že zanecháte :guilabel:`Předplatná`.
:guilabel:`Prodejní možnosti zapnuté.“

.. obrázek: předplatné/předplatné-produkt-formulář.png
:alt:Základní produkt v aplikaci Odoo Subscriptions.

V sekci „Obecné informace“ v dialogovém okně s produktem nastavte následující položky:
předplatného bude fungovat správně:

- „Typ produktu“: Toto pole obvykle obsahuje „Službu“, nicméně jiné
produktové typy se mohou lišit podle účelu předplatného (např. fyzická krabice s produktem).
předplatné, e-learningový kurz s doplňkovým fyzickým zbožím atd.
- :doc:`Zásady fakturace <sales/invoicing/invoicing_policy>“: nastavte tento parametr, pokud chcete, aby zákazník
Měli by být účtováni za své předplatné.
- :guilabel:`Jednotka měření“: jak by se produkt měl počítat v Odoo pro účely skladu.
většině předplatných se jednotka měření zobrazí jako „Jednotky“.
- :guilabel:`Prodejní cena“: zadejte opakující se náklady na předplatné, které zákazník zaplatí
za období opakování.

Volitelně nastavte informace o:

- :guilabel:Vytvořit na objednávku“ pole: To umožňuje další akce v Odoo, jako je například vytváření nových
:guilabel:`Úkol“ v zvoleném :guilabel:`Projektu“ :icon:`fa-building-o“, :guilabel:`Akce
„Registrace“ nebo „Přístup k kurzu“. Pokud zvolíte některou ze třech možností v tomto poli,
Pokud je potřeba vybrat ze seznamu, pak zvolte hodnotu pole „Nic“.
- :tabulka „Vlastnosti a varianty“ (v sekci „Ceny produktů / Ceny výrobků“) v případě předplatného
obsahuje více možností pro zákazníky (např. doručování jídla, šití oblečení na míru atd.).
- :guilabel:Koupit“ v záložce produktu, pokud je získán od dodavatele, například jako součást obchodníka.
obchodní nebo poddodavatelské operace.

V záložce „Opakující se ceny“ upřesněte možnosti účtování za předplatné.
je k dispozici možnost, klikněte na „Přidat cenový pravidlo“.

..tip:
Delší doba: obvykle se prodloužené časové úseky motivují snížením nákladů.
Zvažte snížení celkové hodnoty „Opakovaná cena“ pro zákazníky.
a zároveň podporovat finanční vyhlídky firmy.

A nakonec, pokud se předplatné má prodávat na e-commerce webu, klikněte na
Klikněte na tlačítko „Přejít na web“ v záhlaví stránky produktu.
šedý posuvník ze stavu „Nezařazeno“ do zeleného stavu „Zveřejněno“.

...předplatné/cenové nabídky:

Vytvořit cenovou nabídku na předplatné
================================

Vytvořte novou předplatitelskou službu ručně, přejděte buď do sekce „Prodej“ nebo
Vyberte v nabídce aplikace „Předplatné“ možnost „Nový“.

.. poznámka::
Produkty, které byly označeny štítkem :guilabel:`Předplatné“ na formuláři produktu a jsou také
Prodej na e-commerce webu automaticky vytvoří a potvrdí objednávku.
v zadní části Odoo.

.. důležité:
Pokud je v objednávce prodeje definován opakující se plán, automaticky se z ní stává předplatné.

Vyplňte potřebná pole jako například:guilabel:`Zákazník`
:guilabel:`Opakující se plán“ a také záložka „Řádky objednávek“.

Volitelně zadejte:

- :doc:`Šablona cenové nabídky <sales/sales_quotations/quote_template>“, pokud je k dispozici.
při vyplňování políček na formuláři.
- Datum vypršení platnosti, které ukazuje, kdy nabídka předplatného již není platná.

..tip:
Splatnost dobře ladí s :doc:`slevami <sales/products_prices/prices/discounts>`.
zajistit rychlejší nákupy, protože slevový kód vyprší spolu s nabídkou, pokud nebude
Přeměněna na objednávku k prodeji v daném časovém rozmezí.

- :doc:`Seznam cen <sales/products_prices/prices/pricing>“, pokud je k dispozici a vhodný
použít (tj. slevu v letním výprodeji, zákazníka VIP atd.)
- :guilabel:`Podmínky platby“, aby bylo možné nastavit určité časové okno, ve kterém musí být předplatné zaplaceno.
Toto není možné zaměnit s okamžikem, kdy je citační poptávka potvrzena a stává se objednávkou.
kde je možné získat peníze ihned nebo do určitého počtu dní, týdnů či měsíců.
atd.

.. obrázek: předplatné/nový-předplatitelský-formulář.png
:alt:Ukázka hotového příkladu nové cenové nabídky v Odoo.

..tip:
Definujte různé fakturační a dodací adresy pomocí zapnutí :doc:`Adres zákazníka


..._předplatné/potvrzení:

Potvrzení
============

Odeslat cenovou nabídku zákazníkovi k potvrzení stisknutím tlačítka „Odeslat e-mailem“.
potvrďte jej okamžitě kliknutím na „Potvrdit“.

..tip:
Klikněte na tlačítko „Náhled“ a zobrazí se zákaznický portál, kde si zákazník může prohlédnout své objednávky.
Vyplňte citaci, podepište a zaplaťte, a budeme s vámi komunikovat.

Pokud je k potvrzení objednávky vyžadována :guilabel:`Online podepsání“ nebo :guilabel:`Online platba“,
citace, zaškrtněte políčka vedle buď jednoho nebo obou těchto štítků v seznamu „Další informace“
pod záložkou „Prodej“ v sekci :guilabel:`SALES`.

.. viz též:
   - :doc:`/aplikace/finance/účetnictví/platby/on-line`
   - :doc:`Platební poskytovatelé a platební metody </aplikace/finance/platebni_poskytovatele>`

.. toctree::


předplatné/e-commerce
předplatné/prodlužování
předplatné/obnova předplatného
předplatné/uzavření
předplatné/automatické upozornění
předplatné/časové úlohy
předplatné/zprávy
