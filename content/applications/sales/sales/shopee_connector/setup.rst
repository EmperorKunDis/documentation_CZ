==============================
Konfigurace Shopee Connectoru
==============================

Odoo umožňuje uživatelům synchronizovat se s účtem prodejce na Shopee v databázi, ale uživatelé **musí**
mít registrovaný účet **Shopee Seller** a **Shopee Open** před dokončením
konfigurace.

Zaregistrujte si účet na platformě Shopee Open, nejprve přejděte na stránku „Shopee Open Platform“.
<https://open.shopee.com/>`, a klikněte na tlačítko „Získat přístup (nyní)“, které se nachází v
v polovině stránky.

Použijte „Průvodce pro vývojáře ShopEea <https://open.shopee.com/developer-guide/12>“ a postupujte podle
registrační proces. Jakmile je vše hotovo, postupujte podle níže uvedených pokynů k registraci a propojení
otevřít účet na Shopee v Odoo.

.. důležité:
Přístup k platformě Shopee a požadavky na prodejce jsou **regionálně specifické**.
To znamená, že pravidla, kvalifikace a procesy se v jednotlivých zemích liší.
S nastavením Odoo Shopee Connectoru ověřte požadavky pro vaši konkrétní oblast Shopee.

**Zásadní poznámky:**

   - **Stav a typ podnikání na Shopee:** Musíte mít aktivní účet prodejce na Shopee
(Fyzická osoba nebo registrovaná firma). Vaše kvalifikace závisí na vašem regionu a oboru podnikání.
registrace.
   - **Počet objednávek/úroveň prodejce (pokud je k dispozici):** V mnoha regionech je vyžadován minimální počet objednávek
v určitém časovém rámci nebo u konkrétního prodejce (např. Mall, Preferred, Managed)
získat přístup k platformě Open.

*Potřebuje se vykonat akce*

   #Určete svou oblast na Shopee.
   #Najděte oficiální dokumentaci pro svou oblast na webu Shopee.
„Otevřený průvodce pro vývojáře <https://open.shopee.com/developer-guide/12>“
   #. Pečlivě si přečtěte požadavky na prodejní účty a přístup k otevřené platformě ve vaší
regionu.
   #Zajistěte, aby váš účet na Shopee splňoval všechny potřebné požadavky *předtím*, než začnete s
Konfigurace propojení Odoo a Shopee.

.. _shopee/nastavení:

Připojte účet prodejce na Shopee k Odoo
=====================================

Nainstalujte nástroj Shopee Connector (sale_shoppe) podle návodu v části „Instalace“
:menu:"Aplikace".

Pak připojte svůj účet na Shopee Open kliknutím na: „Prodejní aplikace –> Konfigurace“.
-->Shopee --> Účty“.

Zde klikněte na „New“ pro vytvoření nového účtu ShopBack.

Poté v záložce „Kredence“ vyberte odpovídající „API konec“.
kliknutím na tlačítko „Přidat do košíku“.

.. poznámka::
Shopee nabízí několik koncových bodů API pro produkci a testování. Vyberte správný koncový bod
je klíčovým faktorem pro úspěšnou integraci. Vyberte konec, který odpovídá vašemu tržišti
lokalita.

   - :guilabel:`Konecní bod Shopee (Singapur)`: Tento konečný bod je primárním bodem pro prodejce v
většině zemí APAC. Vyberte tuto možnost, pokud se nepohybujete na pevnině
Čína nebo Brazílie.
   - :guilabel:`Produkční konec Shopee (Čína)`: Tento konec je určen výhradně pro prodávající.
operující v pevninské Číně. Je navržen tak, aby splňoval místní předpisy a obchodní zvyklosti.
praxe.
   - :guilabel:`Konec výroby Shopee (Brazílie)`: Tento konec je určen pro prodávající
provozující v Brazílii. Vyberte tuto možnost, pokud je vaše obchod s názvem Shopee umístěn v Brazílii.
   - :guilabel:`Konecnice Shopee pro testování a vývoj“: Tato konečná stanice je určená pro účely testování a vývoje
pouze. Používejte ji k simulaci interakce s aplikací Shopee bez ovlivnění vašich skutečných dat.
*Nepoužívejte tento koncový bod pro produkci.*
   - :guilabel:`Konec testování Shopee (Čína)“: Podobně jako u obecného konečného bodu pro testování je
Je určena pro testování integrace související s koncovým bodem výroby v Číně.
*Nepoužívejte tento koncový bod pro produkci.*

Po výběru správného API Endpointu v poli „Kredence“ zadejte svůj Open
Do příslušných polí zadejte „ID partnera“ a „Klíč partnera“. Pak klikněte
:guilabel:`Uložit a autorizovat“.

.. důležité:
Potřebujete své Open Shopee Partner ID a Partner Key k dokončení
krok. Zde je návod, jak je najít v otevřené platformě Shopee:

   #**Přihlaste se do platformy Shopee Open:** Přihlášení na
přihlašovací údaje, které jste použili při registraci vašeho účtu na Open Shopee.
   #**Přejděte do sekce Správa aplikací:** Přejděte na kartu „Správa aplikací“ a poté vyberte
:guilabel:`Seznam aplikací“.
   #**Vyberte svou aplikaci:** Vyberte konkrétní aplikaci, se kterou chcete synchronizovat Odoo (buď vaši
aplikaci nebo vaši produkční aplikaci.
   #**Najděte své přihlašovací údaje:** V podrobnostech o aplikaci najdete svou partnerskou identifikační číslo a partner
Hodnota klíče. Tyto hodnoty budete potřebovat zkopírovat a vložit do příslušných polí.
Odoo.

.. poznámka::
   - Pozor na přesnost zadání: Zkopírujte partner ID a partner klíč bez dalších mezer.
nebo znaky. Ty jsou velmi citlivé na velikost písmen.
   - **Uchovejte svůj klíč v bezpečí:** Partnerský klíč je citlivá informace, nikomu ji nedávejte
kohokoliv. Přistupujte k němu jako ke heslu.

Autorizace a registrace účtu
======================================

Po přihlášení do účtu Shopee Seller přes Odoo <shopee/setup> se zobrazí
začíná proces.

Výběr účtu prodejce na Shopee
-------------------------------------

Po kliknutí na tlačítko „Uložit a autorizovat“ je uživatel přesměrován do výběru prodejce na Shopee.
stránka.

- Přihlášený uživatel: Pokud jste již přihlášeni do svého účtu na Shopee, můžete použít e-mailovou adresu nebo
Zobrazí se uživatelské jméno. Klikněte na svůj účet a pokračujte dál.
- **Nelogovaný uživatel:** Pokud nejste přihlášeni, budete vyzváni k zadání přihlašovacích údajů


Přidělování přístupu k Odoo
-----------------------

Po výběru nebo přihlášení do svého účtu prodejce na Shopee vás systém přesměruje na
autorizační stránka. Zde potvrďte, že umožňujete společnosti Shopee udělit aplikaci Odoo přístup k vašim
účet a související data. Tento krok je nezbytný pro správnou funkci integrace.

Registrace účtu a vytvoření obchodu na Shopee
=============================================

Poté, co potvrdíte přístup, vás Shopee vrátí zpět do Odoo. Zobrazí se indikátor, který potvrzuje, že
Váš účet na Shopee byl úspěšně zaregistrován.

Konfigurace po synchronizaci
----------------------------------

Po přesměrování proveďte v Odoo následující kroky:

#**Přejmenujte účet na Shopkee (volitelně):** Nový účet na Shopkee vytvořený v Odoo bude pravděpodobně
má výchozí název. Můžete ho přejmenovat na něco více popisného (např. jméno vaší společnosti).
pro snadnější správu.
#**Datum synchronizace poslední objednávky:** Toto nastavení určuje, od kterého data se bude počítat
získávání objednávek ze Shopee. Vyberte datum, od kterého chcete, aby Odoo získával staré objednávky.
#**Nastavení synchronizace skladu:** Rozhodněte se, zda chcete synchronizovat své produkty
zásoby mezi Odoo a Shopee. Zapněte možnost „Synchronizace zásob“.
automaticky aktualizovat zásoby z Odoo do Shopee. Vypnutí této možnosti zabrání automatickým
aktualizace zásob.
#**Přidělte výchozí prodejní tým:** Přidejte výchozí prodejní tým do vašeho účtu na Shopee v Odoo.
To pomáhá při reportingu a správě objednávek.

S úspěšně registrovaným účtem na Shopee jsou dostupné tržiště s tímto konkrétním
účet lze později synchronizovat stejným způsobem a uvést pod štítkem „Obchody“.
tlačítko.

Shopee objednávky v Odoo
=====================

Při synchronizaci objednávky na Shopee jsou vytvořeny pouze řádky pro položky na prodejní objednávce v Odoo.
Každá z nich představuje jednu prodanou položku na Shopee.

.. obrázek:setup/shopee-sales-odoo.png
:alt:Shopee synchronizuje prodejní objednávky v Odoo.

Všechny potřebné cenové vyrovnání související s dopravou nebo příjmy a poplatky lze řešit později.
pomocí týdenních/měsíčních finančních výkazů společnosti Shopee, které lze následně importovat do systému Odoo
Aplikace pro účetnictví.

Vybrání databázového produktu pro položku objednávky se provádí shodou
:guilabel:`Vnitřní odkaz“ (vlastní identifikátor produktu v Odoo, například „FURN001“)
s kódem SKU z e-shopu Shopee.

Pokud není pro daný vnitřní odkaz nalezen žádný produkt databáze s shodným
:guilabel:„SKU Shopee“, pak výchozí databázový produkt „Item Shopee“.

.. poznámka::
Chcete-li upravit výchozí produkty, zapněte režim pro vývojáře a přejděte na
:menu_selecce:`Prodejní aplikace --> Konfigurace --> Nastavení“. V sekci :guilabel:`Konektory“
pod:guilabel:`Shopee Sync“, najděte:guilabel:`Default Products“.

Konfigurace produktových daní
=========================

Pro daňové vykazování prodejů na Shopee s Odoo jsou aplikovány daně z objednávky
ty, které jsou stanoveny na produktu nebo určeny fiskální pozicí
<../../../finance/fiskalni_lokalizace>.

Ujistěte se, že máte na své produkty v Odoo správně nastavené daně nebo nechte tuto práci na fiskální
položky, aby nedocházelo ke konfliktům v součtech mezi *Shopee Seller Central* a Odoo.

.. poznámka::
Protože Shopify nemusí aplikovat stejné daně jako ty definované v Odoo, může se stát
Výsledná částka se liší o několik centů mezi Odoem a *Shopee Seller Central*.
rozdíly lze vyřešit smazáním, když se platby v Odoo sloučí.

.. _shopee/add-new-marketplace:

Přidejte nový trh
=====================

Chcete-li přidat nový trh, postupujte takto:

#**Přejděte do části „Účty“:** Přejděte na: `Prodej -> Konfigurace -> Účty`.
#**Vytvořte nový účet na ShopEe:** Klikněte na „New“ pro vytvoření nového účtu na ShopEe.
účet.
#**Vyberte koncový bod API:** Vyberte vhodný koncový bod API pro místní trh.
(Většinou bude tento název:guilabel:`Produkční koncový bod Shopee (Singapur)` pokud nejste
provozující v pevninské Číně nebo Brazílii. Podrobnosti o koncových bodech naleznete v dokumentaci.
výběru).
#**Přihlaste se pomocí přihlašovacích údajů:** Vaše „ID partnera“ a „klíč partnera“ jsou stejné jako
to jsou ty, které jsou spojené s vaším jedinečným účtem na Open Shopee. Zadejte je do příslušných polí.
#**Název obchodu:**Přidejte novému obchodu popisný název (například „Shopee Philippines“), který bude sloužit k identifikaci
To se později ukáže.
#**Přidělte prodejní tým:** Přidejte relevantní prodejní tým (například „Shopee Sales Philippines“).
poskytnout pokročilé možnosti reportingu.
#**Synchronizujte svůj účet:** Pokud žádný z vašich stávajících tržišť není uveden, klikněte na
:guilabel:`Přihlásit se s jiným účtem“ k synchronizaci nového. To zahájí proces nákupu na Shopee
autorizační proces.

Automatické synchronizace
-------------------------

Při přidání nových tržišť se automaticky přidají do seznamu synchronizovaných tržišť. Pokud je
Po synchronizaci se tržiště v seznamu nezobrazuje. To znamená, že tržiště
nebo není pro konkrétního prodejce dostupná.
účet. Pro další informace se obraťte na dokumentaci platformy Shopee Open nebo na jejich podporu.
pomoc.

.. důležité:
Odoo umožňuje vytvořit stejný obchod na Shopee vícekrát, ale bude fungovat jen jeden z nich.
z důvodu omezení počtu tokenů. Protože se mohou objevit problémy s objednávkami, synchronizujte každý obchod pouze jednou.
aktualizace spojení, ručně stáhněte objednávky před obnovou spojení.

.. viz též:
   - :doc:`Podporované funkce a tržiště <../shopee_connector>`
   - :doc:`spravovat`
