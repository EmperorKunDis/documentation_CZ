=================================
Díl 9: Připraveni na akci?
=================================

Dosud jsme většinou pracovali s modulem tím, že jsme deklarovali pole a zobrazení. Teprve před chvílí jsme se začali věnovat obchodním funkcím
logice v předchozím kapitole <08_compute_onchange> díky
vypočítané pole a události při změně. V jakémkoliv reálném podnikatelském scénáři bychom chtěli propojit nějaké obchodní
Logiku tlačítek na akci. V našem příkladu s nemovitostmi bychom rádi mohli:

- zrušit nebo nastavit vlastnost jako prodanou
- přijmout či odmítnout nabídku

Můžeme argumentovat tím, že tyto věci už děláme ručně změnou stavu, ale
To není moc pohodlné a navíc chceme přidat další zpracování: když je nabídka
přijali jsme, že chceme stanovit prodejní cenu a kupujícího nemovitosti.

Objekt
===========

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:doc:`../../reference/backend/actions` a :ref:`reference/exceptions`.

.. poznámka::

**Úkol**: na konci této části:

    - Mělo by být možné zrušit nebo nastavit vlastnost jako prodanou.

.. obrázek:: 09_akce/vlastnictví.gif
:align: střed
:alt:Zrušit a nastavit jako prodané

Zrušená nemovitost nelze prodat, prodanou nemovitost nelze zrušit.
jasnosti byl do výhledu přidán stavový prvek „state“.

    - Měli byste být schopni přijmout nebo odmítnout nabídku:

.. obrázek: 09_akce/nabidka_01.gif
:align: střed
:alt:Přijmout nebo odmítnout nabídku

    - Jakmile bude nabídka přijata, měla by být stanovena prodejní cena a kupující:

.. obrázek: 09_akce/nabidka_02.gif
:align: střed
:alt:Přijmout nabídku

V našem modulu nemovitostí chceme propojit obchodní logiku s několika tlačítky. Nejběžnější způsob
a dále:

- Přidejte tlačítko do zobrazení, například do „hlavy“ zobrazení:

... blok kódu::xml

<form>
<hlavička>
<tlačítko jméno="akce_dělat_něco" typ="objekt" string="Dělat něco"/>

<listina>
<pole název/>
</list>


- a připojit tlačítko k logice aplikace:

... kódový blok:: python

od odoo importujeme pole a modely

class TestAction(models.Model):
_name = "test.akce"

jméno = fields.Str()

def akce_k_něčemu(self):
pro rekord v sobě:
jméno_zaznamenání = "Něco"
vrátí True

Přiřazením „type="object““ na tlačítko bude Odoo framework spouštět metodu v Pythonu
s atributem „name=“akce_udělat něco““ na daném modelu.

První důležitou věcí, kterou je třeba si všimnout, je fakt, že název metody není předponován podtržítkem.
(_). Tímto způsobem je naše metoda veřejnou metodou, která může být přímo volána z Odoo
rozhraní (pomocí volání RPC). Dosud všechny metody, které jsme vytvořili (compute, onchange), byly
interně, takže jsme používali metody s připojeným znakem podtržením (předpona _), které jsou vždy definovány
metody jsou soukromé, pokud nejsou potřebné pro volání z uživatelského rozhraní.

Dále si všimněte, že se vracíme na „sebe“. Vždy předpokládejte, že metoda může být volána pro více záznamů; je
lepší pro opakované použití.

Konečně metoda veřejná by měla vždy vrátit něco, aby se mohla volat pomocí XML-RPC.
Pokud nejste si jisti, zkuste „vracet True“.

Ve zdrojovém kódu Odoo je jich tisíce, jedním z příkladů je například
„tlačítko v pohledu <https://github.com/odoo/odoo/blob/cd9af815ba591935cda367d33a1d090f248dd18d/addons/crm/views/crm_lead_views.xml#L9-L11>“
a jeho
„Python metoda odpovídající <https://github.com/odoo/odoo/blob/cd9af815ba591935cda367d33a1d090f248dd18d/addons/crm/models/crm_lead.py#L746-L760>“

..cvičení: Zrušit a nastavit vlastnost jako prodanou.

    - Přidejte tlačítka „Zrušit“ a „Prodáno“ do modelu „nemovitost“. Zrušenou nemovitost
Nemůže být vloženo do prodeje a prodaná nemovitost nelze zrušit.

Viz první obrázek s cílem pro očekávaný výsledek.

Tip: Chcete-li vyvolat chybu, můžete použít třídu :ref:`UserError<reference/exceptions>`.
funkci. V zdrojovém kódu Odoa je jich spousta :-)

    - Přidejte tlačítka „Akceptovat“ a „Odmítnout“ do modelu „nabídka nemovitosti“.

Podívejte se na druhou fotografii s názvem **Cíl** pro očekávaný výsledek.

Tip: chcete-li použít ikonu jako tlačítko, podívejte se
`na tomto příkladu <https://github.com/odoo/odoo/blob/cd9af815ba591935cda367d33a1d090f248dd18d/addons/event/views/event_views.xml#L521>.

    - Když je nabídka přijata, nastavte kupujícího a prodejní cenu odpovídající nemovitosti.

Podívejte se na třetí obrázek cíle pro očekávaný výsledek.

Pozor, v reálném životě lze akceptovat pouze jednu nabídku na danou nemovitost!

Typ akce
===========

V souboru 05_firstui jsme vytvořili akci, která byla spojena s nabídkou.
se možná ptáte, zda je možné spojit akci s tlačítkem. Dobrá zpráva, ano! Jedním ze způsobů, jak to udělat
Je:

... blok kódu::xml

<tlačítko typu "akce" jméno="%(test.test_model_action)d" text="Můj akční krok"/>

Používáme „typ=akce“ a odkazujeme na vnější identifikátor v „názvu“.

V další kapitole :doc:`<10_constraints>` se dozvíme, jak zabránit
kódování nesprávných dat v Odoo.
