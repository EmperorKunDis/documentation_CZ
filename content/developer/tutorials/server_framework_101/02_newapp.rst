============================
Díl 2: Nová aplikace
============================

Účelem této kapitoly je vytvoření základu pro vytváření nového modulu Odoo.
Začneme od nuly s minimem, co je potřebné k tomu, aby náš modul byl uznán v Odoo.
V dalších kapitolách postupně přidáme funkce, abychom vytvořili reálný podnikatelský plán.

Modul Reality
====================================

Náš nový modul pokrývá oblast podnikání, která je velmi specifická, a proto není zahrnuta v
standardní sada modulů: nemovitosti. Zajímavé je, že před
při vývoji nového modulu je dobrým zvykem ověřit, zda Odoo již neposkytuje způsob
Odpovědět na konkrétní obchodní případ.

Níže je přehled hlavního seznamu obsahující některé reklamy:

.. obrázek: 02_newapp/overview_list_view_01.png
:align:center
:alt: Zobrazení seznamu 01

Horní část formuláře zobrazuje důležité informace o nemovitosti, například jméno.
druh nemovitosti, poštovní směrovací číslo a podobně. První záložka obsahuje informace popisující
Vlastnictví: ložnice, obývací pokoj, garáž, zahrada...

.. obrázek: 02_nováaplikace/přehled_formulář_výběr_01.png
:align:center
:alt: Zobrazení formuláře 01

Druhá záložka nabízí nemovitosti, které jsou v nabídce. Zde vidíme, že potenciální kupci mohou
nabídnout cenu nad nebo pod očekávanou prodejní cenou. Rozhodnutí, zda nabídku přijmout, je na prodávajícího.

.. obrázek: 02_novy_aplikace/prihled_formulare_viz_02.png
:align:center
:alt: Zobrazení formuláře 02

Tady je rychlý videonávod, jak modul funguje.

Ať už se to stane brzy nebo později, snad tento záznam bude brzy k dispozici.

Připravte adresář s doplňky
===========================

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`manifest <reference/module/manifest>“.

.. poznámka::

**Úkol**: cílem této části je mít Odoo poznat naši novou modulu, která bude
bude prázdná skořápka, zatímco bude v seznamu aplikací:

....... obrázek: 02_newapp/app_v_seznamu.png
:synchronizace: střed
:alt: Nový modul se objeví v seznamu

Prvním krokem při vytváření modulu je vytvoření jeho adresáře. V příkazu
adresář, přidat nový adresář: soubor `estate`.

Modul musí obsahovat alespoň 2 soubory: „__manifest__.py“ a „__init__.py“.
Soubor „__init__.py“ může zůstat zatím prázdný a vrátíme se k němu v další kapitole.
Na druhou stranu soubor „__manifest__.py“ musí popisovat náš modul a nemůže zůstat prázdný.
Jeho jediným povinným polem je „název“, ale obvykle obsahuje mnohem více informací.

Podívejte se na
„Soubor CRM <https://github.com/odoo/odoo/blob/fc92728fb2aa306bf0e01a7f9ae1cfa3c1df0e10/addons/crm/__manifest__.py#L1-L67>“
například. Kromě popisu modulu („název“, „kategorie“
„souhrn“, „webová stránka“…), uvádí své závislosti („závisí na“). Závislost znamená, že
Rámec Odoo zajistí instalaci těchto modulů před naším modulem. Dále, pokud
Jedna z těchto závislostí je odinstalována, pak bude také odinstalován náš modul a **jakýkoliv další, který na něj závisí.
je odinstalovatelný**. Zkuste si představit svůj oblíbený balíkovací systém pro distribuci Linuxu
(„apt“, „dnf“, „pacman“…): Odoo funguje stejným způsobem.

... cvičení: Vytvořte požadované doplňkové soubory.

Vytvořte následující složky a soubory:

    - „/home/$USER/src/tutorials/estate/__init__.py“
    - „/home/$USER/src/tutorials/estate/__manifest__.py“

Soubor „__manifest__.py“ by měl definovat pouze název a závislosti našich modulů.
Prozatím je nutný pouze modul „base“.


Restartujte server Odoo a přejděte do aplikací. Klikněte na „Zobrazit seznam aplikací“, vyhledejte „estate“ a...
tadaa, váš modul se objevil. Neobjevil se? Možná zkuste odstranit výchozí filtr „Aplikace“ :-)

.. varování:
Pamatujte na zapnutí režimu vývojáře, jak je vysvětleno v předchozím odstavci.
kapitolu. Jinak tlačítko „Zobrazit seznam aktualizací“ neuvidíte.

... cvičení: Udělejte z vašeho modulu aplikaci.

Přidejte odpovídající klíč do souboru „__manifest__.py“, aby se modul zobrazil v části „Aplikace“.
Filtr je zapnutý.

Můžete si dokonce nainstalovat modul! Ale je jasné, že se jedná o prázdný obal, takže vám žádné nabídky nezobrazí.

Vše v pořádku? Pak můžeme začít s tvorbou naší první šablony <03_basicmodel>!
