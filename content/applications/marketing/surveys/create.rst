==============
Vytvářejte průzkumy
==============

Pro vytvoření průzkumu v aplikaci Odoo *Surveys* přejděte na:
Nový odhalil prázdnou anketní otázku.

.. poznámka::
Tlačítko „Nový“ není na panelu „Průzkumy“ přítomné, pokud je v panelu „Aktivita“.
pohled.

Přehledový dotazník
===========

.. obrázek:: vytvořit/prázdný-dotazník.png
:align:center
:alt:Jak vypadá prázdný dotazník v aplikaci Odoo Surveys.

Na začátku dotazníku jsou čtyři tlačítka s rádii, každé z nich reprezentuje jeden styl průzkumu.
Možnosti tlačítka jsou:

- :label:Anketa
- :label:Živá seance
- :guilabel:`Hodnocení“
- :guilabel:`Vlastní“ (výchozí hodnota)

Tyto možnosti jsou zde proto, aby zjednodušily proces vytváření průzkumu tím, že uživatelům poskytují automatizované
Nastavení a možnosti, které jsou vhodné pro tyto typy průzkumů. Každý z těchto typů průzkumu
Každá volba má svůj vlastní výběr možností.

Výchozí volba „Nastavení“ nabízí všechny možnosti z každé potenciální
druh průzkumu (v sekci „Možnosti“).

Pod těmito možnostmi průzkumu je prázdné pole, do kterého musí být zadán název průzkumu.
vstoupil.

Pod pole s názvem průzkumu je pole :guilabel:`Odpovědný`. Zvolte uživatele z roletky
menu pro správu dotazníku. Výchozí uživatel, který dotazník vytvořil, je
vybrána jako výchozí:guilabel:`Zodpovědný“.

Vpravo od těchto políček a nad záložkami je možnost přidat obrázek do pozadí.
je reprezentován ikonou „📷“ (fotoaparát). Po kliknutí se objeví možnost nahrání fotografie.
k dispozici. Toto obrázky by měl být použit jako pozadí pro celý průzkum. To není
povinná volba.

Pod těmito poli a možnostmi jsou čtyři záložky: „Otázky“, „Možnosti“
:guilabel:`Popis“ a „Konec zprávy“.

Karta otázek
-------------

Zobrazit, přistupovat ke, přidávat a odstraňovat otázky a sekce v průzkumu v části „Otázky“
tab.

V záložce „Otázky“ jsou dvě sloupce: „Název“ (tj.
otázka) a :guilabel:`Typ otázky“.

Pokud je zapnutá volba „Náhodně podle oddílu“ v záložce „Možnosti“,
v dotazníku se objeví sloupec s názvem „Vybrané náhodně“
:guilabel:`Dotazy“ záložka.

Uveďte, zda je odpověď na otázku povinná, kliknutím na :guilabel:`(volitelné sloupce)`
ikona vpravo od nadpisů sloupců. Pak vyberte položku „Povinná odpověď“ z
položku „Povinná odpověď“ v seznamu „Otázky“.

.. obrázek:: create/mandatory-answer-dropdown.png
:align:center
:alt:Výběr ze seznamu s možností vyžadované odpovědi v Odoo Surveys.

Přidejte otázku
~~~~~~~~~~~~~~

Přidat otázku do průzkumu můžete kliknutím na tlačítko „Přidat otázku“ v záložce „Otázky“.
a pokračujte v vyplňování okna „Vytvoření sekcí a otázek“.

Jak vytvořit a upravovat otázky, se dozvíte na stránce :doc:`vytváření otázek <questions>
dokumentace.

.. důležité:
Pro vytvoření sekcí a podsekcí je nutné zadat název průzkumu.
se zobrazí okno s otázkami. Pokud není pro průzkum zadán titulek, objeví se chybové okno.
V pravém horním rohu se zobrazí zpráva s instrukcemi pro uživatele, aby zadali název průzkumu.

Přidejte sekci
~~~~~~~~~~~~~

*Sekce* rozděluje průzkum na organizované části, aby vizuálně seskupila podobné otázky.
společně. Chcete-li vytvořit sekci, klikněte na tlačítko „Přidat sekci“ v dolní části stránky
Kartě „Otázky“, zadejte požadovaný název sekce, pak buď
Stiskněte klávesu Enter nebo klikněte pryč.

Ve sloupci otázek je čára oddělující sekce zobrazena šedou barvou.

Pak můžete přetáhnout požadované otázky pod sekci nebo přetáhnout titulek sekce na horní část.
(tj. před požadovanými otázkami v průzkumu). Takto se sekce vyplní otázkami
které odpovídají téma.

Pokud je zapnutá volba „Náhodně podle oddílu“ v záložce „Možnosti“,
při dotazníku se zobrazí číslo „1“ na řádku oddělujícím části, pod nadpisem „:guilabel:#
Kolonka „Vybrané náhodně“.

To znamená, že každý účastník bude vybrán náhodně z jedné otázky ze sekce.
vyplňovat anketu a přeskočit všechny ostatní otázky z vybrané sekce.
Zvolte číslo, vyberte požadovanou hodnotu a vložte ji do jeho políčka. Poté stiskněte
Stiskněte klávesu Enter nebo klikněte pryč.

Karta Možnosti
-----------

V záložce „Možnosti“ průzkumu je mnoho možností k výběru, které jsou oddělené
v čtyřech různých sekcích: „Otázky“, „Čas a skóre“
„Účastníci“ a „Živá sekce“.

Možnosti dostupné v této záložce se liší podle typu průzkumu, který si vyberete pomocí tlačítek nahoře.
formuláře průzkumu: :guilabel:`Průzkum“, :guilabel:`Živé sezení“, :guilabel:`Hodnocení“ nebo
:guilabel:`Vlastní“.

Typ průzkumu Custom zobrazuje všechny možné varianty v seznamu :guilabel:`Options`.
tabulka. Pokud tedy není žádný z následujících možností v seznamu volby „Možnosti“ (viz obrázek), je
Možná proto, že vybraný typ průzkumu jej neposkytuje.

Otázky
~~~~~~~~~~~~~~~~~

.. obrázek: vytvořit/otázky-sekce-možností-nabídka.png
:align:center
:alt:Otázky v sekci Možnosti na formuláři průzkumu v aplikaci Odoo Surveys.

První pole v sekci „Otázky“ se týká „Stránkování“,
nebo celkovému uspořádání průzkumu.

Vyberte si mezi: „Jedna stránka na otázku“, „Jedna stránka na oddíl“ nebo
„Jedna stránka s veškerými otázkami“ v poli „Stránkování“.

.. poznámka::
Pokud je vybrána možnost „Jedna stránka s veškerými otázkami“, zobrazí se všechny zbývající možnosti v
:guilabel:`Otázky“ pole, kromě „Výběr otázek“ je odstraněno, protože nejsou
již nejsou potřeba.

Poté vyberte jednu z následujících možností v poli „Zobrazit postup“:

- :guilabel:`Procento zbývajících otázek“: zobrazuje procento dotazů, které ještě nebyly vyplněny.
- :guilabel:`Počet otázek“: zobrazte počet odpovědí spolu s celkovým počtem
otázky, na které je třeba odpovědět.

V poli „Výběr otázek“ zvolte, aby průzkum ukázal všechny otázky.
nebo:guilabel:`Randomizace podle sekce“. Pokud je zvoleno:guilabel:`Randomizace podle sekce“, vytvoří se nová sloupec
kartě „Otázky“, označené jako „# Otázky náhodně vybrané“.

V sloupci „Náhodně vybrané otázky“ označte kolik otázek, v tom
Každý účastník musí být náhodně přiřazen k určitému oddělení.

Poslední možností je volba „Povolit roaming“. Pokud je zapnutá, účastníkům se umožňuje
navigovat zpět na předchozí stránky v průzkumu.

Sekce čas a skóre
~~~~~~~~~~~~~~~~~~~~~~

.. obrázek: vytvořit/časové skórování - možnosti záložky.png
:align:center
:alt:Sekce Čas a Skóre v záložce Možnosti dotazníku v aplikaci Odoo Surveys.

První možností v sekci „Čas a skóre“ je „Limit času pro průzkum“.
volitelná možnost. Pokud je povolena, zadejte časový úsek (v hodnotě :guilabel:`minutes`)
termínu průzkumu.

Dále v části „Skórování“ zvolte, zda má být:
„Hodnocení odpovědí na každé stránce“, „Hodnocení odpovědí na konci“ nebo
:guilabel:`Skórování bez odpovědí“.

Pokud je vybrána možnost „Nepočítat“, nejsou v této sekci k dispozici žádné další možnosti.
Pokud je však vybrána jiná možnost „Hodnocení“ (viz obrázek výše), objeví se další dvě pole:
:guilabel:`Požadovaný skóre (%)“ a „Je certifikace“.

Do pole „Požadovaný výsledek (%)“ zadejte minimální procento, které musí účastníci dosáhnout.
Pro úspěšné absolvování testu. Skóre pod touto hranicí je považováno za neúspěch. Toto číslo je také
slouží k určení, zda účastník je „certifikovaný“ nebo ne.
je aktivní.

Pokud je zapnutá možnost „Je certifikace“, tak se dotazník stane *certifikací*.
která je zobrazena na hlavním panelu aplikace „Průzkumy“ jako polopravidelný obrázek za průzkumem.
výhru v hlavním zobrazení KanaBanu nebo prostřednictvím ikonky plného poháru při seznamovém zobrazení.

Při zapnuté možnosti „Certifikace“ se objeví tři další pole – jedno
vedle možnosti a dvě pod ní.

Uživatelé mohou vybrat (a :guilabel:`Zobrazit náhled`) možnost z pole vedle ní.
šablona pro certifikaci.

Pod ní v poli „Šablona certifikované pošty“ mohou uživatelé vybrat přednastavený
vzor e-mailu nebo vytvořit ho na lince, který bude odeslán
dokončení.

Poslední možností je zobrazení přednastaveného štítku v případě zapnuté položky „Dát štítek“
kontaktní stránku pro tento ověřený účastník průzkumu.

Součásti účastníků
~~~~~~~~~~~~~~~~~~~~

.. obrázek: vytvořit/účastníci-sekce-možnosti-tabulka.png
:align:center
:alt:Sekce Účastníci v záložce Možnosti dotazníku v aplikaci Odoo Survey.

První dostupnou možností v sekci „Účastníci“ je „Způsob přístupu“.
Toto je pole, kde uživatelé mohou určit, kdo má přístup ke studii. Uživatelé si mohou vybrat buď:
„Kdokoli s odkazem“ nebo „Pouze pozvaní“.

Dále je možné nastavit volbu „Povinné přihlášení“ (viz obrázek). Po zapnutí této funkce musí uživatelé
se přihlásit před vyplněním dotazníku, i když mají platný token.

Poslední políčko je pole „Počet pokusů“. Pokud je zapnuto, objeví se další pole
vedle ní, kde uživatelé mohou určit, kolikrát se uživatelé mohou pokusit o tento průzkum.

Součástí je také sekce Live Session.
~~~~~~~~~~~~~~~~~~~~

.. obrázek: vytvořit/živá sekce možností záložky.png
:align:center
:alt:Sekce Živá sezení v záložce Možnosti dotazníku v aplikaci Odoo Surveys.

.. poznámka::
Ve formuláři průzkumu v záložce „Možnosti“ je k dispozici pouze sekce „Živé zobrazení“.
se týká anket *Živé debaty*.

První možností v sekci „Živá relace“ je pole „Kód relace“.
V tomto poli zadejte vlastní kód, který bude sloužit jako
účastníci, aby se mohli přihlásit do živého průzkumu.

Dalším je pole :guilabel:`Session Link`, které nelze upravit, ale může být odesláno.
na potenciální účastníky.

.. poznámka::
Pokud byl zadán kód relace, bude v poli „Odkaz na relaci“ zobrazen odkaz.
končí konkrétním kódem Session.

Pokud je použito celé :guilabel:`Session Link“ (končící na vlastní :guilabel:`Session Code“)
participantům umožní přístup k anketě v reálném čase, takže odkaz na něj už bude zadán.
V tu chvíli by se jen museli dočkat, až začne anketu moderátor živého vysílání.
a pak by se mohli dostat ven.

Pokud je odeslán :guilabel:`Session Link“ (končící :guilabel:`Session Code“)
**bez** zahrnutí kódu konce sezení :guilabel:`Session Code`, pokud účastníci přistupují na živý
v rámci této seance bude muset uživatelé zadat vlastní kód Session Code, aby mohli přistupovat.

Pokud pole „Kód relace“ je prázdné, zobrazí se o něco delší a složitější URL.
pole „Odkaz na sezení“. Když účastníci pokusí o přístup k živému setkání prostřednictvím
odkaz (bez konfigurovaného :guilabel:`Session Code“), stačí jen počkat na hostitele
účast na živém setkání, které začíná průzkumem, a mohli by se zapojit.

V poslední části „Živé seance“ je možnost „Odměnit rychlé
Odpovědi“. Pokud je tato možnost zapnutá, rychle odpovídající účastníci získávají více
bodů.

.. viz též:
:doc:`živá seance“

Karta popisu
---------------

V tomto nepovinném poli mohou uživatelé zadat vlastní popis průzkumu spolu s jakýmikoliv
vysvětlení nebo pokyny, které účastník průzkumu může potřebovat k tomu, aby se mohl správně zapojit (a
vyplnit dotazník.

Konec zprávy
---------------

V tomto nepovinném poli mohou uživatelé zadat vlastní zprávu, kterou účastníci vidí po dokončení.
průzkum.

Tlačítka pro průzkum
===================

Jakmile je dotazník správně nakonfigurován a otázky přidány, uživatel může využít
která jsou k dispozici v pravém horním rohu dotazníku.

.. obrázek: vytvořit/dotazník-tlačítek.png
:align:center
:alt:Různé tlačítka na dotazníku v aplikaci Odoo Surveys.

Tlačítka jsou následující:

- Kliknutím na tlačítko „Sdílet“ se zobrazí okno pro sdílení s možností
pozvat potenciální účastníky průzkumu - včetně odkazu na průzkum, který mohou vyplnit.
kopírována a zaslána potenciálním účastníkům a přepínač „Odeslat e-mailem“.

.... obrázek:: vytvořit/dotazník-souboru.png
:synchronizace: střed
:alt:Okno „Sdílet průzkum“ v aplikaci Odoo Surveys.

Pokud je přepínač „Odeslat e-mailem“ ve stavu zapnutí (zelený přepínač),
Přibývají další pole, do kterých lze přidat :guilabel:`Zasílatele“ a :guilabel:`Předmět“.
do e-mailu. Pod ním dynamický šablona e-mailu s uživatelským jménem:guilabel:`Start
Ve spodní části se objeví tlačítko „Certifikace“, které lze také upravit.

.... obrázek: vytvořit/průzkum-příspěvek-e-mail-vypnout.png
:synchronizace: střed
:alt:Okno „Sdílet průzkum“ v aplikaci Odoo Průzkumy s aktivovanou funkcí odeslání e-mailem.

Jakmile jsou úpravy dokončeny, klikněte na tlačítko „Odeslat“ a odeslat e-mailovou pozvánku všem uživatelům.
adresy/kontakty uvedené v poli :guilabel:`Příjemci`.
- :guilabel:'Zobrazit výsledky': tlačítko se objeví pouze tehdy, pokud se zúčastnilo alespoň jedno dítě.
který vyplnil dotazník. Kliknutím na tlačítko „Zobrazit výsledky“ se zobrazí samostatná záložka s výsledky
a vizuální analýza otázek a odpovědí v průzkumu. Další informace najdete na
:doc:`dotazníky pro hodnocení <scoring>“ dokumentace.
- :guilabel:`Vytvořit živou relaci“: kliknutím na tento odkaz se otevře oddělené okno
tabulku. Umožňuje účastníkům přístup k živému vysílání, ale samotný průzkum **ne**
do doby, než uživatel hostující živou anketu klikne na tlačítko „Začít“ v
Okno Session Manager*.

Dále, když je kliknuté tlačítko „Vytvořit živou relaci“ a záložka „Správce relací“
je otevřená, tlačítko „Vytvořit živou relaci“ na průzkumném formuláři je nahrazeno
dva nové tlačítka: „Otevřít správce relací“ a „Zavřít živou relaci“.

Kliknutím na tlačítko „Otevřít správce relací“ se otevře další samostatná záložka pro *Správce relací*.
Kliknutím na tlačítko „Zavřít živou relaci“ se zavře a následně ukončí živá relace.
- :guilabel:'Test': kliknutím na tuto ikonu se otevře nové záložce s testovací verzí dotazníku.
aby si uživatel mohl zkontrolovat chyby nebo nesrovnalosti z pohledu účastníka.
Uživatelé mohou zjistit, že jsou v testovací verzi průzkumu, pokud je nahoře modrá lišta.
obrazovce s textem „Toto je testová anketa -> Upravit anketu“.

Pokud je na modrém pruhu kliknutá odkazová adresa, vrátí se uživatel zpět do formuláře dotazníku.
- :guilabel:Tisknout: kliknutím na tento odkaz se otevře nové záložky s tisknutelnou verzí dotazníku.
uživatel může pokračovat v tisku pro své účely.
- :guilabel:`Uzavřít“: kliknutím na tuto ikonu se dotazník uzavře (tj. archivuje).
v červeném rámečku „Uzavřeno“ na horním pravém rohu dotazníku.

Když se tlačítko klikne a průzkum bude ukončen, objeví se jediné tlačítko v pravém horním rohu.
v rohu dotazníku s názvem „Znovuotevřít“. Když je kliknuté na „Znovuotevřít“,
pokud je průzkum znovu otevřen (tj. nearchivován) a odstraněna zpráva „Zaplaceno“.
dotazník.

.. viz též:
   - :doc:`otázky“
   - :doc:`skórování“
