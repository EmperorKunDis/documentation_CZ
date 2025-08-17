=================
PDF kalkulátor cen
=================

Funkce *PDF Quote Builder* v modulu Odoo Sales umožňuje odeslat zákazníkům plně
přizpůsobený PDF soubor pro nabídky s informacemi o společnosti a produktech, obsahující různé informace.
designové prvky namísto pouhého zobrazení ceny a celkové částky.

Nástroj PDF nabídky sloučí hlavičku stránky, popis produktu, cenu a patičku.
Vytvořit podrobnou nabídku. Může také vložit dynamické texty nebo poznámky do PDF, aby byla nabídka osobnější
nabídka pro zákazníky.

Mít na míru upravený PDF v ceně nabídky poskytuje vyšší závěr nákupního zážitku.
zákazníci a dodává společnosti úroveň profesionality.

.. viz též:
„Rychlé tipy Odoo – Vytvoření PDF nabídky [video]“

.. poznámka::
Doporučuje se upravovat PDF formuláře pomocí softwaru Adobe. Formulářové pole v hlavičce a patě
Pro získání dynamických hodnot v Odoo jsou potřeba šablony ve formátu PDF.

Konfigurace
=============

Pokud chcete přidat vlastní PDF soubory pro nabídky, funkce „Stavěč PDF nabídek“ *musí být*
konfigurované.

Pro toto nastavení přejděte na: „Aplikace pro prodej --> Konfigurace --> Nastavení“. Pak
Stránka „Nastavení“, přejděte do sekce „Účty“ a najděte
:guilabel:`Stavěč cen ve formátu PDF“

Přidat PDF jako záhlaví/zápatí
========================

V Odoo Sales je možné přidat vlastní PDF, které lze použít jako hlavičku nebo patu.
Když je v nabídce zapnutý PDF tiskový formulář, můžete poté vybrat všechny hlavičky a
patičky, které chcete použít, pak se tyto PDF také vloží do finálního PDF.

Chcete-li přidat vlastní PDF jako hlavičku nebo patu, začněte tím, že se přesunete do aplikace „Prodej“ a pak klikněte na:
Konfigurace --> Hlavičky a patičky. Z této stránky buď klikněte na tlačítko „Nový“ nebo
:label:Nahrát soubor.

Kliknutím na tlačítko „Nahrát“ se okamžitě zobrazí možnost nahrání požadovaného dokumentu. Pak
Dokument lze dále upravit na kartě dokumentu nebo po kliknutí na
Ikona „vertikální elipsa“ v pravém horním rohu dokumentu
kartu a poté klikněte na „Upravit“.

Kliknutím na tlačítko „Nový“ se zobrazí prázdná dokumentace, do které lze nahrát požadovaný PDF.
pomocí tlačítka „Nahrát soubor“ na formuláři umístěném v části „Obsah souboru“.
pole.

Zde lze upravit různé informace a konfigurace související s nahráváním dokumentu.

První pole dokumentu je pro jeho název a je
šedé (neklikatelné) až do okamžiku nahrání dokumentu. Jakmile je soubor PDF nahraný,
V poli „Jméno“ je automaticky vyplněn název souboru ve formátu PDF a lze ho upravit.

Poté klikněte na pole „Dokumentový typ“ a z rozevírací nabídky vyberte buď:
:guilabel:Hlavička, nebo :guilabel:Patička, abyste určili, zda by byly tyto soubory vybrány k tomu
na začátek nebo na konec citace.

Pod tímto, v sekci „Šablony citací“, lze tento PDF omezit na citaci.
šablony pouze.

.. poznámka::
Alternativně můžete také navigovat do: „Prodejní aplikace“ > Konfigurace“.
Vzorce citací“, vyberte vzorec a přímo „Přidat“ nebo „Nahrát“ PDF.
do něj v záložce Quote Builder.

Poslední možností je vedle pole obsahu souboru pole „Souborový obsah“
:guilabel:`Nastavit dynamické pole“.

Dynamický text v PDF
====================

Při vytváření PDF nabídek s dynamickým obsahem použijte pro Odoo *textové pole*
informace související s citací z databáze Odoo, jako jsou například názvy, ceny atd.

Dynamické hodnoty textu jsou součástí formulářů (vstupy pro text), které lze přidat do PDF souboru.
automaticky doplňuje tyto hodnoty informacemi o citaci.

Dynamické hodnoty textu
-------------------

Níže jsou uvedeny běžné dynamické hodnoty textu, které se používají v již připravených PDF dokumentech a jsou přiřazené k odpovídajícímu
pole a co znamenají.

Pro hlavičku a patu PDF:

- :guilabel:`název`:Referenční číslo objednávky
- :guilabel:`partner_id__name`: Jméno zákazníka
- :guilabel:`user_id__name`: Jméno prodejce
- :guilabel:`nezdaněná částka“: Nezdaněná částka
- :guilabel:`celkem`: Celková částka
- :guilabel:`datum doručení`: Datum doručení
- :guilabel:`platnost_datum`: Datum vypršení platnosti
- :guilabel:`client_order_ref`: Referenční číslo zákazníka


Pro produktový PDF:

- :guilabel:`popis`: Popis produktu
- :guilabel:`množství`: Množství
- :guilabel:`uom`: Jednotka měření
- :guilabel:`cena_jednotka`: Cena za jednotku
- :guilabel:`sleva`: Sleva
- :guilabel:`product_sale_price`: Cena produktu
- :guilabel:`dane“: Dane pojmenovana spojením závorky („“)
- :guilabel:`dph_bez_dph`: DPH bez DPH
- :guilabel:`dph_cena_s_dp` DPH v ceně

Po nahrání PDF pak můžete:guilabel:Konfigurovat dynamická pole. To vám umožní přiřadit
jakýkoliv název pole nalezený ve vašem PDF do pole, které chcete zobrazit, zadáním jakéhokoliv existujícího cesty.
Hlavičky a patky začínají od aktuálního modelu „sale_order“, zatímco produktový dokument
Sleduje jejich cestu od řádku prodejní objednávky.
Zanechání cesty prázdné vám umožní doplnit poznámku přímo z konkrétního citátu.
Nebo je vyžadováno.

Příklad:
Při sestavování PDF je nejlepší postup používat běžné dynamické hodnoty textu (:guilabel:"název" a
:guilabel:`partner_id_name“). Když jsou nahrány do databáze, Odoo automaticky vyplní tyto pole
s informacemi z jejich oboru.

V tomto případě by Odoo automaticky vyplnilo pole „Referenční číslo objednávky“ v poli „Název“ dynamického pole.
textové pole a jméno zákazníka v poli :guilabel:`partner_id_name`.

...... obrázek:: pdf_quote_builder/pdf-quote-builder-sample.png
:synchronizace: střed
:alt: Citaci ve formátu PDF vytváříme pomocí běžných dynamických míst.

Jakmile jsou soubory PDF dokončeny, uložte je na pevný disk počítače a pokračujte v nahrávání.
jejich přes:menuselection:`Prodejní aplikace --> Konfigurace --> Hlavičky a patičky“.

Příklad:
Při nahrávání PDF s polem :guilabel:`fakturační partner - země“, které je
informace dostupné v objednávce prodeje, konfigurujte cestu :guilabel:`path`.
:guilabel:`Jméno pole formuláře“ na:
   - :guilabel:„partner_faktura_id.země_id.název“ pro hlavičku nebo zápatí
   - :guilabel:„faktura_partnera_země_název“ pro fakturu produktu vyplní formulář
s názvem země partnera na faktuře, když je PDF vytvářeno.

Příklad:
Při nahrání jakéhokoliv PDF souboru, který obsahuje pole :guilabel:`custom_note`,
:guilabel:`cesta` prázdná umožňuje prodejci zapsat libovolný poznatek, kde je tento formulářový prvek
dokument a zobrazen při sestavování PDF.

Přidat soubor PDF k produktu
==================

V Odoo Sales je také možné přidat vlastní PDF do produktového formuláře. Když se k produktu připojí
produktu a ten produkt je použit v citaci, tak ten PDF se také vloží do finálního PDF.

Chcete-li přidat vlastní PDF do produktu, začněte tím, že se přesunete na:
--> Produkty“ a vyberte požadovaný produkt, ke kterému chcete přidat vlastní PDF.

.. poznámka::
Dokument může být také přidán k produktové variantě místo produktu. Pokud existují dokumenty
na produktu i jeho variantě se zobrazují pouze dokumenty v variantě.

Chcete-li přidat vlastní dokument do produktové varianty, přejděte na:
Produkty --> Varianty produktů. Vyberte požadovanou variantu a klikněte na tlačítko „Dokumenty“.
tlačítko a postupně nahrajte vlastní dokument k konkrétnímu produktovému variantě.

Na stránce produktu klikněte na tlačítko „Dokumenty“ v horní části stránky a přejděte
stránku s dokumenty k danému produktu, kde jsou uloženy související dokumenty.
Nahráním souboru z počítače nebo pomocí tlačítka „Nový“ nebo „Nahrát“.

.. obrázek: pdf_quote_builder/dokumenty-chytře-tlačítko.png
:alt:Tlačítko „Dokumenty“ na produktovém formuláři v Odoo Sales.

Kliknutím na tlačítko „Nahrát“ se otevře adresář s místními soubory počítače. Nahraný dokument můžete
další konfigurace v dokumentu nebo kliknutím na ikonku
:guilabel:`(vertikální elipsa)` ikona v pravém horním rohu karty dokumentu a poté kliknutí
:edit-guilabel:

Kliknutím na tlačítko „Nový“ se zobrazí prázdná dokumentace, do které lze nahrát požadovaný PDF.
pomocí tlačítka „Nahrát soubor“ na formuláři umístěném v části „Obsah souboru“.
pole.

Konfigurace formuláře ve formátu PDF
----------------------

.. obrázek: pdf_quote_builder/prázdný dokumentový formulář.png
:alt: Standardní dokumentový formulář s různými poli pro konkrétní produkt v Odoo Sales.

První pole dokumentu je pro jeho název a je
šedé (neklikatelné) až do okamžiku nahrání dokumentu. Jakmile je soubor PDF nahraný,
V poli „Jméno“ je automaticky vyplněn název souboru ve formátu PDF a lze ho upravit.

Před nahráním dokumentu je možné určit, zda se jedná o
Vyberte z rozevírací nabídky „Typ“ pole „Soubor“ nebo „URL“.

.. obrázek: pdf_quote_builder/dokument-formulář-nahráno-pdf.png
:alt: Standardní dokument v podobě PDF, který byl nahrán do modulu prodeje Odoo.

.. poznámka::
Pokud je nahrán soubor ve formátu PDF, pole „Typ“ se automaticky vyplní na „Soubor“ a
nelze měnit.

Poté v sekci „Prodej“ v poli „Zobrazit“ vyberte z rolovací nabídky
menu a vyberte buď „Na poptávku“, „Na potvrzenou objednávku“ nebo
:guilabel:`Vnitřní citace PDF“.

- :guilabel:`Citace“: dokument je odeslán zákazníkům a k dispozici kdykoli.

- :guilabel:`Potvrzená objednávka“: dokument je zaslán zákazníkům po potvrzení objednávky.
To je nejlepší pro uživatelské příručky a další doplňkové dokumenty.

- :guilabel:`Uvnitř citace“: dokument je součástí PDF citaci, mezi hlavičku
stránky a sekci „Ceny“ v cenovém návrhu.

Příklad:
Pokud je zvolena možnost „Vnitřní citace“ v poli „Zobrazit“, a
vlastní PDF soubor, který je nahrán jako „Pracovní stůl u zdi.pdf“, je viditelný na cenové nabídce
portál pro zákazníky pod položkou „Dokumenty“.


:alt: Vzorek PDF souboru, který byl nahrán pomocí možnosti „citace“ v prodejním modulu Odoo.

Kromě pole „Obsah souboru“ máte možnost využít také
:guilabel:'Nastavit dynamické pole'. Při tomto nastavení si pamatujte, že výchozím modelem je
:guilabel:`sale_order_line“, na rozdíl od hlaviček a zápatí, které začínají
:guilabel:`prodejní objednávka“.

Nakonec v sekci „E-commerce“ rozhodněte o tom, zda chcete
:guilabel:`Vydat na webu“ tak, aby se soubor PDF zobrazoval na stránce produktu v e-shopu.

Příklad:
Pokud je zapnuta možnost „Zveřejnit na webu“, objeví se odkaz na nahrávaný dokument.
„Kancelářský stůl Corner Desk.pdf“ se objevuje na stránce produktu v e-shopu.

Vyskytuje se pod nadpisem „Dokumenty“, s odkazem na název dokumentu.
nahráním dokumentu.

.. obrázek:: pdf_quote_builder/show-product-page.png
:alt:Zobrazení odkazu na nahrávaný dokument v sekci prodeje pomocí Odoo Sales.

Poptávka ve formátu PDF
=========

V sekci „Smluvní dokumenty“ na objednávce zboží v části „Tvorba nabídky“ vyberte další smluvní dokumenty k sloučení.
do finální verze PDF. Pokud je vybrán dokument s vlastními poli, zobrazí se jako editační textové pole.
musí být vyplněny.

.. obrázek: pdf_quote_builder/quote-builder-headers.png
:alt: Vybrané hlavičky a záhlaví citátu pod sekcí „Quote Builder“ v citaci.

Jakmile je potvrzena citace s přednastaveným PDF, Odoo nabízí možnost tisknout
potvrzený citát pro kontrolu chyb nebo k uchování v záznamu.

Pro tisk PDF cenové nabídky přejděte na potvrzenou cenovou nabídku a klikněte na ikonu „⚙️ (převodovka)“
zobrazí se nabídka. Vyberte položku „Tisk“ z nabídky.
:guilabel:`Citace v PDF“.

.. obrázek:: pdf_quote_builder/drop-down-print-pdf.png
:alt:Vložte možnost tisku PDF nabídky do seznamu volby v konfirmačním prodejním dokladu v Odoo Sales.

Takto je okamžitě stáhne cenová nabídka ve formátu PDF. Když se otevře, zobrazí se spolu s konfigurovanou
Produktový PDF, který byl nastaven tak, aby se zobrazoval uvnitř citace, lze prohlížet a tisknout.

.. poznámka::
Stáhněte si tyto příklady:
nebo stáhnout z přílohy
:stáhnout:vzorek cenové nabídky
jako příklad pro odkaz na PDF souboru.

.. viz též:
   - :doc:`citát_šablona“
