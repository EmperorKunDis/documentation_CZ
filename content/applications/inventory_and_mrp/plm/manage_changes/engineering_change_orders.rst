=========================
Inženýrské změny objednávek
=========================

.. |BOM| nahradit za: :abbr:`BOM (Seznam materiálů pro výrobu)“
.. |BOM| nahradí::: zkratka: `BoM (Bill of Materials)`
.. |ECO| nahradit za: zkratku: `ECO (Engineering Change Order)`
.. |ECN| nahrazuje: zkratka: `ECN (Engineering Change Notices)`

.._plm/eco:

Používejte *změny v projektu* (*ECOs*) k sledování, implementaci a obrácení změn verzím provedených na
produkty a „seznamy materiálů“ (<../../manufacturing/basic_setup/bill_configuration>).

Inženýrské změny lze vytvářet:

#:ref:`přímo v typu ECO (<plm/eco/create-eco>).“
#automaticky z zpětné vazby zaslané na e-mailovou adresu typu ECO podle :ref:`<plm/eco/eco-type>`.

... plm/eco/create-eco:

Vytvořte EKO
==========

Pro vytvoření nového ECO začněte tím, že se přesunete do aplikace PLM. Pak vyberte typ ECO
slouží k sledování pokroku změny. Na záložce „Engineering Change Orders“
stránce, klikněte na tlačítko „Nový“ v pravém horním rohu.

.. poznámka::
:dokument: „Typy ECO <eco_type>“ kategorizují a organizují požadavky na změny. To může zajistit, že
zaměstnanci vidí pouze ECOs související s jejich odpovědnostmi, ať už se jedná o nový produkt
introdukce, aktualizace produktové řady nebo plnění předpisů.

V poli „EKO“ vyplňte následující údaje:

- :guilabel:`Popis“ je stručný popis zlepšení.
- :guilabel:`Typ projektu“: specifikuje typ projektu ECO, který organizují ECOs.
- :guilabel:`Použít na` určuje, zda se změní |ECO| nebo
:guilabel:`Produkt pouze“.
- :guilabel:`Produkt` ukazuje na produkt, který se zlepšuje.
- :guilabel:`Seznam materiálů“ specifikuje změněný seznam materiálů (BOM).
:guilabel:`Produkt“ pole má již existující |BOM|. Pokud existuje více |BOMs|, vyberte požadovaný
ze seznamu volby v rozbalovacím menu.

.... důležité::
Musí být vybrán produkt před zvolením možností „Seznam materiálů“.
dostupné.

- Pole „Společnost“ se používá v databázích s více společnostmi. Uveďte, zda se změna týká
produkty v konkrétní společnosti nebo nechat prázdné, pokud se změna týká všech společností.

....... poznámka::
:guilabel:`Společnost“ je k dispozici pouze v případě, že jsou povoleny více společností. Podrobnosti naleznete v
:doc:`/obecne/firmy/multifirma`.

- :guilabel:`Odpovědný“ představuje osobu, která je zodpovědná za tento |ECO|. (Volitelné)
- :guilabel:`Účinný“ určuje, kdy se |ECO| aktivuje. Vyberte „Jakmile
„možné“ znamená, že ECO se vztahuje na produkci BOM, jakmile je autorizovaný uživatel
:ref:`přidává změny <plm/eco/add-changes>`. :guilabel:`Datum“ s konkrétním datem
Vybrané verze se použijí jen na tento den a budou snadněji sledovatelné.
výrobu, kde je vyráběn BOM.
- :guilabel:`Tagy‘ jsou přiřazeny |ECOům| pro prioritizaci a organizaci. Vytvořte novou tagovou značku
zadáním názvu do pole a výběrem možnosti „Vytvořit“ v rozevírací nabídce.

Po vyplnění formuláře ECO stiskněte tlačítko Start Revision a zahajte implementaci
změny.

Stisknutím tlačítka Start revize se provede následujících tři akce:

#Vyskytne se tlačítko „Dokumenty“, které uloží související dokumenty z |BOM|.
#. Kopie výrobního procesu je uložena v nově se objevujícím tlačítku „Revize“
zpracování |ECO|. Následující volné číslo verze (např. „V2“, „V3“ apod.) je také přiděleno, aby
všech verzí BOM.
#V pravém horním rohu se zobrazují fáze |ECO|:guilabel:„Typ“.

.. poznámka::
K dispozici je pouze tlačítko „Revize“ v rámci funkce „Faktura“.
V poli „Použít na“ je vybrána možnost „Materiál“, v poli „Začínat od“ je vybrán bod „0“.
Byla stisknuta tlačítko „Změna“.

.. obrázek: engineering_change_orders/eco-form.png
:alt:ECO s přehledem fází v pravém horním rohu a tlačítkem pro chytré funkce.

Vyměnit součásti
=================

Pro úpravu součástek v |BOM| klikněte na tlačítko „Revize“ ve formuláři |ECO|.
přistupovat k nové verzi BOM. Odoo rozlišuje neprodukční verzi BOM od
současnou verzi, tím, že označí test |BOM| velkým štítkem s názvem „Archivovaný“.

Příklad:
Po kliknutí na tlačítko „Zahájit revizi“ pro ECO produktu se zobrazí hláška „[D_0045
Židličku]`, provádějte změny v seznamu komponentů (BOM) kliknutím na tlačítko „Revize“.
Provedením takového kroku se otevře archivovaný |BOM|, který je označen velkým červeným štítkem „Archiv“.

.. obrázek:: změny v projektových dokumentacích/archivní BOM.png
:alt:Zobrazit archivovaný seznam materiálů.

Na novém BOM v záložce Komponenty proveďte změnu seznamu komponent tak, že
změnou množství stávajících komponent a přidáním nových komponent pomocí
tlačítko „Přidat řádek“ a odstraňování komponent pomocí ikonky „🗑️ (směsný odpad)“.

.._plm/eco/příklad klávesnice:

Příklad:
Ve verzi 2 BOM pro klávesnici jsou komponenty sníženy na minimum a
je přidán další komponent, „Stabilizátory“.

.... obrázek:: engineering_change_orders/version-2-bom.png
:alt: Aktualizovaná BOM

Srovnejte změny
---------------

Chcete-li porovnat aktualizovanou BOM s předchozí verzí, přejděte na ECO pro tuto BOM v
z těchto způsobů:

#Z aktualizované BOM klikněte na název ECO (například „ECO005: Zlepšit ...“).
v levém horním rohu.
#Zobrazit přehled PLM. Klikněte na tlačítko „Inženýrské změny“.
:guilabel:`Aktualizace BOM“ Kanban karta. Klikněte na Kanban kartu pro příslušný |ECO|, abyste jej otevřeli.

V dialogovém okně ECO se zobrazí nová záložka BoM Changes s rozdíly mezi současným
|BOM| a nová verze.

Modrý text označuje nové součástky přidávané do aktualizovaného BOM, které nejsou v produkčním BOM.
Černý text představuje aktualizace sdílené oběma BOM, zatímco červený text znázorňuje komponenty odstraněné
aktualizovaný BOM.

Změny a testy jsou obsaženy v aktualizovaném BOM a neovlivňují BOM současné.
používané ve výrobě. To je do té doby, než se provede :ref:`změna <plm/eco/apply-changes>`.

Příklad:
Zobrazte souhrn rozdílů mezi aktuální a upravenou klávesnicí |BOMs|
:guilabel:`Změny BoM“ v záložce ECO.

.. obrázek: engineering_change_orders/bom-changes.png
:alt: Zobrazit souhrn změn komponent v záložce Změny v BoM.

Operace změny
=================

Pro úpravu operací v BOM klikněte na tlačítko „Revize“ ve formuláři ECO.
přistupovat k archivované nové verzi BOM.

V nové verzi BOM přepněte na záložku „Operace“ a zobrazte nebo upravujte BOM.
operace. Chcete-li provést změnu, vyberte každou operaci, která otevře příslušný :guilabel:`Open:
Pop-up okno pro operace.

.. poznámka::
Karta „Operace“ není k dispozici v základní verzi. Chcete-li ji povolit, přejděte na
:menuvolba:„Výroba“ --> „Konfigurace“ --> „Nastavení“, a zkontrolujte :guilabel:„Práci
Krabice objednávek.

Upravte libovolné pole v okně „Otevřené operace“ (Guilabel: Open: Operations), pak klikněte
:guilabel:`Uložit“ po dokončení.

Vytvořte nové operace kliknutím na tlačítko „Přidat řádek“ a odstraňte nové operace
kliknutím na tlačítko „Archivní operace“.

Srovnejte změny
---------------

Pro porovnání aktualizované operace s předchozí verzí přejděte na |ECO| pro |BOM| v
Jedna z těchto cest:

#Z aktualizované BOM klikněte na název ECO (například „ECO005: Zlepšit ...“).
breadcrumbs v levém horním rohu
#Zobrazit přehled PLM (z menu „Guilabel“ vyberte položku „Overview“, poté zvolte kartu „ECO“ a následně správný „ECO“).
Kanban pohled.

Na formuláři ECO se zobrazí nový záložka „Změny operace“, která ukazuje rozdíly mezi
současná verze produktového stromu a nová verze.

Modrá barva ukazuje nové operace přidávané do aktualizovaného BOM, které ještě neexistují v
produkce |BOM|. Černý text představuje aktualizace sdílené oběma |BOM| a červený text ukazuje
operace odstraněné v aktualizovaném BOM.

Úpravy v |BOM| v ECO neovlivní použité |BOM| ve výrobě. To znamená
až do chvíle, kdy se změny aplikují.

V záložce „Operace změn“ je každá řádka podrobností pod sloupci v tabulce.
zobrazovat následující informace:

- :guilabel:`Operace“: Jméno operace, která byla změněna.
- :guilabel:`Krok“: určuje kontrolní bod kvality, který je viditelný při provádění operace
podrobný návod.

.. poznámka::
Chcete-li zkontrolovat pokyny, klikněte na položku operace v záložce „Operace“ v
|BOM|. Pak v okně „Otevřít: operace“ vyhledejte
:guilabel:`Návod k použití“ chytrý tlačítko zobrazené v horní části.

Příklad:
„Soubor“ „Operace“ zahrnuje 10 podrobně popsaných „Návodů“, které musíte splnit.
je.

.... obrázek: engineering_change_orders/instructions-smart-button.png
:alt:Zobrazit pokyny chytré tlačítko, abyste si mohli zkontrolovat, zda operace má další
pokyny.

- :guilabel:`Krok typu“ popisuje typ kontroly kvality pro další pokyny v
operace.
- :guilabel:`Typ` odpovídá barevnému textu, který specifikuje, jak se změnil
výroba |BOM|. Typy změn operací mohou být :guilabel:`Přidat`, :guilabel:`Odebrat` nebo
:guilabel:`Aktualizace“.
- :guilabel:`Práce“ určuje pracoviště, na kterém je operace prováděna.
- „Doba trvání“ znamená změnu v poli „Výchozí doba“.
v okně „Otevřené operace“, které uvádí očekávaný čas pro
dokončení operace.

Příklad:
Karta „Změny operace“ porovnává výrobní |BOM| s aktualizovaným |BOM|.
|EKO|

V aktualizované BOM je nová operace „Sestavení“ v :guilabel:`Operaci na pracovišti“
Do výroby je přidána linka číslo 1 a očekávaný čas provedení operace je nastaven na hodnotu 20.00
minutách, jak je specifikováno v :guilabel:`Manuální změna trvání`.

K doplnění operace „Skládání“ jsou přidány dvě instrukce kontroly kvality:

   #Prvním je krok „QCP00039“, který je typem kroku pro registraci.
Produkce komponentů.
   #Druhý je „Krok“ s označením QCP00034, který patří do kategorie „Pokyny“.
Poskytuje další podrobnosti o sestavování.

.... obrázek:: engineering_change_orders/operation-changes.png
:alt:Operace mění záložku v |ECO|.

..._plm/eco/apply-changes:

Přidejte změny
=============

Po ověření změn přesuňte |ECO| do fáze ověřování:
které vyžadují schválení předtím, než budou moci být aplikovány na výrobu.
|BOM|.

Jakmile schválíte změny, tlačítko „Použít změny“ se stane dostupným. Klikněte
tlačítko, a ECO se automaticky přesune do fáze uzavření. Využijte změn, které
archivuje původní produkci BOM a revidovaná BOM se stane novou produkcí BOM.

Zkontrolovat změny
--------------

Aby se změny zobrazily, přejděte na stránku ECO a klikněte na tlačítko „Použít změny“.
stiskněte tlačítko „Zpětná revize“ v záložce „Návrh“.

Na aktualizované BOM je odstraněn velký červený nápis „Archivováno“.

Pro další ověření změn zkontrolujte výrobní BOM kliknutím na: menu: „Výroba
app --> Produkty --> Vyberte produkt.

Poté na kartě produktu stiskněte tlačítko „Seznam komponent“ a vyberte
Vyberte si z nabídky „Různé“ v záložce BOM a vyberte verzi.
Hodnota pole je aktualizována tak, aby odpovídala číslu verze zobrazenému na tlačítku „Změna“
nejnovější |EKO|.

Příklad:
Po aplikaci změn klávesnice |ECO| se zobrazí pohled
verzi aktuálního klávesnice |BOM| v záložce :guilabel:`Různé`. Zde je
:guilabel:"Verze" číslo bylo aktualizováno na "2", což odpovídá "V2", které se zobrazuje v
:guilabel:`Revize“ tlačítko ECO.

.... obrázek: engineering_change_orders/bom-version.png
:alt: Zobrazit aktuální verzi BOM v záložce Ostatní.

Zobrazit změny
============

Změny navrhované v rámci aktualizace si můžete prohlédnout na záložce „Overview“ v aplikaci PLM.
Aktualizace karet typu ECO reprezentuje tlačítko „Inženýrské změny“
Provozní změny vytváří.

Klikněte na tlačítko „Inženýrské změny“ (# Engineering Changes) pro otevření karty kanbanového typu ECO.
zobrazit návrh, vybrat ECO v nové fázi.

Na záložce „Operační změny“ v seznamu ECO zobrazte souhrn navrhovaných změn. Kliknutím
tlačítko „Revize“ k navigaci na revidovanou BOM a prohlédnout si navrhované
v podrobnějším rozsahu.

Příklad:
Provozovatel navrhl další kontrolu poškozených součástí přidáním kroku při provádění
Operace „Sestavit přepínače“ pro výrobní objednávku :abbr:`MO (Manufacturing Order)` s číslem
produktu, „Klávesnice“.

Pak tento vytvořený |ECO| lze zobrazit při procházení typu ECO „Změny BOM“, který je k dispozici
:menu_selection:`PLM aplikace - Přehled“.

V poli „Zodpovědný“ je přiřazeno pole s názvem „Odpovědná osoba“, které ukazuje na operátora, který navrhl změnu.
pracovník, který revidoval BOM, aby se zeptal o další informace u člověka, který navrhl
změny.


.... obrázek:: změny v projektových dokumentacích/zobrazení BOM.png
:alt:Najděte nový ECO v typu „Změna BOM“, ve fázi „Nový“.

Na upraveném |BOM| přepněte na záložku „Operace“ a vyberte ikonu „fa-list-ul“.
:guilabel:`(Zobrazit pokyny)` ikonu. Když tak učiníte, otevře se seznam :guilabel:`Kroků“ k provedení
operace s nejnovějším pokynem „Nová návrhová kroky:“, který je následován vstupem uživatele.
Název. Klikněte na položku, abyste zobrazili navrhované změny.

.. obrázek: engineering_change_orders/show-instructions.png
:alt:"Zobrazit pokyny" ikonu v záložce Operace.

Kontrolní body kvality
----------------------

.. důležité:
Aplikace „Kvalita“ (Quality) je nutná k nastavení kontrolních bodů kvality.

Na formuláři „kontrolní bod kvality“ (viz. <quality/quality_management/quality-control-points>) zajistěte
následující pole jsou přesně vyplněna, aby poskytla podrobné pokyny pro operátory:

- :guilabel:`Název“: přejmenujte na název, který poskytuje stručný popis nové instrukce.
- :guilabel:`Kontrola podle“: zvolte v rozevíracím seznamu, zda se tato instrukce vztahuje na
široce pro produkt, konkrétně pouze pro tuto operaci nebo
konkrétní: množství produktu.
- :guilabel:`Typ kontrolního bodu“: třídí typ kontrolního bodu. Vyberte z roletky
:guilabel:`Návod k použití“ pro podrobné pokyny pro pracovníka.
pracovníci vyberte „Začít fotografovat“, „Registrace spotřebovaných materiálů“
:guilabel:`Tisk etikety“, nebo jiné možnosti „kontroly kvality“
<kvalita/kvalitní řízení/kontrolní body kvality>.

.. viz též:
:ref:`Konfigurace kontrolních bodů kvality <kvalita/kvalitní řízení/kontrolní body kvality>`

Jakmile je kvalitativní kontrolní bod nakonfigurován, vrátí se zpět na :guilabel:`Kroky“ pomocí
kousky chleba. Nakonec přetáhněte poslední položku kontroly kvality do pořadí pokynů.

Příklad:
Přetáhněte a přemístěte příkaz „Zkontrolujte zlomené spínače“ klepnutím a taháním.
:ikonka:oi-draggable:guilabel:(draggable) ikona pro přesun z dolní části na druhou
pozice.

.... obrázek: engineering_change_orders/reorder.png
:alt: Přetáhněte a přesuňte pokyny tím, že vyberete ikonku „přetažení“ v levém rohu.
