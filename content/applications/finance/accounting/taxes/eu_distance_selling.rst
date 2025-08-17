===================================
Prodej na dálku v rámci EU
===================================

Vnitřní obchod v rámci Evropské unie zahrnuje přeshraniční obchod se zbožím a službami.
prodejci registrovaní k DPH pro fyzické osoby (B2C), které se nacházejí v členském státě Evropské unie.
Transakce se obvykle provádí na dálku prostřednictvím internetových platforem, objednávek poštou nebo telefonicky.
nebo jinými komunikačními prostředky.

Prodej na dálku v rámci Evropské unie podléhá specifickým pravidlům a předpisům o DPH. Prodávající
musí být připočítána DPH ve výši sazby DPH platné v zemi kupujícího.

.. poznámka::
Pokud je dodavatel mimo EU, platí to i pro něj.

Konfigurace
=============

Funkce EU Intra-community Distance Selling vám pomůže splnit tuto normu tím, že
Vytváření a konfigurace nových fiskálních pozic a daní na základě země vaší společnosti.
zapněte ji v menu „Účetnictví – Konfigurace – Nastavení – Daně“, zaškrtněte
„Prodej na dálku v rámci EU“, „Uložit“.

.. obrázek:eu_distance_selling/enable-feature.png
:alt: Vlastnost pro vnitroevropské obchodování na dálku je dostupná ve výchozích nastaveních účetnictví Odoo

.. tip::
Každou změnou nebo přidáním daní můžete automaticky aktualizovat své fiskální pozice.
jít na: „Účetnictví / Fakturace --> Nastavení --> DPH --> EU Distance
Vyberte možnost „Prodej“ a klikněte na tlačítko „Obnovit mapování daní“.

.. poznámka::
Doporučujeme si ověřit, zda navrhované mapování je vhodné pro produkty a služby.
předtím, než ji použijete.

.. viz též:
   - :doc:`../dane`
   - :doc:`/fiscal_localizations`
   - :doc:`fiskální pozice“

Elektronický obchod s jedním místem podání (OSS)
===================

Systém jednoho okamžiku, který zavedla Evropská unie, usnadňuje výběr DPH.
pro prodej zboží a služeb přes hranice. Přednostně se vztahuje na obchod mezi podniky a spotřebiteli
případů (B2C). S OSS mohou podniky registrovat DPH ve své domovské zemi a používat
jediný online portál, který by vyřizoval jejich povinnosti v oblasti DPH za prodeje na území EU.
Primární schémata: Schéma pro služby přeshraničního charakteru Union OSS a Schéma dovozu Import OSS
pro zboží v hodnotě do 150 eur.

Zprávy
-------

Pro vytvoření zpráv o prodeji nebo dovozu podle pravidel OSS a jejich odeslání na portál OSS přejděte na
Vyberte položku „Účetnictví“ – „Zprávy“ – „Daňový výkaz“, klikněte na „Výkaz: Obecný daňový výkaz“.
report“ a vyberte buď „Prodej OSS“ nebo „Dovozy OSS“. Jakmile je vybráno, klikněte na
„PDF“, „XLSX“ nebo „XML“ v levém horním rohu. To vygeneruje
otevřený současný report v zvoleném formátu. Jakmile je vygenerován, přihlaste se do své
předložit je příslušnému orgánu státní správy, který ji zveřejní na portálu OSS.

.. obrázek::eu_distance_selling/oss-report.png
:alt:Zpráva o přístupnosti

.. viz též:
   - „Evropská komise: Společný systém odvodu DPH | Daňové a celní unie <https://ec.europa.eu/taxation_customs/business/vat/common-system_en>“
