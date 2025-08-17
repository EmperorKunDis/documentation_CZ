Zobrazit obsah

======================
Bankovní a hotovostní účty
======================

Můžete spravovat takové množství bankovních nebo hotovostních účtů, kolik potřebujete na své databázi. Konfigurace je správná
umožňuje mít všechny své údaje o bankovním účtu vždy aktuální a připravené k :doc:`srovnání
S vašimi záznamy v účetnictví.

V účetnictví Odoo je každému běžnému účtu přiřazen vlastní deník, do kterého se zadávají všechny záznamy.
účet. Obě stránky jsou automaticky vytvořeny a nakonfigurovány, když přidáte
Bankovní účet.

.. poznámka::
Knihy jízd a účty musí být ručně nakonfigurovány.

Bankovní deníky jsou zobrazeny v účetním přehledu (viz :guilabel:`Accounting Dashboard`) ve formě karet.
s akčními tlačítky.

.. obrázek:bankovní_karta.png
:alt:Bankovní deníky jsou zobrazeny na účetním dashboardu a obsahují tlačítka pro akci

...účetnictví, banka, řízení:

Spravovat účty v bance a na peněžním trhu
=============================

Připojte banku pro automatické synchronizace
--------------------------------------------

Chcete-li propojit svůj účet s databází, přejděte na: „Účetnictví --> Konfigurace
--> Přidat bankovní účet“, vyberte svou banku v seznamu, klikněte na „Připojit“ a postupujte podle
návod.

.. viz též:
:doc:`banka/bankovní synchronizace“

...účetnictví/banka/vytvořit:

Založte si účet u banky
---------------------

Pokud není vaše bankovní instituce k dispozici v Odoo nebo pokud nechcete propojit svůj účet
účet do databáze, můžete si svůj bankovní účet nastavit ručně.

Chcete-li ručně přidat bankovní účet, přejděte na: „Účetnictví - Konfigurace - Přidat banku
Vyberte možnost „Záznam transakcí ručně“ (vpravo dole) a vyplňte banku.
informace a klikněte na tlačítko „Vytvořit“.

.. poznámka::
   - Odoo automaticky detekuje typ účtu (např. IBAN) a umožňuje některé funkce
V souladu s tímto rozhodnutím.
   - Výchozí bankovní deník je k dispozici a může být použit k nastavení vašeho bankovního účtu, pokud přejdete na
:menuselection:`Účetnictví --> Konfigurace --> Účetnictví: Knihy --> Banka“. Otevřete ji a
Upravte různé pole tak, aby odpovídaly informacím o vašem účtu.

Vytvořte hotovostní deník
---------------------

Pro vytvoření nového pokladního deníku přejděte na: „Účetnictví“ - „Konfigurace“ - „Účetnictví“.
Klikněte na tlačítko „Vytvořit“ a v poli „Typ“ vyberte možnost „Hotovost“.

Více informací o účetních polích najdete v
:ref:`účetnictví/banka/konfigurace` této stránky.

.. poznámka::
Výchozí deník hotovosti je k dispozici a lze jej ihned použít. Můžete si ho prohlédnout přes
:menu_selection:`Účetnictví --> Konfigurace --> Účetnictví: Knihy --> Hotovost“.

Upravit existující bankovní nebo hotovostní deník
-------------------------------------

Pro úpravu stávajícího bankovního deníku přejděte na: „Účetnictví -> Konfigurace -> Účetnictví“.
Vyberte si požadovaný časopis a klikněte na něj.

.. účetnictví, banka, konfigurace:

Konfigurace
=============

Můžete si upravit účetní informace a číslo bankovního účtu podle svých potřeb.

.. obrázek: bank/bank-journal-config.png
:alt:Manuálně si nastavte údaje o své bance

.. viz též:
   - :doc:`get_started/multi_currency“
   - :doc:`banka/transakce“
   - `Konfigurace banky <https://www.youtube.com/watch?v=tVhhXw-VnGE>`

...účetnictví / banka / pohledávka:

Spořicí účet
----------------

Transakce z výpisu bankovního účtu jsou uvedeny na účet nevyřešených transakcí, dokud nejsou vypořádány.
v daném okamžiku zůstatek účtu očekávaných transakcí v obecném účetnictví ukazuje
Dohody ještě nebyly uzavřeny.

.. poznámka::
Když je bankovní transakce vyrovnána, záznam v účetnictví se upraví tak, aby byla nahrazena bankovní rezerva
účet, ke kterému je zúčtováno vydání časopisu. Tento účet bývá obvykle
:ref:`výpisy nebo platby k účtu <účetnictví/banka/výpisy-platby-k-uctu>`,
vyrovnání s registrovaným platebním příkazem nebo účtem k přijetí nebo odeslání, pokud jde o
fakturu nebo účet přímo.

Výsledovky
------------------------

K zaznamenání zisku se používá účet „Zisk“.
registrace se liší od výpočtu systému.
zaznamenat ztrátu, pokud je konečný stav pokladny odlišný od výpočtu systému.

Měna
--------

Můžete upravit měnu, ve které jsou transakce zadávány.

.. viz též:
:doc:`jak-zacit/multi-mena`

.._účetnictví/banka/číslo účtu:

Číslo účtu
--------------

Pokud potřebujete upravit své bankovní údaje, klikněte na vnější odkaz vedle vašeho
:guilabel:Číslo účtu. Na stránce s účtem klikněte na externí odkaz vedle vašeho
:guilabel:Banka“ a aktualizujte své údaje o bance podle nich. Tyto informace se používají při
evidence plateb.

.. obrázek: banka/číslo účtu.png
:alt:Upravte své údaje o bance

Bankovní příspěvky
----------

:guilabel:`Příchozí platby“ definuje, jak se bankovní transakce zaznamenávají. Tři možnosti jsou
dostupné:

- „Není ještě určeno“, což by mělo být vybráno, pokud zatím nevíte, jestli budete
synchronizovat svůj účet s databází nebo ne.
- „Dodání (CAMT, CODA, CSV, OFX, QIF)“, který byste měli vybrat, pokud chcete importovat
vaše výpisy z účtu a transakce v jiném formátu.
- „Automatická synchronizace bankovního účtu“, která by měla být vybrána, pokud je váš bankovní účet synchronizován.
s vašimi daty.

.. viz též:
   - :doc:`bank/bank_synchronizace`
   - :doc:`banka/transakce“

...účetnictví/banka/pohledávky:

Nedoplatky
====================

Výchozí nastavení plateb v Odoo neobsahuje žádné účetní záznamy, ale lze je snadno nakonfigurovat tak, aby
vytvářet účetní záznamy pomocí **pohledávek**.

- Výjimečný účet příjmů je místo, kam se připisují všechny vstupy do té doby, než jsou spárované.
s příchozími platbami na účet.
- Účet nedoplatků je místo, kam se zadávají výdaje do té doby, než jsou spárovány.
s výstupy z účtu.

Tyto účty jsou obvykle typu :ref:`<chart-of-accounts/type>` :guilabel:`Použité aktiva“.
:guilabel:`Aktiva pohledávky“.

Příjmy, které jsou zaznamenány v Odoo, se přičítají na neuhrazené faktury a účty.
až do jejich vyrovnání. V každém okamžiku je zůstatek účtu vedeného jako nedoplatek na účtech
účetní kniha ukazuje zůstatek registrovaných příchozích plateb, které ještě nebyly vyrovnány.
zůstatek na účtu nedoplatku v účetnictví eviduje zůstatek registrovaných nedoplatků
výstupní platby, které ještě nebyly vyrovnány.

Konfigurace bankovního a hotovostního deníku
-----------------------------------

Pro konfiguraci plateb vytvořte účty pro nevyrovnané platby.
metod. Toto lze provést pro jakýkoliv časopis s typem :ref:`<číselník/typ>
:guilabel:Banka nebo :guilabel:Hotovost.

Pro konfiguraci zůstatků účtů pro platební metody časopisu nejprve přejděte na
Vyberte položku „Účetnictví“ -> „Konfigurace“ -> „Deníky“. Vyberte bankovní nebo hotovostní deník.
„Příchozí platby“ a „Odeslané platby“ a nastavte „Čekající platby“.
Pokladní knihy a účty neuhrazených faktur pro každý způsob platby, který používáte.
chci vytvářet zápisy.

.. poznámka::
   - Pokud je hlavní účet časopisu přidán jako zůstatek na účtu nebo
účet nedoplatků, když je zaevidován příkaz k úhradě, stav faktury nebo zálohové faktury se
přímo nastavit na :guilabel:`Placené“.
   - Pokud je v položce způsobu platby nevyplněno pole pro zůstatek nebo nedoplatek.
Při registraci platby s tímto způsobem platby nebude vytvořen žádný záznam v knize jízd.

..toctree::


banka/bankovní synchronizace
banka/transakce
bankovní/soulad
bankovní/srovnávací modely
banka/výběr z účtu
banka/cizí měna
banka/úvěr
