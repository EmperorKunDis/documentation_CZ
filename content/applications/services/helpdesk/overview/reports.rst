=========
Reportér
=========

.. |SLA| nahradit: :abbr:`SLA (smlouva o úrovni služeb)`
.. |SLA| nahrazuje: zkratka: SLA (Service Level Agreement)

Ve zprávách v Helpdesku Odoo se nabízí možnost řídit pracovní zatížení zaměstnanců, identifikovat oblasti
pro zlepšení a ověřit, zda jsou očekávání zákazníků naplňována.

Dostupné zprávy
=================

Podrobnosti o zprávách dostupných v Helpdesku Odoo naleznete níže.
Zprávy naleznete v aplikaci Helpdesk --> Zprávy a vyberte jednu z následujících možností:
„Analýza lístků“, „Analýza stavu SLA“ nebo „Hodnocení zákazníků“.

Analýza lístků
----------------

Zpráva o analýze lístků (*Ticket Analysis*) (v menu „Pomocná aplikace“ -> „Hlášení“ -> „Analýza lístků“)
poskytuje přehled o každém zákaznickém podpoře v databázi.

Tento report je užitečný pro určení, kde týmy tráví nejvíce času, a pomáhá při určování, zda
Nedochází k rovnoměrnému rozložení pracovní zátěže mezi podporu. Výchozí report počítá
Počet vstupenek na tým a dělí je podle fáze.

.. obrázek:reporty/vstupenky-default.png
:alt: Zobrazení výchozího pohledu na zprávu Analýza lístků.

Alternativní metody lze použít k měření času stráveného na různých místech v
průběh práce. Chcete-li změnit měřítka používaná pro zobrazený současný výstup nebo přidat
Pro více informací klikněte na tlačítko „Měření“ a vyberte jednu nebo více možností z roletky.

- :guilabel:`Průměrný počet hodin na odpověď“: průměrný počet pracovních hodin mezi zprávou zaslanou
klienta a odpověď z týmu podpory. *Tato seznam nezahrnuje zprávy, které byly zaslány v případě
lístek byl v složeném stavu.
- :guilabel:`Otevřeno hodinách“: počet hodin mezi datem vytvoření lístku a datem zavření
datum. Pokud na lístku není uvedeno datum konání akce, použije se aktuální datum. **Tato opatření nejsou
specifické pro pracovní dobu.**
- :guilabel:`Čas strávený (časové listy)“: počet hodin, které byly na lístku zaznamenány v časovém rozvrhu.
Tato funkce je dostupná pouze tehdy, pokud jsou v týmu zapnuté časové listy a aktuální uživatel má k nim přístup.
právo je vidět.*
- :guilabel:`Čas na první reakci“: počet pracovních hodin mezi datem, kdy byl
a datum, kdy byla první zpráva odeslána.*Toto nezahrnuje e-maily zaslané
automaticky, jakmile se lístek dostane do určité fáze.
- :guilabel:`Hodnocení (1-5)`: číslo z pěti, které reprezentuje zpětnou vazbu zákazníka (Nespokojený = 1,
Okay/Neutral = 3, Spokojený = 5).
- :guilabel:`Čas zbývající na SO“: čas zbývající do ukončení prodejního příkazu.
- :guilabel:`Časové údaje k přiřazení“: počet pracovních hodin mezi datem, kdy byl
vytvořené a kdy byl přidělen členovi týmu.
- :guilabel:`Časová osa uzavření“: počet pracovních hodin mezi datem, kdy byl
a datum uzavření.
- :guilabel:`Čas do splnění SLA“: počet pracovních hodin, které zbývají k naplnění posledního
|SLA| termín na lístek.
- :guilabel:`Počet lístků celkem“: celkový počet vstupenek.

.. poznámka::
*Časové údaje* se vypočítávají na základě výchozího kalendáře pracovních dní. Chcete-li zobrazit nebo změnit
pracovní kalendář, přejděte do aplikace „Nastavení“ a vyberte
:menu_vyber:`Zaměstnanci --> Pracovní doba společnosti`.

Analýza stavu SLA
-------------------

Hlášení o stavu SLA (*SLA Status Analysis*)
Analýza) :ref:`analyzuje výkon <helpdesk/analyze-sla-performance> jednotlivých SLA`
Politiky služebních úrovní.

Výchozí nastavení zprávy je filtrováno tak, aby ukazovalo počet |SLA|, které selhaly, jsou v procesu a počet
které byly úspěšné. Výsledky jsou seskupeny podle týmů.

.. obrázek:reports/sla-status.png
:alt:Pohled na skupinu podle možností v hlášení Analýza lístků.

Chcete-li změnit měřítka zobrazeného výstupu nebo přidat další, klikněte na
Tlačítko „Měření“ a vyberte jednu nebo více možností z rozevírací nabídky.

- :guilabel:`Průměrný počet hodin na odpověď“: průměrný počet pracovních hodin mezi zprávou zaslanou
klienta a odpověď z týmu podpory. *Tato seznam nezahrnuje zprávy, které byly zaslány v případě
lístek byl v složeném stavu.
- :guilabel:`Otevřeno hodinách“: počet hodin mezi datem vytvoření lístku a datem zavření
datum. Pokud na lístku není uvedeno datum konání akce, použije se aktuální datum. **Tato opatření nejsou
specifické pro pracovní dobu.**
- :guilabel:`Čas strávený (časové listy)“: počet hodin, které byly na lístku zaznamenány v časovém rozvrhu.
Tato funkce je dostupná pouze tehdy, pokud jsou v týmu zapnuté časové listy a aktuální uživatel má k nim přístup.
právo je vidět.*
- :guilabel:`Čas na první reakci“: počet pracovních hodin mezi datem, kdy byl
a datum, kdy byla první zpráva odeslána.*Toto nezahrnuje e-maily zaslané
automaticky, jakmile se lístek dostane do určité fáze.
- :guilabel:`Počet neúspěšných SLA“: počet ticketů, které selhaly alespoň jednou |SLA|.
- :guilabel:`Hodnocení (1-5)`: číslo, které reprezentuje zpětnou vazbu zákazníka (Nespokojený = 1,
Okay/Neutral = 3, Spokojený = 5).
- :guilabel:`Čas zbývající na SO“: čas zbývající do ukončení prodejního příkazu.
- :guilabel:`Časové údaje k přiřazení“: počet pracovních hodin mezi datem, kdy byl
vytvořené a kdy byl přidělen členovi týmu.
- :guilabel:`Časová osa uzavření“: počet pracovních hodin mezi datem, kdy byl
a datum uzavření.
- :guilabel:`Čas potřebný k dosažení SLA“: počet pracovních hodin mezi datem, kdy byl
a datum, kdy byla SLA splněna.
- :guilabel:`Počet lístků celkem“: celkový počet vstupenek.

.. viz též:
:doc:`Smlouvy o úrovni služeb (SLA) <sla>`

Hodnocení zákazníků
----------------

Hlášení o spokojenosti zákazníků (report „Spokojenost zákazníka“ :menuselection:`Pomocná aplikace - Hlášení - Spokojenost zákazníka`)
zobrazuje přehled hodnocení jednotlivých požadavků na podporu a také
další komentáře, které byly s hodnocením zaslány.

.. obrázek:reports/customer-ratings.png
:alt:Výhled na pás Kanban v zprávě Hodnocení zákazníků.

Klikněte na konkrétní hodnocení, abyste viděli další podrobnosti o hodnocení zákazníka.
včetně odkazu na původní vstupenku.

.. obrázek:reporty/podrobnosti-hodnocení.png
:alt: Zobrazení podrobností o hodnocení konkrétního zákazníka.

..tip:
Na stránce s podrobnostmi o hodnocení zaškrtněte políčko „Zobrazit pouze interně“ a skryjte tak
hodnocení od veřejnosti a uživatelů portálu.

Zpráva o hodnocení zákazníků je zobrazena v kanbanovém pohledu výchozím nastavením, ale lze ji také zobrazit
Graf, seznam nebo přepínač.

.. viz též:
:doc:`Hodnocení <ratings>`

Použití případů
=========

Hodnocení výkonnosti na základě priorit zákazníka
------------------------------------------------

Zpráva „Analýza vstupenek“ může být použita k posouzení doby, kterou trvá vyřešení
vysoké prioritní oproti běžným, což pomáhá zajistit, že vysoké priority budou
je vyřešeno rychle a identifikuje rozdíly v reakčních časech podle priorit.

Nejprve přejděte na: „Aplikace Helpdesk --> Hlášení --> Analýza hlášení“. Klikněte
Vyberte „Měření“ a poté „Časové údaje k uzavření“. Vyhledejte v poli
Vyberte „Skupina“ pod „guilabel:Label“, poté vyberte „Důležitost“. Nakonec v sekci „Filtry“
vyberte možnost „Zavřeno“.

..tip:
Pohled na střed je také užitečný pro tuto verzi zprávy.

Monitorování dodržování smluvních ujednání v čase
-----------------------------------

Zpráva „Analýza stavu SLA“ může být použita k sledování trendů v souladu se SLA, aby bylo možné identifikovat
období s vyšším počtem porušení SLA. Porušení SLA nastávají v případě, když týmy podpory nejsou schopny splnit
odpověď nebo řešení v smlouvě o úrovni služeb (SLA), což může vést k nespokojeným zákazníkům a potenciálním
penále a snížené týmové morálce. Rozpoznání těchto porušení je klíčové pro sledování
v reálném čase, odhalování vzorů a řešení kořenových příčin – jako jsou například problémy s personálem nebo
nedostatečně efektivní procesy.

Nejprve přejděte na: „Helpdesk aplikace -> Zprávy -> Analýza stavu SLA“. Klikněte na
:icon:`fa-area-chart` :guilabel:`(Graf)` ikonu, pak :icon:`fa-line-chart` :guilabel:`(Čára
Ikona „Graf“).

.. poznámka::
Zatímco výchozí pohled na zprávu „Analýza stavu SLA“ je v podobě přehledu, grafy lze zobrazit také jako čárové grafy.
Pro tento konkrétní případ je lepší vizuální reprezentace.

Klikněte na „Metriky“, poté vyberte „Počet neúspěšných SLA“. Tím zajistíte, že budou
Ve zprávě se uvádí pouze informace o lístcích, které selhaly alespoň jednou SLA. Kliknutím na
vyhledávací lišta, pak pod „Skupina“, vyberte „Deadline SLA“ a zvolte čas.
rámec, buď „Měsíc“, „Týden“ nebo „Den“. Tato možnost zobrazuje
nejvyšší počet lístků s |SLA| selhalo, což umožňuje týmu identifikovat vzorce a
připravit se na možné problémy.

..tip:
Časový rámec vybraný pro tento zprávu se může lišit v závislosti na několika faktorech, včetně výše
základními vstupy jsou počet zakoupených lístků na pravidelné akce, počet aktivních |SLA| v databázi a
úlohu týmu. Je vhodné experimentovat a zjistit, která varianta přináší nejvíce poznatků.

.. viz též:
:doc:`Odoo esenciální reportování <../../../essentials/reporting>`
