Zobrazit obsah

==============
Subdodavatelství
==============

.. |BoM| nahradit za: :abbr:`BoM (Seznam materiálů pro výrobu)“

Výrobní proces zahrnuje poddodavatelskou činnost, kdy společnost najímá třetí stranu na výrobu.
nebo poddodavatele k výrobě produktů, které jsou pak prodávány smluvní společností.

Subdodavatelství přináší mnoho výhod jak pro zadavatele, tak i pro dodavatele.
dodavatelé.

Pro zadavatele je poddodavatelská činnost možností, jak prodat širokou paletu vyrobených
produkty bez obav z investic do a údržby zařízení a pracovníků
byli nuceni sami se vyráběním zabývat.

Tímto způsobem se stávají dodavatelské společnosti pružnějšími v rámci hospodářských cyklů a mohou snadno reagovat na změny.
zvýšit nebo snížit své závazky vůči dodavatelům, jak je vyžadováno aktuální situací.
To také znamená, že se mohou soustředit na úkoly, ve kterých vynikají, a přenechat více specializované práci.
dodavatelům.

Na druhé straně vztahu umožňuje poddodavatelům specializovat se na více
nichové oblasti výroby, které mohou být mimo rámec poddodavatelství méně ziskové.
zapojení. V některých případech jim také poskytuje pružnost při výběru
projekty, které přijímají nebo odmítají, a kolik jich pracuje najednou.

V Odoo mohou společnosti konfigurovat své dodavatelské řetězce podle různých typů.
faktory včetně toho, jak jsou komponenty získávány a co se stane s hotovými výrobky po jejich vyrobení.
Vyráběné.

.. karty:

...... karta:: Základní poddodavatel
:target: poddodavatelství/poddodavatelství

Zadat poddodavatelům výrobu bez dodání komponentů.

...... karta: Dodavatel doplňkových služeb
:target: poddodavatelství/poddodavatelská re-výzbroj

Každou chvíli, kdy je potvrzeno objednávkové číslo pro poddodavatelský produkt, posílat díly na lodi k dodavateli.

...... karta::Dodání do poddodavatele
:target:dodavatelé/dodavatelé_drop-shipping

Každýkrát, když je objednávka na dodání dílu pro podřízeného dodavatele, posílejte díl
potvrdil.

Konfigurace
=============

Chcete-li umožnit poddodavatelskou činnost v Odoo, přejděte na: „Výroba --> Konfigurace
→Nastavení“, zaškrtněte políčko vedle „Dodavatelé“ v seznamu
Vyberte záložku „Operace“ a pak klikněte na „Uložit“.

.. obrázek: poddodavatel/poddodavatel-nastavení.png
:align:center
:alt:Nastavení poddodavatelů v aplikaci výroba.

S aktivovaným poddodavatelstvím se v Odoo objeví několik dalších funkcí:

- V poli „Druh BoM“ (BoM Type) je nově možnost „Subdodavatel“.
Povolení typu *Dodavatelské práce* označuje produkt BoM jako dodavatelskou práci.
produkt, který znamená, že Odoo ví, že je produkován dodavatelem, nikoli společností.
jehož databáze je v Odoo.
- V aplikaci Inventář se objeví dvě možnosti poddodavatelského řetězce a lze je přiřadit konkrétním
produkty na záložce „Sklad“ v jejich produktových stránkách:

  - Dodavatel doplňovacího materiálu na objednávku
  - *Dodavatel na objednávku pro dropshipping*

Práce s poddodavateli
========================

V Odoo existují tři způsoby řízení poddodavatelů, hlavní rozdíl mezi nimi je v tom, jakým způsobem se
Subdodavatel získá potřebné součástky:

- V základním postupu poddodavatelských prací je plně odpovědný za získání
komponenty. Tento postup je popsán v :doc:`subcontracting/subcontracting_basic`.
dokumentace.
- V procesu „Dodavatel náhradních dílů na objednávku“ pošle dodavatel smlouvy komponenty.
od svého skladu k poddodavateli. Tento proces je popsán v
:doc:`dodavatelé/dodavatelé_přebytku“ dokumentace.
- V procesu *Dodavatel na objednávku* nakupuje kontraktující společnost
komponenty od dodavatele a nechává je doručit přímo k poddodavateli. Tento postup je
podrobněji v dokumentaci :doc:`subcontracting/subcontracting_dropship`.

Kromě toho, jak dodavatel získává součástky, je také nutné zohlednit proč.
zda se výrobek poddodavatelsky vyrábí a co se s ním děje po jeho výrobě.
subdodavatel.

Z hlediska důvodu proč je zakázka předávána na dodavatele existují dvě hlavní příčiny.
objednávku nebo doplnit zásoby skladem.

Co se týče toho, co se s výrobky stane poté, co jsou vyrobeny, buď je lze poslat na
dodavatelskou společnost nebo přímo konečnému zákazníkovi.

Každý z tří pracovních postupů poddodavatelského řetězce popsaných výše lze nakonfigurovat tak, aby usnadňoval jakoukoli
Tyto možnosti a způsoby jejich provedení jsou popsány v příslušných dokumentech.

Oceňování dodaného zboží
===============================

Hodnota poddodavatelského produktu závisí na několika různých proměnných:

- Náklady na požadované součástky, pokud je dodává zhotovitel; dále jen
to jako „C“.
- Cena za službu výroby podsoučástky, kterou si objednatel nechává vyrábět u poddodavatele.
zde dále jen „M“.
- Náklady na dopravu součástek k dodavateli a zpět do
smluvní společnost, dále jen „S“.
- Náklady na přepravu zboží, pokud jsou komponenty dodány konečnému zákazníkovi od dodavatele.
odkazované jako „D“.
- Jakékoliv další náklady spojené s dovozem (např. cla), které označíme jako „x“.

Proto celková hodnota poddodavatelského produktu („P“) může být vyjádřena následující rovnicí
výraz:

.. matematika::
P = C + M + S + D + x

Je důležité poznamenat, že ne každá externě prováděná ocenění produktu zahrnuje všechny tyto
proměnných. Například pokud se produkt nezasílá přímo zákazníkovi, pak není potřeba
zahrnout náklady na zásilkový prodej.

.. toctree::

dodavatelé/dodavatelé_základní
dodavatelé/základní dodací lhůty
poddodavatelství/přebírání dodavatele
poddodavatelé/dodavatelé materiálu - čas dodání
dodavatelé/dodavatelé_drop-shipping
dodavatelé/dodací lhůty
