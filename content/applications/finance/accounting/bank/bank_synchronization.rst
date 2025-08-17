Zobrazit obsah

====================
Synchronizace bank
====================

Odoo může synchronizovat přímo s vaší bankou, aby byly všechny výpisy z účtu importovány.
automaticky do vaší databáze.

Zkontrolovat, zda je váš bankovní účet kompatibilní s Odoo, navštivte stránku „Funkce účetnictví v Odoo“.
<https://www.odoo.com/page/accounting-features> a klikněte na
:guilabel:`Podívejte se na seznam podporovaných institucí“.

Odoo podporuje více než 26 000 institucí po celém světě.

Odoo k připojení k bankám používá několik webových služeb:

- *Kilt*: Spojené státy americké a Kanada
- **Yodlee**: Svět
- :doc:`Salt Edge <bank_synchronization/saltedge>“: Světově
- :doc:`Ponto <bank_synchronization/ponto>“: Evropa
- :doc:`Povolit bankovní účet <bank_synchronization/enablebanking>“: Skandinávské země

.. viz též:
:doc:`transakce“

Konfigurace
=============

Uživatelé on-premises
----------------

Pro využití této služby je potřeba mít platnou předplatnou Odoo Enterprise.
Ujistěte se, že je váš databázový server registrovaný s vaší smlouvou na Odoo Enterprise.
Používáme také prostředníka mezi vaší databází a poskytovatelem třetí strany, takže v případě
Při připojování došlo k chybě. Zkontrolujte, zda nemáte zapnutý firewall nebo proxy blokující
sídlo:

- https://production.odoofin.com/

První synchronizace
---------------------

Synchronizaci můžete spustit buď v aplikaci Účetnictví a
:menu-vyber->Účetnictví-->Nastavení-->Přidat bankovní účet.

Nyní můžete vyhledat svou banku. Vyberte ji a postupujte podle pokynů k synchronizaci s ní.

.. poznámka::
Pokud se během prvního synchronizování vyskytnou nějaké problémy, zkontrolujte prosím, že je
webový prohlížeč neblokuje reklamy a že je ve vašem prohlížeči vypnutý blokátor reklam.

.. důležité::
Při nastavení synchronizace s bankovním výpisem Odoo automaticky začne evidovat
účetní transakce od data poslední transakce + 1 den (pokud je datum poslední transakce)
31. prosince 2022 (nahrávání začíná 1. ledna 2023). Pokud účetní kniha neobsahuje žádnou transakci,
Odoo získává transakce co nejdále do minulosti. Můžete omezit, jak daleko do minulosti se Odoo dostane.
transakce otevřením aplikace Účetnictví, přechodem na: „Účetnictví --- Zámek dat“
a nastavit datum v poli „Datum uzamčení záznamů“.

Při prvním synchronizaci musíte zadat telefonní číslo, abyste svůj účet zabezpečili.
Takové informace, protože nechceme, aby vaše data spadla do nesprávných rukou. Proto se
detekovat podezřelé aktivity na vašem účtu, takže zablokujeme všechny požadavky odeslané z vašeho účtu.
Musíte ho znovu aktivovat pomocí této telefonní číslo.

Třetí strana může požadovat další informace, aby se připojila k vaší bance.
organizace. Tato informace není uložena na serverech společnosti Odoo.

Výchozí nastavení je takové, že transakce získané ze zdroje online jsou seskupeny v rámci jednoho příkazu.
Jeden výpis z bankovního účtu vzniká měsíčně. Můžete si změnit frekvenci vytváření bankovních výpisů
v nastavení vašeho deníku.

Pro zobrazení všech synchronizací zapněte režim vývojáře (:ref:`<developer-mode>`) a přejděte na
:menu:Účetní -> Konfigurace -> Synchronizace online.

Synchronizovat ručně
--------------------

Po prvním synchronizačním procesu jsou vytvořené záznamy automaticky synchronizovány každých 12 hodin.
Pokud chcete, můžete synchronizaci provést ručně kliknutím na tlačítko „Synchronizovat nyní“.
na přístrojové desce.

Alternativně aktivujte režim vývojáře (:ref:`<developer-mode>`) a přejděte na
V nabídce „Účetnictví -> Konfigurace -> Online synchronizace“ vyberte svoji instituci.
a pak klikněte na tlačítko „Stáhnout transakce“.

.. důležité::
Některé instituce neumožňují automatické stahování transakcí. Pro takové instituce
Při automatické synchronizaci účtu vám přijde chybová hláška s žádostí o zadání
vypnout automatické synchronizace. Toto upozornění najdete ve chatu vašeho online účtu.
synchronizace. V tomto případě je nutné provést ruční synchronizaci.

Problémy
======

Synchronizace v chybě
------------------------

Pokud chcete nahlásit problém s připojením, aktivujte
Vývojářský režim (viz developer mode), přejděte do sekce „Účetnictví“ – „Konfigurace“
Online synchronizace“, vyberte spojení, které selhalo, a zkopírujte popis chyby a
reference.

Synchronizace odpojena
----------------------------

Pokud se váš připojení k proxy rozpojí, můžete se s ním znovu spojit pomocí
Tlačítko „Získat účet“.

.. poznámka::
Pokud se vám nepodaří znovu připojit pomocí tlačítka „Znovu připojit“, kontaktujte prosím
„podpora“ přímo s vaším klientským ID nebo odkazem na chybu
uvedené v chatu.

.._MigrationOnlineSync:

Migrace uživatelů, kteří nainstalovali Odoo před prosincem 2020
======================================================================

Pokud jste na místě, ujistěte se nejprve, že vaše zdroje jsou aktuální s nejnovější verzí.
Odoo.

Uživatelé, kteří vytvořili databázi před prosincem 2020, si nový modul musí nainstalovat ručně.
využít nové funkce.

Pro toto vyberte v nabídce „Aplikace“ -> „Aktualizovat seznam aplikací“, odstraňte výchozí filtr v hledání
baru a typu „účet online synchronizace“. Poté klikněte na:guilabel:"Instalovat".
A nakonec ujistěte se, že všichni vaši uživatelé aktualizují svou stránku v Odoo stisknutím kláves Ctrl + F5.

.. Poznámka:

   - Předchozí synchronizace jsou během instalace odpojeny a nebudou fungovat.
Už nejsou dostupné. Chcete-li je zobrazit, zapněte režim vývojáře a přejděte na
:menu „Účetnictví“ -> „Konfigurace“ -> „Online synchronizace“.
to znamená, že musíte vytvořit nové spojení.
   - Nemusíte odinstalovat modul „account_online_sync“, který je předchozím modulem pro online
synchronizace. Nová ji přebírá.
   - Výchozí modul „account_online_synchronization“ je nainstalován automaticky s
Účetnictví.

Často kladené otázky
===

Synchronizace není v reálném čase. Je to normální?
----------------------------------------------------------------

Tento proces není určen k práci v reálném čase, protože třetí strany synchronizují vaše účty.
v různých intervalech. Chcete-li provést synchronizaci a získat prohlášení, přejděte na své
„Účetní přehled“ a klikněte na tlačítko „Synchronizovat nyní“.
a získat transakce aktivací režimu vývojáře (:ref:`developer mode <developer-mode>`) a přechodem na
Klikněte na „Účetní kniha“ -> „Nastavení“ -> „Online synchronizace“. Někteří poskytovatelé umožňují
jedna aktualizace denně, takže je možné, že kliknutím na tlačítko „Synchronizovat nyní“ nebude
Vaše poslední transakce, pokud jste již dříve v průběhu dne provedli nějakou akci.

Transakce může být na vašem účtu viditelná, ale nezískána, pokud má stav
:guilabel:Čekající“. Vybrané transakce budou zobrazeny pouze v případě, že mají stav „Odesláno“.
transakce ještě nebyla „zveřejněna“, musíte si počkat na změnu stavu.

Je funkce Synchronizace online bankovnictví součástí mého kontraktu?
-------------------------------------------------------------------

- **Edice komunity**: Ne, tato funkce není součástí edice komunity.
- **Online verze**: Ano, i když máte smlouvu na jedno zdarma.
- **Edice Enterprise**: Ano, pokud máte platnou smlouvu o podnikání spojenou se svým databázovým serverem.

Některé banky mají stav „beta“. Co to znamená?
-----------------------------------------------------

To znamená, že finanční instituce zatím nejsou plně podporovány našimi třetími stranami.
nebo jiné problémy mohou nastat. Odoo nepodporuje technické problémy, které se vyskytnou u bank v
Beta fáze, ale uživatel si může stále vybrat připojení. Připojením k těmto bankám přispívá
vývojový proces od doby, kdy bude mít poskytovatel skutečná data a zpětnou vazbu z připojení.

Proč se mi transakce nesynchronizují automaticky, ale až když je ručně obnovím?
----------------------------------------------------------------

Některé banky mají navíc další bezpečnostní opatření a vyžadují další kroky, jako je například zaslání SMS nebo e-mailu.
ověřovací kód nebo jiný typ vícefaktorové autentizace. Proto nemůže integrační partner provádět transakce
až do té doby, než bude kód zabezpečení poskytnut.

Nemám všechny své minulé transakce v Odoo, proč?
-------------------------------------------------

Některé instituce mohou získat pouze transakce do 3 měsíců v minulosti.

Proč nevidím žádné transakce?
---------------------------------

Při prvním synchronizačním spojení jste si vybrali účty, které se rozhodnete synchronizovat.
Odoo. Pokud jste neprovedli žádnou synchronizaci účtu, aktivujte režim vývojáře
<vývojářský režim>, přejděte na: „Účetnictví“ -> „Konfigurace“ -> „Online synchronizace“.
a klikněte na tlačítko „Stáhnout účet“.

Může se také stát, že nebudou nové transakce.

Pokud je váš bankovní účet správně propojen s deníkem a transakce nejsou viditelné ve vašem
databáze, prosím, „podávejte podporu <https://www.odoo.com/help>“.

Jak mohu aktualizovat své bankovní údaje?
-------------------------------------

Abychom aktualizovali vaše přihlašovací údaje, aktivujte režim vývojáře a přejděte na
:menu „Účetnictví“ -> „Nastavení“ -> „Online synchronizace“. Otevřete spojení, které
chcete aktualizovat své přihlašovací údaje a klikněte na tlačítko „Aktualizace přihlašovacích údajů“.

..toctree::


bankovní synchronizace/Salt Edge
bank_synchronizace/ponto
bank_synchronization/enablebanking
