==================================
Import objednávek na nákup a prodej z EDI
==================================

.. |EDI| nahradit za: zkratka: EDI (Elektronická výměna dat)
.. |PO| nahradit za: abbr: PO (objednávka na nákup)
.. |SO| nahradit za: :abbr:`SO (objednávka na prodej)`

Elektronický datový výměnný systém (EDI) umožňuje společnostem používajícím různé softwarové systémy vzájemně si data vyměňovat.
informace v standardizovaném strukturovaném formátu.

V Odoo lze objednávku na nákup (PO) exportovat jako soubor XML a importovat jako objednávka na prodej (SO).
do jiné databáze Odoo, což odstraňuje potřebu manuálního zadávání produktů, množství, cen a
další klíčové informace.

Tento dokument popisuje, jak kupující a prodávající vzájemně sdílejí data.
Odoo databáze. Prodejci mohou také obdržet PDF verzi poptávky.
(RFQ) e-mailem a „nahrajte ho přímo do svého prodejního panelu“.
<nákup/pokročilé/nahrát-rfq>. **Tento způsob je jednodušší**, ale nepoužívá XML-založený výměnný formát
Popisované v dokumentu.

.. poznámka::
Exportované XML soubory se řídí schématem UBL.
<https://docs.peppol.eu/poacc/upgrade-3/syntax/Order/tree/>`_. Při výměně dat mezi dvěma
databáze Odoo, tento schéma zůstane kompatibilní.

Vývoj vlastních řešení pro software, který nepodporuje schéma UBL, však může být
Zavádějí další složitost.

Role a konfigurace
=======================

Pro usnadnění práce s EDI jsou zapojeny dvě společnosti: kupující (firma, která zadává objednávku) a dodavatel (firma, která objednávku vyřizuje).
a dodavatel (firma plnící objednávku). Každá společnost má své specifické role a
konfigurace.

Databáze kupujících
--------------

Databáze kupujících je odpovědná za vytváření a schvalování objednávek. Předpoklady
zahrnuje:

#.(povinné) :ref:`instalace aplikace Purchase <general/install>
#(volitelně) přidat dodavatele (prodejce v tomto procesu) jako uživatele portálu
<../../../obecne/ucastnici/portalu>.

Společnost má databázi prodejců.
---------------

Databáze prodejců je odpovědná za přijímání a zpracovávání objednávek na prodej. Jedinou podmínkou
je instalace aplikace **Prodej** podle návodu v části „Instalace“

Práce s dokumenty
========

Proces kupujícího
---------------

Nejprve se kupující (v databázi) přesune do aplikace Purchase, aby vytvořil
:zkratka:„požadavek na nabídku“.

Zadejte do pole „Dodavatel“ uživatele portálu, který zastupuje prodejce, a potvrďte
:zkratka RFQ (žádost o nabídku). Tím se z ní stane :doc:`objednávka
<../spravovat-smlouvy/rfq>.

Příklad:
|PO| z databáze kupujícího. Výchozí hodnota je „Vendor“, což je uživatelský účet portálu prodejce, Joel.

.. obrázek: edi/po-databáze-výhled.png
:alt: Příklad PO. Prodávajícím je uživatelský účet portálu prodejce, Joel.

Proces prodávajícího
----------------

Jakmile je potvrzeno, zobrazí se na portálu prodejce v panelu nástrojů. Prodávající si stáhne
XML soubor a nahraje ho do své databáze.

Stáhnout soubor
~~~~~~~~~~~~~

Jako prodávající se přihlaste do databáze kupujícího jako uživatel portálu. Na úvodní stránce proklikněte dolů a
Klikněte na tlačítko „Naše objednávky“ . To zobrazí seznam nákupních objednávek, které si kupující
databáze adresovaná uživateli portálu.

Vyberte požadovanou objednávku a klikněte na tlačítko „Připojit se ke svému softwaru“.

V okně s upozorněním zkopírujte poskytnutou adresu URL a vložte ji do nového záložkového panelu pro stažení souboru XML.
soubor.

Příklad:
Joelův pohled na portál PO. První obrázek zobrazuje :guilabel:`Připojte se k
„Software!“ tlačítko a druhé obrázky zobrazuje okno s výzvou k kopírování.
tlačítko.

.. obrázek: edi/po-portál-výhled.png
:alt: Pohled na portál PO s tlačítkem „Připojte své programy!“

.. obrázek: edi/pop-up.png
:alt:Pop-up pro kopírování odkazu.

Příklad:
:stáhnout soubor XML <edi/P00017.xml> pro PO00017

.. nákup/dodání/nahrát RFQ:

Nahrát soubor
~~~~~~~~~~~

Poté se prodejce přihlásí do svého vlastního databáze Odoo a otevře aplikaci „Prodeje“.
:guilabel:`Nahrát“ a vybrat stažený soubor XML. Uživatelé mohou také přetáhnout soubor na
uložit do panelu „Citace“.

Tímto způsobem se automaticky vytvoří objednávka na prodej s kupujícím, který je nastaven jako kupující, a všechny
produktové řady, množství a ceny jsou předvyplněny. Tento proces zajišťuje efektivní a přesné údaje
výměna mezi oběma databázemi.

.. obrázek: edi/so.png
:alt:Prodávající nahrál SO do své databáze.

Nahrál SO do databáze prodejce.

.. viz též:
:doc:`../../../prodej/prodej/vystavit-fakturu/vytvorit-nabidku`

