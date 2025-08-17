.._textový editor:

=====================
Odoo editor s obsahem textu
=====================

Odoo bohatý textový editor umožňuje vytvářet a upravovat obsah bohatého textu v poli HTML, jako je
políčkach „Vnitřní poznámky“ a „Popis“ a také v části „Znalosti“.
články <poznatky/clanky_redakce/edit-article> a :ref:`Zpráva ze studia
editor <studia/pdf-zpravy/editor-zpravy>, mezi dalšími. Zadejte text nebo použijte
:ref:`nástrojová lišta <essentials/html_editor/toolbar>` nebo
pro formátování a strukturu textu.

.. tip::
Procházejte textem a přejíždějte nad jakýmkoliv prvkem (nadpis, tabulka, schránka atd.)
:ikonka: „fa-sort“ :guilabel: (přetahování) ikony. Klikněte a podržte ikonku, abyste mohli přetáhnout a vložit prvek
jinde v textu.

... /essentials/html_editor/toolbar:

Nástrojová lišta textového editoru
===================

Pro úpravu slova, věty nebo odstavce vyberte nebo klikněte na něj dvakrát, abyste zobrazili textový editor.
nástrojovou lištu a použijte libovolnou z následujících možností formátování:

- Styl písma: Změňte styl pomocí různých možností, např. Header 1 až 6
Normální, Odstavec, Kód a :guilabel:„Citace“.
- :guilabel:`B`: Vyberte text a stiskněte klávesu Shift + Ctrl + B.
- :guilabel:`I`: Vložte text do kurzívy.
- :guilabel:`U`: Podtrhněte text.
- :guilabel:`S`: Prostřihnout text.
- :guilabel:`A“ a „:icon:`fa-paint-brush“ (malířská štětec) pro přizpůsobení písma.
pozadí barevně odlišených, tj.:

  - :guilabel:`Solidní“: vyberte preferovanou barvu z předdefinované palety.
  - :guilabel:`Vlastní barvy“: Vyberte si barevný odstín pomocí kolečka nebo konfigurací
:guilabel:`hex“ kód a :guilabel:`RGBA“ hodnoty.
  - :guilabel:`Gradient“: Vyberte předdefinovaný gradient nebo si jej upravte podle vlastních preferencí
mezi „Lineární“ nebo „Radiální“ a upravit kolo.

- Velikost písma: Změňte velikost textu.
- :icon:`fa-list-ul` (:guilabel:`seznam bodů`): Změňte text na seznam bodů.
- :icon:`fa-list-ol` (:guilabel:`číslovaný seznam`): Z textu vytvořte číslovaný seznam.
- :icon:`fa-check-square-o` (:guilabel:`checklist`): Změňte text na seznam úkolů.
- :ikonka: „fa-link“ (:guilabel:„link“): Vložte nebo upravte odkaz na vybraný text a volitelně
nahrát obrázek pomocí jeho souborového URL.
- :guilabel:`Přeložit“: Přeložte obsah v nainstalovaných jazycích

- :icon:`fa-magic` :guilabel:`AI“ (:guilabel:"ChatGPT"): Získejte tipy generované umělou inteligencí a upravujte
tón pomocí kliknutí na tlačítka jako například „Korektní, Zkrácený, Prodloužený, Přátelský“.
Profesionální“ a „Přesvědčivý“.

.. obrázek:: html_editor/styl-a-barvy.png
:alt: Nástrojová lišta textového editoru


.. tip::
Použijte následující klávesové zkratky k aplikaci formátování:
      - **Výrazně**: Stiskněte klávesu CTRL/CMD a poté B, I nebo U pro aplikaci
písmo tučným, kurzivou nebo podtržením.
      - *Seznam s čísly*: Zadejte „1.“ nebo „1.)“ pro zahájení seznamu s čísly.
      - *Seznam s hvězdičkou*: Zadejte znak * nebo -, abyste začali seznam s hvězdičkou.

... /povinné/html_editor/kommandos:

Příkazy k ovladači
=================

Pro použití příkazu zadejte na klávesnici / pro otevření krabičky s příkazy, poté zadejte název příkazu nebo vyberte ze seznamu.
mnoho funkcí pro vkládání tabulek, obrázků, reklamních ploch atd.

.. tip::
Při zahájení nového odstavce se zobrazí nástrojová lišta s ikonami klávesových zkratek. Klikněte na ikonu, abyste přidali
příkaz nebo klikněte na ikonu „Ellipsis“ (ikona s označením „guilabel:ellipsis“) pro otevření
ovládací box pro všechny příkazy.

.. poznámka::
Příkazy specifické pro konkrétní aplikace jsou v této popisu vynechány.

.. záložky::


... seznam-tabulka::
:šířky: 20 80
:hlavičky: 1
:sloupek: 1

         * – Příkaz
           - Použití
         * --:separator:
           - Vložte horizontální oddělovač.
         * --:guilabel:`2 sloupce`
           - Převést na dvě sloupce.
         * --:guilabel:`3 sloupce“
           - Převést na tři sloupce.
         * --label:'4 sloupce'
           - Převést na čtyři sloupce.
         * :- table
           - Vložte tabulku.
         * – :guilabel:`Obsahuje seznam bodů.
           - Vytvořte seznam bodů.
         * – :guilabel:`Seznam číselný“
           - Vytvořte seznam s čísly.
         * – :guilabel:Seznam
           - Vytvořte si seznam.
         * -- :guilabel:`Citát`
           - Přidejte sekci citace.
         * :- guilabel:Kód
           - Přidejte novou část kódu.

.. poznámka::
Začněte organizovat tabulku, přejeďte kurzorem nad sloupcem nebo řádkem, aby se zobrazilo menu pro tabulky. Klikněte na
:ikonka_fa_ellipsis_h: :guilabel_(zavináč): ikona pro pohyb, vložení nebo odstranění sloupce
řada.

.. tab:: Bannery

... seznam-tabulka::
:šířky: 20 80
:hlavičky: 1
:sloupek: 1

         * – Příkaz
           - Použití
         * :-:guilabel:`Banner Info“
           - Vložte informační lištu.
         * „Úspěšný banner“
           - Vložte úspěšný banner.
         * „Varování před bannery“
           - Vložte varovný pruh.
         * „Varování“
           - Vložte varovný pruh.

... tab:: Formát

... seznam-tabulka::
:šířky: 20 80
:hlavičky: 1
:sloupek: 1

         * – Příkaz
           - Použití
         * --:guilabel:Hlava 1
           - Velký nadpis.
         * Hlava 2
           - Střední nadpis.
         * ::h3::Hlava 3
           - Malá nadpisová část.
         * :- guilabel:"Text"
           - Blok odstavce: Vložte odstavec.
         * – :guilabel:`Změnit směr“
           - Převrátit směr textu.

..... tab::Média

... seznam-tabulka::
:šířky: 20 80
:hlavičky: 1
:sloupek: 1

         * – Příkaz
           - Použití
         * :-label:Média
           - Vložte obrázek nebo ikonu: :ref:`Vložit médium <vlozit-medialni-objekt>` nebo vyhledejte v databázi Unsplash
nebo nahrajte obrázky, dokumenty nebo ikony.
         * – :guilabel:`Plocha pro stříhání“
           - Přidejte sekci schránky, do které můžete ukládat obsah a používat ho v jiných aplikacích.
         * – :guilabel:`Nahrát soubor“
           - Přidejte tlačítko ke stažení: sdílejte obrázky, nahrávky nebo dokumenty, které mohou uživatelé v rámci organizace stáhnout.
stáhnout.

.. tab:: Navigace

... seznam-tabulka::
:šířky: 20 80
:hlavičky: 1
:sloupek: 1

         * – Příkaz
           - Použití
         * – :guilabel:`Odkaz`
           - Přidejte odkaz: Zadejte název a vložte URL nebo nahrajte soubor, pak klikněte.
:guilabel:`Použít“.
         * „Tlačítko“
           - Přidejte tlačítko: Zadejte název, zadejte URL nebo nahrajte soubor, vyberte styl tlačítka
typu a velikosti a poté klikněte na tlačítko „Použít“.
         * :- guilabel:"Článek"
           - Vložte zkratku na článek znalostí: `Knowledge article </applications/productivity/knowledge>`.
         * – :guilabel:Termín
           - Přidat konkrétní termín: Vyberte jeden nebo více typů termínu, který chcete přiřadit.
potom klikněte na tlačítko „Vložit odkaz“.
         * —:guilabel:`Obsah`
           - Vyznačte strukturu (nadpisy): Vytvořte obsah založený na nadpisech.
         * :- guilabel:"Video odkaz"
           - Vložte video: Zkopírujte a vložte odkaz na video (jen YouTube, Vimeo, Dailymotion a Youku).

... tab::Widget

... seznam-tabulka::
:šířky: 20 80
:hlavičky: 1
:sloupek: 1

         * – Příkaz
           - Použití
         * :- guilabel:emoji
           - Přidejte emotikon: vyhledejte požadovaný emotikon.
         * :- :guilabel:`Tři hvězdy``
           - Vložte hodnocení do 3 hvězdiček.
         * „Pětihvězdičkový“
           - Vložte hodnocení od 1 do 5 hvězdiček.

.. tab:: Nástroje umělé inteligence

..... seznamová tabulka::
:šířky: 20 80
:hlavičkové řádky: 1
:pilíře: 1

       * – Příkaz
         - Použití
       * :- guilabel:ChatGPT
         - Vytvářejte obsah s umělou inteligencí.

...... záložka: Základní blok

... seznam-tabulka::
:šířky: 20 80
:hlavičky: 1
:sloupek: 1

         * – Příkaz
           - Použití
         * :- guilabel:Podepsané
           - Vložte svůj podpis.

.._vložit-multimédia:

Vložte médium
------------

Pro vložení média zadejte příkaz /Media nebo klikněte na ikonu :icon:`fa-file-image-o` :guilabel:`(obrázek)`
Nástrojové tipy a poté vyberte jednu z následujících karet:

- :guilabel:`Obrázky“

   - Hledejte v databázi Unsplash:
vhodné obrázky.
   - :guilabel:`Přidat URL“: Zkopírujte a vložte **adresu obrázku**.
   - :guilabel:`Nahrát obrázek“: Nahrajte obrázek do knihovny.

- :label:Dokumenty

   - Hledání dokumentu v databázi.
   - :guilabel:`Přidat URL“: Vložte platnou URL adresu.
   - :guilabel:`Nahrát dokument“: Nahrajte dokument z místního disku.

- :guilabel:`Ikony“: Hledání ikony z výběru v databázi.

Nástrojová lišta pro úpravu médií
~~~~~~~~~~~~~~~~~~~~

Po vložení obrázku klikněte na něj a zobrazí se nástroje pro úpravu médií.
použít některý z následujících formátovacích možností:

- :icon:`fa-search-plus` (:guilabel:`preview`): Zobrazte si obrázek, přiblížte nebo oddálte, vytiskněte jej nebo
Stáhněte si ji. Zavřete náhled kliknutím na ikonu „fa-times“ (zavřít) v
v pravém horním rohu.
- :guilabel:`Popis obrázku“: Upravte popis a nápovědu obrázku, pak klikněte na „Uložit“.
- :icon:`fa-square` (:guilabel:`rounded`): Aplikujte zaoblený tvar na rohy obrázku.
- :icon:`fa-circle-o` (:guilabel:`circle`): Aplikuj kruhový tvar na obrázek.
- :icon:`fa-sun-o` (:guilabel:`stín`): Použij na obrázek stíny.
- :icon:`fa-picture-o` (:guilabel:`obrázek`): Použij okraj k obrázku.
- :icon:`fa-plus-square-o` (:guilabel:`padding`): Přidejte obrázkové odsazení a zvolte malý,
malý, střední nebo velký.
- :guilabel:`Výchozí“: obnovit obrázek na jeho výchozí velikost.
- :guilabel:`100 %“: Obrázek nastavte na plnou velikost.
- Guilabel: 50 %: Obraz zmenšete na polovinu.
- :guilabel:`25 %“: Zmenšete obrázek na čtvrtinu jeho velikosti.
- Ikona „Objekt“ (): Změňte velikost a otáčení obrázku. Kliknutím na
:ikona:`fa-object-ungroup` :guilabel:`(objekt)` ikona znovu, aby se obnovila transformace.
- Ikona „Ořezávání“ („Crop“) nebo následující možnosti:

   - Vyberte si z poměrů stran „Pružný“, „16:9“, „4:3“, „1:1“ nebo „2:3“.
   - Zvětšete nebo zmenšete.
   - Otočte vlevo nebo vpravo.
   - Otočit na výšku nebo na šířku.
   - Obnovit obrázek.

- :guilabel:`Vyměnit za obrázek z Unsplashu`: Vyměňte obrázek vyhledáním na Unsplash.
</applications/general/integrations/unsplash> databáze přidáním URL nebo nahrazením jiným.
jedna.
- :ikonka: „fa-link“ (:guilabel:„odkaz“): Vložte odkaz na obrázek, zadejte URL adresu a klikněte
:guilabel:`Použít“. K odstranění odkazu klikněte na ikonku :icon:`fa-chain-broken` :guilabel:`(odpojit)`.
- :icon:`fa-trash` (:guilabel:`trash`): Odstranit obrázek.
