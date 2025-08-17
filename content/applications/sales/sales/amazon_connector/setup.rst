==============================
Konfigurace Amazon Connector
==============================

Odoo umožňuje uživatelům zaregistrovat se jako prodejce na Amazonu v databázi, ale uživatelé **musí mít**
před dokončením konfigurace účet prodávajícího na Amazonu, který je zpoplatněný.

Zaregistrujte se jako prodávající na Amazonu nejprve přihlášením do platformy Amazon a poté přejděte na
Vyberte položku „Účet & Seznamy“ -> „Zahájit prodejní účet“ z nabídky umístěné v
hlavičkové části.

Poté přejděte na stránku „Prodej s Amazonem“ a postupujte podle pokynů k registraci. Nakonec
postupujte podle pokynů níže a zaregistrujte a propojte tento účet Amazonu v Odoo.

.. viz též:
„Prodávejte na Amazonu <https://www.amazon.com/b/?node=12766669011>“

Připojte účet Amazon Seller k Odoo
=====================================

.. _amazon/setup:

Pro propojení účtu Amazon Seller v aplikaci Odoo přejděte na: „Prodej -->
Konfigurace --> Nastavení --> sekce „Spojky“ aktivovat funkci Amazon Sync
a klikněte na tlačítko „Uložit“.

Poté se vraťte do části „Prodejní aplikace -> Konfigurace -> Nastavení -> Zdroje“,
a klikněte na odkaz „Amazon účty“ pod nastavením „Synchronizace s Amazonem“.

.. obrázek:setup/amazon-accounts-link-setting.png
:align:center
:alt:Odkaz na účty Amazonu pod nastavením synchronizace s Amazonem v Odoo Sales.

Tím se zobrazí samostatná stránka „Amazon Accounts“. Zde klikněte na „New“
Vytvořte si nový účet na Amazonu.

Na prázdném formuláři „Amazon Account“ začněte volbou názvu účtu (např.
„Americký trh“). V záložce „Přihlašovací údaje“ vyberte trh, na kterém
Prodávající účet byl původně vytvořen z nabídky „Domácí tržiště“ ve formuláři „Nastavení“.

.. obrázek: nastavení/amazon-accounts-form-page.png
:align:center
:alt: Typická stránka přihlášení do účtu na Amazonu v aplikaci Odoo Sales.

Po uložení se pole v záložce „Kredit“ nahradí odkazem na
Tlačítko „Amazon“.

.. obrázek: setup/amazon-accounts-form-link-button.png
:align:center
:alt: Typická stránka s přihlášením do účtu na Amazonu a tlačítko pro propojení s Odoo Sales.

Kliknutím na tlačítko se přesměruje buď na stránku přihlášení do Amazonu nebo přímo na požadovaný souhlas.
stránka, pokud uživatel je přihlášený na Amazonu.

Na přihlášení se přihlaste do požadovaného účtu prodejce na Amazonu.

Na stránce souhlasu potvrďte, že Amazon může dát společnosti Odoo přístup k účtu a příslušným informacím.
Data.

Poté se uživatel vrací do Odoo a účet je zaregistrován.

S úspěšně registrovaným účtem na Amazonu jsou pro tento konkrétní účet dostupné všechny tržiště.
jsou synchronizovány s Odoo a jsou uvedeny pod záložkou „Trhy“.

Pokud chcete, odeberte položky ze seznamu synchronizovaných tržišť a vypněte synchronizaci.

Objednávky z Amazonu v Odoo
=====================

Při synchronizaci objednávky z Amazonu vznikne na prodejním příkazu v Odoo až tři položky.
Každý z nich představuje prodaný produkt na Amazonu: jeden pro produkt, který byl prodán na Amazonu
Tržiště, jedno pro poštovné (pokud existuje) a druhé pro balení dárku (pokud existuje).

..._amazon/shodné:

Vybrání databázového produktu pro položku objednávky se provádí shodou
:guilabel:`Vnitřní odkaz“ (vlastní identifikátor produktu v Odoo, například „FURN001“)
s kódem SKU pro položky tržiště na Amazonu, s kódem Shipping Code pro přepravní poplatky a
kód pro účtování dárkového balení od Amazonu *.Gift Wrapping*.

Pro produkty z tržiště jsou uložené kombinace uvedeny jako „Nabídky Amazonu“, které se nacházejí pod
Klikněte na tlačítko „Nabídky“ v účtu.

.. obrázek:setup/amazon-offers-button.png
:align:center
:alt:Tlačítko chytré nabídky Amazonu na formuláři objednávky v Odoo Sales.

Nabídky jsou automaticky vytvářeny při založení páru a používají se pro další
pokyny k vyhledání SKU. Pokud nenajdeme nabídku se shodnou SKU, :ref:`interní referenci
místo <amazon/matching>“.

..tip:
Je možné připojit produkt tržiště k určitému výrobku změnou
nebo SKU nabídky, aby se ujistili, že jsou shodné. Nabídka může být ručně vytvořena
pokud se ještě automaticky neprovedlo.

Toto je užitečné v případě, že interní referenční číslo není používáno jako kód výrobku nebo pokud se produkt prodává pod jiným názvem.
různé podmínky.

Pokud nebude nalezen žádný produkt s vnitřním odkazem shodný pro danou skladovou položku nebo dárek
Kód se zabalí do obalu, pak se použije výchozí produkt databáze *Amazon Sale*. To samé platí i pro
výchozí produkt *Amazon Shipping* pokud není pro daný kód doručení Amazonu nalezen žádný databázový produkt.

.. poznámka::
Chcete-li upravit výchozí produkty, zapněte režim pro vývojáře a přejděte na
:menu_selection:`Prodejní aplikace --> Konfigurace --> Nastavení --> Propojení --> Amazon Sync -->
Výchozí produkty.

Konfigurace produktových daní
=========================

Pro daňové hlášení prodejů na Amazonu s Odoo jsou aplikovány daně z objednávky.
Ty, které jsou určeny produktem nebo danou daňovou pozicí.

Ujistěte se, že máte na své produkty v Odoo správně nastavené daně nebo nechte tuto práci na fiskální
položky, abychom se vyhnuli rozdílům v podsoučtech mezi Amazonem Seller Central a Odoo.

.. poznámka::
Amazon nemusí aplikovat stejné daně jako ty, které jsou v Odoo nastaveny.
Tyto objednávky se liší o několik centů mezi Odoo a Amazonem.
rozdíly lze vyřešit smazáním, když se platby v Odoo sloučí.

.. _amazon/add-new-marketplace:

Přidejte nový trh
=====================

Každý trh je podporován Amazon Connectorem. Chcete-li přidat nový trh, postupujte takto:
následuje:

#Aktivujte režim vývojáře:ref:`<developer-mode>`.
#Přejděte na: „Prodejní aplikace“ -> „Konfigurace“ -> „Nastavení“ -> „Zapojení“ -> „Amazon Sync“.
Amazon Marketplace.
#Klikněte na tlačítko „Nový“ pro vytvoření nového záznamu tržiště.
#V poli „Identifikátor API“ zadejte identifikátor tržiště a v poli „Amazon“ vyberte Amazon.
Řádek pro tržiště, jak je popsán v dokumentaci Amazonu o identifikátorech tržišť a
regiony <https://developer-docs.amazon.com/sp-api/docs/marketplace-ids> a
:guilabel:"URL Seller Central" podle popisu v "Dokumentaci Amazonu pro URL Seller Central
<https://developer-docs.amazon.com/sp-api/docs/seller-central-urls>.
#Nastavte název záznamu na Amazon.<kód země> pro snadné vyhledání (např.
„Amazon.se“). API identifikátor, region a prodejce
V poli "Central URL" by měly být uvedeny hodnoty *ID tržiště*, vybrané oblasti Amazonu a
a hodnoty *URL pro Seller Central* z dokumentace Amazonu.
#Jakmile bude tržiště zachráněno, aktualizujte konfiguraci účtu Amazon tím, že přejdete na
:menu_selection:`Prodejní aplikace --> Konfigurace --> Nastavení --> Propojení --> Amazon Sync -->
„Amazon účty“.
#Vyberte účet, na který chcete nový trh používat, přejděte do záložky „Trhy“
a klikněte na „Aktualizace dostupných tržišť“. Animace by měla potvrdit úspěch
operace. Nově přidané tržiště jsou automaticky přidány do seznamu synchronizovaných
tržiště. Pokud nové tržiště nebude v seznamu uvedeno, znamená to, že buď
nekompatibilní nebo nedostupné pro účet prodávajícího.

.. viz též:
   - :doc:`feature“
   - :doc:`spravovat`
