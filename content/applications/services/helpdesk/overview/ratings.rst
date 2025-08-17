================
Hodnocení zákazníků
================

.. |smile| nahradit za zelenou: ikonu `fa-smile-o`: guilabel: (smile):
.. nahradit: žlutá: ikonka `fa-meh-o`: guilabel: (neutrální): ikona
.. nahraďte: červená :icon:`fa-frown-o` :guilabel:`(frown)`

Požádat zákazníky, aby ohodnotili podporu, kterou od týmu Helpdesku obdrželi, je příležitostí
zjišťovat výkonnost týmu a sledovat spokojenost zákazníků.

... /helpdesk/enable-ratings:

Zapněte hodnocení zákazníků u týmů Helpdesku
=========================================

Pro zobrazení hodnocení zákazníků na týmu podpory přejděte do aplikace Helpdesk pomocí volby v nabídce:
Konfigurace --> Týmy helpdesku“. Klikněte na tým z seznamu, abyste otevřeli stránku s nastavením.
do sekce „Výkon“ a zaškrtněte políčko „Hodnocení zákazníků“.

.. obrázek:: hodnocení/hodnoceni-povolit.png
:alt:Přehled stránky nastavení týmu podpory s důrazem na hodnocení v rámci řešení problémů
v Odoo Helpdesku.

Nastavte šablonu e-mailu s žádostí o hodnocení na stáži
===============================================

Pro automatické požadování hodnocení zákazníků poté, co jejich objednávky byly uzavřeny, byl vytvořen e-mailový šablon.
musí být přidán na příslušnou úroveň.

Po zapnutí nastavení „Hodnocení zákazníků“ pomocí příkazu
stránce nastavení týmu, klikněte na odkaz „Nastavit e-mailový šablonu pro fáze“. Vyberte fázi
z seznamu nebo klikněte na „New“ pro vytvoření nové fáze.

.. důležité:
Klienti by měli být požádáni o hodnocení pouze jednou, a to až poté, co bude jejich problém vyřešen.
je uzavřený. Proto by se na něj měl posílat e-mail pouze v případě, že je ve fázi
v kanbanu, protože v označeném stavu jsou považovány za uzavřené.

Na stránce nastavení scény vyberte šablonu „Požadavek na hodnocení lístku Helpdesk“
pole „Šablona e-mailu“. Tato šablona je přednastavena s hodnocením, které mohou zákazníci
pro zasílání zpětné vazby. Chcete-li zobrazit šablonu, klikněte na tlačítko s obrázkem šipky vedle pole.

Po přidání šablony na pódium se automaticky odešle zpráva, když je tiket přesunut do
tento stupeň. Zákazníkům jsou poté nabídnuty barevné ikony, pomocí kterých mohou ohodnotit podporu, kterou od společnosti obdrželi.

 - **Spokojený** - |smile|
 - Okay – |meh|
 - Nespokojený – |mračit se|

.. obrázek: hodnocení/vzorek šablony.png
:alt:Předběžný náhled žádosti o hodnocení vstupenek ve službě Helpdesk.

Po výběru hodnocení jsou zákazníci přesměrováni na webovou stránku, kde mohou poskytnout konkrétní písemný
zpětná vazba k podpoře jejich hodnocení. Hodnocení je pak předloženo a hodnocení i jakákoliv
Přidat komentář lze do diskuse na lístku.

..tip:
Kromě toho lze hodnocení zákazníků zobrazit také v reportu „Hodnocení zákazníků“.
reportovat se dostanete na: „Helpdesk app --> Reporting --> Customer Ratings“.

.. viz též:
   - :doc:`../../../obecne/spolky/vzor-e-mailu`
   - :doc:`../pokrocile/uzavirani-tiketu`
   - :reporty
