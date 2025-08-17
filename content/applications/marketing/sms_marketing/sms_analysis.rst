============
Analýza SMS
============

Na stránce „Zprávy“ (přístupné přes možnost „Zprávy“ v
hlavičkový menu, jsou zde možnosti použití různých kombinací filtrů a
:guilabel:`Metriky“ k zobrazení metrik v několika různých formátech (např.
„Seznam“, „Skupina“ a „Kohorta“ (viz obrázky).

Každá možnost zobrazení metriky „Reporting“ umožňuje podrobnější analýzu výkonnosti
SMS zprávy.

Příkladem je například v výchozím pohledu „Graf“ zobrazení dat SMS (Short Message Service)
je vizualizována jako různé grafy a tabulky, které lze třídit a seskupovat různými způsoby (např.
:guilabel:`Měření“ v rozevíracím seznamu.

.. obrázek: sms_analysis/sms-reporting-page.png
:align:center
:alt:Stránka pro reportování v SMS marketingu.

..tip:
SMS lze odesílat pomocí automatizačních pravidel v Odoo. Pro použití Odoo *Studia* je nutné
automatizace.

Pro instalaci aplikace Odoo Studio přejděte do aplikace Apps. Poté použijte
:guilabel:`Vyhledávání ...“ lišta, vyhledejte „studia“.

Pokud není již nainstalovaný, klikněte na tlačítko :guilabel:`Instalovat“.

Přidáním aplikace Studio se stav předplatného změní na Custom, což zvyšuje
náklady. Pro další informace navštivte stránku „Podpora“ nebo se obraťte na databázi
úspěšný zákazník, se všemi dotazy týkajícími se změny.

Chcete-li používat automatizační pravidla, přejděte do režimu vývojáře :ref:`<developer-mode>`.
:menu: „Nastavení aplikace --> Technické menu --> Automatizace --> Automatizační pravidla“.
Pak klikněte na tlačítko „New“ pro vytvoření nové pravidlo.

Zadejte název automatické pravidlo a vyberte model, na který chcete tento pravidlo aplikovat.

Na základě výběru v poli Trigger se doplní další pole níže.
zapnout spoušť na některé z následujících možností:

:guilabel:`Hodnoty aktualizovány“

   - :guilabel:`Uživatel je nastaven“
   - Stát je připravený
   - :guilabel:`Archivované“
   - :guilabel:`Nevymazáno“

:guilabel:`Podmínky měření“

   - Založeno na poli Datum
   - :guilabel:Po vytvoření
   - :guilabel:`Po poslední aktualizaci“

:guilabel:`Vlastní“

   - :guilabel:`Na uložení“
   - :guilabel:`Na smazání“
   - :guilabel:`Na změnu uživatelského rozhraní“

:guilabel:`Externí“

   - guilabel:Webhook

Jiné možnosti se mohou zobrazit na základě vybraného modelu. Například pokud je
:guilabel:`Událost v kalendáři“ je vybrán, pak se objeví následující možnosti navíc k
ty, kteří jsou nad nimi:

:guilabel:`E-mailové události“

   - :guilabel:`Na příchozí zprávu“
   - :guilabel:`Na odchozí zprávě“

V poli „Před aktualizací domény“ nastavte podmínku, která musí být splněna před aktualizací
Záznam. Klikněte na tlačítko „Upravit doménu“ a nastavte parametry záznamu.

Pod záložkou „Co je třeba udělat“ vyberte možnost „Přidat akci“. V následném dialogovém okně zvolte
okně „Vytvořit akci“ vyberte možnost „Odeslat SMS“ a nastavte
:guilabel:`Dovolené skupiny“. Dovolené skupiny jsou přístupová práva, která je
tuto pravidlo může vykonávat. Nechte pole prázdné, aby všechny skupiny mohly provádět tento postup. Podívejte se na tuto dokumentaci:
:ref:`přístupová práva/skupiny`.

Poté nastavte šablonu pro SMS zprávy a vyberte, zda má být odeslaná SMS zpráva uložena.
poznámku, vyberte možnost v rozbalovacím seznamu: „Odeslat jako“. Klikněte
:guilabel:`Uložit a zavřít“ k uložení změn v této nové akci.

...... obrázek: sms_analysis/automation-rule-sms.png
:synchronizace: střed
:alt:Šablona automatizace s pravidlem pro provedení akce, šablonou SMS a záznamem jako poznámkou zvýrazněna.

Přidejte všechny potřebné poznámky pod záložkou „Poznámky“. Nakonec přejděte na jinou stránku.
dokončená automatická pravidla nebo ručně uložit (kliknutím na ikonu :guilabel:`☁️ (mraky)`).
zavést změnu.
