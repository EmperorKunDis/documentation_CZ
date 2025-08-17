================
Uzávěrka za rok
================

Závěrka je zásadní pro zachování finanční přesnosti, dodržování předpisů a vytváření
informované rozhodování a zajištění transparentnosti při hlášení.

.. viz též:
:doc:`Daňové přiznání <daňové_přiznání>`

…výroční/účetní období:

Daňové období
============

Výchozí nastavení je na 12 měsíců a konec roku je 31. prosince.
Doba trvání a datum ukončení se mohou lišit v závislosti na kulturních, administrativních a ekonomických faktorech.

Tyto hodnoty lze upravit v menu „Účetnictví – Konfigurace – Nastavení“. V části
V části „Účetní období“ změňte pole „Poslední den“ (pokud je třeba).

Pokud doba trvání přesahuje nebo je kratší než 12 měsíců, zapněte :guilabel:`Daňové období`.
:guilabel:`Uložit“. Vraťte se do části „Účetní období“ a klikněte na :icon:`oi-arrow-right`
„Fiskální roky“. Pak klikněte na „Nový“, zadejte „Název“ a obojí.
:guilabel:`Datum zahájení“ a „Datum ukončení“.

.. poznámka::
Jakmile skončí nastavená fiskální období, Odoo se automaticky vrátí k výchozím obdobím.
při zohlednění hodnoty uvedené v poli :guilabel:`Poslední den`.

...Seznam na konci roku:

Seznam věcí, které je třeba udělat před koncem roku
==================

…v závěru roku/před uzavřením:

Před uzavřením
--------------

Před uzavřením účetního období zkontrolujte všechny položky a aktualizujte je:

- Ujistěte se, že všechny bankovní účty jsou plně :doc:`vyrovnány <../bank/reconciliation> do konce roku.
a potvrďte, že závěrečné knihy rovnováhy odpovídají zůstatku na účtu.
- Zkontrolujte, zda byly vytvořeny všechny faktury pro zákazníky a
a že nejsou žádné návrhy faktur.
- Zkontrolujte, zda byly vytvořeny a potvrzeny všechny faktury dodavatelů (viz vendor_bills).
- Zkontrolujte přesnost všech výdajů a ověřte je.
- Zkontrolujte, zda všechny „přijaté platby“ byly zašifrovány a potvrzeny.
- Zavřete všechny „účty napětí“ (<accounting/bank/suspense>).
- Vyúčtovat všechny položky s :doc:`odpisem <../faktury/majetek> a :doc:`předběžným příjmem
v položce „Způsobilé výnosy“.

...účetní uzávěrka za rok

Uzavření účetního období
---------------------

A na závěr za celý fiskální rok:

- Vygenerujte si zprávu o dani podle návodu v článku :ref:`Zpráva o dani <účetnictví/zprávy/daňová zpráva>
Je správné.
- Srovnejte všechny účty na výkazu zisku a ztrát :ref:`<accounting/reporting/balance-sheet>`

  - Aktualizujte zůstatky na účtech v Odoo podle skutečných zůstatků uvedených na výpisu z účtu.
  - Sjednoťte všechny transakce v hotovostních a bankovních účtech provedením :ref:`úhrad
<účetnictví/zprávy/staré pohledávky> a :ref:`staré závazky
<účetnictví/zprávy/staré faktury>
  - Provést audit všech účtů a plně pochopit všechny transakce a jejich povahu včetně půjček

  - Volitelně můžete platby :ref:`<účetnictví/platby/platby-srovnání>` ověřit, abyste zkontrolovali otevřené
faktury dodavatelů a zákaznických faktur s jejich platbami. Tento krok je volitelný, ale mohl by
pomoci s uzavřením účetního období, pokud jsou vyrovnány všechny nedoplatky a faktury.
Potenciálně může najít chyby nebo nedostatky v systému.

Poté účetní pravděpodobně ověřuje položky rozvahy a záznamy v knize:

  - roční konečné ruční úpravy
  - práce ve výrobě
  - účetní zápisy k odpisu.
  - úvěry
  - daňové odpočty.
  - atd.

Během inventarizace může účetní vytisknout papírové kopie všech položek rozvahy (např.
úvěry, bankovní účty, předplacené služby, daňové přiznání k DPH) srovnávat je s vyrovnávacími položkami
zaznamenané v Odoo.

.. tip::
V rámci této operace je nutné nastavit datum „Zamknout vše“ (datum uzavření) na
poslední den předcházejícího účetního období je dobrou praxí. To zajistí, že se v knize
Do účetních záznamů s datem vytvoření nebo změny na nebo po dni uzavírání se již nelze vkládat ani měnit.
audit. Uživatelé s právy správce mohou vytvářet a upravovat záznamy, pokud
Výjimka je nastavena.

...datum uzavření a uzamčení všeho:

Zamkněte všechny datumy
~~~~~~~~~~~~~~~~~~~~

Určení data uzamčení zabraňuje jakýmkoliv změnám v zápiscích, které mají účetní datum.
nebo před datem uzamčení. Také zabraňuje vkládání nových záznamů s účetním datem na nebo před
datum uzamčení. V takovém případě je systém automaticky nastaven na den po uzavření
datum uzamčení.

Chcete-li nastavit datum uzamčení všeho, přejděte na záložku „Účetnictví“ - „Účetnictví“ - „Zamknout“.
Datum. V okně „Záznamy v deníku zamykání“ nastavte datum a
:guilabel:`Uložit“.

.. poznámka::
Uživatelé s přístupovými právy pro aplikaci Účetnictví mohou vytvářet výjimky.
Postupujte takto:

   #Po nastavení data „Zamknout vše“ znovu otevřete „Záznamy zamykání“.
Odebrat záznamy z okna „Vstup“ a odstranit datum „Zamknout vše“.
   #V záložce „Výjimka“ vyberte, zda se tato výjimka má nastavit pro vás.
(aktuální uživatel) nebo :guilabel:`pro všechny“ a jak dlouho by mělo trvat.
   #Příčinu výjimky lze doplnit.
   #Všechny tyto informace jsou zaznamenány v chatu společnosti.
</obecne/firmy/>.

.. tip::
Chcete-li po uložení odstranit datum „Zamknout vše“, nastavte výjimku
použít :guilabel:'pro všechny' a nastavit dobu platnosti na :guilabel:'navěky'.

…výsledky za uplynulé období/za aktuální rok:

Příjmy za letošní rok
~~~~~~~~~~~~~~~~~~~~~~~

Odoo používá jedinečný typ účtu nazvaný „výnosy za letošní rok“, který zobrazuje rozdíl
mezi příjmovými a výdajovými účty.

.. poznámka::
V účetní osnově může být pouze jeden účet tohoto typu. Výchozí je 999999
účet s názvem :guilabel:`Nedotované zisky a ztráty“.

Pro přidělení příjmů za letošní rok vytvořte nový položku s datem nastaveným na konec
fiskálního roku je možné je zahrnout do jakéhokoliv účtu vlastního kapitálu.

Pak ověřte, zda je na účetní výkazu za letošek správně uvedeno nulové číslo.
vyrovnání. Pokud ano, můžete nastavit datum „hard lock“ na poslední den fiskálního roku
:menuselection:`Účetnictví --> Účetnictví --> Zámek dat“.

.. tip::
pole „Datum zablokování“ je nevratné a slouží k zajištění dat.
nepřenositelnost, která je nutná pro splnění účetních předpisů v některých zemích. Pokud takové
Plnění povinností není aplikovatelné, v takovém případě nemusí být nutné nastavit tento prvek. Pokud je však požadováno,
Datum by se mělo nastavit až poté, co bude zkontrolováno a ověřeno, že je správné. **Není možné jej změnit nebo
převedeny na hodnotu false, bez ohledu na oprávnění.
