============================
Daňové přiznání (DPH)
============================

Společnosti s registrovaným číslem DPH musí podat daňové přiznání
měsíčně nebo čtvrtletně podle výše obratu a podle registračního režimu. Daň
Daňový doklad poskytuje finančnímu úřadu informace o zdanitelných transakcích.
Společností. Výstupní daň je účtována na počet prodaných zboží a služeb
podnikání a vstupní daň je daní přičítaná k ceně zboží nebo služeb
koupené. Na základě těchto hodnot může společnost vypočítat daň, kterou musí zaplatit nebo
Vráceny.

.. poznámka::
Na této stránce Evropské komise se dozvíte víc o DPH a jeho fungování.
Komise: „Co je DPH?“ <https://ec.europa.eu/taxation_customs/business/vat/what-is-vat_en>.

.. daňového přiznání/předpokladů:

Předpoklady
=============

... daňových přiznáních/četnost:

Četnost podání daňového přiznání
----------------------

Konfigurace období podání daně umožňuje Odoo správně vypočítat vaši daňovou povinnost.
A také vám poslat upozornění, abyste nikdy nezmeškali termín pro podání daňového přiznání.

K tomu přejděte na: „Účetnictví -> Konfigurace -> Nastavení“. V sekci
V poli „Perioda daňového přiznání“ můžete nastavit:

- :guilabel:`Periodicita“: zde definujte, zda podáváte daňové přiznání měsíčně nebo čtvrtletně.
základní
- :guilabel:`Poznámka k dani z příjmu`: nastavte, kdy by měl Odoo upomínat na podání daňového přiznání.
- :label:Časopis: vyberte časopis, do kterého se má zaevidovat daňové přiznání.


.. poznámka::
To se obvykle nastavuje během prvotní konfigurace aplikace (viz dokumentaci k instalaci).

... daňové přiznání / daňová síť:

Daňové sítě
---------

Odoo vytváří daňové zprávy na základě nastavení „Daňových sítí“ (Guilabel: Tax Grids), které jsou konfigurovány ve vašem
daně. Proto je důležité zajistit, aby všechny zaznamenané transakce používaly správné daně.
Můžete vidět „Daňové sazby“ v záložce „Položky účetní knihy“.
faktura a daňový doklad.

.. obrázek: daňová přiznání/součty daně.png
:alt: podívat se, které daňové sítě slouží k evidenci transakcí v účetnictví Odoo

Pro konfiguraci sazeb daně přejděte na: „Účetnictví --> Konfigurace --> Daně“.
a otevřít daňovou sazbu, kterou chcete upravit. Tam můžete upravit své nastavení daně spolu se sazbou
sítě, které se používají k evidenci faktur nebo vrácených peněz.

.. poznámka::
Daňové přiznání a reporty jsou obvykle již předem nakonfigurované v Odoo: fiskální balíček
<fiscal_localizations/packages> je nainstalována podle země, kterou si zvolíte při vytváření
vaší databáze.

... daňové přiznání/zavřít:

Uzavření daňového období
==================

... daňové přiznání / datum uzamčení:

Datum daňového uzamčení
-------------

Každá nová transakce, jejíž účetní datum předchází datu „Zamknout daňové přiznání“, má svou daň
hodnoty přesunuly do dalšího otevřeného daňového období. To je užitečné, protože se tak zajistí, že nemůže být proveden žádný zásah
výroční zprávu, jakmile skončí její období.

Proto doporučujeme uzamknout datum daně před prací na
:guilabel:`Závěrečný zápis do knihy“.
Takto nemohou ostatní uživatelé měnit nebo přidávat transakce, které by měly vliv na
„Závěrečný záznam“, který vám může pomoci vyhnout se některým chybám při podání daňového přiznání.

Chcete-li zkontrolovat aktuální datum „Zamknutí daňového přiznání“ nebo jej upravit, přejděte na
:menuselection:`Účetnictví --> Účetnictví --> Zámek dat“.

... daňového přiznání/výkazu:

Daňové přiznání
----------

Jakmile budou všechny transakce s daněmi za období, které chcete zobrazit, uloženy, otevřete
Vygenerovat zprávu „Daňové přiznání“ kliknutím na položku „Účetnictví -> Zprávy -> Daňové přiznání“.
Vraťte se“. Vyberte období, které chcete prohlásit pomocí filtru data a zobrazí se vám přehled daně.
návrat. Pak klikněte na položku „Zavírací vstup“ pro vytvoření daňového závěrkového záznamu.
automaticky navrhne podrobnosti záznamu. Udělejte všechny potřebné změny a klikněte
:label:„Pozvánka“.

Ve zprávě klikněte na tlačítko „PDF“ pro stažení PDF daňového přiznání. Nebo klikněte na
Ikona „Nástroje“ (ikona s nářadím) a poté klikněte na „Stáhnout Excel“.
daňové přiznání. Chcete-li uložit zprávu do aplikace Dokumenty, klikněte na ikonu „gear“
ikona, pak klikněte na „Kopírovat do dokumentů“. Vyberte formát pro „Exportovat do“
„Název dokumentu“, složku pro uložení a přidat libovolné „Štítky“.

Zpráva obsahuje všechny hodnoty k vykazování na finanční úřad včetně částky, kterou je třeba
zaplacené nebo vrácené.

.. poznámka::
Pokud jste zapomněli uzavřít daňové období před kliknutím na položku „Záznam o ukončení účetního období“, pak
Odoo automaticky uzamkne váš daňový období na stejný den jako účetní datum vašeho
vstupu. Tato bezpečnostní opatření mohou zabránit některým daňovým chybám, ale je doporučeno zamknout
datum ručně předtím, jak je popsáno výše.

.. důležité::
   - Jakmile je vygenerován daňový doklad za určité období, ale nebyl dosud zveřejněn, může být vystaven další faktura.
Pokud jde o účty z téže období, lze je stále vytisknout a zaúčtovat jako součást uzavíracího zápisu.
Klikněte na ikonu „Oi Arrow Right“ a poté na „Obnovení“ v nabídce „Návrh zavření daně“.
záznam v deníku, nebo klikněte na „Závěrečný záznam“ z daňového hlášení.
   - Po zveřejnění daňového hlášení je období uzamčeno a zabráněno dalšímu
vytváření nových účetních záznamů, které se týkají DPH. Když provedete opravy faktur pro zákazníky nebo dodavatele
Poté musí být faktury zaznamenány v následujícím období.

.. viz též:
   * :doc:`../dane`
   * :doc:`../začínáme“
   * :doc:`/fiscal_localizations`
