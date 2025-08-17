================
Obědová politika
================

V aplikaci Lunch společnosti Odoo je nutné mít někoho, kdo bude spravovat objednávky, dodavatele a
produktů. Dále je potřeba někdo za objednávky zodpovídat a zaměstnance informovat o
Je jim rozkaz doručen. Může se jednat o stejnou osobu.

Objednávky lze zrušit, odeslat do prodejny nebo vyzvednout.
Při příjezdu potvrdil objednávku a zaměstnanci mohou být informováni.
<oběd/upozornění>, ať už z přehledu „Dnešní objednávky“ na panelu <lunch/todays-orders> nebo
:ref:`Dashboard dodavatelů<lunch/control_vendors>“.

Pro správu aplikace Lunch je potřeba mít odpovídající práva administrátora. Ty lze získat
Můžete si ji nastavit tak, že se v aplikaci „Nastavení“ přesunete do části „Správa uživatelů“.
Pak klikněte na požadovaného uživatele a zobrazí se přístupová práva.

Pro více informací o právech přístupu se podívejte na stránku :doc:`Přístupová práva
<https://www.phpbb.com/documentation/> dokumentace.

.. poznámka::
Zobrazit lze pouze uživatelům s právy správce.
:guilabel:`Konfigurace“ nabídky v aplikaci Lunch.

.._oběd/objednávky dnešní:

Dnešní rozkazy
==============

Pro zobrazení a správu objednávek za den přejděte na: „Obědová aplikace --> Správce -->
Dnešní objednávky“. Všechny objednávky za den jsou zobrazeny v seznamovém pohledu na :guilabel:`Dnes
Dashboard objednávek s filtrem dnešních objednávek a seřazených podle dodavatele
výchozí.

Následující informace se objevují v seznamu:

- :guilabel:`Datum objednání“: datum, kdy byla objednávka zadána.
- :guilabel:`Dodavatel`: dodavatel, od kterého je produkt objednáván.
- :guilabel:`Produkt“: konkrétní produkt objednaný zákazníkem.
- :guilabel:`Doplňky“: všechny doplňky, které byly k produktu vybrány.
- :guilabel:`Poznámky“: jakákoliv informace, která je potřeba zaslat dodavateli.
- :guilabel:`Uživatel“: uživatel, který si objednal produkt.
- :guilabel:`Místo oběda“: místo, kde je produkt určen k dodání.
- :guilabel:`Cena celkem“: Celková cena produktu včetně všech příplatků.
- :guilabel:`Stav produktu“: aktuální stav produktu.
- :guilabel:Společnost: společnost, u které byla objednávka zadána.
multifirmový databázový systém.

.. obrázek: management/dnes.png
:alt: Seznam, který se zobrazuje v přehledu Dnes objednané položky s filtry a sloupcem nahoře
jsou zvýrazněny.

...oběd/zrušit:

Zrušit objednávky
-------------

Zrušit objednávku může každý uživatel, nejen majitelé aplikace **Lunch**.

Aby bylo možné zrušit objednávku od dodavatele, musí být jednotlivé položky rušeny postupně.

Na panelu „Dnešní objednávky“ se zobrazí tlačítko „Zrušit“
v pravém dolním rohu každé produktové řady, která může být zrušena. Klikněte na ikonu:
Tlačítko „Zrušit“ k zrušení objednávky pro konkrétní produkt.

.. poznámka::
Zrušit lze pouze objednávky s červeným štítkem „Stav“ s hodnotou „Objednáno“.

.. obrázek: management/zrušit.png
:alt:Zadání řádků objednávky s vyznačeným tlačítkem pro zrušení.

... oběd/objednávky:

Vyřizujte objednávky
-----------

Prvním krokem v řízení aplikace Lunch je odeslání objednávek dodavatelům.

Když jsou objednávky připraveny k odeslání, manažer zodpovědný za odesílání objednávek **musí**
objednávky u dodavatele mimo databázi (telefonická objednávka, online objednávka atd.)

Jakmile jsou objednávky odeslány dodavatelům, klikněte na tlačítko „Odeslat objednávku“
Pozor, u každého prodejce je uvedeno jeho jméno a telefonní číslo.

Jakmile je objednávka odeslána, tlačítko „Odeslat objednávky“ se změní na „Potvrdit objednávky“.
Sloupec „Stav“ je aktualizován z červených štítků „Přijato“ na modré štítky „Odesláno“.
značky, které ukazují, že objednávka byla odeslána dodavateli. Uživatelé, kteří si zadali objednávku v
Aplikace **Oběd** používá tagy :guilabel:`Stav objednávky`, aby sledovala své objednávky.

.. obrázek: management/send.png
:alt:Objednávka prodejce s tlačítky Zrušit a Odeslat objednávku zvýrazněnými.

... oběd/potvrdit objednávku:

Potvrďte objednávky
--------------

Po odeslání objednávky dodavateli následuje potvrzení objednávek po jejich přijetí.
byla dodána.

Na panelu „Dnešní objednávky“ klikněte na tlačítko „Potvrdit objednávku“.
je umístěn vedle jména a telefonního čísla prodejce.

Jakmile je objednávka potvrzena, zmizí tlačítko „Potvrdit objednávky“ a sloupec „Stav“.
je aktualizován z modrých štítků „Odesláno“ na zelené štítky „Přijato“, což znamená, že
Zadané objednávky byly doručeny.

Dále je k dispozici tlačítko „Zrušit“ na konci každé řady produktů.
tlačítko „Odeslat upozornění“.

Pokud je třeba, místo potvrzení všech produktů od dodavatele lze jednotlivé produkty
může být potvrzeno jednotlivě. Pro potvrzení konkrétního produktu klikněte na ikonku :icon:`fa-check
Tlačítko „Potvrdit“ na konci řádku produktu.
výrobky s touto metodou zůstává na řádku dodavatele tlačítko „Potvrzení objednávky“.

.. obrázek: management/potvrzení.png
:alt:Dashboard Dnes objednané položky s dvěma různými způsoby potvrzení objednávky zvýrazněnými.

.. příklad::
Dodavatel dostane objednávku na tři pizzy a objednávku na česnekové koblihy. Když doručovatel
Když se kuchařka zeptá na přípitek, manažer Lunchu si všimne, že chybí houbové knedlíky.

Ředitel nejprve označí tři pizzy jako přijaté potvrzením jednotlivých produktů.
s tlačítkem „Potvrdit“ na konci každé řady produktů.

Později, když dodavatel doručí párky s česnekem, může manažer buď kliknout
:ikona: „fa-check“ tlačítko k potvrzení v řádku s cibulovými uzlíky nebo
Klikněte na tlačítko „Potvrdit objednávky“, které se objeví vedle jména a telefonního čísla dodavatele.
číslo.

... oběd/upozornit:

Informujte zaměstnance
----------------

Po obdržení produktů a potvrzení objednávek musí být zaměstnanci informováni o
jejich objednávky byly doručeny a jsou připraveny k vyzvednutí.

Na rozdíl od zasílání a potvrzení objednávek musí být oznámení zaslána jednotlivě a nelze je poslat
série.

K oznámení uživateli, že zboží dorazilo, klikněte na ikonu „fa-envelope“ a poté na „Odeslat
Tlačítko „Oznámení“ na konci každé produktové řady. Uživateli je odeslána e-mailová zpráva, která ho upozorňuje
Dodávky jejich produktů proběhly.

... oběd/kontrola dodavatelů:

Kontrola dodavatelů
===============

Všechny objednávky všech dodavatelů, jakéhokoliv data, najdete v přehledu *Kontrola dodavatelů*.
Přejděte na: „Obědová aplikace -> Správce -> Kontrola dodavatelů“.

Seznam objednávek se zobrazuje v přehledovém výpisu, řazeném podle „Dodavatele“ (viz guilabel:Vendor). Seznam se načítá
Všichni dodavatelé rozšířili svůj výpis na všechny řádky objednávky pro každého dodavatele.

Následující informace se objevují v seznamu:

- :guilabel:`Datum objednání“: datum, kdy byla objednávka zadána.
- :guilabel:`Dodavatel`: dodavatel, od kterého je produkt objednáván.
- :guilabel:`Produkt“: konkrétní produkt objednaný zákazníkem.
- :guilabel:`Doplňky“: všechny doplňky, které byly k produktu vybrány.
- :guilabel:`Poznámky“: jakákoliv informace, která je potřeba zaslat dodavateli.
- :guilabel:`Uživatel“: uživatel, který si objednal produkt.
- :guilabel:`Místo oběda“: místo, kde je produkt určen k dodání.
- :guilabel:`Cena celkem“: Celková cena produktu včetně všech příplatků.
- :guilabel:`Stav produktu“: aktuální stav produktu.
- :guilabel:Společnost: společnost, u které byla objednávka zadána.
multifirmový databázový systém.

Objednávky lze zrušit, odeslat do prodejny nebo vyzvednout.
Při příjezdu potvrdil objednávku a zaměstnanci mohou být informováni.
<oběd/upozornění> stejným způsobem jako na :ref:`Dnešní objednávky <oběd/todays-orders>“.
přístrojová deska.

.. obrázek: management/kontrola.png
:alt: Zobrazení seznamu všech objednávek, jak je vidět na přehledu dodavatelů v Dashboardu.

.. poznámka::
Rozdíl mezi panelu „Dnešní objednávky“ a „Objednávky dnes“ je v tom, že
:ref:`Dashboard dodavatelů <lunch/control_vendors>` je takový, že uživatelé mohou vidět pouze *dnešní objednávky*.
**ukazuje pouze objednávky za aktuální den, zatímco panel „Kontrola dodavatelů“
zobrazuje všechny objednávky v aplikaci Lunch.

.. viz též:
   - :doc:`../obed`
   - :doc:`uživatelské účty“
