=====================
Nastavení čtečky čárových kódů
=====================

.. _čárový kód/nastavení/hardware:

Přečtěte si tento průvodce, abyste zvolili a nastavili snímač čárového kódu kompatibilní s Inventářem v Odoo.
Aplikace s čárovými kódy.

.. obrázek:: hardware/skener-kodovych-značek.png
:align:center
:alt: Obrázek skenovacího zařízení čárového kódu jako příklad.

Typy skenerů
=============

Před zapojením čárového kódu je důležité určit, který typ skeneru nejlépe vyhovuje
potřebám podnikání. Existují tři hlavní typy skenerů, které lze použít s Odoo, každý
s vlastními výhodami a užitím:

- **Skenery USB** jsou připojeny k počítači a jsou vhodné pro podniky, které skenují produkty.
na pevné pozici, jako je například fronta u pokladny v potravinách.
- **Skenery Bluetooth** se spárují s telefonem nebo tabletem a jsou tak levné a
možnost přenosného čárového kódu. V tomto případě je Odoo nainstalován na chytrém telefonu a umožňuje
dodavatelé skladových služeb mohou provádět operace a kontrolovat zásoby přímo prostřednictvím svých mobilních zařízení.
- **Mobilní skenery čárových kódů** jsou mobilní zařízení, která mají zabudovaný skenovací čtečku čárových kódů.

.. důležité::
Pokud používáte skenovač připojený k USB, ujistěte se, že je skenovač kompatibilní s klávesnicí
počítač.

Pokud používáte mobilní počítačový skener, ujistěte se, že zařízení bude schopno spustit aplikaci Odoo Mobile.
Některé z nových modelů používají operační systém Android s prohlížečem Google Chrome nebo operační
Edge by měl fungovat, ale testování je zásadní kvůli široké nabídce dostupných modelů a
konfigurace.

.. viz též:
„Odoo Sklad a štítky – kompatibilní hardware“

Konfigurace
=============

Při nastavování čtečky čárových kódů se ujistěte, že jsou správně nastaveny následující konfigurace, aby
snímač dokáže správně interpretovat čárové kódy s Odoo.

Klávesnice
---------------

Při používání skenovacího zařízení se zásuvkou USB je třeba nastavit klávesnici podle klávesnice operačního systému.
správné interpretování znaků. Obecně by měl být zapnutý režim skenování, který přijímá USB
klávesnice (HID) s nastavením jazyka podle klávesnice, která je v danou chvíli používána.

Pro konfiguraci klávesnice pro skener Zebra je potřeba naskenovat čárový kód klávesnice.
požadovaný jazyk v uživatelské příručce skeneru.

.. obrázek: hardware/klávesnice-čárový kód.png
:align:center
:alt: Příklad uživatelské příručky pro klávesnici.

Příklady nastavení klávesnice v uživatelské příručce pro skenery Zebra.

Automatické vrácení se na začátek řádku
-------------------------

Odoo má výchozí 100ms pauzu mezi skeny, aby se zabránilo náhodnému dvojitému skenování.
synchronizovat s čtečkou čárových kódů, nastavit ji tak, aby obsahovala „vratný znak“ (:dfn:„zpětný uvozovek“)
klávesu „Enter“ na klávesnici) po každém skenování. Odoo interpretuje ukončení řádku jako konec
skenování čárového kódu; takže Odoo přijímá sken a čeká na další.

Obvykle se na skeneru automaticky zobrazuje mezera. Zkontrolujte, jestli je nastavená
specifický čárový kód v uživatelské příručce, například „ON CR suffix“ nebo „Použijte klávesu Enter pro přidání znaku“.

Čtečka čárových kódů zebra
=============

Při používání snímačů značky Zebra zkontrolujte následující nastavení klávesnice, aby se předešlo chybám.

Začněte na domovské obrazovce skenovače Zebra a vyberte aplikaci DataWedge (aplikace je
jejichž ikona je ve tvaru „(světle modrá čárovka)“.

Na stránce „Profily DataWedge“ vyberte možnost profilu pro přístup k snímači značky Zebra.
Nastavení.

.. varování:
Není doporučeno používat profil „DWDemo“, protože nefunguje správně na všech zařízeních.
okolností.

Není doporučeno používat již existující profily, ale vytvořit si nový, osobní profil. Jakmile bude nový profil vytvořen, přidejte
aplikace *Odoo Mobile* a aplikace *Google Chrome* v sekci „Související aplikace“ na skenovacím zařízení.
domovská obrazovka.

Jakmile si vyberete profil, přejděte dolů na možnost „Výstup z klávesnice“ a ujistěte se, že
Volba „Zapnout/vypnout zadávání klávesových zkratek“ je nastavena na „Povoleno“.

.. obrázek: hardware/enable-keyboard.png
:align:center
:alt:Zobrazit možnost klávesové zkratky v aplikaci DataWedge pro skenery Zebra.

Jakmile je tato možnost zapnutá, přejděte zpět na stránku s nastavením profilu a přejděte do
V části „Zpracování stisknutí klávesnice“. Poté otevřete podnabídku „Možnosti zpracování stisku klávesy“.
Zkontrolujte, zda je zaškrtnutá možnost „Přenášet znaky jako události“.

.. důležité::
V poli „Odeslat znaky jako událost“ musí být zaškrtnuto na skeneru Zebra.
Odoo **není schopna rozpoznat skenované čárové kódy.

Jakmile jsou všechny tyto kroky splněny, proveďte testovací skenování, abyste si ověřili, že skener Zebra funguje.
správně, jak bylo zamýšleno.

Mobilní skenovací terminál společnosti Honeywell
=================================

Při používání snímačů Honeywell postupujte podle níže uvedených pokynů, abyste mohli číst kódy.
Odoo.

Začněte na domovské obrazovce skenovacího zařízení Honeywell a vyberte „Nastavení“, které je znázorněno
:guilabel:„Nastavení Honeywell“ a poté
:guilabel:`Skenování“.

Zde klikněte na položku „Vnitřní skener“ a poté na „Výchozí profil“.
Výsledný seznam možností vyberte položku „Nastavení zpracování dat“.

Vlastnosti zpracování dat z čárového kódu jsou definovány v záložce „Nastavení zpracování dat“.
Najděte nastavení „Metoda vrtule“. Výchozím nastavením je „Standardní“.

.. obrázek:: hardware/hardware-honeywell-settings.png
:align:center
:alt:Nastavení zpracování dat pro snímač Honeywell.

Změňte nastavení „Metoda klávesnice“ na „Klávesnici“.

Po dokončení kroků proveďte kontrolní sken, abyste si ověřili, že skener Honeywell funguje tak, jak má.
účelově.

Mobilní počítač s čtečkou kódů od společnosti CipherLab
=================================

Při používání snímačů CipherLab postupujte podle níže uvedených pokynů, abyste mohli čárové kódy bezpečně skenovat.
Odoo.

Začněte na domovské obrazovce skenovače CipherLab a přejděte do složky „Aplikace“ (vše
Aplikace „Čtečka nastavení“. Pak klikněte na aplikaci „Nastavení čtečky“, která je zobrazena oranžovým
:guilabel:„⚙️“ (kolečko) nad modrým „(štítkem)“.

Poté vyberte profil „Výchozí“ nebo vytvořte nový profil, pokud je potřeba.

V sekci „Obecné nastavení“ klikněte na „Export dat“, následně
:guilabel:`Emulace klávesnice“.

.. obrázek: hardware/hardware-cipherlab-settings.png
:align:center
:alt: Nastavení výstupu dat skenovacího zařízení Cipherlab.

Výchozí hodnotou je „Způsob zadávání“, který se nachází pod „Emulace klávesnice“ a je nastaven na
Nastavení změňte na „Klíčové události“.

.. obrázek:: hardware/hardware-cipherlab-emulation.png
:align:center
:alt:Nastavení klávesnice skenovacího zařízení CipherLab.

Po dokončení kroků proveďte testovací sken, abyste si ověřili, že skener Cipherlab funguje správně.
účelově.

.. viz též:
:doc:`../nastaveni/software`
