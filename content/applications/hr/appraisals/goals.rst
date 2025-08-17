=====
Cíle
=====

Aplikace Odoo **Hodnocení** umožňuje manažerům stanovit (a sledovat) jasné cíle pro své
zaměstnanci. Stálý pokrok směrem k cílům dává zaměstnancům mezi hodnoceními konkrétní cíl.
poskytnout manažerům spolehlivé informace při hodnocení výkonnosti.

Zobrazit cíle
==========

Pro zobrazení všech cílů přejděte na: „Aplikace hodnocení -> Cíle“. Tato aplikace zobrazí
cíle pro každého zaměstnance, v výchozím seznamovém pohledu, seskupené podle :guilabel:`Zaměstnanec`.

Klikněte na zaměstnance, abyste zobrazili seznam stanovených cílů. Každý cíl obsahuje následující informace:

- :guilabel:`Jméno`: Jméno branky.
- :guilabel:`Vytvořeno na“: Datum, kdy byl cíl vytvořen.
- :guilabel:`Pokrok“: Procento pokroku, kterého zaměstnanec dosáhl.
- :guilabel:`Zaměstnanec“: Zaměstnanec přiřazený k cíli.

.. poznámka::
V seznamu se objevují pouze zaměstnanci, kterým byl přidělen cíl.

.. obrázek: góly/golová listina.png
:alt: Seznam cílů pro všechny zaměstnance.

.. _hodnocení / karta s cílem:

Vytvářejte cíle
============

Pro vytvoření nových cílů přejděte na: „Hodnocení aplikace -> Cíle“ a klikněte
V levém horním rohu klikněte na „New“ a otevřete prázdný formulář pro vstřelené góly. Do něj zadejte následující informace
formát:

- :guilabel:`Cíl“: Zadejte stručný název cíle do tohoto pole.
- :guilabel:`Zaměstnanec“: Vyberte zaměstnance, který má být přiřazen k cíli pomocí rozbalovací nabídky.
Pokud je pole vyplněno, manažer zaměstnance vyplní pole :guilabel:`Manažer`.
- :guilabel:"Pokrok": Klikněte na aktuální procento dovednosti, kterou chcete dosáhnout. Možnosti jsou
:guilabel:`0 %“, :guilabel:`25 %“, :guilabel:`50 %“, :guilabel:`75 %“ nebo :guilabel:`100 %“.
- :guilabel:`Manager`: Vyberte manažera zaměstnance z roletkového menu (pokud není již vybrán).
vybrané).
- :guilabel:`Termín splnění cíle“: Vyberte datum splnění cíle pomocí kalendáře.
- :guilabel:`Štítky“: Přidejte do seznamu sestupně jakékoliv relevantní štítky.
cíl.
- :guilabel:`Popis cíle“: Zadejte do této záložky podrobnosti o cíli.

.. tip::
Některé cíle lze rozdělit na kroky, které mohou být zadány jako seznam úkolů. Seznam úkolů je
nástroj, který zaměstnanec může použít k označení svého pokroku.

.. obrázek: góly/nový-gól.png
:alt:Dokončený cíl vytvořený pro učení se Pythonu.

... _hodnocení/přidat štítky:

Štítky
----

Přidávání štítků ke gólům může pomoci při zobrazení zprávy o gólech, abyste viděli, kolik gólů bylo s konkrétním
k zaměstnancům jsou přiřazeny štítky.

Pro zobrazení všech aktuálních štítků a přidání nových klikněte na:
Konfigurace --> Štítky. Všechny štítky se zobrazují v mřížkovém pohledu. Výchozí štítky jsou: :guilabel:`Externí`,
:guilabel:`Technické dovednosti“, „Vnitřní“, „Programování“ a
:guilabel:`Školení“.

Pro přidání nového štítku klikněte na tlačítko „Nový“ v pravém horním rohu, a objeví se nová řádka.
na konci seznamu. Zadejte značku, pak stiskněte klávesu Return nebo klikněte mimo pole.

Aktualizace cílů
============

Během hodnocení zaměstnanců jsou zkontrolovány cíle a zjištěno, jaký pokrok zaměstnanec udělal.
když zaměstnanec dosáhne dalšího stupně pokroku, cíl se musí přizpůsobit.

Aby se aktualizoval procentuální pokrok k dosažení cíle, přejděte na: „Aplikace hodnocení -> Cíle“.
Rozbalte zaměstnance, jehož cíle se hodnotí, a klikněte na konkrétní cíl, abyste otevřeli
rekord v počtu gólů.

Klikněte na nový políčko „Pokrok“ a nastavte novou úroveň pokroku. Doporučuje se přidat poznámky
v záložce „Popis“ v průběhu plnění cíle. Poznámky by měly
Uveďte datum změny a jakékoliv další informace o této změně.

.. poznámka::
Progres může být kdykoliv aktualizován manažerem zaměstnance, nejen při hodnocení.

Úplné cíle
==============

Když je cíl splněn, je důležité záznam aktualizovat. Přejděte na
:menuvolba-->Hodnocení cílů-->Zaměstnanec. Rozbalte zaměstnance, jehož cíle jsou hodnoceny.
Klikněte na jednotlivé góly, aby se zobrazila tabulka s nahrávkami.

Klikněte na tlačítko „Zaškrtnuto“ v pravém horním rohu. Zelené „Dokončeno“ pásmo
je umístěn v pravém horním rohu karty s cílem a zobrazuje se
:guilabel:`100 %“.

.. poznámka::
Na panelu „Cíle“ jsou dokončené cíle označeny zeleným „100 %“.
v sloupci „Pokrok“.
