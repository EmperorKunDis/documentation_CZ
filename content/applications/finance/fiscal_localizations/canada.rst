======
Kanada
======

.. |KOA| nahradit za: zkratka: `KOA (Kniha o účtech)`
.. |AR| nahradit:::zkratka: AR (Příjmy v hotovosti)
.. |AP| nahradit za: zkratka: „AP (Placení faktur)“

Balíček lokálních nastavení pro Kanadu společnosti Odoo poskytuje přizpůsobené funkce a konfigurace pro kanadské
podniky.

Série videí na téma účetnictví je dostupná prostřednictvím e-learningové platformy společnosti Odoo.
Tyto videa pokrývají témata jako začátek od nuly, nastavení konfigurací, dokončení běžných pracovních postupů a
poskytnou hlubší pohled na některé konkrétní případy použití.

.. viz též:
   - „Návody k Odoo: Účetnictví a fakturace
<https://www.odoo.com/slides/accounting-and-invoicing-19>
   - „Odoo SmartClass: Účetnictví <https://www.odoo.com/slides/smartclass-accounting-121>“

Konfigurace
=============

Níže jsou dostupné moduly v Odoo pro účetní použití v Kanadě.

Instalace modulů
--------------------

:ref:`Instalujte následující moduly, abyste získali všechny funkce kanadského
lokalizace:

.. seznam tabulkový::
:hlavičkové řádky: 1
:šířky: 25 25 50

   * Jméno
     - Technické označení
     - Popis
   * --:guilabel:`Kanada - Účetnictví“
     - l10n_ca
     - Základní modul účetnictví pro kanadskou lokalizaci.
   * – :guilabel:`Kanada – Účetní zprávy“
     - `l10n_ca_reports`
     - Přidává kanadské účetní zprávy.
   * --:layout-checku-kanady
     - „l10n_ca_check_printing“
     - Umožňuje tisk plateb na předtištěný šekový papír. Podporuje tři nejčastější
kontroluje formáty a pracuje s odkazy na kontroly z webu checkdepot.net
<https://checkdepot.net/collections/pocka-na-vyber/odoo>.

       - Zkontrolujte nahoře: Quicken/QuickBooks Standard
<https://checkdepot.net/collections/pockety/odoo+top-check>`_
       - Zkontrolujte střed: Standard Peachtree
<https://checkdepot.net/collections/pockety-na-pc/odoo+stredni-check>`_
       - „Kontrola na dně: Standardní ADP
<https://checkdepot.net/collections/pockety-na-karty/odoo+Dno-Peněženka>`_

.. _l10n_ca/coa:

Klasifikační schéma
=================

Kanadský účetní výkaz (COA)
lokalizace v Odoo má účty rozdělené do sedmi hlavních kategorií s odpovídajícími čísly
hodnota, která předchází každému záznamu v deníku:

- Příjmy: zůstatek peněz (nebo kreditu), který je vůči podniku dlužen za dodané zboží nebo služby
dodané nebo použité, ale ještě nezaplacené zákazníky. Kód časopisu pro AR je
začínající na :guilabel:`1`.
- **Vypořádané závazky**: krátkodobé závazky podniku vůči svým věřitelům nebo dodavatelům.
nebyly ještě zaplaceny. Jako zdroj informací je uveden kód periodika označený (či začínající) zkratkou
:guilabel:`2`.
- **Akciová hodnota**: částka peněz, která by byla vrácena akcionářům společnosti, pokud by se prodaly všechny její akcie.
V případě likvidace byly majetkové hodnoty vypořádány a všechny závazky společnosti byly uhrazeny.
Zajištěnost je označena číslem periodika, které začíná na nebo obsahuje znak :guilabel:`3`.
:guilabel:`9`.
- **aktiva**: položky uvedené na účetní bilanci, které mají ekonomickou hodnotu nebo jsou schopny
generovat v budoucnu peněžní toky, jako je stroj, finanční nástroj nebo
patent. Zásoby jsou označeny číslem periodika, které začíná na znaku :guilabel:`1`.
- **Závazky**: odkazují na finanční dluhy nebo závazky společnosti, které vznikly během jejího trvání.
z obchodních operací. Závazky jsou označeny kódem účetního deníku, který je buďto označen nebo začíná
:guilabel:`2`.
- *Příjem* je synonymem pro *čistý zisk*. Jedná se o zisk společnosti po zaplacení všech výdajů.
všechny relevantní výdaje z prodejního příjmu vynaložené. Náklady jsou označeny kódem účetní knihy

- Náklady: náklady, které společnost vynaloží na dosažení zisku. Náklady jsou
indikované kódem časopisu označeným (nebo začínajícím) znakem „:guilabel:`6`“.

.. tip::
Definované účty jsou součástí Odoa, jako součást kanadského |COA|.
balíček pro místní nastavení. Účty uvedené níže jsou přednastaveny tak, aby prováděly určité operace
v rámci Odoo. Je doporučeno, aby tyto účty nebyly smazány; pokud je však potřeba provést změnu,
přejmenujte účty namísto toho.

...... seznamová tabulka::
:hlavičkové řádky: 1
:sloupky: 1

      * --:guilabel:Typ
        - :guilabel:`Název účtu“
      * :-:guilabel:`Vybavení“
        - |:guilabel:`Suspendovaný účet banky“
| :guilabel:`Významné příjmy“
| :guilabel:`Nedoplatky“
| :guilabel:`Převod likvidity“
| :guilabel:`Ocenění akcií“
|:guilabel:`Stock Interim (Přijato)`
| :guilabel:`Stock Interim (Dodáno)`
|:guilabel:`Náklady na výrobu“
      * -- :guilabel:`Příjem“
        - | :guilabel:`Zisk z devizových operací“
| :guilabel:`Rozdíl v hotovosti“
| :guilabel:`Zisk z cashbacku“
      * --:label:Náklady
        - |:guilabel:`Ztráta z cashbacku“
| :guilabel:`Ztráta z devizových operací“
|:guilabel:`Rozdíl v hotovosti“
      * – :guilabel:Současný roční výnos
        - :guilabel:`Nedotované zisky a ztráty“
      * -- :guilabel:`Příjmový účet“
        - :guilabel:`Příjmy za prodej“
      * :- guilabel:Doplatit
        - :guilabel:`Zálohy“

.. viz též:
   - :doc:`../účetnictví/začínáme/rozvaha“
   - :doc:`../účetnictví/začínáme/tabulka-slovníček-pojmů`

... _l10n_ca/fiskální-pozice:

Fiskální pozice
================

Daňové sazby a daňové položky se v Kanadě liší podle provincie a teritoria. Výchozí fiskální pozice jsou
je vytvořen automaticky při instalaci aplikace **Účetnictví**. Pro správu nebo konfiguraci
další daňové pozice, přejděte na: menu „Účetnictví“ -> „Konfigurace“ -> „Daňová
Pozice“.

Následující daňové pozice jsou k dispozici výchozí:

- :guilabel:`Alberta (AB)`
- :guilabel:`Britská Kolumbie (BC)“
- :guilabel:`Manitoba (MB)“
- :guilabel:`Nový Brunšvik (NB)“
- :guilabel:`Nováfoundland a Labrador (NL)“
- :guilabel:`Nová Skotsko (NS)“
- :guilabel:`Severozápadní teritoria (NT)“
- :guilabel:`Nunavut (NU)“
- :guilabel:`Ontario (ON)“
- :guilabel:`Ostrovy prince Edwarda (PE)“
- :guilabel:`Kanada - Quebec (QC)“
- :guilabel:`Saskatchewan (SK)“
- :guilabel:`Jukon (YT)“
- :guilabel:`Mezinárodní (INTL)`

.. obrázek:canada/l10n-ca-fiscal-positions.png
:alt:Výchozí daňová pozice pro kanadskou lokalizaci v účetnictví Odoo.

.. poznámka::
Když se uvažuje o tom, jaké daně se mají použít, je to provincie, kde k dodání dojde.
Proto je dodání na odpovědnosti dodavatele a bude zahrnuto do účetních výkazů.
lokalita zákazníka.

.. příklad::
   - Dodávka je určena zákazníkovi z jiného kraje.
Záznam o zákazníkovi nastavte na úroveň provincie zákazníka.
   - K nákupu přijíždí zákazník z jiného kraje.
Nikdo by neměl být na zákazníkovi zapsán jako daňový subjekt.
   - Zahraniční dodavatel neúčtuje žádnou daň, ale daně se účtují u celního makléře.
Změňte daňovou pozici na záznamu dodavatele na hodnotu *mezinárodní*.
   - Zahraniční dodavatel platí daň z přidané hodnoty na úrovni provincie.
Nastavte daňovou pozici na faktuře dodavatele na vaši pozici.

.. viz též:
:doc:`../účetnictví/daně/daňové pozice`

.. _l10n_ca/taxes:

Daně
=====

Daňové sazby a co je považováno za zdanitelné se v Kanadě liší podle provincie nebo teritoria. Výchozí *Prodej*
a daň z přidané hodnoty vytváří automaticky aplikace Odoo **Účetnictví** při
nainstalovány. Chcete-li spravovat stávající nebo konfigurovat další daně, přejděte na:
--> Konfigurace --> DPH“.

.. _l10n_ca/taxes-avatax:

AvaTax
------

**Avalara AvaTax** je cloudbasedový software pro výpočet daní a dodržování předpisů, který integruje
Odoo pro několik lokalizací včetně Kanady. Propojení AvaTaxu s Odoo poskytuje reálný čas
a daňové výpočty specifické pro danou oblast při prodeji, nákupu a fakturaci položek v databázi.

.. důležité::
AvaTax je k dispozici pro integraci do databází/firem, které mají pobočky v Kanadě a/nebo
Spojené státy. Podrobnosti naleznete v dokumentaci :ref:`/accounting/avatax/fiscal_country`.
informace.

.. viz též:
Řešení pro integraci a konfiguraci účtu AvaTax naleznete v příslušných článcích dokumentace.
Odoo databáze:

   - :doc:`Integrace AvaTaxu <../účetnictví/daně/avatax>`
   - :doc:`Portál Avalara pro správu daní <../accounting/taxes/avatax/avalara_portal>`
   - :doc:`Vypočítat daně s AvaTax <../accounting/taxes/avatax/avatax_use>`
   - Podpora společnosti Avalara: „O AvaTaxu“
<https://community.avalara.com/support/s/document-item?language=en_US&bundleId=dqa1657870670369_dqa1657870670369&topicId=About_AvaTax.html&_LANG=enus>

...

Zprávy
=======

K dispozici je několik výběrů z reportů, viz například:
Kanadská lokalizace pod položkou „Účetnictví -> Zprávy“ v nabídce:

- :ref:`Výkaz zisku a ztráty <účetnictví/zprávy/výkaz zisku a ztráty>“: „snímek“ finanční situace společnosti
pozice v určitém čase, která obsahuje přehled majetku společnosti.
základní kapitál, závazky a vlastní kapitál.

Zvolte možnost „Výsledovka (CA)“ z nabídky :icon:`fa-book`.
:guilabel:`Zpráva“ filtr.

.... obrázek: canada/l10n-ca-balance-sheet.png
:alt: Výběr výkazu zisku a ztráty pro lokalizaci CA v Odoo.

- :ref:`Zisk a ztráta <účetnictví/zprávy/rozvaha>“: jinak známý jako *P&L výkaz* nebo
*Výkaz zisku a ztráty* poskytuje souhrn příjmů, výdajů a zisků/ztrát společnosti za
určité období.

Ujistěte se, že zvolíte možnost „Zisk a ztráta (CA)“ ze seznamu volby „:menuselection:“.
:guilabel:`Zpráva“ filtr.

.... obrázek:canada/l10n-ca-profit-loss.png
:alt:Výběr zisku a ztráty pro lokální verzi CA v Odoo.

- :guilabel:`Výkaz o peněžních tocích“: ukazuje, kolik hotovosti a ekvivalentů v hotovosti společnost obdržela.
a vynaložené za dané období.
- :ref:`Shrnutí výkonné části<účetnictví/zprávy/výkonná část>“: shrnující zpráva, která pokrývá
významné ukazatele finanční pozice společnosti, jako jsou tržby, zisk a
dluh.
- :ref:`Daňový výkaz <účetnictví/výkazy/daňový výkaz>“: oficiální formulář předkládaný finančnímu úřadu
které vykazují příjmy, výdaje a další relevantní informace o dani. Daňové přiznání umožňuje daňovým poplatníkům
vypočítat daňovou povinnost, naplánovat termíny plateb daně nebo požádat o vrácení přeplatku.
daňového přiznání v Odoo lze provádět měsíčně, každé dva měsíce, čtvrtletně, každé čtyři měsíce.
a pololetně.

.. viz též:
   - :doc:`Účetní výkaznictví <../accounting/reporting>`
   - :doc:`../../základy/vyhledávání`

... _l10n_ca/sleva-za-hotovost:

Sleva v hotovosti
=============

Slevu z ceny lze nastavit v aplikaci „Účetnictví“ pod položkou „Platební podmínky“.
Doba splatnosti lze nastavit s hotovostní slevou a sníženou daní.

.. viz též:
:doc:`../účetnictví/fakturace/hotovostní slevy“

Vyplňování šeků
==============

Kanadská lokalizace umožňuje uživatelům tisknout šeky na úhradu faktur. Ujistěte se, že je zaškrtnuté políčko „Canadian
Modul pro lokalizaci tiskových sestav („l10n_ca_check_printing“) je nainstalován:
<generální/instalace>.

Pro tisk šeků z Odoo přejděte na: „Účetnictví--> Konfigurace-->
Nastavení a najděte sekci „Dodavatelské platby“. Zde zaškrtněte políčko „Šeky“
zaškrtávací políčko, které odhaluje několik polí pro konfiguraci kontroly.

Vyberte z nabídky „Zkontrolovat rozložení“:

- :guilabel:`Tisková kontrola (Horní) - CA“
- :guilabel:`Tisková kontrola (střední) - CA“
- :guilabel:`Tisková kontrola (Dno) - CA“

Dále vyberte, zda chcete nebo nechcete zaškrtnout políčko „Vyžadovat více stránek“.

Volitelně nastavte :guilabel:`Zkontrolujte horní okraj“, :guilabel:`Zkontrolujte levý okraj“ nebo :guilabel:`Zkontrolujte
Pokud je třeba, zadejte pravý okraj.

Zatrhněte políčko „Tisk datumu“ (Guilabel: Print Date Label).

Jakmile jsou všechny konfigurace kontrolních bodů dokončené, uložte nastavení pomocí tlačítka „Uložit“.

.. tip::
Některé formáty šeků mohou vyžadovat předtištěný papír od třetí strany.
„Předtištěné šeky od CheckDepot.net <https://checkdepot.net/collections/odoo-checks>“
doporučeno.

.. viz též:
:doc:`../účetnictví/platby/výplaty“

Přijímat předautorizované inkasa
=============================

Předautorizované inkasa jsou způsobem, jakým mohou obchodníci získávat platby od zákazníků.
autorizuje podnik k čerpání prostředků z jeho účtu na pravidelné bázi.
funkce je často používána pro předplatné, opakující se faktury a další pravidelné platby.

V kanadské lokalizaci Odoo jsou předautorizované platby usnadněny prostřednictvím
:doc:`integrace se službou Stripe <../payment_providers/stripe>“.

.. viz též:
   - :doc:`Nastavení platebních poskytovatelů <../payment_providers>`
   - Dokumentace o předautorizovaných platbách Stripe
<https://stripe.com/docs/payments/acs-debit>`_
