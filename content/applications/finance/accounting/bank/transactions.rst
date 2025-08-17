============
Transakce
============

Import transakcí z výpisů z účtu vám umožní sledovat pohyby na vašem účtu.
a vyrovnat je s těmi, které evidujete v účetnictví.

Synchronizace bankovního účtu automaticky provede proces. Pokud však ne
chcete ji používat nebo pokud váš bankovní účet ještě není podporován, existují další možnosti:

- :ref:`Transakce z banky <transactions/import> dodané vaší bankou;
- :ref:`Zadat manuálně transakce z bankovního účtu <transactions/register>“.

.. poznámka::
:ref:`Skupování transakcí podle výpisu <transactions/statements>` je volitelné.

... transakce/dodávky:

Transakce s dovozem
===================

Odoo podporuje více formátů souborů pro import transakcí:

- SEPA doporučuje formát správy hotovosti (CAMT.053).
- Hodnoty oddělené čárkou (CSV)
- Open Financial Exchange (OFX)
- Formát výměny rychlého převodu (QIF)
- Belgie: Kódovaný výpis z účtu (CODA)

Pro import souboru přejděte do sekce „Účetní panel“ a v části „Banka“
klikněte na tlačítko „Importovat soubor“.

.. tip::
Alternativně můžete také:

   - klikněte na ikonu „fa-ellipsis-v“ (zavináč) v položce „Banka“.
vložte do záznamu a vyberte možnost „Importovat soubor“;
   - nebo přejít na seznam transakcí kliknutím na ikonu „:icon:`fa-ellipsis-v`“ :guilabel: („zavináč“)
ikonu na časopisu „Banka“ a vyberte „Transakce“, pak klikněte
ikona „fa-cog“ a vyberte možnost „Importovat záznamy“.

Poté vyberte soubor a nahrajte ho.

Po nastavení potřebných formátovacích možností a přiřazení sloupců souboru k příslušným polím v Odoo
můžete spustit testování a import bankovních transakcí.

.. viz též:
:doc:`/aplikace/základní/export-a-import-dat“

.._transakce/registr:

Zadávat bankovní transakce ručně
===================================

Můžete také manuálně zadávat své bankovní transakce. Chcete-li tak učinit, přejděte na: guilabel:Účetnictví
Přejděte na záložku „Dashboard“, klikněte na záznam „Banka“ a poté na „Nový“. Ujistěte se, že vyplníte
Vyjměte pole „Partner“ a „Label“, aby se usnadnilo proces spojování.

.. transakce/výpisy:

Prohlášení
==========

Bankovní výpis je dokument, který vystavuje banka nebo finanční instituce a uvádí
transakce, které proběhly v konkrétním bankovním účtu za určené období.

V Odoo účetnictví je možné transakce seskupovat podle souvisejícího výpisu, ale závisí
Váš obchodní tok můžete chtít zaznamenat pro účely kontroly.

.. důležité::
Pokud chcete porovnat zůstatky na konci výpisu z účtu s koncovými zůstatky
Váš účetní záznam, nezapomeňte vytvořit otevřenou transakci, která bude zaznamenávat banku
účetní zůstatek ke dni, kdy začínáte synchronizovat nebo importovat transakce.
Je nezbytné zajistit přesnost účetnictví.

Pro zobrazení seznamu stávajících výroků přejděte na stránku „Účetní panel“ (viz ikona „Guide Label: Accounting Dashboard“) a klikněte na
:icon:`fa-ellipsis-v` :guilabel:`(ellipsis)` ikona vedle bankovního nebo hotovostního deníku, který chcete
zkontrolovat a kliknout na:guilabel:"Vyjádření".

.._transakce/vyjádření kanbanu:

Vytváření výkazů z pohledu kanbanu
---------------------------------------

Otevřete zobrazení bankovního vyrovnání (kanbanu) v rozhraní účetnictví kliknutím na
název bankovního časopisu a identifikovat transakci odpovídající poslední (nejnovější).
Transakce z výpisu z účtu. Klikněte na tlačítko „Výpis“ při přejetí nad
horní separátorová linka, která vytvoří výrok z této transakce až po nejstarší transakci.
Není součástí prohlášení.

.. obrázek: transakce/výpisy-kanban.png
:alt:Tlačítko „Vyjádření“ je viditelné při přejetí kurzorem nad čarou oddělující dvě transakce.

V okně „Vytvoření výroku“ vyplňte odkaz na výrok a ověřte
její počáteční a konečný zůstatek a klikněte na „Uložit“.

.._transakce/seznam výpisů:

Vytváření výroků z pohledu seznamu
-------------------------------------

Seznam transakcí otevřete kliknutím na název bankovního deníku a přepnutím na seznam
Vyberte všechny transakce odpovídající výpisu z účtu a v
Sloupec „Vyjádření“, vyberte existující prohlášení nebo vytvořte nové zadáním jeho
odkazu, kliknutím na tlačítko „Vytvořit a upravit…“, vyplněním podrobností o prohlášení a
úspory.

.. _transakce/zobrazit, upravit a tisknout:

Zobrazení, úpravy a tisk prohlášení
----------------------------------------

Pro zobrazení stávajícího prohlášení klikněte na částku v souhrnu (v kanbanovém pohledu).
Klikněte na název výpisu v seznamu transakcí. Zde můžete údaje upravit.
„Referenční hodnota“, „Základní zůstatek“ nebo „Konečný zůstatek“.

.. poznámka::
Ruční aktualizace :guilabel:`Starting Balance` automaticky aktualizuje :guilabel:`Ending
Balíček je založen na nové hodnotě „Začáteční rovnováhy“ a na hodnotě „Hodnoty rovnováhy“.
Transakce uvedené v prohlášení.

.. varování:
Pokud hodnota :guilabel:`Starting Balance` nebude rovna předchozímu výroku s :guilabel:`Ending
Balance“, nebo pokud není rovno „Zůstatek“
(plus transakce v příkazu) se zobrazí varování, které vysvětluje
problém. Flexibilitu lze zachovat i tak, že se peníze nebudou nejprve vyřešeného problému.
problém.

Připojit digitální kopii (tj. JPEG, PNG nebo PDF) výpisu z účtu pro lepší evidenci,
Klikněte na tlačítko „Připojit přílohu“ a vyberte soubor, který chcete připojit.

K vygenerování a tisku výpisu z bankovního účtu klikněte na tlačítko „Tisk“ (pokud je přístupné).
přes „sjednocený pohled“ nebo klikněte na ikonu „fa-cog“ (ikona ozubeného kolečka) a klikněte
:ikonka: tisk: guilabel:Prohlášení (pokud je přístupné v seznamovém pohledu).

.. poznámka::
Když se vytváří výpis pro tisk, je automaticky přidán do
:guilabel:`Přílohy“.
