========
Balíčky
========

.. |SO| nahradit za: :abbr:`SO (objednávka na prodej)`

„Balíček“ je fyzická nádoba, která obsahuje jeden nebo více výrobků. Balíčky mohou být také použity k uchovávání
zboží v balení.

Balíčky se nejčastěji používají pro následující účely:

#.:ref:„Skupování produktů k jejich přesunu ve velkém množství“ (inventář/sklady a skladování/balení).
#.:ref:`Dodání zákazníkům <skladování/sklady a skladování/balení>`: Konfigurace typů balení
aby se přizpůsobily velikosti a hmotnosti lodí, zjednodušily balení.
a zajišťuje dodržování specifikací dopravce pro přepravu zásilek.
#Skladování většího množství věcí.

„Použití balení“ je pole na formuláři balení v Odoo, které se zobrazí pouze po zapnutí „Seskupování“.
Transféry a balíčky (Nastavení -> Inventář aplikace --> Konfigurace).

Výchozí hodnota pole „Použití balení“ na formuláři pro balení je nastavena na „Odpadkový box“. Změňte tento údaj.
pouze při konfiguraci balíčků pro :ref:`vybírání clusterů
<skladové zásoby/úložiště/soubor>.

„Druh balení“ je volitelná funkce, která se používá k výpočtu nákladů na dopravu.
<../../shipping_receiving/setup_configuration>, podle skutečné váhy zásilky. Vytvořte typy balíku
zahrnout hmotnost balení samotného (např. krabice, palety, jiné přepravní obaly).
počítání nákladů na dopravu.

.. poznámka::
Přepravní balíčky se běžně používají v tzv. „třístupňovém“ přepravním systému
<../../shipping_receiving/daily_operations/delivery_three_steps>`, mohou být použity v jakémkoli
práce s produkty, které lze uchovat.

... skladovací prostory / sklady / umožnit balení:

Konfigurace
=============

Pro používání balíčků se nejprve přihlaste do aplikace „Inventář“ v nabídce „Nastavení“. V části
v záhlaví „Operace“, aktivujte funkci „Balíčky“ a pak klikněte
:guilabel:`Uložit“.

... obrázek: /balíček/povolit-balík.png
:align:center
:alt:Aktivujte nastavení balíčků v Nastavení > Konfigurace > Nastavení.

... inventář/správa produktů/přesun celé palety:

Při přesunu balíčků v rámci jedné operace lze zapnout funkci „Přesun celého balíčku“.
upravit typ, který aktualizuje umístění položky obsažené v balíčku při aktualizaci umístění balíčku.

Pro toto proveďte následující kroky:
operace, na kterou se tato funkce bude vztahovat (může být potřeba nastavit ji pro více operací).

Na stránce operačního typu v sekci „Přepravní balíky“ zaškrtněte „Přesun celého
Zatržítko balíčků.

... skladování, sklady a skladovací prostory:

Balit věci
==========

Produkty lze přidat do balíčku v jakémkoliv převodu takto:

#Kliknutím na každý z ikon „Podrobné operace“
na výrobní lince.
#. Pomocí tlačítka „Uložit do balení“
vše do převodu do balíčku.

... skladovací prostory, sklady a podrobná operace:

Podrobná operace
-------------------

Při převodu skladu (např. dodací list, objednávka) klikněte na
:guilabel:`⦙≣ (seznam s čárkami)` ikona v záložce „Akce“.

.. obrázek:balíček/podrobné operace.png
:align:center
:alt:Zobrazit ikonu „Podrobné operace“ v produktové řadě.

Tím se otevře okno „Podrobné operace“ pro produkt.

Chcete-li produkt umístit do balíčku, klikněte na „Přidat řádek“ a přiřaďte produkt
:guilabel:`Základní balíček“. Vyberte existující balíček nebo vytvořte nový zadáním
název nového balíčku a pak vyberte možnost „Vytvořit…“.

.. obrázek: balíček/cesta-balíčku.png
:align:center
:alt:Přiřaďte balík do pole „Konečný balík“.

Do balíčku PACK0000001 bylo umístěno dvanáct jednotek Acoustic Bloc Screen.

Poté zadejte počet položek, které se mají vložit do balení, do sloupce „Dokončeno“.
kroků výše k umístění produktu do různých balíčků. Jakmile je hotovo, klikněte
Klikněte na tlačítko „Potvrdit“ pro zavření okna.

.. viz též:
:doc:`Odeslat jeden balíček v rámci jedné objednávky


... skladování, sklady a skladovací prostory:

Připraveno k prodeji
-----------

Alternativně klikněte na tlačítko „Přidat do balíku“ v jakémkoliv převodu z skladu, abyste vytvořili
nový balíček a vložte všechny položky do přenosu do nově vytvořeného balíčku.

.. důležité::
Tlačítko „Vložit do balíku“ se zobrazí na fakturách, dodacích listech a dalších přepravních formulářích.
s aktivní funkcí „Balíčky“ v nabídce „Správa inventáře --> Konfigurace -->
Nastavení.

.. obrázek: balení/vložení do krabice.png
:align:center
:alt:Obrázek tlačítka „Vložit do košíku“ při jeho stisknutí.

V přenosu v balíčku „BATCH/00003“ byla kliknutá tlačítko „Uložit do balení“, aby se vytvořil nový
balíček, „PACK0000002“, a přiřadit všechny položky k němu do pole „Konečný balík“.

.. skladovací prostory/sklady/balení:

Typ balení
============

Vytvořte typy balíčků pomocí přesunu na:menuselection:Inventářová aplikace --> Konfigurace --> Balík
Typy, abyste mohli nastavit vlastní rozměry a hmotnostní limity. Tato funkce se především používá k
vypočítat hmotnost balíku pro přepravní náklady.

.. viz též:
   - :doc:`Dopravci <../../shipping_receiving/setup_configuration/third_party_shipper>`
   - :doc:`../../shipping_receiving/setup_configuration`

Na seznamu „Typ balíčku“ klikněte na „Nový“. Otevře se prázdná forma pro typ balíčku.
Pole s tímto formátem mají následující hodnoty:

- :guilabel:`Typ balíku“ (povinné): definujte název typu balíku.
- :guilabel:Velikost: definujte rozměry balení v milimetrech (mm). Zleva
vpravo definujte „Délku“, „Šířku“ a „Výšku“.
- :guilabel:`Hmotnost prázdného balení“: hmotnost prázdné obálky (např. prázdná krabice, paleta).

.. poznámka::
Odoo spočítává hmotnost balíku přičtením váhy prázdného balíku k váze obsahujícího balík.
položky, které lze nalézt v poli „Hmotnost“ ve složce „Sklad“,
záložka každého produktu.

- :guilabel:`Maximální hmotnost zásilky“: maximální povolená hmotnost v balíku.
- :guilabel:`Čárový kód“: definujte čárový kód, který identifikuje typ balení z skenování.
- :guilabel:`Společnost“: specifikujte společnost, abyste měli k dispozici pouze jeden typ balení.
společnost. Nechte pole prázdné, pokud je dostupná ve všech firmách.
- :guilabel:`Dopravce“: specifikujte dopravce pro tento typ balíku.
- :guilabel:`Kód přepravce“: definujte kód, který je spojen s typem balíku.

.. obrázek: balíček/balíčkový typ.png
:align:center
:alt:Typ balíku pro přepravu FedEx o hmotnosti 25 kg.

... skladovací prostory, sklady a skladování v uzavřených objektech:

Klastry balíčků
================

Pro použití balíčku clusteru, nejprve přejděte na: „Inventář aplikací - Konfigurace“.
Nastavení“ a aktivujte funkci „Masové převody“, která se nachází v
:guilabel:`Operace“ části. To způsobí, že se pole „Použití balíčku“ zobrazí u balíčku
forma.

.. obrázek: balíček/povolit-soubor.png
:align:center
:alt:Aktivujte funkci „Hromadné převody“ v části Inventář > Konfigurace > Nastavení.

Přidejte nové balíčky kliknutím na: „Nastavení --> Skladové zásoby --> Balení“. Pak
:guilabel:„Nový“, nebo vyberte existující balíček. To otevře formulář s balíčkem, který obsahuje
následujících polích:

- :guilabel:`Odkaz na balíček` (vyžadováno): název balíčku.
- :guilabel:`Typ balení“: používá se k :ref:`konfiguraci přepravních boxů pro odeslání zákazníkovi
<skladové zásoby/balení>

.. poznámka::
:guilabel:`Typ balíčku“ je pro konfiguraci balíčků pro výběr clusteru zbytečný.

- :guilabel:`Hmotnost balíku“: slouží k zadání hmotnosti balíku po jeho změření
skalní stěna.
- :guilabel:`Společnost“: specifikujte společnost, abyste balíček nabídli pouze na vybraném místě.
společnost. Nechte pole prázdné, pokud je zásilka dostupná na všech pobočkách.
- :guilabel:`Lokalita“: aktuální umístění balíku.
- :guilabel:`Datum balení“: datum, kdy byl balíček vytvořen.
- Vyberte „Opakovatelné“ pro balíčky, které se používají k přesunu produktů.
skladu; :guilabel:`Nepoužitelné“ pro balíčky používané k odeslání produktů zákazníkům.

.. obrázek:balíček/balíček.png
:align:center
:alt:Zobrazení balíčku pro vytvoření skupiny.

.. viz též:
:doc:`Používáním balíkových metod <../../shipping_receiving/picking_methods/cluster>`

Zobrazit balíčky
=============

Pro zobrazení všech balení přejděte do aplikace „Nastavení“ - „Produkty“ - „Balíčky“. Výchozí nastavení
balíčky jsou zobrazeny v kanbanovém pohledu a jejich aktuální skladovací místo.

.. tip::
Přetáhněte balíčky a přesuňte je mezi vnitřními lokalitami.

.. obrázek: balíček/balíčky-kanban.png
:align:center
:alt: Dashboard balíčků.

