==========
Používání Avataxu
==========

AvaTax je daňová kalkulačka, která lze integrovat s Odoo ve Spojených státech.
Kanada. Jakmile je dokončené nastavení integrace (viz dokumentace o instalaci), výpočet daně je jednoduchý a
automatické.

.. účetnictví / avatax / daňový výpočet:

Daňové výpočty
===============

Automaticky vypočítávat daně z Odoo nabídek a faktur s AvaTaxem tím, že potvrdíte
dokumenty v průběhu prodeje. Alternativně lze daně vypočítat ručně kliknutím na
tlačítko „Vypočítat daně“ a tyto dokumenty jsou ve fázi návrhu.

.. tip::
Kliknutím na tlačítko „Vypočítat daně“ se daň zboží znovu vypočítá, pokud jsou upravené některé řádky produktů.
na faktuře.

.. obrázek: avatax_use/calculate-avatax.png
:align:center
:alt:Prodejní faktura s vyznačeným tlačítkem potvrdit a počítat daně.

Výpočet daně je spuštěn v následujících případech:
Automatické spouštěče (<avatax/automatic-triggers>), manuální spouštěče (<avatax/manual-triggers>) a další okolnosti.

..._avatax/automatické-spouštěče:

Automatické spouštěče
------------------

- Když obchodní zástupce zašle nabídku emailem pomocí tlačítka „Odeslat emailem“ (připomenutí).
- Když zákazník zobrazí nabídku na portálu.
- Když je cenová nabídka potvrzena a stává se objednávkou na prodej.
- Když zákazník zobrazí fakturu na portálu.
- Při ověřování návrhu faktury.
- Když zákazník zobrazí předplatné v portálu.
- Při vystavení faktury za předplatné.
- Když se zákazník dostane na poslední obrazovku elektronického obchodu.

.. _avatax/ruční spouštění:

Manuální spoušť
---------------

- tlačítko „Vypočítat daně“ na konci citace.
- :guilabel:`Vypočítat daně“ tlačítko v horní části faktury.

Každou z těchto tlačítek můžete použít k ručnímu znovu vypočítání prodejní daně.

.. tip::
Využijte pole „Kód partnera Avalara“ dostupné v záznamu zákazníka, cenovém odhadu
a faktury k přesunu dat do Odoo a AvaTax. Tento prvek je umístěn pod
:menuselection:`Další informace“ v záložce objednávky nebo cenové nabídky v sekci „Prodej“.

V záznamu zákazníka přejděte do aplikace Kontakty a vyberte kontakt. Pak otevřete
:guilabel:`Prodej a nákup“ kartě a „Kód partnera Avalara“ pod
:guilabel:`Prodej“ sekce.

.. důležité::
Fiskální pozice Automatic Tax Mapping (AvaTax) je také aplikována na všechny systémy Odoo.
dokumenty, jako jsou například předplatné.

.. viz též:
   - :doc:`/fiskální_pozice“

Synchronizace s Avataxem
======================

Synchronizace probíhá s Avataxem při vytváření faktury v Odoo. To znamená, že daň z prodeje
je zaznamenána u společnosti Avalara (vývojář softwaru AvaTax).

Pro toto vyberte v menu: „Prodejní aplikace“ – „Objednávky“ – „Dodací listy“. Vyberte dodací list
seznamu.

Po potvrzení cenové nabídky a ověření dodání klikněte na tlačítko „Vytvořit fakturu“. Zadejte
zda je to faktura, záloha nebo
:guilabel:`Záloha (pevná částka).“

Poté klikněte na tlačítko „Vytvořit a zobrazit fakturu“. Zaznamenané daně lze vidět v
Kartě „Články faktury“. Podle druhu daně se liší
umístění adresy pro doručení.

.. obrázek: avatax_use/journal-items.png
:align:center
:alt:Zvýrazněné položky faktury v Odoo.

Nakonec stiskněte tlačítko „Potvrdit“ a dokončete fakturaci a synchronizaci s
Portál AvaTax.

.. varování:
Faktura nelze vrátit do stavu „Návrh“ (tj. zrušit), protože by se tím narušila synchronizace s
AvaTax Portál. Klikněte na „Přidat fakturu“ a zadejte: „Synchronizovat s AvaTax Portálem“.
Podívejte se na tuto dokumentaci: :doc:`/účetnictví/fakturace zákazníků/kreditní poznámky.

Sleva za pevnou cenu
=====================

Přidejte pevnou cenu k hodnotnému zákazníkovi, klepnutím na tlačítko „Přidat řádek“.
faktura zákazníka. Přidejte slevu na produkt a nastavte hodnotu :guilabel:`Cena` buď na kladnou nebo
záporná hodnota. K přepočtu daní klikněte na tlačítko „Vypočítat daň“.

.. tip::
Daňové výpočty lze provádět i na záporných podkladech a kreditních dokladech.

Těžba dřeva
=======

Je možné zaznamenávat akce společnosti Avalara/AvaTax do systému Odoo pro další analýzu nebo ověření.
funkce. Prohlížení je přístupné prostřednictvím nastavení AvaTax.

Chcete-li začít sledovat akce *AvaTax*, nejprve přejděte do aplikace „Účetnictví -->
Konfigurace --> Nastavení.

Pak v sekci „Daně“ pod položkou „Nastavení AvaTaxu“ klikněte
:guilabel:`Zahájení záznamu po dobu 30 minut“.

Při spuštění procesu záznamů se Odoo zaznamená všechny akce Avalara/AvaTax v databázi.

Pro zobrazení protokolu klikněte na „Zobrazit protokol“ vedle „Spustit záznam po dobu 30
minuty. Seznam obsahuje podrobné informace o všech akcích společnosti Avalara/AvaTax*. Tento seznam je možno třídit dle
dalších sloupcích:

- :guilabel:`Vytvořeno“: časová značka výpočtu *AvaTax*.
- :guilabel:`Vytvořeno uživatelem“: číslo uživatele v databázi.
- :guilabel:`Název databáze“: název databáze.
- Typ: do pole lze zadat dvě hodnoty, buď :guilabel:`Server`, nebo
:guilabel:`Klient“.
- :guilabel:`Název služby*: Název služby Avalara. V tomto případě bude *AvaTax*.
- :guilabel:`Úroveň“: výchozí hodnota je „INFO“.
- :guilabel:`Cesta“: ukazuje cestu, kterou bylo možné provést výpočet.
- :guilabel:`Řádek“: ukazuje řádek, na kterém je prováděna kalkulace.
- :guilabel:`Funkce“: ukazuje výpočet na řádku.

.. obrázek: avatax_use/logging.png
:align:center
:alt:Stránka záznamů společnosti Avalara s vyznačeným prvním řádkem seznamu.

Klikněte do logového řádku a zobrazí se další pole s názvem „Zpráva“.

Toto pole obsahuje čistou transkripci transakce, která zahrnuje vytvoření (nebo
upravení faktury na prodej pomocí rozhraní API Avalara *AvaTax*.

Transakce zahrnuje podrobnosti, jako jsou adresy pro zasílání od a do, položky v seznamu popisující
produkty nebo služby, daňové kódy, výši daně a další podstatné informace.

Ve štítku „Zpráva“ jsou uvedeny daně vypočtené pro různé jurisdikce a potvrzují
vytvoření nebo upravení transakce.

.. tip::
Vlastní pole lze vytvořit pomocí nástroje Studio. Klikněte na ikonu :icon:`fa-ellipsis-v
:guilabel:`(elipsa)` v pravém horním rohu. Pak klikněte na :icon:`fa-plus`.
:guilabel:`Přidat vlastní pole“. Tato akce otevře aplikaci Odoo *Studio*.

.. důležité::
Odoo Studio vyžaduje individuální cenovou nabídku. Kontaktujte manažera pro zákaznický servis v databázi
pro více informací o přechodu na jiný plán. Nebo zjistit, zda je v databázi Odoo Studio.
aktuální ceník. Podívejte se na tuto dokumentaci: :doc:`/studio`.

.. viz též:
   - :doc:`../avatax`
   - :doc:`avalara_portal`
   - Daňová souladnost v USA: Video Avatax elearning

   - :doc:`/fiskální_pozice“

