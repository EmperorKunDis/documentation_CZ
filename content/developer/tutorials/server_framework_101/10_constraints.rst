=======================
Díl 10: Omezení
=======================

V předchozím kapitole :doc:`<09_actions>` byla představena schopnost přidat
jak nějakou logiku do našeho modelu. Můžeme nyní spojit tlačítka s obchodním kódem, ale jak zabránit
uživatele vkládat chybné údaje? Například v našem realitním modulu nic nebrání
uživatelům nastavit negativní očekávanou cenu.

Odoo nabízí dvě způsoby, jak nastavit automaticky ověřené invarianty:
:funkce Pythonu omezení <odoo.api.constrains> a
:attr:`SQL omezení <odoo.models.Model._sql_constraints>“.

SQL
===

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`reference/orm/models` a v dokumentaci k PostgreSQL.

.. poznámka::

**Úkol**: na konci této části:

    - Částky musí být (přísně) kladné

.. obrázek:: 10_podmínky/sql_01.gif
:align: střed
:alt: Omezení výše částek

    - Typy nemovitostí a štítky by měly mít jedinečný název

.... obrázek: 10_podmínky/sql_02.gif
:align: střed
:alt: Omezení názvů

SQL omezení je definováno pomocí atributu modelu
:attr:`~odoo.models.Model._sql_constraints`. Tato vlastnost je přiřazena seznamu
trojic obsahujících řetězce „(název, definice SQL, zpráva)“, kde „název“ je
platný název SQL omezení, „sql_definition“ je výraz tabulkového omezení
A „zpráva“ je chybová zpráva.

Najdete zde jednoduchý příklad
„tady <https://github.com/odoo/odoo/blob/24b0b6f07f65b6151d1d06150e376320a44fd20a/addons/analytic/models/analytic_account.py#L20-L23>“.

.. cvičení: Přidat omezení v SQL.

Přidejte následující omezení do jejich odpovídajících modelů:

    - Očekávaná cena nemovitosti musí být přesně kladná
    - Prodejní cena nemovitosti musí být kladná
    - Nabídková cena musí být přesně kladná
    - Název vlastnosti a název typu vlastnosti musí být jedinečné.

Tip: hledejte klíčové slovo „unikátní“ v základu kódu Odoo pro příklady unikátních názvů.

Pokud chcete vidět výsledek, restartujte server s možností „-u estate“. Pozor, může se stát, že budou
který brání nastavení omezení v databázi. Může se zobrazit chybová hláška podobná této:

... blok kódu:: text

CHYBA rd-demo odoo.schema: Tabulka 'nabídka nemovitosti': Není možné přidat omezení 'estate_property_offer_check_price' jako CHECK(price > 0).

Příkladem je, že pokud některé nabídky mají cenu nula, pak omezení nelze použít. Můžete je smazat
problematická data, aby se mohly použít nové omezení.

Python
======

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:func:`~odoo.api.constrains`.

.. poznámka::

**Úkol**: na konci této sekce nebude možné přijmout nabídku
nižší než 90 % očekávané ceny.

.. obrázek:: 10_podmínky/python.gif
:align: střed
:alt:Pythonová omezení

SQL omezení jsou efektivním způsobem, jak zajistit konzistentnost dat. V některých případech však mohou být nezbytné
pro provádění složitějších kontrol, které vyžadují kód v Pythonu. V tomto případě potřebujeme omezení v Pythonu.

Pythonová omezení jsou definována jako metody, které jsou dekorovány
:func:`~odoo.api.constrains` a je používán na záznamové sadě.
určuje, která pole jsou zapojena do omezení. Omezení je automaticky vyhodnoceno
když se některý z těchto polí změní. Metoda očekává
vznést výjimku, pokud není splněna jeho invariantní podmínka::

od odoo.exceptions import ValidationError

    ...

@ApiConstant(„datum_konce“)
def _check_date_end(self):
pro rekord v sobě:
pokud je datum ukončení záznamu menší než dnešní datum:
vyvolat ValidationError ("Datum ukončení nelze nastavit do minulosti")
        # Všechny záznamy prošly testem, nevrátí se nic

Jednoduchý příklad najdeme
„tady <https://github.com/odoo/odoo/blob/274dd3bf503e1b612179db92e410b336bfaecfb4/addons/stock/models/stock_quant.py#L239-L244>“.

... cvičení: Přidat omezení v Pythonu.

Přidejte omezení, aby prodejní cena nemohla být nižší než 90 % očekávané ceny.

Tip: Prodávaná cena je nula, dokud nebude nabídka potvrzena. Budete muset upravit svou
zkontrolovat, zda je tento faktor vztažen k účtu.

.... varování::

Vždy používejte metodu `~odoo.tools.float_utils.float_compare`.
Metoda:meth:`~odoo.tools.float_utils.float_is_zero` z knihovny `odoo.tools.float_utils`.
pracovat s plovoucími čísly.

Zajistěte, aby se omezení spouštělo pokaždé, když je změněna prodejní cena nebo očekávaná cena!

SQL omezení jsou obvykle efektivnější než Pythonová omezení. Když záleží na výkonu, vždy
dávají přednost omezením v SQL před omezeními v Pythonu.

Modul nemovitostí se nám začíná líbit. Přidali jsme nějakou logiku a teď zkontrolujeme
Data jsou konzistentní. Uživatelské rozhraní je však stále trochu hrubé. Podívejme se, jak to může vypadat.
Vylepšit ji v příštím kapitole:doc:`<11_sprinkles>`.

... Dokumentace PostgreSQL
.._tabulková omezení:
    https://www.postgresql.org/docs/12/ddl-constraints.html
