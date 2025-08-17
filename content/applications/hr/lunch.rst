Zobrazit obsah

=====
Oběd
=====

Aplikace Lunch v Odoo umožňuje uživatelům pohodlně objednávat jídlo a platit za něj
přímo z databáze.

Před použitím aplikace Lunch je potřeba provést několik konfigurací.
přidat: „Nastavení“ (<lunch/settings>), „Dodavatelé“ (<lunch/vendors>) a „Místo“ (<lunch/locations>).
<obědy/lokality>“, „produkty <obědy/produkty>“ a „kategorie produktů
<oběd/produktové kategorie>. Jakmile budou vytvořeny a nakonfigurovány, zaměstnanci si je mohou prohlédnout.
objednat jídlo.

... oběd/nastavení:

Nastavení
========

V nabídce „Nastavení“ je potřeba nakonfigurovat pouze dvě položky: nastavení přečerpání a
upozornění. Chcete-li zobrazit nastavení, přejděte na:
Nastavení.

Nastavte následující:

- :guilabel:'Překročení limitu oběda': zadejte maximální přečerpání účtu pro zaměstnance. Formát měny
je určena podle nastavení lokality společnosti.
- :guilabel:`Oznámení o přijetí“: nastavte zprávu, kterou uživatelé obdrží prostřednictvím aplikace **Discuss**
jejich jídlo bylo doručeno. Výchozí zpráva „Vaše obědová přeprava byla doručena. Užívejte si!
jídlo!“ obsadí pole, ale lze ji upravit podle potřeby.

.. tip::
Pokud má databáze nainstalované více jazyků, mnoho formulářů v aplikaci Lunch je
možnost vkládání překladů do různých polí.

Pokud jsou k dispozici překlady pro konfiguraci, za nimi se zobrazí jazyková značka.
pole na formuláři. Chcete-li přidat překlady pro toto pole, klikněte na dvojpísmenný kód jazyka
například:guilabel:'EN' pro angličtinu) a objeví se okno s překladem.

Následující je příklad pro pole „Oznámení o přijetí“ v nastavení
menu:

Přejděte do sekce „Obědy“ v části „Nastavení“ a klikněte na „EN“.
V horním pravém rohu textového pole pod sekcí „Oznámení o přijetí“.
:guilabel:"Přeložit: Oznámení o obědě v kanceláři" se zobrazí okno s možností zadání
překlad do ostatních jazyků, které používá databáze.

První sloupec uvádí různé jazyky v abecedním pořadí a aktuálně vybraný
jazyk v kurzívě. Druhá sloupec obsahuje aktuálně konfigurovaný text ve sloupci. Poslední
Každý jazyk má vlastní textovou oblast, která se nachází na konci pravého sloupce.

Do pole zadejte text, který má být pro každý jazyk, pak klikněte na tlačítko :guilabel:`Uložit`.

.... obrázek:oběd/překlad.png
:alt:Pole pro překlad s aktuálním jazykem zvýrazněným a arabštinou
překladové pole zvýrazněno.

...obědy/místa:

Lokalita
=========

Výchozí nastavení aplikace Lunch vytváří lokalitu „Sídlo společnosti“ při instalaci aplikace. Pokud
Společnost má více lokalit, musí být konfigurovány.

Chcete-li přidat lokalitu, přejděte na: „Obědová aplikace --> Konfigurace --> Lokality“.
V současné době zobrazené umístění se zobrazí v přehledu. Klikněte na tlačítko „Nový“
v horním levém rohu a pod posledním místem v seznamu se objeví prázdná řádka.

Do pole zadejte název místa. Následně klikněte do pole :guilabel:`Adresa`,
příjmení a adresu místa. Je možné zadat více řádků v
adresní pole.

Tento postup opakujte pro všechna místa, která chcete přidat.

.. obrázek: oběd/lokace.png
:alt: Zobrazení seznamu míst s novou tlačítko zvýrazněnou.

Poplachy
======

Je možné nastavit upozornění, která mohou být buď zobrazena v aplikaci Lunch, nebo odeslána
konkrétní zaměstnance prostřednictvím aplikace **Discuss**.

Žádné výstrahy nejsou přednastaveny. Chcete-li nastavit výstrahu, přejděte na:
Konfigurace > Upozornění. V pravém horním rohu klikněte na tlačítko „Nový“ a vytvořte prázdnou
Následně se načte formulář s upozorněním na oběd, do nějž zadáte následující údaje:

- :guilabel:`Název výstrahy“: zadejte název výstrahy. Tento by měl být krátký a popisný, například
„Nová dodavatelská společnost obědů“ nebo „Objednejte do 11:00“. Toto pole je **povinné**.
- Viditelnost zprávy: Zvolte, jestli chcete zprávu vidět v aplikaci Lunch (:guilabel:"Zpráva ve
aplikace nebo zaměstnancům zaslán prostřednictvím aplikace **Discuss** v okně chatu (:guilabel: Chat
oznámení').

  - Pole „Adresáti“ se objeví pouze v případě, že je vybráno pole „Zprávy o chatu“.
možnost Zobrazit. Zvolte, kdo dostane upozornění na chatu. Možnosti jsou:
:guilabel:"Každý", :guilabel:"Zaměstnanec, který objednal minulý týden", :guilabel:"Zaměstnanec,
„Zaměstnanec, který objednal v minulém měsíci“, nebo „Zaměstnanec, který objednal loni“.

- :guilabel:`Lokalita“: vyberte z roletky lokality, na které se upozornění má zobrazit.
Vybrat lze více míst. Toto pole je povinné, protože pokud se upozornění týká
vyberte všechna místa ze seznamu.
- :guilabel:`Zobrazit do“: pokud chcete, aby upozornění vypršelo na konkrétní datum, zvolte datum v
kalendářový výběr.
- :guilabel:`Aktivní“: tato volba je zapnuta (zobrazuje se zeleně) výchozí hodnotou. Chcete-li vypnout upozornění, klikněte na
přepnout tak, aby už nebyla zelená.
- :guilabel:`Zpráva“: Zadejte upozornění v tomto poli. Toto pole je **povinné**.
- Vyberte dny v týdnu, kdy by měla být zpráva odeslána. Výchozí nastavení je
Všechny sedm dní jsou aktivní. Klikněte na zaškrtávací políčko, abyste změnili nastavení z aktivního na neaktivní.

Pokud byl zvolen v poli „Zobrazit“ parametr „Upozornění na chat“,
:guilabel:`Časová značka“ pole také zobrazí. Zadejte čas, kdy má být odeslána zpráva v chatu. Pak vyberte
pokud je čas buď AM nebo PM pomocí vybraného políčka vpravo.
pole „Čas“.

.. obrázek:oběd/upozornění.png
:alt:Formulář s upozorněním na chatu se všemi informacemi vyplněnými pro upozornění zaslané v 10:30 ráno
požadovali, aby zaměstnanci objednávky podávali do 11:30 hodin.

.. viz též:
   - :doc:`oběd/prodejci“
   - :doc:`oběd/produkty“
   - :doc:`oběd/objednávky“
   - :doc:`oběd/uživatelské účty“
   - :doc:`oběd/manažerské dovednosti“

..toctree::


oběd/prodejci
oběd/produkty
oběd/objednávky
oběd/uživatelské účty
oběd/manažer
