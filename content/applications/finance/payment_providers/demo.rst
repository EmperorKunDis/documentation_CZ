====
Demo
====

Demonstrativní platební poskytovatel společnosti Odoo vám umožňuje otestovat obchodní toky, které zahrnují transakce na internetu.
bez skutečných přihlašovacích údajů.

Konfigurace
=============

.. viz též:
:ref:`platební metody/přidat novou`

.. důležité::
Přepněte stav na :guilabel:`Testovací režim`.

Výsledek platby
===============

Při placení v obchodě nebo při platbě účtu online si můžete vybrat způsob platby pomocí demo
Poskytovatel platebních služeb. Klikněte na položku „Stav platby“ a vyberte možnost
požadovaný výsledek.

.. obrázek: demo/demo-payment-outcome.png
:align:center
:alt:Výsledky platebního stavu.

Stav transakce
=================

Pokud jste zvolili jako výsledek platby :guilabel:`Čekající“, můžete změnit stav
transakci přímo z jejího pohledu na formulář. Pro přístup k formuláři transakce aktivujte
:ref:`rozvojový režim <developer-mode>“ a přejděte do „Účetnictví / Webová stránka“.
Konfigurace --> Platební transakce. Pak změňte stav transakce kliknutím na
státní advokátka (:guilabel:"Návrh, Čeká na schválení, Autorizováno, Potvrzeno, Zrušeno, Chyba").

.. obrázek: demo/demo-view-form.png
:align:center
:alt:Stavová lišta transakce.
