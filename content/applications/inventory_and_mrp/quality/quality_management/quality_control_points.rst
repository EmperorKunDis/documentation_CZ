======================
Kontrolní body kvality
======================

...kvalita/kvalitní řízení/kontrolní body kvality:
.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`
.. |MOs| nahradí za: zkratku: `MOs (Manufacturing Orders)`
.. |QCP| nahradit za :: abbr: QCP (kontrolní bod kvality)
.. |QCPs| nahradí: zkratka `QCPs (Kontrolní body kvality)`

V Odoo se používají kontrolní body kvality (QCP) pro automatické vytváření:doc:`kontroly kvality.
kontrolách kvality v předem stanovených intervalech. QCPs lze konfigurovat tak, aby vytvářely
konkrétní operace (výroba, dodání apod.) a konkrétní produkty uvnitř těchto
operace.

Používání QCP umožňuje týmům kvality zajistit, aby byly produkty pravidelně kontrolovány na vady.
další problémy.

Nastavte kontrolní body kvality
================================

Pro vytvoření nového bodu kontroly přejděte na: „Kvalita“ > „Kontrolní body“
a pak klikněte na „Nový“.

Začněte vyplňovat nový QCP zadáním unikátního názvu „Title“, který usnadní identifikaci QCP.
identifikovatelné.

V poli „Produkty“ vyberte jeden nebo více produktů, na které se |QCP| má vztahovat. Pokud
|QCP| by měl být aplikován na celou kategorii produktů, vybrat ji v poli „Kategorie produktu“
pole.

V poli „Operace“ vyberte operaci (operační), která by měla spustit |QCP|.
Příkladem je výběr možnosti „Výroba“ v poli „Provoz“, což způsobí
kontrola kvality pro nové výrobní objednávky (MO).

.. poznámka::
Při vytváření nového |QCP| musí být alespoň jedna operace uvedena v poli :guilabel:`Operace`.
pole. Nicméně pole „Produkty“ a „Kategorie produktů“ mohou být nevyplněna.
. Pokud jsou prázdné, generuje |QCP| kvalitativní kontroly pro každý případ použití.
určité operace.

Pokud je v poli „Operace“ vybrána operace „Výroba“, zobrazí se nové
V poli pod ním se objeví pole s názvem „Operace objednávky“. V tomto poli vyberte konkrétní
pracovní příkaz pro kontrolu kvality této operace namísto výrobního procesu.
všeobecně.

Příklad:
A |QCP| může být konfigurováno tak, aby vytvářelo kvalitativní kontroly pro objednávku „Sestavení“ zadanou v „Kávičce“.
Produkt stolu. Poté, co je nový MO pro stůl potvrzen, vytvoří QCP produkt Coffee Table.
kontrola kvality specifická pro operaci „Sestavení“.

V poli „Kontrola“ je nastaveno jedno ze tří možností, které určují, kdy se zobrazí nová kvalita.
vytváří se kontrola:

- :guilabel:`Operace“: Požaduje se jedna kontrola pro danou operaci jako celek.
- :guilabel:Produkt: Požaduje se jedna kontrola za každý *jedinečný* produkt, který je součástí specifikovaného
operace. Například dodání stolu a čtyř židlí by vygenerovalo dvě
kontrolu, protože se jedná o dvě *jedinečné* produkty.
- :guilabel:`Množství“: Požaduje se kontrola pro určité procento položek v rámci specifikovaného
operaci. Tento podíl je nastaven zaškrtnutím políčka „Částečná převodová zkouška“ a
Pak zadejte číslo v poli „Procento“, které se objeví pod tímto textem.
Pokud je zaškrtávací políčko neaktivní, vytvoří se jedna kontrola kvality pro celé množství.

V poli „Kontrolní frekvence“ je nastavená jedna ze tří možností, které určují, jak často
je vytvořen nový kvalitativní kontrolní bod:

- :guilabel:`Všechny“: Kontrola kvality je požadována vždy, když jsou splněny podmínky |QCP|.
- :guilabel:`Náhodně“: Kvalitativní kontrola je náhodně požadována pro určité procento
operace, které lze specifikovat v poli „Každé # % operací“, které se objevuje

- :guilabel:`Periodicky“: Požaduje se kontrola kvality každých x měsíců.
specifikované zadáním číselné hodnoty do pole níže a výběrem buďto „Dny“,
:guilabel:`Týdny“ nebo :guilabel:`Měsíce“ jako požadovanou dobu trvání.

V poli „Typ“ zadejte typ kontroly kvality, která má být provedena.
metoda zpracování kvalitativních kontrol vytvořená společností QCP závisí na typu kvalitativní kontroly
vybráno:

- :guilabel:`Návod k použití“ poskytuje konkrétní pokyny, jak dokončit kvalitu.
kontrola.
- :guilabel:„Vyfoťte si produkt“ vyžaduje, aby byl později zkontrolován obrázek produktu.
přidělený tým kvality.
- :guilabel:„Registrace výroby“ vyzývá pracovníky v provozu k potvrzení množství
produkt, který byl vyroben během výrobního procesu.
- :guilabel:`Přeskočit - Neprošlo“ kontroly stanovují kritérium, které musí produkt splňovat pro úspěšné provedení kontroly.
- :guilabel:„Měření“ vyzývá zaměstnance, aby zaznamenali měření produktu, který musí být
v rozmezí tolerance norem, aby se test považoval za úspěšný.
- Povinnost vyplnit interaktivní formulář při zpracování šeku je pro zaměstnance, který šek zpracovává.
pracovní list.
- Povinnost vyplnit tabulku pro kontrolu platby vyžaduje, aby zaměstnanec provádějící kontrolu vyplnil
interaktivní tabulka.

.. důležité:
*Návod k použití* je stejné jako krok v pracovním příkazu pro MO.

Když je k pracovnímu příkazu přidán další krok, Odoo uloží tento krok do aplikace Kvalita jako |QCP|.
Je možné vytvořit ručně |QCP| s typem kontroly *Návod*, dokonce i přiřadit ho k
jiná než výroba, například příjmy.

Nicméně při vytváření kontrolního bodu určeného pro účely kvality se používá
Problém je, že jiný typ kontroly je pravděpodobně účinnější.

.. poznámka::
Při vytváření |QCP| s kontrolními typy :guilabel:`Worksheet` nebo :guilabel:`Spreadsheet`
Je nutné specifikovat šablonu pro kvalitu nebo tabulku pro kvalitu.
:guilabel:`Šablona“ pole, které se zobrazuje pod :guilabel:`Typ“.

Vybraný šablona se vytiskne pro každou kvalitativní kontrolu vytvořenou pomocí QCP a **musí být**
vyplněny, aby se mohla provést kvalitativní kontrola.

Chcete-li vytvořit nový šablonu, přejděte na: menu: „Kvalita aplikací --> Konfigurace --> Kvalita
„Šablony listů“ a klikněte na „Nový“.

V poli `Tým` zadejte kvalitní tým, který má na starosti řízení |QCP|.
a kontrolami kvality, které vytváří. Pokud je konkrétní člen týmu kvality zodpovědný za |QCP|
Vyberte je v poli „Odpovědná osoba“.

V poli „Dokumentace kroků“ je dvě možnosti, které určují umístění instrukcí.
dokument, který popisuje, jak provést kontrolu kvality vytvořenou |QCP|.

Vyberte: guilabel:„Přesná stránka pracovního listu operace“ pokud je dokument součástí
pracovní list k objednávce práce, pak zadejte číslo stránky v poli :guilabel:`Pracovní list
Pole „Stránka“ pod ním.

Vyberte „Vlastní“ v případě, že se dokument má zobrazit na záložce „Návod“.
dno QCP.

V dolní části formuláře v záložce „Pokyny“ zadejte pokyny pro způsob
dokončit kvalitativní kontroly vytvořené pomocí QCP.

Pokud byla v poli „Dokument kroku“ výše vybrána možnost „Vlastní“,
dokument lze v této záložce připojit. K tomu buď vyberte možnost „Nahrát soubor“
tlačítko pro otevření správce souborů zařízení, vyberte soubor nebo přidejte odkaz na Google Slides.
dokument v poli „Odkaz na Google Slides“.

V záložce „Pokud selže“ zadejte pokyny pro případ, že kvalitní kontrola
neuspěje. Například instruujte zaměstnance, který provádí kontrolu kvality, aby vytvořil dokumentaci
upozornění <kvalita_upozorneni>

Karta „Poznámky“ se používá k poskytnutí dalších informací o |QCP|, například důvodu
byla vytvořena. Informace zadané do této záložky se **nezobrazují** zaměstnancům, kteří zpracovávají
kontroly kvality vytvořené společností QCP.

.. obrázek: kvalita_kontrolních_bodů/qcp-form.png
:align:center
:alt: Konfigurace QCP, která vytváří kontroly Pass – Fail pro operaci pracovního příkazu.
