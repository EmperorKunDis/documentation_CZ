================
Příjezd a odjezd
================

Aplikace **Přítomnosti** společnosti Odoo umožňuje uživatelům, kteří jsou přihlášeni do databáze, zaznamenat svou přítomnost.
bez nutnosti vstupu do aplikace **Přítomnost** nebo použití pokladny. Pro menší
firmy, kde je každý zaměstnanec také uživatelem, může být tato funkce užitečná.

Uživatel může zkontrolovat příjezd a odjezd na hlavní obrazovce databáze Odoo nebo během používání jakékoliv aplikace.
Pro toto je v horním pravém rohu hlavního menu nad hlavním obsahem, které je vždy viditelné.
jaké aplikaci uživatel používá, a :icon:`fa-circle` :guilabel:`(červený kruh)` nebo
Ikona „fa-circle“ je viditelná. Klikněte na barevný kruh, abyste zobrazili
tlačítko pro návštěvu, které umožňuje zadat příchod nebo odchod.

..přítomnost/registrace:

Příjezd
========

Pokud je kruh u widgetu přítomnosti červený, znamená to, že uživatel není v tuto chvíli přihlášen. Klikněte
:ikona: „fa-circle“ :guilabel: (červený kruh) a zobrazí se widget přítomnosti, který zobrazuje
zelené tlačítko „Přihlášení“.

.. obrázek: check_in_check_out/check-in.png
:alt:Hlavní menu v horním pravém rohu s tlačítkem pro přihlášení zvýrazněné.

Když uživatel zadává své údaje do databáze, aplikace **Attendance** zaznamenává podrobnosti o umístění.
uživatel, včetně IP adresy a souřadnic GPS.

.. důležité::
Pro aplikaci **Přítomnosti** je nutné povolit počítači přístup k lokaci.
přístup k informacím o své poloze.

Pokud uživatel nevyužil v průběhu dnešního pracovního dne možnost přijít a odejít, tato tlačítka jsou jedinými
viditelný prvek v widgetu. Pokud uživatel dříve odhlásil a přihlásil se zpět, zobrazí se :guilabel:`Dnešní celkové číslo
Pole se zobrazí nad tlačítkem a celkový čas strávený v práci za den.
se zobrazí v tomto poli ve formátu „HH:MM“ (hodiny:minuty).

Klikněte na tlačítko „Přihlášení“ (:guilabel:`Check in`) a potvrďte své přihlášení.
:guilabel:„(červený kruh)“ v horním menu se změní na zelenou a widget se změní svým vzhledem.
dobře. Widget se aktualizuje tak, že uživatelé vidí, že jsou online, změnou zeleného
:guilabel:`Přihlášení“ tlačítko do žlutého :guilabel:`Odhlášení“ :icon:`fa-sign-out“
tlačítko.

Klikněte na libovolné místo obrazovky, abyste zavřeli widget přítomnosti.

Vyčkejte prosím
=========

Pokud je uživatel při placení poprvé, v horní části se objeví „Od HH:MM (ráno/večer)“.
widgetu s časem, kdy uživatel zadává datum a čas do pole pro datum. Pod tímto řádkem je
Čas, který uplynul od převzetí zavazadel, je zobrazen v formátu hh:mm.
S postupem času se tato hodnota aktualizuje tak, aby odrážela počet uplynulých hodin a minut.
uživatel se přihlásil.

Pokud uživatel dříve zadával čas příjezdu a odjezdu, jsou k dispozici další pole.
Vedle pole „Od“ se zobrazí pole „Od“ a „Do“, v němž je uvedena hodina a minuta (AM/PM).
Oba tyto pole obsahují stejné informace a jsou vyplněny posledním datem návštěvy.
Pod pole „Před HH:MM (ráno/večer)“ je zobrazen čas předchozího záznamu.
formát hodin:minut (HH:MM).

Dále se pod oběma těmito poli zobrazí pole „Celkem dnes“. To je
součet obou polí „Před HH:MM (ráno/odpoledne)“ a „Od HH:MM (ráno/odpoledne)“.
Je to celková doba, kterou by uživatel strávil na webu, pokud by se v tuto chvíli odhlásil.

S postupem času se oba pole „Od“ a „Dnes celkem“
Aktualizováno v reálném čase. Pro dokončení objednávky klikněte na žluté tlačítko „Přejít do pokladny“ :icon:`fa-sign-out`.
přepíše se widget docházky a zobrazí pole „Dnešní celkový čas“ s hodnotou odpočtu.
Zelená tlačítka „Prohlédnout“ se změní na zelené.
:guilabel:`Přihlášení“ tlačítko s ikonou „fa-sign-in“.

Když uživatel odhlásí ze systému, aplikace **Attendances** zaznamenává podrobnosti o poloze.
uživatel. Tato informace je uložena pouze v případě, že uživatel udělí souhlas.

.. obrázek: check_in_check_out/check-in-database-message.png
:alt:Pop-up okno, které se objeví při kontrole zaměstnance uvnitř databáze.

.. tip::
Počet přihlášení a odhlášení je neomezený. Uživatelé se mohou přihlásit a odhlásit, kolikrát chtějí.
bez jakéhokoliv časového úseku (hodnota 00:00). Každýkrát, když zaměstnanec vstoupí a opustí pracoviště,
informace je uložena a zobrazena na hlavním panelu **Přítomností** včetně docházky a
výběry bez časového limitu.
