===================
Fakturační procesy
===================

V závislosti na vašem podnikání a aplikaci, kterou používáte, jsou
různé způsoby automatizace vytváření faktur pro zákazníky v Odoo.
Obvykle se vytváří zálohové faktury systémem (s informacemi
přicházející z jiných dokumentů (například objednávky nebo smlouvy).
účetní jen musí schválit návrh faktury a odeslat fakturu.
výtisk (poštou nebo e-mailem).

V závislosti na vašem podnikání můžete zvolit jednu ze dvou následujících možností.
vytvářet návrhy faktur:

Prodej
=====

Prodejní objednávka ‣ Faktura
---------------------

V většině společností vytváří obchodníci cenové nabídky, které se stávají objednávkou na prodej.
Jakmile jsou ověřeny, vytváří se návrh faktury na základě
prodejní objednávka. Máte různé možnosti, například:

-  Faktura ručně: použijte tlačítko na prodejním příkazu k vyvolání návrhu
faktura

-  Faktura před dodáním: fakturujte celou objednávku před spuštěním
dodací list

-  Faktura na základě dodacího listu: viz další část

Faktura před dodáním je obvykle využívána v elektronickém obchodování.
Když zákazník zaplatí objednávku a my mu ji dodáme později.
předplacená

Pro většinu ostatních případů je doporučeno fakturovat ručně.
umožňuje obchodníkovi vyvolat fakturu na požádání s možnostmi:
fakturovat celou objednávku, fakturovat procenta (zálohu), fakturovat něco
účetní doklady (faktura, daňový doklad), účetní záznamy o přijaté platbě a fixní záloha.

Tento proces je dobrý jak pro služby, tak i fyzické produkty.

.. viz též:
   - :doc:`/aplikace/obchod/fakturace/přijaté objednávky/dodací listy/proforma“

Prodejní objednávka ‣Dodací objednávka ‣Faktura
--------------------------------------

Obchodníci a e-commerce obvykle fakturují na základě dodacích listů.
místo objednávky na prodej. Tento přístup je vhodný pro podniky, kde
množství, které dodáte, se může lišit od objednaného množství:
potraviny (faktura podle skutečného kg).

Takže pokud dodáte částečný údaj, budete si moci účtovat jen za to, co jste
opravdu dodal. Pokud máte zadané opakované objednávky (dodáváte částečně a zbytek
(později) zákazník obdrží dvě faktury, jednu za každou dodávku
pořádku.

.. viz též:
   - :doc:`/aplikace/prodej/prodej/fakturace/fakturační politika

e-commerce objednávka ‣ faktura
-------------------------

Objednávka v oblasti elektronického obchodu také vyvolá vytvoření objednávky, když
je úplně zaplacená. Pokud umožňujete platbu šekem nebo bankovním převodem
Odoo vytvoří pouze objednávku a faktura bude vyvolána až po
Peníze jsou připsány na účet.

Smlouvy
=========

Pravidelné smlouvy ‣ Faktury
----------------------------

Pokud používáte smlouvy, můžete vystavit fakturu na základě času a materiálu.
vynaložené náklady nebo fixní služby/produkty. Každý měsíc
Prodejce vygeneruje fakturu na základě aktivit v rámci smlouvy.

Aktivitou může být například:

-  pevné produkty/služby, které vycházejí z prodejního příkazu spojeného s tímto kontraktem
-  nakoupené materiály (které budete znovu fakturovat).
-  čas a materiál na základě časových listů nebo nákupu (dodavatelské pracovníky)
-  náklady, jako jsou například cestovné a ubytování, které fakturujete zákazníkovi

Fakturaci lze provést na konci smlouvy nebo vyvolat v průběhu
fakturami. Tento přístup používají společnosti poskytující služby, které vystavují
Hlavně na základě času a materiálu. U služebních firem, které fakturují
Na pevnou cenu používají běžnou prodejní objednávku.

.. viz též:
   - :doc:`/aplikace/prodej/prodej/fakturace/čas a materiál
   - :/applications/sales/sales/invoicing/expense
   - :doc:`/aplikace/prodej/prodej/fakturace/milník`

Opakující se smlouvy ‣ Faktury
------------------------------

Pro předplatné je vyvolávána faktura automaticky a pravidelně.
Četnost fakturace a služeb/produktů, které jsou na faktuře uvedeny,
Uvedené v smlouvě.

.. viz též:
   - :/applications/sales/subscriptions

Ostatní
======

Vytvoření faktury ručně
----------------------------

Uživatelé mohou také vytvářet faktury ručně bez použití smluv nebo
objednávka prodeje. Je to doporučený přístup, pokud nemusíte řídit
prodejní proces (nabídky), nebo dodání zboží.
služby.

I když vám fakturu vygeneruje objednávka na prodej, může se stát, že budete muset
výjimečně vytvářet faktury ručně:

-  Pokud potřebujete vytvořit odstoupení.

-  Pokud chcete poskytnout slevu

-  pokud potřebujete změnit fakturu vytvořenou z objednávky na prodej

-  pokud potřebujete vystavit fakturu za něco, co není součástí vašeho hlavního podnikání

Specifické moduly
----------------

Některé specifické moduly jsou schopné vytvářet i návrhy faktur:

-  Členství: fakturujte členům každý rok

-  **opravy**: fakturujte pozáruční servis

Reorganizace faktur
----------------------------

Je možné sekvenovat faktury, ale s několika omezeními:

#Tato funkce nefunguje, pokud je záznam starší než datum uzamčení.
#Tato funkce nefunguje, pokud je sekvence nesourodá s měsícem vstupu.
#Nesmí vzniknout duplicitní sekvence.
#Zůstává zachována původní pořadí faktury.
#Je užitečná pro lidi, kteří používají číslování z jiného softwaru a chtějí pokračovat v
aktuálním rokem bez nutnosti začít od začátku.

Digitální fakturace s optickým rozpoznáváním znaků
-------------------------------------------------------------

**Digitální fakturace** je proces automatického kódování klasických papírových faktur do
faktury v účetnictví.

Odoo využívá technologie optického rozpoznávání znaků a umělé inteligence k rozpoznání obsahu dokumentů.
Formuláře faktur dodavatelů a zákaznických faktur jsou automaticky vytvářeny a doplňovány na základě skenovaných
faktury.

.. viz též:
   - :doc:`/aplikace/finance/účetnictví/fakturace/digitalizace faktury“
