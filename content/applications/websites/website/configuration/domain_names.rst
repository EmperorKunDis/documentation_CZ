============
Doménová jména
============

Doménové názvy jsou textová adresa, která identifikuje online umístění, například webovou stránku. Poskytují
pamatovatelnější a rozpoznatelnější způsob, jakým lidé procházejí internetem než čísla IP adres.

Databáze **Odoo Online** a **Odoo.sh** používají poddoménu z domény „odoo.com“
výchozí (např. mycompany.odoo.com).

Můžete však použít vlastní doménu místo toho, že si zaregistrujete volnou doménu:
<název domény/registrace> (pouze pro databáze Odoo Online) nebo konfigurací
doménu, kterou již vlastníte (<domain-name/existing>).

.. viz též:
   - „Návody k Odoo: Zaregistrujte si zdarma doménu [video]
<https://www.odoo.com/slides/slide/registrace-bezplatného-doménového-jména-1663>
   - „Kouzelná stránka – Konfigurace doménových webů [PDF]
<https://drive.google.com/drive/folders/1sXbp7sC6TKG2v-8hcRAMhA6ftKmRxba_>

..._doména/registrace:

Zaregistrujte si zdarma doménu s Odoo
=====================================

Pro registraci jednoleté bezplatné domény pro vaši databázi Odoo Online se přihlaste do svého účtu a
Přejděte na „správce databáze“ (https://www.odoo.com/my/databases). Klikněte na ikonu
Tlačítko vedle názvu databáze a vyberte ikony „svět“
Jména.

.. obrázek:doménové_jméno/doménová_jména.png
:alt: Přístup k konfiguraci doménových jmen databáze

Hledejte požadovaný název domény a ověřte jeho dostupnost.

.. obrázek: doménové_jméno/vyhledávání_domény.png
:alt:Hledání volné domény

..tip:
Zajistěte instalaci aplikace Webové stránky, pokud se možnost registrace doménového jména nezobrazí.

Vyberte požadované doménové jméno, vyplňte formulář „Domovský majitel“ a klikněte
:guilabel:`Registrace“. Vybraný název domény je přímo propojen s databází.

.. obrázek: doménové_názvy/domácí_vlastník.png
:alt:Vyplnění údajů o vlastníkovi domény

Dále byste měli:ref:`přidělit doménu vašemu webu Odoo <doména/webová mapa>“.

.. důležité:
Na zadanou e-mailovou adresu bude zaslán ověřovací e-mail od „noreply@domainnameverification.net“.
poskytnuté v poli „Domovská stránka“ formuláře „Vlastník domény“. Je nezbytné ověřit svou e-mailovou adresu,
udržet doménu aktivní a obdržet nabídku na prodloužení před vypršením platnosti.

Registrace doménového jména je zdarma po dobu prvního roku. Po uplynutí této lhůty bude Odoo pokračovat
správa domény ve spolupráci s registrací doménových jmen **Gandi.net** a budete
zaúčtovala „obnovovací poplatek“ pro doménu „Gandi.net“ <https://www.gandi.net/en/domain>. Odoo odesílá obnovení
citace každý rok na e-mailovou adresu uvedenou v :guilabel:`Domaineigentümer` formuláři několik
před uplynutím platnosti domény. Doména se automaticky obnoví, pokud
Citace je potvrzena.

.. poznámka::
   - Tato nabídka je k dispozici pouze pro databáze Odoo Online.
   - Nabídka je omezena na jednu doménu na klienta.
   - Nabídka se vztahuje pouze na registraci nové domény.
   - Tato nabídka je dostupná pro plány One App Free. Ujistěte se, že váš web obsahuje dostatek
originální obsah pro Odoo, abyste mohli ověřit, že váš požadavek je legitimní a respektuje
Pravidla používání (Acceptable Use Policy) <https://www.odoo.com/acceptable-use>. Vzhledem k vysokému počtu
Pokud jsou požadavky v pořádku, může trvat několik dní, než je Odoo zkontroluje.

..._doménové_jméno/registrace_DNS:

DNS záznamy
-----------

Pro správu vašich bezplatných doménových záznamů DNS otevřete „správce databáze“.
Klikněte na tlačítko „Nastavení“ vedle ikony „nástrojů“
Název databáze, vyberte ikony: „fa-globe“ a „Doménové názvy“, klikněte na „DNS“.

- :guilabel:A: záznam A obsahuje IP adresu domény. Vytváří se automaticky a
Nelze je upravit nebo smazat.
- :guilabel:`CNAME“: CNAME záznamy směrují jeden doménový nebo poddoménový název na jiný doménový název.
automaticky vytvořené pro přesměrování domény www. na databázi. Pokud je databáze přejmenována,
CNAME záznam musí být také přejmenován.
- :guilabel:`MX“: Záznamy MX informují servery, kam mají doručovat e-maily.
- :guilabel:`TXT“: TXT záznamy lze použít k různým účelům (např. pro ověření doménového jména
(vlastnictví).

Každá změna záznamů v DNS může trvat až **72 hodin**, než se rozšíří po celém světě na všech
serverů.

.. poznámka::
„Kontaktujte podporu Odoo <https://www.odoo.com/help>“ pokud potřebujete pomoc při správě svého doménového jména
jméno.

Poštovní schránka
-------

Jednoletá nabídka zdarma na doménu nezahrnuje e-mailovou schránku, existují dvě možnosti propojení
Vaše doménové jméno s e-mailovou schránkou.

Použijte poddoménu
~~~~~~~~~~~~~~~

Můžete vytvořit poddoménu (například „poddoména.vašedoména.com“), která bude sloužit jako alternativní doména pro
databáze, která umožňuje uživatelům vytvářet záznamy v databázi z e-mailů přijatých na jejich
Alias „email@subdomain.yourdomain.com“.

Pro to otevřete „správce databází“ (https://www.odoo.com/my/databases), klikněte na
Klikněte na tlačítko „:icon:`fa-gear`“ („:guilabel:`gear`“) vedle názvu databáze a vyberte :icon:`fa-globe`.
Klikněte na „DNS“ a poté na „Přidat záznam“.
„CNAME“. Následně zadejte požadovanou poddoménu do pole „Jméno“ (např.
(např. subdoména), původní databáze s tečkou na konci (např. mycompany.odoo.com.)
poli „Obsah“ a klikněte na „Přidat záznam“.

Pak přidejte doménu alias jako vlastní doménu kliknutím na „Použít vlastní doménu“ a zadejte
Přezdívkový doménový název (například „subdoména.vaše-doména.com“), klikněte na tlačítko „Zkontrolovat“ a potom
„Potvrzuji, že je hotovo“.

Poté přejděte do databáze a otevřete nastavení. Pod :guilabel:`Alias Domain`
pole, zadejte doménové jméno (např. „subdoména.vašedoména.cz“), klikněte na tlačítko :guilabel:`Vytvořit“ a potom
:guilabel:`Uložit“.

Použijte externí e-mailový poskytovatel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pokud chcete používat externí e-mailový server, musíte nastavit záznam MX. Pro provedení této akce otevřete
manažer, klikněte na tlačítko :icon:`fa-gear` (:guilabel:`gear`)
Vyberte vedle názvu databáze a klikněte na ikonu „Globus“ a poté na „Domény“.
„DNS“, pak „Přidat záznam DNS“ a vyberte „MX“. Hodnoty, které byste měli
Vstup do políček pro jméno, obsah a prioritu závisí na
externí poskytovatel e-mailových služeb.

.. viz též:
   - „Google Workspace: Hodnoty záznamů MX <https://support.google.com/a/answer/174125?hl=cs>“
   - „Outlook a Exchange Online: Přidání záznamu MX pro e-mail <https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider?view=o365-worldwide#add-an-mx-record-for-email-outlook-exchange-online>“

Google Workspace
****************

Používat svůj volný doménový název na Gmailu, zaregistrujte se do služby „Google Workspace
<https://workspace.google.com>.

Při registraci vyberte možnost „Nastavení pomocí stávající domény“
:guilabel:`Vyberte způsob, jak nastavit svůj účet“ a zadejte doménu (např. „yourdomain.com“)
Zeptal se: „Jaká je doména vaší společnosti?“.

Kontrola vlastnictví domény
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#Přihlaste se do služby Google Workspace. Když vám bude nabídnuto ověření vašeho doménového jména, klikněte na tlačítko „Přepnout na
manuální kontrola.

.... obrázek: doménové_jméno/ověřit_a_přepnout.png
:alt:Přepnutí na manuální ověřování domény v G Suite

#Vyberte „gandi.net“ jako doménový host a klikněte na „Pokračovat“.

.... obrázek: doménové_jméno/ověření_domény.png
:alt:Vybrat doménový host na Googlu

#Zkopírujte obsah pole „Hodnota“ podle záznamu TXT. Zanechte okno
otevřené.

.... obrázek: doménové_jméno/ověřovací_kód.png
:alt:Kopírování hodnoty TXT na Google Workspace

#Otevřete „správce databáze“ (https://www.odoo.com/my/databases), klikněte na ikonu
tlačítko vedle názvu databáze a vyberte ikonu „globus“
Vyberte možnost „Názvy“. Klikněte na položku „DNS“, poté na „Přidat záznam DNS“ a vyberte „TXT“.

#Zadejte do pole „Jméno“ znak @ a vložte hodnotu, kterou poskytla společnost Google.
poli „Obsah“ a klikněte na „Přidat záznam“.

...... obrázek:: doménové_jméno/workspace-txt.png
:alt: Vytvoření TXT záznamu k ověření vlastnictví domény

#Zpět do služby Google Workspace, zaškrtněte políčko v dolní části a klikněte na tlačítko „Potvrdit“.

.. viz též:
„Google Workspace Admin Help: Verify your domain with a TXT record
<https://support.google.com/a/answer/16018515>

Přesměrujte e-maily na Gmail
^^^^^^^^^^^^^^^^^^^^^^^^

#Otevřete „správce databáze“ (https://www.odoo.com/my/databases), klikněte na ikonu
tlačítko vedle názvu databáze a vyberte ikonu „globus“
Klikněte na „Názvy“. Vyberte možnost „DNS“ a poté klikněte na „Přidat záznam DNS“. Zvolte „MX“.

#V poli „Jméno“ zadejte @, do pole „Důležitost“ zadejte 1.
V poli „Obsah“ zadejte „smtp.google.com.“ a klikněte na „Přidat záznam“.

.. obrázek: doménová jména/workspace-mx.png
:alt: Vytvoření záznamu MX pro přesměrování e-mailů na Gmail

#Otevřete „Konzoli pro správu Google Workspace <https://admin.google.com/ac/domains/manage>“ a klikněte
:guilabel:`Aktivujte Gmail pro svou doménu“ a postupujte podle pokynů.

.. viz též:
„Nápověda pro správce služby Google Workspace: Nastavení záznamů MX pro službu Google Workspace
<https://support.google.com/a/answer/16004259>

.._doménové jméno/existující:

Nastavte existující doménu
=================================

Pokud již máte doménu, můžete ji použít pro svou webovou stránku Odoo.

.. varování:
Je doporučeno postupovat v pořadí těchto tří kroků, aby se předešlo jakémukoliv :ref:`SSL
validace certifikátu <doména/ssl> vydává následující chyby:

   #:ref:`Přidejte záznam CNAME <doménové jméno/cname>“
   #:ref:`Přesměrujte svou doménu bez koncovky <doména bez koncovky>/naked>“ (volitelné, ale doporučené)
   #:ref:`Připojte doménu k databázi Odoo <doména/připojení k databázi>`
   #:ref:`Připojte doménu k webovým stránkám Odoo <doména/webové stránky>“

.._doménové jméno/cname:

Přidej záznam typu CNAME
------------------

Přidání záznamu CNAME, který směruje doménové jméno na adresu vaší databáze Odoo, je nutné.

.. záložky::

...... skupina-tab::Odoo Online

Za cílovou adresu záznamu CNAME by měla být zadána adresa databáze, jak byla definována při jejím vytvoření
(např. „mycompany.odoo.com“).

...... skupina-tab:: Odoo.sh

Záznam CNAME by měl směřovat na hlavní adresu projektu, kterou lze najít na
Odoo.sh by se mělo přepnout na „Nastavení“ -> „Projekt“, nebo konkrétní větve
(výroba, uvedení nebo vývoj) tím, že se přepnete na:menu:Branches --> vyberte
větve --> Nastavení --> Vlastní domény“ a kliknutím na „Jak nastavit svou doménu“.
zpráva ukazuje, na kterou adresu by měl být váš záznam CNAME namířený.

Specifické pokyny se liší podle poskytovatele služby DNS.

.. viz též:
   - „GoDaddy: Přidejte záznam CNAME <https://www.godaddy.com/help/add-a-cname-record-19236>“
   - „Namecheap: Jak vytvořit záznam CNAME pro doménu <https://www.namecheap.com/support/knowledgebase/article.aspx/9646/2237/how-to-create-a-cname-record-for-your-domain>“
   - „OVHcloud: Přidat nový záznam DNS <https://docs.ovh.com/us/en/domains/web_hosting_how_to_edit_my_dns_zone/#add-a-new-dns-record>“
   - Cloudflare: Spravujte záznamy DNS


..._doména/bez obrázku:

Přesměrovat nahou doménu
-----------------------

.. poznámka::
Přestože je tento krok volitelný, doporučujeme jej provést.

Umožnit návštěvníkům používat vaši doménu bez jakýchkoliv poddomén nebo předpon.
(`vase-domena.cz“), vytvořit trvalé přesměrování:
je nutné zadat:

- z http://vašedoména.cz na https://www.vašedoména.cz
- z „https://vase-domena.cz“ na „https://www.vase-domena.cz“.

Specifické pokyny se liší podle poskytovatele služeb DNS. Někteří z nich však nabízejí
Přesměrovat nahý doménu na zabezpečené HTTPS připojení. Pokud narazíte na nějakou chybu, doporučujeme
:ref:`přes Cloudflare <doménové jméno bez zástupné značky/cloudflare>.

..._doménové jméno/nezahalené/Cloudflare:

Použití Cloudflare k zabezpečení a přesměrování domény bez koncovky
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#„Přihlásit se a přihlásit se do Cloudflare <https://dash.cloudflare.com/sign-up>“.
#Zadejte své doménové jméno na panelu Cloudflare <https://dash.cloudflare.com/login>
vyberte možnost „Rychlý skener pro záznamy DNS“.
#Vyberte si plán (zdarma je dostačující).
#Postupujte podle pokynů a doporučení společnosti Cloudflare, abyste aktivovali své účty.
#Přidejte záznam typu CNAME, který směruje doménu bez předpony („yourdomain.com“) na poddoménu „www“.
(např. www.vašedoména.cz) kliknutím na položku „DNS“ v navigačním menu a poté kliknutím
tlačítko „Přidat záznam“ a použijte následující konfiguraci:

   - :guilabel:`Typ`: CNAME
   - :guilabel:`Jméno“:@ (nebo „vašedoména.cz“)
   - :guilabel:`Zaměření“: například „www.vašedoména.cz“
   - :guilabel:`Stav proxy“: Proxy

.... obrázek: doménové_jméno/cloudflare-cname-www.png
:alt:Přidání záznamu CNAME do DNS Cloudflare, který přesměruje doménu bez www na poddoménu www.

#Přidejte další záznam CNAME, abyste přesměrovali poddoménu www (například www.yourdomain.com) na
adresu databáze (např. „mycompany.odoo.com“) pomocí následující konfigurace:

   - :guilabel:`Typ`: CNAME
   - :guilabel:`Název“: např. „www.vašedoména.cz“
   - :guilabel:`Název cíle“ např. „mycompany.odoo.com“
   - :guilabel:`Stav proxy“: pouze DNS

.. obrázek: doménová_jména/cloudflare-cname-db.png
:alt:Přidání záznamu CNAME do DNS Cloudflaře, aby se www poddoména odkazovala na databázi Odoo

#Definujte pravidlo pro přesměrování, které trvale přesměruje (301) vaši doménu bez koncovky (např. „yourdomain.com“).
a k oběma „http://“ i „https://“ přejděte na: „Nastavení -> Vytvořit pravidlo -> Produkty“.
a kliknutím na tlačítko „Vytvořit pravidlo“ pod „Pravidly přesměrování“:

   - Zadejte libovolný název pravidla: guilabel:Rule name.
   - V části „Pokud příchozí požadavky odpovídají…“ vyberte možnost „Vlastní filtr“.
výraz a použít následující konfiguraci:

     - :guilabel:`Field“:Host
     - :guilabel:`Operátor“: rovná se
     - :guilabel:`Hodnota“: např. „yourdomain.com“

   - V sekci „Pak…“ použijte následující konfiguraci:

     - :guilabel:`Typ“: Dynamický
     - :guilabel:`Výraz“: například, „concat('https://www.yourdomain.com', http.request.uri.path)“
     - :guilabel:`Kód stavu“: 301
     - :guilabel:`Uchovat záznamy v dotazovacím řetězci“: zapnuto

.... obrázek: doménové_jméno/cloudflare-redirect-rule.png
:alt:Definování pravidla pro přesměrování Cloudflare, aby vytvořilo trvalé přesměrování (301).

#Přejděte do části „SSL/TLS“ a nastavte režim šifrování na „Full“.

.... obrázek: doménové_jméno/cloudflare-encryption.png
:alt:Nastavení šifrování na plný výkon v Cloudflaře

..._doménové jméno/databáze map:

Přidělit doménu k databázi Odoo
-------------------------------------

.. varování:
Zajistěte si, že máte vytvořený záznam CNAME pro doménu ve svém DNS
**předtím, než přidělíte své doménové jméno k databázi Odoo.

Pokud tak neučiníte, může se stát, že nebude možné ověřit certifikát :ref:`<doména/ssl>`.
Může to vést k chybě „názvu certifikátu“. Prohlížeče často tuto chybu zobrazují jako
varování typu „Váš prohlížeč není soukromý“.

Pokud se vám tento problém objeví po přidělení doménového jména k databázi, počkejte až na pět
dní, protože ověření může ještě probíhat. Pokud ne, můžete podat „ticket
, včetně obrázků vašich záznamů CNAME.

.. záložky::

...... skupina-tab::Odoo Online

Otevřete „správce databáze“ (https://www.odoo.com/my/databases), klikněte na ikonu
vedle názvu databáze tlačítko (:guilabel:`gear`) a vyberte ikony „globe“ (:guilabel:`Domain
Jména a klikněte na „Použít vlastní doménu“. Pak zadejte název domény (např.
„(www.vašedoména.cz)“, klikněte na „Potvrdit“ a „Jsem si jistý/á, že je to hotové“.

.. obrázek: doménové_jméno/mapa_databáze_online.png
:alt:Přidělení doménového jména pro databázi Odoo Online

...... skupina-tab:: Odoo.sh

Na Odoo.sh přejděte na: „Branches“ -> „Vyberte svou větve“ -> „Nastavení“ -> „Přizpůsobené
doménách“, zadejte název domény, kterou chcete přidat, a pak klikněte na „Přidat doménu“.

.. obrázek: doménové_jméno/mapa_databáze_sh.png
:alt:Přidělení doménového jména odnoži Odoo.sh

.. viz také:
:ref:`Odoo.sh větve: nastavení záložka <odoosh-gettingstarted-branches-tabs-settings>`

..._doména/ssl:

Šifrování SSL (protokolem HTTPS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Šifrování SSL** umožňuje návštěvníkům procházet webovou stránku prostřednictvím zabezpečeného připojení, které se na obrazovce zobrazuje
jako protokol https:// na začátku adresy webu místo nezabezpečeného http://
protokol.

Odoo vytváří samostatný SSL certifikát pro každou doménu, která je „připojena“ k databázi
„<název domény/databáze mapy>“ pomocí „certifikačního orgánu Let’s Encrypt a protokolu ACME“.
<https://letsencrypt.org/how-it-works/>

.. poznámka::
   - Vygenerování certifikátu může trvat až 24 hodin.
   - Vaše certifikát je ověřován několikrát za pět dní po tom, co jste svůj doménu zmapovali
do databáze.
   - Pokud používáte jiný systém, můžete ho nadále používat nebo přejít na Odoo.

.. důležité:
Žádný SSL certifikát se negeneruje pro domény bez poddomén :dfn:`(domény bez jakýchkoliv poddomén).
nebo předpony).

.._doména/webová základní URL:

URL webové databáze
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. poznámka::
Pokud máte aplikaci Webové stránky nainstalovanou na databázi, přeskočte tento oddíl a pokračujte od bodu
:ref:`Přidružit doménu k webové stránce <doména/webová stránka>“.

URL adresy webového serveru nebo kořenové URL databáze ovlivňuje hlavní adresu vašeho webu a všechny
odkazů posílaných vašim zákazníkům (např. cenová nabídka, odkaz na portál atd.)

Chcete-li udělat svou vlastní doménu webovým základním URL vaší databáze, přihlaste se do ní pomocí
vlastní doménové jméno a přihlášení jako administrátor (uživatel s oprávněním přístupu do nastavení)
skupina pod správou).

.. důležité:
Pokud se k databázi připojíte pomocí původního adresu Odoo (např. „mycompany.odoo.com“), pak
Základní URL vaší databáze bude aktualizováno podle potřeby. Chcete-li zabránit automatické aktualizaci,
*URL adresy webu* při přihlášení administrátora do databáze aktivovat režim vývojáře
<developer-mode>`, přejděte na: „Nastavení“ --> „Technické“ --> „Systémové parametry“ --> „Nový“,
a zadejte „web.base.url.freeze“ jako klíč a hodnotu „True“.

.. poznámka::
Můžete také ručně nastavit základní adresu URL webu. Chcete-li tak učinit, zapněte režim vývojáře.
<developer-mode>`, přejděte do: „Nastavení“ --> „Technické“ --> „Parametry systému“.
hledejte klíč web.base.url (vytvořte ho, pokud je třeba) a zadejte celou adresu vašeho
webové stránky jako hodnotu (např. „https://www.yourdomain.com“). URL musí obsahovat protokol
„https://“ (nebo „http://“) a nekončit lomítkem („/“).

..._doménové jméno/mapa webu:

Přidružit doménu k webu Odoo
------------------------------------

Přidělení doménového jména webu je odlišné od přidělení databáze:

- Určuje doménové jméno jako hlavní pro váš web a pomáhá vyhledávačům při indexování vašeho
webové stránky správně.
- Určuje doménové jméno jako základní URL pro databázi včetně odkazů na portál posílaných
e-mail zákazníkům.
- Pokud máte více webových stránek, přesměruje váš doménový název na příslušnou webovou stránku.

Přejděte na:menu:Website --> Konfigurace --> Nastavení. Pokud máte více webů, vyberte
ten, který chcete nakonfigurovat. V poli „Doména“ zadejte adresu svého webu
(např. https://www.vašedoména.cz) a stiskněte klávesu Enter.

.. varování:
Přidělení doménového jména vašemu webu Odoo zabraňuje indexování původního obsahu vyhledávačem Google.
adresa databáze (např. „mycompany.odoo.com“).

Pokud jsou obě adresy již indexovány, může trvat nějaký čas, než se indexace druhé adresy dokončí.
adresa je ze služby Google Search odstraněna. Můžete použít „Google Search Console“.
<https://www.google.com/webmasters/tools/home>

.. poznámka::
Pokud máte na své databázi více webů a společností, ujistěte se, že vyberete ten správný.
:guilabel:`Společnost“ pod :menuselection:`Webová stránka --> Konfigurace --> Nastavení“.
Odoo určuje, jaké URL použít jako základní URL podle :ref:`domény a webového základního URL <domain-name/web-base-url>`.
společností.

..tip:
Při migraci z existujícího webu se ujistěte, že jsou nastaveny potřebné :ref:`přesměrování <web/stránky/url-redirection>
Před přidáním doménového jména. Například pokud byla předchozí adresa ve tvaru /path/about/something
existovalo, přesměrujte jej na novou odpovídající stránku vašeho webu Odoo, například na „/něco“.
