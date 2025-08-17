======
Jordánsko
======

.. _lokalizace_jordánsko/konfigurace/moduly:

Moduly
=======

Následující moduly jsou nainstalovány automaticky s jordánskou lokalizací:

.. seznam tabulkový::
:hlavičkové řádky: 1
:šířky: 25 25 50

   * Jméno
     - Technické označení
     - Popis
   * – :guilabel:Jordánská účetnictví
     - „l10n_jo“
     - Jordánské:„daňová balíček místní <fiscal_localizations/packages>“, včetně
Jordánský účetní systém, daně, daňový výkaz a fiskální pozice
   * :- guilabel:Elektronické fakturace v Jordánsku
     - „l10n_jo_edi“
     - Modul pro integraci do JoFotary k podpoře požadavků Jordánska na elektronické faktury

.. poznámka::
V některých případech, například při upgrade na verzi s dalšími moduly, je možné, že
Moduly nemusí být nainstalovány automaticky. Chybějící moduly lze ručně :ref:`nainstalovat
<obecné/instalace>.

.. viz též:
:doc:`Dokumentace k místnímu nastavení platů v Jordánsku <../../hr/payroll/payroll_localizations/jordan>`

..._lokalizace/Jordánsko/Specifika:

Přehled lokalizace
=====================

Jordánský balíček místní úpravy zajišťuje soulad s jordánským daňovým a účetním systémem.
směrnice. Obsahuje nástroje pro správu daní, fiskální pozice, výkaznictví a předdefinované
účetní kniha přizpůsobená jordánským standardům.

Balíček místní jordánské lokalizace poskytuje následující klíčové funkce, které zajišťují soulad s
lokální daňové a účetní předpisy:

- :doc:`../účetnictví/začínáme/rozvaha“: předdefinovaný strukturu přizpůsobený jordánským
účetní standardy
- :ref:`localizations/jordan/taxes`: přednastavené sazby daně včetně základní DPH, nulové sazby a
a volitelné možnosti
- :doc:`../accounting/taxes/fiscal_positions`: automatické daňové úpravy podle zákazníka nebo
stav registrace dodavatele
- :ref:`localizations/jordan/tax-reporting`: podrobný přehled vaší daňové povinnosti
- „Elektronické fakturace (JoFotara)“: integrace elektronických faktur
v souladu s požadavky jordánské vlády

..._lokalizace/Jordánsko/daně:

Daně
-----

Výchozími jsou následující daně:
lokalizační balíček:

- standardní daň z prodeje (16 %): aplikována na většinu produktů a služeb v Jordánsku.
- osvobozené transakce: prodeje a služby osvobozené od DPH, jako jsou finanční služby nebo
zdravotnictví.
- Exportní daň (0 %): nulová sazba daně, která se vztahuje na zboží a služby vyvážené mimo Jordánsko.

... /lokalizace/Jordánsko/Daňové hlášení:

Daňové přiznání
-------------

Podrobné rozdělení naleznete v souboru :doc:`Daňový přehled <../accounting/reporting/tax_returns>`.
Daňové transakce, nulové sazby a osvobozené transakce. Stejně jako ostatní finanční zprávy
<../účetnictví/reporting>“, lze výpis DPH filtrovat podle období a porovnat s jinými.
době a exportovány ve formátech Excelu a PDF, což zajišťuje soulad s daňovými zákony Jordánska.

..._lokalizace/jordánsko/jofotara:

Elektronická fakturace s JoFotarou
=========================

Elektronické fakturace s JoFotarou je integrována do Odoo a zajišťuje tak soulad s jordánským vládním nařízením
technické a právní požadavky na elektronickou fakturaci. Integrace JoFotary do Odoo je možná
spojuje s jordánskou elektronickou fakturační platformou, což umožňuje společnostem:

- vytvářet elektronické faktury v souladu s platnými předpisy
- zasílat faktury v reálném čase k ověření
- sledovat stavy faktur přímo v Odoo

Pro integraci je nejprve nutné vytvořit účet u společnosti JoFotara a následně vygenerovat přihlašovací údaje k API.
a nakonec zadat tyto údaje do databáze Odoo, aby se obě zařízení propojila.

... _návody: https://istd.gov.jo/EN/List/Electronic billing User Manual

„Návody pro vládu“ (manuals_) poskytují pokyny k vytvoření účtu a generování API
Kvalifikace.

... /lokalizace/jordánsko/konfigurace jofotary:

Konfigurace
-------------

..._lokalizace/jordánsko/propojení_Jofotary:

Propojit Odoo s JoFotarou
~~~~~~~~~~~~~~~~~~~~~

#Pokud účet ještě nemáte, vytvořte si ho kliknutím na odkaz „Návody pro vládu“ (manuals_)
stránce a postupujte podle kroků v návodu pro připojení k jordánskému národnímu
Elektronický systém fakturace**.
#Vytvořte klíčové údaje API (číslo aktivity, tajný klíč a identifikátor klienta) přechodem na stránku „government
návodů a postupovat podle pokynů v **Příručce pro propojení s
Jordánský národní systém elektronické fakturace**.
#Ve vaší databázi Odoo přejděte na: „Účetnictví > Konfigurace > Nastavení“.
:guilabel:`Elektronické fakturace (Jordánsko)` sekci a zadejte přihlašovací údaje k API vytvořené
dříve:

   - :guilabel:`Číslo aktivity“ (pořadí zdroje příjmů).
   - :guilabel:`Tajný klíč JoFotary“
   - :guilabel:`ID klienta JoFotara“

#Zadejte:guilabel:„Typ daňového poplatníka“:

   - :guilabel:`Nepřihlášená k dani z přidané hodnoty“ pro podnikatele, kteří nejsou přihlášeni k DPH. Bez daně
na faktuře je nutné uvést.
   - :guilabel:`Registrováno k DPH“ pro podniky registrované u běžné sazby DPH
systému. Na každou řádek faktury je nutné vypočítat jeden daňový odvod jako procento.
   - :guilabel:`Zaregistrováno k dani z přidané hodnoty“: pro podnikatele, kteří jsou registrováni k DPH
předpisy. Je nutné stanovit jednu daň jako procento z obratu a druhou pevnou částku za každý řádek faktury
za fakturu.

#Klikněte na tlačítko „Uložit“.

.. tip::
Pokud v sekci „Elektronické fakturace (Jordánsko)“ chybí
:guilabel:`Nastavení“, zkontrolujte, že modul „Elektronické fakturace Jordánska“ je nainstalován.
<obecné/instalace>.

..._lokalizace/jordánsko/firma-a-kontakty:

Společnost a zákazníci
~~~~~~~~~~~~~~~~~~~~~

Proces fakturace společnosti JoFotara vyžaduje informace o adrese spojené s firmou, která vystavila
faktury a jejich příjemci:

#Přejděte do sekce „Nastavení“ -> „Uživatelé a společnosti“ -> „Společnosti“ a vyberte společnost,
Bude používat JoFotaru.
#Vyplňte pole „Název společnosti“, „Daňové identifikační číslo“ (DIČ) a „Země“. Pokud
požadované, doplňte další nepovinné pole jako např. :guilabel:`Ulice`, :guilabel:`Město“
:guilabel:`Stát“ a :guilabel:`Zip“.

.... důležité::
      - Země musí být nastavena na Jordánsko.
      - Název společnosti musí odpovídat názvu, který je zapsán v příjmech a výdajích.
Sales Tax Department (ISTD).
      - Firma musí nastavit měnu na „JOD“.


#Přejděte na: menu „Účetnictví“ -> „Zákazníci“ -> „Zákazníci“.
#Pro každého zákazníka, pro kterého budou faktury odesílány do JoFotary, klikněte na zákazníka a otevřete formulář.
Výhled a doplňte pole „Země“ a „Daňové identifikační číslo“. Pokud chcete, můžete vyplnit další
volitelné pole jako například „Ulice“, „Město“ nebo „Stát“.
:guilabel:`ZIP“.

... /lokalizace/Jordánsko/zasílání faktur:

Vystavování faktur přes Odoo
-------------------------------------

Jakmile je společnost propojena s JoFotarou <localizations/jordan/linking-jofotara>
Společnost a zákazníci jsou správně nakonfigurováni.
<lokalizace/jordánsko/firma-a-kontakty>“, faktury lze zaslat na JoFotaru přes Odoo:

#Přejděte do sekce „Účetnictví“ – „Zákazníci“ – „Faktury“ a otevřete potvrzenou fakturu.
faktura.
#Klikněte na tlačítko „Odeslat“.
#V okně „Odeslat“ vyberte „Jofotara (Jordan EDI)“ a klikněte na
:guilabel:`Odeslat“.

Když je faktura odeslána do JoFotary, Odoo provede následující:

- vytváří fakturu v požadovaném formátu (UBL 1.2).
- fakturu předává ke kontrole společnosti JoFotara
- obdrží QR kód od JoFotary na faktuře ve formátu PDF

.. tip::
   - Může být zasláno více faktur najednou:ref:`<účetnictví/faktura/odeslání>“ do JoFotary.
   - V zobrazení seznamu faktur filtrujte faktury podle jejich
:ref:`lokalizace/jordánsko/fotografie státu Jordánska` a zobrazit faktury, které byly buď vystaveny nebo
nebyly zaslány do JoFotary.
   - V nabídce „Nastavení“ (ikona „nastavení“) přidejte
:guilabel:`Stav JoFotara“ a :guilabel:`Chyba JoFotara“ pole, abyste viděli stav odeslání
případných chyb v seznamovém zobrazení.

.. důležité::
Vzhledem k tomu, že se v Odoo a ISTD přibližují hodnoty jinak, je zde zásadní rozdíl.
různé architektury systému. Hodnoty JOD v Odoo jsou uloženy a přibližovány na tři desetinná místa.
Výsledky byly zveřejněny v pátek na webových stránkách společnosti ISTD, která očekávala, že výsledek bude mít devět desetinných míst.
nevyhnutelný a vzniká mezi hodnotami uloženými v Odoo a hodnotami předanými do ISTD.
může být chyba menší než 0,001.

..._lokalizace/Jordánsko/Jofotara stát:

Stát JoFotara
~~~~~~~~~~~~~~

V poli „Stát“ v záložce „Další informace“ potvrzených faktur
odráží aktuální stav dokumentu v JoFotarovi a lze ji ručně změnit tak, aby odpovídala
skutečný stav faktur v případě, že technický problém nebo časový limit zabrání Odoo ve změně
automaticky.

..._lokalizace/jordánsko/QR kódy:

Validace QR kódů (Aplikace Sanad)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Zkontrolovat QR kód odeslaný z JoFotary na faktuře provedete takto:

#Nainstalujte aplikaci „Sanad“ (<https://www.sanad.gov.jo/Default/en>).
#Navigujte do sekce „Více“.
#Klikněte na tlačítko „Potvrdit dokument“ a naskenujte kód QR.
#Zpětná vazba.

... /lokalizace/jordánsko/platební karta:

Dodací a fakturační listy
~~~~~~~~~~~~~~~~~~~~~~

Chcete-li odeslat fakturu nebo kreditní poznámku společnosti JoFotara, nejprve vytvořte :ref:`faktura
<účetnictví/přijaté faktury/vystavení debetní poznámky> nebo :ref:`pozvánka na debet
<účetnictví/vystavení kreditní faktury/vydání kreditní faktury>. V okně „Odeslat“ klikněte
:guilabel:`JoFotara (Jordan EDI)` a předložit ho k reálnému ověření. Po úspěšném ověření
QR kód od JoFotary je vložen do PDF faktury nebo zálohové faktury.

.. poznámka::
Zajistěte, aby důvod vytvoření faktury odpovídal ISTD
předpisy.

... /lokalizace/jordánsko/slevy:

Slevy
~~~~~~~~~

JoFotara nepodporuje záporné částky ani záporné ceny na fakturačních řádcích.
funkce globálního slevového kupónu a pevné částky není podporována.

Slevy se musí uplatnit **na každé řádku faktury jako procento** místo celkové slevy nebo
fixní částka.

.. varování:
Pokus o odeslání faktury s negativními položkami do JoFotary bude vyhodnocen jako neplatná
chyby.

.. viz též:
:ref:`Druhy slev <sales/discounts/discount-button>`
