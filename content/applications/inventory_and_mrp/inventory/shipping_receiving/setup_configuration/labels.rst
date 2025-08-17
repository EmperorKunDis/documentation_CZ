=====================
Tisk štítků pro zaslání
=====================

.. |DO| nahradit za: :abbr:`DO (Dodací příkaz)`
.. |SO| nahradit za: :abbr:`SO (Prodejní objednávka)`

Integrovat Odoo s externími dopravci
„/nastavení/konfigurace/třetí strana dopravce“ automaticky vytváří štítky s adresou.
obsahuje ceny, adresy destinace, sledovací čísla a čárové kódy.

.. viz také:
:ref:`Automaticky tisknout štítky dopravce <Inventář / Přijímání a výdej / Štítky dopravce>“

Konfigurace
=============

Pro vytvoření štítku pro třetí stranu dopravce nejprve nainstalujte třetí stranu dopravce.
Konektor <../setup_configuration/third_party_shipper>“. Pak konfigurujte a aktivujte
:ref:`metoda doručení <Inventář/Přijímání a expedice/Nastavení metody doručení>“, přičemž je třeba nastavit
úroveň integrace na „Získat sazbu a vytvořit zásilku“ k vygenerování poštovného
Štítky. Nakonec zadejte adresu zdroje společnosti:
<inventar/versand/konfigurieren-quelladresse>“ a „:ref:„produktgewichte
<Inventar/Versand/Gewicht konfigurieren>.

.. viz také:
:doc:`../nastavení/třetí strana dopravce“

.. obrázek: labels/integration-level.png
:align:center
:alt:Zvolte možnost „Vypočítat sazbu a vytvořit zásilku“.

... inventář/příjem/vyskladnění konfigurace:

Štítky pro vícestupňové
---------------------

Pro společnosti, které používají dva nebo tři kroky v procesu přijetí a dodání zboží.
Dodání <../denní operace/dodání tří kroků>“, štítky mohou být vyvolány pro tisk po
ověření vybírání nebo balení. Chcete-li to provést, přejděte na:
Konfigurace --> Typy operací, vyberte požadovanou operaci.

Na stránce konfigurace „Typ operace“ zaškrtněte políčko „Tisk štítku“.
Aktivací této funkce se zajistí, že třetí strana bude mít k dispozici štítek pro odeslání po ověření.
operace.

Příklad:
pro dvoufázovou dodávku (viz. 2. krok přijímání a dodávky produktů), kde jsou produkty
jsou umístěny přímo do balení při sklizni, společnosti mohou vytisknout štítky s adresami během
vyzvednutí místo dodání. Odoo umožňuje uživatelům zapnout funkci :guilabel:`Tisk štítku`.
sám o sobě, aby dosáhl této pružnosti.

.... obrázek: labels/pick-print-label.png
:srovnání: do středu
:alt:Zapněte funkci „Tisk štítku“.

Tisk etiket sledování zásilky
=====================

Štítky pro sledování jsou tištěny při ověření konkrétních operací. Výchozí nastavení ověřuje
dodací příkaz (DO) generuje sledovací štítek v chatu.

.. poznámka::
Pro společnosti používající dvou nebo tří kroků dodání se obraťte na :ref:`tisk etiket pro vícefázovou
sekci „Dodání“ v části „Skladování, přijímání a vyzvedávání zboží“, kde se dozvíte, jak tisknout štítek.
po ověření vyskladnění nebo balení.

Pokud jsou nainstalovány obě aplikace, začněte v aplikaci „Prodej“.
a pokračujte do požadované citační nebo objednávky prodeje (SO). Tam přidejte náklady na dopravu
„Přidat cenu dopravy“ k objednávce. Pak přejděte na odkazovanou položku „Dodání a příjem“ —
nebo jiného typu operace při vícekrokové dodávce - k ověření operace a tisku
Štítek.

Pokud je nainstalován pouze program Inventář, vytvářejte přímo v něm :abbr:`DOs (Dodací objednávky)“.
Aplikace „Vybavení“ (menu „Zařízení“), doplněk „Dodavatel třetích stran“.
„Validovat tisk štítku“ v poli „Dopravce“, a poté
|DO|.

...Inventarizace, přijímání a vkládání dodacích nabídek:

Připočtěte poštovné na cenovou nabídku
-------------------------

Chcete-li vytvořit sledovací štítek objednávky, začněte tím, že vytvoříte nabídku v sekci „Prodej“
app --> Objednávky --> Nabídky“, klikněte na „Nový“ a vyplňte formulář nabídky. Pak
klikněte na tlačítko „Přidat dopravu“ v pravém dolním rohu cenové nabídky.

.. obrázek: labels/add-shipping-button.png
:align:center
:alt:Zobrazit tlačítko „Přidat dopravu“ na cenovém odhadu.

V okně, které se zobrazí, vyberte požadovaného dopravce ze seznamu „Doprava“.
položky nabídky. Hodnota pole :guilabel:`Celková hmotnost objednávky` se automaticky vyplní na základě
:ref:`váha produktů v objednávce <Inventář/Přijetí a odeslání zboží/Nastavení váhy>“. Upravte tento
pole pro přepsání předpokládané hmotnosti a použít tuto hmotnost k odhadování nákladů na dopravu.

Dále klikněte na „Zobrazit cenu dopravy“ a zobrazte zákazníkům náklady na dopravu prostřednictvím třetí strany.
dodavatele v poli „Náklady“.

.. důležité::
Pokud kliknutím na tlačítko „Získat sazbu“ dojde k chybě, zkontrolujte adresu skladu.
<inventarizace/přijetí a výdej/nastavení zdroje adresy> a :ref:`váha produktů v
musí být správně nakonfigurována.

Klikněte na tlačítko „Přidat“ pro přidání nákladů do cenové nabídky, která je uvedena jako :ref:`konfigurovaná
Dodací produkt <Inventář/Přijetí zboží/Dodací produkt>“. Nakonec klikněte
Potvrďte citaci a klikněte na tlačítko „Dodání“ pro přístup
|DO|.

.. obrázek: labels/get-rate.png
:align:center
:alt:Zobrazit okno „Výpočet sazby“.

..tip:
Pro uživatele, kteří aplikaci *Sales* nemají nainstalovanou, zadejte :guilabel:`Carrier` po přechodu na
aplikaci „Výbava“, přejděte na |DO| a poté do
:guilabel:`Další informace“ v záložce.

.... obrázek: labels/additional-info-tab.png
:srovnání: do středu
:alt:Zobrazte kartu „Další informace“ objednávky dodání.

… inventarizaci, přijímání a ověřování tisknutých štítků:

Potvrzení objednávky
-----------------------

Vyberte si v objednávce dodání možnost „Další informace“, abyste se ujistili, že třetí strana
do pole :guilabel:`Dodavatel dopravy` byl přidán dopravce.

.. důležité::
Pokud není aplikace Sales instalována, je třetí stranou nastavený dopravce v poli Carrier.
pole.

Po zabalení položek objednávky klikněte na tlačítko „Ověřit“ a získejte informace o dopravě.
číslo sledování dopravce a vytvořit štítek pro zaslání.

.. poznámka::
Vytvořte nebo vyberte již existující dodací objednávku v aplikaci „Sklad“ pomocí tlačítka :menuselection:`Inventory`.
vybráním karty „Objednávky dodání“.

Číslo „Referenční číslo“ je vygenerováno v záložce „Další informace“.
dodací příkaz. Klikněte na tlačítko „Sledování“ a přejděte na odkaz sledování zásilky
webové stránky dopravce.

Štítek sledování je uložen v formátu PDF ve zprávě.

.. obrázek:labels/doprava-zboží.png
:align:center
:alt:V chatovacím okně zobrazit generovanou štítek s adresou.

.. poznámka::
Pro vícebalíkovou zásilku se vytváří jeden štítek na balík. Každý štítek je pak viditelný
hádky.

.. obrázek:: /soubory/příklad-etikety.png
:align:center
:alt: Vzorek štítku vygenerovaný z připojení k dodání společnosti Odoo s FedEx.

Vzorek štítku vygenerovaný z připojení k dodání v Odoo s FedEx.

.. viz také:
   - :doc:`fakturace“
   - :doc:`balení více produktů“
