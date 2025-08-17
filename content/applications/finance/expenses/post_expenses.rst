=============
Náklady na poštovné
=============

Jakmile je žádost o proplacení nákladů schválena, další krok je zadání
fakturační doklad do správné účetní knihy.

.. důležité::
Pro zaúčtování výdajových faktur je uživatel povinen mít následující oprávnění:
:doc:`práva přístupu <../obecne/uživatelé/prava_přístupu>“:

   - Účetnictví: *Účetní* nebo *poradce*
   - Náklady: *Manager*

Jen výdajové faktury s označením „Schváleno“ mohou přidat výdaje do účetní knihy. Chcete-li zobrazit všechny
faktury, přejděte na:menu-selection: `Fakturace aplikace --> Fakturační zprávy`.
Pouze schválené výdajové faktury, které je třeba zveřejnit, upravte filtry na levé straně.
Zaškrtnuto je pouze políčko „Schváleno“.

.. obrázek: post_expenses/post-reports.png
:align:center
:alt:Zobrazit zprávy k úhradě kliknutím na výdajové faktury a poté na zprávy k úhradě.

.. poznámka::
Výchozí panel „Všechny zprávy“ zobrazuje všechny výdajové faktury s výjimkou těch, které obsahují
status: „Odmítnuto“.

Faktury mohou být přidány do účetních knih dvěma způsoby:
<náklady/po jednotlivci> nebo :ref:`v hromadě <náklady/po více osobách>“.

.._výdaje/poštovné individuální:

Vytvářejte individuální zprávy
-----------------------

Pro zveřejnění jednotlivé faktury přejděte na: „Náklady aplikace - Fakturace“
Klikněte na konkrétní zprávu s atributem „Stav“ označeným jako „Schváleno“, abyste si ji mohli prohlédnout.
formulář. V tomto pohledu jsou představeny následující možnosti:
„Zpráva v příštím výplatním listu“, „Odmítnout“ nebo „Přepnout do režimu návrhu“.

Klikněte na položku „Záznamy v deníku“ a zobrazí se report.

Do pole :guilabel:`Journal` účetního deníku je zadána položka, kam se připisují náklady.
faktura za služby.

Po vložení výdajů do účetního deníku je možné použít tlačítko „Vstup do knihy“
se zobrazí na vrcholu obrazovky. Klikněte na tlačítko „Záznam v deníku“, a pak se zobrazí
pro záznam v deníku se zobrazí s označením „Přidáno“.

..._náklady/poštovné - více kusů:

Vyplňte více hlášení
---------------------

Pro vkládání více výdajových zpráv najednou přejděte na:
Prohlédněte si seznam faktur za služby. Vyberte faktury k schválení zaškrtnutím
za každý schválený report.

.. poznámka::
Pouze výdajové faktury s stavem „Schválené“ mohou přenést náklady na účet.
účetní deník. Pokud je vybrána faktura, která **nemůže být** zadána do účetnictví, například
neověřený výsledek nebo zpráva již byla publikována v časopise, pak se vyberou možnosti
Tlačítko „Přidat“ není vidět.

.. tip::
Pro výběr pouze schválených faktur doporučujeme upravit filtry na levé straně tak, aby se zobrazily
Zaškrtněte políčko „Schváleno“. Následně zaškrtněte políčko vedle
:guilabel:`Zaměstnanec“ do pole „Název sloupce“, abyste vybrali všechny zprávy s hodnotou „Schváleno“.
ihned.

Dále klikněte na tlačítko „Přidat příspěvky“.

.. obrázek: post_expenses/post-entries.png
:align:center
:alt:Vygenerujte více hlášení o výdajích najednou z pohledu Hlášení o výdajích s filtrem schválené.
