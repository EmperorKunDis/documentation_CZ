========================
Zpráva o distribuci olova
========================

*Zpráva o distribuci kontaktů* může sloužit k zjištění, zda jsou aktivní kontakty rovnoměrně přidělovány.
Prodejní tým. Může být také použito k zobrazení distribuce dobrých nebo kvalitních kontaktů
<report o kvalitě leadů>“ a zjistěte, jak často každý obchodník dostává (a udržuje) leady.

Zprávy o distribuci vedoucích mohou být vytvářeny každý týden, aby pomohly udržet prodejce na správné cestě.
poskytnout jim dostatek dobrých kontaktů. Tyto zprávy lze také použít k tomu, aby se ujistili, že členové prodeje
zůstávají produktivní, pokud se často ztrácí dobré kontakty jedním prodejcem a
v celku se zvyšuje procento dobrých kontaktů.

Vytvořte zprávy o distribuci kontaktů
================================

Pro vytvoření reportu o distribuci kontaktů se nejprve přesunete na: „Aplikace CRM -> Zprávy ->
Trubka“, která odhaluje panel „Analýza trubky“.

Odeberte všechny výchozí filtry v hledaném poli na horní části stránky.
zobrazuje informace o všech kontaktech.

Můžete přidat vlastní filtry kliknutím na ikonu
ikona „(svislý znak)“ vedle vyhledávací lišty pro odhalení nabídky vyhledávání
a filtrační možnosti.

Tři sloupce jsou zobrazeny: „Filtry“ (odkaz na část Filtry), „Skupina“ (odkaz na část Skupiny) a
:ref:`Oblíbené <hledat/oblíbené>“. Chcete-li začít, přejděte na konec filtrů
sloupec a klikněte na „Přidat vlastní filtr“. To otevře okno „Přidat vlastní filtr“
okna, kde lze filtry přidávat postupně.

.. _crm/track_leads/essential-filters:

Nezbytné filtry
-----------------

Následující filtrační podmínky jsou používány k vytvoření základního reportu o distribuci kontaktů.
souhrn všech vytvořených kontaktů za určité časové období, které mají spojený způsob kontaktování.
byli přiděleni do prodejního týmu.

Datum vytvoření kontaktu
~~~~~~~~~~~~~~~~~~

Klikněte na první pole pod nadpisem „Zapadne do kterékoliv z následujících pravidel“ s hodnotou
:guilabel:`Země“ v něm. V okně, které se objeví, zadejte do vyhledávací lišty „Vytvořeno“ nebo
Přejděte dolů, abyste mohli prohledávat seznam a vybrat jej.

V druhém poli řádku pak vyberte z roletky :guilabel:`>=`. Tento operátor
*obsahuje pouze hodnoty větší než nebo rovné hodnotě ve třetím, pravém poli.*

Třetí pole na okně „Přidat vlastní filtr“ by mělo obsahovat nejranější datum.
Vybírají se z nich.

Příkladem je nastavení „01/01/2024 00:00:00“, které zahrnuje pouze kontakty vytvořené od a včetně
1. ledna 2024.

.. obrázek: lead_distribution_report/created-on.png
:align:center
:alt:Přidejte pravidlo Vytvořeno od začátku roku.

.. _crm/track_leads/sales-team:

Prodejní tým
~~~~~~~~~~

Klikněte na „Nový řádek“ a vyberte „Prodejní tým“.
parametr této pravidla. Pak klikněte na druhé pole nového pravidla a vyberte „obsahuje“
z rozevírací nabídky. Vybráním tohoto operátora filtruje všechny záznamy, které obsahují slova
třetí pole vpravo.

..tip:
Pro určité předem stanovené omezené volby, jako je například prodejní tým, se používá operátor „je v“
pomáhá při snadnějším a přesnějším výběru, v třetím poli prostřednictvím rozbalovací nabídky.
místo rizika chybného zadání nebo nesprávné hodnoty v poli textového pole, které
:guilabel:`obsahuje“ operátor.

V tomto třetím poli zadejte jméno požadovaného prodejního týmu (týmů), který chcete zařadit do
reportu. Je důležité, aby všechny hodnoty argumentu `contains` byly konkrétní a
pokud jsou napsány správně tak, jak v Odoo existují, jinak hrozí, že se vrátí více (nebo žádné) hodnoty.

.. obrázek: lead_distribution_report/sales-team-location.png
:align:center
:alt:Použijte prodejní tým k filtrování lokality, ke které je vázán kontakt.

.. důležité:
Přidáním více než jednoho pravidla do formuláře se objeví nová možnost na horní liště okna
výše filtrů, kde je možné specifikovat, zda se jedná o :guilabel:`jakýkoliv` :icon:`fa-caret-down`,
:guilabel:`všechny“ :icon:`fa-caret-down“ podmínek by mělo odpovídat.
Je důležité nastavit správně, protože ovlivňuje způsob řízení filtru při návratu dat.

Klikněte na výchozí položku „Všechny“ a zkontrolujte, že je zaškrtnutá položka „Všechny“.
:ikona „fa-caret-down“ je vybrána místo ní, což znamená, že se zobrazí pouze záznamy, které odpovídají
Všechny pravidla, která jsou uvnitř formuláře.

.. crm/track_leads/phone-number:

Kontaktní metoda
~~~~~~~~~~~~~~

.. poznámka::
Následující instrukce není nutná, je však doporučována k přidání kontaktního bodu.
hodnotu pro kritéria vyhledávání zprávy. Mnoho spamu, duplicitních nebo nízká kvalita kontaktů může snadno
zpráva jednoduše vyřadit tím, že se do ní přidá buďto sada :guilabel:`Telefon`.
:guilabel:`E-mailová“ pravidla.

Přidejte další pole s názvem „Nový pravidlo“ do formuláře a nastavte první položku na první položku
Vyberte „Telefon“ a v druhém poli vyberte možnost „Je nastaven“.
Vybráním tohoto operátora se filtruje pouze na záznamy, které mají telefonní číslo spojené s
vůdce.

Alternativně (nebo navíc výše uvedenému pravidlu) klikněte na tlačítko „Nový řádek“ a nastavte první pole
Vyberte „E-mail“. V druhém poli vyberte možnost „je nastaven“.

Tyto pravidla přidávají do zprávy pouze kontakty s asociovaným způsobem komunikace.

... _crm/track_leads/aktivní stav:

Aktivní stav
~~~~~~~~~~~~~

Klikněte na ikonu „fa-sitemap“ vedle řádku „Telefon je nastaven“.
přidat novou pravidla, která vycházejí z předchozích pravidel.

Dva svislé řádky se zobrazují pod čarou, která znázorňuje:
:guilabel:`of:` možnost. Tato volba filtruje záznamy, které splňují **kteroukoliv z pravidel** obsažených v
vnitřní. Tento používá stejnou logiku jako operátor „nebo“ („|“).

Zadejte do prvního pole hodnotu „Aktivní“. Pak vyberte možnost „Je nastaveno“ pro další pole.

Dále klikněte na tlačítko „Přidat nové pravidlo“ vedle položky „Aktivní je nastavená“.
Vytvořit novou řadu polí pod ním.

V prvním poli nastavte hodnotu na „Aktivní“. V dalším poli vyberte možnost „Není nastaveno“.

.. obrázek: lead_distribution_report/active-set.png
:align:center
:alt:Použijte aktivní, pokud chcete zahrnout stav aktivního v reportu.

Tato pravidlo přidává aktuální stav kontaktu do zprávy.

.. poznámka::
Aktivní stav je důležitý filtr, který byste měli zahrnout při vytváření reportu o distribuci leadů, protože
Zahrnuje všechny kontakty bez ohledu na stav vyhrané/prohrávající nebo aktivní/neaktivní v zprávě.
Poskytuje komplexní pohled na všechny případy, které jsou přiřazeny každému členovi prodejního týmu.

Seskupit podle
~~~~~~~~

Jakmile jsou všechny filtry nastaveny, klikněte na tlačítko „Přidat“ a přidejte tyto filtry do vyhledávací lišty.
Pro správné seskupení zprávy klikněte na ikonu „svislý šipka dolů“ .
ikonu vpravo od vyhledávací lišty a klikněte na :guilabel:Prodejce v :guilabel:Skupině.
Sekce „Výsledky“. Všechny výsledky jsou nyní seskupeny podle prodejce, který byl k dané poptávce přiřazen.

Jakmile jsou nastaveny pravidla filtru, klikněte na tlačítko „Potvrdit“ v dolní části.
nabídku pro uložení vlastního filtru a zavřít nabídku.

Dashboard „Analýza potrubí“ je nyní opět zobrazován při každém filtračním pravidle.
vyhledávací lišta.

Klikněte na ikonu „fa-area-chart“ (Graf) vedle vyhledávací lišty, abyste zobrazili
zprávu ve formě sloupcového grafu. Pokud chcete, můžete kliknout na ikonu „OI View List“ (Seznam)
zobrazit v seznamu sestaveném podle skupin.

..tip:
Chcete-li si filtr uložit tak, abyste jej mohli snadno znovu použít, klikněte na tlačítko „Uložit aktuální vyhledávání“.
tlačítko v sekci „Oblíbené“ v rozbalovacím menu vyhledávací lišty.

Nyní zadejte název filtru do pole pod textovým polem níže. Zatrhněte políčko „Sdílený“ a
Poté je filtr sdílen s každým uživatelem, který má přístup k trase. Nakonec klikněte na fialovou
:guilabel:`Uložit“ tlačítko pod filtrem, abyste jej uložili.

Filtr se nyní objeví pod jménem, které mu bylo dáno v části „Oblíbené“ pod ikonou
je vyvolána kliknutím na ni a lze ji znovu použít kliknutím na ni.

Filtr pro kvalitní leady
------------------------

Následující dodatkové podmínky jsou uvedeny jako příklad dobrého, ale ne kompletního
sady pravidel pro hledání kvalitních leadů. Tyto filtry by měly být aplikovány na
:ref:`crm/track_leads/essential-filters` v pořadí, jak je uvedeno, aby bylo dosaženo velmi podrobného
filtr.

- **Zdroj odkazu:** Filtr pro doporučení, například podle objednání nebo člena prodeje.
- **Zdroj:** Filtr pro konkrétní zdroje UTM, například Facebook nebo LinkedIn.
- **Poznámky:** Filtr pro vnitřní poznámky.
- **Štítky:** Filtr pro kategorické štítky.
- **E-mail:** Filtrujte e-maily konkrétních domén, jako je například gmail.com nebo yahoo.com.
- Prodejce: Filtr pro kontakty spojené s určitými členy prodejního týmu.

Tyto podmínky lze přidat, odstranit nebo upravit tak, aby nejlépe vyhovovaly požadovaným informacím.
reportáž.

.. viz též:
   - :ref:`kvalita_vlajek_report/přidat_kvalitní_pravidlo“
   - :doc:`../../../základy/vyhledávání`
