=======================
Správa objednávek na Shopee
=======================

Mapování produktového katalogu
=======================

Noví zákazníci Odoo bez existujících produktů
--------------------------------------------

Pokud začínáte s novou databází Odoo a vaše produkty jsou k dispozici pouze na Shopee, můžete své
Katalog produktů z Shopee do Odoo.

#**Export katalogu Shopee:** Vyberte možnost *Masová funkce* a exportujte produktový katalog z
Shopee, které zahrnuje i SKU Shopee.

.... obrázek: manage/shopee-seller-centre-product-extract.png
:alt:Výběr funkce v Shopee.

#**Import do Odoo:**:doc:`Import <../../../essentials/export_import_data>` exportovaného katalogu
Do Odoo je možné importovat i zboží nakoupené na Shopee. Během procesu importu je důležité správně přiřadit SKU ze Shopee k produktům v Odoo.
*Vnitřní odkaz* v Odoo. Tento prvek bude sloužit jako spojení mezi vaším Shopeem a
Odoo produkty.

Zákazníci, kteří již používají Odoo a mají produkty v Odoo
-----------------------------------------------------

Pokud již máte produkty v databázi Odoo, budete si muset připojit své nabídky na Shopee k
stávající produkty Odoo.

#**Export katalogu Shopee:** Vyberte možnost „Masová funkce“ a exportujte produktový katalog z Shopee.
(včetně SKU na Shopee) a exportujte svůj produkt pomocí příkazu „:doc:`export <../../../essentials/export_import_data>`“
katalog z Odoa (včetně interních odkazů).
#**Mapa v tabulce:** Využijte tabulku k mapování produktů. Srovnejte SKU z Shopee s
Export ze Shopee s odpovídajícím interním referenčním kódem z exportu z Odoo. Vytvořte sloupec
který propojuje SKU na Shopee s interním referenčním číslem v Odoo.
#**Aktualizace produktů Odoo:**Importujte aktualizovaný sešit zpět do Odoo. Použijte mapování, které
vytvořené v tabulce, které aktualizují pole „Vnitřní odkaz“ vašeho stávajícího systému Odoo.
produkty s odpovídajícím kódem SKU na Shopee. Toto spojení mezi vaším Odoem a
Produkty z obchodu Shopee.

.. důležité:
Synchronizace produktového katalogu mezi Odoo a Shopee není automatická.
**ruční operace**, kterou musíte zahájit. Postup se liší v závislosti na tom, zda jste
produkty již v Odoo existují.

Synchronizace objednávek
=====================

Objednávky jsou automaticky stahovány z Shopee a synchronizovány v Odoo na **pravidelných intervalech**.

Synchronizace je založena na stavu objednávek v aplikaci Shopee: pouze objednávky, jejichž stav se změnil
od poslední synchronizace jsou načítány z Shopee, což obsahuje změny pouze na Shopee.

Pokud je objednávka zrušena na Shopee, aktualizuje stav objednávky v Odoo. Na druhou stranu
Pokud je objednávka zrušena v Odoo, změna se nebude projevovat na Shopee.

Pro každou synchronizovanou objednávku vytvoří Odoo prodejní objednávku a zákazníka (kontakt), pokud
Zákazník nebyl dříve importován z Shopee nebo není již v databázi uveden.

.. poznámka::
Princip synchronizace spočívá v tom, že se stahují pouze objednávky, které je potřeba odeslat.
(tj. „VYEXPEDOVÁNO“, „ZRUŠENO“, „NEZAPLACENO“, „DOKONČENO“).

Synchronizace sil
=====================

Aby se zadání objednávky s **nezměněným** stavem odeslalo do zpracování.
předchozí synchronizace:

Pak přejděte do účtu na Shopee v aplikaci Odoo:menuselection:„Prodej --> Konfigurace --> Shopee“
--> Účet --> Obchod. Upravte datum pro: „Poslední synchronizace objednávky“ pod „Objednávky“.
Další postup.

Ujistěte se, že vyberete datum před poslední změnou stavu požadované objednávky.
synchronizovat a uložit. Tím zajistíte, že se synchronizace provede správně.

Spravujte dodávky v režimu „Fulfilled by Merchant“
========================================================

Při každém synchronizačním procesu objednávky typu FBM (Fulfilled by Merchant) v Odoo je okamžitě vygenerován výdej.
v aplikaci Inventura vytvořené spolu s prodejním příkazem a zákaznickým záznamem.

Při potvrzení vybraného balení je nutné kliknout také na položku „Sestavit“.
Váš účet prodejce na Shopee a zobrazit si „Dodání“ v seznamu položek, abyste mohli vygenerovat a stáhnout
:guilabel:`Dodací štítek“ a :guilabel:"Číslo sledování".

Stavy doručení na Shopee
------------------------

Důležité je pochopit různé stavy dodání na Shopee
Účinně. Podívejte se na přehled:

- **Připraveno k odeslání:** Prodávající může nyní zadat požadavek na expedici pro tento objednávkový formulář.
- Dodání zajištěno: Prodávající dodání zabezpečil online a obdržel číslo pro sledování
od třetí strany, která poskytuje služby logistiky třetích stran (3PL).
- Doručeno: balíček byl doručen na místo třetích stran nebo vyzvednut
poskytovatel.
- Zrušeno: Objednávka byla zrušena.
- **Nepodařilo se vyzvednout balík:** Zkusit vyzvednutí zásilky třetí stranou nevyšlo. Prodávající musí přeorganizovat odeslání.
a zbytku obsahu plnění objednávky.

.. obrázek: manage/shopee-delivery-orders-status.png
:alt:Stav doručení na Shopee v Odoo.

.. důležité:
Nejsou podporovány pro NSSL

Tato funkce není dostupná pro :abbr:`NSSL (Non-Shopee Supported Logistics)“, musíte
ručně vytvořit dodací štítek a sledovací číslo na webu/aplikaci přepravce.
Zkontrolujte svou oblast pro seznam podporovaných logistických služeb (např. „Malajsie
<https://seller.shopee.com.my/edu/article/388>

Shopee vyžaduje od uživatelů, aby při každé dodávce poskytli sledovací číslo. To je nutné k
přidělit dopravce.

Pokud dopravce automaticky neposkytuje sledovací číslo, musí být nastaveno ručně.
Toto pravidlo se vztahuje na všechny tržiště Shopee.

Sledovat dodávky v Odoo
=========================

Pro objednávky typu „plněno obchodníkem“ („FBM (Fulfilled by Merchant)“) je v Odoo automaticky vytvořen pohyb zásob.
Shopee konektor díky stavu doručení Shopee.

.. obrázek: manage/shopee-wh-out.png
:alt:Přesun zboží vytvořený pro objednávku na Shopee v Odoo.

Proces plnění objednávek
-------------------------

Tato část popisuje proces plnění objednávek na Shopee v rámci systému Odoo, od vytvoření objednávky po
Aktualizace zásob.

#**Vytváření nových objednávek:** Když zákazník na Shopee vytvoří novou objednávku, je automaticky vytvořena
Odoo.
#**Připravte odeslání na Shopee:**Předtím, než může být objednávka odeslána, musíte
přepravu prostřednictvím samotné platformy Shopee. Obvykle jde o výběr přepravce
poskytovatel, vytvářející dodací štítek, a plánující odběr nebo předání zásilky. Odoo ne
převzít fyzické dopravní aranžmá, které je zcela v rukou Shopee.
#**Získat štítek pro doručení na Shopee (doručovací lístek):** Jakmile je objednávka uskutečněna na Shopee,
Odoo stáhne vygenerovanou dodací adresu, která slouží jako dodací list.
obsahuje důležité informace, jako je číslo sledování a je nezbytné pro tisk.
připojením štítku k balíčku. Štítek je do systému Odoo importován a spárován s
příslušnou objednávku na prodej.
#**Kontrola skladových zásob v Odoo:** Po získání dodací etikety je nutné kontrolovat
pohyb zásob v Odoo, což potvrzuje, že objednané položky opustily vaše sklady nebo
zásoby. Zkontrolování skladových zásob sníží úrovně zásob v Odoo.
#**Aktualizace zásob na Shopee:** Nakonec Odoo posílá aktualizované skladové úrovně zpět do Shopee.
To zajišťuje, že vaše nabídky na Shopee odpovídají aktuálnímu skladování a zabraňují přeprodávání.
přesnost zásob vašich produktů. Tato synchronizace udržuje vaši prodejnu na Shopee aktuální.
Zůstaňte v obraze ohledně zásob ve vaší Odoo.

Registrace plateb
=================

Protože zákazníci platí Shopee jako prostředníka, je vhodné založit nový bankovní účet (např.
„Shopee platby“), s vlastním účtem „Banka a hotovost“ je doporučený.

Další výhodou je, že Shopee provádí jediný týdenní nebo měsíční účet, takže můžete vybrat všechny faktury spojené
Při registraci plateb je nutné uvést jednotnou platbu.

Pro to použijte příslušný záznam v deníku „Shopee platby“ a vyberte
„Skládání“ jako „Způsob platby“.

Poté vyberte všechny vytvořené platby a klikněte na „Akce“ > „Vytvořit hromadnou platbu“.
--> Zkontrolovat.

..tip:
Toto stejné akce lze provést s fakturami dodavatelů od Shopee, které jsou určeny pro poplatky/provize.

Když je vyrovnání připsáno na účet v průběhu týdne či měsíce a banka
Přihlášky jsou zaznamenány a kreditovaný je účet prostředníka Shopee v částce přijaté.

Analýza prodejů na platformě Shopee s pomocí reportingu v Odoo
============================================

Přístupová stránka Odoo shromažďuje prodejní údaje ze všech vašich propojených prodejních kanálů a poskytuje
komplexní přehled o vašem podnikání. Pro specifickou analýzu prodejů na Shopee
budete potřebovat nakonfigurovat prodejní týmy pro vaše obchody na Shopee. Tato konfigurace vám umožňuje filtrovat a
izolovat prodejní data na platformě Shopee v rámci přehledu Odoo.

Nastavení prodejních týmů pro Shopee
-------------------------------------------

Výchozí nastavení je takové, že tým prodeje vašeho účtu na Shopee sdílíte s celou společností.
Pokud chcete vytvářet samostatné zprávy pro konkrétní obchody nebo tržiště, budete potřebovat přiřadit
Prodejní týmy.

#**Přidělení prodejního týmu k vašemu obchodu na Shopee:** Přejděte do konfigurace účtu
(obvykle se nacházejí pod :menuselection:`Prodej --> Konfigurace --> Účty“). V rámci
údaje o účtu, přiřadit konkrétní prodejní tým k vašemu obchodu na Shopee.
#**Filtrujte prodeje na přístrojové desce:** Jakmile jsou týmy prodeje přiřazeny, můžete použít
filtry na přehledovém panelu, abyste mohli zobrazit prodejní údaje konkrétně pro své obchody na Shopee.
prodejní tým, který izoluje a analyzuje vaše výkony na Shopee.

.. viz též:
   - :doc:`Podporované funkce a tržiště <../shopee_connector>`
   - :doc:`setup`
