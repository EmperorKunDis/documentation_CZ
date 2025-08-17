=====================
Google Search Console
=====================

Google Search Console je bezplatná služba poskytovaná společností Google, která umožňuje majitelům webových stránek
monitorovat, udržovat a řešit problémy s přítomností na stránce ve výsledcích vyhledávání Google.
cenné poznatky o tom, jak Google vnímá a interaguje s vaším webem, pomáhají vám optimalizovat jeho
výkon.

Pro zapnutí služby Google Search Console pro váš web přejděte na stránku „Google Search Console
Pak vyberte typ vlastnictví
:ref:`GSC-Doména“ nebo „GSC-URL předpona“.

.. obrázek: google_search_console/add-domain-or-url-prefix.png
:alt:Doména nebo předpona webové stránky Googlu

.._Doména GSC:

Doménová nemovitost
===============

Vlastnost domény v Search Console sleduje všechny verze vašich webových stránek, včetně poddomén.
protokoly (http/https). Tento komplexní pohled umožňuje analyzovat celkový výskyt vašeho webu ve vyhledávačích.
výkon a učinit informovaná rozhodnutí k optimalizaci jeho viditelnosti. Zadejte doménu, např.
Vyberte „example.com“ a klikněte na tlačítko „Pokračovat“.

.. poznámka::
   - Typ domény lze ověřit pouze prostřednictvím
„Záznam DNS <https://support.google.com/webmasters/answer/9008080?hl=cs#domain_name_verification&zippy=%2Chtml-tag>“.
   - Google doporučuje vytvořit alespoň jednu doménovou vlastnost, aby reprezentovala váš web, protože je nej
kompletní pohled na informace o vašem webu.

.._předpona URL GSC:

Vlastnost předpony URL
===================

Tento typ ověření je obvykle jednodušší, protože máte k dispozici více ověřovacích metod, například
pomocí vašeho stávajícího účtu Google Analytics nebo Tag Manager. Dává také smysl se podívat na část
z vašeho webu samostatně. Například pokud pracujete s konzultantem na určité části vašeho
webové stránky, možná budete chtít tuto část ověřit samostatně, abyste omezili přístup k vašim datům. Zadejte URL
např. „https://example.odoo.com/“ a klikněte na tlačítko „Pokračovat“.


Kontrola vlastnictví webových stránek
===========================

Před použitím služby Google Search Console pro váš web je nutné ověřit vlastnictví webu.
Proces ověření je bezpečnostní opatření, které chrání jak vás, tak i Google. Zajišťuje, že účet může používat jen
autorizovaní uživatelé mají přístup k citlivým datům a že máte kontrolu nad tím, jak se vaše webová stránka
v rámci vyhledávání na Googlu.

K dosažení tohoto cíle lze použít pět metod:

..._web/google-search-console:

#:ref:`Nahrávání souborů HTML GSC“
#„Záznam DNS <https://support.google.com/webmasters/answer/9008080?hl=cs#domain_name_verification&zippy=%2Chtml-tag>“
#„<https://support.google.com/webmasters/answer/9008080?hl=en#meta_tag_verification&zippy=%2Chtml-tag>“
#„Sledovací kód Google Analytics <https://support.google.com/webmasters/answer/9008080?hl=cs#google_analytics_verification>“
#„Snippet kontejneru Google Tag Manager <https://support.google.com/webmasters/answer/9008080?hl=cs#google_tag_manager_verification>“

.. poznámka::
Nejlepší metoda pro vás závisí na vašem komfortu a technických znalostech. Pro začátečníky je
Použití souborového nahrávání nebo HTML tagu může být nejjednodušší. Tyto možnosti jsou pohodlné, pokud již používáte
Google Analytics nebo Tag Manager. Potřebujete přístup do nastavení domény u registrátora.
ověření.

.. _soubor HTML GSC:

Nahrávání souborů ve formátu HTML
----------------

Tento způsob zahrnuje nahrání HTML souboru poskytnutého společností Google, který obsahuje ověřovací kód.
musíte v nastavení webové stránky Odoo zadat. Google ověřuje vlastnictví tím, že kód zkontroluje.

#Jakmile do pole „URL předpona“ zadáte adresu svého webu a kliknete na tlačítko „Pokračovat“,
rozšířit část souboru HTML, kde najdete tlačítko ke stažení :icon:`fa-download`.

.... obrázek:: google_search_console/html-file-download.png
:alt: Stáhnout soubor HTML

#Stáhněte si soubor HTML pro ověření a zkopírujte ověřovací kód (například „google123abc.html“).

...... obrázek: google_search_console/otevřít_kopírovat_html_soubor.png
:alt:Otevřít a zkopírovat soubor HTML

#Ve vaší databázi Odoo přejděte na: „Webová stránka“ -> „Konfigurace“ -> „Nastavení“.
a zapněte v sekci SEO službu Google Search Console. Do pole zkopírujte
ověřovací kód (například „google123abc.html“) do příslušného pole.

....... obrázek: google_search_console/paste-html-code-settings.png
:alt:Vložte HTML kód do Odoo

#Ve službě Google Search Console klikněte na tlačítko „Přidat“ a poté proveďte všechny výše uvedené kroky.
ověření by mělo být provedeno ihned.

.. viz též:
:doc:`doménová_jména“
