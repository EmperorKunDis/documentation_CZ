===================
Vytvářejte SMS zprávy
===================

Nejprve klikněte na tlačítko „Vytvořit“ v hlavním rozhraní modulu SMS marketingu a Odoo odhalí
prázdný vzor SMS zprávy, který lze konfigurovat různými způsoby.

.. obrázek: create_sms/sms-create.png
:align:center
:alt: Vytváření šablony pro SMS marketing.

Nejprve mailem přidejte :guilabel:`Předmět`, který popisuje o čem je mailem.

Dále vyberte v poli „Příjemci“ osobu, které chcete zprávu poslat.
bude odeslána. Výchozí nastavení Odoa je „Seznam rozesílky“. Pokud to má být požadované
V poli „Příjemci“ zvolte, na jakou mailovou adresu má Odoo tento SMS odeslat.
Služba krátkých textových zpráv) do pole „Vybraná seznamová pošta“.

.. poznámka::
Pro vytvoření (nebo úpravu) seznamu e-mailů přejděte na: „Seznamy e-mailových adres – Seznam e-mailových adres“.
Odoo zobrazuje všechny dříve vytvořené seznamy e-mailových adres spolu s různými typy dat souvisejícími s nimi.
tento konkrétní seznam (např. počet kontaktů, rozesílání e-mailů, adresáti atd.)

Chcete-li se dozvědět více o e-mailech a kontaktech, podívejte se na :doc:`mailing_lists_blacklists`.

.. obrázek:: create_sms/sms-mailing-list.png
:align:center
:alt:Pohled na stránku se seznamem odeslaných zpráv v aplikaci pro SMS marketing.

Pro zobrazení všech možných variant v poli „Příjemci“ klikněte na pole a zobrazí se
volby, které nabízí Odoo.

Když je vybrána jiná pole než pole „Mailing List“, může uživatel zadat
vybranému pole se dostane ještě více - buď s výchozím filtrem rovnice příjemce
je automaticky zobrazena (která lze přizpůsobit podle potřeby každé firmy) nebo pokud žádný výchozí
Pokud je filtr příjemce aktivní, objeví se tlačítko „Přidat filtr“.

Kliknutím na tlačítko „Přidat filtr“ se zobrazí plně nastavitelná pole pro doménové pravidlo, která mohou
může být konfigurována podobně jako rovnice. Můžete vytvořit více pravidel pro příjemce, pokud je to nutné.

Pak Odoo odesílá SMS pouze adresátům, kteří se shodují s
jakýkoliv kritérium, které je v těchto polích nastaveno. Můžete přidat více pravidel.

Příklad:
Pokud je vybrána položka „Kontakt“, jsou všechny záznamy v databázi Odoo (dodavatelé,
zákazníci atd. obdrží SMS (krátkou zprávu) - výchozí nastavení, pokud není jinak specifikováno.
Specifické adresní pravidla se zadávají.

Příklad: následující zpráva bude odeslána pouze kontaktům v databázi, kteří jsou umístěni
Spojené státy (např. „Země“ > „Název země“ rovná se „Spojené státy“) a oni ještě
samy sebe zaregistrovali do černé listiny (např. „Černá listina“ > „je“ > „nepovinný parametr“).

.... obrázek: vytvořit_sms/kontakt-adresát.png
:synchronizace: střed
:alt: Kontaktujte příjemce na SMS marketingu.

Spisování SMS zpráv
--------------------

Do pole s textem zadejte obsah SMS (služba krátkých zpráv).
:guilabel:„Obsah SMS“ záložka. Do textového pole lze také vkládat odkazy a emotikony. Pod textovým polem se nachází
ukazuje kolik znaků je v zprávě a také kolik SMS (krátká zpráva)
Zasílání služebních zpráv, které budou potřeba k doručení kompletní zprávy.

..tip:
Chcete-li zkontrolovat cenu odeslání SMS do dané země, klikněte na
:guilabel:`Informace“ ikonu.

.. obrázek: create_sms/sms-cena-kontrola.png
:align:center
:alt: ikona kontroly ceny SMS.

.. poznámka::
Kredity musíte zakoupit u společnosti Odoo, abyste mohli využívat aplikaci SMS marketing.
:zkratka: SMS zprávy nebudou odeslány bez kreditu.

.. viz též:
„FAQ Odoo SMS <https://iap-services.odoo.com/iap/sms/pricing>“

Sledování odkazů v SMS zprávách
--------------------------------

Při použití odkazů v zprávách SMS (Short Message Service) automaticky generuje
Sledovat odkazy a shromažďovat analytická data a metriky týkající se konkrétních odkazů.
je k nalezení v sekci „Nastavení“ -> „Sledovač odkazů“.

.. obrázek: create_sms/sms-link-tracker.png
:align:center
:alt:Stránka služby Link Tracker.

Upravte nastavení SMS
===================

V nastavení SMS šablony je možnost „Zahrnout
odhlášení odběru“ a pokud je aktivní, umožňuje odběrateli se z odběru e-mailů odhlásit.
vyhýbat se všem budoucím rozesílkám.

Zaměstnanec může být označen jako „Odpovědný“ v sekci „Sledování“.
kartě „Nastavení“.

.. obrázek: create_sms/sms-settings-tab.png
:align:center
:alt: Nastavení SMS.

Odesílejte SMS zprávy
=================

Jakmile je poštovní zásilka vytvořena, vyberte si, kdy má Odoo doručit zprávu ze seznamu níže:

- :guilabel:`Odeslat“: okamžitě odesílá zprávu. Zvažte použití této možnosti, pokud se adresáti
je velmi propracovaná, nebo v případě rychle se blížících termínů, jako je „slevová akce“.
- :guilabel:`Plán“: vyberte den (a čas), kdy má Odoo odeslat e-mailovou zprávu. To je obvykle
Nejlepší možností pro zasílání pošty související s konkrétním událostem je taková metoda, která může být také použita k propagaci.
Slevové akce nebo pomoc při plánování obsahového plánu společnosti v předstihu.
- :guilabel:`Testování“: umožňuje odeslat SMS (krátkou zprávu) na jednu nebo více
pro účely testování. Pamatujte na použití čárky mezi telefonními čísly, pokud je uvedeno více čísel.
jako příjemci.
