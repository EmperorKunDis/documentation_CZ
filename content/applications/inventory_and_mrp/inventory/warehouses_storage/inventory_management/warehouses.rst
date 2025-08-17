==========
Skladiště
==========

V aplikaci Odoo *Sklad* je sklad fyzickým prostorem s adresou pro uložení předmětů.
například skladovací prostory, distribuční centrum nebo fyzický obchod.

Každá databáze má přednastavený sklad s adresou společnosti. Uživatelé mohou nastavit více
sklady a vytvářet pohyby zásob (viz:Denní operace > Použití tras).
Mezi nimi.

Konfigurace
=============

Pro vytvoření nebo správu skladů přejděte na: „Aplikace Inventář --> Konfigurace“
Skladiště.

Poté vyberte existující sklad nebo vytvořte nový kliknutím na „Nový“. To otevře
skladový formulář, který obsahuje následující pole:

- :guilabel:`Sklad“ (*povinný údaj*): celé jméno skladu.
- :guilabel:`Krátké označení“ (*povinný údaj*): zkrácená kódová značka skladu (maximálně pět
(znaků). Zkratka pro výchozí sklad v Odoo je „WH“.

... důležité::
Výrobní značka se objevuje na skladovacích dokumentech, proto je doporučeno používat
vzpomínkový, jako například „WH[první písmena místa]“ (např. WHA, WHB atd.).

- :guilabel:`Adresa“ (*povinný údaj*): adresa skladu. Chcete-li změnit sklad,
adresu při vytváření dvou nebo více skladů, přejeďte myší nad pole a klikněte na
:icon:`fa-arrow-right` :guilabel:`(pravý směr).
- :guilabel:`Společnost` (*povinné pole*): společnost, která vlastní sklad; může být nastaveno jako
společnost, která vlastní databázi Odoo, nebo společnost zákazníka či dodavatele.
- :guilabel:`Intrastat region“: :doc:"název regionu
<../../../../finance/účetnictví/hospodářské výsledky/intraSTAT> pro společnosti působící v Evropě.
Společnost.

.. důležité::
Níže uvedené možnosti jsou k dispozici pouze tehdy, když je zapnutá funkce *Multistep Routes*.
:menu: „Aplikace inventáře --> Konfigurace --> Nastavení“.

- :guilabel:`Příchozí dodávky“: vyberte možnost, že chcete zboží přijmout ze skladu v
:doc:`jedna <../../shipping_receiving/daily_operations/dodání a přijetí zboží v jednom kroku>`,
<../../shipping_receiving/daily_operations/receipts_delivery_two_steps>`, nebo :doc:`tři
<../../přijímání a expedice/denní operace/příjem v třech krocích>.

- :guilabel:`Odeslané zásilky“: vyberte možnost dodání produktů ze skladu v
:doc:`jedna <../../shipping_receiving/daily_operations/dodání a přijetí zboží v jednom kroku>`,
<../../shipping_receiving/daily_operations/receipts_delivery_two_steps>`, nebo :doc:`tři
<../../přijímání a expedice/denní operace/doručení ve třech krocích> kroků.

- :guilabel:`Dodavatelé pro dropshipping“: k dispozici s funkcí „Subdodávky“.
:menu_selection:`Výrobní aplikace --> Konfigurace --> Nastavení“. Zaškrtněte tuto políčko, pokud chcete zakoupit
komponenty od dodavatelů a posílají je poddodavatelům.
- :guilabel:`Dodavatelé zásobování“: k dispozici s funkcí „Subdodávky“, zaškrtněte
zaškrtávací políčko, které dodavatelům poskytne suroviny skladované v konkrétním skladu.
- Zaškrtněte políčko „Výroba na doplnění“: zaškrtnutím tohoto políčka umožňujete výrobě předmětů v
tento sklad.
- Výrobce: zvolte, jestli chcete produkty vyrábět ve :doc:`jednom
<../../../manufacturing/basic_setup/one_step_manufacturing>`, :doc:`dva
<../../../manufacturing/basic_setup/two_step_manufacturing> nebo :doc:`tři kroky
<../../../výroba/základní nastavení/třístupňová výroba>.
- Zaškrtněte políčko „Nakoupit na doplnění“: zaškrtnutím políčka povolíte dodání nakoupených produktů.
skladu.
- :guilabel:`Dodávky z:‘: dostupné s více sklady v databázi, vyberte sklady
aby vyčistil zásoby, abychom mohli uspokojit poptávku.

.. viz také:
:doc:`Použijte inventurní úpravy k přidání zásob do nových skladů <počet produktů>`

.. obrázek: sklady/sklad-form.png
:align:center
:alt: Příklad skladového listu.

