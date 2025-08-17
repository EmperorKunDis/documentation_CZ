========================
Zařízení a integrace
========================

Abbreviation: VoIP (voice over internet protocol) can be used on many different devices, such as
počítače, tablety, mobilní telefony a mnoho dalšího. To je užitečné v tom, že snižuje náklady,
Zaměstnanci mohou pracovat z jakéhokoliv místa na světě, pokud mají k dispozici širokopásmové připojení k internetu.

Odoo VoIP je kompatibilní se SIP (Session Initiation Protocol), což znamená, že jej lze používat s jakýmikoli
Aplikace kompatibilní se SIPem.

Tento dokument popisuje proces instalace Odoo VoIP na různých zařízeních.
integrace.

Odoo je plně integrováno se všemi aplikacemi Odoo, což umožňuje uživatelům kliknout do kterékoliv aplikace a naplánovat
volání jako aktivita v chatovací místnosti.

Příklad:
Příkladem je aplikace CRM, kde uživatel může kliknout na příležitost a kliknout na
:guilabel:`Aktivita“ v chatovací místnosti.

Poté mohou vybrat volbu „Zavolat“ a v poli „Termín splatnosti“ si zvolit datum.

Jakmile kliknou na tlačítko „Uložit“, objeví se aktivita v chatu.

Pokud by měl být datum splatnosti dnešním datem, aktivita se zobrazí v :abbr:`VoIP
(hlasová služba přes internetový protokol)

....... obrázek: zařízení/integrace/crm-voip-widget.png
:synchronizace: střed
:alt: Zobrazení kontaktů v CRM a možnost naplánovat aktivitu pro Odoo Discuss.

Odoo VoIP (notebook/stolní počítač)
===================================

Modul a widget Odoo *VoIP* (Voice over Internet Protocol) lze používat z jakéhokoliv prohlížeče na
notebook nebo stolní počítač. Jednoduše klikněte na ikonu v pravém horním rohu :guilabel:`☎️ (telefon)“
v databázi Odoo a widget se zobrazí.

.. viz též:
Zjistit, jak používat widget VoIP (hlasová komunikace přes internet) na stolním počítači nebo notebooku
počítač, podívejte se na tuto dokumentaci: :doc:`voip_widget`.

Odoo VoIP (tablet/mobilní zařízení)
================================

Aplikace Odoo VoIP lze používat na tabletech a mobilních telefonech prostřednictvím aplikace Odoo pro Android nebo iOS.
aplikace. Dále lze databázi přistupovat prostřednictvím mobilního prohlížeče.

.. varování:
Aplikace pro Android a iOS již nejsou podporovány společností Odoo.
Apple portály. To znamená, že podpora Odoo se zabývá pouze omezenými oblastmi Odoo Android nebo Apple IOS
podpora požadavků.

.. důležité:
Při volání z mobilního zařízení lze použít Odoo, ale je třeba mít na paměti, že Odoo není **telefonní
aplikace VoIP (hlasové služby přes internetový protokol) a nezvoní při příchozím hovoru.
hlasové hovory. Pokud uživatel potřebuje být vždy k dispozici na mobilním zařízení, může používat aplikaci, jako je Zoiper,
Je nutné používat aplikace, které zůstávají v pozadí neustále připojené.

Pro více informací se podívejte na tuto dokumentaci: :ref:`voip/zoiper`.

Při přístupu k aplikaci na mobilním zařízení/tabletu otevřete widget VoIP v Odoo, stisknutím
na ikonu „☎️“ v pravém horním rohu. Widget se zobrazí v levém dolním rohu
roh.

Při prvním volání z tabletu pomocí mobilní aplikace je uživatel vyzván k
Povolit databázi používat mikrofon. Klikněte na „Povolit“ při dotazu
Pokračujte v hovoru mikrofonem.

Tento krok je nezbytný pro použití mobilní aplikace Odoo i webového prohlížeče.

.. obrázek: zařízení/integrace/povolit-mikrofon.png
:align:center
:alt:Povolit databázi přístup k mikrofonu.

Odoo poté požádá, jaký způsob hovoru zvolit. Dvě možnosti jsou: :guilabel:`VOIP` nebo :guilabel:`Telefon
(pokud má být tablet připravený k volání). Klikněte na políčko vedle „Pamatovat si?“
bude výchozím nastavením pro všechny budoucí rozhodnutí.

.. obrázek: zařízení_integrace/voip-telefon.png
:align:center
:alt:Okno s výzvou k volbě, zda chcete použít VoIP nebo telefon zařízení pro uskutečnění hovoru.

Tady je návrh, jak vypadá aplikace VoIP v systému Odoo na mobilním zařízení:

.. obrázek: zařízení_integrace/voip-odoo-dashboard.png
:align:center
:alt:Vzhled aplikace pro hlasové volání na mobilním zařízení.

.._voip/zoiper:

Zoiper Lite
===========

*Zoiper Lite* je bezplatná aplikace pro VoIP (hlasová telefonie přes internet) a SIP (zahájení hovoru).
VoIP telefon s hlasovými a videohovory.

Chcete-li začít používat aplikaci Zoiper, stáhněte si ji do zařízení prostřednictvím stránky ke stažení Zoiper.
<https://www.zoiper.com/cs/voip-softphone/stahnout/aktualni/>.

Nejčastější instalací je mobilní zařízení a tento dokument popisuje, jak nastavit na
Aplikace Zoiper pro iOS. Snímky obrazovky a kroky se mohou lišit v závislosti na nastavení.

Po instalaci aplikace Zoiper na mobilní telefon otevřete aplikaci a klepněte na
:guilabel:`Nastavení“. Přejděte na :menuselection:`Účty“ a klepněte na :guilabel:`+ (plus)“.
ikona pro přidání účtu.

Pokud je účet VoIP (Hlasová služba přes internetový protokol) již nastavený, pak klikněte
Ano, což znamená, že uživatelské jméno a heslo byly vytvořeny.

.. obrázek: zařízení/integrace/nastavení účtu Zoiper - skupina.png
:align:center
:alt:Nastavení účtu Zoiper z pohledu mobilního zařízení.

Dále klepněte na :guilabel:`Vyberte poskytovatele“. Na obrazovce, která se zobrazí, klepněte na :guilabel:`Země“,
V pravém horním rohu lze zúžit výběr poskytovatelů na konkrétní zemi. Vyberte zemi
pro poskytovatele, který je konfigurován, pak najděte položku „Poskytovatel“ a vyberte ji.

Příklad:
Pokud je nastavovaným poskytovatelem *Axivox*, pak vyberte Belgii. Pak zvolte
:guilabel:`Axivox“ jako poskytovatele.

.. obrázek: zařízení/integrace/provozovatel-zoiper-odoo.png
:align:center
:alt:Nastavení účtu Zoiper, výběr poskytovatele.

V poli „Možnosti SIP (Session Initiation Protocol)“ zadejte účetní jméno.
„Doména“, „Uživatelské jméno“ a „Heslo“. Všechny tyto informace se liší.
Na základě účtu.

..tip:
Chcete-li se k této informaci dostat, přejděte na portál *Axivox* a v menu vyberte položku „Uživatelé“ – „Vybrat
uživatel --> Upravit --> záložka „Identifikátory SIP“. Uživatelské jméno (SIP), doména
:guilabel:`Heslo SIP“, „Adresa proxy serveru“ a další jsou všechny přítomné v tomto
tabulka

.. seznam tabulkový::
:hlavičky: 1

   * - Zoiper Field
     - Axivox Field
   * - Jméno účtu
     - *Může být cokoliv*
   * Doména
     - Doména
   * - Uživatelské jméno
     - Uživatelské jméno SIP
   * -Heslo
     - Heslo k SIP

Jakmile do pole zadáte své údaje, klikněte na tlačítko „Registrovat“ v horní části stránky.
obrazovce. Jakmile jsou ověřeny registrační údaje, Zoiper vyplní zprávu s informací
:guilabel:`Stav registrace: OK“.

Nyní je Zoiper připravený na volání pomocí VoIP (hlasové telefonování po internetu).
Služba „Protokol“).

.. obrázek: zařízení_integrace/sip-možnosti-zoiper.png
:align:center
:alt:Založení účtu u Zoiperu, registrace proběhla v pořádku.

Linphone
========

Aplikace Linphone je open source aplikací pro VoIP (hlasová telefonie přes internet) a SIP (seskupení hovorů).
Iniciační protokol) pro hlasové, videokonference a zasílání zpráv (skupinových i jednotlivých).
konferenční hovory.

Chcete-li začít používat aplikaci Linphone, stáhněte si ji do zařízení prostřednictvím stránky ke stažení aplikace Linphone.
<https://new.linphone.org/technical-corner/linphone?qt-technical_corner=2#qt-technical_corner>

Nejčastější instalací je mobilní zařízení a tento dokument popisuje, jak nastavit
Aplikace pro iOS Linphone. Snímky obrazovky a kroky se mohou lišit v závislosti na okolnostech.

Chcete-li začít konfigurovat *Linphone* pro použití s poskytovatelem :abbr:`SIP (Session Initiation Protocol)`,
Nejprve otevřete program Linphone a na obrazovce se zobrazí asistent.

Na obrazovce vyberte možnost „Používat účet SIP“. Na další obrazovce zadejte
:guilabel:`Uživatelské jméno“, :guilabel:`Heslo“, :guilabel:`Doména“ a :guilabel:`Zobrazované jméno“.
úplné, stisknout: guilabel:"Přihlásit se".

V tuto chvíli je aplikace Linphone připravena na volání. Jakmile se v horní části objeví zelená tlačítka
aplikační obrazovka s textem „Připojeno“.

.. obrázek: zařízení/integrace/linphone-odoo-setup.png
:align:center
:alt:Nastavení účtu v aplikaci Linphone, registrace proběhla úspěšně.

..tip:
Linphone nabízí širokou škálu aplikací pro mobilní i stolní zařízení v různých operačních systémech.
jako například Windows, Linux, Apple a Android. Protože Linphone je otevřený projekt, existuje mnoho
nové aktualizace jsou vydávány pravidelně.

Podívejte se na stránku dokumentace Linphone na Wiki
<https://wiki.linphone.org/xwiki/wiki/public/view/Linphone/>`.
