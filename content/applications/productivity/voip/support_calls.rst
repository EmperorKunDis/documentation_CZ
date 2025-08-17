=======================
Podpora hovorů pomocí VoIP
=======================

.. |VOIP| nahradit za: zkratku: `VoIP (hlasová služba přes internetový protokol)`

Užitečný nástroj pro podporu zákazníků, Odoo |VOIP| se používá jako způsob kontaktu s klienty.
potřebují pomoc. Používání VoIP může zlepšit spokojenost zákazníků, snížit náklady na podporu a
umožňuje podporovatelům navigovat databázi Odoo během hovoru.

Místo toho, aby byli svázáni u stolu, mohou operátoři podpora volat z jakéhokoliv místa, kde mají přístup
Odoo: VoIP.

.. důležité:
Tato funkce vyžaduje alespoň jednu konfigurovanou frontu hovorů (:doc:`<axivox/call_queues>`).

.. viz též:
„Tutoriál Odoo: Práce jako podpora


Připojte se do fronty na podporu
========================

Pokud jsou nastaveny fronty hovorů (viz. :doc:`call queues <axivox/call_queues>`, začněte podporu telefonickým spojením
pořadí.

Začněte kliknutím na ikonu „Oi VoIP“ v pravém horním rohu databáze Odoo.
Zde klikněte na ikonu „klávesnice“ (Keyboard), poté zadejte číslo pro spojení s agentem.
číslo a klikněte na ikonu: `fa-phone`: guilabel: (telefon).

Jakmile operátor zavolá jejich *agentské spojení* , uslyší krátkou zprávu, která jim sdělí
V tomto okamžiku se operátorům zobrazí hlášení o připojení do fronty. Operátoři pak podle
strategie fronty hovorů správce: `doc:call_queue_strategy <axivox/call_queues>`. Když operátor podpory dostane
volání, v pravém dolním rohu obrazovky se zobrazí widget Odoo |VOIP| s číslem volajícího.
telefonní číslo, stejně jako jméno v případě, že je číslo spojeno s profilovým zákazníkem.

.. poznámka::
Když je podpora přidána jako statický agent do fronty hovorů,
nemusí se přihlásit do fronty, aby mohli přijmout hovory z této fronty.

Zavolejte zákazníkovi z podpůrného požadavku
=====================================

Jako součást každodenních úkolů podpůrného agenta mohou být požádáni o telefonování s klienty se zjištěnou podporou
vstupenek. S Odoo |VoIP| může podpora zůstat v databázi Odoo po celou dobu
workflow.

Na domovské stránce databáze klikněte na aplikaci Helpdesk, pak do helpdesku a poté otevřete
lístek. Pokud lístek již nemá naplánovanou hovorovou aktivitu, klikněte na:guilabel:„Aktivita“
v chatovací části lístku, pak nastavte aktivitu typu :guilabel:`Activity Type` na :guilabel:`Call“.
Vyplňte zbytek aktivity a nakonec klikněte na tlačítko „Zadat do kalendáře“.

.. obrázek: podpora/vytvorit-aktivitu-hovoru.png
:alt:Nastavení času pro aktivitu volání v podpoře.

Agent má tři možnosti, jak zavolat:

- Nechte kurzor nad poli „Telefon“ v lístku, pak klikněte na ikonu „Telefon“
:guilabel:`Volání“.
- V okně pro chat s jízdenkou klikněte na telefonní číslo zákazníka.
- V pravém horním rohu klikněte na ikonu „OI VoIP“ (VoIP) pro otevření
widget. V záložce „Další aktivity“ vyberte hovor a nakonec klikněte na


Pracovat během hovoru
------------------

Jakmile začne hovor s klientem, podpora může stále pohybovat se v databázi Odoo.
Dále jsou v widgetu |VOIP| ikony zkratek, které podpora může použít k přístupu ke společným
akcí, jako je odeslání e-mailu zákazníkovi nebo zobrazení jeho profilu.
:dokumentu: „Dokumenty, které může přístup k během hovoru.“

Operátor podpory může během hovoru také něco udělat:

- :icon:`fa-arrows-h` :guilabel:`(přenos hovoru)`: Přenesení hovoru na jiného člena týmu.
- :ikonka: `fa-microphone` :guilabel: (mikrofon): Technická podpora si během hovoru může vypnout
přivolání.
- :icon:`fa-pause` :guilabel:`(pause)`: Zavoláte na číslo a volající je převeden do stavu čekání.

Zajistit zpětnou vazbu na telefonické hovory
----------------------

Ve widgetu VoIP lze vykonávat některé běžné úkoly související s následováním, ale podpora stále může navigovat v Odoo.
pro úkoly, které nejsou k dispozici v widgetu.

Níže jsou uvedeny některé z běžných úkolů, které lze spravovat pomocí widgetu VOIP:

- Odešlete e-mail s dalšími kroky řešení problému zákazníkovi pomocí
:icon:`fa-envelope` :guilabel:`(poštovní schránka)`
- Aktualizujte adresu zákazníka kliknutím na ikonu :icon:`fa-user` :guilabel:`(uživatel)`
které otevírá jejich profil.
- Zarezervujte si druhé telefonní spojení s klientem kliknutím na ikonu „fa-clock-o“ :guilabel:„(hodiny)“.
ikona, nastaví pole :guilabel:`Activity Type“ na hodnotu :guilabel:`Call“ a poté vyplní
zbytek formuláře.

Ukončit podporu
--------------------

Když je čas ukončit hovor, podpora klikne na červené ikoně telefonu.
ikonu „Telefon“ v dolním pravém rohu widgetu |VOIP|. Když tak učiníte, bude
Záznam o tom, že byl vstupenka zakoupena.

Pokud ještě nebylo provedeno, pak operátor označí telefonní hovor jako dokončený.
to udělejte, přejděte na chatu s lístkem a najděte sekci „Plánované aktivity“ a pak
Klikněte na ikonu „Ověřeno“ a poté na „Hotovo“ v plánovaném hovoru, abyste jej odstranili z
:guilabel:„Další aktivity“ v widgetu VOIP.

Vyčkejte v pořadí na podporu
==========================

Když skončí směna agenta nebo když se chystá na přestávku, může se odpojit z podpůrného hovoru.
pořadí.

Začněte kliknutím na ikonu „Oi VoIP“ v pravém horním rohu databáze Odoo.
Odtud klikněte na ikonu „klávesnice“ (Keyboard), pak zadejte číslo *odpojení agenta*.
číslo a klikněte na ikonu: fa-phone :guilabel:"telefon".

Jakmile operátor zavolá své *agentské odpojovací číslo*, uslyší krátkou zprávu, která jim sdělí
Ví o tom, že jsou z fronty vyřazeni. Zde už jim podpora nebude poskytována.
volat, dokud se nezaregistrují.
