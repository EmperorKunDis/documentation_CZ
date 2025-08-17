==============
Kontroly kvality
==============

...kvalita/kvalitní řízení/kontrola kvality:
.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`
.. |QCP| nahradit za :: abbr: QCP (kontrolní bod kvality)

Kontroly kvality jsou manuální kontroly prováděné zaměstnanci a slouží k zajištění kvality
produktů. V Odoo lze provést kvalitativní kontrolu pro jeden produkt nebo více produktů
v rámci stejného skladového pohybu nebo výrobního příkazu.

Pomocí kontrolního bodu kvality (QCP) lze vytvářet automatické kontroly kvality.
pravidelných intervalech. Když jsou kvalitativní kontroly vytvářeny pomocí QCP, objeví se na výrobním nebo
seznamu skladových položek, kde zaměstnanec zpracovávající objednávku bude vyzván k jejich dokončení.
podrobné vysvětlení, jak vytvořit a nakonfigurovat |QCP|, najdete v dokumentaci k tématu :ref:`kvalita
kontrolní body <kvalita/kvalitativni-rizeni/kontrolni-body>.

Kontroly kvality se nejčastěji vytváří automaticky pomocí nástroje QCP. Je však také možné
ručně vytvořit jednu kontrolu kvality. Vytváření kontroly kvality ručně je užitečné, pokud zaměstnanec chce
zaregistrovat kvalitativní kontrolu, která se bude konat pouze jednou.
nevyžádaně.

Kontrola kvality ručně
====================

Chcete-li ručně vytvořit jedinou kontrolu kvality, přejděte na: „Kvalita“ -> „Kontrola kvality“.
Kontrola kvality“ a klepněte na „Nový“. Na formuláři pro kontrolu kvality začněte výběrem
možnost z nabídky:guilabel:`Kontrola přes`:

- :guilabel:`Operace“ požaduje kontrolu celé operace (např. dodacího příkazu) a všech
produkty v něm obsažené.
- :guilabel:`Produkt“ požaduje kontrolu každé jednotky produktu, který je součástí operace (např.
každé jednotce produktu v dodací objednávce.
- :guilabel:`Množství“ požaduje kontrolu každé množiny produktů, které jsou součástí operace
(např. jedna faktura za pět kusů zboží v rámci objednávky). Vyberte
:guilabel:`Množství“ také způsobuje zobrazení pole „Série / šarže“.
Může být vybrán konkrétní los nebo sériové číslo, pro které má být kvalita ověřena.

Dále vyberte operaci skladu z rozevírací nabídky „Vyskladnění“ nebo výrobní operace z rozevírací nabídky „Výroba“.
objednávku z nabídky „Výrobní objednávka“. Toto je nutné, protože Odoo potřebuje
zda se jedná o kontrolu kvality při určité operaci.

Pokud má být kvalitativní kontrola přiřazena konkrétnímu |QCP|, vyberte jej z pole :guilabel:`Kontrolní
Vyberte možnost „Další“. Tato volba je užitečná v případě, že se kvalitní kontrola vytváří ručně, ale
stále ještě by měly být považovány za patřící do určitého |QCP|.

Vyberte typ kontroly kvality z pole „Typ“:

- :guilabel:`Návod k použití“ poskytuje konkrétní pokyny, jak provést kontrolu kvality.
- :guilabel:`Přiložte fotografii“ vyžaduje připojení fotografie k šeku, než bude možné šek
dokončeno.
- :guilabel:`Prošlo - Neprošlo“ se používá, pokud kontrolovaný výrobek musí splňovat určitá kritéria.
provést kontrolu.
- Vybráním položky „Měření“ se objeví pole „Měření“, do kterého můžete zadat
Musí být zadána měření, než bude možné dokončit kontrolu.
- Vybráním položky „List“ se objeví pole s možnostmi „Šablona kvality“.
Použijte ho k výběru kvalitní pracovní list, který musí být vyplněn, aby byla úloha dokončena.

V poli „Tým“ vyberte kvalitní tým, který je zodpovědný za kontrolu kvality.
V poli „Společnost“ vyberte společnost, která vlastní zkoumaný produkt.

Na kartě „Poznámky“ na spodní části formuláře zadejte případné pokyny.
V poli „Text“ (např. „Přiložte fotografii produktu“).
V poli „Poznámky“ zadejte příslušné informace o kontrole kvality (kdo
kdo ji vytvořil, proč byla vytvořena atd.

Konečně pokud je platba okamžitě zpracována, klikněte na tlačítko „Přijmout“ v horní části stránky.
vlevo od obrazovky v případě úspěšného testu nebo tlačítko „Zkontrolovat“ v případě neúspěšného testu.

.. obrázek: kvalita_kontrol/kvalita-kontrola-formular.png
:align:center
:alt:Formulář kvalitativní kontroly pro ověření PAS/NEPAS.

Kontrola kvality procesu
=====================

Kontroly kvality mohou být zpracovány přímo na stránce kontroly kvality nebo z výrobního procesu.
seznam zásob pro který je nutné provést kontrolu kvality.
přesně specifikované pracovní příkazu, kontrola se zpracovává v modulu Shop Floor.

.. poznámka::
Není možné ručně vytvořit jediný kvalitativní kontrolní bod, který je přiřazen konkrétní práci.
objednávky operací. Kvalitativní kontroly pro operace pracovních objednávek mohou vytvářet pouze |QCP|.
dokumentace k :ref:`kontrolním bodům kvality
<kvalita/kvalitní řízení/kontrolní body kvality> pro informace o tom, jak konfigurovat
|QCP|, který vytvoří kvalitativní kontrolu pro konkrétní operaci pracovního příkazu.

Kontrola kvality stránky
------------------

Pro zpracování kvalitativní kontroly z kontrolního listu začněte tím, že se přesunete na stránku „Kvalita“ a poté vyberte možnost
Kontrola kvality --> Kontrola kvality“, pak vyberte kontrolu, kterou chcete zpracovat. Postupujte podle pokynů pro
jak dokončit kontrolu, uvedenou v poli „Poznámky“ na záložce „Návod k použití“.
v dolní části stránky.

Pokud kvalita odpovídá požadavkům, klikněte na tlačítko „Přijmout“ v horní části stránky. Pokud kontrola
nefunguje, klikněte na tlačítko „Nefunkční“ místo toho.

Kontrola kvality na objednávku
----------------------

Pro zpracování kontroly kvality objednávky vyberte výrobní nebo skladovou objednávku (příjemku).
dodání, vrácení, atd.), pro které je nutné provést kontrolu. Výrobní objednávky lze vybrat
Navigace na: menu výběr: „Výroba“ -> „Provoz“ -> „Objednávky výroby“, a kliknutí
na objednávku. Objednávky na zásoby lze vybrat kliknutím na nabídku „Sklad“ a následně
tlačítko „Proces“ na kartě operace a vybrat objednávku.

Na vybraném výrobním nebo skladovacím příkazu se objeví modrá tlačítka „Kontroly kvality“.
v horní části seznamu. Klikněte na tlačítko pro otevření okna „Kontrola kvality“, které
ukazuje všechny kvalitativní kontroly požadované pro tento objednávkový formulář.

Postupujte podle pokynů, které se zobrazí v okně „Kontrola kvality“. Pokud je výsledek „Prošlo“ nebo „Neprošlo“
provádí se zpracování šeku, dokončete šek kliknutím na tlačítko „Přijato“ nebo „Odmítnuto“.
spodní části okna přesunutého okna. Pro všechny ostatní typy kontroly kvality je tlačítko „Zkontrolovat“
zobrazí se místo něj a klikněte na ni, abyste dokončili kontrolu.

.. obrázek: kvalita_kontrol/kvalitni_kontrola_pop-up.png
:align:center
:alt:Okno „Kontrola kvality“ v objednávce výroby.

Kontrola kvality na pracovním příkazu
---------------------------

Pro zpracování kvalitativní kontroly objednávky začněte tím, že se přesunete na:
-->Provozní operace --> Výrobní objednávky“. Vyberte |MO| obsahující výrobní objednávku, pro kterou chcete vytvořit
je nutná kvalitativní kontrola.

Vyberte záložku „Pracovní příkazy“ na nabídce |MO| a pak klikněte na „Otevřít pracovní příkaz“.
Klikněte na tlačítko „(externí odkaz)“ v řádku pracovního příkazu, který chcete zpracovat. Na výsledné
Okno „Příkazy k práci“ (pop-up), klepněte na tlačítko „Otevřít výrobní plochu“.
Modul „Prodejní plocha“.

.. viz též:
Pro plný průvodce modulu Shop Floor se podívejte na :doc:`Přehled modulu Shop Floor
dokumentace v sekci „Prohlídka výrobních prostor“ na stránce „Přehled výroby“.

Při přístupu z konkrétní objednávky se otevře modul „Dílna“ na stránku s prací
centru, kde je objednávka konfigurována k zpracování a izoluje kartu pracovního příkazu tak, aby
Ostatní karty jsou ukázány.

Postupujte krok po kroku až do kontrolního bodu kvality, který je označený jako
okno s podrobnými pokyny k vyplnění kontrolního seznamu. Po provedení instrukcí
Klikněte na tlačítko „Potvrdit“ k dokončení kontroly. Pokud je zvolená možnost „Projde – Neprojde“,
zpracováno, klikněte buď na tlačítko „Přijato“ nebo „Nepřijato“.

Kontrolu kvality lze také dokončit kliknutím na zaškrtávací políčko vpravo od
krokem, což automaticky označí kontrolu jako „Prošlo“.

.. poznámka::
Specifické kroky pro zpracování kontroly kvality závisí na typu kontroly, která se provádí.
Informace o zpracování každého typu kontroly kvality jsou uvedeny v dokumentaci spojené s tímto nástrojem:

   - :doc:`../kvalita_zkoušek/návod_na_zkoušku`
   - :doc:`../kvalitativni-kontrola/pravidla-pro-pruzkumy/hlaseni-o-vyhodne-a-nezvykle-vyhodne-testu
   - :doc:`../kvalita_zkoušek/měření_zkoušky`
   - :doc:`../kvalita_souboru/obrazový_pruvodce`
