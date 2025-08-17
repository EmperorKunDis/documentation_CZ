======
Xendit
======

„Xendit“ je indonéský poskytovatel platebních řešení, který pokrývá
v několika zemích jihovýchodní Asie. Umožňuje firmám přijímat kreditní karty i
lokální platební metody.

.. poznámka::
    * Platby kreditními kartami jsou zpracovávány systémem Odoo, zatímco ostatní platební metody jsou řešeny
na webu společnosti Xendit.
    * Xendit podporuje tokenizaci karet, pokud si zákazník vyžádal službu Merchant.
Iniciovaná transakce (MIT) od Xendit Support <https://www.xendit.co/en/contact/>.

... _platební_prostředky/xendit/konfigurovat-přístupový-panel:

Konfigurace na dashboardu Xenditu
=====================================

#Vytvořte si účet u Xenditu
pokud je třeba, viz <https://dashboard.xendit.co/register/1?referral_code=odooid&countr_code=ID>
a přihlásit se do „Dashboardu Xenditu <https://dashboard.xendit.co>“.
#Zkontrolujte svůj režim účtu v horním levém rohu stránky. Použijte :guilabel:`Testovací režim`, abyste mohli vyzkoušet
bez účtování svým zákazníkům. Přepněte se do režimu :guilabel:`Live Mode`, jakmile budete
připravené na přijímání plateb.
#Navigujte do části „Konfigurace: Nastavení“ v levém sloupci stránky aplikace.
V sekci „Vývojáři“ klikněte na
„Klíče API <https://dashboard.xendit.co/settings/developers#api-keys>“.
#Klikněte na tlačítko „Vytvořit tajný klíč“. V okně zadejte jakýkoliv název :guilabel:„API klíče“.
zvolte „Zápis“ pro oprávnění „Přijaté produkty“ a „Žádný“.
pro všechny ostatní povolení klikněte na tlačítko „Vytvořit klíč“.
#Potvrďte heslo a zobrazí se klíč API. Kopírujte nebo stahujte klíč a **uložte
tuto informaci bezpečně uložit na později**. To je jediná doba, kdy může být klíč API zobrazen nebo
stáhnout.
#Jakmile je stránka dokončena, přejděte dolů na
„Webové smyčky“ v sekci „Nastavení vývojáře“
token webhooku.
#Pod položkou „Kontrolní kód webového zpracovatele“ klikněte na „Zobrazit kontrolní kód webového zpracovatele“.
Poté zadejte heslo a potvrďte ho, abyste viděli token. Uložte si jej na později.
#V sekci „URL webového konektoru“ zadejte adresu databáze Odoo, následovanou
v poli URL („např. https://example.odoo.com/payment/xendit/webhook“)
:guilabel:`Zaplacené faktury“ a klikněte na tlačítko vedle něj s textem „Ověřit a uložit“.
#Chcete-li povolit opakované platby kreditními kartami, přejděte na: „Nastavení: Platba
V levém sloupci aplikační stránky klikněte na položku „Kanály“. Pak přejeďte myší nad
:guilabel:`Visa, MasterCard, JCB a American Express“ kanálu, klikněte na „Zobrazit podrobnosti“ a zapněte
:guilabel:`Opakované platby“ přepínačem souvisejícího přepínače.

Konfigurace v Odoo
=====================

#:ref:`Přejděte na poskytovatele platebních služeb Xendit <payment_providers/add_new>“ a změňte jeho stav
na: `Zapnuto`.
#Vyplňte pole „Tajný klíč“ a „Token webového zpracovatele“.
informace uložené v kroku :ref:`payment_providers/xendit/configure_dashboard`.
#Nastavte si ostatní možnosti podle svého uvážení.

.. viz též:
:doc:`../platební_prostředky`
