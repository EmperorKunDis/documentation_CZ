================
CRM gamifikace
================

V aplikaci CRM společnosti Odoo jsou k dispozici nástroje pro hodnocení a motivaci uživatelů
skrze přizpůsobitelné výzvy, cíle a odměny. Cíle jsou vytvářeny tak, aby se zaměřovaly na akce uvnitř
Aplikace CRM a může být sledována a odměňována automaticky prodejním týmem.

Konfigurace
=============

Chcete-li nainstalovat modul „Gamifikace CRM“, přejděte do aplikace Apps a klikněte na
do pole „Hledat…“ v horní části stránky a odstranit filtr „Aplikace“.
Do vyhledávacího pole zadejte „CRM Gamification“.

V modulu CRM Gamification klikněte na tlačítko „Instalovat“. Tento modul obsahuje cíle
a související výzvy pro aplikace CRM a Sales.

.. obrázek: gamifikace/gamifikace-modul-instalace.png
:align:center
:alt: Pohled na modul gamifikace v Odoo.

.. poznámka::
Pokud jsou nainstalovány obě aplikace CRM a Sales, modul CRM Gamification
automaticky nainstalován na databázi.

Chcete-li zobrazit nabídku nástrojů Gamification, nejprve zapněte režim vývojáře.

Poté přejděte na: „Nastavení aplikace --> Nástroje pro gamifikaci“.

.. obrázek: gamifikace/gamifikace-nástroje-menu.png
:align:center
:alt:Zobrazte si nástroje pro hraní v nastavení Odoo.

... /crm/create-rewards:

Vytvořte odznaky
=============

„Odměnky“ jsou udělovány uživatelům, když splní výzvu. Různé odměnky mohou být uděleny
podle typu úkolu a může být vydána více uživatelům podle časového limitu
Dosahují cíle.

Pro zobrazení stávajících odznaků nebo vytvoření nového přejděte na:
Nástroje pro gamifikaci --> Označení“.

.. obrázek:gamifikace/odznaky.png
:align:center
:alt: Pohled na stránku s odznaky v Odoo.

.. poznámka::
Některé odznaky lze udělit i mimo výzvy. Vyberte kartu Kanban pro požadovaný
připnout štítek, pak klikněte na „Povolit“. To otevře okno s názvem „Štítek povolení“. Vyberte
z uživatelského pole „Koho chcete odměnit?“.

Pokud chcete přidat další informace o tom, proč uživatel dostává odměnu, vložte je do pole níže.
Pak klikněte na tlačítko „Udělit odznak“.

Pro vytvoření nového odznaku klikněte na „Nový“ v horním levém rohu stránky, abyste otevřeli prázdnou formu.
Zadejte název štítku „Badge“, následovaný popisem.

Pole „Dávka“ určuje, kdy může být uděleno ocenění, a kdo jej udělí:

- :guilabel:Každý: Tento štítek může udělit každý uživatel ručně.
- :guilabel:Vybraný seznam uživatelů“: tento odznak mohou udělit pouze vybraní uživatelé.
Pokud je tato možnost vybrána, vytvoří se nový prvek :guilabel:`Uživatelé s oprávněním k přístupu`. Vyberte
zvolte vhodné uživatele ze seznamu.
- :guilabel:"Lidé s nějakými odznaky": tento odznak může udělit pouze uživatel, který již
byl udělen konkrétní odznak. Pokud je tato volba vybrána, vytvoří se nové pole.
:guilabel:`Požadované odznaky“. Vyberte z rozevíracího seznamu odznak, který musí uživatel mít.
předtím, než jí budou moci udělit ostatním.
- :guilabel:Nikdo, kdo byl přidělen výzvou“: tento odznak nemůže být ručně udělen, může
mohou být uděleny pouze výzvami.

Pro omezení počtu odznaků, které uživatel může poslat, zaškrtněte políčko „Měsíční limitované výdaje“.
zaškrtávací políčko, které nastavuje maximální počet udělených odznaků.
V poli „Počet omezení“ zadejte maximální počet odeslaných štítků.
měsíčně za osobu.

.. obrázek:gamifikace/vytvorit-znacku.png
:align:center
:alt:Stránka s podrobnostmi o novém odznaku.

.._crm/create-challenge:

Vytvořte výzvu
==================

Pro vytvoření výzvy přejděte do nastavení: „Nástroje pro gamifikaci“
Výzvy“. Klikněte na „Nový“ v levém horním rohu, abyste otevřeli prázdnou formu výzvy.

V horní části formuláře zadejte název výzvy.

Vytvořte pravidla přiřazování úkolů
-----------------------

Přiřazení výzvy konkrétním uživatelům vyžaduje použití jednoho nebo více pravidel přiřazování.

Klikněte do prvního pole pod nadpisem „Přidat výzvu“, vyberte parametr z
seznam s možnostmi definice pravidla. Poté klikněte do dalšího pole pro definici operátoru pravidla. Pokud
nutné, klikněte do třetího pole pro další definici parametru.

..tip:
Chcete-li zahrnout všechny uživatele s oprávněním v aplikaci Sales, vytvořte pravidlo se
parametry:

   - :guilabel:`Skupiny“
   - :guilabel:`je v`
   - „Prodej/Uživatel: Vlastní dokumenty“

.... obrázek:: gamification/pravidlo-priznani.png
:synchronizace: střed
:alt: Pohled na část formuláře s pravidly přiřazování úkolů.

V poli „Četnost“ vyberte časový rámec pro automatické hodnocení cílů.

Přidejte si cíle
---------

Výzvy mohou být založeny na jediném cíli nebo mohou obsahovat více cílů s různými cílovými body.
Přidejte si k výzvě cíl, klikněte na záložku „Cíle“ a poté na tlačítko „Přidat linii“.

V poli „Definice cíle“ vyberte z roletky cíl.
Pole „Stav“ automaticky aktualizuje podle stavu stanoveného na cíli.
definice.

..tip:
Modul CRM Gamification obsahuje přednastavené cíle zaměřené na prodejní týmy:

   - :guilabel:`Nové kontakty“
   - :guilabel:`Čas kvalifikovat lead“
   - :guilabel:`Dny k uzavření obchodu“
   - :guilabel:`Nové příležitosti“
   - :guilabel:`Nové objednávky“

Zadejte cíl na základě přípony pomocí „Suffix“.

Tyto kroky opakujte pro každý další cíl.

.. obrázek:: gamifikace/výzvy-cíle.png
:align:center
:alt:Karta s cíli v podobě úkolu.

Přidejte odměny
-----------

Dále klikněte na záložku „Odměna“. Vyberte odznaky, které chcete udělit
„Pro první uživatele“ a „Pro každého dalšího uživatele“ vybráním z
výběrové seznamy.

.. poznámka::
Badge se uděluje po dokončení výzvy. To je buď na konci běhu nebo
při konci termínu výzvy nebo když je výzva ručně uzavřena.

Po dokončení nastavení klikněte na tlačítko „Zahájení výzvy“ v levém horním rohu stránky.
začít výzvu.
