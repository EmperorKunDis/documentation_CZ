====================
Čas na práci
====================

.. |MO| nahradit za: zkratka: `MO (manufacturing order)`

V Odoo se používají *centra práce*, kde jsou prováděny výrobní operace na konkrétních místech.
Pokud ale nějaký pracoviště nelze použít, začnou se hromadit práce na pracovištích.
do centra, dokud nebude opět v provozu.

Proto je nutné v Odoo deaktivovat pracovní centrum, aby se nové objednávky
předány do pracovišť s alternativními úkoly, která jsou v provozu. Pomocí aplikace **Čas volna** společnosti Odoo je
je možné zařadit pracoviště do režimu nedostupnosti na určité období. To zajistí
Výrobní operace mohou pokračovat, dokud není pracovní centrum opět k dispozici.

Konfigurace
=============

Předtím, než bude pracovní centrum označeno jako nedostupné, musí být platforma Odoo správně
Nastavit. Nejprve je nutné zapnout režim vývojáře:ref:`<developer-mode>`, což umožňuje
Tlačítko „Čas volna“ se objeví na stránce „Práce“ každého pracoviště.

Poté nainstalujte aplikaci Time Off. Tato aplikace se používá k řízení dovolených pro všechny zdroje
v rámci Odoo, včetně zaměstnanců a pracovišť.

Chcete-li tak učinit, přejděte na aplikaci „Aplikace“, pak vyhledejte Time Off v poli pro vyhledávání.
Karta pro aplikaci Time Off by měla být jedinou, která se na stránce zobrazí. Klikněte na
Tlačítko „Instalovat“ na kartě a aplikaci nainstalujete.

Posledním krokem je správné nastavení pracovišť. Pro tento proces je nutné mít
nejméně dvou pracovišť: jedno z nich je nedostupné, druhé přijímá objednávky
Druhý pracovní středisko nelze přijmout. Pokud není konfigurováno druhé pracovní středisko, nemůže Odoo směrovat objednávky práce
od nepřítomného pracoviště a hromadí se v jeho frontě.

Pro vytvoření pracovního centra přejděte na: „Výroba“ -> „Konfigurace“ -> „Práce“.
Centra --> Nové“.

.. viz též:
Pro plný návod k vytvoření pracovního centra se podívejte na dokumentaci na :doc:`pracovních centrech
<../pokročilé_konfigurace/používání_centra_práce>.

Ujistěte se, že oba pracoviště mají stejné vybavení uvedené pod záložkou „Vybavení“.
zajišťuje, že operace prováděné na jednom pracovišti mohou být také prováděny na druhém.

Vyberte druhý pracovní středisko z nabídky
:guilabel:`Alternativní pracoviště“ v rozevíracím seznamu. Nyní ví, že má poslat objednávky práce na
druhý pracovní středisko, pokud je první nedostupný z jakéhokoliv důvodu.

.. obrázek:: work_center_time_off/alternativni-pracovni-centrum-vyber.png
:align:center
:alt: Forma pracoviště s alternativním pracovištěm.

Přidejte si volno na pracovišti
==============================

Po dokončení konfigurace je možné přidělit volno pracovišti. Začněte tím, že se v aplikaci přesunete na
:menuselection:`Výrobní aplikace --> Konfigurace --> Střediska“, a poté vyberte poškozená střediska.
centrum práce. Klikněte na tlačítko „Pokračovat“ v pravém horním rohu
z rozevírací nabídky „Směny“, aby se otevřela stránka pracovních směn pro dané středisko.

.. obrázek:work_center_time_off/working-hours-button.png
:align:center
:alt:Tlačítko „Externí odkaz“ na kartě pracovní doby.

Stránka pracovní doby zobrazuje standardní pracovní hodiny pro pracoviště. V režimu vývojáře
Aktivováním se na horní části stránky objeví tlačítko „Čas volna“ s ikonou letadla.
Klikněte na něj, abyste otevřeli stránku „Čas volna“.

Na této stránce klikněte na tlačítko „Nový“ pro konfiguraci nového záznamu o dovolené. V okně s nastavením dovolené poznámku
Důvod uzavření pracoviště (například poškozené vybavení, údržba atd.)
vyberte pracovní centrum, které je postiženo, jako zdroj, a zvolte datum startu.
:guilabel:`Datum ukončení“ a zadat datum, kdy bude pracoviště nefunkční.

.. obrázek:work_center_time_off/time-off-form.png
:align:center
:alt:Formulář „Čas na odpočinek“.

Plánování alternativního pracoviště
================================

Jakmile je pracoviště ve svém stanoveném časovém rozmezí, objednávky zaslané do něj mohou být
automaticky přesměrován do alternativního pracoviště pomocí tlačítka „Plán“.

Začněte vytvořením nové výrobní objednávky (VO), přejděte na: menu selection: Manufacturing app
--> Výroba --> Výrobní objednávky --> Nová“. Na formuláři |MO| zadejte: „Produkt“
která používá nevyužitý pracovní stůl pro jednu ze svých operací. Klikněte na tlačítko „Potvrdit“
potvrdit |MO|.

Na potvrzené objednávce vyberte záložku „Pracovní příkazy“. Výchozí stav nevyřízených pracovních příkazů
centrum je uvedeno v sloupci „Dílna“. Je zde také tlačítko „Plán“
v horním levém rohu stránky.

Klikněte na „Plán“ a zobrazí se pracovní centrum uvedené v sloupci „Pracovní centrum“.
:guilabel:„Pracovní příkazy“ se automaticky změní na alternativní pracoviště.

.. obrázek::work_center_time_off/před-plánováním.png
:align:center
:alt:Před kliknutím na „Plán“ je objednávka práce naplánována v „Hlavní montážní lince“.

Před kliknutím na „Plán“ je pracovní příkaz naplánován v „Hlavním sestavovacím pásu“.

.. obrázek::work_center_time_off/po-plánování.png
:align:center
:alt:Po kliknutí na „Plán“ je objednávka přesunuta do „Alternativní montážní linky“.

Po kliknutí na tlačítko „Plán“ je pracovní příkaz přesunut do :guilabel:`Alternativní montáže
Line.

Jakmile skončí doba volna pro nefunkční pracovní centrum, Odoo uznává, že
je opět k dispozici. V tomto bodě stisknutí tlačítka „Plán“ nevyvolává přesměrování pracovních příkazů na
alternativní pracovní centrum, pokud je první plně obsazený.
