====================================
Využijte služby VoIP v Odoo s OnSIP
====================================

.. důležité:
OnSIP: služby VoIP (hlasové přenosy prostřednictvím protokolu internetového protokole) jsou k dispozici pouze v
Státy (USA). Služby VoIP (hlasové služby přes protokol internetu) jsou v USA běžně dostupné.
do USA (kromě Aljašky a Havaje). V těchto státech mohou být účtovány vyšší poplatky za služby.

Dále je potřeba zadat adresu pro fakturaci v USA (Spojené státy), a adresu kreditní karty v USA (Spojené státy).
Karta je nutná k používání služby.

Než si založíte účet u OnSIP, musíte se ujistit, že máte vše potřebné pro podnikání.
telefonní čísla jsou přenosná na OnSIP.

OnSIP se snaží spolupracovat se všemi poskytovateli telefonních služeb. Některé místní nebo
Registrační pokyny mohou vyloučit současného poskytovatele společnosti z uveřejnění čísla.

Úvod
============

Odoo VoIP lze nastavit tak, aby pracoval s OnSIP (Odoo Landing Page).
<https://info.onsip.com/odoo/>`_. OnSIP je poskytovatel IP telefonie. Pro používání služeb OnSIP je potřeba mít vytvořený účet
Tuto službu využívat.

Než si založíte účet u společnosti OnSIP, ověřte si domácí oblast a oblasti, které budou
jejich služby jsou kryty.

Po založení účtu u OnSIP postupujte podle níže uvedeného nastavení k jeho konfiguraci v Odoo.
databáze.

Konfigurace
=============

Pro konfiguraci databáze Odoo pro připojení k službám OnSIP nejprve přejděte do
V hlavním přehledu Odoo vyberte aplikaci Apps a poté odstraňte výchozí aplikaci Apps.
filtr z lišty vyhledávání „Hledat…“ a hledejte OnSIP.

Dále aktivujte modul VOIP OnSIP.

.. obrázek: onsip/install-onsip.png
:align:center
:alt:Výhled aplikace OnSIP v výsledcích vyhledávání aplikací.

Nastavení VoIP v Odoo
-----------------

Po instalaci modulu VOIP OnSIP přejděte do aplikace Nastavení a posuňte se dolů na
sekci „Spojení“ a najděte pole „VoIP“. Pak postupujte podle následujících pokynů
V těchto třech polích s následujícími informacemi:

- :guilabel:`OnSIP Domain“: doména, která byla při vytváření účtu na OnSIP přidělena
<http://www.onsip.com/>`.
- :guilabel:`WebSocket“: „wss://edge.sip.onsip.com“
- :guilabel:`VoIP prostředí“: :guilabel:`Provozní“

.. obrázek: onsip/voip-settings.png
:align:center
:alt:Nastavení VoIP v aplikaci Nastavení Odoo.

..tip:
Chcete-li se dostat na doménu OnSIP, přejděte na stránku OnSIP (<https://www.onsip.com/>) a zadejte své
klikněte na odkaz „Administrátoři“ v pravém horním rohu stránky.

Poté v levém menu klikněte na položku „Uživatelé“ a potom vyberte libovolného uživatele. Výchozí
Vybraný uživatel otevře kartu „Informace o uživateli“.

Klikněte na záložku „Nastavení telefonu“ a zobrazí se přihlašovací údaje pro konfiguraci služby OnSIP.
sloupci.

.. obrázek: onsip/domain-setting.png
:synchronizace: střed
:alt:Zveřejněno nastavení domény na správném panelu pro správu OnSIP
konzole.

Nastavení uživatele Odoo
-----------------

Dalším krokem je nastavení uživatele v Odoo. Každý uživatel spojený s uživatelem OnSIP musí být také
Nastavení v uživatelských předvolbách Odoo.

Pro toto provedete následující kroky: přejděte na „Nastavení aplikace“ -> „Správa uživatelů“ -> „Vyberte uživatele“.

Na uživatelském formuláři klikněte na tlačítko „Upravit“ a poté na
kartě „Nastavení“ a posuňte se do části „Konfigurace VoIP“.

V této části vyplňte pole s přihlašovacími údaji pro OnSIP.

Vyplňte následující pole uvedenými přihlašovacími údaji:

- :guilabel:`Voip Username“ = OnSIP :guilabel:"Uživatelské jméno"
- :guilabel:`OnSIP Auth Username“ = „OnSIP Auth Username“
- :guilabel:`Tajné heslo VoIP“ = OnSIP: „Heslo SIP“

..tip:
Doplněk OnSIP najdete v horní liště uživatele pod záložkami.

Poté přejděte od uživatelského formuláře v Odoo a uložte konfigurace.

Odoo uživatelé mohou po kliknutí na ikonu ☎️ (telefon) provádět telefonní hovory.
v pravém horním rohu Odoo.

.. viz též:
Další kroky nastavení a řešení problémů naleznete v znalostní bázi OnSIP.
<https://support.onsip.com/cs>.

Příchozí hovory
--------------

Odoo databáze také přijímá příchozí hovory, které produkují okna s upozorněním v Odoo. Když
objeví se okno s výzvou k potvrzení, klikněte na zelené tlačítko „☎️“ pro přijetí hovoru.

Pokud chcete zavolat zpět, klikněte na červené ikonu telefonu :guilabel:`📞`.


.. obrázek: onsip/prijimani-volani.png
:align:center
:alt:Zobrazení příchozího hovoru v aplikaci VoIP Odoo.

.. viz též:
:doc:`voip_widget`

Řešení problémů
---------------

Chybějící parametry
~~~~~~~~~~~~~~~~~~

Pokud se zobrazí hlášení o chybějících parametrech v widgetu Odoo, ujistěte se, že obnovíte prohlížeč Odoo.
okno nebo záložku a zkuste to znovu.

.. obrázek: onsip/onsip04.png
:align:center
:alt:Chybějící parametr v widgetu VoIP od společnosti Odoo.

Chybný číslo
~~~~~~~~~~~~~~~~

Pokud se v widgetu Odoo zobrazí hláška *Nesprávný kód*, ujistěte se, že používáte mezinárodní
formát čísla, což znamená začít mezinárodním kódem země.

Zeměpisný kód je identifikační kód, který umožňuje přístup do telefonního systému požadované země.
Nejprve se volá kód země a poté cílový telefonní číslo. Každá země na světě má svůj vlastní
specifický kód země.

Příkladem je např. „16505555555“ (kde „1“ je mezinárodní předvolba pro Spojené státy americké).

.. obrázek: onsip/onsip05.png
:align:center
:alt:Nesprávný text zprávy v hlášení o počtu volání v widgetu VoIP od společnosti Odoo.

.. viz též:
Pro seznam všech zemí s kompletními kódy navštivte: https://countrycode.org
<https://countrycode.org>.

OnSIP na mobilním telefonu
=====================

Pro volání a přijímání hovorů, když uživatel není před Odoo na svém počítači, je potřeba
softwarový telefon na mobilním telefonu lze používat současně s VoIP v Odoo.

Tento přístroj je užitečný pro pohodlné hovory na cestách a také k zajištění slyšitelnosti příchozích hovorů.
Softfone bude fungovat.

.. viz též:
   - :doc:`integrace zařízení“
   - „Stáhnout aplikaci OnSIP <https://www.onsip.com/app/download>“
