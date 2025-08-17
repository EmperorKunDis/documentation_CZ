========
Webové smyčky
========

.. varování:
Je **velmi doporučeno** konzultovat s vývojářem, architektem řešení nebo jiným technickým pracovníkem.
úlohu při rozhodování o použití webových smyček a během implementačního procesu. Pokud nebudou správně
Pokud jsou konfigurovány webové smyčky, mohou narušit databázi Odoo a trvat dlouhou dobu na obnovení.

Webhooky, které lze vytvořit ve **Studiu Odoo**, umožňují automatizovat akci ve vašem Odoo.
databáze, když se v jiném systému vyskytne určitý události.

V praxi to funguje takto: když se událost stane v externím systému, vytvoří se soubor dat (
„náklad“) je odeslán na URL webového konektoru Odoo prostřednictvím požadavku API typu „POST“ a předem definovaná akce
v databázi vašeho Odoo systému.

Oproti plánovaným akcím, které běží v předem definovaných intervalech, nebo ručním požadavkům na API, které je nutné provést, se jedná o
musí být explicitně vyvolána, webhooks umožňují reálnou komunikaci a automatizaci na základě událostí v reálném čase.
Příkladem je například nastavení webhooku, který aktualizuje vaše zásoby v Odoo automaticky při
Prodejní objednávka je potvrzena v externím prodejním systému.

Založení webhooku v Odoo nevyžaduje žádné programování při propojení dvou databází Odoo.
Testování webového konektoru vyžaduje externí nástroj.
:ref:`Vlastní cílové záznamy nebo akce <studio/webhooks/webhook-example> mohou vyžadovat programování
dovednosti.

.. poznámka::
Tento článek popisuje vytvoření webového konektoru, který přijímá data z externího zdroje.
Je také možné vytvořit automatickou akci, která :ref:`odesílá data na externí webhook
automatizovaných akcích / webhooku, když dojde k změně v databázi Odoo.

.. _studio/webhooks/create-webhook:

Vytvořte webovou službu v Odoo
========================

.. důležité:
Před implementací webového konektoru do živé databáze ho nakonfigurujte a otestujte pomocí :ref:`dupl
databáze (odoo_online/databáze-správa) a zajistit, aby webhook fungoval tak, jak má.

..tip:
:ref:`Aktivace režimu vývojáře <developer-mode> před vytvořením webového kroku dává větší
flexibilita při výběru modelu, který je použit v pravidle automatizace
cíle. Dále umožňuje najít technické jméno modelu a pole, která mohou být
bylo potřeba nakonfigurovat náklad.

Chcete-li najít technické jméno modelu s aktivovaným režimem vývojáře, přejeďte myší nad názvem modelu.
Pak klikněte na ikonu „fa-arrow-right“ a zvolte „Vnitřní odkaz“. Technické označení najdete v
pole „Model“. Například webová událost pro objednávku obsahuje pole „Prodej“.
Model objednávky*, ale v těle zprávy se používá technický název „sale.order“.

Vytvoření webového konektoru v aplikaci Studio provedete takto:

#:ref:`Otevřené studio <studio/access>` a klikněte na :guilabel:`Webové hlásitky“, pak na :guilabel:`Nový“.
#Nezapomeňte dát webovému kroku jasný, výstižný název, který popisuje jeho účel.
#Pokud je zapotřebí, a pokud je aktivován vývojový režim, vyberte vhodný model:
z roletky. Pokud není aktivován vývojářský režim, automatické pravidlo cílí na aktuální
výchozí model.

#URL webhooku je automaticky vygenerována, ale lze ji změnit v případě potřeby kliknutím
:guilabel:`Otočte tajemství“. Toto je URL, které by mělo být použito při implementaci webového kohoutku
vnější systém, který bude aktualizace do databáze posílat.

.... upozornění::
URL je **důvěrná informace** a měla by být zachována v tajnosti. Nesdílejte ji na internetu nebo bez
Pozor, opatrnost může poskytnout nechtěný přístup k databázi Odoo. Pokud je URL aktualizován po
v případě prvotní implementace je nutné aktualizaci provést i ve vnějším systému.

#Pokud chcete, povolte:guilabel:'Záznam hovorů' pro sledování historie požadavků na
URL webového konektoru, například pro účely odstraňování závad.

#Pokud systém odesílající webhook není Odoo, upravte kód :guilabel:`Target Record`, aby vypadal takto:
pro záznam JSON zahrnutý v těle požadavku na adresu webového konektoru, když je odeslán požadavek na URL webového konektoru. Pokud
systém odesílající webhook je databáze Odoo, ujistěte se, že v poli id a modelu se objeví
náklad.

Pokud je webhook používán k vytváření záznamů v databázi Odoo, použijte funkci model.browse(i) nebo
místo výchozího formátu „Záznam cíle“.

#Klikněte na „Přidat akci“ v záložce „Akce k provedení“.
<studia/automatizované akce/akce> k provedení.
#Před implementací webhooku v externím systému proveďte test
a zkontrolujte, zda funguje tak, jak má.

..tip:
   - Webhooky můžete vytvořit také pomocí nabídky Automation v **Studiu**, kde vyberete
spouštěč: guilabel: Na webhooku.
   - Pokud je zapnutá volba „Záznam hovorů“, klikněte na
:guilabel:`Záznamy“ chytrý tlačítko na horní části formuláře „Automatické pravidlo“.
   - Pokud je účel webhooku cokoliv jiného než aktualizace stávajících záznamů, např.
Vytvořit nový záznam, musí být zvolená akce „Spustit kód“.

.._studio/webhooks/test-webhook:

Testování webhooku
==============

Testování webhooku vyžaduje testovací platbu a externí nástroj nebo systém, jako například
„Postman <https://www.postman.com/>“, k odeslání hlavičky prostřednictvím požadavku „POST“ na API. Tato část
popisuje kroky, jak otestovat webhook v aplikaci Postman.

..tip:
   - Podívejte se na část „Použití webových hlášení“ v oddílu „Webové hlášení“ (viz příslušný odkaz).
vysvětlení, jak testovat webhooks pomocí testovacích zátěží.
   - Pokud potřebujete konkrétní pomoc s testováním webhooku v aplikaci Postman, kontaktujte jejich podporu.

#V Postmanu vytvořte nový požadavek HTTP a nastavte jeho metodu na :guilabel:`POST`.
#Zkopírujte odkaz na webhook z databáze Odoo pomocí ikony :icon:`fa-link` :guilabel:`(link)`
a vložte ho do pole URL v Postmanu.
#Klikněte na záložku „Tělo“ a vyberte možnost „neupravené“.
#Zadejte typ souboru jako „:guilabel: JSON“, pak zkopírujte kód ze testovacího nákladu a vložte jej
editor kódu.
#Klikněte na tlačítko „Odeslat“.

.._studio/webhooks/test-webhook-response:

Ve spodní části obrazovky v Postmanu se zobrazuje detailní informace o odpovědi, včetně HTTP
kód odpovědi, který ukazuje, zda funkce webhooku funguje správně.

- Zpráva „200 OK“ nebo „status: ok“ ukazuje, že webhook funguje správně na Odoo.
zde může začít implementace druhého systému pro automatické odesílání API
výzvy k webovému callbacku Odoo.

- Pokud je vráceno jiné odpovědi, číslo spojené s ním pomáhá identifikovat problém.
Příkladem je zpráva „Internal Server Error 500“, která znamená, že Odoo nebylo schopno interpretovat požadavek.
správně. V tomto případě je nutné zajistit, aby pole v souboru JSON byly správně přiřazena
konfiguraci webhooku a systému, který provádí testovací volání.

..tip:
Při zapnutí protokolování hovorů v konfiguraci webhooku v Odoo se zobrazí chybové záznamy, pokud dojde k chybě.
Není funkční tak, jak má.

Implementovat webhook v externím systému
=========================================

Po úspěšném vytvoření webového konektoru v Odoo a jeho otestování jej implementujte do systému.
posílá data do databáze Odoo a zajišťuje, aby byly požadavky na API „POST“ odeslány na adresu webového konektoru.

..._studio/webhooks/webhook-examples:

Příklady použití webhooku
=================

Níže jsou uvedeny dva příklady použití webhooků v Odoo. Každý z nich obsahuje testovací platbu.
a najdete ji v části o testování webhooku. Pro tento účel můžete použít aplikaci Postman
použitý k odeslání zkušebního nákladu.

Aktualizace měny prodejního příkazu
-------------------------------

Tato webová smyčka aktualizuje objednávku v aplikaci Sales na USD, když systém posílá
Požadavek na API „POST“ na adresu webového konektoru, který zahrnuje číslo objednávky prodeje (které je identifikováno
identifikátorem nákladu (payload id record)).

Toto může být užitečné pro dceřiné společnosti mimo Spojené státy, které mají mateřskou společnost umístěnou v USA.
Spojené státy nebo při fúzích, kdy se do jedné databáze Odoo sloučí data z více systémů.

Vytvořte webový konektor
~~~~~~~~~~~~~~~~~~

Vytvoření této webové smyčky probíhá takto:

#Otevřete aplikaci **Prodeje**, pak otevřete Studio a klikněte na Webhooks.
Výchozí je model *Objednávka*.
#Klikněte na „Nový“. Výchozí nastavení je „Na webhooku“.
#Nastavte cílový záznam na
„model.env[payload.get('model')].prohlížet(int(payload.get('id'))), kde:

   - „payload.get('model')“ získá hodnotu spojenou s klíčem „model“ v payload.
tj. „prodej.objednávka“, což je technický název pro model *Objednávky*.
   - „payload.get('id')“ získá hodnotu spojenou s klíčem „id“, tj.:
číslo cílové objednávky prodeje ve vaší databázi Odoo s předponou „S“ a
znaky nuly odstraněny.
   - Funkce int() převádí získané ID na celé číslo, protože metoda
Funkce „browse“ lze použít jen s celým číslem.

#Klikněte na tlačítko „Přidat akci“.
#V části „Typ“ klikněte na „Aktualizovat záznam“.
#V sekci „Podrobnosti o akcích“ vyberte možnost „Aktualizovat“, zvolte pole
:guilabel:`Měna“ a vyberte :guilabel:`USD“.
#Klikněte na tlačítko „Uložit a zavřít“.

Otestujte webový konektor
~~~~~~~~~~~~~~~~

Chcete-li tuto webovou událost otestovat, postupujte takto:

#S aplikací Postman otevřenou vytvořte nový požadavek HTTP a nastavte metodu
:guilabel:`POST“.
#Zkopírujte odkaz na webový konektor Odoo pomocí ikony „fa-link“ a vložte jej
do pole URL v aplikaci Postman.
#Klikněte na záložku „Tělo“ a vyberte možnost „neupravené“.
#Nastavte typ souboru na „:guilabel: JSON“, pak zkopírujte tento kód (tedy platbu) a vložte jej
editor kódu:

... kódový blok: JSON

      {
„model“: „prodej.objednávka“,
„ID“: „ČÍSLO OBJEDNÁVKY PRODEJE“
      }

#Vyberte si v databázi Odoo prodejní objednávku, na kterou chcete webhook otestovat. V zkopírovaném kódu nahraďte
„ČÍSLO OBJEDNÁVKY“ s číslem objednávky bez předpony „S“ nebo nulami před číslem.
číslo. Například prodejní objednávka s číslem „S00007“ by měla být v Postmanu zadána jako „7“.
#Klikněte na tlačítko „Odeslat“.
#Konzultujte odpověď v nástroji Postman v sekci Viewer Response.
určit, zda webový konektor funguje správně. Pokud je odpověď jiná než „200 OK“ nebo
Pokud je vráceno „status: ok“, číslo spojené s zprávou pomáhá identifikovat problém.

.._studia/webhooks/webhook-example:

Vytvořit nový kontakt
--------------------

Tato webová služba používá vlastní kód pro vytvoření nového kontaktu v databázi Odoo, když se systém
Odešle požadavek na API „POST“ na adresu webového konektoru, který obsahuje informace o kontaktu. To může
může být užitečné při automatickém vytváření nových dodavatelů nebo zákazníků.

Vytvořte webový konektor
~~~~~~~~~~~~~~~~~~

Vytvoření této webové smyčky probíhá takto:

#Otevřete aplikaci Kontakty, pak otevřete Studio a klikněte na Webhooky.
Výchozím je model *Kontakt*.
#Klikněte na „Nový“. Výchozí nastavení je „Na webhooku“.
#Nastavte :guilabel:`Zamýšlená položka v databázi“ na model.browse([2]). To je ve skutečnosti místo,
kód v automatické akci říká webovému hlásání, co má získat ze zátěže.
a v jakém modelu se má záznam vytvořit.
#Klikněte na tlačítko „Přidat akci“.
#V sekci „Typ“ klikněte na „Spustit kód“.
#Zkopírujte tento kód a vložte jej do editoru kódu v záložce „Kód“ v
:guilabel:`Podrobnosti o akci“ sekce:

... kódový blok:: python

      # proměnné pro získání a uložení dat ze záplaty
kontaktní_jméno = payload.get('name')
kontaktní e-mail = payload.get('email')
kontaktní_telefon = payload.get("telefon")

      # funkci v Pythonu, která promění proměnné na kontakt v Odoo.
pokud je kontaktní jméno a e-mailová adresa:
nový_partner = env['res.partner'].create({
"jméno": kontaktní jméno
"email": kontaktní email
"telefon": kontaktní telefon,
„typ_společnosti“:„osoba“,
„klient_ranking“: 1
          })
      # chybová hláška chybějících požadovaných dat v nákladu
jinak:
vznést výjimku ValueError ("Chybějící povinné pole: 'name' a 'email'")

#Klikněte na tlačítko „Uložit a zavřít“.

Otestujte webový konektor
~~~~~~~~~~~~~~~~

Chcete-li tuto webovou událost otestovat, postupujte takto:

#V aplikaci Postman vytvořte nový požadavek HTTP a nastavte jeho metodu na
:guilabel:`POST“.
#Zkopírujte odkaz na webový konektor Odoo pomocí ikony „fa-link“ a vložte jej
do pole URL v aplikaci Postman.
#Klikněte na záložku „Tělo“ a vyberte možnost „neupravené“.
#Nastavte typ souboru na „:guilabel: JSON“, pak zkopírujte tento kód (tedy platbu) a vložte jej
editor kódu:

... kódový blok: JSON

      {
„jméno“: „KONTAKTNÍ JMÉNO“,
„e-mail“: „KONTAKTEMAIL@EMAIL.COM“,
„telefon“: „KONTAKTNÍ TELEFONNÍ ČÍSLO“
      }

#Ve vloženém kódu nahraďte CONTACTNAME, CONTACTEMAIL@EMAIL.COM a CONTACTPHONE
„ČÍSLO“ s novou informací o kontaktu.
#Klikněte na tlačítko „Odeslat“.
#Konzultujte odpověď v nástroji Postman v sekci Viewer Response.
určit, zda webový konektor funguje správně. Pokud je odpověď jiná než „200 OK“ nebo
Pokud je vráceno „status: ok“, číslo spojené s zprávou pomáhá identifikovat problém.
