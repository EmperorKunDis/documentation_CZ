============
Překlady
============

Váš web je zobrazen v jazyce, který odpovídá prohlížeči návštěvníka.
jazyk není na webu instalován a přidán, obsah se zobrazuje v
:ref:`výchozí jazyk <translate/default-language>“. Když jsou nainstalovány další jazyky, uživatelé
Mohou si vybrat svůj preferovaný jazyk pomocí :ref:`vybírače jazyka <translate/language-selector>`.

Funkce automatického překladu na vašem webu umožňuje
standardními podmínkami a poskytuje nástroj pro ruční překlad obsahu.

Nainstalujte jazyky
=================

Přeložit svůj web je možné teprve poté, co si nejdříve nainstalujete jazyk.
Požadované jazyky a přidejte je na svůj web. Chcete-li tak učinit, přejděte na:
Konfigurace --> Nastavení a klikněte na ikonu „Přidat jazyk“ v
V sekci „Informace o webu“ v dialogovém okně vyberte jazyky, které chcete přidat.
z nabídky vyberte požadované:guilabel:„Webové stránky k překladu“ a
Klikněte na „Přidat“.

Chcete-li upravit jazyky vašich webových stránek, přejděte na: `Webové stránky – Konfigurace – Nastavení`.
Přidejte nebo odeberte požadované jazyky do/z pole :guilabel:`Jazyky` v
v sekci „Informace o webu“.

..tip:
Alternativně můžete po instalaci jazyků přidat z :ref:`jazykového menu.
Selector <překladač/jazyková volba>. Možná budete muset obnovit stránku, abyste viděli nový.
jazyk.

.._přeložit/jazyk-výchozí:

Výchozí jazyk
----------------

Pokud máte na svých stránkách více jazyků, můžete nastavit výchozí jazyk tak, aby se používal v případě
jazyk prohlížeče návštěvníka není dostupný. Chcete-li tak učinit, přejděte na:
Konfigurace –> Nastavení“, vyberte jazyk v poli „Výchozí“.

.. poznámka::
Toto pole je viditelné pouze v případě, že do vašeho webu nainstalujete více jazyků.

.._přeložit/jazyková-selektor:

Jazyková nabídka
=================

Návštěvníci vašich webových stránek si mohou zvolit jazyk pomocí výchozího jazykového filtru.
sekci „Autorská práva“ na konci stránky.

#Přejděte na svůj web a klikněte na „Upravit“.
#Klikněte na jazykový výběr v bloku „Autorská práva“ a přejděte do
:guilabel:`Ochrana autorských práv“ v části webového editoru.
#Zadejte pole „Jazyk“ s buď „Výběrem“, nebo „Přímým zadáním“.
Klikněte na „Žádné“ pokud nechcete zobrazit jazykový filtr.

.. obrázek: translate/language-selector.png
:alt:Přidat nabídku jazykového výběru.

#Klikněte na tlačítko „Uložit“.

..tip:
Můžete také přidat jazyková tlačítka do hlavičky stránky.
takže klikněte na blok „Hlavička“ a přejděte do sekce „Navigace“, abyste mohli upravit
:guilabel:`Jazyková nabídka“.

.._přeložit/přeložit:

Přeložte svůj web
======================

Vyberte si požadovaný jazyk z nabídky jazyka a uvidíte svůj obsah v jiném jazyce.
Poté klikněte na tlačítko „Přeložit“ v pravém horním rohu, abyste ručně aktivovali
překladový režim, ve kterém můžete překládat věci, které nebyly automaticky přeloženy pomocí Odoo.

Přeložené textové řetězce jsou zvýrazněny zeleně, textové řetězce, které nebyly přeloženy
jsou automaticky zvýrazněny žlutě.

.. obrázek::přeložený text.png
:alt:Přepnutí do režimu překladu

V tomto režimu můžete přeložit pouze text. Chcete-li změnit strukturu stránky, musíte upravit šablonu
stránka, tedy stránka v původním jazyce databáze. Kdykoliv provedete změnu na hlavní stránce
jsou automaticky aplikovány na všechny překlady.

Chcete-li nahradit původní text překladem, klikněte na blok, upravte jeho obsah a
:guilabel:`Uložit“.

.. poznámka::
Pokud web podporuje více jazyků, struktura základní adresy URL zůstává stejná.
jazyky, zatímco konkrétní prvky jako názvy produktů nebo kategorie jsou přeloženy. Například
„https://www.mojespolecnost.cz/eshop/produkt/moje-produkce-1“ je anglická verze stránky produktu.
„https://www.mojespolecnost.cz/cs/eshop/produkt/moje-produkty-1“ je česká verze stejného
stránka. Struktura (/eshop/produkt/) zůstává stejná, ale přeložené prvky (např. produkt)
jméno) se přizpůsobit vybranému jazyku.

..tip:
Jakmile je požadovaný jazyk nainstalován, můžete některé položky z administrace přeložit (např.
název produktu v podobě produktu). Chcete-li tak učinit, klikněte na jazyková označení (např. :guilabel:`EN`)
text, který chcete přeložit, a přidejte překlad.

Zobrazování obsahu podle jazyka
------------------------------

Můžete skrýt obsah (například obrázky nebo videa), v závislosti na jazyce. Chcete-li tak učinit:

#Klikněte na tlačítko „Upravit“ a vyberte prvek webové stránky.
#Přejděte do sekce „Text – obrázek“ a nastavte viditelnost.
#Klikněte na „Žádné podmínky“ a vyberte „Pouze v případě“.
#Přejděte na „Jazyky“ a konfigurujte podmínku (podmínky), která se má použít, vybráním
:guilabel:`Zobrazit pro“ nebo :guilabel:`Skrytý pro“, klikněte na „Vybrat záznam“.
rozhodnout, které jazyky jsou zasaženy.
