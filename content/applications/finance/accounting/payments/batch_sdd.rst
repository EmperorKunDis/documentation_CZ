=========================================
Platby zákazníků v rámci SDD
=========================================

.. |sdd| nahradit za: abbr: SDD (SEPA Direct Debit)

SEPA (Single Euro Payments Area) je iniciativa Evropské unie pro integraci plateb,
usnadňuje standardizované a zjednodušené elektronické platby v eurech mezi zapojenými zeměmi.
S SEPA Direct Debit (SDD) zákazníci podepisují plnou moc, která jim umožňuje, aby v budoucnu
převody z jejich bankovních účtů. To je zejména u pravidelných plateb, které jsou založeny na
:dokument: „Předplatné </aplikace/prodej/předplatné>“.

V Odoo můžete evidovat příkazy zákazníků a vytvářet soubory XML s informacemi o platbách.
Sbírané s mandáty. :ref:`Nahrání těchto souborů do banky <účetnictví/převod_sdd/XML>`
Vybízí je, aby tyto platby vybírali od vašich zákazníků.

.. poznámka::
   - Služba |sdd| je podporována všemi zeměmi SEPA, což zahrnuje i 27 členských států Evropské unie.
Unie i další země.
   - Seznam všech zemí SEPA
<https://www.europeanpaymentscouncil.eu/dokumenty/jiné/seznam zemí SEPA podle EPC>.

.. /účetnictví/položka sdd/sepa-konfigurace:

Konfigurace
=============

Identifikátor věřitele
-------------------

Pro zpracování plateb zákazníků je nutné v nastavení:
Nastavení“, posuňte se do části „Platby zákazníků“ a zapněte „Souhlas s inkasem SEPA“.
(SDD) a klikněte na tlačítko „Uložit“. Pak se přesuňte do části „Platby zákazníků“
Nastavte identifikátor věřitele společnosti, klikněte na „Uložit“.

.. tip::
Identifikátor věřitele vám poskytne buď vaše banka, nebo příslušný orgán.
jejich vydání ve vaší zemi. Pro účely testování můžete použít identifikátor poskytovatele testovacího kreditu
„DE98ZZZ0999999999“.

Verze souboru PAIN
-----------------

Výchozí nastavení je SEPA-kompatibilní soubor XML vytvořený aplikací Odoo
použijte formát **PAIN.008.001.02**. Pokud váš bankovní účet vyžaduje aktualizaci v roce 2023
verzi, přejděte na: „Účetnictví“ - „Konfigurace“ - „Deníky“. Vyberte
„Banka“ a pak v záložce „Příchozí platby“ nastavte „SEPA“.
Hodnotu pole „bolest“ nastavte na: guilabel:Aktualizováno v roce 2023 (pouze Pain 008.001.08)“.

.. viz též:
`SEPA Direct Debit Core Customer-to-PSP Implementation Guidelines
<https://www.europeanpaymentscouncil.eu/document-library/implementation-guidelines/sepa-direct-debit-core-customer-psp-implementation-0>.

.. účetnictví/balíček SDD/SDD pověření:

Příkaz k inkasu SEPA
==========================

Smlouva o |sdd| pověření je právní dokument, který uděluje společnosti oprávnění k inkasu peněz z účtu zákazníka.
účtu. Obsahuje klíčové informace, jako je jméno zákazníka a IBAN, datum zahájení
a datem ukončení a jedinečným identifikátorem mandátu. Mandát musí být vyplněný a podepsaný
zákazník.

Vytváření pověření
-----------------

Vytvořit pověření:

#Přejděte na: menu „Účetnictví“ – „Zákazníci“ – „Souhlasy k inkasu“.
#Klikněte na tlačítko „Nový“ a vyplňte pole.
#Klikněte na tlačítko „Odeslat a vytisknout“ (nebo upravte e-mail), klikněte na tlačítko „Odeslat a vytisknout“.
formulář oprávnění odeslat zákazníkovi k podpisu.
#Klikněte na tlačítko „Potvrdit“.

.. důležité::
Platný IBAN musí být definován v poli „Číslo účtu“ ve formuláři bankovního deníku.
„Banka“ obdržela platby za mandát prostřednictvím účtu „sdd“.

.. tip::
   - Po ověření mandátu klikněte na ikonku „fa-cog“
pak vyberte ikonu „Převodovka“ a poté zvolte „Formulář pověření“.
   - Schéma SDD závisí na typu zákazníka: Vyberte „CORE“ pro B2C
zákazníky a pro firmy v rámci B2B.
   - Příkazy k platbě v režimu SDD jsou automaticky vytvářeny pro:
<../../platební_prostředky/sdd>.

Jakmile je aktivní mandát |sdd|, dalších |sdd| plateb lze vygenerovat prostřednictvím Odoo a
:ref:`na váš internetový bankovní účet <účetnictví/balíček SDD/XML>“. Klienti s
Aktivní platební pověření může také používat tento způsob platby pro online nákupy.
<../../platební_prostředky/sdd>.

... /účetnictví/záloha/zavřít a zrušit pověření:

Zrušení nebo zánik mandátu
-----------------------------

Povinnosti s datem ukončení jsou automaticky uzavřeny po jejich :guilabel:`Datum ukončení`. Pokud je
Pokud je účet neaktivní, pověření zůstává aktivní až do jeho uzavření nebo odvolání.
Přejděte na: „Účetnictví > Zákazníci > Příkaz k inkasu“ a vyberte příslušný.
pověření a klikněte na „Zavřít“ nebo „Odebrat“.

Zavření mandátu aktualizuje den ukončení mandátu na dnešní datum. Faktury vystavené po
dnešní platba nebude zpracována s |sdd|. **Zrušení pověření** zakáže
okamžitě. Žádný záznam o platbě již není možný, ať už se jedná o fakturu
datum. Přesto se do příštího SDD započítávají i platby již zaregistrované.
Soubor XML „<účetnictví/pracovní skupina SDD/XML>“.

.. varování:
   - Mandáty jsou automaticky uzavřeny po uplynutí 36 měsíců od data posledního shromažďování.
   - Zrušené nebo pozastavené mandáty nelze obnovit.

...účetnictví/soubor/XML:

Zpracování platebních příkazů
=========================

Všechny registrované platby lze zpracovat najednou nahráním souboru XML, který obsahuje hromadný příkaz
všech plateb odeslaných přes internetové bankovnictví. Postupujte takto:

#Vytvořte platební příkaz (Účetnictví > Platební příkazy > Vytvoření) a přidejte do něj platby |sdd|.
shromažďovat.

.......
Můžete filtrovat platby podle schématu SDD pomocí :guilabel:`SDD CORE` a :guilabel:`SDD B2B`
filtry.

#.:validace platby v hromadné platbě. XML soubor je vygenerován automaticky a k dispozici
pro stažení do chatu.
#Stáhněte si soubor XML a nahrajte jej do rozhraní internetového bankovnictví, abyste mohli platby zpracovat.
#Jakmile je přijata platba v jedné částce, transakci :doc:`vypořádejte.
<../bank/souhrnné-platby> s platbou v hromadné platbě, která označí související faktury.
:guilabel:`Placené“.

.. tip::
   - Pro zobrazení plateb a faktur spojených s konkrétním |sdd|mandátem klikněte na
:guilabel:`Sbírky“ a :guilabel:`Zaplacené faktury“ chytrý tlačítko na :ref:`Příkaz k inkasu
Formulář „Pověření“ (viz účetnictví/položka sestavy/sestava pověření).
   - Klikněte na tlačítko „Znovu vygenerovat exportní soubor“ pro znovunaplnění XML souboru.

.. viz též:
   - :doc:`batch“
   - :doc:`SEPA Direct Debit pro online platby <../../payment_providers/sdd>`
   - Pokyny SEPA


|sdd| odmítnutí
================

Nejčastějšími důvody odmítnutí jsou nedostatek prostředků na účtu
účet příjemce. S |sdd| jsou peníze připsány na účet příjemce ještě předtím, než se skutečně převedou.
od zákazníka na účet obchodníka. Pokud je později platba zamítnuta,
automaticky strhne z účtu příjemce částku této platby a novou
Transakce s negativním zůstatkem je vytvořena, aby odrážela |sdd| zamítnutí.

Pokud jde o odmítnuté transakce, tak se s nimi zachází různě podle toho, zda jsou účty vedeny:
Zda jsou konfigurovány nebo ne pro platební metodu |sdd|.

.. poznámka::
Následující postupy předpokládají, že bankovní transakce příchozího |sdd| platebního příkazu již proběhla.
bylo vyrovnáno s platbami nebo fakturami.

.. záložky::

.. tab::Bez nedoplatků

Pokud nejsou nastaveny žádné nevyplacené faktury (viz účetnictví, banka, nevyplacené faktury).
platba metodou |sdd|, v takovém případě se nezadává žádný účetní záznam a je nutné transakci zrušit.
nevyrovnat platbu.

      #Přejděte do faktury spojené s odmítnutou platbou.
      #Klikněte na tlačítko „Platby“ v levém sloupci, abyste se dostali k platbě spojené s
faktura.
      #Klikněte na tlačítko „Přepnout zpět do režimu návrhu“, pak na „Zrušit“.
      #Zpět k faktuře a na ikonku „i“ (informace)
v záhlaví karty „Splátkové řádky“ pak stiskněte tlačítko „Nedoplatit“.
      #:ref:`Přejděte na stránku s výpisem z účtu v aplikaci Bankovní deník <účetnictví/vypořádání/přístup>“
:ref:`srovnat <účetnictví/srovnání/srovnat> transakci vytvořenou pro
|sdd| zamítnutí s účetním záporným příjmovým dokladem na účet pohledávky.
příchozí bankovní transakce.

... tab::Využití nedoplatku

Pokud je na účtu nastavená neuhrazená položka, pak se zobrazí jako:
způsob platby, |sdd| platba vytvoří záznamy v knize jízd. Pokud je platba |sdd| zamítnuta,
musí zrušit záznamy v účetní knize spojené s odmítnutou platbou a vyrovnat se zrušením.
záznamu v účetní knize s transakcí pro odmítnutí |sdd|.
kroky:

      #Přejděte do faktury spojené s odmítnutou platbou.
      #Klikněte na ikonu „Informace“ v zápatí.
:guilabel:`Záložka Fakturační řádky“ a pak klikněte na „Zobrazit“, abyste se dostali k platbě spojené s tímto dokladem.
S fakturou.
      #Klikněte na tlačítko „Záznam v deníku“ pro přístup k souvisejícímu záznamu v deníku.
      #Klikněte na tlačítko „Obratný vstup“, případně upravte pole ve vyskakovacím okně, a pak klikněte
:guilabel:`Zpětný odkaz“. Zpětný odkaz vytvoříte s :guilabel:`Poznámkou“ s odkazem
vstupní záznam. Výsledkem je označení faktury jako „neuhrazené“.
      #:ref:`Přejděte na stránku s výpisem z účtu v aplikaci Bankovní deník <účetnictví/vypořádání/přístup>“
:ref:`srovnat <účetnictví/srovnání/srovnat> transakci vytvořenou pro
|sdd| zamítnutí s obratem v případě platby.
