
:ukrýt stránku obsahující obsah:

====================
Správa zásob
====================

V aplikaci Odoo *Skladování* se o větší sklady starají
organizace a distribuce zásob mezi různými fyzickými místy, zatímco:doc:`lokace
<Inventarizace/Použití lokalit> poskytuje podrobnější rozdělení v každé skladovací místnosti.
účinné řízení položek.

Tento dokument slouží jako úvod do terminologie a pojmů nezbytných k ovládnutí
*Seznam*. Pro konkrétní pokyny a příklady, jak věci fungují, odkazujte na jednotlivé
dokumentační stránky.

.. viz také:
„Tutoriál Odoo: Sklady a lokality <https://www.youtube.com/watch?v=zMvudZVLuUo>“

Skladiště
==========

Skladiště představuje fyzické místo s fyzickou polohou.
adresa, na které je uloženo zboží společnosti.

Nastavte trasy v skladu tak, aby odpovídaly trasám
kontrolovat pohyb produktů od dodavatelů k zákazníkům, uvnitř skladu nebo mezi
sklady <dodávky/doplnění skladů>.

Lokalita
=========

„Lokalita“ („<inventory_management/use_locations>“) označuje konkrétní oblasti v skladu.
jako jsou police, podlahy nebo regály. Jsou to podskupiny v skladu a jsou jedinečné pro
skladu. Uživatelé mohou vytvářet a spravovat mnoho lokalit uvnitř jednoho skladu, aby tak uspořádali
Vyčíslení přesněji.

.. viz také:
   - :doc:`skladovani/pouziti-lokalit“
   - :doc:`skladovani/počet produktů
   - :doc:`skladové hospodářství/počet cyklů“
   - :doc:`skladové hospodářství/odpisy skladu“

... skladovací prostory, sklady, místo uložení:

Typy lokalit
--------------

Typy lokalit v Odoo pomáhají kategorizovat a spravovat produkty a činnosti, které se s nimi dějí.
s nimi vzato. Výchozí nastavení je na záložce „Inventář aplikace --> Konfigurace --> Lokality“
stránka, zobrazují se pouze vnitřní lokality.

Pro zobrazení sedmi typů lokalit v Odoo vyberte libovolnou lokaci a klikněte na „Typ lokalit“.
místo je zde:

- :guilabel:`Lokalita dodavatelů“: definuje oblast, odkud pocházejí produkty nakoupené u dodavatelů.
Zde jsou položky **nepřítomné**.

- :guilabel:`Pohled“: používá se k uspořádání a strukturování hierarchie skladu. Například pohled
lokalita „WH“ (zkratka pro sklad) obsahuje všechny vnitřní lokality, například „Zásoby“.
doky, kontrolní stanoviště kvality a balicí prostory, aby bylo zřejmé, že patří ke stejnému skladu.

... důležité::
Zobrazení poloh by nemělo obsahovat produkty, ale je možné je sem přesunout.

- :guilabel:`Vnitřní umístění“: skladovací prostory uvnitř skladu. Zboží, které je zde
lokality jsou zahrnuty v inventarizačním ocenění:
<../produktove-rizeni/hodnoteni-skladu/vyuziti-hodnoteni-skladu>.

- :guilabel:`Lokalita zákazníka“: zde jsou sledovány prodané produkty, položky zde již nejsou skladem.

- :guilabel:'Ztráta zásob': místo pro spotřebu chybějících položek nebo vytvoření zásob.
vyrovnávání rozdílů.

V Odoo jsou příklady míst ztráty zásob například „Změna zásoby“, která se používá k účtování
rozdíly při inventarizaci a Scrapy, kde se poškozené zboží posílá.
účtovat ztráty skladových zásob.

... příklad::
„Virtuální lokace / Změna zásob“ je místo s :guilabel:`Ztrátou zásob“.
typu. Databáze ukazuje 65 jednotek v WH/Sklad, ale inventura odhalí 60.
opravit množství, pět jednotek se přesouvá z „Skladu“ do „Virtuálních místností/Zásob
Změna.

.. obrázek: inventarni-systemy/ztrata-v-skladu.png
:align: střed
:alt: Zboží končí v virtuálních skladech/výpočtu zásob.

- :guilabel:`Výroba“: kde jsou spotřebovávány suroviny a vyráběny výrobky.
Výrobní data jsou vytvářena.

- :guilabel:`Přechodové místo“: používá se pro vnitropodnikové nebo mezi sklady operace k sledování
produkty přepravované mezi různými adresami, např. :ref:`Fyzické umístění / Mezi sklady
přeprava (skladování)

.. obrázek: inventory_management/locations.png
:align:center
:alt: Seznam lokalit v Odoo.

.. poznámka::
V Odoo jsou typy lokalit barevně označeny:
     - **Červená**: vnitřní lokality
     - **Modrá**: zobrazení lokalit
     - **Černá**: vnější lokality (včetně ztrát zásob, dodavatelů a zákazníků).

Zobrazení poloh v Odoo
----------------------

Databáze Odoo zahrnují přednastavené pohledy na umístění, které uspořádají hierarchii míst.
poskytují užitečný kontext a rozlišují mezi vnitřními a vnějšími lokalitami.

- Skupina „Fyzické umístění“ obsahuje vnitřní lokality, jako jsou například sklady a dodavatelé.
webových stránek, protože:doc:`hodnota zásob
<../produktni-management/vykazovani-skladu/vykazovani-skladu-konfigurace> se mění pouze v případě, že je zboží
přesouvat se z interních na vnější lokality. Odoo používá fyzické lokace k sledování zásob, které jsou
nebo v přepravě bez vlivu na hodnotu.

.. skladové zásoby, sklady a přepravu mezi sklady:

...... příklad::
Při pohybu zboží v skladech „WH“ a „WH2“ se položky nezachycují ve skladu, ale
Stále patří společnosti a během přepravy jsou umístěny do „mezskladového přesunu“.
lokalitu, typ „Přestupní místo“.

Tato poloha je pod pohledem na lokaci „Fyzické umístění“, což naznačuje, že
„Vnitroskladní přeprava“ je mimo sklad, ale stále součástí společnosti.
Nepůsobí na ocenění zásob.

- Skupina „Partnerské lokality“ shromažďuje zákaznické a dodavatelské lokality (externí lokality). Převody
to tyto lokality ovlivňují ocenění zásob.
- „Virtuální lokace“ jsou lokace, které neexistují fyzicky, ale je tam umístěno zboží.
nejsou v zásobách uloženy. Jde například o předměty, které jsou již z inventáře vyřazené kvůli ztrátě.
jinými faktory.

.. toctree::
:tituly:

skladování
inventarizace/využití lokalit
inventarizační řízení/počet produktů
inventarizace/počet cyklů
inventarizace/odpisy
inventarizace/produktový katalog
