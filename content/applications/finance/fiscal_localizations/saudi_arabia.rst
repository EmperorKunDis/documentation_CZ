============
Saúdská Arábie
============

Konfigurace
=============

:ref:`Nainstalujte následující moduly, abyste získali všechny funkce saúdskoarabské
lokalizace:

.. seznam tabulkový::
:hlavičkové řádky: 1
:prázdné sloupky: 1

   * Jméno
     - Technické označení
     - Popis
   * Saúdská Arábie – Účetnictví
     - „l10n_sa“
     - Výchozí:balík lokalizace daní:
   * Saúdská Arábie – elektronické faktury
     - „l10n_sa_edi“
     - Implementace elektronických faktur ZATCA
   * Saúdská Arábie – bod prodeje
     - „l10n_sa_pos“
     - Soulad s požadavky na prodejní místo

Elektronické faktury ZATCA
================

Elektronický systém fakturace společnosti ZATCA je navržen tak, aby zjednodušil a digitalizoval proces vystavování faktur.
podniky působící v Saúdské Arábii.

.. viz též:
„Stránka elektronického fakturování ZATCA <https://zatca.gov.sa/en/E-Invoicing/Pages/default.aspx>“

Informace o společnosti
-------------------

Přejděte do sekce „Nastavení“ – „Obecné nastavení“ – „Společnosti“, klikněte na tlačítko „Aktualizovat informace“.
a zajistit, aby následující informace o společnosti byly úplné a aktuální.

- V plném znění: „Název společnosti“.
- Všechny důležité pole adresy včetně pole „Číslo domu“
:guilabel:`Označení plochy“ (čtyři číslice).
- Vyberte podnik: guilabel: Identifikační schéma. Doporučuje se použít
:guilabel:`Registrační číslo obchodní společnosti“.
- Zadejte identifikační číslo pro vybraný identifikační systém.
- Číslo DPH.
- Zajistěte, aby měna byla nastavena na „SAR“.

.. poznámka::
Nezbytné je také vyplnit podobné údaje o spolupracujících firmách.

Simulační režim
---------------

.. důležité::
Doporučujeme pečlivě otestovat všechny fakturační procesy pomocí nástroje Fatoora
**simulační** portál jako první, protože jakákoliv faktura podaná na běžném portálu Fatoory bude
Je třeba vzít v úvahu, že by mohlo dojít k pokutám a sankcím.

Portál simulace Fatoora
~~~~~~~~~~~~~~~~~~~~~~~~~

Přihlásit se na portál „Fatoora <https://fatoora.zatca.gov.sa/>“ pomocí účtu společnosti ZATCA
Poté klikněte na tlačítko „Portál simulace Fatora“ a přepněte se do
simulační portál.

.. viz též:
`ZACTA Fatoora portál - uživatelská příručka verze 3 (květen 2023) <https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/Fatoora_Portal_User_Manual_English.pdf>`

... saúdská arábie/api-mode:

Integrace ZATCA API
~~~~~~~~~~~~~~~~~~~~~

V Odoo přejděte na: „Účetnictví“ -> „Konfigurace“ -> „Nastavení“. Pod položkou „ZATCA
Spojení API“, vyberte „Simulace (předprodukční)“ a klikněte na
:guilabel:`Uložit“.

... saudská arábie/články:

Prodejní knihy
~~~~~~~~~~~~~~

Každý prodejní deník v Odoo musí být nakonfigurován. Pro to je potřeba přejít na:
Konfigurace --> Účetní deníky, otevřete jakýkoli prodejní deník (například Faktury zákazníkům) a přejděte na
:guilabel:„ZATCA“ tabulka. V této tabulce zadejte jakýkoliv „Sériové číslo“, které identifikuje deník.

.. poznámka::
Stejný sériový číslo lze použít pro všechny obchodní deníky společnosti.

Dále klikněte na záložku „Onboard Journal“. V dialogovém okně zadejte OTP (jednorázový
je nutné zadat heslo (viz kód). Heslo lze získat otevřením portálu simulace Fatora
<https://fatoora.zatca.gov.sa/>`_, klikněte na „Nové řešení jednotky/zařízení“ a vyberte
Počet kódů OTP, které je třeba vytvořit (jedna pro každý časopis, který chcete nakonfigurovat) a klikněte na tlačítko „Vytvořit OTP
Kód“. Zkopírujte kód OTP do dialogového okna v Odoo a klepněte na „Požadavek“.

.. poznámka::
Kódy OTP platí po dobu jedné hodiny.

.. tip::
Pokud dojde k problému během procesu přihlašování, klikněte na tlačítko „Vytvořit nový žádost o certifikát“ a začněte znovu.

Testování
~~~~~~~

Při potvrzení faktury je nově možnost zpracovat fakturu a odeslat ji přímo
Portál simulace Fatora. Po každém odeslání formuláře zobrazí Odoo odpověď portálu. Pouze rejstříky
Faktury lze v Odoo vrátit do stavu návrhu a upravit. Navíc na konci každého dne odesílá
všechny nezpracované faktury na portál.

.. tip::
   - Testování všech fakturačních procesů, ideálně s reálnými fakturami a za rozumnou částku
doporučuje se.
   - Srovnejte statistiku přijatých faktur na portálu simulace Fatoora s
faktury v Odoo, aby se obě shodovaly.

Daně
~~~~~

Při použití sazby DPH 0 % je nutné uvést důvod takového postupu.
sazba. Pro konfiguraci daní přejděte na:
Dani“, a otevřete daňovou položku pro úpravy. V sekci „Pokročilé možnosti“ vyberte
Vyberte „Důvod výjimky“ a klikněte na „Uložit“.

Při použití retenční nebo zadržovací sazby v zákaznickém faktuře se používá daň použitá k zachování
Je třeba uvést výši částky.

Produkční režim
---------------

Před zahájením výroby změňte režim API na
Vyberte možnost „Produkce“ a klikněte na „Uložit“.

.. varování:
Přepnutí režimu API do režimu Produkce je **nevratné**.

Prodejní deníky, které byly původně propojeny se simulačním portálem, musí být nyní propojeny s běžným
portál. Proto je nutné znovu na palubě „načíst“ časopisy „<saudi-arabia/journals>“, a to tak, že
tentokrát „portál Fatoora“ <https://fatoora.zatca.gov.sa/>.
