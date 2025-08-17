================
Automatizace pravidel
================

S předplatným v provozu je důležité udržovat kontakt se zákazníky.
účinné využít automatizaci, aby se nemuselo ručně procházet seznamy odběratelů.
Jak se věci vyvíjejí. Právě tam přichází v úvahu funkce automatizace pravidel od společnosti Odoo.

Aplikace Odoo *Subscriptions* umožňuje uživatelům nastavit automatické e-maily a vytvářet úkoly.
prodejci a dokonce i zasílat dotazníky spokojenosti pro předplatitele k hodnocení jejich zkušeností.

Vytvořte pravidla automatizace
=======================

Pro vytvoření automatické pravidlo začněte tím, že se přesunete na:
Konfigurace --> Automatické pravidlo. Tady se nacházejí všechna automatická pravidla pro předplatné.
našel.

Stránka „Automatické pravidlo“ zobrazuje název každého pravidla, jeho „Akci“,
jakým způsobem bude automatická pravidla spouštět a jaké společnosti se na ni budou vztahovat.
Platí.

Pro zobrazení nebo úpravu existujících pravidel automatizace stačí kliknout na požadované pravidlo v této stránce.

.. poznámka::
Při úpravě stávajícího pravidla automatizace se v části „Akce“ zobrazí šedé pozadí.
formulář a poskytuje následující varování:*Aktuální data akce nelze aktualizovat, aby se předešlo neočekávaným výsledkům.
chování. Vytvořte novou akci místo toho.*

Pro vytvoření nové automatické pravidlo klikněte na tlačítko „New“.

.. obrázek: automatic_alerts/automation-rules-page.png
:align:center
:alt:Stránka Automatické pravidlo v aplikaci Odoo Předplatné.

Kliknutím na „Nový“ se zobrazí prázdná stránka s mnoha poli pro
konfigurovat.

.. obrázek: automatické_upozornění/automatizace-pravidel-formulář.png
:align:center
:alt:Příklad formuláře pro automatizaci v aplikaci Odoo Subscriptions.

Pravidla automatizace políček pro formuláře
---------------------------

- :guilabel:`Název akce“: název automatické pravidlo pro akci.

Přihláška
~~~~~~~~~~~~~~~~

Sekce „Použít na“ určuje, které objednávky/zákazníci se tato automatizovaná akce vztahuje.
se vztahuje na.

- :guilabel:`Příjem měsíčně opakovaný (MRR) mezi“: určit rozsah měsíčního příjmu, který je cílem.
- :guilabel:'Změna měsíčních opakujících se příjmů': označte změnu měsíčních opakujících se příjmů jako cíl, buď
procento nebo jednotku měny.
- :guilabel:„Doba“: vyberte časové období, za které jsou určeny klíčové ukazatele výkonnosti
Indikátory jsou vypočítávány.
- :guilabel:`Hodnocení spokojenosti“: označte spokojenost jako „větší než“ nebo
:guilabel:`méně než` procento.
- :guilabel:`Stav“: vyberte stav předplatného, které chcete zahrnout do této automatické pravidlo.
Možnosti jsou: „Citace“, „Odeslaná citace“, „Objednávka“ a
:guilabel:`Zrušeno“.
- :guilabel:`Automatická pravidla začínají od“: určete, kdy by se měl spustit automatický proces, pomocí dvou
pole, která reprezentují dva různé fáze předplatného.
- :guilabel:`Plány předplatného“: vyberte konkrétní plány předplatného, na které se má automatizace zaměřit
pravidlo.
- :guilabel:`Produkty“: vyberte konkrétní produkt, na který se má vztahovat pravidlo automatizace.
- :guilabel:`Zákazníci“: vyberte konkrétního zákazníka, na kterého se má aplikovat automatická pravidla.
- :guilabel:`Společnost“: v prostředí více společností vyberte konkrétní společnost
cílí na automatizační pravidlo.
- :guilabel:`Prodejní tým“: vyberte data konkrétního prodejního týmu, na který se má automatizace zaměřit
pravidlo.

.. poznámka::
Pokud je některé pole nevyplněné, pravidlo se vztahuje na každou smlouvu bez konkrétního
označení.

..tip:
Počet předplatných, které odpovídají nastaveným kritériím pro automatické pravidlo.
Tyto informace se zobrazují na spodní části pole „Aplikovat“.

Pokud je kliknutá zelená odkaz na předplatné, Odoo zobrazí samostatnou stránku s přehledem všech
předplatné, které splňují kritéria automatizačního pravidla.

Akční část
~~~~~~~~~~~~~~

Sekce „Akce“ určuje, co se stane, když je spuštěna automatická pravidla.

V poli „Akce“ vyberte akci, která se bude provádět po spuštění automatické pravidlo.
spuštěno. Kliknutím se zobrazí následující možnosti v rozbalovacím menu:

- :guilabel:`Vytvořit další aktivitu“: vytváří další aktivitu, která je konfigurovaná
:guilabel:`Aktivita“ sekce, která se zobrazuje na spodní části formuláře pro pravidlo automatizace.
- :guilabel:`Odeslat e-mail zákazníkovi“: odesílá e-mail zákazníkům, kteří splňují zadané
kritérií automatického pravidla.
- :guilabel:`Odeslat textovou zprávu zákazníkovi“: odesílá textovou zprávu zákazníkům (zákaznicím), kteří
musí splňovat zadaná kritéria automatizační pravidla.
- :guilabel:`Hodnota smlouvy o zdravotním pojištění“: nastavte hodnotu smlouvy o zdravotním pojištění.

Pokud je vybrána možnost „Odeslat e-mail zákazníkovi“ v poli „Akce k provedení“,
V dalším poli se zobrazí:

- :guilabel:`Šablona e-mailu“: vytvořit novou šablonu e-mailu nebo vybrat ze seznamu
přednastavené e-mailové šablony, které je možné zaslat zákazníkovi.

Pokud je vybrána volba „Odeslat textovou zprávu zákazníkovi“ v poli „Akce, které chcete provést“.
pole se objeví další pole:

- :guilabel:`Šablona SMS“: vytvořit (a upravit) novou šablonu SMS *nebo* vybrat z seznamu
přednastavené textové šablony pro odeslání zákazníkům.

Pokud je vybrána volba „Hodnota smlouvy o zdravotním pojištění“ v poli „Akce k provedení“,
V dalším poli se zobrazí:

- :guilabel:`Zdraví“: určete zdravotní stav předplatného zvolením jednoho z následujících
Možnosti jsou: „Neváhám“, „Dobrá“ nebo „Špatná“.

V poli „Aktivace“ rozhodněte o tom, zda má být automatická pravidla spuštěna na
„Upravení“ nebo „Časová podmínka“.

.. poznámka::
A tlačítko „Spustit nyní“ se objeví pouze v horní části okna s pravidly automatizace, pokud je
byl pro pravidlo nastaven spouštěč.

.. varování:
Když je kliknutá tlačítko „Spustit nyní“, Odoo spustí akci na všech propojených
předplatné bez ohledu na možná časová omezení.

.. poznámka::
Při odesílání SMS zprávy v Odoo je nutné mít kredit nebo tokeny pro In-App Purchase (IAP).
informace o :abbr:`IAP (Nákupy v aplikaci)“, navštivte :doc:`../essentials/in_app_purchase“.
Více informací o zasílání SMS zpráv najdete na
:doc:`../marketing/sms_marketing`.

Pokud je vybrána možnost „Časová podmínka“ v poli „Spouštěcí událost“, následující pole
přijít na scénu:

- :guilabel:`Spouštěcí datum“: reprezentuje kdy by se měla splnit podmínka. Pokud je nechána prázdná,
Akce je vytvářena při vytváření odběru a aktualizacích.
- „Časový zpoždění po spuštění“: vyberte časové zpoždění („minuty“,
:guilabel:`hodiny“, :guilabel:`dny“ nebo :guilabel:`měsíce“) pro Odoo, aby spustilo
konfigurované akce. Pokud je zadána záporná čísla, „zpoždění“ se stane *před*
:guilabel:`Datum spouštění“.

Sportovní sekce
****************

Pokud je vybrána volba „Vytvořit další aktivitu“ v poli „Akce k provedení“,
:guilabel:„Aktivita“ se zobrazuje na spodní části formuláře „Automatické pravidlo“.

- :guilabel:`Typ aktivity“: vyberte přednastavený typ aktivity z roletkového menu.
- :guilabel:`Název aktivity“: zadejte vlastní název pro vybranou aktivitu.
- :guilabel:`Poznámka“: zanechte poznámku pro zaměstnance, kterému je aktivita přiřazena.
- :guilabel:`Termín dokončení“: zadejte počet dní, ve kterých by měla být aktivita dokončena.
- :guilabel:`Přiřadit k:“: vyberte, zda chcete přiřadit konkrétní aktivitu buď k:
Prodejce“, „Vedoucí prodejního týmu“ nebo „Uživatelé“.

.. poznámka::
Pokud je zvolen „Uživatelé“ jako možnost „Přidat“, objeví se nový
:guilabel:`Uživatelé“ se objeví pod ním, kde může být vybrán konkrétní zaměstnanec (nebo více zaměstnanců).
jako příjemce konfigurované aktivity.

.. viz též:
  - :doc:`../předplatné`
  - :doc:`../essentials/in-app-purchase`
