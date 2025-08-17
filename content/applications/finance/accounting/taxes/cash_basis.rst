================
Daň z příjmů na základě hotovosti
================

Daň z prodeje je splatná při přijetí platby, zatímco standardní daň je splatná
faktura je potvrzena. Zároveň hlásíte příjmy a výdaje státu na základě hotovosti
Metoda založená na základě je v některých zemích povinná a podléhá určitým podmínkám.

.. příklad::
prodáváte produkt v prvním čtvrtletí svého účetního roku a platba přijde ve druhém
čtvrtletí. Základem pro výpočet daně je metoda na účetnictví podle hotovosti a daň se platí za 2. čtvrtletí.

Konfigurace
-------------

Přejděte do sekce „Účetnictví“ - „Konfigurace“ - „Nastavení“ a pod položkou „Dani“.
sekce, zapnout:guilabel:„Na základě hotovosti“.

Poté definujte záznam „Daňový deník na základě hotovosti“. Klikněte na tlačítko externího odkazu vedle
časopis aktualizovat své výchozí vlastnosti, jako například „Název časopisu“, „Typ“ nebo
:shortcode:.

.. obrázek: cash_basis/tax_cash_basis_journal.png
:align:center
:alt:Vyberte si svůj daňový deník a klikněte na externí odkaz

.. poznámka::
Výchozí název záznamů v knize :guilabel:`Daň z příjmu na základě obratu“ je „Záznamy daňového účetnictví“.
:guilabel:`CABA“ zkratka.

Jakmile je hotovo, přejděte na :menuselection:`Účetnictví --> Konfigurace --> Účetnictví: Daně`
konfigurovat své daně. Můžete buďto vytvořit novou daň nebo aktualizovat stávající daň tak, že
kliknutím na něj.

Sloupec „Účet“ odráží správné přechodové účty, na které se mají převádět daně do doby
Je zaevidován příjemce platby.

.. obrázek: cash_basis/account_column.png
:align:center
:alt:Do sloupce účtu zadejte přechodný účet, kam se odvádějí daně do doby platby
Je zapsaná.

V záložce „Další možnosti“ rozhodněte o „Zdaňovací povinnosti“. Vyberte
„Založeno na platbě“, takže daň je splatná až po přijetí platby faktury.
Pak také definujte účet „Přechod na účtování v hotovosti“ (guilabel:Cash Basis Transition Account), kam se zaznamenává daňová částka
dokud nebyla původní faktura vyrovnána.

.. obrázek: cash_basis/advanced_options.png
:align:center
:alt: Vložte do účtu Přechod na kasovou metodu, kam se převedou daňové částky až do zaplacení
usmíření.

Dopad hotovostních daní na účetnictví
----------------------------------------

Pokud chceme ilustrovat dopad daňového režimu na účetnictví, vezměme si příklad
prodej produktu za 1 000 $, s daní z příjmů ve výši 15 %.

.. obrázek: cash_basis/faktura_pro_zákazníka_s_cbte.png
:align:center


V účetnictví jsou vytvořeny následující položky a současně je ve zprávě o dani prázdná.

+----------------------------+----------------------------+
|**Kniha zákazníků (INV)**                                     |
+============================+============================+
|Debetní účet|Kreditní účet|
+----------------------------+----------------------------+
|Příjmy 26 783 Kč           |                            |
+----------------------------+----------------------------+
|                              |Příjem 1 000 USD           |
+----------------------------+----------------------------+
|------------------------------|Přechodná daňová účetní kniha $150|
+----------------------------+----------------------------+

Pokud je pak platba přijata, je zaevidována takto:

+----------------------------+----------------------------+
|**Bankovní časopis (BANK)**                                   |
+============================+============================+
|Debetní účet|Kreditní účet|
+----------------------------+----------------------------+
|Banka 27 384 Kč              |                            |
+----------------------------+----------------------------+
|------------------------------|Závazky 27 498 Kč|
+----------------------------+----------------------------+

.. poznámka::
Jakmile je platba zaevidována, můžete použít tlačítko „Rychlé vstupy“ na základě hotovosti.
fakturu, abyste se k nim mohli dostat přímo.

Na závěr se při vyrovnání faktury s platbou automaticky vytvoří
vytvořeno:

+----------------------------+----------------------------+
|Daňový deník na základě hotovostních příjmů (CABA)|
+============================+============================+
|Debetní účet|Kreditní účet|
+----------------------------+----------------------------+
|Příjmový účet 1 000 USD       |                            |
+----------------------------+----------------------------+
|Přechodná daňová účetní kniha za 150 USD |                        |
+----------------------------+----------------------------+
|                              | Účet příjmů 1 000 USD |
+----------------------------+----------------------------+
|                               | Daň přijatá 150 USD       |
+----------------------------+----------------------------+

Výpisy z účtu :guilabel:`Příjmový účet` versus :guilabel:`Příjmový účet“ jsou neutrální, ale
je potřeba, aby byly v Odoo správně vyplněny daňové hlášení a přesné základní částky daně.

Doporučuje se používat výchozí účet „Základní daňový příjem“ (:guilabel:`Base Tax Received Account`), abyste měli zůstatek nulový.
Vaše příjmový účet není zbytečně znečištěn účetními pohyby. Chcete-li tak učinit, přejděte na
V menu „Nastavení“ -> „Doprava“ vyberte
„Příjem z daní“ v „Kapitálovém účtu“.
