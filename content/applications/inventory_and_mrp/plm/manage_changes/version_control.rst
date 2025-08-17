===============
Verzování
===============

.. |BOM| nahradit za: :abbr:`BOM (Seznam materiálů pro výrobu)“
.. |BOM| nahradí::: zkratka: `BoM (Bill of Materials)`
.. |ECO| nahradit za: zkratku: `ECO (Engineering Change Order)`
.. |ECN| nahrazuje: zkratka: `ECN (Engineering Change Notices)`

Použijte systém řízení životního cyklu produktů (PLM) společnosti Odoo k správě předchozích verzí výrobních listů.
(BOMs). Ukládají se do nich původní montážní návody, podrobné informace o součástkách a staré výkresy produktů.
Vynechat z produkce detaily z minulosti.

Při potřebě snadno vrátit se zpět k předchozím verzím BOM. Dále používejte PLM k sledování, která verze BOM
verze byla aktivní na konkrétních dnech pro vzpomínky nebo stížnosti zákazníků.

Každá verze BOM je uložena v *Engineering Change Order* (ECO) pro organizované testování a
vylepšení bez narušování běžné výroby.

.. viz též:
:ref:`Stanovení změny v projektu <plm/eco>`

Aktuální verze BoM
===================

Pro zobrazení aktuální verze BOM používané v produkci přejděte na: menu: `PLM aplikace --> Master
Data-->Seznam materiálů“, vyberte požadovaný seznam „BOM“ a poté přepněte na
kartě „Různé“, kde je aktuální verze BOM.
zobrazeny.

.. poznámka::
|BOMy| lze také zobrazit v nabídce „Výroba“ -> „Produkty“ -> „Souhrnné cenové kalkulace“.
Materiály.

.. obrázek: verze_kontroly/aktuální_verze.png
:align:center
:alt:Zobrazte aktuální verzi BOM v záložce Ostatní.

Historie verze
===============

Chcete-li spravovat všechny verze BOM včetně té současné i budoucích, začněte tím, že se přesunete na
Vyberte „Návrh výrobku“ -> „Produkty“ -> „Seznam materiálů“.

Na stránce BOM klikněte na tlačítko ECO a přepněte se do zobrazení v seznamu.
ikonu „:guilabel:`≣“ v pravém horním rohu.

.. poznámka::
:guilabel:`ECO“ chytrý tlačítko je viditelné pouze v |BOM|, pokud je nainstalována aplikace PLM.

.. obrázek: verze_kontroly/eko-chytrolín.png
:align:center
:alt:Zobrazení tlačítka ECO Smart na BoM.

V seznamu ECO pro produkt přejděte na vyhledávací lištu nahoře a klikněte na
:guilabel:„▼“ ikona vpravo, která umožňuje přístup k rozbalovací nabídce „Filtrů“.

Dále filtrujte podle :guilabel:`Done` |ECOs| a zobrazte seznam revizí |BOM|.
„Odpovědný“ uživatel, který změnu aplikoval, a „Datum účinnosti“
|BOM|.

Každý z těchto |ECO| kliknutím otevřete minulé součástky, operace a návrhové soubory spojené s
|BOM|.

.. obrázek:: verze_kontroly/eko-list.png
:align:center
:alt:Zobrazit historii revizí ECO pro produkt v rámci BOM.

.. poznámka::
Pokud pole „Datum účinnosti“ je prázdné, datum účinnosti pro ECO bude
automaticky nastaven na „Co nejdříve“ a nejsou zaznamenány žádné datumy v revizi
historie BOMu.

.... obrázek:: verze_kontroly/bez_účinného_data.png
:synchronizace: střed
:alt: Seznam platných dat BOM.

..tip:
Kontrolu, kdy byla zveřejněna BOM, lze obejít tak, že se přesunete do chatu a na kurzor myši.
V průběhu času byl |ECO| přesunut do fáze :ref:`zavírání <plm/eco/stage-config>`.

Designové soubory
============

Připojte soubory CAD (CAD), PDF, obrázky nebo jiný návrhový materiál k BOM.
sama o sobě.

Pro toto vyberte v menu: „PLM aplikace -> Strojní části -> Seznam součástek“ a poté vyberte
požadované |BOM|. Na |BOM| přejděte do části „Chat“ a klikněte na ikonu „📎 (špendlík)“.
ikonu.

Soubory spojené s |BOM| jsou zobrazeny v sekci Soubory. Chcete-li přidat další
designové soubory, vyberte tlačítko „Připojit soubor“.

.. obrázek: verze_kontroly/připojit soubory.png

:alt:Zobrazte ikonu špendlíku v chatu, abyste mohli připojit soubory k BoM.

Správa návrhových souborů v ECO
-----------------------------

Přidejte, upravujte a odstraňte soubory v |ECO|. Jakmile je |ECO| schváleno a aplikováno, nové soubory jsou
automaticky propojené s výrobním BOM. Archivované soubory jsou z BOM odstraněny, ale
Dokument je stále dostupný v ECO.

Pro správu návrhových souborů v aplikaci PLM začněte tím, že se přesunete na:
a vyberte požadovanou |ECO|. Následně otevřete stránku „Přílohy“ kliknutím na
:guilabel:`Dokumenty“ chytrý tlačítko.

Přejděte nad každou přílohou a zobrazí se ikonka „︙“ (tři svislé tečky). Odkudkoliv pak
vybrat, zda chcete soubor upravit, odstranit nebo stáhnout.
změny v těchto souborech jsou obsaženy v |ECO| a budou se vztahovat pouze na výrobu.
Jakmile jsou změny aplikovány (viz:plm/eco/apply-changes).

Příklad:
Ve složce „Vytvořit klávesnici s 60 % kláves“ je soubor s návrhem z původního „klávesnice se 100 % kláves“
Nejprve vyberte tlačítko „Dokumenty“ v seznamu chytrých tlačítek.

.... obrázek: verze_kontroly/tlačítko_inteligentního_dokumentu.png
:synchronizace: střed
:alt:Zobrazit tlačítko pro chytré dokumenty z aktivního ECO.

Na stránce „Přílohy“ přejeďte kurzorem nad soubor s názvem „100% klávesnice manuál.pdf“ a
Klikněte na ikonu tří teček vedle názvu aplikace. Pak klikněte na možnost „Odebrat“.
archivovat soubor.

Poté na stejné stránce „Přílohy“ klikněte na tlačítko „Nahrát“, abyste nahráli
nové soubor s návrhem klávesnice označené jako „Manuál 60 %“.

.. obrázek:: verze_kontroly/přílohy.png
:synchronizace: střed
:alt: Zobrazení stránky s přílohami z tlačítka chytré funkce „Dokumenty“. Zobrazí jednu archivovanou a
jedna nová příloha.

.. poznámka::
Archivované soubory nejsou trvale smazány - lze je stále přistupovat v původní složce.
|ECO| nebo jako archivovaný soubor v nejnovější verzi |ECO|, kde k archivování došlo.

Použijte příkaz rebase
============

Odoo usnadňuje řešení konfliktů při slučování změn, které provádí souběžně více uživatelů na stejném produktu.

Konflikty mohou nastat, když je aktualizována výrobní BOM a další ECOs mění
předchozí verze. Rozdíly mezi novou a předchozí verzí výrobního listu jsou zobrazeny v
:guilabel:`Předchozí změny v Eco Bomb“ tabulka, která je viditelná pouze ve scénáři.

Pro vyřešení konfliktů a zachování změn v ECO klikněte na tlačítko „Použít rebase“.

Příklad:
Dva ECO, „ECO0011“ a „ECO0012“, vzniknou při aktuální verzi BOM 5.
„ECO0011“, nová komponenta „Stabilizátor prostoru“ je přidána a změny se aplikují. To znamená
aktuální verze BOM je „6“.

.. obrázek:: verze_kontroly/branch-change.png
:synchronizace: střed
:alt: Použijte změny v ECO k aktualizaci výrobního seznamu položek.

To znamená, že „ECO0012“ upravuje zastaralý |BOM|. Podle obrázku v sekci :guilabel:`Předchozí eko BOM
V záložce „Změny“ chybí „Stabilizátor prostoru“.

abyste zajistili, že se změny aplikované v ECO0011 udrží i při změnách v ECO0012, klikněte
tlačítko „Použít rebase“ k aplikaci předchozích změn |ECO| bez ovlivnění
změny již provedené v ECO0012.


:synchronizace: střed
:alt:Klikněte na tlačítko „Použít převod“ a aktualizujte BOM tak, aby odpovídaly BOM pro výrobu.

