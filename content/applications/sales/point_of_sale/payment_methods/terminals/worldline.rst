=========
Worldline
=========

Připojení platebního terminálu umožňuje nabídnout svým zákazníkům plynulý způsob platby a usnadnit jim tak
Práci vašich pokladních.

.. důležité:
   - Přístupové terminály společnosti Worldline vyžadují :doc:`IoT Box </applications/general/iot>.
   - Služba Worldline je k dispozici pouze v Belgii, Nizozemsku a Lucembursku.
   - Odoo je kompatibilní s terminály společnosti Worldline, které používají protokol CTEP (např. Yomani XR a
Yoximu (terminaly Yoximo). Pokud máte jakékoliv pochybnosti, kontaktujte svého poskytovatele platebních služeb a ověřte si platnost vaší karty.
kompatibilitu terminálu.

Konfigurace
=============

Propojte systém Internetu věcí
---------------------

Připojení terminálu platební brány Worldline k Odoo je funkcí, která vyžaduje systém IoT.
Informace o tom, jak se připojit k databázi, najdete v
:doc:`Dokumentace IoT </aplikace/obecné/iot>“.

Nastavte protokol
----------------------

Ve svém terminálu klikněte na: „.“ --> 3 --> stop --> 3 --> 0 --> 9“. Zadejte
technikovým heslem „1235789“ a klikněte na:menu_selection:„OK --> 4 --> 2“. Pak klikněte na
:menu „Změnit“ -> „CTEP (jako protokol ECR)“ -> „OK“. Klikněte na tlačítko „OK“ třikrát v následujících
obrazovky (ticket CTEP ECR, šířka ECR ticket a znaková sada) a nakonec stiskněte tlačítko **Zastavit**.
minutách, automaticky se restartuje.

Nastavte IP adresu
------------------

Ve svém terminálu klikněte na: „.“ --> 3 --> stop --> 3 --> 0 --> 9“. Zadejte
technikovým heslem „1235789“ a klikněte na tlačítko „OK --> 4 --> 9“. Pak klikněte na
:menuselection:`Změnit --> TCP/IP“ (*Fyzická konfigurace TCP* obrazovka) :menuselection:`--> Ano -->
OK (obrazovka TCP Configuration client).

Nakonec nastavte název hostitele a číslo portu.

Hostitel
~~~~~~~~

|Pro nastavení názvu hostitele zadejte sekvenci číslic IP adresy vašeho systému Internetu věcí a stiskněte tlačítko **OK**.
každé „.“ až do dosažení znaku „:“.
Poté stiskněte dvakrát tlačítko **OK**.

Příklad:
|Tady je sekvence IP adresy: „10.30.19.4:8069“.
|Na obrazovce *Název hostitele* zadejte: 10 --> OK --> 30 --> OK --> 19 --> OK --> 4
--> OK --> OK.

..tip:
IP adresa vašeho systému Internetu věcí je k dispozici na :ref:`kartě systému Internetu věcí v aplikaci
<iot/connect/IoT-form>.

Číslo portu
~~~~~~~~~~~

Na obrazovce Port number zadejte 9001 (nebo 9050 pro Windows) a klikněte na
:menuselection:`OK“ (*protokolem SSL bezpečnostního certifikátu ECR*): :menuselection:`--> OK“. Klikněte na „Přerušit“ třikrát.
Terminál se automaticky restartuje.

.. varování:
Pro virtuální Windows IoT (viz :doc:`Aplikace obecné - Internet věcí <applications/general/iot>` ) je nutno přidat port 9050
jako výjimku z :ref:`Windows Firewall <iot/windows-iot/firewall>`.

Zvolte způsob platby
----------------------------

Zapnout platební terminál:ref:`v aplikačních nastaveních <configuration/settings> a
Vytvořte související platební metodu <../../payment_methods>. Zadejte typ účetního záznamu jako
Vyberte „Banka“ a v poli „Použít platební terminál“ vyberte „Worldline“.
Poté vyberte svůj terminál v poli „Způsob platby“.

.. obrázek:worldline/worldline-platební-terminály.png

Jakmile je platební metoda vytvořena, můžete si ji vybrat ve svých nastaveních POS. Chcete-li tak učinit, přejděte na
Vyberte možnost „Nastavení POS“ (konfigurace/nastavení), klikněte na „Upravit“ a přidejte platební metodu.
pod záložkou „Platby“.

.._svetlinie/yomani-info:

..tip:
   - Heslo technika: „1235789“
   - Pro technickou podporu společnosti Worldline volejte číslo „02 727 61 11“ a zvolte možnost „obchodník“.
Je automaticky převeden na požadovanou službu.
   - Konfigurujte pokladní terminál, má-li být použit jak zákaznický, tak pokladní terminál.
   - Aby se předešlo zablokování terminálu, ověřte si předem počáteční konfiguraci.
   - Přidělte svému IoT boxu pevnou IP adresu, aby nedošlo k přerušení spojení.
