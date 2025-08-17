Zobrazit obsah

=====
Stránky
=====

Odoo vám umožňuje vytvářet stránky pro vaše webové stránky a upravovat jejich obsah a vzhled podle svých představ.
potřeby.

... webové stránky / stránky / typ stránky:

Statické stránky, jako je hlavní stránka nebo jakákoliv jiná vytvořená podle pokynů pro tvorbu webových stránek
obsahují pevný obsah, který se nemění dynamicky. Tyto stránky lze vytvořit ručně a definovat
jejich URL adresy a upravit jejich vlastnosti podle potřeby. **Dynamické**
Na stránky se však vztahuje dynamické generování. Všechny stránky automaticky vygenerované systémem Odoo jsou
například když nainstalujete aplikaci nebo modul (např. /shop nebo /blog) nebo zveřejníte nový produkt nebo
:doc:`blogový příspěvek <../blog>“, jsou dynamické stránky a proto se s nimi zachází jinak.

.. _webu/stránky/vytvoření stránky:

Vytvoření stránky
=============

Stránky webu lze vytvářet z **frontendu** i ze **backendu**.
stránce postupujte následovně:

  #– Otevřete aplikaci Webové stránky, klikněte na tlačítko „Nový“ v pravém horním rohu a vyberte
:guilabel:`Stránka“
     - Nebo přejděte na „Webové stránky“ → „Stránka“ → „Nový“.
  #V nabídce „Nová stránka“ vyberte šablonu. Jsou seřazené podle typu:

     - :guilabel:`Základní“: Univerzální stránka, na které je k dispozici i prázdná stránka pro psaní od nuly.
     - :guilabel:`O značce“: Informace o vaší značce.
     - :guilabel:`Přístupové stránky“: Souhrn obsahu a informací o společnosti.
     - :guilabel:`Galerie“: Fotografie a média.
     - :guilabel:`Služby“: Zaměřte se na to, co prodáváte a kontaktujte.
     - :guilabel:`Cenové plány“: Zvýrazněte předplatné a ceny.
     - :guilabel:`Tým“: Lidé za vaší společností.
     - :guilabel:`Vlastní šablona“: Vybrat vlastní šablonu. Chcete-li přidat šablonu do této kategorie, otevřete
stránku, kterou chcete uložit jako šablonu, pak přejděte na: „Webová stránka --> Vlastnosti“, zadejte
stránka „Název stránky“, upravit vlastnosti stránky
<webové stránky/stránky/vlastnosti stránky>`, aktivujte „Je šablona“ a klikněte
:guilabel:`Uložit“.

  #Zadejte název stránky: guilabel:Název stránky; tento název se používá v nabídce a ve URL adrese stránky.
  #Klikněte na tlačítko „Vytvořit“.
  #Pokud je třeba, upravte obsah a vzhled stránky pomocí webu
editoru a poté stiskněte tlačítko „Uložit“.
  #:ref:`Zveřejnit stránku <website/pages/un-publish-page>“.

..tip:
Deaktivujte položku „Přidat do nabídky“ pokud stránka nemá být v nabídce zobrazena.

.. _webové stránky/stránky/správa stránek:

Správa stránky
===============

..._webové stránky/stránky/odstranit-stránku:

Publikování a odstranění stránek
-----------------------------

Stránky musí být publikovány, aby byly viditelné pro návštěvníky webu. Chcete-li publikovat nebo odstranit stránku
stránku otevřít a přepnout přepínač v pravém horním rohu z „Nedostupné“ na „Zveřejněno“.
:publikován:, nebo naopak.

.. obrázek: stránky/nepublikované_přepínač.png
:alt:Přepínač mezi nezveřejněným a zveřejněným

.. poznámka::
Je také možné:

    - Publikovat nebo odstranit stránku z vlastností stránky:ref:`<website/pages/page_properties>`,
kde můžete definovat datum vydání a případně omezit viditelnost stránky.
    - Zveřejnit nebo skrýt několik stránek najednou: přejděte na: „Webové stránky“ - „Stránka webu“
vyberte stránky a pak klikněte na tlačítko „Akce“ a zvolte možnost „Vydat“.
:guilabel:`Nepublikovat“.


Alternativně můžete definovat jakoukoliv „statickou stránku“ jako domovskou stránku
Přejděte na webové stránky, klikněte na záložku „Správa“ a vyberte možnost „Zveřejnit“.
Zapnout:„Použít jako domovskou stránku“.

... webu/stránky/vlastnosti stránky:

Vlastnosti stránky
---------------

Pro změnu vlastností statické stránky přejděte na stránku, kterou chcete upravit.
upravit a poté přejít na „Sites --> Properties“, kde můžete změnit následující
vlastnosti:

 - :guilabel:`URL stránky` : Upravte adresu URL stránky v poli. V tomto případě můžete přesměrovat
pokud je třeba, přesměruje na novou adresu. Chcete-li tak učinit, zapněte :guilabel:`Přesměrovat starou URL` a poté vyberte
:guilabel:`Typ“ přesměrování dle :ref:`stránky URL-redirection <webové stránky/stránky/přesměrování URL>“

    - :guilabel:`301 Permanent Redirect“: pro trvalé přesměrování stránky.
    - :guilabel:`302 Moved temporarily“: pro přesměrování stránky dočasně.

.. obrázek:: stránky/vlastnosti_stránky.png
:alt: Přesměrujte starou adresu

 - :guilabel:`V nabídce“: Zakážete-li tuto možnost, stránka se nebude zobrazovat v nabídce.
 - :guilabel:`Je domovská stránka“: Zapněte, pokud chcete, aby byla tato stránka domovskou stránkou vašeho webu.
 - :guilabel:`Zveřejněno“: umožňuje stránce být zveřejněna.
 - :guilabel:`Datum vydání“: Klikněte na pole pro zveřejnění stránky v určitém datu a čase.
Zadejte datum a čas, pak stiskněte klávesu **Enter** nebo klikněte na tlačítko „Použít“ pro ověření výběru.
 - :guilabel:`Indexované“: Zakázat, pokud nechcete, aby stránka byla zobrazována ve výsledcích vyhledávání.
 - Viditelnost: Vyberte, kdo může stránku vidět:

    - :guilabel:`Veřejnost“:Stránku může sledovat každý.
    - :guilabel:`Přihlášený uživatel“: Přístup k stránce je možný pouze pro přihlášené uživatele.
    - „Omezená skupina“: Vyberte uživatelskou přístupovou skupinu

    - Pole „S heslem“: Zadejte heslo, které je potřebné k přístupu na stránku.
:guilabel:`Heslo“ pole.

 - :guilabel:`Je šablona“: Přepněte přepínač, abyste stránku uložili jako šablonu a přidali ji do
:guilabel:`Vlastní“ kategorie.

..tip:
Některé z těchto vlastností lze také upravit ve skupině.
:menuselection:`Webová stránka --> Stránky webu“.

... webové stránky/stránky s duplicitním obsahem:

Duplikace stránek
~~~~~~~~~~~~~~~~~

Pro duplikaci stránky přejděte na stránku, pak do nabídky „Webové stránky“ vyberte možnost „Vlastnosti“, a klikněte
Vyberte Duplicitní stránku. Zadejte název stránky a klikněte na OK.
Nová stránka se přidává po duplicitní stránce v navigaci, ale můžete ji z navigace odstranit nebo
změnit svou pozici pomocí menu editoru (viz stránka Pohledy hlavičky a patičky).

..._webové stránky/stránky/smazat stránku:

Smazání stránek
~~~~~~~~~~~~~~

Chcete-li stránku smazat, postupujte takto:

#Přejděte na stránku a pak klikněte na „Správa webu“ > „Vlastnosti“ > „Smazat stránku“.
#Otevře se okno s odkazy na všechny stránky, které odkazují na tu, kterou chcete vymazat.
Řazené podle kategorií. Abyste zajistili, že návštěvníci webu nepřijdou na chybovou stránku, musíte aktualizovat
všechny odkazy na vašem webu vedoucí na tuto stránku. Chcete-li tak učinit, rozbalte kategorii, pak klikněte
link na otevření v novém okně. Místo toho můžete také nastavit :ref:`přesměrování
pro odkaz na stránku, která byla smazána.
#Jakmile aktualizujete odkazy (nebo nastavíte :ref:`přesměrování <webové stránky/stránky/URL-přesměrování>`)
Zatrhněte zaškrtávací políčko „Jsem si jistý/á“, pak klikněte na „OK“.

.._webové stránky/stránky/URL adresy:

Mapování přesměrování URL
--------------------

URL adresa se směruje na jinou adresu, než je ta původní.
požadovanou. Tato technika se používá například k zabránění rozbitéch odkazů při
vymažete stránku (<web/stranky/smazat-stranku>).
:upravit svou adresu URL (viz webové stránky/stránky/vlastnosti stránky) nebo přesunout svůj web z jiné platformy na
Odoo doménu: doc:`<konfigurace/domény>`. Může být také použita k zlepšení stránek: doc:`<stránky/seo>“.

Pro přístup k existujícím směrováním a vytváření nových je zapotřebí aktivovat režim pro vývojáře
a přejděte na Web --> Konfigurace -->
Přesměrování.

.. poznámka::
   - Při každé změně adresy stránky se automaticky přidává záznam o přesměrování.
a zapněte možnost „Přesměrovat starou adresu“.
   - Můžete nastavit přesměrování pro „statické“ a „dynamické“ stránky (viz <website/pages/page_type>).

Pro vytvoření nové přesměrování klikněte na tlačítko „Nový“, pak vyplňte pole:

- :guilabel:`Jméno“: Zadejte jméno, které bude identifikovat přesměrování.
- Vyberte typ přesměrování:

   - :guilabel:`404 Not Found“: návštěvníci jsou přesměrováni na stránku chyby 404, když se pokusí o přístup
nepublikovaná nebo smazaná stránka.
   - :guilabel:`301 Moved Permanently“: pro trvalé přesměrování nezveřejněných nebo smazaných
:ref:`statické stránky <webové stránky/stránky/typ stránky>“. Nová adresa se zobrazuje ve výsledcích vyhledávání.
a odkaz je uložen prohlížeči do mezipaměti.
   - :guilabel:`302 Moved Temporarily“: pro krátkodobé přesměrování například při přechodu na HTTPS.
přepracování nebo aktualizaci stránky. Nová adresa není ukládána prohlížeči ani zobrazována ve vyhledávání.
výsledky motoru.
   - :guilabel:`308 Redirect/Rewrite“: pro trvalé přesměrování stávajících dynamických stránek
<webové stránky/stránka typu>“. URL je přejmenován, nové jméno se zobrazuje ve výsledcích vyhledávání
a je uložena v prohlížečích. Používejte tento typ přesměrování k přejmenování dynamické stránky například tehdy, když ji chcete přejmenovat.
chce přejmenovat složku „/shop“ na „/market“.

- :guilabel:`URL odkazované na“: Zadejte adresu URL, kterou chcete přesměrovat (např. /o-spolecnosti/) nebo vyhledejte
Vyberte požadovanou dynamickou stránku (viz ref:<website/pages/page_type>).
- :guilabel:`URL k přesměrování na:“ Zadejte adresu URL, na kterou se má provést přesměrování.
Pokud chcete odeslat na externí URL, zahrňte protokol (např. „https://“).
- :guilabel:`Webová stránka“: Vyberte konkrétní webovou stránku.
- :guilabel:`Sequenční řazení“: K určení pořadí provádění přesměrování, například v případě
řetězců přesměrování (tj. série přesměrování, kde je jedna adresa odkazována na jinou).
je sama o sobě dále přesměrována na jinou adresu.

Přepněte na tlačítko „Aktivovat“ a přesměrování vypněte.

.. důležité:
404, 301 a 302 jsou určeny k migraci provozu.
:ref:`nepublikované <webové stránky/stránky/un-publish-page> nebo :ref:`smazané <webové stránky/stránky/delete-page>
pro nové stránky a pro trvalé přesměrování stávajících stránek se používá 301 přesměrování, zatímco pro dočasné přesměrování existujících stránek se používá 302 přesměrování.

.. viz též:
   - „Dokumentace Google o přesměrování a vyhledávání <https://developers.google.com/search/docs/crawling-indexing/301-redirects>“
   - :doc:`stránky/seo“

.. toctree::


stránky hlaviček a patiček
stránky/seo
