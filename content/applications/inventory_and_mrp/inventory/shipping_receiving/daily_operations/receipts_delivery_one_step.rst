=============================
Jednokrokové vyzvednutí a dodání
=============================

.. |PO| nahradit za: abbr: PO (příkaz k nákupu)
.. |SO| nahradit za: :abbr:`SO (objednávka na prodej)`
.. |RfQ| nahradit za: zkratku `RfQ (Request for Quotation)`

V Odoo *Skladu* jsou oba příchody i odeslání nakonfigurovány tak, že se zpracovávají v jednom kroku.
výchozí nastavení. To znamená, že nákupy budou přijímány přímo do skladu a dodávky se pohybují
Direkt od skladu k zákazníkovi.

.. tip::
Při příchozích a odchozích dodávkách není nutné nastavovat stejný počet kroků.

Například lze nastavit sklad tak, aby se produkty mohly přijímat přímo v jedné
krok a dodává se ve třech krocích (vybrat + zabalit + poslat).

Konfigurace
=============

Pro konfiguraci jednokrokových příjmových a výdejových dokladů pro sklad navštivte:
Aplikace --> Konfigurace --> Sklady“ a vyberte sklad, který chcete upravit.

V záložce „Konfigurace skladu“ nastavte „Příchozí zásilky“ na
„Přijmout zboží přímo (1 krok)“ a nastavte „Výstupní dodávky“.
:guilabel:`Dodat zboží přímo (1 krok).“

.. obrázek: faktury_doručení_v_jednom_kroku/faktury_doručení_v_jednom_kroku_skladové_nastavení.png
:align:center
:alt:Při příjmu a výdeji zboží na skladovou kartu nastavíte jedním tlačítkem.

.. poznámka::
Od doby, kdy je jednokrokové přijímání a dodávky výchozí pro příchozí i odchozí zásilky v Odoo,
*Vlastnost Multi-Step Routes* není potřeba.

Avšak abyste viděli nastavení „Dodávky“ na formuláři skladu, musíte mít zapnutou funkci
musí být zapnutá.

Pro možnost „Složené trasy“ přejděte do: Menu > Inventářová aplikace > Konfigurace
„Nastavení“. V sekci „Sklad“ zaškrtněte políčko vedle
:guilabel:`Složené trasy“ a klikněte na „Uložit“. Tím se aktivuje také
:guilabel:`Uložiště“ funkci.

...Inventura, faktury, dodání v jednom kroku.

Přijmout zboží přímo (1 krok)
===============================

Pokud jsou produkty přijímány v jednom kroku, budou se pohybovat z místa dodavatele do skladových zásob
do databáze okamžitě po schválení nákupního příkazu (nákupní objednávky).

Vytvořte objednávku k nákupu
---------------------

Vytvořit PO. Přejděte do nabídky „Nákupní aplikace“ a klikněte na „Nový“.
otevře prázdný formulář požadavku na cenovou nabídku (RfQ).

Přidejte dodavatele do pole „Dodavatel“ a pak vyplňte různá pole na formuláři |RfQ|.
nutné.

.. obrázek: faktury_doručení_v_jednom_kroku/faktury_doručení_v_jednom_kroku_nový_poptávkový_formulář.png
:align:center
:alt:Vyplnil nový poptávkový formulář.

Pod záložkou „Produkty“ klikněte na „Přidat produkt“ a vyberte produkt, který chcete přidat.
RfQ.

Jakmile bude připravena objednávka, klikněte na „Zadat objednávku“. Tím se objednávka přesune do stavu „Nákupní objednávka“
stáž.

Jakmile je potvrzena platba, se v horní části formuláře objeví tlačítko „Potvrzení o přijetí“.
Kliknutím na chytrý tlačítko se otevře formulář pro vydání skladového dokladu (WH/IN).

.. obrázek: faktury_doručení_v_jednom_kroku/faktury_doručení_v_jednom_kroku_faktura_tlačítko_chytré.png
:align:center
:alt:Tlačítko pro potvrzení objednávky na formuláři s potvrzenou objednávkou.

Příjem dokumentu
---------------

Za účelem přijetí zboží do skladu lze ze záznamu o vydání dokladu o převzetí zboží vyčíst produkty objednané zákazníkem.
produktu, klikněte na tlačítko „Zkontrolovat“. Jakmile je produkt ověřen, přesune se do složky „Dokončeno“
stáž.

.. obrázek: faktury_doručení_v_jednom_kroku/faktury_doručení_v_jednom_kroku_hotovo_prijemka.png
:align:center
:alt:Doklad o skladování v Done fázi, který byl ověřen.

Klikněte zpět na |PO| (přes chléb kroků nahoře formuláře) a zobrazte si formulář |PO|.
sérii produktů, množství v sloupci „Přijato“ odpovídá objednanému.
:guilabel:`Množství“.

.. inventarizaci, dodání a jednorázové:

Dodat zboží přímo (1 krok)
===============================

Pokud se zboží dodává v jednom kroku, pohybuje se ze skladových zásob přímo ke spotřebiteli.
umístění v databázi ihned po ověření prodejního příkazu (PO).

Vytvořit prodejní objednávku
------------------

Vytvořit SO lze tak, že se přesunete do aplikace „Prodej“ a klikněte na „Nový“.
otevře prázdný prodejní formulář.

Přidejte zákazníka do pole „Zákazník“ a pak vyplňte různé položky v sekci prodeje.
citace v případě potřeby.

.. obrázek: fakturace_doručení_v_jednom_kroku/fakturace-doruceni-v-jednom-kroku-novy-objednavky.png
:align:center
:alt:Vyplnil nový prodejní formulář.

Pod záložkou „Produkt“ klikněte na tlačítko „Přidat produkt“ a vyberte produkt, který chcete přidat.
nabídková cena prodejního příkazu.

Jakmile je připravena, klikněte na „Potvrdit“. To přesune citaci do „Objednávky prodeje“
stáž.

Jakmile je potvrzeno, objeví se nahoře na formuláři tlačítko „Doručení“, které má ikony pro různé způsoby doručení.
Kliknutím na chytrý tlačítko se otevře formulář pro expedici z skladu (WH/OUT).

.. obrázek: faktury_doručení_v_jednom_kroku/faktury-doruceni-v-jednom-kroku-tlacitko-doruceni.png
:align:center
:alt:Tlačítko pro odeslání objednávky potvrzené objednávky.

Dodání procesu
----------------

Z dodacího listu skladu lze odeslat zboží objednané zákazníkem.
skladu. Chcete-li dodat produkty, změňte hodnotu v poli „Množství“ na shodu s
počet objednaných kusů v poli „Požadavek“.

Jakmile je připraveno, klikněte na tlačítko „Zkontrolovat“. Jakmile bude kontrola dokončena, objednávka se přesune do
:guilabel:`Dokončeno“ fáze.

.. obrázek: faktury_doručení_v_jednom_kroku/faktury_doručení_v_jednom_kroku_hotovo_doručení.png
:align:center
:alt:Doručení potvrzené v Done fázi.

Klikněte zpět na SO (pomocí chlebových kousků nahoře na formuláři), abyste viděli formulář SO.
produktové řadě, množství v sloupci „Dodáno“ odpovídá objednanému.
:guilabel:`Množství“.

.. viz též:
:doc:`/denní operace“
