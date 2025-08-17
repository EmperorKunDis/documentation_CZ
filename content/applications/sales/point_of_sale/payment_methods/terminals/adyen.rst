=====
Adyen
=====

Připojení platebního terminálu Adyen umožňuje nabídnout vašim zákazníkům plynulý způsob platby.
a usnadnit práci pokladních.

.. důležité:
   - Platební terminály společnosti Adyen nevyžadují :doc:`IoT Box </applications/general/iot>“.
   - Terminály Adyen lze používat v mnoha zemích, ale ne ve všech. Podívejte se na „Seznam zemí“.
podporované společností Adyen (<https://docs.adyen.com/point-of-sale/what-we-support/supported-languages/>).
   - Adyen spolupracuje pouze s podniky, které zpracovávají více než **10 milionů dolarů ročně** nebo vystavují faktury
minimálně 1000 transakcí měsíčně.

.. viz též:
   - „Seznam platebních metod podporovaných společností Adyen“
   - „Seznam terminálů společnosti Adyen <https://docs.adyen.com/point-of-sale/what-we-support/select-your-terminals/>“

Konfigurace
=============

Začněte vytvořením účtu na webu společnosti Adyen (https://www.adyen.com/). Poté se přihlaste
Postupujte podle pokynů na obrazovce vašeho terminálu.

.. viz též:
„Návody na rychlý start terminálu Adyen <https://docs.adyen.com/point-of-sale/quickstarts/payment-terminal/>“

.. _adyen/api:

Vytvořte klíč API pro Adyen
-------------------------

API klíč **Adyen API** se používá k ověření požadavků z vašeho terminálu Adyen.
klíč, přejděte do svého účtu Adyen > vývojáři > API kredence a vytvořte
nové přihlašovací údaje nebo vyberte existující. Klikněte na tlačítko „Vytvořit klíč API“ a uložte klíč
vložit ho do pole „API klíč Adyen“ v sekci „Vytvoření platebního nástroje“.
<adyen/metoda-vytvoreni>.

.. viz též:
   - „Adyen Docs - API Credentials
<https://docs.adyen.com/development-resources/api-credentials#generate-api-key>.

.. _adyen/identifikátor:

Najděte identifikátor terminálu Adyen
------------------------------------

**Terminálové identifikátory Adyen** jsou sériové číslo terminálu, které se používá k jeho identifikaci.
hardware.

Toto číslo najdete v sekci „Pokladna > Terminály“ vašeho účtu Adyen.
vyberte terminál, který chcete propojit a uložte si jeho sériové číslo, abyste jej mohli vložit do Odoo.
„Identifikátor terminálu Adyen“ pole v části „Vytvoření platebního metody“.
<adyen/metoda-vytvoreni>.

Nastavte adresy URL události
------------------

Pro Odoo, aby věděl, kdy je platba provedena, musíte konfigurovat terminál **Event URL**.

#Přihlaste se na webové stránky společnosti Adyen <https://www.adyen.com/>_.
#Přejděte na stránku „Dashboard Adyen“ –> „Point of Sale“ –> „Terminály“ a vyberte propojený.
terminál.
#V nastavení terminálu klikněte na: guilabel:"integrace";
#Zadejte pole „Přepněte do režimu šifrování, abyste mohli tuto nastavení upravit“ jako „Šifrované“.
#Klikněte na tlačítko „Plnicí pero“ a zadejte adresu svého serveru, následovanou
v poli „URL událostí“ v sekci „Události“.
#Klikněte na tlačítko „Uložit“ v dolní části obrazovky, abyste změny uložili.

... adyen/method-creation:

Zvolte způsob platby
----------------------------

Zapnout platební terminál:ref:`v aplikačních nastaveních <configuration/settings> a
Vytvořte související platební metodu <../../payment_methods>. Zadejte typ účetního záznamu jako
Vyberte „Banka“ a v poli „Použít platební terminál“ vyberte „Adyen“.

Nakonec vyplňte povinná pole vaším :ref:`Adyen API klíčem <adyen/api>`, :ref:`Adyen
Identifikátor terminálu <adyen/identifier>, a :guilabel:„Účet obchodníka Adyen“.

.. obrázek: adyen/payment-method.png

Jakmile je platební metoda vytvořena, můžete si ji vybrat ve svých nastaveních POS. Chcete-li tak učinit, přejděte na
Vyberte možnost „Nastavení POS“ (konfigurace/nastavení), klikněte na „Upravit“ a přidejte platební metodu.
pod záložkou „Platby“.
