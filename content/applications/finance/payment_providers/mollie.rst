======
Molly
======

„Mollie“ je internetová platební platforma založená v Nizozemsku.

Konfigurace
=============

.. viz též:
   - :ref:`platební metody/přidat novou`

Karta Povolení
---------------

Odoo potřebuje vaše **API Credentials** k propojení s vaším účtem Mollie, který zahrnuje:

- **Klíč API**: Testovací nebo živý klíč API v závislosti na konfiguraci poskytovatele.

Můžete si své přihlašovací údaje zkopírovat do svého účtu u Mollie a vložit je do příslušných polí pod
kartu Přihlašovací údaje.

Pro získání klíče API se přihlaste do svého účtu Mollie a přejděte na
:menu-vyber->Vývojáři-->Klíče API, a zkopírujte svůj klíč testovací nebo živé verze.

.. důležité::
Pokud se snažíte o testování Mollie pomocí klíče pro testovací režim, změňte stav na *Testovací režim*.
Doporučujeme provést tento postup na testovací databázi Odoo, nikoli na hlavní databázi.

.. viz též:
   - :doc:`../platební_prostředky`
