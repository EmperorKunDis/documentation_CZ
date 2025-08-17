==================
Vedoucí prodejních týmů
==================

Funkce „Prodejní týmy“ v aplikaci CRM společnosti Odoo umožňuje vytvářet a spravovat více
prodejní týmy s vlastními pravidly pro přidělování úkolů, cíli fakturace a seznamem obchodníků.

Vytvořte prodejní tým
===================

Pro vytvoření nového prodejního týmu přejděte na: „CRM aplikace - Konfigurace - Prodejní týmy“.
Klikněte na položku „Nový“.

Do prázdného pole týmu prodeje zadejte název v poli „Tým prodeje“.

Dále vyberte vedoucího týmu z roletky.

Nastavte alias e-mailu, který automaticky generuje vstupní bod pro tento obchodní tým.
Každou zprávu, která je odeslána na tuto unikátní e-mailovou adresu. Zvolte, jestli chcete přijímat e-maily
:guilabel:„Každý“, :guilabel:„Oprávnění partneři“, :guilabel:„Pouze sledující“ nebo
:guilabel:`Přihlášení zaměstnanci“.

Vyberte společnost z rozevírací nabídky, do které chcete tým přiřadit.

.. poznámka::
Pole „Společnost“ je viditelné pouze v databázích s více společnostmi a není povinné.

.. obrázek: manage_sales_teams/sales-team-creation.png
:align:center
:alt:Nastavení pro nový tým prodeje.

.. poznámka::
Pokud je aplikace Sales nainstalována na databázi, objeví se pole :guilabel:`Invoicing Target`.
tým prodeje. Jedná se o měsíční cíl obratu. Do této kolonky se zadává
Tento pole se používá k vyplnění průběhu fakturace v prodejním týmu na panelu nástrojů.
<crm/sales-team-dashboard>.

Přidejte členy prodejního týmu
----------------------

Chcete-li přidat členy týmu, klikněte na „Přidat“ pod záložkou „Členové“ při úpravě prodeje.
konfigurační stránka týmu. To otevře okno „Vytvoření členů prodejního týmu“.

.. poznámka::
Pokud funkce „Pravidla přiřazení“ nebyla na aplikaci CRM povolena,
stránka nastavení, kliknutím na tlačítko „Přidat“ pod záložkou „Členové“ se otevře
:guilabel:`Přidat: Prodejci“ okno. Zaškrtněte políčko vpravo dole
přidat dalšího prodejce do týmu, pak klikněte na „Vybrat“.

.... obrázek: manage_sales_teams/add-salespersons.png
:synchronizace: střed
:alt:Popis:Okno prodejců se objeví při vytváření nového týmu prodejců.

Vyberte uživatele z rozevírací nabídky :guilabel:`Salesperson`, abyste ho přidali do týmu.
tento obchodník automaticky přiřazené případy nechává bez povšimnutí.
zaškrtávací políčko. Pokud je tato funkce zapnutá, obchodník může být přiřazen k leadům ručně.

.. obrázek: manage_sales_teams/create-sales-team-members.png
:align:center
:alt:Okno pro vytvoření členů prodejního týmu.

Feld „Vedoucí (30 dní)“ sleduje, kolik vedoucích bylo prodejcům přiřazeno za posledních 30 dní.
za posledních třicet dní pro tento tým a maximální počet případů, které by měli být přiřazeni.
maximální počet příležitostí, které může být prodejci přiřazeno, zadejte tento počet do políčka :guilabel:`Příležitosti
„(30 dní)“ pole.

..tip:
:dokument: „Pravidla přiřazování bodů klientům“ lze pro jednotlivé klienty
prodejci, kteří používají sekci „Doména“.

Klikněte na tlačítko „Uložit a zavřít“ nebo „Uložit a nový člen“, pokud chcete přidat další členy.

Povolit více týmů
==================

Pro umožnění prodejcům přidělování více než jedné prodejní skupině je potřeba nastavit
musí být povolena. Nejprve přejděte do sekce „CRM aplikace“ -> „Konfigurace“ -> „Nastavení“.
V části „CRM“ zaškrtněte políčko označené „Multiteams“. Pak klikněte
:guilabel:`Uložit“ v horním levém rohu stránky.

.. obrázek: manage_sales_teams/enable-multi-teams.png
:align:center
:alt:Nastavení aplikace CRM s aktivním nastavením pro více týmů.

.._crm/sales-team-dashboard:

Dashboard pro obchodní tým
====================

Pro zobrazení panelu prodejního týmu přejděte na: „Aplikace CRM --> Prodej --> Týmy“.
uživatel je členem se zobrazuje v přehledu.

.. obrázek: manage_sales_teams/sales-teams-dashboard.png
:align:center
:alt:Dashboard prodejního týmu v aplikaci CRM.

Každá karta Kanban poskytuje přehled otevřených příležitostí prodejního týmu, nabídek, objednávek a
a očekávané příjmy, stejně jako graf s novými příležitostmi za týden a fakturaci.
Progresový proužek.

Klikněte na tlačítko „Pipeline“ a přejděte přímo do CRM pipeline daného týmu.

Klikněte na ikonu „fa-ellipsis-v“ v pravém horním rohu
Kartu Kanban pro otevření rozbalovací nabídky. Pak klikněte na tlačítko Zobrazit nebo Upravit nastavení týmu
:guilabel:`Konfigurace“.

.. viz též:
   - :doc:`../optimize/utilize_activities`
   - :doc:`../track_leads/lead_scoring`
