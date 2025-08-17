Zobrazit obsah

=====
Uživatelé
=====

Odoo definuje uživatele jako osobu, která má přístup k databázi. Administrátor může přidat kolik
uživatelů, které společnost potřebuje, a aby omezila typ informací, ke kterým každý uživatel má přístup.
Pravidla lze aplikovat na každého uživatele. Uživatelé a přístupová práva mohou být kdykoli přidány nebo změněny.

.. viz též:
   - :doc:`uživatelé/jazyk“
   - :doc:`uživatelé/přístupová práva“
   - :ref:`přístupová práva/superuživatel
   - :ref:`práva přístupu/skupiny“

.._user/add-individual:

Přidat uživatele
====================

Pro přidání nových uživatelů přejděte do: `Nastavení aplikace --> Sekce Uživatelé --> Správa uživatelů`.
klikněte na:guilabel:`Nový`.

.. obrázek: /soubor/user_management.png
:alt: Zobrazení nastavení stránky s důrazem na položku spravovat uživatele v Odoo.

Vyplňte formulář s veškerými požadovanými informacemi. Pod :doc:`Přístupové právo
kartě „Uživatelé/Přístupová práva“ vyberte skupinu uživatelů pro každou aplikaci, ke které má mít přístup.

Seznam aplikací je založen na aplikacích nainstalovaných v databázi.

.. obrázek: users/new-user.png
:alt:Zobrazení uživatelského formuláře s vyznačeným záložkovým menu pro přístupová práva v Odoo.

Po vyplnění všech potřebných políček na stránce klikněte na ikonu :icon:`fa-cloud-upload` :guilabel:`(Uložit
ručně). Uživateli je automaticky zaslána e-mailová pozvánka s e-mailem uvedeným v
V poli „E-mailová adresa“ je uživatel vyzván k zadání e-mailové adresy. Uživatel musí kliknout na odkaz v e-mailu, aby přijal
a vytvořit databázi přihlašovacích údajů.

.. obrázek:users/invitation-email.png
:alt: Příklad uživatelského formuláře s upozorněním, že byla odeslána pozvánka na Odoo.

.. varování:
Pokud je společnost na měsíčním předplatném, databáze se automaticky aktualizuje tak, aby odrážela
přidružené uživatele. Pokud je společnost na ročním nebo víceletém plánu, objeví se upomínkový nápis
v databázi. Upsellová nabídka může být vytvořena kliknutím na reklamní banner, který aktualizuje
předplatné. Nebo zkuste „podat žádost o podporu <https://www.odoo.com/help>“
problém.

Typ uživatele
---------

Vyberte si typ uživatele na stránce „Spravovat uživatele“ kliknutím na vyhledávání.
baru a pak nastavit filtr pro buď :guilabel:`vnitřní nebo :guilabel:`vnější
Uživatel nebo:label:Portal User.

Databáze Odoo mají tři typy uživatelů: „Vnitřní uživatel“, „Portál“ a
:guilabel:`Veřejnost“. Uživatelé jsou považováni za uživatele interní databáze. Uživatelé portálu jsou považováni za uživatele externí databáze.
uživatelé, kteří mají přístup pouze do databáze portálu a mohou si prohlížet záznamy. Veřejní uživatelé jsou ti, kteří navštěvují
webových stránek, viz dokumentace na téma „uživatelé/portál“.

Možnost uživatele „Portál“ neumožňuje administrátorovi určit přístupová práva.
Uživatelé mají přednastavená specifická práva (například pravidla záznamů a omezené menu).
obvykle nepatří k běžným skupinám Odoo.

..._uživatelé/deaktivace:

Deaktivovat uživatele
================

Chcete-li archivovat uživatele, přejděte na: `Settings app --> Users section -->
Spravovat uživatele. Pak zaškrtněte políčko vedle jmen uživatelů, kteří mají být deaktivováni.

Po výběru vhodného uživatele k archivování klikněte na ikonu „Nástroje“
ikona a z nabídky vyberte položku „Archiv“. Pak klikněte na tlačítko „OK“.
z okna potvrzování, které se objeví.

.. nebezpečí::
**Nikdy** nedeaktivujte hlavního uživatele (správce) (admin). Změny v účtu správce mohou způsobit
a negativní dopad na databázi. To zahrnuje i „administrátora bez moci“, což znamená, že žádný uživatel nemůže
databáze může provádět změny v přístupových právech. Proto doporučuje kontaktovat
před provedením změn se poraďte s naším týmem podpory nebo analytikem Odoo.

Chyba: příliš mnoho uživatelů
---------------------

Pokud je v databázi Odoo více uživatelů než je uvedeno v předplatném Odoo Enterprise.
zobrazí se následující zpráva.

.. obrázek: users/add-more-users.png
:alt:Příliš mnoho uživatelů na chybovém hlášení databáze.

Když se zpráva objeví, má správce databáze 30 dní na to, aby něco udělal, než dojde k vypršení platnosti databáze.
Sčítání se aktualizuje každý den.

K vyřešení problému lze použít buďto:

- Přidejte další uživatele k předplatnému klepnutím na odkaz „Upgrade your subscription“
zobrazené v zprávě pro ověření cenové nabídky na zvýšení počtu uživatelů a zaplatit za další uživatele.
- :ref:`Zablokovat uživatele <users/deactivate>“ a odmítnout nabídku na zvýšení cen.

.. varování:
Pokud je společnost na měsíčním předplatném, databáze se automaticky aktualizuje tak, aby odrážela
přidružené uživatele. Pokud je společnost na ročním nebo víceletém plánu, objeví se upomínkový nápis
v databázi. Upsellová nabídka může být vytvořena kliknutím na reklamní banner, který aktualizuje
subskripce. Alternativně mohou uživatelé „odeslat požadavek o podporu <https://www.odoo.com/help>“
vyřešit problém.

Jakmile databáze obsahuje správný počet uživatelů, zpráva o vypršení platnosti se sama odstraní.
Po několika dnech, kdy se ověření opakuje.

..._uživatelé/správa hesel:

Správa hesel
===================

Správa hesel je důležitou součástí udělování uživatelům samostatného přístupu k databázi.
době. Odoo nabízí několik různých způsobů, jak obnovit heslo uživatele.

.. tip::
Odoo má nastavení, které určuje délku potřebnou pro heslo. Toto nastavení lze přistupovat
navigace do sekce „Nastavení aplikace“ -> „Povolení“, a zadání požadovaného
délku hesla v poli „Minimální délka hesla“. Výchozí hodnota je 8.

.. obrázek:users/minimum-password-length.png
:alt:Minimální délka hesla je zvýrazněna v části Povolení obecných nastavení.

.. /users/reset-password:

Obnovit heslo
--------------

Uživatelé mohou někdy chtít obnovit svůj osobní heslo pro zvýšení bezpečnosti.
jenom ti, kteří mají přístup ke složce s heslem. Odoo nabízí dvě možnosti obnovení hesla: jednu zahájenou
uživatel si heslo sám změní nebo administrátor spustí reset.

... /reset-password-login/:

Povolit obnovení hesla z přihlašovací stránky
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Možnost obnovení hesla lze zapnout nebo vypnout přímo z přihlašovací stránky. Tato akce je
je dokončena uživatelem a tato volba je ve výchozím nastavení povolena.

Chcete-li změnit tento parametr, přejděte do sekce „Nastavení aplikace“ -> „Oprávnění“.
Následně klikněte na „Resetovat heslo“ a poté na „Uložit“.

.. obrázek: uživatelé/heslo-reset-přihlášení.png
:alt:Zapnutí resetování hesla v nastavení Odoo.

Na stránce přihlášení klikněte na tlačítko „Obnovit heslo“ a zahájí se proces obnovení hesla.
resetovací token zaslaný na e-mail uvedený v profilu.

... /users/reset-password-email:

Odeslat pokyny k obnovení
~~~~~~~~~~~~~~~~~~~~~~~

Přejděte do aplikace Nastavení: Menu > Uživatelé a společnosti > Uživatelé, vyberte uživatele ze seznamu.
a klikněte na tlačítko „Odeslat pokyny pro obnovení hesla“ v uživatelském formuláři.
a automaticky jim byly zaslány pokyny k obnovení hesla.

.. poznámka::
Tlačítko „Odeslat pokyny k obnovení hesla“ se zobrazí pouze v případě, že je pozvánka odeslána prostřednictvím Odoo.
E-mail již byl uživatelem potvrzen. Jinak se zobrazí tlačítko „Znovu zaslat e-mailovou pozvánku“.
se objeví tlačítko.

E-mail obsahuje všechny potřebné pokyny k obnovení hesla spolu s odkazem na přesměrování.
uživatele na stránku přihlášení do Odoo.

.. obrázek: uživatelé/heslo-obnovit-e-mail.png
:alt: Příklad e-mailu s odkazem na obnovení hesla pro účet Odoo.

.. /users/change-password:

Změnit heslo uživatele
--------------------

Přejděte na položku „Nastavení aplikace“ > „Uživatelé a společnosti“ > „Uživatelé“ a vyberte uživatele, který chcete přidat.
Klikněte na ikonu „Nástroje“ (ikona „fa-cog“), vyberte možnost „Změnit heslo“.
z výsledného seznamu. Zadejte nové heslo do sloupce :guilabel:`New Password`.
okně s názvem „Změnit heslo“ a potvrďte změnu kliknutím
:guilabel:`Změnit heslo“.

.. obrázek:users/change-password.png
:alt:Změnit heslo uživatele v Odoo.

.. poznámka::
Tato operace mění heslo uživatelů pouze na místním počítači a neovlivňuje jejich hesla v jiných zařízeních.
Odoo účet.

Pokud je třeba změnit heslo Odoo, použijte odkaz na obnovení hesla.
<users/reset-password-email>. Přístup k stránce My Databases umožňují hesla z webu www.odoo.com.
další funkce portálu.

Po kliknutí na „Změnit heslo“ se stránka přesměruje na stránku přihlášení do Odoa, kde můžete změnit
databáze lze opětovně přistupovat pomocí nového hesla.

.._uživatelé/více společností:

Multi Companies
===============

Pole „Společnosti“ na uživatelském formuláři umožňuje správci poskytnout přístup k
Pro uživatele je k dispozici více společností. Pro konfiguraci prostředí pro více společností pro uživatele přejděte na
Přejděte do aplikace Nastavení: „Uživatelské nastavení“ - „Zařízení“ - „Spravovat uživatele“.
Vyberte uživatele, který chcete otevřít jeho uživatelskou formu a nakonfigurujte s více společnostmi.

V záložce „Přístupová práva“ pod položkou „Společnosti“ nastavte pole označená
„Povolené společnosti“ a „Výchozí společnost“.

V poli „Povolené společnosti“ může být více společností. Jsou to společnosti, které
Uživatel může přistupovat a upravovat podle nastavených oprávnění. Výchozí společnost je
firmě, ke které se uživatel přihlásí při každém přihlášení. Tento prvek může obsahovat pouze jeden
soukromá společnost.

.. varování:
Pokud není nastaveno správně vícefiremní přístup, může to vést k nekonzistentním datům v rámci více firem.
chování. Proto by měli provádět změny oprávnění pouze zkušení uživatelé Odoo.
uživatelé pro databáze s konfigurací více společností. Pro technické vysvětlení se podívejte na
dokumentace pro vývojáře na stránce :doc:`../../../developer/howtos/company`.

.. obrázek: uživatelé/více společností.png
:alt:Zobrazení uživatelského formuláře s důrazem na pole pro více společností v Odoo.

.. viz též:
:doc:`firmy“

..toctree::


uživatelé/jazyk
uživatelé/2FA
uživatelé/práva
uživatelé/portál
uživatelé/facebook
uživatelé/google
uživatelé/Azure
users/ldap
