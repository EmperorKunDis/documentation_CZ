=====================
Politika kontroly účtů
=====================

... nakupovat/spravovat obchody/kontrolovat faktury:

.. |PO| nahradit za: abbr: PO (objednávka)
.. |POs| nahradit za: zkratka: `POs (Purchase Orders)`

V aplikaci nákupu v Odoo se politika „kontrola faktur“ řídí množstvím zboží dodaného dodavateli.
každou objednávku, ať už jde o objednané nebo dodané množství.

Zvolená politika v nastavení aplikace Purchase slouží jako výchozí hodnota a je použita pro jakýkoli
vznikla nová služba.

Konfigurace
=============

Pro konfiguraci politiky „Kontrola faktur“ přejděte na: `Přidání aplikace - Konfigurace
→Nastavení“ a posuňte se dolů do části „Fakturace“. V části „Kontrola faktury“
Vyberte buď „Počet objednaných položek“ nebo „Počet přijatých položek“. Pak klikněte
:guilabel:`Uložit“.

.. obrázek: kontrola_faktur/kontrola-faktur-vybrany-politika.png
:align:center
:alt:Vybranou politiku kontroly faktur v nastavení aplikace Nákup.

- :guilabel:„Počet objednaných položek“: vytvoří fakturu dodavateli, jakmile je potvrzena objednávka.
a množství v PO slouží k generování návrhu zákona.
- :guilabel:`Přijaté množství“: faktura vystavena pouze po převzetí části celkového objednaného
obdržené produkty a množství obdržených položek používá k vytvoření návrhu faktury. Chybová zpráva
Vznikne, pokud se zadá vystavení faktury bez přijetí.

.. obrázek: kontrola_faktur/kontrola-faktur-chyba-vzkazu-plocha.png
:synchronizace: střed
:alt:Chyba při kontrole návrhu zákona o regulaci kryptoměn.

.. poznámka::
Pokud by měl být použit jiný režim kontroly než ten, který byl zvolen v aplikaci Přijetí
nastavení, v případě produktu lze změnit politiku „Kontrola faktur“ z jeho produktového
formulář.

Pro přístup k tomuto nastavení se musíte dostat na: „Koupit aplikaci“ -> „Produkty“ -> „Produkty“.
produktu. Vyberte záložku „Koupit“ a pod záložkou „Dodavatel“ klikněte na tlačítko „Zobrazit“.
V sekci „Faktury“ upravte výběr v poli „Zásady řízení“.

Třístranné shody
==============

Funkce „Třístranné shody“ zajišťuje, že dodavatelé budou platit pouze jednou za některé (nebo všechny) produkty.
Dotace z programu PO byly přijaty.

Pro aktivaci třístranného shody, přejděte na: „Nákup aplikace“ -> „Konfigurace“
Nastavení“ a posuňte se dolů do části „Fakturace“. Pak zaškrtněte políčko u
Zapněte funkci tlačítkem „Třístranné shody“ a klikněte na „Uložit“.

.. obrázek: kontrola-faktur/kontrola-faktur-trojúhelníková-shoda.png
:align:center
:alt:Zapnul funkci třístranného shodování v nastavení aplikace Nákup.

.. důležité:
:guilabel:`Třístranné shody` funkce funguje pouze s politikou :guilabel:`Kontrola faktur“
nastaveno na: guilabel:„Přijaté množství“.

Zaplaťte faktury dodavatelů s třístranným shodováním
------------------------------------

Při zapnuté funkci třístranného shody se v fakturách dodavatelů zobrazí pole „Měl by být uhrazen“ pod
:guilabel:`Další informace“ v záložce „Výrobce“. Když je nová faktura od dodavatele vytvořena, pole se nastaví na hodnotu :guilabel:`Ano“.
výrobek, který je součástí PO, musí být vyroben alespoň částečně.
přijatý.

Pro vytvoření faktury dodavatele z objednávky přejděte na: „Nákupní aplikace“ -> „Objednávky“.
Nákupní objednávky“. V sekci „Nákupní objednávky“ vyberte požadovanou nákupní objednávku z seznamu.
Klikněte na „Vytvořit fakturu“. To otevře nový návrh „Faktura pro dodavatele“ v
Stupeň „Návrh“. Klikněte na záložku „Další informace“ a najděte „Měl by být
Placená reklama.

.. důležité:
Vybraný |PO| z seznamu **nemusí být ještě fakturován**, nebo jinak dojde k chybě.
Okno se objeví, pokud je nastaveno přijaté množství pro |POs| s politikou „Přijatá hodnota“ a
:guilabel:`Úplně fakturováno“ :guilabel:`Stav fakturace“.

.. obrázek:: kontrolni-faktury/kontrolni-faktura-neplatna-operace.png
:synchronizace: střed
:alt:Pop-up okno pro neúčinnou operaci při fakturaci objednávky.

Klikněte na rozbalovací nabídku vedle položky :guilabel:`Měl být zaplacen´, abyste viděli dostupné možnosti:
„Ano“, „Ne“ a „Výjimka“.

.. obrázek: kontrolni-faktury/kontrolni-faktury-se-maji-platit.png
:align:center
:alt:V poli Platba by měl být stav faktury na dodání.

.. poznámka::
Pokud celkové množství produktů z |PO| nebylo přijato, Odoo pouze obsahuje
produkty, které *byly* přijaty v návrhu faktury dodavatele.

Návrh dodavatelské faktury lze upravit tak, aby se zvýšil počet položek a změnil se cenový výpočet.
v návrhu zákona a přidat další produkty do návrhu zákona.

Pokud se změní informace o návrhu zákona, je nastavena hodnota pole
:guilabel:„Výjimka“. To znamená, že Odoo zaznamená rozdíl, ale nezablokuje změny.
nebo zobrazit chybovou hlášku, protože může existovat platný důvod k provedení změn v návrhu.
faktura.

Pro zpracování faktury dodavatele vyberte datum v poli „Datum faktury“ a klikněte
Dále je potřeba kliknout na „Potvrdit“ a následně na „Registrace platby“.

Otevře se okno „Registrace plateb“. Zde je možné zadat účetní informace
předvyplněné na základě účetních nastavení databáze. Klikněte na tlačítko :guilabel:`Vytvořit platbu`.
zpracovat fakturu dodavatele.

Jakmile je platba uhrazena za fakturu dodavatele, a faktura zobrazí zelený štítek „Uhrazeno“,
banneru, pole „Mělo by být zaplaceno“ má stav „Ne“.

..tip:
Stav „Mělo být zaplaceno“ na fakturách je automaticky nastaven systémem Odoo.
může být ručně změněn kliknutím na položku rozbalovací nabídky v sekci „Další informace“
tabulka

Zobrazit stav fakturace objednávky
======================================

Jakmile je potvrzena platba, její stav lze zobrazit pod záložkou „Stav účtu“ v záložce „Ostatní“.
V záložce „Informace“ na formuláři PO.

Pro zobrazení stavu fakturace pro |PO| přejděte na:
Pokyny k nákupu --> Pokyny k nákupu, a vyberte PO pro zobrazení.

Klikněte na záložku „Další informace“ a najděte pole „Stav fakturace“.

.. obrázek: kontrola_faktur/kontrola-faktur-stav-faktury.png
:align:center
:alt:Pole pro stav faktury na objednávce.

Tabulka níže uvádí různé hodnoty pole :guilabel:`Stav fakturace`, které mohou číst.
Podle použitého nastavení politiky *Kontrola účtu*.

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * -Stav fakturace
     - Na přijaté množství
     - Na objednané množství
   * – Není nic pro Billa
     - PO potvrzeno, žádné produkty neobdrženo
     - *Není aplikovatelné*
   * -Čekání na účty
     - Všechny/některé produkty přijaty, faktura nebyla vytvořena
     - PO potvrdil
   * – Plně naúčtované
     - Všechny/některé produkty obdrženy; návrh zákona vytvořen
     - Návrh zákona vznikl

.. viz též:
:doc:`spravovat“
