Zobrazit obsah

===============
Online platby
===============

..toctree::


payment_providers/bankovní převod
payment_providers/sdd
payment_providers/adyen
payment_providers/amazon_payment_services
payment_providers/asiapay
payment_providers/authorize
payment_providers/buckaroo
payment_providers/demo
payment_providers/flutterwave
payment_providers/mercado_pago
payment_providers/mollie
payment_providers/nuvei
payment_providers/paypal
payment_providers/razorpay
payment_providers/stripe
payment_providers/worldline
payment_providers/xendit

Odoo obsahuje několik **platebních poskytovatelů**, které umožňují vašim zákazníkům platit online.
*zákaznická centra*, nebo na vašem *e-shopu*. Mohou platit objednávky, faktury, nebo
Předplatné s opakovanými platbami pomocí jejich oblíbených platebních metod, jako jsou
Kreditní karty.

Každý poskytovatel plateb je spojen s seznamem podporovaných :ref:`platebních metod
Platebních metod, které můžete aktivovat nebo deaktivovat podle svých potřeb.

.. obrázek: platby/onlinni-platebni-metody.png
:alt: Formulář pro online platbu

.. poznámka::
Odoo aplikace předávají zpracování citlivých informací certifikovanému poskytovateli plateb.
že se nemusíte nikdy obávat, že byste nebyli v souladu s předpisy PCI. Žádné citlivé informace (např. údaje o kreditní kartě)
karty) jsou uloženy na serverech nebo databázích Odoo hostovaných jinde. Namísto toho aplikace Odoo
Používat pro uložená data v systémech poskytovatelů plateb unikátní referenční číslo.

.. platby/podporované poskytovatele plateb:

Podporované způsoby platby
===========================

Pro přístup k podporovaným způsobům platby přejděte na: „Účetnictví“ -> „Konfigurace“ ->
Poskytovatelé platebních služeb, volba v menu: Webová stránka - Konfigurace - Poskytovatelé platebních služeb.
:menuselection:`Prodej -> Konfigurace -> Platební poskytovatelé“.

.. platby / online platby:

Online platební poskytovatelé
------------------------

.. seznam tabulkový::
:hlavičkové řádky: 1
:prázdné sloupky: 1
:šířky: auto

   * -
     - Platební tok od
     - :ref:`Tokenizace <platební_prostředky/tokenizace>`
     - :ref:`Manuální skenování <payment_providers/manual_scan>`
     - :ref:`Vrácení peněz <platební_prostředky/vraceni_penez>`
     - :ref:`Rychlý nákup <platební metody/rychlý nákup>`
   * :-: `Adyen <platební_providers/adyen>`
     - Odoo
     - |V|
     - Úplné a částečné
     - Úplné a částečné
     -
   * -- :doc:`Amazon Payment Services <payment_providers/amazon_payment_services>`
     - Webové stránky poskytovatele
     -
     -
     -
     -
   * „:doc:`AsiaPay <platební_prostředky/asiapay>“
     - Webové stránky poskytovatele
     -
     -
     -
     -
   * –:doc:`Authorize.Net <payment_providers/authorize>`
     - Odoo
     - |V|
     - Plně obsazeno
     - Plně obsazeno
     -
   * – :doc:`Buckaroo <payment_providers/buckaroo>`
     - Webové stránky poskytovatele
     -
     -
     -
     -
   * – :doc:`Flutterwave <payment_providers/flutterwave>`
     - Webové stránky poskytovatele
     - |V|
     -
     -
     -
   * – :doc:`Mercado Pago <payment_providers/mercado_pago>`
     - Webové stránky poskytovatele
     -
     -
     -
     -
   * - :doc:`Mollie <platební metody/mollie>`
     - Webové stránky poskytovatele
     -
     -
     -
     -
   * - :doc:`Nuvei <platební metody/nuvei>`
     - Webové stránky poskytovatele
     -
     -
     -
     -
   * :- :doc:`PayPal <platební metody/paypal>`
     - Webové stránky poskytovatele
     -
     -
     -
     -
   * – :doc:`Razorpay <payment_providers/razorpay>`
     - Odoo
     - |V|
     - Plně obsazeno
     - Úplné a částečné
     -
   * – :doc:`Stripe <payment_providers/stripe>`
     - Odoo
     - |V|
     - Plně obsazeno
     - Úplné a částečné
     - |V|
   * - :doc:`Worldline <platební_providers/worldline>`
     - Webové stránky poskytovatele
     - |V|
     -
     -
     -
   * :-: `Xendit <platební_providers/xendit>
     - Odoo nebo webové stránky poskytovatele
     - |V|
     -
     -
     -

.. |V| nahradit::
[*] Pro více informací se podívejte na dokumentaci Xenditu v části „Platební metody“

.. poznámka::
   - Každý poskytovatel má svůj vlastní specifický konfigurační proud podle toho, která funkce je
dostupné.
   - Některé z těchto poskytovatelů plateb přes internet lze také přidat jako „účty
<../finance/účetnictví/banka>`, ale tento proces není stejný jako přidání plateb
poskytovatelé platebních služeb. Poskytovatelé platebních služeb umožňují zákazníkům platit online a přidávat bankovní účty.
v aplikaci Účetnictví, aby provedla bankovní vyrovnání.
<účetnictví/banka/srovnání>.

.. tip::
Kromě běžných poskytovatelů platebních služeb s integrovaným API, jako je například Stripe nebo PayPal,
nebo Adyen, Odoo balí do :doc:`Demonstrativního poskytovatele plateb <platební_poskytovatelé/demo>`. Tento
Poskytovatel vám umožní otestovat obchodní tok, který zahrnuje platby přes internet. Nejsou vyžadovány žádné přihlašovací údaje
Jakmile se totiž jedná o demo platby, jde v podstatě o fiktivní platby.

.. platby poskytovatelů platebních služeb / bankovní platby:

Platby bankovním převodem
-------------

- | :doc:`Převod peněz <payment_providers/wire_transfer>`
|Pokud je vybrána možnost Odoo, zobrazí se informace o platbě s referenčním číslem.
Pokud jste obdrželi platbu na svůj účet, schválte ji ručně.
- | :doc:`SEPA Direct Debit <payment_providers/sdd>`
|Vaši zákazníci mohou provést bankovní převod, aby zaregistrovali příkaz k inkasu SEPA a získali
přímo z účtu na bankovním účtu.

.._platební_prostředky/přidat_nový:

Povolení platebního poskytovatele
===========================

Přidat nového poskytovatele platebních služeb a způsoby platby spojené s ním pro vaše zákazníky
postupujte následovně:

#Přejděte na web platebního poskytovatele, vytvořte si účet a ujistěte se, že máte k dispozici API.
požadované kreditní údaje pro třetí strany. Tyto jsou nezbytné pro komunikaci mezi Odoo a
poskytovatel platebních služeb.
#V Odoo přejděte na záložku „Platební metody“ kliknutím na „Účetnictví >“.
Konfigurace --> Platební poskytovatelé`, :menuitem: `Webové stránky --> Konfigurace --> Platební
Prodejci“, nebo „Nastavení -> Platby -> Provozovatelé plateb“.
#Vyberte poskytovatele a nakonfigurujte kartu „Přihlašovací údaje“.
#Nastavte pole :guilabel:`Stát“ na hodnotu :guilabel:`Zapnuto“.

.. poznámka::
   - V poli dostupných v záložce „Přihlašovací údaje“ se zobrazují informace o platební službě.
do související dokumentace :ref:`<platební metody/podporované poskytovatelé>`.
informace.
   - Jakmile zapnete platební metodu, automaticky se zveřejní na vašem webu.
Pokud chcete příspěvek odstranit, klikněte na tlačítko „Zveřejněno“. Zákazníci nemohou příspěvky smazat.
platby přes neveřejného poskytovatele, ale stále mohou spravovat
:dfn:`(smazat a přiřadit k předplatnému)“ své stávající tokeny spojené s takovým poskytovatelem.

..._platební_prostředky/testovací_režim:

Testovací režim
---------

Pokud chcete vyzkoušet platební metodu jako test, nastavte pole :guilabel:`Stát` v platbě
Zadejte do pole „Provozovatel“ hodnotu „Testovací režim“, poté zadejte přihlašovací údaje svého poskytovatele v testovacím/sandbox režimu.
Karta „Přihlašovací údaje“.

.. poznámka::
Ve výchozím nastavení zůstává poskytovatel platebních služeb neveřejný v režimu testovacího provozu, aby byl nenápadný.
návštěvníci.

.. varování:
Doporučujeme používat režim testování na kopii nebo na testovací databázi, abyste se vyhnuli potenciálním problémům.
s vaším číslováním faktur.

.. platby poskytovatelů platebních služeb a způsobů platby:

Způsoby platby
===============

Každý poskytovatel plateb je spojen se seznamem podporovaných způsobů platby, metody uvedené v
V poli „Způsoby platby“ v záložce „Nastavení“ formuláře platebního poskytovatele
Jedná se o ty, které jsou aktivní. Aktivovat nebo deaktivovat způsob platby pro poskytovatele
Klikněte na tlačítko „Zapnout platební metody“ a poté klikněte na přepínač příslušného způsobu platby.

.. tip::
Zobrazení platebních metod na vašem webu je založeno na jejich pořadí. Chcete-li je přeřadit,
Klikněte na tlačítko „Zapnout platební metody“ v formuláři poskytovatele plateb. Pak klikněte na
:guilabel:`Způsoby platby“ seznamu, přetáhněte a vložte způsoby platby do požadovaného pořadí.

Ikony a značky
----------------

Ikony zobrazené vedle způsobu platby na vašem webu jsou buď ikony značek
aktivovány pro způsob platby nebo, pokud nejsou žádné, ikony platebních metod
vlastní účetnictví. Chcete-li je upravit, přejděte na: „Účetnictví“ -> „Konfigurace“ -> „Způsoby platby“.
„Webová stránka > Konfigurace > Způsoby platby“ nebo „Prodej >
Konfigurace --> Způsoby platby, pak klikněte na způsob platby.

Pro změnu ikony platebního metodu přejeďte myší nad obrázek v pravém horním rohu.
formu a klikněte na ikonu „Penál“ (zobrazí se ikona „Penál“).

Vyberte záložku „Značky“ a zobrazte značky, které byly aktivovány pro platbu.
metodou. Značky a jejich související ikony se zobrazují podle pořadí, v němž jsou uspořádány; k přeskupení
jejich, přetáhněte je do požadovaného pořadí. Chcete-li upravit ikonu značky, vyberte značku, pak
V okně, které se otevře, přejeďte myší nad obrázkem v pravém horním rohu a klikněte
:icon:`fa-pero` (:guilabel:`pero`)

Pokročilá konfigurace
----------------------

Pro další konfiguraci platebních metod přejděte do sekce:
Metody“, „menu“: „Webová stránka -> Konfigurace -> Způsoby platby“ nebo „Prodej“.
Konfigurace -> Způsoby platby. Klikněte na způsob platby a aktivujte
:ref:`rozvojový režim <developer-mode>“. Klikněte na záložku „Nastavení“, abyste mohli přizpůsobit
vlastnosti.

.. nebezpečí::
   - Každý způsob platby je přednastaven tak, aby odpovídal požadavkům poskytovatelů plateb.
chování a jejich integrace do systému Odoo. Každá změna této konfigurace může vést k chybám
a měly by se nejprve otestovat na duplicitním nebo testovacím serveru.
   - Pouze změny konfigurace platebního metodu fungují do míry, v jaké je tento metod.
a schopnosti poskytovatele. Například přidáním :ref:`států
</platby/platební metody/měny-státy> pro platební metodu, která je podporována pouze v jedné zemi nebo
umožňuje tokenizaci metody spojené s poskytovatelem
Pokud nepodpoříte, nedostanete očekávaný výsledek.

.. platby/tokenizace:

Tokenizace
============

Pokud tuto funkci podporuje platební poskytovatel, zákazník
mohou si uložit své platební údaje pro pozdější použití. Chcete-li tuto funkci zapnout, přejděte na
Konfigurační záložka vybraného poskytovatele plateb a zapnout možnost „Umožnit ukládání
Způsoby platby.

V tomto případě je vytvořen **platební token** v Odoo, který bude sloužit jako platební metoda pro další
Platby bez nutnosti zadávat údaje o platební metodě znovu.
Je zvláště užitečný pro konverzi elektronického obchodování a předplatné, které využívají opakující se platby.

.. tip::
Každý zákazník může přidat nebo odstranit své uložené údaje o platební metodě kliknutím na tlačítko „Spravovat
způsoby platby v části „Portál pro zákazníky“ na odkazu: `Způsoby platby <users-portal-payment-methods>.

Poznámka: PCI DSS a prohlášení o souladu

Odoo není certifikováno podle standardu PCI DSS, protože nepodléhá kontrole.
ukládat údaje o držiteli karty nebo zpracovávat platby. Namísto toho se vzdaluje tokenizaci a
:ref:`externí poskytovatelé platebních služeb <platebni_sluzby/online_poskytovatele>“, což znamená, že jako
Odoo zákazník, stačí vyplnit pouze minimální dotazník sebehodnocení (SAQ).
poskytovatelé, kteří získají atestaci shody (AoC) a splní požadavky na PCI.
Není vhodné uvádět jako zpracovatele plateb nebo třetí stranu.
:zkratka:„SAMOHODNOUCÍ PŘEDVÝBĚR“.

.. _platební_prostředky/ruční_zaplacení:

Manuální snímání
==============

Pokud tuto funkci podporuje poskytovatel platebních služeb, můžete
autorizovat a zpracovávat platby ve dvou krocích místo jednoho. Chcete-li tuto funkci aktivovat, přejděte na
Klikněte na záložku „Nastavení“ vybraného poskytovatele plateb a zapněte „Vybrat částku“.
Ručně.“

Při autorizaci platby jsou prostředky rezervovány na účtu zákazníka, ale nejsou převedeny.
účtovány ihned, ale účtují se až v okamžiku, kdy je později ručně zadáte. Můžete také
zrušit autorizaci k zrušení a uvolnit rezervované prostředky. Získávání plateb ručně je
Pomůže v mnoha situacích:

- Přijměte potvrzení o platbě a počkejte, až bude objednávka odeslána, abyste mohli platbu získat zpět.
- Zkontrolujte a ověřte, zda objednávky jsou legitimní před dokončením platby a vyřízení.
Proces začíná.
- Vyhněte se případně vysokým poplatkům za vrácené platby: poskytovatelé platebních služeb nebudou účtovat žádné poplatky
pro zrušení autorizace.
- Zajistěte si vratnou kauci, která bude odečtena od případných srážek (např. za škody).

Chcete-li získat platbu po jejím schválení, přejděte na příslušný prodejní nebo fakturační doklad a klikněte
tlačítko „Získat transakci“. K vyplacení prostředků klikněte na tlačítko „Zrušit
„Převést“ tlačítko.

.. poznámka::
   - Někteří poskytovatelé platebních služeb podporují pouze část autorizované částky.
částku lze pak buď zachytit nebo zrušit. Tito poskytovatelé mají hodnotu **Full a
částí** v tabulce výše. Provozovatelé, kteří
pouze podpora pro zachycení nebo vyprázdnění celkové částky má hodnotu **Plně**.
   - Peníze nejsou rezervovány navždy. Po určité době mohou být automaticky
vrácen zpět na platební metodu zákazníka. Podívejte se do dokumentace vašeho poskytovatele plateb
pro přesnou dobu rezervace.
   - Odoo tuto funkci pro všechny způsoby platby nepodporuje, ale některé umožňují manuální snímání.
z webového rozhraní.

.. platby/vrácení peněz:

Vrácení peněz
=======

Pokud váš poskytovatel plateb podporuje tuto funkci, můžete vrátit platby přímo z Odoo. To
nemusí být nejprve aktivovány. Pro vrácení platby zákazníkovi přejděte na něj a klikněte na
:guilabel:`Vrácení peněz“ tlačítko.

.. poznámka::
   - Někteří poskytovatelé platebních služeb podporují pouze částečné vrácení částky, zbylou část pak
Pokud se rozhodnete vrátit peníze, můžete si je také nechat vrátit. Tyto poskytovatelé mají hodnotu **Plná a částečná** v
:ref:`tabulka výše <platební_metody/online_platby>“. Provozovatelé, kteří podporují pouze online platby
vracení celé částky má hodnotu **Plná cena**.
   - Odoo tuto funkci nepodporuje pro všechny poskytovatele platebních služeb, ale někteří umožňují vrácení platby.
z webového rozhraní.

.. _platební_prostředky/rychlý_nákup:

Rychlé vyzvednutí
================

Pokud tuto funkci podporuje poskytovatel platebních služeb, můžete
umožnit zákazníkům používat tlačítka „Google Pay“ a „Apple Pay“ a platit
Elektronické objednávky na jeden klik. Když zákazníci použijí jednu z těchto ikon, přesměrují se rovnou na
kartu na stránku potvrzení bez vyplnění kontaktního formuláře. Stačí jen ověřit
platba přes platební bránu Googlu nebo Applu.

Chcete-li tuto funkci aktivovat, přejděte na záložku „Nastavení“ vybraného poskytovatele plateb a
Povolit expresní platbu.

.. poznámka::
Všechny ceny uvedené na platební stránce rychlého nákupu zahrnují vždy i daně.

.. platby/dostupnost:

Dostupnost
============

Můžete přizpůsobit dostupnost poskytovatele plateb tím, že zadáte maximální částku.
umožněno a modifikace :guilabel:`Měn“ a :guilabel:`Států“ v
Karta „Nastavení“.

.. tip::
Aby bylo možné zobrazit dostupnost poskytovatelů plateb a způsobů platby a pomoci při diagnostice
Potenciální problémy s dostupností na platební stránce umožňují zapnout režim vývojáře, pak klikněte
:ikonu „Bug“ (ikona „Chyba“) vedle ikony „Zvolte způsob platby“.
hlavičce platebního formuláře. Výpis obsahuje seznam povolených poskytovatelů platebních služeb a
metody, důvody pro jakékoliv platby nebo metody nebude k dispozici, pokud je to vhodné.
seznam podporovaných poskytovatelů pro každý způsob platby.

.._platby/měny_státy:

Měny a země
------------------------

Všichni poskytovatelé platebních služeb mají jiný seznam dostupných měn a zemí, které podporují.
první filtr při platebních operacích, tedy způsoby platby spojené s platebním poskytovatelem
Není k dispozici, pokud měna nebo země zákazníka nejsou na seznamu podporovaných.
seznam dostupných měn a zemí může obsahovat chyby, aktualizace nebo neznámé položky.
Přidání nebo odstranění podporovaných měn či zemí poskytovatele plateb je možné.

.. poznámka::

   - :ref:`Platební metody <platebni-metody/platebni-metody>` také mají svůj vlastní seznam
dostupné měny a země, které slouží jako další filtr při platebních operacích.
   - Pokud je seznam podporovaných měn nebo zemí prázdný, znamená to, že seznam je příliš dlouhý na to, aby
nebyl zobrazen nebo Odoo nemá informace o tomto poskytovateli platebních služeb. Poskytovatel
Zůstává k dispozici i když je možné, že později bude platba zamítnuta.
Pokud země nebo měna nejsou podporovány.

Maximální částka
--------------

Můžete omezit maximální částku, kterou lze s vybraným poskytovatelem zaplatit.
pole na „0,00“ a platba bude možná bez ohledu na výši částky.

.. důležité::
Tato funkce není určena k použití na stránkách, které umožňují zákazníkovi aktualizovat způsob platby.
částka, například v případě snímku Donation a stránky Checkout při placení za dopravu :doc:`přepravních metod
<../websites/ecommerce/dodání> jsou povoleny.

.. platby/noviny:

Účetní deník
===============

Pro zaznamenání platby je nutné definovat v účetní knize „účetní deník plateb“
platby na účet vedený u banky. Výchozí deník je „Banka“,
účetní kniha pro všechny platební metody. Chcete-li ji upravit, přejděte na záložku
vyberte požadovaného poskytovatele plateb a vyberte jiný: `Platby v deníku.

.. poznámka::
   - Platební deník musí být veden jako „Banka“.
   - Ten samý účet můžete používat pro více platebních poskytovatelů.
   - Přiřazení platebních deníků je nutné pouze v případě, že se jedná o aplikaci „Fakturace nebo účetnictví“ (účetnictví).
Je nainstalován.

Účetní pohled
----------------------

Z účetního hlediska existují dvě typy online platebních procesů: platby,
jsou převedeny přímo na váš bankovní účet a následně probíhá obvyklá :doc:`srovnávací
„účetní/bankovní/srovnání“ pracovním postupem a těmi přicházejícími z externích „online plateb
poskytovatelé platebních služeb a vyžadují, abyste sledovali další účetnictví
průběh práce. Pro tyto platby je třeba zvážit, jak chcete vést účetní záznamy o platebních příkazech
vstupy. Doporučujeme vám, abyste se obrátili na svého účetního.

Výchozí hodnotou je účet definovaný pro platební deník podle :guilabel:`Bank Account
Pokud je použito „<platební metody/noviny>“, můžete také zadat :ref:`nevyrovnaný účet
<účetnictví/banka/neuhrazené účty> pro každého poskytovatele platebních služeb, aby byly odděleny platby
z plateb jiných plateb.

.. obrázek: platby/bankovní_účet.png
:alt:Definice výjimečného účtu pro poskytovatele plateb.

.. viz též:
   - :doc:`platební_prostředky/bankovní_převod
   - :doc:`platební_prostředky/sdd`
   - :doc:`platební_prostředky/adyen`
   - :doc:`payment_providers/authorize`
   - :doc:`platební-prostředky/asiapay`
   - :doc:`platební_prostředky/buckaroo
   - :doc:`platební_prostředky/demo`
   - :doc:`platební_prostředky/mercado_pago`
   - :doc:`platební_prostředky/mollie
   - :doc:`platební_prostředky/nuvei`
   - :doc:`platební_prostředky/paypal`
   - :doc:`platební_prostředky/razorpay`
   - :doc:`platební_prostředky/stripe`
   - :doc:`platební_prostředky/worldline
   - :doc:`platební služby/xendit`
   - :doc:`účetnictví/banka
