Zobrazit obsah

========
Platby
========

V Odoo lze platby buď automaticky propojit s fakturou nebo zálohovou fakturou nebo je nechat jako samostatný záznam.
na pozdější použití:

- Pokud je platba spojena s fakturou nebo účtem, snižuje částku dluhu.
faktura. Na jednu fakturu je možné provést více plateb.

- Pokud je platba **nepropojena s fakturou nebo účtem**, zákazník má vůči poskytovateli služeb
firma nebo firma má nedoplatek u dodavatele. Tyto nedoplatky
snížit/vyrovnat nedoplatky za faktury.

.. viz též:
   - :doc:`Vnitřní převody <bank/internal_transfers>`
   - :doc:`bankovní účet/srovnání“
   - „Tutoriály Odoo: Konfigurace bankovnictví
<https://www.odoo.com/slides/slide/bankovní-konfigurace-6832>

...účetnictví/fakturace/způsoby platby:

Způsoby platby
===============

Odoo nabízí několik způsobů platby, abyste mohli nastavit různé konfigurace pro různé typy
Způsobů platby. Mezi příklady patří manuální platby (např. hotovost) a šeky
<platební příkazy/>“, a souborů s hromadnými platbami (např. :ref:`NACHA
<l10n_us/ach-electronic-transfers> a :doc:`SEPA <payments/pay_sepa>). Platby mohou být
konfigurované v záložkách „Příchozí platby“ a „Odeslané platby“ na účtu banky
hotovostní deník.

.. viz též:
:doc:`../sales/point_of_sale/payment_methods` pro Point of Sale

.. účetnictví/úhrady/přednostní způsoby platby:

Předvolená platební metoda
------------------------

Předvolenou platební metodu kontaktu lze nastavit tak, aby při vytváření platby pro tento kontakt
Způsob platby je automaticky vybrán jako výchozí. Faktury a faktury lze filtrovat podle
:guilabel:`Způsob platby“ usnadnit :ref:`skupinu <účetnictví/platby/skupiny-plateb>“.

Chcete-li nastavit preferovaný způsob platby pro zákazníka nebo dodavatele, přejděte na
:menuselection:`Účetnictví -> Zákazníci -> Zákazníci“ nebo „Účetnictví -> Dodavatelé
Vyberte dodavatele nebo odběratele a v záložce „Prodej a nákup“
kontaktní formulář, vyberte preferovanou platební metodu v sekci „Prodej“
fakturačním nebo dodavatelským fakturám v sekci „Nákup“.

.. tip::
Přistupujte k celému seznamu kontaktů z seznamu „Zákazníci“ nebo „Dodavatelé“.
Pokud chcete vidět všechny uživatele, můžete filtr „Zákazníci“ nebo „Dodavatelé“ odstranit.
celý seznam kontaktů prostřednictvím aplikace Kontakty.

..účetnictví/platby/šeky:

Kontroly
------

:doc:`Faktury dodavatelů lze zaplatit šekem <platební metody/platební metoda_checky> pomocí vstupního platebního příkazu
metoda, která umožňuje sledovat čísla šeků a tisknout šeky přímo z Odoo.

Pro příchozí platby od zákazníků můžete použít výchozí platební metodu „Manuální platba“.
metoda nebo můžete vytvořit platební metodu speciálně pro šeky, aby se takové platby lépe identifikovaly.
rychle. Chcete-li vytvořit platební metodu Check, postupujte podle těchto kroků:

#Přejděte na „Účetnictví“ -> „Konfigurace“ -> „Deníky“ a vyberte „Banka“.
časopis.
#V záložce „Příchozí platby“ klikněte na „Přidat řádek“.
#Jako způsob platby vyberte „Manuální“, pak zadejte „Šek“.
:guilabel:`Jméno“.

Při registraci platby zákazníka: ref>: <účetnictví/platby/z-faktury> nebo
:ref:`nejsou spojeny s fakturou <účetnictví/platby/nepárují se>“, použijte nový :guilabel:`Zkontrolovat“
Způsob platby.

.. poznámka::
Registrace platby zákazníka šekem v Odoo nepohybuje penězi. Šeky musí být uloženy na účet
účet, na který jste šek zaslali. Jakmile bude šek uložen ve vaší bance, měl by se objevit jako :doc:`bankovní
Transakce <bank/transakce>, kde se může :doc:`srovnat.
s platbou zaevidovanou v systému.

.. tip::
   - Pro nejlepší praxi zadejte číslo šeku jako :guilabel:`Poznámka k platbě`, když se registruje zákazník
platba šekem.
   - :doc:`Sběrné platby <platby/sberne-platebni-doklady>` mohou usnadnit vyrovnávání vkladů obsahujících více
kontrolách.

...účetnictví/platby/z faktury

Registrace platby z faktury nebo zálohové faktury
===========================================

Pro registraci platby za fakturu nebo účet následujte tyto kroky:

#Klikněte na položku „Zaplatit“ v faktuře zákazníka nebo dodavatele. V okně „Zaplatit“ vyberte
„Deník“ a „Datum platby“.
#Pokud je již nastavená, bude automaticky vybrán kontaktů preferovaný způsob platby.
výchozím nastavení, ale může být aktualizován v případě potřeby.
#Pokud používáte :doc:`platby podle obchodních podmínek <customer_invoices/payment_terms>`, částka
je automaticky nastaven na základě splátkových částek definovaných platebním kalendářem.
částku místo toho klikněte na „celou částku“.
#Pokud je třeba, upravte :guilabel:`Memo`.
#Klikněte na tlačítko „Vytvořit platbu“.

Po zaevidování platby je zákaznický faktura nebo dodavatelský doklad označen jako
:guilabel:`Ve splátkách“.

.. záložky::

.... skupina-tab: Bez nedoplatků

Pokud nejsou nakonfigurovány žádné nedoplatky, nebude se zobrazovat žádný
vytvoří se záznam do deníku. Chcete-li zobrazit další informace o platbě, klikněte na
:guilabel:`Platby“ chytrý tlačítko.

Pokud je faktura nebo dodavatelský list :doc:`srovnán <bank/reconciliation> s bankou
transakce je aktualizována na stav „Uhrazeno“.

.. poznámka::
         - Pokud je transakce v bance vyrovnána v jiné měně, provede se
automaticky vytvořený pro zveřejnění částky výnosů/ztrát z měnových kurzů.
         - Při souladu bankovního výpisu s fakturou na hotovost se v účetnictví provede
automaticky vytvořené pro účely přiznání k dani z příjmu fyzických osob na základě výdajů.

...... skupinový záhlaví: Používání nedoplatků

Výchozí nastavení plateb v Odoo neumožňuje vytvářet účetní záznamy, ale lze je snadno nakonfigurovat.
vytvářet záznamy pomocí odkazů na neuhrazené účty.
<účetnictví/banka/neuhrazené položky>.

Při registraci platby na faktuře odběratele nebo dodavatele vzniká nový účetní záznam.
snižuje částku dluhu podle výše platby.
odrážejí v :ref:`výjimečných <účetnictví/bankovníctvo/vyjimka-z-prijatych-dokladu> příjmech“ nebo
**účet platby**. V tomto bodě je označen faktura zákazníka nebo dodavatelská faktura.
:guilabel:`Ve splátce“. Poté se platba :doc:`vyrovnává <bank/reconciliation>“ s
v případě bankovního převodu, stav faktury nebo dodacího listu se změní na „Zaplaceno“.

Ikona informace vedle řádku platby zobrazuje více informací.
informace o platbě. K přístupu k další informaci, například ke spojenému deníku,
klikněte na tlačítko „Zobrazit“.

.. obrázek: platby/informace-ikonka.png
:alt:Podrobné informace o platbě.

.. poznámka::
         - Nedohodnutá platba odpojí fakturu nebo účetní doklad, ale nevymaže
platba.
         - Pokud je platba (ne)vyrovnána v jiné měně, automaticky se provede účetní zápis.
Vytvořený pro zaznamenání výnosů a ztrát z měnových kurzů (vrácení).
         - Pokud je platba (ne)vyrovnána na faktuře s paušální daní, vzniká
automaticky vytvořen k úhradě daňového přiznání na základě výnosů.

.. tip::
Pokud je jako účet zůstatku nastaven hlavní účet, bude na záznamu o platbě v deníku banky uveden
metoda, při které se celá platba zaeviduje na faktuře nebo zálohové faktuře přesune fakturu/zálohovou fakturu rovnou
bez nutnosti provádět bankovní vyrovnání na stav „Zaplaceno“.

..účetnictví/platby/nezávislé:

Registrace plateb, které nejsou spojeny s fakturou nebo účtem
===================================================

Při registraci nové platby v sekci „Zákazníci/Dodavatelé - Platby“ není
přímou součástí faktury nebo účtu.

.. záložky::

.... skupina-tab: Bez nedoplatků

Platby, které nejsou spojené s fakturou nebo účtem, by neměly být zaznamenány bez použití
:ref:`neuhrazené faktury <účetnictví/banka/neuhrazené-faktury>“, protože není možné
spojit platbu s fakturou nebo účtem, protože žádný záznam v knize nebude.
platba. V účetnictví se nezobrazuje částka zaplacená nebo přijatá,
:guilabel:`Dlužná částka“ se neaktualizuje na základě výše platby.

...... skupinový záhlaví: Používání nedoplatků

Ve skutečnosti je v účetním deníku záznamu o platbě odpovídá zůstatkovému účtu.
pohledávka nebo závazek, dokud nebude ručně spárována s platbou.
související faktura nebo účet. Poté se provede :doc:`srovnání plateb <bank/reconciliation>
bankovní transakce dokončuje platbu.

…účetnictví/úhrady/srovnání plateb:

Platby odpovídající
-----------------

.. poznámka::
Během procesu bankovního vyrovnání dochází k zjištění nevyčerpané částky.
pokud celkové zůstatky a pohyby neodpovídají, když jsou účetní záznamy porovnány s bankou.
transakcí. Tento zůstatek musí být buď později vyrovnán nebo ihned napsán do nuly.

...účetnictví/platby/srovnání faktur a zálohových faktur:

Pro jednu fakturu nebo účet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. záložky::

.... skupina-tab: Bez nedoplatků

Výchozí nastavení plateb v Odoo neumožňuje vytvářet účetní záznamy. V důsledku toho není možné provést platbu.
aby odpovídaly.

...... skupinový záhlaví: Používání nedoplatků

Při ověřování nové faktury se zobrazí modrá páska a **nedoplacená částka**
pro konkrétního zákazníka nebo dodavatele. Chcete-li jej spárovat s fakturou nebo účtem, klikněte
:guilabel:`Přidat“ pod :guilabel:`Nedoplatky“ nebo :guilabel:"Dluhy“.

.. obrázek: platby/add-option.png
:alt:Zobrazí možnost Přidat, která umožňuje spárovat fakturu nebo zálohovou fakturu s platbou.

Poté je faktura označena štítkem :guilabel:`Ve splatnosti`, dokud nebude uhrazena.
:doc:`vyrovnala se svým odpovídajícím bankovním transakcí
</bankovní transakce>.

...účetnictví/platby/automatické vyrovnání nástroj:

Pro více faktur nebo účtů
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. záložky::

.... skupina-tab: Bez nedoplatků

Výchozí nastavení plateb v Odoo neumožňuje vytvářet účetní záznamy. V důsledku toho není možné provést platbu.
to se shoduje, ale tato funkce lze stále použít k vyhledávání různých položek v novinách.

...... skupinový záhlaví: Používání nedoplatků

Nástroj „Platby shodné“ nebo „Automatické vyrovnání“ umožňuje automaticky spárovat platby.
záznamy mezi sebou (tj. platby s fakturami odběratele nebo dodavatele).
jednotlivě nebo ve skupinách. Přihlaste se do :guilabel:`Dashboardu účetnictví`, klikněte na
:ikonou „fa-ellipsis-v“ (guilabel: „Ellipsis“) tlačítko z guilabelu „Zákazník
Doklady o fakturaci nebo „Faktury dodavatelů“ a vyberte „Srovnání plateb“.
Alternativně přejděte na: „Účetnictví“ -> „Účetnictví“ -> „Srovnat“.

Chcete-li ručně vyřešit položky v deníku, vyberte jednotlivé položky z seznamu
zobrazit a kliknout na „Souhlasit“.

.._účetnictví/platby/automatické vyrovnání:

Funkce Auto-Reconcile
**********************

.. záložky::

.... skupina-tab: Bez nedoplatků

Chcete-li použít funkci „Automatické vyrovnání“, postupujte takto:

      #V seznamu položek k vyrovnání v zobrazení pohledu „Položky k vyrovnání“ klikněte na Auto-Reconcile.
vedle účtu pohledávky nebo závazku (nebo skupiny položek deníku pro konkrétní kontakt)
v tomto účtu).
      #V okně „Spojit automaticky“ klikněte na „Spojit“.

...... skupinový záhlaví: Používání nedoplatků

Chcete-li použít funkci „Automatické vyrovnání“, postupujte takto:

      #V seznamu položek k vyrovnání v zobrazení pohledu „Položky k vyrovnání“ klikněte na Auto-Reconcile.
vedle účtu pohledávky nebo závazku (nebo skupiny položek deníku pro konkrétní kontakt)
v tomto účtu).
      #V okně Reconcile Automatically nastavte
:guilabel:`Sjednotit“ pole podle toho, jak chcete spojovat záznamy v deníku:

         - :guilabel:„Dokonalá shoda“: Každý záznam z účetní knihy bude odpovídat
V případě, že se jedná o stejnou hodnotu, vytvořte odpovídající položku kreditního deníku.
         - :guilabel:Jasné účty: Všechny vyrovnané položky v deníku budou mít stejný
shodné číslo, protože jsou vybírány z jednoho účtu.

      #Klikněte na tlačítko „Sjednotit“.

Faktury a fakturační doklady se automaticky přiřadí k odpovídající platbě a označí jako
:guilabel:`Ve splátkách“ až do chvíle, než jsou :doc:`vyrovnány <bank/reconciliation>“.
odpovídající bankovní transakce (bank/transactions).

...účetnictví/platby/skupinové platby:

Registrace plateb na více fakturách, kreditních dokladech nebo účtech za vrácení peněz (skupinová platba)
========================================================================================

Pro registraci plateb na více fakturách nebo zálohových listinách či vrácení platby postupujte takto:

#Přejděte na: „Účetnictví“ - „Zákazníci“ - „Faktury / Dodací listy“.
:menu_selecce:`Účetnictví --> Přijaté faktury/vratky“.
#V seznamovém zobrazení klikněte do vyhledávacího pole, skupujte podle:guilabel:`Způsobu platby` a vyberte
relevantní faktury, kreditní doklady nebo účty a klikněte na „Zaplatit“.
#V okně „Zaplaceno“ vyberte „Deník“ a „Datum platby“.
#Pokud je již nastavená, bude automaticky vybrán kontaktů preferovaný způsob platby.
výchozím nastavení, ale může být aktualizován v případě potřeby.
#Pokud používáte :doc:`platby podle obchodních podmínek <customer_invoices/payment_terms>`, částka
je automaticky nastaven na základě splátkových částek definovaných platebním kalendářem.
částku místo toho klikněte na „celou částku“.
#Pro sloučení všech plateb od jednoho kontaktu do jedné platby zapněte:
Možnost platby nebo nechat pole prázdné pro vytvoření samostatné platby.
#Klikněte na tlačítko „Vytvořit platbu“.

.. záložky::

.... skupina-tab: Bez nedoplatků

Poté jsou faktury nebo účty označeny jako :guilabel:`Ve splatnosti“ a nebudou
:doc:`seznámil s bankovními transakcemi“ a „vyrovnal se s nimi“.

...... skupinový záhlaví: Používání nedoplatků

Poté jsou faktury nebo účty označené štítkem :guilabel:`Ve splatnosti`, dokud neproběhnou bankovní transakce.
jsou s platbami „srovnány“ (bank/reconciliation).

...účetnictví, platby, hromadné platby:

Registrace jednoho platebního příkazu pro více zákazníků nebo dodavatelů (souhrnná platba)
===============================================================================

Skládání plateb z více zákazníků do jedné platby usnadňuje :doc:`vyrovnávání
<bankovní vyrovnání>“. Jsou také užitečné při vkládání šeků:
<účetnictví/platby/šeky> nebo platba v hotovosti na účet u banky nebo pro generování souborů platebních příkazů.
jako SEPA <platební příkazy/platební sepa> nebo NACHA <l10n_us/nacha>.

.. viz též:
:doc:`platební příkazy/soubor“

...účetnictví, platby a shody:

Platby odpovídající
-----------------

Nástroj „Soulad plateb“ otevře všechny nevyřízené položky účetního deníku a umožní jejich zpracování.
Provedené individuálně a shodující se s platbami a položkami v účetnictví.
:guilabel:`Účetní přehled“, přejděte na „Účetnictví -> Účetnictví -> Srovnání“ nebo
Klikněte na tlačítko „:icon:`fa-ellipsis-v` (:guilabel:`ellipsis`)“ z nabídky „:guilabel:`Customer
Dodací listy nebo faktury dodavatele a vyberte „Zálohy shody“.

.. obrázek: platby/platby-deník.png
:alt:Platby odpovídající položkám v rozbalovacím seznamu.

.. poznámka::
Během procesu :doc:`srovnání <bank/reconciliation>` se může stát, že součet dluhů a kreditů bude
Pokud nejsou peníze vyčerpány, zůstává vám na účtu zůstatek. Ten můžete buď vyrovnat později nebo
vyřazeny ze zásob.

..účetnictví, platby, částečné platby:

Registrace částečné platby
=============================

Pro registraci částečné platby klikněte na tlačítko „Zaplatit“ v příslušném faktuře nebo účtu.

.. záložky::

.... skupina-tab: Bez nedoplatků

V případě částečné platby (kdy je zaplaceno méně než celkové
zůstatek na faktuře nebo účtu, vyplňte pole :guilabel:`Zůstatek`.
:guilabel:`Okno pro platbu“

...... skupinový záhlaví: Používání nedoplatků

V případě částečné platby (kdy je zaplaceno méně než celkové
zůstatek na faktuře nebo účtu (v poli „Rozdíl platby“).
Zobrazuje zůstatek na účtu. Existují dvě možnosti:

      - :guilabel:„Zanechat otevřené“: Nechte fakturu nebo účet otevřený a označte jej
:guilabel:`Částečný“ banner;
      - :guilabel:`Zaplatit úplně“: Vyberte účet v „Rozdíl poštovného“
pole a změnit :guilabel:`Štítek`, pokud je třeba. Bude vytvořen záznam, který vyrovná
buď účty k zaplacení nebo účty k vyplacení s vybraným účtem.

.. obrázek: platby/částečná_platba.png
:alt: registrovat částečnou platbu

...účetnictví/výplaty/vyrovnání výplat:

Soulad plateb s transakcemi v bance
===========================================

.. záložky::

.... skupina-tab: Bez nedoplatků

Jakmile je platba zaevidována, stav faktury nebo zálohové faktury je:guilabel:`Vyřízeno
platba. Dalším krokem je pak „srovnání účtů“ souvisejících s „bankou“.
transakce v řádku „Transakce“ s fakturou nebo účtem k dokončení platby
průběh a označit fakturu nebo účet za :guilabel:`Uhrazeno`.

...... skupinový záhlaví: Používání nedoplatků

Jakmile je platba zaevidována, stav faktury nebo zálohové faktury je:guilabel:`Vyřízeno
platba. Dalším krokem je pak „srovnání plateb“ (viz dokumentace v části bankovní transakce).
související s transakcemi bankovního účtu: doc:bank transactions <bank/transactions>
označit fakturu nebo účet jako zaplacenou pomocí značky :guilabel:`Zaplaceno`.

..toctree::


platby/on-line
platby/soubor
platby/soubor
platby/doplnění informací
platby/pay_sepa
platby
platby/prognóza
platby/důvěryhodné účty
