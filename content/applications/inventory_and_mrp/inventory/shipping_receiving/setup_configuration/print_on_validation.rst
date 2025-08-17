=======================
Doručitelné PDF soubory
=======================

Automaticky tisknout dodací PDF dokumenty a štítky v Odoo, které obsahují informace o příjemci balíku
podrobnosti, obsah nebo návod k použití.

Následující soubory PDF lze nakonfigurovat tak, aby se tiskly po ověření operace inventarizace (*Inventory*) (například
doklady o přijetí, vyskladnění a dodání (kontroly kvality):

#:ref:`Přepravní list <sklad/přijímání a výdej zboží/přepravní list>“
#:ref:`Vrácenka <inventura/přijímání a výdej/vracenka>`
#:ref:`Štítky produktů v objednávce <sklad/příjem a výdej/štítky produktů>“
#:ref:`Štítky s číslem a sériovým číslem <inventory/shipping_receiving/lot-sn-labels>“
#:ref:`Štítky přepravce <inventory/shipping_receiving/carrier-labels>`
#:ref:`Dokumenty k vývozu <Inventura/Přijímání a vydávání zboží/Exportní dokumenty>`
#:ref:`Obsah balení <Inventar/Versand und Wareneingang/Paketinhalt>“
#:ref:`Štítek balení <skladování a expedice/balení/štítek balení>`

... inventarizaci, přijímání a tisk:

Pro automatické tisknutí formulářů přejděte na: „Skladové aplikace --> Konfigurace“
Operační typy“ a vyberte požadovaný operační typ.

V záložce „Hardware“ zaškrtněte každou z požadovaných možností dostupných v záložce „Tisk“.
v sekci „Validace“ ke stažení PDF vybraných dokumentů automaticky po
ověření typu operace. Pro podrobnější informace o tom, co každá z možností zaškrtávacího políčka dělá, přeskočte
do příslušného oddílu.

.. obrázek:: tisk-při-validaci/tisk-pri-validaci.png
:align:center
:alt:Zobrazte možnost „Tisk při ověření“ v poli „Operace“.

... inventarizační list, faktura a dodací list:

Dodací lístek
=============

Dodací lístek obsahuje údaje o příjemci a balíčku, obvykle je uvnitř (nebo připojen k)
balení.

.. viz také:
   - :doc:`Štítek sledování <../setup_configuration/labels>`

Po zapnutí nastavení „Dodací lístek“ v sekci
Konfigurační možnosti v záložce „Hardware“ kliknutím na „Validovat“ u požadované
Operační typ stáhne PDF faktury o dodání.

Dodací lístek uvádí produkty, množství a číslo objednávky.
pořadí hmotnosti.

.. obrázek: tisk_kontroly/dodací lístek.png
:align:center
:alt: Příklad dodacího listu.

... inventarizační záznam, faktura, dodací list, vrácený doklad.

Potvrzení o vrácení
===========

Vytiskněte si formulář „vrácení zboží“ a přiložte jej k balíku, který zákazník vrací. Tento formulář obsahuje
obsahuje informace o položce a zákazníkovi. Může také
zahrnout konkrétní pokyny pro vrácení zboží zákazníkovi.

Po zapnutí volby „Výdejní lístek“ v nastavení tisku (viz.
Konfigurační možnosti v záložce „Hardware“ kliknutím na „Validovat“ u požadované
Typ operace stáhne PDF daňového dokladu.

Vrácenku je nutné vyplnit a na ní uvést adresu vrácení společnosti, dále pak čárové kódy objednávky a
návratová operace.

.. obrázek:: tisk_na_validaci/vratka.png
:align:center
:alt: Příklad vrácenky.

...Inventarizaci, přijímání a odesílání zboží, štítky na výrobcích:

Etikety výrobků
==============

Tisknout štítky produktů a připevnit je k položkám objednávky, poskytnutím důležitých informací, jako jsou
název produktu, čárový kód a cena.

Po zvolení požadovaného typu operace (:menuselection:`Skladová aplikace --> Konfigurace -->
Typy operací“), v záložce „Hardware“ zaškrtněte možnost „Štítky produktu“.

Tím se zobrazí rozevírací nabídka „Vytisknout štítek s:“, kde je možné vybrat každý produktový štítek.
bude vytištěna jako:

- :guilabel:„2x7 s cenou“: PDF zobrazuje název produktu, čárový kód a cenu, přičemž dvě řádky
sedm sloupců etiket na stránce.

...... spoiler:: Příklad 2x7

... obrázek:: tisk_při_validaci/dva-sedm.png
:align:center
:alt: Příklad 2x7 s cenou.

- :guilabel:'4x7 s cenou': zobrazuje název produktu, čárový kód a cenu, přičemž se vejde do čtyř řádků.
sedm sloupců etiket na stránce.

..... spoiler::Příklad 4x7

.... obrázek:: print_on_validation/four-seven.png
:align:center
:alt: Příklad 4x7 s cenou.

- :guilabel:`4 x 12“: zobrazuje název produktu a čárový kód. Vhodné pro čtyři řádky a dvanáct sloupců
etiket na stránku.

...... spoiler:: Příklad 4x12

.... obrázek: tisk_při_validaci/čtyři-dvanáct.png
:align:center
:alt: Příklad 4 x 12.

- :guilabel:`4 x 12 s cenou“: zobrazuje název produktu, čárový kód a cenu. Vhodné pro čtyři řádky
dvanáct sloupců etiket na stránce.
- :guilabel:„Štítky ZPL“: tiskne štítky v programovacím jazyce Zebra (ZPL), které obsahují
názvu produktu a čárového kódu. Čitelné pro tiskárny Zebra, které automaticky vytvářejí štítky.
- :guilabel:`Etikety s cenou ZPL Labels“: tisk etiket v jazyce ZPL
obsahující název produktu, čárový kód a cenu.

.. poznámka::
Etikety výrobků lze ručně tisknout z jakéhokoliv dodacího příkazu kliknutím na :guilabel:`Tisk etiket.
Tlačítko „Štítky“.

... inventarizaci, přijímání a expedici zboží, štítky pro loty SN:

Lot/SN štítky
=============

Vytiskněte štítky s číslem objednávky a číslem zásilky, které připevníte k položkám v objednávce. Tyto štítky poskytnou důležité informace, například
název produktu, sériové číslo nebo číslo šarže a čárový kód.

Pro automatické tisky PDF se přihlaste na stránku s nastavením typu operace.
(:menu_selection:"Inventarní aplikace --> Konfigurace --> Typy operací"). Pak v
Karta „Hardware“, zaškrtněte možnost „Štítky lotu / sériového čísla“.

Tím se zobrazí rozevírací nabídka „Vytisknout štítek s:“, kde je možné vybrat každý produktový štítek.
bude vytištěna jako:

- :guilabel:`4 x 12 - Jedna na balení/Sériové číslo v objednávce`: PDF s etiketami pro jedinečné sériové číslo v objednávce
včetně názvu produktu, čísla šarže a čárového kódu. Vhodné pro čtyři řádky a dvanáct sloupců
stránka.

...... spoiler:: Příklad 4x12 - Jedna na lístek/SN

...... obrázek:: tisk_při_validaci/čtyřicet dvanáct lotů.png
:align:center
:alt:Objednávka s jediným unikátním souborem číselného označení.

Štítky pro objednávku s jediným unikátním souborem čísla šarže a čísla výrobního čísla.

- :guilabel:`4 x 12 - Jedna na jednotku`: PDF s etiketami odpovídajícími počtu položek, zobrazující
název produktu, číslo šarže a čárový kód. Vhodné pro čtyři řádky a dvanáct sloupců na stránce.
- :guilabel:`Etikety ZPL - Jedna na šarži/SN“: tiskne etikety v :abbr:`ZPL (Programování
„Jazyk“, která obsahuje název produktu, číslo šarže a čárový kód.
- :guilabel:`ZPL Labels - One per unit“: tiskne štítky s počtem kusů v :abbr:`ZPL
(Programovací jazyk Zebra), který obsahuje název produktu, číslo sady a štítek.

...Inventarizace, přijímání a odesílání zásilek, štítky dopravce:

Přepravní štítky
==============

Automaticky tisknout štítek přepravce s adresou příjemce, číslem zásilky a dopravcem.
pro konkrétní třetí strany poskytující dopravu, dokončete následující nastavení:

#Zatrhněte políčko „Dodavatelské štítky“ v nastavení typu operace.
<Inventura/Přijímání a výdej/Tisková konfigurace>.
#Připojte tiskárnu k aplikaci *IoT*.
#:ref:`Přidělit štítek přepravci na tiskárnu <Inventář/Odeslání a příjem/přidělit-tiskárnu>“.
#. Konfigurujte typ štítku pro způsob dopravy:ref:`<inventory/shipping_receiving/label-type>`.

... _Inventarizace, přijímání a přiřazování tiskáren:

Přiřadit tiskárnu
--------------

Podívejte se na dokumentaci „Připojení tiskárny“ v části „IoT zařízení“ v
podrobnosti o připojení tiskárny k aplikaci Odoo IoT. Po dokončení přiřaďte dopravní štítek
tiskárna, když se přesunula na:menu:IoT aplikace - zařízení a vybrala požadované.
tiskárna.

.. obrázek:: tisk_při_validaci/vyber-tiskárnu.png
:align:center
:alt:Zobrazit seznam zařízení Internetu věcí.

V konfiguračním formuláři pro tiskárnu přejděte na záložku „Zprávy o tisku“ a nastavte typ
dokumentů, které tiskárna automaticky vytiskne. Klikněte na „Přidat řádek“ pro otevření
Popisku „Přidat: Zprávy“ v okně „Přidat“. Do pole „Hledání...“ zadejte Shipping a
Vyberte položku „Dopravní štítky“.

.. poznámka::
Zpráva „Dokumenty o přepravě“ je určena pro :ref:`doklady k vývozu
<Inventura/Přijaté a vydané zboží/Exportní dokument>.

.. obrázek: tisk_kontroly/tisk-zpravy.png
:align:center
:alt:Zprávu o štítku přepravce přidáno do sekce „Zprávy tiskárny“.

Po přidání zprávy „Štítky“ v záložce „Tiskárny“ se ujistěte, že
Vlastnost reportType odpovídá typu tiskárny připojené k internetu věcí.

- Pro laserové tiskárny nastavte „Typ zprávy“ na „PDF“.
- Pro tiskárny Zebra nastavte typ zprávy na „Text“.

… inventarizaci, přijímání a expedici zboží/etiketu:

Štítek dopravce
---------------------------

Následně dokončete nastavení pro třetí stranu.
„<../setup_configuration/third_party_shipper>“. Poté přejděte do sekce „Skladové aplikace“ ->
Konfigurace --> Způsoby doručení“ a vyberte požadovaný způsob dopravy.

V konfiguračním formuláři pro způsob dopravy v záložce „Konfigurace [název přepravce]“
zajistit, aby formát štítku odpovídal typu zprávy, který byl dříve přiřazen
<Inventura/Přijaté a vydané zboží/Přiřazení tiskárny>:

- Pro laserové tiskárny nastavte formát štítku na PDF.
- Pro tiskárny Zebra nastavte formát štítku na „ZPL2“.

.. obrázek: tisk_na_ověření/typ-etikety.png
:align:center
:alt:Zobrazte pole „Typ štítku“ na stránce konfigurace způsobu doručení společnosti FedEx.

Příklad přepravní etikety
---------------------

Po ověření operace je vygenerován dopravce na chatu a tisknout.
IoT tiskárna.

..spoiler::Příklad dopravce

.. obrázek:: tisk_na_validaci/fedex-carrier-label.png
:align:center
:alt:Zobrazte příklad štítku přepravce pro společnost FedEx.

Přepravní štítek pro FedEx s adresou příjemce, číslem zásilky, čárovým kódem a
další dodací informace.

.. viz také:
:doc:`Tisk štítků přepravce <../setup_configuration/labels>`

… inventarizaci, přijímání a expedici zboží:

Exportní dokument
===============

Povinný vývozní doklad, který je nutný pro zaslání balíčku z jednoho státu do druhého, může být
automaticky vytištěno v Odoo podle těchto kroků:

#Zatrhněte políčko „Exportovat dokumenty“ v nastavení typu operace.
<Inventura/Přijímání a výdej/Tisková konfigurace>.
#Připojte tiskárnu k aplikaci *IoT*.
#Přidělte vývozní dokument tiskárně.

Přiřadit tiskárnu
--------------

Podobně jako pokyny pro přiřazení tiskárny k štítku přepravce
<Inventář/Přijetí/Zadání tiskárny>, po připojení kompatibilní tiskárny k Odoo
Aplikaci pro internet věcí (IoT), přejděte na: „Aplikace pro internet věcí –> Zařízení“ a vyberte požadovaný tiskárnu.

V konfiguračním formuláři tiskárny přejděte na záložku „Zprávy o tisku“ a klikněte
„Přidat řádek“. V okně „Přidat: Zprávy“, které se objeví, přidejte
:guilabel:`Dokumenty o přepravě“ zpráva, která přiřadí exportní dokument tiskárně.

.. spoiler::Příklad vývozního dokumentu

.... obrázek: print_on_validation/export-doc.png
:srovnání: do středu
:alt:Exportní dokument pro zásilku ze Spojených států do Belgie.

Exportní dokument pro zásilku z USA do Belgie.

... skladování, přijímání a balení zásilek:

Obsah balení
===============

PDF soubor obsahující informace o balení zahrnuje kód čárového kódu, datum zabalení a seznam obsahu.
produkty a množství.

Pro automatické tisknutí této formuláře přejděte na:
Typy operací“ a vyberte požadovaný typ operace. Poté přejděte na kartu „Hardware“
a zaškrtněte políčko „Obsah balení“.

.. důležité::
Pokud tato možnost není k dispozici, zapněte :doc:`balíčky
funkci „Konfigurace balíčku“ (viz adresa URL: `product_management/configure/package`), přejděte na:
--> Konfigurace --> Nastavení“, zaškrtnout políčko „Pakety“ a kliknout
:guilabel:`Uložit“.

Po zapnutí funkce v záložce „Hardware“ se ověření operace zobrazí ve formátu
Obsah balíčku.

..spoiler::Příklad obsahu balení ve formátu PDF

...... obrázek:: tisk_při_validacích/obsah_balení.png
:srovnání: do středu
:alt:Zobrazuje obsah balení a čárový kód s datem výroby.

Obsah balení s obsahem balení, čárovým kódem a datem balení.

.. inventář/přijetí/balení:

Etiketa balení
=============

Připravený štítek s uvedeným čárovým kódem a datem balení lze vytisknout.
kliknutím na tlačítko „Uložit do balíku“.

.. důležité::
Tlačítko „Vložit do balíku“ je k dispozici pouze v případě, že je aktivní možnost „Přidat balík“.
<../../product_management/configure/feature> funkce je zapnutá.
:menu: „Aplikace inventáře --> Konfigurace --> Nastavení“.

Po zapnutí je tlačítko „Uložit do balíku“ dostupné na všech operacích s inventářem.
(např. faktura, výdejky, vnitrofiremní převody, dodací listy apod.)

Pro automatické tisknutí štítku balení při kliknutí na tlačítko „Uložit do balení“ přejděte na
Vyberte aplikaci „Správa zásob“ > Konfigurace > Typy operací. Vyberte požadovanou operaci
Typ a zaškrtněte políčko „Značka“ v záložce „Hardware“. Značky mohou být
Tisknuté v souborovém formátu PDF nebo ZPL, jak je definováno v tiskové štítku
na hřišti.

.. spoiler::Příklad štítku balení

.... obrázek: tisk-na-validaci/balení-čárový-kód.png
:srovnání: do středu
:alt:PDF s čárovým kódem balení a datem balení.

