==========================
Připojte měřící nástroj
==========================

.. _iot/zařízení/měřicí nástroj:

S Odoo IoT boxem je možné připojit měřicí nástroje k
Odoo databáze pro použití v aplikaci *Kvalita* na kontrolním bodě kvality nebo při kontrole kvality.
výrobní centrum během výroby.

Seznam podporovaných zařízení najdete zde: „Podporovaná zařízení
<https://www.odoo.com/page/iot-hardware>.

Připojte se k univerzálnímu sériovému rozhraní (USB)
=======================================

Pokud chcete připojit zařízení přes :abbr:`USB (Universal Serial Bus)`, zapojte :abbr:`USB (Universal
Sériový kabel do „IoT“ krabičky a zařízení se objeví v Odoo.
databáze.

.. obrázek: měřicí nástroj/vyber zařízení.png
:align:center
:alt:Měřicí nástroj uznávaný na IoT krabičce.

Připojit přes Bluetooth
======================

Aktivujte funkci Bluetooth na zařízení (podrobnější vysvětlení najdete v návodu k použití zařízení).
a IoT box automaticky připojí zařízení.

.. obrázek: měřicí nástroj/měřicí nástroje.png
:align:center
:alt: Indikátor Bluetooth na měřicím zařízení.


Připojit měřící nástroj k bodu kontroly kvality výrobního procesu
===============================================================================

V aplikaci *Kvalita* lze nastavit zařízení na kontrolní bod kvality. K tomu je potřeba přejít na
:menuselection:`Kvalitní aplikace --> Kvalita kontroly --> Kontrolní body“ a otevřete požadovaný bod
kam má být měřicí nástroj napojený.

Zde upravte kontrolní bod, vyberte pole „Typ“ a klikněte
Vyberte možnost „Měření“ z nabídky. To odhalí pole s názvem „Zařízení“.
kde lze vybrat připojené zařízení.

Dále lze konfigurovat :guilabel:`Norm“ a :guilabel:`Tolerance“. :guilabel:`Uložit“
pokud je třeba.

V tomto bodě je měřicí nástroj propojen s vybraným kontrolním bodem kvality. Hodnota
obvykle se musí měnit ručně a aktualizuje se automaticky při používání nástroje.

.. obrázek: měřicí nástroj/měřicí bod.png
:align:center
:alt: Vstup do měřicího nástroje v databázi Odoo.

.. tip::
Kontrolní body kvality lze také zobrazit přes:menu:IoT App -->
Devices“, pak vyberte zařízení. V záložce „Kontrolní body kvality“ najdete
Může být přidán do zařízení.

.. poznámka::
Na formuláři pro kontrolu kvality lze také uvést typ kontroly.
:guilabel:`Měření“. Přejděte na novou stránku s podrobnostmi o kvalitě kontroly, přes
:menu_selection:`Kvalita aplikace --> Kvalita kontroly --> Kontrola kvality --> Nová“.

.. viz též:
   - :doc:`../../../sklad/mpr/kvalita/kontrola_kvality/kontrolni_body_kvality`
   - :doc:`../../../inventar-a-mrp/kvalita/kvalitni-rizeni/kvalitni-upozorneni`

Připojit měřící nástroj k pracovnímu centru v aplikaci Výroba
=================================================================

Pro spojení měřicího nástroje s akcí je nejprve nutné ho nakonfigurovat na pracovišti.
Přejděte na: „Výroba -> Konfigurace -> Střediska“. Pak
vyberte požadované pracoviště, na kterém bude měřicí nástroj použit.

V sekci „Práce“ přidejte zařízení v záložce „IoT spouštěče“.
V poli „Zařízení“ vyberte možnost „Přidat řádek“. Poté můžete měřicí nástroj
spojené s možností z nabídky „Drobečková navigace“ označenou „Změřit“. Klávesa
Aby se spustila akce.

.. důležité::
Je třeba poznamenat, že první uvedený spouštěč je vybrán jako první. Pořadí hraje roli a tyto
spouštěče lze libovolně přetahovat do požadovaného pořadí.

.. poznámka::
Na obrazovce „Pracovní objednávka“ se zobrazuje grafický prvek, který ukazuje, zda je databáze
je správně připojen k měřicímu zařízení.

.. viz též:
:ref:`workcenter_iot`
