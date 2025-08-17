=============
Práva přístupu
=============

Přístupová práva jsou oprávnění, která určují obsah a aplikace, které uživatelé mohou přistupovat.
editace. V Odoo lze pro jednotlivé uživatele nebo skupiny uživatelů nastavit oprávnění.
povolení jen těm, kteří je potřebují, zajišťuje, že uživatelé nemohou nic měnit nebo mazat.
neměly mít přístup k.

Pouze administrátor může změnit přístupová práva.

.. nebezpečí::
Změna přístupových práv může mít negativní dopad na databázi, což zahrnuje
*nezpůsobilý správce*, což znamená, že žádný uživatel v databázi nemůže měnit přístupová práva.
Protože z těchto důvodů doporučuje kontaktovat analytika Odoo nebo naši podporovou skupinu.
prováděním změn.

.. tip::
Uživatel **musí** mít ve svém uživatelském profilu nastavené konkrétní oprávnění pro správu.
změnit přístupová práva jiného uživatele.

Pro přístup k této možnosti přejděte do aplikace „Nastavení“ -> „Správa uživatelů“ -> vyberte
uživatel--> záložka Přístupová práva--> sekce Správce--> pole pro správu.

Jakmile se dostanete na místo, musí už existující správce změnit nastavení.
pole „Administrátoři“ na pole „Přístupová práva“.

Jakmile je změna dokončena, klikněte na tlačítko :guilabel:`Uložit`, abyste uložili změny a implementovali uživatele.
správce.

Uživatelé
=====

Přístupová práva pro :ref:`uživatele <users/add-individual>` se nastavují při přidání uživatele
do databáze, ale mohou být kdykoli upraveny v uživatelském profilu.

Pro změnu práv uživatele klikněte na požadovaného uživatele pro editaci jeho profilu.

.. obrázek:: přístupová práva/navigovat do menu uživatelů.png
:alt:Nápověda uživatelského menu v sekci Nastavení aplikace Odoo.

Na stránce profilu uživatele v záložce „Přístupová práva“ se přesuňte dolů a zobrazte aktuální
Povolení.

Pro každou aplikaci použijte rozbalovací nabídku k výběru úrovně oprávnění, které by měl mít tento uživatel.
Možnosti se liší pro každou část, ale nejčastější jsou: :guilabel:`Prázdný/Žádný`, :guilabel:`Uživatel: Vlastní
Dokumenty“, „Uživatel: Všechny dokumenty“ nebo „Administrátor“.

V poli „Administrátor“ v záložce „Přístupová práva“ je následujících možností:
Nastavení nebo přístupová práva.

.. obrázek: přístupová práva/přístupové právo - menu.png
:alt:V rozevíracím seznamu aplikace Prodej lze nastavit úroveň oprávnění uživatele.

.._přístupová práva/skupiny:

Vytvářejte a upravujte skupiny
========================

Skupiny jsou aplikacemi specifické sady oprávnění, které se používají k řízení společných přístupových práv pro
velké množství uživatelů. Administrátoři mohou upravit stávající skupiny v Odoo nebo vytvořit nové.
definovat pravidla pro modely v rámci aplikace.

Pro přístup k skupinám nejprve aktivujte režim vývojáře v Odoo podle návodu na této stránce. Poté přejděte do
:menu:Nastavení aplikace --> Uživatelé a společnosti --> Skupiny“.

.. obrázek: přístupy/kliknutí uživatelů a společností.png
:alt:Nápověda pro skupiny v sekci Uživatelé a společnosti aplikace Nastavení Odoo.

Pro vytvoření nové skupiny z stránky „Skupiny“ klikněte na „Vytvořit“. Potom z
Vyplňte prázdnou skupinu, vyberte aplikaci a dokončete skupinový formulář (podrobnosti níže).

Pro úpravu stávajících skupin klikněte na existující skupinu v seznamu zobrazeném na
Stránku „Skupiny“ a upravit obsah formuláře.

Do pole „Název skupiny“ zadejte název skupiny a zaškrtněte políčko vedle „Sdílet skupinu“, pokud
Tato skupina byla vytvořena pro nastavení přístupových práv k sdíleným datům u některých uživatelů.

.. důležité::
Vždy zkontrolujte nastavení, která chcete změnit, abyste se ujistili, že jsou aplikována na správné uživatele.

Skupina má více záložek pro správu všech prvků skupiny. V každé záložce klikněte
:guilabel:`Přidat řádek“ pro přidání nové řádky uživatelů nebo pravidel a klikněte na ikonu „fa-times“.
:guilabel:`(zrušit)` ikona pro odstranění řádku.

.. obrázek: přístupová práva/skupiny-form.png
:alt:Tabulky ve skupinách slouží k úpravě nastavení skupiny.

- Karta „Uživatelé“: seznamuje s uživateli v aktuální skupině. Uživatelé označení černou barvou jsou
administrativní práva. Uživatelé bez administrátorských přístupů se zobrazují modře. Klikněte na :guilabel:`Přidat uživatele
do této skupiny přidat uživatele.
- :guilabel:`Dědičné“ záložka: Dědičnost znamená, že uživatelé přidáni do této skupiny jsou automaticky přidáni
do skupin uvedených na této záložce. Klikněte na tlačítko „Přidat řádek“ pro přidání děděných skupin.

...... příklad::
Příkladem může být skupina *Sales/Administrator*, která do seznamu přidává skupinu *Website/Restricted Editor*.
její záložce „Dědičné“ a poté všechny uživatele přidružené k skupině *Prodej/Administrátor*.
automaticky získají přístup do skupiny *Website/Restricted Editor*.

- :guilabel:`MENU“ záložka: definuje, které modely může skupina vidět. Klikněte
:guilabel:`Přidat řádek“ pro přidání konkrétního menu.
- Karta „Zobrazení“: seznam zobrazení v Odoo, ke kterým má skupina přístup. Klikněte na „Přidat
Přidat pohled do skupiny pomocí příkazu „line“.
- Karta „Přístupová práva“: uvádí první úroveň práv (modelů), které má tato skupina.
:guilabel:`Jméno“ slouží k označení názvu pro přístup ke skupině
Vybrány v sloupci Model.

Pro přidání nového práva k skupině klikněte na :guilabel:`Přidat řádek`. Vyberte vhodný model
z nabídky „Model“ a pak zadejte název přístupového práva do
:guilabel:`Jméno“ sloupec. Pro každý model zapněte následující možnosti podle potřeby:

  - :guilabel:`Číst“: Uživatelé mohou vidět stávající hodnoty objektu.
  - :label:Změnit hodnotu objektu: Uživatelé mohou upravit stávající hodnoty objektu.
  - :guilabel:`Vytvořit“: Uživatelé mohou vytvářet nová hodnota pro objekt.
  - :guilabel:`Smazat“: Uživatelé mohou smazat hodnoty pro objekt.

.....tip:
Zatímco není žádné konvence při pojmenovávání práv přístupu, je vhodné zvolit jméno, které
definuje svůj účel.

Příkladem může být přístup nákupních manažerů k modelu :guilabel:`Contact`.
nazvané „res.partner.purchase.manager“. Tento se skládá z technického názvu modelu
Následované jménem skupiny uživatelů, na kterou se vztahuje.

.. obrázek: přístupová práva/název pole.png
:alt:Název přístupového práva k modelu.

Abychom našli technické jméno modelu z aktuálního pohledu, nejprve vložíme do pole místo textu.
V poli „Jméno“ zadejte název, pak klikněte na název „Model“, a nakonec
:icon:`fa-arrow-right` :guilabel:`(Vnitřní odkaz)`

- :guilabel:`Záznamové pravidlo“: ukazuje druhou vrstvu práv na editaci a viditelnost.
:guilabel:`Záznamové pravidlo“ přepsat nebo upřesnit práva skupiny. Klikněte na „Přidat
Zadejte příkaz „line“ a přidejte pravidlo do této skupiny. Pro každé pravidlo zvolte hodnoty pro následující možnosti:

  - :guilabel:`Žádost o čtení“.
  - :guilabel:`Přihlásit se k psaní“.
  - :guilabel:`Přihlásit se k vytvoření“.
  - :guilabel:`Požádat o smazání“.

.. důležité::
Záznamové pravidlo je napsané pomocí domény, nebo podmínky, která filtruje data. Doménová výraznost
Takže je to seznam podmínek, například:

`([['mrp_production_ids'], 'in', uživatel.partner_id.komerční_partner_id.production_ids.ids])`

Toto pravidlo je určeno k tomu, aby se zobrazily varování o spotřebě pro dodavatele.

Odoo má knihovnu přednastavených pravidel pro záznamy, aby bylo používání snadné i pro uživatele bez znalosti
doménám (a doménovým výrazům) by se měli obrátit na analytika podnikání Odoo nebo na podporu Odoo.
Tým před změnami.

..._přístupová práva/administrátor:

Superuživatelský režim
==============

Režim „superuživatel“ umožňuje uživateli obejít pravidla záznamů a oprávnění k přístupu.
prvně aktivujte režim vývojáře:ref:`developer mode <developer-mode>`, pak přejděte do nabídky *debug*.
je zobrazena v horním panelu vedle ikonky s :icon:`fa-bug` :guilabel:`(debug)` .

Na konci nabídky klikněte na „Stát se superuživatelem“.

.. důležité::
Přístup k nastavení pro sekci *Administrace* v části *Práva přístupu* mají pouze uživatelé s
jejich uživatelský profil) mohou přihlásit do režimu *Superuser*.

.. nebezpečí::
V režimu „superuživatel“ lze obejít pravidla záznamů a oprávnění k přístupu, protože
by mělo být vykonáváno s maximální opatrností.

Po opuštění režimu superuživatele mohou uživatelé být zablokováni v databázi kvůli změnám, které byly
Toto může způsobit impotentního administrátora, nebo administrátora bez schopnosti změnit přístup
práva/nastavení.

V tomto případě kontaktujte podporu Odoo zde: „Nový požadavek na pomoc <https://www.odoo.com/help>“.
technická podpora je schopna obnovit přístup pomocí technické podpory.

Způsob opuštění režimu „superuživatel“ spočívá v odhlášení z účtu a přechodu do horního pravého rohu.
Klikněte na uživatelské jméno „OdooBot“ a poté vyberte možnost „Vymazat“.

.. tip::
Alternativní způsob aktivace režimu *superuživatel* je přihlášení se jako superuživatel. Chcete-li tak učinit, přejděte na
do přihlášení a zadat příslušný e-mail a heslo.

Místo kliknutí na „Přihlásit“ klikněte na „Přihlášení jako superuživatel“.
