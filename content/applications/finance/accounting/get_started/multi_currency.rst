=====================
Multiměnová soustava
=====================

Odoo vám umožňuje vystavovat faktury, přijímat faktury a evidovat transakce v měnách jiných než
hlavní měna, kterou máte ve své firmě nastavenou. Můžete si také založit účty v jiných měnách
a vytvářet zprávy o svých devizových aktivitách.

.. viz též:
   - :doc:`../bank/cizí měna`

.._multiměnový/konfigurace:

Konfigurace
=============

.._měnový kurz:

Hlavní měna
-------------

Hlavní měnou je nastavena podle země společnosti. Můžete ji změnit
Přejděte do sekce „Účetnictví“ -> „Konfigurace“ -> „Nastavení“ -> „Měny“ a změňte
měna v nastavení „Hlavní měna“.

.._multiměnovost/konfigurace-zapnout:

Povolit cizí měny
-------------------------

Přejděte na „Účetnictví -> Konfigurace -> Měny“ a zapněte měny, které chcete.
chcete používat přepínačem tlačítka „Aktivní“.

.. obrázek: multi_currency/enable-foreign-currencies.png
:align:center
:alt:Zapněte měny, které chcete používat.

.._s více měnami/konfigurace sazeb:

Směnné kurzy
--------------

Manuální aktualizace
~~~~~~~~~~~~~

Chcete-li ručně vytvořit a nastavit měnový kurz, přejděte na:
Měny“, klikněte na měnu, kterou chcete změnit kurz a pod „Sazby“
klikněte na tlačítko „Přidat řádek“ (viz obrázek) pro vytvoření nové sazby.

.. obrázek: multi_currency/manual-rate-update.png

:alt: Vytvořit nebo upravit kurzovní lístek.

Automatické aktualizace
~~~~~~~~~~~~~~~~

Když aktivujete druhou měnu poprvé, zobrazí se pole „Automatické směnné kurzy“
pod položkou „Účetní přehled“ - „Nastavení“ - „Měny“.
Výchozí nastavení je „Aktualizovat nyní“ (:guilabel:`🗘`):

Odoo může aktualizovat sazby v pravidelných intervalech. Chcete-li tak učinit, změňte
„Ručně“ na „Denně“, „Týdně“ nebo „Měsíčně“. Můžete také
Vyberte webovou službu, ze které chcete získat nejnovější kurzy měn kliknutím na
:guilabel:`Služba“ pole.

.._měnová politika:

Dílčí položky rozdílu z přecenění
---------------------------

Odoo automaticky eviduje rozdíly z převodních kurzů na zvláštních účtech.
noviny.

Můžete definovat, který deník a účty se mají používat k vytváření záznamů o rozdílech při směně.
Přejděte do sekce „Účetnictví“ -> „Konfigurace“ -> „Nastavení“ -> „Výchozí účty“ a upravte
:guilabel:`Kniha účetních záznamů“, :guilabel:`Ziskový účet“ a :guilabel:`Účet ztráty“.

.. příklad::
Pokud obdržíte platbu za fakturu zákazníka jeden měsíc po vystavení faktury, kurz
To se pravděpodobně změnilo od té doby. Tato kolísavost tedy znamená zisk nebo ztrátu kvůli
rozdíl z převodu, který Odoo automaticky eviduje v poli **Exchange Difference**
časopis.

.._s více měnami/konfigurace COA:

Klasifikační schéma
-----------------

Každý účet může mít nastavenou měnu. Tím se všechny pohyby týkající se daného účtu automaticky přepočítají na
měla měnu účtu.

Pro toto nastavení přejděte na: „Účetnictví“ - „Konfigurace“ - „Skladové účty“.
měna v oboru: guilabel:"Základní měna". Pokud je nevyplněno, všechny aktivní měny jsou zpracovávány.
a ne jen jednu.

.._s více měnami / konfigurace účetních knih:

Časopisy
--------

Pokud je měna nastavena na **deník**, tak ten deník zpracovává pouze transakce v této měně.

Pro toto vyberte v menu:Účetnictví - Konfigurace - Účetní deník a otevřete si účetní deník, který chcete upravit.
chcete upravit a vybrat měnu v poli:guilabel:'Měna'.

.. obrázek: multi_currency/journal-currency.png
:align:center
:alt:Vyberte měnu, ve které bude časopis veden.

..._multiměnový/mca:

Účetnictví v několika měnách
=========================

.._více měn/dokumenty MCA:

Faktury, účtenky a další dokumenty
------------------------------------

Pro všechny dokumenty lze vybrat měnu a účetní knihu pro transakci v
sám dokument.

.. obrázek:multi_currency/currency-field.png
:align:center
:alt:Vyberte měnu a časopis, který chcete použít.

..._multiměnový/platba-v-mca:

Registrace platby
--------------------

Pro registraci platby v měně jiné než hlavní měně společnosti klikněte na
Připojte tlačítko „Registrace platby“ k dokumentu a v okně vyberte
Měnu v poli „Částka“.

.. obrázek: multi_currency/register-payment.png



.._více měn/účetní výkazy:

Bankovní transakce
-----------------

Při vytváření nebo importu bankovních transakcí je částka uvedena v hlavní měně společnosti.
v cizí měně, vyberte měnu v poli „Cizí měna“. Jakmile je zvolena, zadejte
:guilabel:`Množství“ ve vaší hlavní měně, aby se automaticky převedlo na cizí měnu.
měna v poli „Částka v měně“.

.. obrázek::multi_currency/foreign-fields.png

:alt:Pole navíc, která se týkají cizích měn.

Při převodu měn se zobrazují jak cizoměnová částka, tak částka v místní měně.
hlavní měnou společnosti.

.._vložení v různých měnách / mca-exchange-entries:

Účetní záznamy o směnném kurzu
-----------------------------

Pro zobrazení záznamů o rozdílech v účetnictví přejděte na: „Účetní dashboard“ - >
Účetnictví --> Knihy: Různé.

.. obrázek: multi_currency/exchange-journal-currency.png
:align:center
:alt: Záznam o směnném kurzu.
