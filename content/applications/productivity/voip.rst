Zobrazit obsah

===================================
VoIP (hlasová telefonie přes internetový protokol)
===================================

.. |VOIP| nahradit za: zkratku: `VoIP (hlasová služba přes internetový protokol)`

V Odoo je možné provozovat hovory přes internet, a to díky integraci s
Odoo aplikace jako například CRM, Helpdesk a další. Hovory a zprávy jsou evidovány v těchto aplikacích.
evidence spojené s interakcemi se zákazníky.

.. viz též:
„Návody k Odoo: VoIP <https://www.odoo.com/slides/voip-voice-over-ip-315>“

Uživatelé mohou volat a přijímat hovory, sledovat historii komunikace a automaticky směrovat hovory podle
předdefinované pravidlo. Funkce jako záznam hovorů a analýza poskytují informace o počtu volání a
doba odpovědí, pomáhající týmům sledovat efektivitu komunikace.

.. karty:
....... karta: Akce VoIP
:target: voip/voip_widget
:velké:

Zorientujte se s funkcemi widgetu VoIP, jako jsou akce, které lze během hovoru provést.
hovor.

...... karta: Zařízení a integrace
:target:voip/integrace-zařízení
:velké:

Zjistěte, jak získat přístup k widgetu VoIP z různých zařízení (např. telefonů) a aplikací (např.
Linphone.

VoIP termíny
==========

- **VoIP**: Voice over Internet Protocol. Technologie, která se používá k řešení hovorů, které nejsou uskutečněny
z telefonní linky.
- **SIP**: Session Initiation Protocol. Technologie zahrnutá v |VOIP|, která se specificky stará o
zřízení, správa a ukončení hovorů.
- Pořadník hovorů: Systém pro směrování hovorů (obvykle v podpoře). To umožňuje zákazníkům čekat.
pokud nejsou k dispozici žádní pracovníci podpory.
- **Plány telefonních čísel**: Systém definující, jak jsou hovory VoIP směrovány podle stanovených pravidel.

Nastavte VoIP
==============

Pro použití VoIP je třeba nejprve nainstalovat modul VoIP podle pokynů v části „Instalace“ a poté se připojit k síti VoIP pomocí příkazu:

Jakmile modul nainstalujete, v horní části obrazovky se zobrazí ikona
obrazovce. Zde se uskutečňují hovory z Odoo. Když na tento ikonu kliknete, otevře se VOIP
Na obrazovce se zobrazuje okno s widgetem, kde lze odesílat e-maily, shromažďovat informace o uživatelích a zaměstnancích.
upravit a spravovat aktivity. Zatímco je tento widget otevřený, může uživatel procházet
prostřednictvím svých aplikací Odoo.

Používání VoIP vyžaduje poskytovatele služeb. Další část vysvětluje, jak se připojit k službě
poskytovatel do databáze Odoo.

VoIP poskytovatelé
--------------

Připojení k VoIP je v Odoo minimální, většina konfigurace se provádí ve službě VoIP
poskytovatelé. Dva ověření poskytovatele jsou :doc:`OnSIP <voip/onsip>` a :doc:`Axivox <voip/axivox>“.
Klikněte na karty níže, abyste se dozvěděli, jak tyto poskytovatele služeb nakonfigurovat v databázi Odoo.
Tyto poskytovatelé nemohou být použity a alternativní poskytovatel musí splňovat tyto požadavky na připojení.
Odoo:

- Hostitel VoIP musí poskytnout přístup k SIP serveru prostřednictvím websocketového spojení.
- Hostitelský server musí podporovat protokol WebRTC.

Pro přidání alternativního poskytovatele kreditů otevřete aplikaci **Nastavení** a vyhledejte VoIP.
V sekci „Spojování“ pod „VoIP“ klikněte na „Spravovat poskytovatele“.
A pak klikněte na tlačítko „Nový“ a zadejte požadované informace (například adresu websocketu).
že pole „Doména OnSIP“ je místo, kam se ukládá doména vytvořená alternativním poskytovatelem.

Pokud se objeví jakékoliv problémy s poskytovatelem služby VoIP, obraťte se na jejich podporu.
týmu. Pokud se při nastavování služby VoIP v Odoo vyskytnou problémy, postupujte podle
:ref:`kroky k řešení problémů <voip/voip_widget/troubleshooting_voip>“.

.. varování:
Odoo nemůže ověřit, že každý alternativní poskytovatel je kompatibilní s jejich systémem.
Pokud jsou splněny výše uvedené požadavky, neměly by být nalezeny žádné problémy.

.. karty:
...... karta: Konfigurace Axivoxu
:target: voip/axivox
:velké:

Naučte se, jak nastavit Axivox v Odoo. To zahrnuje přidání uživatelů do Axivoxu a nastavení hovorů
fronty, a mnoho dalšího.

.......karta: Konfigurace OnSIP
:target: voip/onsip
:velké:

Naučte se, jak nastavit OnSIP v Odoo. To zahrnuje vložení přihlašovacích údajů OnSIP do Odoo.
řešení problémů.

Práce s VoIP
==============

Tady jsou některé běžné pracovní postupy pro Odoo |VOIP|. Tato technologie je obzvláště populární u
Prodejní týmy a podpůrné týmy, ale mohou být užitečné i pro jiné týmy.

.. karty:
...... karta:Prodejní týmy a VoIP
:target: voip/prodej
:velké:

Zjistěte, jak používat VoIP pro tým obchodníků. To zahrnuje uskutečňování telefonických hovorů, řešení následných kroků a
a v průběhu hovoru zaslat nabídku na prodej.

.. karta: Podpora front a VoIP
:target:voip/podpora
:velké:

Zjistěte, jak používat VoIP pro podporu týmu. To zahrnuje připojení se do fronty hovorů jako operátor.
řešení požadavků na podporu, které vyžadují telefonické hovory.

.. toctree::


voip/onsip
voip/axi-vox
voip/voip_widget
voip/integrace_s_zařízeními
voip/prodej
voip/podpora
