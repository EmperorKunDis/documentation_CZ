=================
Vytvářejte citace
=================

V Odoo **Sales** lze vytvářet nabídky a odesílat je zákazníkům. Jakmile byla nabídka
potvrzena, stává se z ní oficiálně objednávka na prodej, která pak může být fakturována a zaplacena.

.. prodej/cenové nastavení:

Nastavení citace
==================

Chcete-li získat přístup k těmto nastavením, přejděte na: „Prodejní aplikace“ -> „Konfigurace“.
Nastavení“, a posuňte se do části „Citace a objednávky“.

.. obrázek: create_quotations/quotations-orders-section.png
:align:center
:alt:Oddíl „Citace a objednávky“ v nastavení aplikace Odoo Sales.

- :guilabel:`Šablony cenových nabídek“: Zapněte tuto možnost, abyste mohli vytvářet šablony cenových nabídek.
standardních produktů nabízených na formulářích s cenovými nabídkami. Pokud je zaškrtnuto
vyznačeno, objeví se další pole s názvem „Výchozí šablona“ spolu s odkazem na
:guilabel:`Šablony citací“ stránce.
- :guilabel:`Online podpis“: Požádejte o online podpis k potvrzení objednávky.
- :guilabel:`Online platba“: Požádejte zákazníky o potvrzení objednávky prostřednictvím online předplatby.
platba v plné nebo částečné výši (přičemž při zaškrtnutí této položky se zobrazí další pole
:guilabel:"Předplacená částka (%)", zobrazí se také odkaz na :guilabel:"Platbu
Stránka poskytovatele.
- :guilabel:`Standardní platnost citační zkratky“: Zadejte pevný počet dnů (v :guilabel:`dnech“)
platnost citátů.
- :guilabel:`Výchozí opakování“: Vyberte výchozí interval z roletky, který chcete použít.
období pro nové cenové nabídky.
- :guilabel:`Varování při prodeji“: Získat varovné zprávy o objednávkách, které obsahují konkrétní produkt nebo
zákazníci.
- :guilabel:`Stavěč cenových nabídek PDF“: Upravte vzhled cenové nabídky pomocí hlavičkových stránek a produktů
popisky, stránky s patičkou a další.
- :guilabel:`Potvrzené prodeje“: Ujistěte se, že nebude možné provádět další úpravy potvrzených objednávek.
- :guilabel:`Faktura pro formální účely“: Odešlete faktury pro formální účely zákazníkům.

Chcete-li aktivovat kteroukoli z těchto možností, zaškrtněte políčko vedle požadované volby (požadovaných voleb) a poté klikněte
:guilabel:`Uložit“.

Dashboard citací
====================

Dashboard „Úryvky“ je stránka, která se zobrazí po otevření aplikace „Prodej“.

Výchozí nastavení panelu „Citáty“ zobrazuje všechny citace v databázi související s
uživatel, který je aktuálně přihlášený, jak naznačuje výchozí filtr „Moje citáty“ v hledání
bar.

.. obrázek: vytvořit_citace/citáty-přístupová-stránka.png
:align:center
:alt:Dashboard citátů, který je součástí aplikace prodeje v Odoo.

.. poznámka::
Pro zobrazení všech citátů v databázi je potřeba odstranit filtr „Moje citace“.
hledání.

Citace na této stránce se zobrazují v výchozím seznamovém pohledu, ale mohou být také zobrazeny jako
:icon:`oi-view-kanban` :guilabel:`Kanban“ pohled, :icon:`fa-calendar“ :guilabel:`kalendář“,
:ikonka: oi-view-pivot :guilabel: Pivotová tabulka, :ikonka: fa-area-chart :guilabel: Graf
:icon:`fa-clock-o` :guilabel:`Aktivita“ Zobrazení.

Pro zobrazení a/nebo úpravu jakéhokoliv uvedeného citátu na panelu „Citáty“ klikněte na
vybrané citační řádky z seznamu a Odoo odhalí konkrétní formulář pro vybranou položku.
citát.

Vytvořit nabídku
================

Pro vytvoření nabídky otevřete aplikaci „Prodej“ a klikněte na tlačítko „Nový“.
umístěné v horním levém rohu hlavního panelu „Citace“.

.. důležité:
Tlačítko „Nový“ je **pouze** přítomno, pokud je panel „Úryvky“ v seznamovém zobrazení.
nebo v kanbanovém pohledu.

Kliknutím na tlačítko „Nový“ se zobrazí prázdná citační forma s různými poli a záložkami.
konfigurovat.

.. obrázek: create_quotations/quotation-form.png
:align:center
:alt: Typická citace ve prodejním modulu aplikace Odoo.

Začněte vložením jména zákazníka do pole „Zákazník“ na horní části formuláře.
je povinný údaj.

Pokud je zákaznická adresa již v databázi, pak se na faktuře zobrazí
V poli „Adresa doručení“ se automaticky vyplní informace uložené pro příslušného zákazníka.
pole, která jsou založena na datech ze záznamu kontaktu zákazníka (nalezeném v části **Kontakty**
aplikace).

Pokud zákazník dostal odkaz od jiného zákazníka nebo kontaktu, zadejte jejich jméno v
:guilabel:`Zdroj odkazu“ pole.

Pokud je vybrán referer, objeví se nové pole „Provizní plán“, ve kterém je
Provize lze vybrat z roletky, tato provize je odměna pro kontakt
vybrané v poli „Zdroj“.

Dále pokud nebyly již automaticky vyplněny informacemi o zákazníkovi, zadejte
Vhodné adresy v polích „Adresa faktury“ a „Adresa dodání“.
Oba tyto políčka jsou povinná.

Pak si z nabídky vyberte šablonu citace.
citace. Je třeba poznamenat, že se mohou objevit další pole v závislosti na šabloně
vybrané.

Výchozí datum, které se zobrazuje v poli „Expirace“ je založeno na čísle, které bylo nakonfigurováno.
v nastavení „Výchozí platnosti cenové nabídky“ (v
:menuselection:`Prodejní aplikace --> Konfigurace --> Nastavení“).

..tip:
Při použití šablony citace je datum v poli „Expirace“ založeno na
:guilabel:`Platnost citace“ na šabloně formuláře.

Pokud je citace pro opakující se produkt nebo předplatné, vyberte požadované:guilabel:Recurring
Vyberte si z nabídky „Plan“.

Pokud chcete, vyberte konkrétní ceník, který se má vztahovat na tuto nabídku.

Zvolte konkrétní platební podmínky, které se mají použít pro tuto nabídku.

Karta řádků objednávky
---------------

První záložka objednávkového formuláře je záložka „Řádky objednávky“.

V tomto záložce vyberte produkty a množství těchto produktů, které chcete přidat do nabídky.

Existují dvě možnosti, jak produkty přidat do nabídky z této záložky.

Klikněte na tlačítko „Přidat produkt“, vyberte požadovaný výrobek z roletky „Produkty“.
pole a pokračujte v nastavení množství vybraného produktu, pokud je třeba.

nebo klikněte na položku „Katalog“ a zobrazí se samostatná stránka s každým výrobkem (a potenciálními
variantu produktu) v organizaci katalogového zobrazení s možností třídění podle:guilabel:Produkt
Kategorie a:guilabel:Atributy.

.. obrázek: vytvořit citace / produktový katalog.png
:align:center
:alt: Katalog produktů přístupný prostřednictvím citační smlouvy v aplikaci prodeje Odoo.

Zde jednoduše najděte požadované položky a klikněte na ikonu „Nákupní košík“
tlačítko na kartě produktu a upravte množství, pokud je potřeba. Když budete hotovi, klikněte
Tlačítko „Přejít zpět k citátu“ v horním levém rohu pro návrat do citace.
nově vybrané položky naleznete v záložce „Dodací řádky“.

Pokud má být na citaci více položek uspořádaných lépe, klikněte na tlačítko „Přidat
Vyberte část, zadejte název části a přetáhněte hlavičku části do požadované
umístění mezi položkami v záložce „Dodací lístky“. Hlavička se zobrazí tučně.

Pokud je třeba, klikněte na „Poznámka“ pod konkrétní produktovou řadou.
Tento konkrétní produkt. Poznámka se zobrazuje kurzívou. Poté, pokud je třeba, proveďte přetažení a vložení
poznámku pod požadovanou produktovou řadou.

Pod produktovými řadami jsou tlačítka, na která lze kliknout a aplikovat libovolnou z následujících možností:
:guilabel:'Kód slevy', :guilabel:'Slevové akce', :guilabel:'Sleva' a/nebo :guilabel:'Přidat
přepravy.

.. viz též:
   - :doc:`../products_prices/ewallets_giftcards`
   - :doc:`../produkty_ceny/slevy-na-pravidelne-nakupovani`
   - :doc:`../products_prices/prices/cena`

Volitelné produkty
---------------------

Otevřete záložku „Volitelné produkty“ a vyberte související produkty, které můžete představit zákazníkům.
zákazníkovi, což může vést k nárůstu prodeje.

Příkladem může být situace, kdy zákazník chce koupit auto. Mezi doplňkové produkty by se mohl zařadit
*Závěs na přívěsný vozík*.

.. viz též:
:doc:`nepovinné produkty“

Další informace
--------------

V záložce „Další informace“ jsou různé konfigurace týkající se citací odděleny
čtyři různé sekce: „Prodej“, „Dodání“, „Fakturace“ a
:guilabel:`Sledování“.

.. poznámka::
Některá pole se objevují pouze tehdy, pokud jsou konfigurovány určité nastavení a možnosti.

Prodej
~~~~~~~~~~~~~

V sekci „Prodej“ v záložce „Další informace“ jsou pole specifická pro prodej.
Konfigurovatelné.

.. obrázek: create_quotations/other-info-sales.png
:align:center
:alt:Sekce Prodej v záložce Jiná informace formuláře nabídky v Odoo Sales.

- :guilabel:`Prodejce“: Přidělte prodejce z roletky, který bude spojen s touto
citátu. V tomto poli je vybrán uživatel, který citát původně vytvořil (výchozí hodnota).
- :guilabel:`Prodejní tým“: Přiřaďte konkrétní prodejní tým k tomuto cenovému nabídkám. Pokud vyberete
:guilabel:`Prodavač“ je členem prodejního týmu, který se automaticky vyplní do pole.
- :guilabel:`Společnost“: Vyberte společnost z rozevírací nabídky, se kterou je tato citace spojena
s tímto účtem. Toto pole se zobrazí pouze při práci v prostředí více společností.
- Zaškrtněte políčko „Online podpis“ a požádejte zákazníka o online podpis.
aby objednávku potvrdil. Toto pole se zobrazí pouze v případě, že je zapnuté nastavení „Elektronická podpisová smlouva“.
- Zatrhněte políčko „Platba online“ a do sousedního pole zadejte požadovanou procentuální částku.
pole, požádat zákazníka o online platbu (za ten určený procento z celkové částky)
výši platby (povinné pole, pokud je nastaveno „On-line platba“).
je aktivní.
- :guilabel:`Referenční číslo zákazníka“: Zadejte vlastní referenční číslo pro tento zákazníka.
Referenční identifikátor může obsahovat písmena, číslice nebo jejich kombinace.
- :guilabel:`Štítky“: Přidejte konkrétní štítky k citátu pro lepší organizaci a zvýšenou
přístupnost v aplikaci Sales v Odoo. Můžete přidat více štítků, pokud je to nutné.

Doručovací sekce
~~~~~~~~~~~~~~~~

V sekci „Dodání“ pod záložkou „Ostatní informace“ jsou uvedeny dodací specifika.
poli, která lze konfigurovat.

.. obrázek: create_quotations/other-info-delivery.png
:align:center
:alt:Dodací sekce záložky „Ostatní informace“ objednávkového formuláře v Odoo Sales.

- :guilabel:`Hmotnost při odeslání“: Zobrazuje hmotnost zboží, které je zasíláno. Tento prvek není
modifikovatelné. Hmotnost produktu je konfigurována na jednotlivých formulářích s produkty.
- :guilabel:`Incoterm“: Vyberte předdefinovaný termín pro mezinárodní obchod
obchodní podmínky pro mezinárodní transakce.
- :guilabel:`Místo podle Incoterms“: Pokud se používá Incoterm, zadejte mezinárodní místo
tento obor.
- :guilabel:`Dopravní politika“: Vyberte požadovanou dopravní politiku z roletky. Pokud všechny
přepravce dodá zboží najednou a objednávku dopravy si naplánuje podle největšího produktu.
dodací lhůta. Jinak se vychází z nejkratší dodací lhůty. K dispozici jsou následující možnosti:
:guilabel:`Jakmile to bude možné“ nebo :guilabel:`Když budou všechny produkty připraveny“.
- :guilabel:'Datum doručení': Klikněte do prázdného pole, aby se zobrazila kalendářová lišta.
Vyberte si datum dodání pro zákazníka. Pokud není požadováno konkrétní datum, odkazujte na
:guilabel:`Očekávaný termín“ uvedený vpravo od pole.

Fakturační část
~~~~~~~~~~~~~~~~~

V sekci „Fakturace“ pod záložkou „Další informace“ jsou fakturační specifické
poli, která lze konfigurovat.

.. obrázek: vytvorit_citace/dalsi_informace_fakturace.png
:align:center
:alt:Fakturační část záložky „Další informace“ objednávkového formuláře v Odoo Sales.

- :guilabel:`Daňová pozice“: Vyberte daňovou pozici, která bude použita k přizpůsobení daní a účtům
particular zákazníci nebo objednávky/faktury. Výchozí hodnota pochází od zákazníka. Pokud je
Vyberte v tomto poli a klikněte na ikonu „Obnovení daní“ vedle odkazu.
Ikona se zobrazí a po kliknutí se aktualizují daně pro konkrétního zákazníka a cenovou nabídku.
V okně potvrzení se objeví také.
- :guilabel:`Analytický účet“: Vyberte analytický účet, ke kterému se má tento zákazník/nabídka vztahovat.

Sledovací sekce
~~~~~~~~~~~~~~~~

V sekci „Sledování“ pod záložkou „Další informace“ jsou uvedeny specifické údaje o sledování.
poli, která lze konfigurovat.

.. obrázek: create_quotations/other-info-tracking.png
:align:center
:alt:Sledovací část záložky jiná informace v objednávkovém formuláři v Odoo Sales.

- Zdrojový dokument: Zadejte odkaz na dokument, který vygeneroval
případně objednávka/faktura.
- :guilabel:`Příležitost“: Vyberte konkrétní příležitost (z aplikace CRM) spojenou s tímto
citace, pokud je k dispozici.
- :guilabel:`Kampaň“: Vyberte marketingovou kampaň související s touto citací, pokud je vhodné.
- :guilabel:`Střední úroveň“: Vyberte metodu, jakým způsobem vznikla tato citace (např. *E-mail*), pokud
aplikovatelné.
- Zdroj: Vyberte zdroj odkazu použitého k vytvoření této citace (například
Facebook, pokud je k dispozici.

.. viz též:


Tabulka poznámek
---------

V záložce „Poznámky“ v okně pro citaci zadejte jakékoli konkrétní poznámky k
citace a/nebo zákazník, pokud je to požadováno.

Posílání a potvrzení cenových nabídek
=================================

Jakmile jsou všechny potřebné pole a záložky nakonfigurovány, je čas poslat cenovou nabídku.
Zákazníkovi k potvrzení. Po potvrzení se z nabídky stává oficiální objednávka.

Na horní části formuláře je řada tlačítek:

- :guilabel:`Odeslat e-mailem“: Když je kliknuté, objeví se okno s názvem zákazníka a
e-mailovou adresu do pole „Příjemci“ a citaci (a referenční identifikátor) do pole
:guilabel:`Předmět` pole a stručný výchozí text v těle e-mailu, který může být
pokud je třeba.

Pod ní je přiložen soubor ve formátu PDF s citací. Kliknutím na tlačítko „Odeslat“ odesíláte
cituje nabídku e-mailem zákazníkovi, aby si ji mohl přečíst a potvrdit.
- Tlačítko „Vystavit proforma fakturu“ se zobrazí pouze v případě, že je vyplněna položka „Proforma faktura“.
je zapnutý. Když na něj kliknete, objeví se okno s názvem zákazníka a e-mailovou adresou.
adresu v poli „Příjemce“ a fakturu (a referenční identifikátor) ve formě proforma v poli
:guilabel:`Předmět` pole a stručný výchozí text v těle e-mailu, který může být
pokud je třeba.

Pod ní je přiložen soubor ve formátu PDF s citací. Kliknutím na tlačítko „Odeslat“ odesíláte
cituje nabídku e-mailem zákazníkovi, aby si ji mohl přečíst a potvrdit.
- :guilabel:'Potvrdit': Když je tlačítko potvrzení kliknuté, citát se potvrdí a stav se změní na
:guilabel:`Prodejní objednávka“.
- :guilabel:`Předběžný náhled“: Když je kliknuté, Odoo zobrazí náhled cenové nabídky, kterou vidí zákazník.
Přihlásí se do svého zákaznického portálu a kliknou na ikonku „Zpět k editaci“.
v horní části náhledu stránky, modrém pruhu, klikněte na odkaz pro návrat do formuláře s citací.
- :cancellabel:Zrušit": Kliknutím je citát zrušen.

.. poznámka::
Pokud je nastavení „Zakázka potvrzena prodejem“ zapnuté, objednávka se stává :guilabel:`Zamčenou` a
Je uvedena na prodejním formuláři.

V tuto chvíli byla cenová nabídka potvrzena, převedena na objednávku prodeje a je nyní připravená k
a zaplacené.

Více informací o fakturaci naleznete v souboru :doc:`Fakturace na základě dodaného nebo objednaného zboží.
množství <../fakturace/fakturační politika>

.. viz též:
   - :doc:`citát_šablona“
   - :doc:`termín“
   - :doc:`get_signature_to_validate“
   - :doc:`get_paid_to_validate“
   - :doc:`pdf_quote_builder“
   - :doc:`../fakturace/proforma`
