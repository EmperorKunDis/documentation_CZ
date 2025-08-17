=======
Vietnam
=======

.._Faktura: https://www.faktura.vn/

... /lokalizace/vietnam/moduly:

Moduly
=======

Následující moduly jsou nainstalovány automaticky s vietnamskou lokalizací:

.. seznam tabulkový::
:hlavičkové řádky: 1

    * Jméno
      - Technické označení
      - Popis
    * --label:Vietnam - Účetnictví
      - „l10n_vn“
      - Tento modul zahrnuje výchozí

    * -- :guilabel:Vietnam - Elektronické faktury
      - „l10n_vn_edi_viettel“
      - Tento modul obsahuje funkce potřebné pro integraci s :ref:`Fakturou
<lokalizace/vietnam/faktura>.

.. poznámka::
V některých případech, například při upgrade na verzi s dalšími moduly, je možné, že
Moduly nemusí být nainstalovány automaticky. Chybějící moduly lze ručně :ref:`nainstalovat
<obecné/instalace>.

..._lokalizace/vietnam/firma:

Společnost
=======

Pro využití všech funkcí této fiskální lokalizace je nutné mít v
:doc:`údaje o společnosti </odborne/obecne/spolecnosti/>“

- :label:Jméno
- včetně města, státu a poštovního směrovacího čísla
a :guilabel:`Země“.

   - Do pole „Ulice“ zadejte název ulice, číslo popisné a případně další adresu.
informace.
   - Do pole „Ulice 2“ zadejte čtvrť.

- :guilabel:`Daňové identifikační číslo“: daňové identifikační číslo.

..._lokalizace/vietnam/sinvoice:

Elektronická fakturace s programem SInvoice
=========================

SInvoice_ je elektronická fakturační služba poskytovaná společností Viettel, jedním z největších poskytovatelů těchto služeb.
poskytovatelé vietnamské verze. Odoo podporuje integraci s Sinvoice pro odesílání faktur vygenerovaných v Odoo.

Konfigurace
-------------

Platforma fakturace
~~~~~~~~~~~~~~~~~

Pro odeslání elektronické faktury do SInvoice je nutné vytvořit následující na SInvoice:

- :ref:`Fakturační účet <lokalizace/vietnam/fakturacni-ucet>`
- :ref:`Šablona faktury <lokalizace/vietnam/sinvoice-template>`
- :ref:`Fakturační symbol <lokality/vietnam/fakturace-symbol>`
- :ref:`Vydání faktury <localizations/vietnam/sinvoice-notice>`

... /vietnam/sinvoice-registration:

Registrace faktury
*********************

Vytvoření účtu provedete na stránce SInvoice_ a zaregistrujete se pro požadovaný plán. Vyplňte formulář
otevře se kontaktní formulář pro vytvoření účtu.

Jakmile máte účet, přihlaste se do aplikace SInvoice pomocí svého uživatelského jména a
:guilabel:`Heslo“.

... /vietnamština/sinvoice-vzor:

Vytvoření vzorového faktury
*************************

#V levém sloupci přehledu klikněte na položku „Správa vydání“ pod názvem
:guilabel:`Vytvořit obchodní informace“.
#V kroku „Aktualizace klíčových informací“ vyplňte následující pole a další volitelná pole.
pokud je potřeba: „Jméno jednotky“, „Adresa“ a „Kontaktní osoba“.
:guilabel:`Druh zastupitelského dokumentu“.
#Klikněte na tlačítko „Aktualizovat“.
#V kroku „Zkontrolujte digitální certifikát“ vyberte možnost „Přidat nový“.
certifikát.
#Vyberte „Organizace“ a „Typ digitálního certifikátu“, pak
Vyplňte požadovaná pole pro každý typ:

     - :guilabel:`Dodavatel“: CloudCA
     - :guilabel:`ID podepisujícího subjektu“: CloudCA
     - :guilabel:`Digitální certifikát“: CloudCA
     - :guilabel:`Jak stáhnout soubor“: HSM
     - :label:Souborový upload: HSM, USB token

#Klikněte na tlačítko „Vytvořit klíčovou dvojici“ pro vytvoření šifrovacích klíčů pro ověřování.
:guilabel:`Uložit“.
#V kroku „Správa šablon faktur“ přidejte novou šablonu faktury.
#Vyberte typ faktury a do políčka „Šablona faktury“ zadejte kód šablony.
:guilabel:`Název šablony faktury“, a další volitelné informace, pokud je potřebujete.
#Klikněte na tlačítko „Aktualizovat“.

.. viz též:
„Výkaz o vystavených fakturách na vytvoření elektronické fakturační šablony


..._lokalizace/vietnamu/sinvoice-symbol:

Vytváření fakturačních symbolů
***********************

V levém sloupci hlavního okna klikněte na položku
:guilabel:Symbol faktury a postupujte podle těchto kroků:

#Klikněte na „Přidat nový“ a vyberte šablonu faktury.
#Nastavte atribut :guilabel:`Status` na hodnotu :guilabel:`Aktivní“ a aktivujte symbol.
:guilabel:`Symbol faktury“.
#Zapněte volbu „Automatické odesílání do finančního úřadu“ a „Výchozí nastavení pro vestavěné
na základě preferencí.
#Klikněte na tlačítko „Uložit“.

... /vietnamsky/sinvoice-notice:

Oznámení o vystavení faktury
***********************

V levém sloupci hlavního okna klikněte na položku
Vyberte možnost „Vytvořit výzvu k vydání“ a postupujte podle těchto pokynů:

#Klikněte na „Přidat nový“, vyberte „Název účetní jednotky pro vystavení elektronické faktury“.
a :guilabel:`Název daňového úřadu`. Podle vybrané obchodní jednotky a daňového úřadu se zobrazí
:guilabel:"Daňové identifikační číslo", :guilabel:"Adresa", :guilabel:"Telefonní číslo" a :guilabel:"Značka oddělující položky
V poli „Uživatelské jméno“ jsou automaticky vyplněny a nelze je upravit.
#Klikněte na tlačítko „Vyberte typ faktury pro vystavení“ a poté vyberte a vyplňte
Následující informace:

   - :guilabel:`Druh faktury“: Druh faktury, na kterou se vydává výzva k prohlášení.
   - :guilabel:`Šablona faktury“: Vyberte z dostupných šablon podle typu faktury.
typu.
   - :symbol: Vyberte symbol z dostupného seznamu podle typu faktury.
   - :guilabel:`Počet faktur“: Celkový počet faktur, které je třeba vystavit pro vybraný typ.
Pokud je typ a šablona vybrána, tento údaj se doplní automaticky. Může být změněn, pokud je to potřeba.
   - :guilabel:`Datum zahájení používání“: Datum od kterého se bude vzor faktury, rozsah a množství
slouží k vydání výzvy.

#Klikněte na tlačítko „Uložit“ a zvolte další typy faktur, pokud je potřebujete, opakovaně prováděním kroků výše.
Klikněte na tlačítko „Uložit“ a návrh oznámení dokončete.
#Klikněte na tlačítko „Odeslat daňovému úřadu“ a potvrďte. Jakmile bude schválená,
:guilabel:`Stav“ se změní na „Aktivní“.

..._lokalizace/vietnam/faktura-odoo:

Odoo databáze
~~~~~~~~~~~~~

Propojit aplikaci Odoo s Sinvoice
*********************

Pro propojení Odoa s Sinvoicem přejděte na: „Účetnictví --> Konfigurace --> Nastavení“.
V sekci „Vietnamská integrace“ vyplňte své uživatelské jméno a
:guilabel:`Heslo“. Přidejte :guilabel:`Výchozí symbol“ pro vytvoření předčíslí fakturační částky
v případě potřeby v SInvoice.

Šablona faktury
****************

Pro vytvoření šablony faktury přejděte na: „Účetnictví --> Konfigurace --> Šablony“.
Klikněte na „Nový“ a přidejte „Šablonový kód“ a „Šablonu faktury“.
:guilabel:Template code je počáteční sekvence čísel v názvu přiděleném společností SInvoice.
Příkladem je například fakturační šablona „1/001 - Faktura GTGT - ND123“.
Kód je 1/001. Šablony faktur v Odoo musí odpovídat šablonám faktur ve SInvoice.

Přidat:guilabel:Symboly faktury, klikněte na:guilabel:Přidat novou řádku.

Vystavování faktur do SInvoice
----------------------------

Faktury můžete odeslat na SInvoice až po jejich potvrzení. Chcete-li tak učinit, postupujte podle
kroky zasílání faktury. V okně „Odeslat“ zapněte
Vyberte možnost „Připojit fakturu“ a klikněte na „Odeslat a tisknout“.

Jakmile je faktura úspěšně odeslána do SInvoice, pole :guilabel:`SInvoice Status`
V záložce „Faktura“ faktury se aktualizuje na „Odesláno“.
:guilabel:`Číslo faktury“, :guilabel:"Datum vystavení", :guilabel:"Tajný kód" a :guilabel:"Elektronická faktura
Aktualizovány jsou také pole číslo. Stejné informace lze najít na faktuře.

Faktury o výměně nebo opravě
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pokud se chystáte vydat náhradní fakturu k opravě faktury, která ještě nebyla uvedena do daňového přiznání,
Vystaví se daňový doklad k opravě jednoho, který byl již předtím přiznán k dani. Postupujte takto
kroky k vystavení náhradního nebo dodatečného daňového dokladu:

#Otevřete fakturu a klikněte na „Kreditní poznámka“.
#V okně „Poznámka k úvěru“ vyplňte následující pole:

   - :guilabel:`Důvod zobrazený na faktuře“
   - :guilabel:`Typ upřesnění“
   - :guilabel:`Název smlouvy“
   - :guilabel:`Datum smlouvy“
   - :label:Noviny
   - :guilabel:`Datum obratu“

#Klikněte na tlačítko „Zrušit a vytvořit fakturu“.
:guilabel:`Zpětná fakturace“ pro vystavení daňového dokladu k úhradě.

Stav faktury v záložce „Faktura“ se aktualizuje na
:guilabel:`Výměna“ pro výměnu faktury nebo „Upraveno“ pro upravenou fakturu.

Zrušení faktury
~~~~~~~~~~~~~~~~~~~~

Pokud je potřeba vystavit fakturu znovu, otevřete si ji a klikněte na tlačítko „Požádat o zrušení“.
Ve vyskakovacím okně „Zrušení faktury“ zadejte důvod zrušení.
„Smlouva“ a „Datum smlouvy“, klikněte na „Požádat o přístup“.
Zrušení.“

Stav faktury v záložce „Faktura“ se aktualizuje na
:cancelled:

.._lokalizace/vietnam/qrcode:

QR kódy pro bankovnictví
================

Vietnamská služba QR bankovnictví je platební platforma, která umožňuje zákazníkům provádět okamžité domácí
platby vietnamským dongům jednotlivcům a obchodníkům prostřednictvím internetového a mobilního bankovnictví.

Konfigurace
-------------

Pro aktivaci kódu QR bankingu přejděte do sekce „Účetnictví -> Konfigurace -> Nastavení“
Zapněte možnost „QR kódy“ v sekci „Platby zákazníků“.

Bankovní účet
~~~~~~~~~~~~

Pro aktivaci QR bankovnictví pro účet přejděte na: „Kontakty –> Konfigurace –>
Vyberte si bankovní účet a vyplňte kód banky,
„Typ proxy“ (na základě informací použitých k identifikaci „Obchodního účtu“),
například číslo karty a čísla účtů) a pole „Zástupný význam“.

Zapněte pole „Přidat odkaz“ a zadejte číslo faktury do QR kódu.

.. důležité::
   - Země uživatele musí být nastavena na „Vietnam“ a město musí být specifikováno.
kontaktní formulář.
   - Je nutné nastavit číslo účtu :ref:`<accounting/bank/account-number>`, stejně jako banku.
:guilabel:`Banka“ časopis.

.. viz též:
:doc:`../účetnictví/banka`

Vytváření QR kódů na fakturách
-------------------------------

Při vytváření nové faktury otevřete záložku „Další informace“ a vyberte „EMV“.
Pokladní předloží kód QR zadaný v poli „Platba QR“.

.. poznámka::
Ujistěte se, že je nastaveno pole „Příjemce banky“, protože Odoo používá tento údaj k vytvoření
kódy.
