==========================
Projektové milníky faktury
==========================

Fakturace podle milníků projektu se hodí pro drahé nebo rozsáhlé projekty.
Milníků v projektu představuje jasný postup práce, který nevyhnutelně vyústí ve
dokončení projektu a/nebo smlouvy.

Tento způsob fakturace zajišťuje, že společnost dostává konzistentní proud peněz po celou dobu své existence.
projektu. Zákazníci mohou sledovat každý fází vývoje projektu, jakmile
Kromě toho se platí větší faktura ve více splátkách namísto jedné.

Vytvořte produkty, které budou mít zásadní význam
=========================

V Odoo je každý milník projektu považován za samostatný produkt.

Aby bylo možné vytvářet a/nebo konfigurovat produkty takto, je třeba nejprve přejít na:
Poté klikněte na produkt nebo vytvořte nový kliknutím
:guilabel:`Nový“.

Možnost fakturace podle etap je dostupná pouze pro určité produkty.

V produktovém formuláři pod záložkou „Obecné informace“ je položka „Produkt“.
pole musí být nastaveno na některou z následujících možností: :guilabel:`Služba`, :guilabel:`Vstupenka na akci`.
„Stánek akce“ nebo „Kurz“.

.. obrázek:milestone/produktovy-typ-pole.png
:align:center
:alt:Výběr možností v poli fakturační politiky ve formuláři produktu.

S jakýmkoliv z těchto možností „Druh produktu“ vyberte „Na základě milníků“.
z rozevíracého seznamu „Zásady fakturace“.

.. obrázek:milestone/fakturace-politika-pole.png
:align:center
:alt:Výběr možností v poli fakturační politiky ve formuláři produktu.

Pod tím je pole Create on Order.

Pro zajištění co nejhladšího průběhu procesu je doporučeno použít možnost
V poli „Vytvořit na objednávku“ je vybráno.

.. poznámka::
Zanechání výchozího nastavení „Nic“ nebude mít na požadovaný výsledek žádný vliv.
průběh procesu. Pokud se však projekt vytváří přímo z objednávky, musí být tento typ objednávky
konkrétní produkt. Jakmile je projekt vytvořen, pak se mohou vytvářet milníky a úkoly.
konfigurována.

Když je kliknutá volba „Vytvořit na objednávku“ v poli „Nic“, zobrazí se vyskakovací okno.
menu se zobrazí s následujícími možnostmi:

- :guilabel:`Úkoly“:Odoo vytvoří úkol spojený s tímto produktem na základě milníku ve *Projektech*.
tento konkrétní produkt je objednán.
- :guilabel:`Projekt & úkol“: Odoo vytvoří projekt a úkol související s tímto milníkem produktu.
aplikace *Projekty*, pokud je tento konkrétní produkt objednán.
- :guilabel:`Projekt“:Odoo vytvoří projekt související s tímto produktem ve složce „Projekty“.
aplikace, která se spustí při objednání konkrétního produktu.

Když je vybrána položka „Úkol“, objeví se pole „Projekt“. V tomto poli zvolte
jaký existující projekt v aplikaci Projects by měla být s touto novou úlohou propojena.

.. obrázek:milestone/task-option-project-field.png
:align:center
:alt:Pole Projekty se zobrazí, pokud je vybráno pole Vytvořit na objednávce.

Když je vybrán projekt nebo úkol, objeví se dvě nová pole:
„Šablona projektu“ a „Šablona pracovního prostoru“.

.. obrázek:milestone/project-task-option-project-workspace-fields.png
:align:center
:alt:Pole projektu a pracovního prostředí, které se objevují na produktu milníku.

V poli „Šablona projektu“ je k dispozici možnost použití šablony pro projekt, který bude vytvořen.
vytvořené při objednání konkrétního produktu.

Klíčové slovo „Vzor pracovního prostoru“ poskytuje možnosti vzoru pro použití ve vašem pracovním prostoru.
(ne aplikace „Projekty“, ale aplikace „Dokumenty“), která se vytvoří automaticky pro projekt při
konkrétní produkt je objednán.

..tip:
Pro organizační účely klikněte na záložku „Prodej“ v produktovém formuláři a zadejte
vlastní popisný prvek „Mílový kámen“ v poli :guilabel:`Popis prodeje“.
informace se objevuje v sloupci „Popis“ na záložce „Dodací lístky“.
objednávka na prodej.

Nebo přímo upravit nebo změnit pole „Popis“ na záložce „Dodací řádky“.
objednávka na prodej.

Toto není požadavkem.

Milníky faktur
==================

.. poznámka::
Následující proud obsahuje trojici produktů, které mají nastavené služby:
jejich „Typ produktu“, a „Úkol“ nastavený na jejich „Vytvořit na objednávku“.
pole.

.... obrázek: milestone/nastavení-procesu.png
:align: center
:alt:Produkt s službou „Typ produktu“ a „Úkol“ v poli Vytvořit na objednávku na formuláři.

Tyto úkoly jsou pak připojeny k již existujícímu projektu, v tomto případě je tímto projektem
nazvaný „Projekty rebrandingu“.

Zaúčtovat faktury za úkoly, vytvořte objednávku s produktem (produkty) pro úkol. Chcete-li tak učinit, přejděte na
Vyberte v nabídce „Prodejní aplikace“ -> „Nový“. To odhalí prázdnou objednávku.

Z této citační formy přidejte :guilabel:`Zákazník“. Pak klikněte na :guilabel:`Přidat produkt“ v
:guilabel:`Řádky objednávek“ a poté přidejte produkt(y) milníku do :guilabel:`Řádků objednávky“.

Jakmile budou přidány odpovídající produkty cíle, klikněte na tlačítko „Potvrdit“
objednávka, která převádí citát na objednávku prodeje.

Když je objednávka potvrzena, nové chytré tlačítko se zobrazí na vrcholu prodejní objednávky podle
byl vybrán v poli „Vytvořit na objednávku“ na kartě produktu.

Z objednávky prodeje klikněte na tlačítko „Míle“ z rolovací nabídky. To odhalí prázdný
Stránku „Významné události“. Klikněte na „Nový“ pro přidání významných událostí.

.. obrázek: milník/přidání milníku.png
:align:center
:alt:Přidávání mezníků do objednávky s produkty, které obsahují mezníky.

Do pole „Název“ zadejte název milníku. Poté aplikujte na příslušný „Prodeje“.
Položka objednávky“. Nakonec můžete přidat položku „Termín“ k milníku, pokud chcete.

Tento proces opakujte pro všechny položky objednávky s milníkovými prodeji.

Pak se vraťte do objednávky a přejděte na
„Úkoly“ chytrý tlačítko. To odhalí „Úkoly“ stránku s úkolem pro každou prodanou položku.
položku objednávky s tímto parametrem označeným v poli Create on Order.

... obrázek:milestone/taskspage.png
:align:center
:alt:Stránka s příkladovými úkoly, přístupná pomocí chytrého tlačítka z objednávky s produktem s milníkovým datem.

Chcete-li ručně přiřadit konfigurovaný milník k úkolu, klikněte na požadovaný úkol, který odhalí úkol.
formuláři úkolu vyberte vhodný milník, ke kterému má být tento úkol připojen,
:guilabel:„Mílový kámen“.

.. obrázek: milník/milníková pole na úkolovém formuláři.png
:align:center
:alt:Pole s mezníkem na formuláři úkolu při práci se zbožím v Odoo Sales.

Tento proces opakujte pro všechny úkoly, které jsou součástí milníku.

Správně nakonfigurované úkoly umožňují zaměstnancům zadávat svůj pokrok v průběhu práce na úkolu.
přidat k tomu i poznámky související s úkolem.

Pak, když je tato úloha hotová, dosáhli jste cíle.
Čas vystavit fakturu za tento milník.

Abychom mohli vystavit fakturu za milník, musíme se nejprve vrátit k objednávce - buď přes chlébovou stopu nebo
Navigace na: „Prodejní aplikace –> Objednávky –> Objednávky“ a výběr vhodného prodeje.
pořádku.

Na prodejním formuláři klikněte na tlačítko „Milníky“ a zaškrtněte políčko
sloupec „Dosaženo“ pro konkrétní úkol.

.. obrázek: milník/dosáhnutý-milník.png
:align:center
:alt:Jak vypadá označení dosažení milníku pomocí chytré tlačítko „Milník“.

Poté se vraťte k objednávce prodeje - buď stisknutím tlačítka „Zobrazit objednávku prodeje“ nebo
:milestones: stránku nebo přes chlébovou stopu.

Vraťme se zpět na prodejní objednávku. V položce s dosaženým milníkem je
V poli „Dodáno“ je vyplněno. To proto, že se splnil cíl a tedy
dodána.

.. obrázek: milník/dodaný-milník-produkt-prodejní-objednávka.png
:align:center
:alt:Důležitý produkt, který byl dosažen, je označen jako dodaný v objednávce na prodej v Odoo.

Klikněte na „Vytvořit fakturu“ v pravém horním rohu. To zobrazí „Vytvořit
okně s fakturou.

.. obrázek:milestone/create-invoices-pop-up.png
:align:center
:alt:Okno s výzvou k vytvoření faktury, které se objeví po stisknutí tlačítka Vytvořit fakturu.

V okně „Vytvořit fakturu“ zanechte zaškrtnutou možnost „Vytvořit fakturu“.
Výchozí výběr „Běžná faktura“ a klikněte na „Vytvořit návrh faktury“.
tlačítko.

Po kliknutí na „Vytvořit návrh faktury“ zobrazí Odoo „Návrh faktury zákazníka“.
*jenom* zobrazuje dosažené milníky v záložce „Splatná částka“.

.. obrázek: milník/faktura-návrh-milníku.png
:align:center
:alt:Návrh faktury zákazníka, který ukazuje pouze dosažený produkt.

Na stránce faktury klikněte na tlačítko „Potvrdit“ a poté, co se zobrazí
Zákazník za tento milník zaplatil, klikněte na „Registrace platby“.

Když je kliknut na tlačítko „Registrace platby“, objeví se okno „Registrace platby“.

.. obrázek: milník/registrace-platby-pop-up.png
:align:center
:alt:Okno s náhledem na platbu, které se objeví po kliknutí na tlačítko Registrace platby.

V tomto okně potvrďte správnost automaticky vyplněných polí a pak klikněte
:guilabel:`Vytvořit platbu“.

Po kliknutí se okno zavře a Odoo se vrátí na fakturu pro daný milník.
, která nyní má zelenou šipku „Ve splatnosti“ v pravém horním rohu. Tato šipka značí
Faktura byla uhrazena.

.. obrázek:milník/výpis-platby-faktury.png
:align:center
:alt:Faktura s produktem, který byl zaplacen pomocí banneru In Payment.

Pak se vraťte na prodejní objednávku přes chlébovou stopu. Na prodejní objednávce
kartě „Zadané objednávky“, dosažená výše úhrady je nyní označena
V poli „Faktura“ je vyplněno.

.. obrázek: milník/fakturovaný sloupec vyplněný milníkem.png
:align:center
:alt:V poli Fakturováno se vyplní částka za hotovou fakturu.

Na horní části faktury je také nová tlačítko „Faktura“, na které stačí kliknout
zobrazuje všechny faktury, které jsou spojeny s tímto prodejním příkazem.

.. obrázek:milestone/faktury-inteligentni-tlacitko.png
:align:center
:alt:Tlačítko chytré faktury, které se objeví na vrcholu objednávky s milníky.

Zopakujte výše uvedený proces pro každé milníky, které jsou v průběhu prací a následně dokončeny.

Tento proces pokračuje až do úplného dokončení projektu, kdy jsou vystaveny faktury za každý z milníků.
A celý nákup byl uhrazen v plné výši.

.. viz též:
   - :doc:`time_materials“
   - :doc:`proforma“
   - :doc:`fakturační politika“
