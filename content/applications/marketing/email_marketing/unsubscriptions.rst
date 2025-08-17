==================================
Správa odhlášení (černá listina)
==================================

Poskytnutí příjemcům možnosti odhlásit se z rozesílek není jen chytrý byznys
praxe je často právní povinností. Povolit příjemcům odhlásit se z e-mailové adresy
Vytváří u publika pocit důvěry a kontroly. Pomáhá také firmám vypadat více
upřímnější a méně „spamový“.

Odhlásit se a zablokovat
=========================

Kromě možnosti odhlásit se z konkrétního mailingu může adresát také
Sami se zařadí do černé listiny při odhlášení, což znamená, že už nikdy nebudou dostávat žádné další
marketingové e-maily z databáze Odoo.

Aby poskytovatelé mohli uživatelům umožnit blokování sami sebe, musí být implementován konkrétní prvek.
je zapnuto v aplikaci Email Marketing*.

Přejděte na: „E-mailový marketing aplikace -> Konfigurace -> Nastavení“ a zaškrtněte
zaškrtávací políčko vedle funkce „Možnost odhlášení se z černé listiny“. Pak klikněte
:guilabel:`Uložit“ v horním levém rohu stránky „Nastavení“.

.. obrázek: odhlášení/černá listina.png
:align:center
:alt: Zobrazení funkce Blacklist na stránce nastavení aplikace Odoo Email Marketing.

Odhlásit se
-----------

Výchozí nastavení zobrazuje odkaz na odhlášení v každém e-mailovém šablonu.

.. varování:
Přepínač „Odhlásit se“ nebude vypadat automaticky, pokud použijete šablonu „Začít od začátku“.
použít k vytvoření newsletteru. Uživatelé **musí** ručně přidat konkrétní odkaz na odhlášení.
/odhlásit se z seznamu v těle e-mailu nebo použít blok z části *Doplňky*.
e-mailový editor, který obsahuje odkaz na odhlášení.

Pokud adresát klikne na odkaz Unsubscribe v e-mailu, okamžitě se z odběru odhlásí.
seznamu, představuje jim stránku „Předplatné“ (viz guilabel:Mailing Subscriptions), kde mohou přímo
správu svých předplatných a informuje je o tom, že byly úspěšně
Odhlášený.

.. obrázek: odhlášení/stránka pro odběr newsletterů.png
:align:center
:alt:Stránka s odběry, která se zobrazí po kliknutí na odkaz „Odhlásit“.

Pod tímto se Odoo ptá bývalého předplatitele: „Prosíme vás, abyste nám sdělili důvod, proč jste své
předplatné“, uživatel může pokračovat ve výběru vhodného důvodu pro odhlášení z řady
možnostech, které jim byly nabídnuty.

.. poznámka::
Možnosti odhlášení lze vytvářet a upravovat kliknutím na :menuselection:`E-mail
Marketingová aplikace --> Konfigurace --> Důvody vypnutí.

Jakmile si vyberou vhodný důvod pro odhlášení z nabízených možností, mohou
Klikněte na tlačítko „Odeslat“. Poté Odoo zaznamenává důvody pro odhlášení v e-mailu
Marketingová aplikace pro budoucí analýzu.

Černá listina
---------

Pro příjemce odstranit (tj. zařadit do černé listiny) všechny e-maily s reklamními nabídkami během
odhlášení z procesu odběru na stránce „Předplatné pošty“ musí kliknout
:guilabel:`Vylouč mě“.

Po kliknutí na „Vynechat mě“ Odoo oznamuje příjemci, že byl úspěšně vyřazen.
černou listinou s textem „Email byl přidán na černou listinu“.

.. obrázek: odhlášení/přihlášení do seznamu blokovaných e-mailů - otázka.png
:align:center
:alt:Dotaz na blokované adresy v sekci Předplatné na stránce Odesílatele, kterou vidí příjemci.

Pod tímto Odoo žádá bývalého předplatitele o informace o tom, proč chce být
Přidali jsme je na černou listinu,“ uvedl pro server TechCrunch.
možnostech, které jim byly nabídnuty.

Jakmile si vyberou vhodný důvod z nabízených možností, mohou kliknout na
tlačítko „Odeslat“. Odoo pak zaznamenává důvody, proč se sami zařadili na černou listinu, v e-mailu
Marketingová aplikace pro budoucí analýzu.

Zablokované e-mailové adresy
===========================

Pro zobrazení kompletního seznamu všech zakázaných e-mailových adres přejděte na:
Marketingová aplikace --> Konfigurace --> Seznam zakázaných e-mailových adres.

.. obrázek: odhlášení/zablokované e-mailové adresy.png
:align:center
:alt:Výhled stránky s černou listinou e-mailových adres v Odoo Email Marketing.

Když je vybrána černá listina z této seznamu, Odoo odhalí samostatnou stránku s
kontaktní údaje příjemce spolu s důvodem, proč si vybral
sám sebe na černou listinu zařadit.

.. obrázek: odhlášení/černá listina kontaktů.png
:align:center
:alt: Pohled na kontaktní údaje vyloučené z odesílání e-mailů v Odoo Email Marketing.

V chatu na stránce s černou listinou je uveden časový razítko, které upozorňuje uživatele
když příjemce sám sebe zablokoval (pomocí záznamu v logu „Vytvořený seznam blokovaných e-mailů“).

.. poznámka::
E-maily na černé listině jsou vyloučeny ze všech obchodních sdělení, ale tyto e-maily stále mohou dostávat.
obdržet transakční e-maily, jako jsou potvrzení objednávek, oznámení o expedici zásilek atd.

Kontakty z nečerné listiny
====================

Klikněte na tlačítko „Unblacklist“ v pravém horním rohu.
stránku černé listiny zrušit kontakt ze seznamu a umožnit jim přijímat
mailingy.

Když je kliknuté tlačítko „Unblacklist“, objeví se „Jste si jistí, že chcete odblokovat
Zobrazí se okno „E-mailová adresa?“.

V tomto okně se zobrazí e-mailová adresa vybraného záznamu v černé listině a
pole „Důvod“, do kterého lze zadat důvody, proč byl tento konkrétní kontakt
byl ze seznamu vyškrtnut.

.. obrázek: odhlášení/odblokování-popup.png
:align:center
:alt: Pohled na okno s upozorněním o nezařazení do černé listiny v aplikaci Odoo Email Marketing.

Po vyplnění všech polí klikněte na tlačítko „Potvrdit“ a oficiálně odstraníte konkrétního kontaktu.
z černé listiny.

.. viz též:
   - :doc:`/email_marketing`
   - :doc:`mailing_listy“
