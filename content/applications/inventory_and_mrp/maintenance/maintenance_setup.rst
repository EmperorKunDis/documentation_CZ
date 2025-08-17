=================
Nastavení údržby
=================

.. |MTBF| nahradit za: :abbr:`MTBF (Průměrný čas mezi poruchami)`
.. |MTTR| nahradit::: zkratka: MTTR (průměrná doba k opravě)

Odoo Maintenance pomáhá společnostem plánovat údržbu zařízení, která se používá
ve svých skladech. To pomáhá firmám vyhnout se poruchám a zádrhelům v práci skladu
centra a náklady na mimořádné opravy.

Servisní týmy
=================

Při vytváření požadavků na údržbu lze přiřadit k žádosti tým pro údržbu jako tým
odpovědný za zpracování žádosti.

Pro zobrazení stávajících údržbových týmů přejděte na: „Aplikace pro údržbu --> Konfigurace
--> Týmy údržby.

Z výsledného seznamu týmů „Teams“ je zobrazen seznam všech existujících týmů (pokud nějaké jsou), s
týmové jméno, týmová členka a společnost uvedené v sloupcích.
výchozím nastavení.

.. obrázek: maintenance_setup/maintenance-setup-teams-list.png
:align:center
:alt: Seznam týmů na stránce Týmy na údržbě.

Chcete-li přidat nový tým, klikněte na „Nový“. Tím se do konce seznamu týmů vloží prázdná řádka.
V prázdném poli pod sloupcem „Tým“ zadejte název nového
tým údržby.

V poli „Člen týmu“ klikněte na pole, abyste zobrazili seznam existujících možností.
uživatelů v databázi. Vyberte, které uživatele by měli být členy nového týmu údržby.

Klikněte na tlačítko „Hledat více…“ a otevřete okno „Hledání členů týmu“.
pro uživatele, kteří nejsou zobrazeni v prvním rolovacím seznamu.

.. obrázek: maintenance_setup/maintenance-setup-search-team-members.png
:align:center
:alt: Hledat: Pop-up okno pro týmové členy.

V poli „Společnost“ v případě více společností klikněte na vyskakovací nabídku
Vyberte společnost v databázi, ke které nový tým údržby patří.

Jakmile je hotovo, klikněte na tlačítko „Uložit“ a uložte změny.

..tip:
Členové údržbových týmů jsou také označováni jako technici.
zobrazením kalendáře údržby.

Přejděte do sekce „Údržba aplikace“ -> „Údržba“ -> „Kalendář údržby“, a klikněte
na již existující požadavek na údržbu. Z výsledného okénka vyhledejte „Technika“.
pole. Jméno uvedené v poli je člen týmu a je uživatelem odpovědným za danou oblast.
zvláštní požadavek.

.... obrázek:: maintenance_setup/maintenance-setup-popover-technician.png
:srovnání: do středu
:alt:Pop-up okno s žádostí o údržbu, kde je zobrazeno pole pro technika.

Na pravé straně stránky je sloupec s kalendářem, který je zmenšený.
dnešní datum a seznam „Technik“ nebo „Člen týmu“, který zobrazuje všechny techniky (či členy týmu).
s aktuálně otevřenými žádostmi.

Vybavení
=========

V Odoo *Údržba* se zařízením rozumí stroje a nástroje používané v rámci skladového provozu.
centrech. Vybavení může zahrnovat technologie jako počítače nebo tablety, elektrické nářadí, stroje používané
pro výrobu a další.

Kategorie vybavení
--------------------

Každý kus vybavení patří do nějaké *kategorie vybavení*. Než přidáte nové vybavení, ujistěte se
aby byla vytvořena příslušná kategorie vybavení.

Pro vytvoření nové kategorie vybavení přejděte na: `Maintenance app --> Konfigurace
Vyberte kategorii vybavení, například „Kategorie vybavení“, a klikněte na tlačítko „Nový“. To vám umožní otevřít prázdnou kategorii vybavení.
forma.

.. obrázek: maintenance_setup/maintenance-setup-category-form.png
:align:center
:alt:Formulář kategorie vybavení s různými informacemi vyplněnými.

Na prázdném formuláři přidejte do pole „Kategorie“ název kategorie.

V poli „Zodpovědná osoba“ přiřaďte uživatele, který bude za vybavení v této
kategorie, pokud je třeba. Výchozí uživatel, který vytváří kategorii, je vybrán jako
Výchozí hodnota je „Zodpovědná osoba“.

V případě více společností klikněte na rozbalovací nabídku v poli „Společnost“ a
vyberte společnost v databázi, ke které patří vybavení této kategorie.

V poli „E-mailová adresa aliasu“ přiřaďte k této kategorii e-mailový alias, pokud je potřeba.

Do pole „Komentáře“ zadejte komentář nebo poznámku pro interní uživatele.
v případě potřeby.

.. poznámka::
Jakmile je vytvořena nová kategorie vybavení, všechno vybavení patřící do této kategorie, stejně jako
Všechny otevřené nebo již uzavřené požadavky na údržbu jsou dostupné z kategorie zařízení.

Přejděte na: `Hlavní aplikace --> Konfigurace --> Kategorie zařízení`
Vyberte kategorii, abyste zobrazili. Najděte „Zařízení“ a „Údržba“.
tlačítka v horní části formuláře.

.... obrázek: maintenance_setup/maintenance-setup-smart-buttons.png
:srovnání: do středu
:alt: Tlačítka pro údržbu a servis na kategorii zařízení vytvářejí formulář.

Klikněte na tlačítko „Vybavení“ a zobrazí se vám všechno vybavení patřící do této kategorie.
Klikněte na tlačítko „Údržba“ v seznamu chytrých tlačítek, abyste zobrazili jakoukoli minulost nebo aktuálně otevřené údržby.
požadavky.

Stroje a nástroje
----------------

Pro přidání nového vybavení přejděte na: „Údržba aplikace --> Vybavení --> Stroje a
Nástroje“ a klikněte na „Nový“. To otevře prázdnou formu nástrojů.

V poli „Název“ přiřaďte novému vybavení název. V poli „Vybavení“
V poli „Kategorie“ klikněte na vykřičník a z rozevírací nabídky vyberte, do které kategorie nové zařízení patří.
to.

V případě více společností klikněte na rozbalovací nabídku v poli „Společnost“ a
vyberte společnost z databáze, ke které nové vybavení patří.

V poli „Použito“ vyberte jednu z tří možností přepínačů:
„Oddělení“, „Zaměstnanec“ nebo „Jiné“.

.. obrázek: maintenance_setup/maintenance-setup-new-equipment-left-side.png
:align:center
:alt:Levá strana informačních polí na novém zařízení.

Pokud je vybrána položka „Oddělení“, objeví se pole „Oddělení“ pod
:guilabel:`Používáno“ pole. Klikněte na seznam a vyberte oddělení, které používá tento
Vybavení.

Pokud je vybrán „Zaměstnanec“, objeví se pole „Zaměstnanec“ pod „Uživatel“.
Vyberte pole „By“ a z rozevírací nabídky vyberte zaměstnance, který tuto techniku používá.

Pokud je zvolená možnost „Ostatní“, obě pole „Oddělení“ a
Pole „Zaměstnanec“ se zobrazuje pod pole „Použito“. Klikněte na rozbalovací nabídku
pro příslušné obory a vyberte, který odbor a zaměstnanec používá tuto techniku.

V poli „Údržbový tým“ vyberte tým odpovědný za tuto techniku.
V poli „Technik“ vyberte člověka nebo uživatele, který je zodpovědný za tuto techniku.

.. obrázek: maintenance_setup/maintenance-setup-new-equipment-right-side.png
:align:center
:alt:Pravá část informačních polí nového zařízení.

Do pole „Použití v lokalitě“ zadejte místo, kde bude tato technika používána.
Pokud ne v pracovním centru interním (např. kancelář).

V poli „Zaměstnanecké centrum“ klikněte na rozbalovací nabídku a vyberte, které zaměstnanecké centrum bude
bude využíváno.

V prázdném poli pod záložkou „Popis“ na konci formuláře přidejte jakékoliv relevantní
informace popisující vybavení pro uživatele k použití jako odkaz.

Karta Informace o produktu
~~~~~~~~~~~~~~~~~~~~~~~

Přidat do nového vybavení jakékoliv relevantní informace z karty vybavení.
Klikněte na záložku „Informace o produktu“.

.. obrázek: maintenance_setup/maintenance-setup-product-information.png
:align:center
:alt:Tab s informacemi o produktu a dostupnými poli pod ním.

Do pole „Dodavatel“ vepište dodavatele, od kterého byl stroj zakoupen.
:guilabel:„Referenční číslo dodavatele“ pole, přidejte referenční číslo produktu získané od dodavatele, pokud
aplikovatelné.

V poli „Model“ zadejte, jaký model je tato zařízení, pokud se to vztahuje. Pokud
zařízení je sériováno, přidejte sériové číslo do pole „Sériové číslo“.

V poli „Datum účinnosti“ klikněte na datum, aby se zobrazila kalendářová lišta, a vyberte
datum. Toto datum ukazuje, kdy bylo zařízení poprvé použito a bude použito k výpočtu
Průměrný čas mezi poruchami (MTBF) v záložce „Údržba“ na kartě zařízení.

V poli „Náklady na pořízení“ zadejte náklady na pořízení zařízení, pokud je to vhodné.

Pokud je vybavení pod zárukou, uveďte datum expirace záruky
Vybrat datum z kalendáře v tomto poli.

Karta údržby
~~~~~~~~~~~~~~~

Pro každý kus zařízení jsou k dispozici různé ukazatele údržby a automaticky
vypočítané na základě opravných a plánovaných preventivních údržbových prací.

Pro zobrazení údajů o údržbě pro konkrétní kus zařízení klepněte na
kartu „Údržba“.

.. obrázek: maintenance_setup/maintenance-setup-metrics.png
:align:center
:alt:Karta údržby na formuláři zařízení s vypočítanými hodnotami.

Tím se zobrazí následující pole:

- :guilabel:`Očekávaný čas mezi poruchami“: doba (v dnech), než dojde k další
Chyba se očekává. To je jediné pole, které není šedé a jediné pole, kterým mohou uživatelé
editovat.
- :guilabel:`Průměrná doba mezi poruchami“: čas (v dnech) od posledního hlášení o poruše.
Tato hodnota je vypočítána na základě úspěšně dokončených opravných údržbových prací.
- :guilabel:`Očekávaný termín dalšího selhání“: datum, kdy se očekává další závada. Toto datum je
je vypočítána jako datum posledního selhání plus MTBF.
- :guilabel:Nejnovější selhání: Datum posledního selhání. Hodnota v tomto poli se aktualizuje jednou za
Pro tuto techniku je hlášena závada.
- :guilabel:`Čas potřebný k opravě“: doba, za kterou se tato technika opraví
Při neúspěchu. Tato hodnota se aktualizuje po dokončení požadavku na údržbu pro tuto zařízení.

Pracoviště
============

Prohlédnout si pracoviště, na kterých se využívá zařízení, a jak je na nich využívají.
Přejděte na menu: „Údržba aplikace“ - „Zařízení“ - „Strojní centra“ a klikněte do pracovního centra.
centrum.

Klikněte na záložku „Zařízení“ v zobrazené pracovní oblasti a zobrazí se všechna zařízení.
nástroje používané v konkrétním pracovním centru.

Každý kus vybavení je uveden s určitými důležitými informacemi, například jméno vybavení:
odpovědný technik, kategorii zařízení, ke kterému patří, a pár
důležité ukazatele údržby: jeho MTBF, MTTR a datum „předpokládaného dalšího selhání“.

.. obrázek: maintenance_setup/maintenance-setup-work-center.png
:align:center
:alt: Seznam zařízení, které je součástí pracovního centra.

..tip:
Chcete-li přidat nové vybavení do pracovního centra přímo z formuláře pracovního centra, klikněte na tlačítko:
pod záložkou „Vybavení“ a otevře dialogové okno „Přidat: Vybavení“.
okno s upozorněním.

V okně zvolte zařízení, které chcete přidat do pracovního centra, a klikněte na
:guilabel:`Vybrat“.

.. viz také:
:doc:`přidat nové vybavení“
