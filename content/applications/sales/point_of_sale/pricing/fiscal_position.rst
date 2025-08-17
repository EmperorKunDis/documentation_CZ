=================================
Příjmy z flexibilních daní
=================================

Při podnikání můžete potřebovat aplikovat různé daně a evidovat transakce na různých účtech.
účty podle typu a umístění vašich zákazníků a dodavatelů.

Funkce „Daňová pozice“ vám umožní nastavit pravidla, která automaticky vyberou správnou
dani a účetnictví používané pro každou transakci.

.. viz též:
   - :doc:`../../../finance/účetnictví/daně/daňová pozice“
   - :doc:`../../../finance/účetnictví/daně`

Konfigurace
=============

Chcete-li tuto funkci zapnout, přejděte na: „Prodejní místo –> Konfigurace –> Nastavení“, posuňte
a v sekci „Účetnictví“ zapněte „Příležitostné daně“.

Poté nastavte výchozí daňovou pozici, která se bude vztahovat na všechny prodeje ve vybraném POS.
:guilabel:`Výchozí“ pole. Můžete také přidat další fiskální pozice, ze kterých se bude moci vybrat v
:guilabel:`Povoleno`.

.. obrázek: fiskální_postavení/pružné_daňové_sazby.png
:align:center

Podle balíčku pro daňovou lokalizaci:
aktivované, několik daňových pozic je přednastaveno a lze je nastavit a použít v POS.
Mohou také vytvářet nové daňové pozice.

.. poznámka::
Pokud nezadáte daňovou polohu, daň zůstane taková, jak je definovaná v poli „Dodavatelské daně“
na výrobku.

Použijte fiskální pozice
====================

Otevřete sezení POS (:ref:`<pos/session-start>`) a použijte jednu ze povolených fiskálních pozic. Pak
Klikněte na tlačítko „Dani“ vedle ikony ve tvaru knihy a vyberte daňovou polohu.
seznamu. Přiřazením produktů k dané skupině se na ně aplikují definovaná pravidla automaticky.
fiskální pozice.

.. obrázek: fiskální_pozice/set-tax.png
:align:center

.. poznámka::
Pokud je nastaven výchozí daňový postih, tlačítko daně zobrazí název daňového postihu.

.. viz též:
:doc:`../../../finance/účetnictví/daně/daňové pozice`
