===================
Vrácení a vrácení peněz
===================

Aplikace Odoo Sales nabízí dvě různé možnosti zpracování vrácených zboží.
Zda byla faktura vystavena či nikoliv.

Před vystavením faktury
================

Vrácení zboží se provádí pomocí funkce „Zpětný převod“ v případě, když zákazník rozhodne vrátit produkt.
Před odesláním nebo ověřením faktury.

.. poznámka::
Pokud chcete používat funkci Reverse Transfers, musíte mít nainstalovanou aplikaci Inventory.

Pro zahájení vrácení před fakturací přejděte do aplikace „Prodej“, vyberte požadované
objednávku a klikněte na tlačítko „Dodání“ chytré etikety, abyste otevřeli spojenou dodávku.
pořádku.

.. obrázek: vratky-a-dodani-klavesnice-chytrosti.png
:align:center
:alt: Typická objednávka s vyznačeným tlačítkem pro dodání v Odoo Sales.

Na potvrzené dodací objednávce klikněte na „Zpět“.

.. obrázek: vraceni-zbozi-v-doby-platnosti-objednavky-tlacitko.png
:align:center
:alt: Potvrzená objednávka s vyznačeným tlačítkem Vrácení v Odoo Sales.

Otevře se okno „Zpětná převod“.

Výchozí hodnota položky :guilabel:`Množství` odpovídá ověřeným množstvím z objednávky dodání.
Aktualizujte množství, pokud je třeba. Klikněte na ikonu „koš“ vedle položky
Odebrat ji z vrácení.

.. obrázek: návrat/obrácený přenos - okno.png
:align:center


Dále klikněte na tlačítko „Vrácení“ pro potvrzení vrácení. To vygeneruje novou operaci skladu.
vrácené zboží.

.. obrázek: vratka-zbozi-potvrzena.png
:align:center
:alt:Skladová operace po potvrzení vrácení v Odoo Sales.

Po obdržení vráceného zboží ověří tým skladu správnost provedené operace kliknutím
:guilabel:`Zkontrolovat“. Poté se na původním prodejním dokladu aktualizuje množství „Dodáno“
odrážejí rozdíl mezi počátečními ověřenými množstvími a vracenými množstvími.

.. obrázek: vratky-prodanych-kusu.png
:align:center
:alt: Aktualizované množství dodaného zboží na objednávce po zpětném převodu.

Při vystavení faktury obdrží zákazník pouze fakturu za produkty, které si objednal.
Pokud nějaká taková existuje.

Po vystavení faktury
===============

Občas se zákazníci vrací s položkou poté, co obdrží a zaplatí fakturu.
případů je použití pouze zpětných převodů nedostatečné, protože jsou v případě platných nebo odeslaných faktur
nemůže být změněna.

Nicméně Reverse Transfer může být použit v kombinaci s Credit Note, aby bylo možné dokončit
vrácení zboží zákazníkem.

Pro zahájení vrácení po fakturaci přejděte na příslušnou objednávku prodeje.
:menuselection:`Prodejce“ aplikace.

Pokud je na prodejním příkazu zadána platba, objeví se v chatu podrobnosti o platbě.
faktura (dostupná přes tlačítko „Faktury“ v horní liště) má zelený „Vyřízeno“
Banner „Platba“.

.. obrázek: vrací/zelenou-v-platbě-banneru.png
:align:center
:alt: Vzorek zelené barvy v reklamním pásu prodeje v Odoo Sales.

Klikněte na tlačítko „Dodání“ v objednávce prodeje, abyste zobrazili ověřené dodání.
Poté klikněte na tlačítko „Návrat“. Otevře se okno s názvem „Odvolání“.

Poté upravte položky „Produkt“ a „Množství“, pokud je třeba. Potom
Klikněte na „Vrácení“. To vytvoří novou operaci skladu pro vracené zboží.
produktu, který je ověřen týmem skladu poté, co bude vrácená objednávka přijata kliknutím
:guilabel:`Zkontrolovat“.

Poté se na objednávce prodeje aktualizuje množství „Dodáno“ o rozdíl.
mezi počty zboží, které bylo původně schváleno a zboží, které bylo vráceno.

Pro vrácení peněz přejděte na příslušnou fakturu (od objednávky klikněte na
Klikněte na tlačítko „Faktura“ (viz obrázek výše) a poté klikněte na tlačítko „Přijatá faktura“ v horní části
ověřená faktura.

.. obrázek: vraceni-zbozi-tlacitko.png
:align:center
:alt: Běžná faktura zákazníka s tlačítkem Kreditní poznámky zvýrazněným v Odoo Sales.

Tím se zobrazí okno „Poznámka o kreditu“.

.. obrázek: vraceni-zbozi-pop-up-form.png
:align:center
:alt: Běžný výpisek o úvěru, který se objevuje v Odoo Sales.

Začněte zadáním důvodu „Výpis kreditu“ a konkrétního „Deníku“.
zpracovat úvěr. Pak vyberte konkrétní datum „Odvolání“.

Po vyplnění informací klikněte na „Zpět“ nebo „Zpět a vytvořit“.
Faktura“. Poté upravte návrh, pokud je třeba.

Poté klikněte na tlačítko „Potvrdit“ a potvrďte fakturu.

Když byla hotová modrá páska s nápisem „Máte u tohoto zákazníka nedoplatky“.
Můžete je přidělit a tuto fakturu označit jako zaplacenou.“

.. viz též:
:doc:`/účetnictví/fakturace/dodací listy/přepravní doklady“
