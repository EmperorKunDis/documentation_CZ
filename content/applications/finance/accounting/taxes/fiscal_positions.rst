==========================================
Fiskální pozice (daňová a účetní mapování)
==========================================

Výchozí daně a účty jsou nastaveny na produktech a zákaznících, aby se vytvářely nové transakce přímo na místě.
V závislosti na lokalizaci zákazníků a poskytovatelů služeb a typu podnikání však mohou být použity
Mohou být zapotřebí daně a účetní záznamy.

„Fiskální pozice“ umožňují vytvářet pravidla pro přizpůsobení daní a účtů používaných pro
transakce automaticky.

Mohou být aplikovány automaticky (viz fiskální pozice/automatické) nebo ručně (viz fiskální pozice/ruční).
<fiscal_positions/manual>“, nebo „přiděleno partnerovi <fiscal_positions/partner>.

.. poznámka::
Řada výchozích daňových pozic je k dispozici jako součást vaší :ref:`daňové lokalizace
balíček <fiscal_localizations/packages>.

Konfigurace
=============

.. fiskální pozice / mapování:

Daňová a účetní mapování
-----------------------

Pro úpravu nebo vytvoření fiskálního postavení přejděte na: „Účetnictví --> Konfigurace --> Fiskální
Položky“ a otevřít záznam pro úpravu nebo kliknout na „Nové“.

Mapování daní a účtů je založeno na výchozích daních a účtech definovaných v
produktová forma.

- Pro přiřazení k jinému dani nebo účtu vyplňte sloupec vpravo (:guilabel:`Danu, na kterou se vztahuje`/
:guilabel:`Účet, který se má použít místo tohoto“.

.. obrázek: fiscal_positions/fiscal-positions-tax-mapping.png
:align:center
:alt:Příklad mapování daně z příjmu

.. obrázek: fiskální pozice/fiskální pozice - účetní mapování.png
:align:center
:alt: Příklad mapování účtu fiskální pozice

- Chcete-li odstranit daň, nechte pole „Daň“ prázdné.
- Nahradit jednu daň několika dalšími daněmi, přidat více řádků s tím samým štítkem „Daň z
Produkt“.

.. poznámka::
Mapování funguje pouze s aktivními daněmi. Ujistěte se tedy, že jsou aktivní kliknutím na
:menu_selection:`Účetnictví --> Konfigurace --> Daňové sazby`.

Přihláška
===========

.. _daňové pozice/automatické:

Automatické podání
---------------------

Pro automatické aplikaci fiskálního postavení podle sady podmínek přejděte na
:menu-vyber->Účetnictví-->Konfigurace-->Daňové pozice“, otevřete daňovou polohu
upravit a zaškrtnout „Detekovat automaticky“.

Zde se mohou aktivovat různé podmínky:

- :guilabel:`Požadováno DPH“: zákazník musí mít na svém kontaktním formuláři číslo DPH.
- :guilabel:`Země“ a „Stát“: fiskální pozice se vztahuje pouze na
zvolené zemi nebo skupině zemí.

.. obrázek: fiscal_positions/fiscal-positions-automatic.png
:align:center
:alt: Příklad automatického nastavení fiskálního postavení

.. poznámka::
   - Pokud je zapnutá funkce „Kontrola DIČ“ (<vat_verification>), kontroluje se každý fiskální úřad.
s aktivním :guilabel:`požaduje DPH“ bude vyžadovat platné číslo DPH v rámci EU.
automaticky.
   - Daň z e-commerce objednávek se automaticky aktualizuje, jakmile zákazník přihlásí nebo
vyplnily své údaje o fakturaci.

.. důležité::
Pořadí fiskálních pozic určuje, která fiskální poloha se použije v případě splnění všech podmínek.
současně naplňují více fiskálních pozic.

Příklad: např. první pozice v sekvenci cílí na zemi A, zatímco druhá
fiskální pozice cílí na skupinu zemí, která zahrnuje zemi A. V tom případě je třeba pouze
První daňová pozice bude aplikována na zákazníky ze země A.

.. _fiskální pozice/manuál:

Manuální aplikace
------------------

Chcete-li ručně vybrat daňovou pozici, otevřete objednávku, fakturu nebo zálohovou fakturu.
Kartě „Další informace“ a vyberte požadovanou položku „Daňová pozice“ před přidáním produktu.
řádky.

.. obrázek:: fiskální pozice/fiskální pozice - manuál.png
:align:center
:alt:Vybrat daňovou položku na objednávce, faktuře nebo zálohové faktuře

... fiskální pozice partnera:

Přidělit partnerovi
-------------------

Pro definování daňového postavení, které se má používat pro konkrétního partnera, přejděte na
V nabídce „Účetnictví -> Zákazníci -> Zákazníci“ vyberte partnera a otevřete
Kartu „Prodej a nákup“ a vyberte položku „Daňová pozice“.

.. obrázek: fiscal_positions/fiscal-positions-customer.png
:align:center
:alt:Výběr fiskální pozice na zákazníka

.. viz též:

  * :doc:`../dane`
  * :doc:`B2B_B2C“
