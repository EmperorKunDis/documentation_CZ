==========================
Změnit velikost štítku s adresou
==========================

Přehled
========

V Odoo je k dispozici mnoho různých typů štítků pro doručení.
objednávek. Podle typu použitého balení se může lišit velikost štítků
je vhodný a lze jej přizpůsobit balíčku.

Konfigurace
=============

V modulu „Sklad“ přejděte do sekce „Nastavení -> Dodávky ->
Způsoby dopravy. Klikněte na požadovaný způsob dopravy. Například FedEx
Bude použito mezinárodní*.

.. obrázek: typ_labelu/dopravní_možnosti.png
:align:center
:alt: Různé způsoby dopravy.

V záložce „Konfigurace“ pod položkou „Typ štítku“ vyberte jeden ze tří typů štítků.
Dostupnost se liší podle dopravce.

.. obrázek: typ_labelu/typ_labelu_vyber.png
:align:center
:alt: Vyberte typ štítku.

Při potvrzení objednávky s odpovídající přepravní společností a vydání dodacího listu
Ověřená objednávka se automaticky vytvoří jako PDF a objeví se ve
:guilabel:`Kecání“.

Vytvořte prodejní objednávku
====================

V aplikaci „Prodej“ klikněte na tlačítko „Vytvořit“ a vyberte mezinárodní.
Zákazník. Klikněte na tlačítko „Přidat produkt“ a vyberte položku. Klikněte na tlačítko „Přidat dopravu“, vyberte
zvolte způsob dopravy, pak klikněte na „Získat sazbu“, a nakonec klikněte na „Přidat“.

.. obrázek: typ_labelu/doprava.png
:align:center
:alt:Přidání způsobu dopravy a sazby k objednávce prodeje.

Po potvrzení kliknutím na tlačítko „Potvrdit“ se zobrazí tlačítko „Doručení“,
se objeví.

.. obrázek: typ_labelu/doprava-italie-so.png
:align:center
:alt: Tlačítko chytré objednávky.

Jakmile je objednávka dopravy potvrzena kliknutím na tlačítko „Potvrdit“ v objednávce dopravy,
dokumenty o přepravě se objevují v :guilabel:`Chatovacím okně“.

.. obrázek: štítek/doprava-pdf.png
:align:center
:alt:Doručování PDF dokumentů.

Příklad etiket
==============

Výchozí typ štítku je „Papír – dopis“. Příklad velikosti FedEx pro dopis
Štítek je:

.. obrázek: /label_type/full-page-fedex.png
:align:center
:alt: Celá stránka velikosti poštovního štítku pro přepravu společností FedEx.

Pro srovnání je zde příklad štítku zespodu poloviny balíčku společnosti FedEx:

.. obrázek: label_type/polovina-stránky-fedex.png
:align:center

