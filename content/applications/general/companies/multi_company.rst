=============
Společnost s více subjekty
=============

.. viz též:
:ref:`Filialy <obecne/spolecnosti/filialy>`

.. |mcd| nahradit:: více společností databáze

V Odoo lze pro jednu databázi nakonfigurovat více společností. To umožňuje sdílení některých dat
mezi společnostmi a zachovat nějakou separaci mezi subjekty.

Centralizované prostředí správy umožňuje autorizovaným uživatelům vybírat více společností
současně a nastavit své specifické sklady, zákazníky, vybavení a kontakty.
generuje zprávy s agregovanými čísly bez přepínání rozhraní a usnadňuje každodenní úkoly.
Zlepšení celkového řídicího procesu.

.. varování:
Povolení funkce více společností v databázi Odoo na plánu Standard je automatické.
Aktivuje prodej na vyšší plán „Custom“. Toto se netýká databází v tarifu „One-App Free“.
plán.

   - **Pro roční nebo víceleté smlouvy**: Upsell objednávka je vytvořena se 30denním limitem.
   - Pro měsíční smlouvy: Služba automaticky přechází na plán *Vlastní*.
nová sazba se použije při vystavení další faktury.

Pro více informací se podívejte na stránku „Ceník Odoo“ <https://www.odoo.com/pricing-plan>.
Kontaktujte svého obchodního zástupce.

... konfigurace pro více společností:

Konfigurace
=============

Otevřete aplikaci Nastavení, přejděte do sekce „Společnosti“ a klikněte
:icon:`oi-arrow-right` :guilabel:`Správa společností“. Pak klikněte na :guilabel:`Nový“ a vyplňte
formulář s informacemi o společnosti (<obecné/firmy/firma>), nebo vyberte existující společnost
upravit ho.

.. poznámka::
Alternativně je možné vytvořit společnost navštívením:
a společnosti --> Společnosti.

.. tip::
Pokud chcete archivovat společnost, postupujte takto:

   #V aplikaci Nastavení přejděte do sekce „Společnosti“ a klikněte na
:icon:`oi-arrow-right` :guilabel:`Správa společností“.
   #V seznamu společností v zobrazení „Společnosti“ vyberte společnost k archivování.
   #Klikněte na ikonu „Nástroje“ a zvolte možnost „Archivovat“.
   #Klikněte na tlačítko „Archiv“ a potvrďte.

..._generální/multikomoditní/multikomoditní prostředí:

Multimodální prostředí
=========================

V prostředí více společností jsou uživatelé oprávněni k přístupu do jedné nebo více společností
<generální/více společností/uživatelský přístup> a :ref:`dat
<obecné/více společností/sdílené a nezávislé záznamy> se vytváří nebo mění podle jejich účelu
používání v rámci této struktury.

.._přístup pro více společností/uživatele:

Přístup uživatele
-----------

Multifiremní prostředí umožňuje flexibilní kontrolu přístupu uživatelů:
a práva přístupu <../users/access_rights>, které lze udělit nebo omezit podle potřeby.

.._generální/více společností/výběr společnosti:

Výběr společnosti
----------------

Chcete-li přepínat mezi (nebo vybírat) více společnostmi, postupujte takto:

#Klikněte na tlačítko „Zvolit společnost“ v horním pravém rohu hlavního menu.
#Vyberte si z roletky požadované společnosti a zaškrtněte u nich příslušné políčko.
#Značky označené tučným písmem ukazují na aktuální aktivní prostředí.
#Chcete-li přepnout na jinou společnost, klikněte na její název v seznamu vybraných společností.

.. příklad::
V následujícím příkladu může uživatel zobrazit šest společností, dvě z nich jsou vybrány.
aktivní společností je My Company (San Francisco).

.... obrázek:: multi_company/multi-companies-menu-dashboard.png
:alt: Pohled na nabídku firem v hlavním panelu Odoo.

..._souborů společných a nezávislých.

Společné a firemně specifické záznamy
-----------------------------------

Data jako jsou produkty, kontakty a zařízení mohou být buď sdílena mezi společnostmi nebo omezena
konkrétní společnosti nastavením pole :guilabel:`Company` na příslušných záznamů:

- nebo nechat pole prázdné, aby bylo přístupné pro všechny společnosti.
- nebo vybrat konkrétní společnost, aby se zobrazila uživatelům přihlášeným do této konkrétní společnosti.

Záznamy, které jsou přímo spojeny s konkrétní společností, jsou přístupné pouze v rámci této společnosti.
Příkladem jsou faktury, zálohové faktury, dodací listy a smlouvy se subdodavateli.
do této společnosti přihlášen a příslušná společnost je automaticky vybrána jako výchozí.
zobrazené v poli „Společnost“ ve formuláři pro zadání údajů o společnosti.

Ve společnosti McDonald's se nové produkty a kontakty sdílejí mezi firmami automaticky.
konkrétní společnosti, nastavte pole „Společnost“ na formuláři záznamu.

.. _obecné/více společností/mezi společnostmi:

Transakce mezi společnostmi
==========================

Funkce „Transakce mezi společnostmi“ umožňuje jedné společnosti v databázi prodat nebo
nakoupit zboží a služby od jiné společnosti v rámci stejné databáze. Podle
konfigurační nastavení, protistranické dokumenty k objednávkám a fakturám lze automaticky generovat.
a synchronizované.

.. varování:
Pro správné zpracování mezipodnikových transakcí je třeba použít:
<../../finance/účetnictví/začínáme> a musí být nastaveny správně konkrétní konfigurace.
včetně:doc:`daňových pozic <../../finance/účetnictví/daně/daňové_pozice>“
:doc:`lokalizace <../../finance/fiskální_lokalizace>“.

Pro aktivaci transakcí mezi společnostmi vyberte příslušnou společnost v :ref:`vybíráči společností
<generální/více společností/vyberte společnost>“, otevřete aplikaci Nastavení a přejděte na
V sekci „Společnosti“ zapněte „Meziplátce“, poté stiskněte tlačítko „Uložit“.
Pak vyberte možnost(y), která vytvoří protějšek pro vybranou společnost:

- :guilabel:`Vytvořit faktury a vrácení peněz“: Vytvořte fakturu/vrácení peněz, když společnost potvrdí
fakturu/daňový doklad pro vybranou společnost. Pro vytvoření platné faktury/vratky zvolte
:guilabel:`Vytvořit a ověřit“.
- :guilabel:`Vytvořit objednávku“: Vytvořte objednávku, když je objednávka
je potvrzena pro vybranou společnost. Chcete-li vytvořit platnou objednávku místo cenové nabídky,
výběr: guilabel:"Vytvořit a ověřit".
- :guilabel:`Vytvořit poptávku“: Vytvořte poptávku
při objednávce použít sklad vybrané společnosti v poli „Použít sklad“
je pro vybranou společnost potvrzena objednávka. Vytvoří se platná objednávka namísto požadavku
pro citování vyberte: guilabel:'Vytvořit a ověřit'.

.. poznámka::
Pro transakce mezi společnostmi musí být produkty sdílené.
mezi zapojenými společnostmi.

.. příklad::
:guilabel:`Vytvořit faktury a vrácení peněz“: když je vystavena faktura pro
zveřejněno na „JS Store Belgium“, automaticky vznikne faktura u „JS Store US“.

:guilabel:`Vytvořit prodejní objednávku“: když je vytvářena prodejní objednávka pro
Objednávka na „JS Store Belgium“ je potvrzena na „JS Store US“, automaticky se vytvoří objednávka
vytvořené (a potvrzené, pokud je zvolena možnost „Vytvořit a ověřit“).

.. viz též:
   - :doc:`Pravidla pro více společností <../../../developer/howtos/company>`
   - :doc:`../../finance/účetnictví/začínáme/měna“

…_univerzální/více společností/použitelné příklady:

Příklady použití
=========

..._generální/víceoborové/příklady použití pro nadnárodní společnosti:

Multinárodní společnosti
-----------------------

Společnost, která provozuje řetězec obchodů ve Spojených státech a Kanadě, musí spravovat transakce
USD a CAD.

Odoo má funkci pro více společností, takže můžete používat stejnou platformu v každé zemi.
Velmi prospěšné.

Toto řešení umožňuje transakce mezi společnostmi, což je nezbytné pro řízení přeshraničních obchodů.
Inventarizační převody. Zjednodušuje také prodejní proces tím, že umožňuje zákazníkům transakce
jejich místní měna.

..._generální/více společností/případ použití - oddělené procesy:

Samostatné procesy
------------------

Malá nábytkářská firma uvádí na trh novou produktovou řadu, která vyžaduje samostatné nákupní procesy.
inventáře a výrobních procesů. Nové produkty se od stávajících výrazně liší.
katalog. Chce tento proces efektivně řídit a zvažuje použití funkce pro více společností
spravovat novou linku jako samostatnou obchodní jednotku.

Vytvoření zcela nové společnosti však může přidat do databáze zbytečnou složitost.
Společnost může využít stávající funkce, jako je například analytické účetnictví.
a více skladů pro správu nových
produktová řada bez zbytečného komplikování celkových provozů.
