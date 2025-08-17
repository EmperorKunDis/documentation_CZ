=============
Rozhodnutí o ceně
=============

Při cash roundingu je nutné použít nejnižší fyzickou nominální hodnotu
menší než minimální jednotka.
účtu.

Například některé země vyžadují od svých společností, aby částky zaokrouhly nahoru nebo dolů.
snížit celkovou částku faktury na nejbližších pět centů.
Platba je v hotovosti.

Každý prodejní místo v Odoo lze konfigurovat tak, aby se používalo konečné sčítání peněz.
k celkovým částkám účtů nebo faktur.

Konfigurace
=============

Přejděte do sekce „Prodejní místo“ > „Konfigurace“ > „Nastavení“.
a zapněte možnost „Rovná se na hotovost“, pak klikněte na tlačítko „Uložit“.

.. obrázek: cash_rounding/cash_rounding01.png


Přejděte na:menu:Prodejní místo --> Konfigurace --> Prodejní místo
Sale`, otevřete bod prodeje, který chcete nakonfigurovat, a zapněte
Možnost „Rovná se kasou“.

Pro definování metody zpracování chyby otevřete seznam a klikněte na
v položce Create and Edit...

Zde definujte svou přesnost zaokrouhlování, účet zisku a
*Ztrátový účet*, pak uložte oba způsoby kulacích a bod
Nastavení prodeje.

.. obrázek: cash_rounding/cash_rounding02.png


Všechny celkové částky z této prodejny nyní přidávají řádek, kde se aplikuje
podle vašich nastavení.

.. obrázek: cash_rounding/cash_rounding03.png


.. poznámka::
Odoo Point of Sale podporuje pouze strategii „Přidat linii zaokrouhlování“ (:guilabel:`Add a rounding line`).
