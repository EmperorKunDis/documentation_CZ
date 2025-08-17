.._plm/eko/ekotyp:

.. |BOM| nahradit za: :abbr:`BOM (Seznam materiálů pro výrobu)“
.. |BOM| nahradí::: zkratka: `BoM (Bill of Materials)`
.. |ECO| nahradit za: zkratku: `ECO (Engineering Change Order)`
.. |ECN| nahrazuje: zkratka: `ECN (Engineering Change Notices)`

====================
Ekologické typy a fáze
====================

Inženýrské změny objednávek (ECO) jsou kategorizovány podle typu změn, které reprezentují.
Stavy jsou sledovány pomocí etap. Typy i fáze definuje uživatel a mohou být
Zaměřené na specifické potřeby podnikání nebo odvětví.

EKO typy
=========

Každý typ |ECO| odděluje |ECOs| do různých projektů v přehledu PLM, což zajišťuje
Spolupracovníci a zainteresované strany vidí pouze a pomáhají s relevantními úpravami BOM.

Příklad:
Společnost zabývající se výrobou elektronických čipů používá pět typů ECO: „Zavedení nového produktu“, „Aktualizace BOM“ a
„Změna komponenty“, „Vylepšení produktu“ a „Aktualizace firmwaru“.
Inženýři mohou trávit čas výhradně na |ECOs| v rámci změn komponent a aktualizací firmwaru.
typy, zatímco návrháři vidí ECO v typu „New Product Introduction“, který umožňuje každému
disciplína se soustředit pouze na změny, které vyžadují jejich odborné znalosti.

.. obrázek: eco_type/eco-type-example.png
:alt: Příklad několika vlastních typů ECO.

Vytvořte typ ECO
------------------

Pro přístup a správu typů ECO se přihlaste do aplikace PLM: „PLM app --> Konfigurace --> ECO
Typy.

Vytvořte nový typ ekologického chování kliknutím na „Nový“. V novém okně „Typy ekologického chování“ vyplňte
následující informace:

- :guilabel:`Název`: název typu |ECO|, který bude organizovat všechny |ECOs| tohoto typu
v projektu.
- :guilabel:`E-mailová adresa aliasu“: pokud je tento nepovinný prvek vyplněn, e-maily zaslané na tuto e-mailovou adresu
automaticky generovat |ECOs| v nejlevnějším stupni této |ECO|.

Příklad:
Typ Formulace změny (ECO) se používá k organizování a sledování souvisejících ECO v jednom
Projekt. Konfigurace pole „E-mailová adresa“ generuje |ECOs| v poli Formulace
změna projektu zaslaná na e-mailovou adresu „pawlish-change@pawlished-glam.odoo.com“.

....... obrázek: eco_type/create-eco-type.png
:alt: Příklad typu ECO.

Upravit typy ECO
--------------

Upravte stávající názvy typů a e-mailové aliasy tím, že se přesunete do aplikace PLM na:
Konfigurace --> stránka „Typy ECO“. Tam klikněte na požadovaný typ z nabídky.

V poli pro každý typ ECO upravte pole „Jméno“ nebo „Alias e-mailu“.

.._plm/eco/stage-config:

Stáže
======

V rámci kanbanového pohledu na změny v konstrukci pro konkrétní typ ECO jsou fáze
milníky používané k identifikaci pokroku v rámci projektu ECO před tím, než budou změny připraveny k aplikaci.
Výchozí nastavení je „Nový“, „Ve výrobě“, „Schválené“ a „Platné“, ale tyto můžete změnit.
Přizpůsobitelný specifickému životnímu cyklu typu ECO.

.. obrázek: eco_type/eco-stage-defaults.png
:alt: Výchozí fáze pro typ ECO.

.. poznámka::
„Účinné“ je v základním nastavení složeno, aby se nezobrazovaly všechny konkrétní |ECO|, které byly do hry zapojeny.
účinek. Podrobnější informace o této konfiguraci naleznete v kapitole :ref:`Zavírací fáze <plm/eco/closing-stage>`.

:ref:`Kontrolní fáze <plm/eco/verification-stage>` vyžadují schválení určitým uživatelem.
zajistit, aby se změny neprovozovaly, dokud nebyly přezkoumány změny ECO.
zúčastněné strany. :ref:`Koncovým fázím<plm/eco/final-phase> lze aplikovat změny vložené do |BOM| a
operace se mění okamžitě a změní všechny nevyřízené a budoucí :abbr:`MO (Manufacturing
objednávky) na nejnovější verzi BOM.

..tip:
Nejčastější praxí je mít alespoň jednu fázi ověření, která je fází s
požadovaný schvalovatel a jednu konečnou fázi, která uchovává ECOs, které byly buď zrušeny
nebo schválené pro použití jako další výrobní |BOM|.

.. viz též:
:doc:`Schválení<../management/approvals>`

..._plm/eco/verification-stage:

Stupně ověření
-------------------

Konfigurace ověřovacího kroku spočívá v tom, že se přesunete na požadovaný krok a vyberete ikonu „nástroje“
Klikněte na „Upravit“ v okně „Akce“. Poté se zobrazí okno s možnostmi. Zatrhněte políčko u
:guilabel:`Povolit aplikaci změn“.

Poté přidejte schvalovatele v sekci :guilabel:`Schvalovatelé`, kliknutím na :guilabel:`Přidat řádek“
Určení role recenzenta, uživatele a schválení.
Typ:guilabel: je vyžadován k schválení. Podrobnější informace o typech schválení naleznete v odkazu:
<plm/schválení/druh schválení>

Osoba uvedená jako schvalovatel je automaticky upozorněna, když jsou ECOs vypuštěny na úrovni specifikované v
plovoucí okno. Jakmile budete hotovi, klikněte na tlačítko „Uložit a zavřít“.

.. viz též:
:doc:`../správa/schválení`

.._plm/eko/konec

Konečné fáze
--------------

Klikněte na typ |ECO| z nabídky: „Aplikace PLM –> Přehled“ a otevřete seznam |ECOs|
tento typ.

Pro konfiguraci uzavírací fáze, která se vztahuje na BOM, upravte fázi a zaškrtněte políčka pro
„Složený v kanbanovém pohledu“, „Povolit aplikaci změn“ a „Konečná fáze“.
Když jsou karty ECO umístěny v stupni, který umožňuje aplikovat změny, pak jakékoli
Změny operací, které byly schváleny v ECO, budou okamžitě zavedeny.
zrušená fáze, vytvoření nebo upravení fáze a zaškrtnutí políček pro:guilabel:Sbaleno ve zobrazení Kanban
:guilabel:`Konečná fáze“. ECO v této fázi jsou odstraněny z potrubí, ale nebudou mít žádný vliv na
změny.

Příklad:
Konečná fáze „Účinné“ je konfigurována pomocí kontroly položky „Složené v kartách“,
:guilabel:`Povolit aplikaci změn“ a „Konečný stav“

.... obrázek: eco_type/uzavření.png
:alt: Konfigurace uzavírací fáze.
