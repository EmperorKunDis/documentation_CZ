=========
Dokumenty
=========

Služba **Odoo Dokumenty** umožňuje ukládat, prohlížet a spravovat soubory v rámci Odoo.

Složky a dokumenty jsou uspořádány do sekcí, které lze zobrazit vlevo od stromu.
Následující sekce jsou k dispozici:

- :guilabel:`Všechny“ zobrazí všechny složky a soubory, ke kterým má uživatel přístup.
- :ikonka: „budova“ :guilabel:„Společnost“: obsahuje složky a soubory sdílené v rámci společnosti.
Přístup je určen podle definovaných práv k přístupu k souborům (viz dokument „Přístupová práva“).
a souboru.
- :icon:`fa-hdd-o` :guilabel:`Můj disk“: osobní pracovní prostor uživatele pro organizování a přístup k
soubory a složky, které vlastní nebo nahráli.
- :icon:`fa-users` :guilabel:`Sdíleno se mnou“: zahrnuje soubory, které byly sdíleny s uživatelem
ale nejsou součástí žádné složky, kterou mají přístup.
- :icon:`fa-clock-o` :guilabel:`Recent“: zobrazuje nedávno upravené soubory, ke kterým má uživatel přístup
k prohlížení nebo editaci.
- :icon:`fa-trash` :guilabel:`Odpad“: ukládá :ref:`smazané soubory a složky <dokumenty/odložené_mazání>“.

Klikněte na část stromu, abyste viděli jeho obsah. Vyberte složku pro otevření nebo správu.
<soubory a složky>“, a přistupovat k jeho souborům.

Klikněte na soubor pro jeho otevření a vyberte dostupné akce (<documents/documents>). Chcete-li soubor zavřít
Stiskněte klávesu **Esc** nebo klikněte na ikonku :icon:`fa-remove` (:guilabel:`Close`). Můžete také přetáhnout a pustit
soubor nebo složku a přesunout ji do jiné složky nebo sekce.

..tip:
   - Použijte pole pro vyhledávání „:ref:“ k rychlému nalezení konkrétních položek.
   - Chatování sleduje změny složek a souborů a umožňuje
komunikace se vnitřními uživateli a externími kontakty.
tlačítko „Info a štítky“ v pravém horním rohu vedle zobrazení, abyste se k němu dostali.

.. viz též:
:doc:`Dokumentace k podpisu <sign>`

Konfigurace
=============

..._soubory/odložení smazání:

Zpoždění smazání
--------------

Výchozí nastavení je takové, že položky přesunuté do koše zůstávají tam po dobu 30 dní a poté jsou natrvalo smazány.
upravit tento zpoždění, přejděte na: „Dokumenty“ → „Konfigurace“ → „Nastavení“ a upravte
:guilabel:`Zpoždění smazání (dny)` pole.

..._souborů/souborová centralizace:

Centralizace souborů
-------------------

Povolení centrální správy souborů pro konkrétní aplikaci automaticky organizuje všechny spojené soubory do
Dokumenty - Konfigurace - Nastavení.
Příkladem je např. možnost :guilabel:`Personal“ umožňující automatické zobrazení dokumentů v oblasti personalistiky.
:guilabel:`Personalistika“ složce, zatímco dokumenty související s mzdami jsou automaticky dostupné v
Podsložku „Mzdy“. Vyberte požadovanou složku z rozevírací nabídky a potvrďte výběr
:ref:`Štítky <dokumenty/štítky>“ k přidání do souvisejících souborů.

..tip:
Při centralizaci účetních souborů klikněte na tlačítko :guilabel:`Journals`, abyste mohli konfigurovat specifické
podsložky pro jednotlivé časopisy.

.. poznámka::
   - Změna složky nebo štítku neovlivní existující soubory; změny se budou vztahovat pouze na
nově vzniklé.
   - Pokud je pro aplikaci povolena centrální správa souborů, odstranění záznamu v této aplikaci přesune její
přílohy v aplikaci Dokumenty.

... dokumenty a složky:

Složky
=======

Můžete organizovat soubory do složek dostupných v ikoně „budova“ nebo
:icon:`fa-hdd-o` :guilabel:`Moje jednotka“ sekce.

Pro vytvoření složky vyberte požadovanou sekci ve stromu, klikněte na tlačítko „New“ a zvolte
:guilabel:`Složka“. V okně zadejte název složky a klikněte na tlačítko :guilabel:`Uložit“.
Pro vytvoření podsložky vyberte nejprve složku nadřazenou, pak postupujte stejným způsobem.

.. poznámka::
Některé složky a podsložky jsou vytvářeny automaticky na základě :ref:`centralizace souborů
nastavení <dokumenty/souborová centralizace>.

Pro správu složky nebo podsložky vyberte ji a klikněte na ikonku „Nástroje“
ikonu nad stromem. V nabídce jsou následující možnosti:

- :icon:`fa-download` :guilabel:`Stáhnout“: Stáhněte složku včetně jejích souborů ve formátu .zip
a podsložky.
- :icon:`fa-pencil-square-o` :guilabel:`Přejmenovat`: Upravit název složky.
- :icon:`fa-share-alt` :guilabel:`Sdílet“: :ref:`Sdílejte složku nebo spravujte přístupová práva
<dokumenty/práva přístupu>.
- :icon:`fa-external-link-square` :guilabel:`Přidat zkratku“: Tato možnost je dostupná pouze pro
podsložky a umožňuje vytvořit zkratku na podsložku.

  - Pokud máte oprávnění pro editaci, je zkratka vytvořena ve stejné složce.
  - Pokud nemáte oprávnění k úpravám, zkratka se objeví v ikoně „fa-hdd-o“.
:guilabel:`Moje úložiště“ sekce.

Poté ji můžete přetáhnout a vložit do požadovaného adresáře.
- :icon:`fa-star-o` :guilabel:`Přidat hvězdičku“: Označte složku jako oblíbenou pro rychlejší přístup.
V nastavení je uživatelsky specifické a neovlivňuje pracovní prostředí ostatních uživatelů. Poté můžete používat
:ref:`Filtr s hvězdičkou <vyhledávání/oblíbené složky>“ pro rychlé přepnutí na vaše oblíbené složky.
- :icon:`fa-info-circle` :guilabel:`Informace a štítky“: Zobrazit podrobnosti o složce
<detailní panel> a chatu.
- :icon:`fa-trash` :guilabel:`Přesunout do koše“: Přesuňte složku a její obsah do :ref:`koše
<soubory/odložení-mazání>.
- :icon:`fa-cog` :guilabel:`Akce na výběr“: Definujte dostupné akce serveru (jako
tlačítka) pro soubory ve složce. Klikněte na akci, která se má přidat nebo odstranit.
:guilabel:`Přidat vlastní akci“ do :ref:`vytvořit novou <odkaz/akce/server>“.
- :icon:`fa-cog` :guilabel:`Automace“: Vytvořit :doc:`pravidla automatizace


.. důležité:
Nastavení vlastních akcí a pravidel automatizace může ovlivnit váš „plán cen“
<https://www.odoo.com/cena/>

... _dokumenty/dokumenty:

Soubory
=====

Pro nahrání souboru vyberte požadovanou složku v stromové struktuře, klikněte na tlačítko „Nový“ a zvolte
:label:Nahrát soubor.

..tip:
   - Ve službě Odoo Online nesmí každý nahraný soubor překročit velikost 64 MB.
   - Můžete také přetáhnout soubor z počítače do požadované složky v Dokumentech.
aplikace.

URL odkazy
---------

Pro přidání odkazu na URL (např. video) a jeho zobrazení v adresáři klikněte na tlačítko „Nový“
a vyberte „Odkaz“. Zadejte „URL“, přidejte „Jméno“ a vyberte
vhodné: `Složka`.

..._souborů/tabulka:

Tabulkové procesory
------------

Vytvoření tabulky provedete kliknutím na „Nový“ a výběrem „Tabulka“.

.. viz též:
:doc:`Dokumentace tabulkového procesoru <spreadsheet>`

Správa souborů
--------------

V horním panelu se při otevření souboru zobrazí několik tlačítek:

- ikonu „fa-cog“ a nabídku „Akce“, která zahrnuje možnosti popsané níže
- :guilabel:`Sdílet“: :ref:`sdílet soubor nebo spravovat přístupová práva <dokumenty/přístupová práva>`
- :download:
- kromě tlačítek definovaných pro složku <documents/folders>

Následující možnosti jsou k dispozici v nabídce „Akce“ (ikona „Ozubené kolo“)

- :icon:`fa-files-o` :guilabel:`Duplikát“: Vytvořit kopii souboru.
- :icon:`fa-trash` :guilabel:`Přesunout do koše“: Přesuňte soubor do :ref:`koše
<soubory/odložení-mazání>.
- :icon:`fa-pencil-square-o` :guilabel:`Přejmenovat“
- :icon:`fa-info-circle` :guilabel:`Informace a štítky“: Zobrazte podrobnosti o souboru :ref:`v detailu
<detailní panel> a chatu.
- :icon:`fa-external-link-square` :guilabel:`Vytvořit zkratku“: Zkratka je odkaz na soubor
umožňuje přístup z více složek bez opakování souboru.

  - Pokud máte oprávnění pro editaci, je zkratka vytvořena ve stejné složce.
  - Pokud nemáte oprávnění k úpravám, zkratka se objeví v ikoně „fa-hdd-o“.
:guilabel:`Moje úložiště“ sekce.

Poté ji můžete přetáhnout a vložit do požadovaného adresáře.
- :ikonka: `fa-history` :guilabel: „Správa verzí“: Zobrazení všech verzí souboru v pořadí nahrávání.
stáhnout konkrétní verzi nebo nahradit ji novou verzí.
- :icon:`fa-lock` :guilabel:`Zamknout“: Zabezpečte soubor proti jakýmkoliv změnám.
- :icon:`fa-link` :guilabel:`Kopírovat odkaz na sdílení“: Kopíruje adresu URL souboru pro sdílení. Přístup je kontrolován
založené na přístupových právech souboru podle :ref:`přístupových práv dokumentů <dokumenty/pristupove-prava>`.
- :icon:`fa-scissors` :guilabel:`Rozdělit PDF soubor“ :ref:`Rozdělení PDF souboru <soubory/pdf>“.

..tip:
Můžete používat e-mailové aliasy specifické pro složku, které vám umožní automaticky ukládat
soubory zaslané na alias do příslušné složky.

... dokumenty/pdf:

Rozdělování a slučování PDF souborů
--------------------------

Pro rozdělení PDF na jednotlivé nebo skupiny stránek otevřete PDF a klikněte na ikonu „nůžky“
V pravém horním rohu náhledu dokumentu klikněte na
Ikona „Nůžky“ (ikona „Nůžky“) mezi stránkami k odstranění rozdělení, pokud je potřeba.
Klikněte na tlačítko „Rozdělit“ a potvrďte.

.. obrázek: dokumenty/split-pdf.png
:alt: Rozdělit PDF

K sloučení souborů PDF postupujte takto:

#Navigujte do složky obsahující soubory, které chcete sloučit. Poté přepněte na zobrazení seznamu a
vyberte soubory, které chcete použít.
#Klikněte na tlačítko „Akce“ a vyberte ikonu „Nůžky“.
:guilabel:`Sloučit PDF soubory“.
#Pokud je potřeba, klikněte na tlačítko „Přidat soubor“ pro procházení a výběr PDF souboru z počítače.
#Klikněte na ikonu „nůžky“ (ikona „nožík“) mezi soubory.
#Klikněte na tlačítko „Rozdělit“ a spojte je.

.. poznámka::
Původní PDF soubory jsou nahrazeny sloučeným dokumentem.

..tip:
   - Stiskněte klávesy **Shift + S**, abyste přidali nebo odebrali všechny rozdělení mezi stránkami.
   - Pro odstranění konkrétní stránky vyberte stránku a klikněte na tlačítko „Smazat“.

..._dokumenty/žádost:

Požadování souborů
----------------

Požádejte uživatele o zaslání souborů jako připomínku k nahrání konkrétních souborů. K tomu postupujte takto
kroky:

#Klikněte na „Nový“ a vyberte „Žádost“.
#Zadejte název dokumentu a vyberte osobu, od které požadujete tento dokument.
:guilabel:`Požadavek na“ pole.
#Pokud je potřeba, nastavte datum splatnosti, vyberte složku, do které se má soubor uložit.
Přidejte tagy, přidejte zprávu a napište :guilabel:`Message“.
#Klikněte na tlačítko „Požadavek“.

Do vybrané složky se vytvoří místo pro chybějící soubor. Jakmile bude k dispozici,
klikněte na místo pro nahrání souboru.

..tip:
Můžete také požádat o dokument z :ref:`seznamu plánovaných aktivit <activities/all>`.

Seznam všech požadovaných souborů najdete v aplikaci Dokumenty ve zobrazení Aktivita.
sloupec „Požadovaný dokument“. Klikněte na datum požadovaného souboru, abyste zobrazili jeho podrobnosti.
Poté můžete:

- Nahrát soubor pomocí tlačítka „Upload“ (ikona „fa-upload“);
- Upravte aktivitu pomocí tlačítka „Penál“ (:guilabel:`edit`)
- Zrušte aktivitu pomocí tlačítka s ikonou „odstranit“ (zobrazovací jméno „Zrušit“)
- Odeslat připomínku e-mailem. Klikněte na tlačítko „Náhled“ pro náhled obsahu připomínky
pokud je třeba, pak: „Odeslat nyní“.

K odeslání e-mailové upomínky na všechny požadované soubory klikněte na ikonu „fa-ellipsis-v“
Ikona „:guilabel:Ellipsis“ v sloupci „Požadovaný dokument“ a vyberte
:guilabel:`Žádost o dokumenty: připomínka“.

.. obrázek: dokumenty/upomínkový email.png
:alt:Odeslat připomínku e-mailem z pohledu činnosti

..._detailní panel:

Panel s detaily
=============

Pro zobrazení informací o složce nebo souboru a štítků vyberte složku nebo soubor, pak klikněte
tlačítko s ikonou „Informace a štítky“ („Info & Tags“) v pravém horním rohu vedle
zobrazit ikony.

Panel s detaily umožňuje následující:

- Změňte složku souboru nebo název složky.
- Zobrazte velikost souboru nebo složky a počet položek v složce.
- Změňte vlastníka a kontaktního uživatele souboru nebo složky. Výchozí hodnoty jsou
Osoba, která vytváří soubor nebo složku, je nastavena jako její :guilabel:`Vlastník` a má přístup s plnými právy.
práva k ní. Chcete-li ji změnit, vyberte požadovaného uživatele z seznamu.

Přístupová práva k souboru nebo složce, např. existující dodavatel v databázi.

...... poznámka::
Pro zobrazení souboru ze svého uživatelského profilu musí být uživatel nastaven jako kontakt.
aspoň :guilabel:`Zobrazení“ :ref:`přístup <dokumenty/práva přístupu>“.

... /dokumenty/e-mailové aliasy:

E-mailové aliasy
-------------

Můžete používat e-mailový alias, který automaticky ukládá soubory zaslané na e-mailový alias do konkrétní složky.
složku. Chcete-li nastavit e-mailový alias pro složku, postupujte podle těchto kroků:

#Vyberte složku, do které se mají soubory ukládat.
#Klikněte na ikonu „fa-info-circle“ („Informace a štítky“) v pravém horním rohu vedle
zobrazit ikony.
#V podrobnostech zadejte požadovanou e-mailovou adresu a vyberte nebo vytvořte doménu.
#Pokud chcete, zadejte typ aktivity a příjemce pro vytvoření :doc:`aktivity

#Volitelně můžete vybrat štítky:ref:`<dokumenty/štítky>`, které se automaticky aplikují na soubory.
Vytvořené prostřednictvím přezdívky.

.. viz též:
:doc:`/aplikace/obecné/e-mailová komunikace/e-mailové servery vstupní“

..._dokumenty/tagy:

Štítky
----

Štítky pomáhají organizovat a kategorizovat soubory, což usnadňuje vyhledávání a filtrování.
Pro konfiguraci štítků pro soubory přejděte na: „Dokumenty -> Konfigurace -> Štítky“. Klikněte
:guilabel:`New“ vytvořit nový štítek. Zadejte „Název štítku“, vyberte „Barvu“ a
Pokud chcete, můžete k tomuto štítku přidat nástrojtip, který se zobrazí při najetí myší nad tento štítek.

K přidání štítků do souboru otevřete soubor, klikněte na ikonku :icon:`fa-info-circle` (:guilabel:`Info & Tags`)
v pravém horním rohu vedle ikon pro zobrazení, a pak v detailním panelu vyberte značku
seznam s možností výběru.

.. poznámka::
:ref:`Alias tagy <dokumenty/e-mailové aliasy>` lze také použít k automatickému přiřazení tagů.
soubory vytvořené přes alias.

..._dokumenty/práva přístupu:

Přístup a práva uživatele
=======================

.. poznámka::
Pouze majitelé práv na úpravu mohou sdílet složky a soubory a upravovat přístupová práva k nim.

Přístupová práva lze nastavit na:

- složky: vyberte složku, klikněte na ikonu „fa-cog“ („gear“) a zvolte
:guilabel:`Sdílet“.
- soubory: Otevřete soubor a klikněte na „Sdílet“ v horním menu.

V okně „Sdílet“ přidejte konkrétní uživatele nebo kontakty klepnutím na jejich jméno.
z nabídky nebo ručně zadáním e-mailové adresy, pak vyberte: guilabel: Viewer
:guilabel:`Editor“.

..tip:
Pro odstranění oprávnění nebo nastavení jeho platnosti stačí myší přejít na příslušné
kontakt a klikněte na ikonu „odstranit“ (zobrazení ikony „odstranit“) nebo „kalendář“.
Tlačítko kalendáře ([:guilabel:`calendar`]) nebo odkaz na kalendář.

.... obrázek: dokumenty/odstranit-právo.png
:alt:Při najetí myší nad oprávnění se zobrazí tlačítka.

Zadat pro uživatele s přístupem „Všeobecný“ nebo „Kdokoli, kdo má přístup“ hodnotu „Obecný přístup“.
linku, vyberte možnost Viewer, Editor nebo None (k omezení přístupu
(celý). Pro :guilabel:`Kdokoli s odkazem“ můžete dále specifikovat, zda se jedná o složku nebo
Soubor by měl být označen jako „discoverable“ (přístupný procházením) nebo vyžadovat, aby uživatelé
:guilabel:'Musíte mít odkaz k přístupu'.

.. poznámka::
   - Veřejní uživatelé: „Musí mít odkaz, aby se dostali“ do složky nebo souboru na portálu
poprvé spojili.
   - Každá složka a soubor má v adrese URL uvedené nastavené oprávnění. Když
Pokud chcete sdílet složku, osoba, které ji sdílíte, je přesměrována na portál určený pro tento účel.
zobrazit soubory v této složce, s výjimkou těch se zakázaným přístupem.

..tip:
:doc:`Uživatelé portálu </applications/general/users/portal>` mají přístup k složkám a souborům, které vlastní.
povolení k prohlížení nebo úpravám prostřednictvím zákaznického portálu kliknutím na tlačítko „Dokumenty“.
karta.

Digitální archiv s umělou inteligencí
=========================

Soubory dostupné v složce Finance lze digitalizovat. Vyberte soubor a klikněte na tlačítko „Vytvořit
Výrobce faktur, vytvořit zákaznickou fakturu nebo vytvořit zákaznickou poznámku k účtu.
Poté klikněte na tlačítko „Odeslat pro digitalizaci“.

.. viz též:
:doc:`Digitální zpracování dokumentů na základě umělé inteligence <../finance/účetnictví/fakturace/invoice_digitization>“
