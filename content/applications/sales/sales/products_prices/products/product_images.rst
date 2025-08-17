=================================
Obrázky produktů s Google Images
=================================

Mít vhodné obrázky produktů v Odoo je užitečné z několika důvodů. Nicméně pokud máte hodně
Produktům potřebují obrázky, přiřazování jim může zabrat spoustu času.

Naštěstí lze tento problém vyřešit tak, že se do databáze Odoo integruje služba Google Custom Search.
Obrázky produktů (na základě jejich čárového kódu) je velmi efektivní.

.. _produktové obrázky/konfigurace:

Konfigurace
=============

Chcete-li využít funkci *Google Custom Search* v databázi Odoo, musíte mít jak databázi, tak i Google
API musí být správně nakonfigurováno.

.. poznámka::
Zdarma poskytované účty Google umožňují uživatelům vybírat až 100 obrázků zdarma denně. Pokud je požadováno větší množství,
Pokud je třeba, je nutné provést upgrade fakturace.

... _produktove-obrazek/google-api-dashboard:

Dashboard služby Google API
--------------------

#Přejděte na stránku „API a služby Google Cloud Platform“
vytvořit přihlašovací údaje služby Google Custom Search API. Poté se přihlásit pomocí účtu Google.
do jejich „Podmínek služby“ zaškrtnutím políčka a kliknutím na „Souhlasím“.
Pokračujte.“
#Zde vyberte (nebo vytvořte) projekt API pro uložení přihlašovacích údajů. Začněte tím, že mu dáte
pamatovatelné: „Název projektu“, vyberte „Lokalitu“ (pokud existuje) a pak klikněte
:guilabel:`Vytvořit“.
#S vybranou možností „Přihlašovací údaje“ v levém panelu klikněte na „Vytvořit
Kredence“ a vyberte „API klíč“.

...... obrázek: produkty/certifikace-api-klíč.png
:synchronizace: střed
:alt:Stránka služeb a rozhraní na platformě Google Cloud Platform.

#Provedením takového kroku se zobrazí okno s názvem „Vytvořený API klíč“, které obsahuje vlastní „API
klíč. Zkopírujte a uložte klíč „Váš API klíč“ do okna – bude použit později.
klíč se zkopíruje (a uloží pro pozdější použití), kliknutím na tlačítko „Zavřít“ se okno s upozorněním odstraní.

.. obrázek: produkty/api-key-pop-up.png
:synchronizace: střed
:alt:Pop-up okno s vytvořeným API klíčem.

#Na této stránce vyhledejte „Vlastní vyhledávací služba“ a zvolte ji.

.. obrázek: produktové_obrázky/vyhledávací lišta služby Custom Search API.png
:synchronizace: střed
:alt: Vyhledávací lišta obsahující „Vlastní vyhledávací služba“ na platformě Google Cloud.

#Zde z webové stránky „Vlastní vyhledávací služba“ můžete v sekci „API“ aktivovat API kliknutím na „Povolit“.

.... obrázek:: produkty/gcp-custom-search-api-page.png
:synchronizace: střed
:alt:"Stránka Custom Search API" s tlačítkem Enable zvýrazněným na platformě Google Cloud.

.. _produktove-obrazek/google-pse-dashboard:

Dashboard programovatelného vyhledávání od Googlu
------------------------------------

#Následně přejděte na „Programovatelný vyhledávač Google <https://programmablesearchengine.google.com/>“
a klikněte na jednu z tlačítek „Začněte“. Přihlaste se pomocí účtu Google, pokud jste jej ještě nezaložili.
Ještě jste se nepřihlásili.

.... obrázek: produktové obrázky/google-pse-get-started.png
:synchronizace: střed
:alt:Stránka programovatelného vyhledávače Googlu s tlačítky Start Now.

#Na formuláři „Vytvořit nový vyhledávač“ zadejte název vyhledávače,
s jakým obsahem by měl vyhledávat a ujistěte se, že zapnete:guilabel:`Obrazový vyhledávání“ a
:guilabel:`Bezpečné vyhledávání“.

.... obrázek:product_images/create-new-search.png
:synchronizace: střed
:alt: Vytvořit nový formulář vyhledávacího motoru, který se zobrazí s konfiguracemi vyhledávacího motoru.

#Zkontrolujte formulář kliknutím na tlačítko „Vytvořit“.
#Tím se zobrazí nová stránka s nadpisem „Váš nový vyhledávač je
Vznikla.

...... obrázek: produkty/nový-vyhledávač-je-vytvořen.png
:synchronizace: střed
:alt:Stránka, která se objeví s kódem pro kopírování, obsahuje nový vyhledávač.

#Na této stránce klikněte na „Upravit“ a otevřete stránku „Přehled - Základní“.
Pak zkopírujte ID do pole „ID vyhledávače“ :guilabel:`Search engine ID`. Tento ID je potřeba pro Odoo
konfigurace.

.... obrázek:: produkty/obecný přehled vyhledávání - id motoru.png
:synchronizace: střed
:alt:Stránka s základním přehledem a políčkem pro vyhledávací identifikaci.

.. _produktové_obrázky/nastavení_v_Odoo:

Odoo
----

#V databázi Odoo přejděte do sekce „Nastavení“ a posuňte se dolů.
:guilabel:`Souhrn integrace“ sekci. Zde zaškrtněte políčko vedle :guilabel:`Google obrázky“.
Pak klikněte na tlačítko :guilabel:`Uložit“.

.. obrázek: produktové_obrázky/google-images-settings.png
:synchronizace: střed
:alt:Nastavení Google Images v aplikaci Nastavení Odoo.

#Poté se vraťte do aplikace „Nastavení“ a posuňte se dolů k položce „Spojení“.
části. Pak zadejte do políček klíč API a identifikační číslo vyhledávače
pod nástrojem „Google Images“.
#Klikněte na tlačítko „Uložit“.

.. _produktove-obrazek/ziskat-produktove-obrazek:

Obrázky produktů v Odoo s vyhledávacím API od Googlu
====================================================

Přidání obrázků do produktů v Odoo lze provést na jakémkoliv produktu nebo jeho variantě. Tento proces může být
dokončena v jakémkoli Odoo aplikaci, která poskytuje přístup k stránce produktu (např. aplikace *Prodej*,
Aplikace „Inventář“ atd.

Níže je krok za krokem popsáno, jak využít službu Google Custom Search API k přiřazení
obrázky k produktům v aplikaci Odoo pomocí aplikace Odoo Sales:

#Najděte si produkty na stránce „Produkty“ v aplikaci „Prodej“ (v menu vyberte „Aplikace Prodej –>
Produkty - Produkty. Nebo se přihlaste do aplikace *Prodej* a vyberte stránku s názvem „Varianty produktů“.
(:menu_selection:„Prodejní aplikace --> Produkty --> Výrobky“).
#Vyberte požadovaný produkt, který potřebuje obrázek.

....... poznámka::
Pro zpracování jsou přijímány pouze produkty (nebo varianty produktů), které mají čárový kód, ale **ne** obrázek.

Pokud je vybrán produkt s jednou nebo více variantami, každá varianta, která odpovídá
uvedených kritérií je zpracováváno.

#Klikněte na ikonu „Akce“ (převodovka) v detailu produktu a vyberte možnost „Získat“.
Obrázky z Google Images ze seznamu, který se objeví.

.. obrázek:: produkty/získat-obrázky-od-google-akce.png
:synchronizace: střed
:alt:Volba Vyhledat obrázky v Google z nabídky akcí v Odoo.

#V okně, které se objeví, klikněte na tlačítko „Získat snímky“.

.... obrázek:: produkty/klikněte a získáte obrázek z vyskakovacího okna
:synchronizace: střed
:alt:Pop-up okno, ve kterém uživatel musí kliknout na možnost „Získat obrázek v prodejním modulu Odoo“.

#Kliknutím na obrázek se zobrazí postupně další fotografie.

....... poznámka::
Jen první deset obrázků se stáhne okamžitě. Pokud jste vybrali více než deset, zbytek bude
jako pozadí.

Zadní pracovní proces zpracovává za minutu přibližně 100 obrázků. Pokud je povolený limit stanovený
(s placeným nebo bezplatným plánem) se dosáhne, pak se zadní pracovník zastaví na 24 hodin.
Poté bude pokračovat tam, kde předchozí den skončila.

.. viz též:
„Vytvořte, upravte nebo zavřete účet Google Cloud Billing

