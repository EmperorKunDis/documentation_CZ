=====================
Spojení společností Silverfin
=====================

„Silverfin“ je třetí stranou, která poskytuje služby cloudu
platforma pro účetní.

Odoo a Silverfin poskytují integraci, která automaticky synchronizuje data.

Konfigurace
=============

Pro nastavení této integrace musíte do svého účtu Silverfin zadat následující údaje:

- e-mailová adresa uživatele
- :ref:`Odoo API klíč <silverfin/api-key>`
- URL databáze Odoo
- název vaší databáze Odoo

.. _silverfin/api-key:

API klíč Odoo
------------

Můžete vytvořit externí klíče API pro jednu databázi buďto:
(hostování: Odoo Online, On-premise, Odoo.sh) nebo :ref:`pro všechny databáze spravované jedním uživatelem
<stříbrnoploutvý/api-víceúčetní> (hosting: Odoo Online).

.. důležité::
   - Tyto klíče API jsou osobní a poskytují plný přístup k vašemu uživatelskému účtu. Uchovávejte je v bezpečí.
   - API klíč můžete zkopírovat pouze při jeho vytvoření. Později jej již nelze získat zpět.
   - Pokud budete potřebovat další klíč API, vytvořte si nový (a smažte ten starý).

.. viz též:
:doc:`/rozvoj/odkaz/externí_api`

.._stříbrnoploutvá/api-singledb:

Podle databáze
~~~~~~~~~~~~

Chcete-li přidat klíč API k jedné databázi, připojte se k ní, zapněte vývojářské rozhraní.
režim vývojáře (developer-mode)“, klikněte na uživatelské menu a poté „Můj profil“
:guilabel:`Nastavení“. V sekci „Bezpečnost účtu“ klikněte na „Nový API klíč“.
Zadejte heslo, potvrďte heslo, zvolte pro nový klíč popisný název a zkopírujte API klíč.

.. obrázek: stříbrnák/api-key-db.png
:alt: vytvoření externího klíče API pro databázi

.. viz též:
:ref:`api/externí_api/klíče`

..._stříbrnoploutvá/api-multidb:

Pro všechny databáze (správce)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Přidat klíč API k **všem** databázím spravovaným jedním uživatelem najednou **(nejjednodušší
pro správce)**, přejděte na webovou stránku „Odoo“ (<https://www.odoo.com>), a zaregistrujte se pomocí
vaše administrátorské účty. Poté otevřete „Nastavení zabezpečení vašeho účtu v režimu vývojáře
<https://www.odoo.com/my/security?debug=1>`, klikněte na „Nová klíčová slova“ a potvrďte
heslo, vytvořte pro nový klíč popisný název a zkopírujte nový API klíč.

.. tip::
Otevřete „správce databází“ (<https://www.odoo.com/my/databases>). Zobrazí se všechny databáze, které budou
být propojen s jediným API klíčem.

.. obrázek: stříbrná ryba/api-key-user.png
:alt: vytvoření externího klíče API pro uživatele Odoo
