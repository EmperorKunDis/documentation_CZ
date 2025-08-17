... tiskárny ePOS:

=========================================
Selbounesignovaný certifikát pro tiskárny ePOS
=========================================

Pro práci s Odoo jsou potřeba tiskárny některých modelů, které lze používat bez
„IoT systém“ může vyžadovat „protokol HTTPS“ (<https>).
Uzavřít bezpečnou síťovou spojení mezi prohlížečem a tiskárnou.
IP adresa tiskárny pomocí protokolu HTTPS vede na stránku varování ve většině prohlížečů. V takovém případě můžete
dočasně: „připojit se k síti <epos_ssc/instructions>“, což vám umožní dosáhnout stránky
v HTTPS a používat tiskárnu ePOS v Odoo, dokud je otevřená okna prohlížeče.

.. varování:
Připojení se ztratí po zavření okna prohlížeče. Proto by tento způsob měl být používán jen výjimečně.
použít jako řešení problému nebo jako předpoklad pro následující pokyny:
<epos_ssc/návod>.

... _epos_ssc/návod:

Vytvořit, exportovat a importovat certifikáty podepsané vlastními klíči
=====================================================

Pro dlouhodobé řešení je nutné vytvořit **certifikát podepsaný vlastním klíčem**. Poté jej vyexportovat a importovat
je do prohlížeče.

.. důležité:
Vytváření SSL certifikátu by se mělo provádět pouze jednou. Pokud vytvoříte další
certifikátu, zařízení používající předchozí certifikát ztratí přístup k HTTPS.

.. záložky::

....... tab:: Windows 10 a operační systém Linux

... záložky::

.. tab:: Vytvoření samozasíťovaného certifikátu

Navštivte adresu IP ePOS (např. „https://192.168.1.25“) a zobrazte stránku.
spojení kliknutím na „Pokročilé“ a „Přejít na [IP adresu]
(nebezpečné).

.. obrázek:: epos_ssc/browser-https-insecure.png
:skal: 75 %
:alt: varovná stránka o soukromí přihlášení na Google Chrome

Varovná stránka v prohlížeči Google Chrome na operačním systému Windows 10

Pak se přihlaste pomocí svých tiskárenských údajů a zobrazte nastavení tiskárny ePOS.
se přihlaste, zadejte do pole „ID“ hodnotu „epson“ a sériové číslo tiskárny do pole
:guilabel:`Heslo“ pole.

Klikněte na „Seznam certifikátů“ v sekci „Autentizace“ a klikněte
:guilabel:`vytvořit“ pro vytvoření nového **certifikátu podepsaného vlastními klíči**.
Název by se měl automaticky vyplnit. Pokud ne, doplňte ho adresou tiskárny
číslo. Vyberte roky, po které bude certifikát platný v poli:guilabel:`Platnost
Do pole „Období“ klikněte na tlačítko „Vytvořit“, „Znovu nastavit“ nebo ručně restartujte
tiskárna

Vytvoří se samozřejmě podepsaný certifikát, stránku znovu načtěte a klikněte na „SSL/TLS“.
v sekci „Zabezpečení“ a zajistit, aby byl certifikát podepsaný sám sebou správně nastaven.
vybrány v sekci „Certifikát serveru“.

.. tab::Export certifikátu s vlastním podpisem

Exportní proces je silně závislý na operačním systému a
prohlížeč. Začněte přístupem k nastavením tiskárny ePOS na webovém prohlížeči, a to pomocí navigace
na jeho IP adresu (např. „https://192.168.1.25“). Poté připojení zavolejte
Vysvětleno je v záložce **Vytvoření samozasíťovaného certifikátu**.

Pokud používáte prohlížeč **Google Chrome**,

            #Klikněte na „Není bezpečné“ vedle vyhledávací lišty a „Soubor certifikátu není
není platný`;

.. obrázek::epos_ssc/browser-warning.png
:alt:Nepovolená tiskárna v prohlížeči Google Chrome.

            #Přejděte na záložku „Podrobnosti“ a klikněte na „Export“.
            #Přidejte na konec názvu souboru příponu „.crt“, aby měl správnou příponu;
            #Vyberte:„Základní šifrování ASCII, jediný certifikát“, na spodku
okno s upozorněním.
            #a certifikát je vyexportován.

.. varování::
Zajistěte si, aby certifikát končil příponou .crt. Jinak některé
Prohlížeče mohou během procesu importu soubor nevidět.

Pokud používáte prohlížeč **Mozilla Firefox**,

            #klikněte na ikonu zámku vlevo od adresního řádku.
            #. jít na: menu výběru:„Připojení není bezpečné – více informací“ – „Karta zabezpečení
--> Zobrazit certifikát“;

... obrázek::epos_ssc/mozilla-not-secure.png
:alt:Tlačítko Připojení není bezpečné v prohlížeči Mozilla Firefox

            #. posuňte se dolů do části „Různé“;
            #Klikněte na „Stáhnout“ v části „PEM (cert)“.
            #a certifikát je vyexportován.

.. tab::Import certifikátu podepsaného vlastními klíči

Proces dovozu je silně závislý na operačním systému a
prohlížeč.

.. tabulky::

.. tab:: Windows 10

Windows 10 spravuje certifikáty, což znamená, že pro samozřejmě podepsané certifikáty musí být
importované z certifikačního souboru namísto prohlížeče. Pro takové použití

                  #Otevřete okno Windows File Explorer a najděte stažený certifikační soubor.
                  #Klikněte pravým tlačítkem na certifikační soubor a klikněte na:guilabel:'Instalovat
„Certifikát“;
                  #Vyberte, kde chcete certifikát nainstalovat a pro koho – buď pro
:guilabel:`Současný uživatel“ nebo všechny uživatele (:guilabel:`lokalní stroj“). Pak klikněte
:guilabel:`Další“;
                  #na obrazovce „Uložiště certifikátů“ zaškrtněte políčko „Veškeré certifikáty uložit do
následující obchod, klikněte na tlačítko „Procházet…“ a vyberte
:guilabel:`Důvěryhodné kořenové certifikační autority“;

.. obrázek::epos_ssc/win-cert-wizard-store.png

                  #Klikněte na tlačítko „Ukončit“ a přijměte okno zabezpečení.
                  #Znovu spusťte počítač, aby se změny aplikovaly.

.. tab::Linux

Pokud používáte prohlížeč **Google Chrome**,

                  #Otevřete si prohlížeč Chrome.
                  #. jít na:menu:Nastavení --> Soukromí a zabezpečení --> Zabezpečení -->
Správa certifikátů
                  #Přejděte na záložku „Úřady“, klikněte na „Import“ a vyberte
exportovaný certifikační soubor.
                  #přijímat všechna varování.
                  #klikněte na tlačítko OK.
                  #Restartujte prohlížeč.


Pokud používáte prohlížeč **Mozilla Firefox**,

                  #Otevřete prohlížeč Firefox.
                  #. jít na:menu:Nastavení --> Soukromí a zabezpečení --> Zabezpečení --> Zobrazit
Certifikáty... --> Import
                  #Vyberte exportovaný certifikační soubor.
                  #zaškrtněte políčka a ověřte.
                  #Restartujte prohlížeč.

....... tab:: Mac OS

Na operačním systému MacOS lze zabezpečit připojení pro všechny prohlížeče podle těchto kroků:

      #Otevřete Safari a přejděte na adresu vašeho tiskárny. To vede k varovné stránce;
      #na stránce varování přejděte na: menu výběru: Zobrazit podrobnosti - navštivte tuto webovou stránku - Navštivte
Webové stránky`, ověřit
      #Restartujte tiskárnu, abyste ji mohli používat s jakýmkoli jiným prohlížečem.

Chcete-li vytvořit a exportovat certifikát SSL a odeslat jej do zařízení iOS, otevřete **Google Chrome**
nebo **Mozilla Firefox**. Pak

... záložky::

.. tab:: Vytvoření samozasíťovaného certifikátu

Navštivte adresu IP ePOS (např. „https://192.168.1.25“) a zobrazte stránku.
spojení kliknutím na „Pokročilé“ a „Přejít na [IP adresu]
(nebezpečné).

.. obrázek:: epos_ssc/browser-https-insecure.png
:skal: 75 %
:alt:Varovná stránka o soukromí při připojení na Google Chrome

Varovná stránka v prohlížeči Google Chrome na operačním systému Windows 10

Pak se přihlaste pomocí svých tiskárenských údajů a zobrazte nastavení tiskárny ePOS.
se přihlaste, zadejte do pole „ID“ hodnotu „epson“ a sériové číslo tiskárny do pole
:guilabel:`Heslo“ pole.

Klikněte na „Seznam certifikátů“ v sekci „Autentizace“ a klikněte
:guilabel:`vytvořit“ pro vytvoření nového **certifikátu podepsaného vlastními klíči**.
Název by se měl automaticky vyplnit. Pokud ne, doplňte ho adresou tiskárny
číslo. Vyberte roky, po které bude certifikát platný v poli:guilabel:`Platnost
Do pole „Období“ klikněte na tlačítko „Vytvořit“, „Znovu nastavit“ nebo ručně restartujte
tiskárna

Vytvoří se samozřejmě podepsaný certifikát, stránku znovu načtěte a klikněte na „SSL/TLS“.
v sekci „Zabezpečení“ a zajistit, aby byl certifikát podepsaný sám sebou správně nastaven.
vybrány v sekci „Certifikát serveru“.

.. tab::Export certifikátu s vlastním podpisem

Exportní proces je silně závislý na operačním systému a
prohlížeč. Začněte přístupem k nastavením tiskárny ePOS na webovém prohlížeči, a to pomocí navigace
na jeho IP adresu (např. „https://192.168.1.25“). Poté připojení zavolejte
Vysvětleno je v záložce **Vytvoření samozasíťovaného certifikátu**.

Pokud používáte prohlížeč **Google Chrome**,

            #Klikněte na „Není bezpečné“ vedle vyhledávací lišty a „Soubor certifikátu není
není platný`;

.. obrázek::epos_ssc/browser-warning.png
:alt:Nebezpečná spojení s tiskárnou - tlačítko v prohlížeči Google Chrome

            #Přejděte na záložku „Podrobnosti“ a klikněte na „Export“.
            #Přidejte na konec názvu souboru příponu „.crt“, aby měl správnou příponu;
            #Vyberte:„Základní šifrování ASCII, jediný certifikát“, na spodku
okno s upozorněním.
            #a certifikát je vyexportován.

.. varování::
Zajistěte si, aby certifikát končil příponou .crt. Jinak některé
Prohlížeče mohou během procesu importu soubor nenajít.

Pokud používáte prohlížeč **Mozilla Firefox**,

            #klikněte na ikonu zámku vlevo od adresního řádku.
            #. jít na: menu výběru:„Připojení není bezpečné – více informací“ – „Karta zabezpečení
--> Zobrazit certifikát“;

.. obrázek: epos_ssc/mozilla-not-secure.png
:alt:Tlačítko Připojení není bezpečné v prohlížeči Mozilla Firefox

            #. posuňte se dolů do části „Různé“;
            #Klikněte na „Stáhnout“ v části „PEM (cert)“.
            #a certifikát je vyexportován.

.......::Android

Chcete-li do zařízení s Androidem nahrát certifikát SSL, nejprve jej vytvořte a exportujte z něj.
počítač. Následně převeďte soubor .crt do zařízení pomocí e-mailu, bezdrátového připojení nebo USB.
soubor je na zařízení.

      #Otevřete nastavení a vyhledejte „certifikát“.
      #Klikněte na:guilabel:Soubor certifikátu AC" (Instalace z úložiště zařízení).
      #Vyberte certifikační soubor, který chcete nainstalovat na zařízení.

....... Poznámka::
Konkrétní kroky pro instalaci certifikátu se mohou lišit v závislosti na verzi
Android a výrobce zařízení.

....... tab:: iOS

Do zařízení s operačním systémem iOS je nutné nejprve certifikát z počítače vytvořit a následně jej exportovat.
Poté převeďte soubor .crt do zařízení pomocí e-mailu, Bluetooth nebo jakéhokoliv jiného způsobu sdílení.
služby.

Stáhnutí souboru vyvolá varovné okno. Klikněte na tlačítko „Povolit“ pro stažení
konfigurační profil a zavřete druhé okno. Pak

      #Přejděte do aplikace Nastavení na zařízení s operačním systémem iOS.
      #Klikněte na „Stáhnout profil“ pod oknem s detaily uživatele.
      #. najít stažený soubor s příponou „.crt“ a vybrat jej;
      #Klikněte na tlačítko „Instalovat“ v pravém horním rohu obrazovky.
      #Pokud je na zařízení nastaveno heslo, zadejte heslo.
      #Klikněte na tlačítko „Instalovat“ v horním pravém rohu obrazovky varování o certifikátu a vyskočí okno.
okno;
      #Klikněte na tlačítko „Hotovo“.

.. obrázek: epos_ssc/ssl-ios-verified.png

Certifikát je nainstalován, ale stále potřebuje ověřit.

      #. jít na: menu „Nastavení“ -> „Obecné“ -> „O aplikaci“ -> „Nastavení důvěryhodnosti certifikátu“;
      #. povolit certifikát nainstalovaný pomocí tlačítka „Slide“;
      #Klikněte na tlačítko „Pokračovat“ v okně s upozorněním.

.. důležité:
   - Pokud potřebujete exportovat SSL certifikáty z operačního systému nebo prohlížeče, které ne
nebylo zmíněno, vyhledejte „Export SSL certifikátu“ + „název vašeho prohlížeče nebo operačního
„systém“ ve své oblíbené vyhledávačce.
   - Podobně je možné do importovat certifikáty z nezmíněných operačních systémů nebo prohlížečů pomocí hledání „import SSL
certifikační autorita kořenového certifikátu a název vašeho prohlížeče nebo operačního systému.
vyhledávač.

Zkontrolujte, zda byl certifikát správně importován
===============================================

Připojte se k IP adrese tiskárny pomocí protokolu HTTPS, abyste si ověřili, že je připojení zabezpečené. Například
otevřete v prohlížeči adresu „https://192.168.1.25“. Pokud je certifikát SSL aplikován
správně byste už neměli vidět varovnou stránku a v adresním řádku se měl objevit zámek.
ikonou, která ukazuje, že je připojení bezpečné.
