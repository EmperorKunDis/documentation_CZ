==================
Tříkrokový recept
==================

Některé společnosti vyžadují kontrolní proces před přijetím zboží od dodavatelů.
k tomu slouží třífázový proces přijímání zboží.

V třístupňovém procesu přijímání produktů jsou produkty přijímány v oblasti příjmu, poté jsou přesunuty do
kontrolní oblast kvality. Produkty, které projdou kontrolou kvality, jsou pak převedeny do
zásobníky. Produkty nejsou k dalšímu zpracování dostupné, dokud nebudou převedeny mimo sklad
kvalitní plochy a do zásob.

Konfigurace
=============

Odoo je ve výchozím nastavení konfigurováno tak, aby přijímalo a dodávalo zboží v jednom kroku.
<příjemce_doručení_v_jednom_kroku>, takže je potřeba nastavení změnit, aby bylo možné využít tři kroky
faktury. Nejdříve zkontrolujte, že je zapnutá možnost „Multistep Routes“ v menu:
Konfigurace > Nastavení > Sklad. Poznámka: Aktivujte Multi-Step Routes
aktivuje také *Skladovací místa*.

.. obrázek: faktury_tři_kroky/faktury-tři-kroky-multikroková trasa.png
:align:center
:alt:Aktivujte vícekrokové trasy a skladové místo v nastavení zásob.

Dále je potřeba sklad nakonfigurovat pro třístupňové přijímání. K tomu se přepněte na
:menu „Výdejní aplikace“ -> „Nastavení“ -> „Sklad“, a vyberte požadovaný sklad
upravit. To odhalí podrobnosti o konkrétním skladu.

Na stránce s podrobnostmi o skladu vyberte možnost „Přijmout zboží“ a pak
kvalita a pak zásoby (3 kroky) pro: guilabel:Příchozí dodávka.

.. obrázek: faktury_tři_kroky/faktury-tři-kroky-příchozí-dodávky.png
:align:center
:alt:Zvolte možnost přijetí zásilky ve třech krocích.

Aktivací třístupňových faktur a dodávek vznikají dvě nové interní lokality: *Vstup*
(WH/Input) a *Kontrola kvality* (WH/Quality Control). Pro přejmenování těchto míst přejděte do
Vyberte aplikaci „Inventář“ -> „Konfigurace“ -> „Místa“, pak klikněte na požadované místo.
změnit (nebo aktualizovat) název.

Přijměte v třech krocích (vstup + kvalita + zásoby)
================================================

Vytvořte objednávku na nákup
-----------------------

Pro vytvoření nové poptávky zadávejte do adresního řádku :abbr:`RfQ (Request for Quotation)` a přejděte na kartu
Nový, který odhaluje prázdnou stránku s formulářem „Žádost o nabídku“ (Request for Quotation). Na této stránce vyberte
Přidejte dodavatele, zboží a poté klikněte na „Potvrdit objednávku“.

V pravém horním rohu se objeví tlačítko „Potvrzení“, a faktura bude spojena
s fakturou. Kliknutím na tlačítko „Faktura“ se zobrazí faktura
pořádku.

.. obrázek: faktury_tři_kroky/faktury-tři-kroky-chytře.png
:align:center
:alt: Po potvrzení objednávky se objeví tlačítko Smart Button pro vystavení faktury.

Zpracovat fakturu
-----------------

Jakmile je potvrzena objednávka, vytvoří se faktura („WH/IN“) a je připravená k
procesu.

Doklad o zaplacení lze doložit originálním nákupním formulářem nebo je možné jej získat
Přejít na aplikaci „Sklad“ a najít kartu úkolů „Faktury“.

Klikněte na tlačítko „Zpracovat“ (Guilabel: # To Process“) pro zobrazení všech příchozích faktur, které je potřeba zpracovat. Klikněte
faktura spojená s předchozí objednávkou.

Klikněte na tlačítko „Potvrdit“ pro potvrzení faktury a přesun produktu do cílové destinace.
umístění, :guilabel:`WH/Input“.

.. obrázek: faktury_tři_kroky/faktury-tři-kroky-příjemka.png
:align:center
:alt:Přijetí výrobku při přesunu na skladovou položku nebo místo vstupu.

Zpracujte převod do kontroly kvality
-------------------------------------

Jakmile je doklad ověřen, proběhne interní převodová operace pro přesun produktu do kvality
kontrola je připravena k vyřízení.

Klikněte na „Přehled skladu“ v navigačním panelu a
Najděte kartu úkolu „Vnitřní převody“.

Vyberte tlačítko „Zpracovat“ (# To Process) pro zobrazení všech vnitřních převodů k zpracování. Poté vyberte
Vnitřní převod spojený s platnou fakturou.

Když bude připraveno, klikněte na tlačítko „Potvrdit“ a dokončete převod. Produkt se poté přesune
:guilabel:`WH/Input“ na „WH/Kontrola kvality“.

.. obrázek: faktury_tři_kroky/faktury-tři-kroky-vnitřní-převod.png
:align:center
:alt: Vnitřní přesun produktu do kontrolního zónového prostoru.

Proces převodu na sklad
===========================

Jakmile je schválena interní přeprava produktu do kontroly kvality, může být další
interní přesunová operace pro přesun produktu do skladových zásob je připravena k zpracování.

Klikněte na „Vaše společnost: Vnitřní převody“ v navigačním panelu, abyste zobrazili seznam všech
interní převody k zpracování. Poté vyberte nový interní převod a přesuňte produkt do
„Kontrola kvality“ na „Sklad“.

Když bude připraveno, klikněte na tlačítko „Potvrdit“ a dokončete převod. Produkt se poté přesune
„Kontrola kvality“ na „Sklad“.

.. obrázek: faktury_tři_kroky/faktury-tři-kroky-druhý-převod.png
:align:center
:alt: Vnitřní převod pro produkt, který se přesouvá do skladu.
