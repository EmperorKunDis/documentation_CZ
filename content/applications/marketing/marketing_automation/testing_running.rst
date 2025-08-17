=========================
Testování a spouštění kampaní
=========================

Aplikace Odoo *Marketing Automation* umožňuje uživatelům před spuštěním kampaně otestovat její funkčnost.
formálně je spouštět, aby se zkontrolovaly chyby a opravily případné chyby předtím, než dosáhne svého cíle
publikum.

Testovací kampaně
==============

Chcete-li otestovat marketingovou kampaň, otevřete aplikaci Marketing Automation a vyberte
požadovanou kampaň otestovat, která odhalí podrobnosti kampaně.

V podrobnostech kampaně se ujistěte, že kampaň již má nastavené aktivity.
workflow (nebo postupujte podle pokynů v souboru :doc:`workflow_activities`)
dokumentace).

.. poznámka::
Testování automatizovaných kampaní je prováděno v produkční verzi.
databáze. Duplicitní (nebo testovací) databáze mají omezené možnosti odesílání e-mailů.

Chcete-li spustit test, klikněte na tlačítko „Spustit test“ v horní části formuláře kampaně.
pravé straně tlačítka „Start“.

.. obrázek: testovani_běhu/spustit-test.png
:align:center
:alt:Spustit tlačítko pro testování na formuláři s podrobnostmi kampaně v Odoo Marketing Automation.

Když na něj kliknete, objeví se okno s názvem „Spustit test“.

.. obrázek: testovani_běhu/spustit_test_okno.png
:align:center
:alt:Zahajte testovací okno s oznámením, které se zobrazí v Odoo Marketing Automation.

V okně „Spustit test“ klikněte na „Zvolit nebo vytvořit kontakt“.
Vytvořte pole „Testovací účastník“ pro zobrazení seznamu kontaktů. Z tohoto seznamu
Vyberte existující kontakt (nebo vytvořte nový), na kterého chcete provést test.

.. poznámka::
V okně „Spustit test“ lze vybrat pouze jeden kontakt.

Pro vytvoření nového kontaktu přímo z okna „Spustit test“ začněte psát
do prázdného pole název nové kontaktní osoby a klikněte na tlačítko „Vytvořit a upravit…“.

.. obrázek: testing_running/new-contact-from-launch-test-popup.png
:align:center
:alt:Při vkládání nového kontaktu přímo z rozhraní při spouštění testovacího okna v Odoo.

Tím se zobrazí prázdná okna „Vytvořit záznam“ a „Kontakt“.
informace (např. e-mailová adresa, mobilní telefon atd.) musí být vyplněny, aby mohl být proveden test
pracovat. Když je vložená potřebná informace, klikněte na tlačítko „Uložit a zavřít“.

.. obrázek: testing_running/blank-contact-form.png
:align:center
:alt: Prázdný kontaktní formulář z otestování okna s vyskakovacím oknem v Odoo Marketing Automation.

Po zadání všech potřebných polí klikněte na tlačítko „Uložit a zavřít“, abyste se vrátili do
Pop-up okno „Spustit test“.

Jakmile je kontakt vybrán, klikněte na tlačítko „Spustit“ (viz ikona vlevo dole), abyste zobrazili stránku testovací kampaně.

.. obrázek: testing_running/test-screen.png
:align:center
:alt:Testovací obrazovka v marketingové automatizaci Odoo.

Na stránce kampaně je vidět název zkoušeného záznamu a
přesný čas, kdy tento pracovní postup začal v poli „Zahájení práce“ .
Pod ní v části „Průběh“ je první aktivita (nebo aktivity).
testovaný pracovní postup.

K zahájení testu klikněte na tlačítko „Spustit“, které je reprezentováno ikonou „▶️ (hračka)“.
ikona vedle první aktivity v průběhu procesu. Po kliknutí se stránka načte a Odoo zobrazí
různé výsledky (a analýzy) spojené s tímto konkrétním činností, jakmile se objeví, v reálném čase.

.. poznámka::
Pokud je podřazená aktivita dítěte naplánována pod nadřazenou aktivitou, tato podřazená aktivita se zobrazí.
slabě vtažený do průběhu procesu, jakmile bude spuštěna jeho rodičovská aktivita, pomocí :guilabel:`▶
ikonu „Spustit“.

.. obrázek: testing_running/workflow-test-progress.png
:align:center
:alt:Průběh testování workflow v marketingovém automatizačním systému Odoo.

Jakmile jsou dokončeny všechny aktivity pracovního postupu, test končí a stavová lišta (v
v pravém horním rohu se přesune do fáze „Dokončeno“.

K ukončení testu před dokončením všech aktivit v procesu klikněte na tlačítko „Zastavit“
v horním levém rohu kampaně v testovací stránce.

Vyvíjejte kampaně
=============

Chcete-li spustit kampaň, přejděte do aplikace „Automatizovaná marketingová komunikace“ a vyberte požadovanou.
kampaň.

Na podrobnostech kampaně s připravenými aktivitami v seznamu :guilabel:`Průběh práce`.
sekci, klikněte na „Spustit“ v pravém horním rohu a oficiálně spusťte kampaň.
konfigurovaná cílová skupina uvedená v podrobnostech kampaně.

Kliknutím na tlačítko „Start“ spustíte kampaň a stavová lišta kampaně se změní na
„Běží“, které se nachází v pravém horním rohu podrobného formuláře kampaně.

.. obrázek: testing_running/campaign-running-status.png
:align:center
:alt:Stav kampaně se mění na běžící v horním pravém rohu.

.. poznámka::
Pokud někteří účastníci již běží na kampani a byla jim zastavena z jakéhokoliv důvodu, kliknutím
:guilabel:`Start“ tlačítko opět vyvolává upozornění v podobě okna s varováním. Toto upozornění radí uživateli, aby
Klikněte na tlačítko „Aktualizovat“ pro aplikaci jakýchkoliv změn, které provedete v kampani.

.... obrázek: testing_running/workflow-modification-warning.png
:synchronizace: střed
:alt:Změněn byl průběh kampaně, varovné okno bylo nahrazeno oznámením.

Věnujte pozornost tomu, že účastníci, kteří již prošli celou kampaní v původním stavu
** lze vrátit do nově upravené kampaně a vytvořit pro něj nové stopy.
jim.

Pak se při spouštění pošty a akcí v workflow zobrazí různé statistiky.
Každá aktivita má svůj vlastní blok, kde se zobrazují informace o dané aktivitě. Dále je zde série statistických
Chytré tlačítka, která se objevují v horní části formuláře s podrobnostmi o kampani.

Tyto analytické chytré tlačítka budou také naplňovat se skutečnými daty v průběhu kampaně:
:guilabel:`Šablony“, :guilabel:`Kliknutí“, :guilabel:`Testy“, :guilabel:"Účastníci".

.. obrázek: testování/testovani_kampaně_smajlíků.png
:align:center
:alt:Řada chytrých tlačítek, které se objevují v současně běžící marketingové kampani v Odoo.

Kampaň proti násilí na ženách
==============

Chcete-li zastavit kampaň, která právě probíhá, přejděte na:
Aplikace, vyberte požadovanou kampaň a v podrobnostech kampaně klikněte na
Tlačítko „Zastavit“ v pravém horním rohu.

.. obrázek: testovani_běhu/tlačítko-kampaně-v-průběhu-testu.png
:align:center
:alt: Tlačítko zastavení na běžném formuláři podrobností kampaně v aplikaci Odoo Marketing Automation.

Když je kampaň kliknutá, oficiálně se zastaví a stav se změní na:guilabel:`Stopped`
v pravém horním rohu formuláře s podrobnostmi kampaně.

... obrázek: testování běhu/kampaň zastavená stavová lišta.png
:align:center
:alt:Stav marketingové kampaně na podrobnostech kampaně v Odoo Marketing Automation.

.. viz též:
   - :doc:`Konfigurace kampaně <../marketing_automation>`
   - :doc:`cílová skupina`
   - :doc:`workflow_activities“
