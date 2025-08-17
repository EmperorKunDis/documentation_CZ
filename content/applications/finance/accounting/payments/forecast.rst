============================
Předvídejte budoucí faktury za služby
============================

V Odoo můžete spravovat platby nastavením automatických podmínek pro platby a sledování plateb.

Konfigurace: platební podmínky
============================

Pro sledování podmínek dodavatelů používáme v Odoo **Platební termíny**. Umožňují sledovat
termíny splatnosti na fakturách. Příklady **Platebních podmínek** jsou:

-  50 % do 30 dnů
-  50 % do 45 dnů

Pro vytvoření jich vyberte v menu: „Účetnictví“ – „Konfigurace“ – „Daňové doklady: Dodací podmínky“.
Klikněte na tlačítko „Vytvořit“ pro přidání nových termínů nebo klikněte na existující, abyste je upravili.

.. viz též:
„Návody k Odoo: Fakturace


Jakmile jsou definovány platební podmínky, můžete je přiřadit k dodavateli výchozí hodnotou. Chcete-li tak učinit, přejděte na
:menu „Dodavatelé“ -> „Dodavatelé“, vyberte dodavatele, klikněte na záložku „Prodej a nákup“.
a vyberte konkrétní platební podmínky. Tímto způsobem při každé objednávce u tohoto dodavatele budete moci používat Odoo
automaticky navrhne zvolený termín platby.

.. poznámka::
Pokud na dodavatele nespecifikujete konkrétní platební podmínky, můžete je nastavit v faktuře od dodavatele.

Předpověď faktur, které je třeba zaplatit s vyúčtováním pohledávek
==================================================

Pro sledování částek, které mají být zaplaceny dodavatelům, použijte zprávu **Zaškrtnuté faktury**. Získat ji můžete kliknutím na
:menuselection:`Účetnictví --> Zprávy --> Hlášení partnerům: Dlužná částka“ Tento report vám dává
Shrnutí částky k zaplacení podle dodavatele v porovnání s jejich splatností (splatnost vypočítána
(včetně každé faktury s těmito termíny). Tento dokument vám řekne, kolik budete muset zaplatit do
měsíců.

Vyberte faktury, které chcete zaplatit
===================

Seznam všech faktur od dodavatelů získáte kliknutím na: „Dodavatelé - Faktury“.
pouze faktury, které je třeba zaplatit, klikněte na: menu „Filtry“ - „Faktury k úhradě“.
pozdržené platby, vyberte filtr „Pozdržení“.

Můžete také skupit faktury podle data splatnosti kliknutím na:menuselection:Skupit podle --> Datum splatnosti
Vyberte časový úsek.
