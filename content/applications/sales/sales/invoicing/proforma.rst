==================
Proforma faktury
==================

Pro forma faktura je zkrácený nebo odhadovaný daňový doklad zasílaný před dodáním zboží.
poznamenává druh a množství zboží, jeho hodnotu a další důležité informace, například váhu
a dopravní poplatky.

Proforma faktury se běžně používá jako předběžná faktura s cenovou nabídkou.
Při dovozu pro celní účely se liší od běžné faktury tím, že nejsou
požadavek na zaplacení.

Konfigurace
=============

Pokud chcete využívat faktury typu „pro forma“, musí být zapnutá funkce „Faktura typu „pro forma““.

Tuto funkci lze zapnout v sekci „Prodejní aplikace“ -> „Konfigurace“ -> „Nastavení“.
V sekci „Citace a objednávky“ klikněte na zaškrtávací políčko vedle „Předběžná faktura“.
Faktura“. Pak klikněte na „Uložit“ a uložte všechny změny.

.. obrázek: proforma/pro-forma-setting.png
:align:center
:alt:Nastavení funkce faktury předem v aplikaci Odoo Sales.

Vystavte fakturu naúčet
======================

Pokud je aktivována funkce „Pro-Forma Invoice“, můžete odeslat fakturu na základě předběžného souhlasu.
nyní dostupné na jakémkoliv citaci nebo objednávce, prostřednictvím tlačítka „Vystavit předběžnou fakturu“.

.. obrázek: proforma/send-pro-forma-invoice-button.png
:align:center
:alt:Tlačítko „Vystavit předběžnou fakturu“ na typické objednávce v Odoo Sales.

.. poznámka::
Pokud je v objednávce nebo cenové nabídce faktura, nelze proforma fakturu zaslat.
platba již byla odeslána nebo se jedná o opakující se předplatné.

V každém případě se tlačítko „Odeslat fakturu“ nezobrazuje.

Pro forma faktury však mohou být vystaveny za služby, registrace na akci, kurzy a podobně.
nové předplatné. Předběžná faktura není omezena pouze na fyzické, spotřební nebo skladovatelné zboží.

Když je kliknut na tlačítko „Vystavit předběžnou fakturu“, objeví se okno s výzvou.
může být odeslána e-mailová zpráva.

V okně přesunutí se pole „Příjemci“ automaticky vyplní zákazníkem z
objednávka nebo cenová nabídka. V poli „Předmět“ a v těle e-mailu lze provádět úpravy
pokud je třeba.

Proforma faktura se automaticky připojí jako příloha k e-mailu.

Když je vše připravené, klikněte na tlačítko „Odeslat“ a Odoo okamžitě pošle e-mail s přílohou faktury.
faktura zákazníkovi.

.. obrázek: proforma/pro-forma-email-message-pop-up.png
:align:center
:alt:Okno e-mailu, které se objeví s fakturou v Odoo Sales.

..tip:
Před zobrazením faktury vám stačí kliknout na PDF níže.
pop-up okno před kliknutím na tlačítko „Odeslat“. Po kliknutí se otevře faktura.
okamžitě stažené. Otevřete soubor PDF, abyste si mohli prohlédnout a zkontrolovat fakturu.

.. obrázek:: proforma/pro-forma-pdf.png
:synchronizace: střed
:alt: Vzorový faktura v PDF z Odoo Sales.

.. viz též:
:doc:`fakturační politika“
