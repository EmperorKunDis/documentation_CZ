=================
Odmítnout žádost
=================

Každý krok v procesu náboru může být zamítnut.

Aby jste odmítli uchazeče, začněte v aplikaci **Personalistika** procházením karty uchazeče.
Provedení se dělí na dvě skupiny:

- Přejděte na:menu-selection:„Nabídka práce -> Přihlášky -> Všechny přihlášky“.
:guilabel:`Seznam aplikací`, klikněte na požadovanou linii uchazeče o práci, abyste se dostali do jeho
konkrétní kartu žadatele.
- Přejděte na hlavní panel „Práce“ pomocí volby v nabídce:menuselection:„Aplikace pro nábor zaměstnanců
-->Aplikace --> Podle pracovní pozice“. Následně klikněte na požadovanou pracovní pozici a poté na
kartu jednotlivce z stránky „Přihlášky“.

Na kartě žadatele je několik tlačítek. Klikněte na tlačítko s názvem
:guilabel:`Odmítnout“.

.._přijímání/důvody odmítnutí:

Důvody odmítnutí
==============

Důvody odmítnutí umožňují personalistům zdokumentovat důvod, proč byl uchazeč nevhodný, a poslat konkrétní
vzorový e-mail s důvodem zamítnutí žádosti zaslaný žadateli.

Kliknutím na „Odmítnout“ v aplikaci uživatele se zobrazí okno s „Důvodem odmítnutí“.
vystoupit.

Výchozí důvody odmítnutí v Odoo a jejich odpovídající e-mailové šablony jsou:

.. seznam tabulkový::
:hlavičkové řádky: 1
:prázdné sloupky: 1

   * - Vzor e-mailu
     - Důvod zamítnutí
   * Odmítnutí uchazečů o zaměstnání
     - |:guilabel:`Nesplňuje požadavky na práci“
| :guilabel:`Pracovní místo již obsazeno“
| :guilabel:`Duplikát“
| :guilabel:`Spam“
   * „Nábor: Nezajímám se“
     - | :guilabel:`Nepřijatelné pro uchazeče: nezpůsobilost k práci`
|:guilabel:`Nepřijatelné pro žadatele: plat`

Další důvody k zamítnutí: lze vytvářet a stávající upravovat (nebo smazat).
<příjem nových odpadů/>.

Vyberte důvod odmítnutí, abyste mohli odeslat e-mail s odmítnutím:

.._příjem nového odpadu:

Vytvořte nebo upravte důvody k odmítnutí
-------------------------------

Pro zobrazení a konfiguraci důvodů odmítnutí přejděte na: „Přijímací aplikace --> Konfigurace
--> Odmítnout důvody. To odhalí stránku „Důvody k zamítnutí“, kde jsou všechny existující
Důvody odmítnutí jsou uvedeny.

Pro vytvoření nového důvodu k odmítnutí z stránky „Důvody k odmítnutí“ klikněte na tlačítko „Nový“.
tlačítko v pravém horním rohu. Na konci seznamu se objeví prázdná řádka s prázdným polem
je uveden v sloupci „Popis“.

Do pole zadejte nový důvod odpadu. Doporučuje se vložit krátký důvod.
stručné, například „Nabídka vypršela“ nebo „Přihlášku stáhla“.

Poté v poli „Šablona e-mailu“ klikněte na pole, abyste zobrazili vyskakovací nabídku. Vyberte
Šablonu e-mailu z seznamu, která bude použita při výběru této důvodové odmítnutí.

Pokud chcete vytvořit nový šablonu e-mailu, zadejte název pro novou šablonu do pole.
Poté klikněte na tlačítko „Vytvořit a upravit…“ a vyskočí okno s formulářem pro vytváření e-mailových šablon.
objeví se okno.

V okně „Vytvořit e-mailový šablonu“ zadejte jméno pro formulář.
e-mail:„Předmět“ do příslušných políček.

Vložte požadovaný obsah e-mailu do záložky „Obsah“. Poté pokračujte v dalších
změny v šabloně v záložce „E-mailová konfigurace“ a „Nastavení“,
Poté klikněte na tlačítko „Uložit a zavřít“ pro uložení šablony. Po tomto kroku se Odoo vrátí do
:guilabel:`Důvody odmítnutí“ seznamu.

Nové šablony se objevují v novém poli „Šablona odmítnutí“: guilabel:Email Template“.

.. poznámka::
Přednastavené e-maily s odmítnutím uchazečů v Odoo používají dynamické položky, které jsou
osobní vložky, které do těla e-mailu přidávají data z rekordu uchazeče.

Příkladem je například použití jména žadatele v dynamické proměnné.
Vyskytne se vždy, když se na šabloně e-mailu objeví dynamická podmínka.

Pro podrobnější informace o šablonách e-mailů se obraťte na
:doc:`../obecne/spolky/vzor-e-mailu` dokumentace.

.._nabídnout místo/poslat e-mail s odmítnutím:

Odešlete odmítnutí e-mailem
==================

Po kliknutí na tlačítko „Odmítnout“ v žádosti se zobrazí :ref:`Důvod odmítnutí
Poté se vybere důvod odmítnutí z okna „Důvod odmítnutí“.
Poté se zobrazí dvě pole pod vybraným důvodem odmítnutí: „Odeslat e-mail“ a
:guilabel:`Šablona e-mailu“.

.. obrázek: odmítnutý uchazeč/odmítnuté okno.png
:alt:Okno s upozorněním, které se objeví při zamítnutí žádosti.

E-mailová adresa žadatele se automaticky vyplní do pole „Odeslat e-mail“;
příjemce e-mailu nelze přidat.

Pokud e-mailová zpráva neměla být odeslána uchazeči, zaškrtněte políčko „Neposlat email“.

Šablona e-mailu spojená s důvodem odmítnutí se vyplní do pole :guilabel:`Šablona e-mailu`.
položka pole. Pokud chcete použít jiný e-mailový šablonu, vyberte jinou šablonu z
:guilabel:`Šablona e-mailu“ v rozevíracím seznamu.

Pokud chcete odeslat odmítnutí uchazeči, zkontrolujte zaškrtávací políčko „Odeslat e-mail“.
Klikněte na „Odmítnout“ v dolní části okna „Důvod odmítnutí“.
Kandidátovi je zaslán odmítavý e-mail a na stránce se objeví červené tlačítko s textem „Odmítnuto“.
Kartu žadatele v pravém horním rohu.

.. obrázek::odmítnutý uchazeč/odmítnout.png
:alt:Karta uchazeče s odmítnutou reklamou v pravém horním rohu červeně.

Pohled na odmítnuté žadatele
=======================

Pokud je žádost zamítnuta, karta uchazeče již není viditelná v kanbanovém pohledu na pracovní pozici.
Stále je možné zobrazit uchazeče, kteří byli zamítnuti.

Pro zobrazení pouze odmítnutých uchazečů přejděte na: „Nabídka práce --> Přihlášky --> Podle
Pozice“, nebo „menuselection:“Nabídka práce -> Přijetí -> Všechny nabídky práce“.
Metody vedou na panel aplikací, jediný rozdíl je v tom, že se používá „Podle práce“
Zobrazení polohy uchazeče v kanbanovém pohledu zobrazí , zatímco :guilabel:„Všechny žádosti“ zobrazí
seznamu uchazečů.

Na stránce „Aplikace“ klikněte na ikonu „fa-caret-down“ (Přepínání vyhledávání).
Tlačítko „Panel“) v vyhledávacím poli a poté klikněte na tlačítko „Odmítnuto“, které se nachází pod
:icon:`fa-funnel` :guilabel:`Filtry“ sekce.

Všichni uchazeči, kteří nebyli přijati na pracovní pozici se zobrazují v záložce „Přihlášky“.
stránku pro tuto pozici, uspořádanou podle fáze, ve které byly zamítnuty.
