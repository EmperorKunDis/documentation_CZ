=================
Místa selhání
=================

.. |QCP| nahradit za :: abbr: QCP (kontrolní bod kvality)
.. |QCP| nahradí ::: zkratka: QCP (Kontrolní body kvality)

V Odoo se používají kontrolní body kvality (QCP), které umožňují vytvářet kontroly kvality, které zaměstnance
aby se ověřila kvalita produktů při jejich zahrnutí do určitých operací.
více míst selhání na QCP, produkty, které neprošly kontrolou kvality, mohou být odeslány do
z uvedených lokalit.

.. důležité:
Příležitost k selhání byla přidána do verze 17.0 Odoa a **nevyskytuje se v žádné jiné verzi**.
předchozí verze. Pro aktualizaci databáze Odoo na novější verzi se podívejte do dokumentace k
:doc:`aktualizace databáze <../../../../administration/upgrade>“.

Konfigurace
=============

Pro použití umístění chyb musí být nastavení „Uložení“ v nastaveních
Aplikace „Inventář“. Tato nastavení umožňuje vytvářet podlokality ve skladu, včetně
místo selhání.

Chcete-li povolit nastavení „Uložiště“, přejděte do:
Konfigurace --> Nastavení, zaškrtněte políčko vedle:guilabel:Uložiště
Poté klikněte na položku „Sklad“. Poté klikněte na tlačítko „Uložit“.

.. obrázek: failures/storage-locations-setting.png
:align:center
:alt:Nastavení skladových míst v aplikaci Nastavení zásob.

.. důležité:
Nejúčinnější jsou lokality selhání, pokud se produkty konfigurují jako „skladovatelné“.
To je proto, že se skladové zásoby evidují pouze u skladovatelných produktů, zatímco u spotřebitelných
produkty, u kterých se přesná čísla nevyhodnocují.

Kontroly kvality ještě mohou být vytvořeny pro spotřební zboží a tyto produkty lze poslat do
místo selhání, pokud selže kontrola. Odoo však nezaznamenává přesný počet
spotřební výrobek uložený na místě poruchy.

Chcete-li produkt nastavit jako skladovatelný, přejděte na: „Nastavení aplikace Inventor --> Produkty -->
Produkty“ a vyberte produkt. V poli „Druh produktu“ v sekci „Obecné informace“ zadejte typ produktu.
v záložce „Informace“ ujistěte se, že je vybrán položka „Skladovatelný produkt“.
menu.

Přidejte místo selhání do QCP
===========================

Chcete-li přidat místo selhání do |QCP|, přejděte na:
--> Kontrolní body“. Vyberte existující QCP ze seznamu nebo vytvořte nový kliknutím
:guilabel:`Nový“.

.. poznámka::
Následující pokyny popisují pouze konfigurační nastavení potřebná pro přidání selhání
místo do QCP. Pro kompletní přehled o QCP a všech možností, které jsou k dispozici při
konfiguraci viz dokumentace k tématu „kontrolní body kvality“ na adrese
</kontrolni-mista>.

V poli „Kontrola“ na formuláři QCP vyberte možnost „Množství“.
Tímto způsobem se objeví pole „Místo selhání“ na formuláři. To je k dispozici pouze
k dispozici, pokud je vybrána možnost „Množství“.

V poli „Místo selhání“ vyberte jedno nebo více míst z roletky.
Vytvořte nové umístění, zadejte požadovaný název do pole a potom vyberte
Vyberte možnost „Vytvořit [název]“ z roletky.

.. obrázek:failure_locations/qcp-form.png
:align:center
:alt:QCP v aplikaci kvalita s nastavenou závadovou lokalizací.

Odeslat produkty na místo selhání
=================================

Jakmile je QCP nakonfigurován s jedním nebo více místem selhání, produkty, které selžou kontrolu
Vytvořené společností QCP lze směrovat na jednu z lokalit.

Pro takové objednávky je nutné otevřít požadavek na kvalitu s kontrolou selhání, který byl vytvořen pomocí konfigurace QCP.
umístění. Například přejděte na:menu:Inventarapp --> Operationen --> Eingangsrechnungen“
Vyberte fakturu.

Vyberte požadovaný typ objednávky a klikněte na tlačítko „Kontrola kvality“ v horní části okna.
okno, ve kterém lze provést kontrolu kvality. V dolní části okna klikněte na
tlačítko „Nesplňuje požadavky“ k neprovedení kontroly kvality, což otevře druhé okno s názvem
:guilabel:`Kontrola kvality selhala u produktu [Produkty].

Do pole „Počet kusů“ zadejte počet produktů, které neprošly kontrolou.
kontrola kvality. V poli „Místo selhání“ vyberte místo, kam se má zpráva o chybě odeslat.
přijmout. Pak klikněte na tlačítko „Potvrdit“ v dolní části okna prohlížeče.
it.

.. obrázek: failures/failed-pop-up.png
:align:center
:alt:Pop-up okno, které se objeví po neúspěšném ověření kvality.

Konečně na konci objednávky klikněte na tlačítko „Potvrdit“ v horní části stránky.
potvrdil, že zboží, které neprošlo kvalitativní kontrolou, bylo odesláno na místo selhání.
Produkty, které testem prošly, byly odeslány do svých obvyklých skladových prostor.

Zobrazit seznam míst selhání
===============================

Pro zobrazení množství skladovaných produktů v místě selhání přejděte na:
Aplikace --> Konfigurace --> Lokality“. Vyberte místo selhání z seznamu. Pak klikněte na
:guilabel:„Aktuální zásoba“ chytrý tlačítko na stránce lokalitě.

Stránka s chybovou zprávou uvádí všechny produkty skladované v daném místě.
počet kusů každé.
