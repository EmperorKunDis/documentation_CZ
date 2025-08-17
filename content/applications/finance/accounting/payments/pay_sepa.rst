=============
Platba SEPA
=============

SEPA je iniciativa Evropské unie pro integraci plateb, která má za cíl
usnadňuje převody mezi bankami v eurech. SEPA umožňuje odesílat platební příkazy do
banka automatizovat převody peněz mezi bankami.

SEPA podporují banky všech členských států Evropské unie a také:

EFTA země:

- Island
- Lichtenštejnsko
- Norsko
- Švýcarsko.

Mimo země EHP/Evropského hospodářského prostoru:

- Andorra
- Monako.
- San Marino
- Spojené království
- Vatikánský městský stát.

Mimo EU:

- Svatý Petr a Mikelon
- Guernsey
- Jersey.
- Ostrov Man.

Při platbě faktury v Odoo můžete vybrat jako způsob platby SEPA příkaz.
Můžete vytvořit soubor SEPA, který obsahuje všechny převody peněz na účet a nahrát jej do svého online
bankovní rozhraní pro zpracování plateb.

Výchozí formát souboru je podle specifikace SEPA Credit Transfer **„pain.001.001.03“**.
Je to dobře definovaný standard mezi bankami. U švýcarských a německých firem se však používají jiné formáty
„pain.001.001.03.ch.02“ pro Švýcarsko a „pain.001.003.03“ pro Německo.

Jakmile jsou platby zpracovány vaší bankou, můžete přímo importovat výpis z účtu
Odoo. Proces vyrovnání účtů bude automaticky shodný s platbami, které jste poslali do své banky.
S reálnými výpisy z účtu.

Konfigurace
=============

Aktivujte převod SEPA (SCT)
-----------------------------------

Pro platbu dodavatelům přes SEPA je nutné aktivovat nastavení **SEPA Credit Transfer**. Pro aktivaci přejděte na
:menu:Účetnictví --> Konfigurace --> Nastavení --> Platby od dodavatelů: SEPA kreditní převod
(SCT`). Po aktivaci nastavení a vyplnění firemních údajů budete moci používat
Možnost platby prostřednictvím SCT při placení dodavateli.

.. poznámka::
Podle instalovaného balíčku lokalizace je možné provádět platby SEPA Direct Debit a SEPA Credit
Přenosové moduly mohou být nainstalovány výchozím nastavením. Pokud ne, musí být :ref:`nainstalovány <general/install>`.

Aktivujte SEPA platební metody u bank
--------------------------------------

V účetním přehledu klikněte na rozbalovací nabídku (:guilabel:`⋮`) u svého bankovního deníku a
Vyberte položku „Konfigurace“ a klikněte na záložku „Odesílání plateb“. Pokud není již vybrána,
přítomný, přidat:guilabel:„SEPA Credit Transfer“ pod:guilabel:„Způsob platby“.

Ujistěte se, že uvedete číslo účtu IBAN (účty v rámci země nefungují s SEPA).
BIC v záložce „Účetní záznamy“.

Registrace plateb
--------------------

Můžete zaregistrovat jakékoliv platby dodavatelům provedené v rámci SEPA. Pro toto je potřeba přejít na :menuselection:`Účetnictví -->
Prodejci --> Platby. Při vytváření platby vyberte možnost „Souhrnné převody SEPA“.
:guilabel:`Způsob platby“.

Při první platbě obchodníkovi pomocí SEPA musíte vyplnit pole „Banka příjemce“.
Zadejte údaje o bance včetně IBAN a BIC (Bank Identifier Code). Odoo automaticky ověří
Pokud je dodržen formát IBAN.

Pro budoucí platby tomuto dodavateli Odoo navrhne automaticky bankovní účet, ale
zůstává možnost vybrat si nového.

Jakmile je platba zaregistrována, nezapomeňte ji potvrdit. Můžete také zaplatit faktury od dodavatelů
fakturu přímo pomocí tlačítka „Registrace platby“ v horní části faktury dodavatele.
Forma je stejná, ale platba je přímo spojená s fakturou a bude automaticky
se s ním smířila.
