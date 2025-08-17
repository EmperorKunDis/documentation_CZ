=================
SEPA Direct Debit
=================

.. |sdd| nahradit za: abbr: SDD (SEPA Direct Debit)

SEPA (Single Euro Payments Area) je iniciativa Evropské unie pro integraci plateb,
usnadňuje standardizované a zjednodušené elektronické platby v eurech mezi zapojenými zeměmi.

SEPA Direct Debit (SDD) je poskytovatel plateb, který umožňuje budoucí platby vybrat z účtu.
účty zákazníků na základě podepsané :ref:`SEPA Direct Debit mandate
<účetnictví/převod/sdílené pověření>. Toto je zejména užitečné pro opakující se platby založené na
:dokument: „Předplatné </aplikace/prodej/předplatné>“.

.. důležité::
Pro použití poskytovatele plateb SEPA Direct Debit (SDD) a vytvoření :ref:`SEPA Direct Debit příkazů


   - Faktura, kterou se platí, musí být v eurech.
   - Funkce „SEPA Direct Deposit (SDD)“ musí být zapnutá a společnost
:guilabel:`Identifikátor věřitele“ musí být definován v nastaveních účetnictví nebo fakturace.
<účetnictví/převodní příkaz/SEPA konfigurace>.

..._sdc/konfigurace:

Konfigurace
=============

Chcete-li nastavit SEPA Direct Debit, postupujte takto:

#:ref:`Přejděte na stránku poskytovatele SEPA Direct Debit <payment_providers/supported_providers>.“
#V záložce „Konfigurace“ vyberte, zda chcete vytvořit poznámku nebo komunikaci.
vedle pokynů k úhradě by měla být zobrazena:

   - :guilabel:`Na základě odkazu na dokument“: číslo objednávky nebo faktury
   - „Založeno na zákaznické identifikaci“: zákaznická identifikace

#Zatrhněte políčko „Povolit QR kódy“ a zapněte platby pomocí QR kódu.

.. poznámka::
:doc:`Potřeba dalšího účetního nastavení <../accounting/customer_invoices/epc_qr_code>“
využívat QR kódy.

#Upravte výchozí pokyny k úhradě v záložce „Zprávy“ tak, aby zahrnovaly vaši banku.
*číslo účtu **. Tyto pokyny se zobrazují na konci procesu objednávky ve vašem
na e-shopu nebo v zákaznickém portálu.
#Nastavte pole :guilabel:`Stát“ na hodnotu :guilabel:`Zapnuto“.

.. důležité::
   - Zaškrtněte pole „Měny“ a nastavte výchozí měnu na „EUR“, aby bylo zajištěno
Je k dispozici pouze pro platby v eurech.
   - Definovaná bankovní účetová značka :guilabel:`Bank Account` pro :guilabel:`Payment Journal` musí být platný IBAN.

.. tip::
Můžete také otestovat platby SEPA převodem pomocí :ref:`platebních metod/testovací režim`.

.. viz též:
:doc:`../platební_prostředky`

Online platby s |sdd|
==========================

Zákazníci, kteří si zvolí jako způsob platby |sdd|, jsou vyzváni, aby doplnili své číslo IBAN.
:ref:<účetnictví/dávkové platby/sdd_povolení>.

Poté je vytvořen mandát |sdd| na základě poskytnutého IBANu a je uložen do složky :guilabel:`Návrh`.
ověřit informace, musí zákazníci potvrdit každou novou pověření úspěšným převodem peněz.
očekávané částce, která bude použita na základě uvedeného platebního referenčního čísla
:formulář poskytovatele SEPA Direct Debit platby (<sdd/configuration>).
a byla přijata a vyrovnána, pak je povinnost automaticky
ověřené a aktualizované na stav „Aktivní“. Jakmile je pověření aktivní, používá se pro
všechny další platby provedené pomocí platební metody |sdd|. Potom je můžete vyzvednout v
:ref:`Nahrání je možné přes online bankovnictví <účetnictví/zálohování/XML>.

.. viz též:
:doc:`../účetnictví/platby/souhrnný_sdd`

.. poznámka::
   - Mandáty jsou automaticky uzavřeny po uplynutí 36 měsíců.
po posledním dni sběru.
   - Služba |sdd| je dostupná také jako platební metoda u dalších poskytovatelů, například
:doc:`adyen`, :doc:`buckaroo“, a :doc:`stripe“. V těchto případech se |sdd| požadavky zpracovávají
ze strany poskytovatele platebních služeb.
