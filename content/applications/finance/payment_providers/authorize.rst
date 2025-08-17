=============
Authorize.Net
=============

`Authorize.Net <https://www.authorize.net>`_ je americká internetová platební služba
poskytovatel, který umožňuje firmám přijímat kreditní karty.

Konfigurace
=============

.. viz též:
   - :ref:`platební metody/přidat novou`

Karta Povolení
---------------

Odoo potřebuje vaše **API Credentials & Keys** k propojení s vaším účtem Authorize.Net,
složení:

- **ID přihlášení API**: Jediný identifikátor účtu, který používá společnost Authorize.Net.
- **Klíč transakce API**
- **Klíč podpisu API**
- **Klíč klienta API**

Pro získání údajů se přihlaste do svého účtu Authorize.Net a v menu vyberte položku „Účet“ – „Nastavení“.
--> Nastavení zabezpečení --> Hodnoty klíčů a přihlašovacích údajů aplikace, vygenerujte si svůj **klíč transakce**
**Základní klíč** a vložte je do příslušných polí v Odoo. Pak klikněte na **Vytvořit zákazníka
Klíč**.

.. důležité::
Pro ověření služby Authorize.Net s účtem pro sandbox změňte stav na „Test“.
Mód. Doporučujeme provést tento postup na testovací databázi Odoo, než na hlavní databázi.

Pokud používáte režim testování s běžným účtem, dojde k následující chybě:
*Heslo obchodníka nebo ID obchodníka je neplatné, nebo účet je neaktivní.*

Karta Konfigurace
-----------------

Zablokovat kartu
~~~~~~~~~~~~~~~~~~~~~~

S Authorize.Net můžete zapnout manuální skenování
<platební_prostředky/ruční_zaplacení>. Pokud je povoleno, jsou peníze rezervovány na
Kartu zákazníka, ale ještě nebyla stržena platba.

.. varování:
Po uplynutí 30 dnů je transakce automaticky zrušena společností Authorize.Net.

.. viz též:
   - :doc:`../platební_prostředky`

.. _autorizace/ACH platby:

Platby ACH (pouze USA)
=======================

Automatizovaný systém pro zpracování platebních příkazů (ACH) je elektronický systém převodu peněz mezi bankami.
účty v USA.

Konfigurace
-------------

Poskytnout zákazníkům možnost platby prostřednictvím ACH, „se přihlaste k odběru služby Authorize.Net eCheck“
<http://www.authorize.net/payments/echeck.html>`. Jakmile je aktivována funkce eCheck,
dříve nakonfigurovaný platební poskytovatel Authorize.Net v Odoo přejděte na:
Konfigurace > Platební metody > Autorizace.NET. Pak klikněte na ikonu kolečka
(:) a vyberte Duplikovat. Změňte název poskytovatele, aby se oba
verze (např. „Authorize.net - Banky“).

Pokud je připravena, změňte stav poskytovatele na „Aktivní“ pro běžný účet nebo
Pro testovací účet v režimu „Sandbox“.

Importujte výpis z účtu Authorize.Net
=================================

..._autorizovat import šablony

Export z Authorize.Net
-------------------------

.. varování: šablona

:stáhnout:Stáhněte si šablonu pro import do Excelu.

- Přihlaste se do systému Authorize.Net.
- Přejděte na:menu:„Účet“ – „Výpisy“ – „Souhrnná vyúčtování eCheck.Net“.
- Definujte oblast vývozu pomocí otevřené a uzavřené smlouvy o vypořádání. Všechny transakce uvnitř
Obě sériové vyúčtování budou exportovány do Odoo.
- Vyberte všechny transakce v požadovaném rozsahu, zkopírujte je a vložte do
:guilabel:`Stáhnout report 1“ listu v :ref:`Šabloně pro import do Excelu
<import-autorizace-vzor>.

.. obrázek: autorizace/autorizace-report1.png
:alt:Vybrat transakce Authorize.Net k importu

.. příklad::

.. obrázek: autorizovat/autorizovat-souhrnné-platby.png
:align:center
:alt:Soubor s platbami z výpisu Authorize.Net

V tomto případě patří první částka (s datem 01.01.2021) do vyrovnání za 31.12.2020.
Protože je to první otevřená smlouva, platí od 31. prosince 2020.

Jakmile jsou data v listu Report 1 Download:

- Přejděte na záložku „Hledání transakcí“ v Authorize.Net.
- V sekci „Datum usmíření“ vyberte předchozí použitou řadu balíčku.
Vyplňte datum usazení v polích „Od“ a „Do“ a klikněte na „Hledat“.
- Po vytvoření seznamu klikněte na tlačítko „Stáhnout do souboru“.
- V okně s náhledem vyberte položku: guilabel:Rozšířená pole se zprávou CAVV/Za oddělovačem stojí tečka.
Zapněte možnost „Zahrnout hlavičky sloupců“ a klikněte na tlačítko „Odeslat“.
- Otevřete soubor s textem, vyberte „Všechny“, zkopírujte si data a vložte je do „Zprávy
2. stáhnout „Import do Excelu“ z :ref:`vzoru importu <autorizace-import-template>“.
- Přechodové linky se automaticky vyplňují a aktualizují v:guilabel:`transit pro zprávu 1`.
:guilabel:`přeprava pro zprávu 2“ listů :ref:`vzoru pro import do Excelu
</import-autorizace-šablona>. Ujistěte se, že jsou všechny položky přítomné a **pokud ne** zkopírujte vzorec
z předchozích vyplněných řádků listu „Přeprava pro hlášení 1“ nebo „2“.
a vložte je do prázdných řádků.

.. důležité::
Aby byl správný závěrkový stav, **neodstraňujte žádnou řádku** v listu Excel.

Import do Odoo
----------------

Pro import dat do Odoo:

- Otevřete šablonu pro import do Excelu: :ref:`<authorize-import-template>`.
- Zkopírujte data z listu „Přeprava pro hlášení 2“ a použijte funkci *vložit speciálně*, abyste vložili
Vložte hodnoty do listu „Import Odoo do CSV“.
- Hledejte buňky s barvou modrou v listu „Import do CSV“. Jsou to záznamy o náhradě
bez čísla referenčního. Jako takové totiž do Česka nemohou být dovezeny,
:menuselection:`Autorizace.net --> Účet --> Výpisy --> Vyrovnání výpisu eCheck.Net“.
- Hledejte položku „Transakce kreditní karty/Zrušení transakce“ a klikněte na ni.
- Zkopírujte popis faktury a vložte jej do buňky pole „Štítek“ v poli „Odoo“.
Importujte do listu CSV a přidejte před popis „Zpětná platba“.
- Pokud je vystaveno více faktur, přidejte řádek do šablony pro import Excelu
pro každou fakturu a vložit popis do příslušného pole.


.. poznámka::
Pro **spojené vrácení peněz/vratky zboží** ve výplatách vytvořte novou řádek v :ref:`importu do Excelu
pro každou fakturu vzor importu autorizace.

.. příklad::

.... obrázek:: autorizace/autorizace-zrušení-účtování-popis.png
:alt: Popis zpětného odběru

- Dále odstraňte položky „Nulová transakce“ a „Zrušená transakce“ a změňte formát
v poli „Částka“ sloupce v listu „Import Odoo do CSV“ na hodnotu „Číslo“.
- Vraťte se na: „eCheck.Net Settlement Statement --> Search for a Transaction“
vyhledat již dříve použitá data pro zpracování plateb.
- Zkontrolujte, zda data ukončení platby na eCheck.Net odpovídají datům plateb nalezeným v
v poli „Datum“ v záložce „Import Odoo do CSV“.
- Pokud neodpovídá, nahraďte datum datem z eCheck.Net a seřaďte sloupec podle *data*.
a ujistěte se, že formát je „DD/MM/YYYY“.
- Zkopírujte data (včetně sloupcových nadpisů) z listu „Import do CSV“ a vložte
je převést do nového souboru Excel a uložit ve formátu CSV.
- Otevřete aplikaci Účetnictví, přejděte do sekce „Konfigurace“ a zaškrtněte
:guilabel:`Autorizace.net“ a klikněte na „Oblíbené -> Nahrát záznamy -> Zatížit
Vyberte soubor .csv a nahrajte jej do Odoo.

.. tip::
Seznam kódů „eCheck.Net return codes <https://support.authorize.net/knowledgebase/Knowledgearticle/?code=000001293>“
