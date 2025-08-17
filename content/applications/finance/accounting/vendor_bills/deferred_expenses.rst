=================
Odložené výdaje
=================

Oba jsou náklady, které se nepromítnou do výsledku hned v okamžiku jejich vzniku.
se již staly pro produkty nebo služby, které ještě nebyly přijaty.

Takové náklady jsou pro společnost, která je platí, **aktivem**, protože už zaplatila za produkty a
služby, ale buď ještě neobdržela, nebo ještě neuplatnila. Společnost nemůže o nich hovořit
na současném výsledovce, tedy na výkazu zisku a ztráty, neboť platby budou
účtována v budoucnu.

Tyto budoucí výdaje musí být odloženy na účetnictví společnosti až do okamžiku, kdy se objeví.
může být uznána v okamžiku nebo za stanovené období na výsledovce.

Příklad: řekněme, že platíme 1200 dolarů najednou za jeden rok pojištění. Už teď tedy zaplatíme celou částku
Ale zatím jsme ji nevyužili. Proto vkládáme tuto novou položku do účtu pro předplacené služby.
rozhodnout se uznávat je měsíčně. Každý měsíc po dobu dalších 12 měsíců bude
uznány jako výdaj.

Odoo Accounting řeší odložené výdaje rozložením na více položek, které jsou
Přidáváme postupně.

.. poznámka::
Server kontroluje jednou denně, zda je potřeba nějaký příspěvek publikovat. Může se tedy stát, že bude trvat až 24 hodin, než
Vidíte změnu z „Návrh“ na „Odesláno“.

Konfigurace
=============

Ujistěte se, že výchozí nastavení je správně nakonfigurováno pro vaši firmu. Chcete-li tak učinit, přejděte na
V nabídce „Účetnictví“ -> „Konfigurace“ -> „Nastavení“ jsou k dispozici následující možnosti:

Journal
Záznamy o odkladu se zaznamenávají do tohoto deníku.
Odložená položka
Výdaje jsou odloženy na účtu Základní aktiva až do chvíle, než je uznáme.
Vytvořit záznamy
Výchozí nastavení Odoo je takové, že automaticky vytváří faktury dodavatelů (<vendor_bills/deferred/generate_on_validation>).
přesunout položky odložené na úhradu v případě, že zadáte fakturu dodavateli.
:ref:`generovat je ručně <vendor_bills/deferred/generate_manually>“ volbou „Generovat manuálně“.
:guilabel:„Ručně a seskupené“ místo toho.
Podle
Předpokládejme, že úhrada za služby v hodnotě 1200 dolarů musí být odložena na dobu 12 měsíců.

  - Možnost Months vám každý měsíc účtuje 100 dolarů, které se přepočítávají na počet dní v
tento měsíc (například 50 USD v prvním měsíci, pokud je nastaven datum zahájení na 15.
měsíc.

  - Volba „Plný měsíc“ považuje každý začínající měsíc za plný (např. 100 USD za
první měsíc, i když je nastaven datum zahájení na 15. den v měsíci; tím se myslí
s možností Full Months je v prvním částečném měsíci uznán celý 100 $,
odstraněním potřeby 13. měsíce, aby se uznal zbytek, jak tomu je v případě použití
volbu `Měsíce`.

  - Možnost „Dny“ bere v úvahu různé částky podle počtu dní.
každý měsíc (např. ~ 102 $ v lednu a ~ 92 $ v únoru).

.. _faktury dodavatele/odložené/vytvořit při ověření:

Vytvořit odkladné položky při kontrole
=======================================

.. tip::
Zkontrolujte, zda jsou viditelné pole „Datum začátku“ a „Datum ukončení“.
:guilabel:`Dodací lístky“ záložce. Většinou by měl být datum „Start Date“ stejné
měsíc jako datum faktury. Příspěvky na odložené výdaje se zadávají od data faktury a
Výsledky jsou v zprávě uvedeny podle toho, jak byly získány.

Pro každou položku faktury, která má být odložena, uveďte datum začátku a konec odkladu
době.

Pokud je pole „Vytvořit položky“ nastavené na „Na ověření faktury/účtu“, Odoo
automaticky vytváří odložení plateb při platbě. Klikněte na
Klikněte na tlačítko „Odložené záznamy“ v horní liště nabídek.

Jedna položka s datem stejným jako den účtování faktury přesouvá částky z
účet na účet odložený. Ostatní položky jsou položky k odložení a měsíčně
Po měsíci převedeme částky faktur z účtu odložených položek na účet nákladů k uznání.
na náklady.

.. příklad::
Můžete odložit účet za leden v hodnotě 1200 dolarů o 12 měsíců, pokud zadáte datum začátku 01/01/2023
a datem ukončení 31. prosince 2023. V polovině srpna je náklad ve výši 800 dolarů považován za výdaj.
Výše příspěvku na důchodové pojištění se zvyšuje o 15 % a částka 400 USD zůstává na účtu pro odložené platby.

Reportáž
=========

Zpráva o odložených výdajích poskytuje přehled o všech potřebných odkladech v každém účtu.
Pro přístup k ní se přesuňte do položky: „Účetnictví“ - „Zprávy“ - „Odložené výdaje“.

Pro zobrazení položek účtu klikněte na název účtu a poté na „Journal
Položky.

.. obrázek: odložené výdaje/zpráva o odložených výdajích.png
:alt:Zpráva o odložených výdajích

.. poznámka::
Jen faktury, jejichž účetní datum je před koncem období hlášení
Jsou zohledňovány.

.. _faktury dodavatelů/odložené/vytvořit ručně:

Vytvořte skupinové odložené vstupy ručně
==========================================

Pokud máte mnoho odložených příjmů a chcete snížit počet vytvářených účetních záznamů,
může vytvářet odložené záznamy ručně. Pro tento účel nastavte pole
Nastavení na „Manuálně a Skupinově“. Poté Odoo sčítá odložené částky v
jednorázový vstup.

Na konci každého měsíce přejděte do zprávy Oddalované výdaje a klikněte na
Tlačítko „Vytvořit položky“. To vytvoří dvě odložená příjmových účetních záznamy:

- Jeden konec měsíce, který sčítá všechny odložené částky pro každý účet.
z tohoto měsíce. To znamená, že na konci této doby je část odložených výdajů
byli uznáni.
- Obrat tohoto vytvořeného záznamu, datovaný na následující den (tj. první den
a příští měsíc zrušit předchozí vstup.

.. příklad::

Je dvě návrhy zákona:

   - Faktura A: Odložení částky 1200 USD od 01. ledna 2023 do 31. prosince 2023
   - Bill B: Deferované částky ve výši 600 USD od 01.01.2023 do 31.12.2023

V lednu
Na konci ledna po kliknutí na tlačítko „Vytvořit záznamy“
Ve výpisu je následujících záznamů:

      - Výpis z účtu č. 1 ze dne 31. ledna:

        - Řádek 1: Účet za výdaje -1200 -600 = **-1800** (součet obou faktur)
        - Řádek 2: Účet výdajů 100 + 50 = **150** (rozpoznání faktury A a faktury B za 1/12)
        - Řádek 3: Zpožděný účet 1800 – 150 = **1650** (zůstatek, který se ještě zpozdí později
na)

      - Dne 1. února zápis číslo 2 s opakem předchozího záznamu:

        - Částka 1800
        - Dohoda o odkladu platby -150
        - Řádek 3: Účet nákladů -1650

V únoru
Na konci února po kliknutí na tlačítko „Vytvořit záznamy“
Ve výpisu je následujících záznamů:

      - Výpis z účtu č. 1 ze dne 28. února:

        - Řádek 1: Účet za výdaje -1200 -600 = **-1800** (součet obou faktur)
        - Řádek 2: Účet výdajů 200 + 100 = **300** (poznání 2/12 faktury A a faktury B)
        - Řádek 3: Zpožděný účet 1800 – 300 = **1500** (zůstatek, který bude odložen později)
na)

      - Dne 1. března zápis číslo 2, který zrušil předchozí záznam.

Od března do října
Stejný výpočet se provádí pro každý měsíc až do října.

V listopadu
Na konci listopadu po stisknutí tlačítka :guilabel:`Vytvořit záznamy`,
Ve výpisu je následujících záznamů:

      - Výpis z účtu č. 1 ze dne 30. listopadu:

        - Řádek 1: Účet za výdaje -1200 -600 = **-1800** (součet obou faktur)
        - Linie 2: Účet výdajů 1100 + 550 = **1650** (uznávání faktury A a faktury B v poměru 11/12)
        - Řádek 3: Zpožděný účet 1800 – 1650 = **150** (zůstatek, který se zpozdí později)
na)

      - Dne 1. prosince zápis číslo 2, který zrušil předchozí záznam.

V prosinci
V prosinci se nic nevygeneruje. Ve skutečnosti pokud provedeme výpočet pro
V prosinci budeme mít nulový zůstatek k odložení.

Ve výsledku
Pokud bychom vše sčítali, dostaneme se na:

      - zákon A a zákon B
      - dvě položky (jedna pro odložení a jedna pro obnovení) za každý měsíc od ledna do
Listopad

Protože v prosinci je účetní období ukončeno, tak se účtuje pouze jednou položka A a B.
Přestože vznikly všechny záznamy díky obratu.
