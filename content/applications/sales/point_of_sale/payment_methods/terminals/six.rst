===
SIX
===

Připojení terminálu SIX umožňuje nabídnout svým zákazníkům plynulý platební tok.
usnadnit práci pokladní.

.. varování:
Světová společnost Worldline koupila SIX Payment Services a obě entity využívají systém platební brány Yomani.
terminaly, jejich software se liší. Terminály dodávané společností Worldline jsou proto neslučitelné
s touto integrací.

Konfigurace
=============

Předpoklady
-------------

#Nainstalujte modul POS IoT Six: :doc:`Aktivujte modul POS IoT Six
<../../../obecne/aplikace_moduly> pro zapnutí platebního terminálu.

....... poznámka::
Tento modul nahrazuje modul POS Six.
#. Připojte systém Internetu věcí: :doc:`Raspberry Pi nebo virtuální systém pro Internet věcí (jen pro operační systém Windows).
je nutné k propojení platebního terminálu SIX s Odoo.

... _šest/konfigurovat:

Zvolte způsob platby
----------------------------

#Zapněte platební terminál:ref:`v aplikačních nastaveních <configuration/settings> a
:doc:`vytvořit platební metodu pro terminály SIX <../../payment_methods>.
#. Zadejte typ záznamu jako „Banka“.
#Vyplňte pole „Záporný zůstatek“.
#Vyberte pole „Terminál“ v poli „Propojení“.
#Vyberte pole „Six IoT“ v poli „Propojit s“.
#Klikněte na tlačítko „Sestavení terminálu 6“.

.. obrázek: six/novy-platebni-system.png
:alt: Vytvoření nového způsobu platby pro platební terminál SIX
:skalka: 45 %

V okně režimu

#Klikněte na pole „IoT Box“ a vyberte systém IoT z nabídky.
#Zadejte šestimístný identifikátor terminálu (TID) poskytnutý společností SIX.
#Vyberte položku z nabídky „Terminál“.
#Konečně klikněte na tlačítko „Přidat terminál“.

.. obrázek: šest/terminal-wizard.png
:alt: Konfigurace terminálu pro platby SIX

.. poznámka::
Zajistěte, aby terminál SIX byl připojený k internetu a měl stejnou síť jako systém Internet věcí.

Přiřaďte platební metodu k terminálu
--------------------------------

Jakmile je metoda platby vytvořena, může být vybrána v nastavení POS.

#Přejděte do nastavení „:ref:`POU'“ (<konfigurace/nastavení>).
#Přidejte platební metodu pod pole „Způsoby platby“ v sekci „Platba“.
části.
