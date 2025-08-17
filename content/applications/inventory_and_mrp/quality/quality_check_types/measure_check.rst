=====================
Kontrola kvality
=====================

.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`
.. |QCP| nahradit za :: abbr: QCP (kontrolní bod kvality)
.. |QCPs| nahradí: zkratka `QCPs (Kontrolní body kvality)`

V Odoo Quality je Measure jedním z typů kvalitativních kontrol, které lze vybrat při
Vytvoření nového bodu kontroly kvality nebo kontrolního bodu kvality (KPQ). Kontrola měření vyzývá uživatele, aby
změřit určitý aspekt produktu a zaznamenat měření v Odoo. Kvalita kontroly
překročení povolené tolerance vůči normě.

Vytvořte kontrolu kvality měření
==============================

Existují dvě různé možnosti, jak vytvořit kontrolu kvality pomocí nástroje Measure. Jedna kontrola může být
ručně vytvořené. Alternativně lze konfigurovat |QCP| tak, aby automaticky vytvářel kontroly při
předem stanovený interval.

Tato dokumentace popisuje pouze konfigurační možnosti, které jsou jedinečné pro kvalitu Measure.
kontrolám a QCP. Pro kompletní přehled všech možností při vytváření
jediný test nebo QCP, viz dokumentace k tématu :ref:`kontrola kvality
<kvalita/kvalitní řízení/kontroly kvality> a :ref:`kontrolní body
<kvalita/kvalitní řízení/kontrolní body kvality>“.

Kontrola kvality
-------------

Pro vytvoření jednoho kontrolního bodu kvality přejděte na: Menu: „Kvalita“ - „Kontrola kvality“.
Klikněte na „Zkontrolovat kvalitu“ a poté na „Nový“. V novém okně zadejte následující údaje:

- V poli „Typ“ vyberte typ kvalitativního kontrolního bodu „Měření“.
- V poli „Tým“ vyberte kvalitní tým odpovědný za řízení
kontrola.
- Do pole „Poznámky“ v záložce „Návod k použití“ zadejte pokyny pro
jak má být fotografie pořízena.

.. obrázek: měření/měření-formulář-1.png
:align:center
:alt:Formulář kvalitativní kontroly, který je konfigurován pro kontrolu měření.

Kontrolní bod kvality (QCP)
---------------------------

Vytvořit QCP, který generuje automaticky kontroly kvality pomocí Measure, přejděte na
:menu „Kvalita“ -> „Kontrola kvality“ -> „Bod kontroly“, a klikněte na „Nový“. Vyplňte
nový formulář QCP takto:

- V rozevíracím seznamu „Typ“ vyberte typ kvalitativního kontrolního pole „Měření“.
V důsledku toho se objeví dvě nová pole: „Norma“ a „Povolené odchylky“.

  - Do prvního pole pro vstup textu pole „Norm“ zaznamenávejte ideální měření.
že výrobek musí splňovat. V druhém poli pro vložení textu zadejte jednotku,
měření, které by se mělo používat.
  - V poli „Tolerance“ jsou dva podpolia: „od“ a „do“.
Použijte pole :guilabel:`from` k určení minimální přijatelné měření a
:guilabel:`to pole“ k určení maximální přijatelné měření.

- V poli „Tým“ vyberte kvalitní tým odpovědný za řízení
kontrolami vytvořenými |QCP|.
- Do pole „Pokyny“ zadejte pokyny pro měření.
Je vybráno.

.. obrázek: měření_kontrola/měření-kontrola-qcp-formulář.png
:align:center
:alt:QCP formulář, který vytváří kontroly kvality měření.

Proces kvality kontroly měření
===============================

Jakmile je vytvořen, existuje několik způsobů, jak mohou být kontroly kvality Measure zpracovány. Pokud
kontrola je přiřazena konkrétnímu skladovému nebo výrobnímu příkazu, lze s ní dále pracovat.
na samotný příkaz nebo lze platbu provést z detailu příkazu.

Na stránce s výpisem z účtu
---------------------

Pro zpracování kvalitativního kontrolního testu Measure zadejte následující adresu URL
:menu „Kvalita“ -> „Kontrola kvality“ -> „Kontroly kvality“, vyberte kontrolu kvality.
:guilabel:`Návod k měření“ pro způsob měření.

Po měření zaznamenávejte hodnotu do pole kvality „Měření“
formulář. Chcete-li manuálně projít nebo neprojít kontrolou, klikněte na „Přijmout“ nebo „Nepřijmout“ v horním levém rohu
úhlu šeku.

Alternativně může být kvalitativní kontrola přiřazena k |QCP| s hodnotami *norm* a *tolerance*.
nebyly specifikovány, klikněte na tlačítko „Měření“ v pravém horním rohu kontroly.
automaticky označí kontrolu jako *Prošlo* pokud zaznamenaná hodnota je v toleranci,
nebo *Nesplněno*, pokud hodnota leží mimo něj.

Na objednávku
-----------

Pro zpracování kontroly kvality *Měření* na objednávce vyberte výrobní nebo zásobovací objednávku.
(přijetí, dodání, vrácení apod.), u nichž je vyžadován doklad. Výrobní objednávky mohou být
vybrané pomocí navigace na:menu: „Výroba“ -> „Provoz“ -> „Dodavatelské objednávky“.
a kliknutím na objednávku skladu. Skladové objednávky lze vybrat přes
:menu „Zásoby“, kliknutím na tlačítko „Proces“ v kartě operace.
vybrat objednávku.

Na vybrané výrobní nebo skladovací objednávce se objeví modrá tlačítka „Kontrola kvality“
v horní části stránky. Klikněte na tlačítko, abyste otevřeli okno „Kontrola kvality“, které
ukazuje všechny kvalitativní kontroly požadované pro tento objednávkový formulář.

Pro zpracování kontroly kvality *Měření* měřte produkt podle pokynů, pak zadejte hodnotu do
V poli „Měření“ na okně s upozorněním. Nakonec klikněte na „Potvrdit“, abyste měření zaregistrovali.
Zaznamenaná hodnota.

.. obrázek: měření-kontrola-pop-up.png
:align:center
:alt:Okno s názvem Kontrola kvality měření na výrobním nebo skladovém příkazu.

Pokud hodnota zadaná v poli je uvedena v rozsahu, který je definován v sekci „Tolerance“
Pokud je kvalita v pořádku, zobrazí se okno s výzvou k ukončení a ostatní výroba nebo
Pak lze objednávku skladu zpracovat jako obvykle.

Pokud je hodnota zadaná mimo stanovené rozmezí, objeví se nové okno s názvem
„Kontrola kvality selhala“. Tělo okna zobrazuje varovný textový řádek s informací, že
„Měřili jste jednotky a mělo by se pohybovat mezi jednotkami a jednotkami.“
návod, který je zadán v záložce „Zpráva při neúspěchu“ v QCP. Na konci
přepadový okno se dvěma tlačítky: „Opravit měření“ a „Potvrdit měření“.

.. obrázek: měření/měření-selhalo.png
:align:center
:alt:Okno „Kontrola kvality selhala“.

Pokud měření nebylo zadáno správně a je třeba ho změnit, vyberte: guilabel:"Korektura
Měření. To znovu otevře okno „Kontrola kvality“. Zadejte opravené
měření v poli „Měření“ a poté klikněte na „Ověřit“, abyste dokončili
check.

Pokud byla měření zadána správně, klikněte na tlačítko „Potvrdit měření“ místo toho a kvalita
kontrola selhává. Postupujte podle pokynů uvedených v okně „Kontrola kvality neprošla“.
okno.

Pokud musí být vytvořen varovný upozornění kvality, klikněte na tlačítko „Varování kvality“
výrobní nebo skladovací objednávku po neúspěšné kontrole. Kliknutím na:guilabel:"Kvalita
„Alertování“ otevírá formulář kvalitního upozornění na nové stránce.

.. viz též:
Pro kompletní návod k vyplnění formuláře pro hlášení kvality se podívejte na dokumentaci.
:doc:`upozornění na kvalitu <../quality_management/quality_alerts>.

Na pracovní příkaz
---------------

Při konfiguraci |QCP| spouštěného při výrobě lze také zadat konkrétní pracovní příkaz.
je specifikován v poli „Operace pracovního příkazu“ na formuláři QCP. Pokud je pracovní příkaz
specifikován, v případě konkrétního pracovního úkolu je vytvořen kontrolní bod kvality „Měření“, nikoliv
výrobní zakázku jako celek.

Kontroly kvality, které jsou pro objednávky nakonfigurovány, musí být dokončeny z výrobního podlaží.
modul. Chcete-li tak učinit, začněte tím, že se přesunete na :menuselection:`Výroba -> Operace
Výrobní objednávky“. Vyberte výrobní objednávku, která obsahuje pracovní příkaz pro který je prováděna kontrola kvality „Měření“
Je nutné mít s sebou.

Vyberte záložku „Pracovní příkazy“ na kartě |MO| a klepněte na tlačítko „Otevřít pracovní příkaz“.
Klikněte na tlačítko „(externí odkaz)“ v řádku pracovního příkazu, který chcete zpracovat. Na výsledné
Okno „Příkazy k práci“ (pop-up), klepněte na tlačítko „Otevřít výrobní plochu“.
Modul „Prodejní plocha“.

Při přístupu z konkrétní objednávky se otevře modul „Dílna“ na stránku s prací
centru, kde se objednávka konfiguruje k zpracování a izoluje kartu pracovního příkazu, aby nedošlo k
Ostatní karty jsou ukázány.

Procesujte kroky pracovního příkazu, dokud nedosáhnete kroku Kontrola měření. Klikněte na krok
otevřít okno s pokyny, jak měření provést. Po
Při měření zadejte hodnotu do pole „Měření“ v okně s nápovědou a poté
Klikněte na tlačítko „Přijmout“.

.. obrázek:: měření/měření-v-provozu.png
:align:center
:alt: Kontrola měření v modulu Podlaha.

Pokud měřená hodnota spadá do tolerančního rozsahu uvedeného v sekci Tolerance.
Pokud je kvalita v pořádku, zobrazí se okno s dalším krokem práce.
Pokud je měřená hodnota mimo uvedené rozmezí, objeví se nové okno.
s titulkem „Kontrola kvality selhala“.

Tělo okna s upozorněním „Kontrola kvality selhala“ zobrazuje zprávu, která uvádí
„Měřili jste jednotky a mělo by se pohybovat mezi jednotkami # a #.“
návod, který je zadán v záložce „Zpráva při neúspěchu“ v QCP. Na konci
přiblížení okna, dvě tlačítka se objeví: „Opravit měření“ a „Potvrdit měření“.

.. obrázek: měření/měření na podlaze/měření na podlaze selhalo.png
:align:center
:alt:Okno chybové hlášky kvality pro kontrolu měření v modulu výrobní plochy.

Pokud měření nebylo zadáno správně a je třeba ho změnit, vyberte: guilabel:'Upravit
Měření. Po otevření nového okna s názvem „Kontrola kvality“ zadejte opravené
v poli měření Measure a poté klikněte na tlačítko Validate pro dokončení kontroly.
a zavřít okno s upozorněním.

Pokud byla měření zadána správně, klikněte na tlačítko „Potvrdit měření“ místo toho a kvalita
kontrola selhává. Postupujte podle pokynů uvedených v okně „Kontrola kvality neprošla“.
okno.

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
