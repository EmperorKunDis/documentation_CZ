===================
Windows virtuální IoT
===================

Pro začít používat virtuální Windows IoT:

#Ujistěte se, že jsou splněny všechny požadavky.
#:ref:`Nainstalujte virtuální operační systém pro internet věcí (IoT) na počítač s Windows.
#:ref:`Nastavte firewall ve Windows <iot/windows-iot/firewall>“.
#Připojte své zařízení k virtuálnímu IoT v systému Windows.
#:doc:`Připojte virtuální zařízení IoT na Odoo databázi <connect>.

.._iot/windows-iot/prerequisites:

Předpoklady
=============

Před zprovozněním a používáním virtuálního IoT systému Windows musí být splněny následující předpoklady:

- Platná předplatná :ref:`IoT boxu <iot/iot/iot-subscription>“.
- Aktualizovaná a nedávná verze systému Windows (tj. Windows 10 nebo Windows 11) nainstalovaná na Windows
počítač (notebook, stolní PC nebo server).

.. poznámka::
   - :zkratka MRP (plánování materiálových požadavků), včetně kamer a měřicích nástrojů
Není kompatibilní se virtuálními zařízeními IoT od společnosti Microsoft.
   - Je také možné vytvořit virtuální počítač Windows na počítači MacOS nebo Linuxu.
Tato možnost není podporována v Odoo a nebude poskytnuta žádná pomoc při řešení problémů.

..._iot/windows-iot/instalace:

Instalace
============

Pro instalaci virtuálního operačního systému Windows pro Internet věcí na počítači s Windows:

#Přejděte na stránku ke stažení „Odoo“ (<https://odoo.com/download>). Stáhněte si instalaci Odoo.
balíček pro Windows, který odpovídá verzi vaší databáze.
#Otevřete stažený soubor „.exe“ a umožněte aplikaci provádět změny na vašem zařízení, vyberte
jazyk a klikněte na tlačítko „OK“.
#Klikněte na tlačítko „Další“ a pak na „Souhlasím“.
#Vyberte možnost „Odoo IoT“ z rozevírací nabídky „Zvolit typ instalace“.
následující komponenty by měly být vybrány: server Odoo, Odoo IoT, webový server Nginx a Ghostscript
tlumočník.
#Zkontrolujte, zda máte na počítači dostatek místa a klikněte na tlačítko „Další“.
#V poli „Soubor s instalací“ zadejte C:\\odoo a klikněte na „Instalovat“.

.. varování::
Nainstalujte virtuální IoT Odoo pro Windows nikde v adresáři uživatele Windows, protože to může způsobit
problémy s :ref:`iot/https_certifikat_iot/vytvoreni`.

#Jakmile je instalace dokončena, klikněte na tlačítko „Další“.
#. Nainstalujte GPL Ghostscript: Klikněte na tlačítko „Další“, přijměte podmínky a klikněte
:guilabel:`Instalace“, pak „Dokončit“.
#Klikněte na tlačítko „Další“, „Další“ a „Dokončit“.
:ref:`Domovská stránka systému IoT <iot/windows-iot/homepage> se automaticky otevře v prohlížeči.
URL „http://localhost:8069“.

.......
Pokud prohlížeč nezobrazuje nic, restartujte jej pomocí příkazu :ref:`<iot/windows_iot/restart>`.
Windows virtuální služba pro internet věcí.

#Zkontrolujte, že se můžete připojit na domovskou stránku systému IoT:
prohlížeč:

   - na virtuálním počítači IoT v systému Windows.
   - na jiném zařízení (např. na mobilním telefonu) přes stejnou síť jako je systém Internet of Things, a to po zadání adresy URL
„http://xxx:8069“ (kde „xxx“ je IP adresa systému IoT).
   - na jiném zařízení (např. na mobilním telefonu) přes stejnou síť jako je systém Internet of Things, a to po zadání adresy URL
„https://xxx“ (kde „xxx“ je IP adresa systému IoT), aby se ověřilo, zda existuje:doc:`HTTPS
spojení typu <iot_advanced/https_certificate_iot>.

.......tip:
Pokud nemůžete přistupovat na domovskou stránku systému IoT, viz
jiný zařízení vytvořte pravidlo pro :ref:`Windows Firewall <iot/windows-iot/firewall>`, které umožní
komunikace přes port 8069.

.._iot/windows-iot/firewall:

Konfigurace firewallu v systému Windows
==============================

Firewally pomáhají udržet zařízení v bezpečí, ale někdy blokují i legitimní připojení. Pokud jde o
virtuální IoT není dostupný na LANu, tedy například z jiného
zařízení, může to být kvůli blokování připojení firewallem. Chcete-li tomuto problému zabránit, nakonfigurujte
výjimky pro objevování sítě v nastavení operačního systému nebo ve firewallech.

.. poznámka::
Pokud je na počítači s operačním systémem Windows nainstalována třetí strana firewall, obraťte se na výrobce softwaru.
dokumentace pro konfiguraci výjimek z omezení firewallu.

Pro vytvoření pravidla pro Windows Defender a umožnění komunikace přes port ‚8069‘ postupujte podle těchto
kroky:

#Vyhledejte v nabídce Start systému Windows „Firewall“ a vyberte „Windows Defender Firewall“.
s aplikací Advanced Security.
#V levém okně vyberte položku „Pravidla příchozí pošty“.
#V pravé části okna pod položkou „Akce“ klikněte na „Nový pravidlo“.
#V novém dialogovém okně „Nová pravidla pro příchozí poštu“ vyberte typ pravidel „Přístav“.
a klikněte na tlačítko „Další“.
#Na stránce Protokoly a porty zkontrolujte TCP a Specifikované.
vyberte místní porty a do pole zadejte následující hodnotu: „8069, 80, 443“ a klikněte
:guilabel:`Další“.

.. poznámka::
Jiná přístavní města mohou být nutná v závislosti na vašich zařízeních pro internet věcí. Například
:doc:`/aplikace/prodej/pokladny/platební metody/termíny/worldline“ platebního terminálu.
přidat port 9050.

#Na stránce „Akce“ vyberte možnost „Povolit připojení“ a klikněte
:guilabel:`Další“.
#Na stránce „Profil“ vypněte všechny typy připojení, které se na vás nevztahují.
Vyberte počítač s operačním systémem Windows a klikněte na tlačítko „Další“.
#Na stránce „Název“ zadejte název (např. Odoo) a volitelně krátký popis.
:guilabel:`Popis“, pak klikněte na „Dokončit“.

.. viz též:
„Dokumentace k pravidlům Windows Firewall
<https://docs.microsoft.com/cs-cz/windows/security/operating-system-security/network-security/windows-firewall/rules>

.. _iot/windows-iot/domovská stránka:

Domovská stránka virtuálních zařízení pro internet věcí od společnosti Microsoft
============================

Pro přístup na domovskou stránku virtuálního IoT systému Windows zadejte do adresy URL „http://localhost:8069“
Virtuální počítač s operačním systémem Windows nebo otevřete webový prohlížeč z jiného počítače **na stejné síti jako
IoT systém** a přejít na adresu URL http://xxx:8069 (kde „xxx“ je IP adresa IoT systému
adresa)

Jakmile je virtuální Windows IoT propojen s databází Odoo, jeho domovská stránka může
Otevřít aplikaci IoT a kliknout na odkaz zobrazený v systému IoT.
karta.

.. obrázek: windows_iot/iot-windows-homepage.png
:scale: 75 %
:alt:Domovská stránka virtuálního operačního systému pro internet věcí od společnosti Microsoft

.. poznámka::
Zkontrolujte, zda je nastaveno :ref:`<iot/windows-iot/firewall> Windows Firewall`, aby umožnil přístup.

Připojení zařízení
=================

Většina zařízení <devices> se automaticky připojuje k počítači s Windows, který je používán pro
Virtuální IoT prostřednictvím „Windows Plug and Play (PnP)“
<https://docs.microsoft.com/cs-cz/windows-hardware/drivers/kernel/introduction-to-plug-and-play>.
Pokud však operační systém Windows zařízení nepozná automaticky při připojení, je administrátor
Mohou muset nainstalovat příslušné ovladače ručně.

.. tip::
Po připojení zařízení k počítači obnovte stránku domovské stránky systému IoT.
<iot/windows-iot/homepage> a ověřte, zda je zařízení uvedeno. Pokud se zařízení nezobrazí,

<iot/windows-iot/homepage>.

... iot/windows-iot/restart:

Windows virtuální IoT restart
===========================

Chcete-li ručně restartovat službu Windows IoT Server, vyhledejte v nabídce Start „Služby“ a
Vyberte aplikaci „Služby“. Vyhledejte službu „odoo-server-xxx“ (kde
„xxx“ je verze odoo), klikněte na něj pravým tlačítkem a vyberte „Spustit“ nebo „Znovu spustit“.

.. _iot/windows_iot/uninstall:

Odinstalace virtuálního zařízení IoT v systému Windows
=============================

Pro odinstalování virtuálního operačního systému Windows IoT použijte příkaz
<https://support.microsoft.com/cs-cz/windows/odinstalovat-nebo-odstranit-aplikace-a-programy-v-oknech-4b55f974-2cc6-2d2b-d092-5905080eaf98#ID0EBD=Windows_11>
program Odoo ve vašem počítači s Windows. Potvrďte odinstalaci a dokončete kroky v
Dialog „Odoo Odinstalovat“.
