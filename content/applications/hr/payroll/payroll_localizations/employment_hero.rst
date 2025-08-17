=======================
Hrdina zaměstnavatele
=======================

Modul „Employment Hero <https://employmenthero.com/>“ synchronizuje účetní záznamy o platbách v mzdovém účetnictví
(např. výdaje, sociální odvody, závazky, daně) automaticky ze systému Employment Hero do Odoo.
Mzdová agenda je stále vedená v aplikaci Employment Hero, ale **účetní záznamy** jsou prováděny
Odoo.

.. důležité::
V březnu 2023 dojde k přejmenování společnosti KeyPay na **Hrdinu zaměstnání**.

.. konfigurace:

Konfigurace
-------------

#Aktivujte modul „Mzdy“ pomocí příkazu „Nainstalovat“.
(„l10n_employment_hero“).
#Konfigurujte **API Employment Hero** přejděte na: „Účetnictví -> Konfigurace
--> Nastavení. Po kliknutí na pole „Zapnout Employment Hero“ se zobrazí další položky
„Integrace“.

.... obrázek:: employment_hero/employment-hero-integration.png
:alt:Povolení integrace aplikace Employment Hero do účetnictví Odoo zobrazí nová pole v
nastavení

   - API klíč najdete v sekci „Můj účet“ na platformě Employment Hero.

...... obrázek:: employment_hero/employment-hero-myaccount.png


   - V poli „Mzda“ je výchozí hodnota prázdná, aby se předešlo záměně. Prosím vyplňte ji podle
k dokumentaci specifické pro lokalizaci.

.. poznámka::
Hrdina zaměstnanosti je k dispozici pro :ref:`Austrálii <payroll/l10n_au/employment-hero>`.
Malajsie:ref:`<malaysia/employment-hero>`
:ref:`Nový Zéland <novy-zalan/prace-hero>`,
Singapur:ref:`<singapore/employment-hero>`
a v :ref:`Spojeném království <localization/united-kingdom/employment-hero>.

   - ID podniku najdete v adrese webové stránky společnosti Employment Hero (např. 189241).

.... obrázek:: employment_hero/employment-hero-business-id.png
:alt:Číslo podniku Employment Hero je v adrese URL

   - Vyberte si v Odoo jakýkoliv účetní deník, kam budete zadávat výplatní pásky.
#Konfigurace daně se provádí v menu: „Účetnictví“ - „Nastavení“ - „Daně“. Vytvořte
potřebné daně pro výplatní pásky od společnosti Employment Hero. Zadejte daňový kód
**Hrdina zaměstnání** v poli „Soulad s daní Hrdiny zaměstnání“.

Jak funguje API?
----------------------

API synchronizuje záznamy z knihy pracovních úkolů v aplikaci Employment Hero s Odoo a nechává je ve stavu návrhu.
reference zahrnuje identifikační číslo platové složenky od společnosti Employment Hero v uvozovkách, aby byl pro uživatele snadno dostupný.
stejný záznam v aplikaci Employment Hero a Odoo.

.. obrázek: zamestnanec-hrdina/zamestnanec-hrdina-casopisne-clanky.png
:alt: Příklad záznamu v deníku zaměstnance v účetnictví Odoo (Austrálie)

Výchozí nastavení je jednou za týden. Záznamy lze ručně stahovat kliknutím na
V menu „Účetnictví“ -> „Konfigurace“ -> „Nastavení“ a v poli „Zapnout
Vyberte možnost „Spojení s aplikací Employment Hero“ a klikněte na „Stáhnout platby ručně“.

Příjmy v mzdovém výměru od společnosti Employment Hero fungují na principu dvojího účetnictví.

Účty používané společností Employment Hero jsou definovány v části „Nastavení mzdy“.

.. obrázek: zamestnanec_hrdina/zamestnanec-hrdina-evidence-tržeb.png
:alt:Nápověda k položce „Účetnictví“ v aplikaci Employment Hero

Pro funkci API je nutné vytvořit stejná uživatelská jména jako výchozí účty společnosti Employment Hero.
podnikání (**stejné jméno a stejný kód**) v Odoo. V Odoo je nutné vybrat správnou položku typu účtu.
generovat přesné finanční zprávy.
