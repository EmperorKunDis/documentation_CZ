==========================
Kontrola kvality pokynů
==========================

.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`
.. |QCP| nahradit za :: abbr: QCP (kontrolní bod kvality)

V Odoo *Kvalita* je kontrola návodu jedním z typů kvalitativních kontrol, které lze vybrat.
při vytváření nové kontroly kvality nebo kontrolního bodu kvality (QCP)*. Návody na kontrolu kvality obsahují
textové pole pro zadání pokynů, jak dokončit kontrolu.

Pro kompletní přehled o tom, jak nakonfigurovat kvalitativní kontrolu nebo QCP, viz dokumentace
kontrolními body kvality a kontrolami kvality.
<kvalita/kvalitní řízení/kontrolní body kvality>“.

Zkontrolovat kvalitu instrukcí
=====================================

Existuje několik způsobů, jak mohou být kontroly kvality prováděny. Pokud je
Pokud je přiřazen k určitému výrobnímu nebo skladovému příkazu, lze šek zpracovat na
objednávku přímo. Alternativně lze objednávku zpracovat z stránky šeku.

Proces z karty kontroly kvality
-------------------------------------

Pro zpracování kontroly kvality *Návod* začněte procházením stránky s kontrolou.
:menu „Kvalita“ -> „Kontrola kvality“ -> „Kontroly kvality“, vyberte kontrolu kvality.
:guilabel:`Návod k použití` pro dokončení kontroly.

Pokud produkt projde kontrolou kvality, klikněte na tlačítko „Prošel“ nad formulářem s kontrolou kvality. Pokud
produkt neprošel kontrolou, klikněte na tlačítko „Zrušit“.

Kontrola kvality procesu na objednávce
---------------------------------

Pro zpracování kontroly kvality *Návod* u objednávky vyberte výrobní nebo skladovou objednávku.
objednávka (dodání, vrácení, atd.), u které je nutné předložit fakturu. Výrobní objednávky lze
vybrané pomocí navigace na:menu: „Výroba“ -> „Provoz“ -> „Dodavatelské objednávky“.
a kliknutím na objednávku skladu. Skladové objednávky lze vybrat přes
:menu „Zásoby“, kliknutím na tlačítko „Proces“ v kartě operace.
vybrat objednávku.

Na vybrané výrobní nebo skladovací objednávce se objeví modrá tlačítka „Kontrola kvality“
nad objednávkou. Klikněte na tlačítko pro otevření okna „Kontrola kvality“, ze kterého
Může být zpracována jakákoliv kvalitativní kontrola vytvořená pro objednávku.

.. obrázek: návod_kontrola_kvality_pop-up.png
:align:center
:alt:Okno kvalitativní kontroly při výrobním nebo zásobovacím příkazu.

Pro dokončení kontroly kvality podle pokynů *Návod k použití* postupujte podle následujících instrukcí:
Okno „Kontrola kvality“ a nakonec stiskněte tlačítko „Potvrdit“, abyste potvrdili, že
Provedena kontrola.

Pokud během kvalitativní kontroly zjistíte nějaký problém nebo vadu, může být nutné vytvořit upozornění na kvalitu.
upozornit kvalitní tým. Klikněte na tlačítko „Upozornění kvality“ v horní části obrazovky.
výrobního nebo skladovacího příkazu po ověření kontroly.

Kliknutím na tlačítko „Upozornění kvality“ se otevře formulář s upozorněním na kvalitu nové stránky.
jak vyplnit formulář kvalitní výstrahy, zobrazit dokumentaci na téma:ref:`kvalitní výstraha
<kvalita/kvalitní management/upozornění na kvalitu>.

Kontrola kvality práce na zakázkách
--------------------------------

Při konfiguraci |QCP|, který je spouštěn výrobním příkazem, lze také zadat konkrétní pracovní příkaz.
musí být uveden v poli „Provádění pracovního příkazu“ na formuláři QCP. Pokud je
specifikované, pro konkrétní objednávku práce je vytvořen kontrolní seznam kvality „*Návod k použití*“ namísto
Ve své podstatě je MO celkem.

Kontroly kvality, které jsou pro pracovní příkazy nastaveny, musí být provedeny z modulu *Podlaha*.
takže začněte tím, že se přesunete na: „Výroba -> Provoz -> Výrobní objednávky“.
Vyberte |MO|, které obsahuje pracovní příkaz, pro který je vyžadována kontrola kvality *Návod*.

Vyberte záložku „Pracovní příkazy“ na kartě |MO| a klepněte na tlačítko „Otevřít pracovní příkaz“.
(čtverec s šipkou, která z něj vychází) na řádku právě zpracovávané objednávky.
výsledné okno s názvem „Pracovní příkazy“, klikněte na tlačítko „Otevřít výrobní plochu“.
otevřít modul *Prodejní plocha*.

Při přístupu z konkrétní objednávky se otevře modul „Dílna“ na stránku s prací
centru, kde je objednávka konfigurována k zpracování a izoluje kartu pracovního příkazu tak, aby
Ostatní karty jsou ukázány.

Začněte zpracovávat kroky pracovního příkazu, dokud nedosáhnete kroku *Návod*.
Klikněte na krok, abyste zobrazili okno s podrobnostmi o tom, jak dokončit kontrolu kvality.
klikněte na tlačítko „Další“ a pokračujte do dalšího kroku.

.. obrázek: návod_kontrola/návod-kontrola-podlaha.png
:align:center
:alt:Kontrola instrukcí, jak se zobrazuje v modulu výroby.

Alternativně můžete kvalitní kontrolu „Návod“ dokončit kliknutím na zaškrtávací políčko
se objevuje na pravé straně čáry kroku v pracovním příkazu.
kontrola kvality probíhá automaticky bez otevření okna s upozorněním.

.. poznámka::
Pro plný průvodce modulu Shop Floor se podívejte na :ref:`Přehled Shop Floor
dokumentace pro výrobní závod nebo pro přehled výroby.
