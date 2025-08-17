=====
Ponto
=====

Služba **Ponto** umožňuje společnostem a profesionálům sjednotit své účty na jednom místě.
místě a přímo všechny jejich transakce v jedné aplikaci. Jde o třetí stranu, která je
neustále rozšiřovat počet bankovních institucí, které lze synchronizovat s Odoo.

Systém **Odoo** může být napojen přímo na váš účet v bance, takže všechny výpisy budou automaticky importovány.
do vaší databáze.

Ponto je placený třetí stranou, který může zajistit synchronizaci mezi vašimi účty.
a Odoo.

.. viz též:
   - :doc:`/bankovní synchronizace``
   - :doc:`../transakce`

Konfigurace
=============

Připojte své bankovní účty k Ponto
----------------------------------

#Navštivte webové stránky Ponto (https://myponto.com) <https://myponto.com>.
#Vytvořte si účet, pokud ho ještě nemáte.
#Jakmile se přihlásíte, vytvořte si organizaci.

.. obrázek:: ponto/ponto-organizace.png
:alt: Vyplňte formulář pro přidání organizace do Ponto.

#Přejděte na „Účty“ – „Živé“ a klikněte na „Přidat účet“. Možná budete muset
Přidejte své údaje o fakturaci jako první.
#Zvolte svou zemi, banku a souhlasíte s Ponto. Pak následujte kroky
na obrazovce, aby váš účet v bance propojil s vaším účtem u Ponto.

.... obrázek: ponto/ponto-add-account.png
:alt:Přidejte si do účtu Ponto bankovní účty.

#Přidejte všechny bankovní účty, které chcete synchronizovat s databází Odoo a přejděte k dalšímu kroku.

Připojte svůj účet Ponto k databázi Odoo
-----------------------------------------------

#Přejděte na: „Účetnictví“ -> „Konfigurace“ -> „Přidat bankovní účet“.
#Hledejte svou instituci a vyberte ji, abyste si mohli ověřit, že třetí strana je
Ponto.
#Klikněte na tlačítko „Připojit“ a postupujte podle pokynů.
#Vyberte všechny účty, které chcete přistupovat a synchronizovat v Odoo, i ty z jiných zdrojů.
jiných bankovních institucí.

.. obrázek:: ponto/ponto-select-accounts.png
:alt: Vyberte účty, které chcete synchronizovat s Odoo.

#Dokončit proud.

.. poznámka::
Musíte autorizovat všechny účty, které chcete přistupovat v Odoo, ale Odoo bude filtrovat
účty založené na instituci, kterou jste si vybrali v druhém kroku.

Aktualizujte své přihlašovací údaje pro synchronizaci
---------------------------------------

Aby jste aktualizovali své Ponto přihlašovací údaje nebo změnili nastavení synchronizace, aktivujte
Vývojářský režim (viz developer mode), přejděte do sekce „Účetnictví“ – „Konfigurace“
Online synchronizace“ a vyberte instituci, ze které chcete stáhnout druhou
Klikněte na tlačítko „Získat účty“.

.. poznámka::
Dokud probíhá aktualizace, vyberte všechny účty, které chcete synchronizovat, i ty, které pocházejí z
jiných bankovních institucí.

Vygenerovat nové účty
------------------

Přidat nové online účty do vaší sítě, aktivujte režim vývojáře
Přejděte do sekce „Účetnictví“ -> „Konfigurace“ -> „Online synchronizace“, vyberte
instituci, ze které chcete ostatní účty získat. Klikněte na tlačítko „Získat účty“
začít proudit.

.. poznámka::
Nezapomeňte na autorizaci stávajících účtů (pro všechny instituce, které máte).
synchronizovaný s Ponto).

Často kladené otázky
===

Po mé synchronizaci se účet nezobrazí
--------------------------------------------

Zvolili jste instituci ze seznamu a neautorizovali žádné účty z této instituce.

Mám chybu, že vypršela platnost mé autorizace.
-------------------------------------------------------

Každých 6 měsíců (180 dní) musíte znovu autorizovat připojení mezi vaším bankovním účtem
a Ponto. To musíte udělat na webu „Ponto“ <https://myponto.com>. Pokud ne
v tom případě se synchronizace pro tyto účty zastaví.

Mám nějaké chyby s mým betou.
-------------------------------------------

Ponto poskytuje instituce v beta verzi, tyto instituce nejsou přímo podporovány Odoem
a doporučujeme vám kontaktovat přímo společnost Ponto.

.. důležité::
Pro Ponto je výhodné používat instituci v betě, protože jim umožňuje mít skutečný
zpětná vazba na spojení s institucí.
