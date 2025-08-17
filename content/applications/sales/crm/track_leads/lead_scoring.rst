=========================================
Předvídejte skóre pro určení priorit
=========================================

Aplikace Odoo CRM může automaticky přiřadit leady a příležitosti prodejním týmům a prodejcům.
standardní postup je přiřazovat vedení podle pravděpodobnosti, že se každé vedení podaří získat. Firmy mohou
prioritizujte větší pravděpodobnost úspěšného obchodu rychlou přiřazením
Prodejcům, kteří jsou na tento produkt specializováni.

Odoo automaticky vypočítává pravděpodobnost získání každé zakázky pomocí metody nazvané *prediktivní
hodnocení potenciálních zákazníků.

Prediktivní hodnocení potenciálních zákazníků
=======================

Prediktivní lead scoring je strojově učící model, který využívá historická data z Odoo CRM.
dát otevřené šance/příležitosti.

Jakmile společnost zpracovává příležitosti prostřednictvím kanálu CRM, Odoo shromažďuje data o tom, které
příležitosti se získávají a ztrácejí. Prediktivní hodnocení potenciálu využívá tato data k předpovědi pravděpodobnosti
vítězství každého nového kontaktu nebo příležitosti.

Čím více příležitostí projde přes kanál CRM, tím více dat Odoo shromažďuje.
Výsledkem je přesnější pravděpodobnost.

Specificky používá prediktivní hodnocení potenciálních zákazníků v Odoo na modelech pravděpodobnosti *naive Bayes*.

.. matematika::
\begin{equation}
P(A|B) = \frac{P(A) \times P(B|A)}{P(B)}


Rozklad rovnice:

- P(A|B) = Výhoda úspěšného vedení *v tomto případě*
- P(A) = Celková pravděpodobnost úspěšného vedení bez ohledu na podmínky
- P(B|A) = Výše pravděpodobnosti, že je tento případ skutečný, pokud byl veden úspěšně
- P(B) = Výše pravděpodobnosti, že je tento případ skutečný

Termín *v tomto případě* odkazuje na proměnné, které mohou ovlivnit úspěšnost vedení v Odoo.
Může se jednat o proměnné jako například přiděleného obchodníka, zdroj vedení, jazyk.
v čele s dalšími historickými a demografickými daty.

Kalkulaci lze upravit tak, aby se zohledňovaly tyto proměnné:
Konfigurace skórování vedení, abyste mohli přizpůsobit výpočet potřebám každé společnosti.

Šance na úspěch každé příležitosti je zobrazena v kartě příležitosti a aktualizuje se
automaticky, jakmile se příležitost posune po cestě v rámci CRM.

.. obrázek::lead_scoring/probability-opportunity-form.png
:align:center
:alt:Úspěšnost zobrazená na příležitostní kartě.

Když se příležitost dostane na další úroveň, její šance na úspěch automaticky vzrostou.
podle předpovědní metody hodnocení leadů.

...Scoring a konfigurace:

Konfigurace
-------------

Prediktivní hodnocení potenciálních zákazníků je vždy aktivní v Odoo CRM.
pravděpodobnost úspěchu lze upravit v nastavení.

Pro přizpůsobení proměnných používaných pro prediktivní hodnocení potenciálních zákazníků se přihlaste do:
Konfigurace --> Nastavení. Pod položkou „Prediktivní hodnocení leadů“ klikněte na
Tlačítko „Aktualizovat pravděpodobnosti“.

Poté klikněte na rozbalovací nabídku a vyberte, které proměnné chcete použít pro předpovědní funkci hodnocení potenciálních zákazníků.
Bude brát v potaz.

.. obrázek: lead_scoring/update-probabilities.png
:align:center
:alt:Okno Updates Likelihood v nastavení prediktivního skórování leadů.

Každá z následujících proměnných může být aktivována:

- :guilabel:`Stát“: stát, ze kterého pochází příležitost
- :guilabel:`Země“: země původu příležitosti
- :guilabel:`Kvalita telefonního čísla“: zda je u příležitosti uvedeno telefonní číslo
- :guilabel:`Kvalita e-mailu“: zda je u příležitosti uvedena e-mailová adresa
- :guilabel:`Zdroj“: zdroj příležitosti (např. vyhledávač, sociální média)
- :guilabel:`Jazyk“: řeč, kterou je uvedeno v příležitosti
- :guilabel:`Štítky“: štítky umístěné na příležitosti

.. poznámka::
Variably Stage a Team jsou vždy platné. Variála Stage odkazuje na fázi prodejního cyklu ve společnosti CRM.
že příležitost je v procesu. „Tým“ odkazuje na prodejní tým, který je přiřazen k příležitosti.
Prediktivní hodnocení vždy zohledňuje tyto dvě proměnné, ať už se jedná o jakoukoli
jsou vybrány volitelné proměnné.

Dále klikněte na pole s datem vedle možnosti „Považovat vytvořené leady za ty vzniklé od“
Vyberte datum, od kterého bude předpovědní skórování začínat své výpočty.

Nakonec klikněte na tlačítko :guilabel:`Potvrdit`, abyste změny uložili.

Změňte pravděpodobnost ručně
-------------------------------

Pravděpodobnost úspěchu příležitosti lze změnit ručně na kartě příležitostí. Klikněte na
číslo pravděpodobnosti, které chcete upravit.

.. důležité:
Manuální změna pravděpodobnosti odstraní automatické aktualizace pravděpodobnosti pro tento
příležitostí. Pravděpodobnost se již neaktualizuje automaticky, jakmile příležitost postoupí
každé fázi plynovodu.

Pro znovuaktivaci automatické pravděpodobnosti klikněte na ikonu ozubeného kolečka vedle procenta pravděpodobnosti.

.. obrázek: lead_scoring/probability-gear-icon.png
:align:center
:alt:Ikona převodovky, která se používá k opětovnému zapnutí automatické pravděpodobnosti na příležitostném formuláři.

Přiřaďte kontakty na základě pravděpodobnosti
=================================

Odoo *CRM* může přiřadit příležitosti a prodejní týmy na základě zadaných pravidel.
Vytvořte pravidla pro přidělování úkolů na základě pravděpodobnosti úspěchu vedení, abyste zvýšili priority těch, které jsou
Je pravděpodobnější, že vyústí v dohody.

Nastavte pravidla pro přiřazení
-------------------------------

Pro aktivaci pravidla přiřazování, přejděte na: „CRM --> Konfigurace -->
Nastavení, a aktivujte: guilabel:Pravidla přiřazování.

Funkce přiřazení pravidel lze nastavit tak, aby běžela manuálně: guilabel: Manually, což znamená, že uživatel Odoo musí
spustit přiřazení ručně nebo opakovaně, což znamená, že Odoo spustí automaticky
přiřazení podle zvoleného časového období.

Pro automatické přiřazování kontaktů vyberte „Opakovaně“ pro „Běžné“.
sekci. Poté upravte četnost automatického přiřazování v
:guilabel:`Opakujte tento“ část.

.. obrázek: lead_scoring/pravidlo-na-přiřazení.png
:align:center
:alt:Nastavení přiřazení v nastavení CRM.

Pokud je nastaveno opakované přiřazení pravidlem, přidělení může být
spuštěné ručně pomocí ikony kruhové šipky v nastavení „Pravidla přiřazování“
(nebo pomocí tlačítka „Přidělit kontakty“ na stránce konfigurace prodejního týmu).

Nastavte pravidla přiřazování
--------------------------

Dále nastavte pravidla pro přidělování úkolů pro každý tým a/nebo prodejce.
určit, které kontakty Odoo přiřadí k čemu. Nejprve přejděte na: „:menuselection: CRM
V části Konfigurace -> Týmy prodeje vyberte tým prodeje.

V konfiguraci prodejního týmu pod položkou „Pravidla přiřazování“ klikněte na „Upravit“.
Domain je konfigurovat pravidla, podle kterých Odoo určuje přidělování vedení pro tento obchodní tým.
Pravidla mohou obsahovat cokoliv, co by mohlo být pro tuto společnost nebo tým důležité, a jakýkoliv počet pravidel.
Mohou být přidány.

Klikněte na tlačítko „Přidat filtr“ a začněte vytvářet pravidla přiřazování. Klikněte na plus
právo pravidla přidat další řádek. Klikněte na znak „x“, abyste jej odstranili
hranice.

Pro vytvoření pravidla pro přiřazování na základě pravděpodobnosti úspěchu příležitosti klikněte na
v levém sloupci s kategoriemi pravidel a vyberte možnost „Věrohodnost“.

V prostředním rozevíracím seznamu vyberte požadovaný znak pro rovnice – nejčastěji znak pro
*větší než*, *menší než*, *větší nebo rovno* nebo *menší nebo rovno*

V prostoru prava vložte požadovanou hodnotu čísla pro pravděpodobnost a klikněte
:guilabel:`Uložit“ pro uložení změn.

Příklad:
Řízení přiřazení tak, aby obchodní tým dostávali leady s pravděpodobností
úspěch větší než 20 %, vytvořte řádek domény s názvem: Probability >= 20.

.... obrázek: lead_scoring/probability-domain.png
:synchronizace: střed
:alt:Prodejní tým je nastaven na pravděpodobnost větší než nebo rovna dvaceti procentům.

Pro jednotlivé členy týmu lze také nastavit samostatná pravidla pro přidělování úkolů.
konfigurační stránce, klikněte na člena týmu v záložce „Členové“, pak upravte
Klikněte na tlačítko „Uložit“ pro uložení změn.

Pokud je v nastavení automatické přiřazení kontaktů k prodejcům a týmům, oba tyto typy se budou zobrazovat.
členové mají možnost zvolit si volbu „Přeskočit automatické přiřazení“. Zatrhněte tuto položku, abyste vynechali konkrétní
prodejní tým nebo prodejce, aby se jim automaticky přidělovaly případy podle pravidel v Odoo.
funkcí. Pokud je aktivována možnost „Přeskočit automatické přiřazení“, může prodejní tým nebo prodejce stále
by měly být přidělovány ručně.

K ručnímu přiřazení vedení k tomuto prodejnímu týmu klikněte na tlačítko „Přiřadit vedení“.
nahoře na stránce konfigurace prodejního týmu. To přiřadí všechny nezařazené nabídky
a odpovídat doméně daného týmu.
