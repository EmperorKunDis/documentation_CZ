========
Služby
========

Aby bylo možné udržovat vozový park v dobrém stavu, je nutná pravidelná údržba i občasné opravy.
je nezbytné naplánovat opravy a spravovat služby pro celý flotilu, aby se zajistilo, že
Vozidla jsou v dobrém technickém stavu, když je potřebují.

Služby, jako je pravidelná údržba, například výměna oleje nebo přetočení pneumatik, lze zadat předem.
Ostatní opravy se zaznamenávají, jakmile k nim dojde.

...flotila/služba:

Vytvořit servisní záznamy
======================

Pro zadání služby pro vozidlo přejděte na hlavní panel „Služby“ kliknutím na
:menu „Flotilní aplikace“ -> „Flotila“ -> „Služby“. Novou službu otevřete kliknutím na
:guilabel:„Nový“ tlačítko v pravém horním rohu.

Vyplňte informace na formuláři. Jediné dvě pole, která je nutné vyplnit jsou
„Služba“ a „Dopravní prostředek“.

V poli na formuláři je:

- :guilabel:`Popis“: Do tohoto pole zadejte stručný popis služby.
- :guilabel:Typ služby: Vyberte typ poskytované služby z rozbalovací nabídky.
Pokud požadovaná služba neexistuje, zadejte nový typ služby a klikněte buď na „Vytvořit
„(typ služby)“ nebo „Vytvořit a upravit...“ klikněte na odkaz „Přidat typ služby a konfigurovat jej
<flotila/nový typ>.

.. důležité::
:guilabel:`Jenom jedna služba je přednastavena v Odoo: Výpis od dodavatele.

- :guilabel:`Datum“: Vyberte datum poskytnutí služby nebo je
která má být provedena. Přejděte na požadovaný měsíc pomocí ikonky „oi-chevron-left“
Klikněte na ikonu „vpravo“ („arrow“) a poté na datum pro výběr.
- :guilabel:`Náklady“: Zadejte odhadované náklady služby, pokud jsou k dispozici. Pokud je služba
předběžné opravy, tento prázdný řádek nechávejte prázdný. Tato pole se aktualizují podle přijatých odhadů
a znovu, až bude známá konečná cena opravy.
- :guilabel:`Dodavatel“: Vyberte dodavatele služby z roletky. Pokud
pokud dodavatel již nebyl v systému zadán, doplňte a nakonfigurujte dodavatele
<flotila/nový dodavatel>
- :guilabel:"Vozidlo": Vyberte vozidlo, které bylo servisováno.
Když je vybrán vůz, pole „Řidič“ se zaplní a jednotka měření pro
:guilabel:`Hodnota tachometru“ pole se objeví.
- :guilabel:Řidič:Toto pole se automaticky vyplní podle aktuálního řidiče vozidla při
:guilabel:`Vozidlo“ je vybráno. Pokud chce řidič změnit řidiče, může si vybrat jiného řidiče
vyberte z nabídky.
- :guilabel:`Hodnota tachometru“: Zadejte číslo na tachometru, které bylo naměřeno při provedení servisu. Jednotky
Jednotky měření jsou buď v kilometrech (:guilabel:"km") nebo mílích (:guilabel:"mi"), podle toho, jak
Vybrané vozidlo bylo nakonfigurováno.

.....tip:
Chcete-li změnit z kilometrů na míle nebo naopak, klikněte na ikonu :icon:`oi-arrow-right`.
:guilabel:`(Interní odkaz)` ikona vedle vozidla vybraného v :guilabel:`Vozidlo“
pole.

Změňte jednotku měření a poté se vraťte zpět na formulář služby pomocí odkazů „breadcrumb“.
Poté se jednotka měření aktualizuje v poli „Hodnota tachometru“ (viz obrázek).

- :guilabel:`POZNÁMKY K OPRAVĚ`: Zadejte poznámky k opravě na konci servisního formuláře. Například
To může zahrnovat podrobnosti o odhadované ceně nebo náhradních dílech.

.. obrázek: service/new-service.png
:alt: Zadejte informace o nové službě. Povinná pole jsou typ služby a vozidlo.

.. flotila/nový typ:

Vytvoření typu služby
-------------------

Jediný způsob, jak vytvořit typ služby, je z :ref:`služebního formuláře <fleet/service-form>`.

Na formuláři služby (odkaz na formulář „Služba“) zadejte název nové služby.
Zadejte příslušný typ do pole. Pak klikněte na tlačítko „Vytvořit a upravit…“ a
Zobrazí se okno „Vytvořit typ služby“.

Typ služby zadaný v kartě Služba se automaticky vyplní do pole Jméno.
které lze upravit podle potřeby.

Poté vyberte kategorii nového typu služby z roletky v
položka. K dispozici jsou dvě výchozí volby: „Smlouva“ nebo „Služba“.
Nové kategorie **nemohou být vytvořeny**.

Pokud se služba vztahuje pouze na smlouvy nebo služby, vyberte příslušnou
:guilabel:`Kategorie“. Pokud se služba vztahuje na oba smlouvy a služby, nechte pole
prázdná.

Po dokončení klikněte na tlačítko „Uložit a zavřít“.

..._flotila/nový dodavatel:

Vytvořit dodavatele
-------------

Když je služba poprvé poskytnuta, obvykle se v prodejním záznamu neobjeví.
byly přidány do databáze. Je vhodné přidat do databáze všechny podrobnosti o dodavateli, takže
aby bylo možné získat všechny potřebné informace.

Dodavatele přidává aplikace **Kontakty**. Podívejte se na dokumentaci:
Pro více informací navštivte stránku <../../essentials/contacts>.

.. poznámka::
Na formuláři pro vytvoření dodavatele mohou být viditelné různé záložky nebo pole, podle toho, co
jsou nainstalovány další aplikace.

Zobrazit služby
=============

Pro zobrazení všech služeb v databázi, včetně starých a nových požadavků, přejděte na
:menu „Flotila aplikace“ --> „Flotila“ --> „Služby“. Všechny služby se zobrazí v přehledovém zobrazení, včetně
podrobnosti o každé službě.

Služební záznamy jsou seskupeny podle typu služby: „<fleet/new-type>“. Počet oprav
Jméno služby je následováno závorkami s uvedením typu služby.

Každý služební úřad zobrazuje následující informace:

- :label_guid:`Datum“: datum, kdy byla služba nebo oprava provedena (nebo požadována)
zahrála.
- :label:Popis: krátký popis konkrétního typu služby nebo opravy
aby bylo jasné, o jaký konkrétní službu se jedná.
- :guilabel:`Typ služby“: typ poskytované služby nebo opravy. Je vybrán z seznamu
služeb, které musí být nakonfigurovány podle pokynů v části „Nová třída“.
- :guilabel:`Vozidlo“: konkrétní vozidlo, na kterém byla služba poskytnuta.
- :guilabel:`Řidič“: současný řidič vozidla.
- :guilabel:`Dodavatel“: konkrétní dodavatel služby nebo opravy.
- :guilabel:`Poznámky“: jakákoliv informace spojená s poskytováním služeb nebo opravou, která je zaznamenaná
přidat vysvětlení.
- :guilabel:`Náklady“: Celkové náklady služby nebo opravy.
- :guilabel:`Stav“: stav služby nebo opravy. Možnosti jsou :guilabel:`Nový“,


Na konci sloupce „Náklady“ jsou uvedeny celkové náklady na všechny služby a opravy.

.. obrázek:service/services.png
:alt: Kompletní seznam služeb v databázi Odoo.
