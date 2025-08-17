==============
Nedostatek objednávek
==============

.. |BoM| nahradit za: :abbr:`BoM (Seznam materiálů pro výrobu)“

V některých případech je nutné rozebrat vyrobené výrobky na jednotlivé komponenty.
Toto může být vyžadováno v případě, že bylo vyrobeno příliš mnoho kusů produktu nebo pokud jsou součásti jednoho produktu
musí být znovu použity při výrobě jiných produktů.

V Odoo Manufacturing lze produkty rozebrat a jejich komponenty vrátit do zásob.
pomocí příkazů „nebudovat“. Použitím příkazů „nebudovat“ lze tuto úlohu splnit.
hotový výrobek a jeho součásti zůstávají přesné podle množství rozebraných produktů.
a množství komponentů, které byly získány zpět.

Vytvořte nebudoucí pořádek
====================

Nový nevyrobený příkaz lze vytvořit kliknutím na: „Výrobní aplikace -> Operace
a klikněte na „Nový“.

Začněte vyplňovat nový nevybudovaný příkaz výběrem produktu, který chcete zrušit. Po provedení
takže pole „Seznam materiálů“ se automaticky vyplní odpovídajícím seznamem materiálů.
(BoM). Pokud má být použit jiný BoM, klikněte na pole „Seznam materiálů“ a
Vyberte si ho z roletky.

Alternativně lze zvolit konkrétní BoM v poli „Seznam materiálů“ před
vybráním produktu, který způsobí automatické vyplnění odpovídajícího produktu.
:guilabel:`Produkt“ pole.

Dále zadejte množství produktu, který se rozebírá.

Pokud byl výrobek původně vyroben v konkrétním výrobním příkazu (VŘ),
Vyberte ji v poli „Dodací objednávka“.

V poli „Zdroj“ vyberte místo, kde je produkt, který se chystá zlikvidovat.
aktuálně uložené.

V poli „Místo určení“ vyberte lokalitu, kde byly komponenty získány.
a jsou uloženy po dokončení nevybudovaného objednávky.

Pokud je v nastavení aplikace Inventář zapnutá funkce „Čísla sérií a čísla losů“,
:guilabel:`Číslo sériového štítku“ pole se zobrazuje na nevyrobené objednávce a může být použito k určení
číslo sériového nebo čísla losu výrobku (pokud je takové číslo přiděleno).

Pokud je databáze Odoo nakonfigurována pro více společností, pole „Společnost“
je na nevyhotoveném objednávkovém formuláři, který lze použít k určení společnosti vlastnící produkt.
nepostavené.

Konečně, po rozebrání produktu, klikněte na tlačítko „Odmontovat“ v horní části
aby bylo možné potvrdit, že byla dokončena.

.. obrázek: unbuild_orders/unbuild-order.png
:align:center
:alt:Vyplněný nevyužitý požadavek.

.. varování:
Při vytváření nevyřízených objednávek je možné vytvořit objednávky na produkty, které mají nulový nebo nižší počet jednotek
Pokud je zboží na skladě, není doporučeno jej převést na prodej, protože může vést k rozdílům v zásobách.

Pokud je vytvořen nevyplněný objednávkový lístek pro produkt s nulovým (nebo nižším) množstvím skladem, objeví se okno
je zobrazena varovná hláška, že není dostatek prostředků k demontáži.

Ignorovat varování a pokračovat v nevybudovaném příkazu kliknutím na tlačítko „Potvrdit“
na spodní části okna. Chcete-li se vrátit k nepotvrzenému nevybudovanému objednávkovému lístku, klikněte
:guilabel:`Smazat“, místo toho.

.... obrázek:unbuild_orders/insufficient-quantity.png
:synchronizace: střed
:alt:Pop-up s nedostatečným množstvím, který se objeví po pokusu o potvrzení nevybudované objednávky
pro produkt, který je skladem ve stavu nula nebo méně kusů.

Po dokončení nevyřízené objednávky se automaticky aktualizují zásoby na základě množství
nepostavených produktů a množství součástek získaných zpět.

Příklad:
Produkt „Koš na oblečení“ se skládá z jednoho komponentu „Dřevěný sloupek“ a šesti komponentů „Dřevěná tyčka“.
součástky.

Na jeden kus zboží Coat Rack se vytvoří nevyplněná objednávka. Jakmile bude objednávka dokončena,
K dispozici je o jednu méně „Stolek na kabáty“, zatímco „Dřevěné tyče“ jsou stále v zásobách.
a „Dřevěné kolíky“ se zvýší o jednu a šest.

Vyřaďte nefunkční součástky
=========================

V některých případech mohou být po dokončení procesu rozebírání součástky nefunkční.
Inventarizační soupisy přesně odrážejí množství použitelných součástek skladem, včetně komponent, které
nemůže být již použit, musí být vyřazen z evidence pomocí příkazu :doc:`scrap
<../../skladovani/sklady-a-uskladnani/správa-skladu/odpadový-sklad>.
