=========
Distributoři
=========

V aplikaci CRM společnosti Odoo lze kontakty předávat do prodeje partnerům. Kontakty mohou být převedeny ručně
přiřazené nebo automaticky přiřazené na základě určeného stupně a umístění prodejců.

Konfigurace
=============

Pro využití funkcí pro přeprodej musí být nejprve nainstalován modul „Přeprodejci“. Přejděte na
aplikaci Apps, odstranit filtr aplikací
Vyhledávací lištu „Hledat…“ a pak vyhledejte „Distributoři“.

.. obrázek: obchodníci/obchodníci-modul.png
:align:center
:alt:Modul pro přeprodej v Odoo.

Klikněte na tlačítko „Aktivovat“ v modulu karty „Distributoři“, který se zobrazí. Tímto způsobem nainstalujete
modul a vrátí se na hlavní obrazovku Odoo.

Po instalaci modulu přejděte do aplikace CRM. Pod
:menu: „Konfigurace“ je nová sekce s názvem „Prodejci“, která obsahuje tři
pod ním: „Úrovně partnerů“, „Aktivace partnerů“ a
:guilabel:`Plány komise“.

.. _crm/partner-levels:

Úrovně partnerů
==============

Partnerské úrovně se používají k rozlišení různých distributorů. Chcete-li zobrazit partnerské úrovně
přejít na:menu: „CRM aplikace -> Konfigurace -> Prodejci: Úrovně partnerů“.

Na stránce „Úrovně partnerů“, která se objeví, jsou tři výchozí úrovně:

- :guilabel:`Zlato“
- :guilabel:`Stříbrná“
- :guilabel:`Bronz´

Nové úrovně lze přidávat tak, že kliknete na tlačítko „New“ a vyplníte novou úroveň.
forma.

Existující úrovně lze také upravovat a přejmenovávat, pokud si to budete přát. K úpravě úrovně vyberte ji
seznamu a pokračujte v provádění požadovaných změn na stránce úrovně, která se objeví.

Hodnota úrovně váhy se používá k rozhodnutí, jaká je pravděpodobnost přiřazení partnerovi příležitosti nebo kontaktu.
úrovně, přiřaďte číselnou hodnotu (větší než nula) do pole „Hmotnost úrovně“
Pokud je hmotnost nulová, nejsou žádné vodiče přiřazeny.

..tip:
*Hodnota úrovně* může být přiřazena na jednotlivé kontaktní záznamy. Hodnota, kterou je možné přiřadit na
individuální rekord přepíše výchozí hodnotu přiřazenou na formuláři konfigurace úrovně.

... _crm/partner-activations:

Aktivace partnerů
===================

Partnerové aktivace se používají k identifikaci stavu partnera. Aktivace jsou přiřazeny na
individuální záznam kontaktu a může být použit k seskupení nebo filtrování zprávy o partnerství.
(:menu_selection:`CRM aplikace --> Zprávy --> Partnerství`).

Pro zobrazení úrovní partnerů přejděte na: „Aplikace CRM –> Konfigurace –> Partner“.
Aktivace“.

V aplikaci *CRM* jsou tři typy aktivace vytvořeny výchozí hodnotou:

- :guilabel:`Plně funkční“
- :guilabel:`Zrychlení“
- :guilabel:`První kontakt“

Noví partneři mohou být aktivováni podle potřeby kliknutím na tlačítko „Nové“ a zadáním
V nově vzniklé řádce zadejte „Jméno“ a poté vyberte požadovaný stav.
Sloupec „Aktivní“.

Stávající aktivace partnerů mohou být také upraveny nebo přejmenovány, pokud si to budete přát. K přejmenování stavu klikněte
Zadejte do pole „Jméno“ požadovaného úrovně nové jméno.

Pro změnu aktivního stavu aktivaci posouvejte přepínač v sloupci „Aktivní“
požadované aktivování na pozici *neaktivní*.

.. obrázek:reseller_activation_toggle.png
:align:center
:alt: Seznam aktivací výchozích partnerů v aplikaci CRM.

Seznam výchozích partnerských aktivací v aplikaci CRM. Vypínač pro první kontakt je v
v neaktivní poloze a zbytek je aktivní.

Přiřazení partnerů
===================

Po partnerských úrovních a aktivacích partnerů
<crm/partner-activations> nakonfigurováno.

Abychom aktualizovali záznam jednoho z našich obchodních partnerů, přejděte do části:
Kartu pro požadovaného obchodního partnera a klikněte na tlačítko „Zobrazit zákazníka“.

V záložce „Přiřazení partnera“ klikněte na záznam zákazníka.

Klikněte na pole „Úroveň partnera“ a vyberte možnost z nabídky.
úrovně. Klikněte na pole „Aktivace“ a vyberte typ aktivace partnera z
seznamu, pokud je to požadováno. Poté klikněte na pole „Hmotnost úrovně“ a přidejte jinou hodnotu.
pokud je třeba, upravit hmotnost na úrovni.

Vydavatelé partnerů
================

S aplikacemi Odoo WebSite a Resellers je vytvořena nová stránka („/partners“),
zobrazit seznam všech aktivních partnerů z aplikace CRM.

Nyní se vraťte do nabídky CRM aplikace -> Prodej -> Zákazníci a klikněte na kartu Kanban pro
partnera. Z kontaktního formuláře partnera klikněte na tlačítko „Přejít na web“
nahoru na stránku, abyste otevřeli webovou stránku daného partnera.

Dále klikněte na „Upravit“ v pravém horním rohu webu partnera a použijte :doc:`stavbu
bloky, které můžete použít k přidání jakéhokoliv dalšího designu
elementy nebo informace o partnerovi.

..tip:
Doplněním společenské smlouvy je užitečná také informace o firmě.

Po provedení případných změn stránky klikněte na tlačítko „Uložit“. V horní části stránky
Přesuňte přepínač „Nedostupné“ do aktivní polohy „Dostupné“, pokud je třeba.

Tyto kroky opakujte pro všechny partnery.

.. obrázek:resellers/partners-webpage.png
:align:center
:alt:Příklad webové stránky partnera s uvedenými dostupnými partnery podle úrovně a místa.
