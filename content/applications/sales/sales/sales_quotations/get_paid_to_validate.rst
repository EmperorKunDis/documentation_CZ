=================================
Potvrzení o online platbě
=================================

Aplikace Odoo Sales poskytuje zákazníkům možnost potvrzovat objednávky prostřednictvím online
platba přímo na prodejní objednávce. Jakmile zákazník elektronicky zaplatí fakturu za zboží,
Prodavač přidružený k objednávce je okamžitě informován, že objednávka byla potvrzena.

Aktivujte online platby
========================

Pokud chcete, aby zákazníci potvrzovali objednávky s platbou přes internet, nastavte
*musí být aktivován.*

Pro aktivaci funkce „Online platba“ přejděte do: „Prodejní aplikace --> Konfigurace -->
Nastavení“, posuňte se na hlavičku „Citace & objednávky“ a zaškrtněte políčko vedle
Vyberte možnost „Platba online“ a klikněte na „Uložit“.

.. obrázek: get_paid_to_validate/online-payment-setting.png
:align:center
:alt:Nastavení plateb přes internet v aplikaci Odoo Sales.

Pod možností „Online platba“ v sekci „Nastavení“ na stránce „Prodej“ je
„Výchozí platnost citace“ pole. V tomto poli je možné přidat konkrétní
Počet dnů, po které platí citační údaje v základním nastavení.

Pro zapnutí této funkce v běžném ceníku klikněte na zaškrtávací políčko „Platba“.
volitelná funkce umístěná v poli „Online potvrzení“ na záložce „Další informace“.
tab.

.. obrázek:get_paid_to_validate/online-payment-option-quote.png
:align:center
:alt:Nastavení platebního příkazu v rámci standardní nabídky prodeje v Odoo Sales.

Aby se tato funkce zobrazila v šabloně cenového odhadu, klikněte na zaškrtávací políčko „Platba“.
volitelná funkce, která je umístěna v poli „Online potvrzení“ šablony objednávkového formuláře.

.. obrázek:get_paid_to_validate/online-payment-option-quotation-template.png
:align:center
:alt:Nastavení platebního příkazu v objednávkovém formuláři Odoo Sales.

Poskytovatelé platebních služeb
=================

Po aktivování funkce „Online platba“ se objeví odkaz na konfiguraci „Platby
Pod ním je uvedeno „Poskytovatelé“.

Kliknutím na odkaz se zobrazí samostatná stránka „Poskytovatelé platebních služeb“, kde je velké množství
Provizních partnerů lze zapnout, upravit a zveřejnit.

.. obrázek:get_paid_to_validate/payment-providers-page.png
:align:center
:alt:Stránka platebních poskytovatelů v Odoo Sales.

.. viz též:
:doc:`../../../finance/platební_prostředky`

Registrovat platbu
==================

Po otevření cenových nabídek v zákaznickém portálu mohou klienti kliknout na tlačítko „Přijmout a zaplatit“.
Potvrzení objednávky provést online platbou.

.. obrázek:get_paid_to_validate/accept-and-pay-button.png
:align:center
:alt:Tlačítko „Přijmout a zaplatit“ na internetové nabídce v Odoo Sales.

Po kliknutí na „Přijmout a zaplatit“ se zákazníkům zobrazí „Zkontrolovat objednávku“.
okno s různými možnostmi pro provedení online plateb.
s oddělením.

.. obrázek:get_paid_to_validate/validate-order-pay-with.png
:align:center
:alt:Jak zaregistrovat platbu na okně prodejního dokladu v Odoo Sales.

.. poznámka::
Odoo nabídne pouze platby na :guilabel:`Potvrdit objednávku“ okně.
byly publikovány a nakonfigurovány na stránce „Dodavatelé plateb“.

Když si zákazník vybere svůj preferovaný způsob platby, kliknou na tlačítko „Zaplatit“.
tlačítko na okně přesunutí, aby potvrdil objednávku. Odoo ihned informuje prodejce
Po potvrzení objednávky s platbou online.

.. obrázek: get_paid_to_validate/payment-confirmation-notification-chatter.png
:align:center
:alt: Příklad oznámení, které se zobrazí v chatu při provedené platbě přes internet.

.. viz též:
   - :doc:`citát_šablona“
   - :doc:`get_signature_to_validate“
   - :doc:`../../../finance/platební_prostředky`
