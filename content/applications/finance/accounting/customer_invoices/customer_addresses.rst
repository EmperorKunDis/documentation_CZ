==============================
Dodací a fakturační adresa
==============================

Společnosti často mají více poboček a je běžné, že by měla být faktura odeslána na
jedna adresa a zásilka by měla být zaslána na jinou. Funkce **Adresy zákazníků** v Odoo je
jehož cílem je usnadnit specifikaci adresy pro každý případ.

.. viz též:
:doc:`přehled“

Konfigurace
=============

Pro specifikaci fakturační a dodací adresy objednávky prodeje se nejprve přesuňte na záložku:menuselection:Účetnictví
V sekci „Konfigurace“ -> „Nastavení“. V části „Faktury zákazníků“ zapněte
Klikněte na „Uložit“.

V citaci a v objednávce je nově pole pro adresu faktury.
:guilabel:`Adresa dodání“. Pokud zákazník má fakturu nebo adresu dodání uvedenou na svém
:ref:`záznam kontaktu <sales/send_quotations/contact-form-config>“, v příslušném poli se používá
adresu, pokud není k dispozici žádná adresa kontaktu.

.. viz též:
Pro více informací se podívejte na dokumentaci k :ref:`Nastavení formuláře pro kontakt
<prodej/zaslání nabídek/kontaktní formulář - konfigurace>.


Faktura a dodání na různé adresy
==========================================

Příkazy k dodání a jejich přepravní lístky používají adresu nastavenou jako :guilabel:`Dodací
Adresa na prodejním dokladu. Výchozí nastavení fakturace ukazuje jak adresu dodací, tak i
adresu na faktuře, aby si zákazník mohl být jistý, že zboží dorazí na správné místo.

E-maily také putují na různé adresy. Citaci a objednávku zasíláme na hlavní kontakt
e-mail, jak je obvyklé, ale faktura bude zaslána na e-mailovou adresu uvedenou jako
„Fakturační adresa“ na objednávce prodeje.

.. poznámka::
   - Zprávy, jako je faktura a dodací list, lze upravit pomocí Studio
</aplikace/studio/pdf_reporty>.
   - Pokud je zaškrtnuté pole „Odeslat poštou“ při kliknutí na tlačítko „Odeslat a vytisknout“,
faktura bude zaslána na adresu uvedenou v objednávce.
