======================
Prodejní hovory s VoIP
======================

.. |VOIP| nahradit za: zkratku: `VoIP (hlasová služba přes internetový protokol)`

Používání VOIP zvyšuje efektivitu hovorů, snižuje náklady a umožňuje obchodníkovi přístup do Odoo.
databáze během hovoru. Namísto používání samostatného telefonu pro obchodní hovory může
volat přímo z databáze Odoo.

Tento článek se zabývá nastavením Odoo |VOIP| pro prodejní tým, který již má |VOIP| nakonfigurované.
Pokud není konfigurace VoIP nastavena, podívejte se na dokumentaci „Nastavení VoIP“ (<../voip>).
Začít.

.. viz též:
„Tutoriál Odoo: Prodejní hovory s VoIP
<https://www.odoo.com/slides/slide/sales-calls-with-voip-4562>

Udělejte obchodní telefonát
=================

Tento postup začíná v aplikaci CRM. Jako obchodník klikněte do příležitosti prodeje. Pokud
neexistuje již naplánovaná telefonická aktivita, klikněte na položku „Aktivita“ v příležitosti.
povídat si, pak nastavte typ aktivity na „Hovor“ a poté vyplňte
zbytek aktivity a nakonec klikněte na „Vytvořit plán“.

Od tady je tři možnosti, jak začít telefonní hovor s klientem:

- Přejděte na pole „Telefon“ v příležitostní kartě a pak klikněte na ikonu „Telefon“.
:guilabel:`Volání“.
- V okně s příležitostí klikněte na telefonní číslo zákazníka.
- V pravém horním rohu klikněte na ikonu „OI VoIP“ (VoIP) pro otevření
widget. V záložce „Další aktivity“ vyberte hovor a nakonec klikněte na


Pracovat během hovoru
------------------

Jakmile začne hovor s klientem, obchodník může stále procházet databází Odoo.
Dále jsou v widgetu |VOIP| ikony zkratek, které obchodník může použít k přístupu ke společným
akcí, jako je odeslání e-mailu zákazníkovi nebo zobrazení jeho profilu.
:dokumenty, které může prodejce během hovoru zobrazit (<voip_widget>).

Prodejce může během hovoru také něco udělat:

- :icon:`fa-arrows-h` :guilabel:`(přenos hovoru)`: Přenesení hovoru na jiného člena týmu.
- :icon:`fa-microphone` :guilabel:`(mikrofon)`: Zástupce společnosti může během hovoru snížit svou hlasitost.
- :icon:`fa-pause` :guilabel:`(pause)`: Zavoláte na číslo a volající je převeden do stavu čekání.

.. obrázek: sales_calls/voip-widget-call.png
:alt:VoIP widget se otevřel hovoru, který zobrazoval ikonky pro volání, které má obchodník k dispozici.

Zajistit zpětnou vazbu na telefonické hovory
----------------------

Widget VOIP může zvládnout některé běžné úkoly následné péče, ale prodejci stále mohou používat Odoo.
pro úkoly, které nejsou k dispozici v widgetu.

Níže jsou uvedeny některé z běžných úkolů, které lze spravovat pomocí widgetu VOIP:

- Odešlete e-mail s novými nabídkami produktů zákazníkovi pomocí ikonky „fa-envelope“
:guilabel:`(obálka)` ikonu.
- Aktualizujte adresu zákazníka kliknutím na ikonu :icon:`fa-user` :guilabel:`(uživatel)`
které otevírá jejich profil.
- Zarezervujte si druhé telefonní spojení s klientem kliknutím na ikonu „fa-clock-o“ :guilabel:„(hodiny)“.
ikona, nastaví pole :guilabel:`Activity Type“ na hodnotu :guilabel:`Call“ a poté vyplní
zbytek formuláře.

Vyžádejte nabídku během hovoru
--------------------------------

Pokud je zákazník připravený vidět nabídku na prodej během hovoru, může obchodník zaslat tuto
citace bez opuštění hovoru.

Pokud chce obchodník během hovoru zaslat nabídku, měl by být v příležitosti k prodeji.
zahájili hovor z této strany. Zde budou :doc:`posílat cenovou nabídku tak, jak obvykle
<../../prodej/prodej/faktury/vytvorit-fakturu>.

Přidanou hodnotou je, že zákazník může být na telefonu s prodejcem, když ten posílá e-mail.
citace je, že na konkrétní otázky lze odpovědět v reálném čase.

Ukončete prodejní hovor
------------------

Když je čas ukončit hovor, obchodník klikne na červené :icon:`fa-phone` :guilabel:`(telefon)`
ikonu v dolní pravé části widgetu VOIP. Když ano, hovor je zaznamenán v
hádky o příležitosti.

Pokud ještě nebylo provedeno, pak prodejce označí telefonní hovor jako hotový.
takže se přesuňte do chatu příležitosti a najděte část „Plánované aktivity“.
Klikněte na ikonu „Ověřeno“ a poté na „Hotovo“ v plánovaném hovoru, abyste jej odstranili z
:guilabel:„Další aktivity“ v widgetu VOIP.
