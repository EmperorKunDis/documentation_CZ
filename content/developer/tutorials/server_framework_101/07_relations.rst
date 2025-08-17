===================================
Kapitola 7: Vztahy mezi modely
===================================

V předchozím kapitole :doc:`<06_basicviews>` jsme se věnovali vytváření vlastních pohledů.
zobrazení pro základní pole. V reálném podnikatelském scénáři však potřebujeme více než
jedna varianta. Kromě toho je nutné vytvářet mezi modely vazby. Lze snadno představit si jednu variantu obsahující
zákazníky a druhý obsahuje seznam uživatelů. Možná budete muset odkazovat na zákazníka
nebo uživatel na jakémkoliv stávajícím obchodním modelu.

V našem modulu nemovitostí chceme následující informace o nemovitosti:

- kupující nemovitosti
- Makléř, který nemovitost prodal.
- druh nemovitosti: rodinný dům, byt, mezonet, zámek...
- seznam štítků charakterizujících vlastnost: útulné, zrekonstruované…
- seznam přijatých nabídek

Mnoho2jedna
========

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:třída:~odoo.fields.Many2one

.. poznámka::

**Úkol**: na konci této části:

    - nový „typ nemovitosti“ by měl být vytvořen s odpovídajícím menu, akcí a pohledy.

.. obrázek:: 07_vztahy/typ_souboru.png
:align: střed
:alt: Druh nemovitosti

    - Do modelu „majetek.vlastnictví“ by měly být přidány tři pole Many2One: typ vlastnictví, kupující a prodávající.

.. obrázek:: 07_vztahy/vlastnictví_mnoho-na-jedno.png
:align: střed
:alt:Vlastnictví

V našem modulu nemovitostí chceme definovat pojem druhu nemovitosti. Druh nemovitosti
Jedná se například o dům nebo byt. Je běžnou součástí podnikání rozdělit
podle typu, zejména pro vylepšení filtrování.

Nemovitost může mít pouze jeden typ, ale stejný typ lze přiřadit k mnoha nemovitostem.
Tento koncept podporuje **many2one**.

Many2One je jednoduchý odkaz na jiný objekt. Například k definici odkazu na
V našem testovacím modelu můžeme napsat:

partner_id = fields.many2one('res.partner', string='Partner')

Ve většině případů mají pole typu many2one koncovku „_id“. Přístup k datům v partnerovi
Pak je snadno proveditelný::

print(my_test_object.partner_id.name)

.. viz též:

`cizí klíče <https://www.postgresql.org/docs/12/tutorial-fk.html>`

V praxi můžeme mnoho-na-jedno vidět jako seznam, který se zobrazuje v pohledu na formulář.

...cvičení: Přidejte tabulku typu nemovitosti.

    - Vytvořte model „estate.property.type“ a přidejte následující pole:

    ========================= ========================= =========================
pole                    typ                        atributy
    ========================= ========================= =========================
název                    Char                     povinné
    ========================= ========================= =========================

    - Přidejte menu, jak je zobrazeno v této sekci Goal.
    - Přidejte pole „property_type_id“ do vašeho modelu a jeho formuláře, seznamu
a vyhledávací pohledy

Toto cvičení je dobrým shrnutím předchozích kapitol: musíte vytvořit
:dokument: `model <03_basicmodel>`, nastavte
:dokumentu „<04_securityintro>“ a přidejte
:doc:`akci a nabídku <05_prvniui>“.
:doc:`vytvořit pohled <06_základnípohledy>.

Tip: nezapomeňte nové soubory v jazyce Python přidat do „__init__.py“, nová data do
„__manifest.py__“ nebo přidat práva k přístupu :-)

Znovu spusťte server a aktualizujte stránku, abyste viděli výsledky.

V modulu nemovitostí chybí ještě dvě informace o nemovitosti, které bychom chtěli mít:
kupující a prodávající. Kupujícím může být kdokoli, na druhou stranu
prodejce musí být zaměstnancem realitní kanceláře (tedy uživatelem Odoo).

V Odoo existují dvě modely, které běžně označujeme jako:

- „res.partner“: Partnerem může být fyzická nebo právnická osoba. Může jít například o společnost, jednotlivce nebo
a dokonce i kontaktní adresu.
- „uživatelé“: uživatelé systému. Uživatele mohou být „interní“, tj. mají
přístup k Odoo backendu. Nebo mohou být „portálem“, tj. nemají přístup k backendu, ale pouze k
frontend (např. k přístupu ke svým předchozím objednávkám v elektronickém obchodování).

...cvičení: Přidejte kupujícího a prodejce.

Přidejte kupujícího a prodejce do „modelu nemovitosti“ pomocí dvou běžných modelů
takto uvedené. Měly by být přidány v novém záložce prohlížeče ve formátu zobrazeném v části **Úkol**.

Výchozí hodnota pro obchodníka musí být aktuální uživatel. Kupující by neměl být kopií.

Tip: pro získání výchozí hodnoty se podívejte na poznámku níže nebo na příklad.
`tady <https://github.com/odoo/odoo/blob/5bb8b927524d062be32f92eb326ef64091301de1/addons/crm/models/crm_lead.py#L92>.

.. poznámka::

Objekt „self.env“ umožňuje přístup k parametrech požadavku a dalším užitečným
věci:

    - „self.env.cr“ nebo „self._cr“ je objekt databázového *kursoru*; je
sloužící k dotazování databáze
    - „self.env.uid“ nebo „self._uid“ je aktuální uživatelův identifikátor v databázi
    - „self.env.user“ je záznam aktuálního uživatele
    - „self.env.context“ nebo „self._context“ je kontextová složka
    - „self.env.ref(xml_id)“ vrací záznam odpovídající XML id
    - „self.env[název_modelu]“ vrací instanci daného modelu

Nyní se podívejme na další typy odkazů.

Many-to-many
=========

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:třída:~odoo.fields.Many2many

.. poznámka::

**Úkol**: na konci této části:

    - nový „model vlastnictví“ by měl být vytvořen s odpovídajícím menu a akcí.

.. obrázek: 07_vztahy/vlastnostní_tag.png
:align: střed
:alt: Atribut vlastnosti

    - k modelu „majetek.vlastnictví“ by měly být přidány tagy:

.. obrázek: 07_vztahy/vlastnost_mnoho-množství.png
:align: střed
:alt:Vlastnictví

V našem modulu nemovitostí chceme definovat pojem vlastnických značek. Vlastnické značky
Jedná se například o vlastnost „pohodlný“ nebo „zrekonstruovaný“.

Může mít nemovitost mnoho štítků a jeden štítek může být přiřazen k mnoha nemovitostem.
Tento princip podporuje koncept **many2many**.

Many-to-many je oboustranná vícenásobná vazba: každý záznam na jedné straně může být spojen s libovolným
počet záznamů na druhé straně. Například pro definici odkazu na
Model „účet.dph“ na našem testovacím modelu můžeme napsat:

daňové identifikátory = pole.Mnoho2množství ("účetní daně", řetězec = "Daně")

Podle zvyklosti mají pole typu mnoho-k-mnoho příponu „_ids“. To znamená, že může být zahrnuto více daní.
přidán do našeho testovacího modelu. Chová se jako seznam záznamů, což znamená, že přístup k datům musí být
opakovaně uzavřený do smyčky

pro daně v objektu my_test_object.tax_ids:
print(tax.name)

Seznam rekordů se nazývá záznamová sada, tedy uspořádaná sbírka rekordů. Podporuje
standardní operace s kolekcemi v Pythonu, jako je „len()“ a „iter()“, navíc další sada
operace jako „recs1 | recs2“.

... cvičení: Přidejte tabulku s tagy nemovitostí.

    - Vytvořte model „estate.property.tag“ a přidejte následující pole:

    ========================= ========================= =========================
pole                    typ                        atributy
    ========================= ========================= =========================
název                    Char                     povinné
    ========================= ========================= =========================

    - Přidejte menu, jak je zobrazeno v této sekci Goal.
    - Přidejte pole „tag_ids“ do vašeho modelu „estate.property“ a v jeho formuláři a seznamovém výpisu

Tip: v pohledu použijte atribut „widget=many2many_tags“ podobně jako je ukázáno zde
`tady <https://github.com/odoo/odoo/blob/5bb8b927524d062be32f92eb326ef64091301de1/addons/crm_iap_lead_website/views/crm_reveal_views.xml#L36>`.
Atribut „widget“ bude podrobně vysvětlen v pozdější kapitole školení :doc:`<11_sprinkles>“.
Až do této chvíle můžete zkusit přidávat a odebírat a uvidíte výsledky :-)

One2many
========

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:třída:~odoo.fields.One2many

.. poznámka::

**Úkol**: na konci této části:

    - nový model „nabídka nemovitosti“ by měl být vytvořen s odpovídajícím formulářem a zobrazením seznamu.
    - nabídky by měly být přidány do modelu „nemovitost“.

.. obrázek:: 07_vztahy/nabídka_vlastnictví.png
:align: střed
:alt:Nabídka nemovitostí

V našem modulu nemovitostí chceme definovat pojem nabídky nemovitosti. Nabídka
Je to částka, kterou potenciální kupující nabídne prodávajícímu. Nabídka může být nižší nebo vyšší než
Očekávaná cena.

Nabídka se vztahuje na jednu nemovitost, ale stejná nemovitost může mít mnoho nabídek.
Znovu se objevuje koncept **many2one**. V tomto případě ale chceme zobrazit seznam
nabídek na danou nemovitost, tak použijeme koncept **jedno-mnoho**.

Odrážkou je obrázek jedna k mnoha. Například jsme definovali
na našem testovacím modelu je odkaz na model „res.partner“ díky poli „partner_id“.
Můžeme definovat obrácenou vazbu, tj. seznam testovacích modelů spojených s naším partnerem:

test_ids = pole.One2many("test_model", "partner_id", string="Testy")

První parametr se nazývá „comodel“ a druhý parametr je pole, které chceme
inverzní.

Podle konvence mají pole typu „one2many“ příponu „_ids“. Chovají se jako seznam záznamů, což znamená
Přístup k datům musí být prováděn v cyklu:

for test in partner.test_ids:
print(test.jméno)

.. nebezpečí::

Protože je :class:`~odoo.fields.One2many` virtuální vztah,
musí být definováno pole :class:`~odoo.fields.Many2one` v komodulu.

... cvičení: Přidejte tabulku nabídky nemovitostí.

    - Vytvořte model „nabídka nemovitosti“ a přidejte následující pole:

    ========================= ================================ ============= =================
Pole                   Typ                              Atributy       Hodnoty
    ========================= ================================ ============= =================
cena                    Float
status                   výběr                             bez kopie      přijato, zamítnuto
partner_id                 Many2One('res.partner')           povinné
property_id                Many2One('estate.property')  required
    ========================= ================================ ============= =================

    - Vytvořte seznamový a formulářový pohled s poli „cena“, „partner_id“ a „stav“.
musíte vytvořit akci nebo nabídku.
    - Přidejte pole „offer_ids“ do vašeho modelu „estate.property“ a v jeho formuláři zobrazte
které jsou popsány v části **Cíl** této sekce.

Je zde několik důležitých věcí, které je třeba si všimnout. První z nich je, že nepotřebujeme akci nebo nabídku pro všechny
modely. Některé modely jsou určeny k přístupu pouze skrze jiný model. To je případ i našeho
cvičení: vždy se nabídka dostane přes nemovitost.

Druhým důvodem je skutečnost, že pole „property_id“ je povinné, ale v
názorů. Jak si Odoo může být jistý, že se naše nabídka vztahuje k určitému majetku? To je součástí
magie používání rámce Odoo: někdy jsou věci definovány implicitně. Když vytváříme
rekord přes pole one2many, odpovídající mnoho2jedna se vyplní automaticky
Pro pohodlí.

Stále živí? Tato kapitola rozhodně není nejjednodušší. Zaváděla několik nových pojmů
a zároveň na všechno, co bylo předtím zavedeno.
:doc:`další kapitola bude lehčí, nebojte se :-)
