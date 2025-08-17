================================
Slevy a daňové úlevy
================================

Slevy na hotovost jsou snížení částky, kterou zákazník musí zaplatit za zboží nebo služby nabízené jako
a motivací k rychlému zaplacení jejich faktury. Tyto slevy jsou obvykle procentem z
celkové částce faktury a jsou uplatňovány, pokud zákazník zaplatí do určitého časového limitu. Sleva za platbu v hotovosti
Může pomoci společnosti udržet stabilní tok peněz.

.. příklad::
Vy vystavíte fakturu za 100 eur 1. ledna. Celá částka je splatná do 30 dnů a vy
Vám také nabídnou slevu ve výši 2 % pokud zaplatíte do sedmi dnů.

Zákazník může zaplatit až do 8. ledna částku 98 eur. Po tomto datu by musel uhradit 100 eur.
do konce ledna.

Snížení daně může být také aplikováno v závislosti na zemi.
nebo regionu.

.. viz též:
   - :doc:`platební podmínky“
   - :doc:`../platební_karty`

..._slevy za platbu v hotovosti/konfigurace:

Konfigurace
=============

Předtím, než zákazníkům poskytnete slevu v hotovosti, musíte nejprve ověřit ziskové a ztrátové účty.
<slevy na hotovost a účetnictví zisků a ztrát>. Pak nakonfigurujte:
<slevy za platbu předem/splatnost faktur> a přidejte slevu za platbu předem označením „Sleva při rychlém zaplacení“.
zaškrtávací políčko a vyplnění slevy v procentech, dnů slevy a daně.
snížení cen (slevy v hotovosti, snížené daně).

… _kasovým slevám a účetnictví zisků a ztrát:

Účty zisků a ztrát z hotovostních slev
--------------------------------

Slevou na hotovost získáte peníze podle toho, jestli zákazník využívá slevu na hotovost
slevu nebo ne. To vždy vede k zisku a ztrátě, která je evidována na účtech výchozích hodnot.

Pro úpravu těchto účtů přejděte na: „Účetnictví – Konfigurace – Nastavení“ a v
sekci „Výchozí účty“, vyberte účty, které chcete používat pro
:guilabel:'Příjem z cashbacku' a :guilabel:'Ztráta z cashbacku'.

.._sleva za platbu v hotovosti / splatnost faktur:

Platební podmínky
-------------

Slevy za platbu v hotovosti jsou definované na :doc:`podmínkách plateb <payment_terms>“. Konfigurujte je dle svého uvážení
Přejděte na „Účetnictví“ -> „Nastavení“ -> „Platební podmínky“ a ujistěte se, že je vyplněno
sleva v procentech, počet dní slevy a :ref:`daňová sleva <slevy-na-hotovost/>`
pole.

.. obrázek: cash_discounts/platebni-podminky.png
:alt: Konfigurace platebních podmínek s názvem „2/7 NET 30“. V poli „Popis na faktuře“
„Platební podmínky: 30 dní, slevy za předčasné splacení ve výši 2 % do 7 dnů“.

.. slevy a daňové úlevy:

Daňové slevy
--------------

V závislosti na zemi nebo oblasti se může lišit základní částka používaná k výpočtu daně, což může vést
na snížení daně. Daňové slevy jsou totiž stanoveny na individuálních podmínkách, takže každý z nich může využít
specifická daňová úleva.

Konfigurace způsobu snížení daně se provádí v platebním termínu s :guilabel:`Dřívější
Zatrhněte políčko „Sleva“ a vyberte jednu z následujících možností:

- Vždy (na faktuře)
Daň se vždy snižuje. Základní částka používaná k výpočtu daně je snížená částka.
zda zákazník zlevněné zboží využívá či nikoliv.

- Na předčasné splacení
Daň se sníží jen v případě, že zákazník zaplatí dříve. Základ pro výpočet daně je částka
Stejně jako u slevy: pokud zákazník využívá slevu, pak se daň snižuje. To znamená
Aby se mohla lišit výše daně, záleží na zákazníkovi.

- Nikdy
Daň se nikdy nezmenšuje. Základní částka používaná k výpočtu daně je plná částka, ať už jde o celou
zákazník získá slevu nebo ne.

.. příklad::

Vy vystavíte fakturu za 100 eur (bez DPH), s daní 21 % k 1. lednu.
splatnost je do 30 dnů a nabízíte i slevu ve výši 2 % pokud zákazník zaplatí včas.
sedm dní.

... záložky ::

.. tab:: Vždy (na faktuře)

... seznamová tabulka::
:hlavičkové řádky: 1

            * -Termín splatnosti
              - Celková částka splatná
              - Počítání
            * – 8. ledna
              - €118.58
              - €98 + (21 % z € 98)
            * – 31. ledna
              - €120.58
              - 100 EUR + (21 % z 98 EUR)

... tab: Předčasné splacení

... seznamová tabulka::
:hlavičkové řádky: 1

            * -Termín splatnosti
              - Celková částka splatná
              - Počítání
            * – 8. ledna
              - €118.58
              - €98 + (21 % z € 98)
            * – 31. ledna
              - €121.00
              - €100 + (21 % z € 100)

.. tab:: Nikdy

... seznamová tabulka::
:hlavičkové řádky: 1

            * -Termín splatnosti
              - Celková částka splatná
              - Počítání
            * – 8. ledna
              - €119.00
              - €98 + (21 % z € 100)
            * – 31. ledna
              - €121.00
              - €100 + (21 % z € 100)

.. poznámka::
   - :ref:`Daňové sazebníky <daňová přiznání/sazebníky daňových sazeb>“, které se používají pro daňový přehled, jsou správně
vypočítané podle typu slevy na dani, viz :ref:`slevy na dani <cash-discounts/tax-reductions>`.
konfigurována.
   - Výši slevy na spotřební dani lze správně přednastavit podle vašeho
:ref:`daňová lokalizační balíček <fiscal_localizations/packages>“.

.._sleva za platbu v hotovosti/faktura pro zákazníka:

Připočíst hotovostní slevu k faktuře zákazníka
===========================================

Na faktuře zákazníka aplikujte slevu za platbu zvolením platebních podmínek, které jste vytvořili.
<slevy za hotové platby/splatnost faktur>. Odoo automaticky vypočítá správné částky, daňové částky a splatnosti.
datum a účetní záznamy.

Pod záložkou „Články v časopise“ můžete zobrazit podrobnosti o slevě kliknutím na
„přepínač“ tlačítko a přidat sloupec :guilabel:Sleva Datum a :guilabel:Sleva Množství.

.. obrázek: cash_discounts/faktura-doklad.png
:alt:Faktura v hodnotě 100 EUR s výběrem platebních podmínek „2/7 Netto 30“. V záložce „Položky účetnictví“
je otevřený a v poli „Sleva“ a „Slevová částka“ se zobrazují informace.

Sleva i splatnost je také zobrazena na vystaveném faktuře, který byl zaslán na
zákazníkovi, pokud je zaškrtnuto pole „Zobrazit splátkové termíny“.

.. obrázek: cash_discounts/faktura-tisk.png
:alt:Faktura v hodnotě 100 eur s následujícím dodatkem k obchodním podmínkám: „30
Dny, slevy za předčasné splacení ve výši 2 % do 7 dnů. V případě zaplacení do 01/08/2023 je splatná částka 118,58 EUR."

Srovnání plateb
----------------------

Při zadávání platby nebo při vyrovnávání bankovních transakcí
<../bank/rekonciliace>“, při určování, zda je zákazníkova platba v pořádku, bere v úvahu datum přijetí platby.
Zákazník může využít slevu z kupní ceny nebo ne.

.. poznámka::
Pokud zákazník zaplatí částku slevy až po datu slevy, můžete vždy rozhodnout se pro
fakturu označit za úplně zaplacenou s odpisem nebo částečně zaplacenou.
