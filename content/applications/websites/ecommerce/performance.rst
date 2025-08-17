======================
Správa výkonu
======================

Odoo integruje různé nástroje pro analýzu a zlepšení výkonnosti vašeho e-shopu.
webové stránky.

Monitorování dat
===============

Služba **Website** umožňuje sledovat a analyzovat prodejní výkonnost vašeho e-shopu.
Výchozí pohled na zprávy, přejděte do: „Webová stránka“ → „Zprávy“ → „E-commerce“. Tento panel vám pomůže
Sledujete vše související s prodejem, jako je například výkon prodeje podle produktu, kategorie nebo dne atd.

.. obrázek: výkon/reporting.png
:align:center
:alt:Reportování výkonu elektronického obchodu

Kliknutím na „Měření“ můžete vybrat typ měření použitý v grafu, například:

- :guilabel:„Poznámka“;
- :guilabel:`Počet faktur“;
- :guilabel:`Celková daň z přidané hodnoty nezahrnutá v ceně“;
- :guilabel:`Velikost“;
- ...

Mezi další možnosti patří více pohledů (převrácení, srovnání atd.), porovnávání období nebo let.
vložit do tabulky, atd.

Analýza
=========

Můžete propojit svou webovou stránku s :ref:`analytics/plausible`.
:ref:`analytics/google-analytics`.

.. ecommerce/výkon/poštovní fronta:

Optimalizace e-mailové fronty
========================

Pro weby, které prodávají vstupenky na akce nebo zaznamenávají velký nárůst provozu,
potvrzení objednávky mohou zpomalit proces platby.
pro ostatní zákazníky.

Pro zlepšení výkonu mohou být tyto e-maily zařazeny do fronty a zpracovány samostatně od objednávky.
potvrzení. Tento proces řídí akce „Odeslat nevyřízené e-maily“ z rozhraní pro správu schválených objednávek.
která odesílá e-maily v pořadníku co nejdříve.

Pro umožnění asynchronního odesílání e-mailů:

#Aktivujte vývojářský režim: doc:`Vývojářský režim </aplikace/obecné/vývojářský_režim>“.
#Přejděte do nabídky „Aplikace“, odstraňte filtr „Aplikace“ a nainstalujte filtr „Prodej“.
   - Modul Asynchonní e-maily.
#Přejděte do sekce „Nastavení“ – „Technické“ – „Parametry systému“ a nastavte
:parametr systému guilabel:sale.async_emails nastavte na hodnotu True.
#Přejděte na „Nastavení > Technické > Plánované akce“ a ujistěte se, že je
:guilabel:`Akce: Odeslat neodeslané e-maily“ je zapnutá.

.. upozornění:
Povolení této funkce může zpoždění potvrzení objednávky a fakturačních e-mailů o pár minut oddálit.
je doporučován pouze pro vysokonávštěvnostní weby, protože může způsobit zbytečné prodlevy u elektronického obchodování
webové stránky s průměrným provozem.
