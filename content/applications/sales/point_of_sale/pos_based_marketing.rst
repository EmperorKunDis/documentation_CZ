==================
Marketingové funkce
==================

Použijte svůj systém pro zpracování plateb, abyste se s klienty mohli spojit přímo a posílat jim nabídky prostřednictvím e-mailu.
nebo na WhatsApp.

Uchovávání kontaktních údajů
=======================

Tato funkce vyžaduje kontaktní údaje zákazníků, buď e-mailovou adresu nebo telefonní číslo.

- **E-mailové adresy**: automaticky získané a uložené v objednávkách POS při odeslání účtenky
e-mail
- **Telefonní čísla**: ukládání telefonních čísel při zasílání faktur přes WhatsApp nebo SMS.

  #Přejděte do sekce „Nastavení“ a posuňte se dolů k položce „Faktury a
Souhrn příjmů
  #Aktivujte možnost „WhatsApp Enabled“ nebo „SMS Enabled“.

.. obrázek: pos_based_marketing/sms-whatsapp-enabled.png
:alt: nastavení, které umožňuje ukládat telefonní čísla při zasílání faktur

Pokud chybí kontaktní údaje zákazníka, budou automaticky uloženy do objednávek v POS.
Potvrzení o přijetí platby je zasláno e-mailem, SMS nebo prostřednictvím aplikace WhatsApp.

..tip:
Z objednávkového formuláře POS přejděte do kategorie „Kontaktní informace“ pod
:guilabel:`Extra info“ záložce a klikněte na e-mailový nebo WhatsApp symbol pro odeslání samostatného
marketingové zprávy.

.... obrázek:: pos_based_marketing/samostatne-marketing-z-pociskoveho-zařízení.png
:alt:poskytuje možnost samostatného marketingového sdělení

E-mailový marketing
===============

Posílat marketingové e-maily zákazníkům z objednávek na prodejně

#Přejděte na: „Prodejní místo“ --> „Objednávky“ --> „Objednávky“.
#Vyberte objednávky.
#Klikněte na „Akce“, pak na „Odeslat e-mail“ z nabídky.

Tím se otevře okno pro psaní e-mailu. Vyplňte jej a stiskněte tlačítko „Odeslat“.

.. obrázek: pos_based_marketing/mail-composer.png
:alt: kompozitní pohled na e-mail
:skalka: 50 %

..tip:
   - Ušetřete si čas tím, že uložíte své obsahy jako šablonu. Klikněte na vertikální tři tečky
vyberte si šablonu pod záložkou „Vložit šablonu“.
   - Můžete také uložit své obsahy jako šablonu pro pozdější použití. Klikněte na tlačítko vertikální elipsy
a vyberte možnost „Uložit jako šablonu“.

.. poznámka::
   - Vyplňte pole „Název masového rozesílání“ pro vytvoření masového rozesílání a sledování jeho výsledků
v aplikaci Email marketing (viz. :doc:`Email Marketing app <../../marketing/email_marketing>`).
   - Pokud e-mailová adresa není spojena s existujícím zákazníkem, je automaticky vytvořen nový
vytvářené při odesílání marketingových e-mailů.

.. viz též:
:doc:`Použijte aplikaci pro e-mailový marketing pro pokročilé funkce marketingu
<marketing/email_marketing>.

Marketing přes WhatsApp
==================

.. pos_based_marketing/whatsapp_config:

Konfigurace
-------------

Nejprve je třeba povolit související akci serveru, aby mohl odesílat marketingové zprávy přes WhatsApp z vašeho POS.
Používají telefonní čísla shromážděná z objednávek na místě prodeje.

#Přejděte do aplikace WhatsApp.
#Vytvořte nový šablonu pro WhatsApp:ref:`<WhatsApp/templates>`.
#Nastavte pole:

   - Vlastnost pole „Aplikace“ nastavena na „Pokladní objednávky“.
   - Pole „Kategorie“ na pole „Marketing“.
   - „Telefonní pole“ na buď „Mobil“ nebo „Klient > Telefon“.
#Klikněte na tlačítko „Předložit k schválení“.
#Jakmile je schválená, klikněte na tlačítko „Povolit více“ a vytvořte akci pro terminál.
Zobrazení seznamu objednávek.

.. obrázek: pos_based_marketing/whatsapp-template.png
:alt: schválené a konfigurované pro marketingové účely

.. varování:
Pokud upravíte obsah šablony, musíte požádat o schválení znovu, protože stav šablony se vrátí
do stavu :guilabel:`Návrh“.

.. viz též:
:doc:`Konfigurace WhatsAppu <../../produktivita/whatsapp>`

Posílejte reklamní zprávy přes WhatsApp
--------------------------------

#Přejděte na: „Prodejní místo“ --> „Objednávky“ --> „Objednávky“.
#Vyberte objednávky.
#Klikněte na „Akce“ a poté na „Zprávu WhatsApp“.

Tím se otevře okno pro psaní zprávy v aplikaci WhatsApp. Vyberte požadovaný šablonový e-mailový vzor.
Vyberte pole „Šablona“ a stiskněte tlačítko „Odeslat zprávu“.

.. obrázek:: pos_based_marketing/whatsapp-composer.png
:alt: zobrazení kompozice WhatsApp

.. poznámka::
   - Pro využití marketingu na platformě WhatsApp v místě prodeje musí být schválené marketingové šablony
:guilabel:„Povolit více“ zaškrtnuto a „Objednávky v prodejně“ vybráno ve
:guilabel:`Použití pro` pole.
   - Pokud se zobrazí akce serveru bez správně nakonfigurovaného šablonového souboru, objeví se chybová hláška
se objeví, klikněte na „Nastavení šablon“ a dokončete nastavení WhatsAppu podle návodu
<pos_based_marketing/whatsapp_config> kroků.

.. viz též:
:doc:`../produktivita/whatsapp`
