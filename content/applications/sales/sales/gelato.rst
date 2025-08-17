======
Gelato
======

Gelato je globální tisková platforma na míru, která se integruje s Odoo pro synchronizaci produktových katalogů.
automatizovat zpracování objednávek.

Připojení služeb Gelata k aplikacím Sales a eCommerce společnosti Odoo umožňuje následující:

- Synchronizujte objednávky od zákazníků v Odoo s Gelatem pro automatické vyřizování objednávek
- Vytvářejte a spravujte produkty Gelato v Odoo; podporuje synchronizaci variant a obrázků
- Nastavte možnosti doručení v Odoo a dostávejte informace o objednávkách prostřednictvím webových smyček.

Konfigurace
=============

.. důležité:
Společnost (jméno společnosti a fakturační adresa) v účtu na Gelato (*musí* odpovídat)
informace o společnosti v databázi Odoo, aby byly potvrzeny a odeslány objednávky na prodej
do Gelata pro vyřízení.

.... obrázek: gelato/gelato-company.png
:alt: Informace o společnosti v Gelatu.

.... obrázek:: gelato/odoo-company.png
:alt:Informace o společnosti v Odoo.

Nastavte klíče API a webové zpětné volání v Gelatu
-----------------------------------------

Než začnete konfigurovat Gelato v Odoo, získáte nejprve API klíče a webhooks od
Gelato účet.

Koncovky API umožňují Odoo Sales odesílat a přijímat data z Gelata pro zpracování objednávek.
Webové smyčky poskytují okamžitá data o stavu objednávky a sledování zásilky.

API klíč
~~~~~~~

API klíč je jedinečný autentizační token, který umožňuje Odoo bezpečně komunikovat s Gelatem.
API, které umožňuje odesílání objednávek, aktualizace stavu a synchronizaci dat.

Po přihlášení do Gelata klikněte na ikonu „fa-code“ v levém menu.
klikněte sem a pak na tlačítko „Přidat klíč API“.
otevřete nový formulář pro vytvoření klíče API. Zadejte název, pak klikněte na tlačítko „Vytvořit klíč“.

Kopírovat vygenerovaný klíč API pomocí tlačítka „Vložit do schránky“.

.. obrázek: gelato/gelato-api-key.png
:alt: Nově vygenerovaný klíč API v platformě Gelato.

.. důležité:
Zkopírujte klíč API a uložte jej na bezpečném místě před opuštěním této stránky. Jakmile odejdete
Pokud je okno obnovené nebo zavřené, klíč nebude k dispozici pro kopírování.

Pokud klíč nelze zkopírovat nebo je ztracený, navštivte stránku s klíčem API a začněte znovu.
vytvoření nového API klíče.

Webhook
~~~~~~~

Webhook je automatizovaný systém oznámení, který okamžitě aktualizuje Odoo při zpracování objednávek.
loď nebo doručí objednávku, zajišťuje sledování v reálném čase a minimální ruční zásahy.

Pro vytvoření webového kroku přejděte do položky „Vývojář“ -> „Webové kroky“ pod záložkou „Vývojář“.
v levém menu v seznamu. V nové stránce klikněte na tlačítko „Přidat webovou událost“ pro otevření
Formulář „Vytvořit webovou událost“.

Webhookový formulář vyžaduje několik specifických konfigurací:

- :guilabel:`URL“: Toto sdělení Gelatu říká, kam poslat aktualizace objednávek v Odoo. Zkopírujte a vložte
URL databáze Odoo s příponou „/gelato/webhook“.

...... příklad::
„https://stealthywood.odoo.com/gelato/webhook“

- Klikněte do pole a vyberte „stav objednávky“. Vybrat
:guilabel:`order_status_updated“ zajišťuje, že změny v objednávce jsou odesílány automaticky do Odoa.
- :guilabel:Metoda: Klikněte do pole a zvolte možnost :guilabel:HTTP Post, protože
metoda požadavku, který slouží k odesílání dat z Gelata do Odoo.
- Zaškrtněte políčko vedle:guilabel:Chci autorizaci pro tento webhook.
- :guilabel:`Název hlavičky“: Do tohoto pole zadejte „podpis“, abyste odpovídali poli v Odoo.
- Klikněte na tlačítko „Vytvořit klíč“ pro vytvoření hodnoty „Hlavičky“.
- Klikněte na tlačítko „Vytvořit“ pro dokončení konfigurace webového konektoru.

.. obrázek: gelato/gelato-webhook.png
:alt: Nově nakonfigurovaný webový konektor v rámci platformy Gelato.

..tip:
Zkopírujte klíč API a webovou událost na poznámkový blok, než se přesunete pryč z webové stránky Gelato.
záloha.

Nastavte koncový bod Gelato v Odoo
----------------------------------

V Odoo přejděte na: „Prodejní aplikace“ -> „Konfigurace“ -> „Nastavení“, pak posuňte dolů
sekci „Konektory“. Zapněte konektor „Gelato“ zaškrtnutím políčka.
Poté vložte do příslušných polí nově vygenerované klíče API a tajný klíč webhook.
Uloženo, Gelato je k dispozici v produktech Odoo **Prodej** a **E-commerce**.

Synchronizace produktů Gelato s Odoo Sales
=============================================

Doporučuje se mít produkty již nakonfigurované v Gelatu, než je konfigurujete v Odoo.
Získat identifikátor produktu v Gelatu, přejít na stránku šablon z nabídky postranního panelu.
Vyberte produkt, který chcete synchronizovat v Odoo, pak přejděte na kartu produktu a zobrazí se
:icon:`fa-ellipsis-v` :guilabel:`(vertikální elipsa)` ikona nabídky. Klikněte na ikonu nabídky a pak klikněte
:guilabel:`Kopírovat identifikátor šablony produktu“ pro kopírování identifikátoru šablony produktu do schránky.

.. viz též:
„Začněte prodávat produkty s Gelatem: Rychlé a snadné nastavení



Produkt Odoo Sales
------------------

Pro vytvoření produktu v Odoo, který odpovídá produktu Gelato, přejděte na:
--> Produkty --> Produkty“, vyberte „Nový“ pro vytvoření nového produktu. Zadejte název produktu
Poté přejděte na záložku „Prodej“ a najděte sekci „Gelato“.
Poté klikněte do pole „Odkaz na šablonu“ a vložte zkopírovaný identifikátor šablony
Produkt gelato. Nakonec klikněte na tlačítko „Synchronizovat“.

Úspěšná synchronizace táhne produktové varianty Gelata do nově nakonfigurovaného Odoa.
produkt.

V novém poli „Tisk obrázků“ klikněte na značku „výchozí“, abyste nastavili výchozí
obrázek produktu. Klikněte na ikonku „Penál“ a vyberte soubor obrázku produktu
nahrát, pak:„Uložit a zavřít“.

.. důležité:
pole „Tisk obrázků“ musí být konfigurováno na všech produktech Gelato a jejich
příslušné varianty produktů před objednáním.

Varianty produktů
----------------

Pro zobrazení a úpravu nově synchronizovaných variant produktů přejděte do sekce „Vlastnosti &
Karta variant, která bude obsahovat varianty vytažené z konfigurace produktu Gelato. Klikněte na
tlačítko „Nastavit“ pro editaci a konfiguraci variantních obrázků, způsobů dodání a dalších možností.
cenotvorba, atd.

Objednejte si produkt Gelato přes Odoo
--------------------------------

Jakmile jsou produkty Gelata synchronizovány, lze je objednat v Odoo prostřednictvím cenových nabídek:
<prodejní faktury> nebo na e-shopu. Dodání zmrzliny je automaticky
synchronizované podle konfigurace API a webhooku.

Přidání gelata do objednávky provedete kliknutím na tlačítko „Dodání“ v objednávce. Vyberte
„Standardní dodání“ nebo „Rychlé dodání“ v poli „Způsob dopravy“.
klikněte na pole a pak vyberte možnost „Získat sazbu“.

Jakmile je cenová nabídka potvrzena, stává se aktivním prodejním příkazem a objednávka je odeslána do Gelata.
pro vyřízení. Jakmile je objednávka odeslána z Odoa do Gelata, Gelato zpracuje objednávku.
Vyrábí produkt v nejbližším skladu a odesílá ho přímo zákazníkovi.

.. viz též:
:doc:`fakturace/vytvorit-fakturaci“

.. důležité:
Při vytváření prodejního příkazu na produkty Gelato v databázi lze použít pouze produkty Gelato.
Přidány do stejné objednávky prodeje. S Gelato není možná multivendorová objednávka.
tentokrát.
