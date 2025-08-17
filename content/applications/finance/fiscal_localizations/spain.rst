=====
Španělsko
=====

Konfigurace
=============

Nainstalujte balíček pro místní daňové sazby 🇪🇸 **Spanish** :doc:`<../fiscal_localizations>`, abyste získali všechny
standardní účetní funkce španělské lokalizace.

Existují tři španělské lokalizace, každá s vlastním přednastaveným **PGCE** účetním systémem:

- Španělsko – malé a střední podniky (2008)
- Španělsko - komplet (2008)
- Španělsko - Neziskové organizace (2008)

Pro výběr jednoho z nich přejděte do :menuselection:`Účetnictví --> Konfigurace --> Nastavení`.
Vyberte balíček v sekci „Daňová lokalizace“.

.. varování:
Můžete měnit účetní balíček, dokud nebudou vytvořeny žádné účetní záznamy.

.. viz též:
   - Dokumentace o zákonnosti a souladu s předpisy v oblasti elektronického fakturování ve Španělsku
<../fakturace/zákazníci/daňové doklady/elektronické fakturace/Španělsko>
   - Dokumentace o zákonnosti a souladu s předpisy v Baskicku
<../účetnictví/fakturace zákazníkům/elektronická fakturace/Baskicko>

Klasifikační schéma
=================

Doklad o účetnictví lze dostat kliknutím na: menu > Účetnictví > Konfigurace
Účetnictví: Skladba účtů.

.. tip::
Při vytváření nové databáze Odoo Online je nainstalován výchozí modul **Španělsko – malé a střední podniky (2008)**.

Daně
=====

Výchozí daně specifické pro Španělsko jsou vytvářeny automaticky při
Modul „Spanish - Accounting (PGCE 2008)“ je nainstalován a daňové zprávy
je k dispozici při instalaci modulu:guilabel:`Španělsko - Účetnictví (PGCE 2008) (l10n_es_reports)`
Každá daň ovlivňuje španělské **daňové zprávy (Modelo)** dostupné po kliknutí na
:menu-selection:Účetnictví -> Zprávy -> Výkaznictví: Daňový výkaz.

Zprávy
=======

Tady je seznam španělsky specifických zpráv o prohlášeních:

- Výsledovka
- Zisk a ztráta.
- Prodejní seznam E. C.;
- Daňový přehled (Modelo 111)
- Daňový přiznání (Vzor 115)
- Daňový přiznání (vzor 130)
- Daňový přehled (modelo 303)
- Daňový výkaz (vzor 347)
- Daňový přiznání (vzor 349)
- Daňový výkaz (vzor 390).

Přejděte na stránku s hlášením o daních, kliknutím na ikonu knihy v části „Hlášení“
vybrat svou španělsky specifickou verzi: :guilabel:`(ES)`

.. obrázek:spain/modelo-reports.png
:alt: Španělsky specifické daňové zprávy.

Model 130
----------

Změňte procento
~~~~~~~~~~~~~~~~~~~~~

Pokud chcete změnit procenta počítaná v poli [04] pod pole I
část a/nebo krabice: guilabel: [09] pod částí:

#Aktivujte režim vývojáře, přejděte do sekce „Účetnictví“ a zvolte možnost
Vyberte v seznamu „Zpráva“ možnost „Daňová zpráva“, a poté vyberte zprávu „Daňová zpráva (Modelo 130)“.
#Klikněte na ikonu „Nástroje“ (ikona „fa-cogs“) vedle položky „Zpráva: Daňová zpráva
(Mod 130) (ES`).
#Klikněte na políčko, které chcete změnit, a v okně s upozorněním klikněte na „procento“.
řádku. V novém okně zadejte hodnotu do pole Formule.
procenta, která chcete použít.
Pokud chcete změnit i druhý box, opakujte tento postup.

Zpráva o zemědělské činnosti
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pokud chcete mít vloženou jakoukoliv částku do sekce „II“ (od políček „[08]“ po
:guilabel:`[11]`), musíte změnit průmysl kontaktu na
:guilabel:`Zemědělství“:

#Přejděte na kontaktní formulář (menu „Účetnictví -> Zákazníci -> Zákazníci“
nebo například „Účetnictví -> Zásoby -> Kontakt“).
#V záložce „Prodej a nákup“ nastavte pole „Průmysl“ na
:guilabel:`Zemědělství“.

Tuto operaci opakujte pro všechny kontakty související s oborem zemědělství.

TicketBAI
=========

„Ticket BAI“ nebo „TBAI“ je elektronický fakturační systém
systém používaný vládou Baskicka a třemi jejími provinciálními radami (Álava, Biskaja a
Gipuzkoa).

Odoo podporuje elektronickou fakturaci v souladu s formátem TicketBAI (TBAI) pro všechny tři regiony
**Baskicko**. Chcete-li povolit **TicketBAI**, nastavte pro svou společnost zeměpisnou polohu:
V nastavení „Obecné“ pod položkou „Společnosti“
§

Poté nainstalujte modul „Španělsko - Ticket BAI (l10n_es_edi_TBAI)“ pomocí příkazu :guilabel:`install <general/install>`.
Přejděte na: „Účetnictví“ -> „Konfigurace“ -> „Nastavení“, vyberte si **oblast** v
V sekci „Lokalizace Španělska“ pole „Daňová agentura pro TBAI“.

Jakmile je vybrána oblast, klikněte na tlačítko „Spravovat certifikáty (SII/TicketBAI)“ a poté
:label:Nové“, nahrajte certifikát a zadejte heslo poskytnuté finančním úřadem.

.. varování:
Pokud testujete certifikáty, zapněte režim „Test“ v
:guilabel:`Lokalizace pro Španělsko“ v sekci :guilabel:`Účetnictví“.
aplikace **Nastavení**.

Příklad použití
--------

Jakmile je vystavena a potvrzena faktura,
V horní části obrazovky se zobrazuje banner společnosti TicketBAI.

.. obrázek:spain/ticketbai-invoice.png
:alt:Banner TicketBAI na vrcholu faktury po odeslání.

Odoo vystavuje faktury automaticky každých **24 hodin**. Nicméně můžete kliknout
:guilabel:`Zaslat fakturu hned“ pro odeslání faktury ihned.

Když je faktura odeslána, stav pole :guilabel:`Elektronická faktura“ se změní na
:guilabel:„Odesláno“, a soubor XML najdete v chatu.
kartě „Sledovatelné dokumenty EDI“, můžete sledovat další vytvořené dokumenty související s
faktura (např. pokud má být faktura zaslána i přes SII, objeví se zde).

.. poznámka::
QR kód TBAI je zobrazen na faktuře ve formátu PDF.

.. obrázek:spain/qr-code.png
:alt:QR kód vstupenky TicketBAI na faktuře.

FACE
====

„FACe“ je elektronická fakturační platforma používaná veřejnými správami v
Španělsko bude odesílat elektronické faktury.

Před konfigurací systému FACe (Obecný vstup pro elektronické faktury)
:ref:`instalovat modul <general/install>“ Spánsko – fakturace EDI (l10n_es_edi_facturae)
a další moduly související s fakturami EDI.

Pro konfiguraci FACE postupujte následovně:

#Přejděte do sekce „Účetnictví“ -> „Konfigurace“ -> „Certifikáty“.
#Klikněte na tlačítko „Nový“ pro vytvoření nového certifikátu.
#Vyplňte všechna pole včetně nahrazení souboru certifikátu poskytnutého
Daňovému úřadu a poskytnuté heslo pro certifikát.

.. poznámka::
Pokud chcete používat fakturační aplikaci namísto účetnictví, přejděte na:
Konfigurace --> Certifikáty.

Příklad použití
--------

Jakmile vytvoříte fakturu a potvrdíte ji,
její název a klikněte na „Odeslat a tisknout“. Ujistěte se, že je zapnutá volba „Vytvořit soubor Faktury EDÍ“,
Klikněte na tlačítko „Odeslat a vytisknout“ znovu. Jakmile je faktura odeslána, soubor XML, který byl vygenerován, je k dispozici
v chatu.

.. varování:
Soubor se **NEODEŠLE AUTOMATICKY**. Musíte jej poslat ručně.

.. tip::
Velké soubory XML lze odesílat v hromadných operacích přes „portál vlády <https://www.facturae.gob.es/formato/Paginas/descarga-aplicacion-escritorio.aspx>“.

Administrativní centra
----------------------

Aby mohl **FACE** spolupracovat s **správními středisky**, musí být faktura vystavena na konkrétního
údaje o centrech.

.. poznámka::
Zajistěte si aktualizaci:guilabel:`Španělsko - Fakturae EDI - Administrativní centra
modul l10n_es_edi_facturae_adm_centers nainstalován podle odkazu general/install.

Přidejte nové administrativní středisko, vytvořte nový kontakt a přidejte jej do partnera.
Vyberte typ „Centrum FACE“, přiřaďte kontaktu jednu nebo více rolí a
:guilabel:`Uložit“. Obvykle se vyžadují tři role:

- Řídící orgán: :guilabel:`Receptor“ (Příjemce).
- Zpracovatelská jednotka: :guilabel:`Pagar` (Platit)
- Účetní kancelář: :guilabel:`Daňový úřad“ (Daňový úřad).

.. obrázek:spain/administrativni-centrum.png
:alt:Kontaktní formulář pro veřejné instituce.

.. tip::
   - Pokud administrativní centra potřebují různé kódy podle role, musíte vytvořit
pro každou roli jiný centrální bod.
   - Při vytváření elektronické faktury prostřednictvím partnera s **správními centry** se všechny
do účtenky se započítávají administrativní poplatky.
   - Můžete přidat jeden kontakt s více rolí nebo více kontaktů se různými rolími.
