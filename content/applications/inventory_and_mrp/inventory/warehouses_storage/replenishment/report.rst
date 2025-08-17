====================
Zpráva o doplnění
====================

.. |SO| nahradit za: :abbr:`SO (Prodejní objednávka)`
.. |SOs| nahradit za: zkratka: `SOs (Sales Orders)`

*Zpráva o doplňování zásob* je interaktivní panel, který používá :doc:`pravidla ručního doplňování
<prioritní pravidla>, dodací lhůty a přicházející poptávku k předpovědi množství produktů, které budou potřeba
dodatečné zásobení.

Pravidla přehazování používaná na této liště jsou obvyklá pravidla přehazování, ale uživatel z nich má
monitorování nabídky s dalšími možnostmi pro správu doporučení na doplnění zásob.

Uživatelům umožňuje předvídat budoucí potřeby a udržovat méně produktů skladem bez rizika
vyprodává se, plánujeme a konsolidujeme objednávky.

Procházejte zprávu o doplňování zásob
=================================

Pro přístup k zprávě o doplňování zásob se přihlaste na: „Skladové aplikace -> Provoz ->
Dodávka.

.. poznámka::
Automatické pravidlo pro přeřazení je dostupné i na tomto menu, ale výchozí nastavení je skryté.

Políčka a funkce, které jsou jedinečné pro obrazovku doplňování zásob, jsou uvedeny níže.
z dalších polí, přejděte do sekce Vytvořit pravidla pro přeskupování.
<výroba/sklady a skladování/polní obilí>.

Výchozí množství v poli „Požadované“ je množství potřebné k dosažení stanoveného
„Maximální množství“. Nicméně množství „Na objednávku“ lze upravit kliknutím na
pole a změnit hodnotu. Ručně doplnit produkt kliknutím na ikonku
:label:Objednávka

Klikněte na ikonu „fa-bell-slash“ a poté na tlačítko „Snooze“, abyste dočasně vypnuli pravidlo přeskupování.
doba nastavená v rámci skrytí záznamu z doplnění na přehledové ploše, kdy má být vidět.

..tip:
Definice :guilabel:`Výrobce` umožňuje filtrovat nebo seskupit poptávky podle výrobce. To usnadňuje
Proces identifikace produktů k objednání a snížení nákladů na dopravu.
:ikona:"nastavení" (upravit nastavení)" ikona a vyberte "Dodavatel".
vybrat si ze seznamu a zobrazit pole v hlášení.

.. obrázek:report/doplněk-přehledy.png
:alt:Zpráva o doplňování, která zobrazuje doporučené množství k objednání.

Objednávka na maximum
------------

Pokud pravidlo pro přeobjednávání neočekává příchod produktu pod minimální hodnotou, dojde k
nemůže být spuštěn, protože je považován za „nepotřebný“. V některých případech však může dojít k situacím, kdy
Zboží je nutné doplnit i v případě, že není považováno za „nutné“, například když je potřeba objednat
aby se dosáhlo lepších slev nebo úspory na dopravě.

Nejprve vyberte jeden nebo více produktů zaškrtnutím příslušného políčka. Poté klikněte na
Tlačítko „Dodat“ a vyberte možnost „Objednat na maximum“. Tím vytvoříte požadavek.
citace (RFQ) pro první možnou dobu zásobování každého produktu na maximální specifikovanou
v pravidle přeřazování.

.. obrázek::report/order-to-max.png
:alt:Možnost „Max“ na přehledu zásob v objednávce.

.. skladové zásoby, sklady a doba uložení:

Horizon Days
------------

Dny horizontu určují, kolik dní dopředu Odoo kontroluje předpokládané množství a zda klesne pod
pravidlo pro minimální počet položek v objednávce. Tato funkce má pomoci uživatelům při plánování doplňování zásob s předstihem,
Zvýšení předpokládaného data na
:doc:`dokumentace o doplňování zásob <report>“.

Příklad:
Nastavení počtu dní na obzoru na hodnotu 7 zajistí, že se všechny ručně nastavené pravidla pro přeřazení spustí v následujících
7 dní se zobrazují na výkazu doplňování, což umožňuje uživatelům přezkoumat a rozhodnout se o produktech
je nutné si objednat předem.

Pro nastavení dnů zásobování přejděte na: „Inventář aplikace -> Provoz - > Dodávky“.
Klikněte na ikonu „fa-angle-double-right“ v levém sloupci vedle ikony „fa-folder“.
Zobrazí se nabídka, nastavte počet dní „Horizon“.

Horizontální dny i :ref:`dny viditelnosti <inventory/warehouses_storage/visibility-days>
Odoo předvídá budoucí poptávku, ale fungují jinak:

- Dny viditelnosti: pouze kontrolují budoucí poptávku, pokud by dnes došlo k obnovení zásob.
- **Dny horizontu**: zobrazuje předpověď počasí na určitý počet dní a spouští pravidla pro přeskupování, jakmile
předpokládané množství klesne pod minimální hodnotu v tomto okně – i když nebude doplňováno
Je nezbytná dnes.

Příklad:
   - Aktuální datum: 18. února
   - Na skladě je k dispozici 10 kusů.
   - Pravidlo přeskupení: Min: 5, Max: 10
   - Doba dodání od dodavatele: 1 den

Pro dosažení |SO| na 23. února je potřeba 8 jednotek. To znamená, že v den 23. února bude k dispozici pouze 2 jednotky
zásoby.

**Bezhorizontní dny**

   - Poptávka se objevuje na dodacím listu až 22. února, tedy den před dodáním
datum.
   - Datum předpokládaného doručení: 19. února (současné datum + doba dodání dodavatelem)

**S dny s obzorem (4 nebo více dní)**

   - Odoo považuje poptávku do 23. února za aktuální dnes (18. února).
   - Potřeba dalších osmi kusů se objevuje ihned v zásobovacím hlášení
   - Datum předpokládaného příchodu: 23. února (aktuální datum + doba potřebná k dodání + počet dní, které ještě zbývají do konce zásob).

.... obrázek::report/horizon-days.png
:alt:Zobrazit předpověď s posunutým datem.

Informace o doplnění
=========================

V každé řádce zásobovací zprávy klikněte na ikonu „info“
Ikona otevře okno „Informace o doplňování zásob“, které zobrazí *dodací lhůty*.
a předpokládaný termín.

Pro podrobné informace o tom, jak tuto funkci používat pro doplňování zásob, přejděte na odkaz:
Logika v sekci „Skladování a sklady“.

Vyberte sklad
------------------

Pokud je metoda doplňování skladu:doc:`dodávka z jiného skladu
<přepočítání zásob>, zkontrolujte dostupné množství produktů ve skladech ostatních prodejen kliknutím na
Pop-up okno „Informace o doplňování zásob“. Sklady, které mohou zásoby doplnit, jsou
v záložce „Sklad“ a v položce „Dostupné množství“ je
Na skladě v každé prodejně.

Po výběru skladu pro nakládku zboží klikněte na tlačítko „Vybrat trasu“
klikněte na tlačítko „Zpět“, pravidlo přesměrování se vrátí ke své preferované cestě (Koupit nebo Vyrábět).

.. obrázek:report/vyber-sklad.png
:alt:Karta skladu v okně s informacemi o doplňování zásob.

.. viz také:
:ref:`Pravidla pro dočasné přeskupení zásob <nákupy/dodávky>“
