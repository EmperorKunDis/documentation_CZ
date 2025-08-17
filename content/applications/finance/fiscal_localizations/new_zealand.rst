===========
Nový Zéland
===========

.. _lokalizace/nový-zéland/moduly:

Moduly
=======

Následující moduly související s novozélandskou lokalizací jsou k dispozici:

.. seznam tabulkový::
:šířky: 25 25 50
:hlavičkové řádky: 1

   * Jméno
     - Technické označení
     - Popis
   * - :guilabel:`Nový Zéland - Účetnictví“
     - „l10n_nz“
     - Nastaveno výchozí nastavení, pokud je balíček účetní fiskální lokalizace nastaven na Nový Zéland.
Tento modul také instaluje modul výkazu o převodu peněz.
   * – :guilabel:`Nová Zélandská mzda od společnosti Employment Hero“
     - „l10n_employment_hero“
     - Tento modul synchronizuje všechny platby zaměstnanců z aplikace Employment Hero s položkami v účetní knize Odoo.
   * – :guilabel:`Sběrná platba EFT“
     - „l10n_nz_eft“
     - Tento modul umožňuje podnikům zefektivnit platby většího rozsahu, jako jsou například výplaty zaměstnanců a platby dodavatelům.
Každá banka má svůj specifický formát pro tyto transakce.

.. poznámka::
K jádru lokalizace jsou automaticky nainstalovány všechny základní moduly. Ostatní můžete
je nutné je ručně nainstalovat:doc:`</applications/general/apps_modules>`.

.. _lokalizace/nový_zéland/lokalita:

Přehled lokalizace
=====================

- :doc:`../účetnictví/začínáme/rozvaha`: předdefinovaný struktura, která je přizpůsobena pro New
Západozélandské účetní standardy
- :doc:`../accounting/taxes/fiscal_positions`: automatické daňové úpravy podle zákazníka nebo
stav registrace dodavatele
- :ref:`lokalizace/nový-zéland/dani-gst`
- :ref:`lokalizace/nový-zéland/hlášení

... /lokalizace/nový-zéland/daně-gst/:

Daň z přidané hodnoty
-------------

Výchozí daně ovlivňují
:dokumentu „Zpráva o GST“ (viz příloha „Daňové přiznání“).
přístupný přes menu:Účetnictví --> Zprávy --> Daňová přiznání

Standardní sazba daně z přidané hodnoty (GST) je 15 %, ale existují různé sazby a výjimky.
pro konkrétní kategorie zboží a služeb.

.. viz též:
:dokument: „Zpráva o DPH“ (viz aplikace Finance / Účetnictví / Zpracování účetních dokladů / Daňové přiznání)

.. _lokalizace/nový-zéland/daňová-mapa:

Daňová mapa
~~~~~~~~~~~

V rámci novozélandské lokalizační sady zahrnují názvy daně i daňovou sazbu jako součást
Jejich pojmenování.

.. viz též:
:doc:`Dokumentace daní <../../../applications/finance/accounting/taxes>`

Jde o daně v Odoo.

.. seznam tabulkový::
:šířky: 25 25 25 25
:hlavičkové řádky: 1

   * -Jméno GST
     - Popis
     - Štítek na fakturách
     - Typ GST
   * - 15%
     - Sleva (15%)
     - Prodej s DPH (15 %)
     - Prodej
   * - 15%
     - Purch (15 %)
     - GST nákupy (15 %)
     - Nákupy
   * – 0 % EX
     - Nula/Export (0 %)
     - Prodeje s nulovou sazbou DPH
     - Prodej
   * 0 % F
     - Nula/Dovoz (0 %)
     - Nákupy bez DPH
     - Nákupy
   * – 0 % TPS
     - Purch (Dovozní cla)
     - Nákup (Daně z dovozu) – Daň zaplacená zvlášť
     - Nákupy
   * – 100 % JEN
     - GST pouze na dovoz
     - DPH pouze na dovoz
     - Nákupy

.. /lokalizace/nový-zéland/hlášení:

Reportáž
---------

... /lokalizace/nový-zéland/gst-report:

Zpráva o GST
~~~~~~~~~~

Zpráva o DPH je kritická daňová zpráva pro podniky.
registrováni k DPH. Daňový přiznání se používá pro hlášení a odvádění DPH na **Finanční správě
Oddělení pro daně z příjmu (IRD)**.

.. obrázek: new_zealand/GST_report.png
:alt:Zpráva o GST.

Základní a daňové částky se vybírají z DPH, které je v Odoo přednastavené tak, aby bylo v souladu
s požadavky na vrácení DPH (části 1 až 15). **GST** lze také ručně nakonfigurovat pro speciální
příklady použití, jako jsou specifické způsoby zdanění DPH (např. nulová sazba pro zemědělské výrobky vyvážené do zahraničí).
Jakmile je nastavení GST pro každý účet dokončeno, Odoo automaticky zařadí položky z knihy
do příslušných políček. To zajišťuje, že daňový přiznání GST je správné a plně odráží
Hospodářské činnosti podniku.

.. viz též:
:doc:`Dokumentace daní <../../../applications/finance/accounting/taxes>`

... _lokalizace/nový-zéland/dph-uzavření:

Závěr zprávy o GST
**********************

Doba podání daňového přiznání musí být nastavena před odesláním
:ref:`daňový přiznání <daňové přiznání/zpráva>“ (**zpráva GST**) na **IRD**.

.. viz též:
:doc:`Dokumentace k ukončení roku


Před prvním zavřením vstupu zapněte režim vývojáře
a přejděte na: „Účetnictví“ ->
Konfigurace --> Daňové skupiny, abyste nastavili výchozí účet pro platbu DPH a účet pro přijatou DPH.
účet**.

Jakmile jsou zřízeny účty „Placená DPH“ a „Přijatá DPH“, je možné vytvořit „Zprávu o dani“.
generuje automaticky přesnou záznam závěrky účetnictví, která vyrovnává stav DPH s DPH.
účet pro vyrovnání.

Rozvaha mezi přijatými a vydanými GST je vyrovnána na účtu daňového vypořádání
definované na základě skupiny daní. Výše, kterou je třeba zaplatit nebo obdržet od IRD, lze pak vyrovnat
bankovním převodem.

.. důležité::
Zpráva GST není předložena přímo finančnímu úřadu (IRD), ale místo toho je předána prostřednictvím Odoo.
automaticky vypočítává požadované hodnoty pro každou sekci a poskytuje možnost auditu
a zkontrolovat data pro lepší pochopení jeho historie. Poté mohou podniky
Tyto hodnoty předložit na portál IRD <https://myir.ird.govt.nz/>.

... /nová_zelanda/příkaz_k_výplatě:

Příkaz k převodu
~~~~~~~~~~~~~~~~~

Příkaz k úhradě je dokument používaný jako důkaz o zaplacení podniku. Chcete-li se dostat k němu, přejděte na
Vyberte položku „Účetnictví“ -> „Dodavatelé“ -> „Platby“ a vyberte platbu (nebo platby). Pak klikněte
:icon:`fa-print` :guilabel:`Tisk“ a vyberte :guilabel:`Potvrzení o platbě“.

.. obrázek: new_zealand/transfer_advice_new.png
:alt:Příkaz k úhradě.

.. /nová-zelanda/účetnictví:

Účetnictví
==========

... _lokalizace/nový-zéland/elektronické-fakturace:

Elektronické fakturace
-----------

Odoo umožňuje nastavit :ref:`elektronické fakturace <e-invoicing/configuration>“ na úrovni
Kontakt

.. obrázek: new_zealand/peppol_contact_new.png
:alt: Peppol Kontakt.

.. důležité::
Zkontrolování faktury nebo kreditní zprávy pro kontakt na síti PEPPOL stáhne
souladu s XML souborem, který lze ručně nahrát do sítě PEPPOL. Odoo je v tuto chvíli
proces stát se přístupovým bodem pro oblast ANZ.

.. viz též:
„Požadavky PEPPOLu <https://www.peppol.cz/o-nas/clanky/clanek/2018/04/05/peppol-v-novem-zelandu/>“

... /nová_zelanda/eft-batch-payments/:

EFT platby v hromadných transakcích
------------------

Soubor s příponou :abbr:`EFT (electronic funds transfer)` je digitální formát, který usnadňuje hromadnou
Zpracování plateb pro podniky. Umožňuje společnostem sdružit více příchozích a odchozích
vložení plateb do jednoho elektronického souboru. Tento proces je běžně používaný firmami, které se zabývají
více plateb najednou, například mzdy nebo platby více dodavatelům.

... /lokalizace/nový-zéland/konfigurace eft:

Konfigurace
~~~~~~~~~~~~~

... /lokalizace/nový-zéland/nastavení eft:

 #:ref:`Nainstalujte modul „Sběr plateb“ („l10n_nz_eft“)“.
 #Přejděte na: „Účetnictví“ -> „Konfigurace“ -> „Nastavení“.
:guilabel:`Platby zákazníků“ sekci, zapněte :guilabel:`Skládané platby“.

.. viz též:
:doc:`../../../aplikace/finance/účetnictví/platby/soubor`

... /nove-zeland/banka-eft-novinky/:

Bankovní časopis
************

Přejděte do sekce „Účetnictví“ -> „Konfigurace“ -> „Deníky“. Zde můžete nakonfigurovat bankovní deník.
V záložce „Účetní položky“ zadejte číslo účtu a klikněte
Vyberte položku „Vytvořit a upravit…“ a v okně „Vytvoření čísla účtu“ vyplňte
:guilabel:„Banka“ a „Poslat peníze“, aby byl účet považován za důvěryhodný.
Pole „Měna“ je nepovinné.

... /lokalizace/nový-zéland/kontakty-na-eft:

Bankovní účty kontaktů
***********************

Chcete-li přidat informace o bankovním účtu kontaktu, přejděte na
:menuselection:`Účetnictví --> Zákazníci --> Zákazníci“
:menu „Účetnictví“ -> „Dodavatelé“ -> „Dodavatelé“, nebo přímý kontakt
Aplikace Kontakty. Vyberte příslušného kontaktu a otevřete záložku Účetnictví. Pod
V sekci „Účty“ klikněte na tlačítko „Přidat řádek“, abyste zadali požadované údaje.

- :guilabel:`Číslo účtu“
- :guilabel:`Banka“
- :guilabel:`Majitel účtu“ (bude automaticky vybrán pro kontakt).
- :guilabel:`Poslat peníze“ musí být zapnuté.

... /lokalizace/nový-zéland/eft-generovat:

Vytvořit soubor EFT
~~~~~~~~~~~~~~~~~~~~

Přejděte na:menu:Účetnictví --> Zákazníci --> Faktury
nebo:menu:Účetnictví --> Přijaté faktury --> Faktury k zaplacení.
listovat a kliknout na „Zaplatit“. V poli „Způsob platby“ vyberte
Vyberte „New Zealand EFT“ a klikněte na „Create Payment“.

.. poznámka::
Zaškrtávací políčko „Souhrnná platba“ je nepovinné. Tato možnost se objeví pouze v případě, že
více faktur nebo účtů od stejného kontaktu.

V okně plateb je požadována pro každou platbu potřebná informace o elektronickém převodu prostředků, například
:guilabel:`Podrobnosti“ a „Kód analýzy“, mohou být zadány, pokud je potřeba.

.. poznámka::
Stejné platební údaje lze najít pod položkou „Účetnictví“ -> „Zákazníci“.
Platby nebo:menu:Účetnictví --> Dodavatelé --> Platby.

Poté se vraťte na stránku „Výpisy plateb“, vyberte platby, které chcete spojit dohromady, a klikněte
:guilabel:`Vytvořit Batch“.

V okně „Soubor plateb“ vyplňte následující pole:

- :guilabel:`Formát souboru EFT“
- :guilabel:`Platební referenční číslo“
- :guilabel:`Údaje o platbě“

.. obrázek: new_zealand/batch_payment_view.png
:alt:Sběrné platby.

Poté klikněte na tlačítko „Ověřit“. Odoo vytvoří soubor EFT ve schránce. Klikněte na soubor
předběžně si jej prohlédnout nebo stáhnout.

.. důležité::
Každá banka má své specifické požadavky na formát platby EFT v rámci hromadné platby. Ujistěte se, že zvolíte
správný formát souboru EFT. Některé banky mohou také vyžadovat doplnění dalších polí, například
jako „Informace o inkasu“ a „Nedostatečný účet“.

.. viz též:
:dokumentace_převodu_bankou
<../../../aplikace/finance/účetnictví/platby/soubor>

.. _lokalizace/nový-zéland/XXXXX:

Oborové specifikace
==========================

.. /lokalizace/nový-zéland/hvězdná-loď:

Starshipit - přepravní služba
-------------------

„Starshipit <https://starshipit.com/>“ je operátor přepravní služby, který usnadňuje
integrace australské lodní přepravy s Odoo.

.. viz též:
   - „Záznam webináře Starshipit <https://www.youtube.com/watch?v=TcDWnoYLXWg>“
   - :doc:`Starshipit shipping <../../../applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/starshipit_shipping>`

... /nová_zelanda/koupit_teď_zaplatit_později:

Nákup nyní, zaplaťte později
----------------------------

„Kup teď, zaplať později“ jsou oblíbené platební metody pro e-shopy. Některé z těchto řešení
jsou k dispozici prostřednictvím „Stripe <https://stripe.com/au/payments/payment-methods>“ a
„Poskytovatelé služby „AsiaPay platba“ (<https://www.asiapay.com.au/payment.html#option>).

.. viz též:
   - :doc:`Dokumentace k poskytovateli platební služby AsiaPay <../../../applications/finance/payment_providers/asiapay>`
   - :doc:`Dokumentace Stripe Payment Provider <../../../applications/finance/payment_providers/stripe>`

... /lokalizace/nový-zéland/pos-termíny:

Terminály na prodejních místech
-----------------------

Pro přímé propojení mezi Odoo a platebním terminálem je potřeba :doc:`Stripe terminal
Je potřeba nainstalovat modul „Stripe“ (odkaz na stránku s instalací).
podporuje řešení platby prostřednictvím elektronického bankovnictví (EFT).

.. poznámka::
K používání Odoo jako hlavního systému prodejních míst není potřeba platební terminál Stripe.
Nevýhodou nespoléhání se na Stripe je, že pokladní musí zadávat ručně konečnou částku za platbu.
terminal.

.. viz též:
   - :doc:`Dokumentace Stripe Payment Provider <../../../applications/finance/payment_providers/stripe>`
   - „Přístupový panel Stripe.com <https://dashboard.stripe.com/login?redirect=%2Fdashboard>“
   - „Dokumentace Stripe.com: Terminál <https://docs.stripe.com/terminal>“

.. _nový-zéland/mzdová-účetní:

Mzdy
=======

.. _novy-zeland/zamestnani-hero:

Spojení s aplikací Employment Hero
---------------------------

Pokud je vaše podnikání již v provozu s „Hrdinou zaměstnanců“ <https://employmenthero.com/>,
Koncový bod může být použit jako alternativní řešení pro platby zaměstnancům.

Modul Employment Hero automaticky synchronizuje účetní záznamy o platbách (např. výdaje).
sociální odvody, pohledávky a daně) z aplikace **Employment Hero** do Odoo.
stále vedené v Employment Hero, pouze záznamy do Odoo.

.. důležité::
Konfigurovat API Employment Hero pro **Nový Zéland**
použijte následující hodnotu jako :guilabel:`URL mzdové účtárny“: „https://api.nzpayroll.co.nz/“.
