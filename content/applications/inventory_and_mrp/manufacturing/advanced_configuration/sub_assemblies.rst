===============
Multilevé BoM
===============

.. |BOM| nahradit za: zkratka: `BoM (Bill of Materials)`
.. |BOMy| nahrazují:: :abbr:`BOMs (Seznamy materiálů)`
.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`

Použijte víceúrovňový seznam materiálů (BOM), pokud je vyrobený produkt součástí jiné sestavy.
Tento způsob umožňuje vložit |BOM| do jiného |BOMu| a organizovat složité výrobky, zatímco zjednodušuje
výrobou, kdy je každý krok nákupu a výroby odděleně definován.

Podúrovně BOM (podsestavy nebo polotovary) zjednodušují tyto výrobní procesy a
Jsou užitečné, pokud se podsestava používá v různých finálních výrobcích (tj. pokud by se
na více vrcholových BOMech). Čím složitější je výroba nebo nákup produktu, tím větší hodnota
multilevel BOM může poskytnout. Proto je plánování zásobování komponent a podsestav důležité
je nezbytná pro zajištění hladkého chodu víceúrovňových BOMů.

Proč je důležité plánování zásob
=======================================

:doc:`Dodávky <../../inventory/warehouses_storage/dodavky>` jsou kritické pro víceúrovňové
BoMs zabraňují vzniku zácp a řídí časové plány i skladovou dostupnost. Bez nich by chyběly
komponenty mohou zastavit výrobu, oddálit objednávky a zvýšit náklady. Plánované doplňování zásob
Strategie zajišťuje „dodání včas“.
<../../skladové zásoby/dodávky/dodavatelé/nastavení pravidel replnění>`, :doc:"automatizuje nákup
<../../inventory/warehouses_storage/replenishment/reordering_rules>“, vyrovnává zásoby a
Zajišťuje efektivní dodavatelské řetězce. To minimalizuje zpoždění, snižuje manuální úsilí a zajišťuje hladký
výroba.

Objednávky výroby (MO), které pocházejí z BOM, vyžadují, aby byly všechny součásti k dispozici před
Tento |MO| lze dokončit, a to je zobrazeno v poli „Stav komponenty“ na stránce s informacemi o tomto |MO|.
Naučte se, jak zkontrolovat stav komponenty MO: doc:~bill_configuration

..._výroba/pokročilá/vytvořit víceúrovňový BOM:

Vytvořte víceúrovňový BoM
=======================

Pro vytvoření víceúrovňové BOM je nutné nejprve vytvořit produktovou BOM pro vrcholový produkt a produktové BOM pro podřízené produkty.
Pokud začínáte od nuly, postupujte od nejnižší úrovně produktu.
Pak je třeba tyto produkty zahrnout jako součást vyšší úrovně „BOM“.

Příklad:
Tisková deska klávesnice obsahuje stovky elektronických součástek.
komponenty, jako jsou tranzistory, odporové prvky a kondenzátory. Namísto uvádění všech těchto
komponenty ven, vytvoří se podúrovňový produkt a BOM pro PCB, který sleduje množství
- tranzistory a další malé součástky bez nutnosti přeplňovat výrobní listinu (BOM) pro
vlastní klávesnice a zobrazit je. Namísto toho se BOM klávesnice sestává z různých
komponentů a podúrovní BOM stejně jako klávesnice, spínače, deska plošných spojů a základna klávesnice.

:dokument:„Naučte se vytvářet jednoduchou specifikaci materiálů <../basic_setup/bill_configuration>.
PCB, což zahrnuje tranzistory, odporové prvky a další součásti.

.. obrázek: sub_assemblies/sublevel-bom.png
:alt: Seznam součástek pro plošný spoj.

Po úplném konfigurování podúrovňových produktů (jako jsou klávesnice, klávesy a deska klávesnice)
Vytvořte produkt na úrovni nadřazenosti kliknutím na:
Produkty“ a poté vyberte „Nový“. Zde upravte specifikaci produktu
nebylo nutné.

Jakmile je konfigurován hlavní produkt (klávesnice), klikněte na „Seznam materiálu“.
tlačítko na produktovém formuláři a poté vyberte: guilabel: New | BOM | pro vrchní úroveň
produktu. Přidejte podúrovňové produkty do této BOM a všechny další potřebné součástky.

.. obrázek: součástky/sestava.png
:alt: Seznam komponent pro klávesnici obsahující seznam komponent pro desku plošných spojů.

Řízení plánování výroby
==========================

Níže uvedené dvě možnosti jsou dvě z nejlepších způsobů, jak automatizovat objednávky výroby pro produkty.
s víceúrovňovými BOM.

.. poznámka::
Komplexní BOM se používá k řízení výrobků, které vyžadují složené součásti.
a vytváří se BoM pro organizování komponent nebo balení prodejných produktů, viz dokumentace:
místo toho použijte „<dodání v krabici>“.

Automaticky spouštět objednávky na výrobu podúrovňových produktů po potvrzení výrobní zakázky
objednávku hlavního produktu je dvě možnosti:

- **Možnost 1 (doporučeno):** Vytvořte pravidla pro přesunutí produktů na nižší úroveň a nastavte obě
minimální a maximální potřebné zásoby na „0“.
- **Možnost 2:**Aktivujte trasy „Dodání na objednávku (MTO)“ a „Výroba“.
pod záložkou Inventář v produktovém formuláři podúrovňového produktu.

.. viz také:
   - :doc:`../../skladovani/dodavky/naskladnovani/pravidla-pro-dodavku
   - :doc:`../../sklad/dodavky/dodavky_do_skladu/mto`

Volba číslo 1 je flexibilnější než volba číslo 2 a je doporučena. Pravidla pro přeřazování nejsou přímo spojená
požadovat doplnění zásob, které umožňuje uvolnit zásoby a přidělit je podle potřeby.
Přepravní trasa objednávky (MTO), ale jedinečně propojuje produkty nižšího a vyššího řádu, rezervující množství
potvrzený výrobní závazek na nejvyšší úrovni.

V obou metodách musí být výrobky nižší úrovně kompletně vyrobeny před zahájením produktu nejvyšší úrovně.

Nastavení sítě BoM v několika úrovních
=========================

Následující část popisuje, jak nastavit víceúrovňové BoM, zadat počáteční zásoby a vytvořit
„Pravidlo pro přesun 0/0/1 <Výroba/Advanced/Způsob nákupu>“ (doporučená výrobní praxe)
plánovat termíny, nastavit časové plány a zvolit způsoby výroby.

Vytvoření pravidla pro přeskládání zboží na úrovni podúrovní (minimální zásoba nastavena na nulu, maximální zásoba
(přiřazen na nulu, automaticky přečíslovat) bez ohledu na to, zda jsou součástí nebo podsestavou.
doporučený přístup k řízení víceúrovňového BOM. Tento systém používá zásoby
Aplikace **Výroba** a **Nákup**.

.. důležité::
To je jen jedním příkladem, jak vytvořit víceúrovňový BOM v Odoo. Zvažte všechny unikátní
okolnosti, které je třeba řešit při konfiguraci a ujistěte se, že jsou zahrnuty
v nastavení. Pokud bude potřeba jakýkoliv konkrétní typ pomoci při nastavování, zvažte koupi balíčku „úspěchu“.
<https://www.odoo.com/pricing-packs>.

Vytvořte BoM
---------------

Postupujte podle kroků v návodu :ref:`Vytvoření víceúrovňového BOM <manufacturing/advanced/create-multilevel-bom>`.
sekce pro stavbu bomb.

Ujistěte se, že vytváříte víceúrovňový BOM odspodu nahoru. Začněte tím, že vytvoříte nejnižší úroveň
součástky v Odoo, pak součástky, které se používají pro tyto součástky a nakonec |BOM|
pro tuto sestavu a opakujte, dokud nebude vytvořena celá hierarchie BOM.

Zadat počáteční zásoby
-------------------------

.. poznámka::
Pokud není k dispozici počáteční soupis majetku, který by bylo možné nakonfigurovat, přeskočte tento oddíl a začněte konfigurovat
způsob nákupu pro víceúrovňový BOM.

Aktualizujte množství skladem pro každý z produktů nakonfigurovaných v předchozím kroku (obě složky,
sestavami a konečným výrobkem. Chcete-li to provést otevřete aplikaci **Inventář** a pak najděte
produkty s filtry, vyhledávacím polem nebo posouváním a pak na ně klikněte pro otevření jejich produktu
formulář. Zde klikněte na tlačítko „Na skladě“ a vyberte variantu
pokud je tato konfigurace povolena, a poté zadejte
Dostupné množství.

.. viz také:
:doc:`../sklady-a-ukladiste/správa-skladu/počet-produktů`

... výroba/pokročilá/získávání metoda:

Nastavte způsob nákupu
--------------------------------

Nyní je čas vybrat si způsob nákupu, který používá tato víceúrovňová struktura BOM. Následující dvě možnosti jsou
přednostní, ale v některých případech může být jiný způsob zadávání zakázek více smysluplný.

- **Možnost 1 (doporučeno):** Vytvořte pravidla pro přesunutí produktů na nižší úroveň a nastavte obě
minimální a maximální potřebné zásoby na „0“.
- **Možnost 2:**Aktivujte trasy „Dodání na objednávku (MTO)“ a „Výroba“.
pod záložkou Inventář v produktovém formuláři podúrovňového produktu.

.. viz také:
   - :doc:`../../skladovani/dodavky/naskladnovani/pravidla-pro-dodavku
   - :doc:`../../sklad/dodavky/dodavky_do_skladu/mto`

Pravidla přehodnocování jsou doporučena, protože nezavazují k výrobě konkrétního produktu.
objednávka prodeje, která umožňuje, aby vyrobený produkt splnil jinou objednávku na prodej v případě, že původní
je zrušen.

Výroba na zakázku není doporučována, protože vyrobené zboží nelze použít k
splnit další objednávku. Ale může být užitečné, pokud je nutná přísná kontrola
podnikání.

Zadejte dodací lhůty pro dodavatele a výrobce
-----------------------------------------

Doba dodání a doba výroby jsou používány v Odoo k koordinaci výroby a nákupu
akce, které zajistí dodržení termínů objednávek. Ustanovte dodací lhůty pro komponenty, které jsou zakoupeny.
Může se objevit na jakémkoli úrovni v hierarchii výrobku, kromě finálního produktu. Zadejte časové rozpětí pro výrobu
pro výrobky, které jsou vyrobeny pomocí |BOM|. Tyto položky se mohou objevit na jakémkoliv úrovni v hierarchické struktuře |BOM|
s výjimkou nejnižší úrovně (kdy jsou jednotlivé komponenty nakupovány).

.. viz také:
:doc:`../sklady-a-skladovani/dodavky/dodacni-lhuty`

Zajistit provoz, který bude zvládat produkční proud
--------------------------------------------------

Nejprve určete současný výrobní proces pro podnikání a pak vyberte odpovídající Odoo.
konfigurace. Níže uvedený seznam je pouze několika příklady konfiguračních prvků, které mohou být zapojeny do tohoto kroku.

- Kroky výroby: Zvažte, kolik kroků výroby je zapotřebí (jednokrokové, dvoukrokové nebo vícekrokové).
třístupňového výrobního procesu.
- *Centra práce*: Zjistěte, zda je třeba nakonfigurovat nějaké :doc:`centrum práce <používání_centra_práce>`.
- **Plán výroby**: Pokud jsou potřeba ručně plánované objednávky na výrobu (například pro
(vypořádat se s sezónní poptávkou), vytvoříte „hlavní výrobní plán“ (MPS).

..tip:
Výrobní operace je uměním i vědou, takže konfigurace zavedeného proudu do Odoo
je doporučený přístup k této fázi. Další informace o výrobě v Odoo najdete na stránce:
<../výroba>

Shrnutí konfigurace
---------------------

Na konci procesu je nakonfigurován víceúrovňový BOM a produkt na nejvyšší úrovni má své
sčítání zásob, způsoby nákupu, doba dodání a výrobní operace
konfigurovat. Zde lze do prodejních objednávek zahrnout i nadřazený produkt a automatické nákupy prostřednictvím
Prodávající nebo výrobce může začít prodávat své produkty na e-shopu.

.. viz také:
   - :doc:`../../../sales/sales/sales_quotations/create_quotations`
   - :/dokumenty/webové stránky/obchod/produkty/katalog
