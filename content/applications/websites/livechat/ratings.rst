=======
Hodnocení
=======

.. |smile| nahradit za zelenou: ikonu `fa-smile-o`: guilabel: (smile):
.. nahradit: žlutá: ikonka `fa-meh-o`: guilabel: (neutrální): ikona
.. nahraďte: červená :icon:`fa-frown-o` :guilabel:`(frown)`

Na konci živého chatu mají zákazníci možnost ohodnotit kvalitu
podpoře, kterou od operátora chatu obdrželi. Hodnocení zákazníci zadávají ihned po uzavření
konverzace. To umožňuje operátorům získat okamžitou zpětnou vazbu na jejich výkony.
umožňuje zákazníkům sdílet jakékoli konečné poznámky před opuštěním okna chatu.

Hodnotit živé chaty
============================

Zákazníci ukončí živý chat kliknutím na ikonu „Oi“ (zavřít)
v pravém horním rohu okna chatu. Pak je vyzváni k výběru ikonky,
odráží jejich spokojenost. Ikony znázorňují následující hodnocení:

 - **Spokojený** - |smile|
 - Okay – |meh|
 - Nespokojený – |mračit se|

.. obrázek: hodnocení/hodnocení živého chatu/obličeje.png
:alt: Pohled na okno chatu z pohledu uživatele pro Odoo Live Chat.

.. poznámka::
Když zákazníci ukončí konverzaci, pole označené:guilabel:`Přijmout kopii této konverzace“
V seznamu uvedených pod ikonami hvězdiček jsou e-mailové adresy zákazníků. Zákazníci mohou své e-maily zadat buď před, nebo po vstupu do obchodu.
hodnotit.

Když zákazník vybere „úsměv“, objeví se mu zpráva „Díky“ a
:guilabel:`Zavřít konverzaci“ odkaz.

.. obrázek: hodnocení/díky za chat.png
:alt: Pohled na okno živého chatu zákazníka s poděkováním.

Pokud si zákazník vybere buď „meh“ nebo „frown“, objeví se okno s textem. Zákazníci mohou přidat
komentář do této textové schránky a vysvětlit důvod svého hodnocení. Tento komentář spolu s hodnocením
ikonou, je odeslána živému operátorovi chatu.

.. obrázek: hodnocení/hodnoceni-operátora-okna-chatu.png
:alt:Zobrazení okna chatu z pohledu operátora s vyznačeným hodnocením pro Odoo Live Chat.

Zveřejňujte hodnocení zákazníků
========================

Chcete-li zveřejnit hodnocení kanálu na webových stránkách, nejprve přejděte do záznamu živého chatu kanálu
přejít do aplikace „Živý chat“ a kliknout na ikonu „fa-ellipsis-v“.
:guilabel:`(vertikální elipsa)` ikona na kartě kanbanu pro tým. Pak klikněte
Klikněte na „Nastavení kanálu“ a otevřete formulář s podrobnostmi o kanále. Pak klikněte na „Přejít do
Tlačítko „Chytré rozhraní“. To otevře stránku s názvem „Statistiky živého chatu“.

V horním pravém rohu stránky klikněte na červený posuvník :guilabel:„Nepublikováno“. Posuvník
změna z :guilabel:`Nezařazeno“ na :guilabel:`Zveřejněno“.

.. obrázek: hodnocení/hodnoceni-chatu-nepublikovano.png
:alt: Pohled na zveřejněné hodnocení na portálu pro živý chat Odoo.

.. poznámka::
Záznamy zákazníků, které byly k hodnocení přiloženy, nejsou zveřejněny na webu; jsou uchovány
interní. Statistická přehled o výkonnosti operátorů pro kanál se objevuje na
webové stránky.

Přidat stránku s hodnocením na web
------------------------

Jakmile je stránka s hodnocením zveřejněna, musí být ručně přidána na web. Pro tento úkon postupujte takto:
hlavnímu přehledu Odoo a otevřete aplikaci **Webové stránky**.
Webové stránky --> Stránky“, pak klikněte na „Nový“.

Otevře okno „Nový list“. Do pole „Název stránky“ zadejte
„livechat“. Tento údaj slouží jako URL pro zveřejněnou stránku.

.. důležité:
URL musí být pojmenováno jako „livechat“, aby databáze rozpoznala a propojila hodnocení
stránka. Po zveřejnění stránky lze později změnit název stránky pod
:guilabel:`Editor menu“.

Klikněte na tlačítko „Vytvořit“ a otevře se nová stránka. Zobrazí se editor webových stránek
v pravém sloupci.

Stránka uvádí názvy kanálů chatu, jejichž hodnocení stránek
publikovány. Uživatelé mohou kliknout na ikonu v levém sloupci kanálu a přejít na
stránka s hodnocením pro příslušný kanál.

.. obrázek: hodnocení/publikovaný-ikonka-chatu.png
:alt:Výhled na webovou stránku s hodnocením živého chatu, který zdůrazňuje ikonu kanálu.

..tip:
Ikona zobrazená na této stránce je konfigurována v nastavení kanálu chatu.
aktualizovat tuto obrazovku, přejít do aplikace „Živý chat“ a kliknout na
:icon:`fa-ellipsis-v` :guilabel:`(vertikální elipsa)` ikona na kartě Kanban pro tým.
Poté klikněte na tlačítko „Nastavení kanálu“ a otevřete formulář s podrobnostmi o kanálu.
:ikonka: „fa-pencil“ :guilabel:„(pencil)“ ikona v obrázkovém boxu pro nahrání obrázku.

Udělejte si na této stránce libovolné změny nebo doplňky, pak klikněte na tlačítko „Uložit“ v pravém horním rohu
editor webové stránky. Panel editora webových stránek se zavře a webová stránka zůstane na obrazovce.

Pro zveřejnění stránky „Živý chat“ se vraťte na seznam stránek kliknutím na
Vyberte v menu položku „Webová stránka“ → „Obsah“ → „Stránky“. Zaškrtněte políčko vedle „Live chat“.
seznam stránek pro výběr stránky a zvýraznění řádku. Pak klikněte na zaškrtávací políčko pod sloupcem
Označeno: guilabel:Je publikováno. Políčko je vyznačeno bílou barvou. Po kliknutí
zaškrtávací políčko znovu, aby se aktivoval prvek „Je zveřejněno“. Web je nyní publikován.

.. obrázek: hodnocení/živý chat je zveřejněn.png
:alt:Výhled na seznam stránek webu s vyznačeným políčkem „je publikován“.

Jakmile je stránka přidána na web, hodnocení jsou nastavena tak, aby byla zveřejněna výchozí volba.
Individuální hodnocení lze ručně vybrat tak, aby bylo skryto před veřejností. Hodnocení stále
zahrnuty do interních zpráv a stále jsou k dispozici pro vnitřní týmy. Veřejná webová stránka
Návštěvníci a uživatelé portálu k nim nemají přístup.

Podrobnější informace naleznete v části „Skrytí hodnocení uživatelů“ na odkazu:

Zpráva o hodnocení zákazníků
=======================

Zpráva „Hodnocení zákazníků“ („Živý chat –> Zprávy –> Hodnocení zákazníků“)
zobrazuje přehled hodnocení z živých chatu a jakékoliv další
komentáře, které byly k hodnocení přiloženy.

.. obrázek: hodnocení/živé chaty - hodnocení reportu.png
:alt: Pohled na hodnocení zákazníků v chatu Odoo Live.

Výsledky se zobrazují v kanbanovém pohledu s každým hodnocením reprezentovaným jinou kartou.
Další pohled na věc získáte kliknutím na jedno ze symbolů v pravém horním rohu obrazovky.
v zobrazení seznamu, sloupcovém zobrazení a grafickém zobrazení.

Kliknutím na jednotlivé hodnocení se zobrazí další podrobnosti o konverzaci a hodnocení.

.. _livechat/overview/hide-ratings:

Skrýt jednotlivé hodnocení
-----------------------

Hodnocení je nastaveno k zobrazení výchozím způsobem. Nicméně jednotlivá hodnocení lze ručně vybrat
skrýt před veřejností. Hodnocení je stále součástí interních zpráv a lze jej nadále sledovat
Vnitřními týmy. Veřejnost a uživatelé portálu však nemají přístup.

Chcete-li skrýt hodnocení, přejděte na: „Živé chaty -> Hlášení -> Zákaznické hodnocení“. Klikněte na
Kartička kanbanu pro skrytí hodnocení. Na stránce s podrobnostmi o jednotlivém hodnocení zaškrtněte políčko
označené štítkem:guilabel:`Viditelné pouze v rámci organizace`.

.. obrázek: hodnocení/hodnoceni-chatu-viditelne-pro-internetove-pripojeni.png
:alt: Detailní stránka s hodnocením jednotlivce, kde je vidět zaškrtnuté vnitřní nastavení.

.. viz též:
   - :/aplikace/weby/livechat
   - :doc:`odpovědi“
   - :/aplikace/weby/webu
