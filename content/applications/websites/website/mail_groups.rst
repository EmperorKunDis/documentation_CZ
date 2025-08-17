===========
Skupiny e-mailů
===========

Funkce „Skupina e-mailů“ umožňuje návštěvníkům webu vést veřejnou diskuzi prostřednictvím e-mailu.
Připojte se k skupině, abyste dostávali e-maily od ostatních členů skupiny (tj. uživatelů webu, kteří se přihlásili k
a poslat nové všem členům skupiny.

Chcete-li tuto funkci aktivovat, nainstalujte modul „Website Mail Group“ pomocí příkazu :ref:`install <general/install>`.
modul (webová_pošta_skupina).

.. poznámka::
**Skupiny e-mailů** není možné zaměnit s
:doc:`../marketing/email_marketing/mailing_lists` v aplikaci Email Marketing.

.. _webové stránky/e-mailové seznamy/konfigurovat skupiny:

Konfigurace skupin e-mailů
=======================

Pro konfiguraci skupin e-mailů postupujte takto:

#Nastavte si vlastní e-mailový alias domény přes **Obecné nastavení**, kde se dostanete dolů na
sekci „Diskuse“, která umožňuje funkci „Vlastní e-mailový server“.
při vstupu do aliasového doménového jména (:guilabel:`@mycompany.com`, např.).
#Přejděte na „Webové stránky > Konfigurace > Seznamy odběratelů“, pak klikněte na „Nový“.
#Uveďte název skupiny, e-mailovou adresu aliasu a popis.
#Zapněte „Moderovat tuto skupinu“ a zadejte „Moderátory“, pokud chcete.
:ref:`mírnější zprávy <webová stránka/mailingové seznamy/mírné zprávy>“ od této skupiny.
Skupina není moderovaná, můžete definovat uživatele s oprávněním k řízení zpráv.
ve skupině.
#V záložce „Soukromí“ definujte, kdo může do skupiny e-mailu přistupovat:

   - :guilabel:`Každý“: udělit skupině e-mailu veřejný přístup, aby se mohl k ní přihlásit každý.
   - :guilabel:"Členové pouze": umožnit se přihlásit jen uživatelům definovaným jako členové.
   - :guilabel:`Vybraná skupina uživatelů“: umožnit přístup pouze uživatelům z „Oprávněné skupiny“.
se přihlásit do mailové skupiny.

#Pokud je skupina pošty moderovaná, můžete automaticky upozornit autory na jejich zprávu.
dočasně nezveřejněné, aktivací možnosti „Automatická notifikace“ v sekci „Upozornění“
Kartu členů a zadat do pole „Zpráva“:guilabel:„Oznámení“.
#Pokud chcete novým uživatelům zasílat pokyny, povolte :guilabel:`Send guidelines to new
odběratelů a zapsat je do záložky „Pokyny“. To se zejména hodí, když
předmět je moderován.

Používání skupin e-mailů
=================

Přihlášení a odhlášení
-------------------------

Podle konfigurace skupiny e-mailů podle návodu :ref:`<website/mailing_lists/configure_groups>`
uživatelé mohou přidávat a odebírat seznamy e-mailů z webové stránky (výchozí adresa je "/groups").

.. obrázek: mail_groups/mail-group-page.png
:alt:Stránka skupiny e-mailu.

Vnitřní uživatelé mohou také provést tuto akci z: „Webové stránky --> Konfigurace --> Seznamy na odesílání e-mailů“.
pomocí tlačítka „Připojit“ a „Odejít“.

Posílání zpráv
----------------

Pro odesílání zpráv do mailové skupiny mohou uživatelé webu poslat e-mail na e-mailovou adresu :ref:`mailové skupiny
<webová stránka/seznamovací služby/konfigurace skupin>. Interní uživatelé mohou také vytvářet zprávy přímo
Odoo. Chcete-li tak učinit, přejděte na: „Webové stránky“ - „Nastavení“ - „Seznamy pro odesílání e-mailů“, vyberte požadovaný e-mail
Skupina, klikněte na tlačítko „E-maily“ a poté na „Nový“. Potom vyplňte
pole a klikněte na tlačítko „Odeslat“.

..tip:
   - Seznam zpráv lze také zobrazit výběrem skupiny na webu /groups.
stránka.
   - Členové skupiny mohou také zrušit své členství ve skupině, přistupovat na stránku poštovní skupiny a odesílat e-maily.
do skupiny pomocí URL v zápatí jakékoliv e-mailové zprávy, kterou obdrželi.

.. obrázek:: mail_groups/mail-group-URLs.png
:alt: URL v zápatí skupinové e-mailové zprávy.

... _webové stránky/e-mailovou konferenci/moderovat:

Moderování zpráv v e-mailových skupinách
==============================

Pokud je pro skupinu zapnutá funkce „Změnit moderátora“,
:ref:`skupina pošty <webová stránka/poštovní seznamy/konfigurovat skupiny>“, jeden z :guilabel:`moderátorů“ musí
schválit zprávy skupiny před jejich odesláním ostatním členům.

Pro moderování zpráv přejděte na: „Webové stránky --> Konfigurace --> Seznamy rozesílek“, vyberte
Skupina pošty a klikněte na tlačítko „Zobrazit“ chytré klávesnice. Můžete moderovat zprávy pomocí
tlačítka na konci řádku zprávy nebo vyberte zprávu pro její obsah a upravte ji
Podle toho.

.... obrázek: mail_groups/mail-group-moderation.png
:alt:Tlačítka pro moderování v řádku zprávy.

Následující akce jsou k dispozici:

- :guilabel:`Přijmout“: přijmout e-mail a poslat jej členům skupiny.
- :guilabel:`Odmítnout“: odmítnout e-mail. V okně, které se otevře, klikněte
:guilabel:`Odmítnout tichým způsobem“ odmítnout e-mail bez oznámení autorovi nebo specifikovat
vysvětlení odmítnutí zprávy a poté klikněte na tlačítko „Odeslat a odmítnout“ pro odmítnutí zprávy
a vysvětlení autorovi zaslat.
- :guilabel:„Bílá listina“: přijmout autora, tj. automaticky všechny jeho e-maily.
Výsledkem je vytvoření pravidla pro moderování příspěvků autora (moderace).
e-mailová adresa s nastavením: guilabel: „Vždy povolit“.
- :guilabel:"Ban": zakázat autorovi odesílat e-maily, tj. automaticky je ignorovat.
okno s upozorněním, které se otevře, klikněte na tlačítko „Zakázat“ a zakážete autora bez jeho oznámení nebo
Uveďte vysvětlení a klikněte na tlačítko „Odeslat a zablokovat“, abyste autora zablokovali a poslali mu
vysvětlení. V důsledku toho je vytvořen pravidlo pro :ref:`moderaci <website/mailing_lists/moderate>`.
autorovu e-mailovou adresu s oprávněním :guilabel:`Trvalý zákaz`.

.. poznámka::
Příspěvky můžete také upravovat z seznamu příspěvků skupiny. Přejděte na :menuselection:`Web
--> Skupiny --> Seznamy e-mailů“, vyberte poštovní skupinu a klikněte na „E-maily“.
tlačítko.

... _webové stránky/mailing listy/pravidla pro moderátory:

Bílá a černá listina autorů
=================================

Můžete přidat autora buď přímo do seznamu bílých nebo černých.
<webová stránka/seznamovací služba/upravit> nebo vytvořte pravidlo pro moderování.
Vyberte v nabídce „Webová stránka“ -> „Konfigurace“ -> „Pravidla moderátora“ a klikněte na „Nový“. Pak
vyberte skupinu, zadejte e-mail autora a nastavte stav
pole.

..tip:
Přístup k pravidlům pro moderování skupiny pošty lze získat také pomocí odkazu na webové stránky:
Konfigurace --> Seznamy rozesílek“, vyberte skupinu a pak klikněte na „Moderace“
tlačítko s integrovanou inteligencí.
