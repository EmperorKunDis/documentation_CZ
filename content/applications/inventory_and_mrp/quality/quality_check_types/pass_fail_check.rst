=========================
Prošlo - neprošlo kvalitativní kontrolou
=========================

.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`
.. |QCP| nahradit za :: abbr: QCP (kontrolní bod kvality)
.. |QCP| nahradí ::: zkratka: QCP (Kontrolní body kvality)

V Odoo *Kvalita* je „Pas - Neprošel“ jedním z typů kontroly kvality, které lze vybrat při
vytvoření nového bodu kontroly kvality nebo kontrolního bodu kvality (QCP)*. Kontrola „Pas“ – „Neprošel“ se skládá z textu
políčko, které umožňuje tvůrci určit kritéria, která musí produkt splnit, aby prošel
check.

Vytvořte kontrolu kvality PAS/NEPAS
==================================

Existují dvě různé možnosti, jak vytvořit test kvality Pass – Fail. Jedním z nich je
ručně vytvořené. Alternativně lze konfigurovat |QCP| tak, aby automaticky vytvářel kontroly při
předem stanovený interval.

Tato dokumentace popisuje pouze konfigurační možnosti, které jsou jedinečné pro kvalitu Pass-Fail.
kontrolám a QCP. Pro kompletní přehled všech možností při vytváření
jediný test nebo QCP, viz dokumentace k tématu :ref:`kontrola kvality
<kvalita/kvalitní řízení/kontroly kvality> a :ref:`kontrolní body
<kvalita/kvalitní řízení/kontrolní body kvality>“.

Kontrola kvality
-------------

Pro vytvoření jediného testu kvality „Pas/Neprošel“ přejděte na: Menu > Kvalita > Kvalita
Kontrola-->Kontroly kvality, a pak klikněte na:guilabel:Nový. Vyplňte novou kontrolu kvality takto:
následuje:

- V poli „Typ“ vyberte typ kvalitativního testu „Projde – Neprojde“.
- V poli „Tým“ vyberte kvalitní tým odpovědný za řízení
kontrola.
- Do pole „Poznámky“ v záložce „Návod k použití“ zadejte pokyny pro
jak provést kvalitativní kontrolu a kritéria, která musí být splněna, aby byla kontrola úspěšná.

.. obrázek:pass_fail_check/kvalitativni-prezkum-formular.png
:align:center
:alt:Formulář kvalitativní kontroly, konfigurovaný pro kontrolu kvality PAS-NEPAS.

Kontrolní bod kvality (QCP)
---------------------------

Chcete-li vytvořit QCP, který provádí automatické kvalitativní kontroly s výsledkem *Pas - Neprošlo*, začněte tím, že se přesunete na
:menu „Kvalita“ -> „Kontrola kvality“ -> „Bod kontroly“, a klikněte na „Nový“. Vyplňte
nový formulář QCP takto:

- V poli „Typ“ vyberte typ kvalitativního testu „Projde – Neprojde“.
- V poli „Tým“ vyberte kvalitní tým odpovědný za řízení
kontrolami vytvořenými |QCP|.
- Do pole „Pokyny“ zadejte pokyny pro dokončení kvality
kontrola a kritéria, která musí být splněna pro úspěšné vykonání kontroly.

.. obrázek:pass_fail_check/qcp-form.png
:align:center
:alt: Formulář kontroly kvality bodu (QCP), který vytváří kontrolu kvality PAS/NEPAS.

Procesujte kvalitu „Pas“ nebo „Neprošlo“
===================================

Jakmile je vytvořen, existuje několik způsobů, jak mohou být kontroly kvality Measure zpracovány. Pokud
kontrola je přiřazena konkrétnímu skladovému nebo výrobnímu příkazu, lze s ní dále pracovat.
na samotný příkaz nebo lze platbu provést z detailu příkazu.

Na stránce s výpisem z účtu
---------------------

Pro zpracování kvalitativního kontrolního testu Measure zadejte následující adresu URL
:menu „Kvalita“ -> „Kontrola kvality“ -> „Kontroly kvality“, vyberte kontrolu kvality.
:guilabel:`Návod k použití` pro dokončení kontroly.

Klikněte na tlačítko „Přijato“ v pravém horním rohu
stránce. Pokud kritéria nejsou splněna, klikněte na tlačítko „Nepovoleno“.

Na objednávku
-----------

Pro zpracování kontroly kvality „Pas/Nepas“ na objednávku vyberte výrobní nebo skladovou objednávku.
objednávka (dodání, vrácení atd.) pro kterou je nutné předložit fakturu. Výrobní objednávky mohou být
vybrané pomocí navigace na:menu: „Výroba“ -> „Provoz“ -> „Dodavatelské objednávky“.
a kliknutím na objednávku skladu. Skladové objednávky lze vybrat přes
:menu „Zásoby“, kliknutím na tlačítko „Proces“ v kartě operace.
vybrat objednávku.

Na vybrané výrobní nebo skladovací objednávce se objeví modrá tlačítka „Kontrola kvality“
v horní části seznamu. Klikněte na tlačítko pro otevření okna „Kontrola kvality“, které
ukazuje všechny kvalitativní kontroly požadované pro tento objednávkový formulář.

Pro zpracování kontroly kvality „Pas/Neprošel“, postupujte podle pokynů zobrazených na štítku
Zkontrolujte okno s výzvou. Pokud jsou splněny kritéria pro kontrolu, klikněte na tlačítko „Přijmout“ v
spodní část okna. Pokud kritéria nejsou splněna, klikněte na tlačítko „Zrušit“.

.. obrázek: pass_fail_check/pass-fail-check-pop-up.png
:align:center
:alt:Okno kvalitativní kontroly „Přeskočit – Neprošlo“ na výrobním nebo skladovém příkazu.

Pokud musí být vytvořen varovný upozornění kvality, klikněte na tlačítko „Varování kvality“
výrobní nebo skladovací objednávku po neúspěšné kontrole. Kliknutím na:guilabel:"Kvalita
„Alertování“ otevírá formulář kvalitního upozornění na nové stránce.

.. viz též:
Pro kompletní návod na vyplnění formuláře o kvalitě výrobku se podívejte do dokumentace.
:ref:`kvalitní výstrahy <kvalita/kvalitni_rizeni/kvalitni_vystrahy>“.

Na pracovní příkaz
---------------

Při konfiguraci |QCP| spouštěného při výrobě lze také zadat konkrétní pracovní příkaz.
je specifikován v poli „Operace pracovního příkazu“ na formuláři QCP. Pokud je pracovní příkaz
specifikován, vytvoří se pro konkrétní objednávku kvalitativní kontrola „Pas-Nepas“,
výrobní zakázku jako celek.

Kontroly kvality, které jsou pro pracovní příkazy nakonfigurovány, musí být dokončeny z výrobního podlaží.
modul. Chcete-li tak učinit, začněte tím, že se přesunete na :menuselection:`Výroba -> Operace
Výrobní objednávky“. Vyberte |MO| obsahující výrobní objednávku, která zahrnuje práci na kterou je vydán *Pas/Nepas*
Prosím, zkontrolujte si svou e-mailovou adresu.

Vyberte záložku „Pracovní příkazy“ na nabídce |MO| a pak klikněte na „Otevřít pracovní příkaz“.
Klikněte na tlačítko „(externí odkaz)“ v řádku pracovního příkazu, který chcete zpracovat. Na výsledné
Okno „Příkazy k práci“ (pop-up), klepněte na tlačítko „Otevřít výrobní plochu“.
Modul „Prodejní plocha“.

Při přístupu z konkrétní objednávky se otevře modul „Dílna“ na stránku s prací
centru, kde je objednávka konfigurována k zpracování a izoluje kartu pracovního příkazu tak, aby
Ostatní karty jsou ukázány.

Začněte zpracovávat kroky pracovního příkazu, dokud nedosáhnete kroku *Prošlo/neprošlo*. Klikněte
na krok, který otevře okno s podrobnostmi o kritériích pro úspěšné nebo neúspěšné splnění kontroly.
Klikněte na tlačítko „Přijmout“ v dolní části okna, pokud kontrola projde, nebo
:guilabel:„Zkontrolovat“ tlačítko, pokud selže.

Pokud je kliknutá tlačítko „Doporučit“, přechází se na další krok práce.
pořadí. Pokud je kliknutá tlačítko „Neúspěch“, zobrazí se okno
se objeví s podrobným popisem dalších kroků.

.. obrázek: pass_fail_check/pass-fail-check-shop-floor.png
:align:center
:alt:Kontrola Přijato/Nepřijato v modulu Skladové hospodářství.

..tip:
Alternativně místo kliknutí na krok pro otevření okna můžete použít *Pas/Neprošel*.
Kontrolu lze dokončit kliknutím na zaškrtávací políčko, které se objeví po pravé straně řádku kroku.
na pracovním příkazu. Při použití této metody prochází kvalitativní kontrola automaticky bez
okno s výzvou k akci.
