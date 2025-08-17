Zobrazit obsah

=======
Členové
=======

Aplikace „Členové“ je místo, kde lze všechny operace týkající se členství nakonfigurovat.
je spravována. Aplikace „Členové“ integruje aplikaci „Prodej“ a „Účetnictví“, aby bylo možné prodávat a
fakturovat členství přímo zákazníkům.

Členství
===================

Pro vytvoření nového členství přejděte na: `Members app --> Konfigurace -->
Produkty členství“ a klikněte na „Nový“, abyste otevřeli prázdnou záznamovou knihu produktů.

Vyplňte prázdný formulář potřebnými informacemi včetně členství
Délka.“

.. poznámka::
Produkty členství vyžadují datum začátku a konce, protože se používají k určení :ref:`členství
stav <prodej/členství-stav>. Členství může být prodáno před aktivním začátkem.
datum.

.. obrázek: členství/členský produkt.png
:align:center
:alt: Nový produkt členství v aplikaci pro členy.

Členství lze přidat do prodejního příkazu a fakturovat jako běžný produkt nebo
předplatné.

Aktivujte členství
=====================

Aby se aktivovala členství z aplikace Kontakty, přejděte do nabídky:menuselection:Kontakty.
Klikněte na kontakt, abyste otevřeli jeho podrobné informace.

V důsledku kontaktního formuláře otevřete záložku „Členství“ a klikněte na „Koupit“.
Členství.

V okně „Připojení k členství“, které se objeví, vyberte z nabídky
položku rozbalovacího menu. Poté nastavte cenu pro členy.

Klikněte na položku „Faktura členství“ při vyplnění obou polí. To zobrazí
stránce „Faktury za členství“, kde lze faktury potvrdit a dokončit.

Alternativně nabídněte členství zdarma zaškrtnutím políčka „Člen bezplatný“.
Kontaktní formulář, karta „Členství“.

..prodeje/členství:

Stav členství
=================

Stav členství je uveden na záložce „Členství“ každého
Kontaktní záznam:

- :guilabel:`Nepřítel“: partner, který **neaplikoval za členství“.
- :guilabel:`Zrušený člen“: člen, který zrušil své členství.
- „Starý člen“: člen, jehož datum ukončení členství již uplynulo.
- „Čekající člen“: člověk, který požádal o vstup do klubu, ale jeho faktura ještě nebyla zaplacena.
Dokud nebude vytvořen.
- :guilabel:`Člen s fakturou“: člen, jehož faktura byla vystavena, ale nebyla zaplacena.
- :guilabel:`Placený člen“: člen, který zaplatil členské příspěvky.

Vydat adresář členů
=========================

Pro zveřejnění seznamu aktivních členů na webových stránkách je nutné použít aplikaci
prvně nainstalovat modul:ref:<general/install>. Po instalaci modulu přidat stránku
menu webu: editace menu webu <../websites/website/pages/header_footer>.

.. obrázek: členové/adresář členů aplikace.png
:align:center
:alt: Modul online adresáře členů v Odoo.

Zveřejnit jednotlivé členy
--------------------------

Přejděte zpět na kartu aplikace CRM - Prodej - Zákazníci a klikněte na kartu pro člena.
Klepněte na tlačítko „Přejít na web“ ve vzniklém formuláři pro zákazníky.
nahoru stránky otevřít webovou stránku člena.

Klikněte na tlačítko „Upravit“ (ikonka :icon:`fa-pencil`) v pravém horním rohu obrazovky, abyste zobrazili boční panel nástrojů pro úpravy.
Pokud je potřeba provést nějaké změny na stránce, klikněte na tlačítko „Uložit“. Na horní části stránky přejeďte
Přepněte na aktivní položku „Nezařazeno“ a poté na „Zveřejněno“.

Tyto kroky opakujte pro všechny požadované členy.

.. toctree::


členové/členové - analýza
