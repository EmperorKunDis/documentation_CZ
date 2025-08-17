===========
Provize
===========

.. |SOs| nahradit za: zkratka: `SOs (Sales Orders)`

Provize jsou silným nástrojem k motivaci prodejního týmu. Motivují výkon a zvyšují
produktivitu a podpořit zdravou soutěživost. Funkce „Komise“ v Odoo Sales
Aplikace poskytuje způsob, jak odměnit obchodníky nebo týmy na základě jejich výkonu.
tato funkce podporuje vytváření flexibilních a měřitelných struktur odměňování, které se shodují s obchodními cíli.
cíle, ať už jde o zvýšení tržeb, objemu, zisku nebo opakovaných smluv.

Konfigurace
=============

Pro zapnutí funkce „Komise“ přejděte do: „Prodejní aplikace“ -> „Nastavení“ ->
Nastavení“. Vyhledejte sekci „Fakturace“ a zaškrtněte „Provize“.
zaškrtnutí políčka. Poté klikněte na tlačítko „Uložit“. To způsobí, že se objeví nový „Provize“
v nabídce. Pro vytvoření nového plánu komisí přejděte na:
Vyberte možnost „Plány“ a klikněte na „Nový“.

Struktura plánu komise
=========================

Každý plán odměn se skládá z několika částí:

- :guilabel:Na základě: Určuje, zda jsou odměny udělovány na základě pokroku
:guilabel:`Cíle“ nebo „Dosáhnuté cíle“.
- :guilabel:`per`:Ukazuje, zda se plán týká jednotlivých obchodníků nebo celé prodejní
tým
- :guilabel:`Četnost cílů“: Umožňuje nastavit, jak často se cíle obnoví: **Měsíčně**, **Čtvrtletně** nebo
**Ročně**.
- :guilabel:`Dosahování cílů“: určuje, co se měří v rámci provizí.

.. obrázek: komise/nový plán komisí.png
:alt: Nová podrobnější verze plánu komise.

Plány na provize založené na cílech
-----------------------------

V komisním plánu založeném na cílech jsou provize udělovány podle procenta tržeb.
cíle dosaženy. Plány založené na cílech jsou ideální pro stanovení jasných a měřitelných cílů, jako je například fakturace
určité množství prodejů za čtvrtletí, pak postupně odměňovat obchodníky podle toho, jak blízko
Dosahují nebo překračují cíl.

..tip:
Plány založené na dosažení cíle se liší od plánů založených na dosažení úspěchu, protože jsou založené na dosažení cíle.
fixní, předem stanovený cíl. Zaměřují se na motivaci založenou na dosažení cíle a splnění výkonnostních milníků.

Pro konfiguraci nového cílového plánu založeného na provizích přejděte do aplikace „Prodej“ v nabídce „Nástroje“.
Provize --> Základní plán, pak klikněte na „Nový“. Klikněte v poli „Založeno na“
Vyberte si z nabídky a v poli „per“ vyberte možnost.

V poli „Provize“ nastavte výplatu za dosažení 100 % cíle
cíl. Aktualizujte pole „Účinný čas“ a potvrďte datum tohoto plánu. Pak
aktualizovat pole „Četnost cíle“ podle toho, jak často by měly být cíle nastaveny a
hodnocené.

- *Měsíční*: krátkodobé cíle s častými výplatami.
- Čtvrtletní: Synchronizuje se s obchodními cykly a poskytuje střednědobé cíle.
- *Ročně*: dlouhodobé prodejní cíle pro strategické plánování.

Po aktualizaci pole „Četnost cílové skupiny“ se v záložce „Zaměření“ zobrazí
seznam vhodného časového rámce. Pro každý z nich zadejte cíl „Zaměření“.

Na záložce „Dosáhnuté cíle“ přidejte jeden nebo více ukazatelů dosažených cílů.
„Prodej“, „Provize“ nebo „Dosažené cíle“ pro tento plán kliknutím na „Přidat nový cíl“.

Klikněte na záložku „Prodejní zástupci“ a přiřaďte tento plán k odpovídajícím zaměstnancům. Klikněte buď
Pokud chcete přidat nového prodejce jednotlivě, použijte :guilabel:`Add New Sales Person`, pokud chcete přidat více prodejců najednou, použijte :guilabel:`Add Multiple Sales People`.
Prodavačky přidávají na váhu postupně.

.. poznámka::
Tlačítko „Přidat více prodejců“ je k dispozici pouze v případě, že
:doc:`Vývojářský režim je aktivní.“

Úrovně
------

Pro dodatečný impuls mohou být k plánům „Zaměřeno na cíl“ přidány úrovně provize.
úrovně umožňují prodejcům vydělávat různé provize podle výkonnosti.
může začít na 0 % a postupně se zvyšovat. To umožňuje prodejcům vydělávat provize i když
Nedosahují „sto procent“ cíle, stejně jako schopnost dosáhnout více než „100 %“.
cíl. Úrovně provizí lze nastavit v záložce „Provize“ při tvorbě provize.
plán.

Pokud nejsou přidány žádné úrovně nad 100 %, obchodníci nemohou vydělat více, než je uvedeno v provizi.

Příklad:
V níže uvedeném plánu začínají úrovně na 0 % a pokračují až do 300 %. Pokud obchodník překročí
„100 %“ očekávaného cíle, jejich očekávaný výdělek stále roste až na „300 %.

.... obrázek: komise/úrovně komisí.png
:alt:Příklad provizních sazeb, kde je úroveň nad 100 procenty.

Plány odměňování na základě dosažených výsledků
----------------------------------

V plánu na základě dosažených výsledků dostávají prodejci procento z hodnoty faktury.
provize. Plány založené na cílech jsou ideální pro odměňování konzistentní obchodní aktivity bez ohledu na
konkrétní cíle. Například nabídnout 5% provizi z celkové částky faktury bez ohledu na to, jak
Prodává se hodně.

..tip:
Achievement-based plány se liší od plánů založených na cílech, protože jsou vypočítávány podle
skutečné dosažené výsledky za použití rovnoměrné sazby. Jsou prospěšné pro trvalé, necílové
plány odměňování založené na výkonnosti.

Pro konfiguraci nového cílového plánu založeného na provizích přejděte do aplikace „Prodej“ v nabídce „Nástroje“.
Provize --> Základní plán, pak klikněte na „Nový“. Klikněte v poli „Založeno na“
Vyberte možnost „Dosáhnout“ a poté vyberte možnost v poli „Počet“.

Aktualizujte pole „Platnost“ a potvrďte datum tohoto plánu. Poté aktualizujte
Zadejte hodnotu pole „Četnost cílů“ podle toho, jak často by měly být cíle nastaveny a vyhodnocovány.

Na záložce „Dosáhnuté cíle“ přidejte jeden nebo více ukazatelů dosažených cílů.
„Prodej“, „Provize“ nebo „Dosažené cíle“ pro tento plán kliknutím na „Přidat nový cíl“.

Klikněte na záložku „Prodejní zástupci“ a přiřaďte tento plán k odpovídajícím zaměstnancům. Klikněte buď
Pokud chcete přidat nového prodejce jednotlivě, použijte :guilabel:`Add New Sales Person`, pokud chcete přidat více prodejců najednou, použijte :guilabel:`Add Multiple Sales People`.
Prodavačky přidávají na váhu postupně.

..prodej/provize/metrika výkonu:

Dosavadní úspěchy
------------

Výkonnost lze měřit různými způsoby v plánech výkonu. Tyto jsou konfigurovány v
Kartě „Dosáhnuté cíle“ každého plánu.

- :guilabel:`Prodáno“: celková hodnota prodejních objednávek (PO).
- :guilabel:`Potvrzená faktura“: Celková hodnota potvrzených faktur.
- :guilabel:`Prodejní množství“: celkový počet jednotek prodaných prostřednictvím SOs.
- :guilabel:`Počet fakturovaných jednotek“: celkový počet jednotek, které byly fakturovány.
- :guilabel:`Marže“: ziskovost (prodejní cena mínus nákupní cena).
- :guilabel:`MRR“: nový měsíční příjem z předplatného.
**pouze** pokud je nainstalovaná aplikace „Předplatné“ (viz dokumentační stránku).

.. poznámka::
Ať už je plán jakýkoliv, každý z nich potřebuje obě složky „Dosáhnout“ a
*Záměry* nakonfigurovány.

Schválení plánu
=============

Po potvrzení podrobností nového plánu klikněte na tlačítko „Schválit“. To přesune plán do
Stav „Návrh“ do stavu „Schváleno“.

.. důležité:
Plány komise v stádiu schválení **nemohou být upravovány**. Chcete-li upravit schválený plán, musíte jej nejprve smazat a poté znovu přidat.
Pokud chcete změnit plán, musíte nejprve zrušit aktuální verzi.

Po schválení plánu automaticky sleduje výkonnost a vypočítává provize na základě
Ustálené parametry.
