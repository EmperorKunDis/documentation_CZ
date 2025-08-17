=============
Vytváření úkolů
=============

Úkoly v projektu Odoo lze vytvářet ručně nebo automaticky, včetně e-mailů a webových stránek.
formuláře.

Vytváření manuálních úkolů
====================

Otevřete aplikaci Project a vyberte požadovaný projekt. Vytvořte novou úlohu provedením jedné z následujících akcí:
následující:

 - Kliknutím na tlačítko „Plus“ v horním levém rohu, což vytvoří
a novou úlohu v prvním kroku vašeho pohledu na Kanban.
 - Stisknutím tlačítka s ikonou „+“ vedle názvu stupně Kanban.
Vytváří novou úlohu v této fázi kanbanu.

Vyplňte pole „Název úkolu“ a přidejte jednoho nebo více „Příjemců“, pak klikněte
:guilabel:`Přidat“.

..._vytváření úkolů/konfigurace úkolu:

Konfigurace úloh
------------------

Klikněte na úkol, abyste jej otevřeli. Formulář úkolu zahrnuje následující pole, která můžete vyplnit:

 - :guilabel:`Název úkolu“: název úkolu.
 - :icon:`fa-star-o` (:guilabel:`Hvězda`): klikněte na ikonu :icon:`fa-star-o` (:guilabel:`hvězda“)
zadanou úlohu jako vysoce prioritní. Ikona se změní na žlutou barvu. Klikněte na ni znovu, abyste úkol označili za nízkou prioritu.
 - :guilabel:`Projekt“: projekt, ke kterému tato úloha patří.
 - :guilabel:`Příjemci úkolu“: osoba (osoby), která má na starosti vyřizování práce na tomto úkolu.
 - :tagy: vlastní štítky, které umožňují kategorizovat a filtrovat úkoly.
 - :guilabel:`Zákazník“: osoba nebo společnost, která bude fakturována za tuto práci. Toto pole je
Vyskytuje se v úkolech, které patří do fakturovatelných projektů.
 - :guilabel:„Položka objednávky“: může jít buď o prodejní objednávku, ze které byla tato položka vytvořena
úkolu nebo v prodejním příkazu, který byl k tomuto úkolu přidán ručně. Toto pole se zobrazuje pouze u úkolů
spojené s projekty, které lze fakturovat.
 - :guilabel:`Čas přidělený na úkol“: doba, po kterou se očekává práce na tomto úkolu.
evidované pomocí časových listin.
 - :guilabel:`Termín dokončení“: očekávaný termín dokončení úkolu. Jakmile tento pole vyplníte, můžete
Přidejte také datum začátku, abyste označili celou dobu trvání úkolů.

..tip:

   - Můžete také vytvářet nové úkoly přepnutím na seznam nebo Ganttovu tabulku a kliknutím
:guilabel:`Nový“.
   - Následující pole lze také upravovat přímo z pohledu Kanban bez otevření
individuální úkol: :icon:`fa-star-o` (**důležitost**), :guilabel:`Čas přidělený na úkol`,
:guilabel:'Přiřazení', 'Stav úkolu' a také můžete úkoly barevně označit nebo :guilabel:'Nastavit
Klikněte na ikonu :icon:`fa-ellipsis-v` (vertikální elipsa) a přidejte obrázek.
   - Můžete používat následující klávesové zkratky v titulku úkolu k nastavení nových úkolů (upravit
hodnoty v příkladech níže podle vašich potřeb):

     - **30 hodin**: přidělit úkolu 30 hodin.
     - **#tagy**: přidat tagy k úkolu.
     - **@uživatel**: přidělit úkol uživateli.
     - **!**: zařadit úkol jako prioritu.

Kromě použití správného formátu postupujte podle následujícího pořadí: název úkolu, poté
vyhrazený čas, štítky, přiřazené osoby a pak priorita.

Například pokud chcete vytvořit úkol s názvem „Připravit workshop“, přidělte mu 5 hodin.
přidat štítek „Škola“, přiřadit ho Audrey a nastavit jeho prioritu na :guilabel:`Vysoká“.
následující název úkolu:Připravit workshop 5 hodin #škola @Audrey!

.. obrázek:: task_creation/task-shortcuts.png
:alt:Vytváření úkolů v Projectu pomocí klávesových zkratek.

... _vytváření úkolů/e-mailová adresa:

Vytváření úkolů z e-mailového aliasu
==================================

Tato funkce umožňuje automaticky vytvářet úkoly projektu, jakmile je e-mail doručen na
určený e-mail).

Pro nastavení otevřete aplikaci Projekt, pak klikněte na ikonu „vertikální tři tečky“ (guilabel:„vertikální
Ikona „Ellipsis“ vedle názvu požadovaného projektu. Vyberte „Nastavení“, pak otevřete
:guilabel:„Nastavení“ karta.

V poli „Vytvářet úkoly pomocí odeslání e-mailu“ zadejte následující hodnotu:

 - **Část alia před znakem @**: Zadejte název e-mailového alia, např. „kontakt“
„pomoc“, „práce“.
 - **Doména**: většinou je tato hodnota vyplněna automaticky podle vašeho :doc:`doménového jména

 - Přijímat e-maily od: upravte seznam zasilatelů, jejichž e-maily vytvoří úkoly v projektu.

.. obrázek: task_creation/email-configuration.png
:alt: Pohled na e-mailovou adresu, kterou si zvolíte v přehledu projektu v Odoo

Jakmile je nastaveno, můžete e-mailovou adresu vidět pod názvem vašeho projektu na ploše Kanban.

Když je e-mail odeslán na alias, e-mail se automaticky převede na úkol projektu.
Přihlášení do soutěže probíhá podle následujících pravidel:

- Zasílatel e-mailu je zobrazen v poli :guilabel:`Klient`.
- Téma e-mailu se zobrazuje v poli „Název úkolu“.
- Tělo e-mailu se zobrazuje v poli :guilabel:`Popis`.
- Veškerý obsah e-mailu je navíc zobrazen v chatu.
- Všichni příjemci e-mailu (To/Cc/Bcc), kteří jsou uživateli Odoo, jsou automaticky přidáni jako
**příznivci úkolu**.

Vytváření úkolů z webového formuláře
==================================

Pokud máte aplikaci Webové stránky nainstalovanou ve své databázi, můžete konfigurovat jakýkoli formulář na
webové stránky, které vyvolají vytvoření úkolů v projektu.

#Přejděte na stránku, kde chcete přidat formulář a vložte blok Form.

#Ve webovém editoru upravte následující pole:

   - :guilabel:`Akce“: vyberte „Vytvořit úkol“.
   - :guilabel:`Projekt“: vyberte projekt, do kterého chcete přidat nové úkoly.

#:ref:`Upravte formulář <webová stránka/bloky/formulář>.

Při odeslání formuláře se automaticky vytvoří úkol projektu. Obsah úkolu je definován
odpovídajícími poli formuláře.

.. viz též:
:ref:`Webové formuláře <web/bloky/formulář>`
