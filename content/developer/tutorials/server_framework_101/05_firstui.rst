========================================
Kapitola 5: Konečně nějaké uživatelské rozhraní, se kterým můžete pracovat
========================================

Nyní, když jsme vytvořili naši novou :doc:`modelovou strukturu <03_basicmodel> a její
přidělit příslušná práva, je čas na
interagovat s uživatelským rozhraním.

Na konci této kapitoly vytvoříme několik nabídek pro přístup k výchozím seznamům.
a vzhled.

Datové soubory (XML)
================

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
Reference/Data.

V sekci „04_securityintro“ jsme přidali data pomocí souboru CSV.
Formát je pohodlný, pokud má načítaná data jednoduchou strukturu. Když je formát složitější
Pokud je potřeba načíst strukturu pohledu nebo šablony e-mailu, používáme formát XML. Například
to
„pomocné pole <https://github.com/odoo/odoo/blob/09c59012bf80d2ccbafe21c39e604d6cfda72924/addons/crm/views/crm_lost_reason_views.xml#L61-L69>“
obsahuje značky HTML. I když by bylo možné načíst taková data pomocí souboru CSV, je
je praktické používat soubor XML.

XML soubory musí být přidány do stejných složek jako CSV soubory a definovány podobně v
„__manifest__.py“. Obsah datových souborů je také načítán sekvenčně při instalaci modulu nebo
aktualizován, proto platí pro soubory XML všechny poznámky uvedené u souborů CSV.
Při propojení dat s pohledy je přidáme do složky „views“.

V této kapitole si načteme první akci a menu z XML souboru. Akce a menu jsou
standardní záznamy v databázi.

.. poznámka::

Pokud je důležitá rychlost, preferuje se formát CSV před formátem XML. To platí pro Odoo
kde načítání CSV souboru je rychlejší než načítání XML souboru.

V Odoo je uživatelské rozhraní (akce, menu a pohledy) v podstatě definováno tím, že se
a vytváření záznamů definovaných ve souboru XML. Běžným vzorem je Menu > Akce > Zobrazení.
Uživatel prochází několika úrovněmi nabídek, nejhlubší je
akce, která spustí seznam záznamů.

Akce
=======

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:doc:`../../reference/backend/akce`.

.. poznámka::

**Cíl**: Na konci této části by se měla v systému načíst akce. My ji ale neuvidíme.
nic v uživatelském rozhraní, ale soubor by se měl načíst do protokolu:

... kódový blok :: text

INFO rd-demo odoo.modules.loading: loading real_estate/views/real_estate_property_views.xml

Akce může být spuštěna třemi způsoby:

1. kliknutím na položky nabídky (které jsou spojeny s konkrétními akcemi)
2. kliknutím na tlačítka v pohledech (pokud jsou spojena s akcemi).
3. jako kontextová akce na objekt

V tomto kapitole se budeme zabývat pouze prvním případem, druhý případ bude pokryt v
:kapitola později v knize (viz kapitolu 09 „Akce“).
pokročilé téma. V našem příkladu s nemovitostmi bychom chtěli propojit nabídku s „nemovitostí“.
modelu, takže můžeme vytvořit nový záznam. Akce je možné chápat jako spojení mezi nabídkami
a modelka.

Základní akce pro našeho „test_model“ je:

... blok kódu::xml

<záznam id="test_model_action" model="ir.actions.act_window">
<pole jméno="testovací akce" />
<položka jméno="res_model">test_model</položka>
<položka jméno="výhledový režim">seznam,formulář</položka>
</záznam>

- „id“ je vnější identifikátor. Může se použít k odkazování na záznam
(bez znalosti jeho identifikátoru v databázi).
- „model“ má pevně stanovenou hodnotu „ir.actions.act_window“ (viz odkaz na „reference/actions/window“).
- „name“ je název akce.
- „res_model“ je model, na který se akce vztahuje.
- „view_mode“ jsou pohledy, které budou k dispozici; v tomto případě jde o seznam a formulářové pohledy.
Vidíme, že existují i jiné režimy zobrazení.

Příklady najdete všude v Odoo, ale
„toto <https://github.com/odoo/odoo/blob/09c59012bf80d2ccbafe21c39e604d6cfda72924/addons/crm/views/crm_lost_reason_views.xml#L57-L70>“
je příkladem jednoduché akce. Všímejte si struktury souboru XML, protože
Potřebujeme ji v následujícím cvičení.

.. cvičení: Přidat akci.

Vytvořte soubor „estate_property_views.xml“ v příslušné složce a definujte jej v
„__manifest__.py“ soubor.

Vytvořte akci pro model „nemovitost“.

Restartujte server a měli byste vidět soubor nahrán v protokolu.

Menu
=====

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`reference/data/zkratky“.

.. poznámka::

**Úkol**: Na konci této části by mělo být vytvořeno tři menu a výchozí pohled
zobrazeno:

... obrázek: 05_prvniu/stavebni_menu_kořen.png
:synchronizace: střed
:alt:Hlavní menu

.. obrázek: 05_prvniu/stavebni_menu_akce.png
:synchronizace: střed
:alt:První úrovně a akční menu

.. obrázek: 05_prvni/nemovitost_formulář_výchozí.png
:synchronizace: střed
:alt: Výchozí zobrazení formuláře

Pro snížení komplexnosti při vyjadřování menu („ir.ui.menu“) a při propojení s příslušnou akcí
Můžeme použít zkratku „<menuitem>“.

Základní nabídka našeho „test_model_action“ je:

... blok kódu::xml

<menuitem id="test_model_menu_action" action="test_model_action"/>

Menu „test_model_menu_action“ je propojeno s akcí „test_model_action“, a akce
je spojen s modelem test_model. Jak bylo uvedeno dříve, akce může být považována za odkaz
Mezi menu a modelem.

Nicméně menu vždy následuje architekturu a ve skutečnosti existují tři úrovně menu:

1. Hlavní nabídka, která se zobrazuje v přepínači aplikací (přepínač aplikace pro komunitu Odoo je
(výběrové menu)
2. První úroveň nabídky v horním panelu
3. Akční nabídky

.. obrázek: 05_první_uiv/menu_01.png
:synchronizace: střed
:alt:Hlavní menu

.... obrázek:: 05_prvniu/menu_02.png
:synchronizace: střed
:alt:První úrovně a akční menu

Nejjednodušší způsob, jak strukturu definovat, je vytvořit ji ve souboru XML.
struktura naší „test_model_action“ je:

... blok kódu::xml

<menuitem id="test_menu_root" name="Test">
<menuitem id="test_prvni_stupen_menu" name="První úroveň">
<menuitem id="test_model_menu_action" action="test_model_action"/>
</menuitem>
</submenu>

Název pro třetí nabídku je vztažen k názvu „akce“.

.. cvičení: Přidat menu.

Vytvořte soubor „estate_menus.xml“ v příslušné složce a definujte ho v
„__manifest__.py“ soubor. Pamatujte na sekvenční načítání datových souborů :-)

Vytvořte tři úrovně menu pro akci „majetek.vlastnictví“ vytvořenou v předchozím
cvičení. Podívejte se na **cíl** této části, kde je uveden očekávaný výsledek.

Restartujte server a obnovte prohlížeč. Nyní byste měli vidět menu.
A dokonce si vytvoříte svou první reálnou inzerci nemovitosti!

Pole, atributy a pohled
===========================

.. poznámka::

**Cíl**: na konci této části by měla být cena prodeje čitelná pouze jako číslo.
počtu pokojů a datumu dostupnosti by měly mít výchozí hodnoty. Dále prodejní cena
a hodnoty dostupnosti se při kopírování záznamu nekopírují.

.. obrázek: 05_prvni_ui/atribut_a_vypocet.gif
:synchronizace: střed
:alt: Interakce mezi modelem a pohledem

Do modelu „estate.property“ jsou přidány rezervované pole „active“ a „state“.

Dosud jsme používali jen obecný pohled na reklamy nemovitostí.
Většinou chceme upravit pohled. V Odoo je mnoho možností úprav, ale
Nejprve je třeba zkontrolovat, že:

- Některé pole mají výchozí hodnotu.
- Některá pole jsou čtení jen
- Některá pole nejsou při kopírování záznamu přenášena.

V našem případě bychom rádi následující:

- Prodávaná cena by měla být čtena pouze, později se do ní automaticky vyplní.
- Datum dostupnosti a prodejní cena by se neměly kopírovat při kopírování záznamu
- Standardní počet ložnic by měl být 2
- Datum dostupnosti by mělo být vždy po 3 měsících.

Některé nové atributy
-------------------

Před dalším pokrokem v návrhu pohledu se vrátíme k definici našeho modelu. Ukázali jsme si, že některé
atributy, jako například „required=True“, ovlivňují tabulkovou schémata v databázi. Další atributy
bude ovlivňovat pohled nebo poskytovat výchozí hodnoty.

.. cvičení: Přidat nové atributy do polí.

Najděte vhodné atributy (viz :class:`~odoo.fields.Field`) pro:

  - součást ceny prodeje nastavit jako čtení
  - zamezit kopírování dat dostupnosti a prodejní ceny

Restartujte server a obnovte prohlížeč. Neměli byste být schopni nastavit žádné prodejní ceny.
Pokud se jedná o kopii záznamu, měla by být prázdná jeho dostupnost.

Výchozí hodnoty
--------------

Každému poli lze přiřadit výchozí hodnotu. V definici pole přidejte možnost
„default=X“, kde „X“ je buďto hodnota Pythonu (logická, celé číslo)
plovoucí nebo řetězec) nebo funkce přijímající model a vracící hodnotu:

name = fields.Char(výchozí hodnota = "Neznámé")
last_seen = fields.DatumVČasu("Last Seen", výchozí hodnota = DatumVČasu.nyní)

V poli „název“ bude výchozí hodnota „Neznámý“, zatímco v poli „poslední vidění“ bude
začít od současného času.

..cvičení:Nastavte výchozí hodnoty.

Přidejte vhodné výchozí atributy, aby:

    - Výchozí počet ložnic je 2
    - Výchozí termín dostupnosti je za 3 měsíce.

Tip: možná vám pomůže metoda:

Zkontrolujte, zda jsou nastaveny výchozí hodnoty tak, jak se očekává.

Rezervované pole
---------------

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`reference/orm/fields/reserved`.

Několik polí je vyhrazeno pro předdefinované chování.
model, když chceme vyvolat příslušné chování.

.. cvičení: Přidejte aktivní pole.

Přidejte pole „aktivní“ do modelu „nemovitost“.

Restartujte server, vytvořte novou vlastnost, pak se vrátíme zpět na pohled na seznam… Vlastnost bude
nebýt uveden! Například pole „active“ je rezervované pole s konkrétním chováním:
Pokud je v záznamu aktivní hodnota False, je automaticky vyřazen z jakéhokoliv vyhledávání.
Vytvořené vlastnictví budete muset hledat speciálně neaktivní záznamy.

.. obrázek: 05_prvniu/neaktivni.gif

:alt: Neaktivní záznamy

.. cvičení:Nastavte výchozí hodnotu pro pole aktivní.

Nastavte vhodný výchozí hodnotu pole „active“, aby se již neztrácelo.

Zapamatujte si, že všechny existující záznamy byly nastaveny na „aktivní = False“.

..cvičení::Přidat pole státu.

Přidejte pole „stát“ do modelu „majetek“. Pět hodnot je možných: Nový,
Nabídka přijata, nabídka přijata, prodáno a zrušeno. To musí být vyžadováno, nemělo by se kopírovat
a její výchozí hodnotu by měla mít nastavenou na „New“.

Ujistěte se, že používáte správný typ!

„Stát“ bude později použit pro několik vylepšení uživatelského rozhraní.

Nyní, když máme možnost interagovat s uživatelským rozhraním díky výchozím pohledům, je další krok
je zřejmé, že chceme definovat vlastní pohledy (viz 06_základní pohledy).

... [#refresh] Protože klient webu uchovává různé menu v mezipaměti, je nutné provést obnovení.
a pohledy pro výkonnostní důvody.
