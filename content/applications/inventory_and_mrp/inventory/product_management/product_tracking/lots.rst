===========
Číslo losu
===========

.. |PO| nahradit za: abbr: PO (příkaz k nákupu)
.. |SO| nahradit za: :abbr:`SO (objednávka na prodej)`
.. |DO| nahradit:: :abbr:`DO (Dodací příkaz)`
.. |seznam| nahradit za: :icon:`fa-list` :guilabel:`(seznam)`

*Lot* je jednou ze dvou možností, jak v Odoo identifikovat a sledovat produkty. Obvykle představuje
Konkrétní dodávka produktů, které byly přijaty, skladovány, odeslány nebo vyráběny vlastními silami.

Výrobci přiřazují čísla šarží skupin výrobků s podobnými vlastnostmi, což usnadňuje
stoprocentní sledovatelnost od konce k začátku jejich životního cyklu.

Lot je užitečný pro správu velkého množství vyrobených nebo přijatých výrobků a pomáhá
sledování položek zpět k jejich skupině, zejména při vzpomínkách nebo expiraci
<datum expirace>.

.. viz též:
:doc:`sériová čísla“

Zapněte položky a sériové čísla
============================

Pro sledování produktů pomocí šarží a sériových čísel zapněte funkci „Šarže a sériové číslo“.
:menu:„Aplikace inventář --> Konfigurace --> Nastavení“, posuňte se dolů na
V sekci „Sledovatelnost“ a zaškrtněte políčko vedle „Šarže a sériové číslo“.
Poté klikněte na tlačítko „Uložit“.

.. viz též:
   - :doc:`Sledování dat expirace <expiration_dates>`
   - :ref:`Tisk GS1 čárových kódů pro sériové a kontrolní číslo <barcode/operations/gs1-lots>`

.. obrázek: lots/enabled-lots-setting.png
:align:center
:alt:V nastavení skladu se nachází funkce pro sériová čísla a šarže.

... _Inventar/Verwaltung/Tracking von Produkten nach Losen:

Kus po kuse
=============

Jakmile je zapnuta funkce „Sériové číslo a šarže“, konfigurujte jednotlivé produkty tak, aby
je možné sledovat pomocí lotů. Pro toto klikněte na: „Nástroje --> Skladové zásoby --> Produkty“,
Vyberte produkt, který chcete nakonfigurovat.

V sekci „Sklad“ klikněte na záložku „Sledovatelnost“.
Vyberte možnost „Počet kusů“ v poli „Sledování“. Nyní můžete nové nebo existující počty kusů
čísla lze přiřadit k nově dodaným nebo vyrobeným dávkám tohoto produktu.

.. viz též:
:doc:`datum vypršení platnosti“

.. důležité::
Pokud je produkt na skladě před aktivací sledování podle číselného nebo sériového čísla, zobrazí se varování.
zobrazí se zpráva. Použijte funkci „přidělení inventárního čísla“ (reassign) k přiřazení čísel položek existujícím
zboží skladem.

.. obrázek: lots/tracking-product-form.png
:align:center
:alt:Aktivovali jsme funkci sledování položek na produktovém formuláři.

Přiřaďte si místa pro příjem a odesílání
======================================

Přiřaďte nové číslo skladu k položkám zboží, které přišly do skladu.
přijaté zboží, při odeslání pak „výstupní zboží“.
<Inventar/Produktverwaltung/Lieferungen zuweisen>, wählen Sie Produkte mit bestimmten Losnummern aus
přepravní objednávkový list.

...Inventarizace, správa produktů, přiřazení položek:

Na účtence
-----------

Přiřazení nových nebo stávajících čísel skladových položek k příchozím zásilkám lze provést přímo na fakturách.

Nejprve přejděte do aplikace Purchase a vytvořte a potvrďte objednávku.
<https://www.youtube.com/watch?v=o_uI718P1Dc>_ a |PO| pro produkty sledované podle čísla šarže. Pak
Klikněte na tlačítko „Potvrzení“ v horní části stránky, abyste se dostali do
formulář skladového potvrzení.

.. poznámka::
Alternativně můžete otevřít existující fakturu přes aplikaci „Sklad“ v nabídce.
kliknutím na kartu „Faktury“ a výběrem požadované faktury.

.. důležité::
Pokud k přiřazení čísla losu stisknete tlačítko „Zkontrolovat“, zobrazí se chyba, která ukazuje, že
číslo losování musí být přiděleno před ověřením příjmu.

.... obrázek: lots/user-error.png
:align:center
:alt:Přidat okno s chybovou hláškou při zadávání čísla šarže.

V příjmovém formuláři na řádku produktu v záložce „Provoz“ vyberte ikonu
Vpravo od produktu, který je sledován podle čísla šarže.

.. obrázek: lots/list-icon.png
:align:center
:alt:Zobrazte ikonu seznamu bodů na produktové lince.

Tím se otevře okno „Otevřít pohyb zásob“, kde je možné vybrat položku „Lot/sériové číslo“.
Přiřazení čísel a množství.

Dva způsoby přiřazení čísla šarže: ručně a importem.

Manuální přiřazení
~~~~~~~~~~~~~~~~~

Chcete-li ručně přiřadit číslo šarže, klikněte na tlačítko „Přidat řádek“. Zadejte „Číslo šarže“ nebo „Sériové číslo“.
Číslo obchodu, kde je položka k dispozici, množství a cílové místo.
Balíček, pokud existuje.

.. poznámka::
Pokud chcete přiřadit více čísel nebo skladovat na více místech, klikněte na tlačítko „Přidat řádek“
Vyplňte nový číselný kód „Lot/Serial“ pro další množství. Opakujte, dokud nebude celkové množství v
:guilabel:`Množství“ slouží jako „Požadavky“.

.. obrázek: lots/assign-lots-popup.png
:align:center
:alt: Přiřadit číslo pozemku do podrobné operace.

Dodávky větších objemů
~~~~~~~~~~~

V okně „Přesun otevřeného skladu“ klikněte na „Import sériových čísel / šarží“, pak vložte
v poli „Sériové číslo“.

.. obrázek: tabulka-s-dostatkem-nebo-nedostatkem-excel.png
:align:center
:alt:Seznam čísel vylosovaných na listu Excelu.

Seznam čísel losů zkopírovaný do tabulek na Google.

.. obrázek: bulk_sn.png
:align:center
:alt: Čísla položek zkopírována do řádku číslo položky.

Čísla losů vložená do pole „Losy/Sériová čísla“ v okně s názvem „Dodávky“.

Zatrhněte políčko „Udržet současné řádky“ a vytvořte tak další čísla losů.
Okno „Otevřeno: Přesuny skladu“. Chcete-li nahradit čísla položek v seznamu, nechte
Zatrhněte možnost „Udržet současné řádky“.

V neposlední řadě klikněte na tlačítko „Vytvořit“.

Jakmile jsou všechny množství produktů přiřazeny k jednomu číslu šarže, klikněte na tlačítko „Uložit“ pro uzavření
přepínací okno. Pak klikněte na tlačítko „Zkontrolovat“ v příjmovém formuláři.

.. viz též:
:ref:`Zpráva o stopách pro čísla šarží <sklad/správa produktů/stopa šarže>`

...Inventar/Produktverwaltung/Zuteilen von Losen an Lieferanten:

Na dodacích objednávkách
------------------

Odoo umožňuje specifikovat, které čísla šarže pro konkrétní produkt jsou určena k expedici
na dodací listu.

Nejprve vytvořte nebo vyberte existující citaci z aplikace Sales. Poté
potvrzujícím |SO| se zobrazí tlačítko „Doručení“. Po kliknutí
Klikněte na tlačítko „Dodání“ v seznamu chytrých tlačítek, abyste zobrazili fakturu o převzetí skladového zásobování pro konkrétní |SO|.

.. poznámka::
Alternativně se můžete dostat k objednávkám dodání zadáním aplikace „Sklad“ a
kliknutím na kartu kanbanu Dodací objednávky.

Kliknutím na tlačítko „Dodání“ se otevře formulář objednávky dodání, kde jsou čísla
jsou vybrány k dodání. V záložce „Provoz“ klikněte na ikonu seznamu vedle
produkt, který je sledován pomocí čísla šarže. Po kliknutí na ikonu se zobrazí:guilabel:`Skladové zásoby
pop-up okno.

V okně prohlížeče se zobrazí vybrané číslo a místo uložení.
sloupec „Vybrat z“, kde je celé množství vybrané ze specifické
losování (pokud je v daném balení dostatek zásob).

Pokud je v daném skladě nedostatek zásob nebo pokud jsou k dispozici pouze částečné množství položek
musí být odebrány z více položek, změňte přímo :guilabel:`Množství`.

.. poznámka::
Automaticky vybraný sklad pro expediční objednávky se liší podle zvoleného odběrného místa.
strategie (:zkratka: „FIFO (první do skladu, první ven)“, „LIFO (poslední do skladu, první ven)“ nebo
(První expirace, první vypovězení) a závisí také na objednaném množství a zda je zakázka
skladové množství je dostatečné k uspokojení objednávky.

.. viz též:
:doc:`../dodavatelé/strategie-vykládání“

Opakujte výše uvedené kroky, dokud nevyberete dost balíčků, aby se vyhovělo požadavku a poté
Stiskněte tlačítko „Uložit“ pro zavření okna. Nakonec stiskněte tlačítko „Potvrdit“.
Doručit zboží.

.. obrázek: lots/pick-from-lots.png
:align:center
:alt:Pop-up okno s číslem položky na objednávce.

.. viz též:
:ref:`Zpráva o stopách pro čísla šarží <sklad/správa produktů/stopa šarže>`

Správa parkovacích míst
==============

Spravujte a zobrazujte stávající čísla šarží produktů v panelu „Číslo šarže“ pomocí
Přejít na:menu:Inventář aplikace --> Zboží --> Sériové číslo.

Výchozí nastavení je takové, že čísla losů jsou seskupena podle produktu a vybráním položky v rozevíracím seznamu pro každý produkt
Zobrazuje stávající čísla losů. Vyberte číslo losu, abyste mohli:
<inventar/produktverwaltung/bearbeiten-los>“ verknüpft mit dem Los. Losnummern können auch als :ref:`erstellt
„Vytvořit nový lot“ z této stránky kliknutím na „Nový“.
tlačítko.

.. obrázek: loty_dashboard.png
:align:center
:alt:Zobrazit panel „Číslo sériového čísla“.

Zobrazte čísla šarží, seskupená podle produktů, na panelu **Číslo šarže/sériové číslo**.

.. inventář/správa produktů/upravit položku:

Změnit los
----------

Kliknutím na mnoho políček z panelu „Číslo sériové šarže“ se objeví samostatná stránka, kde
Může být poskytnuta další informace o položce.

.. tip::
Odoo automaticky vytváří nový :guilabel:`Číslo šarže/losování`, který bude následovat nejnovější
číslo. Je však možné jej upravit kliknutím na řádek pod nadpisem „Číslo šarže“.
pole a změnit generované číslo na jakékoliv požadované.

V poli číslo stavebního pozemku lze měnit následující údaje:

- :guilabel:`Číslo šarže/sériové číslo“: změňte číslo šarže spojené s produktem.
- :guilabel:`Vnitřní referenční číslo“: zaznamenává alternativní číslo šarže používané ve skladu
která se liší od použitého dodavatelem výrobce.
- :guilabel:`Společnost“: specifikujte společnost, kde je k dispozici číslo šarže.
- :guilabel:`Popis`: do pole s textem zadejte další podrobnosti o položce nebo čísle sériovém.

.. důležité::
Na stávajících položkách nelze v poli „Produkt“ a „Množství na skladě“ vyplnit hodnotu.
upraveno, protože čísla losů jsou propojena s již existujícími pohyby zásob.

.. obrázek: loty/číslo_losu.png
:align:center
:alt:Zobrazit formulář pro číslo šarže.

.. viz též:
:doc:`Datum vypršení platnosti pro jednotlivé položky <expiration_dates>`

Přidej vlastnost
~~~~~~~~~~~~

Pro přidání vlastních polí k jednotlivým položkám pro lepší sledovatelnost existují dvě metody přidávání vlastností
na pozemkové knize:

#Klikněte na ikonu „fa-cog“ v levém horním rohu stránky a poté vyberte
:icon:`fa-cogs` :guilabel:`Přidat vlastnosti“ z nabídky.
#Klikněte na tlačítko „Přidat vlastnost“ pod stávajícími poli.

Název a konfiguraci nového pole nastavte v sekci </applications/essentials/property_fields>.
Vyberte dokončený stav a zadejte hodnotu nového pole.

.. příklad::
Do nové vlastnosti „Druh dřeva“ se zadá hodnota „Třešeň“.

.. obrázek: lots/add-properties.png
:align:center
:alt:Zobrazit tlačítko „Přidat vlastnosti“ na formuláři pro číslo pozemku.

.. viz též:
:doc:`Konfigurace vlastních vlastností </aplikace/základní/vlastnosti_složek>`

... vytvoření nové šarže:

Rezervovat číslo skladového místa pro produkt
--------------------------------

Pro vytvoření čísla výrobku začněte na: „Skladové aplikace -> Produkty
Vyberte „Číslo šarže“ a klikněte na „Nový“.

.. důležité::
Vytvořením čísla šarže si rezervujete produkt, ale **nepřiřazujete jej**. Přiřadit číslo šarže
čísla, viz část o :ref:`přidělování čísel na fakturách
<Inventar/Produktverwaltung/Zuordnen von Losen>.

.. tip::
Zatímco Odoo automaticky vytváří nové číslo „Lot/Serial“ podle nejnovějších
číslo, které lze upravit a změnit na jakékoliv požadované číslo kliknutím na řádek pod
:guilabel:`Číslo šarže“ pole na formuláři pro lotek a změnou generovaného čísla.

Jakmile je nové číslo sériového štítku vygenerováno, klikněte na prázdné pole vedle
Klikněte na tlačítko „Produkt“ pro zobrazení rozbalovací nabídky. V této nabídce vyberte produkt, ke kterému chcete přidat nový
bude přiděleno.

.. příklad::
Pro výrobek „Šuplík černý“ je vytvořená sériová čísla „000001“.

.... obrázek: lots/nový-pozice-číslo.png
:align:center
:alt: Nový formulář pro vytváření nových čísel losů s přiřazeným produktem.

Po vytvoření nového čísla šarže, uložení a přiřazení k požadovanému produktu se zobrazí
je uložena jako stávající číslo položky spojené s produktem a lze ji vybrat při :ref:`přiřazování
čísla šarží produktům na faktuře (Inventář/Správa produktů/Přidělit číslo šarže) nebo při vytváření
Inventarizační rozdíl.

.. příklad::
Po vytvoření čísla položky se zobrazí možnost „Černá“ s hodnotou „000001“.
čísla skladových položek na stránce „Změna zásob“.

....... obrázek: lots/inventory-adjustment.png
:align:center
:alt:Ukažte, jak přiřadit čísla skladových položek na stránce Změna zásob.

Spravujte různé typy operací
==========================================

Nové šarže lze vytvářet pouze při příjmu zboží a existující čísla šarží nelze měnit.
je možné ji používat. Pro prodejní objednávky lze využít jen stávající čísla položek a nová nemohou být vytvořena
na dodací listině.

Chcete-li změnit schopnost používat nové (nebo stávající) čísla losů na jakémkoli typu operace, přejděte do
:menu „Inventarizační aplikace“ -> „Konfigurace“ -> „Druhy operací“ a vyberte požadovanou.
druh operace.

V poli „Typ operace“ zaškrtněte pole „Sériové číslo“.
Zatrhněte políčko „Vytvořit nové číslo“ a umožněte vytváření nových čísel během této operace.
Vyberte možnost „Použít existující“ (guilabel:Use Existing ones), pokud lze vybrat pouze stávající čísla.

.. obrázek: lots/operation-type-form.png
:align:center
:alt:Povolení sledovatelnosti operace typu v formuláři.

.. tip::
Pro přesuny mezi sklady zboží sledovaného podle šarží může být užitečné zapnout
:guilabel:"Použít stávající čísla skladových záznamů"

.. evidence/správa produktů/sledovatelnost šarží:

Zobrazte položky na dodacích lístcích
==============================

Při prodeji zboží označeného šaržemi je možné do dodacího listu uvést i čísla šarží.
dodané zákazníkům. To může být užitečné pro zákazníky v případě, kdy jsou potřeba čísla losů.
například podáním žádosti o vrácení zboží nebo opravu nebo registrací výrobku.

Zahrnout čísla položek na dodacích listech. Otevřete aplikaci „Sklad“ a přejděte do
:menu:Nastavení --> Nastavení. Vyhledejte sekci :guilabel:Sledovatelnost
Zatrhněte políčko „Zobrazit čísla a sériová čísla na fakturách“ a klikněte
:guilabel:`Uložit“.

Po zapnutí nastavení „Zobrazit čísla a sériová čísla na fakturách“ se zobrazují
Jsou uvedeny na dodacích lístcích pro produkty sledované podle šarží, jakmile je objednávka přijata.

Chcete-li zobrazit čísla položek na fakturách a dodacích listech, přejděte do
Aplikaci „Inventář“ otevřete kliknutím na „Příjemky“ a vyberte příjemku obsahující
produkt sledovaný pomocí čísla šarže.

Pro zobrazení čísla položky produktů v objednávce ujistěte se, že je na kartě „Operace“
je vybrán, pak klikněte na tlačítko „Nastavení“ („Adjust“) vedle
tabulka. Zajistěte si zaškrtnutí položky „Sériové číslo“, což způsobí
Sloupec „Sériové číslo“ se objeví. Sériové číslo (čísla) každého produktu, který je součástí
V této sloupci jsou zobrazeny objednávky.

Když je objednávka připravena k zpracování, klikněte na tlačítko „Potvrdit“ pro potvrzení dodání a přidání
informace o produktu na dodací lístek.

V horní části řádku příkazů klikněte na tlačítko „Akce“ (viz ikona „fa-cog“) a vyberte
:guilabel:`Tisk --> Přepravní list“. Poté je přepravní list stáhnut a otevřen.
pomocí prohlížeče nebo správce souborů zařízení. Čísla šarží jsou uvedena vedle příslušných produktů
ve sloupci „Číslo šarže“.

.. obrázek: lots/dodací lístek.png
:alt:Část objednávkového lístku se seznamem položek, ukazující produkt a jeho sériové číslo.

Sledovatelnost
============

Výrobci a společnosti mohou odkazovat na zprávy o stopách, aby viděli celý životní cyklus výrobku.
produkt: odkud pochází, kdy dorazil, kde byl uskladněn, komu šel (a kdy).

Pro zobrazení celé trasovatelnosti produktu nebo skupiny podle šarží přejděte do aplikace Inventura.
--> Produkty --> Sériové číslo“. To zobrazí: „Sériová čísla“
přístrojová deska.

Zde budou výrobky s přidělenými čísly šarží zobrazovány automaticky a lze je rozbalit.
ukázat čísla losů, které jsou těmto produktům přiřazena.

Pro seskupení podle skupin začněte odstraněním filtrů v liště „Hledat…“. Pak klikněte na
:icon:`fa-caret-down` :guilabel:`(caret down)` ikonu pro otevření nabídky filtrů
Možnosti „Skupina“ a „Oblíbené“. V sekci „Skupiny“
Vyberte možnost „Přidat vlastní skupinu“ a zvolte „Číslo sériového čísla“.
kliknutím na tlačítko „Přidat do košíku“.

Tímto způsobem se všechny záznamy na stránce přeorganizují tak, aby byly zobrazeny všechny existující čísla a sériová čísla.
a může být rozšířen, aby zobrazoval všechny produkty s tímto přiděleným číslem.

.. obrázek: lots/group-by-number.png
:align:center
:alt: Zpráva o sledovatelnosti čísla a sériového čísla.

Zpráva o stoprocentní stopě
-------------------

Pro zobrazení celého reportu o pohybu zásob pro konkrétní číslo položky vyberte řádek s číslem položky.
Dashboard „Sériové číslo“. Na formuláři sériového čísla klikněte na „Stopa“.
smart tlačítko.

.. obrázek: lots/traceability-report.png
:align:center
:alt:Zobrazte stromový report pro zboží, které obsahuje pohyby zásob.

.. viz též:
:doc:`/produktove-sledovani`
