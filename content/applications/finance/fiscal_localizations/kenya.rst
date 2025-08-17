=====
Keňa
=====

.._lokalizace/keňa/konfigurace:

Konfigurace
=============

Nainstalujte balíček pro místní daňové příjmy 🇰🇪 **Kenya** :ref:`<fiscal_localizations/packages>`, abyste získali
všechny funkce kenijské lokalizace.

eTIMs
=====

„Kenya Revenue Authority (KRA)“ <https://www.kra.go.ke/>_ implementovala
„elektronický systém pro správu daňových dokladů (eTIMS)“
Pro vybírání daní.

Pro zaslání dokumentů prostřednictvím e-TIMs musíte použít :abbr:`OSCU (Online Sales Control Unit)“.
integruje s již existujícími systémy fakturace pro obchodníky (TIS), jako je například Odoo.
OSCU se používá k ověření, šifrování, podepisování, přenášení a ukládání daňových dokladů.

.. poznámka::
Zajistěte si instalaci modulu **Kenya eTIMS EDI**, abyste mohli používat OSCU.
zařízení plně.

.. _keňa/základní informace:

Inicializace zařízení OSCU
--------------------------

OSCU musí být inicializován před použitím. Chcete-li tak učinit, přejděte na:
Nastavení“, klikněte na „Aktualizovat informace“ v sekci „Společnosti“ a zadejte své
:guilabel:`Daňové identifikační číslo“.

Pro inicializaci OSCU:

#Přejděte na „Nastavení -> Obecné nastavení“ a posuňte se dolů k položce „Keňa“.
v sekci „Součást eTIMS“.
#Nastavte režim serveru na „Test“ pro inicializaci.
#Zadejte sériové číslo zařízení a zaškrtněte obě dvě políčka.
#Klikněte na tlačítko „Inicializovat OSCU“.

.. poznámka::
K dispozici jsou tři režimy serveru:

   - :guilabel:`Demo`: Vytvořený pro účely demonstrace, používá falešná data a nevyžaduje
inicializovala OSCU.
   - :label:Testování: Používá se k ověření připojení k eTIMS.
   - :guilabel:`Produkce“: používá se pro živé databáze, které jsou připraveny k odesílání dat.

.. Důležité:
Pokud je zařízení již **zapojeno do jiného ERP systému**, zapněte funkci
:doc:`../obecne/rozvojovy-mod.html“. Pak v sekci „Integrace s Kenyským systémem eTIMs“
Do pole „ID jednotky“ zadejte ID jednotky a klíč, který byl vytvořen předchozím krokem.
inicializaci v poli CMC klíč. Klikněte na tlačítko Uložit, když je hotovo.

Jakmile je modul **OSCU inicializován** (viz kapitola „Inicializace“), může být použit k získání sériového čísla
je generován pro každou společnost na této databázi s nastaveným státem :guilabel:`Keňa`.
sériové číslo je generováno na základě identifikačního čísla společnosti (bez ohledu na jeho platnost).
je jedinečné a sekvenční sériové číslo začínající předponou „ODOO“ následované jménem společnosti.
Číslo DPH a sekvence čísel.

Registrace na eTIMs
--------------------

Daňoví poplatníci musí zaregistrovat a vytvořit účet na portálu KRA <https://etims.kra.go.ke/basic/login/indexLogin>.
Pokud účet ještě nemáte, postupujte takto:

#Zaregistrujte se, zadejte své **PIN** a ověřte všechny údaje, včetně telefonního čísla.
číslo, e-mailovou adresu a poštovní adresu. Na stránce iTax opravte všechny chyby.
<https://itax.kra.go.ke/KRA-Portal/>`.
#Odpověď s kódem OTP (jednorázový heslo) je odeslána na telefonní číslo, které jste uvedli.
pokud jste ji neobdrželi.
#Nahrát identifikační číslo podnikatele nebo ředitelské číslo (jak je uvedeno v iTaxu), spolu s
vyplněné a podepsané **závazek**.
#Na stránce eTIMs klikněte na „Žádost o službu“ v horní části stránky a vyberte
:guilabel:`OSCU“ jako typ eTIMS, zadejte „Odoo KE LTD“ jako třetí stranu a
Vyplňte sériové číslo OSCU své společnosti, které jste si dříve získali.

.. poznámka::
Schválení požadavku na službu je obvykle rychlé. Pokud dojde k prodlevě, kontaktujte operaci eTIMS
nebo kanceláři KRA.

.. varování: Závazná forma

   - Část 1: Vyplňte údaje poplatníka.
   - Část 2: Vyplňte informace o majiteli podniku nebo jeho ředitele.
   - Část 3: Vyplňte své jedinečné sériové číslo z Odoo.
   - Část 4: Zaškrtněte políčko **OSCU**, zadejte PIN společnosti Odoo KE LTD „PO52112956W“ a zadejte verzi Odoa, kterou používáte
používat od verze 17.0 nebo novější.
   - Část 5: Zkontrolujte povinná pole, zadejte datum a podepište.

e-TIMs kódy
-----------

Komunální kódy jsou automaticky stahovány z serverů API KRA eTIMS každé dva dny.
Chcete-li je ručně stáhnout, postupujte takto:

#Zapněte vývojářský režim pomocí příkazu :doc:`../../general/developer_mode`.
#Přejděte na „Nastavení > Technické > Automatizace: Plánované akce“ a vyhledejte
:guilabel:`K ETIMU: Získat kódy standardu KRA“.
#Klikněte na akci v seznamu a poté klikněte na tlačítko „Spustit ručně“, abyste získali kódy.

Přejděte na „Účetnictví >> Konfigurace >> Kódy Oscu“ a zobrazte seznam
oscu kódy.

.. obrázek: kenya/oscu-codes.png
:alt: Seznam získaných kódů OSCU.

.. _etims/unspsc:

Kódy UNSPSC
------------

KRA potřebuje k registraci produktu kódy UNSPSC. Tyto kódy jsou automaticky
získané z API serverů KRA eTIMS každý den. Chcete-li je stáhnout ručně, postupujte takto:

#Zapněte vývojářský režim pomocí příkazu :doc:`../../general/developer_mode`.
#Přejděte na „Nastavení > Technické > Automatizace: Plánované akce“ a vyhledejte
:guilabel:`K eTIMS: Stáhnout kódy UNSPSC z eTIMS“.
#Klikněte na akci v seznamu a poté klikněte na tlačítko „Spustit ručně“, abyste získali kódy.

Přejděte do formuláře produktu a v záložce „Účetnictví“ klikněte na „UNSPSC“.
Zobrazit seznam kódů UNSPSC, které byly získány.

Oznámení
-------

Zprávy jsou automaticky stahovány z serverů KRA eTIMS API každý den.
Pokud chcete provést změnu ručně, postupujte takto:

#Zapněte vývojářský režim pomocí příkazu :doc:`../../general/developer_mode`.
#Přejděte na „Nastavení > Technické > Automatizace: Plánované akce“ a vyhledejte
:guilabel:`K ETIMU: Stáhnout upozornění z eTIMU“.
#Klikněte na akci v seznamu a poté klikněte na „Spustit ručně“, abyste získali oznámení.

Přejděte na: „Účetnictví“ -> „Konfigurace“ -> „OSČ - oznámení“.
Vyhledávací oznámení.

Společnost s více subjekty
-------------

.._keňa/odnož:

.. viz též:
:doc:`../obecne/spolecnosti`

Pokud máte více společností, můžete je centralizovat a spravovat.
všechny na jedné databázi Odoo. KRA identifikuje a rozlišuje mateřskou společnost od
jejími „pobočkami“ pomocí identifikátorů. Dále jsou dceřiné společnosti zařazeny jako :ref:`filiálky
<obecné/firmy/oddělení> mateřské společnosti.

Pro konfiguraci identifikátoru společnosti otevřete aplikaci Nastavení, klikněte na tlačítko „Aktualizovat informace“
sekci „Společnosti“ a vyhledejte pole „Kód pobočky eTIMS“.
Společnost má v prostředí více společností identifikátor pobočky rovný hodnotě 00. Společnosti, které nejsou
mateřská společnost má jiný identifikátor než 00 a byla přiřazena identifikační číslo od KRA.

Pro vyzvednutí identifikátoru větve (Branch ID) z KRA pro vaše nepodřízené společnosti zajistěte, aby mateřská společnost měla
keňský daňový identifikátor a zařízení OSCU bylo inicializováno.
Poté přejděte na záložku „Větve“ a klikněte na „Naplnit z KRA“.

.. poznámka::
   - KRA považuje každou **místo plnění** za samostatnou pobočku (ID).
   - Zařízení **OSCU** musí být inicializováno nezávisle na každém
pobočku.

Kontaktní číslo pobočky
-----------------

Přiřadit kontaktu identifikátor větve, přejděte na formulář Kontakty, klikněte na položku Účetnictví.
tabulka, a do pole „Kód pobočky eTIMS“ zadejte kód pobočky.

.. poznámka::
Výchozí hodnota ID větve kontaktu je nastavena na „OO“.

Sekvenční řetězce KRA
-------------

.. důležité::
Výpisy faktur v Odoo a výpisy v KRA jsou **různé**.

V Odoo se sledování faktur týká **mateřské společnosti**. Mateřské společnosti mohou vidět faktury
filiálky, ale filiálky **nemohou** vidět faktury mateřské společnosti nebo jiných poboček.

KRA potřebuje **nezávislé** sekvence na každé větvi. Proto Odoo spravuje sekvence individuálně
na pobočku.

.. příklad::
Pokud máte mateřskou společnost s dvěma pobočkami, pak by se vám na fakturách objevovalo následující pořadí:

   - Vytvoření faktury na **oddělení 1**: INV/2024/00001
   - Vystavení faktury na **oddělení 2**: INV/2024/00002;
   - Vystavení faktury na mateřskou společnost: INV/2024/00003.

Takto Odoo řeší sekvence, aby byly v souladu s předpisy KRA:

   - Vytvoření faktury na **oddělení 1**: INV/2024/00001
   - Vystavení faktury na **oddělení 2**: INV/2024/00001
   - Vystavení faktury na účet mateřské společnosti: INV/2024/00001.

Pojištění
=========

Pro poskytovatele zdravotních služeb můžete zaslat informace o pojišťovně rodiče a pobočce
a aktualizujte ji v eTIMS. Pro aktualizaci přejděte na:
Nastavení“, posuňte se do části „Kenya eTIMS Integration“ a vyplňte
:guilabel:„Kód“, :guilabel:„Jméno“ a :guilabel:„Sazba“. Klikněte na „Odeslat pojištění“
Podrobnosti jsou na konci.

.. _keňa/registrace výrobku:

Registrace produktu
====================

KRA vyžaduje, aby se produkty zaregistrovaly předtím, než začnou podnikat.
pohyb zásob, :abbr: „BOM“ (seznam materiálů), faktury zákazníkům atd. Pro výrobek je
registrované, musí být na formuláři výrobku vyplněny tyto pole:

- V záložce „Obecné informace“ v položce „Náklady“.
- V záložce „Účetnictví“:

  - „Přepravní jednotka“
  - :guilabel:`Množství balení“;
  - :guilabel:`Původní země“;
  - :guilabel:`Produktový typ eTIMS“;
  - :guilabel:`Pojištění platné“;
  - :ref:`Kategorie UNSPSC <etims/unspsc>“.

Pokud jsou výše uvedené prvky definovány, produkt se automaticky zaregistruje při odeslání
operace na KRA. Pokud ne, upozorní vás žlutý pruh nahoře na obrazovce
Zveme vás k ověření chybějících prvků.

.. obrázek:kenya/product-registration.png
:alt:Šablona pro registraci produktu.

Pohyby na burze
===============

Všechny pohyby zásob musí být zaslány do KRA. Nemusí obsahovat fakturu, pokud
vnitřní operace nebo úpravy zásob; proto Odoo automaticky odesílá všechny pokud je alespoň jedna
pokud jsou splněny následující podmínky:

#Žádný kontakt není stanoven pro přesun.
#Kontakt je vaší mateřskou společností nebo pobočkou mateřské společnosti.

Pokud se pohybují akcie vnější operací (např. kontakty, které nejsou součástí rodičovské
součástí společnosti nebo jejích poboček), pošle se automaticky pohledávka *po* odeslání faktury
eTIMs.

.. poznámka::
   - Přesun akcií musí být potvrzen před odesláním faktury do eTIMS.
   - Produkt musí být zaregistrován, aby se mohl přesunout na sklad.
odeslána do eTIMS. Pokud produkt ještě není zaregistrovaný, objeví se žlutá lišta s upozorněním.
registraci výrobků.

Nákupy
=========

Odoo automaticky stahuje nové faktury od dodavatelů z eTIMS každý den.
faktury dodavatelů a zaslat potvrzení do KRA. Potvrdit fakturu dodavatele je možné pouze v případě, že bude spojena s
jedna nebo více potvrzených objednávkových linií.

.. kenya/nákupy:

V případě nákupů (ne dovozních dokladů) je možné spojit řádky objednávkových dokladů s fakturami.
Jsou následující:

#Přejděte na: „Účetnictví“ - „Dodavatelé“ - „Faktury“.
Výpis z prodejního dokladu se stáhne ze serverů KRA. Soubor ve formátu JSON je k dispozici v chatu
fakturu dodavatele, pokud je třeba.
#Odoo se dívá na daňové identifikační číslo dodavatele (dodavatele).

   - Pokud je neznámý, vytvoří se nový kontakt (partner).
   - Pokud je známý kontakt a identifikátor pobočky je stejný, použije Odoo známý kontakt.

#Vybraný faktura od KRA obsahuje položku „Produkt“. Každá dodavatelská faktura musí obsahovat
produkt, který bude později potvrzen a odeslán do eTIMS.
#Odoo kontroluje stávající nákupní objednávky, které odpovídají produktům zadaným v předchozím kroku.
a partnerovi (pokud je nějaký). Klikněte na pole „Dodací lístek“ a vyberte správný.
souvisejících položek nákupního příkazu, které odpovídají produktům. Množství na faktuře *musí být*
stejné jako objednané množství uvedené v nákupním příkazu.

Pokud žádná z existujících položek objednávky neodpovídá položkám na faktuře, klikněte
:guilabel:`Vytvořit objednávku“ a vytvořte objednávku na základě nezpracované řádky.
:guilabel:`Potvrdit“ výsledný pohyb zásob a „Potvrdit“ fakturu.

#Nastavte metodu v poli „Způsob platby“ na hodnotu eTIMS.
#Jakmile jsou všechny kroky dokončeny, klikněte na tlačítko „Odeslat do e-TIM“ a odeslat fakturu dodavateli.
Výpis z eTIMu potvrzuje fakturu dodavatele, číslo faktury KRÁLKA je uvedeno v
:guilabel:`Podrobnosti o eTIM“ záložka.

.. obrázek: kenya/purchase-order-lines.png
:alt: Kroky při registraci účtu.

Fakturace
=========

.. poznámka::
KRA neakceptuje prodej, pokud není zboží skladem.

To je doporučený prodejní tok v Odoo při prodeji:

#Vytvořte objednávku na prodej.
#:guilabel:`Přijmout“ dodávku.
#Potvrďte fakturu.
#Klikněte na tlačítko „Odeslat a vytisknout“ a poté zapněte „Odeslat do eTIMS“.
#Klikněte na tlačítko „Odeslat a vytisknout“.

Jakmile je faktura odeslána a podepsána KRNAPem, následující informace se na
it:

- **Číslo faktury KRA**
- Povinné pole faktury KRA, jako například **informace o SCU**, **datum**, **ID SCU** nebo **číslo dokladu**
číslo, počet položek, vnitřní datum a podpis o přijetí.
- Tabulka daně z příjmu fyzických osob - KRA.
- Jedinečný **KRA QR kód** pro podepsaný daňový doklad.

Dovoz
=======

Kódy celních dovozů jsou automaticky stahovány z serverů API KRA eTIMS každý den.
Pokud chcete získat soubory ručně, postupujte následovně:

#Zapněte vývojářský režim pomocí příkazu :doc:`../../general/developer_mode`.
#Přejděte na „Nastavení > Technické > Automatizace: Plánované akce“ a vyhledejte
:guilabel:`K ETIMu: Přijmout celní dovoz z OSCU“.
#Klikněte na akci v seznamu a poté klikněte na tlačítko „Spustit ručně“, abyste získali kódy.

Přejděte na „Účetnictví“ -> „Dodavatelé“ -> „Dovoz zboží“.

Potřebné kroky pro odeslání a podepsání **celních dovozů** v KRA jsou následující:

#Přejděte na: „Účetnictví“ -> „Dodavatelé“ -> „Zahraniční dovoz“. Zahraniční dovoz je získán.
automaticky z KRA.
#.Souhlasí importovaný produkt s již registrovaným produktem v poli „Produkt“ (nebo
vytvořit produkt, pokud neexistuje žádný související produkt.
#Zadejte dodavatele do pole „Dodavatel“ (vlastnost guilabel:Partner).
#. Podle partnera se importovaný položka shoduje s příslušnou objednávkou nákupu (viz
:ref:`kroky nákupu <kenya/purchases>). Při přepravě do zemí mimo EU je nutné správně nastavit
dovážení je povoleno.

Pokud neexistuje související objednávka nákupu, vytvořte ji a potvrďte ji. Poté potvrďte
převzetí zboží kliknutím na tlačítko „Přijmout produkty“, poté na „Zkontrolovat“ v nákupním košíku
pořádku.

#Klikněte na tlačítko „Souhlasit a schválit“ nebo „Souhlasit a zamítnout“, podle toho, jaký
stav zboží.

.. poznámka::
Přílohou chatu o dovozu je soubor JSON, který obdržíme od KRA.

BOM
===

KRA vyžaduje odeslání všech BOM do svého systému. Pro zaslání BOM do eTIMS je nutné poslat produkt a jeho součásti
*musí být* zaregistrována: [ref] „Registrace produktu“ [/ref]. Chcete-li zobrazit seznam součástek produktu, klikněte na
produkt a pak klikněte na tlačítko „Seznam komponent“.

Ujistěte se, že jsou vyplněny požadované pole „KRA“ podle
v sekci „Podrobnosti o KRA eTIMS“ v záložce „Účetnictví“ v kartě produktu.
klikněte na tlačítko „Odeslat do eTIMS“. Úspěšné odeslání BOM je potvrzeno v chatovací oblasti.
Kde je také uložen odeslaný požadavek v připojeném souboru ve formátu JSON.

Kreditní poznámky
============

KRA nepřijímá kreditní faktury s vyššími cenami nebo množstvím než v původním daňovém dokladu.
Vytvoření kreditní poznámky vyžaduje uvedení důvodu: V tiskopisu pro vystavení kreditní poznámky přejděte na
kartě „Podrobnosti o eTIMs“, vyberte důvod „eTIMs fakturační poznámky“ a poté zvolte
číslo faktury do pole „Zrušení“.
