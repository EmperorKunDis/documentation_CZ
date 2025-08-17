===============================
Kontrola identifikačního čísla DPH (VIES)
===============================

„Systém výměny informací o DPH <https://ec.europa.eu/taxation_customs/vies/#/vat-validation>“ nebo
**VIES** je nástroj poskytovaný Evropskou komisí, který vám umožňuje ověřit platnost DPH.
čísla pro společnosti registrované v Evropské unii.

Funkce ověřování DPH společnosti Odoo využívá VIES k ověření DIČ vašich kontaktů přímo z
Odoo rozhraní.

.. poznámka::
Ať už je funkce ověření DPH zapnutá nebo ne, Odoo kontroluje formát
Dph kontaktu proti očekávanému formátu čísel DPH
<https://cs.wikipedia.org/wiki/DIČ> z dané země.

Kontrola DIČ v rámci systému VIES
============================

Chcete-li tuto funkci aktivovat, přejděte na: „Účetnictví – Konfigurace – Nastavení“.
V sekci „Dani“ zapněte funkci „Kontrola DIČ“,
:guilabel:`Uložit“.

Jakmile je zapnutá funkce „Kontrola daňového čísla“, kontakt s :guilabel:`Tax ID“
pole je vyplněné a země není stejná jako země vaší společnosti, pak se v Odoo zobrazí
Zatrhněte políčko „Vnitrostátní platnost“. Odoo ověřuje DPH na základě údajů z VIES a
automaticky zkontroluje nebo odškrtne políčko „Vnitroskupinová platnost“ podle
platnost DPH.

.. obrázek: vat_verification/intra-community-valid.png
:alt: Vnitřní platnost zaškrtnutí položky na kontaktu

.. důležité::
Je možné ručně přepsat pole „Vnitroskupinový valid“ na kontaktu.
pokud je automatická kontrola VIES chybná (například pokud společnost byla nedávno založena).
Jeho DPH ještě není v systému VIES (VAT Information Exchange System), což je zaznamenáno do chatu pro transparentnost.

.. poznámka::
Odoo může automaticky aplikovat daňové pozice. Pokud chcete ověřit DPH, musíte
Funkce čísel je zapnutá, takže pokud máte v nastavení fiskálních položek povolené DPH, bude
Intra-komunitní platná čísla DPH se aplikují automaticky.
