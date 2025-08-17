=======================
Řízení objednávek na Amazonu
=======================

Synchronizace objednávek
=====================

Objednávky jsou automaticky stahovány z Amazonu a synchronizovány v Odoo na pravidelných intervalech.

Synchronizace je založena na stavu objednávky v Amazonu: pouze pokud se od poslední synchronizace změnil stav objednávky,
poslední synchronizace jsou získávány z Amazonu. To zahrnuje změny na obou koncích (Amazon nebo Odoo).

Pro FBA (Fulfilled by Amazon) jsou získávány pouze objednávky „Odesláno“ a „Zrušeno“.

Pro FBM (Fulfilled by Merchant) se stejné dělá pro objednávky *Unshipped* a *Cancelled*.
synchronizovaný pořad, objednávka prodeje a zákazník vytvoříte v Odoo (pokud zákazník již nebyl
evidované v databázi).

.. poznámka::
Když je objednávka v Amazonu zrušena a byla již synchronizována v Odoo, odpovídající
Pokud zákazník vrátí objednávku, je v Odoo automaticky zrušena.

Synchronizace sil
=====================

Aby se zadání objednávky s **nezměněným** stavem odeslalo do zpracování.
předchozí synchronizace, začněte aktivací režimu vývojáře (:ref:`<developer-mode>`).
zahrnuje změny na obou stranách (Amazon nebo Odoo).

Poté přejděte do účtu Amazonu v Odoo (v menu vyberte: „Prodejní aplikace“ - „Nastavení“).
Nastavení > Připojení > Amazon Sync > Amazon účty a upravte datum pod
:menu_vyber->„Sledování objednávek –> Poslední synchronizace objednávky“.

Ujistěte se, že vyberete datum před poslední změnou stavu požadované objednávky.
synchronizovat a uložit. Tím zajistíte, že se synchronizace provede správně.


..tip:
Pro okamžité synchronizaci objednávek účtu na Amazonu přepněte do režimu vývojáře
<developer-mode>`, přejděte do účtu na Amazonu v Odoo a klikněte na „Synchronizovat objednávky“.
stejné lze udělat s výběrem kliknutím na „Synchronizovat výběr“.

Zajistit dodávky v rámci FBS
========================

Při každém synchronizačním procesu objednávky typu FBM (Fulfilled by Merchant) v Odoo je okamžitě vygenerován výdej.
Vytvořené v aplikaci Inventura společně s prodejním příkazem a zákaznickým záznamem. Pak se rozhodnete buď
zaslat všechny objednané produkty zákazníkovi najednou nebo zasílat produkty částečně pomocí zpětných objednávek.

Když je potvrzena skladová výdejka související s objednávkou, je pak odeslána zpráva na Amazonu, který
informuje zákazníka o tom, že objednávka (nebo její část) je na cestě.

.. důležité:
Amazon vyžaduje od uživatelů, aby při každé dodávce poskytli sledovací číslo. To je potřebné k
přidělit dopravce.

Pokud dopravce neposkytuje automaticky sledovací číslo, je nutné ho nastavit ručně.
Tato pravidla se vztahují na všechny tržiště Amazonu.

..tip:
Pokud zvolený dopravce není podporován v Odoo, může být stále vytvořen dopravce se stejným jménem.
(např. vytvořit dopravce s názvem „easyship“). Název použitý není citlivý na velikost písmen, ale buďte při jeho zadávání opatrní
aby se předešlo chybám. Pokud jsou chyby, Amazon je nepozná. Poté vytvořte doručovací adresu
dopravce s názvem „Vlastní doručení“ informuje Amazon, že uživatel bude zásilky doručovat sám.
tuto trasu je nutné stále zadávat sledovací číslo. Pamatujte na to, že zákazník je o této skutečnosti informován.
doručení e-mailem a dopravce spolu s referenčními údaji o sledování jsou zobrazeny
e-mail zákazníkovi.

.. viz též:
:doc:`../../../inventar-und-mrp/Inventur/Versand und Empfang/Konfiguration/Drittanbieter-Spediteure`

... _spravovat/správu chyb při doručení:

Správa chyb při synchronizaci dodávek
-------------------------------------------

Amazon někdy nedokáže správně zpracovat všechny informace odeslané prostřednictvím Odoo. V tomto případě
Odešle e-mail s seznamem všech neúspěšných dodávek a chybami, které mu Amazon poslal spolu s nimi.
kromě toho jsou tyto dodávky označeny štítkem „Nesouhlas s Amazonem“.

Obvykle lze chybu opravit přímo v zadní části Amazonu nebo v Odoo. Pokud je problém
opravené v Odoo, opět synchronizovat pomocí tlačítka „Pokusit se o synchronizaci s Amazonem“.

.. poznámka::
Je možné, že Odoo obdrží oznámení od Amazonu, že nějaké zásilky
Informace nebyla zpracována, ale bez uvedení, které zásilky byly postiženy.
Pokud se tak stane, budou všechny neznámé zásilky považovány za selhání synchronizace.
Jakmile Odoo obdrží oznámení od Amazonu, že byla zásilka zpracována, bude na ní umístěn štítek.
změnit na: „Synchronizováno s Amazonem“. K tomu můžete použít rychlejší proces na vašem účtu Amazon.
klikněte na tlačítko „Synchronizovat objednávky“ nebo klikněte na
:guilabel:`Obnovit objednávku“ a zadejte odkaz na příslušnou objednávku Amazonu.

Sledujte dodávky v rámci služby FBA
========================

Při synchronizaci objednávky FBA (Fulfilled by Amazon) v Odoo je zaznamenán pohyb zásob.
Ve skladovém záznamu pro každý položku objednávky je uložená inventura.

Správci zásob mohou tyto pohyby zásob zobrazit kliknutím na:
Hlášení --> Historie pohybů.

Pro objednávky z FBA je v Odoo automaticky vytvořen pohyb skladu díky Amazonovému propojení.
stav dodání na Amazonu. Při odesílání nových produktů na Amazon by uživatel měl ručně vytvořit
objednávku na vyzvednutí, která tyto produkty převezme z jejich skladu do míst Amazonu.

..tip:
Pro sledování zásob v Amazonu (FBA) v Odoo je potřeba provést inventurní úpravy po doplnění zásob.
Automatické doplňování z pravidel opětovného objednávání lze také spustit na místě Amazonu.

Amazon lokalitu je možné nakonfigurovat přístupem do Amazon účtu spravovaného v Odoo.
Amazon účty v Odoo se přesouvají na:menuselection:Prodej aplikace --> Konfigurace --> Nastavení -->
Konektory --> Synchronizace s Amazonem --> Amazon účty.

Všechny účty stejné společnosti používají výchozí umístění Amazonu. Nicméně je možné
sledovat cenu akcií filtrovaných na burze.

Pro to nejprve odstraňte tržiště, kde je možné najít požadovanou akcii, kterou chcete sledovat zvlášť.
z seznamu synchronizovaných tržišť, který lze najít po kliknutí na
:menu-vyber->Prodejní aplikace-->Konfigurace-->Nastavení-->Připojení-->Amazon Sync-->Amazon
Účty.

Nyní vytvořte další registraci pro tento účet a odstraňte všechny tržiště - s výjimkou
Tento trh se chce izolovat od ostatních.

Nakonec přidělte další skladovou položku k druhému zápisu účtu.

Faktury a platby z účtu
=============================

Vystavit faktury
--------------

Amazon nemá politiku sdílení e-mailových adres zákazníků, takže není možné zaslat
faktury přímo zákazníkům z Amazonu přes Odoo. Nicméně je možné i manuální nahrání
vytvářely faktury z Odoa do Amazon back-endu.

Dále je pro klienty B2B aktuálně nutné ručně získat DIČ.
Amazon Backend před vytvořením faktury v Odoo.

Registrace plateb
-----------------

Od zákazníků totiž Amazon dostává peníze jako prostředníka, proto vytvořil speciální bankovní účet (například s názvem
„Amazon Payments“), s vlastním účtem „Banka a hotovost“ je doporučený.

Další výhodou je, že Amazon platí jednou měsíčně, takže můžete vybrat všechny faktury spojené s
Při registraci plateb je nutné uvést jednorázový poplatek.

Pro to použijte příslušný záznam v deníku „Journal“ určený pro platby na Amazonu a vyberte
„Skládání“ jako „Způsob platby“.

Poté vyberte všechny vytvořené platby a klikněte na „Akce“ > „Vytvořit hromadnou platbu“.
--> Zkontrolovat.

..tip:
Toto stejné akce lze provést s fakturami dodavatele od společnosti Amazon, které jsou určeny na provize.

Když je vyrovnání připsáno na účet v průběhu měsíce a výpisy z účtu
Peníze jsou zaznamenány a na účet prostředníka Amazonu je připsána částka obdržená.

Sledujte prodeje na Amazonu v reportingu
======================================

Na účtu profilu na Amazonu v Odoo je nastaven tým pro sledování objednávek pod :guilabel:`Sledování objednávky
tab.

Tímto způsobem lze rychle získat přístup k důležitým metrikám souvisejícím s prodejem. Výchozí hodnotou je Amazon
Prodejní tým účtu je společný pro všechny účty společnosti.

Pokud je to potřeba, může být tým prodejců na účtu změněn za jiný, aby provedl samostatný
zpracovávání prodejů z této účetní knihy.

..tip:
Je také možné provádět reportování na základě trhu.

Nejprve odstraňte požadovanou burzu z seznamu synchronizovaných burz.

Chcete-li zobrazit seznam synchronizovaných tržišť v aplikaci Odoo, přejděte na:
--> Konfigurace --> Nastavení --> Propojovací body --> Amazon Sync --> Amazon účty.

Pak vytvořte další registraci pro tento účet a odstraňte všechny ostatní tržiště kromě
ten, který izoluje.

Nakonec přidělte další prodejní tým jednomu z dvou registrací účtu.

.. viz též:
   - :doc:`feature“
   - :doc:`setup`
