... _ceny/ceny_a_často_kladené_dotazy:

===================
Sazebník a často kladené otázky
===================

Co potřebuji k odesílání SMS zpráv?
============================

Služba SMS Text Messaging je službou In-App Purchase (IAP), která vyžaduje předplacené kredity, aby fungovala.

Jaké druhy SMS existují?
=================================

Jsou dvě verze: GSM7 a UNICODE.

Standardní formát GSM7 má omezení na 160 znaků v jednom SMS a obsahuje
následujících znaků:

.. obrázek: ceny_a_faq/faq1.png
:align:center
:alt:Grafické znaky GSM7 jsou k dispozici v marketingu SMS Odoo.

Formát Unicode se používá v případě speciálního znaku, který není uveden v seznamu GSM7.
Limit pro jednu SMS: 70 znaků.

.. poznámka::
Pro GSM7 SMS je maximální velikost zprávy 160 znaků a pro Unicode 70. Nad tento limit se nepřenáší.
obsah je rozdělen do více částí* a počet znaků je snížen na 153 pro
7 a kód 67 pro Unicode. Systém pak v reálném čase zobrazuje počet odeslaných SMS zpráv.
zpráva představuje.

Jaká je cena za odeslání jednoho SMS?
=====================================

Cena SMS se odvíjí od destinace a délky zprávy (počtu znaků).
zprávu. Cenu za zemi najdete na webové stránce: `Odoo SMS - FAQ
<https://iap-services.odoo.com/iap/sms/cena#sms_faq_01>

Počet SMS, které zpráva představuje, bude vždy k dispozici v databázi.

.. obrázek: ceny_a_faq/faq2.png
:align:center
:alt: Počet znaků GSM7, které se vejdou do SMS v marketingu SMS Odoo.

Jak koupit kredity
==================

Přejděte na:menu:"Nastavení" --> "Koupit kredity".

.. obrázek: ceny_a_faq/faq3.png
:align:center
:alt: Nákup kreditů pro SMS marketing v nastavení Odoo.

Nebo přejděte na: `Nastavení --> Zobrazit mé služby`.

.. obrázek: ceny_a_faq/faq4.png
:align:center
:alt:Použití služby Odoo IAP k dobití kreditu pro marketingové SMS v nastavení Odoa.

..tip:
Pokud se používá verze SaaS společně s verzí Enterprise, je možné využít zkušební kredity.
k dispozici pro otestování funkce.

Častější otázky
=====================

#|**Je nějaká doba, po kterou jsou kredity platné?**
|Ne, kredity nevyprší.

#|**Můžu poslat SMS na telefonní číslo (které není mobilním telefonem), protože vidím ikonu
před zbytkem pole "telefon"?
|Pouze v případě, že dané telefonní číslo podporuje SMS (např. SIP telefony).

#|**Dostanu fakturu, když si koupím kredity?**
|Ano.

#. | **Může příjemce odpovědět mi?**
|Není možné odpovědět na SMS.

#|**Co se stane, když posílám více SMS najednou, ale nemám dostatek kreditu na jejich odeslání
všichni?**
|Pokud odesíláte více SMS najednou, počítá se to jako jedna transakce, takže žádné SMS nebudou
posílat, dokud nebudou kredity na všechny zprávy.

#| **Mám historii odeslaných SMS zpráv?**
|Historie odeslaných SMS včetně všech relevantních informací o kontaktech, které byly při odeslání SMS zadány.
samotná zpráva) se nachází v sloupci „Odeslané“ hlavního dialogu „SMS“.
Marketingový panel (při zobrazení v :guilabel:`Kanbanu`).

Pro podrobnější informace vyberte požadovanou SMS z hlavního panelu (v
:guilabel:`Kanban“). Klikněte na odkaz v modrém pruhu nad formulářem pro zobrazení podrobností o SMS.
aby se dozvěděli více.

#. | **Mohu posílat kolikrát chci SMS najednou?**
|Ano, pokud máte dostatek kreditů.

#|**Pokud bude odesláno SMS na číslo, které v seznamu příjemců není, budou kredity
ztracené?
|Ne, pokud je telefonní číslo nesprávně formátované (například příliš mnoho číslic).
Pokud je SMS zaslána špatnému člověku (nebo na falešné číslo), kredit za tuto SMS bude ztracen.

#Co se stane, když poslám svou SMS na placené číslo (např.: soutěž o vstupenku do kina)?
(festival)?**
|SMS se na takové číslo nedoručí, proto nebudou účtovány žádné poplatky.

#|**Mohu identifikovat čísla, která neexistují, když posílám několik SMS zpráv?**
| Jen ty, které mají neplatný formát.

#. | **Jak se tento servis dotýká nařízení GDPR?**
|Najdete ji zde <https://iap.odoo.com/privacy#sms>.

#. | **Mohu používat vlastní poskytovatele SMS?**
|Ano, ale není možné to udělat přímo z balíčku.Odoo odborníci mohou pomoci s přizpůsobením databáze tak, aby umožnila
pro používání osobního poskytovatele SMS. Podívejte se na naše balíčky úspěchu zde
<https://www.odoo.com/cena-balíčků>.
