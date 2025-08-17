.._odkaz/orm/historie změn:

=========
Seznam změn
=========

Odoo verze 18.0
=================

- Hledání podle jména je nyní implementováno jako pole „_search_display_name“ stejně jako všechny ostatní.
Podívejte se na požadavek číslo 174967.
- Nový způsob kontroly oprávnění a pravidel nyní kombinuje oba přístupy
a pravidla: „kontrola přístupu“, „má přístup“ a „filtrovaný přístup“.
Podívejte se na požadavek s číslem 179148.
- Překlady jsou k dispozici v sekci „Prostředí“ na adrese https://github.com/odoo/odoo/pull/174844.


Odoo Online verze 17.4
========================

- Vnitřní operátor inselect je odstraněn. Alternativou je použití in
s dotazem nebo objektem SQL. #171371 <https://github.com/odoo/odoo/pull/171371>_.


Odoo Online verze 17.3
========================

- Nyní můžeme seskupit podle částečných dat v poli read_group, pole _read_group a domén s číslem 159528 <https://github.com/odoo/odoo/pull/159528>.


Odoo Online verze 17.2
========================

- Atribut :attr:`group_operator` třídy :class:`~odoo.fields.Field` je přejmenován na
:attr:`sčítadlo“ s #127353 <https://github.com/odoo/odoo/pull/127353>“.
- Nyní můžeme seskupit/agregovat/seřadit podle souvisejícího pole no-store.
„#127353 <https://github.com/odoo/odoo/pull/127353>“.

Odoo Online verze 17.1
========================

- Metoda meth:~odoo.models.Model._flush_search byla zastaralá a
`#144747 <https://github.com/odoo/odoo/pull/144747>.
Flushing polí je nyní prováděn metodou:
a je založena na metadatech uložených v objektu :class:`~odoo.tools.SQL`.
:metoda:meth:`~odoo.models.BaseModel._search` a další nízkopoziční metody ORM
vytvářet takové objekty. Tyto metody jsou také zodpovědné za kontrolu přístupu
práva na polích, které jsou použity v objektu SQL.

Odoo verze 17.0
=================

- Vytvořte objekt wrapperu třídy `~odoo.tools.SQL`, který umožní sestavit SQL
je snazší a bezpečnější s ohledem na SQL injekce. Metody ORM nyní používají
interně. Zavedeno vrácením #134677 <https://github.com/odoo/odoo/pull/134677>_.

Odoo Online verze 16.4
========================

- Metoda meth:~odoo.models.Model.name_get byla zrušena s
`#122085 <https://github.com/odoo/odoo/pull/122085>`_.
Čtěte pole „jméno zobrazení“.

Odoo Online verze 16.3
========================

- Metoda meth:~odoo.models.Model._read_group má nový podpis s
`#110737 <https://github.com/odoo/odoo/pull/110737>`_

Odoo Online verze 16.2
========================

- Změnit implementaci metod pro vyhledávání a čtení, aby bylo možné
spojit oba v co nejmenším počtu dotazů SQL. Zavádíme dvě nové metody
:metoda ~odoo.model.Model.search_fetch a metoda ~odoo.model.Model.fetch
které využívají kombinace. Více informací najdete na stránkách s tahem
požadavek na změnu s číslem #112126 (<https://github.com/odoo/odoo/pull/112126>).

Odoo verze 16.0
=================

- Překlady polí, která byla přeložena, jsou uloženy jako hodnoty JSONB.
„#97692 <https://github.com/odoo/odoo/pull/97692>“
a číslo revize 101115 (<https://github.com/odoo/odoo/pull/101115>).
Překlady kódu již nejsou ukládány do databáze.
Stávají se statickými a jsou extrahovány z PO souborů, když je potřeba.
- Metoda ~odoo.models.Model.search_count bere v úvahu limit s parametrem #95589 <https://github.com/odoo/odoo/pull/95589>.
Zmenšuje počet záznamů, které se musí spočítat, což zlepšuje výkon, pokud je přijatelná částečná odpověď.

Odoo Online verze 15.4
========================

- Nový API pro odstranění dat z databáze a vymazání mezipaměti
„#87527 <https://github.com/odoo/odoo/pull/87527>“.
Do knihovny „odoo.models.Model“ a „odoo.api.Environment“ byly přidány nové metody
a jsou méně matoucí v tom, co se skutečně dělá v každém případě.
Podívejte se na část :ref:`Výkonnost SQL <reference/orm/sql>“.

Odoo Online verze 15.3
========================

- Argument „args“ je přejmenován na „doménu“ pro metodu „hledání“, „počet hledaných položek“.
a metoda :meth:`~odoo.models.Model._search`.
- Metoda ~odoo.models.Model.filtered_domain zachová pořadí aktuálního záznamového souboru.
- Metoda ~odoo.models.Model.browse neakceptuje jako id hodnotu typu str. #83687
- Metody :meth:`~odoo.models.Model.fields_get_keys` a :meth:`~odoo.models.Model.get_xml_id` na třídě :class:`~odoo.models.Model` jsou zastaralé. `#83687 <https://github.com/odoo/odoo/pull/83687>`
- Metoda:meth:`~odoo.models.Model._mapped_cache` je odstraněna. #83687
- Odeberte atribut :attr:`limit` tříd :class:`~odoo.fields.One2many` a :class:`~odoo.fields.Many2many`.

Odoo Online verze 15.2
========================

- Specifické typy indexů na polích: s #83274 <https://github.com/odoo/odoo/pull/83274>_.
#83015 <https://github.com/odoo/odoo/pull/83015>_, vývojáři mohou nyní definovat, jaký typ
indikátory mohou být použity na poli v PostgreSQL. Podívejte se na vlastnost :ref:`index <reference/fields>
`odoo.fields.Field`.
- Atribut :attr:`_sequence` třídy :class:`~odoo.models.Model` je odstraněn. Odoo umožňuje PostgreSQL používat výchozí sekvenci primárního klíče.
- Metoda:meth:`~odoo.models.Model._write` nevyvolává chybu při zápisu do neexistujících záznamů.
- Atributy :attr:`column_format` a :attr:`deprecated` třídy :class:`~odoo.fields.Field` jsou odstraněny. #82727 <https://github.com/odoo/odoo/pull/82727>
