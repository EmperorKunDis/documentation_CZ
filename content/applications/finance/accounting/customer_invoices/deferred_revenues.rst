=================
Odměny odložené na později
=================

Později vybrané příjmy nebo nevybrané příjmy jsou faktury adresované zákazníkům.
za zboží ještě nedodané nebo služby ještě neposkytnuté.

Společnost je nemůže uvést v aktuální zprávě o výsledcích hospodaření, tedy v účetní závěrce.
Přičemž dodávky a služby budou skutečně poskytnuty v budoucnu.

Tyto budoucí příjmy musí být na účetní bilanci společnosti zařazeny mezi současné závazky
až do chvíle, kdy je lze uznat okamžitě nebo v určeném časovém období na výsledovce.
Prohlášení.

Příkladem může být například společnost, která prodává licenci na software za 1200 dolarů na jeden rok.
fakturovat zákazníkovi, ale nemůže je považovat za uhrazené, protože budoucí měsíce licencování
nebyly dodány. Proto je ukládají na účet odložených příjmů.
je uznávána měsíčně. Každý měsíc po dobu dalších 12 měsíců bude uznáno
Příjmy.

Odoo Accounting vypořádává odložené příjmy rozprostřením do více položek, které jsou zadány
periodicky.

.. poznámka::
Server kontroluje jednou denně, zda je potřeba nějaký příspěvek publikovat. Může se tedy stát, že bude trvat až 24 hodin, než
Vidíte změnu z „Návrh“ na „Odesláno“.

Konfigurace
=============

Ujistěte se, že výchozí nastavení je správně nakonfigurováno pro vaši firmu. Chcete-li tak učinit, přejděte na
V nabídce „Účetnictví“ -> „Konfigurace“ -> „Nastavení“ jsou k dispozici následující možnosti:

Journal
Záznamy o odkladu se zaznamenávají do tohoto deníku.
Zálohované příjmy
Příjmy jsou odloženy na účet závazků v této fázi, dokud nejsou uznány.
Vytvořit záznamy
Výchozí nastavení Odoo je takové, že automaticky vytváří faktury na základě potvrzení objednávky.
přesunout položky odložené na později v okamžiku, kdy zadáte fakturu zákazníkovi.
:ref:`generovat je ručně <faktury/odložené/zadat_ručně>“ volbou „Generovat manuálně“.
:guilabel:„Ručně a seskupené“ místo toho.
Podle
Předpokládejme, že musí být odložena faktura v hodnotě 1200 dolarů na dobu 12 měsíců.

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

... _faktury_pro_zákazníky/odložené/vytvořit při ověření:

Vytvořit odkladné položky při kontrole
=======================================

.. tip::
Zkontrolujte, zda jsou viditelné pole „Datum začátku“ a „Datum ukončení“.
:guilabel:`Dodací lístky“ záložce. Většinou by měl být datum „Start Date“ stejné
měsíc jako datum faktury. Zálohy jsou vystavovány z faktur.
datum a jsou zobrazeny v hlášení podle toho.

Pro každou řádek faktury, která má být odložená, zadejte datum začátku a konec.
odkladné období.

Pokud je pole „Vytvořit položky“ v nastavení nastavené na „Na faktuře/faktuře“,
validace“, když je faktura ověřena, automaticky vytvoří odkladné položky. Klikněte
klikněte na tlačítko „Později“ v seznamu všech položek.

Jedna položka s datem stejným jako datum účetního záznamu přesouvá částky faktury
výdajový účet na účet odložených výdajů. Ostatní položky jsou položkami odložených nákladů, které se měsíčně
Po měsíci převedeme částky faktur z účtu odložených položek na účet příjmů, abychom je uznali.
Příjmy.

.. příklad::
Můžete odložit únorový fakturu v hodnotě 1200 dolarů o 12 měsíců, pokud zadáte datum začátku 01/01/2023
a datem ukončení 31. prosince 2023. V polovině srpna je pak zaznamenáno jako příjem 800 $.
Výše příspěvku na důchodové pojištění se zvyšuje o 15 % a částka 400 USD zůstává na účtu pro odložené platby.

Reportáž
=========

Zpráva o odložených příjmech vytváří přehled potřebných odkladů pro každý účet.
Pro přístup k ní přejděte na: „Účetnictví“ – „Zprávy“ – „Odhadované příjmy“.

Pro zobrazení položek účtu klikněte na název účtu a poté na „Journal
Položky.

.. obrázek: odložené příjmy/odložený příjem report.png
:alt:Zpráva o odložených příjmech

.. poznámka::
Pouze faktury, jejichž účetní datum je před koncem období hlášení
Jsou zohledňovány.

... _faktury_pro_zákazníky/odložené/vytvořit ručně:

Vytvořte skupinové odložené vstupy ručně
==========================================

Pokud máte mnoho odložených příjmů a chcete snížit počet vytvářených účetních záznamů,
může vytvářet odložené záznamy ručně. Pro tento účel nastavte pole
Nastavení na „Manuálně a Skupinově“. Poté Odoo sčítá odložené částky v
jednorázový vstup.

Na konci každého měsíce přejděte do sekce „Účetnictví“ - „Zprávy“ - „Odhadované příjmy“.
Klikněte na tlačítko „Vytvořit záznamy“. To vytvoří dvě odložená oznámení:

- Jeden konec měsíce, který sčítá všechny odložené částky pro každý účet.
z tohoto měsíce. To znamená, že část odloženého příjmu je uznávána na konci tohoto
období.
- Obrat tohoto vytvořeného záznamu, datovaný na následující den (tj. první den
a příští měsíc zrušit předchozí vstup.

.. příklad::
Jsou dva faktury:

   - Faktura A: 1200 dolarů odloženo do 31. prosince 2023 z důvodu splatnosti 1. ledna 2023
   - Faktura B: 600 dolarů odložených do 31. prosince 2023 z důvodu splatnosti 1. ledna 2023

V lednu
Na konci ledna po kliknutí na tlačítko „Vytvořit záznamy“ jsou v seznamu
následujících položek:

      - Výpis z účtu č. 1 ze dne 31. ledna:

        - Řádek 1: Účet nákladů -1200 -600 = **-1800** (součet obou faktur)
        - Řádek 2: Účet 100 + 50 = **150** (uznávání 1/12 faktury A a faktury B)
        - Řádek 3: Zpožděný účet 1800 – 150 = **1650** (zůstatek, který se ještě zpozdí později
na)

      - Dne 1. února zápis číslo 2 s opakem předchozího záznamu:

        - Částka 1800
        - Dohoda o odkladu platby -150
        - Řádek 3: Účet nákladů -1650

V únoru
Na konci února po kliknutí na tlačítko „Vytvořit záznamy“ jsou v seznamu
následujících položek:

      - Výpis z účtu č. 1 ze dne 28. února:

        - Řádek 1: Účet nákladů -1200 -600 = **-1800** (součet obou faktur)
        - Řádek 2: Účet 200 + 100 = **300** (uznávání faktury A a faktury B v poměru 2/12)
        - Řádek 3: Zpožděný účet 1800 – 300 = **1500** (zůstatek, který bude odložen později)
na)

      - Dne 1. března zápis číslo 2, který zrušil předchozí záznam.

Od března do října
Stejný výpočet se provádí pro každý měsíc až do října.

V listopadu
Na konci listopadu po kliknutí na tlačítko „Vytvořit záznamy“ jsou v seznamu
následujících položek:

      - Výpis z účtu č. 1 ze dne 30. listopadu:

        - Řádek 1: Účet nákladů -1200 -600 = **-1800** (součet obou faktur)
        - Řádek 2: Účet 1100 + 550 = **1650** (uznávání 11/12 faktury A a faktury
          B)
        - Řádek 3: Zpožděný účet 1800 – 1650 = **150** (zůstatek, který se zpozdí později)
na)

      - Dne 1. prosince zápis číslo 2, který zrušil předchozí záznam.

V prosinci
V prosinci se nic nevygeneruje. Ve skutečnosti pokud provedeme výpočet pro
V prosinci máme nulový zůstatek k odložení.

Ve výsledku
Pokud bychom vše sčítali, dostaneme se na:

      - faktura A a faktura B
      - dvě položky (jedna pro odložení a jedna pro obnovení) za každý měsíc od ledna do
Listopad

Proto na konci prosince budou faktury A a B plně uznány jako příjem
jen jednou i přes všechny vytvořené záznamy díky obratu.
