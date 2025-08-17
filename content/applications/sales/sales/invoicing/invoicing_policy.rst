================================================
Faktura na základě dodaných nebo objednaných množství
================================================

Různé obchodní politiky mohou vyžadovat různé způsoby fakturace:

- Pravidlo „Faktura, která je objednána“ se používá jako výchozí režim v Odoo Sales, což znamená
Zákazník je fakturován až po potvrzení objednávky.
- Pravidlo „Faktura vystavená při dodání“ vystavuje zákazníkům fakturu, jakmile je dodávka hotová. Toto pravidlo
je často používána pro podniky prodávající materiál, tekutiny nebo potraviny ve velkém množství.
v případě objednaného množství se může lišit o něco od dodaného množství, což je výhodné
to fakturovat skutečně dodané množství.

Možnost mít různé způsoby fakturace poskytuje větší flexibilitu.

Politika fakturace
=========================

Pro aktivaci potřebných funkcí fakturace přejděte na: „Sales app -->
Konfigurace --> Nastavení“, a pod nadpisem „Fakturace“ vyberte
Pravidlo „Způsob fakturace“: „Fakturovat, co je objednáno“ nebo „Fakturovat, co je skutečně dodáno“.
dodáno.

.. obrázek: fakturace_politika/fakturace-politika-nastaveni.png
:align:center
:alt:Volba způsobu fakturace v Odoo Sales.

.. důležité:
Pokud je vybrána pravidla „Faktura co přijde“, není možné aktivovat
automatické vystavování faktur, které automaticky generují faktury při nákupu na internetu.
platba je potvrzena.

Způsob fakturace produktu
================================

Na jakékoliv stránce produktu přejděte na „Aplikace pro prodejní tým --> Produkty --> Dashboard s produkty“ a najděte
V položce „Způsob fakturace“ v záložce „Obecné informace“.
Můžete je změnit ručně pomocí rozbalovací nabídky.

.. obrázek: fakturace_politika/fakturace-politika-obecne-informace-tab.png
:align:center
:alt:Jak změnit způsob fakturace produktu na formuláři prodeje v Odoo.

Dopad na prodejní tok
====================

V modulu Odoo Sales je základní prodejní proces zahájen vytvořením nabídky. Pak se nabídka
je odeslána zákazníkovi. Následně je potřeba ji potvrdit, čímž se závazná nabídka mění na objednávku k prodeji.
Tím vzniká faktura.

Následující tabulka ukazuje, jak se na zmíněný prodejní tok vztahují pravidla účtování.

- „Faktura co je objednáno“: V základním prodejním toku nemá vliv. Faktura se vytvoří jako
ještě před potvrzením prodeje.
- :guilabel:`Faktura za dodané zboží“: Malý dopad na průtok prodeje kvůli dodanému množství
musí být ručně zadána do objednávky na prodej. Nebo lze nainstalovat a používat aplikaci Inventář
aby se před vystavením faktury pomocí aplikace *Prodej* ověřila dodaná množství.

.. varování:
Pokud uživatel zkusí vytvořit fakturu bez ověření dodaného množství, následuje
Při zadání chybného čísla se objeví hláška: „Není vložena fakturační položka. Pokud má produkt stav dodaný,
prosím, ujistěte se, že byla dodána objednaná množství.

.... obrázek: fakturace_politika/chyba_v_fakturaci.png
:synchronizace: střed
:alt:Pokud je zvolena politika fakturace dodaných množství, ujistěte se, že bylo dodáno nějaké množství.

.. poznámka::
Jakmile je potvrzena nabídka a stav se změní z „Nabídka odeslána“ na
:guilabel:`Objednávka na prodej“, dodané a fakturované množství je k dispozici ke zhlédnutí přímo
z objednávky prodeje. To platí pro obě možnosti nastavení účetního pravidla.

....... obrázek: fakturace_politika/fakturace-politika-dodacni-linie.png
:synchronizace: střed
:alt:Jak vidět dodané a fakturované množství v Odoo Sales.

Odoo automaticky přidává množství na fakturu, a to jak pro položky „Dodané“, tak i
:guilabel:`Faktura“, i když se jedná o částečnou dodávku, po potvrzení cenové nabídky.

Konečně existuje několik různých možností vytvoření faktury: :guilabel:`Běžná faktura“.
„Úhrada v hotovosti (v procentech)“ nebo „Úhrada v hotovosti (pevná částka)“.

.. viz též:
Zkontrolujte dokumentaci, která vysvětluje možnosti úvěru na hypotéku, abyste se dozvěděli více.
:doc:`/aplikace/prodej/prodej/fakturace/dodatečná platba“
