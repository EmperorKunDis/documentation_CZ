=================
Srážková daň
=================

Daň srážková, také známá jako daň z úschovy, ukládá plátci faktury zákazníka
Odečíst daň z platby a odvést ji státu. Obvykle se daně
součet pro výpočet celkové částky zaplacené, zatímco srážková daň se přímo odečte od
Platbu.

Konfigurace
=============

V Odoo se srážková daň definuje vytvořením záporné daně. K jejímu vytvoření postupujte takto:
do sekce „Účetnictví“ - „Nastavení“ - „Daně“ a v poli „Částka“
zadat zápornou částku.

.. obrázek: zadržení/záporná částka.png
:alt:  negativní daň v poli

Pak přejděte na záložku „Další možnosti“ a vytvořte daňovou skupinu s pojmenováním „Tax Group“.

.. obrázek:retention/tax-group.png
:alt: daňová skupina pro daň z příjmu.

.. tip::
Pokud je odpočet procentem z běžné daně, vytvořte :guilabel:`Dani` s
:guilabel:`Daňová kalkulace“ jako „Skupinu daní“. Pak nastavte oba běžné daně
v záložce „Definice“.

Daň z přijaté tržby na fakturách
===========================

Jakmile je daň z držení vytvořena, může být použita na formulářích zákazníků, objednávkách a
faktury zákazníků.
K jedné řádku faktury lze přiřadit několik daní.

.. obrázek:retence/faktura-dph.png
:alt: daňové řádky faktury

.. viz též:

:doc:`../dane`
