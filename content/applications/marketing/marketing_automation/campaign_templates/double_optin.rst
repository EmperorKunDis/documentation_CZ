=============
Dvojitý opt-in
=============

V některých zemích může být vyžadován dvojitý souhlas, tzv. potvrzený souhlas (opt-in).
pro marketingové komunikace kvůli zákonům proti SPAMu. Potvrzení souhlasu má i další výhody
a také: ověřuje e-mailové adresy, zabraňuje spamu a robotickým odběratelům, udržuje seznamy čisté.
obsahuje pouze kontakty, které jsou v seznamu odběratelů zahrnuty.

Při použití šablony kampaně Double Opt-in vytvoříte novou seznamu kontaktů s názvem Confirmed contacts.
je vytvářena v aplikaci Email Marketing a všechny nové kontakty z e-mailového seznamu jsou přidávány do
Přednastavený seznam Newsletter je zasílán potvrzující e-mail k dvojitému souhlasu. Kontakty, které
kliknutím na potvrzovací odkaz v e-mailu jsou automaticky přidány do seznamu *Potvrzené kontakty*.
mailing list v Odoo.

.. důležité:
Při použití šablony kampaně *Dvojitý opt-in* se kontakty zobrazí jen v seznamu *Potvrzené kontakty*.
se považuje za potvrzení souhlasu.

.. marketingová automatizace / šablona / použití dvojitého potvrzení:

Použijte šablonu pro dvojitý opt-in.
=======================================

Otevřete aplikaci Marketing Automation a vyberte Double Opt-in.
šablona kampaně pro vytvoření nové kampaně ke schválení souhlasu.

..tip:
Kampaně v předdefinovaných šablonách se **nezobrazují**, pokud existují již existující marketingové
Automatizované kampaně. Pro zobrazení šablon kampaní zadejte název kampaně (který
Do pole „Hledat…“ vložte (pokud neexistuje ve výpisu), pak stiskněte klávesu Enter.

Například hledání slova „prázdný“ zobrazí karty šablon kampaně znovu, dokud nebude prázdná.
Není kampaň s názvem „prázdný“ v databázi.

Konfigurace kampaně
----------------------

Při vytváření kampaně se načte nová přednastavená kampaň.

Kampaně má následující konfigurace cílového a filtračního objektu:

- :guilabel:`Jméno“: „Dvoufázové potvrzení“
- :guilabel:`Odpovědný“\*: Uživatel, který vytvořil kampaň.
- :guilabel:`Zákazník“: :guilabel:`Kontakt pro poštovní služby“
- :guilabel:`Uničnost na základě emailu“: :guilabel:`E-mailová adresa (Kontakt pro rozesílání)“
- Filtr:

  - :guilabel:`E-mailová adresa je nastavena“
  - :guilabel:`Černá listina“ :guilabel:`není nastavena“
  - :guilabel:`Seznamy na mail“ :guilabel:`obsahuje“ „Novinky“

*Pole „Zodpovědný“ je viditelné pouze v režimu vývojáře.

.. důležité:
Model kampaně „Cíl“ („Target“) by neměl být měněn. Změna cíle kampaně
:guilabel:`Základní cíl“ model s aktivitami v :guilabel:`Průběhu práce“ neplatí pro existující
aktivity v :guilabel:`Průběhu práce“.

Šablona kampaně „Dvojitý opt-in“ je určena pouze pro použití s :guilabel:`Kontaktem na mailu`.
model.

Kampaň načte dvě aktivity v sekci „Průběh“ kampaně: e-mail
akce s dětskou serverovou akcí, která se spustí při kliknutí.

Výchozí nastavení e-mailové aktivity „Potvrzení“ je nastaveno na :guilabel:`1 hodinu` po
začátek průběhu. Jinými slovy, e-mail je odeslán 1 hodinu po přidání nového kontaktu do
Seznam Newsletter.

E-mailová aktivita používá přednastavený e-mailový šablonu potvrzení, který obsahuje tlačítko
kliknout na odkaz, který potvrdí jejich souhlas.

Pro úpravu šablony e-mailu vyberte tlačítko „Šablony“ v horní liště.
v horní části kampaně. Poté v seznamu šablon vyberte e-mail „Potvrzení“
šablona.

Ujistěte se, že obsah e-mailového šablonu přizpůsobíte svým potřebám, ale je doporučeno zachovat
obsah potvrzovacích e-mailů o dvojím souhlasu je stručný a výstižný.

Výchozí tlačítko potvrzení v šabloně odkazuje přímo na databázi.
domovská stránka webu. Klikněte na tlačítko pro úpravu textu a URL adresy.

..tip:
Pro zajištění plynulého zážitku pro kontakt zvažte vytvoření stránky na :doc:`tématu kontaktu.
webové stránky <../../../websites/website/pages>, které vyjadřují poděkování kontaktu za
potvrzením jejich přihlášení k odběru newsletteru. Přidejte odkaz na tuto stránku do URL adresy
tlačítko potvrzení.

.. důležité:
E-mailový šablonu by měl obsahovat pouze jediný odkaz na potvrzení, kromě
odhlášení z odběru.

Kliknutí na jakýkoliv odkaz nebo tlačítko v potvrzovacím e-mailu kromě odhlášení
Tlačítko spouští akci serveru *Přidat do seznamu*.

Akce serveru pro děti „Přidat na seznam“ nemůže rozlišit mezi
více URL v e-mailu, kromě tlačítka „odhlásit se z odběru“, které je
v jakémkoliv bloku patičky.

Akce „Přidat do seznamu“ serverového kroku spouští okamžitě po kliknutí v rodičovském
Aktivita potvrzení e-mailu je detekována.

Při spuštění aktivita „Přidat do seznamu“ provede serverovou akci „Přidat na potvrzený seznam“,
automaticky přidávat kontakt do seznamu *Potvrzené kontakty*, pokud uživatel není v něm zahrnut.
v e-mailové konferenci.

Pro změnu akce serveru vyberte název aktivity pro otevření :guilabel:`Open:
Otevřete okno aktivit a upravte konfiguraci akcí serveru.

..tip:
Zvažte nastavení hodnoty :guilabel:`Expiry Duration`, aby se aktivita nevykonávala po
určité množství času.

.. důležité:
Neporušujte přednastavený kód v Pythonu v :guilabel:`Přidat do potvrzených
Pokud se rozhodnete přidat svůj server do seznamu serverů, může to způsobit změnu v cenové politice databáze.

Jakmile je konfigurace kampaně dokončena, zvažte spuštění testu podle návodu :doc:`Testování běhu <../testing_running>
aby se ověřilo, že kampaň funguje tak, jak má. Pokud je testování kampaně úspěšné,
:guilabel:`Začít“ kampaň, která začne odesílat dvojnásobné potvrzení o přijetí e-mailů do newsletteru
kontakty na seznamu adresátů a naplňte seznam „Potvrzené kontakty“ aktivními kontakty.

.. marketingová automatizace / šablona / dvojitý opt-in případ:

Případ použití double opt-in
======================

Příklad:
Před odesláním newsletterových e-mailů na databázi Odoo je potřeba vytvořit seznam kontaktů.
musí být získáni. Jedním ze způsobů, jak se předplatitelé shromažďují, je prostřednictvím registračního formuláře na webových stránkách.
Přidává kontakty do seznamu adresátů newsletteru při odeslání formuláře.

....... obrázek::double_optin/newsletter-signup.png
:synchronizace: střed
:alt:Přihláška k odběru newsletteru na webové stránce Odoo v zápatí.

Před odesláním jakýchkoliv marketingových e-mailů použijte šablonu „Dvojitý souhlas“.
</marketing_automation/template/using-double-optin> v aplikaci Marketing Automation k potvrzení
Marketingový souhlas s e-maily od kontaktů v seznamu Newsletter.

Po spuštění kampaně Double Opt-in zkontrolujte kontakty s dvojitým potvrzením v
*Potvrzené kontakty* seznamu emailů (:menuselection:`E-mailový marketing aplikace --> Seznamy e-mailů -->
Mailové konference`.

.... obrázek: double_optin/double-optin-metrics.png
:synchronizace: střed
:alt: Metriky aktivit na kampani.

Nyní je seznam potvrzených kontaktů připraven k použití pro rozesílání novinek.
e-maily z databáze Odoo.

.. viz též:
   - :doc:`../pochopeni_metrik`
   - :doc:`../../email_marketing/mailing_lists`
   - :doc:`/email_marketing`
