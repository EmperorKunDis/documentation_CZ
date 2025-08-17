==========================================
Kapitola 4: Zabezpečení – stručný úvod
==========================================

V předchozím kapitole jsme vytvořili první tabulku
Určená k ukládání firemních dat. V podnikovém softwaru jako je Odoo je jedna z prvních otázek
Je třeba zvážit, kdo může přistupovat ke službám. Odoo poskytuje bezpečnostní mechanismus pro omezení přístupu
k datům pro konkrétní skupiny uživatelů.

Téma bezpečnosti je podrobněji popsáno v kapitole :doc:`../restrict_data_access`, která se zaměřuje
abychom pokryli minimální požadovanou částku pro náš nový modul.

Datové soubory (CSV)
================

Odoo je velmi datově orientovaný systém. Přestože chování je upravováno pomocí kódu v Pythonu, část
Hodnota modulu je v datech, které nastaví při načtení. Jedním ze způsobů načítání dat je pomocí CSV
soubor. Jedním příkladem je „seznam států“.
„<{GITHUB_PATH}/odoo/addons/base/data/res.country.state.csv>“ je načtena při instalaci
Modul „základ“.

... blok kódu:: text

"id","země_id:id","název","kód"
state_au_1,au,"Teritorium hlavního města Austrálie", "ACT"
state_au_2,au,"Nový Jižní Wales", "NSW"
state_au_3,au,"Severní teritorium", "NT"
state_au_4,au,"Queensland", "QLD"
    ...

- „id“ je vnější identifikátor. Může se použít k odkazování na záznam
(bez znalosti jeho identifikátoru v databázi).
- „country_id:id“ odkazuje na zemi pomocí jejího „externího identifikátoru“.
- „název“ je název státu.
- „kód“ je kód státu.

Tyto tři pole jsou
„definováno <https://github.com/odoo/odoo/blob/2ad2f3d6567b6266fc42c6d2999d11f3066b282c/odoo/addons/base/models/res_country.py#L108-L111>“
v modelu „stát“.

Podle konvence je soubor importující data umístěn v složce „data“ modulu.
Jde o bezpečnostní soubor, je umístěn v složce „Bezpečnost“. Pokud se data týkají
názory a činy (přesněji se na ně podíváme později) je umístěno v adresáři „views“.
Dále musí být všechny tyto soubory deklarovány v „data“.
seznam v souboru „__manifest__.py“. V našem příkladovém souboru je definován
v manifestu základního modulu <https://github.com/odoo/odoo/blob/e8697f609372cd61b045c4ee2c7f0fcfb496f58a/odoo/addons/base/__manifest__.py#L29>.

Pozor, obsah datových souborů se načítá pouze v případě instalace modulu nebo
Aktualizováno.

.. varování:

Data jsou nahrávána postupně podle jejich pořadí v souboru „__manifest__.py“.
To znamená, že pokud data „A“ odkazují na data „B“, musíte zajistit, aby „B“
je načtena před „A“.

V případě zemí států si všimnete, že u zemí států je
`seznam zemí <https://github.com/odoo/odoo/blob/e8697f609372cd61b045c4ee2c7f0fcfb496f58a/odoo/addons/base/__manifest__.py#L22>`__
je načtena **předtím, než**
`seznam zemí <https://github.com/odoo/odoo/blob/e8697f609372cd61b045c4ee2c7f0fcfb496f58a/odoo/addons/base/__manifest__.py#L29>.
Protože státy odkazují na země.

Proč je vše důležité pro bezpečnost? Protože všechny konfigurace zabezpečení modelu se načítají přes
datové soubory, jak uvidíme v další části.

Přístupová práva
=============

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`reference/security/acl`.

.. poznámka::

**Cíl**: na konci této části by už neměl být tento upozornění:

... kódový blok :: text

UPOZORNĚNÍ rd-demo odoo.modules.loading: Model ['estate.property'] nemá žádné přístupové pravidlo...

Pokud není na modelu definován přístupový právo, Odoo určí, že žádný uživatel nemůže s daty pracovat.
Ještě je o tom v protokolu napsáno:

... blok kódu:: text

UPOZORNĚNÍ rd-demo odoo.modules.loading: Model ['estate.property'] nemá žádné přístupové pravidlo v modulu 'estate', zvažte jejich přidání, například:
id,název,model_id:id,skupina_id:id,čtení,zápis,vytváření,odkazování

Přístupová práva jsou definována jako záznamy modelu „ir.model.access“.
přístupové právo je spojeno s modelem, skupinou (nebo žádnou pro globální
přístup) a sadu oprávnění: vytvářet, číst, psát a odstraňovat (nebo #odstraňovat). Takový přístup
práva jsou obvykle definována v souboru CSV s názvem
„ir.model.access.csv“.

Tady je příklad pro naše předchozí „test_model“:

... blok kódu:: text

id,název,model_id/id,skupina_id/id,čtení,zápis,vytvoření,odstranění
access_test_model,access_test_model,model_test_model,base.group_user,1,0,0,0

- „id“ je „externí identifikátor“.
- „name“ je název „ir.model.access“.
- „model_id/id“ odkazuje na model, ke kterému se vztahují práva přístupu. Standardní způsob, jak odkazovat
k modelu je „model_<název modelu>“, kde „<název modelu>“ je „_name“ modelu
s „.“ nahrazeným „_“. Zní to složitě? Ano, je to složité…
- „group_id/id“ odkazuje na skupinu, ke které se přístupové právo vztahuje.
- „perm_read,perm_write,perm_create,perm_unlink“: čtení, zápis, vytváření a odstraňování

.. cvičení: Přidat oprávnění.

Vytvořte soubor „ir.model.access.csv“ v příslušné složce a definujte jej v
„__manifest__.py“ soubor.

Dávejte čtení, zápis, vytváření a odstraňování souborů skupině „base.group_user“.

Tip: varovný vzkaz v protokolu vám dává většinu řešení :-)

Server restartujte a varovné hlášení by mělo zmizet!

Je na čase konečně se s uživatelským rozhraním :doc:`seznámit <05_prvniui>!

… [#kdo], což znamená, který uživatel nebo skupina uživatelů.

... „Unlink“ je ekvivalentem „smazat“.
