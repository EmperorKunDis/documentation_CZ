===========
Těžba olova
===========

.. |IAP| nahradit za: zkratka: `IAP (In-App Purchase)`
.. |CC| nahradit: :guilabel:'Společnosti a jejich kontakty'

Těžba cínu je funkcí, která umožňuje uživatelům CRM vytvářet nové kontakty přímo do systému Odoo.
databáze. Kvalifikace vedení je určena množstvím filtrování
kriteria jako země, velikost společnosti a odvětví.

Konfigurace
=============

Chcete-li začít, přejděte na: „Aplikace CRM --> Konfigurace --> Nastavení“ a zaškrtněte
Zatrhněte políčko „Těžba“ a klikněte na tlačítko „Uložit“.

.. obrázek: aktivace těžby olova/aktivace těžby olova.png
:align:center
:alt:Aktivujte těžbu olova v nastavení CRM Odoo.

Vytvářejte leady
==============

Po aktivaci nastavení „Těžba kontaktů“ se objeví nová tlačítka s názvem „Vytvořit kontakty“.
použít v horním levém rohu aplikace CRM Pipeline (výběr menu: CRM aplikace - Prodej - Moje
Plynovod").

Žádosti o těžbu cínu jsou také dostupné přes:menuselection:`CRM aplikace --> Konfigurace --> Žádost
Těžební požadavky“ nebo prostřednictvím „:menuselection: CRM aplikace --> Kontakty --> Kontakty“, kde
Tlačítko „Vytvořit lead“ je také k dispozici.

.. obrázek:: těžba olova/generovat-leady-tlačítko.png
:align:center
:alt:Tlačítko Vytvořit kontakt, které lze použít k funkci těžby kontaktů.

Klikněte na tlačítko „Vytvořit kontakt“ a v okně se objeví různé možnosti.
kriteria, podle kterých generovat leady.

.. obrázek: lead_mining/generate-leads-popup.png
:align:center
:alt:Okno s výběrovými kritérii pro generování leadů v Odoo.

Vyberte možnost generování leadů pro:guilabel:Společnosti`, abyste dostali informace pouze o společnostech nebo
Získat informace o společnosti a kontaktní údaje jednotlivých zaměstnanců.

.. poznámka::
Když se zaměříte na |CC|, máte k dispozici další možnosti filtrování kontaktů podle
:guilabel:`Role“ nebo :guilabel:`Pozice“.

Další filtrační možnosti zahrnují následující:

- :guilabel:`Státy“: filtrujte výsledky podle země, ve které se nachází.
- Filtr „Státy“: další filtr vede k výběru států podle jejich umístění, pokud
aplikovatelné.
- :guilabel:`Průmysly“: filtrovat nabídky podle konkrétního průmyslu, ve kterém pracují.
- Zatrhněte políčko „Filtr podle velikosti“ a zadejte počet zaměstnanců v dané firmě.
Vytvoří pole s názvem „Velikost“ a vyplňte mezery, abyste vytvořili rozsah pro
požadované velikosti společnosti.
- :guilabel:`Prodejní tým“: vyberte, k jakému prodejnímu týmu budou leady přiřazeny.
- :guilabel:`Prodejce“: vyberte, koho ze členů prodejního týmu budou leady přidělovány.
- :guilabel:`Výchozí štítky“: vyberte, které štítky se aplikují na objevené kontakty hned po jejich nalezení.

.. důležité:
Zajistěte si, že budete informováni o nejnovějších evropských předpisech při získávání kontaktních údajů.
informace o Obecném nařízení o ochraně osobních údajů na stránce „Odoo GDPR <http://odoo.com/gdpr>“.

Zobrazení pohledů
----------

Po vytvoření leadů jsou přiděleny určenému prodejci a týmu.
Pokud chcete získat další informace o kontaktu, vyberte si jeden ze seznamu a klikněte na něj pro jeho otevření.

V diskuzním vláknu k hlavnímu tématu se poskytuje další informace. Může jít například o číslo
zaměstnanců, technologií používaných společností, časového pásma a kontaktních údajů.

.. obrázek: těžba olova/vzniklé olovo.png
:align:center
:alt:Diskuzní vlákno nově vytvořené poptávky.

.. poznámka::
Pokud nejsou v databázi povoleny leady, pak se leady generují jako
*možnosti*, a přidaly se do prodejního řetězce určenému prodejci.

Pro zapnutí funkce „Vedení“ přejděte na kartu „Konfigurace“.
--> Nastavení a zaškrtněte políčko „Vedení“. Pak klikněte na „Uložit“.

Ceny
=======

Těžba olova je funkcí In-App Purchase a každý vytěžený kus stojí jeden :ref:`kredit
<platba v aplikaci/kredity>.

.. důležité:
Vytváření |CC| stojí jedno další kredit za každý kontakt, který byl vytvořen. Podrobnosti naleznete zde.
informace o ceně: „Odoo IAP Lead Generation


Kredity si můžete koupit v aplikaci CRM: „Nastavení“ → „Konfigurace“.
V sekci „Generování kontaktů“ pod funkcí „Těžba kontaktů“ klikněte na „Koupit“.
Kredity.

Kredity lze také zakoupit po načtení aplikace „Nastavení“.
V sekci „Kontakty“ pod funkcí „Odoo IAP“ klikněte na „Zobrazit moje“.
Služby.

.. obrázek:lead_mining/view-my-services-setting.png
:align:center
:alt:Kredity si můžete zakoupit v nastavení Odoo IAP.

.. poznámka::
Uživatelé podnikového řešení Odoo s platnou licencí získají bezplatné kredity pro testování funkcí |IAP| před jejich zakoupením.
nákup dalších kreditů pro databázi. To zahrnuje i demoverze a databáze pro vzdělávání
databáze a databáze bez aplikace.

.. viz též:
:doc:`/aplikace/základní/v-aplikaci/nákupy-u-vnitř
