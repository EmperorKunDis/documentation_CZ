
.. referenční/bezpečnostní:

================
Bezpečnost v Odoo
================

Kromě ručního řízení přístupu pomocí vlastního kódu nabízí Odoo dvě hlavní
mechanismy řízené daty, které umožňují nebo omezují přístup k datům.

Oba mechanismu jsou propojeny s konkrétními uživateli prostřednictvím skupin: uživatel patří
jakékoliv skupině a k bezpečnostním mechanismům jsou přiřazeny skupiny.
Takže aplikují bezpečnostní mechanismy na uživatele.

... třída: res.groups

...... atribut:: jméno

slouží jako čitelné identifikace skupiny (vyslovuje jméno).
účel skupiny

...... atribut:: kategorie_id

Kategorie modulu slouží k asociaci skupin s aplikací Odoo.
(soubor souvisejících obchodních modelů) a převést je na exkluzivní
výběr v uživatelském formuláři.

......: zjednodušit a zdokumentovat speciální případy a vztahy mezi
skupiny a kategorie lépe

...... atribut: implicitní identifikátory

Jiné skupiny, které se k uživateli přidají vedle této. To je
Pseudo-dědičnost je pohodlná: lze ji použít, pokud
explicitně odstranit implicitní skupiny uživatele bez odstraňování
implikátor.

...... atribut:: komentář

Případné další poznámky k skupině, např.

.._odkaz/bezpečnost/ACL:

Přístupová práva
=============

Dává přístup k celému modelu pro daný soubor operací. Pokud není přístup
práva odpovídají operaci na modelu pro uživatele (prostřednictvím jejich skupiny).
uživatel nemá přístup.

Přístupová práva jsou sčítací, přístupy uživatele jsou součtem přístupů
Přes všechny své skupiny, například uživatel, který je součástí skupiny A
přidělením čtení a zápisu a skupinou B přidělením aktualizace, uživatel
bude mít všechny tři - vytvořit, číst a aktualizovat.

.. třída: ir.model.access

...... atribut:: jméno

Účel nebo úloha skupiny.

...... atribut:: model_id

Model, jehož přístup kontroluje ACL.

...... atribut:: skupina

K těmto přístupům je udělován přístup do skupiny :class:`res.groups`, která je prázdná
:attr:`group_id` znamená, že práva jsou udělena všem uživatelům.
(např. uživatelé portálu nebo veřejnost).

Atributy :samp:`perm_{metoda}` udělují příslušný přístup k čtení, zápisu, smazání a aktualizaci.
Pokud jsou nastaveny, jsou všechny vypnuté výchozí hodnotou.

...... atribut:: perm_create
...... atribut:: perm_read
.... atribut:: perm_write
...... atribut:: perm_unlink

.. odkaz/bezpečnost/pravidla:

Rekordní pravidla
============

Pravidla pro zaznamenávání jsou podmínky, které musí být splněny, aby byla operace
aby byla povolena. Pravidla pro záznamy jsou hodnocena záznam po záznamu, podle přístupu
práva.

Záznamy jsou ve výchozím nastavení povoleny: pokud má uživatel oprávnění k přístupu, není žádný záznam.
používání a modelu pro uživatele, přístup je povolen.

.. třída: ir.Rule

...... atribut:: jméno

Popis pravidla.

...... atribut:: model_id

Model, na který se pravidlo vztahuje.

...... atribut:: skupiny

Které skupiny mají být přístupné (nebo ne)
lze určit skupiny. Pokud není žádná skupina specifikována, pravidlo je *globální*.
Jež se liší od pravidel pro „skupinu“ (viz níže).

...... atribut:: globální

Výpočet na základě atributu :attr:`groups` poskytuje snadný přístup k
celosvětový stav pravidla (nebo ne).

.. atribut:: doména_povinná

Predikát specifikovaný jako doména, viz :ref:`domény <reference/orm/domains>`.
Pravidlo umožňuje vybrané operace, pokud doména odpovídá záznamu.
a zakazuje jinak.

Doména je *Python výraz*, který může používat následující
proměnné:

„čas“
Pythonovou modul :mod:`python:time`.
„uživatel“
Aktuální uživatel jako jediný záznam v seznamu.
„company_id“
Aktuální uživatel vybrané společnosti jako jediný identifikátor společnosti
(není záznamový set).
„company_id“
Všechny společnosti, ke kterým má aktuální uživatel přístup jako seznam
společností (ne jako záznamová sada), viz
viz [1] pro další informace.

Metody samp_method mají zcela odlišný význam než metoda pro
:třída:ir.model.access: pro pravidla určují, která operace se má vztahovat na pravidlo
se vztahuje na. Pokud není vybrána operace, pak pravidlo nebude kontrolováno
Aniž by se o tom někdo zajímal, jako kdyby taková pravidla neexistovala.

Všechny operace jsou vybrány výchozí volbou.

...... atribut:: perm_create
...... atribut:: perm_read
.... atribut:: perm_write
...... atribut:: perm_unlink

.._odkaz/bezpečnost/pravidla/globální:

Globální pravidla proti skupinovým pravidlům
-------------------------------

Je velký rozdíl mezi globálními a skupinovými pravidly, jak je sestavují
a spojit:

* Globální pravidla se kříží, pokud se dvě globální pravidla vztahují na stejný objekt, pak musí platit obě.
spokojený s tím, že přístup bude povolen, což znamená vždy přidat globální pravidlo
Začíná se omezovat přístup ještě více.
* Skupinové pravidlo *sjednocuje*, pokud se dvě skupinová pravidla vztahují na stejný objekt, pak platí *kterákoli* z nich.
spokojeni s přístupem, což znamená, že přidáním skupinových pravidel
rozšířit přístup, ale ne za hranice definované globálními pravidly.
* Globální a skupinové pravidla se kříží, což znamená, že první skupinový
Pokud je přidán do určitého globálního pravidla, bude omezen přístup.

.. nebezpečí::

Vytváření více globálních pravidel je rizikové, protože je možné vytvořit
nepřekrývající se pravidla, která odstraní všechny přístupy.

.. odkaz/bezpečnostní pole:

Přístup k poli
============

Klasa pole :class:`~odoo.fields.Field` může mít atribut „skupiny“.
poskytnutí seznamu skupin (jako řetězec oddělených čárkami)
:term:`externí identifikátory“).

Pokud je aktuální uživatel v žádné z uvedených skupin, nemůže
přístup na hřiště:

* Omezená pole jsou automaticky odstraněna z požadovaných výhledů.
* omezené pole jsou odstraněny z metody :meth:`~odoo.models.Model.fields_get`.
Odpovědi
* Pokusy o čtení nebo zápis do omezených polí způsobí
chyba přístupu

.. vše::

Přístupové skupiny pole se vztahují na superuživatele, ale ne na
číst/zapisovat...

... časový modul: https://docs.python.org/3/library/time.html


.. reference/bezpečnost/případné nástrahy:

Bezpečnostní pasti
=================

Jako vývojář je důležité pochopit bezpečnostní mechanismy a vyhnout se
časté chyby vedoucí k nezabezpečenému kódu.

Nejisté veřejné metody
---------------------

Každá veřejná metoda může být spuštěna prostřednictvím RPC volání.
„<api/external_api/calling_methods>“ s vybranými parametry.
začínající znakem „_“ nelze volat pomocí tlačítka akce nebo externího API.

Na veřejných metodách záznam o tom, jaká metoda byla spuštěna a parametry
nemůže být důvěryhodný, protože ověřování ACL se provádí pouze při operacích CRUD.

... kódový blok:: python

    # tento způsob je veřejný a jeho argumenty nelze brát vážně
def action_done(self):
pokud je stav „návrh“ a uživatel má skupinu „správce základní úrovně“,
sebe.stav = "hotovo"

    # Tento způsob je soukromý a může být volán pouze z jiných metod Pythonu.
def __set_state__(self, nový stav):
self.sudo().write({"state": nový_stav})

Zatímco udělení metody soukromé je zřejmě nedostatečné, je třeba dbát na její používání.
v pořádku.

Obcházení ORM
-----------------

Nikdy nepoužívejte přímo databázový průchody, když ORM dokáže stejnou věc
Vaše věc! Tímto způsobem obcházíte všechny funkce ORM a možná i
automatické chování jako překlady, neplatnost políček, „aktivní“,
přístupová práva a podobně.

A je dost pravděpodobné, že tím kód také ztěžujete čtení a možná
méně bezpečná.

... kódový blok:: python

    # velmi velmi špatně
self.env.cr.execute("SELECT id FROM auction_lots WHERE auction_id IN (%s) AND state = %s AND obj_price > 0" % (','.join(map(str, ids)), 'draft'),
auction_lots_ids = [x[0] pro x v seznamu self.env.cr.fetchall()]

    # bez injekce, ale stále špatně
self.env.cr.execute("SELECT id FROM auction_lots WHERE auction_id IN %s "
'AND stav=%s AND cena>0', (((id, 'návrh'), ),))
auction_lots_ids = [x[0] pro x v seznamu self.env.cr.fetchall()]

    # lepší
aukční_loť_idy = sebevražedná[('aukce_id','in',idy), ('stav','=','návrh'), ('objektivní cena','>',0)]


SQL injekce
~~~~~~~~~~~~~~

Při používání musí být dbáno na to, aby se nedostaly do systému zranitelnosti SQL injection.
ručně psané dotazy na databázi. Zranitelnost je přítomna, pokud jsou vstupy uživatele buď
špatně filtrované nebo špatně citované, což umožňuje útočníkovi zavést
nežádoucí podmínky do dotazu SQL (například obcházení filtrů nebo
výkonných příkazů „UPDATE“ nebo „DELETE“.

Nejlepší způsob, jak se ubránit je nikdy, NIKDY nepoužívat operátor sčítání (plus).
nebo interpolace proměnných do řetězce dotazu SQL (%).

Druhý důvod je téměř stejně důležitý a spočívá v tom, že
databázového abstrakčního vrstvy (psycopg2) aby se rozhodla o formátování parametrů dotazu.
To není vaše práce! Například psycopg2 ví, že když předáte seznam hodnot
musí je formátovat jako oddělené čárkami seznam uvedený v závorkách !

... kódový blok:: python

    # je to velmi špatné:
    #   - je to zranitelnost vložením SQL
    #   – je nepřečitelný
    #   – není vaší povinností formátovat seznam ID
self.env.cr.execute("SELECT DISTINCT child_id FROM account_account_consol_rel " +
"KDE id rodiče = (".join(map(str,ids)) + ")

    # lepší
self.env.cr.execute("SELECT DISTINCT child_id "
„Od účtu_účet_konzol_vztah“
"WHERE id rodiče v %s",
(tupla(id),)

To je velmi důležité, takže prosím buďte opatrní také při refaktorování a
Důležité je, abyste tyto vzory nekopírovali!

Pamatujte si, že tento příklad je vhodný k připomenutí problému (ale
Nepřenášejte kód tam (nebo se ujistěte, že jste si přečetli
Online dokumentace k používání knihovny psycopg2:

- „Problém s parametry dotazu“ (http://initd.org/psycopg/docs/usage.html#the-problem-with-the-query-parameters)
- „Jak předat parametry s psycopg2 <http://initd.org/psycopg/docs/usage.html#passing-parameters-to-sql-queries>“
- „Pokročilé typy parametrů <http://initd.org/psycopg/docs/usage.html#adaptation-of-python-values-to-sql-types>“
- „Dokumentace Psycopg <https://www.psycopg.org/docs/sql.html>“

Nepotlačovaný pole
-----------------------

Při zpracování obsahu pomocí JavaScriptu a XML může člověk být lákán k použití
„t-raw“ pro zobrazení obsahu s bohatým textem. Toto by se mělo vyhnout, protože je časté
Vektor „křížové šíření skriptů“ (XSS).

Je velmi těžké kontrolovat integritu dat od výpočtu až do uložení.
konečné zapracování do prohlížeče. „T-raw“ správně zabezpečený
Při zavádění se může stát, že nebude bezpečný při příštím opravném balíčku nebo
refaktorování.

... kódový blok: JavaScript

QWeb.zobrazit('nebezpečný šablonový soubor', {
info_message: „Máte důležitou zprávu“,
    })

... blok kódu::xml

<div t-name="nebezpečný vzor">
<div id="informační lišta">


Následující kód může působit bezpečně, protože obsah zprávy je kontrolován, ale je špatný
Praktiky, které mohou vést k neočekávaným bezpečnostním slabinám.
bude v budoucnu vyvíjet.

... kódový blok: JavaScript

    // XSS possible with unescaped user provided content !
QWeb.zobrazit('nebezpečný šablonový soubor', {
informační zpráva: „Máte důležitou notifikaci na“
            + „produkt <strong>“ + product.name + „</strong>“.
    })

Pokud by se šablona formátovala jinak, takové zranitelnosti by nebyly možné.

... kódový blok: JavaScript

QWeb.render('bezpečný šablonový soubor', {
zpráva: „Máte důležitou notifikaci na produktu:“,
předmět: produkt.název
    })

... blok kódu::xml

<div t-name="bezpecnostni_vzor">
<div id="informacni-brana">
<div class="info">{{ message }}</div>
<div class="předmět">
</div>


... kódový blok:: CSS

.subjekt {
font-weight: 700;
    }

Vytváření bezpečného obsahu pomocí třídy Markup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Podívejte se na „oficiální dokumentaci <https://markupsafe.palletsprojects.com/>“
vysvětlení, ale velkou výhodou
Třída Markupsafe.Markup je tak bohatá, že přebírá
operace na objektu typu str, které automaticky uniknou parametry.

To znamená, že je snadné vytvářet bezpečné HTML fragmenty pomocí
:klasu ~markupsafe.Markup na řetězci a „vložení formátování“
uživatelsky poskytnutý obsah, který je tedy potenciálně nebezpečný:

... kódový blok:: pycon

>>> Markup('<em>Ahoj</em> ') + '<foo>'
Markup('<em>Ahoj</em>&lt;foo&gt;')
>>>Markup('<em>Ahoj</em> %s') % '<foo>'
Markup('<em>Ahoj</em>&lt;foo&gt;')

Ačkoliv je to velmi dobrá věc, mějte na paměti, že účinky mohou být někdy zvláštní:

... kódový blok:: pycon

>>>Markup('<a>').replace('>', 'x')
Markup('<a>')
>>> Markup('<a>').replace(Markup('>'), 'x')
Markup('<ax>')
>>> Markup('<a>').replace('>', 'x')
Markup('<ax>')
>>>Markup('<a>').replace('>', '&')
Markup('<a&')

Tip: Většina bezpečných API skutečně vrací
:třída ~markupsafe.Markup s tím, co to obnáší.

Metoda ~markupsafe.escape (a její
alias:class:`~odoo.tools.misc.html_escape`) převádí řetězec na
:třída ~markupsafe.Markup a uvede její obsah do uvozovek.
obsah objektu třídy Markup.

... kódový blok:: python

def get_name(self, to_html=False):
Pokud chcete použít funkci to_html,
vrací Markup („<strong>%s</strong>“), který uvede jméno
jinak:
vrací sebe sama

>>>record.jméno = "<R&D>"
>>> uniknout(record.get_name())
Markup ("&lt;R&amp;D&gt;")
>>> uniknout(record.get_name(True))
Značení (<strong><R&D></strong>) # HTML je zachováno

Při generování HTML kódu je důležité oddělovat strukturu (tagy).
obsah (text).

... kódový blok:: pycon

>>>Značkování („<p>“) + „Ahoj R&D“ + Značkování („</p>“)
Markup('<p>Ahoj &lt;R&amp;D&gt;</p>')
>>>Markup("%s <br/> %s") % ("<R&D>", Markup("<p>Ahoj</p>"))
Markup("&lt;R&amp;D&gt;<br />
>>> uniknout ("<R&D>")
Markup('<R&amp;D>')
>>>_„Seznam úkolů projektu %s: %s“,
...     projekt.název
... Markup („<ul>%s</ul>“) % Markup ().join (Markup ("<li>%s</li>") % t.jméno pro t v projektu.úkoly.id)
    ... )
Markup('Seznam úkolů pro projekt R&D:<ul><li>První úkol v rámci R&D</li></ul>')

>>>Markup(„<p>Foo %</p>“ % bar) # špatně, bar není uveden v uvozovkách
>>>Markup("<p>Foo %</p>") % bar # dobré, bar je zabezpečený pokud je text a zachován pokud je značkování

>>>link = Markup('<a>%s</a>') % self.name
>>> zpráva = "Klikněte na %s" % odkaz # špatně, zpráva je text a Markup nic nedělal
>>> zpráva = unescape('Klikněte na %s') % odkaz # dobrý, formátujeme dva objekty značek


>>> formátování značky (<p>Foo {bar}</p>) s proměnnou self.bar

Při práci s překlady je zvláště důležité oddělovat HTML
z textu. Překladový algoritmus přijímá:
parametrů a pokud dostanou alespoň jeden, uniknou překladu.

... kódový blok:: pycon

>>>Markup("<p>%s</p>") % _("Ahoj <R&D>")
Markup('<p>Bonjour &lt;R&amp;D&gt;</p>')
>>_("Objednávka číslo %s byla potvrzena", Markup("<a>%s</a>") % objednávky.číslo)
Markup('Objednávka číslo <a>SO42</a> byla potvrzena.
>>>_("Zpráva od %(jméno)s <%(e-mail)s>"),
...  name=self.jméno,
...   email=Markup('<a href="mailto:%s">%s</a>') % (self.email, self.email)
Markup('Zpráva od Georges <a href="mailto:george@abitbol.example">george@abitbol.example</a>')


Úniky vs. dezinfekce
----------------------

.. důležité:

Vždy je únik z dat a kódu 100% povinný, bez ohledu na to, jak
zabezpečit data

Funkce **Uniknout** převádí *TEXT* na *KÓD*. Je naprosto nezbytné, aby se tato funkce používala
Každý pokus o smíchání *DAT/TEXTOVÉHO OBSAHU* s *KÓDEM* (např. vytváření HTML nebo Python kódu)
hodnotit uvnitř funkce safe_eval), protože *KÓD* vždy vyžaduje *TEXT*.
musí být kódován. Je to kritické pro bezpečnost, ale také otázka
správnost. I když není žádné bezpečnostní riziko (protože text je 100 %
garantovat bezpečnost nebo důvěryhodnost), je stále vyžadováno (např. aby se předešlo porušování
layout v generovaném HTML.

Utečení nikdy nezruší žádnou funkci, pokud vývojář pozná, která
Proměnná obsahuje text TEXT a kód CODE.

... kódový blok:: python

>>> odoo.tools.html_escape, odoo.tools.html_sanitize
>>> data = "<R&D>" # data je nějaký text, který přichází z někam

    # Utíká se do kódu, dobře!
>>>code = html_escape(data)
>>> kód
Markup('<R&amp;D>')

    # Nyní můžete kód smíchat s jiným kódem…
>>> sebevlastní webová stránka.popis = Markup('<strong>%s</strong>') % kód

**Dezinfekce** převádí *KÓD* na *BEZPEČNĚJŠÍ KÓD* (ale ne nutně na *bezpečný* kód).
Nepracuje s textem. Dezinfekce je nutná pouze u kódu
neověřené, protože pochází zcela nebo částečně od nějakých dat poskytnutých uživatelem.
Uživatelsky zadaná data jsou v podobě textu (*TEXT*) (např. obsah formuláře).
(vyplněná uživatelem) a zda byla před vložením do ní správně převedena
*KÓD*, pak je dezinfekce zbytečná (ale může se provádět dál). Pokud však
Pokud nebyla uživatelská data „nevyhledána“, pak dezinfekce nebude fungovat.
očekávané.

... kódový blok:: python

    # Sterilizace bez úniku je POŠKOZENA: datové soubory jsou poškozené!
>>>html_sanitizer(data)
Markup("")

    # Dezinfekce po útěku je v pořádku!
>>>html_sanitizovat(kód)
Markup('<p>&lt;R&amp;D&gt;</p>')

Dezinfekce může narušit funkci, v závislosti na tom, zda se očekává, že
obsahují vzory, které nejsou bezpečné. Protože jsou v souboru
Funkce tools.html_sanitize() má možnosti pro vylepšení úrovně čištění
stylů, atd. Tyto možnosti je třeba pečlivě zvážit v závislosti na tom, kde
Data pochází od a požadované vlastnosti. Bezpečnost ošetření
Váženo proti poruchám dezinfekce: čím bezpečnější je dezinfekce, tím
Je pravděpodobné, že něco rozbije.

... kódový blok:: python

>>>code = "„<p class='text-warning'>Důležité informace</p>“
    # Tím se odstraní styl, který může narušit funkce.
    # Je však nezbytná, pokud zdroj není důvěryhodný.
>>>html_sanitize(kód, odstranění tříd = True)
Markup('<p>Důležité informace</p>')

Hodnocení obsahu
------------------

Někteří lidé mohou chtít použít „eval“ k analýze uživatelsky poskytnutého obsahu. Použití „eval“ by
její použití se vyhýbat na všechny náklady. Bezpečnější metoda :meth:`~odoo.tools.safe_eval`
, ale stále poskytuje uživateli obrovské možnosti.
a měla by být vyhrazena pouze důvěryhodným uživatelům se zvláštním oprávněním, protože
bariéra mezi kódem a daty.

... kódový blok:: python

    # velmi špatný
doména = eval(self.filtr_doména)
vrací sebe sama

    # lepší, ale stále nedoporučovaný
od odoo.tools import safe_eval
doména = bezpečně vyhodnocená hodnota (self.filtr_domena)
vrací sebe sama

    # dobrý
od ast import literal_eval
doména = literální hodnota (self.filtr_doména)
vrací sebe sama

Analýza obsahu nepotřebuje „eval“

==========  ==================  ================================
Jazyk     Datový typ          Vhodný parser
==========  ==================  ================================
Python       int, float atd.     int(), float
Javascript  int, float atd.   parseInt(), parseFloat()
Python         slovník                   json.loads(), ast.literal_eval()
Objekt JavaScriptu, seznam atd. JSON.parse()
==========  ==================  ================================

Přístup k atributům objektů
---------------------------

Pokud je potřeba dynamicky získat nebo změnit hodnoty záznamu, můžeme
chce používat metody „getattr“ a „setattr“.

... kódový blok:: python

    # nebezpečné získání hodnoty pole
def _get_state_value(self, res_id, stavový_prvek):
record = self.sudo().prohlížet(res_id)
vrací hodnotu atributu record pro pole stav

Tento kód však není bezpečný, protože umožňuje přístup ke všem vlastnostem záznamu.
včetně soukromých vlastností nebo metod.

Metoda __getitem__ pro objekt Recordset byla definována a přístup k dynamickému
Hodnota pole lze bezpečně dosáhnout snadno:

... kódový blok:: python

    # lepší vyhledávání hodnoty pole
def _get_state_value(self, res_id, stavový_prvek):
record = self.sudo().prohlížet(res_id)
vraťte hodnotu pole [státní pole]

Metoda výše je samozřejmě stále příliš optimistická a další ověření
Na záznamovém ID a hodnotě pole musí být provedeny změny.
