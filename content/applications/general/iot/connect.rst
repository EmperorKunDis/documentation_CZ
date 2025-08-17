=============================
Připojení systému IoT k Odoo
=============================

Předpoklady
=============

Pro připojení systému IoT k databázi Odoo je nutné splnit následující podmínky:

- Aplikace Internetu věcí (IoT) musí být nainstalována.
- IoT systém musí být připojen k síti.
- K počítači připojenému k Odoo musí být připojeno stejné síťové zařízení jako k systému Internet věcí.

.. poznámka::
Je doporučeno připojit systém IoT k **produkčnímu** instanci, protože jiné typy
prostředí mohou způsobit problémy (např. s generováním certifikátu HTTPS).
<iot/https_certificate_iot/iot-eligibility>

.. viz též:
   - :doc:`iot_box`
   - :doc:`windows_iot`

Připojení
==========

IoT systém lze propojit s databází Odoo pomocí :ref:`párovacího kódu
<iot/connect/pairing-code> nebo :ref:`token pro připojení <iot/connect/token>“.

..._iot/connect/pairing-code:

Párování pomocí kódu
-------------------------------

.. poznámka::
   - Párovací kód se zobrazuje po dobu až 5 minut od spuštění systému Internet věcí. Pokud
není již viditelná, restartujte IoT box nebo restartujte virtuální službu IoT ve Windows.
restartovat zařízení a zobrazit kód párování znovu. Nebo můžete připojit IoT
systém do databáze pomocí :ref:`připojovacího tokenu <iot/connect/token>“.
   - Párovací kód se nezobrazí, pokud je systém IoT již propojen s databází (např.
(testovací databáze).

#Získat kód párování systému IoT:

... záložky ::

... skupina-tab:: IoT box

Připojte krabičku IoT k externímu monitoru nebo tiskárně. Pokud byla již krabička připojena,
Předtím restartujte tím, že ho odpojíte na několik sekund a znovu připojíte.

         - Venkovní monitor: Kód párování se na obrazovce zobrazí po několika minutách
restartovat zařízení pro internet věcí.
         - Tiskárna: Párovací kód by měl být automaticky vytištěn.

.. tip::
Pokud není k internetovému boxu připojen žádný externí monitor nebo tiskárna, přihlaste se do
domovská stránka boxu <iot/iot-box/homepage>`, kód se zobrazuje v :guilabel:`Párování
Kódová sekce.

.. skupina-tab:: Windows virtuální IoT

Na počítači s virtuální verzí systému Windows otevřete domovskou stránku systému IoT
V prohlížeči přejděte na adresu URL „http://localhost:8069“ a poté posouvejte stránku dolů.
:guilabel:`Kód pro párování“ sekci.

#V Odoo otevřete aplikaci Internet věcí a klikněte na „Připojit“.
#V okně „Připojení k internetu věcí“ zadejte :guilabel:„Kód pro párování“.
#Klikněte na tlačítko „Pár“.

.. _iot/connect/token:

Připojení pomocí přihlašovacího tokenu
-----------------------------------

#V Odoo otevřete aplikaci Internet věcí a klikněte na „Připojit“.
#V okně „Připojení k internetu věcí“ zkopírujte token.
#Připojte se k:
<iot/windows-iot/homepage> domovská stránka.
#V sekci „Připojená databáze Odoo“ klikněte na „Nastavení“.
#Vložte token do pole „Token serveru“ a klikněte na „Připojit“.

..._iot/connect/iot-form:

Forma systému internetu věcí
===============

Jakmile je systém IoT připojen k databázi Odoo, zobrazí se jako karta v aplikaci IoT.
Klikněte na adresu IP v kartě, abyste se dostali do :ref:`stránky IoT boxu <iot/windows-iot/homepage>`.
Klikněte na kartu pro přístup na domovskou stránku virtuálního operačního systému Windows IoT.
seznam zařízení připojených k systému Internet věcí.

.. tip::
:ref:`Zapnout režim vývojáře <developer-mode> k přístupu do systému internetu věcí.
:guilabel:`Technické informace“, například jeho :guilabel:`Identifikátor“ a :guilabel:`Doména“.
„Adresa“, „Obrázek“ a „Versie“.

.. poznámka::
Výchozí nastavení je takové, že se ovladače automaticky aktualizují každou chvíli.
IoT systém je restartován. Chcete-li vypnout automatické aktualizace, odstraňte zaškrtnutí políčka :guilabel:`Automatické ovladače
volba „Aktualizovat“.

..._iot/connect/troubleshooting:

Řešení problémů
===============

Párovací kód se nezobrazuje nebo nespolupracuje
-------------------------------------------------

Kód párování (:ref:`<iot/connect/pairing-code>`) nemusí být zobrazen nebo tisknut.
Tyto okolnosti:

- IoT systém není připojen k internetu.
- IoT systém je již propojen s databází Odoo.
- Zobrazení kódu párování (:ref:`<iot/connect/pairing-code>` ) vypršelo. Restartujte IoT box
nebo restartovat virtuální službu Internetu věcí pro Windows, viz:
opakovat kód.
- Ve výchozím nastavení je verze obrázku systému IoT příliš stará a potřebuje být aktualizována.
<iot/updating_iot/obraz-kod>.

IoT systém je připojený, ale v databázi se nezobrazuje
---------------------------------------------------------------

IoT systém může trvat několik minut, než se znovu spustí, když připojí k databázi. Pokud ano
neobjevit se po několika minutách:

- Zkontrolujte, zda je systém IoT schopen se dostat k databázi, a zda server nepoužívá více databází.
životní prostředí.
- Restartujte IoT box nebo restartujte virtuální službu IoT v systému Windows: :ref:`<iot/windows_iot/restart>`.

IoT box je připojen k databázi Odoo, ale není dostupný
-------------------------------------------------------------------

Zkontrolujte, zda je systém Internetu věcí a počítač běžící databázi Odoo připojený ke stejné
síť.

Domovská stránka virtuální platformy IoT pro Windows nelze přistupovat z jiného zařízení
-------------------------------------------------------------------------

Zkontrolujte :ref:`iot/windows-iot/firewall`.

IoT systém je po upgradu Odoa odpojený od databáze
----------------------------------------------------------------------

:ref:`Aktualizujte obrazový kód systému IoT <iot/updating_iot/image-code>“ pomocí přepisování paměťové karty v IoT boxu
:ref:`odinstalování virtuálního programu pro internet věcí Windows <iot/windows_iot/uninstall>`.
:ref:`nainstalovat nejnovější balíček pro Windows, který odpovídá vašemu
verze databáze**.
