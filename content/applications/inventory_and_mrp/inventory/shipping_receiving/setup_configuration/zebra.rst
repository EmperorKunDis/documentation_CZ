=========================
Konfigurace štítku zebry
=========================

.. |ZPL| nahradit za: zkratka: ZPL (Zebra Programming Language)

V Odoo jsou štítky vytisknuté v formátu souboru Zebra Programming Language (ZPL) navrženy tak, aby
čtyřnásobný šestinásobný etiketový štítek. K přizpůsobení (nebo formátování) textu k různým velikostem etiket ZPL
Přejděte na pohled na štítky ZPL (<inventory/shipping_receiving/zpl-view>) a změňte |ZPL|
kód.

.. varování::
Při přizpůsobování kódu v Odoo je třeba mít na paměti, že aktualizace databáze na novější verzi
porušit vlastní kód. **Klienti jsou zodpovědní za udržování svého vlastního kódu**.

Pro vysvětlení a příklad kódu často požadovaných zebr se podívejte na následující části.
Vlastní úpravy štítků.

- :ref:`Upravte marže <sklad/přijetí a expedice/marže>“
- :ref:`Zvětšit/zmenšit čárový kód <sklad/přijetí/dodání/změnit velikost>“
- :ref:`Přetočit položky <sklad/příjem a výdej/rotate>“

.. inventarizaci, přijímání a expedici zboží:

Přejděte na pohled štítku ZPL
==========================

Pro začátek přizpůsobení štítku Zebra v Odoo zapněte režim vývojáře (viz developer-mode).
hlavní přehledový panel Odoo, typ „Zprávy“. Z výsledků vyhledávání, které se objeví v následujícím okně
V okně zvolte položku „Nastavení / Technické / Hlášení / Zprávy“ a otevřete
Stránka „Zprávy“.

.. poznámka::
Chcete-li ručně přejít na stránku „Zprávy“, přejděte do aplikace Nastavení a poté na:
Technické --> Hlášení: Zprávy.

.. obrázek:zebra/hledani.png
:align:center
:alt:Zobrazit celosvětový výsledek vyhledávání „Reporty“.

Na stránce „Hlášení“ v poli „Vyhledávání…“ zadejte ZPL a stiskněte klávesu Enter.
Při tomto kroku představuje Odoo seznam dostupných štítků Zebra v Odoo. Vyberte požadovaný štítek Zebra
Štítek ze seznamu, abyste jej mohli upravit na samostatné stránce.

.. poznámka::
Tisknutelné etikety ZPL v Odoo:

   - :ref:`číslo sériového čísla <zásobník/příjem zboží/štítky s číslem sériovým>“
   - druh operace
   - čárový kód balení
   - :ref:`Štítek výrobku <Inventura/Přijetí a expedice/Štítky výrobků>`
   - obal výrobku
   - hotový výrobek (aplikace Odoo Manufacturing je nutná)

Dále klikněte na tlačítko s ikonou „fa-code“ a vyberte požadovaný text.
:doc:`zobrazení <../../../../../developer/reference/user_interface/view_records>“.

.. obrázek: žirafa/qweb-views.png
:align:center
:alt:Zobrazit chytrý tlačítko Qweb na zprávě o číslech a sériích (ZPL).

**Číslo a sériové číslo (ZPL)**, vyznačující chytrý tlačítko Qweb.

Ve zobrazeném pohledu přejděte na záložku „Architektura“, abyste viděli kód |ZPL|.

.. důležité::
Pro zajištění, že přizpůsobení nebude při aktualizaci přepsáno, klikněte na ikonu „chyba“
:guilabel:'(chyba)' ikona na stránce zobrazující pohled. Pak vyberte možnost „Zobrazit metadata“.
zobrazí se vyskakovací okno pro zobrazení metadat.
zajistit, aby pole „Žádné aktualizace“ bylo nastaveno na „Pravda (změnit)“. Klikněte na „OK“
zavřít okno „Zobrazit metadata“.

.. obrázek:zebra/architektura.png
:align:center
:alt:Architektonická záložka v pohledu.

.. skladování, přijímání a marže:

Upravte marži
=============

Text se na štítku ZPL od Odoo zkrátí, pokud překročí padesát pět
znaků. Pro umístění dlouhých názvů produktů nebo čísel šarží na jediné řádce upravte odsazení.

Nejprve přejděte na ZPL kód štítku v sekci „Inventura a příjem zboží“
kartě Architektura. V kódu pro etikety produktů hledejte příkaz ^FT
která určuje, kde začít umisťovat text nebo grafický prvek na etiketu. Obě čísla
Poté, co zadáte „^FT“, definujte souřadnice x a y pomocí teček (podobně jako
pixelů z levého a horního okraje).

.. důležité::
Při přizpůsobení štítků pro sériové číslo a výrobní číslo hledejte příkaz ^FO místo ^FT.

Příklad:

Následující příklad ukazuje, jak je produktu přiřazené jméno v základním nastavení |ZPL|
formátování. V záložce **Pevná** je zadán počáteční souřadnicový bod etikety ve tvaru
změnil na „^FT0,80“, aby se vešel celý název.

.. záložky::

... tab:: Výchozí

.. obrázek: zebra/default-margin.png
:align: střed
:alt: Příklad etikety s čárovým kódem a názvem výrobku přetrženým.

**Kód**:

... kódový blok:: xml

^XA^CI28
^FT100,80^A0N,40,30^FD[E-COM11] Skříň s dvířky (dřevo: třešeň, úchytky: mosazné)^FS
         ...
^XZ

.. tab:: Upraveno

.. obrázek: zebra/pevný-okraj.png
:align: střed
:alt: Příklad štítku s čárovým kódem a názvem produktu posunutým doprava.

**Kód**:

... kódový blok:: xml

^XA^CI28
^FT0,80^A0N,40,30^FD[E-COM11] Skříň s dvířky (dřevo: třešeň, úchytky: mosazné)^FS
         ...
^XZ

.. inventura/příjem/zmenšení:

Změnit velikost čárového kódu
==============

Abychom upravili velikost čárového kódu na měřítko, začněte tím, že se přesunete do :ref:`ZPL kódu štítku
„Zobrazit“ v záložce „Architektura“. Hledejte řádek s „^FO
příkaz (obvykle na třetí řádce), který je výchozím bodem pro nastavení okraje čárového kódu.

Komandu ^BY lze použít k nastavení velikosti čárového kódu. Tato funkce potřebuje tři čísla: šířku čárky, šířku široké čárky
výšku a šířku pásu. Výchozím kódem v Odoo je ^BY3, který nastavuje
šířka tří teček, typická velikost, kterou snadno čtejí skenery čárových kódů.

Příklad:
Pro zmenšení čárového kódu na požadovanou velikost se „^BY3“ sníží na „^BY2“.

.. záložky::

... tab:: Výchozí

.. obrázek:: zebra/normální_čárový_kód.png
:align: střed
:alt:Příklad štítku s čárovým kódem.

**Kód**:

... kódový blok:: xml

^XA^CI28
         ...
^FO100,160^BY3
         ...
^XZ

.. tab:: Upraveno

.. obrázek: zebra/shrink-barcode.png
:align: střed
:alt: Příklad štítku s čárovým kódem, na kterém je zmenšený rozměr čárového kódu.

**Kód**:

... kódový blok:: xml

^XA^CI28
         ...
^FO100,160^BY2
         ...
^XZ

... inventář/přijetí/obrat:

Natočte prvky
===============

Pro otáčení prvků v |ZPL| začněte tím, že se přesunete do kódu štítku
„Zobrazení“ v záložce „Architektura“.

První parametr příkazu ^BC (:dfn:informace, která ovlivňuje chování příkazu)
definuje otáčení položky, která může být:

- „n“: zobrazit normálně
- `R`: otočit o 90 stupňů
- „I“: otočit se o 180°
- „B“: otočit o 270°

Příklad:
Pro otočení čárového kódu je změněna zkratka na „^BCB“.

.. záložky::

... tab:: Výchozí

.. obrázek:: zebra/lot.png
:align: střed
:alt:Příklad štítku s čárovým kódem.

**Kód**:

... kódový blok:: xml

^XA^CI28
         ...
^BCN,100,Y,N,N
         ...
^XZ

.. tab:: Upraveno

.. obrázek: zebra/rotate.png
:align: střed
:alt:Příklad štítku s čárovým kódem, který je nakloněn.

**Kód**:

... kódový blok:: xml

^XA^CI28
          ...
^BCB,100,Y,N,N
          ...
^XZ

