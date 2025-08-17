=============
Čištění dat
=============

Aplikace **Odoo Data Cleaning** zajišťuje integritu a sjednocenost dat následujícími funkcemi:

- :ref:`Sjednocuje duplicitní záznamy <úprava dat/sjednocení duplicitních záznamů>“: sloučí nebo odstraní duplicitní záznamy, aby se zajistilo
Data jsou jedinečná.
- :ref:`Recyklace <úprava dat/recyklace>: identifikuje zastaralé záznamy k archivaci nebo odstranění
jejich.
- :ref:`Formáty <úprava dat/čistění polí>“: standardizuje textová data tím, že je najde a nahradí
podle specifikovaných potřeb.

Přizpůsobitelné pravidla zajišťují, aby byla textová data aktuální, přehledná, konzistentně formátovaná a
s konkrétními požadavky na formátování společnosti.

.. data_cleaning/instal-moduly:

Nainstalujte moduly
===============

Aplikace **Data Cleaning** se skládá z několika modulů. Instalovat:ref:`<general/install>`.
Pokud chcete mít přístup k všem dostupným funkcím:

.. seznam tabulkový::
:hlavičky: 1
:šířky: 40 60

   * |Jméno
| „Technické jméno“
     - Popis
   * |:guilabel:`Recyklace dat`
| `data_recyklace`
     - Modul základní funkce pro recyklaci, dostupný v:odoo_community_edition
"<instalace/edice>".
   * |:guilabel:`Čištění dat`
| `úprava dat`
     - Zajišťuje funkci čištění pole pro formátování textových dat v rámci více záznamů, dostupnou
**pouze** v edici Odoo Enterprise (viz instalaci/edice).
   * | :guilabel:`Čistění dat (sloučení)`
|  data_souboru
     - Umožňuje funkci duplikátů najít podobné záznamy a sloučit je.
dostupná pouze v edici :ref:`Odoo Enterprise <install/editions>`.

.. spoiler:: K dispozici jsou také některé aplikačně specifické moduly

...... seznamová tabulka::
:šířky: 40 60

      * – | :guilabel:`Dedupe CRM“
|  data_merge_crm
        - Aktivuje funkci duplicitního vyhledávání v aplikaci CRM a používá výchozí nastavení
sloučení funkce <../sales/crm/pipeline/merge_similar>.
      * |:guilabel:`Služba Helpdesk Merge“
| `data_merge_helpdesk`
        - Aktivuje funkci pro sloučení v aplikaci Helpdesk.
      * |:guilabel:`Akce sloučení projektů“
| data_souboru
        - Zapíná funkci pro sloučení projektů v aplikaci **Projekty**.
      * – | :label:„Deduplifikační služba UTM“
| data_merge_utm
        - Aktivuje funkci pro sloučení dat v aplikaci **UTM Tracker**.
      * |:guilabel:`Spojení účetnictví WMS“
|  „součet skladových zásob“
        - Vytváří upozornění v případě sloučení produktů, které mohou ovlivnit ocenění zásob.
Je nainstalována aplikace Inventář.

... _úprava dat a odstranění duplicitních záznamů:

Deduplifikace
=============

Plocha Duplicates seskupuje podobné záznamy, které lze sloučit:
Srovnáním podmínek v záznamu, který definují pravidla pro sjednocování
<úprava dat/zjednodušení pravidel>.

Přejděte na tento panel pomocí odkazu v menu „Data Cleaning app --> Deduplication“.

.. obrázek:: data_cleaning/data-cleaning-duplicates.png
:alt:Dashboard duplicit v aplikaci Data Cleaning.

Stránka vedlejší lišty :guilabel:`RULE` zobrazuje každou aktivní pravidlo pro sjednocování a celkový počet
Počet duplicitních záznamů vedle každého pravidla.

Výchozí je pravidlo „Všechny“. Záznamy jsou seskupeny podle svého pravidla, s
Hodnocení podobnosti (z 100 %), s následujícími sloupci:

- :guilabel:`Vytvořeno“: datum a čas, kdy byla původní záznam vytvořena.
- :guilabel:`Jméno`: původní název nebo titul nahrávky.
- :guilabel:`Hodnoty pole“: původní hodnoty polí použitých k detekci duplicitních záznamů.
- :guilabel:`Použito v:“ seznamuje s dalšími modely, které odkazují na původní záznam.
- :guilabel:`ID“: jedinečný identifikátor původního záznamu.
- :guilabel:Je to hlavní záznam: Duplicitní záznamy jsou sloučeny do záznamu „hlavního“.
*jedna* hlavní záznam v souboru podobných záznamů.

Vyberte konkrétní pravidlo v bočním panelu „Pravidla“ (viz obrázek) k filtrování duplicitních záznamů.

... _úprava dat/sloučení záznamů:

Sloučit duplicitní záznamy
-----------------------

Nejprve si vyberte hlavní záznam v rámci skupiny podobných záznamů. Hlavní
Záznam slouží jako základ, na který se přidávají další informace z podobných záznamů.

Pokud chcete, nemusí být nastaven žádný hlavní záznam, takže Odoo může náhodně vybrat jeden z nich k sloučení.

Nyní klikněte na tlačítko „Sloučit“ v horní části skupiny podobných záznamů. Pak klikněte
:guilabel:OK, aby se spojení potvrdilo.

Jakmile je záznam spojen s hlavním záznamem, je do chatu hlavního záznamu zaznamenána zpráva popisující
sloučit. Některé záznamy, jako například úkoly v projektu, jsou zaznamenány v chatu s odkazem na starý
zaznamenat jako pohodlný odkaz na sloučení.

..tip:
Skupiny odstraníte kliknutím na tlačítko :guilabel:`DISCARD`. Po tomto kroku skupina
skryté z listu a archivované.

Zobrazte skupiny, které byly vyhozeny, kliknutím na filtr „Vyhozené“ v sekci „Hledat“.
<hledání/filtry>“.

... _úpravy dat/sjednocení pravidel:

Pravidla pro duplicitní obsah
-------------------

Pravidla pro odstranění duplicitních záznamů určují podmínky, za kterých jsou záznamy detekovány jako duplicity.

Tyto pravidla lze pro každý model v databázi nakonfigurovat s různými úrovněmi
Specifika. Pro začátek přejděte na: „Aplikace pro čištění dat --> Konfigurace -->
Deduplifikaci.

..tip:
Deduplikační pravidla se spouští každý den, výchozí hodnota je jeden denně jako součást plánované akce cron.
(*Spojování dat: Najít duplicitní záznamy*) nebo ručně.
<data_cleaning/run-deduplication-rule> kdykoliv.

Upravte pravidlo pro odstranění duplicitních záznamů
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vyberte výchozí pravidlo k úpravě nebo vytvořte nové pravidlo klepnutím na tlačítko „Nový“.

Nejprve vyberte model pro tuto pravidlo. Vybráním modelu aktualizuje titulek pravidla
k vybranému modelu.

Pokud chcete, nastavte doménu pomocí :guilabel:`Doména`, abyste určili záznamy, které se týká tato pravidla.
Počet splňujících podmínky záznamů je zobrazen v odkazu „:icon:`oi-arrow-right` :guilabel:`# záznamů““.

Podle zvoleného modelu se v poli „Odstranění duplicit“ objeví pole s názvem „Odstranění duplicit“.
Vyberte, zda chcete archivovat nebo smazat sloučené záznamy.

Dále vyberte režim sloučení:

- :guilabel:'Manuální': vyžaduje ruční sloučení každé duplicitní skupiny a umožňuje
:guilabel:`Upozornit uživatele“ pole.
- :guilabel:`Automaticky“: automaticky slučuje duplicitní skupiny bez upozornění uživatelům na základě
záznamy s podobností vyšší než je hodnota prahového procenta nastavená v :guilabel:`Podobnost
Pole „Překážka“.

Zapněte přepínač „Aktivní“ a zahajte sledování duplicitních záznamů pomocí této pravidlo.
zachráněny.

Nakonec vytvořte alespoň jednu pravidlo pro eliminaci duplicitních záznamů ve sloupci „Deduplikační pravidla“.
klikněte na tlačítko „Přidat řádek“, které se nachází pod sloupcem „Unikátní identifikační pole“.

- Vyberte pole v modelu z rozevírací nabídky Unique ID Field. Toto pole je
odkazované na podobné záznamy.
- Vyberte shodný stav v poli „Přiřadit pokud“ pole :guilabel:`Match If`,
podle textu v poli „Jedinečný identifikátor“:

  - :guilabel:`Přesné shody“: znaky v textu přesně odpovídají.
  - „Přesnost při nezávislosti na přízvuku“: písmena v textu se shodují bez ohledu na
způsobu oblékání a rozdíly v přízvuku, který je specifický pro daný jazyk.

.. důležité:
Jeden alespoň z těchto pravidel musí být nastaven, aby se pravidlo mohlo snažit o odstranění duplicitních položek.

..tip:
Pro pokročilé konfiguraci jsou k dispozici další pole.

Pokud je databáze více společnostmi sdílena, je k dispozici pole :guilabel:`Křížová společnost“.
jsou navrhovány duplicity mezi různými společnostmi.

Aktivujte režim vývojáře, abyste viděli pole „Návrhová hranice“.
pokud je pod prahem nastaveným v tomto poli, nebudou navrhovány.

Pokud je konfigurace pravidla dokončena, buďte zavřete formulář pro pravidlo nebo spusťte pravidlo ručně:
„Ověřit duplicitní záznamy“ a okamžitě zachytí duplicitní záznamy.

... _vyčistit data/spustit pravidlo pro odstranění duplicitních záznamů:

Použijte ručně spuštěnou pravidlo pro odstranění duplicitních položek
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chcete-li manuálně spustit konkrétní pravidlo duplicitního odstranění v libovolný čas, přejděte na:
Aplikace „Nastavení“ – „Deduplifikační pravidla“ a vyberte pravidlo, které chcete spustit.

Poté vyberte tlačítko „Sloučit“ na pravém horním rohu formuláře.
Ikona „Klon“ zobrazuje počet duplicitních záznamů zachycených v databázi.

Klikněte na tlačítko „Duplikáty“ chytrého panelu.
<vyčištění dat/sloučení záznamů>.

.. _úklid dat/vyčištění:

Recyklujte gramofonové desky
===============

Použijte funkci *vyčistit databázi od starých a zastaralých záznamů*.

Příkazový řádek pro recyklaci polí zobrazuje záznamy, které lze archivovat nebo smazat, a to na základě shody
podmínky uvnitř záznamů stanovených pravidly pro recyklaci dat:

Přejděte na tento panel pomocí následujícího postupu: Data Cleaning app --> Recycle Records.

.. obrázek:: data_cleaning/data-cleaning-recycle.png
:alt:Přístupový panel aplikace Data Cleaning s přehledem recyklace dat.

Nápověda „Pravidla pro recyklaci“ uvádí každé aktivní pravidlo pro recyklaci záznamů.

Výchozí volbou je možnost „Všechny“. Záznamy se zobrazují následovně
sloupky:

- :guilabel:`ID původního záznamu“: ID původního záznamu.
- :guilabel:`Název záznamu“: název nebo titul původního záznamu.

Vyberte konkrétní pravidlo v bočním panelu „RECYCLE RULES“ k filtrování záznamů.

K recyklaci záznamů klikněte na tlačítko „Potvrdit“ vedle řádku záznamu.

Při provedení takového kroku je záznam znovu použit podle nastavení pravidla buď
archivovány nebo odstraněny z databáze.

..tip:
Zrušte skupiny kliknutím na tlačítko „Zrušit“ (ikona „fa-times“). Po tomto kroku se
záznam se skryje z seznamu a nebude detekován znovu v budoucnu podle pravidla recyklace.

Zobrazte vyhozené záznamy pomocí filtru „Vyhozeno“ v :ref:`vyhledávacím poli
v seznamu „Vyhledávání / filtry“.

.. _data_cleaning/recyklace-pravidla:

Recyklace rekordů
--------------------

Pravidla pro zpětný odběr nahrávek (Recycle Records Rules) stanovují podmínky, za jakých jsou nahrávky recyklovány.

Tyto pravidla lze pro každý model v databázi nakonfigurovat s různými úrovněmi
Specifika. Pro začátek přejděte na: „Aplikace pro čištění dat --> Konfigurace -->
Recycle Records.

..tip:
Recyklace pravidel se spouští jednou za den, výchozím nastavením je součástí plánované akce cron (*Data Recycle:
Clean Records*). Každá pravidla však lze spustit ručně:
Kdykoliv.

Výchozí nastavení neobsahuje žádné pravidlo pro zpětnou recyklaci. Kliknutím na tlačítko „Nový“ vytvořte nové pravidlo.

Na záznamu o recyklaci vyberte první model pro tuto pravidlo cílit. Vyberte
model aktualizuje název pravidla na vybraný model.

Volitelně můžete nakonfigurovat filtr, který určí záznamy, které jsou v souladu s touto pravidlem.
Počet splňujících podmínky záznamů je zobrazen v odkazu „:icon:`oi-arrow-right` :guilabel:`# záznamů““.

Následně nastavte pole a časové rozpětí pro způsob detekce záznamů k recyklaci:

- :guilabel:`Časové pole“: vyberte pole z modelu, na jehož základě se bude čas počítat (:dfn:`Delta`).
- :guilabel:`Delta`: zadejte délku času, která musí být celé číslo (např. 7).
- „Deltamodul“: vyberte jednotku času („Dny“, „Týdny“)
:guilabel:`Měsíce“ nebo :guilabel:`Roky“.

Poté vyberte režim „Recycling“:

- :guilabel:„Manuální“: vyžaduje ruční recyklaci každého detekovaného záznamu a umožňuje
:guilabel:`Upozornit uživatele“ pole.
- :guilabel:`Automaticky“: automaticky slučuje skupiny vytříděného odpadu bez upozornění uživatelů.

V neposlední řadě vyberte akci „Recyklace“ buď „Archivovat“ nebo „Smazat“.
záznamy. Pokud je vybrána volba „Smazat“, zvolte, zda chcete nebo nechcete archivované záznamy zahrnout
údaje v pravidlech.

Pokud je konfigurace pravidla dokončena, buďte zavřete formulář pro pravidlo nebo spusťte pravidlo ručně:
„Vyčistit data / spustit pravidlo recyklace“ k okamžitému zachycení záznamů pro recyklaci.

Příklad:
Řízení recyklace lze nakonfigurovat tak, aby byly smazány archivované kontakty a příležitosti, které byly naposledy upraveny
aktualizován před rokem a s konkrétním důvodem ztráty pomocí následujícího nastavení:

   - :guilabel:`Model“: :guilabel:"Vedoucí/Příležitost"
   - Filtr:

     - „Aktivní“ je „nepovolený“.
     - „Ztracený rozum“ je „moc drahý“.

   - :guilabel:`Časová pole“: :guilabel:"Poslední aktualizace (lead/příležitost)"
   - :guilabel:`Delta“: „1“
   - :guilabel:`Delta Unit“: :guilabel:`Roky“
   - :guilabel:`Režim recyklace“: „Automaticky“
   - :guilabel:`Recyklace akce“: :guilabel:`Smazat“
   - :guilabel:`Zahrnout archivované stránky“: :icon:`fa-check-square`

.... obrázek:: data_cleaning/data-cleaning-recycle-rule.png
:alt:Formulář pro vytváření záznamů o recyklaci pro příležitosti/prodejní příležitosti.

..._data-cleaning/run-recycle-rule:

Spusťte ručně opětovné použití pravidla
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chcete-li ručně spustit konkrétní pravidlo pro čištění dat v libovolný okamžik, přejděte na:
--> Konfigurace --> Vyprázdnit záznamy“ a vyberte pravidlo, které chcete spustit.

Poté klikněte na tlačítko „Spustit nyní“ v pravém horním rohu.
Ikona „fa-bars“ v tlačítku „Chytré tlačítko“ zobrazuje počet zachycených záznamů.

Klikněte na tlačítko „Záznamy“ v ikoně „fa-bars“ a poté vyberte možnost „Spravovat záznamy“.
<vyčištění dat/recyklace>.

...úprava dat / úprava polí:

Čištění pole
==============

Použijte funkci vyčištění pole k udržení konzistentního formátování jmen, telefonních čísel, identifikátorů a
dalších polích v databázi.

Dashboard *Údaje o čištění polí* zobrazuje formátování dat v polích záznamu.
Vyhovět konvenci stanovené pravidly pro čištění hřišť.

Přejděte na tento panel pomocí volby v menu: Data Cleaning app --> Field Cleaning.

.. obrázek:: data_cleaning/data-cleaning-field.png
:alt: Panel čistících záznamů v aplikaci Čištění dat.

V záložce „Čistící pravidla“ je uveden seznam všech aktivních čistících pravidel.

Výchozí je pravidlo „Všechny“. Záznamy jsou seřazeny podle následujících sloupců:

- :guilabel:`ID původního záznamu“: ID původního záznamu.
- :guilabel:`Název záznamu“: název nebo titul původního záznamu.
- :guilabel:`Pole“: pole původního záznamu, které obsahuje hodnotu k formátování.
- :guilabel:`Aktuální hodnota“: aktuální hodnota v poli původního záznamu.
- :guilabel:`Navrhované“: navrhovaný formátovaný výraz v poli původního záznamu.

Pro vyčištění a formátování záznamů klikněte na tlačítko „Zkontrolovat“ v řádku
rekord.

Při tomto způsobu se záznamy formátují a čistí.

..tip:
Zaznamenané hodnoty můžete vymazat kliknutím na tlačítko „Odmítnout“ (viz ikona „fa-times“).
záznam je skrytý v seznamu a nebude detekován pravidlem pro čištění pole znovu.
budoucnost.

Zobrazte vyhozené záznamy pomocí filtru „Vyhozeno“ v :ref:`vyhledávacím poli
<hledání/filtry>“.

..._vyčištění dat/pravidlo pro vyčištění polí:

Pravidla pro čištění hřišť
--------------------

Pravidla pro čištění a formátování pole stanovují podmínky pro čištění a formátování pole.

Tyto pravidla lze pro každý model v databázi nakonfigurovat s různými úrovněmi
Specifika. Pro začátek přejděte na: „Aplikace pro čištění dat --> Konfigurace -->
Čištění pole.

..tip:
Pravidla pro čištění pole se spouští každý den jednou, výchozím nastavením je součástí plánované akce cron
(*Čistění dat: Čisté záznamy*) Nicméně každá pravidla může být ručně spuštěna pomocí příkazu
<vyčištění dat/spuštění pravidla vyčistění pole> kdykoli.

Výchozí pravidlo „Kontakt“ slouží k formátování a vyčištění záznamů v aplikaci „Kontakty“.
Vyberte záznam „Kontakt“ k úpravám nebo vyberte tlačítko „Nový“ pro vytvoření
nový pravidlo.

Na formuláři pro čištění pole nejprve vyberte model, na který se tato pravidla vztahují. Vybrat
model aktualizuje název pravidla na vybraný model.

Dále si vytvořte alespoň jednu pravidla kliknutím na tlačítko „Přidat řádek“ v sekci „Pravidla“.
část.

Při tom se objeví okno „Vytvořit pravidla“ s následujícími poli:
konfigurovat

- Vyberte pole, které chcete vyčistit, ze seznamu polí ve vašem modelu a přiřaďte jej k akci.
- Vyberte jednu z následujících možností:

  - „Odstraňte mezeru“ odhalí pole „Odstraňte mezeru“, aby bylo možné vybrat „Všechny prostory“.
nebo možností „Přebytečné mezery“ (Leading, Trailing a Successive Spaces).
se považuje za zbytečné.

...... příklad::
Kontaktní jméno „Dr. John Doe“ lze formátovat následujícím způsobem:
možnosti:

        - :guilabel:`Všechny prostory“: „Dr. John Doe“
        - :guilabel:`Přebytečné prostory“: „Dr. John Doe“

  - Pole „Typ případu“ (Case) se zobrazí pole „První případ“ (First Case) k výběru.
Dopisy do velkých písmen, nebo do malých písmen.

...... příklad::
Název příležitosti/šance „Lumber Inc., Lorraine Douglas“ lze formátovat následovně
:guilabel:`Možnosti případu`:

       - :guilabel:`První písmena velkými písmeny“: „Dřevařská společnost, Lorraine Douglasová“
       - :guilabel:Všechny velké písmena: „DŘEVO, LORRAINE DOUGLAS“
       - :guilabel:`Všechny malé písmena“: „Dřevařská společnost, Lorraine Douglasová“

  - :guilabel:`Formát telefonního čísla“ převádí telefonní číslo na mezinárodní formát.

...... příklad::
       - Belgie: 061928374: ikonka: fa-long-arrow-right +32 61 92 83 74
       - Spojené státy: „800 555-0101“:icon:`fa-long-arrow-right` „+1 800-555-0101“

  - :guilabel:`Scrap HTML“ převádí :abbr:`HTML (Hypertextový značkovací jazyk)“ na čistý text.

...... příklad::

... kódový blok:: html
:caption: HTML text

<h1>Jan Novák</h1>
<p>Lorem ipsum dolor sit amet.</p>

... kódový blok:: text
:caption: Text bez formátování

**Jan Novák**Lorem ipsum dolor sit amet [1].

Jakmile si vyberete pole a akci, klikněte na tlačítko „Uložit“ v dialogovém okně „Vytvořit pravidla“.
pop-up okno.

Poté vyberte režim čištění:

- :guilabel:„Manuální“: vyžaduje ruční čištění každého detekovaného pole a umožňuje
:guilabel:`Upozornit uživatele“ pole.
- :guilabel:`Automaticky“: automaticky vyčistí pole bez upozornění uživatele.

Pokud je konfigurace pravidla dokončena, buďte zavřete formulář pro pravidlo nebo spusťte pravidlo ručně:
„Přidat pole k čištění“ a okamžitě získat pole, která chcete vyčistit.

..._vyčistit data/spustit pravidlo pro čištění polí:

Spusťte ručně pravidlo pro čištění pole
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chcete-li ručně spustit konkrétní pravidlo čištění pole v kterékoliv časové fázi, přejděte na:
Aplikace pro čištění obrazovky --> Konfigurace --> Čisticí pole“, a vyberte pravidlo, které chcete spustit.

Poté v pravidle vyberte tlačítko „Čistit“ na horním levé rohu.
Ikona „fa-bars“ v tlačítku „Chytré tlačítko“ zobrazuje počet zachycených záznamů.

Klikněte na tlačítko „Záznamy“ v horní liště.
<čištění dat/čištění polí>.

.. _úprava dat/souboru/sloučení/akce manažera:

Spojit akční manažer
====================

Nástroj pro správu akcí Merge umožňuje zapínat nebo vypínat akci Merge dostupnou v nabídce Actions.
pro modely v databázi.

Zapněte režim vývojáře a přejděte do aplikace „Čištění dat“ – „Konfigurace“.
Spojit akční manažer“.

Modelové příklady jsou uvedeny v následujících sloupcích:

- :guilabel:`Model`: technický název modelu.
- :guilabel:`Popis modelu“: zobrazovaný název modelu.
- :guilabel:`Typ modelu“: zda je model typu *Objekt základní třídy* nebo *Vlastní objekt*.
- :guilabel:`Přechodný model“: tento model zpracovává dočasná data, která nemusí být uložena
dlouhodobě v databázi.
- :guilabel:`Může být sloučeno“: umožňuje akci „Spojení“.

Chcete-li zobrazit modely povolené výchozím nastavením, použijte vyhledávací lištu k filtrování
modelů, které lze sloučit.

.. viz též:
:doc:`../základy/kontakty/sloučení“
