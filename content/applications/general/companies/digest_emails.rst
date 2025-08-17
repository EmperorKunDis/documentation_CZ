=============
Pročistěte si e-mailovou schránku
=============

„E-maily s výstupem“ jsou periodické snímky zasílané e-mailem uživatelům v organizaci, které obsahují
informace o výkonnosti podniku na vysoké úrovni.

Chcete-li začít odesílat souhrnné emaily, začněte tím, že se přesunete na:
sekci, aktivujte funkci „Zpracování e-mailů“ a klikněte na „Uložit“.

.. obrázek: digest_emails/digest-email-settings.png
:align:center
:alt: sekce Digest Emails v obecných nastaveních.

Pro nastavení e-mailů s výpisem lze použít různé možnosti, například:

- Rozhodování o tom, které „klíčové ukazatele výkonnosti“ jsou sdíleny v e-mailech s přehledy
- Určení, jak často jsou zasílány e-maily s informacemi o stavu objednávky
- Volba, kdo v organizaci dostane e-maily s výběrem
- Vytváření vlastních šablon e-mailů s přehledem
- Přidání dalších KPI (klíčových ukazatelů výkonnosti) (*Studiová aplikace*)

.. poznámka::
Výchozí nastavení zahrnuje funkci „Digest Email“. Funkce „Odoo Periodic“ je vždy zapnutá.
Digest slouží jako hlavní šablona, která obsahuje všechny klíčové ukazatele výkonnosti.
indikátorů) v rámci celé databáze Odoo a je zasílán každý den správcům.

.. varování:
Při vytváření duplikátů databází s možností odesílání (ne testovací režim)
Pokud nechcete dostávat e-maily s výpisem z databáze duplicitních účtů, je třeba tyto e-maily vypnout.

Chcete-li vypnout e-mail s výpisem, přejděte na: „Nastavení“ -> „Statistiky“.
Pak deaktivujte funkci „Zasílání zpráv v digestu“ odškrtnutím políčka a kliknutím na
:guilabel:`Uložit“. Viz část o :ref:`digest-emails/deaktivovat`.

.._zpracovávat emaily/upravit zpracování emailů:

Upravte výchozí e-mail s přehledem
==============================

Pro přizpůsobení výchozího e-mailu s výpisem (e-mail *Vaše pravidelná zpráva Odoo*) přejděte na: `Nastavení
app --> Statistiky --> pole „Digest Email“ a poté vyberte „Vaše období v Odoo“.
Digest“ a klikněte na ikonu „↗️ (Externí odkaz)“, která se nachází vedle vybraného položkového menu.

Zobrazí se okno s různými nastaveními, mezi nimiž je například:

- :guilabel:„Jméno e-mailu s přehledem“: jméno e-mailu s přehledem.
- „Periodicita“: kontrolujte, jak často jsou zasílány e-maily s výstupy z analýz („denně“,
:guilabel:"Týdenní", :guilabel:"Měsíční" nebo :guilabel:"Čtvrtletní".
- :guilabel:`Datum dalšího odeslání“: datum, kdy bude zaslána další zpráva.
- :guilabel:`KPI“ tabulka: zkontrolujte nebo odškrtněte každý vypočítaný „KPI (klíčový ukazatel výkonnosti)“.
se objevuje v emailech s výpisem. Zaškrtnutá políčka ukazují na aktivní :abbr:`KPI (klíčový ukazatel výkonnosti)`
v e-mailu s výběrem. Podívejte se na část o :ref:`e-mailech s výběrem/kpis`.
- :guilabel:`Příjemci‘: přidat/odebrat uživatele, kteří dostávají e-maily s výběrem. Viz část
:ref:`souhrn e-mailů/adresáti“.

.. poznámka::
KPI lze upravit pomocí Odoo Studio.
Náklady na databázi jsou účtovány v případě, že je potřeba nainstalovat Studio. Viz tento
sekci o :ref:`souhrnných emailech/vlastních KPI“.

.. obrázek: digest_emails/periodic-digest.png
:align:center
:alt: Upravte výchozí nastavení e-mailu s přehledem a vlastními klíčovými ukazateli výkonnosti (KPI).

..._souhrnné e-maily/deaktivovat:

Deaktivujte e-mail s výpisem příspěvků
=======================

Chcete-li ručně vypnout jednotlivý e-mailový zpravodaj, nejprve přejděte do aplikace „Nastavení“.
V sekci „Statistiky“ a klikněte na tlačítko „Nastavení e-mailů s přehledem“. Poté vyberte požadovanou
zpracovat e-mail ze seznamu, který by měl být odstraněn.

Dále klikněte na :guilabel:`ZAKÁZAT PRO VŠECHNY`, abyste zakázali e-mailovou zprávu s výběrem pro všechny.
:guilabel:`ODEBRAT MĚ“ pro odhlášení uživatele z odběru. Tlačítka
je umístěna v horním menu, hned nad položkou „Jméno trávicího traktu“.

Odeslat e-mail s výběrem
==========================

Chcete-li odeslat manuálně výstup e-mailu s agregovanými daty, nejprve se přihlaste do aplikace „Nastavení“ a poté klikněte na „Statistiky“.
sekci“Nastavení e-mailů s agregovanými informacemi“ a klikněte na „Upravit e-maily s agregovanými informacemi“. Poté vyberte požadovaný e-mail s agregací informací,
Klikněte na tlačítko „ODESLAT TEĎ“. Toto tlačítko je umístěno v horním menu, hned nad tlačítkem „Souhrn
Jméno.

.._souhrnné e-maily/kpis:

KPI
====

Přednastavené KPI (klíčové ukazatele výkonnosti) lze přidat do shrnutí e-mailu z
:guilabel:„KPI“ v e-mailovém šablonu pro formulář s přehledem.

Nejprve přejděte do aplikace Nastavení: „Aplikace“ --> „Statistiky“, a klikněte
:guilabel:`Nastavit e-maily s hašem“.

Pak vyberte požadovaný e-mail s výstupem a otevřete záložku „KPI“.

Chcete-li přidat klíčový ukazatel výkonnosti (KPI) do zprávy o stavu, zaškrtněte políčko vedle
požadované: zkratka KPI (klíčový ukazatel výkonnosti). Po všem: zkratka KPI (klíčové ukazatele výkonnosti)
klikněte na tlačítko „Uložit“.

Následující :abbr:`KPI (klíčové ukazatele výkonnosti)` jsou k dispozici v záložce
vzor e-mailu s výpisem v Odoo:

.. obrázek: digest_emails/oob-kpis.png
:synchronizace: vpravo
:alt:KPI uvedené v e-mailu s přehledem zpráv.

:guilabel:`Obecný“
   - :guilabel:`Připojené uživatele“
   - :guilabel:`Zprávy“

:guilabel:`Projekt“
   - :guilabel:`Otevřené úkoly“

:guilabel:`Nábor“
   - :guilabel:`Zaměstnanci“

:guilabel:`CRM“
   - :guilabel:`Nové příležitosti“
   - :guilabel:`Získané příležitosti“

:guilabel:`Prodej“
   - :guilabel:`Všechny prodeje“
   - :guilabel:`Prodej na internetu“

:guilabel:`Pokladna“
   - :guilabel:`Prodej na prodejně“

:guilabel:`Živý chat“
   - :guilabel:`% štěstí“
   - :guilabel:`Řešené konverzace“
   - :guilabel:`Čas na odpověď (s)`

:helpdesk
   - :guilabel:Zavřené vstupenky

:guilabel:`Fakturace“
   - :guilabel:`Příjem“
   - :guilabel:`Banky a pohyb peněz“

..._souhrnné e-maily/adresáti:

Příjemci
==========

Příjemci zprávy o sledování jsou přidáváni ze záložky „Zpracovatelé“ v šabloně e-mailu o sledování.
forma.

Chcete-li přidat příjemce, přejděte do aplikace „Nastavení“ -> „Statistiky“ a klikněte
Konfigurace e-mailů s výběrem požadovaného e-mailu a otevřením
:guilabel:`Příjemci“ záložka.

K přidání příjemce klikněte na tlačítko „Přidat řádek“ a poté vyberte možnost „Přidat příjemce“.
je zobrazena se všemi dostupnými uživateli jako příjemci.

V okně s náhledem zatrhněte zaškrtávací políčko vedle názvu uživatele (uživatelů) a klikněte na
Tlačítko „Vybrat“.

Pro odstranění uživatele jako příjemce klikněte na ikonu „❌ (odstranit)“ vpravo vedle uživatele.
je uveden v záložce „Příjemci“.

Klikněte na tlačítko „Uložit“ pro zavedení změn.

..._souhrnné e-maily/vlastní e-maily:

Vytvořit zprávy s výběrem
====================

Pro vytvoření nového e-mailu s výpisem přejděte do: „Nastavení aplikace --> Statistiky“
Klikněte na tlačítko „Nastavit e-maily s agregací“. Pak klikněte na „Vytvořit“ pro vytvoření nové agregace.
e-mail.

Na samostatné stránce se objeví vzor e-mailu s výpisem příspěvků, který je možné upravit.
Nastavení, včetně:

- :guilabel:„Jméno e-mailu s přehledem“: jméno e-mailu s přehledem.
- „Periodicita“: kontrolujte, jak často jsou zasílány e-maily s výstupy z analýz („denně“,
:guilabel:"Týdenní", :guilabel:"Měsíční" nebo :guilabel:"Čtvrtletní".
- :guilabel:`Datum dalšího odeslání“: datum, kdy bude zaslána další zpráva.
- :guilabel:`KPI“ tabulka: zkontrolujte nebo odškrtněte každý vypočítaný „KPI (klíčový ukazatel výkonnosti)“.
se objevuje v emailech s výpisem. Zaškrtnutá políčka ukazují na aktivní :abbr:`KPI (klíčový ukazatel výkonnosti)`
v e-mailu s výběrem. Podívejte se na část o :ref:`e-mailech s výběrem/kpis`.
- :guilabel:`Příjemci‘: přidat/odebrat uživatele, kteří dostávají e-maily s výběrem. Viz část
:ref:`souhrn e-mailů/adresáti“.

Od této chvíle přidejte do e-mailu s výběrem příspěvků :guilabel:`Jméno výběru`, zadejte :guilabel:`Četnost`
Vyberte požadované :abbr:`KPI (klíčové ukazatele výkonnosti)` a přidejte :guilabel:`Příjemce“, jak je
nebyla nutná.

Po kliknutí na tlačítko „Uložit“ je nový vlastní e-mail s přehledem dostupný jako volba ve
:guilabel:`Digest e-mail“ pole v sekci „Nastavení aplikace – Statistiky“.

... _zpracovávat emaily/vlastní KPI:

Sestavte si vlastní KPI s Odoo Studio
============================

Vzor e-mailu s přehledem obsahuje klíčové ukazatele výkonnosti (KPI).
:guilabel:„KPI“ tabulka lze upravit pomocí nástroje „Odoo Studio“.

.. varování:
Při používání databáze se účtují další náklady na předplatné.
nainstalovány.

Nejprve klikněte na ikonu „🛠️“ v pravém horním rohu obrazovky. Toto je odkaz na
aplikace Odoo *Studio*.

Chcete-li vytvořit další pole, vytvořte dvě pole na objektu hash:

#Vytvořte pole s logickou hodnotou nazvané „kpi_myfield“ a zobrazte jej v záložce „KPI“.
#Vytvořte pole s počítanou hodnotou nazvané kpi_myfield_value, které vypočítává vlastní klíčové ukazatele výkonnosti (zkratka KPI).
výkonnostní ukazatel`.
#Vyberte klíčové ukazatele výkonnosti (KPI) v záložce KPI.

.. tip::
Zde je zdrojový kód
<https://github.com/odoo/odoo/blob/15.0/addons/digest/models/digest.py>`_ pro soubor `digest.py
soubor, který programátorovi pomáhá při kódování vypočítaného pole.

.. viz též:
Uživatelé mohou také kliknout na záložku „Příjemci“ a poté na vertikální tři tečky.
:guilabel:`(kebab)“ nabídku pro editaci tohoto pohledu. Klikněte buď na :guilabel:`EDIT LIST VIEW“ nebo
:guilabel:`Upravit formulář“ k tomuto záložce.

Tabulka odkazující na hodnoty vypočítané
-------------------------------

+-----------------------+-------------------------------------------+
|Štítek                  |Hodnota                                         |
+=======================+===========================================+
|Připojené uživatele      | `kpi_res_users_connected_value`           |
+-----------------------+-------------------------------------------+
|Počet odeslaných zpráv|`kpi_mail_messages_sent_total_value`           |
+-----------------------+-------------------------------------------+
|Nové kontakty           | ‚kpi_crm_lead_created_value‘            |
+-----------------------+-------------------------------------------+
|Získané příležitosti      |`kpi_crm_opportunities_won_value`          |
+-----------------------+-------------------------------------------+
|Otevřené úkoly         |  kpi_projekt_úkol_otevřený_hodnota       |
+-----------------------+-------------------------------------------+
|Zavřené požadavky      |`kpi_helpdesk_tickets_closed_value`         |
+-----------------------+-------------------------------------------+
|Procento štěstí           |Hodnota ukazatele kpi_livechat_rating    |
+-----------------------+-------------------------------------------+
|Počet řešených konverzací | `kpi_livechat_conversations_value`          |
+-----------------------+-------------------------------------------+
Čas na odpověď (s)     |`kpi_livechat_response_value`              |
+-----------------------+-------------------------------------------+
|Všechny prodeje           |`kpi_all_sales_total_value`               |
+-----------------------+-------------------------------------------+
|Prodej přes internet     |  kpi_web_prodeje_celkem                      |
+-----------------------+-------------------------------------------+
|Tržby                  |`kpi_account_total_revenue_value`          |
+-----------------------+-------------------------------------------+
|Bankovní a hotovostní pohyby |  kpi_account_bank_cash_value |
+-----------------------+-------------------------------------------+
|Prodej na prodejně         |`kpi_pos_total_value`                      |
+-----------------------+-------------------------------------------+
|Noví zaměstnanci       |`kpi_hr_recruitment_new_employees_value` |
+-----------------------+-------------------------------------------+
