Zobrazit obsah

===========
Začněte
===========

Když poprvé otevřete aplikaci účetnictví v Odoo, zobrazí se na :guilabel:`Účetní přehled`.
krok za krokem seznamovací baner, průvodce, který vám pomůže začít. Tento seznamovací baner je
zobrazeno, dokud si nevyberete zavřít ho.

Nastavení viditelné v uvítacím banneru lze později změnit kliknutím na
:menu:"Účetnictví -> Konfigurace -> Nastavení".

.. poznámka::
Odoo účetnictví automaticky nainstaluje příslušný balíček pro fiskální lokalizaci pro vaši zemi.
Společnost podle země, kterou si zvolíte při vytváření databáze. Takto se dostanete k správnému
účty, zprávy a daně jsou připravené.
pro více informací o daňových balíčcích.

Bannery pro přivítání nových účetních
============================

Krok za krokem probíhá proces přijímání účetnictví v reklamním banneru, který je rozdělen do čtyř kroků:

.. obrázek:get_started/accounting-onboarding-banner.png
:alt: Bannery krok za krokem v Odoo účetnictví

#:ref:`účetní období“
#:ref:`účetní nastavení banka“
#:ref:`účetní nastavení daně“
#:ref:`účetní nastavení grafu

.._doba nastavení účetnictví:

Účetní období
------------------

Definujte datum otevření a zavření fiskálního roku, které se používají k generování reportů
automaticky a nastavte si frekvenci podání daňového přiznání, včetně upozornění na to, abyste nikdy nezapomněli na daň.
termínu pro vrácení.

Výchozí datum otevření je 1. ledna a datum uzavření 31.
Prosinec, protože je to nejčastější použití.

.. poznámka::
Můžete také změnit tyto nastavení přejdete-li na:
Nastavení --> Daňové období“ a aktualizovat hodnoty.

..._účetní nastavení banky

Bankovní účet
------------

Připojte svůj bankovní účet k databázi a nechte si automaticky synchronizovat výpisy z banky.
takže najděte svou banku v seznamu, klikněte na „Připojit“ a postupujte podle pokynů na obrazovce.

.. poznámka::
:doc:`Chcete-li se dozvědět více o této funkci, klikněte sem <bank/bank_synchronization>.“

Pokud vaše bankovní instituce nemůže být automaticky synchronizována nebo pokud si přejete nechat ji
databáze, můžete si také manuálně nastavit svůj účet v bance tak, že zadáte jeho název a kliknete
Vytvořit bankovní účet“ a vyplnit formulář.

- :guilabel:`Název účtu“: název bankovního účtu zobrazený v Odoo.
- :guilabel:`Číslo účtu“: číslo vašeho bankovního účtu (IBAN v Evropě).
- Klikněte na „Vytvořit a upravit“ a zadejte podrobnosti o bance. Přidejte
bankovní instituce: její název a identifikační kód (BIC nebo SWIFT).
- :guilabel:`Kód“: tento kód je vaším :guilabel:`Krátkým kódem“, jak je zobrazen v Odoo.
Výchozí nastavení je takové, že Odoo vytvoří novou knihu s touto zkratkou.
- :guilabel:„Kniha bankovních transakcí“:Toto pole se zobrazí, pokud máte existující bankovní knihu, která není
spojený s bankovním účtem. Pokud ano, pak vyberte záznamní knihu, kterou chcete použít k zaznamenání
finanční transakce spojené s touto bankovní účet nebo vytvořit nový kliknutím
:guilabel:`Vytvořit a upravit“.

.. poznámka::
   - Nástroj umožňuje přidat libovolný počet účtů, a to tak, že se dostanete na
:menu_selecce:`Účetnictví --> Konfigurace --> Přidat bankovní účet`.
   - Klikněte zde pro více informací o bankovních účtech.

.._účetní nastavení a daně:

Daně
-----

Tento nástroj vám umožní vytvářet nové daně, deaktivovat nebo upravit stávající daňové sazby.
:dokumentu: „lokalizační balíček <../fiscal_localizations>“ nainstalovaný na vaší databázi,
Váš stát je již nakonfigurován.

.. poznámka::
Klikněte zde <taxes> pro více informací o daních.

..._sestavení účetní knihy:

Kontrolní účet
-----------------

S pomocí této nabídky můžete k účtům v **Knize jízd** přidávat účty a uvádět jejich počáteční
účetní zůstatky.

Základní nastavení jsou zobrazena na této stránce, aby vám pomohla prohlédnout si svůj účetní rozvahový list.
nastavení účtu, klikněte na tlačítko „Nastavení“ v závěru řádku.

.. obrázek::get_started/setup_chart_of_accounts.png
:alt:Nastavení účetních knih a jejich otevřených zůstatků v Odoo Accounting

.. poznámka::
:doc:`Klikněte zde <get_started/chart_of_accounts> pro více informací o tom, jak nastavit svůj
Výkaz zisku a ztráty.

Fakturační banner přihlášení na palubě
===========================

Další krok za krokem je banner, který vám pomůže využít fakturační modul Odoo.
a aplikace pro účetnictví. Banner přivítání při používání
Fakturační aplikace namísto účetní aplikace.

Pokud máte v databázi nainstalovanou aplikaci Odoo Accounting, můžete se k ní dostat tak, že přejdete na
:menu:"Účetnictví --> Zákazníci --> Faktury".

Přihlášení do fakturačního systému se skládá ze čtyř hlavních kroků:

.. obrázek: get_started/invoicing-onboarding-banner.png
:alt: Krok za krokem na palubě v Odoo Fakturaci

#:ref:`fakturační nastavení společnosti“
#:ref:`fakturační sestava/formát“
#:ref:`fakturace-nastavení-daňového dokladu“
#:ref:`fakturace-nastavení-platby

.._fakturační nastavení společnosti:

Společnost
------------

Přidejte do svého profilu podrobnosti o vaší společnosti, jako je název, adresa, logo, webová stránka, telefonní číslo a e-mail.
a daňové identifikační číslo nebo DIČ. Tyto údaje jsou pak zobrazeny na vašich dokumentech, jako například fakturách.

.. poznámka::
Můžete také změnit podrobnosti o společnosti kliknutím na:menu-selection:Nastavení --> Obecné
Nastavení“, posunout se do části „Společnosti“ a „Aktualizovat informace“.

..._fakturační nastavení a rozložení

Uspořádání dokumentů
----------------

Upravte výchozí vzor faktury podle návodu :ref:`Výchozí vzor faktury <studio/pdf-reports/default-layout>`.

.. poznámka::
Můžete také změnit vzhled faktury, když přejdete na:menu:Nastavení --> Obecné
Nastavení“, posunutím dolů do sekce „Společnosti“ a kliknutím na „Konfigurovat“.
„Vzhled dokumentu“.

.._fakturaci-a-vytváření-faktur:

Vystavit fakturu
--------------

Vytvořte svůj první fakturační doklad.

.. tip::
Přidejte své číslo bankovního účtu a odkaz na svá Obecná ustanovení v zápatí.
Takto je možné najít plnou verzi smluvních podmínek na internetu bez nutnosti tisknout.
Je možné je uvádět na fakturách, které vystavujete.

... _fakturaci a nastavení plateb:

Online platby
---------------

Začněte s platbami pomocí služby Stripe a umožněte bezpečné integrované platby kreditními a debetními kartami v systému Odoo.

.. tip::
Chcete-li používat jiné platební metody, přejděte na
:guilabel:`Fakturace --> Konfigurace --> Způsoby platby“ a
:doc:`zapnout požadované poskytovatele platebních služeb <../payment_providers>.


.. viz též:
   * :doc:`banka“
   * :doc:`jak-zacit/uctovani-na-knihach“
   * :doc:`get_started/consolidation“
   * :doc:`bank/bank_synchronizace`
   * :doc:`../daňové lokality“
   * „Návody k Odoo: Účetnictví a fakturace – Začínáme [video]
<https://www.odoo.com/slides/slide/getting-started-7063>

..toctree::


get_started/cheat_sheet
get_started/účetní kniha
začít/konzolidaci
get_started/multiměnová
get_started/průměrná cena
get_started/daňové jednotky
