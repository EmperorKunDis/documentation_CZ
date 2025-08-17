=========================
Vytvářejte přizpůsobené zprávy
=========================

SQL vzory jsou technikou pro vytváření přizpůsobených zpráv, které ukazují data, která nelze
ukázána s existujícími modely a pohledy. Tato technika pomáhá vyhnout se
zbytečné vytváření a počítání dalších polí pouze pro analýzu dat
účelům.

Vytvořte si vlastní model
==============

Vytvoření vlastního pohledu na databázi je podobné jako vytvoření standardní tabulky.

... kódový blok:: python

od odoo importujeme pole a modely


třída ModuleReport(model.Model):
_name = 'modul.report'
_description="Modul Report"
_rec_name = 'modul_pole'
_auto = False

Kde jsou atributy:

- Příznak _auto = False znamená, že nechceme ukládat model do databáze.
- Značka '_rec_name' ukazuje, které pole modelu reprezentuje název záznamu (tj.
název, který se použije v navigační liště chlebů s prohlížením záznamu.

a její pole jsou definována stejně jako u standardního modelu, s tím rozdílem, že každé pole je
označena jako readonly=True.

.. poznámka::
Nezapomeňte přidat svůj nový model do souboru s bezpečnostními informacemi.

Naplňte model
==================

Existují dvě možnosti, jak do tabulky v SQL View přidat data:

- překrýt metodu BaseModel.init(),
- nastavit vlastnost _table_query.

Ať už se používá jakýkoliv způsob, bude proveden dotaz na databázi pro naplnění modelu.
Proto lze použít jakékoliv příkazy SQL k získání a/nebo výpočtu potřebných dat.
a musíte mít na paměti, že jste obcházeli ORM (tj.
Dobrá myšlenka přečíst si reference a bezpečnost (pokud jste ještě neučinil(a)). Sloupce
Vrácené z výběru „SELECT“ vyplní pole modelu, takže ujistěte se, že vaše sloupec
jména odpovídají vašim polím nebo použijte jméno přezdívky, které odpovídá.

.. záložky::

....... tab:: Přepsání metody `BaseModel.init()`

Ve většině případů je převzetí metody BaseModel.init() standardem a lepší volbou.
použít. Jeho použití vyžaduje import nástrojů a obvykle se píše takto:

... kódový blok: Python

def __init__(self):
nástroje.odstranit_výhled_pokud_existuje(self.env.cr, self._tabulka)
self.env.cr.execute("""Vytvořit nebo nahradit vlastnost %s jako
SELECT
                                       %s
OD
                                       %s
)""" % (self._tabulka, self._vybrat(), self._z_))

Funkce tools.drop_view_if_exists zajistí, že se nebude vytvářet konfliktní pohled, pokud již existuje
Provede se dotaz v jazyce SQL. Je běžné oddělit různé části dotazu, aby bylo možné
umožnit snadnější rozšíření modelu. Přesný způsob, jak je dotaz rozdělen mezi metody, není
standardizované, ale alespoň metody _select a _from jsou běžné.
Všechny tyto metody vrací řetězce.

.. viz také:
„Příklad: vzorec SQL s přesměrováním metody init() z třídy BaseModel
<{GITHUB_PATH}/addons/project/report/project_report.py>

... tab::Použití funkce _table_query

Vlastnost "_table_query" se používá, když závisí na kontextu. Typicky se jedná o
Ve znění následujícím:

... kódový blok: Python

@vlastnost
def __tabulkový dotaz(self):
return "VYBRAT '%s' Z '%s'" % (self._select(), self._from())

a sleduje stejné standardy metod jako funkce inicializace třídy BaseModel.

Příklad použití vlastnosti namísto převzetí metody init() z třídy BaseModel
je v prostředí více společností a více měn, kde jsou potřeba částky spojené s měnou.
to se převede na měnovou konverzi, když uživatel přepíná mezi společnostmi.

.. viz také:
„Příklad: Vizuální dotaz na tabulku pomocí _table_query
<{GITHUB_PATH}/addons/account/report/account_invoice_report.py>

Použijte model.
=============

Zobrazení a položky nabídky pro vaše vlastní SQL zobrazení jsou vytvářeny a používány stejným způsobem jako jakákoliv jiná.
jiný model Odoo. Můžete začít používat své SQL pohledy. Užijte si to!

Další tipy
==========

..tip:
Nejčastější chybou v návrzích SQL je nezohlednit duplikaci některých dat.
v důsledku spojení tabulek. To může vést k chybnému počítání, pokud se používá pole s agregátorem
a/nebo s výchozím pohledem. Nejlepší je otestovat svůj SQL pohled na dostatečném množství dat, abyste se ujistili, že
Výsledné hodnoty pole jsou takové, jaké očekáváte.

..tip:
Pokud máte pole, které nechcete jako měřítko (tj. ve svých grafických nebo přehledových zobrazeních),
Přidejte k ní příznak „store=False“ a nebude se zobrazovat.
