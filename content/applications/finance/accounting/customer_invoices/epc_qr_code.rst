============
QR kódy EPC
============

Kódy rychlé odpovědi Evropského platebního konsorcia, nebo **EPC QR kódy**, jsou dvourozměrné čárové kódy.
, které zákazníci mohou naskenovat pomocí svých mobilních aplikací pro bankovnictví, aby zahájili
převod (SCT) a zaplatit jejich faktury okamžitě.

Kromě snadného použití a rychlosti výrazně snižuje počet chyb při psaní, které by
mohou vést k problémům s platbami.

.. poznámka::
Tato funkce je k dispozici pouze pro společnosti v několika evropských zemích, jako je Rakousko.
Belgie, Finsko, Německo a Nizozemsko.

.. viz též:
   - :doc:`/banka`

Konfigurace
=============

Přejděte do sekce „Účetnictví“ – „Konfigurace“ – „Nastavení“ a aktivujte QR
Kódy se nacházejí v části „Platby zákazníků“.

Nastavte si účetní deník u svého bankovního účtu
-------------------------------------

Ujistěte se, že je vaše bankovní účet správně nakonfigurován v Odoo s vaším IBAN a BIC.

Pro toto vyberte v menu „Účetnictví“ -> „Nastavení“ -> „Knihy“ a otevřete si bankovní knihu.
Poté vyplňte pole „Číslo účtu“ a „Banka“ pod položkou „Bankovní účet“.
Sloupec číslo.

.. obrázek: epc_qr_code/bankovni-zpravodaj.png
:alt: Sloupec čísla účtu v knize banky

Vystavujte faktury s EPC QR kódy
================================

QR kódy EPC se automaticky přidávají do faktur. Pokud máte banku, která podporuje platby
Přes EPC budou moci kódy skenovat a platit faktury.

Přejděte na záložku „Účetnictví“ -> „Zákazníci“ -> „Faktury“ a vytvořte novou fakturu.

Před odesláním otevřete záložku „Další informace“. Odoo automaticky vyplní
V poli „Příjemce banka“ zadejte své číslo účtu IBAN.

.. poznámka::
V záložce „Další informace“ je uvedeno číslo účtu zadané v poli „Příjemce banka“.
je používán k přijetí platby od vašeho zákazníka. Odoo automaticky vyplňuje tento údaj podle
IBAN je výchozí a používá se k generování QR kódu EPC.

Když je faktura vytisknuta nebo zobrazena na displeji, kód QR se objeví na spodní části.

.. obrázek: epc_qr_code/faktura-qr-code.png
:alt:QR kód na faktuře zákazníka

.. tip::
Pokud chcete vystavit fakturu bez QR kódu EPC, odstraňte zadaný IBAN.
:guilabel:`Banka příjemce“ pole pod záložkou „Další informace“ v faktuře.
