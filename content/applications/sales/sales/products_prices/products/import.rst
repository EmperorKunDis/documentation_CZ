===============
Dovoz produktů
===============

Odoo Sales poskytuje šablonu pro import produktů s kategoriemi a variantami, které lze
otevřít a upravit pomocí jakéhokoliv tabulkového softwaru (Microsoft Excel, OpenOffice, Google Sheets atd.).

Pokud se tento list bude vyplňovat správně, může být rychle nahrán do databáze Odoo.
nahráním těchto produktů jsou okamžitě přidány do katalogu produktů a jsou přístupné a upravitelné.

Šablona importu
===============

Pro import produktů s kategoriemi a variantami je potřeba použít šablonu pro import produktů.
musí být stáhnuty. Jakmile jsou staženy, lze je upravit a přizpůsobit podle vlastních potřeb a pak
nahrán zpět do databáze Odoo.

Pro stažení potřebného šablony pro import přejděte na: „Prodejní aplikace --> Zboží -->
Produkty“. Na stránce „Produkty“ klikněte na ikonu „⚙️ (převodovka)“ v pravém horním rohu
koutu. To odhalí rozbalovací nabídku.

Vyberte možnost „Přidat záznamy“.

.. obrázek: import/gear-import-records-option.png
:align:center
:alt:Možnost importu záznamů zvolitelná v ozubeném kolečku na stránce produktů v prodejním modulu Odoo.

Vybráním položky „Dodatečné záznamy“ se zobrazí samostatná stránka s odkazem ke stažení.
Klikněte na odkaz „Šablona pro produkty“. Po stažení šablony ji otevřete v editoru.

.. obrázek: import/import-template-produkty.png
:align:center
:alt:Možnost importu záznamů zvolitelná v ozubeném kolečku na stránce produktů v prodejním modulu Odoo.

Jakmile je stáhnutý šablonový soubor, otevřete soubor s tabulkou a upravte jej podle svých potřeb.

Upravte šablonu pro dovoz produktů
=================================

Když se návrh dovozu stáhne a otevře, je čas upravit jeho obsah.
Předtím, než se do procesu pustíte, je třeba si uvědomit několik věcí:

- Můžete bez obav odstranit všechny sloupce, které nejsou považovány za nutné. Ale je silně doporučeno
:guilabel:`Vnitřní odkaz` zůstává.

I když není povinné, mít v :guilabel:`Interní popisky (např. „FURN_001“)
Do sloupce „Reference“ můžete zadat číslo produktu, které vám pomůže při mnoha příležitostech. To dokonce i s předchozími
softwarové tabulky, které usnadňují přechod na Odoo.

Příkladem je například aktualizace dovážených produktů. V tomto případě lze stejný soubor importovat několikrát bez
vytváření duplicit, čímž se zvyšuje efektivita a jednoduchost řízení dováženého produktu.
- Nepřejmenujte sloupce, které mají být importovány. Jinak se Odoo nebude
je rozpoznat a uživatel je musí ručně přiřadit na obrazovce pro import.
- Pokud chcete přidat nové sloupce do šablonového listu, můžete tak učinit.
Pole musí existovat v Odoo. Pokud Odoo nenajde pole s daným jménem sloupce, může být spárováno
manuálně během procesu importu.

Během procesu importu dokončeného šablonového souboru se Odoo zobrazí stránka s výpisem všech
- části nově nakonfigurovaného šablony produktu ve formátu tabulky oddělené znakem :guilabel:`File
Kolonka, pole Odoo a komentáře.

Chcete-li ručně zadat název sloupce s polem v Odoo, klikněte na tlačítko :guilabel:`Odoo Field`.
nabídka vedle sloupce „Soubor“ (viz guilabel:File Column), která vyžaduje manuální nastavení.
vhodný výběr z nabídky.

.. obrázek: import/odoo-field-dropdown-menu.png
:synchronizace: střed


Šablona importu produktů v tabulkovém formátu
===================================

Po přizpůsobení šablony tabulky produktu se vraťte na stránku importu produktů Odoo, kde
odkaz na stažení šablony je nalezen a klikněte na tlačítko „Nahrát soubor“ v pravém horním rohu.
roh.

.. obrázek: upload-file-button.png
:align:center
:alt:Tlačítko pro nahrání souboru na stránce stahování šablony dovozu produktů v Odoo Sales.

Poté se zobrazí okno s dokončeným šablonou tabulky produktu.
vybrány a nahrané do Odoo.

Poté se zobrazí stránka s jednotlivými prvky nově nakonfigurovaného šablony produktu.
tabulka oddělená znakem „:guilabel:“ File Column“, „:guilabel:“ Odoo Field“ a „:guilabel:“ Comments“.

.. obrázek: import/import-souboru-stránka.png
:align:center
:alt:Import stránky s přidáním souboru po nahrání šablony produktu do Odoo Sales.

Zde lze ručně přiřadit :guilabel:`File Column` k :guilabel:`Odoo Field`, pokud
nutné.

Aby bylo vše v pořádku a všechny sloupce a pole jsou správně uspořádány.
klikněte na tlačítko „Zkouška“ v pravém horním rohu.

Pokud je vše správně nastavené, Odoo zobrazí modrou lištu na horní části stránky.
Informuje uživatele, že: „Vše vypadá jako platné“.

.. obrázek: import/vše-vypadá-platně-zpráva.png
:align:center
:alt:Všechno vypadá, jako by bylo správně zapsané, pokud jsou ve sloupcích souboru uvedeny správné hodnoty.

Pokud se vyskytne nějaká chyba, Odoo zobrazí červenou hlavičku na stránce s pokyny
Kde se nacházejí konkrétní problémy a jak je vyřešit.

.. obrázek: import/import-error-message.png
:align:center
:alt:Chybová zpráva, která se objeví při nesouladu sloupců ve formátu souboru s poli v Odoo.

Jakmile jsou chyby opravené, klikněte na tlačítko „Test“ znovu, abyste se ujistili, že všechny potřebné problémy byly vyřešeny.
bylo odstraněno vhodně.

Pokud je třeba nahrát další šablonu produktu ve formátu Excel, klikněte na „Nahrát soubor“.
klikněte na tlačítko, vyberte požadovaný šablonový list v Excelu a opakujte proces.

Když je vše připraveno, klikněte na tlačítko „Import“.

Po kliknutí se okamžitě načtou tyto produkty a zobrazí hlavní stránku s produkty.
Pop-up okno v pravém horním rohu, které uživateli sděluje, kolik
produkty se podařilo úspěšně dovézt.

.. obrázek: import/úspěšný-import-okno.png
:align:center
:alt:Okno, které se objeví po úspěšném procesu importu produktů do Odoo Sales.

V tuto chvíli jsou všechny nově importované produkty přístupné a upravitelné prostřednictvím
Stránka „Produkty“.

Importujte vztahové pole, atributy a varianty
================================================

Je důležité si uvědomit, že každý objekt v Odoo je spojen s mnoha dalšími objekty. Například
Produkt je spojen s kategoriemi produktů, atributy, dodavateli a podobně.
Spoje jsou známé jako vztahy.

.. poznámka::
Pro import vztahů mezi produkty musí být do systému importovány záznamy objektu, který je s tímto produktem spojen.
*první* z vlastního seznamu nabídek.

Pole vztahů
---------------

Na produktových formulářích v Odoo je několik polí, která lze upravit a přizpůsobit.
čas. Tyto pole se nacházejí pod každou záložkou v produktovém formuláři. Přestože jsou tyto položky
editovatelné přímo v produktové kartě, lze je také upravit pomocí produktového importu.

Jak bylo zmíněno výše, takové vztahové pole lze do produktů importovat pouze tehdy, pokud
existuje v databázi. Například pokud uživatel zkouší do systému importovat produkt s hodnotou *Typ produktu*,
je možné pouze jedno z předdefinovaných produktových typů, které existují v databázi (např. *Skladovatelné
Produkt* (Produkt), Spotřební materiál* (Spotřební materiál), atd.

Pro import informací o vztahu na šabloně pro import produktů do tabulky přidejte jméno
pole jako název sloupce/nadpisu v tabulce. Poté přidejte
Pole volby požadované vztahy.

Po zadání všech požadovaných informací o poli vztahů uložte tabulku a importujte ji.
do databáze podle procesu uvedeného výše (:menuselection:`Prodejní aplikace --> Produkty -->
Produkty --> ikona „Nástroje“ --> Nahrát záznamy --> Nahrát soubor“.

Jakmile byla do tabulky nahrána nově konfigurovaná pole vztahů, klikněte
„Dodavatelé“ a Odoo se vrátí na stránku „Produkty“.

Když jsou produkty s novými vztahovými poli změněny nebo upraveny.
importovány a nahrazeny novými informacemi, které lze najít na stránce :guilabel:`Produkty`.

Příznaky a hodnoty
---------------------

Odoo umožňuje uživatelům importovat atributy a hodnoty produktů, které lze použít pro produkty.
a nebo s dováženými produkty.

Pro import atributů a hodnot je potřeba samostatný sešit nebo soubor CSV určený pro atributy.
Hodnoty musí být importovány a nahrané, než mohou být použity pro další produkty.

Název sloupců/nadpisy atributů a hodnot tabulky by měly být následující:
:guilabel:'Atribut', :guilabel:'Zobrazovací typ', :guilabel:'Způsob vytváření variant' a
:guilabel:`Hodnota/hodnoty“.

.. obrázek: import/attributy-a-hodnoty-v-tabulce.png
:align:center
:alt:Šablona tabulky pro import atributů a hodnot.

- :guilabel:`Atribut`: název atributu (např. „Velikost“).
- :guilabel:`Zobrazovací typ“: Zobrazovací typ použitý v konfigurátoru produktu. Existují tři
typ možností:

  - :guilabel:`Rádio“: hodnoty zobrazené jako tlačítka
  - :guilabel:`Výběr“: hodnoty zobrazené v seznamu výběru
  - :guilabel:`Barva“: hodnoty vyjádřené jako výběr barvy

- :guilabel:`Způsob vytváření variant“: jak se varianty vytváří při aplikaci na produkt.
Existují tři možnosti vytváření režimu:

  - :guilabel:'Okamžitě': všechny možné varianty jsou vytvořeny ihned po atributu a jeho
hodnoty jsou přidány do výrobku
  - :guilabel:Dynamicky: každá varianta je vytvořena pouze tehdy, když odpovídají jejím atributům a
hodnoty se přidávají do objednávky na prodej
  - :guilabel:`Nikdy“: varianty jsou vždy vytvářeny pro atribut

.. poznámka::
Vlastnost „Vytváření variant“ **nemůže být změněna**, jakmile je použita na nějakém objektu.
aspoň jednu položku.

- :guilabel:`Hodnoty/Hodnota“: hodnoty odpovídající příslušnému atributu. Pokud existuje více
hodnoty pro stejnou vlastnost musí být na jednotlivých řádcích tabulky.

Jakmile jsou do tabulky zadány požadované atributy a hodnoty, je čas na
import a nahrajte ji do Odoo. Pro přístup k této funkci přejděte na: „Prodejní aplikace --> Konfigurace
--> Vlastnosti --> ikonu „Nástroje“ --> Importovat záznamy --> Nahrát soubor“.

Jakmile byla do tabulky s novými atributy a hodnotami nahrána, klikněte
„Dodavatelé“, a Odoo se vrátí na stránku „Vlastnosti“. Tam jsou tyto
nově přidané atributy a hodnoty lze najít a upravit, pokud je třeba.

Jak bylo uvedeno výše, když jsou atributy a hodnoty přidány do databáze Odoo, mohou být
použít pro stávající nebo dovážené výrobky.

Varianty produktů
----------------

Když jsou v databázi nakonfigurovány atributy a hodnoty produktu, mohou být použity na produkt.
importovat tabulky doplnit produkty o další informace a detaily.

Pro import produktů s atributy a hodnotami musí být vložen do tabulky šablony pro import produktů.
může být konfigurován s konkrétními atributy produktu, například „Attribute“ nebo „Product
Atributy/Hodnoty a sloupec guilabel:Jméno.

Mohou být i další sloupce, ale tyto jsou **povinné** pro správné importování.
produkty s konkrétními variantami.

.. obrázek: import/produktova-vlastnost-seznam-importu.png
:align:center
:alt: Tabulka s variantami produktu a atributy pro účely importu.

- :guilabel:`Název produktu`: název produktu
- :guilabel:`Produktové atributy/Atribut“: název atributu
- :guilabel:`Vlastnosti produktu/Hodnoty“: hodnoty odpovídající příslušnému atributu

..tip:
Pro dovoz více hodnot oddělte je pouze čárkou, **ne** čárkou následovanou mezerou.
v šabloně pro dovoz produktů (např. „nábytek, sedačka, domov“).

Když jsou v tabulce uvedeny požadované produkty a varianty produktů a uloženy,
čas na import a nahrání je v aplikaci „Prodej“. Pro přístup k této možnosti se přesuňte na:
Produkty --> Produkty --> ikonka ⚙️ --> Nahrát záznamy --> Nahrát soubor.

Jakmile byla do tabulky s nově konfigurovanými produkty a variantami produktů nahrána,
Klikněte na „Import“ a Odoo se vrátí na stránku „Produkty“. Tam můžete
Najdete zde nově přidané produkty.

Pro zobrazení a úpravu vlastností a variant produktů vyberte požadovaný produkt ze seznamu
Stránku „Produkty“ a klikněte na záložku „Atributy a varianty“.

.. viz též:
:doc:`varianty“
