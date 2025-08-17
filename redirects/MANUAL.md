# Pravidla pro přesměrování

## Co jsou pravidla pro přesměrování?

Pravidla přesměrování umožňují přesměrovat uživatele na novou dokumentační stránku, když se ocitnou na staré stránce.
Tyto soubory jsou uloženy v adresáři .txt a jsou buď přejmenovány nebo přesunuty na jiné místo.
Podadresář „redirects/“ v kořenovém adresáři dokumentace. Každá řádka těchto souborů určuje jednu
pravidlo, které se vztahuje na jednu stránku dokumentu.

## Jak fungují pravidla pro přesměrování?

Pro každý pravidlo přesměrování vytvoří rozšíření Sphinxu **redirects** prázdný soubor HTML na dané adrese
určeného cíle pouze pomocí značky „meta http-equiv="refresh"“ v záhlaví. Když uživatelé
návštěvu souboru HTML, vyvolá se klientská přesměrování a prohlížeč načte cílovou stránku.
Stránka s dokumentací.

Podrobnější informace najdete na adrese https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta#attr-http-equiv
informace.

## Jak vytvořím pravidlo pro přesměrování?

1. Otevřete soubor s textem uvnitř složky „redirects“ odpovídající verzi, se kterou právě pracujete.
Příkladem je příkaz „redirects/13.0.txt“ v případě přesunu nebo přejmenování zdrojového souboru (.rst).
dokumentace ve verzi 13.0 dokumentace. Pokud soubor ještě neexistuje, vytvořte
je.
2. Hledejte blok přesměrovacích pravidel souvisejících s tím, který chcete přidat. Například hledejte
blok přesměrovacích pravidel, které začínají na „applications/sales/sales“, pokud přidáváte přesměrování.
pravidlo pro stránku v aplikaci Prodej. Pokud blok ještě neexistuje, vytvořte ho.
Bloky pro aplikace nebo rozsahy a pravidla přesměrování musí být seřazeny abecedně.
3. Vložte svou pravidla přesměrování do bloku. Linie by měla mít následující vzor:

„cesta k starému souboru.rst cesta ke novému souboru.rst # volitelný komentář“

## Kdy vytvořit pravidlo pro přesměrování?

Pokud přesunete nebo přejmenujete zdrojový soubor, pravděpodobně budete potřebovat vytvořit pravidlo pro přesměrování pro tento soubor.
Pravidlo přesměrování musí být v následujících případech doplněno:
1. Zdrojový soubor je přejmenován.

Příklad: Např. se soubor contributing/documentation/guidelines.rst přejmenuje na
„contributing/documentation/rst_guidelines.rst“ protože přidáváte nový „content_guidelines.rst“.
souboru. Pravidlo pro přesměrování by mělo být:

`contributing/documentation/guidelines.rst contributing/documentation/rst_guidelines.rst
2. Zdrojový soubor je přesunut z jednoho místa na druhé.

Příklad:Stránka s vývojářskými pokyny je přesunuta z `developer/misc/guidelines.rst` na
„přispět/vyvíjet/pravidla.rst“. Pravidlo přesměrování by mělo být:

`developer/misc/guidelines.rst contributing/develop/guidelines.rst # Přesunout všechny pokyny do sekce přispívání`
3. Souborů s různými zdroji je spojeno do jednoho.

Příklad: Celý obsah souboru „administace/instal/odoo_sh.rst“ je přesunut do
„administrace/odoo_sh.rst“ a první soubor je smazán. Pravidlo přesměrování by mělo být:

„správa/instalace/odoo_sh.rst správa/odoo_sh.rst  # Přesunout všechny informace týkající se Odoo.sh na jednu stránku“

Pravidlo přesměrování by nemělo být vytvořeno, pokud byl smazán zdrojový soubor bez alternativy.
