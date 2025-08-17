==============
Sloučit kontakty
==============

Aplikace *Kontakty* společnosti Odoo umožňuje uživatelům spojit duplicitní kontakty bez ztráty dat.
informace v procesu. To udržuje databázi organizovanou a zabraňuje tomu, aby se kontakty
Kontaktováni více než jedním prodejcem.

..._kontakty/sloučit-dupl:

Sloučit duplicitní kontakty
========================

.. nebezpečí::
Spojování je nevratná akce. Nepřidávejte kontakty, pokud nejste naprosto jisti, že
by měly být spojeny.

Přejděte do aplikace Kontakty a vyberte ikonu :icon:`oi-view-list`.
:guilabel:`(seznam)` ikona. Vyberte dvě nebo více duplicitních kontaktů ze seznamu a zaškrtněte políčko
(vlevo dole) pro kontakty, které mají být sloučeny. Pak klikněte na ikonu „fa-cog“
ikonu „Akce“ a vyberte možnost „Sloučit“.

.. obrázek: sloučit/sloučit-menu.png
:align:center
:alt:Možnost sloučení kontaktů v aplikaci Kontakty.

Otevře se okno „Spojení“. Zde si zkontrolujte podrobnosti o kontaktech před
potvrzující, že by se měly sloučit. Pokud některé kontakty v seznamu neměly být sloučeny, klikněte na
:icon:`fa-times` :guilabel:`(smazat)` ikona vpravo dole u kontaktu.

.. tip::
Klikněte na jednotlivé kontakty, abyste otevřeli záznam pro daného kontaktu a zobrazili další informace.
informace.

.. obrázek:: sloučit/sloučení okna.png
:align:center
:alt:Okno pro sloučení v aplikaci Kontakty.

Klikněte na pole „Kontakt v cílové zemi“ a vyberte možnost ze seznamu.
V poli se vždy zobrazí kontaktní záznam, který byl do systému přidán jako první.

Po potvrzení informací v okně zkontrolujte položku „Sloučit kontakty“.

Sjednotit kontakty
====================

Po dokončení sloučení se objeví okno potvrzující jeho úspěšné dokončení.
obsahuje také tlačítko „Sjednotit kontakty“. Tato funkce hledá
duplicitní záznamy na základě zvolených kritérií a automaticky je spojuje nebo po ruce.
schválení.

Klikněte na tlačítko „Sjednotit ostatní kontakty“ a otevřete si dialogové okno „Sjednocení kontaktů“.
Okno s kontakty.

Vyberte jedno nebo více polí, která chcete použít při vyhledávání duplicitních záznamů.
Hledat lze podle následujících kritérií:

- :guilabel:`E-mail“
- :label:Jméno
- :guilabel:`Je společnost“
- :guilabel:`DPH“
- :guilabel:`Mateřská společnost“

.. poznámka::
Pokud je vybráno více polí, jsou navrženy pouze záznamy, které mají **všechna pole společná**.
jako duplicity.

Pokud je třeba, vyberte kritéria k použití pro vyloučení potenciálních duplikátů z vyhledávání.
Duplicitní záznamy lze vyloučit z vyhledávání na základě následujících kritérií:

- :guilabel:`Uživatel spojený s kontaktem“
- :guilabel:`Položky novin zobrazené v kontaktu“

Po potvrzení vyhledávacích kritérií klikněte buď na „Spojit s ručním ověřením“ nebo
„Spojit automaticky“ nebo „Spojit automaticky všechny procesy“.

Pokud je vybrána možnost „Sloučit s ruční kontrolou“, dokončete sloučení podle kroků uvedených v odkazu
nad kontakty/sloučit duplicitní kontakt“.
