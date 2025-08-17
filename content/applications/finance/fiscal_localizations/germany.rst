=======
Německo
=======

Účetnictví
==========

Klasifikační schéma
-----------------

Oba typy účetních knih SKR03 i SKR04 jsou v Odoo podporovány. Když vytvoříte nový online účet v Odoo
databáze SKR03 je instalována výchozím nastavením.

Zkontrolujte, zda je nainstalována v sekci „Účetnictví“ – „Konfigurace“ – „Nastavení“.
a zkontrolovat pole „Zboží“ pod záložkou „Daňové lokalizace“.

.. varování:
Vybrat jiný balíček je možné pouze v případě, že účetní záznam zatím nebyl vytvořen.
Pokud je zveřejněno nové oznámení, musí být zřízena nová společnost nebo databáze pro výběr dalšího balíčku.
Kromě toho budou všechny záznamy vedení účetnictví potřeba znovu vytvořit.

Zprávy
-------

Následující německé zprávy dostupné v Odoo Enterprise:

- Výsledovka
- Zisk a ztráta
- Daňový přehled (Přiznání k dani z přidané hodnoty)
- Seznam prodejů
- Intrastat

Exportování záznamů z Odoo do DATEV
------------------------------------

Pokud by jeden z německých daňových balíčků
Pokud je nainstalován modul <fiscal_localizations/packages>, můžete exportovat účetní záznamy z Odoa do
Datový soubor z účetní knihy.

Export je potřeba provést dvakrát: nejprve export DATAV ATCH, pak export DATAV DATA.

.. poznámka::
Oba jsou potřeba v různých fázích pro přenos dat správně do DATEV, protože DATEV pracuje s
dvě rozhraní, jedno pro klienty (DUO - DATEV Unternehmen Online) a druhé pro daňové poradce (DATEV
Revize účetnictví).

1. DATEV ATC
~~~~~~~~~~~~~

Přejděte do sekce „Účetnictví“ - „Zprávy“ - „Obecná kniha“, klikněte na ikonu „fa-cog“.
Tlačítko „Akce“ a vyberte „Datový soubor ATCH (ZIP)“.

.. obrázek:germany/datev-export.png
:alt: Menu akcí účetního deníku s exporty do DATEV

Nahrát stažený ZIP soubor pomocí programu DATEV Belegtransfer <https://www.datev.de/web/de/service-und-support/software-bereitstellung/download-bereich/betriebliches-rechnungswesen/belegtransfer>.

Pokud na svém počítači nemáte nainstalovaný program DATEV Belegtransfer, požádejte o radu daňového poradce.
Pomůžeme vám s tím.

.. varování:
Soubor DATEV ATCH ZIP obsahuje soubory (hlášení), které jsou spojeny s fakturou nebo účtem v Odoo.
faktura zákazníka, soubor musel být vytvořen pomocí tlačítka „Tisk a odeslání“
tlačítko. Pro faktury dodavatelů musí být soubor přijat e-mailovou adresou nebo nahrán.
pomocí tlačítka „Nahrát“.

.. varování: soubor ZIP s příponou .ATCH

ZIP soubor obsahuje dvě typy souborů:

   - individuální fakturační soubor (PDF, JPEG atd.) pro vybrané období na hlavní
účetní kniha.
   - Soubor XML, který se používá k generování jedinečného identifikátoru (GUID) pro každý soubor.

Tyto jedinečné identifikátory jsou nezbytné, protože umožňují DATEVu automaticky propojit soubory s příslušnými daty.
samostatné položky periodik, které budou importovány s datovým souborem DATEV v dalších krocích.

2. DATA DATAV
~~~~~~~~~~~~~

Přejděte do sekce „Účetnictví“ - „Zprávy“ - „Obecná kniha“, klikněte na ikonu „fa-cog“.
tlačítko „Akce“ a vyberte „Datav DATA (zip)“.

ZIP soubor stažený z webu převeďte svému daňovému poradci. Ten by měl ZIP soubor doplnit do systému DATEV
Účetnictví.

Zeptejte se svého daňového poradce, jak často potřebují tyto soubory.

.. varování: soubor ZIP s příponou .ATCH

ZIP soubor obsahuje tři soubory CSV.

   - soubor EXTF_customer_accounts.csv obsahující všechny informace týkající se vašeho
zákazníci
   - soubor EXTF_vendor_accounts.csv obsahující všechny informace o vašich dodavatelích.
a
   - souboru EXTF_accounting_entries.csv obsahující všechny položky účetních záznamů za období definované
účetní knihu i jedinečné identifikátory (GUID), aby se záznamy mohly propojit s položkami v účetnictví.
soubory uvnitř archivu DATEV ATCH ZIP.

..._nemecko/gobd:

Splnění požadavků GOBD
---------------

**GoBD** znamená *Zásady pro řádné vedení a ukládání knih.
Záznamy a dokumenty ve formátu elektronických souborů a k přístupu ke datům. Zkrátka jde o
pokyny pro správné nakládání a skladování knih, záznamů a dokumentů v elektronické podobě
a také pro přístup k datům, která jsou relevantní pro německou daňovou správu a daňové přiznání.
Výsledovka.

Tyto principy byly napsány a zveřejněny Federálním ministerstvem financí (BMF).
Listopad 2014. Od ledna 2015 jsou **normou** a nahradily dříve
přijatých postupů v oblasti počítačové evidence.
Pro rok 2019 a leden 2020 je nutné specifikovat některé obsahy vzhledem k vývoji digitálních řešení.
(hosting v cloudu, papírové společnosti apod.)

.. důležité::
Odoo je certifikováno jako **splňující požadavky GoBD**.

Poznání požadavků GoBD v souvislosti s účetními programy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Povinnost dodržovat GoBD se vztahuje na společnosti povinné k předkládání účetní závěrky**, což jsou i malé a střední podniky.
osobám samostatně výdělečně činným a podnikatelům. Protože takový poplatník je
je jediným plně odpovědným subjektem za uchovávání úplných a vyčerpávajících daňových dat (shora uvedených)
finanční a související údaje)

Kromě požadavků na software je uživatel povinen zajistit vnitřní kontrolní systém.
§ 146 zákona o dani z přidané hodnoty*)

- kontrola přístupových práv.
- segmentace odpovědnosti, funkční oddělení.
- kontroly vstupu (oznamování chyb, kontrola pravděpodobnosti).
- sjednocení kontrol při zadávání dat
- kontroly zpracování.
- opatření k zabránění záměrnému nebo neúmyslnému pozměňování softwaru, dat nebo dokumentů.

Uživatel musí přidělit úkoly v rámci své organizace na příslušná místa (kontrola).
ověřit, že úkoly jsou řádně a kompletně vykonány (doplnění: dozor). Výsledkem těchto
kontroly musí být zaznamenány (dokumentace) a pokud se při nich objeví chyby
Přijmout vhodná opatření k nápravě situace (prevence).

Bezpečnost dat
~~~~~~~~~~~~~

Daňový poplatník musí zajistit systém proti ztrátě dat v důsledku smazání, odstranění nebo krádeže
jakákoliv data. Pokud nebudou účetní záznamy dostatečně zabezpečeny, bude se jevit jako nespolehlivé
v souladu s pokyny GoBD.

Jakmile jsou objednávky konečně zveřejněny, už je nelze změnit nebo smazat.
aplikace.

- Pokud je Odoo používán v cloudu, pravidelné zálohování je součástí služby Odoo Online. Kromě toho
pravidelné zálohy lze stáhnout a uložit na externí systém.

......viz také:
„Služba Odoo Cloud – Smlouva o úrovni služeb <https://www.odooo.com/cloud-sla>“

- Pokud je server provozován lokálně, uživatel je zodpovědný za vytvoření potřebných záloh.
infrastruktura.

.. důležité::
V některých případech musí být data uložena po dobu deseti let nebo déle, takže vždy mějte zálohy.
Ještě důležitější je, pokud se rozhodnete změnit poskytovatele softwaru.

Zodpovědnost softwarového vydavatele
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pokud se GoBD vztahuje pouze na daňového subjektu, **nemůže být výrobce softwaru za žádných okolností postižen.
odpovědné za přesné a v souladu s předpisy zaznamenání finančních transakcí svých uživatelů.
dat**. Může jen poskytnout uživateli potřebné nástroje k respektování softwarových souvislostí
pokyny popsané v GoBD.

Zajištění souladu prostřednictvím Odoo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Klíčová slova v souvislosti s GOBD jsou: **sledovatelné, ověřitelné, pravdivé, jasné a kontinuální**.
Zkrátka potřebujete mít vytvořený archivovatelný audit a Odoo Vám poskytne prostředky k tomu.
dosáhnout všech těchto cílů:

#. | **Sledovatelnost a ověřitelnost**
|Každý záznam v Odoo je označen jménem tvůrce dokumentu, datem vytvoření a
datum změny a kdo ji provedl. Dále jsou sledovány relevantní položky, takže je
vidět, která hodnota byla změněna kým v chatu daného objektu.
#|**Úplnost**
|Všechny finanční údaje musí být zaznamenány v systému a nesmí chybět žádné položky. Odoo zajišťuje, že
neexistuje mezera v číslování finančních transakcí. Jejich pořadí je na odpovědnosti
uživatelé kódují veškerá finanční data v systému. Většina finančních dat v Odoo je generována
automaticky zůstává na uživateli, aby všechny faktury dodavatelů kódoval.
různé operace úplně.
#. | **Přesnost**
|Odoo zajišťuje, že s vhodně nastavenou konfigurací jsou používány správné účty. Dále
kontrolní mechanismy mezi objednávkami a fakturami.
odrážet skutečnost podnikání. Je na uživateli, aby skenoval a připojil
papírový fakturu dodavatele do příslušného záznamu v Odoo. Pomůže vám s tím Odoo Dokumenty.
automatizovat tuto činnost.
#. | **Včasné rezervace a evidování záznamů**
| Většina finančních dat v Odoo pochází z transakčních objektů (např.
(při potvrzení objednávky), Odoo zajišťuje automatické včasné zpracování účetních dokladů.
odpovědnost uživatele za včasné kódování všech faktur dodavatelů.
jako různé operace.
#. | **Pořadí**
|Finanční údaje uložené v Odoo jsou, podle definice, uspořádány a lze je přeorganizovat dle
většina políček obsažených ve schématu. Přesný pořadí není stanoveno GOBD, ale
Systém musí zajistit, aby finanční transakce mohla být rychle nalezena třetí stranou.
odborníkem. To zajišťuje Odoo již v základní verzi.
#. | **Nepřekonatelnost**
|S německou lokalizací Odoo je Odoo v základním nastavení takto konfigurován, že
nezměnitelnost ustanovení lze bez dalších úprav dodržet.

Export GOBD
~~~~~~~~~~~

V případě daňové kontroly může finanční úřad požádat o tři stupně přístupu k
účetní systém (Z1, Z2, Z3). Tyto úrovně se liší od přímého přístupu k rozhraní až po
předání finančních údajů na záznamové médium.

V případě předání finančních dat na úložný prostředek nejsou
formátu. Může být například ve formátu XLS, CSV, XML, Lotus 123, SAP, nebo jiném.
Odoo podporuje vývoz finančních dat z tabulky CSV a XLS přímo z výchozího nastavení.
Export do konkrétního XML formátu GOBD (viz „Přílohy“).
Předání nosičů dat“ § 3, ale není závazný.

Nesplnění
~~~~~~~~~~~~~~

Pokud porušíte zákon, můžete se těšit na pokutu a soudní příkaz k vrácení
zavedení konkrétních opatření.

..._německo/poz:

Prodejní místo
=============

Technická bezpečnostní opatření
-------------------------

**Zákon o ochraně před manipulací s digitálními záznamy**
vyžaduje, aby elektronické systémy evidence - včetně bodu prodeje
) musí být vybaveny technickým zabezpečovacím systémem.
(dříve také nazývané TSS nebo TSE).

Odoo nabízí služby, které jsou v souladu s platnými zákony díky „Fiskalům <https://fiskaly.com>“,
*řešení založené na cloudu*.

.. důležité::
Protože je tato aplikace cloudová, je nutný připojení k internetu.

.. poznámka::
Jedinými povolenými sazbami DPH jsou ty, které uvedl Fiskal. Tyto sazby si můžete ověřit na
'Fiskalní rozhraní DSFinV-K API: definice DPH
<https://developer.fiskaly.com/api/dsfinvk/v0/#tag/DPH-Definice>.

Konfigurace
~~~~~~~~~~~~~

:ref:`Instalovat <generální/instalace> certifikátu pro prodejní místo v Německu“
(`l10n_de_pos_restaurant`)
(moduly `l10n_de_pos_res_cert`).

.. tip::
Pokud se tyto moduly nezobrazují, aktualizujte seznam aplikací podle návodu v části „Instalace“ (viz odkaz výše).

Zaregistrujte si firmu u finančního úřadu
***********************************************

Pro registraci společnosti otevřete aplikaci „Nastavení“, klikněte na „Aktualizovat informace“ pod
V sekci „Společnosti“ a vyplňte následující pole:

- :guilabel:`Název společnosti“
- :guilabel:`Adresa“
- :guilabel:`DPH“
- :guilabel:`Daňové identifikační číslo“ (DIČ), které je každému daňovému subjektu přiděleno finančním úřadem.
přírodní nebo právnická osoba (např. „2893081508152“).
- :guilabel:`IČO“ (identifikační číslo osoby, podnikající fyzické osoby)
identifikační číslo ekonomicky aktivních osob.

Poté můžete svou společnost zaregistrovat prostřednictvím Fiskalů kliknutím na záložku :guilabel:`Fiskaly`.
kliknutím na tlačítko „Registrace Fiskaly“.

.. tip::
Pokud nevidíte tlačítko „Registrace Fiskaly“, ujistěte se, že jste svůj soubor *uložili*.
jsou již neupravitelné.

Jakmile je registrace dokončena, objeví se nové pole:

- :guilabel:`ID organizace Fiskaly“ odkazuje na identifikační číslo vaší společnosti na straně Fiskaly.
- Kredence „API klíč Fiskaly“ a „Tajný klíč Fiskaly“ jsou přihlašovací údaje systému.
používá k přístupu ke službám poskytovaným společností Fiskaly.

.. obrázek:germany/fiskaly-registration.png
:alt:Registrační karta fiskálu

.. poznámka::
Pokud dojde k problémům s aktuálními přihlašovacími údaji, je možné požádat o nové přístupové údaje kliknutím
tlačítko „Nový klíč“.

Vytvořit technickou bezpečnostní ochranu a propojit ji s POS
*******************************************************

Pro použití bodu prodeje v Německu nejprve vytvořte :abbr:`TSS (Technical Security System)` přejít
do položky „Prodejní místo“ v nabídce „Nastavení“ a poté vyberte
položku „Prodejní místo“ k úpravě a poté zaškrtnutím políčka „Vytvořit TSS“ pod
:guilabel:`API Fiskal“ sekci.

Jakmile bude vytvoření TSS úspěšné, můžete najít:

- :guilabel:„ID TSS“, což odkazuje na vaši ID TSS na straně Fiskal.
- „ID klienta Fiskaly“, což odkazuje na váš POS na straně Fiskaly.

.. obrázek:germany/fiskaly-tss.png
:alt:Fiskální API

Export do DSFinV-K
~~~~~~~~~~~~~~~

Při každém ukončení sezení PoS jsou detaily objednávek odeslány na :abbr:`DSFinV-K
Služba digitální rozhraní finanční správy pro pokladní systémy) služby Fiskaly.

Pokud dojde k auditu, můžete vyexportovat data zaslaná do DSFinV-K přes tlačítko „Bod
Prodej --> Objednávky --> DSFinV-K Exporty --> Nový.

.. obrázek:germany/pos-orders-menu.png
:alt:Export DSFinV-K

Tyto pole jsou povinná:

- :guilabel:`Čas začátku“: export dat s daty většími nebo rovnými danému datu
- :guilabel:`Datum ukončení“: export dat s datem menším nebo rovným zadanému datu ukončení

Zaškrtněte pole „Prodejní místo“ a zadejte prázdný řetězec, pokud chcete exportovat všechna prodejní místa.
Určete jeden, pokud chcete exportovat data pouze pro tento konkrétní POS.

.. obrázek:germany/dsfinv-k-export.png
:alt:Export do DSFinV-K

Když je export úspěšně spuštěn a zpracováván, pole :guilabel:`Stav` by mělo
Zmínit: „Čeká na schválení“. Klikněte na „Obnovit stav“ a zkontrolujte, jestli je připraveno k použití.
