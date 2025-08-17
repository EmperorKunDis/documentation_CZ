===================
Bankovní vyrovnání
===================

Proces „Srovnání bankovního účtu“ je procesem, při kterém se vaše :doc:`bankovní transakce <transakce> shodují s
Vaše obchodní záznamy, například:
<../faktury dodavatelů>, a :doc:`platby <../platební styk>“. To je nejen povinné pro většinu
firem, ale nabízí také několik výhod, jako je snížení rizika chyb v oblasti finančních
zprávy, odhalování podvodných aktivit a zlepšení řízení hotovostního toku.

Díky bance se používají :doc:`modelové rekonciliace <reconciliation_models>`, které předvybírají
automaticky shodné záznamy.

.. viz též:
   - „Návody k Odoo: Bankovní vyrovnání
<https://www.odoo.com/slides/slide/bankovní vyrovnání 2724>
   - :doc:`bankovní synchronizace“
   - :doc:`transakce“

.. účetnictví/srovnání/přístup:

Zobrazení bankovního vyrovnání
========================

Pro přístup k rozvaze v režimu „Soulad“ se přihlaste do svého účtu na stránce „Dashboard účetnictví“.
nebo:

- Klikněte na název časopisu (např. :guilabel:`Bank`) a zobrazí se všechny transakce včetně těch
dříve usmířené
- Klikněte na tlačítko „Sjednotit položky“ a zobrazí se všechny transakce, které Odoo předem vybralo.
usmíření. Můžete odstranit filtr :guilabel:`Nesouhlasí´ z vyhledávací lišty, aby se do výsledků
dříve vyrovnané transakce.

.. obrázek: usmíření/kreditní karta.png
:alt:Dostupnost nástroje pro vyrovnání bankovních účtů z účetního přehledu

Výpis z účtu je rozdělen do tří samostatných částí: transakce, protistrana
vstupy a výsledný vstup.

.. obrázek: usmíření/uživatelské rozhraní.png
:alt:Uživatelské rozhraní pro zobrazení výpisu z účtu.

Transakce
V levém sloupci je sekce transakcí, kde jsou zobrazeny všechny bankovní transakce, nejnovější vpředu.
1) Klikněte na transakci, kterou chcete vybrat.

Protiexekuční záznamy
V části pro protichůdné záznamy na spodním pravém okraji se zobrazí možnosti, jak vybrat výběr.
bankovní transakce. K dispozici jsou také další záložky, včetně
:ref:`sjednocení/stávajících záznamů“, :ref:`sjednocení/přímé platby“.
:ref:`sjednocení/ruční operace“ a „Diskuse“, která obsahuje chat.
vybraný bankovní účet.

Výsledný záznam
Výsledný záznam v horním pravém rohu zobrazuje vybranou bankovní transakci, která se shoduje s
- vzájemné položky a zahrnuje jakékoliv zbývající kredity nebo debety. V této části můžete
ověřit shodu nebo ji označit jako „Kontrola“. Kdokoli může použít kteroukoli z :ref:`modelů
Tlačítka <reconciliation/button> jsou také k dispozici v sekci výsledku.

...účetnictví/vyrovnání/vyrovnat:

Sjednotit transakce
======================

Transakce lze spárovat automaticky pomocí modelů pro vyrovnání.
<model_of_reconciliation>, nebo je lze spárovat s existujícími záznamy
<sjednocení/stávajících záznamů>, :ref:<výplaty v hromadných platbách><sjednocení/hromadné platby>.
„ruční operace“ (viz „Manuální operace“), a „tlačítka pro modelovou kontrolu“.
<rekonstrukce/tlačítko>.

#Vyberte transakci mezi nezaúčtovanými bankovními transakcemi.
#Definujte protějšek. Existuje několik možností definování protějšku včetně
:ref:`současnými záznamy <rekonciliace/soucasne-zaznamy>“, :ref:`ruční operace
<sjednocení/ruční operace>“, „<sjednocení/výběry v hotovosti>“ a
:ref:`tlačítka pro vyrovnání <reconciliation/button>“.
#Pokud je výsledný záznam nevyvážený, vyrovnejte jej přidáním dalšího existujícího protějšku.
vstup nebo jej zapsat ručně pomocí :ref:`ruční operace <srovnání/ruční-operace>`.
#Klikněte na tlačítko „Potvrdit“ a potvrďte dokončení srovnání.
transakce.

.. tip::
Pokud nejste si jisti, jak se vypořádat s konkrétní transakcí, rádi vám pomůžeme.
Later můžete použít tlačítko „Zkontrolovat“ namísto „Přidat“. Všechny transakce označené jako „Zkontrolovat“
„Zkontrolovat“ lze zobrazit pomocí filtru „Pro kontrolu“.

.. poznámka::
Bankovní transakce jsou zaznamenány na účet **záložního deníku** až do doby, než je vyrovnána.
bod, sjednocení mění záznam z účetního deníku tím, že nahradí bankovní odloženou položku.
účet s příslušným pohledávkovým, závazkovým nebo nedoplatkem.

..._usmíření/existující záznamy:

Souhlasit s existujícími záznamy
----------------------

Tato záložka obsahuje shodné položky, které Odoo automaticky vybírá podle srovnání.
modely. Seznam vstupů je založen na :doc:`modelu shody <reconciliation_models>`, s
navržené položky se zobrazují jako první.

.. tip::
Vyhledávací pole v záložce „Přidat existující položky“ umožňuje vyhledávat podle
konkrétní položky periodika.

..._usmíření / hromadné platby:

Skládané platby
--------------

:doc:`Sběrná platba <../platební-metody/sběrné-platby>` vám umožňuje seskupit různé platby, abyste usnadnili
usmíření. V záložce „Souhrnné platby“ najdete souhrnné platby pro zákazníky a
prodejci. Podobně jako v záložce „Přidat stávající položky“, je i v záložce „Souhrnné platby“
Má vyhledávací lištu, která vám umožní hledat konkrétní platby.

.._usmíření/ruční operace:

Manuální operace
-----------------

Pokud neexistuje záznam odpovídající vybrané transakci, můžete místo toho
Zaplaťte transakci ručně vybráním správného účtu a částky. Poté dokončete platbu
povinných polí.

.. tip::
Můžete použít možnost „plně zaplaceno“ (:guilabel:`fully paid`) k vyrovnání platby i v případě, že byla provedena jen částečná úhrada.
Při přijetí částečné platby se v části výsledného záznamu objeví nová řádka, která odráží
otevřený zůstatek na účtu pohledávek, který je registrován výchozím nastavením. Můžete si vybrat jiný
účet kliknutím na novou řádku v sekci s výsledky a výběrem
:guilabel:`Záznam o účtu“ pro zaznamenání nevyrovnaného zůstatku.

.. poznámka::
Řádky se tichým způsobem slučují, pokud není vyžadováno smazání, což spouští
kouzelník usmíření.

.. obrázek: usmíření/plně zaplaceno.png
:alt:Klikněte na plně zaplaceno, abyste ručně nastavili fakturu jako úplně zaplacenou.

.._usmíření/tlačítko:

Tlačítka pro připojení k rekonfiguračnímu modelu
----------------------------

Použijte tlačítko „Model slučování“ (reconciliation_models) pro ruční operace, které
často používané. Tyto tlačítka umožňují rychle manuálně vyrovnat bankovní transakce a
Může být také použita v kombinaci s již existujícími položkami.
