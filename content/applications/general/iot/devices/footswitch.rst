====================
Připojte pedál.
====================

Při práci v prostředí výroby je pro obsluhu vždy lepší mít obě ruce.
k dispozici kdykoliv. IoT krabička společnosti Odoo umožňuje tento přístup při použití
footswitch.

S nožním spínačem je možné přepínat mezi obrazovkami a provádět
akce s nohou, což lze snadno nakonfigurovat na pracovním stole v
Aplikace pro výrobu.

Připojení
==========

K propojení pedálu s „boxem“ IoT je potřeba připojit oba zařízení prostřednictvím
kabelu. Častěji se však používá kabel :abbr:`USB (Univerzální sériová sběrnice)“.

Pokud je footswitch „podporovaným zařízením“ (https://www.odoo.com/page/iot-hardware/), neexistuje
musíte podniknout další kroky, protože se automaticky detekuje při připojení.

.. obrázek: footswitch/footswitch-dropdown.png
:align:center
:alt:Přepínač nohou rozpoznán na IoT krabičce.

Připojit nožní spínač k pracovnímu centru v aplikaci Odoo Manufacturing
================================================================

Chcete-li připojit pedál k akci, musí být nejprve nakonfigurován na pracovním stole. Přejděte do
:menuselection:`Výrobní aplikace --> Konfigurace --> Stroje“. Zde se přesuňte na požadované
„Práce“ a přidejte zařízení do
Karta „Aktivátory IoT“ v záložce „Zařízení“, pod záložkou „Přidat aktivátor IoT“.
Line. To znamená, že spínač nohou může být propojen s možností v sloupci „Akce“.
příkazu, který se spustí po stisku klávesy. Příkladem je
Aplikace pro výrobu může být tlačítko „Zkontrolovat“ nebo „Označit jako hotové“.
výrobní zakázka.

.. obrázek: footswitch/footswitch-example.png
:align:center
:alt:Nastavení footswitche v databázi Odoo.

.. důležité::
Je třeba poznamenat, že první uvedený spouštěč se vybírá jako první. To znamená, že pořadí je důležité a
Tyto triggery lze libovolně přesouvat. Na obrázku výše je použit pedál.
automaticky přeskakuje část procesu, kterou aktuálně pracujete.

.. poznámka::
Na obrazovce „Pracovní objednávka“ se zobrazuje grafický prvek, který ukazuje, zda je databáze
je správně připojen k pedálu.

.. viz též:
:ref:`workcenter_iot`
