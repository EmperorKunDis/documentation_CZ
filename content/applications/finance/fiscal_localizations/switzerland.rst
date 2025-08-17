===========
Švýcarsko
===========

ISR (Potvrzení o zaplacení s referenčním číslem)
===========================================

ISR je v Česku označení pro účtenky, které se používají ve Švýcarsku.
přímý odkaz na Odoo. Na fakturách pro zákazníky je nová tlačítka
*Tisk ISR*.

.. obrázek: Švýcarsko/Švýcarsko00.png
:align:center

.. tip::
Tlačítko "Vytisknout ISR" se objeví pouze tehdy, pokud je vedený účet.
uvedené na faktuře. Můžete použít CH6309000000250097798 jako číslo
číslo účtu a 010391391 jako referenci v měně ISR.

.. obrázek: Švýcarsko/Švýcarsko 01.png
:align:center

Pak otevřete PDF soubor v ISR.

.. obrázek:Švýcarsko/Švýcarsko 02.png
:align:center

Existují dvě varianty ISR: jedna s a jedna bez banky
souřadnice. Pro výběr se nabízí možnost tisknout
bankovní informace na ISR. Aby se aktivovaly, je potřeba
:menu:Účetnictví -> Konfigurace -> Nastavení -> Faktury zákazníkům
a povolit tiskárnu na ISR:

.. obrázek: švýcarsko/švýcarsko03.png
:align:center

Referenční číslo faktury ISR
-------------------------

Pro usnadnění procesu smíření můžete své referenční číslo ISR přidat jako „Referenční platba“ do
faktury.

Pro to je potřeba nakonfigurovat účetní deník, který obvykle používáte pro vystavování faktur. Přejděte na
Vyberte položku „Účetnictví“ -> „Konfigurace“ -> „Deníky“, otevřete deník, který chcete upravit (kliknutím na
Výchozí nastavení (pokud není zadána jiná hodnota, je název časopisu *Faktury zákazníkům*) klikněte na položku *Upravit* a otevřete *Pokročilé
Karta Nastavení*. V poli Komunikační standard vyberte Švýcarsko a klikněte na tlačítko Uložit.

.. obrázek:Švýcarsko/Švýcarsko - Izrael - reference.png
:align:center
:alt:Nastavte svůj deník tak, aby na fakturách v Odoo zobrazoval vaši ISR jako platbu.

Aktuální kurz měny
=========================

Můžete aktualizovat automaticky své měnové kurzy na základě Federální
Finanční správa ze Švýcarska. Pro tento případ je nutné
:menu „Účetnictví“ -> „Nastavení“, aktivujte nastavení více měn a vyberte službu
chcete.

.. obrázek: Švýcarsko/Švýcarsko 04.png
:align:center

Aktualizovaná sazba DPH pro leden 2018
============================

Od 1. ledna 2018 se sníží sazby DPH na některé výrobky a služby
vztahuje na Švýcarsko. Normální sazba 8 % se přepne na 7,7 %.
Sazba pro hotelnictví se přepne z 3,8 na 3,7 procenta.

Jak aktualizovat daně v Odoo Enterprise (Online nebo on-premise)?
------------------------------------------------------------------------

Pokud máte verzi 11.1, všechna práce je již hotová,
Nemusíte nic dělat.

Pokud jste začali s předchozí verzí, nejprve musíte aktualizovat
modul „Švýcarsko – účetní výkazy“. Pro tento modul se přihlaste
:menuvolba-->Aplikace --> odebrat filtr Aplikace --> vyhledat „Švýcarsko – Účetní výkazy“ --> otevřít modul --> kliknout na „aktualizovat“.

.. obrázek: švýcarsko/švýcarsko05.png
:align:center

Jakmile to uděláte, můžete začít vytvářet nové daně pro
Aktualizované sazby.

.. tip::
**Nepřekračujte ani nezměňte stávající daně** (8 % a 3,8 %).
Chcete je ponechat, protože můžete oba kurzy používat pro krátkodobé transakce.
dobu. Místo toho si pamatujte na uložení po kódování
všechny transakce v roce 2017.

Vznik takových daní by měl být následující:

-  Daň z přidané hodnoty: kopírujte původní daň, změňte její název a označení
faktura, sazba a skupina daně (platné od verze 10 pouze)

-  Dodatečné daně: kopírujte původní daň, změňte její název a označení
faktura, sazba a skupina daně (platné od verze 10 pouze). Od verze 10
nový výkaz zobrazuje podrobnosti pro staré a nové sazby.
Aby také nastavil tagy podle toho.

   -  Pro 7,7 % daně: Švýcarsko DPH formulář: sazba 302 základ, Švýcarsko
Formulář DPH: sazba daně 302

   -  Sazba DPH 3,7 %: Švýcarsko - daňový formulář: svislá čára 342 základ
Forma DPH: sazba daně 342

Níže najdete správnou konfiguraci pro všechny daně.
je součástí Odoo

+-------------------------------------------------+------------+------------------------+--------------------------------------+-----------------+---------------------------------------------------------------------------+
|Název daně|Sazba DPH|Jméno na faktuře|Skupina daní (účinná od verze 10)|Předmět daně|Štítek|
+=================================================+============+========================+======================================+=================+===========================================================================+
|DPH 7,7 % při nákupu B&S (TN)               | 7,7 %      | 7,7 % při nákupu     |DPH 7,7 %                | Nákupy       | Švýcarsko DPH Formulář: svislá čára 400                                             |
+-------------------------------------------------+------------+------------------------+--------------------------------------+-----------------+---------------------------------------------------------------------------+
|DPH 7,7 % při nákupu B&S (včetně DPH)              | 7,7 %      | 7,7 % kupní cena vč.       |DPH 7,7 %                             |Nákupy        |Švýcarská daňová forma: sazba 400                                           |
+-------------------------------------------------+------------+------------------------+--------------------------------------+-----------------+---------------------------------------------------------------------------+
|7,7 % z investic a dalších položek (TN)     |7,7 %      |7,7 % investičních výdajů  |7,7 % DPH                             |Nákupy        |Švýcarsko VAT Form: grid 405
+-------------------------------------------------+------------+------------------------+--------------------------------------+-----------------+---------------------------------------------------------------------------+
|DPH 7,7 % z investic a dalších položek (včetně DPH)   |7,7 %      |DPH 7,7 % vč. DPH       |DPH 7,7 %                          |Nákupy        |Švýcarská daňová forma: sazba 405
+-------------------------------------------------+------------+------------------------+--------------------------------------+-----------------+---------------------------------------------------------------------------+
|DPH 3,7 % při nákupu B&S (TS)              | 3,7 %      | 3,7 % při nákupu     | DPH 3,7 %                             | Nákupy       | Švýcarsko VAT Form: grid 400                                            |
+-------------------------------------------------+------------+------------------------+--------------------------------------+-----------------+---------------------------------------------------------------------------+
|DPH 3,7 % při nákupu B&S (včetně TS)           | 3,7 %      | 3,7 % při nákupu vč.       |DPH 3,7 %                             |Nákupy        |Švýcarská daňová forma: sazba 400
+-------------------------------------------------+------------+------------------------+--------------------------------------+-----------------+---------------------------------------------------------------------------+
|DPH 3,7 % z investic a dalších položek (TS)     | 3,7 %      | 3,7 % investice         |DPH 3,7 %                             |Nákupy       |Švýcarská daňová forma: sazba 405
+-------------------------------------------------+------------+------------------------+--------------------------------------+-----------------+---------------------------------------------------------------------------+
|DPH 3,7 % z investic a dalších položek (včetně TS)   | 3,7 %      |3,7 % investice vč.     |DPH 3,7 %                             |Nákupy       |Švýcarsko DPH Formulář: sestava 405
+-------------------------------------------------+------------+------------------------+--------------------------------------+-----------------+---------------------------------------------------------------------------+
|DPH ve výši 7,7 % (TN)                              |7,7 %       |7,7 %                    |DPH ve výši 7,7 %                     |Prodej         |Švýcarsko VAT Form: sazba 302 základ, Švýcarsko VAT Form: sazba 302 daň
+-------------------------------------------------+------------+------------------------+--------------------------------------+-----------------+---------------------------------------------------------------------------+
|DPH 7,7 % (včetně DPH)                              | 7,7 %       | 7,7 % včetně DPH      |DPH 7,7 %                             |Prodej         |Švýcarsko VAT Form: Grid 302 Base, Švýcarsko VAT Form: Grid 302 Tax   |
+-------------------------------------------------+------------+------------------------+--------------------------------------+-----------------+---------------------------------------------------------------------------+
|DPH ve výši 3,7 % (TS)                              | 3,7 %       | 3,7 %                   |DPH ve výši 3,7 %                             |Prodej         |Švýcarsko VAT Form: grid 342 základ, Švýcarsko VAT Form: grid 342 daň
+-------------------------------------------------+------------+------------------------+--------------------------------------+-----------------+---------------------------------------------------------------------------+
|DPH 3,7 % (včetně TS)                              | 3,7 %      |3,7 % včetně DPH          |DPH 3,7 %                             |Prodej           |Švýcarsko VAT Form: grid 342 základ, Švýcarsko VAT Form: grid 342 daň
+-------------------------------------------------+------------+------------------------+--------------------------------------+-----------------+---------------------------------------------------------------------------+

Pokud máte dotazy nebo připomínky, kontaktujte prosím naši podporu pomocí
www.odoo.com/help.

.. tip::
Pamatujte na aktualizaci svých fiskálních pozic. Pokud máte verzi
Pokud je verze 11.1 nebo vyšší, nic se neděje. Jinak budete také
Musíte aktualizovat své daňové pozice v souladu s tímto.
