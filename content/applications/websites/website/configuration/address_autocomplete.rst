====================
Doplňování adresy
====================

Můžete použít službu Google Places API na svých webových stránkách, abyste zajistili, že vaši uživatelé zadávají správnou adresu dodání.
existují a jsou chápány dopravci. Služba Google Places API umožňuje vývojářům přístup k podrobné
informace o místech prostřednictvím požadavku HTTP. Auto-doplňování předpovídá seznam míst, když
uživatel začíná zadávat adresu.

.. obrázek: autocomplete-adresy/autocomplete-adres-priklad.png
:alt: Příklad doplňování adresy

.. viz též:
   - „Google Maps Platform <https://mapsplatform.google.com/maps-products>“
   - „Google Developers Documentation: Google Places API
<https://developers.google.com/maps/documentation/places/web-service/autocomplete>

Pro toto nastavení přejděte na „Webové stránky -> Konfigurace -> Nastavení“ a zapněte
V sekci „SEO“ v položce „Adresa doplňování“.

.. obrázek: adresa_automatického_vyplnění/zapnout_adresní_automatické_vyplňování.png
:alt:Povolit automatické doplňování adresy

Do pole „API klíč“ vložte svůj :guilabel:`Google Places API klíč`. Pokud nemáte
vytvořte si vlastní na „Google Cloud Console <https://console.cloud.google.com/getting-started>“
a postupujte takto.

.. _adresa_autocomplete/generovat_api_klíč:

Krok 1: Zapněte službu Google Places API
====================================

**Vytvořit nový projekt:**
Chcete-li povolit **Google Places API**, nejprve musíte vytvořit projekt. K tomu klikněte na
V horním levém rohu vyberte „Projekt“ a poté „Nový projekt“. Postupujte podle pokynů.
Vytvořit svůj projekt.

**Zapněte službu Google Places API:**
Přejděte do sekce „Zapnuté služby a aplikace“ a klikněte na „+ PŘIDAT SLUŽBU A APLIKACI.“
Vyhledejte „Places API“ a vyberte ji. Klikněte na tlačítko „Zapnout“.

.. poznámka::
Cena Googlu závisí na počtu požadavků a jejich složitosti.

Krok 2: Vytvoření přihlašovacích údajů pro API
==============================

Přejděte na „API a služby –> Přístupové údaje <https://console.cloud.google.com/apis/credentials>“.

Vytvořte přihlašovací údaje:
Pro vytvoření přihlašovacích údajů přejděte do sekce „Přihlášení“, klikněte na „Vytvořit přihlašovací údaje“ a
vyberte:guilabel:API klíč.

Poznámka: Omezte klíč API (volitelně).

Pro zabezpečení můžete omezit použití vašeho klíče API. Můžete přejít na
:guilabel:`Omezení API“ sekci, abyste specifikovali, které API může klíč přistupovat.
Pokud používáte Places API, můžete omezit požadavky na webové stránky nebo aplikace.

.. důležité:
   - Uložte svůj API klíč: zkopírujte si svůj API klíč a bezpečně jej uložte.
   - Neposkytujte ho veřejně nebo nezveřejňujte jej v kódu na straně klienta.
