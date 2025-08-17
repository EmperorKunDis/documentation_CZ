===========
Filipíny
===========

Konfigurace
=============

Instalovat balíček pro daňovou lokalizaci pro Filipíny:
<fiskální lokality/balíčky> získat všechny výchozí účetní funkce Filipín
lokalizaci, například účetní knihu, daně a zprávy. Tyto poskytují základní šablonu pro začátek
začal používat filipínské účetnictví.

.. poznámka::
  - Při vytváření nové databáze a výběru Filipín jako země se fiskální
modul pro lokalizaci **Filipíny – Účetnictví** je automaticky nainstalován.
  - Pokud se modul instaluje do již existující společnosti, pak se vytvoří
nebude nahrazen, pokud již existují zveřejněné záznamy.

Účetní kniha a daně
---------------------------

Nainstalována je minimální konfigurace výchozího rozvrhu účtů a následující typy daní
nainstalován a propojen s příslušným účtem:

- DPH při prodeji a nákupu 12 %
- DPH z prodeje a nákupu osvobozeno
- DPH z nulové sazby
- Srážky z prodeje a nákupu

Pro srážkové daně (v menu „Účetnictví“ -> „Konfigurace“ -> „Daně“) je
Další pole „ATC Filipíny“ pod záložkou „Filipíny“.

.. obrázek: filipíny/filipíny-atc-kód.png
:alt: Filipínské kódy letištních řídicích věží nastavené na daně.

.. poznámka::
ATC kód daně se používá pro :ref:`daňový formulář BIR 2307 <lokalizace/filipíny/zpráva-BIR1207>`.
:ref:`Zprávy SAWT a QAP <lokality/filipíny/zpravy-QAP-SAWT>“. Pokud je zavedeno nové zdanění,
Pokud je v systému ručně přidán jeho kód ATC,

Kontakty
--------

Když je kontakt s firmou nebo jednotlivcem (nepracujícím pro firmu) umístěn na Filipínách
Vyplňte pole „Daňové identifikační číslo“ číslem „Identifikátoru poplatníka daně (TIN)“.

Pro osoby nepatřící do společnosti použijte následující další pole:

- :guilabel:`Jméno a příjmení“
- :guilabel:`Střední jméno“
- :guilabel:`Příjmení`

.. poznámka::
Pro oba subjekty, ať už jde o společnost nebo fyzickou osobu, by měl následovat
Formát „NNN-NNN-NNN-NNNNN“. Kód pobočky by měl následovat poslední číslice DIČ nebo jinak.
Může zůstat jako „00000“.

Zprávy
=======

..._lokalizace/filipíny/zpráva_BIR1207:

Zpráva BIR 2307
---------------

**BIR 2307** hlásí také známý jako „Certifikát o sražené dani z příjmu
<http://www.bir.gov.ph/bir-forms?tab=Certificates&idTag=BIR2307&datasetCode=3381&label=2307&type=TAB%20LINK>
Může být vygenerován pro nákupní objednávky a platby dodavatelům s příslušnými odpočty daně z přidané hodnoty.

Pro vytvoření výkazu BIR 2307 vyberte jeden nebo více faktur od dodavatele z přehledového seznamu a klikněte
:menu:Akce --> Stáhnout soubor BIR 2307 XLS.

.. obrázek: filipíny/filipíny-multibil.png
:alt:Výběr více faktur od dodavatelů s akcí „Stáhnout BIR 2307 XLS“.

.. tip::
Stejnou akci lze provést i na faktuře dodavatele z pohledu formuláře.

V okně, které se otevře, zkontrolujte výběr a klikněte na tlačítko „Generovat“.

.. obrázek: filipíny/filipíny-generovat.png
:alt:Příkazové okno pro generování souboru XLS s formulářem BIR 2307.

Tímto vytváří soubor „Form_2307.xls“, který obsahuje všechny řádky faktur dodavatelů s příslušnými
Srážková daň.

Proces výše lze použít i pro jediného dodavatele, pokud jde o platbu :doc:`faktury <../accounting/invoices>`.
Je spojen s jedním nebo více fakturami dodavatele (:doc:`<../accounting/payments>`) se zaplacenou daňovou srážkou.
daně.

.. poznámka::
  - Pokud se neaplikuje srážková daň, pak soubor XLS nebude generovat záznamy pro tyto dodavatele.
řádky účtu.
  - Při skupinovém placení za více faktur Odoo rozděluje platby podle kontaktu.
platbu, kliknutím na „Akce“ -> „Stáhnout formulář BIR 2307 XLS“ vytvoříte zprávu.
pouze faktury dodavatelů, které souvisí s tímto kontaktem.

.. důležité::
Odoo nemůže vytvářet PDF zprávu nebo soubory DAT přímo.
:soubor: Form_2307.xls lze exportovat do externího nástroje pro převod na formát BIR DAT nebo PDF
formátu.

Zpráva SLSP
-----------

Pro přístup k zprávě „Shrnutí prodeje a nákupu“ (Summary List of Sales and Purchases) přejděte na
:menuvolba:`Účetnictví -> Zprávy -> Souhrnný seznam prodejů a nákupů“.

Klikněte na tlačítka v horní části obrazovky, abyste zobrazili požadovaný výkaz:

- Výběr „Prodeje“ pro zprávu „Souhrnné seznamy prodejů“.
|V této zprávě jsou uvedeny všechny faktury zákazníků včetně aplikovaných daní z přidané hodnoty.
- Pro zprávu „Shrnutí nákupů“ je vhodné použít štítek „Nákupy“.
|V tomto výkazu jsou uvedeny všechny faktury dodavatelů spolu s příslušnými daněmi z přidané hodnoty.

.. obrázek: filipíny/slsp.png
:alt:Zpráva SLSP

Výchozí nastavení obou reportů vylučuje záznamy o příjmech a výdajích bez čísla daňového identifikačního kódu.
s daní z dovozu. Chcete-li je vidět nebo skrýt, klikněte na „Možnosti“ a vyberte
Požadovaný filtr:

- :guilabel:`Včetně partnerů bez DIČ“
- :guilabel:`Včetně dovozů“

Pro export souhrnného seznamu prodeje a nákupu klikněte na tlačítko „Export
SLSP.

.. důležité::
Odoo nemůže přímo generovat soubory DAT. Funkce „Export SLSP“ a „XLSX“
tlačítka se používají k exportu souboru XLSX, který lze zpracovat pomocí externího nástroje.
převést ho do formátu DAT.

Deklarace k dani z příjmů fyzických osob za rok 2018
----------------

Daňový výkaz je dostupný po kliknutí na:
Výkaz zisku a ztráty - daňový výkaz --> 2550Q (P)H. Formulář je postaven na nejnovější verzi *2550Q
Čtvrtletní přiznání k dani z přidané hodnoty* verze ledna 2023.

.. obrázek: filipíny/2550Q.png
:alt: Daňový výkaz

.. tip::
Většina řádků v daňovém přiznání je automaticky vypočítána na základě daní.
zpracování a podání daňového přiznání lze manuální účetní operace také napojit na daňový
přednastavené **Daňové sítě** pro každou řádek daňového hlášení.

.. důležité::
Odoo nemůže přímo vytvářet PDF zprávu ve formátu BIR 2550Q. Mělo by se používat jako
jako odkaz při ručním nebo elektronickém podání formuláře mimo území Spojených států.

... /filipíny/zpráva QAP SAWT:

Zprávy QAP a SAWT
------------------

Pro přístup k :abbr:`QAP (Quarterly Alphalist of Payees)` a :abbr:`SAWT (Summary Alphalist of
Daň z příjmu právnických osob) podávat, přejděte do sekce „Účetnictví“ - „Zprávy“ - „Výkaz zisku a ztrát“, klikněte
tlačítko „Zpráva“ s ikonou „Kniha“, vyberte „Sawt a Qap (PH)“.

Klikněte na tlačítka v horní části obrazovky, abyste zobrazili požadovaný výkaz:

- :guilabel:`SAWT“ pro zprávu „SAWT (Souhrnná alfalistina srážkové daně)“.
|Všechny faktury zákazníků s příslušnými odpočty daně z přidané hodnoty jsou zde uvedeny.
zpráva.
- :guilabel:`QAP“ pro zprávu „QAP (Quarterly Alphalist of Payees)“.
|V tomto výkazu jsou uvedeny všechny faktury dodavatelů spolu s příslušnou daňí z přidané hodnoty.

.. obrázek:: filipíny/filipíny-sawt.png
:alt:Hlášení SAWT a QAP

Exportovat souhrnné seznamy srážkových daní SAWT (Summary Alphalist of Withholding Tax) a čtvrtletní
Seznam příjemců (Alphalist of Payees) ve formátu XLSX, klikněte na: guilabel: Export SAWT a QAP.

.. důležité::
Odoo nemůže vytvářet soubory DAT přímo. Pomocí funkce :guilabel:`Export SAWT & QAP`
:guilabel:`XLSX“ tlačítka slouží k exportu souboru ve formátu XLSX, který lze zpracovat pomocí
*externí* nástroj pro převod na formát DAT.

Tisk šeků
==============

Filipínský šekový tisk má podobu nejnovějšího PCHC (Philippine Clearing House
Standardizovaný formát korporace). Chcete-li tisknout šeky, přejděte na „Účetnictví“ ->
Konfigurace --> Nastavení, povolit „Zkontrolovat“ a nastavit „Vzhled kontrolky“ na
„Tisková kontrola - PH“.

Šeky se tisknou podle standardního postupu uvedeného v příručce „Standardní postup tisku šeků“ (viz též účetnictví, platby, platby šekem).
