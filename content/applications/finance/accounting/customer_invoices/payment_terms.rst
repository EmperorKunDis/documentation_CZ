===================================
Platební podmínky a splátkový kalendář
===================================

Podmínky platby definují všechny podmínky pro úhradu nákupu, aby se zajistilo, že zákazníci zaplatí své
faktury správně a včas.

Platební podmínky jsou obecně stanoveny na dokumentech jako objednávkách prodeje, fakturách zákazníkům a
faktury dodavatelů. Podmínky platby zahrnují:

- Termín splatnosti
- Sleva za předčasné splacení
- Jiné podmínky platby

Instalatérské splátky umožňují zákazníkům platit faktury v částkách a
datum splatnosti, které si určil prodávající.

.. příklad::
Okamžitá platba
Platba je splatná v den vystavení faktury.
15 dní (nebo Net 15)
Celá částka je splatná do 15 dnů od data faktury.
21 MFI
Celá částka je splatná do 21. dne následujícího měsíce po datu faktury.
30 % dopředu konec následujícího měsíce
30 % splatného dne vystavení faktury, zbývající částka je splatná na konci období.
následující měsíc.
2 % 10, NET 30 EOM
Sleva ve výši 2 % v případě, že platba proběhne do deseti dnů od data faktury.
V opačném případě je splatná celá částka v měsíci následujícím po datu faktury.

.. poznámka::
   - Platební podmínky nesmí být zaměňovány s fakturami na zálohu.
</objednavky/prodej/fakturace/doplněk/>. Pokud pro konkrétní objednávku vystavíte
vystavit zákazníkovi více faktur, které nejsou splatností ani splátkovým kalendářem.
politiku fakturace.
   - Tato stránka je o funkci „Platební podmínky“, nikoliv o :doc:`podmínkách a pravidlech
<terms_conditions>, které lze použít k vyjádření smluvních povinností týkajících se obsahu.
používání, vracení zboží a další politiky týkající se prodeje zboží a služeb.

.. viz též:
   - „Odoo Tutorials: platební podmínky <https://www.odoo.com/slides/slide/payment-terms-1679>“
   - :doc:`cash_discounts“

.. účetnictví, platební podmínky, konfigurace:

Konfigurace
=============

Pro vytvoření nových platebních podmínek postupujte takto:

#Přejděte na „Účetnictví -> Konfigurace -> Podmínky platby“ a klikněte na
:guilabel:`Nový“.
#Zadejte název do pole „Platební podmínky“. Tento název se zobrazí jak v platebních podmínkách, tak
vnitřně a na objednávkách prodeje.
#Zatrhněte políčko „Sleva v předstihu“ a vyplňte procento slevy, počet dní slevy.
a pole „daňová sazba“ a „sleva za platbu v hotovosti“, abyste mohli přidat :doc:`slevu za platbu v hotovosti
, pokud je to možné.
#V části „Povinnosti“ v seznamu guilabel:Due Terms přidejte sadu pravidel (podmínek), které definují, co má být zaplaceno.
a které splatnost. Při definování termínu se automaticky vypočítá datum splatnosti.
je zvláště užitečná pro správu splátkových kalendářů (:dfn:`splátkových kalendářů s více splátkami).
termíny.

Chcete-li přidat nový řádek, klikněte na tlačítko „Přidat řádek“, zadejte hodnotu slevy a napište
:guilabel:`Datum splatnosti“ políčka, pak vyplňte pole „Po“ k určení data splatnosti.

.......
Volba „Konec měsíce“ v nabídce :guilabel:`Dny na konci měsíce` umožňuje přidat do kalendáře
</účetnictví/platba/rezerva> tak, aby faktura vystavená na konci měsíce nebyla
splatná v prvním dni následujícího měsíce.

#Zadejte text, který se má zobrazit na dokumentu (faktura, prodejní objednávka atd.) do šedého políčka.
v sloupci „Náhled“.
#Zatrhněte políčko „Zobrazit datum splatnosti“ a zobrazí se přehled každé platby.
jeho splatnost na faktuře, pokud si přejete.

.. tip::
Místo toho zadejte počet dní před koncem měsíce, použijte k tomu zápornou hodnotu.
:guilabel:`Po“ pole.

Pro ověření, že jsou nastaveny správně platební podmínky, zadejte datum faktury.
:guilabel:'Příklad' řádek, který generuje platby, které jsou splatné a jejich splatnost
s těmito platebními podmínkami.

.. důležité::
Termíny jsou vypočítávány v pořadí jejich splatnosti.

.. příklad::
V následujícím příkladu je splatná třicetiprocentní částka v den vydání a zbývajících sedmdesát procent pak o dva měsíce později.
konci následujícího měsíce.

.. obrázek: platebni_podminky/konfigurace.png
:alt: Příklad platebních podmínek. První řádek je 30 % hned, druhý řádek
zbylých 70 % do konce následujícího měsíce.

.. účetnictví, platební podmínky, rezerva:

Záloha na konec měsíce
-----------------------

Možnost „Konec měsíce“ v poli „Dny“ umožňuje uživatelům přidat rezervu, aby se vyhnuli
faktura vystavená na konci měsíce není splatná na začátku následujícího měsíce.
Pokračuje.

Při použití této možnosti vypočítává Odoo datum splatnosti na základě data faktury a přičte celé číslo
Do pole „Po“ se dostaneme na konec vzniklého měsíce a pak přičteme celé číslo
z pole „Dny v následujícím měsíci“.

.. příklad::
Příkladem mohou být dva faktury, jedna datovaná 5. března a druhá datovaná 28. března. Oba používají stejný
splatnost s jedinou řádkou „Termín splatnosti“ pro 100 % dlužné částky, splatná „5“.
:guilabel:`Konec měsíce na 1. den v měsíci.`

Pro fakturu ze dne 5. března je termín splatnosti stanoven na **1. duben** s následujícím
výpočty:

   - 5. března + 5 dní = 10. března
   - 10. březen + konec měsíce = 31. březen
   - 31. března + 1. dubna = 1. duben


Pro fakturu ze dne 28. března je termín splatnosti stanoven na **1. května** s tím, že
výpočty:

   - 28. března + 5 dní = 2. duben
   - 2. duben + konec měsíce = 30. duben
   - 30. dubna + 1. května = 1. května

.. účetnictví/splatnost/použití:

Použitím platebních podmínek
===================

Termíny splatnosti lze definovat pomocí pole „Platební podmínky“ v:

- Kontakty: Chcete-li automaticky nastavit výchozí platební podmínky pro nové objednávky kontaktu
fakturami a fakturami. Toto lze upravit v kontaktním formuláři pod záložkou:
Koupit
- **Údaje o cenách a objednávky:** Chcete-li automaticky nastavit konkrétní platební podmínky na všech fakturách vystavených.
z citační nebo objednávky na prodej.

Podmínky platby lze definovat pomocí pole „Datum splatnosti“ s parametrem „Období“.
seznam s možností výběru:

- **Faktury zákazníkům:** Uzavření smlouvy o konkrétních platebních podmínkách na faktuře.
- **Faktura dodavatele:** Uzpůsobit platbu na faktuře.

.. tip::
Zadávání platebních podmínek na faktuře dodavatele je většinou užitečné pro správu platebních podmínek
předem nebo slevou z kupní ceny. Jinak postačí ruční nastavení **splatnosti**.
Vyplňte pole pro výběr data.

...účetnictví/splatnost faktur/účetní záznamy

Deník
===============

Faktury s konkrétními platebními podmínkami vyvolávají jiné účetní zápisy, přičemž každý z nich má svůj vlastní účetní záznam.
za každý vypočtený termín splatnosti.

To usnadňuje :doc:`další kroky </aplikace/finance/účetnictví/platby/dalsi_kroky>“.
:odkaz:rekonciliace odoo-banku-reconciliation
datum splatnosti, nikoli jen datum splatnosti zůstatku. Pomáhá také k přesnému
:ref:`účetní závazek v souvislosti s věkem faktury <účetnictví/fakturace/věk faktur>“.

.. příklad::
.... obrázek: platební podmínky/účetní záznam.png
:alt: Výše účtované částky na účet pohledávek je rozdělena do dvou položek v knize jízd.
odlišné termíny splatnosti

V tomto příkladu byla vystavena faktura ve výši 1000 USD s následujícími platebními podmínkami: *30 % je
za den vydání a zbývajících 70 % je splatných na konci následujícího měsíce.

   +----------------------+-------------+---------+---------+
|Účet                 |Termín splatnosti|Debet     |Kredit   |
   +======================+=============+=========+=========+
|Závazky vůči příjemcům|21. února|300     |         |
   +----------------------+-------------+---------+---------+
| Závazky vůči příjemcům  | k 31. březnu  | 700     |         |
   +----------------------+-------------+---------+---------+
|Prodej produktů       |             |         |  1000   |
   +----------------------+-------------+---------+---------+

1 000 dolarů odečtených z účtu pohledávek je rozděleno do dvou samostatných položek v knize jízd.
Tyto úkoly mají své vlastní termíny splnění.
