.. odkaz/účet daňový:

=====
Daně
=====

...automodel:odoo.addons.account.models.account_tax.AccountTax
:hlavní:

...... pole auto: jméno
... auto pole: typ daňového užití
.. pole s automatickým vyplněním: daňový rozsah
.. pole:: typ_částky
......autooblast:: aktivní
... auto pole: děti_daňové_identifikátory

... pole auto: částka
... auto-field:: popis

... auto pole: zahrnout základní částku
... auto pole: je_základní_objekt_postižen
......autooblast::analytická
......autooblast::faktura_rozúčtovací_řádky_id
......autofield::refund_repartition_line_ids
...... pole auto:: daňová skupina
.. pole:: daňová povinnost
......autočíslo::cash_basis_transition_account_id
