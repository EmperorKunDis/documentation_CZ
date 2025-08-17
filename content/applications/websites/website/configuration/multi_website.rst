=================
Více webových stránek
=================

Odoo vám umožňuje vytvářet více webových stránek z jedné databáze. To může být užitečné například
Pokud máte více značek pod jednou organizací nebo chcete vytvořit samostatné webové stránky pro
různé produkty nebo služby, nebo různé publikum. V těchto případech mít různé weby
pomáhají zabránit zmatkům a usnadňují vytváření digitálních marketingových strategií, které umožní dosáhnout cílové skupiny.
cílová skupina.

Každá webová stránka může být navržena a konfigurována nezávisle na vlastním doménovém jménu.
<doménové_jméno>, :doc:'vzhled <../web_design/vzledek>', :doc:'stránky <../stranky>', :doc:'menu
<../pages/header_footer>`, :doc:`jazyky <translate>`, :doc:`produkty
<../../ecommerce/products>“, přidělený obchodní tým atd. Mohou také
:ref:`sdílet obsah a stránky <multi-website/website_content>“.

..tip:
Duplicitní obsah (tj. stránky a obsah sdílené mezi více webovými stránkami) může mít negativní vliv.
dopad na stránku „SEO“.

Tvorba webu
================

Pro vytvoření nové webové stránky postupujte takto:

#Přejděte na: menu: „Webová stránka“ --> „Konfigurace“ --> „Nastavení“.
#Klikněte na tlačítko „Nový web“.

.. obrázek:: multi_website/create-website.png
:alt: Nový tlačítko webové stránky

#Uveďte název webu a doménu webu. Každý web musí být
publikovány pod vlastními doménami: :doc:`<domain_names>
#Adaptujte pole „Název společnosti“, „Jazyky“ a „Výchozí jazyk“.
pokud je třeba.
#Klikněte na tlačítko „Vytvořit“.

Poté můžete začít stavět svou novou webovou stránku.

.. poznámka::
Výchozí nastavení aplikací pro webové stránky, které máte nainstalované (např. eCommerce),
**Fórum**, **Blog**, atd. a související webové stránky jsou také k dispozici na
nový web. Odstraníte je změnou menu na webu.

Přepínání webových stránek
==================

Přepněte mezi webovými stránkami kliknutím na nabídku vedle tlačítka „+ Nový“
v pravém horním rohu a vyberte web, na který chcete přepnout.

.. obrázek: multi_website/switch-websites.png
:alt: Vybíráč webů

.. poznámka::
Při přechodu na jinou webovou stránku vás systém automaticky přesměruje na domovskou stránku této webové stránky.

Webové konfigurace
==============================

Většina nastavení webu je web-specifická, což znamená, že lze povolit/zakázat pro každý web.
upravit nastavení webu, přejděte na: „Webová stránka --> Konfigurace --> Nastavení“.
Vyberte požadovaný web v poli „Nastavení webu“ na horním okraji
Nastavení“ stránce a v žlutém pruhu upravte možnosti pro konkrétní
webové stránky.

.. poznámka::
   - Webové stránky jsou vytvářeny s výchozími nastaveními, která nejsou kopírována z jedné webové stránky na druhou.
druhý.
   - Ve více společnostním prostředí (</applications/general/companies>) může každá webová stránka být
spojené s konkrétní firmou v databázi, takže se zobrazují pouze informace týkající se dané firmy (např.
produkty, pracovní místa, události atd. se zobrazují na webových stránkách. Pro zobrazení
do pole :guilabel:`Společnost` zadat požadovanou společnost.

.. _multisite/webové stránky:

Dostupnost obsahu
--------------------

Výchozí nastavení je takové, že stránky, produkty, události atd. vytvořené z přední části (pomocí
Tlačítko „Nový“ (viz obrázek výše) je k dispozici pouze na webu, ze kterého byl vytvořen záznam.
Vytvářené zadní části jsou však k dispozici na všech webech výchozí. Obsah
Dostupnost lze změnit v administraci, například ve webovém rozhraní v poli „Webová stránka“. Například pro
produkty, přejděte na: „E-commerce --> Produkty“, vyberte produkt a přejděte do
:guilabel:`Prodej“ záložka. Pro fóra přejděte na „Nastavení -> Fóra“, pak vyberte
forum.

.. obrázek:: multi_website/forum-multi-website.png
:alt:Webová stránka v příspěvku na fóru

.. _webové pole:

Dokumenty a funkce lze zpřístupnit:

- Na všech webech: v poli `Webová stránka` nechte prázdné.
- Pouze na jedné webové stránce: nastavte pole :guilabel:`Webová stránka“ podle toho.
- Na některých webech: v tomto případě byste měli duplikovat položku a nastavit :guilabel:`Webová stránka`.
pole.

Stránky webu
~~~~~~~~~~~~~

Pro úpravu webové stránky, na které má být příspěvek publikován, postupujte takto:

#Přejděte na záložku „Webová stránka“ - „Struktura webu“ - „Stránky“.
#Otevřete vyhledávací lištu a vyberte webovou stránku, na které je aktuálně publikována.

.... obrázek:: multi_website/pages-switch-websites.png
:alt: Zobrazit stránky na webu

#Zaškrtněte políčko vedle stránky, kterou chcete změnit.
#Klikněte na pole „Webová stránka“ a vyberte webovou stránku nebo ji nechte prázdnou pro publikování stránky na
všechny weby.

.. poznámka::
Každá webová stránka musí mít svou vlastní domovskou stránku a nesmí být používána pro více webových stránek.

e-commerce funkce
==================

e-commerce funkce jako jsou produkty, kategorie e-shopu, ceníky, slevy, způsoby platby.
atd. lze omezit na:ref:`konkrétní web <webová stránka>“.

Zákaznický účet
-----------------

Můžete umožnit svým zákazníkům používat stejný účet
Všechny vaše weby přidáním možnosti „Sdílené
Zatrhněte políčko „Kontrolní účet“ v nastavení webu.

Ceny
-------

Ceny produktů se mohou lišit podle webové stránky pomocí :ref:`ceníků
<ecommerce/ceny>. Následující konfigurace je nutná:

#Přejděte na: menu: „Webová stránka“ --> „Konfigurace“ --> „Nastavení“.
#. Posuňte se dolů do části „Obchod – Zboží“ a vyberte „Ceníky“.
volba: `Nastavení více cen za produkt`.
#Klikněte na tlačítko „Ceník“ a definujte nové ceníky nebo upravte stávající.
#Vyberte ceník nebo klikněte na „Nový“, abyste vytvořili nový. Pak vyberte
:guilabel:`Konfigurace“ záložka a nastavte pole „Webová stránka“.

Reportér
=========

Analýza
---------

Každá webová stránka má své vlastní analytické nástroje. Chcete-li přepínat mezi webovými stránkami, klikněte na
v horním pravém rohu.

.. obrázek: multi_website/analytics-switch-websites.png
:alt:Přepínání webů v analýze

Další uvedené údaje
--------------------

Další reportovací údaje, jako například datový panel pro elektronický obchod, analýzy prodejů a návštěvníků lze
Skupiny podle webu, pokud je to nutné. Otevřete vyhledávací panel a zvolte: „Skupina podle…“ → „Web“.
