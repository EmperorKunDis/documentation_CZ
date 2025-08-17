============================
Kontrola kvality obrázku
============================

.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`
.. |QCP| nahradit za :: abbr: QCP (kontrolní bod kvality)
.. |QCP| nahradí ::: zkratka: QCP (Kontrolní body kvality)

V Odoo *Kvalita* je „Začni fotit“ jedním z typů kontroly kvality, které lze vybrat.
při vytváření nové kontroly kvality nebo kontrolního bodu kvality (QCP). Kontrola „Vyfoťte se“ vyžaduje
obrázek připojený k šeku, který pak může být prohlížen kvalitativním týmem.

Vytvořte kontrolu kvality Fotka
=====================================

Existují dvě různé možnosti, jak vytvořit kontrolu kvality obrázku. Jedna kontrola může
je možné je vytvářet ručně. Alternativou je konfigurovat |QCP| tak, aby automaticky vytvářel kontroly při
předem stanovený interval.

Tato dokumentace popisuje pouze konfigurační možnosti, které jsou pro aplikaci *Take a Picture* jedinečné.
kontrolách kvality a QCP. Pro kompletní přehled všech dostupných konfiguračních možností při
vytváření jediného testu nebo QCP, viz dokumentace k tématu :ref:`kontroly kvality
<kvalita/kvalitní řízení/kontroly kvality> a :ref:`kontrolní body
<kvalita/kvalitní řízení/kontrolní body kvality>“.

Kontrola kvality
-------------

Pro vytvoření jediného kvalitativního testu přejděte na: Menu > Kvalita > Kvalita
Kontrola-->Kontroly kvality, a pak klikněte na:guilabel:Nový. Vyplňte novou kontrolu kvality takto:
následuje:

- V poli „Typ“ vyberte typ kvality kontroly „Zachycení obrázku“.
- V poli „Tým“ vyberte kvalitní tým odpovědný za řízení
kontrola.
- Do pole „Poznámky“ v záložce „Návod k použití“ zadejte pokyny pro
jak má být fotografie pořízena.

.. obrázek: obrázku_kontroly/obrazek-kontroly-formulář.png
:align:center
:alt:Formulář kvalitativní kontroly konfigurovaný pro kontrolu kvality Fotografuj.

Kontrolní bod kvality
---------------------

Pro vytvoření QCP, který generuje automaticky kvalitní kontroly ve formátu „Vyfotografujte si to“, přejděte na
:menu „Kvalita“ -> „Kontrola kvality“ -> „Bod kontroly“, a klikněte na „Nový“. Vyplňte
nový formulář QCP takto:

- V poli „Typ“ vyberte typ kvality kontroly „Zachycení obrázku“.
- Pokud je nainstalována aplikace „Údržba“, po výběru
*Změřte obraz* - typ kontroly. Toto pole použijte k určení zařízení, které by mělo být použito pro pořízení
kontrolu kvality obrázků. Informace o správě zařízení v aplikaci *Údržba* najdete na
dokumentace na téma:ref:`přidání nového zařízení <údržba/správa-zařízení/přidat-nové-zařízení>`.
- V poli „Tým“ vyberte kvalitní tým odpovědný za řízení
kontrolami vytvořenými |QCP|.
- Do pole „Poznámky“ zadejte pokyny pro zpracování fotografie.
Je vybráno.

.. obrázek: obrázky/obrázek-kontrola-příspěvku-formulář.png
:align:center
:alt: Formulář kvalitního kontrolního bodu (QCP), který je konfigurován tak, aby vytvářel kvalitativní kontrolu fotografií.

Kontrola kvality zpracování a pořízení snímku
======================================

Jakmile je kvalita kontroly vytvořena, existuje několik způsobů, jak ji mohou být zpracovány. Pokud
kontrola kvality je přiřazena konkrétnímu skladovému zásobování, výrobě nebo pracovnímu příkazu. Kontrola může být
je možné ji zpracovat přímo na stránce objednávky nebo z její stránky.

Na stránce s výpisem z účtu
---------------------

Pro zpracování kvalitativní kontroly *Vyfoťte se* z stránky kontroly začněte tím, že se přesunete na
Vyberte možnost „Kvalita“ -> „Kontrola kvality“ -> „Kontroly kvality“, vyberte kontrolu kvality.
Postupujte podle pokynů v části „Návod“.

Po pořízení snímku se ujistěte, že je uložen na zařízení používaném k zpracování kvality.
zkontrolovat (počítač, tablet atd.). Poté klikněte na tlačítko :guilabel:`✏️ (tužka)“ v
Klikněte na tlačítko „Obrázek“ v sekci „Zobrazit“. V prohlížeči souborů přejděte do složky
obrázek, vyberte jej a klikněte na tlačítko „Otevřít“, abyste jej připojili.

.. obrázek: obrázku_kontroly/tlačítko_pro_úpravu_obrazu.png
:align:center
:alt:Tlačítko pro editaci (tužka) na kvalitě Fotografování.

Na objednávku
-----------

Pro zpracování kontroly kvality „Vyfotit“ na objednávce vyberte výrobní nebo skladovou objednávku.
objednávka (dodání, vrácení atd.) pro kterou je nutné předložit fakturu. Výrobní objednávky mohou být
vybrané pomocí navigace na:menu: „Výroba“ -> „Provoz“ -> „Dodavatelské objednávky“.
a kliknutím na objednávku skladu. Skladové objednávky lze vybrat přes
:menu „Zásoby“, kliknutím na tlačítko „Proces“ v kartě operace.
vybrat objednávku.

Na vybrané výrobní nebo skladovací objednávce se objeví modrá tlačítka „Kontrola kvality“
v horní části stránky. Klikněte na tlačítko, abyste otevřeli okno „Kontrola kvality“, které
ukazuje všechny kvalitativní kontroly požadované pro tento objednávkový formulář.

Postupujte podle pokynů popisujících, jak fotku pořídit, které jsou uvedeny na :guilabel:`Kvalita
Zkontrolujte okno „Check“. Po pořízení fotografie se ujistěte, že je uložena na zařízení, které používáte k
provést kvalitativní kontrolu (počítač, tablet atd.)

Poté klikněte na tlačítko „Vyfotit“ v sekci „Obrázek“, abyste otevřeli
správce souborů zařízení. V správci souborů přejděte do složky s obrázkem, vyberte jej a klikněte
Připojte jej pomocí tlačítka „Otevřít“ a nakonec klikněte na „Zkontrolovat kvalitu“ a poté na „Validovat“.
okno pro dokončení kontroly kvality.

.. obrázek: obrázky/obrazky-kontroly-pop-up.png
:align:center
:alt:Okno kvality zobrazené při výrobním nebo skladovém příkazu.

Pokud musí být vytvořen varovný upozornění kvality, klikněte na tlačítko „Varování kvality“
výrobní nebo skladovací objednávku po ověření kontroly. Po kliknutí
:guilabel:„Varování kvality“ otevře formulář varování kvality na nové stránce. Pro kompletní průvodce, jak
vyplnit formulář o kvalitě, prohlédnout si dokumentaci na téma „kvalita“
<kvalita/kvalitní management/upozornění na kvalitu>.

Na pracovní příkaz
---------------

Při konfiguraci |QCP| spouštěného při výrobě lze také zadat konkrétní pracovní příkaz.
je specifikován v poli „Operace pracovního příkazu“ na formuláři QCP. Pokud je pracovní příkaz
specifikované, v případě konkrétního pracovního úkolu je vytvořen kontrolní seznam kvality „Zkontrolujte fotografii“, nikoli
výrobní zakázku jako celek.

Kontroly kvality objednávek v aplikaci Take a Picture **musí být** dokončeny z obchodu.
Modul podlaha*. Začněte tím, že se přesunete na :menuselection:`Výroba -> Operace
Výrobní objednávky“. Pak vyberte |MO| obsahující výrobní objednávku pro kterou je povoleno „Začít fotografování“
je nutná kvalitativní kontrola.

Vyberte záložku „Pracovní příkazy“ na nabídce |MO| a pak klikněte na „Otevřít pracovní příkaz“.
Klikněte na tlačítko „(externí odkaz)“ v řádku pracovního příkazu, který chcete zpracovat. Na výsledné
Okno „Příkazy k práci“ (pop-up), klepněte na tlačítko „Otevřít výrobní plochu“.
Modul „Prodejní plocha“.

Při přístupu z konkrétní objednávky se otevře modul „Dílna“ na stránku s prací
centru, kde se objednávka konfiguruje k zpracování a izoluje kartu pracovního příkazu, aby nedošlo k
Ostatní karty jsou ukázány.

Postupujte krok po kroku až do fáze kontroly kvality *Zaostřit*. Klikněte na
krok k otevření okna s pokyny, jak má být fotografie pořízena.
Po pořízení snímku se ujistěte, že je uložen na zařízení používaném k zpracování kvality.
kontrola (počítač, tablet atd.)

Poté klikněte na tlačítko „Vytvořit snímek“ v okně prohlížeče, abyste otevřeli soubor
správce souborů. V manažeru souborů přejděte na obrázek, vyberte ho a klikněte na tlačítko „Otevřít“
Připojte ho.

Konečně klikněte na tlačítko „Potvrdit“ v dolní části okna, abyste dokončili kvalitu
check. Následně se okno přesune na další krok objednávky.

.. obrázek: obrázky/obrazky-kontrola-plochy.png
:align:center
:alt: Kontrola v modulu Výroba.

Pokud musí být vytvořen upozornění na kvalitu, zavřete okno klepnutím na tlačítko „X (zavřít)“.
v horním pravém rohu.

Poté klikněte na tlačítko „⋮“ (tři vertikální tečky) v pravém dolním rohu práce.
zadat kartu pro otevření okna „Co chcete udělat?“.

V okně „Co chcete udělat?“ vyberte možnost „Vytvořit kvalitu“.
Tlačítko „Vyvolat požadavek“. To otevře prázdný formulář žádosti o kvalitu v novém okně.
okno.

.. viz též:
Pro kompletní návod na vyplnění formuláře o kvalitě výrobku se podívejte do dokumentace.
:doc:`upozornění na kvalitu <../quality_management/quality_alerts>.

Příloha obrázku pro kontrolu kvality
========================================

Po připojení fotografie k faktuře ji mohou zkontrolovat členové týmu kvality nebo
další uživatelé. Chcete-li tak učinit, přejděte na: menu „Kvalita“ -> „Kontrola kvality“ -> „Kontroly kvality“.
a vyberte si kvalitativní kontrolu, kterou chcete zkontrolovat.

Příloha je uvedena v sekci „Obrázek“ na formuláři kvalitativní kontroly.
Pokud kontrola projde, klikněte na tlačítko „Prošlo“.
:guilabel:`Vyhození“ tlačítko, pokud kontrola selže.

.. obrázek: review-picture-check.png
:align:center
:alt: Kontrola s přiloženou fotografií.
