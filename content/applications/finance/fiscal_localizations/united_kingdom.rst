==============
Spojené království
==============

..._lokalizace/británie/moduly:

Konfigurace
=============

Instalujte modul UK – Účetnictví a modul UK – Účetnictví
Moduly zpráv dostanou všechny funkce lokace Spojeného království.

.. seznam tabulkový::
:hlavičkové řádky: 1

   * Jméno
     - Technické označení
     - Popis
   * -- :guilabel:`Účetnictví UK“
     - l10n_cz
     -  -Účetní kniha připravená pro CT600
        - Struktura daně připravená na VAT100
        - Seznam anglických hrabství od společnosti Infologic
   * --:guilabel:`Velká Británie - Účetní zprávy“
     - „l10n_uk_reports“
     -  -Účetní zprávy pro Spojené království
        - Umožňuje odesílat daňový přiznání k DPH pomocí rozhraní MTD-VAT API na HMRC.
   * – :guilabel:`Britské soubory platebních příkazů BACS“
     - „l10n_uk_bacs“
     - Umožňuje vytvářet soubory pro platby faktur a účtů :ref:`lokalizace/jednotné království/BACS`.
   * --:guilabel:`Spojené království - Schéma pro stavební průmysl“
     - l10n_uk_reports_cis
     -  - umožňuje odeslat měsíční daňový přiznání HMRC
        - Zpráva o odpočtu pro stavební průmysl ve Spojeném království
   * --:guilabel:`Velká Británie - HMRC API“
     - „l10n_uk_hmrc“
     - Zahrnuje základy HMRC.

.. poznámka::
   - Pouze britské společnosti mohou podávat zprávy HMRC.
   - Instalací modulu :guilabel:`UK - Účetní výkazy` se nainstalují oba dva moduly najednou.
   - Modul :guilabel:`UK - Construction Industry Scheme` automaticky zahrnuje
:guilabel:`Modul UK - HMRC API“ během instalace.

.. viz též:
   - „Daňové a celní úřady <https://www.gov.uk/government/organisations/hm-revenue-customs/>“
   - Přehled o DigiTax
<https://www.gov.uk/government/publications/making-tax-digital/overview-of-making-tax-digital/>

.._lokalizace/británie/účetní kniha

Klasifikační schéma
=================

Účetní kniha Spojeného království je součástí modulu :guilabel:`UK - Accounting`. Přejděte na
:menu-vyber->Účetnictví-->Nastavení-->Účetnictví: Skladová kniha

Nastavte si :abbr:`CoA (účetní knihu)“ přes menu „Účetnictví -> Konfigurace
→ Nastavení → Sekce „Účetní import“ a vyberte možnost: „Zkontrolovat ručně“ nebo
:guilabel:`Přeneste počáteční zůstatky (doporučeno).“

.. _lokalizace/británie/daně:

Daně
=====

Součástí lokální modulace je automatické vytváření daně z UK s příslušnými finančními
účty a konfigurace.

Přejděte na: „Účetnictví“ -> „Konfigurace“ -> „Nastavení“ -> „Daně“.
„Výchozí daně“, „Četnost podání daňového přiznání“ nebo „Nastavení vašeho
Daňové účty.

Pro úpravu stávajících daní nebo pro vytvoření nové daně přejděte na :menuselection:`Účetnictví -->
Konfigurace --> Účetnictví: Daně.

.. viz též:
   - :doc:`dani <../účetnictví/daně>`
   - Návod: „Daňové přiznání a hlášení
<https://www.odoo.com/slides/slide/dane-zpravy-a-vratky-1719?fullscreen=1>.

..._lokalizace/jednotné-království/digitální daň:

Making Tax Digital (MTD)
------------------------

Ve Velké Británii musí všechny podniky registrované k DPH dodržovat pravidla MTD a využívat ke zpracování dat softwarové aplikace.
daňové přiznání k DPH.

Modul UK – Účetní zprávy umožňuje splnit požadavky HM Revenue & Customs.
<https://www.gov.uk/government/organisations/hm-revenue-customs/>_ požadavky týkající se
„Daňová digitální transformace
<https://www.gov.uk/government/publications/making-tax-digital/overview-of-making-tax-digital/>`.

.. důležité::
Pokud je vaše periodická podání pozdější než o tři měsíce, již není možné podat
její prostřednictvím Odoo, jelikož Odoo získává pouze otevřené dluhopisy za poslední tři měsíce.
Musí se provést ručně kontaktováním HMRC.

..._lokalizace/jednotné-království/hmrc-registrace:

Registrujte svou společnost u HMRC před první žádostí
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Přejděte do sekce „Účetnictví“ – „Zprávy“ – „Daňový výkaz“ a klikněte na
:guilabel:`Připojit se k HMRC“. Zadejte informace o své společnosti na platformě HMRC.
to udělat jednou.

... _lokalizace/británie/periodické podání HMRC:

Periodické podávání HMRC
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Importujte své povinnosti HMRC, filtrujte podle období, ve kterém chcete předložit daňový přehled a odešlete jej
kliknutím na tlačítko „Odeslat do HMRC“.

.. tip::
Můžete použít falešné přihlašovací údaje k demonstraci průtoku HMRC. Chcete-li tak učinit, aktivujte
:ref:`rozvojový režim <developer-mode>` a přejděte do sekce „Obecné nastavení“.
Technické --> Systémové parametry“. Zde hledejte „l10n_uk_reports.hmrc_mode“ a změňte
hodnotu řádku na „demo“. Tento typ přístupových údajů získáte v aplikaci HMRC Developer Hub.
<https://developer.service.hmrc.gov.uk/api-test-user>.

... _lokalizace/jednotné-království/periodické podání HMRC - více:

Pravidelné podávání HMRC pro více společností
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pouze jedna společnost a jeden uživatel mohou být připojeni k HMRC současně. Pokud existuje více britských společností,
na stejné databázi musí uživatel, který podává zprávu pro HMRC, tyto pokyny dodržet před
každá přihláška:

#Přihlaste se do společnosti, pro kterou má být podání provedeno.
#Přejděte do sekce „Obecné nastavení“ a v části „Uživatelé“ klikněte na
:guilabel:`Spravovat uživatele“. Vyberte uživatele, který je spojen s HMRC.
#Přejděte na záložku „Spojení s UK HMRC“ a klikněte na „Obnovit autentizaci“.
Tlačítko „Přidat ověřovací údaje“ nebo „Odebrat ověřovací údaje“.
#:ref:`Registrujte svou společnost u HMRC <lokalizace/británie/registrace-u-hmrc>“ a podávejte
daňovém přiznání společnosti.
#Opakujte kroky pro podání HMRC ostatních společností.

.. poznámka::
V průběhu této operace se tlačítko „Připojit k HMRC“ již nezobrazuje pro ostatní britské společnosti.
společnosti.

..._lokalizace/velká-británie/bacs-soubory:

Soubory BACS
==========

Elektronické soubory Bacs (Bankers' Automated Clearing Services) se používají ve Spojeném království k
provádět platby a převody mezi bankovními účty.

Pro používání souborů Bacs je nutné zajistit
Pokud je nainstalován modul „UK BACS Payment Files“:

#Nastavte své číslo služby uživatele Bacs:

   #Přejděte na „Účetnictví > Konfigurace > Nastavení“ a posuňte se dolů do
v sekci „Platby zákazníků“.
   #Zadejte své číslo uživatele služby („Service User Number“) do pole „BACS“ a ručně uložte.

#Nastavte si svůj bankovní deník.

   #Přejděte do sekce „Účetnictví“ - „Konfigurace“ - „Deníky“ a vyberte svou **banku**
časopis.
   #V záložce „Příchozí platby“ nastavte číslo účtu a
:guilabel:`Banka“ poli.
   #V záložce „Příchozí platby“ a „Odeslané platby“ se ujistěte, že
:guilabel:`Přímý debet BACS“ je povolen.

#Nastavte kontakty, pro které chcete používat soubory Bacs: Přejděte do formuláře s kontakty a
v záložce „Účetnictví“, klikněte na „Přidat řádek“ a vyplňte
:guilabel:`Číslo účtu“ a :guilabel:`Banka“.

..._lokalizace/jednotné-království/fakturace:

Splátky účtů
-------------

Pro generování souborů Bacs pro platby faktur nastavte pole „Způsob platby“ na
„Direct Debit BACS“ při registraci plateb dodavatelům (<../accounting/payments>).

Pak vytvořte platbu pro dodavatele:

#Přejděte na „Účetnictví“ – „Dodavatelé“ – „Množstevní platby“ a klikněte na „Nový“.
#Vyberte bankovní deník v poli „Banka“ a nastavte způsob platby na
:guilabel:`Direct Credit BACS“, vyberte „Datum zpracování“.
#Můžete také:

   - vyberte datum splatnosti BACS.
   - Zapnout možnost zpracování plateb v režimu BACS Multi Mode na individuální datum.

#Klikněte na tlačítko „Přidat řádek“, vyberte platby, které chcete zahrnout, klikněte na „Vybrat“.
Pak zadejte „Validovat“.

Jakmile je soubor BACS ověřen, je k dispozici v chatu. Můžete také:
Exportovat soubor „Export File“ pokud potřebujete nový soubor pro tuto platbu.

.. obrázek: united_kingdom/bacs-files.png
:alt:Výpis faktur od dodavatele s vygenerovaným souborem BACS.

.. viz též:
:doc:`../účetnictví/platby/souborová platba“

..._lokalizace/jednotné-království/fakturační-platby:

Platby faktur
----------------

Před tím, než vytvoříte soubor pro platbu faktur pomocí Bacs, musíte nejprve vytvořit **BACS Direct Debit.
Návod**: Přejděte na: „Účetnictví“ -> „Zákazníci“ -> „Pokyny k inkasu přes BACS“
a klikněte na „Nový“. Vyberte si „Zákazníka“, jejich „IBAN“ a
:guilabel:`Časopis“ chcete použít.

Pro generování souborů BACS pro platby faktur nastavte pole „Způsob platby“ na
:guilabel:`Direct Debit BACS“ při „registraci plateb faktur <../účetnictví/platební příkazy>“.

.. tip::
Pokud se přihlásíte k platbě faktury spojené s předplatným nebo přes
V menu „Účetnictví -> Zákazníci -> Platby“ můžete vybrat :guilabel:`BACS.
Typ platby:

   - „Převod z účtu - první výběr ze série“
   - „Souběžný inkasní příkaz“
   - „Opakované inkaso z bankovního účtu“
   - :guilabel:`Souhrnná platba - konečné vyúčtování série“.

Pak vytvořte soubor plateb pro zákazníky:

#Přejděte na „Účetnictví“ – „Zákazníci“ – „Množstevní platby“ a klikněte na „Nový“.
#Vyberte bankovní deník v poli „Banka“ a nastavte způsob platby na
:guilabel:`Direct Credit BACS“, vyberte „Datum zpracování“.
#Můžete také:

   - vyberte datum splatnosti BACS.
   - Zapnout možnost zpracování plateb v režimu BACS Multi Mode na individuální datum.

#Klikněte na tlačítko „Přidat řádek“, vyberte platby, které chcete zahrnout, klikněte na „Vybrat“.
Pak zadejte „Validovat“.

Jakmile je soubor BACS ověřen, je k dispozici v chatu. Můžete také:
Exportovat soubor „Export File“ pokud potřebujete nový soubor pro tuto platbu.

... _lokalizace/británie/pracovní_hvězda:

Mzdový systém Employment Hero
=======================

Pokud vaše podnikání již funguje s :doc:`Employment Hero
„<https://www.payroll-hero.com/hr/payroll/payroll_localizations/employment_hero>“, můžete použít náš konektor jako
alternativní řešení pro mzdy.

.. důležité::
Konfigurace služby API pro řešení problémů s zaměstnáváním**
Království**, použijte následující hodnotu jako :guilabel:`URL pro výplatu mzdy“: „https://api.yourpayroll.co.uk/“.

.._lokalizace/británie/daňové slevy:

.. |HMRC| nahradit za: zkratka: HMRC (HM Revenue and Customs)
.. |CIS| nahradit za: zkratku: „CIS (Schéma pro stavební průmysl)“

Odčitatelná položka CIS
=============

Systém slevy pro stavební průmysl (CIS deduction) je daňový odpočet používaný ve Spojeném království.
jejímž cílem je stavebnictví, vyžaduje od dodavatelů určitou slevu
úhradách provedených poddodavatelům a tyto odpočty předat HM Revenue & Customs (HMRC).
Tyto slevy se vztahují pouze na mzdu a slouží jako předplatby.
směrem k dani z přidané hodnoty a pojistnému na sociální zabezpečení.
registrovat se do systému, ale poddodavatelé nejsou. Nicméně poddodavatelé, kteří nejsou registrováni
musí odečíst 20 % z plateb dodavatelům.
registrovaným poddodavatelům se sníží odečet na 30 %, u nezaregistrovaných zůstává stejný.

.. viz též:

   - „Schéma stavebního průmyslu (CIS)“ <https://www.gov.uk/what-is-the-construction-industry-scheme>
   - Pokyny pro dodavatele v rámci Společenství nezávislých států
<https://www.gov.uk/government/publications/what-you-must-do-as-a-cis-contractor>
   - Pokyny pro poddodavatele v rámci Společenství nezávislých států


Jako zhotovitel je povinen se registrovat u CIS před nástupem poddodavatelů a
Zkontrolujte, zda je každý poddodavatel registrován u CIS. Musíte také vést záznamy o všech
platby a slevy a podávat měsíční vratky na finančním úřadě, včetně následujících detailů:

- informace o poddodavatelích
- záznamy o platbách a případných srážkách
- prohlášení, které potvrzuje, že zaměstnanecký status všech poddodavatelů byl zkontrolován
- prohlášení o tom, že všechny poddodavatelé vyžadující ověření byly ověřeny.

.. poznámka::
Pokud se v předchozím měsíci neprovedly žádné platby poddodavatelům, musí zhotovitelé oznámit
|HMRC| do 19. dne v měsíci, aby se vyhnuli pokutě.

Podat měsíční vratky HMRC: ref: „nainstalovat <obecné/instalovat>“.
:ref:`UK - Stavební průmysl <lokalizace/united-kingdom/moduly>` modul.

.. tip::
Pro zapnutí režimu Test a použití testovacích přihlašovacích údajů otevřete aplikaci Nastavení, aktivujte
:ref:`rozvojový režim <developer-mode>` a přejděte do :menuselection:`Nastavení --> Technické -->
„Systémové parametry“. Hledejte „l10n_uk_hmrc.api_mode“, vyberte jej a změňte
:guilabel:`Hodnota“ z „produkce“ do „testu“.

... _lokalizace/británie/cis-měsíční-vratky:

Měsíční výnosy
---------------

Měsíční vratky fungují pouze pro faktury dodavatelů a platby od dodavatelů.
HMRC, abyste mohli uvést všechny platby, které jste poskytli poddodavatelům.
schéma v předchozím měsíci daně:

- :ref:`lokalizace/jednotné království/cis-dodavatelský model“
- :ref:`lokalizace/jednotné království/cis-poddodavatelský systém
- :ref:`lokalizace/jednotné království/faktury dodavatelů CIS“
- :ref:`lokalizace/spojené království/měsíční zpráva o odeslání CIS“

... _lokalizace/jednotné_království/cis-dodavatelský_základ:

Založení smluvního partnera
~~~~~~~~~~~~~~~~~~~~~~~~~~

Pro konfiguraci informací o vaší společnosti v aplikaci Nastavení přejděte do aplikace
V sekci „Společnosti“ klikněte na „Aktualizovat informace“. Otevřete záložku „HMRC“ a
konfigurovat informace v poli „HMRC Credentials“ a „Contractor details“.
oddílů. Všechny položky jsou povinné.

..._lokalizace/británie/cis-poddodavatelský-set-up

Nastavení subdodavatelů
~~~~~~~~~~~~~~~~~~~

Přejděte na kontaktní formulář poddodavatele a vyberte záložku „Účetnictví“.
V části „Podrobnosti HMRC“ povolte možnost „Školicí program pro stavební průmysl“.
Zobrazují se pole související s CIS.

Výchozí sazba odpočtu je nastavena na 30 %. Chcete-li ji změnit, nejprve zadejte
:guilabel:`Kontrolní číslo“ poskytnuté |HMRC| při ověřování postavení poddodavatele.
aktualizovat pole „Sazba odpočtu“ podle toho.

.. poznámka::
Pole „Jméno“ a „Příjmení“ jsou povinná, pokud je kontakt typu „Osoba“.
do:guilabel:"Osoba".

... _lokalizace/jednotné-království/cis-faktury-prodejců:

Faktury dodavatelů
~~~~~~~~~~~~

Na fakturách dodavatelů se musí uplatnit vhodný daňový režim, a to na položky „práce“ podle
dodavatelů: „Sazba odpočtu“: „0 % CIS“, „20 % CIS“ nebo
:guilabel:`30 % CIS“. Aplikaci sazby proveďte v sekci „Dodavatelské řádky“ pod záložkou
fakturu a vybrat vhodný daňový sazebník v sloupci „DANĚ“ v poli „PRACOVNÍK“.
položky.

.. poznámka::
   - Daň z přidané hodnoty CIS není nutná pro materiální položky na fakturách dodavatelů.
   - Pokud se zobrazí žlutá pásučka na hlavičce stránky, znamená to, že:

     - Možnost „Schéma stavebního průmyslu“ v nastavení není povolena.
:ref:`poddodavatel <lokalizace/jednotné království/cis-subcontractor-setup>
:guilabel:`Kontakt“ při vytváření faktury pro dodavatele.
     - Daň z přidané hodnoty uvedená na faktuře dodavatele se nezapočítává do očekávaného odpočtu DPH.
:ref:`dodavatel <lokalizace/jednotné-království/cis-dodavatel-nastavení>`.

..._lokalizace/jednotné-království/cis-měsíční-výkaz-zaslání:

Měsíční odeslání výnosů
~~~~~~~~~~~~~~~~~~~~~~~

Odoo každého 6. v měsíci pošle e-mail s upozorněním na podání měsíčního přiznání HMRC.
adresa příjemce je ta, kterou máte uvedenou v poli „E-mail“ společnosti.
vraťte se do HMRC a přejděte na „Účetnictví -> Zprávy -> Daňový návrat“.
kroky:

#Klikněte na ikonu „fa-book“ a vyberte „Zpráva: CIS Odpočet (GB)“.
#V kalendáři :icon:`fa-calendar` :guilabel:`(kalendář)` je možné vybrat datum v poli :guilabel:`Doba platnosti
Budou automaticky upraveny tak, aby odpovídaly období výpočtu CIS.
#Klikněte na „Odeslat do HMRC“ v levém horním rohu.
#V okně měsíčního přiznání CIS vyberte požadované možnosti v
:guilabel:`Deklarace“ části:

   - :guilabel:`Stav zaměstnání“: aby bylo deklarováno, že stav zaměstnání všech poddodavatelů je
Bylo provedeno přezkoumání.
   - :guilabel:`Kontrola poddodavatelů“: Prohlásit, že všechny předložené poddodavatele vyžadující
ověření byly ověřeny.
   - :guilabel:Indikátor nečinnosti: Prohlásit dočasnou nečinnost.

#V části „Deklarace o správnosti informací“ potvrďte, že údaje jsou pravdivé.
doplňte zaškrtnutím políčka a pak zadejte heslo používané v
:guilabel:"Přihlašovací údaje HMRC" v části
:ref:`sestavení dodavatele <lokalizace/jednotné království/cis-supplier-set-up>“.
#Klikněte na tlačítko „Odeslat“ a vyzvěte systém Odoo, aby požádal HMRC o zahájení transakce.

Když HMRC odpoví na transakci, Odoo automaticky upozorní uživatele, který ji podal.
e-mail, který jim sděluje, že odpověď je k dispozici v chatu společnosti s
přílohu ve formátu XML ke stažení. Obě tištěná i elektronická verze potvrzení
musí být zachována. Pokud se zjistí chyba, je nutné podat novou žádost v souladu s HMRC
požadavky.

.. poznámka::
   - Transakce jsou aktualizovány každý den. Chcete-li ručně aktualizovat požadavek na HMRC, klikněte na ikonu „fa-cog“
:guilabel:`(převodovka)` ikona a vyberte možnost „Obnovení požadavku na HMRC“.
   - Faktury CIS jsou zahrnuty v hlášení „Odpočet CIS (GB)“, ale nejsou odesílány
|HMRC|.
