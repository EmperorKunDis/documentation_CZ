================
Aplikace a moduly
================

:ref:`Instalace <general/install>“, :ref:`Aktualizace <general/upgrade>` a :ref:`Odinstalování
Odinstalujte všechny potřebné aplikace a moduly z panelu „Aplikace“.

Výchozí filtr je „Aplikace“. Chcete-li vyhledávat moduly také, zvolte
:guilabel:`Extra“ z :icon:`fa-filter“ :guilabel:`Filtrů“.

.. obrázek: apps_modules/apps-search-filter.png
:alt:Přidejte filtr „Extra“ do aplikací Odoo.

.. varování:
Přidáním nebo odstraněním aplikací můžete výrazně ovlivnit ostatní aplikace v databázi a změnit
účtování za předplatné. Zvažte pečlivě nebo otestujte změny v testovacím prostředí, než
řízení.

   - **Administrátoři spravují databázi**: Administrátor databáze je zodpovědný za
jejich používání, protože nejlépe vědí, jak jejich organizace funguje.
   - **Aplikace Odoo mohou mít závislosti**: Nainstalování některých aplikací a funkcí s
A také nainstalovat další aplikace a moduly, které jsou technicky potřebné, i když uživatelé databáze
nepoužívejte je aktivně.
   - **Duplikovat databázi pro testování aplikací**: Testování na duplicitní databázi odhalí, co aplikaci
závislosti mohou být vyžadovány nebo jaká databáze bude smazána. Naučte se duplikovat
:doc:`Online databáze Odoo <../../administration/odoo_online> nebo :doc:`Klientská instalaci Odoo
databáze <../../správy/na_půdě>.

..._instalace/generální:

Nainstalujte aplikace a moduly
========================

Otevřete hlavní panel aplikace Odoo a poté zvolte možnost „Aplikace“. Poté klikněte na vyhledávací lištu.
Najít aplikaci k instalaci nebo posunout se k ní. Zde klikněte na tlačítko „Aktivovat“
karta aplikace.

.. poznámka::
Pokud se v seznamu aplikací nebo modulů, které mají být nainstalovány, nezobrazí, aktualizujte seznam aplikací aktivací
:ref:`vývojářský režim <developer-mode>“ a poté přejděte na „Aplikace --> Aktualizovat aplikace
List a pak klikněte na tlačítko „Aktualizovat“.

.._generální/upgrade:

Aktualizujte aplikace a moduly
========================

S každým novým vydáním aplikace Odoo (viz <administration/supported_versions>) se objevují nové funkce nebo aplikace.
byly přidány nové funkce, které lze používat po aktualizaci aplikace.

Přejděte na:menu: „Aplikace“ a pak v aplikaci k aktualizaci klepněte na ikonu: „fa-ellipsis-v“
Ikona „Vodorovná elipsa“ a výběr „Aktualizovat“.

.._souborů generálního/odinstalovat:

Odinstalujte aplikace a moduly
==========================

.. nebezpečí::
Odinstalování aplikací také odstraní jejich záznamy v databázi. Otestujte odinstalování aplikací na kopii
databáze před odstraněním aplikací na produkční databázi.

.. poznámka::
Některé aplikace mají závislosti, což znamená, že jedna aplikace vyžaduje jinou. Proto je třeba odinstalovat
Aplikace může odinstalovat více aplikací a modulů.

Přejděte do sekce „Aplikace“ a poté klikněte na aplikaci, kterou chcete odinstalovat.
:guilabel:`(vertikální elipsa)` ikona a vyberte :guilabel:`Odinstalovat“ pro otevření
Pop-up okno „Odinstalovat modul“.

Seznam aplikací k odinstalování je uveden v části „Aplikace k odinstalování“.

.. tip::
Vyberte zaškrtávací políčko „Zobrazit všechny“ a zobrazte všechny závislosti modulu.

Sekce „Dokumenty k smazání“ obsahuje databázové záznamy, které mají být odstraněny.

Pokračovat v odinstalování aplikace, jejích závislostí a všech souvisejících databázových záznamů klikněte
:guilabel:`Odinstalovat“.

.. obrázek: apps_modules/uninstall.png
:alt:Karta aplikace s vyznačeným menu „Odinstalovat“.

.. příklad::
Aplikace Restaurant vyžaduje aplikaci Point of Sale k fungování, takže odinstalujte
Aplikace **Point of Sale** také odinstaluje aplikaci **Restaurant** a všechny související záznamy.

...... obrázek: apps_modules/uninstall-deps.png
:alt:Varovný vzkaz, který zobrazuje aplikace, které jsou odinstalované, pokud je odinstalace dokončena.
