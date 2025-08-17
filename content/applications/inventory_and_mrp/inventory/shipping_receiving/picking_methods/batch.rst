=============
Vybírání zásilek
=============

...Inventarizace/Další/Přeprava:

Metoda *batch picking* umožňuje jednomu pracovníkovi zpracovat více objednávek najednou, čímž se snižuje
čas potřebný k navigaci do skladu. Při sběru v dávkách jsou objednávky seskupeny a
Seskupené do seznamu vyskladňování. Po vyskladnění je sada převezena na výstupní místo, kde
Produkty jsou následně tříděny do příslušných dodacích balíčků.

Odcházejícím zbožím musí být přiřazena adresa v místě výdeje po vyzvednutí. Proto je tento způsob skladování vhodný
podnikům s několika produkty, které se často objednávají. Skladování vysoké poptávky u
Dostupné lokality mohou zvýšit počet objednávek, které jsou vyřizovány efektivně.

Pokud je objem objednávek vysoký a stálý, pak je metoda batch pickingu ideální.
poptávky. Tento způsob zvyšuje efektivitu tím, že umožňuje pracovníkům vybírat položky pro více objednávek najednou.
Jeden průchod skladem a snížení doby cestování i produktivity.

Konfigurace
=============

Pro aktivaci možnosti skladování v balíčcích začněte tím, že přejdete do sekce „Aplikace Sklad -->
Konfigurace --> Nastavení“. V sekci „Operace“ zkontrolujte položku „Soubor“,
Box Wave & Cluster Transfers.

.. obrázek: batch/batch-transfer-checkbox.png
:alt:Povolte funkci „Hromadné převody“ v Nastavení > Konfigurace > Nastavení.

Odvozené skladování je metoda optimalizace operace „vybrat“ v Odoo, takže :guilabel:`Sklad
Možnosti „Umístění“ a „Vícekrokové trasy“ pod záložkou „Sklad“ musí být
je možné také zkontrolovat na této stránce nastavení. Po dokončení klikněte na tlačítko „Uložit“.

.. obrázek: batch/locations-routes-checkbox.png
:alt:Zapněte položky *Skladové místo* a *Dvoufázový přepravní plán* v sekci Inventář > Konfigurace > Nastavení.

.. viz též:
   - :doc:`Dodání ve dvou krocích <../denní operace/přijetí zboží ve dvou krocích>`
   - :doc:`../denní operace/dodání v třech krocích“

Vytvořit hromadnou platbu
======================

Pokud chcete přesunout položky přímo z aplikace Inventář, ukazujte kurzorem na
požadovaný typ operace z nabídky „Přehled skladu“ (např. „Příjmy“)
Kanban kartu), klikněte na ikonku „fa-ellipsis-v“ (vertikální elipsa) a poté vyberte
:guilabel:`Připravit Batch“.

.. obrázek: batch/prepare-batch.png
:alt:Dashboard inventáře s vyznačenou možností Připravit várku.

V poli převodu vložte následující údaje:

- :guilabel:`Odpovědný“: zaměstnanec, který byl přiřazen k vyskladnění. Nechte pole prázdné, pokud je vyskladňování prováděno *kýmkoliv*.
Tento výběr může vykonat.
- :guilabel:`Typ operace“: z rozevírací nabídky vyberte typ operace pod kterou
Přeprava je rozdělena do kategorií.
- :guilabel:`Datum plánovaného termínu“: určuje datum, do kterého je osoba odpovědná za
dokončit převod na výstupní místo.

.. viz též:
Chcete-li se dozvědět více o lokalitě přístavu, vozidle a vozidle, klikněte na tlačítko „Další informace“.
pole kategorie, viz :doc:`systém pro řízení odeslání
<../../přijímání a expedice/nastavení a konfigurace/expedice>.

Dále v seznamu „Převody“ klikněte na „Přidat řádek“, abyste otevřeli „Přidat“.
Okno přestupů.

Pokud je pole „Druh operace“ vyplněno, seznam bude filtrovat převodní záznamy odpovídající
vybraný typ operace.

Klikněte na tlačítko „Nový“ pro vytvoření nového převodu.

Po výběru přenosových záznamů klikněte na tlačítko „Potvrdit“ pro potvrzení hromadného vybírání.

.. příklad::
Nový převod je přiřazen k odpovědné osobě „Joel Willis“ pro přebírání.
:guilabel:`Typ operace“. Datum „11. srpna“ je nastaveno jako :guilabel:`Datum plánované operace“.

....... obrázek:: batch/batch-transfer-form.png
:alt: Zobrazení formuláře pro hromadné převody.

Kliknutím na tlačítko „Přidat řádek“ se otevře okno „Přidat převody“.
zobrazuje pouze sklizeň. To je proto, že vlastnost „Operační typ“ byla nastavena na „Sklizeň“.
Formulář pro hromadný přenos.

Zatrhněte políčko vedle převodů „WH/PICK/00001“ a „WH/PICK/00002“, abyste je zahrnuli.
je v novém převodu a pak klikněte na tlačítko „Vybrat“ pro zavření
:guilabel:`Přidat: Převody“ okno.

.... obrázek:batch/add-transfers-window.png
:alt:Vyberte více převodů z okna *Přidat:Převody*.

...Inventarizační sklad/sklad/přidat přesuny zásob:

Přidejte částku z převodů
-----------------------------

Další metodou vytváření hromadných převodů je možnost „Přidat do hromadného převodu“
seznam. Přejděte na položku „Aplikace Inventář --> Provoz“ v rozbalovacím seznamu a vyberte libovolnou
přepínače „Převody“ otevře filtrovaný seznam převodů.

.. obrázek:batch/transfers-drop-down.png
:alt:Zobrazit všechny typy převodů v roletce: Příjmy, Výdeje, Vnitrofiremní převody,
Výroba, přesuny várky, dodávky na objednávku.

V seznamu převodů vyberte zaškrtávací políčko vedle vybraných převodů, které chcete vložit najednou.
Poté přejděte na tlačítko „Akce“ (ikona „fa-cog“) a klikněte na „Přidat do balíčku“.
z výsledného seznamu.

.. obrázek: batch/add-to-batch.png
:alt:Klikněte na tlačítko „Přidat do sady“, které je v seznamu tlačítek „Akce“.

Tím se otevře okno „Přidat do balíčku“, ve kterém může zaměstnanec
:guilabel:`Zodpovědný“ za vyskladňování lze přiřadit.

Vyberte si z dvou možností rádia, které chcete přidat k existujícímu přenosu nebo vytvořit
:guilabel:'nové přesunutí'.

Přidejte popis pro tento balíček.

.. tip::
V poli `Popis` lze použít pole :guilabel:`Description`, které umožňuje přidat další informace, které mohou pomoci pracovníkům
identifikovat zdroj balení, kde umístit balení, jaké přepravní kontejnery použít atd.

Pro vytvoření šarže k pozdějšímu zpracování vyberte zaškrtávací políčko „Náčrtek“.

Proces ukončete kliknutím na tlačítko „Potvrdit“.

.. obrázek: batch/add-to-batch-window.png
:alt:Zobrazte okno „Přidat do balíčku“ pro vytvoření přenosu balíčkem.

Automatické sériové výrobky
-----------------

Soubory mohou být automaticky vytvářeny a přiřazovány podle několika kritérií. Automatické soubory
Volba je definována na úrovni operačního typu.

.. příklad::
V případě vícekrokového procesu dodání může být operace vyzvednutí zboží seskupena podle zákazníka.
Dodací operace může být organizována dopravcem a zemí určení.

Chcete-li povolit automatické balíčky, přejděte na:
Operační typy“ a vyberte požadovaný operační typ (např.: „Dodání“,
„Pick“, atd.). Pak vyberte jeden nebo více kritérií „Skupina zpracování“ zaškrtnutím
příslušné zaškrtávací políčko. I když je vybráno více možností skupinového výběru, vytvoří se pouze jedna sada.

Soubory mohou být automaticky vytvářeny na základě následujících kritérií:

- :guilabel:`Kontakt“
- :guilabel:`Dodavatel“
- :guilabel:`Země určení“
- :guilabel:`Zdrojová poloha“
- :guilabel:`Místo určení“

.. obrázek: batch/auto-batch-grouping.png
:alt:Nastavení stránky Přesuny várky a vlny s viditelnými kritérii automatického seskupování várky.

Přenos procesního balíčku
======================

Zpracovávejte hromadné převody v aplikaci „Sklad --> Provoz --> Hromadné převody“
stránka.

Zde vyberte požadovaný převod ze seznamu. Poté zadejte
Podrobnosti o každé položce v záložce „Podrobná operace“.
Nakonec vyberte možnost „Přijmout“ k dokončení výběru.

.. tip::
Zkontrolujte, zda je přenos celé sady dokončený, když se tlačítko „Přijmout“ zvýrazní.
purpurová. Pokud je namísto toho vyznačena tlačítko „Zkontrolovat dostupnost“, znamená to, že jsou
položky ve várce, které jsou nyní **nevyzvednutelné**.

... inventarizaci, správu a příjem zboží:

.. příklad::
V případě hromadného převodu zboží ze skladových výdejů „WH/PICK/00001“ a „WH/PICK/00002“
:guilabel:"Podrobné operace" karta ukazuje, že produkt "Skříň s dveřmi" byl vybrán
protože sloupec „Hotovo“ odpovídá hodnotě v poli „Rezervace“.
Výrobky „Kabelová řídící skříňka“ však mají množství 0,00.

.... obrázek: batch/process-batch-transfer.png
:alt:Zobrazte přesun produktů z více skladovacích míst v záložce *Podrobné operace*.

V záložce „Podrobné operace“ jsou viditelné pouze produkty skladem.

Pro zobrazení celého seznamu produktů přepněte na záložku „Operace“. Na tomto seznamu jsou
Kolonka „Požadované množství“ ukazuje požadovaný počet kusů pro objednávku. Kolonka „Rezervováno“
slouží k uvedení dostupného zásobního množství pro vyřízení objednávky. Poslední sloupec „Dokončeno“
Výrobky, které byly vybrány a jsou připraveny na další krok.

.. příklad::
Produkt „Desk Pad“ z téže série jako v předchozím příkladu:
<inventář/správa/příklad přenosu v balíčcích> je viditelný pouze ve složce :guilabel:`Operace`.
tabulku, protože v zásobách nejsou žádné „Rezervované“ množství k uspokojení přenosu balíčku.

Klikněte na tlačítko :guilabel:`Zkontrolovat dostupnost`, abyste znovu vyhledali skladové zásoby produktů, které jsou k dispozici.

.... obrázek::batch/operations-tab.png
:alt:Zobrazit nedostupné rezervované množství v záložce *Operace*.

Vytvořit poptávku
----------------

Na přepravním lístku se uvádí množství produktu „Dokončeno“, které je nižší než
Vyskytne se okno s výzvou k zadání rezervovaného množství.

Toto okno nabízí možnost „Vytvořit objednávku na vyzvednutí?“.

Kliknutím na tlačítko „Vytvořit zpětný odběr“ se automaticky vytvoří nová objednávka.

.. poznámka::
Při vytváření nové objednávky se přenosy, které nebyly ověřeny v balíčku, **nebudou**
být z něj odebrán.

Klikněte na tlačítko „Žádné další objednávky“ a dokončete vyzvednutí bez vytváření nových objednávek.

Klikněte na tlačítko „Zrušit“ a vraťte se zpět do formuláře pro přenos souborů.

.. obrázek: batch/create-backorder.png
:alt:Zobrazit okno pro vytvoření objednávky na dodání.
