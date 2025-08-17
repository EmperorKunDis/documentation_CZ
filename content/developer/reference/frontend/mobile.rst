.. odkaz/mobil:

=================
Mobilní JavaScript
=================

Úvod
============

V Odoo 10.0 jsme vydali mobilní aplikaci, která umožňuje přístup k všem **aplikacím Odoo**
(i vaše vlastní moduly).

Aplikace je kombinací **Odoo Web** a **Nativních mobilních komponentů**.
je nativní mobilní aplikace s WebView kontejnerem pro Odoo Web.

Tato stránka dokumentuje, jak můžete přistupovat k mobilním nativním komponentám jako je fotoaparát.
Vibrace, oznámení a hlášení prostřednictvím webu Odoo (pomocí JavaScriptu).
nemusíte být mobilní vývojář, pokud znáte Odoo JavaScript API, můžete
mít přístup k všem dostupným funkcím mobilu.

.. varování:
Tyto funkce fungují pouze s verzí Odoo Enterprise 10.0 a vyšší

Jak to funguje?
=================

Vnitřní fungování mobilní aplikace:

.. obrázek: mobil/mobilni-prace.jpg

Samozřejmě jde o stránku, která se načítá v mobilním nativním webovém kontejneru.
integrována tak, že můžete přistupovat k nativním zdrojům z vašeho webu.
JavaScript.

Webové stránky (Odoo Web) jsou na vrcholu každé vrstvy, kde druhá vrstva je most
mezi Odoo Web (JS) a nativními mobilními komponentami.

Každá volání z JavaScriptu prochází přes most a most.
přenese ji do původního vyvolavatele, aby tuto akci provedl.

Když nativní komponenta splnila svou práci, je znovu předána do mostu.
Výstup v JavaScriptu získáte.

Čas zpracování požadavku komponentou Native závisí na tom, co žádáte
z nativních zdrojů, například z fotoaparátu nebo polohy pomocí GPS.

Jak s ním zacházet?
==============

Stejně jako webový framework Odoo, mobilní rozhraní lze použít kdekoli pomocí objektu z
**web_mobil.rpc**

.. obrázek: mobil/odoo_mobile_api.png

Mobilní objekt RPC poskytuje seznam metod, které jsou k dispozici (to funguje pouze s mobilním
aplikace (app).

Zkontrolujte, zda metoda existuje, a poté ji spusťte.

Metody
-------

.. poznámka: Každá metoda vrací objekt jQuery.Deferred, který vrací
a datová struktura JSON

Zobrazte Toast v zařízení
~~~~~~~~~~~~~~~~~~~~

... funkce ...: zobrazit hlášení

:parametrem objektu args: **zpráva** zobrazovaný text

Toast poskytuje jednoduchou zpětnou vazbu o provedené operaci ve formě malého okna.
vyplňuje potřebný objem prostoru pro zprávu a aktuální činnost
zůstává viditelný a interaktivní.

... kódový blok: JavaScript

mobil.metody.zobrazitToast({'zpráva': 'Zpráva odeslána'});

.. obrázek: mobil/toast.png

Vibrační zařízení
~~~~~~~~~~~~~~~~

..js:funkce:vibrace

:param args:Vibruje neustále po dobu zadanou v parametrech
(v milisekundách).

Vibrujte mobilní zařízení po dobu danou.

... kódový blok: JavaScript

mobile.methods.vibrace({'délka': 100});

Show svačinka s akcí
~~~~~~~~~~~~~~~~~~~~~~~~~

... funkce: zobrazitNápovědu

:parametrem objektu args: (*povinné*) **Zpráva**, která se zobrazí v liště a akce **tlačítko s názvem** v liště (volitelně)
:vrací: „Pravda“ v případě kliknutí uživatelem na tlačítko „Akce“, „Nepravda“ v případě automatického zavření SnackBaru po nějaké době.

Svačinové bary poskytují lehké zpětnou vazbu o operaci. Ukazují krátký
zpráva v dolní části obrazovky na mobilu nebo v levém dolním rohu u větších zařízení.
Svačinové bary se zobrazují na obrazovce jako první a může být pouze jeden.
zobrazit v určitém čase.

... kódový blok: JavaScript

mobile.methods.showSnackBar({'message': 'Zpráva byla smazána', 'btn_text': 'Vymazat'}).then(function(result){
pokud (result) {
            // Do undo operation
}
            // Snack Bar dismissed
        }
    });

.. obrázek: mobil/svačinka.png

Zobrazení notifikace
~~~~~~~~~~~~~~~~~~~~

..js:funkce:zobrazitNotifikaci

:parametrem objektu args: **nadpis** (první řádek) oznámení, **zpráva** (druhý řádek) oznámení v běžném oznámení.

Oznámení je zprávou, kterou můžete uživateli zobrazit mimo vaši aplikaci.
obvyklé uživatelské rozhraní aplikace. Když systém pošle oznámení,
prvně se objeví jako ikona v oznámení. Chcete-li zobrazit podrobnosti,
oznámení, uživatel otevře notifikační lištu. Oba typy
Oblast a oznamovací lišta jsou systémem ovládané oblasti, které může uživatel
v jakoukoliv denní či noční dobu.

... kódový blok: JavaScript

mobile.showNotification({'title': 'Základní notifikace', 'message': 'Toto je test pro základní notifikaci'});

.. obrázek: mobil/mobilni_upozorneni.png


Vytvořit kontakt v zařízení
~~~~~~~~~~~~~~~~~~~~~~~~

..js:funkce: přidat kontakt

:parametrem args: Dikta se všemi kontaktními údaji. Možné klíče (jméno, mobil, telefon, fax, email, webová stránka, ulice, ulice2, země_id, stát_id, město, poštovní směrovací číslo, rodič_id, funkce a obrázek)

Vytvořit nový kontakt s uvedenými údaji.

... kódový blok: JavaScript

kontakt: {
"jméno": "Michel Fletcher",
"mobil": "9999999999",
"telefon": "7954856587",
'fax': '765898745',
"e-mail": "michel.fletcher@agrolait.example.com",
"webová stránka": "http://www.agrolait.com",
„ulice“: „69 Rue de Namur“,
"ulice2": false
'country_id': [21, 'Belgie']
'state_id': false
„město“: „Wavre“,
'zip': '130 00',
'rodiče': [8, 'Agrolait']
'funkce': 'Analytik',
„obrázek“: „<<datová zpráva v Base64 pro obraz>>“.
    }

mobile.metody.přidatKontakt(kontakt);

.. obrázek: mobil/mobilni-kontakt-vytvorit.png

Skenování čárových kódů
~~~~~~~~~~~~~~~~~

..js:funkce: skenovat čárový kód

:vrací: Skenovaný „kód“ z jakéhokoliv čárového kódu

Barcode API detekuje čárové kódy v reálném čase na zařízení a ve všech orientacích.

Barcode API dokáže číst následující typy čárových kódů:

* 1D čárové kódy: EAN-13, EAN-8, UPC-A, UPC-E, Code-39, Code-93, Code-128, ITF, Codabar
* 2D kódy: QR kód, Data Matrix, PDF-417, AZTEC

... kódový blok: JavaScript

mobile.metody.snímačKódu().pak(funkce(kód){
Pokud je kód platný,
            // Perform operation with the scanned code
        }
    });

Přepínání účtu v zařízení
~~~~~~~~~~~~~~~~~~~~~~~~~~~

..js:funkce: přepnout účet

Použijte funkci přepínání účtů, abyste se na zařízení mohli přepnout mezi různými účty.

... kódový blok: JavaScript

mobile.metody.přepnoutÚčet();

.. obrázek: mobil/přepnout-účet-mobilu.png
