================
Připojte kameru
================

Kamera může být připojena k :abbr:`IoT (Internet of Things)` boxu s databází Odoo za
pár kroků. Jakmile je kamera připojena k :abbr:`IoT (Internet of Things)` boxu, může být použita v
výrobní proces nebo je spojen s kontrolním bodem kvality / kontrolou kvality.
umožňuje pořízení snímků při dosažení vybraného kontrolního bodu nebo
Při stisknutí konkrétního tlačítka při výrobě.

Připojení
==========

Pro připojení kamery k internetovému boxu stačí propojit oba zařízení pomocí kabelu.
Tento krok se obvykle provádí pomocí nějakého USB (Univerzální sériový bus) kabelu.

Pokud je kamera „podporována <https://www.odoo.com/page/iot-hardware>“, není třeba ji nastavovat
cokoliv, protože bude detekováno ihned po připojení.

.. obrázek: fotoaparát/fotoaparát-výběr.png
:align:center
:alt:Kamera zaznamenaná na IoT boxu.

Připojit kameru ke kontrolnímu bodu výrobního procesu
=============================================================

V nabídce „Kvalita“ lze zařízení nastavit na „Kontrolní bod kvality“.
Pro toto nastavení přejděte na: „Kvalita aplikace > Kvalita kontroly > Kontrolní body“
otevřete požadovaný bod „Kontrolní bod“ spojený s kamerou.

V poli kontrolního bodu vyberte typ kontrolního bodu.
Kliknutím na položku „Vyfotit“ z nabídky. To odhalí pole s názvem
:guilabel:`Zařízení“, kde lze vybrat připojené zařízení. Po stisknutí tlačítka „Uložit“ se změny uloží.
povinné.

.. obrázek:kamera/ovládací-bod-zařízení.png
:align:center
:alt:Nastavení zařízení na kontrolním bodě kvality.

Kamera je nyní použitelná s vybraným kontrolním bodem kvality. Když se zvolený
bude dosaženo během výrobního procesu, databáze vyzve obsluhu k pořízení fotografie.

.. obrázek:camera/sériové číslo-obraz.png
:align:center
:alt:Grafické uživatelské rozhraní zařízení na kontrolním bodě kvality.

.. poznámka::
Kontrolní body kvality lze také zobrazit přes:menu:IoT App -->
Zde vyberte zařízení. V záložce „Kontrolní body kvality“ je možné zvolit
Mohou být přidány pomocí zařízení.

.. tip::
Na kvalitativní kontrolní formuláři lze také zadat typ kontroly, například „Provést
obrázek. Přejděte na: menu-selection: „Kvalita aplikace“ -> „Kontrola kvality“ -> „Nový“
vytvořit novou kvalitu kontroly z stránky „Kontroly kvality“.

.. viz též:
   - :doc:`/aplikace/skladové hospodářství a výroba/kvalita/kontrola kvality/kontrolní body kvality“
   - :doc:`/aplikace/sklad/kvalita/kvalitní řízení/kvalitní upozornění`

Připojte kameru ke stanici v aplikaci výroby
=====================================================

Aby kamera byla propojena s akcí, musí být nejprve nastavena na pracovišti. Přejděte do
Vyberte položku „Výroba“ -> „Konfigurace“ -> „Střediska“. Poté přejděte na požadovanou
:guilabel:„Dílna“ s kamerou, která odhalí podrobnosti konkrétní dílny
formulář. Zde přidejte zařízení do záložky „Akce IoT“ v záložce „Zařízení“.
sloupci kliknutím na tlačítko „Přidat řádek“.

Nyní je možné kamerový zařízení propojit s možností zvolení položky „Akce“ v seznamu
:guilabel:„Uložit obrázek“. Akci lze také spustit pomocí klávesové zkratky.

.. důležité::
První z uvedených spouštěčů je vybrán jako první. Pořadí spouštěčů má vliv a lze je přetahovat
do libovolného pořadí.

.. poznámka::
Na obrazovce „Pracovní objednávka“ se zobrazuje grafický prvek, který ukazuje, zda je databáze
Je správně připojen k fotoaparátu.

.. viz též:
:ref:`workcenter_iot`
