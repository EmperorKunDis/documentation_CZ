====
Peru
====

… |SUNAT| nahradit za: zkratka: SUNAT (Národní správce cel a administrativy)
Tributaria)
.. |GRE| nahradit za: zkratka: „Elektronická referenční příručka“
.. |RUS| nahradit za: zkratka: RUS (jednoduchý jednotný režim)
.. |EDI| nahradit za: zkratka: `EDI (Elektronický výměnný obchod)`
.. |PLE| nahradit za: abbr: `PLE (Programa de Libros Electrónico)`

Moduly
=======

:ref:`Instalujte následující moduly, abyste mohli využívat všechny aktuální funkce
Peruánská lokalizace.

.. seznam tabulkový::
:hlavičkové řádky: 1

   * Jméno
     - Technické označení
     - Popis
   * --label:Účetnictví v Peru
     - l10n_pe
     - Přidává účetní funkce pro peruánskou lokalizaci, které představují minimální
konfigurace, kterou společnost potřebuje pro svůj provoz v Peru a podle předpisů SUNAT.
směrnice. Hlavními prvky zahrnutými v tomto modulu jsou účetní kniha, daně a
typy dokumentů.
   * --label:Peru - Elektronické fakturace
     - l10n_pe_edi
     - Zahrnuje všechny technické a funkční požadavky na generování a přijímání elektronických
faktury online na základě předpisů SUNAT.
   * -- :guilabel:`Účetní zprávy Peru“
     - l10n_pe_reporty
     - Zahrnuje následující finanční zprávy:

       - První sada hlavních finančních výkazů:

         - Registr tržeb a příjmů (RTPI) - 14.4
         - Registr elektronických nákupů (RCE) - 8,4
         - Elektronický nákupní rejstřík - informace o transakcích s neadresnými osobami
(RCE) - 8,5

       - Druhé finanční výkazy:

         - PLE 5.1 Obecný deník
         - PLE 5.3 Schéma účtů
         - PLE 6.1 Účetnictví

       - Třetí finanční výkaz:

         - PLE 1.1 Kniha o pokladně
         - PLE 1.2 Kniha bank

   * --:guilabel:`Dodací listina elektronického přepravce“
     - l10n_pe_edi_stock
     - Přidává dodací průvodku (Guía de Remisión), která je potřebná jako důkaz, že zásilku odesíláte.
zboží mezi A a B. Dodací průvodka se ověřuje až poté, co je platná dodací objednávka.
Může být vytvořen.
   * – Peru – Zprávy o akciích
     - l10n_pe_reporty_sklad
     - Umožňuje vytvářet zprávy o stavu zásob podle :ref:`PLE <peru/reports-ple>`, tedy pro trvalý skladový záznam
jednotky a trvalé záznamy o hodnotě majetku.
   * --:guilabel:Peruánské e-commerce
     - l10n_pe_web_prodej
     - Umožňuje identifikaci typu v elektronických obchodních formulářích a generování
elektronické faktury.
   * --:guilabel:Peruánský bod prodeje s PE Docem
     - „l10n_pe_pos“
     - Umožňuje kontaktní daňové informace upravitelné od POS Session pro generování elektronických
faktury a vrácení peněz.

.. poznámka::
   - Odoo automaticky nainstaluje potřebný balíček podle země, ve které se firma nachází
vybrané při vytváření databáze.
   - Modul *Průvodce elektronickou dodávkou* závisí na aplikaci *Sklad*.
nainstalovány.

.. viz též:
   - „Tour App - Lokace Peru“
   - „Chytrý návod – Lokace v Peru (videa pro práci a konfigurace)“
<https://www.odoo.com/slides/smart-tutorial-localizace-peru-133>
   - :doc:`Dokumentace o zákonnosti a souladu s předpisy při elektronické fakturaci v Peru
<../účetnictví/fakturace zákazníkům/elektronická fakturace/Peru>

Konfigurace
=============

Nainstalujte peruánské moduly pro místní prostředí
-----------------------------------------

Přejděte do sekce Apps a vyhledejte Peru, pak klikněte na tlačítko Instalovat v modulu Peru EDI. Tento modul má
závislost na modulu Peru – Účetnictví. Pokud tento modul není nainstalován, Odoo jej nainstaluje
automaticky v rámci EDI.

.. obrázek: peru/peru-modules.png
:alt: Filtr „Modul“ je nastaven na „Peru“

.. poznámka::
Pokud při instalaci databáze zvolíte Peru jako zemi, Odoo automaticky
instaluje základní modul: Peru – Účetnictví.

Nastavte svou společnost
~~~~~~~~~~~~~~~~~~~~~~

Kromě základních informací o společnosti je nutné nastavit Peru jako zemi, což
je nezbytná pro správnou funkci Daňového dokladu v elektronické podobě.
kód zřízení přidělený SUNATEM při registraci RUC (jedinečný příspěvovatel)
Registrace):

.. obrázek: peru/peru-spolecnost.png
:alt:Údaje o společnosti pro Peru včetně kódu RUC a kódu typu adresy.

.. tip::
Pokud je kód typu adresy neznámý, můžete jej nastavit jako výchozí hodnotu: 0000.
že pokud bude zadána nesprávná hodnota, může dojít k chybám při kontrole elektronické faktury.

.. poznámka::
Název NIF by měl být ve formátu RUC.

Přehled účtů
~~~~~~~~~~~~~~~~

Kniha jízd je nainstalována v základním balíčku dat, který je součástí
lokalizační modul, účty se automaticky mapují do:

- Daně
- Neplacená faktura.
- Neplacené faktury

Účetní osnova pro Peru je založena na nejaktuálnější verzi :abbr:`PCGE (Plán
Účetní generální obchodní společnosti“, která je rozdělena do několika kategorií a je kompatibilní s NIIF
účetnictví.

.._přepnout nastavení účetní knihy:

Nastavení účetnictví
-------------------

Jakmile jsou moduly nainstalovány a základní informace o vaší společnosti nastaveny, musíte
Nastavte požadované prvky pro elektronickou fakturaci. Pro tento účel přejděte na: menu:Účetnictví
--> Nastavení --> Lokální nastavení pro Peru“.

Základní pojmy
~~~~~~~~~~~~~~

Tady jsou některé termíny, které jsou nezbytné pro peruánskou lokalizaci:

- **Elektronický datový výměnný systém (EDI)**: Elektronický datový výměnný systém, v tomto případě elektronická faktura.
- **SUNAT** je organizace, která vykonává celní a daňovou kontrolu v Peru.
- **OSV**: elektronický poskytovatel služeb, definice „OSV Sunat“
<https://cpe.sunat.gob.pe/aliados/ose#:~:text=Elektrárenský%20operátor%20(OSE)%20je%20organizace,která%20se%20stará%20o%20elektřinu>.
- **CDR**: Potvrzení o přijetí (Certificado de Recepción).
- **Kredence SOL**: Sunat Operaciones en Línea. Uživatelské jméno a heslo jsou poskytovány SUNATem
poskytnout přístup do systému Online Operations.

Poskytovatel podpisu
~~~~~~~~~~~~~~~~~~

Společnost musí vybrat jeden z následujících způsobů vystavení faktury:
Poskytovatel podpisu, který se postará o proces podepisování dokumentů a spravuje SUNAT.
ověřovací odpověď. Odoo nabízí tři možnosti:

#IAP (Odoo In-App Purchase).
#.Digiflow
#Sunat

Prosím, podívejte se na následující části pro podrobnosti a zvážení každé možnosti.

IAP (In-App Purchase od Odoo)
**************************

Toto je výchozí a doporučená volba, protože digitální certifikát je součástí
služby.

.. obrázek: peru/peru-IAP.png
:alt: možnost IAP jako poskytovatele podpisů.

Co je IAP?
^^^^^^^^^^^^^^^^

Toto je podpisový servis nabízený přímo společností Odoo. Servis se postará o další procesy:

#Provádí elektronické fakturační certifikáty, takže nemusíte získávat certifikát sami.
#Dokument pošlete na OSSZ, v tomto případě na DigiFLOW.
#Získat ověření OSE a CDR.

Jak to funguje?
^^^^^^^^^^^^^^^^^

Tato služba vyžaduje kredity, abyste mohli zpracovávat své elektronické dokumenty. Odoo poskytuje 1000
kredity zdarma v nových databázích. Po spotřebování těchto kreditů je nutné zakoupit Kredit
Balíček.

+---------+-----+
|Zdroj|EUR|
+=========+=====+
| 1000    | 22  |
+---------+-----+
| 5000    | 110 |
+---------+-----+
| 10,000  | 220 |
+---------+-----+
| 20,000  | 440 |
+---------+-----+

Kredity se spotřebovávají za každý dokument, který je odeslán do OSE.

.. důležité::
Pokud máte chybu ověření a dokument musí být odeslán znovu, můžete použít jednu další
V takovém případě bude účtován poplatek za kredit. Proto je důležité zkontrolovat všechny informace, aby byly správné
před odesláním dokumentu do OSE.

Co musíte udělat?
^^^^^^^^^^^^^^^^^^^^^^^

- V Odoo se aktivuje smlouva o podnikání a začínáte pracovat v Produkci.
musíte si koupit kredity, jakmile spotřebujete první tisíc.
- Digiflow je používán jako OSE v IAP, takže musí být přiřazen jako oficiální OSE pro váš
Společnost na webu SUNAT. Je to jednoduchý proces. Pro více informací navštivte
„Příručka pro připojení k OSE
<https://drive.google.com/file/d/1BkrMTZIiJyi5XI0lGMi3rbMzHddOL1pa/view?usp=sharing>.
- Prosím zaregistrujte společnost Digiflow jako oprávněného dodavatele PSE.
„Průvodce pro členství v PSE
<https://drive.google.com/file/d/1QZoqWvtQERpS0pqp6LcKmw7EBlm9EroU/view?usp=sharing>.

Digiflow
********

Tato možnost může být použita jako alternativa k využívání služeb IAP.
ověření dokumentu přímo do Digiflow. V tomto případě je třeba zvážit:

- Kupte si vlastní digitální certifikát: Pro více informací o oficiálním seznamu dodavatelů a
Proces získání certifikátu, prosím, sledujte na stránce SUNAT Digital Certificates.
<https://cpe.sunat.gob.pe/informacion_general/certificados_digitales/>`.
- Zaregistrujte se přímo u Digiflow <https://www.digiflow.pe/>_.
- Přihlaste se pomocí svých SOL kreditů.

.. obrázek: peru/peru-Digiflow.png
:alt:Digiflow.

Sunat
*****

Pokud chce vaše společnost podepsat přímo s SUNATEM, je možné vybrat tuto variantu.
v konfiguraci. V tomto případě je třeba zvážit:
- Dokončit proces certifikace SUNAT.

- Kupte si vlastní digitální certifikát: Pro více informací o oficiálním seznamu dodavatelů a
Proces získání certifikátu, prosím, sledujte na stránce SUNAT Digital Certificates.
<https://cpe.sunat.gob.pe/informacion_general/certificados_digitales/>`.

- Předložte své SOL kreditní údaje.

.. důležité::
Při použití přímé spojení s SUNAT musí být uživatel SOL nastaven na společnost RUT + Uživatel
Id. Příklad: „20121888549JOHNSMITH“

Testovací prostředí
~~~~~~~~~~~~~~~~~~~

Odoo poskytuje testovací prostředí, které lze aktivovat před zahájením provozu vaší společnosti.

Při používání testovacího prostředí a podpisu IAP nemusíte kupovat testovací kredity
pro všechny transakce, protože jsou všechny automaticky ověřovány.

.. tip::
Výchozí nastavení databází je na produkci. Ujistěte se, že máte zapnutý testovací režim
pokud je třeba.

Certifikát
~~~~~~~~~~~

Pokud nepoužíváte službu Odoo IAP, abyste mohli vytvořit elektronickou podpisovou účtenku, je potřeba
Potřebujete certifikát s příponou „.pfx“. Přejděte do této části a nahrajte soubor.
heslo.

.. obrázek: peru/peru-certifikat.png
:alt: Průvodce certifikací EDI.

Multiměnová
~~~~~~~~~~~~~

Oficiální směnný kurz v Peru je poskytován agenturou SUNAT. Odoo se může připojit přímo k
služby a získat směnný kurz buď automaticky nebo ručně.

.. obrázek: peru/l10n-pe-banksync-sunat.png
:alt:SUNAT zobrazen v možnosti služby Multicurrency.

Pro více informací o tomto tématu se prosím podívejte na další část dokumentace.
:doc:`více měn <../accounting/get_started/multi_currency>“.

... _master_data:

Konfigurace hlavních dat
---------------------

Daně
~~~~~

Součástí lokálního modulu je automatické vytváření daní a jejich příslušných sazeb.
finanční účet a konfigurace elektronické faktury.

.. obrázek: peru/peru-taxes.png
:alt: Seznam základních daní.

Konfigurace EDI
*****************

Součástí konfigurace daně je tři nové pole, která jsou pro elektronickou fakturaci povinná.
V případě daní vytvořených výchozím nastavením jsou tyto údaje zahrnuty, ale pokud si vytvoříte nové daně,
Zaručeně vyplňte pole:

.. obrázek: peru/peru-dane-edi.png
:alt:Daňové údaje pro Peru.

Fiskální pozice
~~~~~~~~~~~~~~~~

V základním nastavení je dvě hlavní daňová pozice, které jsou zahrnuty při instalaci peruánské lokalizace.

**Cizinec – Export**: Zadejte tuto daňovou položku pro exportní transakce.

**Místní Peru**: Zvolte tuto daňovou pozici pro místní zákazníky.

Druhy dokumentů
~~~~~~~~~~~~~~

V některých zemích Latinské Ameriky, včetně Peru, jsou účetní transakce jako faktury a
Faktury dodavatelů jsou tříděny podle typu dokumentu, který definují daňové úřady vlády.
Tento případ řeší SUNAT.

Každý dokumentový typ může mít jedinečnou sekvenci pro každé časopisy, kde je přiřazen.
lokalizace, dokumentový typ obsahuje zemi, pro kterou je dokument platný; datum
je vytvořen automaticky při instalaci modulu lokálizace.

Informace potřebná pro typ dokumentu jsou zahrnuty výchozím nastavením, takže uživatel nepotřebuje
vyplnit cokoliv na této stránce:

.. obrázek: peru/peru-dokument-typ.png
:alt: Seznam typů dokumentu.

.. varování:
Aktuálně podporované dokumenty na zákaznických fakturách jsou: Faktura, Boleta, Dodací list a
Kreditní poznámka.

Časopisy
~~~~~~~~

Při vytváření prodejních deníků je nutné vyplnit následující informace navíc k běžným údajům.
políčka v sekci Články:

Použijte dokumenty
*************

Toto pole se používá k určení, zda časopis používá typy dokumentů. Použije se pouze pro
Kupní a prodejní deníky, které lze spojit s různými sadami
dokumenty dostupné v Peru. Výchozí nastavení je takové, že všechny faktury vytvořené používají dokumenty.

Elektronický datový výměnný systém
***************************

Tato část ukazuje, který způsob práce s daty v faktuře je použitý pro Peru. Pro nás je potřeba vybrat
„Peru UBL 2.1“.

.. obrázek: peru/peru-journal-edi.png
:alt: pole pro zadání časopisu EDI.

.. varování:
Výchozí hodnotou je vždy Faktura-X (FR), ujistěte se, že můžete ručně zrušit zaškrtnutí.

Partner
~~~~~~~

Identifikační typ a DPH
***************************

Jako součást peruánské lokalizace jsou nyní definovány identifikační typy podle SUNAT.
Tuto informaci lze získat na partnerovi, a je nezbytná pro většinu transakcí buď
Zkontrolujte si vlastní záznamy u odesílatele a u příjemce.

.. obrázek: peru/peru-id-type.png
:alt: Typ identifikace partnera.

Produkt
~~~~~~~

Kromě základních informací o produktech pro peruánskou lokalizaci poskytuje UNSPC
Kód produktu je povinný parametr, který se musí konfigurovat.

.. obrázek: peru/peru-unspc-code.png
:alt:Kód produktů podle UNSPSC.

Použití a testování
=================

Faktura pro zákazníka
----------------

EDI Elements
~~~~~~~~~~~~

Jakmile si nastavíte svá hlavní data, faktury můžete vytvářet z vašich objednávek.
ručně. Kromě základních informací o faktuře uvedených na stránce
fakturačním procesu (viz účetnictví / fakturace zákazníkům / přehled), je zde několik
povinné pole v rámci Peru EDI:

- **Druh dokumentu**: Výchozí hodnota je „Faktura elektronická“, ale můžete ji ručně změnit.
dokumentu, pokud je potřeba, a vyberte například Boleta.

.... obrázek: peru/peru-faktura-dokumenty.png
:alt:Pole typu faktury na fakturách.

- **Typ operace**: Toto pole je povinné pro Elektronickou fakturu a uvádí typ transakce
typ, výchozí hodnota je „Vnitřní prodej“, ale může být zvolena jiná hodnota ručně,
například Export zboží.

.... obrázek: peru/peru-operace-typ.png
:alt:Pole pro typ účetního dokladu na fakturách.

- Důvod EDI Affectation: V poli DPH v fakturačních řádcích je navíc pole „EDI
„Příčina“ určující rozsah daně na základě seznamu SUNAT, který je zobrazen.
Všechny daně nahrávané výchozím nastavením jsou spojeny s výchozí afekcí důvodu EDI, pokud je to potřeba.
Při vytváření faktury si můžete manuálně vybrat jiný.

.... obrázek: peru/peru-tax-affectation-reason.png
:alt: Důvod daně v položce faktury.

Kontrola faktury
~~~~~~~~~~~~~~~~~~

Jakmile zkontrolujete všechny informace na faktuře, můžete pokračovat v ověřování.
Akce zaznamená přesun účtu a spustí průběh elektronické fakturace, aby byla odeslána na
OSA a SUNAT. Na faktuře je následně uvedeno:

.. obrázek: peru/peru-vystavena-faktura.png
:alt:Odeslání faktury v EDI formátu modré barvy.

Asynchronní znamená, že dokument se neodesílá automaticky po vystavení faktury.

..._elektronické faktury:

Elektronická fakturační stav
*************************

**K odeslání**: Ukazuje, že dokument je připraven k odeslání do OSE.
a nebo automaticky prostřednictvím Odoo s cronem, který běží každou hodinu.
immediátně kliknutím na tlačítko „Odesláno“.

.. obrázek: peru/peru-sent-manual.png
:alt: Manuálně odeslat EDI.

**Odesláno**: Udává, že dokument byl zaslán do OSE a úspěšně ověřen.
Validace souboru ZIP je stáhnuta a do chatu se zaznamenává zpráva, která ukazuje
správné ověření vládou.

.. obrázek: peru/faktura-zaslana-z-peru.png
:alt:Zpráva na chat při platnosti faktury.

Pokud dojde k chybě při ověřování, zůstane stav faktury v položce „K odeslání“.
opravit lze a fakturu můžete zaslat znovu.

.. varování:
Jeden kredit se spotřebuje při každém odeslání dokumentu pro ověření. V tomto smyslu pokud
Při detekci chyby na faktuře je odeslána jedna další zpráva a spotřebováno se dvě kredity.
celkem.

Nejčastější chyby
~~~~~~~~~~~~~

Existuje mnoho důvodů, proč může být žádost o povolení od OSE nebo SUNAT zamítnuta.
Odesílá zprávu na vrcholu faktury s podrobnostmi o chybě a v nejběžnějším
Případy jsou jen náznakem, jak problém vyřešit.

Pokud dostanete chybovou hlášku o neplatnosti, máte dvě možnosti:

- Pokud se jedná o chybu v hlavních datech o partnerovi, zákazníkovi nebo dani, můžete ji snadno
aplikovat změnu v záznamu (například typ identifikace zákazníka) a poté kliknout
na tlačítko Znovu.
- Pokud je chyba spojena s nějakými údaji na faktuře přímo (Operační typ, chybějící
(údaje na fakturačních řádcích), správným řešením je vrácení faktury do stavu Návrh a aplikace
změny a poté opět zašlete fakturu na SUNAT k dalšímu ověření.

.... obrázek:: peru/peru-errors.png
:alt: Seznam nejčastějších chyb na fakturách.

Pro podrobnější informace se můžete podívat na stránku „Nejčastější chyby v SUNAT
<https://www.nubefact.com/codigos-error-sunat/>

Faktura v PDFReport
~~~~~~~~~~~~~~~~~~

Po schválení a ověření faktury ze strany SUNAT lze vytisknout zprávu o faktuře ve formátu PDF.
Ve zprávě je uveden QR kód, který potvrzuje, že faktura je platným daňovým dokladem.

.. obrázek: peru/peru-PDF.png
:alt:Přehled o fakturách ve formátu PDF.

IAP kredity
~~~~~~~~~~~

Elektronický IAP společnosti Odoo nabízí 1000 kreditů zdarma. Po spotřebování těchto kreditů v
výrobní databáze musí vaše společnost kupovat nové body, aby zpracovala vaše transakce.

Jakmile vyčerpáte kredity, zobrazí se vám červený štítek nahoře na faktuře s informací, že
Potřebujete další kredity? Můžete si je snadno zakoupit přes odkaz uvedený v
zprávu.

.. obrázek: peru/peru-credits-IAP.png
:alt: Nákup kreditů v IAP.

V rámci služby IAP jsou k dispozici balíčky s různými cenami podle počtu kreditů.
V ceníku v IAP je vždy uvedena částka v eurech.

Speciální případy použití
~~~~~~~~~~~~~~~~~

Postup zrušení
********************

Některé scénáře vyžadují zrušení faktury, například když byla vystavena omylem.
Pokud byla faktura již odeslána a schválena SUNATEM, správným postupem je
kliknutím na tlačítko „Požádat o zrušení“:

.. obrázek: peru/peru-zruseni.png
:alt:Tlačítko pro zrušení faktury.

Pro zrušení faktury je nutné uvést důvod zrušení.

Elektronická fakturační stav
^^^^^^^^^^^^^^^^^^^^^^^^^

**Zrušit**: Udává, že žádost o zrušení je připravena k odeslání do OSE.
buď automaticky prostřednictvím Odoa s cronem, který běží každou hodinu, nebo uživatel může odeslat
Odeslat ihned kliknutím na tlačítko „Odeslat nyní“. Jakmile je odesláno, obdržíte lístek s
Výsledkem je další zpráva a soubor CDR.

.. obrázek: peru/peru-zruseni-crd.png
:alt: Zrušení CDR zaslané SUNATem.

Zrušeno: Udává, že žádost o zrušení byla zaslána do OSE a úspěšně zpracována.
ověřený. Součástí ověření je stáhnutí archivu ZIP a zaznamenání hlášky do
Komunikace, která ukazuje správné ověření vlády.

.. obrázek: peru/peru-zrušeno.png
:alt:Faktura po zrušení.

.. varování:
Jeden kredit je spotřebován při každém požadavku na zrušení.

Exportní faktury
***************

Při vystavování vývozních faktur je třeba zohlednit následující skutečnosti:

- Typ identifikace vašeho zákazníka musí být Cizinec.
- Výběr typu operace ve faktuře musí být „Export“.
- Daň zahrnutá v řádcích faktury by měla být DPH.

.. obrázek: peru/peru-exp-faktura.png
:alt: Hlavní údaje exportního faktury.

Předplatby
****************

#Vytvořte fakturu na zálohu a aplikujte související platbu.
#Vytvořte konečnou fakturu bez zohlednění zálohy.
#Vytvořte konečnou fakturu s částkou přijaté zálohy.
#Sjednocení zápočtového listu s konečnou fakturou.
#Zbylou částku na konečném vyúčtování je nutné uhradit běžnou platební transakcí.

Zneužití faktur
*******************

Při vystavování faktur za zboží podléhající odpočtu je třeba brát v úvahu následující skutečnosti:

#Všechny produkty uvedené na faktuře musí mít tyto pole nastaveny:

.. obrázek:: peru/peru-detrackce.png
:alt:Zákazníci se obávají, že je vyrábějí z nekvalitních surovin.

#Výchozí operační typ v faktuře musí být „1001“.

.... obrázek: peru/peru-faktura-odpočtu.png
:alt:Kód detrakce na fakturách.

Kreditní poznámky
------------

Pokud je nutná oprava nebo vrácení peněz za platnou fakturu, musí být vygenerován kreditní doklad.
k tomu stačí kliknout na tlačítko „Přidat fakturu“, část peruánské lokalizace, kterou potřebujete
prokázat důvod pro poskytnutí úvěru vybráním jedné z možností v seznamu.

.. obrázek: peru/peru-kreditni-nota.png
:alt: Přidat fakturu s kreditním dokladem.

.. tip::
Při vytváření první kreditní poznámky vyberte metodu kreditu: Částečná náhrada, toto umožňuje
aby definoval pořadí kreditních poznámek.

Za výchozí je nastavený doklad o vrácení peněz v typu dokumentu:

.. obrázek: peru/peru-kreditni-doklad.png
:alt: Dokument typu kreditní poznámky.

Pokud chcete dokončit práci, postupujte podle pokynů na stránce „Credit Notes“
<../účetnictví/faktury zákazníkům/kreditní poznámky>.

.. poznámka::
Pro zpracování kreditních poznámek funguje stejně jako pro zpracování faktur.

Debetní poznámky
-----------

V rámci peruánské lokalizace kromě vytváření faktur z již existujícího dokumentu
Můžete také vytvářet poznámky o úhradě. Pro tento případ stačí použít tlačítko „Přidat poznámku k úhradě“.

Zaškrtnutím políčka „Debetní poznámka“ se vytvoří nový typ dokumentu.

.. _peru-edg:

Elektronická průvodce doručováním 2.0
-----------------------------

Elektronický dokument Guía de Remisión (GRE), který je vytvořen přepravcem,
podporovat přepravu nebo přesun zboží mezi místy, jako je sklad nebo
zřízení. V Odoo je potřeba provést několik kroků konfigurace, než bude možné úspěšně používat
tuto funkci.

Používání elektronického dokumentu „elektronická vrácená objednávka“ je povinné a vyžaduje se.
SUNAT pro daňové poplatníky, kteří potřebují převést své produkty, s výjimkou jednoduchého systému
Režim* (jednoduchý režim nebo RUS).

Příručky pro doručovatele
~~~~~~~~~~~~~~~~~~~~

Vysílač
******

Příručka pro doručení typu *Odesílatel* se vydává při uskutečnění prodeje nebo poskytnutí služby (včetně
zpracování), zboží se přiděluje k užívání nebo mezi prostory stejného
Společnost a další.

Tento dodací list vydává odesílatel zboží (tj. osoba, která zásilku poslala) na začátku
doručení zásilky. V Odoo je podporován průvodce doručením odesílatele.

.. viz též:
„Příručka pro vrácení <https://www.gob.pe/7899-guia-de-remision>“

Nosič
*******

Dodací průvodka typu Carrier ospravedlňuje přepravní službu, kterou poskytuje řidič (nebo dopravce).
hraje.

Tento přepravní řád vydává dopravce a musí být předán každému odesílateli při dodání zásilky.
Prochází veřejnou dopravou.

.. důležité::
Příručka pro doručovatele není v Odoo podporována.

.. viz též:
„Příručka pro přepravce SUNAT


Druhy dopravy
~~~~~~~~~~~~~~~~~~~~

Soukromý
*******

Pokud majitel přepravuje zboží vlastními prostředky, použije možnost „Soukromá doprava“.
vozidel. V tomto případě musí být vystaven odesílateli dodací list.

Veřejné
******

Při volbě dopravy typu „Veřejná“ se zboží přepravuje externím dopravcem.
v tomto případě musí být vystaveny dvě přepravní listy: jeden pro odesílatele a druhý pro přepravce.
Příručka pro doručovatele.

Přímo k SUNAT
~~~~~~~~~~~~~~~~~~~~~~~~~~

Vytvoření průvodce dodávkou v Odoo **musí být** zasláno přímo na SUNAT.
ať už se jedná o elektronický dokument poskytovatele: IAP, Digiflow nebo SUNAT.

Povinné informace
~~~~~~~~~~~~~~~~~~~~

Ve verzi 2.0 elektronického průvodce dodáním je vyžadována další informace o
konfiguraci, vozidla, kontakty a produkty. V obecné konfiguraci je nutno
Přidejte nové přihlašovací údaje, které si můžete stáhnout z portálu SUNAT.

Zrušení
~~~~~~~~~~~~~

Oba - odesílatel i přepravce - mohou elektronický nákladní list zrušit, pokud splňují následující
jsou splněny podmínky:

- Zásilka nebyla zahájena.
- Pokud byla zásilka zahájena, musí být změněn příjemce před dosažením konečného
cíl.

.. důležité::
SUNAT již nepoužívá výraz „Anula“, ale nyní používá výraz „Dar de baja“.
zrušení.

Testování
~~~~~~~

Sunat nepodporuje testovací prostředí, což znamená, že jakékoliv dodavatelské příručky, které byly
vzniklé omylem **bude** zasláno na adresu SUNAT.

Pokud se chybně vytvoří přepravní list na tomto zařízení, je nutné jej z
Portál SUNAT.

Konfigurace
~~~~~~~~~~~~~

.. důležité::
   - Elektronický odesílatel |GRE| je v současné době jediným podporovaným typem přepravní smlouvy v Odoo.
   - Dodací průvodce je závislý na aplikaci Odoo *Inventory*, štítku :guilabel:`l10n_pe_edi`.
:guilabel:`l10n_pe` moduly.
   - Druhý uživatel **musí být přidán** pro vytváření elektronických dokumentů.

Po provedení kroků pro konfiguraci elektronické fakturace podle pokynů v části „Nastavení účetnictví“
a „master data“ (<peru-master_data>) a „instalace“ (<general/install>).
:guilabel:`Dodací listina Peru 2.0“ („l10n_pe_edi_stock_20“).

Dále si musíte získat *ID klienta* a *tajné heslo klienta* od společnosti SUNAT. K tomu postupujte podle
„Manuál pro webové služby platformy nové GRE
<https://cpe.sunat.gob.pe/sites/default/files/inline-files/Manual_Servicios_GRE%20(1).pdf>.

.. poznámka::
Ve službě SUNAT je důležité mít správně nastavená oprávnění, protože ta se mohou změnit.
lišit od uživatelského nastavení pro elektronické fakturace.

Tyto přihlašovací údaje by měly být použity k konfiguraci obecných nastavení pro doručení zásilek.
:menu:„Soubor“ → „Nastavení“ → „Možnosti“, a v seznamu nalevo klikněte na „Peru
Soubor „Průvodce dodávkou“.

Nastavte následující pole:

- :guilabel:`ID klienta průvodce“: jedinečná *ID klienta* vygenerovaná v portálu SUNAT
- :guilabel:`Klientské tajné heslo klienta“: jedinečný API *klientský klíč*, který byl vytvořen na portálu SUNAT
- :guilabel:`Uživatelský účet SOL“: číslo RUC + uživatelské jméno SOL
- :guilabel:`Heslo uživatele SOL“: heslo uživatele SOL

.. obrázek: peru/gre-fields-example.png
:alt:Příklad konfigurace sekce pro průvodce dodávkou služby SUNAT.

.. poznámka::
Je nutné dodržovat formát „RUC + UsuarioSol“ (např. 20557912879SOLUSER).
:guilabel:`Uživatel SOL“ pole podle uživatele vybraného při generování |GRE| API
v portálu SUNAT.

Provozovatel
********

Operátorem je řidič vozidla v případě, že se dodací průvodka řeší soukromou cestou.
Doprava.

Pro vytvoření nového operátora přejděte na :menuselection:`Kontakty --> Vytvořit“ a vyplňte kontakt.
informace.

Nejprve vyberte „Osoba“ jako „Typ společnosti“. Poté přidejte
„Řidičský průkaz“ v záložce „Účetnictví“ kontaktního formuláře.

Pro adresu zákazníka zkontrolujte následující pole:

- :guilabel:`Okres“
- :guilabel:`Daňové identifikační číslo“ (:guilabel:„Doklad o identitě“/:guilabel:„Číslo registrace podniku“)
- :guilabel:`Daňové identifikační číslo“

.. obrázek: peru/operator-configuration.png
:alt: Konfigurace individuálního typu operátora v kontaktním formuláři.

Nosič
*******

Používá se, pokud je dopravní průvodce přepravován veřejnou dopravou.

Pro vytvoření nového dopravce přejděte na: „Kontakty – Vytvořit“ a vyplňte kontakt.
informace.

Nejprve vyberte „Společnost“ jako „Typ společnosti“. Pak přidejte „MTC
Registrační číslo“, „Vydavatelská instituce“ a „Autorizační úřad“.
Číslo.

Pro adresu společnosti zkontrolujte následující pole:

- :guilabel:`Okres“
- :guilabel:`Daňové identifikační číslo“ (:guilabel:„Doklad o identitě“/:guilabel:„Číslo registrace podniku“)
- :guilabel:`Daňové identifikační číslo“

.. obrázek: peru/company-operator-configuration.png
:alt:Konfigurace typu společnosti v kontaktním formuláři.

Dopravní prostředky
********

Pro konfiguraci dostupných vozidel přejděte na:
Vozidla a vyplňte formulář vozidla s informacemi potřebnými pro vozidlo:

- :guilabel:`Název vozidla“
- :guilabel:`Registrační značka“
- :guilabel:Je to M1 nebo L?
- :guilabel:`Speciální autorizační orgán“
- :guilabel:`Číslo autorizace“
- :guilabel:`Výchozí operátor“
- :guilabel:`Společnost“

.. důležité::
Je důležité zaškrtnout políčko „Jedná se o vozidlo M1 nebo L?“, pokud má vozidlo méně než čtyři kola.
koly nebo méně než osmi sedadly.

.. obrázek: peru/vozidlo-neni-m1-nebo-l-pe.png
:alt:Vozidlo nebylo vybráno jako vozidlo typu M1 nebo L s dalšími poli zobrazenými.

Produkty
********

Pro konfiguraci dostupných produktů přejděte na: „Sklad --> Produkty“ a otevřete
produkt, který má být konfigurován.

Ujistěte se, že v produktové formě je úplně konfigurována použitelná informace.
Zadejte pole „Částka celního tarifu“ (Field: Tariff item).

Vytvoření GRE
~~~~~~~~~~~~~~~~

Jakmile během procesu prodeje vytvoříte dodání ze skladu, ujistěte se, že dokončíte
V poli „GRE“ na pravém horním rohu převodního formuláře pro pole:

- :guilabel:`Doprava“
- :guilabel:`Důvod převedení“
- :guilabel:`Datum odjezdu“

Je také nutné vyplnit pole „Dopravní prostředek“ a „Řidič“ pod
:guilabel:`Pokyny pro odstoupení PE“ tab.

Převod zásilky musí být označen jako „Dokončeno“ pro tlačítko „Vytvořit odeslání“.
objevit se v levém menu převodního formuláře.

.. obrázek: peru/generate-gre-transferview.png
:alt:Tlačítko pro vytvoření přesměrovacího průvodce na přepravní formuláři ve fázi hotovo.

Jakmile je převodní formulář správně ověřen v SUNAT, generovaný soubor XML se stává dostupným.
v chatu. Nyní můžete vytisknout dodací lístek, který obsahuje podrobnosti o převodu a QR
kód, který byl ověřen SUNATem.

.. obrázek: peru/gre-dodací-lístek.png
:alt:Podrobnosti o převodu a QR kód na vygenerovaném lístku k přepravě.

Nejčastější chyby
~~~~~~~~~~~~~

- „Různé předpony pro produkty (T001 u některých, T002 u jiných)“

V současné době Odoo nepodporuje automatické přidávání předpon k produktům. Toto lze provést
ručně pro každý produkt vypouštěný do přírody. Toho lze dosáhnout i u nezpracovatelných produktů.
s tím, že nebude možná stoprocentní dohledatelnost.
- „2325 – Hmotnostní měření – Hodnota nesplňuje zadaný formát „Chybí pole“
„Váha“ v produktu

Tento problém nastává v případě, že je na produktu nastaveno „0,00“. Chybu lze opravit tak, že se zruší
přepravní list a vytvořit jej znovu. Ujistěte se, že jste před tvorbou přepravního listu nastavili hmotnost produktu.
nový nákladní list nebo se objeví stejná chyba.
- „JSONDecodeError: Očekávala se hodnota: řádek 1 sloupec 1 (znak 0) při vytváření průvodce doručením“

Tento chybový kód se obvykle vyskytuje kvůli problémům uživatele SOL. Zkontrolujte připojení uživatele
|SUNAT|; uživatel SOL musí být zaregistrován v RUT + ID uživatele. Například
„2012188549JOHNSMITH“.
- „Číslo související s přepravou zboží nesplňuje stanovený formát:
chyba: dokument související

Pole „Druh souvisejícího dokumentu“ a „Číslo souvisejícího dokumentu“ se vztahují pouze na faktury.
účtenky.
- „Chyba klienta 400: špatná žádost o adresu“

Tento problém nelze vyřešit v Odoo, doporučujeme kontaktovat |SUNAT| a ověřit
Uživatel. Možná bude nutné vytvořit nového uživatele.

- „Nalezeno neplatné obsahové znaménko začínající prvkem cac:BuyerCustomerParty“

Toto chybové hlášení se zobrazí, pokud je důvod převodu nastaven na „jiný“. Prosím vyberte jinou možnost.
Podle oficiální dokumentace průvodce přepravními listy společnosti SUNAT je důvodem převodu 03
(prodej s dodáním třetí straně) nebo 12 (ostatní) nefunguje v Odoo, protože byste neměli
mít prázdného nebo neexistujícího zákazníka.
- „Duda klient: spotřeba kreditů IAP při používání GRE 2.0“

Pro klienty v reálném čase používající IAP není spotřebováno žádné kredity (teoreticky), protože neprojdou
OSE, tedy tyto dokumenty jsou zasílány přímo na SUNAT.
- „Chyba s kredenčními formuláři GRE 2.0 (sledování chyby)“

Odoo v současné době vyhazuje chybu s stop-tracing místo zprávy, že kreditní údaje nejsou platné.
je správně nakonfigurován v databázi. Pokud se takové chyby vyskytnou ve vaší databázi, zkontrolujte prosím
kvalifikace.

Elektronické fakturace v e-commerce
------------------------------

Nejprve nainstalujte modul „e-commerce v Peru“ („l10n_pe_website_sale“).

Modul **peruánského e-commerce** umožňuje funkce a konfigurace:

- umožňují klientům vytvářet online účty pro účely elektronického obchodování;
- podpora byla vyžadována v oblasti fiskálních polí aplikace **eCommerce**.
- přijímat platby za objednávky online.
- generovat elektronické dokumenty z e-commerce aplikace.

.. poznámka::
Modul **peruánské elektronické komerce** je závislý na předchozí instalaci
Aplikace pro fakturaci nebo účetnictví, stejně jako aplikace Webové stránky.

..._konfigurace e-commerce Peru:

Konfigurace
~~~~~~~~~~~~~

Po konfiguraci peruánského :ref:`elektronického fakturace <peru-accounting-settings>` toku dokončete
následující konfigurace pro e-commerce tok:

- „Registrace klientského účtu“ viz „Pravidla pro nákup online“
- Automatické zpracování faktur <handling/legal>
- :/dokumenty/e-commerce/produkty/: nastavte :guilabel:„Způsob fakturace“ na
:guilabel:`Počet kusů“ a definujte požadované „Daň z přidané hodnoty zákazníka“.
- :doc:`../platební_poskytovatelé`;
- :/dokumenty/e-commerce/doručení/: Pro každý způsob dopravy nastavte
Zadejte pole „Dodavatel“ jako „Fixní cena“. Pak nastavte „Fixní cenu“.
výše větší než 0,00 (ne 0,00), protože cena dopravy se přičítá k fakturační linii.

.. poznámka::
   - „Mercado Pago <https://www.mercadopago.com/>“ je internetový poskytovatel platebních služeb, který je v Odoo podporován
jehož území zahrnuje několik zemí, měn a platebních metod v Latinské Americe.
   - Ujistěte se, že definujete „Prodejní cenu“ na „Dodací produkt“.
způsob dopravy, který zabrání chybám při ověřování faktury u |SUNAT|.
   - Zdarma doručení nabídnout ručně odstraněním produktu „Doručení“ nebo alespoň použitím
0,01 USD (1 cent) za ověření faktury u SUNAT.

.. viz též:
:doc:`Nastavte platební metodu Mercado Pago. <../payment_providers/mercado_pago>`

Fakturační tok pro elektronický obchod
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Jakmile jsou všechny konfigurace nastaveny, fiskální vstupní pole budou
být k dispozici během procesu platby pro přihlášené zákazníky.

Když zákazníci vloží svá daňová data do pokladny při placení a úspěšně nakoupí, obdrží fakturu.
je vytvořen s odpovídajícím elementem EDI. Druh dokumentu (Faktura/Boleta) je vybrán
na základě jejich daňového identifikačního čísla (RUC/DNI). Faktura musí být poté zaslána do OSE a k SUNAT
<stav-elektronické-faktury-v-peru>. Výchozí nastavení je takové, že všechny vystavené faktury jsou odeslány jednou denně
plánovaná akce, ale můžete také odeslat každou fakturu ručně, pokud je třeba.

Jakmile je faktura ověřena u SUNATu, zákazníci mohou stáhnout soubor .zip s CDR, XML.
a přímo z portálu zákazníka kliknutím na tlačítko „Stáhnout“.

Zprávy
=======

... _peru/reports-ple:

Trvalé inventarizační zprávy: |PLE| 12.1 a |PLE| 13.1
------------------------------------------------------

Odoo může vytvořit dva trvalé skladové výkazy ve formátu souboru .txt pro účetnictví v Peru:
a |PLE| 13.1. Všechny skladové operace musí být zaznamenány.

- |PLE| 12.1 pouze eviduje skladové zásoby v jednotkách fyzických jednotek a soustředí se na příjem a výdej
zboží pro efektivní řízení a plánování.

- |PLE| 13.1 sleduje **fyzické množství i peněžní hodnotu zásob** a poskytuje
komplexní pohled na daňové a řídící účely.

Obě zprávy musí být aktualizovány každých šest měsíců (leden až červen, červenec až prosinec) s měsíční
transakční podrobnosti uvedené v těchto obdobích. Termíny pro odevzdání jsou 1. října pro
První pololetí a 1. dubna pro druhé pololetí v souladu s rozhodnutím
Úřadová vyhláška č. 169/2015*.

Konfigurace
~~~~~~~~~~~~~

Než vygenerujete zprávy PLE 12.1 nebo PLE 13.1, ujistěte se, že je v nastavení pole Peru - Sklad
Pokud je modul „Zprávy“ („l10n_pe_reports_stock“) nainstalován, pak aktualizujte pole pro:

- :ref:`Produkty <peru/reports-ple-products>`
- :ref:`Skladiště <peru/reporty-ple-skladiste>“
- :ref:`Přesuny zásob <peru/reports-ple-transfers>“

.. peru/reports-ple-products:

Produkty
********

Pro hlášení |PLE| je nutné použít několik konfigurací, které se týkají produktu nebo kategorie produktů:

- Typ existujícího stavu: Pro všechny produkty vyžadující hlášení PLE se přejděte do záznamu produktu.
:guilabel:`Účetnictví“ záložce a vyberte typ existence podle SUNAT
v příloze č. 5 pro účetní závěrku.

- **Automatická inventarizace**: Pro skladovatelné zboží (:dfn:`produkty sledovaného skladu`)
použít automatické ocenění zásob.
<../../Inventar a MRP/Inventar/Produktverwaltung/Bestandsbewertung/Bestandsbewertungs-Konfiguration>.
Jakmile je zapnutá automatická inventarizace, tento způsob ocenění může být aktivován pro
:ref:`Kategorie produktu <Inventar/Lagerbestand/Bewertung nach Produktkategorie>“.

- Metoda výpočtu: Skladovatelné zboží musí použít metodu výpočtu:

**jiný než** než Standardní cena, protože účetní záznamy vytvořené při pohybu skladových zásob jsou
používané k vyplnění zprávy PLE.

...

Skladiště
**********

Když se budete snažit o zřízení skladu
<../../skladovani-a-mpr/sklady-a-ukladiště/sledování-zásob/sklady>
Do pole „Kód zřízení“ musí být vyplněn kód, který slouží jako jedinečné identifikační číslo pro každý
skladu a mělo by se jednat o číselnou kombinaci, která má obsahovat mezi 4 až 7 číslicemi.

..._peru/reports-ple-transfers

Převody zásob
*******************

Přesun zásob je klíčovým procesem zachyceným v zprávách PLE 12.1 a PLE 13.1.
:doc:`Přesuny zásob <../../inventory_and_mrp/inventory/shipping_receiving/daily_operations>`
zahrnují jak příchozí, tak odchozí zásilky.

Při ověřování převodu zásob (na faktuře nebo dodacímu listu) vyberte
:guilabel:`Druh operace (PE)` podle tabulky č. 12 SUNAT
reportér.

Vytvořte soubor .txt pro trvalé záznamy o inventuře Kardex
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|PLE| 12.1 a 13.1 jsou dvě samostatné knihy. Knihy musí být stáhnuty jako soubor v příponě „.txt“
formátu z Odoo a poté je předat do softwaru |SUNAT| |PLE|.

V seznamu reportů klikněte na položku „Hodnotící zpráva o inventáři“ (viz část Inventář > Hlášení > Zprávy o inventáři).
tlačítko „Zprávy PLE“ a poté vyberte období a zprávu, kterou chcete zobrazit.
Export: Buď PLE 12.1 nebo PLE 13.1. Odoo vytvoří soubor s příponou .txt
pro zvolený výkaz.

.. obrázek: peru/l10n-ple-export-button.png
:alt: Výběr tlačítek export

.. poznámka::
Stáhnout lze pouze zprávu ve formátu .txt, žádný náhled nebo vizualizace není k dispozici.
dostupné v rámci Odoo.
