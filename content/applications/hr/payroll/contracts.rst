=========
Smlouvy
=========

Každý zaměstnanec v Odoo musí mít platnou smlouvu, aby byl zaplacen.
upřesňuje podmínky pracovního místa zaměstnance, jeho odměnu, pracovní dobu a případně další
další podrobnosti o jejich postavení.

.. důležité::
Smluvní dokumenty (PDF soubory) jsou nahrávány a organizovány pomocí aplikace *Dokumenty*.
podepsané aplikací Sign*. Ujistěte se, že máte tyto aplikace nainstalované pro odesílání a podepisování
smlouvy. Prosím, obraťte se na :doc:`../../produktivita/dokumenty`.
:doc:`../produktivita/znaky` dokumentace.

Zobrazit pracovní smlouvy můžete v aplikaci „Mzdy“ - „Smlouvy“ - „Smlouvy“.
v horním menu. Všechny pracovní smlouvy a jejich aktuální stav jsou zobrazeny v
výpisem. Výpis zobrazuje běžící smlouvy, smlouvy vyžadující akci a
vypršené smlouvy a zrušené smlouvy.

.. obrázek: smlouvy/smluvni-prehled.png
:align:center
:alt: Zobrazení panelu smluv, které zobrazuje běžící smlouvy a smlouvy s problémy.

.. poznámka::
Seznam smluv v aplikaci Mzdy odpovídá seznamu smluv v
Aplikace pro zaměstnance.

.. _mzdy/nový kontrakt:

Pro výplatu zaměstnanci je nutný aktivní pracovní poměr. Pokud je potřeba nová smlouva,
klikněte na tlačítko „Vytvořit“ v přehledu smluv. Objeví se formulář pro vytváření smlouvy.
kde lze informace zadat.

Nový smluvní vzor
-----------------

... _mzdy/gen-info:

Oddělení obecných informací
---------------------------

- :guilabel:`Kontaktní odkaz“: zadejte jméno nebo titul kontraktu, například „John Smith
Smlouva. Toto pole je **povinné**.
- :guilabel:`Zaměstnanec“: vyberte zaměstnance, na něhož se smlouva vztahuje.
- :guilabel:`Datum zahájení smlouvy“: datum, kdy začíná platit smlouva. Chcete-li vybrat datum, klikněte na
položky rozbalovací nabídky, přejděte na správný měsíc a rok pomocí ikon „< >“
Pak klikněte na požadovaný den. Toto pole je **povinné**.
- :guilabel:`Datum ukončení smlouvy“: pokud má smlouva konkrétní datum ukončení, vyberte z roletky.
Navigujte na správný měsíc a rok pomocí ikon „< > (šipka)“ a pak klikněte na
Požadovaný termín.
- :guilabel:'Rozvrh směn': vyberte jeden z rozvrhů směn ze seznamu.
pole je **povinné**.

.....tip:
V rozevíracím seznamu „Rozvrh práce“ jsou zobrazeny všechny pracovní rozvrhy pro dané zařízení.
vybrané společnosti. Chcete-li tento seznam upravit nebo doplnit, přejděte na:
Konfigurace --> Nastavení pracovních plánů. Klikněte na „Nový“ a vytvořte nový pracovní plán.
nebo klikněte na existující pracovní plán a proveďte úpravy.

- „Zdroj vstupu do práce“: vyberte, jak se generují „vstupy do práce“ (work_entries).
Toto pole je **povinné**. Klikněte na tlačítko vedle požadovaného výběru. Možnosti jsou:

  - :guilabel:`Plán práce“: pracovní záznamy se generují na základě vybraného
:guilabel:`Rozvrh práce“.
  - :guilabel:`Přítomnost“: pracovní záznamy jsou vytvářeny na základě záznamů o přítomnosti zaměstnance
aplikace *Přítomnosti*. (Tato vyžaduje aplikaci *Přítomnosti*.)
  - :guilabel:`Plánování“: pracovní vstupy jsou generovány na základě plánovaného rozvrhu zaměstnance
od aplikace Plánování (vyžaduje aplikaci Plánování).

- :guilabel:`Typ struktury mzdy“: vyberte jeden z typů struktury mzdy ze seznamu
menu. Výchozí typy struktury mzdy jsou :guilabel:`Zaměstnanec“ nebo :guilabel:`Dělník“.
Pokud je potřeba, lze vytvořit nový typ struktury mzdy:
- Vyberte oddělení, na které se smlouva vztahuje z roletky.
- :guilabel:`Pozice v zaměstnání“: vyberte konkrétní pozici, na kterou se smlouva vztahuje z
rozbalovací nabídka.

.. poznámka::
Pokud je k vybrané pozici nastaven šablonový pracovní smlouvu, který má určitý
:guilabel:`Typ struktury mzdy“, typ struktury mzdy se změní na
spojené s touto pozicí.

- :guilabel:`Mzda na mzdovém listu“: zadejte měsíční plat zaměstnance.
- Vyberte buď „Plný úvazek“, nebo „Dohodou“.
Vyberte možnost „Sezónní“, „Plný úvazek“ nebo „Částečný úvazek“.

.. obrázek: smlouvy/povinné-údaje.png
:align:center
:alt: Nový smluvní vzor pro nové smlouvy, se vyplňovacími poli
vyznačené červeně.

.. tip::
V seznamovém poli „Rozvrh práce“ jsou zobrazeny všechny pracovní doby pro vybraný den.
:guilabel:`Společnost“. Chcete-li upravit nebo přidat do seznamu, přejděte na :menuselection:`Mzdová aplikace -->
Konfigurace --> Nastavení pracovní doby, buď vytvořte novou pracovní dobu nebo klikněte na
pracovní dobu, která již existuje, pak upravte kliknutím na tlačítko :guilabel:`Upravit`.

- „Roková cena (reálná)“: tento prvek se automaticky aktualizuje po „Časovém harmonogramu“.
Do políčka „Mzda“ a „Guilabel“ se zadává částka, která je celkovou roční cenou za zaměstnance.
zaměstnavatele. Tento údaj lze měnit. Pokud je však tento údaj změněn, pole :guilabel:`Mzda
aktualizace podle toho. Zajistěte aktualizaci obou polí „Mzda“ a „Roční náklady (reálné)“.
Pokud tento prvek upravíte, bude se vám zobrazovat správně.
- „Měsíční náklady (reálné)“: tento prvek se automaticky aktualizuje po „Plánu
Do políčka „Mzda“ a „Guilabel“ se zadává tento příjem, který je celkovou měsíční částkou za
zaměstnavatele. Toto pole nelze měnit a je vypočítáváno na základě :guilabel:`Rokové
Cena (Reál. CZK).

.. obrázek: smlouvy/informace o platu.png
:synchronizace: střed
:alt:Doplňkové záložky pro novou smlouvu.

Karta Podrobnosti o smlouvě
--------------------

Karta „Podrobnosti smlouvy“ umožňuje přidání nebo úpravu smlouvy spolu s
Určuje, který šablonu použít při vytváření nové smlouvy. Tato pole **musí být vyplněna**
aby vytvořil novou smlouvu.

.. důležité::
Chcete-li přistupovat k různým polím šablony smlouvy v záložce „Podrobnosti o smlouvě“,
Modul *Salary Configurator* (`hr_contract_salary`) **musí být** nainstalován.
<obecné/instalace>.

Když je nainstalován modul Mzdový konfigurátor, tak moduly Mzdový konfigurátor – Dovolená a
*Moduly Salary Configurator - Mzdy* se také instalují.

Jakmile jsou moduly nainstalovány, databáze se vrátí na hlavní panel.

- :guilabel:Šablona smlouvy“: vyberte již existující šablonu smlouvy ze seznamu.
Výchozí smluvní šablony se obvykle vytváří pomocí konfiguračního menu a ukládají do
*Dokumenty*.

Značková část
~~~~~~~~~~~~

- :guilabel:`Odpovědný za HR“: vyberte osobu, která je odpovědná za ověření smlouvy
rozbalovací nabídka. Toto pole je povinné.
- :guilabel:`Nový šablonový dokument smlouvy“: vyberte ze seznamu smlouvu, kterou chcete
Tyto dokumenty jsou uloženy v aplikaci Sign.
- Vyberte smlouvu z rozevírací nabídky.
zaměstnanec má již existující smlouvu, která vyžaduje aktualizaci. Tyto dokumenty jsou uloženy v aplikaci Sign
aplikace.

.. důležité::
`HR odpovědný za pracovníky`, „Nový vzor smlouvy“ a
:guilabel:`Smluvní aktualizační dokumentový šablona“ pole jsou viditelná pouze v aplikaci *Sign*.
je nainstalován spolu s moduly „hr_contract_salary“ a „hr_contract_salary_payroll“.
<../../obecné/aplikace_moduly>. Aplikace Sign je místo, kde jsou uloženy šablony smluv.
Tato žádost je nutná pro podepsání smlouvy zaměstnancem.

Účetní oddělení
~~~~~~~~~~~~~~~~~~

- :guilabel:`Analytický účet“: vyberte z roletky účet, který se smlouvou souvisí.
Je doporučeno ověřit si u účetního oddělení, aby bylo zvoleno správné konto.

Část „Na částečný úvazek“
~~~~~~~~~~~~~~~~~

- Zatrhněte políčko „Částečný úvazek“, pokud zaměstnanec pracuje částečně.
Ve výsledcích se objevují pole:

  - :guilabel:`% (Procento)‘: zadejte procenta času, který zaměstnanec pracuje v porovnání s
plný úvazek.
  - :guilabel:`Standardní kalendář“: vyberte pracovní hodiny, které běžný plný úvazek používá
z nabídky.
  - :guilabel:`Typ účtování práce na částečný úvazek“: vyberte typ účtování práce na částečný úvazek, který vytváří rovnováhu
plný úvazek.

... příklad::
Pokud zaměstnanec pracuje na plný úvazek 40 hodin týdně a zaměstnanec pracuje 20 hodin, zadejte „50“.
:guilabel:`% (Procento)` pole (50 % z 40 hodin = 20 hodin). Zaměstnanec vyrobí dvacet
vstupy do evidence pracovní doby pod položkou „částečný úvazek“ a dalších dvacet (20).
hodin práce v záznamu typu „generální dovolená“, celkem čtyřicet (40).
hodin práce.

Poznámky
~~~~~~~~~~~~~

- :guilabel:`Poznámky“: pole pro zadání poznámek k pracovní smlouvě, které se uloží do budoucna.
referenci.

.. obrázek: smlouvy/podrobnosti_smlouvy.png
:align:center
:alt:Podrobnosti o smlouvě v volitelných záložkách pro novou smlouvu.

Upravit vzor smlouvy
~~~~~~~~~~~~~~~~~~~~~~~~~~

Klikněte na ikonu „Externí odkaz“ (viz obrázek) v závěru buď
„Nová šablona smlouvy“ nebo „Soubor aktualizace smlouvy“ k otevření.
související šablonu smlouvy a pokračujte v provádění požadovaných změn.

Klikněte na tlačítko „Nahrát soubor“ vedle příslušného dokumentu a přejděte do
soubor, pak klikněte na tlačítko „Otevřít“ a vyberte dokument, který chcete přidat do záložky.

Úprava šablon dokumentů
============================

Šablony smluv lze kdykoliv upravit, pokud je třeba změnit něco.

- :guilabel:`Štítky“: vyberte všechny štítky spojené s kontraktem.
- „Správa podepsaných dokumentů“: zde jsou uloženy podpisy. Vyberte
předkonfigurované pracovní prostředí nebo vytvořit nové. Chcete-li vytvořit nový :guilabel:`Podepsaný dokument
Pracovní prostor“, zadejte název pracovního prostoru a poté klikněte na „Vytvořit“ pro přidání nového
pracovní prostor nebo :guilabel:`Vytvořit a upravit“ pro přidání pracovního prostoru a úpravu podrobností o pracovním prostoru.
- :guilabel:`Štítky podepsaných dokumentů“: vyberte nebo vytvořte jakékoli štítky, které jsou spojeny pouze s
smlouva podepsaná, nikoliv původní nepotvrzená smlouva.
- :guilabel:`Přesměrování odkazu“: zadejte přesměrovací odkaz pro zaměstnance, aby se mohl dostat k smlouvě.
Přesměrování odkazu přenese uživatele z jedné adresy URL na jinou. V tomto případě je přesměrováno na
nově aktualizovanou smlouvu, která byla pro ně napsána.
- :guilabel:`Kdo může podepsat“: vyberte buď „Všichni uživatelé“ nebo „Na pozvání“.

  - :guilabel:`Všichni uživatelé“: smlouvu může podepsat kterýkoliv uživatel v organizaci.
  - :guilabel:`Na pozvání“: smlouvu mohou podepsat pouze uživatelé vybraní v tomto poli.

- :guilabel:`Zvaní uživatelé“: vyberte osobu (nebo osoby), které mohou dokument podepsat.
- :guilabel:`Dokument“: připojený dokument lze nahradit kliknutím na :icon:`fa-pencil`.
:guilabel:`(tužka)` ikona. V okně se objeví vyskakovací okno, takže lze zvolit jiný dokument
uložení souboru. Soubor **musí být ve formátu PDF**. K odstranění dokumentu klikněte na ikonku
:guilabel:`(koš)` ikonu.

Jakmile jsou úpravy dokončeny, klikněte na tlačítko „Uložit“. Všechny informace o vybraném
Šablona smlouvy vyplní pole v záložce „Informace o mzdě“.
pokud je to možné, se zobrazí záložka například „Osobní dokumenty“.

Osobní doklady
------------------

Tento záložka se objeví pouze po výběru zaměstnance a ukrývá všechny dokumenty.
jsou spojeny s pracovníkem v jeho osobním záznamu. Do této záložky nelze přidávat dokumenty,
Zobrazuje pouze dokumenty, které jsou již nahrány a spojeny s daným zaměstnancem.

Dokumenty dostupné v této záložce lze stáhnout. Klikněte na ikonu:
:guilabel:`(stáhnout)` ikona vedle dokumentu pro stažení.

Smlouvu podepište.
-----------------

Klikněte na následující tlačítko pro odeslání smlouvy zaměstnanci.

.. obrázek: smlouvy/odeslat-smlouvu.png
:align:center
:alt: Smlouvu zaměstnanci zašlete jedním z tlačítek.

- Kliknutím na tlačítko „Vytvořit nabídku“ se otevře okno s základními informacemi.
informace z kupní smlouvy, stejně jako odkaz na smlouvu při použití platu
konfigurátor. Klikněte na tlačítko „Odeslat“ a odeslat e-mail zaměstnanci, aby mohl být podepsán.
smlouvu.

Na spodní části okna se nachází pole „Datum vypršení platnosti odkazu“. To je časový úsek, který
Nabídka smlouvy je platná po dobu. Výchozí hodnota tohoto pole je 30 dní, ale může být
by měl být upraven.

.. poznámka::
Pro odeslání smlouvy pomocí tlačítka „Vytvořit simulační odkaz“ **musí být**
pole pro podpis v kontraktu ve formátu PDF, který je zasílán zaměstnanci, aby jej mohl podepsat.

- :guilabel:„Žádost o podpis“: kliknutím na tento odkaz se zobrazí okno s e-mailovou adresou
pracovníkovi. Vyberte dokument (například smlouvu, DPA nebo pracovní směrnici o home office).
klikněte na tlačítko „Odeslat“, když je e-mail připravený k odeslání.
bude zaslána.

.. poznámka::
Pro odeslání smlouvy pomocí tlačítka „Vytvořit simulační odkaz“ musí být podepsaná.
pole v kontraktu ve formátu PDF, který je odesílán zaměstnanci, aby jej mohl podepsat.

Příslušenství k mzdě
------------------

Jakékoliv automatické srážky nebo přidělování pro zaměstnance, například platby za výživné a mzdy
Doplňky jsou označovány jako „přídělek“. V této části je uveden všechny tyto
nejsou stanoveny žádné slevy nebo odpočty.

Pro přidání nové slevy nejprve přejděte na: „Mzdy --> Smlouvy --> Mzda
Přílohy“. Následně klikněte na „Vytvořit“ a nová formulářová příloha se načte.

.. obrázek: smlouvy/sražení.png
:align:center
:alt:Příloha s plněním mzdy pro výživné Ronnieho Harta.

Vyplňte následující pole v formuláři:

- :guilabel:`Zaměstnanec“: z rozevírací nabídky vyberte zaměstnance, na kterého se vztahuje příloha mzdy
to.
- :guilabel:`Popis“: zadejte krátký popis pro přílohu mzdy, například „Dítě
„Podpora“ nebo „Příspěvek 529“.
- :guilabel:`Typ přílohy“: Vyberte typ přílohy, kterou chcete vytvořit.
- :guilabel:`Datum zahájení platby“: datum, od kterého se začne připisovat mzda. Vyberte si datum kliknutím na
kliknutím na rozbalovací nabídku, přesunem do správného měsíce a roku pomocí ikonky „fa-chevron-left“
:ikonu „fa-chevron-right“ a následně kliknutím na požadovaný den.
Je **povinný**.
- „Odhadovaný konec“: Toto pole se automaticky vyplní po obou polích
:guilabel:Měsíční částka a celková částka jsou vyplněny.
**neupravitelné**.
- :guilabel:'Dokument': připojte příslušné dokumenty k příloze mzdy. Klikněte na
:guilabel:`Nahrát soubor“ tlačítko, přejděte do požadovaného dokumentu v prohlížeči souborů a poté
Klikněte na tlačítko „Otevřít“ a vyberte dokument, který chcete připojit k formuláři.
dokumentu, klikněte na ikonu „:icon:`fa-pencil`“ :guilabel:`(pencil)` a vyberte jiný dokument.
Pro odstranění dokumentu klikněte na ikonu „koš“ .
- :guilabel:`Měsíční částka“: zadejte částku, která bude každý měsíc odečtena ze mzdy zaměstnance
měsíc pro tento konkrétní příplatek.
- :guilabel:`Celková částka“: zadejte celkovou částku, kterou zaměstnanec platí za přílohu k platu
ještě nebylo dokončeno.
