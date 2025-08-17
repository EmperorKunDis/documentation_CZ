Zobrazit obsah

================
Sociální marketing
================

Aplikace Social Marketing společnosti Odoo pomáhá obsahovým marketérům vytvářet a plánovat příspěvky a spravovat
různé sociální média, analyzovat účinnost obsahu a přímo se zapojit do sociálních sítí
Sledující v jednom centrálním místě.

.. viz též:
   - „Tutoriály Odoo: Marketing <https://www.odoo.com/slides/marketing-27>“

.. karty:

.......karta: Sociální sítě
:target: marketing/sociální sítě

Zjistěte vše, co potřebujete vědět o tom, jak vytvářet a upravovat příspěvky na sociálních sítích
pomocí Odoo.

......karta: Sociální kampaně
:cíl: marketing sociální/kampaně

Zjistěte, jaké nástroje pro kampaně a marketing tato aplikace nabízí.

Sociální média
=====================

Odoo Social Marketing je nástroj pro vytváření sociálních příspěvků a analýzu obsahu.
účty musí být přidány jako „proud“ na hlavní ploše aplikace.

.. poznámka::
Pozor, osobní profily nelze přidat jako stream. Hlavním účelem aplikace Odoo Social je zobrazit obsah
Marketing* má na starosti správu a analýzu firemních účtů na sociálních sítích.

.. varování:
Odoo Social Marketing má některé omezení v oblasti sociálních médií. Například
Odoo **není schopna zpracovat velké množství různých stránek (např. ~ 40 stránek) pod jednou společností.
Stejné limity jsou přítomny v prostředí více společností kvůli tomu, jak je API implementováno.
postaveny.

.. varování:
V prostředí více společností se může stát, že každá společnost neaktivuje stránku najednou.
v chybě povolení.

Příkladem je například, že pokud je společnost 1 jedinou vybranou společností z hlavního panelu Odoo,
aktivuje stránky Facebook Page 1 a Facebook Page 2, pak se tyto stránky zobrazí na
Dashboard pro sociální marketing.

Avšak pokud na stejné databázi uživatel přidá společnost 2 z nabídky firem v rozevíracím seznamu
hlavičku a pokusí se přidat stejné streamy, což způsobí chybu při oprávnění.

.... obrázek:social_marketing/permission-error.png
:synchronizace: střed
:alt:Pohled na chybu povolení, která se objeví při nesprávném pokusu o přidání streamu.

Sociální média
====================

Pro přidání účtu sociálních médií jako proudu přejděte na: „Sociální marketing“.
Aplikace a vyberte tlačítko „Přidat stream“ v horním levém rohu.
zobrazí okno „Přidat stream“.

.. obrázek: social_marketing/add-stream-social-popup.png
:align:center
:alt:Zobrazení okna, které se objeví při výběru možnosti Přidat stream v Odoo.

V okně „Přidat stream“ vyberte možnost „Propojit nový účet“.
podnikání na kterékoliv z následujících populárních sociálních sítí: :guilabel:`Facebook`
:guilabel:'Instagram', :guilabel:'LinkedIn', :guilabel:'Twitter' a :guilabel:'YouTube'.

Po kliknutí na požadovaný sociální média z okna „Přidat proud“ se Odoo
přesměruje přímo na stránku autorizace konkrétního sociálního média, kde je potřeba
aby byl přidán konkrétní účet sociální sítě jako proud do sekce *Sociální média.
Marketingová aplikace.

.. obrázek:social_marketing/social-marketing-dashboard.png
:align:center
:alt:Příklad obsazeného sociálního panelu s přehledy sociálních médií a obsahu.

Jakmile je povolení uděleno, Odoo se vrátí na hlavní stránku k položce „Krmivo“.
příkazem „Sociální marketing“ a novou sloupcovou tabulkou s příspěvky tohoto účtu.
Účty a streamy můžete přidávat kdykoliv.

.. důležité:
Stránku „Facebook“ lze přidat, pokud je k dispozici účet „Facebook“, který umožňuje
K udělení souhlasu je oprávněn správce stránky, a mělo by se také zmínit, že různé stránky mohou mít
pro různé proudy.

.. poznámka::
:guilabel:`Instagram“ účty se přidávají pomocí přihlášení na :guilabel:`Facebooku“, protože používá
Stejná API. To znamená, že účet na Instagramu musí být propojený s
:guilabel:`Facebook“ účet, aby se zobrazila jako proud v Odoo.

Stránka na sociálních sítích
=================

Další způsob, jak rychle propojit sociální média s aplikací Odoo Social Marketing, je provést na
:guilabel:Stránka sociálních médií. Chcete-li zobrazit stránku sociálních médií, přejděte na
:menuselection:„Aplikace pro sociální marketing“ --> „Konfigurace“ --> „Sítě“.

Na stránce „Sociální média“ je k dispozici seznam všech možností sociálních sítí.
s tlačítkem pro připojení účtu :guilabel:`Link account` - :guilabel:`Facebook`, :guilabel:`Instagram“,
:guilabel:`LinkedIn“, :guilabel:`Twitter“, :guilabel:`YouTube“ a :guilabel:`Push Notifications“.

.. obrázek: social_marketing/social-media-page.png
:align:center
:alt: Pohled na sociální média v aplikaci Odoo Social Marketing.

Stránka sociálních účtů
====================

Seznam všech sociálních účtů a webových stránek spojených s databází najdete na
:menuvolba:„Social Marketing app“ -> „Konfigurace“ -> „Společenské účty“. Tato volba:„Social
Zobrazuje se jméno, zkratka a sociální sítě.
Platforma médií, kdo ji vytvořil: „Vytvořeno“ a „Společnost“, ke které patří
související.

.. obrázek:social_marketing/social-accounts-page.png
:align:center
:alt: Pohled na stránku sociálních účtů v aplikaci Odoo Social Marketing.

Upravit nebo změnit jakýkoliv účet na této stránce je velmi snadné.
seznam na této stránce a pokračujte v provádění případných úprav.

Stránka sociálních proudů
===================

Prohlédnout samostatnou stránku s veškerými sociálními médii, které byly přidány do hlavní *Social
Marketingový panel, přejděte na: menuselection:„Aplikace pro sociální marketing --> Konfigurace --> Sociální
Přímé přenosy.

.. obrázek: social_marketing/social-streams-page.png
:align:center
:alt: Pohled na stránku sociálních účtů v aplikaci Odoo Social Marketing.

Zde je informace z sociálních sítí uspořádané v seznamu s :guilabel:`Sítěmi sociálními`.
Název kanálu, typ kanálu (např. „Zprávy“).
„Klíčové slovo“, „Vytvořeno“ a „Společnost“ atd.
Je s ní spojeno.

Pro úpravu informací o jakémkoli přenosu stačí kliknout na požadovaný přenos v seznamu a poté pokračovat
udělat všechny potřebné úpravy.

Návštěvníci
========

Prohlédnout si kompletní přehled všech návštěvníků webových stránek spojených s
databáze, přejděte na: menu-vyber->Sociální marketingová aplikace - Návštěvníci.

.. obrázek:social_marketing/návštěvníci.png
:align:center
:alt: Zobrazení stránky Návštěvníků v aplikaci Odoo Social Marketing.

Odoo zde poskytuje podrobný seznam všech relevantních informací o návštěvnících v přednastaveném kartách
zobrazení. Pokud uživatelé mají v databázi kontaktní údaje, mohou je odeslat
E-mailová a/nebo SMS zpráva je k dispozici.

Tato stejná návštěvní data lze také zobrazit jako seznam nebo graf. Tyto možnosti jsou umístěny v
v pravém horním rohu stránky „Návštěvníci“.

.. toctree::

marketing_sociální/sociální_posty
sociální marketing/kampaně
