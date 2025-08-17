
.. _avatax/portal:

=======================
Portál Avalara (Avatax)
=======================

Správcovská konzole společnosti Avalara (AvaTax) nabízí možnosti správy účtu včetně: zobrazení / editace
transakce odeslané z Odoo do AvaTaxu, podrobnosti o výpočtu daní, daňové hlášení.
správa osvobození od daně a zdroje pro podání daňového přiznání.

.. tip::
Avalara je vývojář softwaru pro daňovou evidenci, *AvaTax*.

Chcete-li se dostat k konzole, nejprve přejděte na sandbox Avalara
<https://sandbox.admin.avalara.com/>` nebo `produkční <https://admin.avalara.com/>` prostředí.
Toto bude záviset na typu účtu, který byl nastaven v integraci :doc:`<../avatax>`. Přihlaste se
správce.

.. obrázek: avalara_portal/avalara-portal.png
:align:center
:alt: Dashboard společnosti Avalara po přihlášení do portálu pro správu.

.. viz též:
Pro více informací se podívejte na dokumentaci společnosti Avalara: „Aktivujte svůj portál zákazníka v oblasti komunikace“
účet
<https://community.avalara.com/support/s/document-item?language=en_US&bundleId=qvv1656594440497&topicId=Activate_your_Communications_Customer_Portal_account.html&_LANG=enus>

... _avalara/portal-transactions:

Transakce
============

Pro přístup k transakcím klepněte na odkaz „Transakce“ v hlavním panelu.
Přihlásit se do portálu Avatax. Chcete-li přistupovat k stránce Transakce ručně, zatímco jste přihlášeni
konzoli Avalara přejděte na: „Transakce“ -> „Transakce“.

.. obrázek: avalara_portal/avalara-transactions.png
:align:center
:alt:Portál společnosti Avalara s vyznačeným zkratkem transakcí.

Upravit transakci
----------------

Klikněte na transakci, abyste získali další informace o této transakci. Tyto informace zahrnují
sekce „Podrobnosti faktury“, „Další informace“ a „Informace o zákazníkovi“.
Klikněte na ikonu „Penál“ a poté na „Upravit podrobnosti transakce“, abyste mohli změnit transakci.

K faktuře lze přidat pole „Sleva“, které se hodí zejména v případě, kdy
Transakce již byla synchronizována s Avalarou / AvaTaxem a změny musí být provedeny později.

... _avalara/portal-filter:

Filtr
------

Filtrujte transakce na stránce „Transakce“ nastavením „Od“ a
„To“ pole a nastavit další pole pro filtrování včetně:

- „Stav dokumentu“: libovolné z následujících možností: „Všechny“, „Zrušeno“.

- „Kód dokumentu“: jedna z následujících možností:
:guilabel:`Začíná na“, nebo :guilabel:`Obsahuje“.
- :guilabel:`Kód zákazníka/dodavatele“: kód zákazníka/dodavatele v Odoo (např. „Kontakt 18“).
- :guilabel:`Země“: země, pro kterou byla tato daň vypočítána; pole obsahuje text.
- „Region“: oblast země, která se liší podle „Země“.
výběru.

Klikněte na ikonu „+“ a zvolte filtry.

- :guilabel:`Dokumentový typ“: libovolná z následujících možností, :guilabel:`Všechny“, :guilabel:`Prodej
Faktura, Přijatá faktura, Vrácená faktura, Skladová převod
Výchozí faktura, „Převod zásob do výstupu“ nebo „Transfer Customs“.
Faktura.
- :guilabel:`Importní identifikátor“: představuje importní identifikátor dokumentu.

Řadit podle
-------

Na stránce „Transakce“ budou transakce uvedeny podle nastavení.
:ref:`avalara/portal-filter`, které se nacházejí v horní polovině stránky. Následující sloupce jsou
výchozí, řazení podle vzestupného nebo sestupného pořadí:

- :guilabel:`Kód dokumentu“: jedna z následujících možností:
:guilabel:`Začíná na“, nebo :guilabel:`Obsahuje“.
- :guilabel:`Stav dokumentu“: jedna z následujících možností: :guilabel:`Všechny“, :guilabel:`Zrušené“.

- :label:„Kód zákazníka/dodavatele“: Jedná se o kód zákazníka nebo dodavatele v Odoo (např. Kontakt 18).
- :guilabel:`Krajina`: toto je krajina země, tento se bude lišit podle
:guilabel:`Země“
- :label_částka: číselná částka celkové částky na dokladu Odoo.
- :guilabel:'Daň': Násobek daňového základu a daně.

.. obrázek:avalara_portal/transactions.png
:align:center
:alt:Stránka transakcí na portálu Avalara s filtrem a možností třídění vyznačená.

Upravte sloupce
~~~~~~~~~~~~~~~~~

Další sloupce lze přidat kliknutím na ikonu „Nastavení sloupců“ (viz ikona „fa-cog“).
vzniklé okno přesunutím kurzoru na položku „sloupec“
změnila.

Následující sloupce lze přidat pro další transakční informace:

- :guilabel:`AvaTax vypočítal“: daň vypočtená pomocí *AvaTaxu*.
- :guilabel:`Země“: země, pro kterou byla tato daň vypočítána; pole obsahuje text.
- :guilabel:`Kód zákazníka/dodavatele“: kód zákazníka nebo dodavatele v Odoo (např. „Kontakt 18“).
- :guilabel:`Měna“: standardizovaná zkratka měny, ve které je vyjádřen celkový obnos.
- :guilabel:`Datum vytvoření dokumentu“: datum vzniku dokumentu.
- :guilabel:Stav dokumentu: libovolná z následujících možností: :guilabel:Všechny, :guilabel:Zrušené

- Vyberte jeden z následujících výběrů: Všechny, Prodej
Faktura, Přijatá faktura, Vrácená faktura, Skladová převod
Výchozí faktura, „Převod zásob do výstupu“ nebo „Transfer Customs“.
Faktura.
- :guilabel:`Importní identifikátor“: představuje importní identifikátor dokumentu.
- :guilabel:`Poslední změna“: čas poslední úpravy dokumentu.
- :guilabel:`Kód místa“: kód místa používaný k výpočtu daně na základě dodání
adresa.
- :guilabel:`Číslo objednávky“: číslo objednávky.
- :guilabel:`Referenční kód“: odoo referenční kód (např. NV/2024/00003)
- „Oblast“: oblast země se mění podle „Země“.
výběru.
- :guilabel:`Kód prodejce“: číselný identifikátor uživatele přiřazeného k objednávce v Odoo.
- :guilabel:`Datum daně“: měsíc, den a rok výpočtu daně.
- :guilabel:`Typ přeplatku daně“: v poli, kde by se měla objevit výjimka, pokud žádná není,
populace se vytváří s hodnotou None.

Přidat novou sloupec můžete kliknutím na ikonu „+“ v sekci „Sloupce“.

.. viz též:
Pro více informací o transakcích *AvaTax* se podívejte na tuto dokumentaci společnosti Avalara: „Transakce
<https://community.avalara.com/support/s/document-item?language=en_US&bundleId=qvv1656594440497&topicId=transactions.html&_LANG=enus>

Import-export
-------------

Přejděte na stránku „Transakce portálu“ a klikněte na ikonu „Stáhnout“
transakce“ nebo „:icon:`fa-upload` :guilabel:`Import/export transakcí“ pro import nebo export transakcí.

Zprávy
-------

Pro přístup k reportům přejděte na odkaz „Zprávy“ v horním menu společnosti Avalara.
správce konzole. Poté vyberte jednu z dostupných záložek pro reportování: „Transakce
Zprávy o odpovědnosti a daňových přiznáních“ nebo „Zprávy o osvobození“.

.. tip::
Dále je zde záložka „Oblíbené“ a „Stahování“.
:guilabel:`Oblíbené“ záložka obsahuje všechny uložené konfigurace zpráv pro uživatele Avalara.
:guilabel:`Stahování“ obsahuje seznam, kde uživatel může stáhnout vysoké objemy dat.
transakční zprávy vytvořené za posledních 30 dní.

Vyberte kategorii zprávy v poli „Kategorie zprávy“ a název zprávy v poli „Název zprávy“.
sekci „Vybrat zprávu“.

Dále vyplňte část „Vybrat podrobnosti o zprávě“. Tyto možnosti se budou lišit v závislosti na
výše uvedené záložce.

V části označené „Zpráva“ jsou k dispozici následující dvě možnosti v závislosti na velikosti zprávy.
Vyberte přibližný počet transakcí pro váš výkaz. Vytvořit a
stáhnout zprávu okamžitě“ (pro malé zprávy) a „Vytvořit a stáhnout zprávu v
zadní“ (pro větší zprávy). Vyberte jednu nebo druhou podle objemu
transakce v tomto hlášení.

V neposlední řadě pod sekcí s názvem „Náhled zprávy a export“ vyberte
formát souboru ke stažení. Buď :guilabel:`.PDF` nebo :guilabel:`.XLS“ lze vybrat.
soubor lze prohlédnout kliknutím na možnost „Náhled“.

Po provedení všech konfigurací klikněte na tlačítko „Vytvořit zprávu“ pro stažení zprávy.
:icon:`fa-star-o` :guilabel:`Uložit tento report jako oblíbený“ k uložení konfigurace reportu.
oblíbené uživatele.

Po vytvoření zprávy klikněte na tlačítko :icon:`fa-download` :guilabel:`Stáhnout soubor“ a stáhněte si soubor.
zařízení.

.. tip::
Vyberte si přednastavený report z sekce „Často používané zprávy“ v části :guilabel:`Souhrnné zprávy
přehledový panel.

Přístup k tomuto seznamu získáte klepnutím na možnost „Zprávy“ v horním menu společnosti Avalara.
správce konzole a posuňte se na konec stránky.

.. viz též:
‚Podívejte se na dokumentaci společnosti Avalara: Zprávy v AvaTax
<https://community.avalara.com/support/s/document-item?language=en_US&bundleId=rjq1671176624730&topicId=Reports_in_AvaTax.html&_LANG=enus>

Přidejte více jurisdikcí
======================

Další daňová místa (daňové lokality) lze přidat v konzole pro správu Avalara. Přejděte na
buď „pískoviště“ společnosti Avalara („https://sandbox.admin.avalara.com/“) nebo „produkční“ verze.
<https://admin.avalara.com/>_ prostředí. To závisí na tom, jaký typ účtu byl nastaven v
:doc:`integrace <../avatax>“.

Dále přejděte na „Nastavení“ -> „Kde platíte daň“. Vyberte mezi třemi
různé záložky podle potřeby podniku. První záložka je: „DPH a spotřební daň“.
kde se dá vybírat daň pro Spojené státy. Klikněte na :icon:`fa-plus` :guilabel:`Přidat do
Přidáte další místo, kde společnost vybírá daň z prodeje a užívání.

Druhou možností je záložka „DPH / DPH“, kde můžete pomocí ikonky „+“ přidat další zemi.
nebo území, kde vybíráte DPH/GST, můžete zvolit další zemi nebo území,
Společnost vybírá DPH.

Na konci je pak záložka „Cla“, kde lze přidat zemi, pro kterou
Společnost vybírá clo. Jednoduše klikněte na ikonu „+“ a zvolte „Přidat zemi
Kde se vám zobrazí ikonka pro výpočet cla.

.. obrázek: avalara_portal/where-you-collect-tax.png
:align:center
:alt: Správa daně AvaTax v konzole pro správu daňových povinností na stránce Kde se daně platí s tlačítkem Přidat.
zvýrazněn daňový řádek z daně z přidané hodnoty a spotřební daně.

.. viz též:
‚Podívejte se na dokumentaci společnosti Avalara: Přidání místních daní
<https://community.avalara.com/support/s/document-item?language=en_US&bundleId=bla1700809896571_bla1700809896571&topicId=nbw1698727575499.html&_LANG=enus>

Osvobození od daně
=========================

Daňové osvobození pro zákazníky lze přidat do správy konzole Avalara, takže
Společnost AvaTax je schopna určit, které zákazníci mohou být osvobozeni od platby některých daní.
certifikát* přejděte na:menu-selection:„Výjimky“ --> „Zákaznický certifikát“. Zde klikněte na
:ikonka:fa-plus: guilabel:Přidat certifikát, abyste mohli vytvořit výjimku.

.. varování:
Pro připojení je potřebná předplatná služby Avalara na správu výjimky z daně (ECM).
obrázky certifikátů a být připraveni na audit. Více informací o tom, jak se k této službě přihlásit, najdete na
„Avalara
<https://community.avalara.com/support/s/document-item?language=en_US&bundleId=hff1682048150115_hff1682048150115&topicId=fol1682356576230.html&_LANG=enus>

Operace na konci roku
======================

Mezi služby společnosti Avalara patří zpracování daňového přiznání, které je třeba podat na konci roku.
rok. Chcete-li získat přístup k daňovým službám společnosti Avalara, přihlaste se do portálu pro správu
<https://admin.avalara.com/>`_. Poté klikněte na hlavní panel a vyberte možnost „Návraty“.
Avalara uživatele vyzve k přihlášení z důvodu bezpečnosti a přesměruje jej na stránku „Vrácení“.
portál.

.. obrázek: avalara_portal/avalara-returns.png
:align:center
:alt:Portál společnosti Avalara s vyznačeným odkazem na vrácení daně.

Klikněte na tlačítko „Začněte“ a zahajte proces podání daní. Pro více informací se podívejte sem
Dokumentace společnosti Avalara: „O řízených vraceních
<https://community.avalara.com/support/s/document-item?language=en_US&bundleId=hps1656397152776_hps1656397152776&topicId=Learn_about_Managed_Returns.html&_LANG=enus>

.. tip::
Alternativně klikněte na tlačítko „Návrat“ v horním menu společnosti Avalara.
správní konzole.

.. viz též:
   - :doc:`../avatax`
   - :doc:`avatax_use`
   - Daňová souladnost v USA: Video Avatax elearning

