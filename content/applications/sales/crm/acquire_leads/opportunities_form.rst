===========================================
Vytvářejte příležitosti z kontaktních formulářů na webu
===========================================

Přidání kontaktního formuláře na webové stránky usnadňuje přeměnu návštěvníků na potenciální zákazníky.
Po odeslání informací návštěvníkem může být vytvořen příležitost automaticky a přiřazeno.
určitému prodejnímu týmu a konkrétní osobě.

.. _crm/přizpůsobit kontaktní formulář:

Upravte kontaktní formuláře
=======================

Výchozí stránka „Kontaktujte nás“ na webu Odoo zobrazuje přednastavenou kontaktní formulář.
Formulář lze upravit podle potřeby tak, aby vyhovoval konkrétnímu prodejnímu týmu.

Přejděte na:menu-selection:Webová aplikace - Kontaktní informace, pak klikněte na tlačítko :guilabel:Upravit.
v pravém horním rohu obrazovky otevřete webový editor. Klikněte na blok tvořící formulář v těle
webovou stránku, která otevře nastavení formuláře v pravém sloupci. Následující možnosti jsou
k dispozici pro přizpůsobení kontaktního formuláře z sekce „Od“ v pravém sloupci:

.. obrázek:: příležitosti_formulářů/přizpůsobení_formuláře.png
:align:center
:alt: Konfigurace formulářů na webu Odoo.

- :guilabel:`Akce“: výchozí akcí pro kontaktní formulář je „Odeslat e-mail“. Vyberte

aplikace
- :guilabel:`Tým prodeje“: vyberte tým prodeje z rozbalovací nabídky, ze které pocházejí příležitosti
Tento formulář by měl být přiřazen k tomuto pole. Toto pole se zobrazí pouze v případě, že je pole „Akce“
nastaveno na: guilabel: Vytvořit příležitost.
- :guilabel:`Prodejce“: pokud by měly být příležitosti přiřazeny konkrétnímu prodejci, vyberte
Vyberte je z nabídky. Pokud v tomto poli nebude žádný výběr, budou možnosti
byla přidělena podle stávajících pravidel týmu.
- :guilabel: pole označená hvězdičkou: použijte tento prvek k nastavení způsobu, jakým formulář zachází s poli označenými hvězdičkou.
Další možností je označit pole s hodnotami jako „Povinné“, což je doporučený způsob.
- :guilabel:`Mark Text“: vyberte, jak by měly být identifikovány pole označená jako „Marked Fields“.
znakem je hvězdička (*).
- :guilabel:`Šířka štítků“: použijte tento prvek k úpravě rozměru štítku v pixelech, pokud chcete.
- :guilabel:Na úspěchu webu: vyberte, jak se webová stránka chová po úspěšném odeslání objednávky
Formulář: guilabel:"Nic" udrží zákazníka na stejném obrazovce s přidáním
Potvrzující zpráva, že formulář byl úspěšně odeslán. :guilabel:`Redirect` odešle
zákazníka na novou stránku na základě adresy uvedené v poli „URL“ níže.
:guilabel:`Zobrazit zprávu“ nahrazuje formulář přednastavenou zprávou, která informuje zákazníka
Je třeba, aby se na ně kdokoliv co nejrychleji ozval.
- :guilabel:`URL“: pokud je vybrána možnost „Přesměrování“, zadejte
URL webové stránky, na kterou by měli být zákazníci přesměrováni po úspěšném odeslání formuláře.
- :guilabel:`Zobrazit“: použijte rozbalovací nabídku k přidání jakýchkoliv podmínek zobrazení pro tento prvek.
požadované.

.. důležité:
Pokud jsou aktivovány *leady*, výběrem možnosti „Vytvořit příležitost“ se vytvoří
a místo toho aktivujte kontakty. Chcete-li aktivovat kontakty, přejděte na: „CRM aplikace --> Konfigurace -->
Nastavení“ a zaškrtněte políčko „Vedení“. Pak klikněte na „Uložit“.

Upravte pole kontaktního formuláře
-----------------------------

Kromě nastavení formuláře lze upravit i nastavení každého pole.
Ve stále otevřeném menu webového editoru klikněte do pole, abyste otevřeli konfiguraci políčka
Nastavení v bočním panelu. Následující možnosti jsou k dispozici pro přizpůsobení pole:

- :guilabel:`Typ“: vyberte možnost z vlastního pole nebo existujícího typu pole.
- :guilabel:`Typ vstupu“: určete typ informací, které zákazníci mají zadat. K dispozici
Možnosti jsou: „Text“, „E-mail“, „Telefon“ nebo „URL“.
Vybraný formát omezuje formáty, které mohou zákazníci používat při zadávání informací.
- :guilabel:Jméno pole: zadejte název pro pole.
- :guilabel:`Pozice“: vyberte způsob, jakým se štítek bude vztahovat k ostatním prvkům formuláře. Štítek může
může být skryta nad hřištěm, vlevo od hřiště nebo upravena tak, aby byla blíž k hřišti.
- :guilabel:`Popis`: posuňte přepínač, abyste mohli do pole vložit popis, který může poskytnout
přidat další pokyny pro zákazníky. Klikněte pod políčkem na formuláři a přidejte popis.
- :guilabel:`Příklad“: zadejte příklad, aby uživatelé věděli, jak vkládat informace tam
Formátování je důležité například u telefonního čísla nebo e-mailové adresy.
- :guilabel:`Výchozí hodnota“: zadejte hodnotu, která se má vkládat do formuláře výchozím způsobem, pokud zákazník
neposkytovat informace v tomto poli. *Není doporučeno zadávat výchozí hodnotu
*povinné pole.
- :guilabel:`Povinné pole“: posuňte přepínač, aby bylo tento prvek povinný a musí být vyplněn
za každou podanou žádost.
- :guilabel:`Zobrazitelnost“: vyberte, kdy by mělo být toto pole viditelné.
zvolit, zda se tento prvek na ploše uživatele zobrazí nebo skryje.
zvolit, zda tento prvek ukázat nebo skrýt uživatelům mobilních zařízení.
- :guilabel:`Animace“: vyberte, zda by měl být tento prvek animován.

.. obrázek: možnosti_formuláře/přizpůsobení_pole.png
:align:center
:alt:Nastavení konfigurace pole na webu Odoo.

Podívejte se na příležitosti
==================

Po odeslání kontaktního formuláře je vytvořen příležitost, která se přiřazuje na základě
:ref:`Nastavení formuláře <crm/customize-contact-form>“. Pro zobrazení příležitostí přejděte na
:menu-selection:„Aplikace CRM –> Prodej –> Můj prodejní kanál“.

.. poznámka::
Pokud jsou kontakty aktivovány v databázi, při odeslání kontaktního formuláře se generují jako leadové kontakty, nikoli
příležitosti. Chcete-li aktivovat kontakty, přejděte na: „CRM aplikace -> Konfigurace ->
Nastavení“ a zaškrtněte políčko „Vedení“. Pak klikněte na „Uložit“.

Přejděte na:menu:crmapp-->leads, abyste viděli nové kontakty.

Na panelu „Moje trubice“ klikněte na kartu příležitosti v zobrazení Kanban.
vizibilita příležitosti. Informace, které zákazník do příležitosti zadává, jsou viditelné na příležitosti.
rekord.

.. poznámka::
Jakmile jsou pole kontaktního formuláře přizpůsobitelná, tak pole na záznamu příležitosti, kde je formulář
Uložená data se liší podle typu informace.

Pokud je použito přednastavené kontaktní formulář, pole „Předmět“ se přidá k poli „Název“.
pole a obsah v poli „Poznámky“, které je označeno jako „Vaše poznámky“.
Položka „Dotaz“ je přidána do záložky „Vnitřní poznámky“.

.. viz též:
   - :doc:`../pipeline/manage_sales_teams`
   - :doc:`převést na jiný formát
   - :doc:`../track_leads/lead_scoring`
   - [:ref:`Webové formuláře <web/bloky/formulář>“
