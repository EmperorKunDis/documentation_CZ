=====================
Objednávání a placení
=====================

Odoo eCommerce nabízí několik možností, jak uspořádat proces objednávání a platby.
různé možnosti tlačítek pro objednávku a sekvenční
:ref:`kroky při placení <ecommerce/payment/steps>“, některé z nich podporují další funkce.
Související tlačítka a stránky s objednávkou lze upravit pomocí webového editoru.

..._ecommerce/checkout/objednávkové tlačítko:

Tlačítka pro objednávání
=============

Pro přizpůsobení procesu objednávání v Odoo eCommerce můžete:

- změnit chování tlačítka „Přidat do košíku“ (viz:ref:Add to Cart <ecommerce/checkout/add-to-cart>“).
- místo toho nahraďte tlačítko s vlastním :ref:`<ecommerce/checkout/prevent-sale>“
- Přidejte tlačítko „Koupit nyní“ (viz. odkaz na stránku s nákupem)
- Přidat tlačítko „Znovu objednat“ do zákaznického portálu.

..._ecommerce/checkout/add-to-cart:

Možnosti přidání do košíku
-------------------

Výchozí chování při přidávání položky do košíku
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kliknutím na tlačítko „Přidat do košíku“ může být spuštěno různé akce. Chcete-li konfigurovat
jejich, přejděte na „Webová stránka --> Konfigurace --> Nastavení“, posuňte se dolů do
V sekci „Obchod – proces objednávky“ a vyberte jednu z následujících možností:

- :guilabel:`Zůstat na stránce produktu“: Zákazník zůstává na stránce s produktem.
- :guilabel:`Přejít do košíku“: Zákazník je ihned přesměrován na stránku s obsahem nákupního košíku.
- :guilabel:`Nechte uživatele rozhodnout (dialog)`: Zákazník si může vybrat, jestli chce pokračovat do košíku
nebo pokud se rozhodnou zůstat na stránce produktu
([:label_continue_shopping]).

.. poznámka::
Toto okno se vždy zobrazí, bez ohledu na konfiguraci, aby navrhlo: doc:`volitelné produkty.
"produkty/křížové prodeje", pokud existují.

.._ecommerce/checkout/prevent-sale:

Možnost přizpůsobit tlačítka
~~~~~~~~~~~~~~~~~~~~

Můžete nahradit tlačítko „Přidat do košíku“ tlačítkem „Kontaktujte nás“, které
Přesměruje uživatele na kontaktní formulář.

.. poznámka::
Odstranění možnosti přidat produkt do košíku se často používá u firem, které chtějí zobrazit
online katalog, ale nemohou sdílet ceny veřejně (například nabídnout individuální nebo proměnlivé cenové zvýhodnění).

Pro to je potřeba se přesunout na: „Webové stránky“ -> „Konfigurace“ -> „Nastavení“. Pod položkou „Obchod –
Sekce produktů, zaškrtněte: guilabel: Prevent Sale of Zero Priced Product. Nový: guilabel: Tlačítko
V poli „URL“ se zadává odkaz na stránku, která bude přesměrována.

Poté nastavte cenu všech produktů, které by měly zobrazovat tlačítko „Kontaktujte nás“, na
„0“ pomocí produktové formy nebo „:doc: ceník <../../sales/sales/products_prices/prices/pricing>“.

.. obrázek: checkout/cart-contact-us.png
:alt:Kontaktujte nás tlačítko na stránce produktu

.. poznámka::
Tlačítko pro kontakt, jeho název a URL jsou všechny stejné.
Název a popis produktu lze upravit na stránce produktu v režimu :guilabel:`Edit
režim.

Další tlačítka přidat do košíku
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Můžete přidat další tlačítko „Přidat do košíku“ a propojit ho s konkrétními produkty.
webové stránky.

Chcete-li je přidat, otevřete editor webu a vložte obsah tlačítka „Přidat do košíku“
stavební blok. Jakmile je umístěn, klikněte na tlačítko, posuňte se dolů a klikněte na tlačítko „Přidat do košíku“.
sekci a nakonfigurujte následující:

- :guilabel:`Produkt“: Vyberte produkt, ke kterému chcete tlačítko připojit.
- Výběr zda se má jednat o „Přidat do košíku“ nebo „Koupit nyní“.
tlačítko „Koupit nyní“

.. poznámka::
   - Pokud má produkt varianty, buď vyberte jednu nebo nechte možnost na:guilabel:'Návštěvník
„Vyberte si“, což zákazníka vyzve k výběru varianty a poté kliknutí na „Pokračovat
Kontrola objednávky nebo pokračovat v nákupu.
   - Výchozí tlačítko „Přidat do košíku“ tyto možnosti neobsahuje, ale jeho název lze změnit.
se změnila.

..tip:
V režimu :guilabel:`Edit“ je také možné zobrazit nebo skrýt ikonku :icon:`fa-shopping-cart`.
ikona „Košík“ v hlavičce stránky. Klikněte na hlavičku a poté na
:ikona_fa_nákupní_vozík: tlačítko vedle možnosti „Zobrazit prázdné“
v záložce „Nastavení“.

..._ecommerce/checkout/koupit-teď:

Kupte si nyní
-------

Umožnit zákazníkům pokračovat do kroku „objednávka ke kontrole“ (přesměrování na stránku s objednávkou).
Přímý odkaz na tlačítko „Koupit teď“ můžete přidat přímo. Chcete-li tak učinit, přejděte na
„Webová stránka“ -> „Nastavení“ -> „Předvolby“. Pod položkou „Obchod – Pokladna
V sekci „Proces“ zaškrtněte možnost „Koupit hned“.

..tip:
Alternativně můžete tuto funkci zapnout navštívením jakékoliv stránky produktu v režimu „Upravit“.
a v záložce „Upravit“ kliknutím na tlačítko „Koupit hned“ s ikonou „fa-bolt“.
vedle možností :guilabel:`Košík`.

.. obrázek: checkout/cart-buy-now.png
:alt:Koupit nyní tlačítko

..._ecommerce/checkout/re-order:

Přeposlat z portálu
--------------------

Zákazníci si mohou znovu objednat položky z předchozích fakturací prostřednictvím svého zákaznického portálu.
:guilabel:`Objednat znovu“ tlačítko. Chcete-li jej přidat, přejděte na :menuselection:`Webové stránky --> Konfigurace -->
Nastavení“. Pod položkou „Obchod – Objednávkový proces“ zaškrtněte „Přeposlat z
Portálův seriál.

.. obrázek: checkout/order-again-button.png
:alt: Tlačítko pro přeřazení

..._ecommerce/checkout/policy:

Zásady pro platbu
===============

Když chcete umožnit zákazníkům platit jako hosté nebo je nutit se přihlásit/založit účet, přejděte na
:menuselection:`Webová stránka --> Konfigurace --> Nastavení“, posuňte se dolů na :guilabel:`Obchod -
Krok „Zpracování objednávky“ a nastavte možnost „Přihlášení při placení“.
Následující možnosti jsou k dispozici:

- :guilabel:`Volitelné“: Zákazníci mohou nakupovat jako hosté a registrovat se později prostřednictvím objednávky
potvrzující e-mail, aby mohli sledovat svou objednávku.
- :guilabel:`Znevýhodnění (koupit jako host)“: Zákazník může provést nákup bez vytvoření účtu.
- :guilabel:`Povinné (bez hostování)“: Klienti musí přihlásit nebo vytvořit účet na
:ref:`Krok „Přezkoumání objednávky“ <ecommerce/checkout/review_order> k dokončení nákupu.“

Správa přístupu k B2B
---------------------

Omezení výdeje pouze pro vybrané zákazníky z řad B2B:

#Přejděte na „Webové stránky – Konfigurace – Nastavení“ a v poli „Obchod –
část „Proces platby“, zapněte možnost „Povinné (bez hostování)“
<ecommerce/checkout/policy> možnost.
#. Vyhledejte část „Soukromí“ a v sekci „Zákaznický účet“ vyberte
:guilabel:`Na pozvání“.
#Přejděte na webové stránky „e-commerce“ a přepněte se do pohledu „Seznam“.
a vyberte zákazníky, kterým chcete udělit přístup do svého :doc:`portálu
<../../pokrocile/user/portal>.
#Klikněte na tlačítko „Akce“ a poté na „Povolit přístup k portálu“.
#Zkontrolujte vybrané zákazníky v okně „Správa přístupu do portálu“ a klikněte
:guilabel:`Povolit přístup“.

Jakmile je vše hotovo, zákazníci obdrží e-mail potvrzující založení účtu, včetně
návod na nastavení hesla a aktivace účtu.

.. poznámka::
   - Můžete odvolat přístup nebo znovu pozvat zákazníka pomocí příslušných tlačítek v
:guilabel:`Správa přístupu do portálu“ okno.
   - Uživatelé mohou mít pouze jeden přístup k portálu na jednu e-mailovou adresu.
   - Nastavení je webu specifické, takže můžete nastavit B2C web, který umožňuje hostování a
web pro obchodníky s povinným přihlášením.

.. viz též:
   - :doc:`Dokumentace k zákaznickým účtům <customer_accounts>`
   - :doc:`Dokumentace přístupu do portálu <../../general/users/portal>`

... _ecommerce/checkout/kroky:

Kroky při placení
==============

Během procesu platby zákazníci procházejí následujícími kroky:

- :ref:`Objednávka k přezkoumání <ecommerce/checkout/review_order>“
- :ref:`Doručení <ecommerce/checkout/delivery>`
- :ref:`Další informace (pokud jsou povoleny) <ecommerce/checkout/extra_step>`
- :ref:`Platba <ecommerce/checkout/payment>`
- :ref:`Potvrzení objednávky <ecommerce/checkout/order_confirmation>`

... _ecommerce/checkout/customize_steps:

Každý krok lze upravit pomocí webového editoru přidáním bloků: doc:`
nebo otevřít záložku „Nastavení“ (:guilabel:`Customize`) a povolit různé
možnosti platby.

.. poznámka::
Obsah přidaný pomocí bloků je **specifický pro každý krok**.

.. _ecommerce/checkout/review_order:

Řazení podle recenzí
------------

Krok „Potvrzení objednávky“ umožňuje zákazníkům zkontrolovat položky, které přidali do košíku, a případně je upravit.
množství nebo: guilabel:Odebrat produkty. Informace o cenách a daních
Zobrazují se také aplikované slevy. Když zákazník kliknutím na tlačítko „Pokladna“ potvrdí, že chce pokračovat v
krok „Doručení“ (<ecommerce/checkout/delivery>).

Otevřete editor webu, abyste mohli aktivovat možnosti „pokladny“ v rámci procesu nákupu.
jako:

- :guilabel:`Doporučené doplňky“: ukázat :ref:`doplňkové produkty
<E-Commerce/Cross-Upselling/Accessory>
- :guilabel:`Slevový kód“: umožňuje zákazníkům uplatnit :ref:`dárkové poukazy <ewallet_gift/dárkové-poukazy>“
nebo použít slevový kód:
- :guilabel:`Přidat do seznamu přání“: :ref:`Zapnout seznamy přání <ecommerce/produkty/seznamy-přání>`
přihlášeným uživatelům umožnit odstranit produkt z košíku a přidat ho na seznam přání pomocí
:guilabel:`Uložit na později“ možnost.

.. poznámka::
   - Pokud je zjištěna pozice v rozpočtu (viz též :doc:`fiskální pozice <../../finance/accounting/taxes/fiscal_positions>`)
automaticky se stanoví daň z přidané hodnoty podle IP adresy zákazníka.
   - Pokud instalovaný poskytovatel platebních služeb podporuje
:ref:`rychlý nákup <platební metody/rychlý nákup>“, na kterém je zobrazena speciální tlačítko.
umožňuje zákazníkům přejít přímo z košíku na stránku potvrzení bez vyplnění
kontaktní formulář.

.. e-commerce/objednávka/doručení:

Dodání
--------

Jakmile si objednávku prohlédnou:

- Nepřihlášení zákazníci jsou vyzváni k přihlášení nebo zadání e-mailové adresy.
adresu, spolu s adresou dodání a telefonními údaji.
- Zaregistrovaní zákazníci si mohou vybrat vhodné „Adresa dodání“.

Poté si mohou vybrat způsob doručení (dopravce), zvolit nebo vložit své fakturační údaje.
Adresa (nebo přepněte na „Stejná jako adresa pro dodání“ pokud je fakturační a dodací adresa stejná)
adresy jsou shodné) a klikněte na tlačítko „Potvrdit“.

..tip:
   - Pro firemní zákazníky je možné také :ref:`zapnout <ecommerce/checkout/customize_steps> volitelné
:guilabel:`DPH“ a :guilabel:`Název společnosti“ políčka přepínáním tlačítka :guilabel:`Zobrazit firemní pole“.
možnost v editoru webových stránek.
   - Můžete přidat zaškrtávací políčko pro uživatele bez účtu k přihlášení k odběru novinek. Chcete-li tak učinit, postupujte podle následujících kroků:
do: „Webová stránka -> Konfigurace -> Nastavení“. Pod položkou „Obchod“
v sekci „Objednávkový proces“ zapněte funkci „Zprávy“ a vyberte
:label:`Seznam pro zasílání novinek`.

.. e-shopu / pokladna / další krok:

Doplňující informace
----------

Můžete přidat krok „Další informace“ v procesu objednávky, abyste shromáždili další informace od zákazníků.
informace prostřednictvím online formuláře, který je pak zahrnut do objednávky na prodej.
<obsluha/prodej>. Proto je nutné aktivovat <e-commerce/checkout/customize_steps> a <guilabel>Extra
Možnost v editoru webu. Formulář lze upravit podle :ref:`vlastních potřeb <website/building_blocks/form>
dle potřeby.

..tip:
Alternativně přejděte na: „Webová stránka --> Konfigurace --> Nastavení“, posuňte se dolů
v části „Obchod – proces objednávky“, zapněte „Další krok při objednávce“ a
Klikněte na tlačítko „Uložit“. Klikněte na ikonu „Pravý směr“ a poté na „Upravit formulář“, abyste jej upravili podle svých představ.

.._e-shop/objednávka/platba:

Platba
-------

V kroku „Způsob platby“ si zákazníci vyberou způsob platby, zadají své platební údaje
podrobnosti a klikněte na „Zaplať teď“.

Můžete požadovat, aby zákazníci souhlasili s vašimi :doc:`podmínkami a pravidly.
<../../finance/accounting/customer_invoices/terms_conditions>` před zaplacením. Chcete-li toto nastavení povolit, přejděte na
„Nastavení kroků“ v nabídce „E-shop / Objednávka / Nastavení kroků“, přejděte do editoru webových stránek a změňte
:guilabel:`Přijmout podmínky a ustanovení“ funkci.

..tip:
Zapněte režim vývojáře pomocí tlačítka „Vývojářské prostředí“ (viz ikona „Bug“).
ikonu zobrazit hlášení o dostupnosti platebních metod.
poskytovatelé a způsoby platby, což pomáhá diagnostikovat potenciální problémy s dostupností plateb.
formulář.

.. e-commerce/checkout/order_confirmation:

Potvrzení objednávky
------------------

Posledním krokem procesu objednávky je potvrzení objednávky, které poskytuje
Shrnutí informací o nákupu zákazníka.

.. viz též:
:doc:`Dokumentace k zpracování objednávek <order_handling>`
