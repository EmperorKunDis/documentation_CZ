===================
Přehled výrobní plochy
===================

... výroba / podlaha / přehled podlahy:
.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`
.. |MOs| nahradit za:: :abbr:`MOs (Výrobní objednávky)`

Modul „Podlaha“ je doplňkovým modulem aplikace „Výroba“. Modul „Podlaha“ poskytuje
vizuální rozhraní pro zpracování výrobních objednávek (MO) a pracovních příkazů.
sledování množství času, které zaměstnanci ve výrobě stráví prací na výrobních a pracovních objednávkách.

Modul Shop Floor je nainstalován vedle aplikace Manufacturing. Není možné jej instalovat
sám. Chcete-li nainstalovat aplikaci *Výroba*, přejděte do sekce „Aplikace“, vyhledejte
„Výroba“ v poli „Hledat…“ a pak klikněte na „Instalovat“
:guilabel:`Výroba“ aplikační karta.

.. důležité::
Modul „Podlaha“ nahrazuje funkci tabletu v aplikaci „Výroba“,
je k dispozici pouze v verzích Odoo od verze 16.4 a vyšších.

Chcete-li zkontrolovat číslo verze databáze Odoo, přejděte do sekce „Nastavení“ a posuňte
a dokonce až na část „O aplikaci“ v dolní části stránky, kde je zobrazeno číslo verze.
tam.

Chcete-li přejít na novější verzi Odoo, podívejte se do dokumentace na :doc:`přechod databáze
<../../../administration/upgrade>.

Navigace
==========

*Prodejní plocha* je rozdělena do tří hlavních pohledů, které lze vybrat z navigačního panelu
horní část modulu:

- Stránka „Všechno“ slouží jako hlavní panel modulu a zobrazuje informace
karty pro MOs.
- Každé pracoviště má také svou vlastní stránku, na které se zobrazují informační karty pro výrobní zakázky přiřazené
do pracovního centra. Stránky pracovního centra lze zapnout nebo vypnout kliknutím na tlačítko :guilabel:`+
(plus) tlačítko v navigační liště, vybírat nebo odstraňovat je z okna s výběrem.
Vyskočí okno s názvem „Potvrzení“ a po kliknutí na něj.
- Stránka s názvem „Můj“ zobrazuje informační karty pro všechny pracovní objednávky přidělené zaměstnanci,
Profil je aktuálně aktivní v ovládacím panelu na levé straně modulu.
Zobrazuje pracovní příkazy přidělené aktivním zaměstnancům a funguje stejně jako stránky pro
každé pracoviště.

..tip:
Chcete-li izolovat |MO| nebo pracovní příkaz, aby se nezobrazily žádné další objednávky, jednoduše vyhledejte odkaz
počet MO v seznamu na liště hledání nad modulovým oknem. Tento filtr vyhledávání
Zůstává aktivní při přepínání mezi různými pohledy na moduly.

Na levé straně modulu je ovládací panel, který zobrazuje všechny zaměstnance v současné době
, a umožňuje novým zaměstnancům se přihlásit. Panel obsluhy je vždy
je k dispozici v modulu a je možné ho zapnout nebo vypnout pomocí
kliknutím na tlačítko „Navigační lišta“ v nejlepším levém rohu navigační lišty.

.. obrázek: shop_floor_overview/sidebar-button.png
:align:center
:alt:Tlačítko „boční lišta“, které se používá k zapnutí nebo vypnutí ovládacího panelu.

Stránka
--------

Výchozí stránka „Všechny“ zobrazuje informační kartu pro každé |MO| připravené k
start*. Jako připravený k startu je považován za potvrzení a všechny požadované komponenty.
Je k dispozici.

Pro zobrazení všech potvrzených |MO| bez ohledu na jejich stav klikněte na tlačítko
filtr „Připraveno k použití“ odstranit z filtru „Hledat…“.

Informační karta MO
~~~~~~~~~~~~~~~~~~~

Informační karta MO na stránce „Všechny“ zobrazuje všechny podstatné informace o
spojené s |MO| a poskytuje zaměstnancům možnosti zpracování |MO|.

Hlavička karty MO uvádí číslo MO, produkt a počet jednotek vyráběných.
a stav MO. Pokud práce na MO ještě nezačaly, zobrazí se
:guilabel:„Potvrzeno“. Jakmile začnete pracovat, stav se změní na „Ve výrobě“. Pokud je vše
úkoly pro MO byly dokončeny a MO je připraveno k uzavření, stav se aktualizuje na
:guilabel:Zavřít.

Hlavní část karty |MO| zobrazuje řádek pro každou dokončenou objednávku, pokud existuje, následovaný
aktuální pracovní úkol, který je třeba dokončit. Dokončené pracovní úkoly jsou označeny zeleným štítkem
značku vpravo od názvu práce. Aktuální pracovní příkaz je označen tlačítkem
otevírá stránku pracovního centra, ke kterému je objednávka přiřazena.

Pod současným pracovním příkazem je řádek s názvem „Registrace výroby“, který se používá k
Zaznamenávat počet vyrobených produktů. Chcete-li ručně zadat počet vyrobených jednotek, klikněte
V poli „Jednotky“ na řádku „Registrace výroby“ zadejte hodnotu.
vzniklé okno, pak klikněte na tlačítko „Zkontrolovat“.

Alternativně klikněte na tlačítko „Jednotky“ vpravo od řádku, které
automaticky zaznamenává počet jednotek, které byly vytvořeny pro |MO| jako počet vyrobených jednotek.
Příkladem je vytvoření |MO| pro deset jednotek stolu. Po kliknutí na tlačítko „10 jednotek“
Tlačítko ukazuje, že bylo vyrobeno 10 kusů.

Na kartě |MO| je v zápatí tlačítko pro zavření výroby, které se používá k uzavření
Výroba je hotová a následně se provádí kvalitativní kontrola výrobku.
V celém systému MO (ne v jednotlivých pracovních příkazech) se objeví tlačítko „Kontrola kvality“
místo toho klikněte na tlačítko „Kontrola kvality“ a otevře se okno s požadovanou kontrolou
mohou být dokončeny kontroly.

Po kliknutí na tlačítko „Ukončit výrobu“ se začne zobrazovat karta |MO| a
Tlačítko „Zrušit“ se objeví v zápatí. Kliknutím na tlačítko „Zrušit“ zůstane |MO|
otevřené. Jakmile zmizí karta |MO| úplně, je práce dokončena.

Vpravo dole je tlačítko s ikonou „⋮ (možnosti)“, které otevře okno
s dalšími možnostmi pro |MO|:

- :guilabel:`Scrap“ se používá k odeslání komponent do skladu pro nepotřebné součástky, pokud jsou zjištěny jako
vadný.
- :guilabel:`Přidat pracovní objednávku“ se používá k přidání další pracovní objednávky do |MO|.
- :guilabel:Přidat komponentu se používá k přidání další komponenty do |MO|.
- :guilabel:`Otevřít zadní část MO“ otevře |MO| v aplikaci Manufacturing.

.. obrázek: shop_floor_overview/mo-card.png
:align:center
:alt: Informační karta pro MO na stránce „Vše“ v modulu Provozovna.

Stránky pracovního centra
-----------------

Výchozí stránka pro každé pracoviště zobrazuje kartu informací o každém přiděleném úkolu.
je připravená k zahájení. Pracovní objednávka se považuje za připravenou k zahájení, pokud je součástí
je připravena k zahájení a všechny předchozí pracovní příkazy byly dokončeny.

Pro zobrazení všech potvrzených pracovních příkazů přiřazených k pracovišti bez ohledu na stav, klikněte na
Tlačítko „Odebrat“ na filtru „Připraveno k použití“, které se nachází v
:guilabel:„Hledat…“ lišta.

Informační karta o objednávce práce
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Karta s informacemi o pracovním příkazu na stránce pracoviště zobrazuje všechny podstatné detaily
přidružený pracovní příkaz a také poskytuje zaměstnancům možnosti zpracování pracovního příkazu.

Hlavička pracovního příkazu zobrazuje referenční číslo MO, pro které je pracovní příkaz vystaven.
části, produktu a počtu jednotek vyráběných, a stav objednávky na práci. Pokud je
práce na zakázce nezačala, stav se zobrazí jako:guilabel:`To Do`. Jakmile začne práce,
Aktualizace stavu zobrazí časovač, který ukazuje celkový čas strávený na pracovním příkazu.

Hlavní část karty pracovního příkazu obsahuje řádek pro každý krok, který je potřeba provést při dokončení pracovního příkazu.
Krok pracovního příkazu lze dokončit kliknutím na řádek a následně podle pokynů v
okně s upozorněním, které se objeví. Místo toho můžete zaškrtnout políčko vedle každé řádky
automaticky krok označí jako dokončený.

Pod posledním krokem objednávky práce je řádek s názvem „Registrace výroby“, který
funguje stejně jako řádek „Registrace výroby“ na kartě |MO|. Registruje
Počet vyrobených jednotek na pracovním příkazu pomocí výrobní linky „Registrace“
dokončuje krok pro spojenou kartu MO.

Pokud je zpracovávaná pracovní objednávka konečnou pracovní objednávkou pro |MO|, zobrazí se tlačítko „Zavřít“.
Tlačítko „Produkce“ se objeví na záložce s pracovním příkazem. Po kliknutí se zobrazí:„Zavřít
Produkce uzavírá jak objednávku práce, tak i MO, pokud není vyžadována kontrola kvality.
|MO|. V tomto případě musí být kvalitativní kontrola dokončena z karty |MO| před tím, než může být
Zavřeno.

Alternativně, pokud MO vyžaduje dokončení dalších pracovních příkazů, může být použit :guilabel:`Značka
Zobrazí se tlačítko „Ukončit“. Po kliknutí na něj je aktuální pracovní příkaz označen jako
a způsobuje zobrazení dalšího pracovního příkazu na stránce pro pracoviště, ke kterému je přiřazen.
to.

Po kliknutí na „Uzavřít výrobu“ nebo „Zadat dokončeno“ se začíná pracovní karta objednávky.
vybledne a na záhlaví se objeví tlačítko „Zrušit“. Kliknutím na „Zrušit“
zůstane otevřená. Jakmile úplně zmizí karta s pracovním příkazem, je
označeno jako:guilabel:`Dokončeno` na |MO|.

Vpravo dole je tlačítko s ikonou „⋮ (možnosti)“, které otevře okno
s dalšími možnostmi pro objednávku práce:

- :guilabel:`Scrap“ se používá k odeslání komponent do skladu pro nepotřebné součástky, pokud jsou zjištěny jako
vadný.
- :guilabel:Přidat komponentu se používá k přidání další komponenty do |MO|.
- Přesun na pracoviště je používán k přesunu objednávky práce do jiného pracoviště.
- :guilabel:Navrhněte zlepšení pracovního listu“ umožňuje uživatelům navrhovat změny v práci.
pokyny nebo kroky příkazu.
- Kliknutím na tlačítko „Vytvořit upozornění na kvalitu“ se otevře formulář, který lze vyplnit a odeslat jako upozornění na kvalitu.
kvalitní tým o potenciálním problému.

.. obrázek:shop_floor_overview/wo-card.png
:align:center
:alt: Informační karta pro objednávku v modulu Výroba.

Panel operátora
--------------

Ovládací panel se používá k řízení zaměstnanců, kteří jsou přihlášeni do modulu Shop Floor.
Panel ukazuje jméno a profilovou fotografii každého zaměstnance, který je v současné době přihlášen.
Všechny instancí databáze.

Pro interakci s *Shop Floor* jako konkrétním zaměstnancem klikněte na jméno zaměstnance.
profily. Profily, které nejsou aktivní, se zobrazují s jejich jménem a profilovými obrázky šedě.

Když je vybrán zaměstnanec na ovládacím panelu, může začít pracovat na objednávce.
kliknutím na hlavičku pracovního úkolu. Pokud zaměstnanec pracuje na více pracovních úkolech,
Název objednávky se zobrazí pod jménem uživatele spolu s časovým indikátorem, který ukazuje, jak dlouho pracoval.
každý objednávkový formulář.

Chcete-li přidat nového zaměstnance do ovládacího panelu, klikněte na tlačítko „Přidat operátora“
spodní části panelu. Pak vyberte zaměstnance z okna „Vybrat zaměstnance“.

Chcete-li zaměstnance ze seznamu operátorů odstranit, jednoduše klikněte na tlačítko vedle jeho jména.
jméno v liště.

.. obrázek:shop_floor_overview/operator-panel.png
:align:center
:alt:Ovládací panel modulu Podlaha obchodu s třemi zaměstnanci přihlášenými.

Prioritizace MO/WO
====================

Modul „Prodejní plocha“ používá datum, které bylo zadáno v MOS, k prioritizaci MOS.
pracovní příkazy, které se zobrazují na stránkách modulu Dashboard a Work Center.
Ty, které jsou naplánované dříve, mají vyšší prioritu a zobrazují se před těmi, které byly naplánovány později.
výstupy.

Pro určení termínu v aplikaci |MO| začněte procházením sekce:
→ Provoz → Výrobní objednávky“ a klikněte na „Nový“, abyste vytvořili novou |MO|.

Klikněte na pole „Datum“ a otevře se okno s kalendářem. Výchozí datum je
Tlačítko „Datum“ a jeho odpovídající okno zobrazují aktuální datum.
čas.

V kalendáři vyberte datum, od kterého by měla být zahájena zpracování pro MO. V polích
Do dolní části okna přidejte hodinu a minutu, ve které by měla zpracování začít.
v 24hodinovém formátu.

Konečně klikněte na tlačítko „Použít“ v dolní části okna připnutého okna a nastavte datum a čas.
V poli „Datum“ a poté klikněte na tlačítko „Potvrdit“ v horní části stránky.
„To potvrdilo i MO.“

Jakmile je potvrzeno MO, objeví se v modulu Shop Floor, dokud nebude
Stav „Připraveno“, což znamená, že jsou všechny komponenty k dispozici.

Na panelu Odoo klikněte na modul „Výroba“ a otevřete jej.
:guilabel:'Všechny MO #' stránka panelu zobrazuje *Připraveno* |MOs|, seřazené podle jejich
termíny, které jsou v rozpisu.

Na horní části modulu vyberte pracoviště, abyste viděli objednávky na něm přidělené.
Každé pracoviště zadává práce na základě plánovaných termínů svých odpovídajících |MOs|.

Příklad:
Tři MO jsou potvrzeny pro produkt knihovny:

   - WH/MO/00411 má datum plánovaného spuštění 16. srpna.
   - WH/MO/00412 má naplánovaný termín 20. srpna.
   - WH/MO/00413 má datum „Plánované“ 18. srpna.

Na stránce „Všechny MO“ modulu Shop Floor se zobrazují karty pro každou |MO|.
tohoto rozkazu: WH/MO/00411, WH/MO/00413, WH/MO/00412.

.... obrázek:shop_floor_overview/mo-order.png
:srovnání: do středu
:alt:MO v modulu Výroba, seřazené podle jejich plánovaného data.

Každý |MO| vyžaduje jeden pracovní příkaz provedený na :guilabel:`Sestavovací stanici 1`. Kliknutím na
:tlačítko „Montážní stanice 1“ v horní části obrazovky otevře stránku pro práci
centru, který zobrazuje jednu kartu pro každý pracovní příkaz, v pořadí stejném jako jejich
corresponding MOs.
