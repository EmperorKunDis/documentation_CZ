Zobrazit obsah

=========
Společnosti
=========

V Odoo je společnost jednotlivým podnikatelským subjektem, který funguje nezávisle s vlastním právním
identitu, finanční záznamy a specifické nastavení provozu.

.. viz též:
   - :ref:`obecná/firmy/pobočky`
   - :doc:`Společnost s více společnostmi <companies/multi_company>`

..._generál/firmy/konfigurace:

Konfigurace
=============

Chcete-li založit společnost, postupujte takto:

#:ref:`Nastavte podrobnosti o společnosti <obecné/firmy/společnost>.
#.:ref:„Správa uživatelů a jejich oprávnění <obecné/firmy/uživatelé>“.
#:ref:`Upravit vzhled dokumentu <obecné/firmy/vzhled-dokumentu>“.

.._generál/firmy/firma:

Společnost
-------

Pro vytvoření společnosti otevřete aplikaci Nastavení, přejděte do sekce „Společnosti“ a klikněte
:ikonka: „Otevřít společnosti“ a v seznamu „Společnosti“ klikněte na
:guilabel:`Nový“ a nastavte následující pole:

- :guilabel:`Název společnosti“
- :guilabel:`Adresa“
- :guilabel:`Daňové identifikační číslo“: daňové identifikační číslo.
- :guilabel:`LEI“: identifikátor právnické osoby.
- :guilabel:`IČO“): číslo z obchodního rejstříku (pokud se liší od „DIČ“)
- :ref:`Měna <multi-currency/config-main-currency>`
- :guilabel:`Telefon“ a :guilabel:"Mobil"
- :guilabel:`E-mail“
- :guilabel:`Webová stránka“
- :guilabel:`E-mailová doména“
- :guilabel:`Barva“

Nahrát firemní logo a stisknout tlačítko „Uložit“.

.. poznámka::
   - Alternativně je možné vytvořit společnost kliknutím na:
Uživatelé a firmy --> Firmy.
   - Informace o společnosti se mohou lišit v závislosti na daňovém úřadu.
<../finance/fiskalni_lokalizace>.

.._generál/firmy/uživatelé:

Uživatelé
-----

Po založení společnosti přidejte uživatele podle návodu :doc:`users <users>`, a nakonfigurujte jejich přístup dle :ref:`přístupu <access>`
<uživatelé/přidat-jednotlivce> a :dokumentace: „práva přístupu“ <uživatelé/práva-přístupu>.

.. viz též:
:ref:`Uživatelé v prostředí více společností <uživatelé/více-společností>`

.._generál/firmy/dokumentace:

Uspořádání dokumentu
---------------

Nastavte výchozí rozložení pro všechny dokumenty společnosti.

.._obec/firmy/odvětví:

Banky
========

Branchy představují divize v rámci společnosti, jako jsou regionální kanceláře nebo oddělení.
fungují pod společným mateřským subjektem. Podporují hierarchické struktury firem prostřednictvím
:ref:`konfigurovatelné nastavení <obecné/firmy/pobočky/konfigurace>>, které umožňuje
:ref:`komplexní nebo specializované pohledy <obecné/firmy/odvětví/konzolidační pohled> s
flexibilní: přístupový kontrolu obecně/firem/oddělení/uživatelů
Sdílená viditelnost záznamů (<všeobecné/firmy/pracoviště/sdílené záznamy>) a přizpůsobitelná
:ref:`hospodářské výsledky <účetnictví/podniky/obory/výsledovka>“.

.. poznámka::
Sesterské společnosti by měly být vytvořeny jako samostatné firmy a ne jako pobočky.

.. viz též:
   - :doc:`Společnost s více subjekty </aplikace/obecné/firmy/multisubjektní-firma>`
   - :ref:`Účetnictví poboček <účetnictví/pobočky>`

.._generál/firmy/oddělení/konfigurace:

Konfigurace
-------------

Každá větev je spojena se svou mateřskou společností a může obsahovat odlišné nebo specifické informace, například
jako je například adresa nebo logotyp.
víceúrovňová architektura.

.. důležité::
   - Zjistěte strukturu a hierarchii společnosti před vytvořením firemních poboček a divizí v Odoo.
Společnost definovaná jako mateřská nemůže být později přeměněna na pobočku, protože takový krok může vést ke ztrátě
:doc:`přístupová práva uživatelů <users/access_rights>“.
   - Vždy nejdříve vytvořte mateřskou společnost.

Vytvoření větve provedete následovně v aplikaci Nastavení:

#Přejděte do sekce „Společnosti“, klikněte na ikonu „Oi-arrow-right“ a poté na „Spravovat“.
Firmy“, nebo přejděte na „Nastavení“ → „Uživatelé a společnosti“ → „Společnosti“.
#V seznamu společností otevřete požadovaný formulář rodičovské společnosti.
#V záložce „Branches“ klikněte na tlačítko „Přidat řádek“ a vyplňte pole „Obecné
položky „Informace“ v okně „Vytvořit pobočku“.

Pro vytvoření větví z větve a pro vytvoření víceúrovňové architektury klikněte na :guilabel:`Přidat řádek`.
v nové větvi v záložce „Větve“.

.. tip::
Aktivujte režim vývojáře (:ref:`vývojářský režim <developer-mode>`), abyste mohli nastavit účty na sociálních sítích.
a systémem e-mailové komunikace specifickým pro danou společnost.
parametry.

.. varování:
Přidáním pobočky do společnosti se otevře možnost používat funkce pro více společností:

.._souhrnně/firmy/pobočky/konzolidační pohled:

Souhrnné nebo odvětvové pojetí
-------------------------------------

.. poznámka::
Vybráním mateřské společnosti se všechny její pobočky automaticky propojí, vybrání-li se pobočka
připojuje se pouze k této pobočce. Chcete-li přepínat mezi nimi, použijte výběr společnosti
<všeobecné/více společností/vybraná společnost>.

Všechny konfigurace kromě nastavení účetnictví dědí z
mateřská společnost musí být nastavena zvlášť pro každou pobočku. To umožňuje konfiguraci specifickou pro jednotlivé pobočky, například
:doc:`věrnostní programy <../sales/point_of_sale/pricing/loyalty>“, :doc:`ceníky
<../prodej/prodejna/cenotvorba/cenniky>, nebo :doc:`skladové položky
<../skladovani-a-mpr/sklady-a-uskladnani/sledovani-zbozi/vyuziti-lokalit>.

.._účty/firmy/odvětví/uživatelské přístupy:

Přístup uživatele
~~~~~~~~~~~

Stejně jako v prostředí více společností podporují rodičovské společnosti a pobočky flexibilní
přístup do skupiny uživatelů, a také přístup k dokumentaci o právech uživatele.
Může být udělena nebo omezena na úrovni mateřské společnosti, pobočky nebo obojího. Například
Uživatel může být omezen na konkrétní pobočku, zatímco administrátor s přístupem k mateřské společnosti
může spravovat všechny související pobočky.

.._generál/firmy/oddělení/sdílené záznamy:

Společné záznamy
~~~~~~~~~~~~~~

V Odoo jsou některé záznamy výchozími pro jednu entitu nebo sdílené mezi více entitami.
mateřská společnost a všechny její pobočky.

Při vytváření cenové nabídky, faktury nebo dodavatelské faktury je automaticky vybrána aktivní společnost nebo pobočka.
vybírá a zobrazuje v poli „Společnost“ . Pokud je aktivní společnost mateřskou společností
nebo jeho pobočky, pak jsou přístupné pouze záznamy přímo spojené s touto entitou.
Tato entita je viditelná pouze při výběru společnosti nebo pobočky pomocí odkazu na:ref:`společnost
selector <všeobecné/více společností/sledující společnost>.

Naopak některé záznamy, jako například produkty nebo kontakty
<Všeobecné/více společností/souborů sdílených a nesdílených záznamů>, nejsou vázány na žádnou konkrétní entitu a jsou
Sdílené v rámci mateřské společnosti a všech jejích poboček. Nicméně je možné omezit
jedinou entitou nastavením vhodné hodnoty pole :guilabel:`Společnost`, pokud je potřeba.

.. viz též:
:ref:`Účetnictví poboček <účetnictví/pobočky>`

.._generální/firmy/oddělení/účetnictví:

Reportáž
~~~~~~~~~

Všechny zprávy lze vytvořit pouze pro mateřskou společnost.
nebo s jeho pobočkami na základě:ref:`přístupu uživatele <obecné/multicompany/user-access>`.

..toctree::


společnosti/více společností
společností/zpracování e-mailů
společností/příklad emailu
