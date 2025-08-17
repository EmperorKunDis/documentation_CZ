============
Pracoviště
============

Centra práce jsou místem, kde se zpracovávají pracovní příkazy pro výrobu a lze je použít k sledování
náklady, vytvářet harmonogramy, plánovat kapacitu, organizovat vybavení a sledovat efektivnost. Specifikace práce
centrum je vyžadováno při definování pracovního příkazu v záložce Operace na lístku materiálů
pro produkt.

.. důležité::
Pracovní střediska se zobrazí pouze v případě zapnutého nastavení „Zadání práce“. Chcete-li tak učinit, přejděte na
:menuvolba:`Výrobní aplikace --> Konfigurace --> Nastavení“, pak zaškrtněte :guilabel:`Práci
Zaškrtávací políčko „Poptávky“. Poptávky lze spravovat v aplikaci Manufacturing vybráním
:menu:"Úkoly --> Úkoly".

.. viz také:
:doc:`../základní nastavení/fakturační konfigurace`

Konfigurace pracovního centra
=========================

... výrobu/správu/používání pracovních center/WC-Setup:

Vytvořte nové pracoviště
------------------------

V aplikaci Manufacturing vyberte: menu selection: Konfigurace -> Stroje a klikněte na
Tlačítko „Nový“ pro otevření nového formuláře pracovního centra.

.. obrázek: používání pracovních center/pracovní centrum - formulář.png
:alt:Příklad plně konfigurovaného pracoviště.

- :guilabel:`Název pracovního centra“: štítek pro pracovní centrum používaný k výběru na objednávce nebo
na přehledových panelech
- :guilabel:`Štítek“: znovu použitelné štítky, které lze použít k třídění pracovišť v seznamovém zobrazení
- :guilabel:`Alternativní pracoviště“: na které se má provést práce, pokud je tato práce plánována
Není k dispozici
- :guilabel:`Kód“: referenční ID pracovního centra, které se zobrazí v seznamu
- :guilabel:`Provozní doba“: hodiny, kdy je možné využívat pracovní centrum během týdne

... výrobu/řízení/používání pracovišť/směny:

Pracovní doba
~~~~~~~~~~~~~

Časová osa definuje, kdy by měl pracovat určitý pracovní středisko podle jednodenního nebo dvoutýdenního plánu.
Tyto hodiny také tvoří základ pro výpočet celkové efektivity zařízení (OEE).

.. poznámka::
Výchozí nastavení používá Odoo pracovní dobu „Standard 40 hodin týdně“, která očekává, že pracoviště budou
Provoz je mezi 8:00 a 17:00 v pondělí až pátek.

Změnit pracovní dobu je možné přetažením aktuální hodnoty „Pracovní doba“ a kliknutím na
:icon:`fa-arrow-right` (:guilabel:`Vnitřní odkaz“) ikonu pro otevření formuláře s pracovní dobou.

.. obrázek:: pouzivani_pracovnich_centru/casova_praha.png
:alt:Pracovní doba je stanovena na 40 hodin týdně.

Vytvořit nový rozvrh pracovní doby, klikněte na tlačítko „Nový“ a přidejte mu název.
Zde můžete upravit jakékoli hodnoty „Čas od“ nebo „Čas do“, abyste zadali časový rozsah. Odstraňte
kliknutím na ikonu „odpadkový koš“ (trash) v pravém horním rohu obrazovky.
Klikněte na „Přidat řádek“ v dolní části seznamu.

.. viz také:
   - :doc:`../reporting/oee`
   - :doc:`../workflows/work_center_time_off`

Určit produktivitu a umožnit zaměstnancům
------------------------------------------------

Karta „Obecné informace“ na formuláři pracovního centra umožňuje stanovit produktivní cíle.
přiděleny do pracovního střediska. Tyto hodnoty slouží jako základ pro výpočet potenciálu
době, kdy je pracoviště využíváno a náklady na jeho provoz.

.. obrázek: používání pracovních center/obecné informace o pracovním centru.png
:alt:Informační záložka pracovního centra.

- :guilabel:`Účinnost času“: násobek, který ukazuje, jak používání tohoto pracoviště ovlivňuje normální rychlost
způsobu provedení pracovního úkolu

...... příklad::
Pokud pracoviště má zastaralé vybavení a výrobní objednávky trvají dvojnásobně déle, pak je „Čas“
Efektivita by byla „50,00 %“.

- :guilabel:`Kapacita“: počet produktů, které lze zpracovat na pracovišti
současně

- :guilabel:`OEE Target“: cíl efektivity na pracovišti

...... příklad::
Pokud je pracoviště k dispozici 8 hodin denně, ale očekává se, že bude používáno jen 7
hodin denně, pak by OEE bylo 87,5 %.

......viz také:
:doc:`../reporting/oee`

- :guilabel:`Čas na nastavení“: čas potřebný k zahájení práce na objednávce
- :guilabel:`Čas na úklid“: doba potřebná k odstranění nepořádku po ukončení pracovního příkazu
- :guilabel:`Náklady na hodinu“: provozní náklady tohoto pracoviště.
Hodnota je určena pro odhad průměrného nákladu na zaměstnance.

...... viz také:
:doc:`../základní_nastavení/mo_náklady`

- :guilabel:`Povolené zaměstnance“: zaměstnanci, kteří mohou pracovat na pracovišti. Pokud je prázdné
Všichni zaměstnanci jsou povoleni.

... příklad::
Pokud je na pracovišti vyžadována certifikace k provozu zařízení, pak:
Pracovníci mohou uvést pouze ty zaměstnance, kteří mají certifikaci.

Snížení výrobních kapacit
-------------------------

Nastavení kapacity na pracovišti vytváří výchozí hodnotu počtu jednotek, které mohou být
v jednom čase v pracovním centru. Specifikovat, že pracovní centrum může produkovat různé
množství různých výrobků, vyberte záložku „Specifické kapacity“.

.. obrázek: pouzivani_centra_prace/kapacity_centra_prace.png
:alt: Forma pracoviště s různými kapacitami pro různé výrobky.

..tip:
Specifikovat výrobní kapacity v různých měřítkách od počtu jednotek umožňuje
*Jednotky měření* jsou součástí aplikace **Sklad**.

.. viz také:
:doc:`../../údržba/přidat nové vybavení

.. _workcenter_iot:

Propojit zařízení internetu věcí
---------------------

Karta „IoT spouštěče“ umožňuje integraci zařízení IoT.
s pracovním centrem:

- :guilabel:`Zařízení“: určuje zařízení IoT, které má být spuštěno
- :guilabel:`Klíč zařízení“: bezpečnostní klíč pro zařízení
- :guilabel:`Akce“: akce spuštěná na zařízení IoT

.. obrázek: pouzivani_centra_prace/centrum_práce_iot.png
:alt:Karta spouštěcích událostí v pracovním centru.

Přiřazování zařízení k pracovištím
===================================

Aplikace **Údržba** umožňuje přidat konkrétní zařízení do pracoviště.
sledovat své náklady a produktivitu. Přidává také :guilabel:`Zařízení`.
:guilabel:`Údržba“ karty do pracovního centra, které se používá pro vyjmenování zařízení a plánování údržby
údržbové činnosti.

.. viz také:
:doc:`../../údržba/přidat nové vybavení

Nastavit zařízení
-------------------

Pomocí záložky „Vybavení“ lze konkrétnímu vybavení přiřadit
do pracovního centra. Pro každý přidaný kus vybavení se zobrazí následující informace:

- :guilabel:`Název zařízení“: název kusu
- :guilabel:`Servisní technik“: osoba odpovědná za údržbu zařízení
- :guilabel:`Kategorie vybavení“: kategorii, do které patří vybavení
- :guilabel:`MTBF“: doba mezi poruchami; průměrná doba, po kterou bude kus zařízení
operovat, dokud nezpůsobíte havárii
- :guilabel:`MTTR‘: doba potřebná k obnovení funkčnosti zařízení; průměrný čas, který uplyne od chvíle, kdy se zařízení stane nefunkční
je plně funkční
- :guilabel:`Předpokládaný čas dalšího selhání“: odhad, kdy dojde k dalšímu selhání

.. obrázek: pouzivani_centra/vybaveni_centra.png
:alt:Karta vybavení pracovního centra.

.. poznámka::
:guilabel:`MTBF“, :guilabel:`MTTR“ a „Odhadovaný další problém“ jsou všechny vypočítané
automaticky na základě dat o minulých neúspěších, pokud existují.

Plánování pracovního centra
====================

Aktuálně plánované objednávky lze zobrazit po přístupu na:
Plánování --> Plánování pracovištěm.

.. obrázek:: pouzivani_centra_prace/planovani_centra_prace.png
:alt:Grafické zobrazení plánu s dvěma pracovišti montáže.

Různé pohledy ukazují, kolik pracovních příkazů je naplánováno a kolik minut každou hodinu.
výrobní centrum je v provozu a termíny a časy práce
objednávky. Časy a plánovaná pracoviště lze změnit kliknutím na přístup k jednotlivým pracovním úkolům.
pořádku.

Výkonnost pracovního centra
=======================

Výkon pro jednotlivé pracoviště lze zobrazit výběrem:menuselection:Konfigurace
→Střediska práce, kliknutím na středisko práce se zobrazí metriky v chytrých tlačítkách nahoře
formátu.

.. obrázek:: pouzivani_centra_prace/centrum_prace_smajlici.png
:alt: Formulář pracovního centra s chytrými tlačítky, které zobrazují výkonnostní metriky.

- :guilabel:`OEE“: celková efektivita vybavení, procento času, kdy je pracoviště
Využila svých pracovních hodin efektivně.

...... viz také:
      - :doc:`../reporting/oee`

- :guilabel:`Ztracený čas“: množství ztraceného času v důsledku výpadků
- :guilabel:`Náklady na dokončení práce“: čas, který bude potřeba k dokončení aktuální pracovní zátěže
- :guilabel:„Výkon“: skutečná doba pracovní doby, vyjádřená jako procento očekávané
délka

Příklad použití: měření výkonu za směnu pomocí pracovišť
===========================================================

Střediska práce podporují definované pracovní hodiny, které umožňují sledovat produktivitu zaměstnanců na směny.
Pro konfiguraci sledování podle směn vytvořte pracovní dobu pro každou ze směn a poté duplikujte
verze každé práce pro každou směnu. S touto konfigurací lze porovnat produktivitu jednotlivých směn.
může být proveden pomocí kterékoliv z dostupných nástrojů pro reportování:

Práce na více směnách
---------------------------------

Pro vytvoření pracovních hodin pro více směn otevřete formulář pracoviště a zadejte do pole „Práce“
Zadejte hodiny do pole a klikněte na ikonu „pravý směr“ (:guilabel:„Vnitřní odkaz“), poté
Tlačítko „Nový“ k vytvoření nové sady hodin pro druhou směnu.

Příklad:
Výrobce má dvě směny: denní od 5 do 13 hodin a noční od 13 do 21 hodiny.
Začněte s jakýmkoli existujícím pracovištěm a upravte stávající směny tak, aby odpovídaly dennímu provozu.

.... obrázek: používání pracovišť/příklad přesunutí dne.png
:alt: Denní směna

Jakmile je denní směna uložena, klikněte na ikonu „fa-cog“ a vyberte
:guilabel:`Duplikát“. Přejmenujte tento nový rozvrh na „Noční směnu“ a změňte každé :guilabel:`Pracovní
od 8 do 13 hodin a od 17 do 21 hodiny.

....... obrázek:: používání pracovních center/příklad-směna-noční.png
:alt:Pracovní doba noční směny

Práce v několika směnách
--------------------------------

Vytvoření duplicitních pracovišť je možné provést návratem do pohledu na pracoviště.
:menu „Nastavení“ --> „Střediska“ a duplikací každého střediska, které je
používané oběma směnami, a to buď přímo na pracovních centrech nebo z pohledu seznamu.

..tip:
Klikněte na ikonu „fa-check-square-o“ pro přímé duplikování pracovních center z pohledu seznamu.
:guilabel:`(zaškrtávací políčko)` se zobrazí nad seznamem položek a vyberte všechny. Pak klikněte
:ikonka:`fa-cog` tlačítko „Akce“ v horní části seznamu a vyberte
:guilabel:`Duplikát“.

Příklad:
Výrobce má dvě pracoviště, „Sestavovací linka 1“ a „Sestavovací linka 2“, a dva pracující
hours, Day Shift a Night Shift.

... obrázek:: pouzivani-pracovnich-center/pracovni-centra-s-smeny.png
:alt:Zaměstnanci pracují na směny denní a noční.

Pro vytvoření verzí „Linky 1“ a „Linky 2“ pro každou směnu je třeba každý z nich duplikovat.
výrobní centra. Vyberte první výrobní centrum a přidejte název směny do názvu tohoto výrobního centra
a přiřadit mu odpovídající pracovní dobu. Volitelně lze každému pracovišti přidělit svou vlastní pracovní dobu.
jako protisměrný posunový partner, aby se zajistilo, že výrobní objednávky budou
Mohou být přiřazeny oběma. Štítky také pomáhají vytvářet vizuální rozdíl mezi každým směnným provozem.

.......tip::
Použijte znak :icon:`oi-chevron-left`.
:guilabel:„(levý směr)“ a :icon:„oi-chevron-right“ :guilabel:„(pravý směr)“ tlačítka v
v horním levém rohu, aby se přesunul na další položku v seznamu bez návratu do zobrazení seznamu.

Zprávy porovnávající různé směny
----------------------------------

S více pracovišti vytvořenými pro zobrazení směn se nyní reporty řadí podle pracoviště.
porovnat směny. Toto lze použít k porovnání počtu pracovních příkazů, které jsou přiřazeny každé
přesunutí, OEE nebo skutečný čas potřebný každé směně k výrobě produktu.

Příklad:
Vytvořen byl report, který porovnává efektivitu času dvou směn produkujících stejný výrobek.
v jednom pracovišti.

.... obrázek:: používání pracovních center/délka odchylky od plánu.png
:alt:Graf s dvěma pracovišti, kde je odchylka od plánované doby -6,50 a 15,00

Pro vytvoření této zprávy přejděte na: „Zprávy – Pracovní příkazy“ a klikněte na odstranění.
:ikonka: `fa-filter` filtrovat podle stavu
Klikněte na ikonu „fa-x“ vpravo a poté klikněte na
tlačítko „Měření“ a vyberte „Doba odchylky (%)“.

V tomto případě pracovní směna denního provozu v průměru trvala déle než očekávaný čas k výrobě produktů.
(-6,50 %) zatímco noční směna trvala méně než očekávaný čas (15 %).

