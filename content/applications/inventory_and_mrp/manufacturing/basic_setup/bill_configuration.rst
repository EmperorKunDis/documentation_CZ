=================
Seznam součástí
=================

.. |BOM| nahradit za: zkratka: `BoM (Bill of Materials)`
.. |BOMy| nahrazují:: :abbr:`BOMs (Seznamy materiálů)`
.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`

Seznam komponent (nebo zkráceně BoM) dokumentuje konkrétní součástky spolu s jejich
odpovídající množství potřebné k výrobě nebo opravě produktu. V Odoo slouží jako
návrhy výrobků a sestav, často obsahují výrobní operace a postupy.
směrnic.

BoM nastavení
=========

Pro vytvoření |BOM| přejděte na :menuselection:`Výroba --> Produkty --> Seznamy materiálů`.
Klikněte na „Nový“.

Dále nastavte pole „Typ BoM“ na „Výroba tohoto produktu“.

Pak specifikujte požadované komponenty:ref:`<manufacturing/basic_setup/setup-components>`, a pokud
nutné, definujte jakékoliv:ref:`výrobní operace <výroba/základní nastavení/nastavení operací>“.

..tip:
Individuální BOM lze také rychle otevřít nebo vytvořit kliknutím na tlačítko „Faktura“.
Tlačítko „Chytrý materiál“ na jakémkoliv produktu v podobě přístupného prostřednictvím položek *Prodej*, *Sklad* a
Aplikace pro výrobu, stejně jako všechny vnitřní odkazy na produkt.
jako v poli nebo ve sloupci.

.. obrázek:: bill_configuration/bom-example.png
:align:center
:alt:Zobrazte seznam komponent produktu.

BoM pro „Šuplík“, zobrazující kartu **Součásti**.

.. viz také:
   - :doc:`../pokrocile_konfigurace/dodani_sady`
   - :doc:`../poddodavatelska_praxe/poddodavatelska_praxe_zacinaci`

.. výroba/základní nastavení/součásti nastavení:

Součásti
----------

V kartě „Součástky“ v seznamu BOM zadejte součásti použité při výrobě produktu.
Klikněte na tlačítko „Přidat řádek“. Vyberte z rozevírací nabídky „Komponenty“
existující produkty nebo vytvořit nový produkt, zadáním názvu a výběrem buď
:guilabel:`Vytvořit „“ pro rychlé přidání položky nebo :guilabel:`Vytvořit a upravit...“
možnost přidat komponentu a pokračovat do jejího konfiguračního formuláře.

.. obrázek: bill_configuration/komponenta.png
:align:center
:alt:Komponentu přidejte vybráním z nabídky.

Pokud chcete, můžete přidat další pole kliknutím na ikonu „Nastavení“ (viz ikona oi-settings-adjust).
„Komponenty“ kartě vpravo dole. Zatrhněte zaškrtávací políčka u
následující funkce, aby se tyto sloupce zobrazily:

- Vyberte, na které varianty se aplikace vztahuje.
<../advanced_configuration/product_variants> každý komponent používá. Pokud pole necháte prázdné,
je prázdný, komponent se používá ve všech variantách produktu.

... výroba/základní nastavení/spotřeba při provozu:

- Specifikujte operaci pomocí komponenty. Užitečné pro
určení :ref:`připravenosti k výrobě <výroba/základní nastavení/připravenost k výrobě>“.
- :guilabel:`Nutnost ručního spotřebování“: zaškrtněte políčko, abyste operátorům
:guilabel:`Spotřeba“ zaškrtávací políčko v objednávce výroby (MO).

.... obrázek: bill_configuration/consumed-field.png
:align:center
:alt:Zobrazit výrobní objednávku s vyznačeným polem *Využito*.

Pokud tak neučiníte, vyvolá se chybová hláška „Varování o spotřebě“, kde je uvedené množství spotřebovaného
V opačném případě nelze operaci dokončit.

.... obrázek:bill_configuration/consumption-warning.png
:align:center
:alt:Zobrazit varovný výstražný text spotřeby.

... výroba/základní nastavení/nastavení operací:

Operace
----------

Přidejte k BOM operaci, která specifikuje pokyny pro výrobu a zaznamenává čas strávený na
operaci. Chcete-li tuto funkci používat, nejprve zapněte funkci „Pracovní příkazy“ přechodem na
:menuvolba:`Výroba“ -> „Konfigurace“ -> „Nastavení“. V části „Operace“
sekci, zaškrtněte políčko „Dodací listy“ a zapněte funkci.

.. viz také:
:doc:`../pokrocile_konfigurace/zavislosti_objednávky_na_práci“

.. obrázek: bill_configuration/enable-work-orders.png
:align:center
:alt:"Možností objednávek" v nastavení stránky.

Dále přejděte na stránku BOM kliknutím na tlačítko „Výrobní aplikace“ v nabídce „Nástroje“ a poté na „Produkty“ a „Bill of Materials“.
Materiály a výběrem požadovaného BOM. Chcete-li přidat novou operaci, přejděte na :guilabel:`Operace`.
tabu, klikněte na tlačítko „Přidat řádek“.

Tím se otevře okno „Vytvoření operací“, kde jsou různá pole pro
operace jsou konfigurovány:

- :guilabel:`Operace“: název operace.
- :guilabel:„Zaměstnání“: vyberte existující místo pro provedení operace nebo vytvořte nové pracoviště.
Vytvořte centrum zadáním názvu a výběrem možnosti „Vytvořit „“.
- :guilabel:`Aplikovat na varianty“: specifikujte, zda je tato operace k dispozici pouze pro určité produkty
varianty. Pokud se operace vztahuje na všechny produktové varianty, nechte pole prázdné.

......viz také:


- :guilabel:'Počítání doby trvání': vyberte, jakým způsobem je sledováno čas strávený na operaci.
:guilabel:`Výpočet na základě sledované doby“ použít časový sledovač operace nebo :guilabel:`Nastavit
„Délka manuálně“ pokud mohou operátoři sami zaznamenat a upravit čas.

Vybráním možnosti „Počítat podle sledované doby“ se aktivuje volba „Na základě poslední
__ možností pracovních příkazů, která automaticky odhadne dobu potřebnou k dokončení této operace na základě
posledních několik operací. Vybráním možnosti „Manuálně nastavit dobu“ se aktivuje volba „Výchozí
V poli Délka namísto toho.
- :guilabel:`Délka výchozího trvání“: odhadovaná doba, po kterou bude operace probíhat; používá se k
„Plánování výrobních objednávek“ a „Určení
„Dostupnost pracovních míst <https://www.youtube.com/watch?v=3YwFlD97Bio>“.
- :guilabel:`Společnost“: určete společnost, pro kterou je k dispozici BOM.

Vložte podrobnosti o operaci do záložky „Pracovní list“. Vyberte možnost „PDF“ pro připojení souboru
nebo:guilabel:`Google Slide“ s veřejným přístupem, abyste mohli sdílet odkaz. Vyberte „Text“, abyste mohli psát
návod v poli popisu.

..tip:
Pro zobrazení seznamu formátovacích možností a funkcí včetně ChatGPT stiskněte klávesu /.

... obrázek: bill_configuration/description.png
:srovnání: do středu
:alt:Zobrazte funkci ChatGPT, která generuje pokyny pro pracovní příkaz.

.. obrázek:bill_configuration/create-operations.png
:align:center
:alt: Vyplňte okno vytvoření operací.

Konečně klikněte na tlačítko „Uložit a zavřít“ pro uzavření okna s upozorněním. Chcete-li přidat další operace, klikněte
„Uložit a nový“ a opakujte stejné kroky výše, abyste nakonfigurovali další operaci.

.. poznámka::
Každá operace je unikátní, protože je vždy exkluzivně spojena s jedním |BOM|.

..tip:
Poté, co vytvoříte operaci, klikněte na tlačítko „Kopírovat existující operace“ a vyberte ji.
operace duplikátu.

.... obrázek:bill_configuration/copy-existing-operations.png
:srovnání: do středu


Návod
~~~~~~~~~~~~

.. důležité::
Pokud chcete přidat podrobné pokyny k operacím, musíte nainstalovat aplikaci Quality.

Přidejte konkrétní pokyny k existující operaci klepnutím na ikonu operace :icon:`fa-list-ul`.
:guilabel:`(seznam)` ikona v sloupci :guilabel:`Návod k použití“. Číslo v
Sloupec „Návod“ ukazuje, kolik podrobných návodů existuje pro
operace.

.. obrázek: bill_configuration/add-instructions.png
:align:center
:alt:Zobrazte sloupec Návod a ikonu seznamu.

Na panelu „Kroky“ klikněte na „Nový“, abyste otevřeli prázdnou formulářovou stránku pro kontrolní bod.
kde lze nový výrobní krok vytvořit. Zde je třeba konkrétně instruovat
„Název“ a nastavte „Typ“ na „Pokyny“.
V záložce „Návod“ vytvořte pokyny pro krok operace.

.. poznámka::
Další úpravy lze provést zde na tomto formuláři, kromě běžných pokynů, také
zahrnují specifické kontrolní body kvality, které mají specifické (nebo složité) podmínky.
více informací o kontrolních bodech kvality najdete v :doc:`Návodu na kontrolu
dokumentace k typu kontroly „Návod“.

.. obrázek: bill_configuration/steps.png
:align:center
:alt:Zobrazit stránku pro přidání kvality.

Různé
-------------

V záložce „Různé“ najdete víc možností |BoM| pro konfiguraci nákupu.
vypočítat náklady a definovat spotřebu komponentů.

... výroba/základní nastavení/výrobní připravenost:

- :guilabel:"Připravenost k výrobě": vybrat "Když jsou komponenty pro první operaci
„K dispozici“ zobrazuje :guilabel:`Stav komponenty“ jako „zelené“ :guilabel:`Není k dispozici“.
jenom součástky, které jsou spotřebovány v první operaci, jsou skladem. To ukazuje na
I když nejsou k dispozici všechny komponenty, operátoři mohou začít alespoň s první operaci.
Vybráním možnosti „Když jsou všechny komponenty k dispozici“ se zobrazí červený **upozornění** „Není
Pokud je stav komponenty k dispozici, není-li všechny komponenty dostupné.

..tip:
Specifikujte, která operace spotřebovává každou složku na BoM v části „Manuální spotřeba“ ve výkladovém slovníku.
pole <výroba/základní nastavení/spotřeba při provozu>`.

.... obrázek: bill_configuration/component-status.png
:align:center
:alt:Zobrazte pole „Stav komponenty“ na kartě výrobního příkazu.

- :guilabel:`Verze“: zobrazuje aktuální verzi |BoM|, která je viditelná pouze s aplikací *PLM*
pro správu změn |BoM|.
- :guilabel:`Přístupná spotřeba“: specifikuje, zda lze použít komponenty v množství odlišném od toho uvedeného.
definované na BoM. Zvolte:guilabel:`Blokované“ pokud operátoři musí striktně dodržovat
|BoM| množství. Jinak zvolte možnost :guilabel:`Povolené“ nebo :guilabel:`Povoleno s varováním“.
- :guilabel:`Doprava“: vyberte typ výrobní operace pro produkty v preferovaném skladu
vyráběné v několika skladech. Pokud je pole nevyplněno, pak se použije typ operace „Výroba“ pro tento sklad.
je používán výchozím nastavením.
- Vyberte předdefinované analytické distribuční modely:
zadaný v seznamu automaticky uložit.
cenu výroby produktů v zvoleném časopise.
- :guilabel:„Doba dodání výrobku“: definujte počet dní potřebných k dokončení |MO| od data
potvrzení.
- :guilabel:`Dny potřebné k vyřízení objednávky na výrobu“: počet dní nutných k doplnění součástek.
vyrábět podsestavy produktu.

.. viz také:
   - :doc:`Analytická účetní evidence <../../../finance/accounting/reporting/analytic_accounting>`
   - :doc:`Doba dodání <../../skladovani/dodavky/dodavky_zbozi/dodacni_doby>`

.. obrázek: bill_configuration/misc-tab.png
:align:center
:alt:Zobrazte záložku „Různé“ v BoM.

Přidejte vedlejší produkty do BOMů
=======================

Přípravek je vedlejším produktem, který vzniká při výrobě navíc k hlavnímu
produkt vedlejšího výrobku. Na rozdíl od primárního produktu může být na BOM více vedlejších produktů.

Přidat vedlejší produkty do BOM lze po zapnutí funkce *Vedlejší produkty*.
:menuvolba:`Výroba“ -> „Konfigurace“ -> „Nastavení“. V části „Operace“
sekci, zaškrtněte políčko pro :guilabel:`Případy“ a zapněte tuto funkci.

.. obrázek: bill_configuration/by-products.png
:align:center
:alt:"Možností By Products" v nastavení stránky.

Jakmile je tato funkce zapnutá, přidejte vedlejší produkty do BOM klepnutím na záložku :guilabel:`Vedlejší produkty`.
Klikněte na tlačítko „Přidat řádek“ a vyplňte pole „Výrobní odpad“, „Množství“ a
„Jednotka měření“. Volitelně můžete zadat „Vyrobeno v operaci“ pro
případný vedlejší produkt.

Příklad:
Případný vedlejší produkt „Mush“ vzniká při výrobě červeného vína jako vedlejší produkt operace „Lisování hroznů“.

.... obrázek: bill_configuration/add-by-product.png
:srovnání: do středu
:alt:Zobrazte ukázkový vedlejší produkt v BoM.
