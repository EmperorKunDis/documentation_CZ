..

===================
Překlad modulů
===================

Tato část vysvětluje, jak přidat do modulu překladové schopnosti.

.. poznámka: Pokud chcete přispět k překladu samotného Odoo, obraťte se na
„Stránka Odoo Wiki <https://github.com/odoo/odoo/wiki/Translations>.

Exportovat přeložitelný výraz
===========================

Některá slova ve vašich modulích jsou implicitně přeložitelná.
i když jste nic konkrétního k překladu neudělali, můžete exportovat
Vaše modulové termíny a můžete najít obsah, se kterým budete pracovat.

... potřebuje technické funkce

Export překladů se provádí v administračním rozhraní po přihlášení
zadní rozhraní a otevření:menu:Nastavení --> Překlady
-->Import/Export-->Export překladů

* zanechat jazyk na výchozí hodnotu (nový jazyk/prázdný šablonový soubor).
* Vyberte formát souboru „PO“
* vyberte si modul
* Klikněte na tlačítko „Export“ a stáhněte si soubor.

.. obrázek:translations/po-export.png

:šířka: 75 %

Tímto vám vytvoří soubor s názvem :file:`{yourmodule}.pot`, který by měl být přesunut do
souboru ve složce {yourmodule}/i18n/. Soubor je šablonou *.po
pouze seznam přeložitelných řetězců a skutečné překlady (soubory PO).
může být vytvořen. Soubory PO lze vytvářet pomocí msginit_ s konkrétním
překladovým nástrojem jako je POEdit nebo prostě kopírováním šablony do nového souboru
Název souboru je {language}.po. Přeložené soubory by měly být uloženy
:file:`{yourmodule}/i18n/`, vedle :file:`{yourmodule}.pot` a bude
automaticky načítána v případě instalace odpovídajícího jazyka (pomocí
Nastavení -> Překlady -> Jazyky

.. poznámka: jsou nainstalovány nebo aktualizovány překlady pro všechny načtené jazyky
při instalaci nebo aktualizaci modulu

Implicitní export
================

Odoo automaticky exportuje přeložitelné řetězce ze „šablon“ typu „Data“:

* Ve všech ne-QWebových pohledech jsou exportovány všechny textové uzly a obsah
„řetězec“, „pomoc“, „součet“, „potvrzení“ a „výplň“.
atributy
* Šablony QWeb (serverové i klientské) obsahují všechny textové uzly
s výjimkou obsahu v bloku „t-překlad=vypnuto“.
„Název“, „Popisek“ a „Značka“ jsou také
exportované
* pro pole typu :class:`~odoo.fields.Field`, pokud je jejich model označen
„_přeložit = False“:

  * jejich atributy „string“ a „help“ jsou exportovány
  * Pokud je „vybrané“ přítomno a je to seznam nebo tupl, bude exportováno.
  * Pokud je jejich atribut „přeložit“ nastaven na hodnotu „True“, všechny jejich stávající
hodnoty (všechny záznamy) jsou exportovány
* chybové hlášky a upozornění metody :attr:`~odoo.models.Model._constraints`.
:attr:`~odoo.models.Model._sql_constraints` jsou exportovány

Explicitní vývoz
================

Při řešení „nutnějších“ situací v kódu Python nebo Javascript
kód, Odoo nemůže automaticky exportovat překladatelné termíny.
musí být explicitně označena pro export. To se provádí zabalením literálu
string v volání funkce.

V Pythonu je funkce pro zabalení :func:`odoo.api.Environment._`.
a funkce :func:`odoo.tools.translate._`:

... kódový blok:: python

titulek = self.env._("Bankovní účty")

    # starý API pro zpětnou kompatibilitu
od odoo.tools import _
název = _("Bankovní účty")

V jazyce JavaScript je obalovací funkcí zpravidla :js:func:`odoo.web._t`:

... kódový blok: JavaScript

title=_t("Bankovní účty");

.. varování:

Exportovat lze pouze výslovné řetězce, ne výrazy nebo
proměnných. V případě formátování řetězců to znamená, že
formátovací řetězec musí být označený, nikoliv formátovaný řetězec

Nebezpečná verze znaků „_“ a „_t“ je třída LazyTranslate definovaná v modulu odoo.tools.translate.
továrna v Pythonu a funkce :js:func:`odoo.web._lt` v JavaScriptu.
Překladový výhled je prováděn pouze
při renderování a lze je použít k deklaraci přeložitelných vlastností metod třídy
globálních proměnných.

... kódový blok:: python

od odoo.tools import LazyTranslate
_lt = LazyTranslate(_name_)
LAZY_TEXT = _lt("nějaký text")

.. poznámka::

Překlady modulu nejsou v základním nastavení vystaveny přednímu konci.
takže pro skriptování nejsou dostupné. Chcete-li dosáhnout tohoto cíle, musíte
název modulu musí být buď předponován „website“ (stejně jako
„webová stránka prodej“, „webová událost“ atd. nebo explicitně registrovat implementací
:meth:_get_translation_frontend_modules_name pro model ir.http.

Takováto podoba by mohla vypadat například takto:

od odoo importujeme modely

třída IrHttp(model.AbstraktníModel):
dědí od ir.http

@metoda_třídy
def _get_překlad_modulů_jméno(klasu):
moduly = super._get_přeložené_moduly_jméno_předního_koncového_zařízení()
vraťte moduly + ['vaše_modul']

Kontext
-------

Pro překlad je nutné, aby funkce pro překlad znala jazyk a
*modul* jméno. Při použití „Environment._“ je známý jazyk a vy
může jako parametr předat modulový název, jinak se extrahuje z
volající.

V případě „odoo.tools.translate._“ je jazyk a modul
vytržené z kontextu. Pro tento účel prohlížíme místní proměnné volajícího.
Nevýhodou této metody je, že je chybovost vysoká: snažíme se najít
kontextová proměnná nebo „self.env“, ale tyto mohou být neexistující, pokud používáte
překlady mimo metodiku; tedy nefunguje u běžných
funkce nebo komprese Pythonu.

Překlady s nízkou kvalitou jsou při jejich vytváření připojeny ke konkrétnímu modulu.
jazyk se vyhodnotí při hodnocení pomocí funkce str().
Pozor, že můžete také předat lenivý překlad do „Environment._“.
přeložit ho bez jakéhokoliv kouzelného jazykového řešení.

Proměnné
---------

**Nepoužívejte** extrakt, který by mohl fungovat, ale nebude správně překládat text.

_("Smluvená schůzka s %s" % jméno pozvaného)

**Nastavte** dynamické proměnné jako parametr vyhledávání překladu (toto
pokud v překladu chybí místo pro zástupný symbol).

_("Smluvená schůzka s %s", jméno pozvaného)


Bloky
------

Překlad nerozdělujte na několik bloků nebo řádků.

    # špatný, za sebou padající mezeru, bloky mimo kontext
_("Máte ") + len(faktur) + _("nevyřízených faktur")
_t("Máte ") + faktury.length + _t("nevyřízených faktur");

    # špatné, mnoho malých překladů
_("Odkaz na dokument, který vygeneroval") + \
_("toto požadavky na prodejní objednávku.").

**Uchovávejte v jednom bloku a poskytněte překladatelům celý kontext.**

    # dobrý, umožňuje změnit pozici čísla v překladu
_("Máte %d nezaplacených faktur") % len(invoices)
_.str.sprintf(_t("Máte %s nezaplacených faktur"), invoices.length);

    # Dobrá, celá věta je srozumitelná
_("Odkaz na dokument, který tento vytvořil " +
„(tento požadavek na prodejní objednávku).“

Množné číslo
------

**Nepoužívejte anglické způsoby plurálu.**

msg = _("Máte %(count)s fakturu", count=faktura_počet)
pokud je objednávka větší než jedna,
msg += _("s")

Pamatujte na to, že každý jazyk má své vlastní množné tvary.

pokud je objednávka větší než jedna,
msg = _("Máte %(count)s faktur, " count=invoice_count)
jinak:
msg = _("Máte jeden fakturu")

Čas čtení vs. doba spuštění
----------------

Nepoužívejte vyhledávání překladů při spuštění serveru:

ERROR_MESSAGE = {
      # špatně, hodnoceno při spuštění serveru bez jazyka uživatele
'access_error': _('Přístupový problém'),
'chybka_chybějícího_záznamu': _('Chybějící záznam'),
    }

třída Record(model.Model):

def _raise_error(self, kód):
vznést výjimku typu UserError s chybovou zprávou ERROR_MESSAGE[code]

Při načítání souboru JavaScriptu nevyvolávejte vyhledávání překladů.

    # špatné, je-li hodnoceno příliš brzy
var webCore = require('web.core');
var _t = jádro._t;
mapa_nazev = {
přístup_chyba: _t('Přístupová chyba'),
chybějící_chyba: _t('Chybí záznam'),
    };


Používejte metodu prohledávání pomalého překladu.

ERROR_MESSAGE = {
'access_error': _('Access Error'),
„chybějící_chyba“: _lt('Chybějící záznam'),
    }

třída Record(model.Model):

def _raise_error(self, kód):
        # překlad provedl při chybě
vznést výjimku typu UserError s chybovou zprávou ERROR_MESSAGE[code]


nebo dynamicky hodnotit přeložitelný obsah:

    # dobrý, hodnocený při spouštění
def __get_error_message__(self):
return {
přístupní chyba: _('Přístupová chyba'),
chybějící_chyba: _('Chybí záznam'),
      }

**Do** v případě, kdy je vyhledávání překladu prováděno při načítání souboru
Použijte místo _t_ _lt_, pokud se slovo používá, a ne překládá.

    # dobrá, je-li vyhodnocena látka lazile
var webCore = require('web.core');
var _lt = jádro._lt;
mapa_nazev = {
přístupní chyba: _lt('Přístupová chyba'),
chybějící_chyba: _lt('Chybí záznam'),
    };


... _PO soubor: https://cs.wikipedia.org/wiki/Gettext#Přeložení
... _msginit: https://www.gnu.org/software/gettext/manual/gettext.html#Creating
.._POEdit: https://poedit.net/
