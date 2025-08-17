===============
Šablony e-mailů
===============

Šablony e-mailů jsou uložené e-maily, které se používají opakovaně k odeslání e-mailů z databáze.
umožňují uživatelům odesílat kvalitní zprávy bez opakování stejného textu.

Vytváření různých šablon, které jsou přizpůsobeny konkrétním situacím, umožňuje uživatelům vybrat tu správnou.
poselství pro správnou cílovou skupinu, což zvyšuje kvalitu poselství a celkově
zapojení zákazníka.

.. poznámka::
Emailové šablony v Odoo používají QWeb nebo XML, což umožňuje upravit e-maily ve svém konečném
renderování, které zvyšuje odolnost proti změnám bez nutnosti jakéhokoli kódu.
to znamená, že Odoo může používat grafické uživatelské rozhraní (GUI) k úpravám e-mailů, které upravují zadní část
kód. Když je e-mail přečten uživatelovým programem, může být formátován jinak a
grafika se objeví v konečné podobě.

Přejděte do režimu vývojáře, abyste získali přístup k e-mailovým šablonám v části
Nastavení aplikace --> Technické menu --> E-mail --> Vzory e-mailů.

Úprava šablon e-mailů
=======================

Funkci *powerbox* lze použít při práci s e-mailovými šablonami. Tato funkce poskytuje
schopnost přímo upravovat formátování a text v e-mailovém šabloně, stejně jako schopnost přidat
odkazů, tlačítek, možností objednání nebo obrázků.

Dále je možné upravovat přímo XML/HTML kód šablony e-mailu.
:guilabel:`<></>“ ikonou. Dynamické vložky (odkazující na pole v Odoo) jsou také k dispozici pro
použít v šabloně e-mailu.

Powerbox
--------

Funkce „PowerBox“ je obohacený textový editor s různými možnostmi formátování, uspořádání a vkládání textu.
Může být také použito k přidání funkcí XML/HTML do šablony e-mailu. Funkce powerbox je aktivována
pomocí znaku zpětného lomítka v těle e-mailového šablonu.

Když je v těle e-mailového šablonu zadán zpětlomový znak /, objeví se na něm
následující možnosti:

:guilabel:`Struktura“

- :guilabel:`Seznam s odrážkami`: Vytvořte jednoduchý seznam s odrážkami.
- :guilabel:`Číslovaný seznam“: Vytvořte seznam s číslováním.
- :guilabel:`Seznam úkolů“: Sledování úkolů pomocí seznamu úkolů.
- :guilabel:`Tabulka“: Vložte tabulku.
- :guilabel:`Separator“: Vložte horizontální čáru oddělující.
- :guilabel:`Citace“: Přidejte sekci citátu.
- :guilabel:`Kód`: Přidejte sekci kódu.
- :guilabel:`2 sloupce“: Převést na dvě sloupce.
- :guilabel:`3 sloupce“:Převést na tři sloupce.
- :guilabel:`4 sloupce“:Převést na čtyři sloupce.

:label:Formát

- :guilabel:`Hlava 1“: Velký nadpis.
- :guilabel:`Hlava 2`: Středně velký nadpis.
- :guilabel:`Hlava 3`: Malá podnadpisová část.
- :guilabel:`Změnit směr“: Změňte směr textu.
- :guilabel:`Text`: Blok odstavce.

:guilabel:`Média“

- :guilabel:`Obrázek“: Vložte obrázek.
- :guilabel:`Článek`: Odkaz na článek.

:guilabel:`Navigace“

- :guilabel:`Odkaz`: Přidej odkaz.
- :guilabel:`Tlačítko“: Přidejte tlačítko.
- :guilabel:`Termín“: Přidat konkrétní termín.
- :guilabel:`Kalendář“: Zarezervujte si termín.

:guilabel:`Zobrazit widgety“

- :guilabel:`Tři hvězdy`: Vložte hodnocení v rozmezí od 1 do 3.
- :guilabel:`Pětihvězdičkový rating“: Vložte hodnocení v počtu pěti hvězd.

:guilabel:`Základní bloky“

- :guilabel:`Podpis“: Vložte svůj podpis.

:guilabel:`Marketingové nástroje“

- :guilabel:`Dynamické vložky“: Vložte osobní obsah.

.. tip::
Pro použití kterékoliv z těchto možností klikněte na požadovanou funkci v nabídce napájení.
formátovat existující text pomocí možnosti související s textem (např. :guilabel:`Hlavička 1`, :guilabel:`Přepínač
směr, atd.), vyznačte text a poté zadejte klíč aktivátoru (zpětné lomítko) /.
Vyberte požadovanou možnost z roletkového menu.

.... obrázek:email_template/powerbox-feature.png
:align:center
:alt: Vlastnost Powerboxu v šabloně e-mailu.

.. viz též:
:ref:`Používáním dynamických proměnných <email_template/dynamic-placeholders>`

Editor kódu XML/HTML
--------------------

Chcete-li se dostat k editoru XML/HTML pro šablonu e-mailu, nejprve vstupte do režimu vývojáře.
„<vývojářský režim>“. Pak klikněte na ikonu „:guilabel:“ v pravém horním rohu šablony.
a pokračujte v editaci XML/HTML. Chcete-li se vrátit do standardního textového editoru, klikněte na :guilabel:`</`
ikonou znovu.

.. obrázek:email_template/html-code-editor.png
:align:center
:alt:HTML editor v e-mailovém šabloně.

.. varování:
Editor XML/HTML by měl být přístupný s opatrností, protože se jedná o kód zadního konce šablony.
Upravit kód může způsobit, že se e-mailový šablonu zhroutí ihned nebo při aktualizaci.
databáze.

... šablona e-mailu/dynamické proměnné:

Dynamické proměnné
--------------------

*Dynamické vložky* odkazují na určité pole v databázi Odoo a produkují tak jedinečná data.
vzor e-mailu.

.. příklad::
Mnoho společností se rádo přizpůsobí svým e-mailům s informací o zákazníkovi
aby upoutal pozornost. To lze v Odoo dosáhnout tím, že se odkazuje na pole uvnitř modelu
například v e-mailu může být uvedeno jméno zákazníka.
z pole „Zákazník“ na modelu „Prodejní objednávka“. Dynamický vložený text
pro tento prvek je: {{ objekt.partner_id }}.

Dynamické proměnné jsou kódovány tak, aby zobrazovaly pole zevnitř databáze. Dynamické proměnné
mohou být použity v poli „Tělo“ (položka „Obsah“) šablony e-mailu. Mohou také
mohou být použity v polích uvedených v záložce „Nastavení e-mailu“, a to v poli
e-mail a pole „Jazyk“.

Použít dynamické zástupce v těle e-mailu otevřete funkci **PowerBox**
Zadání znaku „/“ do těla šablony e-mailu pod záložkou „Obsah“. Vyhledat
Dole seznamu možností vyberte: „Marketingové nástroje“. Následně vyberte: „Dynamické
Zástupný symbol. Pak vyberte dynamický zástupný symbol ze seznamu dostupných možností a postupujte podle
na konfiguraci s požadovaným odpovídajícím poli v Odoo. Každý dynamický zástupný symbol
liší se konfigurací.

.. obrázek: email_template/dynamické_místa.png
:align:center
:alt:Použití dynamických vložek v e-mailovém šabloně.

.. poznámka::
Každá jedinečná kombinace polí, podmodelů a podpolí
Vytváří jiný dynamický místo pro vložení. Představte si ho jako kombinaci do pole, které je aktuálně vyplňováno.
vytvořen.

Pro vyhledávání dostupných polí stačí zadat název předního panelu (na uživatelském rozhraní).
pole v hledání. To najde výsledek z všech dostupných polí pro daný model.
pro kterou je vytvářen e-mailový šablon.

.. varování:
Změna e-mailových šablon není v rámci podpory Odoo možná.

Editor s bohatými možnostmi
----------------

Nástrojová lišta pro editaci bohatého textu se zobrazí, když bude vybraný text v šabloně e-mailu.
slouží k přepnutí nadpisu, velikosti písma či stylu, barvy, typu seznamu nebo odkazu.

.. obrázek: email_template/rich-text-editor.png
:align:center
:alt: Editor s bohatými možnostmi v šabloně e-mailu.

Obnovení e-mailových šablon
-------------------------

Pokud e-mailový vzor nebude fungovat kvůli změně kódu, může být resetován a obnoven.
zpět k výchozímu šabloně, stačí na tlačítko „Přepnout šablonu“
V horním levém rohu obrazovky a v šabloně se vrátí na výchozí hodnoty.

.. obrázek:: email_template/reset.png
:align:center
:alt:Resetování e-mailového šablonu.

Výchozí odpověď v e-mailových šablonách
--------------------------------

Pod záložkou „Konfigurace e-mailu“ v šabloně e-mailu je položka „Odpovědět“.
pole. Do tohoto pole zadejte e-mailové adresy, na které se odpovědi při zasílání e-mailů přesměrují.
masivně používaný tento šablonový vzor.

.. tip::
Přidejte více e-mailových adres oddělením čárkou (`,`) mezi adresy nebo dynamicky
místo proměnných.

.. obrázek: email_template/reply-to-template-sales.png
:align:center
:alt:Odpovědní pole šablony.

Pole „Odpovědět“ je používáno **pouze** pro masovou poštu (posílání e-mailů ve velkém množství).
e-maily můžete odesílat téměř ve všech aplikacích Odoo, které mají možnost zobrazení seznamu.

Zasílat hromadné e-maily, zatímco v pohledu „seznam“ zaškrtněte políčka vedle požadovaných záznamů
kde se mají e-maily odeslat, klikněte na tlačítko „Akce“ (jehož znakem je :guilabel:`⚙️
(ikona „Nástroje“) a vyberte požadovanou možnost e-mailu z rozevírací nabídky „Akce“. E-mail
Možnosti se mohou lišit v závislosti na konkrétním pohledu a aplikaci.

Pokud je možné odeslat e-mail, objeví se okno pro tvorbu pošty s hodnotami, které lze
definovány a přizpůsobeny. Tato možnost bude dostupná v tlačítku „Akce“ na stránkách
kde lze posílat e-maily ve velkém množství - například na stránce „Zákazníci“ v aplikaci CRM.
Toto je akce, která se děje po celé databázi Odoo.

.. obrázek:email_template/kompozitní-hromadná-pošta.png
:align:center
:alt:E-mailový kompozit s odpovědí zvýrazněnou v režimu masového rozesílání.

Transakční e-maily a odpovídající URL
===========================================

V Odoo může vyvolat odeslání automatických e-mailů více událostí. Tyto e-maily se nazývají
*transakční e-maily*, a někdy obsahují odkazy, které směřují na databázi Odoo.

Výchozí nastavení odkazů generovaných databází používá dynamickou hodnotu klíče web.base.url definovaného v systému
parametry. Více informací o tomto naleznete v části :ref:`systémové parametry
<název domény/URL webové stránky>.

Pokud není aplikace WebSite nainstalována, klíč web.base.url bude vždy nastaven na výchozí hodnotu
parametr používaný k generování všech odkazů.

.. důležité::
Klíč web.base.url může mít pouze jedinou hodnotu, což znamená, že v případě více webových stránek nebo
více společností v databázi, i když pro každou webovou stránku existuje specifický doménový název.
Linky, které vytváříme k sdílení dokumentu (nebo odkazy u transakčních e-mailů), mohou zůstat
stejné, bez ohledu na webovou stránku nebo společnost, která je spojena s odesláním e-mailu/dokumentu.

...... příklad::
Pokud hodnota systémového parametrů :guilabel:`web.base.url` je rovna
„https://www.mojefirma.cz“ a jsou zde dva samostatné subjekty v Odoo s různými
webové adresy: „https://www.mojefirma2.cz“ a „https://www.mojefirma1.cz“, které vytvoří odkazy
Odoo sdílet dokument nebo odeslat transakční e-mail přichází z domény:
„https://www.moufirma.cz“, bez ohledu na společnost, která dokument nebo e-mail odesílá.

To však není vždy pravidlem, protože některé aplikace Odoo (například e-commerce) mají odkaz
v databázi s aplikací *Website*. V takovém případě je pro konkrétní doménu
pro webovou stránku, URL v e-mailovém šabloně používá doménu definovanou na webové stránce.
odpovídající webové stránky společnosti.

...... příklad::
Když zákazník nakoupí na webu Odoo *eCommerce*, objednávka je zadána.
odkaz na tuto webovou stránku. V důsledku toho jsou v potvrzujícím e-mailu zaslaném zákazníkovi
použít doménové jméno pro konkrétní webovou stránku.

.. poznámka::
Dokument sdílený pomocí aplikace „Dokumenty“ vždy používá klíč `web.base.url`.
protože sdílený dokument není spojen s žádným konkrétním webem, což znamená, že URL
Vždy bude stejná (hodnota klíče web.base.url), bez ohledu na společnost, od které je sdílena.
Toto je známá omezení.

Pro více informací o konfiguraci domén se podívejte na dokumentaci :doc:`doménových jmen
</aplikace/weby/webové stránky/konfigurace/doménová jména>.

Aktualizace překladů v e-mailových šablonách
--------------------------------------------

V Odoo jsou e-mailové šablony automaticky překládány pro všechny uživatele v databázi.
jazyky nainstalované. Překlady nemusí být nutné měnit. Pokud je ale pro konkrétní
důvodem je některá z překladů, která by měla být změněna.

.. varování:
Stejně jako jakákoliv změna v kódu, pokud se překlad neprovádí správně (například
(včetně změn vedoucích k špatné syntaxi), může narušit šablonu a jako důsledek toho šablonu.
Ve výsledku bude prázdná.

Chcete-li upravit překlad, nejprve se přepněte do režimu vývojáře (:ref:`vývojářský režim <developer-mode>`). Pak
šablonu e-mailu, klikněte na tlačítko „Upravit“ a pak na jazykové tlačítko.
zastupované počátečními písmeny jazyka, který je v současné době používán (např. :guilabel:`EN` pro angličtinu).

.. obrázek: email_template/edit-language-template.png
:align:center
:alt: Upravit jazyk šablony.

.. poznámka::
Pokud v databázi není více jazyků instalovaných a aktivovaných nebo pokud uživatel
Pokud nemáte přístupová práva na správu, tlačítko pro jazyk se nezobrazí.

Zobrazí se okno s různými jazyky instalovanými v databázi. Z tohoto okna
Úpravy překladů jsou možné. Když provedete požadované změny, klikněte na
Tlačítko „Uložit“ k uložení změn.

.. obrázek:email_template/překlad-těla.png

:alt:Překlad těla šablony pro objednávku termínu.

.. poznámka::
Při úpravě překladů se v poli jazyka zobrazuje výchozí nastavený jazyk ve **tučném písmu**.
