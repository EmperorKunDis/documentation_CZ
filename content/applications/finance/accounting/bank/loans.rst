================
Správa půjček
================

Odoo nabízí kompletní seznam všech půjček, které vaše společnost vzala na sebe.
udržovat celkový a předvídatelný pohled na blížící se termíny splatnosti (např. předpověď hotovosti).
amortizační plány - nebo je do Odoa importovat a nechat si automaticky vypočítat měsíční úroky a
hlavní úpravy, aby vaše finanční zprávy vždy odrážely skutečnost s minimálním úsilím.

Vytvořit nový úvěr
-----------------

Vytvořte nový úvěr kliknutím na: „Účetnictví“ - „Účetnictví“ - „Úvěry“.
Nová půjčka má tři možnosti, jak vytvořit splátkový kalendář:

- importem z podporovaného souboru.
- Výpočet provádíme z více vstupních hodnot (např. částka půjčené,
:guilabel:`Doba trvání“, atd.) pomocí tlačítka :guilabel:`Vypočítat“.
- ručně vyplňovat řádky rozvrhu.

V každém případě je nutné vyplnit tři různé pole pro každou řadu v plánu splácení:
Datum, hlavní dlužník a úrok.

Políčka „Požadovaná částka“, „Úrok“ a „Doba splatnosti“ budou červená.
Pokud součet řádků neodpovídá celkovému součtu řádků v plánu splácení.

Mechanismus vstupů úvěrů
----------------------

Pokud je půjčená částka převedena na bankovní účet, měla by být převedena do dlouhodobého
účet (definovaný v záložce „Nastavení půjčky“). Poté, co byla půjčka schválena, Odoo
Vytváří potřebné záznamy, aby vždy bylo možné získat komplexní a předvídatelný pohled na
připravované splatnosti. Celý proces je plně automatizován s dlouhodobými i krátkodobými
hlavní mechanismus přeřazování.

Odoo vytvoří následující položky pro každou řádek plánu splácení:

Zápis o platbě z tohoto data
  - zaúčtuje na dlouhodobý účet částku jistiny.
  - úroky se odečítají na účet nákladů.
  - Připíše se kratšímu účtu částka za platbu. To je částka, která bude
staženy z účtu.

Vstup do nové třídy na stejný den,
  - zaúčtuje na dlouhodobý účet částku splatných jistin za dalších 12 měsíců.
  - připíše na účet krátkodobý zůstatek celkové částky splatných měsíců následujících dvanáct měsíců.

Změna třídění zaznamenaná v záznamu o změně třídění na následující den, která jednoduše obrátí předchozí
jedna.

Tímto mechanismem je měsíc za měsícem krátkodobý účet vždy aktuální s
aktuální krátkodobé pohledávky.

Splatit půjčku
--------------

Půjčka bude automaticky uzavřena v okamžiku, kdy je zveřejněn poslední záznam o platbě. Nicméně může být také
lze ručně zavřít (například proto, že je předčasně splacen) kliknutím na tlačítko „Zavřít“
tlačítko. Vyskočí okno, ve kterém se zeptá na datum splatnosti půjčky. Všechny položky
Tyto údaje budou také smazány po tomto datu.

Půjčku lze také zrušit. V takovém případě budou všechny záznamy smazány i když už byly
zveřejněno.

Analýza půjček
---------------------

Pokud se přesunete na „Účetnictví > Zprávy > Analýza půjček“, získáte
report s přehledem vašich aktuálních půjček. Výchozí nastavení zobrazuje jen částku
úrok a celková splátka za každý rok po dobu trvání úvěru.
