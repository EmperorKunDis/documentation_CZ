==========================================
Vytvořit časové listy při ověření dovolené
==========================================

Odoo automaticky vytváří docházkové listy na projekty a úkoly při žádostech o volno. To umožňuje lepší
celkové kontrole ověřování docházky, neboť nezbývá místo na zapomínání
a dotazy po pracovní době, které nebyly zaznamenány v hodinách.

Aktivujte režim vývojáře (:ref:`vývojářský režim <developer-mode>`), přejděte do části *Záznamy o pracovní době* a změňte projekt.
a úkoly, které jsou nastavené výchozí hodnotou, pokud se vám líbí.

.. obrázek: time_off/record_time_off.png
:align:center
:alt: Zobrazení nastavení časových záznamů, které umožňuje zaznamenat dovolenou v Odoo Timesheets

Přejděte na „Čas volna –> Konfigurace –> Druhy času volna“. Vyberte nebo vytvořte
požadovaný typ a rozhodnout se, zda chcete požadavky ověřovat nebo ne.

.. obrázek: time_off/time_off_types.png
:align:center
:alt: Pohled na typy volna s důrazem na požadavky na dovolenou a mzdy
Odoo Time Off

Nyní, když zaměstnanec požádal o dovolenou a žádost byla schválena (nebo ne),
podle nastavení (v případě automatického přidělování času na Timesheety), je čas přiřazen na Timesheety.
respektive projekt a úkol.
|V následujícím příkladu uživatel požadoval „Čas dovolené“ od 13. do 15. července.

.. obrázek:: volno/požadavek na dovolenou.png
:align:center
:alt: Zobrazení žádosti o dovolenou v Odoo Time Off

Vzhledem k tomu, že validace není vyžadována, požadovaný čas dovolené se automaticky zobrazí v
*Časové listy*. Pokud je nutná kontrola, čas se automaticky přidělí po schválení
Tohle dělá osoba, která ověřuje.

.. obrázek:: time_off/timesheets.png
:align:center
:alt:Video s časovými listy, které zdůrazňují požadovaný čas volna zaměstnance v aplikaci Odoo Timesheets

Klikněte na zvětšovací sklo a přejděte nad buňkou, kterou chcete zobrazit, abyste měli k dispozici všechna agregovaná data.
na daném buňce (den) a zobrazit podrobnosti projektu/úkolu.

.. obrázek:time_off/timesheet_description.png
:align:center
:alt: Zobrazení podrobností projektu/úkolu v Odoo Timeheets
