==========
Nástup do zaměstnání
==========

Při nástupu nového zaměstnance je důležité mít postup pro začlenění do týmu, který lze dodržovat.
Tím se zajistí, že zaměstnanci obdrží informace, vybavení a školení.
Pro podnikání jsou přidělovány správné osoby.

Důkladné zaškolení zajistí, že nový zaměstnanec dostane všechny potřebné informace a nástroje k tomu, aby
uspějí v nové pozici a budou mít hladký přechod do nového zaměstnání.

Přehled plánu na začlenění
====================

Než se začne s procesem nástupu do zaměstnání, je vhodné zkontrolovat výchozí plán nástupu.
s přednastavenou aplikací Employees. Chcete-li zobrazit aktuální výchozí plán, přejděte na
:menuvolba-->Zaměstnanci --> Konfigurace --> Plán aktivit. Klikněte na
zobrazit podrobný plán nástupu do zaměstnání.

... _přijetí zaměstnance/plánování:

Plánová forma obsahuje následující informace:

- :guilabel:`Název plánu“: konkrétní název pro plán načítání.
- :label_guid:`Model`: určuje, kde se tento plán používá. V tomto případě v aplikaci **Zaměstnanci**.
- :guilabel:`Oddělení“: pokud je nevyplněno (výchozí nastavení), tento plán je dostupný pro všechny
pracovních oddělení. Omezte použití plánu na konkrétní pracovní oddělení výběrem oddělení.
v roletce.
- „Aktivita vytvořit“: tato záložka zobrazuje všechny kroky při nástupu do zaměstnání. Každá řádka ukazuje:

  - :guilabel:`Typ aktivity“: konkrétní aktivita pro krok. Výchozí možnosti jsou
:guilabel:'E-mail', :guilabel:'Telefon', :guilabel:'Schůzka', :guilabel:'Úkoly' nebo
:guilabel:`Nahrát dokument“. Pokud je nainstalovaná aplikace **Sign**, zobrazí se možnost „Požádat o podpis“
je k dispozici.
  - :summary: stručný popis kroku.
  - Vyberte osobu, která bude úkol dokončovat vzhledem k nově příchozímu zaměstnanci.

    - Vyberte uživatele v poli „Přiřazeno“ při spuštění aplikace.
:ref:`spuštění plánu nástupu do zaměstnání <employees/launch-plan>`.
    - Vyberte uživatele, který vždy tuto činnost řeší.
:guilabel:`Přiřazeno k` pole.
    - :guilabel:`Manager`: přiřazuje manažera zaměstnance, který je definován na záznamu o zaměstnanci.
    - :guilabel:„Kouč“: přiřadí kouče zaměstnance, jak je definován na záznamu o zaměstnanci.
    - :guilabel:`Zaměstnanec“: nový zaměstnanec dokončí činnost.
    - :guilabel:`Flottenmanager“: zuweist den für die Verwaltung der App „Flotte“ zuständigen **Flottenmanager“. Diese Option ist nur
bude k dispozici, pokud je nainstalovaná aplikace Fleet.

  - :guilabel:`Přiřazeno uživateli“: pole zůstává prázdné, pokud je vybrán „Uživatel výchozí“.
pro pole :guilabel:`Přiřazení`. Pokud je vybráno pole :guilabel:`Výchozí uživatel`, toto pole
obyvatelé s vybraným uživatelem.
  - :guilabel:`Dokument k podepsání“: odpovídající dokument, který vyžaduje podpis.
  - :guilabel:`Intervál`: čas, kdy je aktivita aktivní.
  - „jednotka“: pevně stanovený časový úsek buď „dny“, „týdny“ nebo
:guilabel:`měsíce“.
  - :guilabel:„Spouštěč“: jak je určeno rozvržení pro aktivity. Možnosti jsou buď
:guilabel:`Před plánovaným datem“ nebo :guilabel:`Po plánovaném datu“.

... příklad::
Před nástupem do práce musí být novému zaměstnanci přidělen notebook, který je nutné nastavit a zaregistrovat.
tento krok by měl provádět vždy manažer IT, Abby Jonesová.

Pro konfiguraci této aktivity s těmito parametry je nastaven typ aktivity na
:guilabel:"Dělat", s výčtem :guilabel:"Přidělit notebook".
pole je nastaveno na „Výchozí uživatel“ a pole „Přiřazeno“ je nastaveno na
:guilabel:"Abby Jones". Interval je :guilabel:"1" a jednotka
Je nastaven na :guilabel:`dny“. Trigger je nastaven na :guilabel:`Před datem plánu“.

.. obrázek:: onboarding/activity-plan.png
:alt:Aktivita, která je konfigurována tak, aby notebook přidělila den před nástupem zaměstnance do práce.

Kroky plánu onboardingu
---------------------

Výchozí plán „Přijetí“ zahrnuje tři výchozí kroky. Všechny kroky jsou
Aktivitami typu „Co dělat“ a jsou naplánovány na den spuštění plánu nástupu.
(:guilabel:'Před plánovaným datem').

- :guilabel:`Nastavení materiálů IT“: manažer musí shromáždit a nakonfigurovat všechny materiály IT.
- :label:Školení pro nového zaměstnance“: manažer musí naplánovat školení pro nového zaměstnance.
- :guilabel:Školení“: nový zaměstnanec musí absolvovat školení naplánované manažerem.

.. obrázek:: onboarding/onboarding.png
:alt:Tři základní kroky v plánu Onboarding.

... zaměstnanci/upravit plán:

Upravte plán přijetí nových zaměstnanců
======================

Společný plán přijetí nového zaměstnance funguje jen tehdy, pokud je celá společnost na stejné vlně.

.. poznámka::
Pokud máte univerzální plán přijetí zaměstnance, přidejte nebo upravte výchozí plán přijetí.
Pro jednotlivé oddělení je potřeba vytvořit plán onboardingu, viz. „Vytvoření nového plánu onboardingu“.
<zaměstnanci/vytvořit plán>.

Aby bylo možné změnit výchozí plán, je třeba nejprve přejít na:
Plán aktivit“, pak klikněte na „Přijetí“.

K úpravě kroku je potřeba na něj kliknout. V okně „Otevřené aktivity“ vyberte požadovanou
změny kroku, pak stiskněte tlačítko „Uložit“.

Chcete-li přidat další krok, klikněte na „Přidat řádek“ v seznamu aktivit.
kartě „Aktivita“, a prázdné okno „Vytvořit aktivitu“
objeví se okno s informacemi. Zadejte všechny údaje do okna a poté klikněte na tlačítko „Uložit a zavřít“.
nejsou další kroky, které je třeba přidat, nebo klikněte na „Uložit a nový“ pokud jsou potřeba další kroky.

… zaměstnanci/vytvořit plán:

Vytvořte plán přijetí
======================

Některé společnosti vyžadují různé plány na začlenění zaměstnanců do týmu v závislosti na tom, zda je začleňování specifické pro danou divizi.
postupy, které se nevztahují na celou společnost. Pro tyto případy vzniká nový oddělení
musí být vytvořen plán onboardingu.

Chcete-li vytvořit nový plán přivítání, navštivte požadovaný plán a nakonfigurujte všechny požadované
kroky zaměstnanců a modifikace plánu“.

.. příklad::
Firma, která se zabývá výrobou a prodejem venkovního kovového nábytku, může mít
velkou továrnu, která produkuje výrobky, a samostatnou prodejní kancelář. Tato společnost může
separátní plány pro nové zaměstnance, jeden pro pracovníky ve výrobě a druhý pro kancelářské pracovníky.

Plán pro nové zaměstnance ve výrobním závodě je nastaven v oddělení :guilabel:`Výroba`.
a zahrnuje speciální úkoly související s prací ve fabrice, například sběr nových
- pracovní oděv a ochranné pomůcky, přiřazení bezpečnostního kurzu, zaslání e-mailu týmu o nových pravidlech.
zaměstnání, přínosy a další.

.... obrázek: onboarding/factory-onboarding.png
:alt:Plán nástupu do zaměstnání pro pracovníky ve výrobních závodech.

... zaměstnanci/plán startu:

Zahájení plánu na uvítání nových zaměstnanců
======================

Po nástupu zaměstnance a vytvoření jeho profilu zaměstnance :ref:`
<příjem nového zaměstnance>“, přejděte na profil požadovaného zaměstnance kliknutím na jeho KanaBan
kartu na stránce aplikace „Zaměstnanci“ a poté klikněte na tlačítko :guilabel:`Spustit plán“.
pracovní profil zaměstnance a prázdné okno „Plán spuštění“ se načte.

V poli „Plán“ vyberte požadovaný plán přijetí. Poté použijte kalendář
vyberte datum v poli „Datum plánu“ (obvykle první den zaměstnance).
Datum ale může být libovolné.

V pravé části okna „Plán startu“ se zobrazují všechny kroky v zvoleném plánu.
plán, který je seskupen podle toho, co bylo vybráno v polích „Přidělení“ na formuláři plánu
<příručka pro nováčky/plán>.

Jakmile jsou nastaveny pole „Plán“ a „Datum plánu“, klikněte na
tlačítko „Zadat termín“ a Odoo naplánuje vše podle plánu.
přesné termíny splatnosti.

Všechny plánované aktivity se zobrazují v chatovacím okně profilu zaměstnance i v chatovacím okně
uživatelé s přiřazenými úkoly souvisejícími s plánem.

.. poznámka::
Pokud byly nějaké úkoly přiřazeny na „Zeptej se při spuštění“, pak „Přiřazený“
V poli „Zahájení“ se objeví pole „Plán spuštění“. Pomocí rozevírací nabídky vyberte
uživatel, který je zodpovědný za všechny nezařazené aktivity.

.. obrázek: onboarding/onboarding-chatter.png
:alt:Všechny úkoly spojené s nástupem do práce naplánované v chatu.
