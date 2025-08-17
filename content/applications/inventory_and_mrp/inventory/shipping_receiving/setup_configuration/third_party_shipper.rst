=============================
Třetí strany poskytující dopravní služby
=============================

.. |SO| nahradit za: :abbr:`SO (Prodejní objednávka)`
.. |DO| nahradit za: :abbr:`DO (Dodací příkaz)`

... inventář/dodání/třetí strana:

Uživatelé mohou propojit třetí strany s databází Odoo, aby ověřili přepravce.
doručení na konkrétní adresy, automatické výpočty poštovného
<../setup_configuration>, a také vytváří štítky pro odeslání zboží <labels>.

V Odoo lze přepravce aplikovat na prodejní objednávku (PO), fakturu nebo dodací list.
Tipy pro řešení běžných problémů při konfiguraci přepravních spojů, přeskočte na
:ref:`Řešení problémů <inventory/shipping_receiving/third-party-troubles>`

.. viz také:
   - :doc:`dhl_credentials“
   - :doc:`sendcloud_shipping`
   - :doc:`ups_credentials“

Následující je seznam dostupných připojení k dopravcům v Odoo:

.. seznam-tabulka::
:hlavičkové řádky: 1
:sloupek: 1

   * – Nositel
     - Dostupnost regionu
   * :-:dhl_credentials
     - Všichni
   * – :doc:`Envia.cz <envia_shipping>`
     - Všichni
   * – FedEx
     - Všichni
   * --:<ref name="ups_credentials">{{Citace elektronického dokumentu
     - Všichni
   * -Poštovní služba USA
     - Spojené státy americké
   * :-:sendcloud_shipping
     - Některé evropské země (podrobnosti níže)
   * :-:doc:`Bpost <bpost>`
     - Belgie
   * EasyPost
     - Severní Amerika
   * – Shiprocket
     - Indie
   * – :doc:`Starshipit <starshipit_shipping>`
     - Austrálie a Nový Zéland

.. důležité::
Další služby společnosti DHL nejsou podporovány.

Společnost Sendcloud v současné době podporuje zasílání zásilek ze zemí **Austrálie, Belgie, Francie, Německa, Itálie a**
Nizozemsko, Španělsko a Spojené království, **a do kterékoliv evropské země**.

Konfigurace
=============

Pro správné nastavení třetích stran pro přepravu s Odoem postupujte podle následujících kroků:

#:ref:`Nainstalujte modul pro zasílání zásilek <Inventář/Odesílání a příjem/Zasílací modul>“.
#:ref:`Nastavit způsob dodání <Inventář a příjem zboží/Konfigurace způsobu dodání>“.
#:ref:`Aktivujte produkční prostředí <Inventura/Přijímání a výdej/Produkční prostředí>“.
#:ref:`Nastavit sklad <Inventura / Přijetí a výdej / Nastavení zdroje adresy>“.
#:ref:`Uveďte hmotnost produktů <Inventar/Versand und Empfang/Konfigurieren der Gewichtseinheit>“.

...Inventarizace, přijímání a odesílání zboží:

Nainstalujte přepravní konektor
--------------------------

Pro instalaci přepravních konektorů přejděte do sekce „Nastavení“ v aplikaci Inventor.

V sekci „Připojení k dopravcům“ zaškrtněte políčko třetích stran.
je nainstalovat. Můžete vybrat více třetích stran pro doručení najednou. Pak klikněte
:guilabel:`Uložit“.

.. poznámka::
:dokument: „Metody doručení <../setup_configuration>“ lze také integrovat s operacemi v
*Prodej*, *E-commerce* a *Webové stránky*. Pro instalaci se podívejte na :ref:`instalace aplikací a modulů
dokumentace pro instalaci obecně.

.. obrázek:: třetí strana dopravce/dopravní spojení.png
:align:center
:alt:Možnosti dostupných připojení v Odoo.

...Inventarizace, přijímání zásilek, konfigurace způsobu dodání:

Metoda doručení
---------------

Chcete-li nakonfigurovat přihlašovací údaje API a aktivovat dopravce, začněte v
Vyberte „Aplikace pro inventář“ -> „Konfigurace“ -> „Dopravní metody“, a vyberte požadovanou.
metoda doručení.

.. poznámka::
Seznam často obsahuje **dva** způsoby doručení od stejného poskytovatele: jeden pro
mezinárodní a jedna pro vnitrostátní dopravu.

Přidat lze další způsoby dodání pro specifické účely, například :doc:`balení
<../../produktní-management/konfigurovat/balení>.

.. viz také:
:doc:`Nastavte způsoby doručení <../setup_configuration>`

.. poznámka::
Zajistěte, aby byl způsob doručení zveřejněn ve chvíli, kdy by měl být k dispozici na webové aplikaci.
Vložit způsob doručení na webovou stránku, kliknout na požadovaný způsob doručení a poté kliknout
:guilabel:`Nepublikované“ chytré tlačítko. Když tak učiníte, změní se chytré tlačítko na „Nepublikované“.
:guilabel:`Zveřejněno“.

...Inventarizační/přijímací/výdejní metody:

Stránka „Dopravní metoda“ obsahuje podrobnosti o poskytovateli, včetně:

- :guilabel:`Metoda doručení“ (*Povinný údaj*)): název způsobu dopravy (např. „FedEx USA“)
„FedEx EU“, atd.
- :guilabel:`Webová stránka“: Konfigurace způsobu dopravy pro e-shop, který je připojen k
konkrétní webové stránky v databázi. Vyberte příslušnou webovou stránku z roletkového menu nebo nechte pole prázdné.
nechat metodu používat na všech stránkách.
- :guilabel:`Dodavatel“ (*Povinné pole*)): vyberte třetí stranu, která zajišťuje doručení, například FedEx.
při výběru poskytovatele, úrovně integrace, způsobu fakturace.
:guilabel:`Sazba pojistného“ se stává dostupnou.
- Vyberte možnost „Úroveň integrace“ a zvolte „Získat sazbu“, abyste dostali pouze odhadovanou
náklady na dopravu (výdejky, příjemky, třetí strana) v inventáři nebo faktuře.

... důležité::
Vyberte možnost „Získat sazbu a vytvořit zásilku“ také pro tvorbu poštovních štítků.
</labels>.

- :guilabel:`Společnost“: pokud by měla být doprava určena konkrétní společnosti, vyberte ji z
vyberte ze seznamu. Nechte pole prázdné, pokud chcete metodu aplikovat na všechny společnosti.
- :guilabel:`Dodací produkt“ (*Povinný údaj*)): název dodacího poplatku, který se přidává k
|Faktura nebo SO.
- :guilabel:`Zásady fakturace“: vyberte a spočítejte odhadované náklady na dopravu
přímým odesílatelům zásilek. Pokud chcete místo skutečné ceny poštovného,
viz dokument „Skutečné náklady na dopravu - fakturační údaje“ dostupný na odkazu:
- :guilabel:`Přirážka k sazbě“: zadejte další procentní částku, která se přičítá k základní dopravní
připočítat k ceně náklady navíc, jako jsou například manipulační poplatky, obalový materiál, směnné kurzy atd.
- :guilabel:`Doprava zdarma při objednávce nad‘ umožňuje bezplatnou dopravu pro objednávky přesahující určitou částku.
částka, která byla zadána do příslušného pole :guilabel:`Částka`.
- :guilabel:`Procento pojištění“: zadejte procentuální částku, kterou vám bude vrácena za dopravné.
pokud balík ztratí nebo ho někdo ukradne během přepravy.

.. obrázek:: třetí_osoba_dodavatel/fedex.png
:align:center
:alt:Snímek obrazovky s metodou přepravy společnosti FedEx.

Konfigurační stránka „Způsob dopravy“ pro FedEx USA.

V záložce Konfigurace vyplňte pole s přihlašovacími údaji do API (např. klíč API, heslo).
číslo účtu, atd. V závislosti na zvoleném přepravci třetí strany v
V poli „Poskytovatel“ se objeví pole s názvem „Konfigurace“, které obsahuje různé požadované
pole. Pro více informací o konfiguraci přihlašovacích údajů konkrétních dopravců se podívejte na následující
dokumenty:

.. viz také:
   - :doc:`Přístupové údaje DHL <dhl_credentials>`
   - :doc:`Kreditní údaje Sendcloudu <sendcloud_shipping>`
   - :doc:`Přístupové údaje UPS <ups_credentials>`

... inventář/přijímání a odesílání/výroba:

Produkční prostředí
----------------------

Po nastavení podrobností o způsobu doručení klikněte na tlačítko „Testovací prostředí“
její hodnotu nastavte na :guilabel:`Produkční prostředí“.

.. varování::
Nastavení způsobu doručení na „Produkce“ vytváří skutečné dodací štítky a uživatelé
Jsou vystaveny riziku, že budou účtovány přes jejich účet dopravce (např. UPS, FedEx atd.) **předtím, než**
Uživatelé účtují zákazníkům za přepravu. Zkontrolujte všechny konfigurace před spuštěním
způsob dodání do :guilabel:`Výroba“.

.. obrázek::third-party-shipper/production.png
:align:center
:alt:Zobrazit tlačítko „Testovací prostředí“.

... inventář/příjem a odeslání/konfigurace zdrojového adresáře:

Konfigurace skladu
-----------------------

Zajistěte, aby se v záložce „Adresa“ (včetně PSČ) a „Telefon“ objevily
zadána správně. Chcete-li tak učinit, přejděte na: „Nastavení aplikace Inventar --> Konfigurace -->
Skladovací prostory“ a vyberte požadovaný sklad.

Na stránce konfigurace skladu otevřete stránku kontaktů skladu kliknutím na
:guilabel:`Společnost“ pole.

.. obrázek: třetí strana dopravce / vnitřní odkaz.png
:align:center
:alt:Zvýrazněte pole „Firma“.

Zkontrolujte, zda je správná adresa a telefonní číslo (jsou vyžadovány)
aby funkce připojení fungovala správně.

.. obrázek: třetí strana dopravce/firma.png
:align:center
:alt:Zobrazit adresu a telefonní číslo společnosti.

... inventarizaci, přijímání a konfiguraci hmotnosti:

Hmotnost výrobku
--------------

Pro správnou funkci integrace dopravců je nutné u produktů vyplnit hmotnost
Vyberte aplikaci „Nákupní seznam“ -> „Produkty“ -> „Produkty“ a vyberte požadovaný produkt.

Poté přepněte na záložku „Sklad“, a definujte hmotnost produktu v
sekci Logistika.

.. obrázek: třetí strana dopravce / produkt - hmotnost.png
:align:center
:alt:Zobrazit pole „Hmotnost“ v záložce Skladovací prostory produktového formuláře.

...Inventarizace, přijímání a odesílání zásilek, použití třetích stran pro přepravu:

Použijte třetí stranu k přepravě zboží
==================================

Dopravci mohou být aplikováni na fakturu, objednávku nebo dodací list.

Po konfiguraci způsobu doručení třetí strany
„Nastavení způsobu dodání“ v Odoo, vytvořte nebo přejděte na nabídku.
Přejděte na: menuSelection:„Prodejní aplikace“ --> „Objednávky“ --> „Nabídky“.

... skladování, přijímání a třetí strany:

Prodejní objednávka
-----------

Chcete-li zadat třetí stranu pro přepravu a získat odhad nákladů na přepravu, začněte v
:menuvolba:Prodejní aplikace --> Objednávky --> Cenové nabídky“. Vytvořte nebo vyberte existující cenovou nabídku a
Přidejte náklady na dopravu prostřednictvím třetí strany k nabídce, kliknutím na
Tlačítko „Přidat dopravu“ v dolní pravé části záložky „Řádky objednávky“.

.. obrázek: třetí_strana/přidat_dopravu.png
:align:center
:alt:Zobrazte tlačítko „Přidat dopravu“ na konci cenové nabídky.

V okně s názvem „Přidat způsob dopravy“ vyberte zvoleného dopravce.
Vyberte možnost dopravy v rozevíracím seznamu „Doprava“. Hodnota pole „Náklady“ je automaticky vyplněna
založené na:

- přesně stanovená hmotnost objednávky uvedená v poli „Celková hmotnost objednávky“ (v případě, že není uvedena, je to celková
přepravní hmotnosti (viz. :ref:`Hmotnost produktů <sklad/dodání a přijetí/nastavení hmotnosti> v objednávce`)
- vzdálenost mezi skladovým :ref:`zdrojovým adresním místem
a adresu zákazníka.

...Inventarizace, přijímání a třetí strana:

Po výběru třetí strany v poli „Metoda dopravy“ klikněte
V okně „Přidat způsob dopravy“ vyberte možnost „Získat sazbu“.
náklady přes dopravce. Pak klikněte na tlačítko „Přidat“ a zvolte způsob doručení
účtovat na SO nebo vystavit fakturu.

.. viz také:
:doc:`Za dopravu po dodání produktů účtovat <účetnictví>`

.. inventář/přijetí/třetí strana:

Dodací lístek
--------------

Pro uživatele odesílající zásilky bez instalace aplikace *Sales* přiřaďte dopravce k
dodací příkaz, nejprve se v aplikaci „Sklad“ podíváte na položku „Dodací příkazy“. Pak
Panel „Přehled skladu“, vyberte typ operace „Objednávky dodání“ a
vyberte požadovanou objednávku dodání, která není již označena jako: guilabel: Done
:guilabel:`Zrušeno“.

V záložce „Další informace“ nastavte pole „Dodavatel“ na požadovaného třetího stranu.
dopravce. Když je zvolen způsob dodání, nastaví se na hodnotu :ref:`výrobní režim
<Inventar/Versand/Einlagerung/Konfigurieren der Liefermethode>, a „Sledovací číslo“ je
Provádí se.

.. viz také:
:doc:`Vytvořit štítky pro zasílání <labels>`

.. obrázek: třetí_strana_dodavatel/doručení.png
:align:center
:alt:Zobrazte záložku „Další informace“ v objednávce dodání.

..Inventarizace, přijímání a odesílání zboží, problémy s třetími stranami:

Odstranění problémů
===============

Připojovací kabely mohou být někdy složité nastavit, takže zde jsou některé kontroly, které se vyplatí zkusit.
Něco nefunguje tak, jak by mělo.

#Zajistěte, aby byla zadána informace o skladu:
(např. adresa a telefonní číslo) v Odoo je správné **a** odpovídá záznamům uloženým v
webové stránky dopravce.
#Zkontrolujte, že typ balíku je správný (viz. :ref:`balík <inventory/warehouses_storage/package-type>`) a parametry
Jsou platné pro přepravce. Zkontrolujte, zda je možné přímo vytvořit objednávku na
webové stránky dopravce.
#Když se setkáte s rozdílem mezi odhadovanými náklady Odoa a cenou poskytovatele, nejprve
zajistit, aby se způsob doručení nastavil na :ref:`produkční prostředí
<sklad/přijímání a výdej/výroba-env>.

Pak vytvořte zásilku na webu dopravce i v Odoo a ověřte si cenu.
stejné v Odoo, u přepravce a ve výpisu chyb.

... příklad::
Při kontrole cenového rozdílu v logu ladění se požadavek na balík váží
přepravce FedEx uvádí hmotnost balíku sedm kilogramů.
dospěla k závěru, že problém je na straně společnosti FedEx.

Logy sledování chyb
---------

Zkontrolujte nesrovnalosti v dodacích datech aktivací ladění. Chcete-li to provést, přejděte na stránku s dodávkou
konfigurační stránka metody (:menuselection:`Skladová aplikace --> Konfigurace --> Doprava
Metoda“), a vyberte požadovaný způsob dopravy. Klikněte na tlačítko „Žádné ladění“, které je chytře označené jako
Aktivujte: guilabel: Debug Requests.

.. obrázek: třetí strana dopravce/bez ladění.png
:align:center
:alt:Zobrazit tlačítko „No Debug“.

Při zapnuté možnosti „Zobrazit požadavky na ladění“ se při každém použití přepínače pro odhadování
náklady na dopravu jsou uloženy v zprávě „Logování“. Zprávu otevřete kliknutím na
:ref:`rozvojový režim <developer-mode>“ a přejděte do „Nastavení aplikace --> Technické -->
Sekce „Struktura databáze“ --> „Sledování“.

.. poznámka::
Pro každý způsob dopravy se vytváří log, pokaždé když je vypočítána cena.
Při kliknutí na tlačítko „<inventory/shipping_receiving/third-party-rate>“ se zobrazí informace o ceně prodejního dokladu.
a faktury, **a také** když zákazník přidá dopravce do objednávky prostřednictvím
*Webová aplikace*

.. obrázek:third_party_shipper/log.png
:align:center
:alt:Ukažte, jak najít možnost „Záznamy“ v nabídce „Technické“.

Klikněte na položku „Požadavek HTTP“ pro zobrazení podrobné stránky a ověřte správnou informaci.
odeslané z Odoo dopravci. V odpovědi HTTP ověřte, že je stejná informace
přijat.

.. obrázek: třetí strana dopravce/záznamy.png
:align:center
:alt:Zobrazit historii požadavků na ladění v Nastavení > Technické > Protokolování.
