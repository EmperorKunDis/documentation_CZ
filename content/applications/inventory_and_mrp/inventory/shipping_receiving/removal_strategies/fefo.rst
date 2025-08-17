============
Odstranění FEFO
============

Strategie „První vypršelé, první ven“ (FEFO) určuje produkty k odstranění na základě jejich
přidělené termíny odsunu.

.. viz také:
:doc:`O odstraňovacích strategiích <../removal_strategies>`

... skladové zásoby, sklady, uskladnění, datum odstranění:

Datum odstranění
============

Produkty musí být odebrány z inventáře před jejich datem odstranění, které je nastaveno jako určitý
Počet dní před datem vypršení platnosti výrobku.

Uživatel si tento počet dní nastaví po přechodu na záložku „Sklad“.
V sekci „Sledovatelnost“ zkontrolujte pole „Sledování“, které by mělo být buď
„Počtem“ nebo „Sériovým číslem“.

Dále vyberte možnost „Datum vypršení platnosti“, která dává do pole „Datum odstranění“
a dalších polí s datem).

.. důležité::
Poznámka: funkce „Sériové číslo“ a „Datum vypršení platnosti“ musí být povoleny.
je zapnuto v položce menu „Inventářová aplikace -> Konfigurace -> Nastavení“ pro sledování vypršení platnosti.
datumy.

Datum spotřeby je určeno přičtením data, kdy byl produkt obdržen.
Počet dní uvedených v poli „Datum vypršení platnosti“ na formuláři produktu.

Datum odstranění bere datum vypršení platnosti a odečte počet dnů uvedených v
V poli „Datum odstranění“ v kartě produktu.

.. viz také:
:doc:`Datum vypršení platnosti <../../produktové řízení/sledování produktů/datum vypršení platnosti>`

Příklad:
V záložce „Sklad“ produktu „Vejce“ jsou nastaveny následující „Datumy“
uživatelem:

   - :guilabel:`Datum vypršení platnosti“: 30 dní po obdržení
   - :guilabel:`Datum vypršení platnosti“: 15 dní před datem vypršení platnosti

.... obrázek: fefo/user-set-date.png
:srovnání: do středu
:alt:Zobrazit datum vypršení platnosti a odstranění nastavené na formuláři produktu.

Dodávka vajec dorazila do skladu 1. ledna. Proto datum spotřeby vajec je
**31. ledna** (1. ledna + 30). Prodlouženě pak odstranění je **16. ledna** (31. ledna –
   15).

... skladovací prostory, inventář, datum expirace:

Pro zobrazení dat spotřeby položek v zásobách přejděte na stránku produktu a klikněte na
:guilabel:`Na ruce“ chytrý tlačítko.

Dále klikněte na ikonu dalších možností umístěnou v pravém dolním rohu a vyberte sloupce:
:guilabel:`Datum vypršení platnosti“ a „Datum odstranění“.

.. obrázek: fefo/odstraneni-datum.png
:align:center
:alt:Zobrazte data vypršení platnosti z modelu inventarizace přístupného ze zásob.
chytrý tlačítko z produktové řady.

Průběh práce
========

Použitím strategie „první vypršelé, první ven“ se zajistí, že produkty s
Nejblíže termínu odjezdu jsou vybírány první.

Chcete-li pochopit, jak tato strategie funguje, podívejte se na následující příklad o
produkt „Krabice vajec“, což je krabice obsahující dvanáct vajec.

Produkt je sledován podle značky „Ve velkém“, a kategorie produktu je označena jako „Povinné odstranění“.
Strategie je nastavena na: „První expirované, první ven“.

.. viz také:
   - :ref:`Nastavte strategii odstraňování skladů <inventory/warehouses_storage/removal-config>“
   - :ref:`Nastavit sledování skladových položek <sklad/skladové zásoby a skladování/nastavení skladových položek>`
   - „Tutoriály Odoo: Zboží s omezenou trvanlivostí <https://www.odoo.com/slides/slide/5324/share>“

.. seznam-tabulka::
:hlavičkové řádky: 1
:sloupek: 1

   * -
     - LOT 1
     - LOT2
     - LOT3
   * -Na skladě
     - 5
     - 2
     - 1
   * - Datum vypršení platnosti
     - 4. dubna
     - 10. dubna
     - 15. dubna
   * :-: Odstranění datumu skladování (datum expirace)
     - 26. února
     - 4. března
     - 9. března

Chcete-li vidět strategii odstranění v akci, přejděte do aplikace „Prodej“ a vytvořte nový
citát.

Kliknutím na tlačítko „Potvrdit“ se vytvoří dodací příkaz pro dnešní datum 29. prosince a číslo položky
Ty s nejkratší dobou trvanlivosti jsou vyhrazeny a používají se podle zkratky FEFO (první vypršelé, první ven).
strategie odstranění.

Pro zobrazení podrobného výpisu klikněte na ikonu „⦙≣ (seznam bodů)“, která se nachází v
pravicové kartony v sortimentu vejce, v záložce „Dodávky“
dodržet pořadí. To způsobí, že se otevře okno „Přesun zboží“ s názvem „Otevřený přesun“.

V okně „Přesun otevřeného skladu“ se v poli „Odebrat z“ zobrazí
Zde se vybírají množství, které budou uspokojovat poptávku.

Vzhledem k tomu, že objednávka požadovala šest krabic vajec, bylo použito zkratky FEFO (první vypršelé, první ven).
strategie odstranění, všech pět kartonů z „LOT1“ s datem vyřazení 26. února jsou odebrány.
Zbylý karton je vybrán z „LOT2“, který má datum odstranění 4. března.

.. obrázek: fefo/sbirani-vajec.png
:align:center
:alt:Okno s pohybem zásob, které ukazuje položky k odstranění pomocí FEFO.
