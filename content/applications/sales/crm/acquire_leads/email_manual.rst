=====================================
Vytvářejte kontakty (e-mailem nebo ručně)
=====================================

.. |st-o| nahradit za: :icon:`fa-star-o`
.. |st| nahradit za: :icon:`fa-star`

Leady lze přidat do aplikace CRM z vlastních e-mailových aliasů a ručně vytvořených nových.
záznamy, které jsou navíc k dispozici v aplikaci prostřednictvím
:doc:`kontaktní formulář na webu <opportunities_form>“.

Nejdříve zkontrolujte, že funkce Leads je zapnutá v databázi kliknutím na:menuselection:CRM
Přejděte do sekce „Nastavení“ a zaškrtněte políčko vedle „Vedení“. Pak klikněte
:guilabel:`Uložit“.

.. _crm/konfigurovat_e-mailovou_přezdívku:

Nastavte e-mailové aliasy
=======================

Každý prodejní tým má možnost vytvořit a používat své vlastní unikátní e-mailové přezdívky. Když
je zaslána na tuto adresu, vytvoří se příležitost (nebo kontakt) s informacemi z
zpráva.

Chcete-li vytvořit nebo aktualizovat e-mailovou adresu pro tým obchodníků, přejděte na:
Konfigurace --> Prodejní týmy“. Klikněte na tým z seznamu, abyste otevřeli stránku s podrobnostmi o týmu.

.. obrázek: email_manual/email-alias.png
:align:center
:alt:Stránka s podrobnostmi o prodejním týmu, zaměřená na sekci e-mailových přezdívek.

Do pole „E-mailový alias“ zadejte jméno e-mailového aliasu nebo upravte stávající jméno.
V poli „Přijímat e-maily od“ vyberte možnost z rolovací nabídky, která určuje, kdo může posílat
zprávy na tuto e-mailovou adresu:

- :guilabel:`Každý“: zprávy přijímá ze všech e-mailových adres.
- :guilabel:`Ověření partnerů“: přijímá pouze zprávy od e-mailových adres spojených s
partnera (kontakt nebo zákazníka).
- :guilabel:`Pouze pro sledovatele“: přijímá pouze zprávy od uživatelů, kteří sledují příspěvek související s
tým, například vedoucí nebo příležitost. Zprávy mohou také přijímat členové týmu.
- :guilabel:`Přihlášení zaměstnanci“: přijímá pouze zprávy od e-mailových adres, které jsou propojené
do rekordu v aplikaci *Zaměstnanci*.

Zákazníci získaní e-mailem
------------------------

Zprávy z e-mailových aliasů lze prohlížet kliknutím na:
Záznamy. Klikněte na záznam v seznamu, abyste jej otevřeli, a zobrazte podrobnosti.

E-mail, který přišel na alias, je přidán do vlákna „*chatter*“ pro kontaktní osobu.
Zpráva je přidána do pole titulku a pole :guilabel:`E-mail` je aktualizováno na
e-mailová adresa kontaktu.

.. obrázek: email_manual/chatter-message.png
:align:center
:alt:Chatová vlákna nově vytvořené příležitosti v aplikaci CRM.

.. poznámka::
Pokud funkce *leads* není na databázi povolena, zprávy zaslané na e-mailovou adresu jsou přidány
do databáze jako příležitosti.

.. viz též:
:doc:`/​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​

Vytvořte vlastní leady
=====================

Leady lze přidat přímo do aplikace CRM ručním vytvořením nového záznamu. Přejděte na
:menuvolba:`CRM aplikace --> Vedení obchodů“ pro zobrazení seznamu existujících vedených obchodů.

..tip:
Lze také přidávat kontakty pomocí tlačítka „Vytvořit kontakt“ v sekci „Generovat kontakty“.

V horním levém rohu seznamu klikněte na „Nový“ a otevřete prázdnou formu „Leads“.

Do prvního pole nového formuláře zadejte název pro nový kontakt. Následně do pole „Kontakt“ zadejte:
Název, a :label:„Firma“.

.. poznámka::
Pokud je kontakt převeden na příležitost, pole „Název společnosti“ se změní.
buď se tato příležitost spojí s existujícím zákazníkem nebo vytvoří nového zákazníka.

Vytvářejte příležitosti ručně
-----------------------------

Chcete-li ručně vytvořit příležitost, přejděte na: „Aplikace CRM - Prodej - Můj potrubí“.
V horní části stránky klikněte na tlačítko „Nový“ pro vytvoření nové kanbanové karty.
Do pole „Organizace / Kontakt“ zadejte název společnosti pro příležitost.

Vyberte si jméno a zadejte ho do pole „Příležitost“ (viz obrázek). *Toto je povinné pole*.
Pokud ručně vytváříte příležitost, je užitečné přidat jméno, které se týká podrobností o
možnost.

Příklad:
V následujícím příkladu je příležitost pojmenována „5 křesel pro prezidenty“. To určuje produkt,
zákazník zajímá, stejně jako potenciální počet produktů.

.... obrázek:email_manual/opportunity-example.png
:synchronizace: střed
:alt: Příklad příležitosti v prodejním kanálu CRM.

Zadejte kontaktní informace pro příležitost do pole Email a Phone.
pole.

Do pole „Očekávaný příjem“ zadejte odhadovanou hodnotu příležitosti.

.. poznámka::
Informace v poli „Očekávaný příjem“ a „Priorita“ lze použít k sledování
výkonnost jednotlivých prodejců i týmově.
:doc:`../výkonnost/očekávané příjmy“ a :doc:`../sledování leadů/hodnocení leadů“ pro více informací.
informace.

Pak použijte ikony |st-o| :guilabel:`(hvězda)` k přiřazení priorit.

- |st-o| |st-o| |st-o|: nízká priorita
- |st| |st-o| |st-o|: střední priorita
- |st| |st| |st-o|: vysoká priorita
- |st| |st| |st|: velmi vysoká priorita

.. poznámka::
Přiřazením prioritního stupně se změní pořadí úkolů v zobrazení kanbanu tak, že úkoly s vyšším prioritním stupněm
zobrazeny první.

Jakmile do něj vložíte všechny potřebné informace, klikněte na tlačítko „Přidat“.

.. obrázek:: email_manual/create-opportunities.png
:align:center
:alt:Pipeline CRM s nově vytvořenou příležitostí.
