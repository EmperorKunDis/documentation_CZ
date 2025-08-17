=======================================
Kapitola 13: Interakce s ostatními moduly
=======================================

V předchozím oddílu <12_dědičnost> jsme použili dědičnost k
změnit chování modulu. V našem scénáři s nemovitostmi bychom chtěli jít ještě dál
a vytvářet faktury pro naše zákazníky. Modul Fakturace je součástí Odoo, takže
by bylo pěkné vytvářet fakturu přímo z našeho modulu nemovitostí, tedy jednou nemovitosti
je nastaven na „Prodáno“, v aplikaci Fakturace je vytvořen fakturační doklad.

Příklad: přesun účtu
==============================

.. poznámka::

**Úkol**: na konci této části:

    - Nový modul „účetní evidence“ by měl být vytvořen
    - Při prodeji nemovitosti je třeba vystavit fakturu kupujícímu

.. obrázek: 13_other_module/create_inv.gif
:align: střed
:alt: Vytvoření faktury

Každý moment, kdy interagujeme s jiným modulem, musíme mít na paměti modulárnost. Pokud se chceme vyhnout problémům,
nabídnout aplikaci realitním kancelářím. Některé z nich by mohly chtít i fakturační modul.
Někdo jiný si ho nemusí přát.

Modul odkazů
-----------

Pro takové použití je běžným postupem vytvořit modul „odkaz“. V našem případě je tento modul
závisí na „majetku“ a „účtu“ a zahrnuje logiku vytváření faktur.
majetkového účetnictví. Tímto způsobem lze nainstalovat moduly nemovitostí a účetnictví.
nezávisle na sobě. Když jsou oba nainstalovány, modul pro propojení poskytuje novou funkci.

.. cvičení: Vytvořit modul odkazu.

Vytvořte modul „účet“ (estate_account), který závisí na modulech „majetek“ a „účet“.
Ale zatím bude prázdná skořápka.

Tip: už jste to udělali v
:dokument: „začátek návodu <02_novaplikace>“. Proces je velmi
podobné.

Když se v seznamu objeví modul „účetní kniha“, nainstalujte ho. Zjistíte, že
Instaluje se i Fakturace, což je očekávané, protože váš modul na ní závisí.
Pokud odinstalujete aplikaci Fakturace, bude odinstalován i váš modul.

... _tutorials/server_framework_101/13_other_module/create:

Vytvoření faktury
----------------

Nyní je čas vytvořit fakturu. Chceme přidat funkci
„majetek“ model, tedy chceme přidat nějakou další logiku pro případ, kdy je nemovitost prodána.
Zní vám to povědomě? Pokud ne, je dobré se vrátit k
:kapitola „Dědičnost“ (<12_inheritance>) protože jste ji možná přehlédli
něco :-)

Prvním krokem je rozšíření akce volané při stisku
Tlačítko „Prodat“ na nemovitosti (<09_actions>).
vytvořit model dědění v oblasti účetnictví.
modul pro „majetek a nemovitosti“. V současné době převzatá akce pouze vrátí
„super“ volání. Možná příklad vysvětlí, co myslím:

od odoo importujeme modely

třída Dědičný model (modelů.Model):
_inherit = "dědičný model"

def inherited_action(self):
vrací se zpět do super().inherited_action

Praktickým příkladem je například
„tady <https://github.com/odoo/odoo/blob/f1f48cdaab3dd7847e8546ad9887f24a9e2ed4c1/addons/event_sale/models/account_move.py#L7-L16>“.

...cvičení: Přidejte první krok vytváření faktury.

    - Vytvořte soubor „estate_property.py“ v příslušné složce modulu „estate_account“.
    - „dědit“ model „majetku“.
    - Změňte metodu „action_sold“ (možná jste ji pojmenovali jinak), aby vracela „super“.
hovor.

Tip: abyste si byli jisti, že funguje, přidejte tisk nebo bod zastavení v metodě, kterou překrýváte.

Funguje to? Pokud ne, možná je třeba zkontrolovat, že jsou všechny soubory ve formátu Python správně importovány.

Pokud převod probíhá správně, můžeme pokračovat a vystavit fakturu. Bohužel
je nelehké zjistit, jak vytvořit libovolný objekt v Odoo. Většinou je nutné
podívat se na jeho model, najít požadovaná pole a poskytnout odpovídající hodnoty.

Dobrý způsob, jak se něco naučit, je podívat se na to, co už jiná modulová knihovna dělá tak, jak chcete vy. Například
Základními toky prodeje je vytvoření faktury z objednávky na prodej. To vypadá dobře
začátek, protože dělá přesně to, co chceme udělat. Vyhraďte si čas na to, abyste si přečetli a pochopili
Vytvoření faktur <https://github.com/odoo/odoo/blob/f1f48cdaab3dd7847e8546ad9887f24a9e2ed4c1/addons/sale/models/sale.py#L610-L717>
metoda. Když se doplačete z toho jednoduchého úkolu, který vypadá až příliš složitě, můžeme pokračovat.
přednášky.

Pro vystavení faktury potřebujeme následující informace:

- „partner_id“: zákazník
- „typ pohybu“; má několik „možných hodnot <https://github.com/odoo/odoo/blob/f1f48cdaab3dd7847e8546ad9887f24a9e2ed4c1/addons/account/models/account_move.py#L138-L147>“
- „journal_id“: účetní deník

Takto vznikne prázdný doklad.

...cvičení: Přidejte druhý krok vytváření faktury.

V metodě „action_sold“ vytvořte prázdný objekt „account.move“:

    - „partner_id“ je vzata z aktuální „majetku“.
    - „move_type“ by měl odpovídat „Faktura pro zákazníka“.

Tipy:

    - Vytvořit objekt použijte „self.env[model_name].create(values)“, kde „values“
Je to „diktát“.
    - Metoda „Vytvořit“ nepřijímá pole záznamů jako hodnotu pole.

Když je nemovitost nastavena na „Prodáno“, mělo by být vytvořeno nové fakturační upozornění pro zákazníka.
Fakturace / zákazníci / faktury.

Zatím nemáme žádné fakturační řádky. Chceme-li vytvořit fakturační řádek, potřebujeme
informace:

- „název“: popis linky
- „množství“
- „cena_jednotky“

Dále je nutné vázat fakturační řádek na fakturu. Nejjednodušší a nejefektivnější způsob
Připojit linii k faktuře je zahrnout všechny linie při vytváření faktury.
V poli „fakturační řádek“ je zahrnuto pole „vytvoření pohybu“, které je
:třída ~odoo.pole.One2many. One2many a Many2many používají speciální „příkazy“, které jsou
byly převedeny do čitelné podoby pomocí prostoru jmen `~odoo.fields.Command`. Tento prostor jmen představuje
Trojice příkazů k provedení na sadě záznamů. Trojice byla původně jedinou možností
těmto příkazům, ale nyní je běžné používat místo nich prostor jmen. Formát je takový, že se
v seznamu, který je prováděn postupně. Tady je jednoduchý příklad zahrnutí One2many
pole „line_ids“ při vytváření objektu „test_model“:

od odoo importujeme příkaz

def inherited_action(self):
self.env["test_model"].vytvořit (
            {
"name": "Test",
"line_ids": [
Command.create({
"field_1": "value_1",
"field_2": "value_2",
                    })
                ],
            }
        )
vrací se zpět do předchozího metodu

...cvičení: Přidejte třetí krok vytváření faktury.

Přidejte dvě řádky faktury během vytváření „účetního pohybu“. Každý prodaný majetek
bude vyúčtována podle těchto podmínek:

    - 6 % z prodejní ceny
    - dalších 100 Kč z poplatků za správu

Tip:Přidejte „fakturační řádek“ vytvořením podle příkladu výše.
Pro každou řádek potřebujeme „název“, „množství“ a „jednotku ceny“.

Tento kapitol může být jedním z nejnáročnějších, které byly dosud pokryty, ale je také nejbližším.
jaké bude v praxi vývoj aplikací na platformě Odoo. V další kapitole
<14_qwebintro>, představíme si šablonovací mechanismus používaný v Odoo.
