=========================================
Online podpisy pro potvrzení objednávek
=========================================

Aplikace Odoo Sales poskytuje zákazníkům možnost potvrzovat objednávky prostřednictvím online
podpisem přímo na prodejním dokladu. Jakmile je elektronicky podepsaný prodejní doklad,
zákazníkovi, okamžitě se o tom dozví i prodejce přidružený k objednávce.
potvrzeno.

Aktivujte elektronické podpisy
==========================

Aby zákazníci mohli potvrdit objednávky elektronickým podpisem, je v e-shopu funkce
*musí být aktivován.*

Pro aktivaci funkce „Online podpis“ přejděte do sekce:
Nastavení“, posuňte se na hlavičku „Údaje o cenách a objednávkách“ a aktivujte
Vyberte možnost „Online podpis“ a zaškrtněte pole vedle ní.

.. obrázek:get_signature_to_validate/signature-setting.png
:align:center
:alt:Volba funkce „Online podpis“ v nastavení aplikace Odoo Sales.

Poté klikněte na tlačítko „Uložit“ v pravém horním rohu.

.. poznámka::
Při vytváření šablony cenového nabídky je funkce elektronického podpisu označena jako :guilabel:`Podpis
možností, která je umístěna v poli „Online potvrzení“ na formuláři šablony nabídky.

..... obrázek::get_signature_to_validate/signature-feature-quotation-template.png
:synchronizace: střed
:alt:Možnost online potvrzení objednávky, která je k dispozici na každém šabloně faktury v Odoo.

Na standardních citačních závorkách je funkce elektronického podpisu volbou „Podpis“ v seznamu
pod záložkou „Další informace“ v objednávkovém formuláři.

.. obrázek: get_signature_to_validate/signature-other-info-tab.png
:synchronizace: střed
:alt:Možnost vložit elektronickou podpis do jiných informací o ceně v kalkulačce Odoo.

Potvrzení objednávky s elektronickým podpisem
==========================================

Když klienti přistupují ke svým cenám online prostřednictvím portálu pro zákazníky, je zde:guilabel:`Značka
Tlačítko „Zaplatit“ přímo v citaci.

.. obrázek:get_signature_to_validate/sign-and-pay-button.png
:align:center
:alt:Tlačítko Sign and Pay, které se nachází v internetových cenách v Odoo Sales.

Když na něj kliknete, objeví se okno „Potvrdit objednávku“. V tomto okně můžete
V poli „Plné jméno“ je automaticky vyplněno na základě kontaktních údajů v databázi.

.. obrázek: získat podpis pro ověření / ověřit objednávku - okno.
:align:center
:alt:Okno pro ověření objednávky v Odoo Sales.

Poté mají zákazníci možnost vložit elektronickou podpisovou značku s následujícími možnostmi:
:guilabel:`Auto“, :guilabel:"Kreslení" nebo :guilabel:"Načíst".

:guilabel:`Auto“ umožňuje Odoo automaticky vytvořit elektronickou podpisovou značku na základě informací uvedených
V poli „Plné jméno“ lze zadat celé jméno zákazníka. Pomocí pole „Kreslení“ může zákazník použít kurzor k vytvoření
vlastní podpis přímo na okně s upozorněním. A: „Nahrát“ umožňuje zákazníkům nahrávat
signaturu, kterou si vytvořili na svém počítači.

Po výběru zákazníkem některé ze tří uvedených možností podpisu
(:guilabel:'Auto', :guilabel:'Draw' nebo :guilabel:'Load'), kliknou na tlačítko :guilabel:'Accept &
Tlačítko „Sign“.

Když je kliknuté tlačítko „Přijmout a podepsat“, jsou dostupné různé možnosti plateb.
(pokud se tato cenová nabídka vztahuje na online platby).

Pak, když je citaci zaplacena a potvrzena, automaticky vznikne objednávka na dodání (pokud
Odoo aplikace Inventář (je nainstalována).

.. viz též:
   - :doc:`citát_šablona“
   - :doc:`get_paid_to_validate“
