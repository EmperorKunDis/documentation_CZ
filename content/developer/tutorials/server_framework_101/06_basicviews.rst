======================
Kapitola 6: Základní pohled
======================

V předchozím kapitole jsme viděli, že Odoo je schopné
Vytvořit výchozí pohled na daný model. Ve skutečnosti je **vždy** výchozí pohled nepřijatelný
pro obchodní aplikaci. Místo toho bychom měli alespoň logicky uspořádat různé pole.
měna.

Výhledy jsou definovány v XML souborech s akcemi a menu. Jsou to instancí
Model „ir.ui.view“.

V našem modulu nemovitostí je potřeba pole uspořádat logicky:

- V seznamovém zobrazení chceme zobrazit více než jen název.
- V zobrazení formuláře by měly být pole seskupeny.
- V hledání chceme možnost vyhledávat na více než jenom na jméno. Konkrétně chceme
filtr pro vlastnosti „Dostupné“ a zkratku k seskupení podle PSČ.

Seznam
====

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`reference/view_architectures/list`.

.. poznámka::

**Úkol**: V závěru této části by měl vypadat seznam následovně:

.. obrázek:: 06_základní pohledy/seznam.png
:synchronizace: střed
:alt: Zobrazení seznamu

Listové zobrazení, také nazývané tabulkové zobrazení, zobrazuje záznamy v tabulkovém tvaru.

Jejich základní prvek je „<list>“. Nejzákladnější verze této zobrazení je jednoduše
zobrazuje všechna pole, která se mají zobrazit v tabulce (kde každé pole je sloupec):

... blok kódu::xml

<list string="Testy">
<pole název/>
<field name="poslední vidění"/>


Jednoduchý příklad najdeme
„tady <https://github.com/odoo/odoo/blob/18.0/addons/crm/views/crm_lost_reason_views.xml#L45-L53>“.

...cvičení: Přidejte vlastní seznam zobrazení.

Definujte seznamový pohled na model „majetek.vlastnictví“ v příslušném souboru XML.
**Účel** této části je zobrazit pole.

Tipy:

    - Nepřidávejte atribut „editable=“dolů“, který najdete v příkladu výše.
se k tomu vrátit později.
    - Některé pole štítků mohou být upraveny tak, aby odpovídaly referenci.


Jako vždy je nutné restartovat server (nezapomeňte na možnost „-u“), a prohlížeč aktualizovat.
Podívat se na výsledek.

.. varování:

V této kapitole budete pravděpodobně používat nějaké kopírování a vkládání, proto si vždy zkontrolujte, že „id“
zůstává pro každý pohled jedinečný!


.. varování:
Pamatujte na správné nastavení přístupových práv uživatele, jak je popsáno v :doc:`úvodu do bezpečnosti <04_securityintro>`.

Tlačítko pro vytvoření nebude zobrazeno, pokud má uživatel jen čtenářská práva.

Tvar
====

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`reference/view_architectures/form`.

.. poznámka::

**Úkol**: Po dokončení této části by měl vypadat pohled na formulář takto:

... obrázek: 06_základnípohledy/formulář.png
:synchronizace: střed
:alt: Zobrazení formuláře

Formuláře se používají k vytváření a úpravě jednotlivých záznamů.

Jejich základním prvkem je „<form>“. Skládají se z vysoké úrovně struktury
elementy (skupiny a záložky) a interaktivní prvky (tlačítka a pole):

... blok kódu::xml

<form string="Test">
<listina>
<skupina>
<skupina>

</skupina>
<skupina>
<pole název="poslední viděný čas"/>
</skupina>
</skupina>
<poznámkový blok>

<vlastnost název/>


</list>


Můžete používat běžné značky HTML, jako například „div“ a „h1“, stejně jako atribut „class“.
(Odoo poskytuje několik předdefinovaných tříd) pro vylepšení vzhledu.

Jednoduchý příklad najdeme
„tady <https://github.com/odoo/odoo/blob/6da14a3aadeb3efc40f145f6c11fc33314b2f15e/addons/crm/views/crm_lost_reason_views.xml#L16-L44>“.

... cvičení: Přidejte vlastní zobrazení formuláře.

Definujte vhodnou XML soubor pro pohled na „majetek.vlastnictví“.
**Účel** této části pro očekávaný finální návrh stránky.

Možná bude nutné vyzkoušet několik možností, než dosáhnete očekávaného výsledku :-) Doporučujeme
Přidávejte pole a tagy postupně, abyste pochopili, jak funguje.

Aby se nemusel server znovu spouštět pokaždé, když provedete změnu v pohledu, můžete
je vhodné při spouštění serveru používat parametr „--dev xml“:

.. kódový blok: konzole

$ ./odoo-bin --addons-path=addons,../enterprise/,../tutorials/ -d rd-demo -u estate --dev xml

Tento parametr vám umožní jen obnovit stránku a zobrazit vaše změny pohledu.

Hledání
======

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`reference/view_architectures/search`.

.. poznámka::

**Cíl**: na konci této části by mělo vypadat vyhledávací okno takto:

.. obrázek: 06_základní pohledy/vyhledávání_01.png
:synchronizace: střed
:alt: Hledání

.. obrázek: 06_základní pohledy/vyhledávání_02.png
:synchronizace: střed
:alt: Filtr

.. obrázek: 06_základní pohledy/vyhledávání_03.png
:synchronizace: střed
:alt: Skupina

Výsledky vyhledávání jsou mírně odlišné od výpisů a formulářů, protože nezobrazují
*obsah*. I když se vztahují na konkrétní model, používají se k filtrování
obsah jiných pohledů (obvykle agregované, například
Reference [online]. Dostupné z: https://www.php.net/manual/en/ref-architecture.php
definován stejně.

Jejich základní prvek je „<hledání>“. Nejzákladnější verze této zobrazení jednoduše
zobrazuje všechny pole, pro která je zkratka požadována:

... blok kódu::xml

<hledaný výraz="Testy"
<pole název/>
<field name="poslední vidění"/>


Výchozí vyhledávací pohled generovaný Odoem poskytuje zkratku pro filtraci „název“. Je velmi
přidat pole, která uživatel bude pravděpodobně filtrovat v přizpůsobeném pohledu na vyhledávání.

... cvičení: Přidejte vlastní vyhledávací panel.

Definujte vyhledávací pohled na model „majetek.vlastnictví“ v příslušném souboru XML.
První obrázek této části cíle pro seznam polí.

Po obnovení servisu by mělo být možné filtrovat na zadaných polích.

Vyhledávací pohled může také obsahovat „<filtr>“ prvky, které slouží jako přepínače.
předdefinované vyhledávání. Filtry musí mít jednu z následujících vlastností:

- „doména“: přidá do aktuálního vyhledávání zadanou doménu
- „kontext“: přidává nějaký kontext k aktuálnímu vyhledávání; používá klíč „group_by“, aby data seskupila
výsledky na daném názvu pole

Jednoduchý příklad najdeme
„tady <https://github.com/odoo/odoo/blob/715a24333bf000d5d98b9ede5155d3af32de067c/addons/delivery/views/delivery_view.xml#L30-L44>“.

Před pokračováním v cvičení je nutné představit pojem „doména“.

Domény
-------

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`reference/orm/domains`.

V Odoo doménu kóduje podmínky
záznamy: doména je seznam kritérií používaných k výběru podmnožiny modelu
záznamy. Každý kritérium je trojice s názvem pole, operátorem a hodnotou.
Záznam splňuje kritérium, pokud pole splňuje podmínku operátoru použitého na hodnotu.

Příkladem je použití na produktu *Produkt*, kdy se vybere následující doména
všechny služby s jednotkovou cenou vyšší než *1000*:

[('produktové_druhy', '==', 'služba'), ('jednotková_cena', '>', 1000)]

Výchozí kritéria se automaticky spojují s implikovaným „a“ a tedy platí, že *každé* kritérium
musí být splněny pro záznam, aby odpovídal doméně. Logické operátory
„&“ (a „AND“), „|“ (nebo „OR“) a „!“ („NOT“) lze použít k explicitnímu spojení
kriterií. Používají se v předponové pozici (operátor je vložen před
argumenty než mezi nimi. Například vybrat produkt „který je
služby nebo jednotková cena, která není mezi 1000 a 2000'

    ['|',
('produktové_druhy', '==', 'služba')
        '!', '&',
('cena_jednotky', '>=', 1000)
['cena_za_jednotku' < 2000]

.. poznámka: XML neumožňuje používat „<“ a „&“ uvnitř XML
elementy. Proto by měly být používány entity reference:
„&lt;“ pro „<“ a „&amp;“ pro „&“. Jinak jsou v entity odkazovány
jsou volitelné.

...... příklad::
... kódový blok::xml

<filtr jméno="negativní" doména="[('test_val', '<', 0)]"/>

...cvičení: Přidej filtr a seskupení.

Následně do již vytvořeného vyhledávacího pohledu přidáme následující:

    - filtr, který zobrazuje dostupné nemovitosti, tedy stav by měl být „New“ nebo
„Přijato“.
    - Možnost seskupit výsledky podle poštovního směrovacího čísla.

Vypadá dobře? V tuto chvíli už jsme schopni vytvářet modely a navrhovat uživatelské rozhraní.
Dává smysl z hlediska podnikání. Chybí však klíčová součást:
:doc:`vztah mezi modely <07_relations>“.
