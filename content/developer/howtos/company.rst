
.. odkaz/jak-na-to/firma:

========================
Multioborové pokyny
========================

.. varování:

Tento návod vyžaduje dobré znalosti systému Odoo.
Prosím, nejprve se podívejte na návod :doc:`../tutorials/server_framework_101`, pokud je potřeba.

Od verze 13.0 může uživatel být přihlášen do více společností najednou. To umožňuje uživateli
získávat informace z více společností, ale také vytvářet/upravovat záznamy ve více společnostech.
environmentální.

Pokud není správně řízena, může být zdrojem mnoha nekonzistentních chování více společností.
Příkladem může být uživatel přihlášený do obou firem A a B, který vytvoří objednávku ve firmě A.
přidat do ní produkty společnosti B. Výjimkou je pouze případ, kdy se uživatel odhlásí z
dojde k chybám při přístupu ke smlouvě o prodeji.

Odoo poskytuje mnoho funkcí pro správu chování více společností:

- :ref:`Společností závislé pole <jak_na_to/spolecnosti/spolecnost_zavisle_pole>`
- :ref:`Soulad mezi více společnostmi <jak_udělat/firma/zjistit_firmu>`
- :ref:`Výchozí společnost <jak_na_to/spolecnosti/vychazispolecnost>`
- :ref:`Názory <jak_na_firmu/nazory>`
- :ref:`Pravidla bezpečnosti <jak_na_firmu/bezpecnost>`

..._jak-na-to/firma/firma-zavisla:

Společností závislé pole
------------------------

Když je záznam k dispozici od více společností, musíme očekávat, že budou mít různé hodnoty.
přiřazen k určitému poli podle společnosti, která hodnotu nastavila.

Pro pole stejného záznamu může podporovat více hodnot, pokud je definováno atributem
Vlastnost „závislost na společnosti“ nastavena na hodnotu True.

... kódový blok:: python

od odoo importujeme moduly api, fields a models

třída Record(model.Model):
_name = 'rekorde.veřejné'

info = fields.Text
společnost_info = pole.Text(společnost_závislá=True)
display_info = pole.Text(string='Informace', výpočet='_výpočet_zobrazení_informací')

@api.depends_context('firma')
def _vypočítat_zobrazovací_informace(sebe):
pro rekord v sobě:
zobrazit_informace = informace_o_záznamu + informace_o_společnosti

.. poznámka: Metoda _compute_display_info je ozdobena metodou depends_context('company')
(viz atribut ~odoo.api.depends_context) a zajistit, aby vypočítaná pole byla znovu vypočítána
podle aktuální společnosti (self.env.company).

Při čtení pole závislého na společnosti se použije aktuální společnost k získání jeho hodnoty. V ostatních
slovy, pokud uživatel je přihlášen do společností A a B s A jako hlavní společností a vytvoří záznam pro
firma B, hodnota závislých polí bude stejná jako u firmy A.

Pro přečtení hodnot polí závislých na společnosti nastavených jinou společností než je aktuální potřebujeme
abychom si ověřili, že používáme správnou společnost. To lze provést metodou:
která aktualizuje současnou společnost.

... kódový blok:: python

   # Přístup přes hlavní společnost (self.env.company)
val = pole závislé na společnosti v rekordu

   # Přístup jako požadovaná společnost (firma_B)
val = rekord.společností(firma B).Společnost závislá na poli
   # record.s_firmy(firma_B).env.firma == firma_B

.. varování:

Kdykoli počítáte/vytváříte/... něco, co se může chovat jinak
v různých společnostech, měli byste se ujistit, že děláte to, co dělat chcete.
v dobré společnosti. Není třeba za každou cenu používat sémantiku „s firmou“.
aby se vyhnuli problémům později.

.. kódový blok:: python

@api.onchange('jméno pole')
def onchange_field_name(self):
self = self.s_firmy(self.firmovy_id)
        ...

@api.depends('pole 2')
def _vypočítat_pole_3(self):
pro rekord v sobě:
record = record.s_firmy(record.firma_id)
          ...

...jakto/firma/zjistit-firmu:

Soulad mezi více společnostmi
-------------------------

Pokud je záznam sdílen mezi více společnostmi pomocí pole „company_id“,
musí dbát na to, aby se k záznamu jiné společnosti nemohlo připojit pomocí vztahového pole.
Například nechceme mít prodejní objednávku a její fakturu patřící různým společnostem.

Aby bylo zajištěno jednotné fungování více společností, musíte:

* Nastavte atribut třídy _check_company_auto na hodnotu True.
* Definujte vztahová pole s atributem „check_company“ nastaveným na hodnotu „True“, pokud jejich model obsahuje
pole „ID společnosti“.

Na každé metodě :meth:`~odoo.models.Model.create` a :meth:`~odoo.models.Model.write` jsou automatické kontroly
bude spuštěna, aby se zajistila konzistence záznamů mezi společnostmi.

... kódový blok:: python

od odoo importujeme pole a modely

třída Record(model.Model):
name = 'record.shareable'
_check_company_auto = True

company_id = fields.many2one('res.company')
jiný_rekordní_id = pole.Mnoho2jedna(jiný.rekord, ověření společnosti = True)

.. poznámka: pole company_id nesmí být definováno s hodnotou check_company = True.

.. současný modul: odoo.model
...automethod:Model._check_company

Upozornění: Funkce „check_company“ provádí přísnou kontrolu! To znamená, že pokud záznam nemá
(tj. pole není povinné), nelze ho propojit s záznamem, jehož
je nastaveno.

.. poznámka::

Pokud není na poli definována žádná doména, pokud je nastaveno check_company na hodnotu True,
přidáno: ['|', '(company_id', '=', False), '(company_id', '=', company_id)]

...jakto/firma/výchozí firma:

Nadnárodní společnost
---------------

Když je pole „company_id“ na modelu vyžadováno, dobrou praxí je nastavit výchozí hodnotu
firma, která usnadňuje průchodnost nastavení pro uživatele a dokonce i garantuje jeho platnost v případě, že je
skrytý před zraky uživatele. Ve skutečnosti je společnost obvykle skryta, pokud uživatel nemá přístup k
více společností (tj. v případě, že uživatel nemá skupinu „base.group_multi_company“).

... kódový blok:: python

od odoo importujeme moduly api, fields a models

třída Record(model.Model):
name = 'record.restricted'
_check_company_auto = True

company_id = fields.many2one(
'soukromá společnost', vyžadováno=pravda, výchozí hodnota=lambda sebe: sebe.obchodní prostředí
       )
jiný_rekordní_id = pole.Mnoho2jedna(jiný.rekord, ověření společnosti = True)


..._jak-na-to/firma/pohledy:

Názory
-----

Jak je uvedeno výše v části „Firma“ (viz odkaz na začátku článku), firma bývá obvykle skrytá.
z pohledu uživatele, který nemá přístup k více společnostem. Toto hodnotí skupina
„base.group_multi_company“.

... blok kódu::xml


<políčko name="jméno">povolená forma záznamu</políčko>
<položka jméno="model">record.restricted</položka>
<položka jméno="arch" typ="xml">
<form>
<list>
<skupina>


<pole název="další záznam ID"/>


</list>

</p>
</záznam>


..._jak-na-firmu-a-bezpecnost

Bezpečnostní pravidla
--------------

Při práci s nahrávkami sdílenými mezi společnostmi nebo omezenými na jednu společnost musíme vzít
o tom, aby uživatel neměl přístup k záznamům jiných společností.

Toho je dosaženo pomocí bezpečnostních pravidel založených na proměnných „company_ids“, které obsahují aktuální společnosti
uživatel (firmy, které si uživatel zkontroloval pomocí widgetu pro více společností).

... blok kódu::xml

<!-- Sdílené záznamy -->
<záznam modelu "ir.rule" s ID "záznam společného podnikání - pravidlo">
<field name="název">Společný záznam: více společností</field>
<field name="model_id" ref="model_record_sdílená"/>
<pole jméno="globální" hodnota="Pravda"/>
<pole název="doména_povinná">
['|', ('company_id', '==', False), ('company_id', 'in', company_ids)]
</p>
</záznam>

... blok kódu::xml

<!-- Společnostem přístupné záznamy -->
<záznam typu "ir.rule" s ID "záznam_s_omezeným_přístupem_pro_firmy">
<pole jméno="název">Omezený záznam: více společností</pole>
<políčko jméno="model_id" odkaz="model_record_restricted"/>
<pole jméno="globální" hodnota="Pravda"/>
<pole název="doména_povinná">
[('společnost_id', 'in', společnost_id)]
</p>
</záznam>

...::check_company na poli závislém na společnosti.
