==============================
Upravte zásoby s čárovými kódy
==============================

„Inventarizace“ nebo „inventarizační audit“ je proces ověřování skutečného stavu zásob.
výrobků v souladu s množstvím zaznamenaným v databázi. Pravidelné kontroly zajišťují přesné zásoby
evidence záznamů, zabránění rozdílům v zásobách a udržení efektivních provozů. V prostředí skladu
Obvykle jsou inventury přidělovány zaměstnancům, kteří pak chodí do určených míst a skenují
kódy výrobku a upravit množství dle potřeby.

Inventarizační úpravy lze provést pomocí aplikace **Čárový kód** s kompatibilním
skener nebo mobilní aplikaci Odoo.

.. poznámka::
Pro seznam kompatibilních s Odoo skenerů čárových kódů a dalšího hardwaru pro **Sklad**
a aplikace Barcode, viz stránka Odoo Inventory • Hardware.
<https://www.odoo.com/app/inventory-hardware>.

.. viz též:
:doc:`../sklady-a-skladovani/inventarizace/poctu-produktu`

.. tip::
Aplikace **Barcode** společnosti Odoo poskytuje ukázkové kódy s čárovými kódy, které lze použít ke zkoumání funkcí aplikace.
aplikaci. Tyto lístky můžete používat k testování a vytisknout si je z domovské obrazovky aplikace.

Chcete-li se dostat k tomuto ukázkovému datu, přejděte na aplikaci čárových kódů a klikněte na
v horní liště nad skenerem.

.... obrázek: upravit/upravit-čárový kód-skladové listy.png
:alt:Při spuštění aplikace se objeví okno s informacemi o demo datových souborech.

Přiřazování záznamů o inventarizaci
==========================

Před provedením inventurního počtu mohou manažeři :ref:`přidělit <inventarizaci/plánování-počtů> počítání
úkoly zaměstnancům. To lze provést prostřednictvím:menuselection:`Skladové aplikace --> Objednávky -->
Fyzický inventář“ vybírá konkrétní lokality a produkty k počítání a přiřazuje
:guilabel:`Uživatel“ jim přiřadí. Jakmile budou uživatelé přiřazeni, uvidí počet nevyřízených úkolů, když otevřou
Aplikace **Čárový kód**

Pro zobrazení požadovaného počtu skladových položek přejděte na panel „Aplikace čárových kódů“. Pokud je
byl požadován sečet, počet produktů k sečtení je uveden na :guilabel:`Seznam inventury
tlačítko „Počet“.

.. obrázek: úpravy/přidělené počty.png
:alt:Dashboard s přiděleným počtem.

Konfigurace
=============

Před provedením inventarizace pomocí aplikace **Barcode** musí být aplikace
nainstalován a nakonfigurován. Přejděte na:
Nastavení“ a posuňte se do části „Čárový kód“. Zaškrtněte políčko vedle
:guilabel:`Čtečka čárových kódů“ a klikněte na „Uložit“, abyste uložili změny. Pokud je potřeba, klikněte
Vyberte možnost „Potvrdit“ v okně s upozorněním.

.. nebezpečí::
Pro zapnutí funkce čárového kódu je nutné nainstalovat aplikaci Barcode.
nová aplikace na databázi One-App-Free spouští patnáctidenní zkušební dobu. Na konci zkušební doby
Pokud nebude do databáze přidán placený účet, uživatelé ho již nikdy neuvidí.

Po uložení se zobrazí nové rozbalovací nabídka pod volbou :guilabel:`Skenování čárových kódů`, označená
„Název produktu“, kde buď „Výchozí název“ nebo
Můžete vybrat „Výchozí GS1 Nomenklatura“. Každá z možností určuje, jak
Skenery dekódují čárové kódy v Odoo.

Zaúčtovat produkty pomocí čárových kódů a zajistit, aby byly nastaveny čárové kódy pro produkty i skladovací prostory.
prvotně v Odoo. Podrobné pokyny najdete zde: :ref:`Nastavení štítků produktů
<výčet/čárový kód/sada čárových kódů>.

.. obrázek: nastavení čárového kódu
:alt:V nastavení aplikace Sklad zapnul funkci čárového kódu.

.. inventarizační číslo, čárový kód a počet:

Provádění inventarizace
=============================

Pro provedení inventarizační úpravy nejprve přejděte do aplikace „Čárový kód“. Pokud je přiřazen
seznamy existují, stiskněte tlačítko „Inventarizační seznam“ a zobrazí se nevyřízené úkoly.

.. obrázek: upravit/upravit-snímač-čárových kódů.png
:alt: Obsahuje obrazovku aplikace s čárovým kódem a skenerem.

Přejděte k určenému skladovacímu místu a naskenujte kód umístění.

.. tip::
Pokud funkce skladu s více umístěními není v databázi povolena, zdrojová lokalita
nemusí být skenován. Namísto toho naskenujte čárový kód produktu a zahajte úpravu zásob.

Tímto způsobem se zobrazí umístění a všechny produkty, které jsou zde uloženy.
Každý produkt upravit počet.

.. poznámka::
Pokud uživateli nebyly přiřazeny žádné počty, pak se použije metoda :ref:`Počítání celých lokalit
funkce „<inventory/barcode/count-location>“ je **nepovolena**, žádné produkty se po ní nemohou objevit.
je skenován čárový kód umístění.

Pokud je nutné, upravte množství ručně klepnutím na ikonu „Kulička“ (Editovat).
Tím se otevře nové okno s klávesnicí. Upravte číslo v řádku :guilabel:`Quantity`.
změnit množství. Kromě toho lze kliknout na tlačítka „+1“ a „-1“, aby
Přidávat nebo odečítat množství produktu a klávesy pro přidávání množství lze použít také k odečítání množství.

.. příklad::
V níže uvedeném seznamu položek byl skenován zdrojový údaj „WH/Sklad/Police 1“, což bylo přiřazeno
místo. Poté byl naskenován čárový kód produktu „Stojan na psací stůl s obrazovkou“ [FURN_7888].
třikrát, zvyšujeme jednotky v nastavení. K tomu můžete přidat další produkty
upravit pomocí skenování čárových kódů u konkrétních produktů.

...... obrázek: upravit/upravit-čárový kód inventárního klienta - akce.png
:alt:Stránka s kódem čárového kódu a akcí pro úpravu zásob.

... inventární číslo, štítek, počet kusů na místě:

Sčítej celé lokality
----------------------

Funkce „Sčítat celé lokalitě“ přiřazuje uživatele k počtu všech produktů v
umístění, jakmile se skenují čárové kódy pro tuto polohu. To umožňuje snadnější počítání kol obsluhy
přiřazením celé lokace uživateli přiřazením jednoho počtu produktů během cyklických sčítání.
Uživatelé mohou zkontrolovat správné počty zásob, zjistit, jestli jsou produkty, které by tam být měly,
nebo objeví produkty nesprávně skladované v daném místě.

Chcete-li tuto funkci aktivovat, přejděte na: „Aplikace Inventář --> Konfigurace --> Nastavení“.
a přejděte na část „Čárový kód“. Zaškrtněte políčko „Spočítat celkový počet lokalit“.
Poté klikněte na tlačítko „Uložit“.

.. důležité::
Toto nastavení je viditelné pouze tehdy, pokud je zaškrtnutá políčka „Uložiště“.

Pro provedení inventury celé lokalitě přejděte na:
Inventura. Skenujte čárový kód požadované položky. Aplikace pak zobrazí všechny přiřazené produkty
Toto umístění. :ref:`Pokračujte v počítání <inventory/barcode/perform-count> podle pokynů.“

Zobrazte počet k vypočítání
----------------------

Při inventarizaci je zobrazeno výchozí množství produktů.
poskytnout uživateli základní referenční bod pro provádění počítání.
Pokud uživatelé spoléhají na tento počet namísto provedení nového počtu, může být skryta.

Přejděte na:menu: „Skladová aplikace -> Konfigurace -> Nastavení“.
V části „Čárový kód“ vyberte možnost „Zobrazit množství“, pak
:guilabel:`Uložit“.

.. obrázek: upravit/ukázat-množství-pro-počítání-zapnuté.png
:alt:Inventarizační sečet bez funkce zobrazování skutečného množství.

Přidat produkty do seznamu skladových zásob ručně
===========================================

Pokud nejsou k dispozici čárové kódy pro umístění nebo produkty, může být aplikace **Barcode** stále použita
provádět inventarizační zápisy.

Pro tento účel přejděte na položku „Barcode app --> Inventory Count“.

Chcete-li ručně přidat produkty do této úpravy, klikněte na bílou tlačítko „Přidat produkt“
dole na obrazovce.

Toto vás přesměruje na novou prázdnou stránku, kde musíte zadat požadovaný produkt, množství a zdroj.
vybráno.

.. obrázek: nastavení/nastaveni-klávesnice.png
:alt:Klávesnice pro přidávání produktů na stránce akce Klientské skladové inventarizace s čárovým kódem.

Nejprve klikněte na řádek „Produkt“ a vyberte produkt, jehož zásoba by měla být
upravit. Poté ručně zadáte množství daného produktu, a to buď změnou čísla „1“ v
:guilabel:`Množství“ řádku nebo kliknutím na tlačítka „+1“ a „-1“, abyste přidali nebo
Odečíst množství produktu. Na klávesnici lze použít i pro přidání množství.

Pod číselnou klávesnicí je řádek s adresou, který by měl být vždy nastaven na „WH/Stock“.
Klikněte na tuto řádku, abyste zobrazili seznam lokalit k výběru. Vyberte
:guilabel:`Zdrojová poloha“ pro tuto korekci zásob.

Klikněte na tlačítko „Potvrdit“ pro potvrzení změn.

Dokončení inventarizace
=============================

Počítej všechny produkty a zkontroluj záznamy, aby byly všechny počítané množství
přesně zadané. Chcete-li dokončit inventarizaci, klikněte na tlačítko „Použít“.

.. tip::
Kód „Validate“ můžete skenovat místo kliknutí na „Apply“.
tlačítko.

Odoo poté přejde na obrazovku „Skenování čárových kódů“ a v horní části se zobrazí malý zelený pruh.
v pravém horním rohu potvrzuje, že se změnila evidence skladových zásob.
