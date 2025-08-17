Zobrazit obsah
:ukrýt stránku obsahu:

==================
Projektové řízení
==================

Projekt Odoo používá systém řízení projektů Kanban. To znamená, že všechny projekty jsou rozděleny
do úkolů, které jsou na tabuli rozřazeny podle fáze výroby.

.. varování:Víte, že...

Slovo „kanban“ pochází z japonštiny a označuje metodu řízení „vizuální tabule“.

..._projektové řízení/konfigurace:

Konfigurace
=============

Otevřete aplikaci **Projekt** a klikněte na tlačítko „Vytvořit“ pro zahájení nového projektu. Zadejte
Vyberte název projektu a klikněte na tlačítko „Vytvořit projekt“.

Můžete upravit své stávající projekty z přehledu kliknutím na rozbalovací nabídku
tlačítko (:guilabel:`⋮`) na kartě vašeho projektu.

.. obrázek: projekt_management/projekt-nastaveni.png
:align:center
:alt:Projektní karta

To umožňuje nový menu rozdělené do čtyř částí:

- :guilabel:`Přehled“: zobrazte si přehled projektu a jeho součástí, například :guilabel:`Úkoly“.
:guilabel:`Zásadní milníky“ a „Aktualizace projektu“. V závislosti na tom, které aplikace máte
aktivovány, což umožňuje další možnosti, například: guilabel:"Dokumenty". Všechny nahrané soubory mohou být
je naleznete pod tímto menu i v aplikaci **Dokumenty** pod položkou „Projekty“.
- :guilabel:`Zprávy“: analyzujte postup a ziskovost projektu pomocí grafů
statistiky
- **Barva**: vytvořte linku barvy na levé straně karty, aby váš projekt byl
rozpoznatelná.
- :guilabel:`Nastavení“: můžete změnit následující:

  - Název projektu:
  - Název úkolů nalezených pod tímto projektem.
  - „Zákazník“, pro kterého je projekt určen.
  - :guilabel:`Štítky`, které se používají k filtrování.
  - Společnost odpovědná za projekt:guilabel:`Company`;
  - zaměstnanec označený jako „Projektní manažer“;
  - datum plánovaného ukončení projektu;
  - celkový počet hodin přidělených tomuto projektu.

Dále můžete projekt označit jako :guilabel:`Favorite`, což vám umožní jej najít pomocí
Filtr „Moje oblíbené“ v kartovém zobrazení.

.. obrázek: projekt_management/projekt_nastaveni_otevrene.png
:align:center
:alt: Nastavení projektu

.. viz též:
„Odoo Tutoriály: Přizpůsobení projektů


Další nastavení je k dispozici pod záložkou „Nastavení“. Většina z nich je dostupná pouze
podle aktivovaných aplikací.

Viditelnost a spolupráce
----------------------------

Odoo vám umožňuje nastavit viditelnost pro každý projekt a tím pádem můžete svůj projekt
dostupné pro všechny uživatele ve vaší organizaci nebo omezit přístup na určité vnitřní nebo externí uživatele.

Pro toto nastavení přejděte na záložku „Nastavení“ projektu a vyberte požadovanou „Viditelnost“.
možnost:

- „Zváni interní uživatelé (soukromí)“: Pouze uživatelé, kteří sledují projekt a uživatelé s
Ředitel projektu: přístupové právo „access right“ lze nastavit v aplikaci „Users“ – „Access rights“.
přistupovat k projektu a úkolům.
- :guilabel:`Všichni uživatelé v rámci organizace“: Všichni uživatelé ve společnosti mohou přistupovat k projektu a všem jeho úkolům.
- :guilabel:`Zváni jsou pouze portáloví uživatelé a všichni interní uživatelé (veřejně)“: Všichni interní uživatelé mohou přistupovat
projekt a všechny jeho úkoly. Při sledování projektu:
Přístup k úkolům mají pouze uživatelé, kteří sledují konkrétní úkoly.
Toto nastavení je výchozím.

Zveřejnění pro externí uživatele
-----------------------

Pro pozvánku externích uživatelů zkontrolujte, že:guilabel:'Invited portal users and all internal users
Vyberte možnost „Zveřejnit projekt“ v horní části nastavení projektu.
Následující možnosti jsou k dispozici:

- Zkopírujte a sdílejte odkaz „Veřejný odkaz“ zobrazený na horním okraji okna. Kdokoli s
Tento odkaz umožňuje přístup k projektu v režimu čtení.
- Klikněte na „Přidat řádek“, vyberte „Spolupracovníka“ a zvolte
:guilabel:`Způsob přístupu“ a zaškrtněte políčko pro odeslání pozvánky na jejich e-mailovou adresu.

Existují tři typy přístupu pro spolupracovníky:

  - :guilabel:`Číst“: Spolupracovníci mohou úkoly zobrazit, ale nemohou je upravovat.
  - :guilabel:`Úprava s omezeným přístupem“: Spolupracovníci mohou prohlížet a upravovat úkoly, které sledují.
  - :guilabel:`Edit“: Spolupracovníci mohou zobrazit a upravovat všechny úkoly.

Pro odvolání přístupu pozvaného spolupracovníka klikněte na „Sdílení projektu“ v horní části
Nastavení projektu a klikněte na ikonku „Odpadkový koš“ .

.. poznámka::
Uživatelé z interní sítě, kteří nemají přístup do projektu, mohou stále pracovat na úkolu, pokud byl odkaz sdílen.
s nimi. Pro projekty nastavené jako „Zváni interní uživatelé (soukromý)“ musí být také
být příznivcem úkolu.

Plánování aktivit
=====================

Můžete plánovat aktivity (např. „Hovor“, „Schůzka“ atd.) na projektu
kliknutím na ikonu hodin v projektu. To způsobí, že se zobrazí seznam již naplánovaných aktivit
a umožňuje plánovat nové aktivity kliknutím na tlačítko „Schedule an activity“. Na vyskakovacím okně
okno, vyberte „Typ aktivity“, zadejte „Popis“ pro tuto aktivitu,
„Datum splatnosti“ a přiřaďte jej zaměstnanci. Podle „Typu aktivity“ můžete
mohou mít k dispozici další možnosti.

.. poznámka::
Pokud je aktivita již naplánovaná, ikona se může změnit na telefon, skupinu lidí.
nebo jiná.

.._projekt/projektové řízení/hlavní lišta:

Horní pás
=======

V řízení projektů je často nutné projít různé záznamy a dokumenty související s daným projektem.
nutné. V horní liště projektu Odoo jsou rychle dostupné tyto základní zdroje.
Upravit horní lištu každého projektu tak, aby odpovídala jeho specifickým potřebám.

Chcete-li nastavit horní lištu pro projekt, přejděte do aplikace „Projekt“, klikněte na kartu projektu.
Klikněte na tlačítko v horní liště s ikonou „fa-sliders“ a textem „(sliders)“. V liště se objeví
nad vyhledávacím polem klikněte na tlačítko s ikonou „fa-sliders“ a textem „(sliders)“.
chcete zobrazit, jako jsou například časové listiny, objednávky, faktury, dokumenty nebo přehledy.

Poté můžete kliknout na tlačítka, abyste se dostali ke souvisejícím záznamům bez opuštění aplikace Project.
Vraťte se do pohledu na úkoly v kanbanu projektu a klikněte na tlačítko „Úkoly“ v horní liště.

.. obrázek: projekt_management/hlavni_panel.png
:alt: Vybrané nabídky v horní liště

Klasické tlačítka s horním okrajem
----------------------

Můžete také vytvořit své vlastní tlačítka pro přístup k více specifickým pohledům:

#Klikněte na existující tlačítko v horní liště, abyste se dostali do pohledu.
#Upravte pohled pomocí klíčových slov, filtrů a možností seskupení v poli pro vyhledávání.
#Klikněte na tlačítko „Slider“ v horní liště a vyberte
:guilabel:`Uložit pohled“.
#Upravte název výchozího tlačítka podle potřeby a zapněte Shared, pokud chcete sdílet
tlačítko s ostatními uživateli.

.. toctree::


projektové řízení/přehled projektu
Projektové řízení / Ziskovost projektu
