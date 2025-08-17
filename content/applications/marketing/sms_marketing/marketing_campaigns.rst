=====================
Nastavení kampaně SMS
=====================

Používání kampaní SMS (Short Message Service) s Odoo *SMS Marketing* není jen
účinná reklama, je také skvělý způsob, jak připomenout lidem blížící se události.
vystavené faktury a mnoho dalšího.

Ale předtím, než se mohou vytvářet a odesílat kampaně SMS (Short Message Service), musí být splněny některé konkrétní
musí být nejprve povoleny nastavení a funkce.

Nastavení SMS kampaně
====================

Pro umožnění kampaní SMS (Short Message Service) v Odoo zajistěte, aby byly zapnuté služby *Mailing Campaigns*.
tuto funkci lze aktivovat přechodem na: „E-mailový marketing“ -> „Konfigurace“ -> „Nastavení“,
a poté zapnout „Poštovní kampaně“ a „Uložit změny“.

.. obrázek: marketing_kampane/sms-mailing-kampane.png
:align:center
:alt: Pohled na nastavení kampaně v Odoo.

.. poznámka::
Pro aktivování funkce *Poštovní kampaně* v sekci *Obecné nastavení* je zapotřebí také povolit funkci *Test A/B*.
funkcí.

Jakmile je nastavení zapnuté, přejděte zpět do aplikace SMS marketing a zkontrolujte
Hlavička „Kampaň“ je nyní k dispozici pro použití. Podobně jako hlavička „Test A/B“.
je nyní dostupný také na každém šablonovém formuláři SMS (služba krátkých zpráv).

Testy A/B
=========

:guilabel:`A/B Testy“ umožňují testovat jakýkoliv „SMS (Krátký textový servis)“ e-mail.
další verze v rámci stejné kampaně, abyste porovnali, která verze je nejúspěšnější.
produkují zapojení a/nebo konverze.

Na šabloně SMS pod záložkou A/B testy
Začíná se jediným zaškrtávacím políčkem s názvem „Povolit testování A/B.“

Když na něj kliknete, objeví se další možnosti.

.. obrázek: marketing_campaigns/ab-tests-sms.png
:align:center
:alt:Tab pro testování A/B je umístěn na formuláři kampaně v aplikaci SMS marketingu Odoo.

V prvním poli zadejte požadovaný podíl příjemců, na kterých chcete provést test A/B.

Pod procentuální políčko je pole „Výběr vítěze“, což je to, co používá Odoo.
určit úspěšný výsledek testu A/B. Jinými slovy, tento parametr říká Odoo, jaký
vítězný test A/B.

Následující sekce jsou dostupné: „Manuál“, „Nejvyšší kliknutí“,
:guilabel:`Příležitosti“, „Kalkulace“ nebo „Tržby“.

Poslední políčko je „Odeslat konečné“. To znamená datum a čas, který používá Odoo.
jako termín pro určení vítězné verze newsletteru. Poté Odoo odesílá právě tuto vítěznou verzi
změnu pro zbývající příjemce, kteří se testu neúčastnili, ke dni předchozímu.
čas.

..tip:
Rychle vytvořte různé verze e-mailu a přidejte je do testování A/B kliknutím na
:guilabel:`Vytvořit alternativní verzi“ tlačítko.

.. poznámka::
Pamatujte na to, že vítězná varianta e-mailu je založena na kritériích vybraných v
:guilabel:`Výběr vítěze“ pole.

Stránka kampaně
==============

Pro vytváření, úpravu nebo analýzu jakékoliv kampaně klikněte na položku „Kampaně“ v horním menu.
Aplikace „Marketing SMS“. Na stránce „Kampaně“ se zobrazují různé
informace o kampani spojené s těmito rozesílkami (např. počet e-mailů, sociální
příspěvky, SMS a oznámení).

.. obrázek: marketing_campaigns/kampaně.png
:align:center
:alt:Pohled na různé kampaně v aplikaci Odoo SMS Marketing oddělené podle fáze.

Šablony kampaně
==================

Klikněte na tlačítko „Vytvořit“ a Odoo zobrazí prázdný vzor pro novou kampaň.
vyplnit. Můžete také vybrat jakoukoliv již vytvořenou kampaň a zkopírovat, prohlédnout nebo
upravit šablonu kampaně.

.. obrázek: marketing_kampaně/sms-kampan-vzor.png
:align:center
:alt: Příklad vzhledu šablony kampaně pro SMS marketing v Odoo.

S každou kampaní se objevují možnosti „Odeslat nový e-mail“ a „Odeslat SMS“.
Ve výše uvedeném šabloně jsou k dispozici tlačítka „Odeslat sociální příspěvek“ a „Zasílání oznámení“.
forma.

Každý z těchto komunikačních kanálů přidá do kampaně Odoo nový.
odpovídající záložka v šabloně formuláře, kde lze zprávy daného typu prohlížet nebo upravovat.
spolu s různými datovými sadami, které jsou spojeny s každou konkrétní poštou.

Na vrcholu šablony jsou různé chytré tlačítka pro analýzu. Když je kliknete, Odoo vám ukáže
hluboké metriky související s konkrétním tématem (např. :guilabel:`Engagement`,
„Možnosti“, „Příležitosti“ atd. na samostatné stránce.

Pod chytrými tlačítky jsou pole pro „Název kampaně“ a „Odpovědný“.
Odoo umožňuje také přidávat různé :guilabel:`Tagy`, pokud je to potřeba.

Odesílání SMS z aplikace Kontakty
=====================================

Odesílání „krátkých“ zpráv přímo přes kontaktní formulář je dostupné
výchozím nastavení.

Chcete-li poslat SMS v tomto stylu, přejděte na
V aplikaci „Kontakty“ vyberte požadovaný kontakt v databázi a klikněte na
:guilabel: ikona „SMS“ v kontaktním formuláři (vedle pole „Telefonní číslo“).

.. obrázek: marketing_campaigns/sms-kontaktni-formular.png
:align:center
:alt:Ikona SMS je umístěna na kontaktním formuláři uživatele v aplikaci Kontakty.

Chcete-li poslat zprávu více kontaktům najednou, přejděte do hlavní aplikace „Kontakty“
Hlavní panel, vyberte „Zobrazení seznamu“, a vyberte všechny požadované kontakty, kterým chcete zaslat
zprávu odeslat. Pak v poli „Akce“ vyberte možnost „Odeslat SMS“.

.. obrázek: marketing_campaigns/sms-contacts-action-send-message.png
:align:center
:alt:Vyberte několik kontaktů, klikněte na akci a vyberte možnost „Odeslat více SMS“.

Vytvořte si šablony pro zasílání SMS, které můžete v budoucnu používat.
===================================

Chcete-li vytvořit šablony SMS pro budoucí použití, zapněte režim vývojáře.
<rozvojářský režim>“, přejděte na hlavní obrazovku Odoo, která je plná aplikací a vyberte
:menu: „Nastavení“. Pak přejděte dolů do sekce „Vývojové nástroje“ a
klikněte na tlačítko „Zapnout vývojářský režim“.

Jakmile je zapnutý režim vývojáře, hlavní panel aplikace Odoo se objeví znovu s nyní viditelným
ikona hmyzu, která se nachází v pravém horním rohu panelu; tato ikona ukazuje, že
Vývojářský režim je aktuálně aktivní.

Poté se vraťte do aplikace Nastavení a v horních nabídkách hlavního menu
Vyberte možnost „Technické“ a poté klikněte na odkaz „Šablony SMS“.
Šablony pro budoucí kampaně.

.. obrázek: marketing_campaigns/sms-template-settings.png
:align:center
:alt:Vyberte možnost šablony SMS v sekci Technické nastavení v aplikaci Nastavení.

V rámci rozhraní „Šablony SMS“ odhaluje Odoo celou stránku s názvem „SMS (Krátké zprávy)“.
Zprávy“ šablony. Výchozí pohled „Seznam“ zobrazuje název každé šablony.
komu se vztahuje.

Na této stránce můžete upravit nebo vytvořit zcela nové šablony pro SMS (Short Message Service).

.. obrázek: marketing_campaigns/sms-template.png
:align:center
:alt:Stránka šablon pro SMS v Odoo je dostupná po zapnutí vývojářského režimu v Nastavení.
Nastavení
