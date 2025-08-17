=============
Samoobjednávání
=============

Funkce samoobsluhy umožňuje zákazníkům procházet vaše nabídky nebo katalog produktů, objednat si a
a zaplatit pomocí svého mobilního zařízení nebo samoobslužného terminálu.

Konfigurace
=============

Aktivace funkcí
------------------

Chcete-li tuto funkci zapnout a vybrat typ samoobslužného objednávání, přejděte do nastavení POS.
<konfigurace/nastavení>“, posuňte se dolů do části „Samoobslužný kiosek a mobilní objednávka“
Vyberte možnost „Sebeobjednávka“ pod položkou „Aktivace QR menu a kiosku“.

Můžete si vybrat z:

.. záložky::

.. skupinová záložka: QR menu

Vyberte možnost „QR menu“ nebo „QR menu + objednávky“, abyste zákazníkům umožnili přístup k vašemu
nabídku nebo produktový katalog pomocí skenování QR kódu na svém osobním zařízení.
jim umožňuje provést objednávku a zaplatit.

.. obrázek:: self_order/qr-activation.png
:alt: Aktivace QR menu a kiosku

      - Klikněte na ikonu „fa-arrow-right“ a poté stáhněte PDF dokument s
vytvářejí QR kódy.
      - Klikněte na ikonu „fa-arrow-right“ a poté stiskněte tlačítko „Stáhnout QR kódy“.
s vygenerovanými QR kódy.

.. poznámka::
V restauracích se při tisku nebo stažení QR kódu vytvoří stejný počet QR kódů.
Počet volných stolů. V obchodech generuje pouze jeden univerzální QR kód.

...............tip:
Pro přizpůsobení QR kódů

         #Naskenujte příslušný QR kód a získáte jeho URL.
         #Použijte generátor QR kódů (např. „QR Code Monkey <https://www.qrcode-monkey.com>“ nebo „QR
generátor kódu QR (https://www.qr-code-generator.com`) vytvořit vlastní QR kód.

...... skupina-tab:: Kiosk

Když je vybrána volba „Kiosk“, zákazníci mohou přistupovat k nabídce nebo produktovému katalogu a
objednávat si sami a platit na automatu.

.. obrázek: self_order/kiosk-aktivace.png
:alt: Aktivace QR menu a kiosku

Jakmile je vybrán typ samoobslužného objednávání, jsou k dispozici další nastavení (viz. :ref:`přidat další nastavení <pos/self_order/add-settings>`).
aktualizace, která bude vyhovovat potřebám zvoleného typu.

.. _pos/self_order/add-settings:

Další nastavení
-------------------

.. záložky::

...... záložka: Tlačítko Domů

Výraz „tlačítko domů“ se zobrazuje na rozhraní kiosku nebo mobilního zařízení.
zákazníci si objednávají sami. Chcete-li je nastavit, klikněte na ikonu :icon:`fa-arrow-right` :guilabel:`Domů
tlačítko. Pak

      #Klikněte na tlačítko „Nový“.
      #Zadejte hodnotu:guilabel:„Štítek“.
      #Zadejte URL s předponou https://, aby se zákazníci dostali na konkrétní URL.
kliknutím na tlačítko. Například byste mohli odeslat uživatele na videokampaň.
nový produkt nebo na stránku soutěže.
      #V stejném sloupci „URL“ zadejte /produkty, abyste vytvořili tlačítko, které přesměruje
zákazníky do katalogu produktů.
      #Vyberte bod prodeje a zkontrolujte, aby se tlačítko zobrazovalo pouze na vybraných bodech.
Samoobslužný rozhraní pro objednávání zboží.
      #Vyberte předdefinovaný styl ze seznamu.

.. poznámka::
         - Ponechání pole „Prodejní místa“ prázdné sdílí tlačítko se všemi prodejními místy.
         - Sloupec Preview automaticky aktualizuje, takže vám dává představu o tom, jak bude
vzhled tlačítka podle jeho konfigurace.

....... tab:: Lokalita a způsoby platby

      - Vyberte místo, kde se služba odehrává, buď „Stůl“ nebo „Oblast pro vyzvednutí“.
pod položkou služby.
      - V poli „Zaplatí později“ zadejte, kdy a jak zákazníci zaplatí. Zákazníci mohou platit
po: „Každé jídlo“ nebo „Každá objednávka“.
      - Možnosti platby a umístění služeb se liší podle typu samoobslužného zařízení.
služby a POS:

        - **QR menu + objednávání**:

          - **Restaurace**: Klienti mohou být obsluhováni u stolu nebo v zóně pro vyzvednutí jídla.

            - Při podávání jídla na jejich stole mohou platit po každém jídle nebo objednávce.
            - Při podávání v zóně vyzvednutí mohou platit pouze po každé objednávce.
          - Prodejny: Zákazníci mohou být obsluhováni pouze v zóně vyzvednutí a platit za každý nákup zvlášť.
          - Ať už se jedná o jakýkoliv typ POS terminálu, zákazníci mohou platit online.

metoda <platební_metody>.

        - **Kiosk**:

          - Ať už se jedná o jakýkoliv typ POS, zákazníci mohou být obsluhováni buď u svého stolu nebo v
odběrové zóně, ale musí platit za každou objednávku.
          - Samoobslužné objednávání přes stánek funguje pouze s :doc:`Adyen <platební metody/termíny/adyen>
a:doc:`termíny Stripe <platební metody/terminaly/stripe>“.
          - Funkce „Online platba“ není podporována.

.. viz také:
         - :doc:`../../finance/platební_prostředky`
         - :doc:`platební metody“

... tab::Jazyk

Tato volba umožňuje nastavit více jazyků pro rozhraní samoobsluhy.
navrhované jazyky jsou ty, které již byly nainstalovány v Odoo. Chcete-li rozšířit výběr, přidejte další
jazyky:

      #Klikněte na ikonu „Přidat jazyky“.
      #Přidejte do pole :guilabel:`Jazyky` kolik jazyků potřebujete.
      #Klikněte na tlačítko „Přidat“.
      #Přidejte tyto jazyky do pole :guilabel:`Dostupné`.

.. viz také:
:doc:`../obecne/uzivatele/jazyk`

....... záložka: Splash screeny

Spláškové obrazovky jsou úvodní obrazovky zobrazené při spuštění samoobslužného rozhraní nebo kiosku.
spuštěny. Obvykle obsahují značku, uvítací zprávy nebo pokyny k použití.

      - Pro přidání obrázku na úvodní obrazovku klikněte na ikonu „Papírový uzel“ a poté vyberte možnost „Přidat obrázek“.
otevřít obrázek.
      - Pro odstranění obrázku zadní obrazovky přejeďte myší nad obrázek a klikněte na ikonu „fa-times“
([:label:`Smazat`]).

.. poznámka::
Můžete přidat více obrázků záložního plátna najednou.

.. tab:: Jídlo s sebou

Aktivujte tuto možnost, abyste si mohli upravit sazbu daně podle toho, zda se jedná o daň z přidané hodnoty nebo ne.
Klienti si mohou jídlo vzít s sebou nebo si ho objednat na místě.

      - Vyplňte pole existujícím alternativním fiskálním postavením.
      - Vytvořte novou daňovou položku vyplněním pole a kliknutím
:guilabel:`Vytvořit a upravit“; nebo
      - Vytvořte novou fiskální pozici kliknutím na ikonu „Pravý úhel“ a zvolte „Fiskální
Pozice.

.. viz také:
:doc:`cenotvorba/fiskální-poloze“

Představení
-------

Zkontrolujte rozhraní předtím, než bude funkce samoobsluhy k dispozici zákazníkům, abyste se ujistili, že
jsou nastaveny správně. Klikněte na ikonu „Předběžný náhled webového rozhraní“
pod pole „Vlastní seřazení“ a zkontrolovat všechna další nastavení
Pokud se nastavení správně aplikují.

Použití
================

.. záložky::

.. skupinová záložka: QR menu

Na straně uživatele POS přistupujte k samoobslužnému rozhraní.

      - Skenování staženého nebo tištěného QR kódu.
      - Kliknutím na ikonu „vertikální elipsa“ (zobrazenou jako :guilabel:„vertikální elipsa“) v kartě POS.
Pak:„Mobilní menu“.

Na straně zákazníků

      #Přihlaste se do rozhraní pro samoobsluhu pomocí skenování staženého nebo tištěného QR kódu.
      #Klikněte na tlačítko „Domů“ (viz obrázek výše).
      #Vyberte položky a klikněte na tlačítko „Objednat“.
      #Postupujte podle pokynů na obrazovce a přiřaďte si stůl a zaplaťte objednávku.

...... skupina-tab:: Kiosk

Na straně uživatele POS je

      #Klikněte na tlačítko Start Kiosku.
      #Otevřete na pokladně zadanou webovou adresu.

         - Klikněte na poskytnuté URL, abyste otevřeli stánek v novém okně.
         - Klikněte na tlačítko „Instalovat aplikaci“ a nainstalujte modul samoobslužného kiosku do svého kiosku pro sebeobsluhu.
         - Klikněte na „Otevřít v krabici IoT“ pokud je váš stánek propojen s systémem IoT.
<../../obecne/iot/pripojeni>

.. obrázek: self_order/kiosk-otviraci-popup.png
:alt:Pop-up okno pro otevření stánku

.. poznámka::
         - Jakmile je otevřená jedna seance, přepne :guilabel:`Start Kiosk“ na „Open Kiosk“.
platební karta POS.
         - Klikněte na tlačítko „Otevřít kiosk“ v POS kartě, abyste znovu otevřeli okno a získali přístup
vlastní rozhraní pro samoobsluhu.

Na straně zákazníků

      #Klikněte na tlačítko „Domů“ z kiosku pro sebeobsluhu.
dostanete se na nabídku nebo produktový katalog.
      #Vyberte položky a klikněte na tlačítko „Objednat“.
      #Postupujte podle pokynů na obrazovce a přiřaďte si stůl a zaplaťte objednávku.

.. obrázek: self_order/kiosk-endscreen.png
:alt: kiosková obrazovka pro zákazníky
:skalka: 65 %

.. důležité:
   - Pokladní sezení musí být otevřené pro zákazníky, aby mohli objednat.
   - Jakmile je objednávka vytvořena, automaticky se zobrazí na obrazovce pro přípravu.
a přidána do seznamu příkazů POS.
