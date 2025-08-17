===============
Zpracování olova
===============

Služba „Obsah zinku“ poskytuje obchodní informace o kontaktu připojeném k leadu.
Zpracování olova je nákup v aplikaci (IAP), který vyžaduje kredity a je k dispozici pro
existující kontakty v databázi Odoo.

Informace, které poskytuje lead enrichment, mohou zahrnovat obecné informace o podnikání
(včetně celého názvu a loga), sociálních médií, :guilabel:`Typ společnosti`,
Informace o založení, informace o sektorech a počet
:guilabel:`Zaměstnanci“, :guilabel:`Odhadovaný obrat“, :guilabel:`Telefonní číslo“
:guilabel:`Časová zóna“ a „Použité technologie“.

.. poznámka::
Uživatelé podnikového řešení Odoo s platnou licencí získají bezplatné kredity na testování:abbr:`IAP (In-App
Před rozhodnutím o koupi dalších kreditů pro databázi se ujistěte, že jste si přečetli popis funkce „Koupit“. To zahrnuje
demonstrační databáze, vzdělávací databáze a databáze bez aplikace.

.. důležité:
Funkce „Leads“ musí být aktivována v nastavení CRM, aby se mohl používat lead.
enrichment. Chcete-li získat přístup k nastavením aplikace CRM, přejděte na:
--> Nastavení. V sekci „CRM“ aktivujte možnost „Vedení obchodních příležitostí“ a klikněte
:guilabel:`Uložit“.

Zařízení pro obohacování olova
======================

Pro nastavení označení vedení v aplikaci CRM přejděte na:
Konfigurace --> Nastavení. Pak pod položkou „Vedení zákazníků“ zaškrtněte políčko
vedle položky „Zpracování kontaktů“ a vyberte buď „Pouze na poptávku“ nebo
Klikněte na tlačítko „Uložit“ pro aktivaci
změny.

.. obrázek: lead_enrichment/lead-enrichment-activate.png
:align:center
:alt:Nastavení generování leadů v CRM, s aktivací doplňování kontaktních údajů označenou, a doplnění
Vedení účtu je možné pouze na vyžádání.

V čele stojí Enrich
============

Zpracování kontaktů je založeno na doméně e-mailové adresy zákazníka, který je nastaven v kontaktu.
Existují dvě různé možnosti, jak může být kontakt obohacen: automaticky nebo ručně.

Automaticky obohacovat kontakty
--------------------------

Při nastavování, pokud byl vybrán parametr „Automaticky obohacovat všechny kontakty“ v CRM.
„Nastavení“ stránku, pak uživatel nemusí nic dělat, aby byl veden zlepšen.
Akce podle plánu běží automaticky každých 60 minut a obohacování probíhá na kontaktech po
je kontaktována vzdálená databáze.

..tip:
Přístup k cronu, který běží pro automatické doplňování kontaktů, aktivujte v režimu vývojáře.
<developer-mode>`, a přejděte na: menuselection: „Nastavení aplikace“ --> „Technické menu“ --> „Automatizace“.
části --> Akce v plánu. V poli „Hledat…“ zadejte „CRM“. Klikněte na
Výsledek označte štítkem :guilabel:`CRM: obohacení kontaktů (IAP)` a provádějte případné úpravy.
V poli „Spustit každých“ zadejte hodnotu větší než nebo rovnou pěti minutám.

Příklad:
Následující je příklad úspěšně dokončené automatické doplňování dat o obsahu olova:

.... obrázek:: lead_enrichment/lead-enrichment-data.png
:synchronizace: střed
:alt:Chatová konverzace ukazující data o obohacování olova.

Manuálně obohacovat kontakty
---------------------

Pokud byla zvolena možnost „Vyžádáno“ v položce „Nastavení“ na kartě CRM,
stránce, když aktivujete:guilabel:"Získání informací o kontaktu", každý kontakt, který uživatel chce obohatit, **musí být**
ručně obohatit. To se provede kliknutím na tlačítko „Obohatit“ v horní nabídce
v čele.

Stejná informace bude získána za stejnou cenu kreditu „IAP (In-App Purchases)“ (jedno na
enrichmentu. Tento způsob enrichmentu je užitečný v případě, že ne každý vzorek potřebuje být obohacen, nebo
Jde o peníze.

.. obrázek: lead_enrichment/ruční obohacení.png
:align:center
:alt:Tlačítko pro ruční doplnění údajů označené na kartě kontaktu v CRM.

..tip:
Manuálně obohatit větší množství kontaktů pomocí pohledu „Seznam“. Nejprve přejděte do sekce „Aplikace CRM“
--> Vedoucí pracovníci a klikněte na tlačítko seznamu zobrazení (:guilabel:`☰ (tři horizontální čáry)` ikona).
Vyberte zaškrtávací políčka u kontaktů, které chcete ručně doplnit informacemi. Nakonec klikněte na
:guilabel:`Akce“ ikonu a vyberte z rozevírací nabídky „Zpřístupnit“.
Také lze dosáhnout z stránky My Pipeline. Stačí otevřít aplikaci CRM nebo
navigovat do:menuvolba:„Aplikace CRM - Prodej - Můj prodejní kanál“. Obě cesty odhalují kontakty.
možnosti na stránce Pipeline.

Ceny
=======

Zpracování kontaktů je funkcí In-App Purchase (IAP), a každý zpracovaný kontakt stojí jeden kredit.

.. poznámka::
Více informací o cenách naleznete zde: „Generování leadů pomocí Odoo IAP
<https://iap.odoo.com/iap/in-app-services/273>.

Kredity si můžete koupit v aplikaci CRM: „Nastavení“ → „Konfigurace“.
:guilabel:`Generování leadů“ v sekci „Zpracování leadů“, klikněte na
:guilabel:`Koupit kredity“.

.. obrázek: lead_enrichment/koupit-kredity-na-zpracování-leadu-vlastnosti.png
:align:center
:alt: Kredity koupíte v nastavení pro zvýšení účtu.

Kredity a zůstatky lze také zakoupit po načtení aplikace „Nastavení“.
sekci „Kontakty“, pod položkou „Odoo IAP“ klikněte na „Zobrazit“.
Můj servis“.

.. obrázek: lead_enrichment/view-my-services-setting.png
:align:center
:alt:Kredity si můžete zakoupit v nastavení Odoo IAP.

.. viz též:
:doc:`../../../základy/nákupy_v_aplikaci“

.. důležité:
Při shromažďování kontaktních údajů společnosti se ujistěte, že máte přehled o nejnovějších pravidlech EU.
předpisy. Více informací o obecném nařízení o ochraně osobních údajů najdete v následujícím odkazu: Odoo GDPR
<http://odoo.com/gdpr>.
