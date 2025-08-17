================
Datum spotřeby
================

.. |RFQ| nahradit za: zkratka: „RFQ (žádost o nabídku)“

… inventář/správa produktů/sledování produktů/datumy expirace:

V Odoo lze použít datum expirace k řízení a sledování životních cyklů potravin.
od nákupu po prodej. Používání datumů spotřeby snižuje ztráty produktů v důsledku neočekávaného vypršení platnosti a
pomáhá zabránit odesílání nevyhovujících výrobků zákazníkům.

V Odoo lze pouze produkty sledovat pomocí *sériových čísel* a *čísel šarží*, které mohou být přiřazeny datumu vypršení platnosti.
informace. Jakmile je přiděleno mnoho nebo sériové číslo, lze nastavit datum vypršení platnosti.
Především pro firmy (například výrobce potravin), které pravidelně nebo výhradně nakupují
a prodávat zboží s omezenou trvanlivostí.

.. viz též:
   - :doc:`../produkt/sledovani-skladu/lokace`
   - :doc:`../produktove_sledovani/seriovy_cislo`

Povolit datum vypršení platnosti
=======================

Pro použití dat expirace přejděte do: „Inventář aplikace --> Konfigurace -->
Nastavení“ a posuňte se dolů do části „Sledovatelnost“. Pak klikněte na zaškrtávací políčko
Zapnout funkci „Sériová čísla a šarže“.

Jakmile tuto funkci aktivujete, objeví se nová možnost pro zapnutí :guilabel:`Datum vypršení platnosti`.
Zaškrtněte tento políček pro zapnutí funkce a ujistěte se, že změny uložíte.

.. obrázek: expiration_dates/expiration-dates-enabled-settings.png
:alt:Zapnul položky a sériové čísla a nastavení datumů expirace.

.. tip::
Jakmile je aktivována funkce „Sériové číslo a šarže“, objeví se další funkce.
:guilabel:`Zobrazit čísla a sériová čísla na dodacích lístcích“. Aktivací těchto funkcí se zlepší
celkovou stopu výrobku, což usnadňuje řízení stahování produktů zpět na trh, identifikaci šarží s vadnými
produkty a mnoho dalšího.

Nastavte datum vypršení platnosti u produktů
======================================

Jakmile budou funkce „Sériové číslo“ a „Datum vypršení platnosti“ aktivní,
Pokud je v nastavení aplikace **Inventář** povolena funkce vypršení platnosti, lze konfigurovat informace o vypršení platnosti na jednotlivé
Produkty.

Pro toto vyberte v nabídce: „Inventář aplikace -> Zboží -> Zboží“ a zvolte produkt.
Upravit. Vybráním produktu se zobrazí tvar produktu pro daný výrobek.

.. důležité::
Řízené pomocí čísla šarže nebo sériového čísla, nebo konfigurované pro informace o datu vypršení platnosti,
musí mít nastavenou položku „Produktová skupina“ na „Zboží“ pod „Obecné“.
Vyberte záložku „Informace“ a v poli „Skladová inventura“ vyberte buď „Podle
Unikátní sériové číslo nebo :guilabel:„Počet“.

Pak klikněte na záložku „Sklad“ a posuňte se dolů do části „Sledovatelnost“.
Zatrhněte políčko „Datum vypršení platnosti“.

.. poznámka::
Pokud má produkt skladovou zásobu před aktivací sledování podle čísel nebo sériových čísel,
Potřeba přizpůsobení zásob může vzniknout, aby se k již existujícím položkám přiřadily čísla šarží.
zásoby.

.. tip::
Pro zpracování velkého množství produktů na příjmech nebo dodávkách se doporučuje sledovat
používání velkého množství produktů, takže lze stejným způsobem sledovat více výrobků v případě problémů.

.. obrázek: expiration_dates/expiration-dates-product-configuration.png
:alt: Konfigurace datumů expirace na formuláři produktu.

V sekci „Datum“ jsou čtyři kategorie informací o datu vypršení platnosti.
konfigurovat produkt:

- :guilabel:`Datum vypršení platnosti“: počet dní po obdržení produktů (od dodavatele nebo
výrobě (tj. v zásobách, kde mohou být zboží nebezpečné a nesmí se používat nebo konzumovat).
- „Nejlepší do“: počet dní před datem vypršení platnosti, ve kterých jsou zboží
se začne zhoršovat, **až do té doby, než se stane nebezpečným**.
- :guilabel:`Čas odstranění‘: počet dní před datem vypršení platnosti, ve kterých by měly být zboží
být vyřazen z prodeje.
- :guilabel:`Časová hodnota upozornění“: počet dní před datem vypršení platnosti, ve kterých by měla být aktivována
zboží z určitého balení nebo s konkrétním číslem sériového čísla.

.. poznámka::
Hodnoty zadané do těchto polí automaticky vypočtou datum spotřeby pro zboží vložené
do zásob, ať už byly zakoupeny od dodavatele nebo vyráběny ve vlastní firmě.

.. tip::
Pokud pole „Datum“ není vyplněno žádnými hodnotami pro informace o platnosti, datum
Může se přidělovat ručně při příjmech a výdejích v rámci skladu.
I když jsou přiřazeny, mohou být přepsány a změněny ručně, pokud je to potřeba.

Datum vypršení platnosti na účtenkách s čísly a sériovými čísly
===========================================================

Datum vypršení platnosti pro zboží, které přišlo do skladu, lze nastavit přímo na etiketě „Příjem“.
Přejděte na:menu:„Skladové aplikace - operace - příjemky“, pak klikněte na řádek
otevřít záznam „Pokladní doklad“.

.. důležité::
Před přiřazením objednaného množství produktů sériovému číslu klikněte na tlačítko „Zkontrolovat“.
Vyvolává okno „Chyba uživatele“. Okno vyžaduje zadání čísla nebo sériového čísla.
číslo objednaného zboží. Faktura nelze ověřit bez přidělené šarže nebo
sériové číslo.

.... obrázek: expiration_dates/expiration-dates-user-error-popup.png
:alt:Popup chyby uživatele při ověřování objednávky bez čísla položky.

Zde klikněte na ikonu „fa-list“ s popiskem „Detailní informace“.
Po kliknutí se zobrazí okno s podrobnými informacemi o operaci.

V okně přesunutí se automaticky vyplní datum expirace na základě konfigurace
na položku „Číslo šarže“. Klikněte na pole „Číslo šarže“ v příslušné řádce a pak
Zadejte číslo nebo sériové číslo.

.. tip::
Pokud pole „Datum“ na formuláři produktu nebylo nakonfigurováno,
:guilabel:`Datum vypršení platnosti“ lze ručně zadat.

Klikněte na tlačítko „Uložit“ a zavřete okno. Nakonec klikněte na „Zkontrolovat“.

.. obrázek: expiration_dates/expiration-dates-detailed-operations-popup.png
:alt:Popup s podrobnostmi o objednávce, který zobrazuje datum vypršení platnosti objednaných produktů.

Po ověření účtenky se vám zobrazí tlačítko „Sledovatelnost“. Kliknutím na
:guilabel:„Sledovatelnost“ chytrý tlačítko, které zobrazí aktualizovanou „Zprávu o sledovatelnosti“.
zahrnuje: dokument „Referenční číslo“; produkt, který je sledován;
:guilabel:`Číslo šarže/sériové číslo“; a další.

Určete datum spotřeby výrobků
=============================================

Datum spotřeby lze také vygenerovat pro výrobky vyráběné ve vlastní režii.
datum výroby kupovaného produktu, pro dokončení objednávky na výrobu (MO) je potřeba.

Pro vytvoření :abbr:`MO (manufacturing order)` přejděte na :menuselection:`Operace
Vyberte možnost „Zadání výrobních objednávek“ a klikněte na tlačítko „Nový“. Vyberte produkt, který chcete vyrobit.
Vyberte pole „Produkt“ v seznamu „Drobečků“, pak vyberte „Množství“.

.. obrázek: expiration_dates/expiration-dates-manufacturing-order.png
:alt: Výrobní objednávka na výrobek s datem spotřeby.

.. poznámka::
Pro výrobu produktu musí být materiál k spotřebě v linkách ve výrobním závodě.
:guilabel:`Produkt“ sloupec. To lze dosáhnout buď vytvořením :guilabel:`Faktura“.
Materiál pro výrobek nebo ruční přidání materiálu k spotřebě klepnutím
:guilabel:`Přidat řádek“.

Po dokončení klikněte na tlačítko „Potvrdit“.

Vhodné množství políček „Sériové číslo“ se automaticky vyplní do pole.
Klikněte na ikonu „fa-list“ a zobrazí se další informace o těchto
konkrétní číslo. Na tomto okně se zobrazí všechny informace o vypršení platnosti, které byly pro
je zboží vystaveno.

.. obrázek: vypršení platnosti / komponenty-povolení.png
:alt:Pop-up okno s informacemi o datu vypršení platnosti pro konkrétní číslo šarže.

Prodávejte zboží s datem spotřeby
===================================

Prodávat zboží s datem spotřeby se dělá stejně jako u jiných produktů.
Prvním krokem při prodeji zboží se sníženou trvanlivostí je vytvoření objednávky na prodej.

Pro toto vyberte možnost „Nové“ v aplikaci „Prodej“, zadejte své údaje a
informace na objednávkovém lístku.

Přidejte položku „Zákazník“, pak klikněte na „Přidat produkt“ pro přidání požadovaných produktů do
:guilabel:`Produkt“ a nastavte „Množství“.

Poté klikněte na záložku „Ostatní informace“. V sekci „Dodání“ změňte
„Datum dodání“ na datum po očekávaném datu a klikněte na „Použít“, abyste potvrdili
datum. Nakonec klikněte na tlačítko „Potvrdit“ pro potvrzení objednávky.

.. důležité::
Pokud jsou produkty dodány před datem upozornění nastaveným v kartě produktu, pak se žádné
Vytváří se upozornění.

Nyní klikněte na tlačítko „Dodání“ v horní části objednávky. Zobrazí se sklad
pokladní doklad.

Na formuláři záznamu o skladování klikněte na „Potvrdit“ a poté na „Uplatnit“.
příležitostném okně, které automaticky zpracuje všechny množství „Dokončeno“ a dodá
Zboží zákazníkovi.

.. důležité::
Pro prodej zboží se sníženou trvanlivostí a datem spotřeby je vhodná strategie
:guilabel:`Lokalita“ skladování produktů musí být nastaveno na „FEFO (První expirace, první
Pokud není dostatečný počet zboží v jedné dodávce, Odoo automaticky
přebytečné množství odebrat z druhé dodávky s nejbližším datem spotřeby.
Strategie odstranění mohou být také nastaveny na :guilabel:`Kategorie produktů“.

.. viz též:
:doc:`../dodavatelé/strategie-vykládání“

Zobrazte data vypršení platnosti pro sériové číslo a šarže
===============================================

Pro zobrazení (a/nebo seskupení) všech produktů s datem spotřeby podle čísla šarže přejděte na
:menu:„Aplikace Inventář --> Produkty --> Sériové čísla“.

Jakmile tam budete, odstraňte z vyhledávací lišty jakékoliv výchozí filtry a poté klikněte na tlačítko „Seskupit“.
Vyberte možnost „Přidat vlastní skupinu“ a zvolte parametr „Datum vypršení platnosti“.
nabídka. Tím se rozpadne vše z kategorie potravin, jejich minimální trvanlivosti a
číslo pořadí přiřazené k danému pozemku.

.. obrázek: expiration_dates/expiration-dates-group-by-dates.png
:alt: Skupina podle data vypršení platnosti a sériových čísel na stránce se skupinami.

.. tip::
Klienti mohou také vidět upozornění na vypršení platnosti v jejich zákaznickém portálu.

...Inventar/Produktverwaltung/Ablaufdatumsbenachrichtigungen:

Upomínky k vypršení platnosti
-----------------

Pro zobrazení upozornění na vypršení platnosti přejděte do aplikace „Skladové zásoby“ - „Produkty“ - „Sériová čísla“.

Pak klikněte na pole „Číslo šarže“ s potravinami se zkracující se dobou trvanlivosti. To vám ukáže
formulář pro podrobné údaje o sériovém čísle.

.. tip::
Chcete-li zobrazit informace o datu vypršení platnosti v seznamovém pohledu, klikněte na ikonu „Oi-settings-adjust“
:guilabel:`(upravit nastavení)` ikona v horní části seznamu záznamů a pak zaškrtněte
:guilabel:`Datum vypršení platnosti“ zaškrtávací políčko.

Na formuláři pro podrobné informace o čísle šarže a sériovém čísle je seznam všech dat vypršení platnosti.
informace o produktech.

Pokud vypršela platnost čísla šarže nebo data výroby, zobrazí se na formuláři červené
:guilabel:`Expiration Alert“ nahoře na stránce, aby uživatelé věděli, že produkty v tomto balení jsou
nebo brzy vyprší.

Zde klikněte zpět na stránku „Sériová čísla“ (pomocí chleba s nápisem).

Pro zobrazení nové výstrahy před vypršením platnosti nebo jakékoliv jiné výstrahy pro produkty, které jsou již vyprodané (nebo se brzy stane),
v nejbližší době vyprší), klikněte zpět na stránku „Sériové číslo“ pomocí chlebových zbytků. Odstraňte
všechny filtry vyhledávání z panelu nástrojů „Sériová čísla“ na :guilabel:„Položky/sériová čísla“.

Poté klikněte na „Filtry“ a vyberte „Upomínky o expiraci“.

.. obrázek: expiration_dates/expiration-dates-expiration-alert.png
:alt:Upozornění na produkt, který již vypršel.

Oznámení o vypršení platnosti
------------------------

Uživatelé mohou být upozorněni, když vyprší platnost produktu. To jim pomůže udržet si určitý
zaměstnance informovat o stavu věcí, které mají na starosti.

Pro konfiguraci upozornění přejděte do sekce „Aplikace Inventuru --> Zboží --> Zboží“.
Vyberte produkt, který je konfigurován s čísly šarží a datem vypršení platnosti.
Karta „Sklad“. V sekci „Logistika“ vyberte uživatele
:guilabel:`Zodpovědný“ pole.

Když uplyne datum vykoupení pro dané číslo sériového listu nebo šarže tohoto produktu, je odeslána
uživatel v tomto poli.

.. poznámka::
Jakmile je datum vypršení platnosti splatné, vytvoří se upozornění na vypršení platnosti na formuláři pro zobrazení položky/sériového čísla.
číslo výrobku.

Chcete-li upravit tyto výstrahy, zapněte režim pro vývojáře (viz Developer Mode), přejděte na
:menu: „Nastavení aplikace“ --> „Technické“ --> „Typy aktivit“, a vyberte :guilabel:„Poplach
Datum dosažení cíle

Uživatel, který je přiřazen výchozímu uživateli, bude upozorněn, jakmile vyprší platnost. Pokud není
Pokud je nastaven výchozí uživatel, aktivita bude přiřazena uživateli s názvem „Odpovědný“.
zvolené na záložce „Sklad“.
