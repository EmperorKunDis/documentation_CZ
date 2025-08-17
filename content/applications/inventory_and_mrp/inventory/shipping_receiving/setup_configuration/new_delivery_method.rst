=========================
Přidejte nový způsob doručení
=========================

Možnost výpočtu nákladů na dopravu v objednávkách na prodej je přidána do nastavení *Způsoby doručení*.
a elektronické nákupní košíky. Náklady na dopravu lze pak přidat do objednávky jako dodací
a do objednávky přidat podrobnosti o dodání.

.. viz také:
:doc:`../nastavení_konfigurace`

Konfigurace
-------------

Pro konfiguraci způsobu doručení přejděte na: „Inventář aplikace --> Konfigurace --> Doručování
Metody.

.. poznámka::
Pokud možnost „Způsoby doručení“ není dostupná z „Konfigurace“,
nabídka rozbalovacího menu, ověřte, zda je funkce zapnutá podle těchto kroků:

   #Přejděte na:menu: „Skladová aplikace“ -> „Konfigurace“ -> „Nastavení“.
   #Přejděte do sekce „Doprava“ a zapněte funkci „Způsoby doručení“.
zaškrtnutím příslušného políčka.

.... obrázek: nový způsob doručení/zapnout doručování.png
:alt:Funkce Způsoby doručení zapnutá v nastavení.

… skladování, přijímání a dodávky zboží:

Na stránce „Způsoby doručení“ klikněte na tlačítko „Nový“. To zpřístupní
formulář pro poskytnutí podrobností o přepravci, včetně:

- :guilabel:`Metoda doručení“ (*Povinný údaj*)): název metody doručení (např. „paušální platba“)
„doručení na dobírku“, „dodání v den objednávky“ atp.
- :guilabel:`Webová stránka“: Konfigurujte způsoby dopravy pro e-shopovou stránku. Vyberte příslušný
Webovou stránku vyberte ze seznamu nebo nechte pole prázdné a metoda bude aplikována na všechny webové stránky.
- :guilabel:`Poskytovatel služeb“ (*Povinný údaj*)): vyberte doručovací službu, jako je například FedEx, pokud používáte
:ref>:„dodavatelské dopravce <skladování/doručení/třetí strana>“. Zajistěte integraci s
přepravce je správně nainstalován a vyberte poskytovatele z nabídky.
podrobnosti o konfiguraci vlastních způsobů dopravy, například:ref:`fixní cena
nebo podle možností „<inventarizace/dodání/fixní“ nebo „podle pravidel <inventarizace/dodání/pravidla>“.
jejich příslušné části níže.
- :guilabel:`Společnost“: Pokud se má zvolený způsob dopravy vztahovat na konkrétní společnost, vyberte ji z
vyberte ze seznamu. Nechte pole prázdné, pokud chcete metodu aplikovat na všechny společnosti.
- :guilabel:`Trasy“: vyberte vhodné trasy a definujte různé způsoby doručení, například
Standardní nebo expresní doručení podle různých časových úseků. Pro více informací přeskočte na
:ref:`Nastavte trasy na způsobu dopravy v sekci <Inventář/Přijetí a výdej/Doprava>.“
- :guilabel:`Dodací produkt“ (*Povinný údaj*) – produkt uvedený na řádku objednávky.
<Inventář/Dodání/Prodejní objednávka> jako poplatek za dodání.
- Zdarma při objednávce nad: zaškrtnutím políčka se zobrazí možnost bezplatné dopravy, pokud je hodnota objednávky vyšší než
spořil více, než bylo uvedeno.
- :guilabel:`Sledovací odkaz“: Tato možnost přidá do portálu odkaz, pomocí kterého může zákazník sledovat svou objednávku.
dodání. Když je k objednávce přidán vlastní dopravce, tlačítko sledování se aktivuje a
Odkaz vede na sledovací portál s tímto URL.

... skladování, přijímání a dostupnost:

V záložce „Dostupnost“ definujte podmínky pro způsob dodání na základě
obsahu nebo cílové adrese objednávky:

- :guilabel:`Státy“: Uveďte jednu nebo více zemí, kde je metoda k dispozici.
- :guilabel:`Maximální hmotnost“: Zadejte maximální hmotnost; metoda je dostupná pouze pro objednávky pod touto hodnotou
limit.
- :guilabel:`Maximální objem“: Zadejte maximální objem; metoda je k dispozici pouze pro objednávky pod touto hodnotou
limit.
- :guilabel:Povinné štítky: Metoda je k dispozici pouze v případě, že alespoň jeden produkt v objednávce má
jedním z těchto tagů.
- :guilabel:`Vyloučené štítky“: Metoda není dostupná, pokud alespoň jeden produkt v objednávce má jeden
z těchto štítků.

Pokud chcete konfigurovat specifické způsoby dopravy, podívejte se na následující příklady.

... skladové zásoby, expedice a pevné:

Fixní cena
-----------

Pro konfiguraci ceny dopravy stejné pro všechny objednávky přejděte na:
Klikněte na „Nastavení“ a poté na „Metody doručení“. Pak klikněte na „Nový“ a zvolte metodu doručení.
formulář, nastavte pole „Poskytovatel“ na možnost „Fixní cena“. Vyberte tuto možnost
Zobrazí pole „Fixní cena“, kam se zadává fixní poštovné.
je stanovena.

Pokud chcete umožnit bezplatné poštovné při objednávce nad určitou částku, zaškrtněte políčko
:guilabel:`Zdarma při objednávce nad` a vyplňte částku.

Příklad:
Chcete-li nastavit $20 poštovné, které se stane zdarma při nákupu nad $100, vyplňte
následujících polích:

   - :guilabel:`Způsob doručení“: „Plná cena dopravy“
   - :guilabel:`Poskytovatel“: :guilabel:`Fixní cena“
   - :guilabel:`Fixní cena“:$20.00
   - :guilabel:`Zdarma při objednávce nad`: `$100.00`
   - :guilabel:`Dodací produkt“: „[PLOCHA] Plochá“

.... obrázek: nový způsob doručení/nový způsob dopravy.png
:alt: Příklad vyplnění způsobu dopravy.

... inventář/dodání/pravidla:

Podle pravidel
--------------

K výpočtu ceny přepravy podle pravidel cenotvorby nastavte pole „Dodavatel“ na
Možnost „Podle pravidel“ (volitelně upravte „Poměr na sazbu“).
:guilabel:`Přirážka k ceně dopravy“ pro zahrnutí dalších nákladů na dopravu.

Vytvořte cenové pravidlo
~~~~~~~~~~~~~~~~~~~~

Přejděte na záložku „Ceník“ a klikněte na „Přidat řádek“. To vám otevře
Okno „Vytvořit pravidla pro cenotvorbu“, kde je položka „Podmínky“ týkající se produktu
hmotnost, objem, cena nebo množství se porovná s definovaným množstvím k výpočtu
„Náklady na doručení“.

Jakmile je hotovo, klikněte na buď :guilabel:`Uložit a nový`, nebo :guilabel:`Uložit a zavřít“.

Příklad:
Za dodání objednávky s pěti a méně produkty účtovat zákazníkům 20 dolarů.
:guilabel:`Podmínka“ na „Množství < 5,00“, a :guilabel:`Náklady na dodání“ na „$20“.

.... obrázek: nová_doručovací_metoda/cena_pravidlo.png
:alt:Zobrazit okno pro přidání cenového pravidla. Zadejte podmínku a náklady na dodání.

Omezit dopravu na konkrétní cíle na e-commerce webové stránce v metodě doručení
formulář, přejděte na záložku „Dostupnost cíle“ a definujte země.
„Státy“ a „Předčíselné kódy“. Nechte tyto pole prázdné, pokud se vztahuje na všechna místa.

Vypočítat náklady na doručení
~~~~~~~~~~~~~~~~~~~~~~~

Přepravné je dáno hodnotou Doprava specifikovanou v pravidle, které splňuje
„Podmínky“, včetně případných dalších poplatků z „Přirážka k sazbě“.
:guilabel:`Přidružený marže“.

.. matematika::
Celkem = Cena dodání podle pravidel + (Přirážka k ceně za dodání podle pravidel) + Přirážka navíc

Příklad:
S dvěma následujícími pravidly:

   #Pokud objednávka obsahuje pět nebo méně produktů, poštovné je 20 $.
   #Pokud objednávka obsahuje více než pět výrobků, je poštovné 50 $.

Margin na sazbu je 10 % a dodatečný marže je 9 $.

.... obrázek: nový způsob doručení/příklad nákladů na dopravu.png
:alt:Zobrazte příklad způsobu dopravy „Na základě pravidel“ s nastavenými maržemi.

Když se používá první pravidlo, je cena doručení 31 dolarů (20 + (0,1 * 20) + 9). Když se používá druhé
Při aplikaci této pravidla je cena poštovného 64 dolarů (50 + (0,1 * 50) + 9).

.. skladování, příjem a expedice:

Trasa na dopravní metodu
------------------------

Pokud chcete nastavit jiný proces doručení do skladu pro dopravní metodu, můžete tak učinit konfigurací
různé trasy pro něj.

Příklad:
Konfigurace více tras na jednu dopravní metodu je užitečná pro přizpůsobení skladu
procesy založené na:

   - rychlost (např. použijte :doc:`jednokrokovou dodávku <../daily_operations/receipts_delivery_one_step>`)
expresní přeprava nebo dvoufázový proces (viz dokumentace: „Dodání a vyzvednutí v dvou krocích“).
standardní doprava).
   - mezinárodní doprava (např. použití:doc:`třístupňového dodání
<../denní operace/doručení tří kroků> na přípravu dokumentů pro celní úřad.
   - vyzvednutí v obchodě nebo domácí dodání: odeslat z centrálního skladu, nebo vyzvednout ze skladu prodejny.
zásobách podle výběru zákazníka.

Pro nastavení tras jděte do: „Inventář aplikace“ --> „Konfigurace“ --> „Trasy“. Klikněte
:guilabel:`Nový“, nebo vyberte požadovanou trasu.

V sekci „Použitelné na“ v poli trasy zaškrtněte možnost „Dopravní metody“.
zaškrtávací políčko.

.. obrázek: nový způsob dodání/dopravní trasa.png
:alt:Trasy vytváří se zaškrtnutou položkou dopravních metod.

Dopravní trasy vytváří při zaškrtnuté položce „Způsob dopravy“.

Pak přejděte na: „Aplikace Inventura –> Konfigurace –> Způsoby dodání“ a vyberte
požadovaný způsob dopravy.

V poli „Doprava“ na formuláři zvolte dostupnou metodu doručení.
z nabídky volby trasy.

.. poznámka::
Pokud požadovaná trasa není vybíratelná, zkontrolujte, zda je zapnutá volba „Dopravní metody“.
části „Použitelné od“ v sekci trasy.

.. obrázek: nový způsob doručení/zadání trasy.png
:alt:Zobrazit trasy na formuláři dopravního způsobu.
