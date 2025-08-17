=======
Belgie
=======

.._belgie/konfigurace:

Konfigurace
=============

Nainstalujte balíček fiskálního umístění „Belgie“ (⚠️)
<fiskální lokality/balíčky> získat všechny výchozí účetní funkce belgického
lokalizace podle pravidel IFRS (mezinárodních účetních standardů).

.. viz též:
:doc:`Dokumentace o právnosti a dodržování předpisů v Belgii


.._belgie/znak:

Klasifikační schéma
=================

Doklad o účetnictví lze získat kliknutím na položku „Účetnictví“ v nabídce „Nástroje“.
Konfigurace --> Účetnictví: Skladová kniha.

Belgický účetní systém zahrnuje přednastavené účty, jak je popsáno v :abbr:`PCMN (Plán
Kontabilní minimální normovaný). Klikněte na „Nový“ a nová řádka se objeví. Vyplňte
je do něj, klikněte na „Uložit“ a poté na „Nastavení“, abyste jej mohli dále konfigurovat.

.. viz též:
:doc:`../účetnictví/začínáme/rozvaha“

.. belgie/daně:

Daně
=====

Výchozí belgické daně jsou vytvářeny automaticky při založení účtu pro Belgii a
Moduly „Belgie – Účetní výkazy“ jsou nainstalovány. Každá daň má vliv na belgickou
„Daňový výkaz“, k dispozici po zvolení „Účetnictví -> Zprávy ->
Výroky a zprávy: Daňový report.

V Belgii je základní sazba DPH 21 %, ale existují nižší sazby pro některé druhy zboží.
a služeb. Na sociální bydlení a jídlo podávané v restauracích se uplatňuje sazba DPH ve výši **12 %**
restaurace, zatímco snížená sazba 6 % se vztahuje na základní zboží, jako je jídlo, pitná voda a
knihy a léky. Sazba 0 % se vztahuje na některé výjimečné zboží a služby, jako jsou například
denní a týdeníky i použité zboží.

..._Belgie/neodpočitatelné:

Neodpočitatelné daně
--------------------

V Belgii jsou některé daně neodpočitatelné, například daň z údržby automobilů.
Za určitou část těchto daní se považuje výdaj.

V Odoo můžete nastavit neodpočitatelné daně vytvořením daňových pravidel pro tyto daně a propojením
jejich účty a systém automaticky spočítá daně a
Přiděluje jim příslušné účty.

Pro konfiguraci nového neodpočitatelného daně se přejděte do: „Účetnictví“ -> Konfigurace ->
Účetnictví: daně“, a klikněte na „New“:

#:guilabel:`Přidat řádek“ a vyberte „Základ“ v sloupci „Založeno na“.
#Přidejte řádek, pak vyberte „Na dani“ v sloupci „Založeno na“
do sloupce „%“ zadejte **neodpočitatelnou částku**.
#Vyberte na řádku „Daň“ pole „Sazba daně“ a vyberte sazbu daně spojenou s vaší daní.
#:guilabel:`Přidat řádek“ s procentem „odpočtu“ v sloupci :guilabel:`%“;
#Zaškrtněte políčko „Daň“ v seznamu „Založeno na“.
#Vyberte účet s názvem „411000 DPH obnovitelný“ a vyberte příslušný daňový řádek.

Jakmile vytvoříte neodpočitatelnou daň, můžete ji použít na své transakce zvolením
Vhodná daň při kódování faktur a zálohových listů. Systém automaticky vypočítá
Určí daňovou částku a přidělí ji na příslušné účty podle daných pravidel.

.. příklad::
S belgickou lokalizací vzniká **automobilový daňový tarif 21 %** (50 % neodpočitatelné části).

.... obrázek: belgium/sleva_z_dane.png
:alt: Příklad neúplně odečitatelné daně

.. viz též:
  - :doc:`Daň z příjmu <../accounting/taxes>`
  - :doc:`../účetnictví/výkaznictví/daňové přiznání

.. belgie/zpravy:

Zprávy
=======

Seznam zpráv o konkrétních problémech v Belgii:

- Výsledovka
- Zisk a ztráta.
- Daňový přiznání
- Partner VAT Listing
- Prodejní seznam E. C.;
- Intrastat.

Přejděte na ikonu knihy, pokud chcete zobrazit verzi hlášení specifickou pro Belgii.
report a vybírá jeho belgickou verzi: **(BE)**.

.. obrázek: belgium/belgian-reports.png
:alt:Belgická verze zpráv

.. viz též:
:doc:`../účetnictví/reporting`

..._belgie/neuznané výdaje:

Zpráva o neuznaných výdajích
--------------------------

Nepovolené výdaje jsou výdaje, které můžete odečíst z účetního výsledku, ale ne ze
Váš daňový výsledek.

Hlášení o neuznaných výdajích je k dispozici po přechodu na:
Management: Zákaz nákladů. Umožňuje finanční výsledky v reálném čase a periodicky
změn. Tento výkaz vychází z kategorií nákladů, které jsou zakázané.
Přejděte na:menu:Účetnictví -> Konfigurace -> Správa: Zákaz výdajů
Kategorie“. Některé kategorie jsou již vytvořeny, ale nemají žádnou sazbu. Klikněte na
:guilabel:„Nastavit sazby“ pro aktualizaci konkrétní kategorie.

.. tip::
  - Můžete přidat více sazeb pro různé datumy. V takovém případě se používá
výdaje se odvíjí od data, ke kterému jsou vypočítávány, a sazby stanovené pro tento den.
  - Pokud máte aplikaci Fleet nainstalovanou, zaškrtněte při potřebě pole „Kategorie vozidla“.
To dělá vozidlo povinným při objednávání faktury dodavatele.

K propojení s konkrétním účtem přejděte na: „Účetnictví“ ->
Nastavení --> Účetnictví: Výkaz zisku a ztráty. Najděte účet, který chcete, a klikněte na
„Nastavení“. Přidejte kategorii „Zákaz nákupu“ do „Nastavení“.
Pole výdajů. Od teď, když se vytvoří výdaj s touto položkou, bude zakázaný výdaj
vypočítané na základě sazby uvedené v kategorii „Náklady, které nelze odepsat“.

Pojďme si ukázat příklad, který odráží náklady na jídlo a dopravu.

..._belgie/náklady-na-jídlo-v-restauracích:

Náklady na restauraci
~~~~~~~~~~~~~~~~~~~

V Belgii je 31 % nákladů na restaurace nezdanitelné. Vytvořte novou položku „Nedovolené výdaje“
kategorii a nastavte obě pole „Související účet“ a „Aktuální sazba“.

.. obrázek: belgium/restaurant-expenses.png
:alt:Zákazové kategorie výdajů

.._belgie/vozidlo-dvoukolove:

Náklady na dopravu: rozdělení vozidla
~~~~~~~~~~~~~~~~~~~~~~~~~~~

V Belgii se procento odpočtu liší podle každého vozu a proto by mělo být uvedeno
každé vozidlo. Chcete-li tak učinit, otevřete nabídku „Společnost“ a vyberte vozidlo. V poli „Daň
V záložce „Informace“ přejděte do sekce „Sazba nákladů na zakázané výdaje“ a klikněte na „Přidat“.
line. Přidejte :guilabel:Datum zahájení a :guilabel:%. Výše poplatků je stejná pro všechny
náklady na automobil.

Když vytváříte fakturu za auto, můžete přiřadit každou položku k určitému vozu tak, že vyplníte
sloupec „Vozidlo“, takže se na vozidle aplikuje správný podíl.

.. obrázek: belgium/car-bill.png
:alt:Zákazové kategorie výdajů

Možnost „Vyčlenění vozidla“ dostupná v zprávě o zakázaných výdajích umožňuje vidět
sazba a neuznaná částka za každé auto.

.. obrázek:belgium/vehicle-split.png
:alt:Zákazové kategorie výdajů

..._belgie/formy:

Formulář č. 281.50 a formulář č. 325
============================

.._Belgie/281.50:

Správní poplatek 281,50 Kč
---------------

Ročně je nutné ohlásit fiskálnímu úřadu sazbu ve výši 281,50 Kč na formuláři pro hlášení poplatku.
Kontaktní formulář dotčených subjektů musí obsahovat částku 281,50 Kč.
Přidejte štítek, otevřete: menu-selection: Contacts, vyberte osobu nebo společnost, kterou chcete vytvořit
Vyplňte formulář „Poplatek 281,50 Kč“ a přidejte štítek „281,50“ do pole :guilabel:„Štítky“.

.. obrázek: belgium/281-50.png
:alt: přidat značku 281.50 do kontaktního formuláře

.. poznámka::
Ujistěte se, že jsou také uvedeny informace o **ulici, PSČ, zemi a DIČ**.
**Kontaktní formulář**.

Pak podle charakteru výdaje přidejte příslušný štítek „281.50“ k dopadu
účetnictví. Chcete-li tak učinit, přejděte na: menu „Účetnictví“ -> „Konfigurace“ -> „Účetnictví:
Účty“ a klikněte na „Nastavení“, abyste v případě dopadu na účet přidali značku „281.50“.
účty, tj. např.: „281.50 - Provize“ podle charakteru výdaje.

..._belgie/325:

Formulář 325
--------

Můžete vytvořit formulář 325 kliknutím na:
Vytvořit formulář 325. Nová stránka se otevře, vyberte správné možnosti a klikněte na tlačítko „Vytvořit 325
formu. Chcete-li otevřít již vygenerovaný formulář 325, přejděte na:
Belgie: Otevřené formuláře 325.

.. obrázek: belgium/325-form.png
:alt:Přidejte do kontaktního formuláře tag 281-50

..._belgie/coda-soda:

Prohlášení CODA a SODA
========================

.._belgie/coda:

CODA
----

Formát **CODA** je elektronický formát XML, který se používá k importu belgických výpisů z banky. Formát CODA
soubory z vaší banky a přímý import do Odoo kliknutím na tlačítko „Importovat soubor“.
Váš záznam o bankovním účtu v sekci „Dashboard“.

.. obrázek: belgium/coda-import.png
:alt:Import souborů CODA

.. viz též:
:ref:`Import bankovních souborů <transakce/import>

.._belgie/soda:

SODA
----

Formát **SODA** je elektronickým formátem XML, který se používá k importu účetních záznamů souvisejících s platy.
soubory lze do účetního programu, ve kterém evidujete mzdy, importovat kliknutím na svůj účet.
příkazovém řádku a kliknutím na tlačítko „Nahrát“ v příslušném formuláři pro karty časopisu.

Jakmile jsou importovány soubory **SODA**, vzniknou automaticky záznamy ve vašem mzdovém deníku.

.. obrázek: belgium/soda-import.png
:alt:Import souborů Soda

..._belgie/fakturace:

CodaBox
-------

Služba **CodaBox** umožňuje belgickým společnostem a účetním firmám přistupovat k bankovnímu
informace a prohlášení. Odoo poskytuje způsob, jak automaticky do systému importovat takové prohlášení.

Konfigurace
~~~~~~~~~~~~~

Než začnete konfigurovat a používat Codabox, nejprve nainstalujte modul :guilabel:`CodaBox`.

.._belgie/konfigurace-krabice-codabox:

Nastavte připojení
************************

.. záložky::

.. tab:: Pro společnosti

... důležité::
Zkontrolujte, zda jsou správně nastaveny :doc:`firemní nastavení <applications/general/companies>`.
konfigurována, tj. země je nastavena na „Belgie“ a daňové identifikační číslo nebo
:guilabel:`Firma“ pole je vyplněno.

      #Přejděte na „Účetnictví“ -> „Konfigurace“ -> „Nastavení“, pak přejděte do
:guilabel:`CodaBox & SODA“
      #Klikněte na tlačítko „Spravovat připojení“ a otevře se průvodce připojením, který zobrazuje
:guilabel:`Číslo DPH/IČ společnosti, které bude použito k propojení.“
      #Pokud je to vaše první připojení, klikněte na tlačítko „Vytvořit připojení“.
Kouzelník potvrdil, že připojení bylo vytvořeno na straně Odoo. Následně
kroků na ověření spojení i na straně CodaBoxu.

Pokud se jedná o vaši první instalaci, pak je třeba zadat heslo.
Odoo bude po prvním připojení požádáno o vytvoření nového spojení.

.. poznámka::
Tento :guilabel:`Heslo` je jedinečný pro Odoo a musí být bezpečně uchováván
Na vaší straně.

...... tab:: Pro účetní
.. poznámka::
Účetní společnosti musí své klienty spravovat na samostatných databázích a je nutné je konfigurovat.
Každý účet musí být veden samostatně, aby se předešlo zaměňování dat. Připojení musí být provedeno prostřednictvím účtu
firma s platnými přihlašovacími údaji do CodaBoxu Connect.
V následujících pokynech budeme vašeho klienta označovat jako „Společnost“ a
vaše účetní firmu jako *Účetní firma*.

... důležité::
Zkontrolujte, zda jsou správně nastaveny :doc:`firemní nastavení <applications/general/companies>`.
konfigurována, tedy je nastaveno :guilabel:`Belgie“, :guilabel:`Daňové identifikační číslo“ nebo
:guilabel:`Společnost“ a :guilabel:`Účetní firma“ políčka jsou vyplněna.
:guilabel:`Daňové identifikační číslo“ účetní firmy.

      #Přejděte na „Účetnictví“ -> „Konfigurace“ -> „Nastavení“, pak přejděte do
:guilabel:`CodaBox & SODA“
      #Klikněte na tlačítko „Spravovat připojení“ a otevře se průvodce připojením, který zobrazuje
:guilabel:`Daňové identifikační číslo účetní kanceláře“ a „Daňové identifikační číslo společnosti“.
sloužit k propojení.
      #Pokud je to vaše první spojení, klikněte na tlačítko „Vytvořit spojení“. Otevře se průvodce.
Potvrzuje, že připojení bylo vytvořeno na straně Odoo. Postupujte podle kroků pro
ověřit spojení i na straně CodaBoxu.

Pokud se jedná o **ne první spojení**, pak zadaný heslo pro účetní firmu
Odoo během prvního připojení požádá o vytvoření nového spojení.

.. poznámka::
Toto heslo pro účetní firmu je jedinečné pro Odoo a musí být uchováno
bezpečně na vaší straně.

Nyní by měl být stav přepnutý na „Připojen“.

Nastavte záznamy
**********************

.. záložky::

...... tab:: Pro soubory CODA

      #Vytvořit nový bankovní deník (viz účetnictví/banka).
      #V poli „Číslo účtu“ zadejte správný IBAN.
      #Vyberte „Synchronizace CodaBox“ jako „Bankovní zprávu“.

.. obrázek: belgium/codabox_configuration_coda_journal.png
:synchronizace: střed
:alt: Konfigurace časopisu CODA.

.. tip::
Při práci s bankovními transakcemi používajícími různé měny je doporučeno
Vytvořit více účetních knih s jedním bankovním účtem, ale různými měnami.

...... tab:: Pro soubory SODA

      #Vytvořte nový odborný časopis.
      #Přejděte na „Účetnictví“ -> „Konfigurace“ -> „Nastavení“, pak přejděte do
:guilabel:`CodaBox“ sekci.
      #Vyberte si nový časopis v poli časopisu SODA.

.. obrázek: belgium/codabox_configuration_soda_setting.png
:synchronizace: střed
:alt: Konfigurace časopisu Soda.

Synchronizace
~~~~~~~~~~~~~~~

Jakmile je připojení zprovozněno, může být Odoo synchronizován s CodaBoxem.

.. záložky::

...... tab:: Pro soubory CODA

Soubory CODA jsou automaticky importovány z CodaBox každých 12 hodin.
Nemusíte nic dělat. Pokud však chcete, můžete to udělat ručně také.
kliknutím na tlačítko „Stáhnout z CodaBoxu“ v přehledu účetnictví.

...... tab:: Pro soubory SODA

Soubory ve formátu SODA jsou automaticky importovány z CodaBox jednou denně jako návrh. Nemusíte
nic nedělat. Pokud ale chcete, můžete si ho také nastavit ručně kliknutím na
v sekci Účetnictví na záložce Fetch z CodaBoxu.

Výchozí nastavení je takové, že pokud účet v souboru SODA není přiřazen k účtu v Odoo, dojde k
Pro účet (499000) se používá poznámka k vytvořenému dokladu.

.. poznámka::
Můžete se dostat k mapování mezi účty SODA a Odoo přes
:menu „Účetnictví“ -> „Nastavení“ a kliknutím na
:guilabel:`Otevřít mapování“ tlačítko v sekci „CodaBox“.


Potenciální problémy
~~~~~~~~~~~~~~~~

* **Nastavení CodaBoxu není správné. Zkontrolujte prosím své nastavení.**

Evidentně není nastavená ani jedna z těchto položek: „Daň z přidané hodnoty“ nebo „Daňová firma“.

*  S těmito účetními firmami a společnostmi s DPH neexistuje žádný vztah.
**Zkontrolujte si prosím konfiguraci.**

Toho se může stát při kontrole stavu připojení a v případě účetní firmy DPH
:guilabel:`Kombinace DPH společnosti“ ještě není zaregistrována. To se může stát, pokud jste
změnil název společnosti na „DPH“. Pro bezpečnostní důvody byl
musíte:ref:`vytvořit nové připojení <belgium/codabox-configuration-connection>“.
pro tento :guilabel:`Daň z přidané hodnoty společnosti“.

*  Vypadá to, že vaše připojení k CodaBoxu není platné. Prosím, připojte se znovu.

Tohle se může stát, pokud jste odebrali přístup aplikace Odoo k vašemu účtu CodaBox nebo ještě nemáte dokončené
proces konfigurace. V tomto případě musíte odpojit připojení a vytvořit nové.

*  **Zadané heslo není platné pro tuto účetní firmu.**
**Musíte použít heslo, které jste dostali od Odoa při své první konexi.**

Heslo, které jste zadali, je odlišné od hesla, které vám poskytla společnost Odoo při vaší první registraci.
připojení. Musíte použít heslo, které jste obdrželi od Odoa při prvním spojení.
vytvořit nové připojení pro tuto účetní firmu. Pokud jste zapomněli heslo, musíte nejprve
zrušit připojení Odoo na straně CodaBoxu (tedy v mém portálu myCodaBox). Pak už jen
zrušit spojení na straně Odoo.
:ref:`vytvořit novou <belgium/codabox-configuration-connection>.

*  **Vypadá to, že číslo DPH společnosti nebo účetní firmy, které jste uvedli, není platné.**
**Zkontrolujte si prosím konfiguraci.**

Buď varianta „Daň z přidané hodnoty pro společnost“ nebo „Daň z přidané hodnoty pro účetní firmu“ není platná.
Belgický formát.

*  Zdá se, že daňové identifikační číslo účetní firmy, které jste poskytli, neexistuje v CodaBoxu.
**Zkontrolujte si prosím konfiguraci.**

Číslo účetní firmy DPH, které jste uvedli, není registrováno v CodaBoxu.
Možná nemáte platnou licenci CodaBox propojenou s tímto DIČ.

*  **Vypadá to, že jste již vytvořili připojení k CodaBox prostřednictvím této účetní firmy.**
**Pro vytvoření nového připojení je nutné nejprve zrušit stávající na portálu myCodaBox.**

Musíte se dostat na svůj portál myCodaBox a odebrat přístup k vašemu účtu CodaBox společnosti Odoo.
Pak můžete vytvořit nové připojení:
na straně Odoo.

.. tip::
Zrušit propojení mezi Odoo a CodaBoxem, přejděte do
:menu_selecetion:`Účetnictví --> Konfigurace --> Nastavení“, posuňte se dolů do části
:guilabel:`CodaBox“ části, klikněte na „Spravovat připojení“, pak klikněte
:guilabel:`Odebrat“.

Elektronická fakturace
====================

Odoo podporuje elektronický formát fakturace Peppol BIS Billing 3.0 (UBL). Pro jeho zapnutí je potřeba
zákazníkovi, přejděte na:menu:„Účetnictví“ -> „Zákazníci“ -> „Kontakt“, otevřete jejich kontaktní formulář.
a pod záložkou „Účetnictví“ vyberte formát „Faktura v systému Peppol BIS 3.0“.

.. viz též:
:doc:`../účetnictví/fakturace zákazníků/elektronická fakturace“

.._belgie/slevy-za-hotovost:

Sleva v hotovosti
=============

V Belgii se při slevě za rychlou platbu na faktuře počítá daň z
sleva z celkové ceny, ať už zákazník slevu využije nebo ne.

Pro správné nastavení daně a její uvedení v daňovém přiznání zvolte slevu na dani
:guilabel:`Vždy (na faktuře).“

.. viz též:
:doc:`../účetnictví/fakturace/hotovostní slevy“

..._belgie/pos-restaurace-certifikace:

Daňová certifikace: restaurace POS
====================================

V Belgii je podle zákona majitel kuchyňského podniku jako restaurace nebo jídelního vozu povinen
musí používat certifikovaný pokladní systém, tedy pokud jejich roční obrat
příjmy (bez DPH, nápojů a jídla s sebou) přesahují 25 000 eur.

Toto schválené řešení vyžaduje použití certifikovaného systému POS.
<belgium/certified-pos>, spolu s zařízením nazývaným :ref:`Modul pro fiskální data <belgium/fdm>“ (nebo
černá krabička“) a :ref:`kartu pro podepisování DPH <belgium/vat>“.

.. důležité::
Nezapomeňte se zaregistrovat jako „manažer potravinářského průmyslu“ na webu Federal Public Service
Formulář pro registraci finančních prostředků <https://www.systemedecaisseenregistreuse.be/fr/enregistrement>.

.. belgie/certifikovaný_pos:

Certifikovaný systém prodeje na místě
--------------------

Systém prodejního místa Odoo je certifikován pro databáze uložené na **Odoo Online**, **Odoo.sh** a
**Na místě**.

.. viz též:
:doc:`/administrace/podporovane-verze`

„Certifikovaný systém prodeje na místě“ (https://www.systemedecaisseenregistreuse.be/systemes-certifies)
plnit přísná vládní nařízení, což znamená, že funguje jinak než certifikované
POS.

- Na certifikovaném POS nelze:

  - Nastavte a použijte funkci **globálních slev** (modul pos_discount je na černé listině).
Není aktivována.
  - Nastavte a používejte funkci věrnostního programu (modul pos_loyalty je na černé listině).
Není aktivována.
  - Reprinty dokladů (modul „pos_reprint“ je na černé listině a nelze jej aktivovat).
  - Upravte ceny v položkách objednávky.
  - Upravit nebo smazat řádky objednávky v POS.
  - Prodat zboží bez platného DPH.
  - Použijte POS, který není připojen k IoT boxu.

- Funkce „kontrola hotovosti“ musí být
aktivován a nastaven na „Přesnost zaokrouhlování“ 0,05 a „Metodu zaokrouhlování“
nastavit jako :guilabel:`Poloze nahoru“.
- Dotace musí být nastaveny jako součást ceny. Chcete-li je nastavit, přejděte na:
Konfigurace --> Nastavení“, a z části „Účetnictví“ otevřete
:guilabel:`Výchozí daň z přidané hodnoty“ kliknutím na šipku vedle pole „Výchozí daň z přidané hodnoty“.
Vyberte si v nabídce „Pokročilé možnosti“ a zapněte „Zahrnuto v ceně“.
- Na začátku sezení POS uživatelé musí kliknout na „Pracovat“ pro zaznamenání pracovní doby.
registraci objednávek na pokladně. Pokud uživatel není přihlášený, nemůže vytvářet objednávky na pokladně.
Stejně tak musí kliknout na „Trénink“ a poté na „Odchod“.

.. varování:
Pokud nastavíte POS tak, aby pracovalo s :abbr:`FDM (Fiscal Data Module)` nelze ho použít znovu.
bez něj.

..._belgie/fdm:

Modul daňových dat (FDM)
------------------------

FDM nebo „černá skříňka“ je certifikované zařízení vlády, které spolupracuje s místem
Aplikace prodeje a ukládá informace o objednávkách na místě prodeje. Konkrétně hash (:dfn:`unikátní kód`):
je vygenerován pro každou objednávku na POS a přidán do jejího dokladu o prodeji. To umožňuje vládě ověřit, že
Všechny příjmy jsou vykázány.

.. varování:
Jediný FDM od **Boîtenoire.be** s číslem certifikátu FDM BMC04
<https://www.systemedecaisseenregistreuse.be/fr/systemes-certifies#FDM%20certifiés>`_ je
podporované společností Odoo. „Kontaktujte výrobce (GCV BMC) <https://www.boitenoire.be/contact>“
objednat si jeden.

Konfigurace
~~~~~~~~~~~~~

Před zprovozněním databáze pro práci s FDM zajistěte následující hardwarové vybavení:

- **Boitenoire.be** (číslo certifikátu BMC04) FDM;
- sériový kabel typu RS-232 s nulovou komunikací podle FDM.
- adaptér sériového portu RS-232 na USB podle FDM;
- :ref:`IoT Box <belgium/iotbox>“ (jedna IoT box na FDM).
- tiskárna účtenek.

.._belgie/černá skříňka:

Černá skříňka
****************

Jako předpoklad je zapotřebí aktivovat modul „Belgický registrovaný pokladní systém“ pomocí příkazu :ref:`activate <general/install>`.
Technické označení „pos_blackbox_be“.

.. obrázek: belgium/be-modules.png
:alt: černé skříňky pro belgickou daňovou certifikaci

Jakmile modul aktivujete, přidejte své DIČ do firemních informací. Chcete-li nastavit, přejděte na
Nastavení -> Firmy -> Aktualizace informací, ve kterém vyplníte pole DPH.
Poté zadejte národní registrační číslo pro každého zaměstnance, který obsluhuje POS systém.
takže se přihlaste do aplikace „Zaměstnanci“ a otevřete formulář zaměstnance. Tam pak vyberte „Personal
karta Nastavení --> Přítomnost / Prodejní místo, vyplňte pole „Číslo INSZ nebo BIS“.

.. obrázek:belgie/cislo-bise.png
:alt: pole čísla ISNZ nebo BIS na formuláři zaměstnance

.. tip::
Chcete-li vložit své informace, klikněte na svůj avatar, přejděte na „Můj profil“ a poté na „Nastavení“.
„Tab“, a do pole pro zadání čísla vložte své číslo INSZ nebo BIS.

.. varování:
Musíte nastavit modul pro fiskální data přímo v produkčním databázovém serveru.
Použití tohoto nástroje v testovacím prostředí může vést k tomu, že se do FDM uloží nekorektní data.

.._belgie/iotbox:

IoT Box
*******

Chcete-li používat modul pro fiskální data (:abbr:`FDM (Fiscal Data Module)`), potřebujete registrovanou krabičku IoT.
IoT box je nutné kontaktovat prostřednictvím našeho „formuláře pro podporu“ <https://www.odoo.com/help>“.
Prosím o sdělení následujících informací:

- Vaše DIČ.
- název vaší společnosti, adresu a právní strukturu.
- MAC adresa vaší IoT krabičky.

Jakmile bude vaše IoT krabička certifikována, připojte ji k databázi pomocí příkazu connect.
ověřit, že IoT box rozpoznává FDM, přejít na stránku IoT a projít dolů
sekci „IoT zařízení“, která by měla zobrazit FDM.

.. obrázek: belgium/iot-devices.png
:alt:Stránka stavu hardwaru na registrovaném IoT Boxu

Pak přidejte IoT do svého POS. Chcete-li tak učinit, přejděte na:
Pokladna“, vyberte svou pokladnu, posuňte se dolů do části „Připojené zařízení“ a zapněte
:guilabel:IoT Box“. Nakonec přidejte FMD do pole „Modul fiskálních dat“

.. poznámka::
Pro použití FDM musíte připojit alespoň jeden tiskárnu účtenek.

.. belgie/vat:

Podepsaná karta pro DPH
----------------

Když otevřete sezení POS a provedete svou první transakci, budete vyzváni k zadání PIN
vystavené na vaší :abbr:`VSC (Potvrzení o registraci k DPH)“. Karta je vydávána :abbr:`FPS (Finanční správou)“.
Veřejné federální finance) po registraci na stránce https://www.systemedecaisseenregistreuse.be/fr/enregistrement
