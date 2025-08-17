=================
Připojit tiskárnu
=================

Instalace tiskárny je velmi snadná. Tiskárna může být použita k tisku účtenek.
štítky, objednávky nebo dokonce zprávy z různých aplikací Odoo. Dále lze
při výrobním procesu přiřazen jako akce na spoušť nebo kvalitě
kontrolní bod nebo kvalitativní kontrola.

.. varování:
Jediný způsob, jak připojit tiskárnu přímo k databázi Odoo, je použití IoT.
systém. Bez internetu věcí lze tisknout i nadále, ale je řízen přes tiskárnu
sám o sobě, což není doporučovaný proces.

Připojení
==========

Systémy IoT podporují tiskárny připojené pomocí USB, sítě nebo Bluetooth.
„Podporované tiskárny <https://www.odoo.com/page/iot-hardware>“ jsou detekovány automaticky a
objevit se v seznamu zařízení aplikace IoT.

.. obrázek: tiskárna/zjištěná tiskárna.png
:alt: Tiskárna, jak by se zobrazila v seznamu zařízení aplikace pro internet věcí.

.. poznámka::
Tiskárny mohou trvat až dvě minuty, než se objeví v seznamu zařízení aplikace IoT :guilabel:`Devices`.

Připojit tiskárnu
==============

Připojit pracovní příkazy k tiskárně
-----------------------------

Pracovní příkazy lze propojit s tiskárnami, přes kontrolní bod kvality, aby se na nich vytvořily štítky.
Vyráběné výrobky.

V aplikaci „Kvalita“ lze zařízení nastavit na
kontrolní bod kvality. Chcete-li tak učinit, přejděte na:
Body a otevřete požadovaný bod kontroly.

.. důležité::
Kvalitativní kontrola musí být připojena k výrobnímu procesu a operaci objednávky.
pole před políčkem :guilabel:`Typ` umožňuje volbu :guilabel:`Tisk štítku`.
vybráno.

Zde upravte kontrolní bod vybráním pole „Typ“ a výběrem
Vyberte možnost „Tisk štítku“ z nabídky možností. Tím se objeví „Zařízení“.
políčko, kde lze vybrat připojené zařízení.

Tiskárna je nyní možné používat s vybraným kontrolním bodem kvality. Když se kvalitativní bod
je dosaženo během výrobního procesu, databáze nabízí možnost tisknout štítky pro
Konkrétní produkt.

.. tip::
Kontrolní body kvality lze také zobrazit pomocí navigace na :menuselection:`IoT -->
Devices“, pak vyberte zařízení. Přejděte na kartu „Kontrolní body kvality“ a přidejte je
do zařízení.

.. poznámka::
Na kvalitativní kontrolu se používá tzv.
</aplikace/inventar-a-mrp/kvalita/kvalitní řízení/kontroly kvality>
:guilabel:`Typ“ kontroly může být také nastaven na „Tisk etikety“.

.. viz též:
   - :doc:`/aplikace/skladové hospodářství a výroba/kvalita/kontrola kvality/kontrolní body kvality“
   - :doc:`/aplikace/sklad/kvalita/kvalitní řízení/kvalitní upozornění`

... _iot/link-printer:

Link se připojuje k tiskárně
-------------------------

Je možné spojit typy zpráv s konkrétním tiskárnám. Pro to:

#Přejděte na „IoT -> Zařízení“ a vyberte požadovaný tiskárnu.
#Přejděte na záložku „Zprávy tiskárny“ a klikněte na „Přidat řádek“.
#V okně, které se otevře, vyberte typy zpráv, ke kterým má být tiskárna připojena, a klikněte
:guilabel:`Vybrat“.

.. obrázek:: tiskárna/zprávy_o_tiskárně.png
:alt:Seznam zpráv přidělených tiskárně v aplikaci Internet věcí.

.. tip::
Zprávy lze také nakonfigurovat tak, že zapnete režim vývojáře:ref:`<developer-mode>`, a poté
do:menuvolba:Nastavení --> Technické --> Zprávy. Vyberte požadovanou zprávu ze seznamu
a nastavte zařízení pro internet věcí.

Při prvním výběru pro tisk spojeného hlášení se zobrazí okno „Vybrat tiskárnu“
zobrazí se. Zaškrtněte políčko vedle správného tiskárny pro zprávu a klikněte na:guilabel:`Tisknout`.
V tu chvíli je zpráva spojena s tiskárnou.

Vyčistit mezipaměť tiskárny
~~~~~~~~~~~~~~~~~~~~~~~~~~

Po připojení tiskárny k tisku zprávy se nastavení uloží do mezipaměti prohlížeče.
uživatel může mít v mezipaměti různé zařízení pro různé zprávy podle typu zařízení.
slouží k přístupu do Odoo, což také znamená, že různí uživatelé mohou mít automaticky vytištěný report
různé tiskárny podle jejich preferencí.

Pro odpojení zprávy od tiskárny přejděte na: „IoT --> Konfigurace --> Obnovení
Spojené tiskárny“. Tato funkce vytváří seznam zpráv, které jsou spojeny s aktuální tiskárnou.
zařízení. Klikněte na tlačítko „Odpojit“ vedle každého hlášení, abyste odstranili odkaz.

.. důležité::
Toto kroky **jen** zabrání automatickému tisku zprávy na uvedený tiskárny.
aktuálním prohlížečem. Zpráva je stále:odkazovaná na zařízení, pod
záložce „Zprávy tiskárny“.

.. obrázek: tiskárna/čisté_zprávy.png
:alt: Seznam zpráv, které jsou nyní spojeny s tiskárnou v aplikaci Internet věcí.

.. viz též:
:doc:`Tisk objednávek POS <../../../sales/point_of_sale/restaurant/kitchen_printing>`

Potenciální problémy
================

Tiskárna není detekována
---------------------------

Pokud tiskárna není uvedena v seznamu zařízení, přejděte na stránku :ref:`IoT boxu <iot/iot-box/homepage>`.
nebo na domovské stránce virtuálních Windows IoT, klikněte na „Zobrazit“
sekci „Zařízení“ a ujistěte se, že tiskárna je uvedena.

Pokud se tiskárna nezobrazí na domovské stránce systému Internet věcí, klikněte na „Server tiskárny“ a
„Správa“ a „Přidat tiskárnu“. Pokud tiskárna není v seznamu, je
nepravděpodobně není správně připojený.

Tiskárna vytváří náhodný text
-------------------------------

Pro většinu tiskáren by měl být správný ovladač detekován a vybrán automaticky.
V některých případech může být automatické detekční zařízení nedostatečné a pokud není nalezen žádný řidič,
Tiskárna může vytisknout náhodné znaky.

Řešením je ruční výběr odpovídajícího ovladače. Na domovské stránce systému IoT klikněte
Poté vyberte tiskárnu v seznamu.
V nabídce „Administrace“ klikněte na „Upravit tiskárnu“. Postupujte podle pokynů
a vyberte značku a model tiskárny.

.. obrázek: tiskárna/upravit-tiskárnu.png
:scale: 75 %
:alt:Upravte tiskárnu připojenou k systému IoT.

.. poznámka::
Epson tiskárny účtenek a etiketovací tiskárny Zebra nepotřebují ovladače k práci. Ujistěte se, že je nainstalovaný správný ovladač.
je zvolen pro tiskárny s tímto ovladačem.

Tiskárna je detekována, ale není správně rozpoznána
-------------------------------------------------------

Pokud systém Odoo a IoT nepoznají tiskárnu správně, přejděte na: menu:IoT
→ zařízení“, klikněte na kartu zařízení a nastavte pole „Podtyp“ na
vhodné možnosti: „Tiskárna účtenek“, „Etiketovací tiskárna“ nebo „Kancelářská tiskárna“.
Tiskárna.

Epson konfigurační speciální případ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Většina tiskáren Epson podporuje tisk účtenek pomocí příkazu „GS v 0“ v Odoo Point of Sale.
Následující modely tiskáren Epson však tuto příkazovou řádku nepodporují:

- TM-U220
- TM-U230
- TM-P60
- TMP-P60II

Tento problém obejdete tak, že nastavíte tiskárnu na používání příkazu „ESC*“.

Nejprve zkontrolujte webové stránky společnosti Epson pro kompatibilitu obou modelů „GS v 0
<https://download4.epson.biz/sec_pubs/pos/reference_en/escpos/gs_lv_0.html> a „*
<http://www.epson.cz/cs/podpora/technicke-informace/referencni-dokumenty/escpos/esc_asterisk.html>

Pokud tiskárna není kompatibilní s „GS v 0“, ale podporuje „ESC *“, nastavte systém IoT tak, aby používal
Komandu „ESC *“ takto:

#Připojte se k:
<iot/windows-iot/homepage> domovská stránka.
#Klikněte na tlačítko „Tiskový server“, pak klikněte na „Administraci“ v CUPS.
stránka.
#Klikněte na tlačítko „Přidat tiskárnu“ v sekci „Tiskárny“. Vyberte tiskárnu a klikněte
:guilabel:`Pokračovat“.

.......
Pokud ještě není jasné o jakého tiskaře se jedná, postupujte takto:

      #Pozorně si prohlédněte seznam tiskáren na stránce CUPS.
      #Zapněte tiskárnu a obnovte stránku.
      #Srovnejte rozdíl s prvním seznamem a zjistěte, který tiskárna zmizela.
      #Zapněte tiskárnu a znovu načtěte stránku.
      #Zkontrolujte seznam ještě jednou, abyste zjistili, zda tiskárna znovu nevyskočí.
      #Jedná se o tiskárnu, která zmizela a znovu se objevila v seznamu dostupných tiskáren.
tiskárna, která je v daném okamžiku vypnutá. Může být označena jako „Neznámý“ pod „Veřejné tiskárny“.

#Vyberte stránku „Přidat tiskárnu“ a zadejte název tiskárny pomocí následujícího
konvence: <název tiskárny>__IMC_<parametr 1>_<parametr 2>_..._<parametr n>__, kde:

   - Název tiskárny je název tiskárny. Může obsahovat jakýkoliv znak s výjimkou znaku podtržítka, lomítka, křížku nebo mezery.
(mezera).
   - „IMC“ znamená „režim obrazového sloupce“ (zjednodušený název pro „ESC *“).
   - „param_1“: To je konkrétní parametr:

     - `SCALE<X>“: Poměr stran obrázku. Hodnota X musí být celé číslo
popisující procento stupnice, které by se mělo použít. Například „100“ je původní velikost.
„50“ je poloviční velikost a „200“ je dvojnásobná velikost.
     - `LDV`: *nízká hustota vertikálně* (bude nastaveno na *vysokou hustotu vertikálně*, pokud není specifikováno).
     - `LDH`: *nízká hustota horizontální* (bude nastavena na *vysokou hustotu horizontální* pokud není specifikována).

.. poznámka::
        - Parametry hustoty mohou být konfigurovány v určitém způsobu, podle
tiskárna.
        - Při odkazu na dokumentaci „Epson ESC*“ (<https://download4.epson.biz/sec_pubs/pos/reference_en/escpos/esc_asterisk.html>)
aby zjistil, jestli tiskárna vyžaduje nastavení těchto parametrů.

... příklad::
Následující příklady ukazují správné a nesprávné formátování jména:

Formátování jmen:

       - „EpsonTMm30II_IMC“
       - „Epson TM-U220 IMC LDV Scale80“

Nesprávné formátování názvu (toto nezabrání tisku, ale výsledek nemusí být takový, jaký chcete)
(očekávaný tiskový výstup):

       - „Epson TM-m30II“: Název nemůže obsahovat mezery.
       - „EpsonTM m30 II“: Samotný název je správně, ale nebude používat „ESC *“.
       - „EpsonTMm30II__IMC“: Tento název chybí koncovka „__“.
       - „EpsonTMm30II__IMC_XDV__“: Parametr „XDV“ neodpovídá žádnému existujícímu parametru.
       - „EpsonTMm30II__IMC_SCALE__“: Chybí hodnota měřítka.

#Jakmile je tiskárna označena správným názvem podle příslušného konvenčního jména, klikněte
:guilabel:`Pokračovat“.
#Nastavte hodnotu :guilabel:`Make` na :guilabel:`Raw“ a hodnotu :guilabel:`Model“ na
:guilabel:`Nebalená fronta (en)`
#Klikněte na tlačítko „Přidat tiskárnu“. Pokud byly všechny kroky provedeny správně, stránka by měla přesměrovat na
:guilabel:`Bannery“ stránka.
#Připojte se k síti Wi-Fi, počkejte pár minut na detekci tiskárny a synchronizaci s serverem Odoo.
#Přejděte do části „Nastavení terminálu“ a vyberte svůj terminál nebo klikněte na
tlačítko vertikální elipsy (:guilabel:`⋮`) na kartě POS a klikněte na „Upravit“. Vyhledejte
do sekce „Připojená zařízení“, zapněte „IoT Box“ a vyberte tiskárnu
v poli „Tiskárna účtenek“ a klikněte na „Uložit“.

.. poznámka::
Pokud tiskárna nebyla správně nastavena (např. stále vytiskne náhodný text nebo tiskne
Pokud je účtenka příliš velká nebo příliš malá, nelze ji upravit prostřednictvím názvu tiskárny v CUPS.
Vyberte nový tiskárny s upravenými parametry a postupujte podle kroků
výše.

..spoiler::
Příklad

Následující je příklad postupu při odstraňování závad u tiskárny typu TM-U220B pomocí
„ESC *“ příkaz. Příklad správně tisknutého účtenky je uveden na obrázku níže.
v důsledku správného formátování (teoreticky):

.. obrázek:: tiskárna/příklad_faktury.png
:skalka: 60 %
:alt: Správně formátovaný obrázek účtenky z ukázkové databáze.

Tisk bez řádného formátování nefunguje hned, protože TM-U220B
Tiskárna daného typu nepodporuje příkaz „GS v 0“. Namísto toho se na papír vytištějí náhodná písmena:

.... obrázek:: tiskárna/výpis_tisknutých_písmen.png
:skalka: 60 %
:alt:Tisková papírová páska s náhodně vypadajícími znaky.

Pro správné nastavení formátování pro tiskárnu Epson TM-U220B postupujte následovně:

   #Po kontrole webových stránek společnosti Epson pro kompatibilitu s oběma modely „GS v0
<https://download4.epson.biz/sec_pubs/pos/reference_en/escpos/gs_lv_0.html> a „ESC *
příkazů typu _<http://download4.epson.biz/sec_pubs/pos/reference_en/escpos/esc_asterisk.html>_.
tiskárna TM-U220B je skutečně neslučitelná s „GS v 0“, ale podporuje „ESC *“.

.. obrázek:: tiskárna/epson-kompatibilita-srovnání.png
:alt:Epsonovská kompatibilita z webu Epson.

   #Když přidáte tiskárnu, CUPS zobrazí seznam dostupných tiskáren:

.. obrázek:: tiskárna/přidat_tiskárnu.png
:skalka: 75 %
:alt: Nastavení tiskárny, přidat výběr tiskárny.

V tomto případě je tiskárna připojena přes USB a není součástí sítě.
:guilabel:`Nalezené síťové tiskárny“. Místo toho je pravděpodobně součástí :guilabel:`Neznámých“
výběr pod:guilabel:'Veřejné tiskárny'. Po odpojení kabelu USB tiskárny z IoT
systému a obnovením stránky zmizí tiskárna „Neznámá“. Po připojení se zobrazí.
pokud se vrátíte zpět, tiskárna se znovu objeví.

   #Pro pojmenování konvence, protože tiskárna musí používat příkaz „ESC *“, je
je nutné přidat __IMC__.

.. obrázek: tiskárna/epson-tm-u220-specifikace.png
:alt:Specifikace tiskárny Epson TM-U220 na webu výrobce.

Pro tento konkrétní model (TM-U220) by měl být „m“ roven nule nebo jedné.
:guilabel:`Popis produktu“ v sekci „Epson ESC * webové stránky
<https://download4.epson.biz/sec_pubs/pos/reference_en/escpos/esc_asterisk.html>, kde je znak „m“
hodnoty mohou být 0, 1, 32 nebo 33. V tomto případě tedy nelze použít hodnotu 32 nebo 33
(jinak se tisknou náhodná písmena).

Tabulka obsahuje čísla 32 a 33, obě se vyskytují v případě, že je zadáno číslo
bitů pro vertikální data je nastaven na 24, tedy má vysokou vertikální hustotu. V případě
pro nastavení tiskárny Epson TM-U220 bude nutné nastavit hodnotu *nízké vertikální hustoty*.
tato tiskárna modelu nepodporuje *Vysokou vertikální hustotu* pro příkaz „ESC *“.

Chcete-li přidat parametr „nízká vertikální hustota“, přidejte do názvu konvence parametr LDV.

.. obrázek: tiskárna/přidat_tiskárnu_zaplněné.png
:alt:Přidejte parametr *nízká vertikální hustota* (LDV).

   #Klikněte na tlačítko „Pokračovat“. Nastavte hodnotu „Vyrobit“ na „Rohož“
a hodnotu :guilabel:`Model` nastavit na :guilabel:`Raw Queue (en)`

.. obrázek: tiskárna/přidat_tiskárnu_přidat.png
:alt: Specifikace tiskárny Epson TM-U220 na webu výrobce.

Pokud se však pokusíte tisknout s názvem „EpsonTMU220B__IMC_LDV__“, bude to
pokladní doklad je vytisknut, ale je příliš velký a přesahuje okraj. Chcete-li tento problém vyřešit, přidejte nový
tiskárna (a konvence pojmenování) s parametrem „SCALE<X>“ pro přizpůsobení velikosti účtenky.

Například zde:

... seznam-tabulka::
:hlavičky: 1

         * -Název tiskárny
           - „EpsonTMU220B__IMC_LDV__“
           - „EpsonTMU220B__IMC_LDV_SCALE75__“
           - „EpsonTMU220B__IMC_LDV_LDH__“
           - „EpsonTMU220B__IMC_LDV_LDH_SCALE35__“
         * .. obrázek:: tiskárna_příjemka_příklad.png
:alt: Příklad formátu faktury.
           - .. obrázek: tiskárna/tm-u220-ldv.png
:alt: Formát účtenky s názvovou konvencí: EpsonTMU220B__IMC_LDV__.
           - .. obrázek:: tiskárna/tm-u220-ldv-scale75.png
:alt: Formát účtenky s názvovou konvencí: EpsonTMU220B__IMC_LDV_SCALE75__.
           - .. obrázek:: tiskárna/tm-u220-ldv-hdv.png
:alt: Formát účtenky s názvovou konvencí: EpsonTMU220B__IMC_LDV_LDH__.
           - .. obrázek: tiskárna/tm-u220-ldv-hdv-scale35.png
:alt: Formát účtenky s názvovou konvencí: EpsonTMU220B__IMC_LDV_LDH_SCALE35__.

Tiskárna štítků DYMO LabelWriter má problém
----------------------------

Dymo LabelWriter má známou chybu při tisku s IoT systémy. Server OpenPrinting CUPS
Instaluje tiskárnu pomocí řešení Local RAW Printer. Chcete-li vytisknout cokoliv, musíte
Ve správci zařízení je potřeba nastavit pole „Typ a model“ na odkazující řidiče, pokud se chcete při používání
zařízení.

Dále je nutné přidat nový tiskárnu, aby se snížil zpoždění při tisku po aktualizaci.
Řidič.

.. důležité::
DYMO LabelWriter 450 DUO je doporučený tiskárnou DYMO pro použití s Odoo a IoT.
systémů. Toto zařízení kombinuje dva tiskárny: etiketovou tiskárnu a páskovou tiskárnu. Při konfiguraci
následujících procesů je nezbytné zvolit správný model (buď DYMO LabelWriter 450
DUO Label (angl.) nebo DYMO LabelWriter 450 DUO Tape (angl.). Pro zachování konzistence jsou následující procesy
:Popisuje kroky konfigurace pro tiskárnu štítků DYMO LabelWriter 450 DUO Label (en). Upravte model
v případě potřeby.

.. _tiskárna/DYMO/aktualizace ovladačů:

Tiskárna štítků DYMO LabelWriter nefunguje
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pokud tiskárna DYMO LabelWriter nefunguje správně, nainstalujte nový ovladač:

#Přejděte na domovskou stránku systému Internet věcí a klikněte na „Tiskový server“.
Konzole OpenPrinting CUPS.
#Klikněte na nabídku „Tiskárny“ v horním menu a poté klikněte na tiskárnu v seznamu.
#Vyberte možnost „Údržba“ v prvním rolovacím seznamu.
#Vyberte položku „Upravit tiskárnu“ v druhém rozevíracím seznamu.

.. obrázek: tiskárna/hlavní-změnit.png
:alt:Upravte značku a model DYMO LabelWriter. Vyberte položku údržby a úprav.
menu zvýrazněny.

#Vyberte konkrétní síťovou konektivitu/tiskárnu, na které se má provést změna.
klikněte na tlačítko „Pokračovat“.
#Na další stránce klikněte na tlačítko „Pokračovat“, poté vyberte možnost DYMO.
:guilabel:`Vytvořit“ seznam.
#Klikněte na tlačítko „Pokračovat“ a nastavte model na „DYMO LabelWriter 450“.
DUO Label (nebo jakýkoliv jiný tiskárna štítků DYMO).
#Klikněte na tlačítko „Upravit tiskárnu“ a nastavte nový ovladač; objeví se potvrzovací stránka.
#Klikněte na „Tiskárny“ v horním menu. Všechny tiskárny nainstalované na OpenPrinting CUPS
server se objeví včetně nově aktualizovaného :guilabel:`DYMO LabelWriter 450 DUO Label` (nebo
ať už je použitý jakýkoli typ tiskárny DYMO.
#Klikněte na nový tiskárnu a poté klikněte na položku „Údržba“ z nabídky.
Vyberte možnost „Tisk zkušební etikety“ pro tisk zkušební etikety. Zkušební etiketa se vytiskne po několika
pokud aktualizace ovladače byla úspěšná.

Pro snížení této prodlevy přidejte nový tiskárnu podle níže uvedených kroků.

DYMO LabelWriter tisková prodleva
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::
Pokud tiskárna štítků DYMO LabelWriter 450 DUO nefunguje vůbec nebo není rozpoznána (např.
Pokud má zařízení (jako např. RAW driver typu) pak je třeba aktualizovat ovladače na zařízení.
<tiskárna/dymo/aktualizovat_ovladače>.

K vyřešení problému s prodlevou po změně řidiče je nutné tiskárnu znovu nainstalovat:

#Přejděte na domovskou stránku systému Internet věcí a klikněte na „Tiskový server“.
Konzole OpenPrinting CUPS.
#Klikněte na položku „Správa“ v horním menu, pak klikněte na „Přidat tiskárnu“.
#Na další stránce v sekci „Veřejné tiskárny“ vyberte možnost „DYMO“.
LabelWriter 450 DUO Label (DYMO LabelWriter 450 DUO Label) (nebo jakýkoliv jiný tiskárny značky DYMO).
jejíž tiskárna je již předinstalovaná, klikněte na „Pokračovat“.

.. obrázek:: tiskárna/lokální_tiskárna.png
:alt:Přidat tiskárnu na OpenPrinting CUPS s DYMO LabelWriter 450 DUO
zvýrazněny.

#Na další obrazovce aktualizujte pole „Jméno“ na něco snadno identifikovatelného, protože
originální tiskárna zůstane v seznamu. Pak klikněte na „Pokračovat“.

.... obrázek: tiskárna/přejmenovat_tiskárnu.png
:alt:Přejmenujte stránku přidání tiskárny v proudu „Přidat tiskárnu“, kde je pole pro název zvýrazněno.

#Nastavte pole „Model“ na „DYMO LabelWriter 450 DUO Label (en)“ (nebo
Poté klikněte na tlačítko „Přidat tiskárnu“ (v závislosti na použitém modelu tiskárny DYMO).
instalaci.

.. obrázek:: tiskárna/vyber-tiskárnu.png
:alt:Vyberte model obrazovky na konzole OpenPrinting CUPS s modelem a přidejte tiskárnu
zvýrazněny.

#Klikněte na nabídku „Tiskárny“ v horní liště a klikněte na nově nainstalovanou tiskárnu.
:guilabel:`Tiskárna štítků DYMO LabelWriter 450 DUO Label“ (nebo jakýkoliv jiný model tiskárny značky DYMO, který je používán).
v seznamu.

.... obrázek:: tiskárna/tiskárna-stránka.png
:alt:Stránka tiskárny s nově nainstalovanou tiskárnou zvýrazněná.

#Klikněte na seznam „Údržba“ a vyberte možnost „Tisk testovací stránky“, abyste tiskli.
testovací štítek. Testovací štítek by měl vytisknout okamžitě nebo po jedné či dvou sekundách.

Tiskárna Zebra nefunguje
-----------------------------------------

Tiskárny značky Zebra jsou poměrně citlivé na formát tisku jazyka programovacího jazyka Zebra (ZPL).
kódu. Pokud z tiskárny nic nevychází nebo jsou tištěny prázdné etikety, zkuste změnit formát
zprávy předávané tiskárně. Pro její aktivaci je potřeba zapnout režim vývojáře (viz developer-mode).
:menu:Nastavení --> Technické --> Uživatelské rozhraní --> Zobrazení“ a vyhledejte
přesný vzor.

.. viz též:
„Návod k tisku souborů ZPL společnosti Zebra“


Problémy s čtečkou čárových kódů
======================

Znaky, které čte čárový kód, neodpovídají skutečnému kódu
-------------------------------------------------------------------

Většina čteček čárových kódů je v základním nastavení konfigurována ve formátu QWERTY pro USA. Pokud je
používá jiný formát, přejděte na: „IoT -> Zařízení“ a klikněte na kartu zařízení s čárovým kódem.
Poté vyberte správný jazyk v poli „Klávesnice“.

.. poznámka::
Klávesnice má jazyková specifika. Nastavení se liší podle dostupných možností.
zařízení a jazyk databáze (např. :guilabel:`Angličtina (Velká Británie)` nebo :guilabel:`Angličtina
(USA), atd.

Když se čárový kód naskenuje, nic se nestane
-----------------------------------------

Zkontrolujte, že je v nastavení „Prodejní místo“ vybráno správné zařízení.
</nastavení/prodejní místo/konfigurace/pos_iot> (pokud je to možné) a čárový kód
konfigurována tak, aby na konci každého čárového kódu poslala znak „Enter“ (klávesová zkratka 28).

Skenovač čárových kódů je detekován jako klávesnice
---------------------------------------------

.. důležité::
Některé čtečky čárových kódů jsou identifikovány jako klávesnice USB, nikoliv jako čtečky čárových kódů a nejsou
rozpoznávané systémem IoT.

Chcete-li změnit typ zařízení ručně, přejděte na: „IoT -> Zařízení“ a klikněte na čárový kód.
kartu zařízení. Poté zapněte:guilabel:"Je skener".

Skenovač čárových kódů zpracovává znaky čárového kódu jednotlivě.
-------------------------------------------------------------

Při přístupu k mobilní verzi Odoa z mobilního zařízení nebo tabletu, které je spárováno s čárovým kódem
snímačem přes internet věcí (IoT) může senzor interpretovat každou hodnotu v čárovém kódu jako samostatnou.
Scanování. Pro vyřešení této situace přejděte na: „IoT -> Zařízení“ a klikněte na čárový kód zařízení.
kartu. V poli „Klávesnice“ vyberte správný jazyk.

.. poznámka::
Klávesnice má jazyková specifika. Nastavení se liší podle dostupných možností.
zařízení a jazyk databáze (např. :guilabel:`Angličtina (Velká Británie)` nebo :guilabel:`Angličtina
(USA), atd.
