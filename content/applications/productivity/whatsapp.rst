========
WhatsApp
========

Aplikace **WhatsApp** je aplikace pro okamžitou zprávu a hlasové přenosy prostřednictvím IP, která umožňuje uživatelům posílat zprávy nebo volat.
volat a sdílet obsah. Firmy mohou využívat aplikaci WhatsApp Business
<https://developers.facebook.com/products/whatsapp/>_ komunikovat se svými zákazníky prostřednictvím zpráv.
poskytovat dokumenty a podporu.

.. varování:
WhatsApp je aplikace pro Odoo Enterprise, která nefunguje v edici Odoo Community.
Pokud se chcete zaregistrovat do verze Odoo Enterprise, klikněte sem: „Zkušební verze Odoo <https://www.odoo.com/trial>“.

.. viz též:
Pro více informací o migraci z verze Odoo Community na verzi Odoo Enterprise se podívejte sem.
dokumentace: :doc:`/správa/na-pracovišti/komunita-do-podniku`.

S aplikací **Odoo WhatsApp** může společnost propojit účet WhatsApp Business Account (WABA) s Odoo.
databáze, která umožňuje následující:

- Přijímat a odpovídat na zprávy WhatsApp přímo ze záznamů v databázi Odoo
- Vytvořit nové šablony s dynamickými proměnnými
- Odešlete předem schválené šablony s dynamickými proměnnými, například:

  - Citace z aplikace **Sales**
  - Účtenky a faktury z aplikace Point of Sale
  - Vstupenky z aplikace **Eventy**

.. viz též:
   - „Meta Business: vytvořit šablony zpráv pro účet WhatsApp Business
<https://www.facebook.com/business/help/2055875911147364>.
   - „Meta Business: připojit telefonní číslo k účtu WhatsApp Business
<https://www.facebook.com/business/help/456220311516626>.
   - „Meta Business: změňte jméno zobrazení služby WhatsApp Business
<https://www.facebook.com/business/help/378834799515077>.

WhatsApp je komunikační služba provozovaná společností Meta, která je mateřskou společností Facebooku.
je běžně používána jako komunikační nástroj v mnoha zemích a firmách.
Dokumentace bude pokrývat integraci firemního účtu WhatsApp s Odoo.
Meta účet je konfigurován v Odoo prostřednictvím :abbr:`API (Application Programming Interface)`
připojení.

Konektor WhatsApp podporuje dva proudy: iniciované společností a iniciované zákazníkem. Společnost může
Zahájit diskusi zasláním šablony jednomu nebo více lidem. Jakmile je šablona odeslána,
adresát může odpovědět, aby spustil diskuzi mezi odesílatelem a příjemcem (a
Okno „Diskuse“ se objeví, pokud zákazník odpoví do 15 dnů.

Pokud klient iniciuje diskuzi (např. zasláním do veřejného WhatsAppu společnosti)
číslo, pak se Odoo otevře skupinový chat s operátory odpovědnými za tento kanál WhatsApp.

..tip:
Je vhodné zřídit více účtů WhatsApp pro různé oddělení. Například
tým podpory a prodejní týmy mohou komunikovat na různých kanálech.

.. viz též:
„Zázračný list - konfigurace WhatsAppu [PDF]


Nastavení aplikace WhatsApp v Meta
================================

Integrace aplikace WhatsApp s Odoo využívá standardní :abbr:`API (Application Programming Interface)`
spojení a je konfigurováno na Meta v následujících krocích:

#Vytvořte si firemní účet na Facebooku
#Vytvořte si účet vývojáře na Meta
#Vytvořte aplikaci a produkt WhatsApp na vývojářském portálu Meta.
#Otestujte připojení k API.

Jakmile je zařízení připojeno, zprávy jsou pak odesílány a přijímány pomocí aplikace *Discuss* společnosti Odoo.
WhatsApp: zkratka API (Application Programming Interface).

Nastavení firemního účtu na Facebooku
---------------------------

Pro vytvoření firemního účtu na Meta (majitel Facebooku) přejděte na: „Facebook Business Manager
<https://business.facebook.com/overview>`. Začněte kliknutím na „Vytvořit účet“ a pak
Zadejte název podniku, jméno správce a e-mailovou adresu pro práci. Pak klikněte
„Další“, objeví se okno s dotazem na potvrzení e-mailové adresy. Po
Potvrďte kliknutím na tlačítko „Done“ a zavřete okno.

Následně postupujte podle pokynů v e-mailu odeslaném společností Facebook pro potvrzení vytvoření obchodního účtu.
účet a dokončit nastavení.

.. viz též:
„Založte si firemní účet na Meta
<https://www.facebook.com/business/help/1710077379203657?id=180505742745347>.

.. důležité:
Pokud je firemní účet propojen s osobním Facebookem, pak administrátor musí
přepínat mezi osobním a firemním účtem po zbytek roku.
konfigurace.

Chcete-li přepnout na firemní účet, přejděte do Facebook Developer Console.
a klikněte na jméno účtu v pravém horním rohu.
Pod nadpisem „Firemní účty“ klikněte na požadovanou firmu.
konfigurace by měla probíhat. Toto je účet, na který bude Odoo odesílat a přijímat
WhatsApp zprávy.

.. obrázek: whatsapp/toggle.png
:alt:Přepínání mezi osobními a firemními účty Meta.

.. důležité:
Pro vytvoření firemního účtu na Meta musí uživatel mít osobní účet na Facebooku.
účet, který existoval alespoň hodinu před zřízením firemního účtu na Facebooku
účet. Před touto dobou se pokus o vytvoření firemního účtu nezdaří.

Tvorba aplikací
------------

Na panelu „Meta pro vývojáře“ <https://developers.facebook.com> se přihlaste pomocí Meta
účet vývojáře. Pokud ještě účet nebyl nastaven, připojte k Facebooku účet Meta
účet vývojáře.

.. poznámka::
Facebookový účet pro vývojáře je odlišný od firemního účtu na Facebooku. Zatímco účet pro vývojáře
účty se skládají z osobních účtů na Facebooku a firemní účty nejsou, protože
reprezentují firmu a spravují všechny aktiva firmy v Meta, jako jsou aplikace.

.. viz též:
„Začněte s platformou pro podnikání na WhatsApp
<https://www.facebookblueprint.com/student/collection/409587/path/360218>.

Klikněte na „Moje aplikace“ v pravém horním rohu po úspěšném přihlášení do Meta
účet vývojáře. To přesměruje správce na všechny aplikace, které si vývojář nakonfiguroval
v tomto konkrétním účtu vývojáře. Klikněte na tlačítko „Vytvořit aplikaci“, abyste mohli začít proces
konfigurace nové aplikace Meta.

Typ aplikace
--------

Na stránce „Vytvoření aplikace“ vyberte možnost „Jiné“ pod sekcí s názvem
„Hledáte něco jiného?“ a pak klikněte na „Další“, abyste se dostali na další
stránku a vyberte typ aplikace. Pak klikněte na první možnost uvedenou pod
:guilabel:`Vyberte typ aplikace“ a titulek „Podnikání“. Tato volba umožňuje
vytvoření a správa API aplikace WhatsApp.

Nyní klikněte na „Další“ a konfigurujte aplikaci podle svého přání. Když se aplikace *typ*
připravené, správce se přesune do části „podrobnosti aplikace“.

Podrobnosti o aplikaci
-----------

V sekci „Podrobnosti“ v procesu „Vytvoření aplikace“ zadejte „Odoo“.
pole pod štítkem „Přidat název aplikace“.

.. poznámka::
Aplikaci lze později změnit v nastavení, pokud je třeba.

.. varování:
Značky a značkové prvky nesmí být použity v této části textu. To zahrnuje Meta
součástí skupiny firem. Slovo „WhatsApp“ do textu nezapomeňte vložit, jinak systém chybu ohlásí.

Poté zadejte e-mailovou adresu vývojáře do pole pod štítkem :guilabel:`E-mailová adresa pro kontakt s aplikací`.

Nakonec nastavte pole :guilabel:`Business Account - Optional` na profil Meta business account.
pomocí rozbalovací nabídky. K dokončení klikněte na tlačítko „Vytvořit aplikaci“. Toto bude vytvářet aplikaci
a vyvolává smlouvy o podmínkách služby Meta Platform a vývojářské politiky.

Přijmout dohody, zadat heslo na Facebooku pro účely bezpečnosti a kliknout
Klikněte na tlačítko „Odeslat“ a aplikaci vytvořte. Prohlížeč pak přesměruje na stránku „Meta
pro Dashboard vývojářů.

.. poznámka::
Pokud je účet pro podnikání zakázán k reklamě, nelze tvrdit, že aplikace není povolena.
řešit tento problém navštivte stránku <https://business.facebook.com/business> pro pomoc.

Více informací najdete v dokumentaci Meta o reklamních omezeních.
<https://www.facebook.com/business/help/975570072950669>.

Přidejte produkt WhatsApp do aplikace
---------------------------------

Nyní, když je vytvořena základní struktura aplikace, bude potřeba přidat produkty.
Aplikace začíná přístupem do dashboardu aplikace Meta, který lze najít
„<https://developers.facebook.com/apps>“ a kliknutím na aplikaci, kterou chcete nakonfigurovat.

Na další stránce klikněte na tlačítko „Nastavení“ vedle políčka s
WhatsApp je umístěna na spodní části stránky.

.. viz též:
„Dokumentace pro vývojáře aplikace WhatsApp od Meta“ <https://developers.facebook.com/docs/whatsapp/>“.

Stránka poté přesměruje na konfigurační stránku pro :guilabel:`WhatsApp Business Platform API`.
Vyberte ze seznamu nabídky Meta, pro kterou chcete nastavit :guilabel:`Select a Meta
Možnost „Firemní účet“ a pak klikněte na tlačítko „Pokračovat“, abyste potvrdili výběr.

.. poznámka::
Když je kliknuté tlačítko „Pokračovat“, administrátor souhlasí s podmínkami a pravidly společnosti Meta.
spojené na :guilabel:`Dashboard aplikace Meta`.

.. poznámka::
Jakmile bude produkt WhatsApp přidán do aplikace, Meta poskytne telefonní číslo pro testování WhatsApp
s pěti zkušebními zprávami.

Začněte používat WhatsApp API
----------------------------

Po dokončení předchozího průvodce produktem WhatsApp a kliknutím na „Pokračovat“ se v prohlížeči
měla směřovat na stránku WhatsAppu „Rychlý start“; tato stránka „Rychlého startu“
Je tady, kde začít konfigurovat WhatsApp API přidáním telefonního čísla a následně odesláním počáteční
testovací zpráva.

.. obrázek: quickstart.png
:alt:Přechod na rychlý start WhatsApp v Meta pro vývojáře.

.. poznámka::
Pokud prohlížeč není na stránce „Rychlý start“ aplikace WhatsApp, přejděte na
<https://developers.facebook.com/apps> a klikněte na aplikaci, kterou chcete nakonfigurovat (v
aplikace se jmenuje Odoo (pokud byly následující pokyny dodrženy).

Pak v levém menu na stránce klikněte na ikonu „v“
vedle nadpisu „WhatsApp“. Otevře se malé menu obsahující
Následující možnosti:

   - :guilabel:`Rychlý start“
   - :guilabel:`Nastavení API“
   - :guilabel:`Konfigurace“

Klikněte na možnost „Rychlý start“ a poté klikněte na „Začněte používat rozhraní API“.

Nastavení API
~~~~~~~~~

Po kliknutí na „Začněte používat API“ se zobrazí stránka s nastavením „API“.
Nyní, když je vytvořen testovací kód, může být odeslána zpráva pro ověření, že WhatsApp funguje.
fungovat správně. Nejprve přejděte na sekci stránky označenou:guilabel:`Odesílání a příjem
zprávy“ a klikněte na rozbalovací nabídku vedle „Další krok: vyberte telefon“.
čísla“.

Nyní vyberte jedinou dostupnou možnost: „Správa seznamu telefonních čísel“. Postupujte podle pokynů a
Přidejte až pět čísel, abyste mohli poslat zdarma testovací zprávy do příslušné země. Po zadání správné země
kód a telefonní číslo, klikněte na „Další“.

.. důležité:
Přidání telefonního čísla pro odeslání v tomto kroku umožní úspěšné odeslání zkoušky.
terminalu. To je kritické pro zajištění, aby WhatsApp :abbr:`API (Application Programming Interface)`
Je to v pořádku.

Poté je na telefonní číslo odeslána ověřovací SMS z aplikace WhatsApp Business.
na další obrazovce ověřit vlastnictví telefonního čísla. Zadejte ověřovací kód a klikněte
:guilabel:`Další“ pro ověření čísla.

Odešlete zkušební zprávu přes terminál
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dále pošlete zkušební zprávu prostřednictvím terminálu. Pod sekcí označenou:guilabel:`Krok 2: Odeslat
zprávy s API“, klikněte na „Odeslat zprávu“. Pak bude odeslána testovací zpráva do
telefonní číslo, které bylo nastaveno v předchozím oddíle.

Pokud jste úspěšně přijali zprávu na číslo, pokračujte do další části a
Nastavit webové události.

... produktivitu/whatsapp/webhooks:

Konfigurace WhatsApp v Odoo
==============================

Další kroky konfigurované v této části jsou všechny uložené v databázi Odoo. Několik různých hodnot
Token, telefonní číslo a identifikátory účtu musí být v Odoo nakonfigurovány; tyto hodnoty jsou
nutné pro vytvoření :guilabel:`Callback URL“ a :guilabel:`Webhook Verify Token“, které
Poté jsou použity k konfiguraci webových smyček (aby se zprávy vrátily do databáze).

V Odoo přejděte na: „WhatsApp app --> Konfigurace --> Účty pro službu WhatsApp“.
Poté klikněte na tlačítko „Nový“ a konfigurujte účet pro podnikání v aplikaci Odoo.

V jiném záložce prohlížeče přejděte na adresu:menuselection:`https://developers.facebook.com --> My Apps -->
WhatsApp --> Konfigurace API“, a poté zkopírujte následující hodnoty ze stránky vývojáře Meta
Do příslušných polí v Odoo:

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * - Jméno
     - Meta Console
     - Odoo rozhraní
   * – Telefon
     - :guilabel:`ID telefonního čísla“
     - :guilabel:`ID telefonního čísla“
   * Token
     - :guilabel:`Přechodná přístupová značka“
     - :guilabel:`Přístupový token“
   * - ID aplikace
     - :guilabel:`ID aplikace“
     - :guilabel:`ID aplikace“
   * -ID účtu
     - :guilabel:`ID účtu WhatsApp Business“
     - :label:ID účtu

Chcete-li získat :guilabel:`App Secret`, přejděte na vývojářský panel Meta.
„<https://developers.facebook.com/apps>“ a vyberte aplikaci, ve které je Odoo konfigurováno. Pak
V levém menu vyberte položku „Nastavení aplikace“ a v následujícím okně zvolte možnost „Základní“.

Nyní klikněte vedle pole „App secret“ na „Zobrazit“, zadejte svůj účet
heslo k ověření vlastnictví. Zkopírujte hodnotu :guilabel:`App secret` a pak vložte zkopírovanou hodnotu
pole „Tajné heslo“ v konfiguraci účtu WhatsApp Business na Odoo
přístrojová deska.

K dokončení nastavení firemního účtu WhatsApp v Odoo klikněte na tlačítko „Ověřit připojení“.
úspěšná zpráva v zelené barvě se objeví v pravém horním rohu panelu, pokud
je správně nastavená.

Konfigurace webhooků
--------------------

Pro konfiguraci webových konektorů pro WhatsApp v Odoo přejděte na
„<https://developers.facebook.com/apps>“ a vyberte aplikaci, ve které je Odoo konfigurováno.
Pod nadpisem „WhatsApp“ v levém sloupci obrazovky klikněte na
Následně přejděte do sekce označené „Krok 3: Konfigurace“.
webové události pro přijímání zpráv a klikněte na „Nastavit webové události“.

..tip:
Další způsob, jak nakonfigurovat webové konektory, je přejít na adresu <https://developers.facebook.com/apps>_.
a vyberte aplikaci, ve které je Odoo konfigurováno. Pak vyberte v levém menu:guilabel:"Webhooks".
vlastními rukama.

.... obrázek:: webhooks.png
:alt: Ruční procházení konfigurace webových zpětných odkazů WhatsApp.

Na stránce Konfigurace webového kroku klikněte na tlačítko Upravit.
Do pole „URL zpětného volání“ a „Token ověření webového kroku“ se přidají hodnoty z Odoo.

.. poznámka:
Hodnoty :guilabel:`Callback URL` a :guilabel:`Webhook Verify Token“ byly automaticky
po kliknutí na tlačítko „Ověření připojení“ v předchozím kroku.

V samostatném okně prohlížeče získáme potřebné hodnoty v Odoo kliknutím na
:menuselection:`WhatsApp app --> Konfigurace --> WhatsApp Business Accounts“ a vyberte
účet, který je v nastavení. Hodnoty najdete pod položkou „Příjem
Zprávy.

Zkopírujte a vložte :guilabel:`Callback URL` z Odoo do pole :guilabel:`Callback URL`.
Meta. Podobně zkopírujte a vložte :guilabel:`Webhook Verify Token“ do :guilabel:`Verify
V poli „Token“ na vývojářské konzoli Meta také.

Konečně klikněte na tlačítko „Přidat a uložit“ v konzoli vývojáře Meta.

Webhook pole
~~~~~~~~~~~~~~

Nyní zadejte jednotlivé položky webového konektoru do konzole vývojáře Meta pod názvem „Webhook
sekce pole. Klikněte na tlačítko „Spravovat“ a když se objeví okno s výzvou, zaškrtněte políčka v
Sloupec „Přihlásit se“ pro následující pole:

- „aktualizace účtu“
- „kvalita_aktualizace“
- „Vyplnění formuláře“
- „zprávy“
- „template_category_update“

Po výběru klikněte na tlačítko „Dokončit“.

Hotová konfigurace webových událostí bude vypadat takto ve vývojářském konsoli Meta:

.. obrázek: whatsapp/webhooks-done.png
:alt:Webové služby nastavené v konzoli vývojáře Meta.

.. důležité:
Pole webhooku se objeví až po potvrzení odběru pomocí
:guilabel:`URL callbacku“ a :guilabel:`token ověření webhooku“.

.. viz též:
„Dokumentace Meta pro nastavení webových zpětné vazby“
<https://developers.facebook.com/docs/whatsapp/cloud-api/guides/set-up-webhooks>.

Přidej telefonní číslo
~~~~~~~~~~~~~~~~

Pro konfiguraci telefonního čísla pro použití aplikace WhatsApp v Odoo se vrátíme na stránku Meta Developer.
konzoli („<https://developers.facebook.com/apps>“) a znovu vyberte aplikaci, kterou používáte
je nastaveno. V levém sloupci obrazovky pod položkou „WhatsApp“ klikněte na
Následně přejděte do sekce označené: „Krok 5: Přidat
telefonní číslo“ a klikněte na „Přidat telefonní číslo“.

Do pole „Název firmy“ zadejte také název webové stránky nebo profilu.
stránka.

..tip:
V poli „Obchodní webová stránka nebo profil“ může být uveden odkaz na sociální síť.
(univerzální identifikátor zdroje).

Dokončete vyplnění obchodních informací kliknutím na zemi, ve které se společnost nachází
podnikání z nabídky v sekci „Země“ a přidejte adresu, pokud chcete.
Tato informace je však nepovinná. Po přidání umístění klikněte na tlačítko „Další“.
pokračovat.

Následující stránka obsahuje informace o profilu WhatsApp Business.
Dále v textu se budeme věnovat jednotlivým částem, tedy:

- :guilabel:`Název profilu WhatsApp Business“
- :guilabel:`Časové pásmo“
- :guilabel:`Kategorie“
- :guilabel:`Popis podnikání“ (volitelné)

Jakmile jsou tyto sekce dokončené, klikněte na tlačítko „Další“. Stránka se aktualizuje a poté vás vyzve
administrátorovi do pole „Přidat telefonní číslo pro WhatsApp“ zadáte zde
telefonní číslo, které je potřeba nastavit v aplikaci WhatsApp.

.. viz též:
„Přesunout existující číslo aplikace WhatsApp do firemního účtu

číslo na firemní účet>.

Dále vyberte metodu ověření telefonního čísla. Vyberte buď „SMS“ nebo
Poté klikněte na „Další“.

Do zadaného telefonního čísla dorazí buď SMS nebo hovor s kódem přes WhatsApp.
podle zvoleného ověřovacího postupu. Zadejte tento ověřovací kód do
Zadejte ověřovací kód do pole „Kontrolní kód“ a klepněte na tlačítko „Další“.

.. varování:
Pokud platební metoda nebyla přidána, je třeba ji dokončit. „Navštivte stránku Meta“
dokumentace o tom, jak přidat platební metodu v Business Manageru Meta
<https://www.facebook.com/business/help/915454841921082?id=180505742745347>_. To je součástí
Meta má systém pro detekci podvodů, aby se ujistila, že účet/firma jsou skutečné a platba
Je nutné použít metodu, která je k dispozici.

.. viz též:
„Meta pro vývojáře: Přidej telefonní číslo
<https://developers.facebook.com/docs/whatsapp/cloud-api/get-started/add-a-phone-number>.

.. produktivitu / whatsapp / token:

Trvalý token
~~~~~~~~~~~~~~~

Po dokončení konfigurace a testování by měl být vytvořen trvalý token, který nahradí
:guilabel:`Dočasný token“.

.. viz též:
„Meta pro vývojáře: přístupové tokeny uživatelů systému

>_

Začněte tím, že se přesunete na adresu <https://business.facebook.com/> a pak pokračujte k položce „Business
Nastavení --> Uživatel --> Systémové uživatele“. Vyberte existující systémového uživatele nebo vytvořte nového systémového uživatele
kliknutím na tlačítko „Přidat“.

Nyní musí být aktiva přidána do systému uživatele, poté může být vytvořen trvalý token.

.. varování:
Toto je povinný krok. Pokud se trvalá značka nepřidá, databáze Odoo zobrazí
:ref:`chyba tokenu <whatsapp/token_error>“.

Klikněte na tlačítko „Přidat aktiva“ a v okně, které se objeví, vyberte „Aplikace“.
Vyberte typ aktiv a poté aplikaci Odoo. Zapněte oprávnění na *Zapnuto*.
pod volbou „Plná kontrola“. Nové oprávnění nastavíte kliknutím
„Uložit změny“, ke kterému se zobrazí okno potvrzující přidání
aktivaci systémovému uživateli. Zavřete aplikaci kliknutím na tlačítko „Dokončit“.

Poté se vytvoří trvalý token. Klikněte na tlačítko „Vytvořit nový token“ a vyskočí okno
zobrazí se okno, ve kterém si vyberete aplikaci pro tento token. Vyberte :guilabel:`Aplikace`.
proč je tento token vytvořený. Pak určete datum vypršení platnosti buďto:
:guilabel:Nikdy.

Konečně, když Meta požádá o povolení pro uživatele systému, přidejte všechny následující
povolení:

- „podnikové řízení“
- whatsapp_business_messaging
- whatsapp_business_management

Když jsou povolení nastavená, klikněte na tlačítko „Vytvořit token“. Zkopírujte hodnotu tokenu, která se zobrazí.
obrazovka, která následuje.

S tímto tokenem aktualizujte pole „Přístupový token“ v účtu pro podnikání na WhatsApp.
Odoo se přesunete na:menu:„WhatsApp app“ --> „Nastavení“ --> „WhatsApp Business
Účty.

Spustit aplikaci Meta
=========================

Aby se aplikace spustila, musí být v aplikaci Meta nastaveno na „Živé“ v Meta Developer.
Konzoli přejděte na adresu <https://developers.facebook.com/apps> a klikněte na aplikaci, kterou chcete
konfigurovat. V horním menu přepněte pole :guilabel:`Režim aplikace“ z :guilabel:`Vývoj“ na
:label:Živě.

.. důležité:
Pokud stav aplikace není nastaven na hodnotu *live*, pak databáze bude schopna kontaktovat pouze testovací verzi.
čísla uvedená v vývojářské konzoli.

.. varování:
URL adresy pro ochranu soukromí musí být nastaveno, aby aplikace mohla být nasazena do provozu. Přejděte na stránku vývojáře Meta
konzole, v části „<https://developers.facebook.com/apps>“ a vyberte aplikaci, ve které je Odoo
Poté přejděte na levou stranu obrazovky a vyberte možnost :menuselection:`Aplikace
Nastavení --> Základní“. Pak zadejte odkaz na zásady ochrany osobních údajů pod
:guilabel:`Ochrana osobních údajů“ pole formuláře. Klikněte na :guilabel:`Uložit změny“ a aplikovat
zásady ochrany osobních údajů aplikace.

Jakmile se aplikace dostane do vývojářského centra Meta, je odeslána potvrzovací e-mailová zpráva na
správce.

... produktivitu/whatsapp/vzory:

Šablony pro WhatsApp
==================

Šablony v aplikaci WhatsApp jsou uložené zprávy, které se opakovaně používají k odeslání zpráv ze záznamů.
Umožňují uživatelům odesílat kvalitní zprávy bez opakovaného psaní stejného textu.

Vytváření různých šablon, které jsou přizpůsobeny konkrétním situacím, umožňuje uživatelům vybrat tu správnou.
zprávu pro správnou cílovou skupinu. To zvyšuje kvalitu sdělení a celkové zapojení
s klientem.

Šablony pro WhatsApp lze vytvářet na obou konzolách Odoo i Meta. Následující postup je
představí proces vytváření šablon v Odoo a poté v Meta.

.. důležité:
WhatsApp má schvalovací proces, který musí být dokončen před tím, než lze šablonu používat.
:ref:`produktivita/whatsapp/schválení`.

... _WhatsApp/šablony:

Vytváření šablon v Odoo
--------------------------

Chcete-li přistupovat a vytvářet šablony aplikace WhatsApp, začněte tím, že se dostanete na stránku:menuselection:WhatsApp app -->
Dashboard šablon.

Na konci jednotlivé šablony je tři záložky: :guilabel:`Tělo`,
„Tlačítka“, „Proměnné“ a „WhatsApp“. Tři tyto záložky v kombinaci vytváří aplikaci WhatsApp.
šablona.

Text se zadává do záložky Body a dynamický obsah, který je v ní vyvolán,
Tabulka „Tělo“ je specifikována v záložce „Proměnné“. Každý kus dynamického obsahu
(např. místo uživatelských proměnných) v zprávě (těle) je specificky vyzýváno a specifikováno
:guilabel:`Proměnné“ záložka.

Šablony jsou předpřipravené šablony, které umožňují uživatelům odesílat profesionálně vypadající zprávy.
zákazníci. Tyto šablony jsou schopny obsahovat dynamická data, která se nakonec vyplní
zprávu s proměnnými nastavenými v konfiguraci šablony. Například zpráva může
obsahovat jméno koncového uživatele, vyzývat k nákupu určitého produktu nebo odkazovat na objednávku, abychom zmínili několik příkladů.
pohodlné a významné proměnné.

Pro vytvoření šablony pro WhatsApp přejděte na panel „Aplikace WhatsApp - Šablony“.
Klikněte na „Nový“. V poli zadejte název šablony a vyberte
:guilabel:`Jazyk“.

.. důležité:
Pro dokončení této další úlohy je potřeba mít administrátorská práva k editaci
:guilabel:`Použití na“ pole. Podrobnosti o tomto tématu naleznete v této :doc:`dokumentaci práv přístupu
pro více informací.

V rozevíracím seznamu „Účet“ vyberte účet WhatsApp Business v Odoo.
šablona by měla odkazovat na. Následně pod políčkem :guilabel:`Applies to` vyberte model serveru
Tento vzor bude aplikován na tuto akci.

..tip:
Tyto modely lze také zobrazit v režimu pro vývojáře: viz. :ref:`režim pro vývojáře <developer-mode>`. Na kontaktním formuláři
(nebo podobný relevantní formulář v Odoo), přejděte na model, který je odkazován, a zobrazte
jakýkoliv název pole. S konkrétním Odoo se zobrazí informace o backendech.
:guilabel:`Model“ v zadní části. Hledání (pomocí názvu předního panelu) tohoto modelu v zadní části
:guilabel:`Použít na“ v šabloně aplikace WhatsApp.

.. varování:
Často při změně modelu nebo pole „Použito pro“ se může objevit pole „Telefon“.
Výjimku vyvolává pole telefonu: guilabel: Phone Field by mělo být vždy nastaveno na Telefon nebo Mobil.
model.

Pro vyhledání dostupných polí vepište přední název do vyhledávacího pole. Toto najde výsledek
všechny dostupné pole pro daný model ([:guilabel:`Použito u`)], pro který je šablona vytvářena.

.. poznámka::
Abyste našli konkrétní pole, může být nutné procházet více úrovněmi výsledků vyhledávání.
boxu. Použijte ikony „>“ (pravý závorek) a „⬅️“ (levý závorek), abyste se v boxu pohybovali
mezi jednotlivými úrovněmi nabídky.

.. obrázek:whatsapp/telefonni-pole.png
:alt: Hledání pole telefonu v poli vyhledávání.

Změňte pole „Kategorie“ na „Marketing“, „Užitečnost“ nebo
Kategorie „Přihlášení“. Většinou se používají první dvě možnosti, pokud není
Uživatel by chtěl poslat heslo nebo něco souvisejícího s bezpečností. Zadejte: guilabel:Marketing
pokud by mělo být něco propagujícího zasíláno a nastaveno na:guilabel:Utility
obecné transakční zprávy (např. objednávka prodeje, vstupenka na akci atd.).

.. důležité:
Specifikace nesprávné kategorie může způsobit zrušení schválení na Meta.
procesu.

Přidejte všechny uživatele s oprávněním používat tento šablonu. V pravém sloupci zobrazte
Konfigurace hlavičky může být prováděna společně s konfigurací zprávy hlavičky.

K dispozici jsou následující typy hlaviček:

- Text
- Obrázek
- Video
- Dokument
- Umístění (proměnné musí být nastaveny)

Přejděte na záložku „Tělo“ a konfigurujte hlavní zprávu šablony.

Po provedení všech potřebných změn v šabloně klikněte na tlačítko „Odeslat
tlačítko „Schválit“ v pravém horním rohu, což způsobí změnu stavu šablony na
:guilabel:`Čeká na schválení“.

Stav zůstane v položce „Pending“ do té doby, dokud nebude rozhodnuto na Meta, kde bude
Poté bude zaslána e-mailová zpráva, která potvrdí schválení (nebo zamítnutí) šablony.
Šablony pak budou potřeba synchronizovat z databáze Odoo.

Pro více informací o synchronizaci šablon navštivte část „Synchronizace šablon“ v kapitole „Produktivita“.

..tip:
Zvažte předpřipravené vzory datových šablon dostupné v Odoo, které můžete použít nebo upravit.
Šablony lze použít tak, jak jsou, nebo je upravit podle konkrétních potřeb podnikání.

Chcete-li tyto šablony používat, přejděte na: `WhatsApp app --> Templates` a vyberte požadovanou šablonu.
přednastavený šablonu. Klikněte na tlačítko „Předložit k schválení“, abyste zahájili proces schválování.
E-mail je odeslán administrátorovi účtu Meta, jakmile byl šablona schválena.

Tlačítka
~~~~~~~

Tlačítka lze přidat do zprávy v záložce „Tlačítka“. Zadejte typ
(nebo :guilabel:"Navštiv web", :guilabel:"Zavolej číslo" nebo :guilabel:"Rychlá odpověď"), a pak
Specifikujte text tlačítka, telefonní číslo nebo webovou adresu (včetně
URL typu“), v závislosti na typu tlačítka.

.. poznámka::
Tlačítka můžete také přidat na firemní konzoli Meta. Podívejte se na šablonu panelu WhatsApp od Meta.
navigace na adresu <https://business.facebook.com/wa/manage/home> a poté přejděte do
:menu:„Nástroje účtu“ --> „Šablony zpráv“.

Použití místních proměnných a proměnných
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dynamické proměnné odkazují na určité pole v databázi Odoo, aby produkovaly jedinečná data.
WhatsApp zpráva při použití šablony. Dynamické proměnné jsou kódovány pro zobrazení políček uvnitř
databáze, která odkazuje na pole v rámci modelu.

Příklad:
Mnoho firem rádo upraví své zprávy na WhatsApp podle osobních potřeb zákazníka.
informace, která upoutá pozornost. To lze v Odoo dosáhnout odkazem na pole
vytvořit proměnnou dynamickou. Například jméno zákazníka může být odkazováno na
e-mail z pole „Zákazník“ na modelu „Prodejní objednávka“.

.. obrázek:whatsapp-zpráva.png
:alt:Zpráva na WhatsApp s dynamickými proměnnými zvýrazněná.

Dynamické proměnné lze přidat do :guilabel:`Body` pomocí :guilabel:`placeholderů“ v
*text*. Do zprávy vložte místo prázdného místa následující text: {{1}}.
Zástupný znak vložte jako „{{2}}“ a postupně jej zvýšete, pokud do textu přidáte další zástupné znaky.

Příklad:
*Následuje text z vzoru těla faktury za platbu:*

Dobrý den,

|Tady je faktura za *{{2}}* z *{{3}}*, celkem *{{4}}{{5}}*.
|Zkontrolovat fakturu nebo zaplatit online: {{6}}

Děkuji

.. viz též:
:ref:`produktivita/whatsapp/vzory`.

Tyto proměnné musí být nakonfigurovány na kartě Variablen v šabloně.
zaslat k schválení na Meta. Nejprve je třeba změnit dynamické proměnné v šabloně.
:guilabel:„Typ“ do „Záznamu“. To umožňuje Odoo odkazovat na pole v záznamu.
Vytvářet jedinečná data v zprávě, která je odesílána.

Dále upravte pole „Záznam“ dynamických proměnných. V poli „Použití“ v
Šablona by měla být upravena předem, aby se zajistilo, že je správný vzor a pole odkazována.

Pro vyhledávání dostupných polí vepište přední název pole do vyhledávacího pole.
Vyhledejte výsledky pro všechny dostupné pole modelu (:guilabel:"Použito u")
vytváří se šablona pro. Může být více úrovní, které je třeba nakonfigurovat.

Příklad:
Následující je příklad proměnných nastavených pro výše uvedené místní proměnné v platbě
přijetí uvedené výše:

...... seznamová tabulka::
:hlavičkové řádky: 1
:kolonky: 1

      * - Jméno
        - Hodnota vzorku
        - Typ
        - Hřiště
      * {{1}}
        - Interiér v modrém
        - Modelářský koutek
        - „Partner“
      * – tělo – {{2}}
        - INV/2022/00001
        - Modelářský koutek
        - „Číslo“
      * {{3}}
        - Moje společnost
        - Modelářský koutek
        - Společnost
      * – tělo – {{4}}
        - $
        - Modelářský koutek
        - „Měna > Znak“
      * {{5}}
        - 4000
        - Modelářský koutek
        - „Množství“
      * {{6}}
        - https://...
        - Portálový odkaz
        -

Příklad:
Příkladem je v záložce Body, pokud se zadá „Ahoj {{1}}“, pak se zobrazí
musí být nastaveny v záložce „Proměnné“. V tomto konkrétním případě by měla zpráva oslovovat
zákazník jménem, takže {{1}} by mělo být nakonfigurováno tak, aby bylo vyplněno {{1}}
:guilabel:`Pole“ s názvem :guilabel:`Zákazník“.

.. varování:
Přizpůsobování šablon aplikace WhatsApp není v rámci podpory Odoo možné.

... produktivita/whatsapp/schválení:

Schválení šablony
~~~~~~~~~~~~~~~~~~~~~~

Po aktualizaci dynamických proměnných na šabloně je nutné šablonu odevzdat do Meta pro
opět schválit. Klikněte na tlačítko „Předložit k schválení“ a začněte proces schvalování. E-mailová zpráva
bude zaslána správci účtu na Meta, jakmile bude schválen.

Po schválení v Meta synchronizujte šablony znovu v databázi Odoo.
dokumentace: :ref:`produktivita/whatsapp/synchronizace`.

..tip:
Zkontrolovat stav aplikace WhatsApp na šabloně Meta Dashboardu, přejděte do
„<https://business.facebook.com/wa/manage/home>“. Pak přejděte na „Nástroje účtu“ ->
Vzory zpráv.

.._produktivita/whatsapp/synchronizace:

Synchronizace šablon
~~~~~~~~~~~~~~~~~

Šablony musí být synchronizovány s databází Odoo po schválení týmem Meta.
začněte tím, že se přesunete na: „Aplikace WhatsApp --> Konfigurace --> WhatsApp Business
Vyberte účty a konfigurace, které chcete synchronizovat. V sekci označené
V sekci „Odesílání zpráv“ v dolní části klikněte na „Synchronizace šablon“.
aktualizovali šablony schválené tak, aby je bylo možné využívat s různými aplikacemi v
databáze.

.. obrázek: whatsapp/sync-template.png
:alt:Synchronizace šablon Meta WhatsApp do databáze Odoo pomocí funkce „Synchronizovat šablony“
zvýrazněny.

Úspěšná zpráva v zeleném odstínu se objeví v pravém horním rohu s počtem šablon
Aktualizováno.

..tip:
Šablony lze také synchronizovat jednotlivě přímo ze šablony. Přejděte na
:menu_vyber:`WhatsApp aplikace --> Šablony“ panelu a vyberte šablonu ke synchronizaci. Pak
Klikněte na tlačítko „Synchronizovat šablonu“ v horním menu formuláře šablony.

Vytváření šablon v Meta
--------------------------

Nejprve přejděte na šablonu Meta pro WhatsApp.
<https://business.facebook.com/wa/manage/home>_ a pak přejděte na:
Šablony zpráv.

.. obrázek:whatsapp/account-tools.png
:alt: Nástroje účtu zvýrazněné v manažerovi stránek s odkazem na správu šablon.

Pro vytvoření šablony WhatsApp klikněte na modrý tlačítko „Vytvořit šablonu“ a poté vyberte
kategorie. Zahrnuty jsou například následující možnosti:
a:guilabel:`Přihlášení“. Většinou se používají první dvě možnosti, pokud uživatel
Chcete poslat heslo nebo něco souvisejícího se zabezpečením?

Zadejte název šablony a pak vyberte jazyk.
šablona.

.. poznámka::
Můžete vybrat více jazyků zadáním názvů jazyka a výběrem ostatních.
jazyky, jak je potřeba.

.. obrázek: whatsapp/template-config.png
:alt:Seznam konfiguračních možností šablony s uvedením marketingu, služeb, názvu a jazyka
zvýrazněny.

Po provedení vhodného výběru klikněte na tlačítko „Pokračovat“ v pravém horním rohu.
Stránka se přesměruje na stránku pro úpravu šablony. Zde je možné upravit hlavičku,
Konfigurace tlačítek, hlavičky a patičky je hotová.
šablona je náhled, jak bude šablona vypadat ve výrobě.

.. obrázek:whatsapp/edit-template.png
:alt: Upravte šablonu pomocí hlavičky, těla, patičky a tlačítek.

Po provedení všech potřebných změn v šabloně klikněte na tlačítko :guilabel:`Odeslat`.
v pravém horním rohu. Otevře se okno k potvrzení jazyka - klikněte
Klikněte na tlačítko „Potvrdit“ k potvrzení a pak se objeví okno, ve kterém je uvedeno, že šablona byla
podán k projednání a schválení společností Meta.

Stav šablony zůstane v :guilabel:`In review“ až do rozhodnutí.
byla provedena společností Meta. Jakmile obdržíte e-mailovou zprávu s potvrzením šablony, šablony budou
musí být synchronizovány z databáze Odoo.

.. viz též:
Pro více informací o konfiguraci šablon na vývojářském portálu Meta navštivte stránku „Meta“.
Dokumentace šablony pro WhatsApp
<https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates/>`.

Oznámení
=============

Oznámení v aplikaci WhatsApp jsou zpracovávána podobně jako konverzace v Odoo. Při příchozím oznámení se zobrazí
Zobrazuje se s přijatou konverzací od zákazníka. Výchozí nastavení notifikací je v
Konfigurace firemního účtu WhatsApp v Odoo.

Nastavení oznámení lze upravit kliknutím na:
Konfigurace --> WhatsApp Business Accounts. Vyberte účet a posuňte se dolů na
:menuselection:`Kontrola“ sekce, kde jsou zpracovávány oznámení. Pod :guilabel:`Upozornit uživatele“
Zadejte do pole název, který uživatelé mají dostávat zprávy o tomto konkrétním kanálu WhatsApp.

.. poznámka::
Jednou z funkcí je také možnost zasílat ostatním uživatelům notifikace, pokud dojde k rozhovoru mezi uživatelem a zákazníkem.
budou zasílány pouze oznámení, která jsou nastavena v konfiguraci firemního účtu WhatsApp.
v konverzaci se objeví. Pokud uživatel neodpoví do 15 dnů,
Odpověď zákazníka po uplynutí patnácti dnů se opět objeví u všech uživatelů, které jsou v poli „Uživatelé“
Nastavení aplikace WhatsApp.

Přidávání uživatelů do chatu
====================

Uživatele lze přidat do chatu WhatsApp rozšířením okna aplikace WhatsApp.
Konverzace jsou umístěny v aplikaci Discuss. Klikněte na ikonu „👤 + (přidat uživatele)“ vedle
a okno se objeví s výzvou k účasti na konverzaci.

.. obrázek:: whatsapp/add-users.png
:alt:Přidání uživatelů do konverzace v aplikaci WhatsApp s vyznačeným ikonou přidat uživatele.

FAQ o WhatsApp API
================

Přezkoumání
------------

Od 1. února 2023 bude aplikace Meta vyžadovat plný přístup k oprávněním pro pokročilé uživatele.
Může být nutné dokončit ověření podnikání, což zahrnuje předložení dokumentů k podnikání v kanceláři.
Meta. „Podívejte se na tuto dokumentaci
<https://developers.facebook.com/docs/development/release/business-verification>.

.. viz též:
„Dokumentace Meta o ověřování přístupu k aplikaci WhatsApp“
<https://developers.facebook.com/docs/development/release/access-verification/>

Chyby šablony
---------------

Upravování šablon může způsobit sledování a chyby, pokud není dodržován přesný proces uvedený výše, zde:
[:ref:`produktivita/whatsapp/vzory`].

Duplicitní chyba ověření
~~~~~~~~~~~~~~~~~~~~~~~~~~

Při synchronizaci šablon může dojít k situaci, kdy existuje více šablon se stejným názvem.
název na manažera obchodu Meta a v Odoo. Toto způsobuje chybovou hlášku při duplicitním ověření.
tento problém, přejmenujte duplicitní šablonu v Odoo a synchronizujte šablony znovu.
podle kroků zde: :ref:`produktivita/whatsapp/synchronizace`.

.. obrázek: validation-error-2.png
:alt:Chyba uživatele, která se objevila v Odoo, když existuje duplicitní šablona.

.. whatsapp/token_error:

Chyby tokenů
------------

Chyba uživatele
~~~~~~~~~~

Pokud se dočasný token nebude nahrazovat trvalým tokenem, objeví se chyba uživatele v Odoo.
Při testování spojení po odeslání zprávy. Chybu lze opravit podle
:ref:`produktivita/whatsapp/token`.

.. obrázek:whatsapp/user-error.png
:alt: Chyba uživatele se objevila v Odoo, když vypršela platnost tokenu.

Chyba uživatele systému 100
~~~~~~~~~~~~~~~~~~~~~

Pokud by měl být uživatel systému při nastavení trvalého tokenu zaměstnancem, došlo k chybě.
Obyvatelů bude 100.

Chybu lze opravit vytvořením uživatele systému s názvem „Admin“, který bude postupovat podle procesu popsaného zde:
:ref:`produktivita/whatsapp/token`.

.. obrázek: whatsapp/user-error-2.png
:alt:Chyba uživatele se objevila v Odoo, když byl vygenerován zaměstnanecký token místo správce.
