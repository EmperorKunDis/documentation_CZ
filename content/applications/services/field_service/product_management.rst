==================
Produktové řízení
==================

Když pracovníci v terénu vykonávají práce na místě, často používají produkty k dokončení své práce.
Odoo Field Service jim umožňuje tyto produkty zaznamenávat pomocí katalogu produktů a výchozích hodnot.
skladové funkce. To udržuje zásoby aktuální v reálném čase a automaticky přidává
zboží na fakturu.

Katalog produktů
===============

Chcete-li aktivovat produktový katalog pro Služby v terénu, přejděte na:
Konfigurace --> Nastavení a zapněte funkci „Fakturace za čas a materiál“.

Pokud chcete přidat produkty do úkolu, postupujte takto:

#Přejděte do sekce Služby v terénu a otevřete úkol.
#Klikněte na tlačítko „Produkty“.
#Klikněte na tlačítko „Přidat“ v kartě produktu, abyste jej přidali do úkolů.
#Pokud je potřeba, upravte počet produktů pomocí tlačítka „-“ a „+“.

Pokud jde o vaši práci, chytrý tlačítko nyní zobrazuje množství produktů, které jste přidali.
cena. Výběr produktů můžete kdykoliv upravit v katalogu produktů.

..tip:
   - Pro vytváření a úpravy produktů z Field Service přejděte na:
Konfigurace --> Produkty.
   - Chcete-li najít své produkty snadněji, použijte vyhledávací lištu a filtrujte své produkty podle
:guilabel:`Kategorie produktů“ a :guilabel:"Vlastnosti".

Výchozí sklad uživatele
======================

Nastavení výchozího skladu může být užitečné pro terénní pracovníky, kteří mají zásoby na cestách.
Ve svých dodávkách nebo ti, kteří vždy nakupují ze stejného skladu. Dále umožňuje pracovníkům na místě
Přepínat sklady z jejich profilů.

Všechny produkty v objednávce vytvořené během terénního zásahu jsou vždy odebírány ze standardní
skladu, který zajišťuje přesné zásoby.

.. viz též:
:doc:`../inventarizace-a-mrp/inventar`

Konfigurace
=============

Pro nastavení výchozího skladu uživatele je potřeba zadat:
<../../skladovani/sklady/vyuziti-lokalit/>
Funkci je nutné aktivovat v aplikaci Inventář a zároveň je potřeba mít více než jeden
sklad v databázi.

Můžete si ji nastavit buď pro svůj profil (<default-warehouse/my-profile>), nebo pro všechny
uživatelé <výchozí sklad/všichni uživatelé>.

.. viz též:
:doc:`../skladovani-a-dodavky/sklady-a-uskladneni/správa-skladových zásob/použití-lokalit“

.._výchozí sklad/můj profil:

Pro váš profil
----------------

Chcete-li si nastavit výchozí sklad pro sebe, klikněte na ikonu vašeho profilu v pravém horním rohu
obrazovce pak přejděte na: „Můj profil“ – „Nastavení“ – „Výchozí sklad“. Vyberte
výchozí sklad ze seznamu.

.._sklad-výchozí/pro všechny uživatele:

Pro všechny uživatele
-------------

Pro nastavení výchozího skladu pro konkrétního uživatele přejděte do sekce „Nastavení“ - „Uživatelé“.
Spravujte uživatele, vyberte uživatele, pak přejděte na záložku „Nastavení“. Vyhledejte
:guilabel:`Skladová evidence“ a vyberte výchozí sklad ze seznamu.

.. obrázek: product_management/user-default.png
:alt: Výběr výchozího skladu na uživatelském profilu.

Použití v terénních pracích
==========================

Jakmile je pro uživatele nakonfigurováno výchozí skladové zařízení, materiály používané při objednávce
spojené s úkolem servisního oddělení jsou stáhnuty z konkrétního skladu. Otevřete související prodeje
Vyberte si, přejděte na záložku „Ostatní informace“, pak se posuňte dolů k záložce „Dodání“. Výchozí
sklad je správně aplikován.

Jakmile je úkol Služby v terénu označen jako dokončený, zásoby skladu výchozího skladu jsou automaticky
Aktualizováno.
