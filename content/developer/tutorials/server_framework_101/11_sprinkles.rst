=============================
Díl 11: Přidejte posypku
=============================

Realitní modul nyní dává smysl z hlediska podnikání. Vytvořili jsme
Dodatečně přidala několik dalších
:doc:`tlačítka akcí <09_actions>“ a
Omezení (<10_constraints>) jsou však stále trochu nepřehledná.
hrubě. Chceme přidat nějaké barvy do seznamových pohledů a udělat některá pole a tlačítka podmíněně
zmizet. Například tlačítka „Prodat“ a „Zrušit“ by měly zmizet, když je nemovitost
prodává nebo ruší, protože v tomto bodě již není možné změnit stav.

Tato kapitola pokrývá velmi malou část toho, co lze v pohledech udělat. Neváhejte
Přečtěte si odkazovanou dokumentaci pro komplexnější přehled.

**Poznámka**: dokumentace k této kapitole je uvedena v
:doc:`../../reference/user_interface/view_records`.
:doc:`../../reference/user_interface/view_architectures`.

Příslušenství
============

.. poznámka::

**Cíl**: na konci této části by měla být k vlastnostem přidána specifická seznam vlastností.
typ zobrazení:

.. obrázek:: 11_sprinkles/inline_view.png
:synchronizace: střed
:alt: Zobrazení seznamu v inline

Do modulu nemovitosti jsme přidali seznam nabídek na nemovitost. Jednoduše jsme přidali pole
„ID nabídky“ s:

... blok kódu::xml

<field name="offer_ids" />

Tento pohled se používá pro „soubor.vlastnictví.nabídka“. V některých případech chceme definovat
konkrétní pohled na seznam, který je používán jen v kontextu formuláře. Například bychom chtěli
zobrazit seznam vlastností spojených s typem vlastnosti. Chceme však zobrazit pouze tři
políčka pro jasnost: jméno, očekávaná cena a stát.

Pro tento účel lze definovat seznamy vhodných pro zobrazení „inline“. Seznam „inline“ je definován přímo uvnitř
formulářový pohled. Například:

... kódový blok:: python

od odoo importujeme pole a modely

class TestModel(models.Model):
name="test_model"
_description = „Test Model“

popis = fields.Char()
line_ids = pole.One2many ("test_model_line","model_id")


klasa TestModelLine(modeli.Model):
_name = "test_model_line"
_popis = „Test Model Line“

model_id = fields.many2one('test_model')
field_1 = fields.Char()
field_2 = fields.Char
pole_3 = pole.Char

... blok kódu::xml

<form>
<field name="description" />
<položka jméno="line_ids">
<seznam>
<pole název="pole_1"/>
<pole název="pole_2"/>
</seznam>
</p>


V objektu test_model definujeme konkrétní seznamový pohled na test_model_line.
s poli „pole_1“ a „pole_2“.

Příkladem může být
„tady <https://github.com/odoo/odoo/blob/0e12fa135882cd5095dbf15fe2f64231c6a84336/addons/event/views/event_tag_views.xml#L27-L33>“.

... cvičení:Přidejte seznam s výhledem na řádky.

    - Přidejte pole „One2many“ „property_ids“ do modelu „estate.property.type“.
    - Přidej pole do formuláře „druh nemovitosti“ tak, jak je znázorněno v **cíli** tohoto
části.

Widgety
=======

**Poznámka k použití**: Dokumentace související s touto částí je dostupná na
:ref:`reference/js/widgety`.

.. poznámka::

**Úkol**: Na konci této části by měl být zobrazen stav nemovitosti pomocí
konkrétní widget:

.. obrázek:: 11_sprinkles/widget.png
:synchronizace: střed
:alt: Widget stavové lišty

Zobrazují se čtyři stavy: Nový, Příjem nabídky, Přijetí nabídky a Prodáno.

Každou dobu, kdy jsme přidali pole do našich modelů, jsme se téměř nikdy nemuseli starat o tom, jak
Jak by takové pole vypadalo v uživatelském rozhraní? Například datumový výběr
pro pole „Datum“ a pole „Jedna na mnoho“ se zobrazí automaticky jako seznam.
Volí správný „gadget“ podle typu pole.

V některých případech však chceme konkrétní reprezentace pole, což lze provést díky
„widget“ atribut. Už jsme ho používali při práci s „tag_ids“ pole, když jsme
Atribut „widget=many2many_tags“. Pokud bychom ho nepoužili, pak by pole zobrazovalo
list.

Každý typ pole má sadou widgetů, které lze použít k jemnému nastavení jeho zobrazení. Některé widgety také
zvolit další možnosti. Kompletní seznam naleznete v odkazu :ref:`reference/js/widgets`.

... cvičení: použijte panel s informacemi o stavu.

Použijte widget „stavová lišta“, abyste zobrazili stav „nemovitosti“ vlastněné „majitelem“.
popsané v části „Cíl“.

Tip: jednoduchý příklad najdete například zde
`tady <https://github.com/odoo/odoo/blob/0e12fa135882cd5095dbf15fe2f64231c6a84336/addons/account/views/account_bank_statement_views.xml#L136>`.

Varování: Stejný pohled na pole vícekrát

Přidejte pole pouze jednou do seznamu nebo do zobrazení formuláře. Přidání ho vícekrát je
není podporována.

Seznam pořadí
==========

**Poznámka k použití**: Dokumentace související s touto částí je dostupná na
:ref:`reference/orm/models`.

.. poznámka::

**Úkol**: na konci této sekce by měly být všechny seznamy zobrazovány výchozím nastavením v
pořadí. Druhy nemovitostí lze upravovat ručně.

Při předchozích cvičeních jsme vytvořili několik zobrazení seznamů. Nicméně žádné z nich nebylo specifikováno
v jakém pořadí se musely záznamy zobrazovat vždy automaticky. To je pro mnohé firmy velmi důležitá věc.
případů. Například v našem modulu nemovitostí bychom chtěli zobrazovat nejvyšší nabídky nahoře.
list.

Model
-----

Odoo nabízí několik způsobů, jak nastavit výchozí pořadí. Nejčastěji se používá
atribut „_order“ přímo v modelu. Tímto způsobem získané záznamy budou následovat
deterministický pořad, který bude konzistentní ve všech zobrazeních včetně vyhledávání záznamů.
programově. Výchozí řazení není specifikováno, proto budou záznamy
vyhledávané v ne-deterministickém pořadí podle PostgreSQL.

Atribut „_order“ přijímá řetězec obsahující seznam polí, která budou použita k třídění.
Bude převedena na příkaz ORDER BY v SQL. Například:

... kódový blok:: python

od odoo importujeme pole a modely

class TestModel(models.Model):
name="test_model"
_description = „Test Model“
_order = "id sestupně"

popis = fields.Char()

Naše záznamy jsou řazeny podle „id“ vzestupně, tedy nejvyšší je na prvním místě.

... cvičení: Přidat pořadí modelu.

Definujte následující objednávky ve svých odpovídajících modelech:

    =================================== ===================================
Model                Pořadí
    =================================== ===================================
„majetek, nemovitost“                Sestupně ID
„nabídka nemovitosti“            Sestupně cena
„soubor.vlastnictví.tag“                  Jméno
„typ nemovitosti“                   Jméno
    =================================== ===================================

Výhled
----

Objednávání je možné na úrovni modelu, což má výhodu v konzistentním objednávání všude
Vyhledá se seznam rekordů. Je však také možné definovat konkrétní pořadí přímo
v pořadí podle „default_order“ atributu
(`příklad <https://github.com/odoo/odoo/blob/892dd6860733c46caf379fd36f57219082331b66/addons/crm/report/crm_activity_report_views.xml#L30>`).

Návod
------

Oba typy pořadí modelů a pohledů umožňují pružnost při třídění záznamů, ale stále existuje jeden případ
Musíme pokrýt: manuální objednávání. Uživatel může chtít seřadit záznamy podle obchodní činnosti
logice. Například v našem modulu nemovitostí bychom rádi typy nemovitostí řadili ručně.
Je dobré, aby se na začátku výpisu objevily nejčastěji používané typy nemovitostí.
agentura hlavně prodává rodinné domy, je vhodnější, aby se před „bytem“ objevilo slovo „dům“.

Pro tento účel se používá pole „sekvence“ v kombinaci s widgetem „handle“. Je zřejmé
Hodnota pole „sled“ musí být první hodnotou v atributu „_order“.

...cvičení:Přidat ruční objednávání.

    - Přidejte pole:

    =================================== ======================= =======================
Model                                Pole                    Typ
    =================================== ======================= =======================
"typ nemovitosti"                        Sekvence               Integer
    =================================== ======================= =======================

    - Přidejte sekvenci do „vlastnictví.typ“ v pohledu s příslušnými ovladači.

Tip: příklad najdete třeba zde:
`model <https://github.com/odoo/odoo/blob/892dd6860733c46caf379fd36f57219082331b66/addons/crm/models/crm_stage.py#L36>`__

`výhled <https://github.com/odoo/odoo/blob/892dd6860733c46caf379fd36f57219082331b66/addons/crm/views/crm_stage_views.xml#L23>`.

Atributy a možnosti
======================

Pokusit se popsat všechny dostupné funkce, které umožňují jemnou úpravu vzhledu
Proto se budeme držet nejčastějších.

Tvar
----

.. poznámka::

**Cíl**: V závěru této části bude mít vlastnostní pohled na objektu následující vzhled:

    - Podmíněné zobrazení tlačítek a polí
    - Barvy štítků

.. obrázek:: 11_sprinkles/form.gif
:synchronizace: střed
:alt:Forma s práškem


V našem modulu nemovitostí chceme upravit chování některých polí. Například nechceme
chceme mít možnost vytvářet nebo upravovat typ vlastnosti z pohledu formuláře. Namísto toho očekáváme
typu, který se má zobrazit v příslušném menu. Dále chceme dát tagům barvu. K tomu je potřeba
chování jsme mohli přizpůsobit několika polím s atributem „options“.

.. cvičení: Přidat možnosti widgetu.

    - Přidejte vhodný parametr do pole „property_type_id“, abyste zabránili vytváření a
úprava typu vlastnosti z pohledu formuláře pro vlastnost. Podívejte se na
:ref:`Dokumentace widgetu Many2One <reference/js/widgets>“ pro více informací.

    - Přidejte pole:

    =================================== ======================= =======================
Model                                Pole                    Typ
    =================================== ======================= =======================
„majetek.vlastnictví.tag“           Barva                      Celé číslo
    =================================== ======================= =======================

Pak přidejte vhodný parametr do pole „tag_ids“ pro přidání barevného výběru u štítků.
Podívejte se na dokumentaci pole :ref:`FieldMany2ManyTags <reference/js/widgets>`.
pro více informací.

V souboru 05_firstui jsme viděli, že rezervované pole jsou používána pro
konkrétní chování. Například pole „aktivní“ se používá k automatickému filtrování
neaktivní záznamy. Přidali jsme pole „stát“ jako rezervované, takže je na čase ho použít!
Pole „stát“ lze použít v kombinaci s atributem „neviditelný“ ve zobrazení, aby se zobrazilo
tlačítka podmíněně.

...cvičení:Přidat podmíněné zobrazení tlačítek.

Použijte atribut „invisible“, abyste zobrazili tlačítka hlavičky podmíněně, jak je znázorněno na obrázku
v sekci **Úkoly** (zpozorujte, jak se mění tlačítka „Prodáno“ a „Zrušeno“, když je stav změněn).

Tip: Neváhejte hledat v souborech XML Odoo „invisible=“ pro několik příkladů.

Obecně lze pole „skrýt“, „číst jen“ nebo „povinné“.
na hodnotu ostatních polí. Pozor, „neviditelné“ lze také aplikovat na další prvky
takové jako „knoflík“ nebo „skupina“.

„neviditelné“, „čtení pouze“ a „požadované“ mohou mít jakýkoli výraz v Pythonu jako hodnotu. Výraz
Uvádí podmínku, za kterých se vlastnost uplatňuje. Například:

... blok kódu::xml

<form>
<položka jméno="popis" skrytá="nejsou partnerem"/>


To znamená, že pole „popis“ je skryté, pokud je hodnota „is_partner“ nastavena na „false“.
důležité poznamenat, že pole používané v „neviditelném“ musí být přítomno ve výhledu.
mělo by být skryto před uživatelem, můžeme použít atribut „neviditelný“, který ho skryje.

... cvičení: použijte „neviditelné“.

    - Zobrazit zahradu a orientaci v „vlastnictví nemovitosti“ ve formě výhledu
zahrada zde chybí.
    - Zobrazit tlačítka „Přijmout“ a „Odmítnout“ pouze v případě, že je nastaven stav nabídky.
    - Nepovolujte přidávání nabídek, když je stav nemovitosti „Akceptováno“, „Prodáno“ nebo
„Zrušeno“. Toho lze dosáhnout pomocí atributu „readonly“.

.. varování:

Použití „čteného“ atributu v pohledu může být užitečné k zabránění zadávání dat.
chyb, ale pamatujte na to, že neposkytuje žádnou úroveň zabezpečení. Kontrola se neděje
Serverová strana, takže je vždy možné do pole napsat přes RPC volání.

Seznam
----

.. poznámka::

**Úkol**: Na konci této části by měly mít vlastnosti a nabídky barevné ozdoby.
Navíc nabídky a štítky budou možné upravovat přímo v seznamu a datum dostupnosti bude
skryté výchozím nastavením.

.. obrázek:: 11_sprinkles/dekorace.png
:synchronizace: střed
:alt: Zobrazení seznamu s dekoracemi a možností pole

.. obrázek: 11_sprinkles/editable_list.gif
:synchronizace: střed
:alt:Editovatelný seznam

Pokud má model jen pár polí, může být užitečné zadávat záznamy přímo v seznamu.
zobrazit a nemusíte otevřít formulářový pohled. V příkladu s nemovitostmi není potřeba otevírat formulářový pohled
přidat nabídku nebo vytvořit nový štítek. To lze dosáhnout díky atributu „editable“.

... cvičení: Umožnit editaci seznamového výhledu.

Zpřístupnit seznam „nabídka nemovitosti“ a „štítek nemovitosti“.

Na druhou stranu, když má model hodně polí, může být lákavé přidat příliš mnoho polí.
výhled a nejasnost. Alternativní metodou je přidat pole, ale udělat je volitelnými
skrytý. Toho lze dosáhnout díky atributu „volitelný“.

..cvičení:Povolit pole jako volitelné.

Zobrazit v seznamu „estate.property“ pole „date_availability“ jako volitelné a skryté.
výchozí.

Konečně barvy kódů jsou užitečné pro vizuální zvýraznění záznamů. Například v nemovitostech
modul, ve kterém bychom rádi zobrazili odmítnuté nabídky červeně a přijaté nabídky zeleně. To lze dosáhnout
díky atributu „dekorace - {$name}“ (viz odkaz na :ref:`reference/js/widgets`)
kompletní seznam):

... blok kódu::xml

<list dekorace-úspěch="je partnerem == True">
<pole název/>


Záznamy, kde je „is_partner“ „True“, budou zobrazeny v zeleném.

..cvičení: Přidejte nějaké dekorace.

Na seznamu „majetek.vlastnictví“:

    - Nabídkou obdrženými jsou zelené
    - Nabídky přijaté jsou zelené a tučné
    - Prodané nemovitosti jsou ztišeny

V seznamu „Nabídka nemovitosti“:

    - Nabídky, které byly odmítnuty, jsou červené
    - Přijaté nabídky jsou zelené
    - Stát by měl být neviditelný

Tipy:

    - Pamatujte na to, že všechny pole používané v atributech musí být ve výběru!
    - Pokud chcete otestovat barvu stavů „Nabídka přijata“ a „Nabídka přijata“, přidejte
pole v podobě formuláře a změníme ho ručně (později implementujeme business logiku pro tento krok).

Hledání
------

**Poznámka k použití**: Dokumentace související s touto částí je dostupná na
:ref:`reference/view_architectures/search` a :ref:`reference/view_architectures/search/defaults`.

.. poznámka::

**Cíl**: na konci této části budou filtrována dostupná vlastnost výchozím způsobem.
a vyhledávání v obytné ploše vrací výsledky, kde je obytná plocha větší než zadaná.
číslo.

.. obrázek:: 11_sprinkles/search.gif
:synchronizace: střed
:alt: Výchozí filtry a domény

A nakonec bychom rádi nějaké úpravy provedli v hledání. První věcí je, že
chceme mít filtr „Volné“ aplikován automaticky při přístupu k nemovitostem.
musí použít akci „hledání výchozího {$name}“, kde „{$name}“ je název filtru.
To znamená, že můžeme definovat, které filtry budou aktivovány v základním nastavení na úrovni akce.

Tady je příklad jednoho z
„akce <https://github.com/odoo/odoo/blob/6decc32a889b46947db6dd4d42ef995935894a2a/addons/crm/report/crm_opportunity_report_views.xml#L115>“
s
„odpovídající filtr <https://github.com/odoo/odoo/blob/6decc32a889b46947db6dd4d42ef995935894a2a/addons/crm/report/crm_opportunity_report_views.xml#L68>“.

...cvičení: Přidat výchozí filtr.

V akci „nemovitost“ nastavte výchozí filtr „Dostupné“.

Další užitečnou vylepšenou funkcí našeho modulu by bylo efektivní vyhledávání podle obytné plochy.
V praxi uživatel bude chtít vyhledávat nemovitosti s plochou alespoň dané velikosti. Je nepravděpodobné
očekávat, že uživatelé budou chtít najít nemovitost s přesným obytným prostorem. Je vždy
Je možné provést vlastní vyhledávání, ale je to nepraktické.

Vyhledávací pole „<field>“ mohou obsahovat „filter_domain“, který přebírá
doménu pro vyhledávání na zadaném poli. V dané doméně
„self“ představuje hodnotu zadanou uživatelem. V následujícím příkladu je
používá se k vyhledávání v obou polích „název“ a „popis“.

... blok kódu::xml

<hledaný řetězec="Test">
<pole název="Description" typ="Text"
filtr_doména=["||", ("jméno", "like", self), ("popis", "like", self)]"/>


.. cvičení: Změnit vyhledávání v oblasti bydlení.

Přidejte „filtr domény“ do oblasti bydlení, abyste zahrnuli nemovitosti s plochou rovnající se nebo vyšší než
větší než zadaná hodnota.

Tlačítka pro statistiky
============

.. poznámka::

**Cíl**: na konci této části bude v zobrazení vlastností typu objektu tlačítko s názvem Statistika
který zobrazuje seznam všech nabídek souvisejících s nemovitostmi daného typu po kliknutí na něj.

... obrázek: 11_sprinkles/stat_button.gif
:synchronizace: střed
:alt: Tlačítko pro zobrazení stavu

Pokud jste již některé funkční moduly v Odoo používali, pravděpodobně jste se už setkali s „stati
tlačítko. Tato tlačítka se zobrazují v pravém horním rohu formuláře a poskytují rychlý přístup k
související dokumenty. V našem modulu nemovitostí bychom rádi měli rychlý odkaz na nabídky
související s určitým typem vlastnosti, jak je uvedeno v cíli této části.

V tomto bodě návodu jsme již viděli většinu konceptů potřebných k provedení této operace.
Není jediná správná cesta a může být matoucí, pokud nevíte, odkud začít.
Postup řešení si ukážeme na cvičení. Může se vám hodit i pro jiné příklady.
příklady v základu kódu Odoo hledáním „oe_stat_button“.

Následující cvičení může být o něco náročnější než předchozí, protože předpokládá, že
Můžete si vyhledávat příklady ve zdrojovém kódu sami. Pokud se vám nedaří, pak
někdo z okolí, kdo vám pomůže :-)

Cvičení představuje pojem :ref:`reference/fields/related`. Nejjednodušší způsob, jak
pochopit, že je třeba ji považovat za konkrétní případ vypočítaného pole. Následující definice
z pole „popis“:

... kódový blok:: python

        ...

partner_id = fields.many2one('res.partner', string='Partner')
popis = pole.Text(související="partner_id.jméno")

je ekvivalentem:

... kódový blok:: python

        ...

partner_id = fields.many2one('res.partner', string='Partner')
popis = pole.Char(vypočítat ="_vypočítat_popis")

@api.depends('partner_id.name')
def _vypočítat_popis(self):
pro rekord v sobě:
record.popis = record.partner_id.jméno

Každá změna názvu partnera je do popisu přidávána.

... cvičení: Přidat tlačítko pro zobrazení statistiky k typu vlastnosti.

    - Přidejte pole „property_type_id“ do „estate.property.offer“. Můžeme ho definovat jako
vztahované pole „property_id.property_type_id“ a nastavte jej jako uložený.

Díky tomuto poli se při vytváření nabídky automaticky propojí s typem nemovitosti. Můžete přidat
pole do seznamového pohledu nabídek, aby fungovalo.

    - Přidejte pole „nabídkové ID“ do vlastnosti „druh nemovitosti“, která je proti vztahu One2many obrácená
pole definované v předchozím kroku.

    - Přidejte pole „offer_count“ do „estate.property.type“. Jedná se o počítané pole, které počítá
počet nabídek pro konkrétní typ nemovitosti (použijte „offer_ids“ k tomu).

V tuto chvíli máte všechny potřebné informace k tomu, abyste věděli, kolik nabídek je spojeno s
typ vlastnosti. Pokud máte pochybnosti, přidejte přímo do výhledu „id nabídky“ a „počet nabídek“.
Následující krok je zobrazit seznam, když na tlačítko statistiky kliknete.

    - Vytvořte tlačítko „stát“ na „typ nemovitosti“, které bude odkazovat na „nabídku nemovitosti“.
akce. To znamená, že byste měli použít atribut „type="action““ (vraťte se na začátek).
:doc:`09_akce“ pokud potřebujete připomenout.

V tomto bodě by mělo kliknutí na tlačítko statistiky zobrazit všechny nabídky. Ještě je potřeba filtrovat
nabídky.

    - Do akce „nabídka nemovitosti“ přidejte doménu, která definuje „typ nemovitosti“.
jako rovnající se „active_id“ (= aktuálnímu záznamu).
„tady je příklad <https://github.com/odoo/odoo/blob/df37ce50e847e3489eb43d1ef6fc1bac6d6af333/addons/event/views/event_views.xml#L162>“

Vypadá dobře? Pokud ne, nemusíte se bát. Další kapitola
<12_dědictví> nevyžaduje tlačítka pro statistiky :-)

… _order_by:
    https://www.postgresql.org/docs/12/queries-order.html
