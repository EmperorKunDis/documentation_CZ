=============================
Dvoufázové potvrzení přijetí a dodání
=============================

.. |PO| nahradit za: abbr: PO (příkaz k nákupu)
.. |SO| nahradit za: :abbr:`SO (objednávka na prodej)`
.. |DO| nahradit:: :abbr:`DO (Dodací příkaz)`
.. |RfQ| nahradit za: zkratku `RfQ (Request for Quotation)`

V závislosti na potřebách společnosti může být příjem a odesílání produktů do skladu nebo z něj.
vyžadují vícekrokové operace. V Odoo *Skladu* lze tento proces uskutečnit pomocí *Vícekrokových tras*.

V případě dvoufázového procesu přijímání zboží je zboží přijato v oblasti pro příjem a poté převedeno do skladu.
Tento typ procesu pro příchozí zásilky může být užitečný pro sklady s konkrétním uskladněním
místo, jako jsou například mrazáky nebo chladničky, uzavřené prostory s kódem, speciální regály a police.

Produkty lze třídit podle místa uložení a zaměstnanci mohou skladovat všechny
produktů určených pro konkrétní lokalitu. Produkty nejsou k dispozici pro další zpracování
až do chvíle, než budou převedeny na účet.

V procesu dvoufázového dodání jsou produkty nejprve vyzvednuty z jejich příslušného místa v
skladu, pak převedena na výstupní místo a následně odeslána zákazníkovi.

Toto může být pro společnosti používající systém „první dovnitř, první ven“ (FIFO) nebo „poslední dovnitř, první ven“ (LIFO) výhodné.
(FIFO), nebo „první vyřazený, první vypuštěný“ (FEFO).

.. tip::
Při příchozích a odchozích dodávkách není nutné nastavovat stejný počet kroků.

Například lze nastavit sklad tak, aby se do něj zboží dodávalo ve dvou krocích.
(vstupy + zásoby) a dodávány ve třech krocích (vybrat, zabalit, odeslat).

Konfigurace
=============

V Odoo *Skladu* jsou oba příchody i odeslání nakonfigurovány tak, že se zpracovávají v jednom kroku.
Výchozí nastavení. Chcete-li změnit tyto nastavení, musí být zapnutá funkce *Multistep Routes*.

Pro umožnění funkce „Vícekrokové trasy“ přejděte do sekce:
Nastavení“. V části „Sklad“ zaškrtněte políčko vedle „Multikrokový
Zvolte možnost „Uložit trasu“ a klikněte na tlačítko „Uložit“. Tím se také aktivuje „Soubory ke stažení“
feature.

.. obrázek: faktury_doručení_ve_dvou_krocích/faktury-doruceni-ve-dvou-krocich-nastaveni.png
:align:center
:alt:V nastavení aplikace Sklad zapněte funkci vícefázových tras.

Dále si nakonfigurujte sklad pro dvoufázové příjmy a dodávky.
Vyberte v nabídce aplikace „Skladovací zásoby“ – „Konfigurace“ – „Sklady“ sklad, který chcete upravit.

V záložce „Konfigurace skladu“ nastavte „Příchozí zásilky“ na
„Přijmout zboží do vstupu a poté sklad (2 kroky)“ a „Výdejové faktury“.
:guilabel:„Odeslat zboží a poté doručit (2 kroky)“.

.. obrázek: faktury_doručení_v_dvou_krocích/faktury_doručení_v_dvou_krocích_zásilky.png
:align:center
:alt:Příjmy a výstupy zboží nastavit na dvoukrokové skladové formuláře.

.. poznámka::
Výběrem dvoufázových příjmů a dodávek se automaticky vytvoří nové položky *Příjem* a *Výdej*.
skladovací místa v databázi s názvy „Vstup“ a „Výstup“.

Chcete-li přejmenovat nebo upravit tyto položky, přejděte do nabídky :menuselection:`Inventář aplikace --> Konfigurace
--> Lokality a vyberte požadovanou lokalitu.

Na položce „Název místa“ změňte :guilabel:`Název místa` a udělejte další potřebné úpravy.
změny.

Zadání přijaté faktury ve dvou krocích (vstup + zásoba)
============================================

Pokud jsou produkty přijímány ve dvou krocích, nejprve se přesouvají z místa dodavatele na vstup
místo. Poté se přesouvají z vstupního místa do skladu na skladovém místě v databázi
ověření objednávky (PO) a následný interní převod.

Vytvořte objednávku k nákupu
---------------------

Vytvořit PO. Přejděte do nabídky „Nákupní aplikace“ a klikněte na „Nový“.
otevře prázdný formulář požadavku na cenovou nabídku (RfQ).

Do pole „Dodavatel“ zadejte dodavatele. Pak vyplňte různá pole v RfQ, jako
nutné.

.. obrázek: faktury_doručení_ve_dvou_krocích/faktury_doručení_ve_dvou_krocích_nové_poptávky.png
:align:center
:alt:Vyplnil novou žádost o cenovou nabídku u dodavatele.

Pod záložkou „Produkty“ klikněte na „Přidat produkt“ a vyberte produkt, který chcete přidat.
RfQ.

Jakmile bude připravena objednávka, klikněte na „Zadat objednávku“. Tím se objednávka přesune do stavu „Nákupní objednávka“
stáž.

Jakmile je potvrzena platba, se v horní části formuláře objeví tlačítko „Potvrzení o přijetí“.
Kliknutím na chytrý tlačítko se otevře formulář pro vydání skladového dokladu (WH/IN).

.. obrázek: faktury_doručení_ve_dvou_krocích/faktury-doruceni-ve-dvou-krocich-smart-button.png
:align:center
:alt:Tlačítko pro doručení objednávky, která byla schválena.

.. tip::
Pro podniky s více sklady, které mají odlišné konfigurace kroků, je
:guilabel:"Dodání" pole na formuláři PO **musí být** správně nastaveno jako vstupní
místo, které je spojeno s dvoufázovým skladem.

Toho lze dosáhnout výběrem skladu z rozbalovací nabídky, která obsahuje položku „Příjmy“.
na konci jména.

Příjem dokumentu
---------------

Za účelem přijetí zboží do skladu lze ze záznamu o vydání dokladu o převzetí zboží vyčíst produkty objednané zákazníkem.
produktu, klikněte na tlačítko „Zkontrolovat“. Jakmile je produkt ověřen, přesune se do složky „Dokončeno“
stupně a produkty se přesouvají na místo :guilabel:`WH/Input`.

.. obrázek:: faktury_doručení_ve_dvou_krocích/faktury_doručení_ve_dvou_krocích_příjemce.png
:align:center
:alt:Formulář pro vystavení faktury za zboží objednané u dodavatele.

Klikněte zpět na |PO| (přes chléb kroků nahoře formuláře) a zobrazte si formulář |PO|.
sérii produktů, množství v sloupci „Přijato“ odpovídá objednanému.
:guilabel:`Množství“.

Přesun v rámci procesu
-------------------------

Jakmile je faktura ověřena, vytvoří se interní převod a bude připraven k zpracování.

Pro zobrazení vnitřního převodu se přesuňte do aplikace „Sklad“, a najděte
Kartu úkolu „Vnitřní převody“.

Klikněte na tlačítko „Proces“ v kartě úkolu, abyste zobrazili seznam všech interních procesů.
převody k zpracování a vybrat převod spojený s již dříve ověřenou fakturou.

Když bude připraveno, klikněte na tlačítko „Potvrdit“ a dokončete převod. Produkt se poté přesune
z „WH/Vstup“ na „WH/Zásoby“.

Jakmile je převod ověřen, produkty jsou zahrnuty do zásob a k dispozici pro zákazníky.
dodávky nebo výrobní objednávky.

.. obrázek: faktury_doručení_ve_dvou_krocích/faktury_doručení_ve_dvou_krocích_vnitřní_převod.png
:align:center
:alt:Formulář pro vnitropodnikovou přepravu zboží objednaného u dodavatele.

... skladování a přijímání zboží, dvoufázové dodávky:

Dodání procesu objednávky ve dvou krocích (vybrat + odeslat).
=================================================

Pokud jsou produkty dodávány ve dvou krocích, přecházejí z skladového zásobení do výstupní lokality.
Poté se přesunou z výstupního místa do databáze s adresami zákazníků po ověření
dodací objednávka (DO) a následně expediční objednávka (EO).

Vytvořit prodejní objednávku
------------------

Vytvořit SO lze tak, že se přesunete do aplikace „Prodej“ a klikněte na „Nový“.
otevře prázdný prodejní formulář.

Přidejte zákazníka do pole „Zákazník“ a pak vyplňte různé položky v sekci prodeje.
citace v případě potřeby.

.. obrázek: faktury_doručení_ve_dvou_krocích/faktury_doručení_ve_dvou_krocích_nový_objednávkový_list.png
:align:center
:alt:Vytvořil novou objednávku.

Pod záložkou „Řádky objednávky“ klikněte na „Přidat produkt“, vyberte produkt, který chcete přidat
do objednávky na prodej.

Jakmile je připravena, klikněte na „Potvrdit“. To přesune citaci do „Objednávky prodeje“
stáž.

Jakmile je potvrzeno, objeví se nahoře na formuláři tlačítko „Doručení“, které má ikony pro různé způsoby doručení.
Kliknutím na chytrý tlačítko se otevře formulář pro expedici z skladu (WH/OUT).

.. obrázek: faktury_doručení_ve_dvou_krocích/faktury_doručení_ve_dvou_krocích_tlačítko_pro_doručení.png
:align:center
:alt:Tlačítko pro doručení na potvrzené objednávce.

Picking procesů
---------------

Jakmile je potvrzena prodejní objednávka, vytvoří se vyskladňovací objednávka a bude připravená k zpracování.

K dokončení sběru přejděte do aplikace „Sklad“ a najděte položku „Sběr“.
úkolovou kartu na panelu „Přehled zásob“. Jako alternativu lze použít také pořadí vyskladňování.
je přístupný prostřednictvím tlačítka „Dodání“ v horní části formuláře objednávky.

Na stránce „Přehled zásob“ klikněte na tlačítko „Zpracovat“.
Klikněte na kartu úkolu „Pick“. To zobrazí seznam všech vybraných položek, které je třeba zpracovat.

Klikněte na operace vyskladnění spojenou s objednávkou, abyste zobrazili vyskladňování.
pořádku.

.. obrázek: faktury_doručení_v_dvou_krocích/faktury_doručení_v_dvou_krocích_vyzvednutí_formulář.png
:align:center
:alt: Vybírání objednávky na produkty zahrnuté v prodejní objednávce.

Manuálně nastavte množství změnou hodnoty v sloupci „Množství“.
hodnota v sloupci „Požadavek“.

Po dokončení klikněte na tlačítko „Potvrdit“ a přesuňte produkt.
:guilabel:`WH/Stock“ na „WH/Output.“

Dodání procesu
----------------

Jakmile je vybraná objednávka potvrzena, vytvoří se dodací příkaz, který je připraven k zpracování. Po kliknutí na
Kliknutím na tlačítko „Dodání“ v objednávce zobrazíte nově vytvořenou dodací objednávku.

Alternativně k zobrazení objednávky dodání se vraťte na stránku „Přehled zásob“,
Přes „kousky chleba“ a najít kartu úkolu „Objednávka“.

Klikněte na tlačítko „Zpracovat“ v kartě úkolu, abyste zobrazili seznam všech objednávek.
je zpracovat a vybrat objednávku spojenou s již dříve ověřeným výběrem.

.. obrázek: faktury_dodání_ve_dvou_krocích/faktury_dodání_ve_dvou_krocích_objednávka_na_dodání.png
:align:center
:alt:Formulář pro objednávku produktů na základě požadavků zákazníka.

Aby bylo možné dodat produkty, změňte hodnotu v poli „Množství“ tak, aby odpovídalo objednanému
množství v poli „Požadavky“.

Jakmile je připraveno, klikněte na tlačítko „Zkontrolovat“. Jakmile bude kontrola dokončena, objednávka se přesune do
:guilabel:`Dokončeno“ fáze.

.. viz též:
:doc:`/denní operace“
