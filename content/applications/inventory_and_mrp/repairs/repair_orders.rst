=====================
Opravy objednávek
=====================

.. |SO| nahradit za: :abbr:`SO (Prodejní objednávka)`
.. |DO| nahradit za: :abbr:`DO (Dodací příkaz)`
.. |RO| nahradit za: :abbr:`RO (Oprava)“
.. |UoM| nahradit za: zkratka `UoM (jednotka měření)`

Někdy se může stát, že zboží dodané zákazníkům je poškozené nebo rozbité v průběhu přepravy a potřebuje
vráceny zpět pro vrácení peněz, dodání náhradního produktu nebo opravu.

V Odoo lze sledovat opravy produktů vrácených zákazníky v aplikaci *Opravy*.
opraveny a mohou být znovu dodány zákazníkovi.

Obvykle se proces vrácení a opravy poškozených výrobků řídí následujícím postupem:

#:ref:`Zpracování objednávky na opravu poškozeného produktu <repairs/repair_orders/return-order>`
#:ref:`Vytvořit opravný příkaz pro vrácený produkt <opravy/opravní příkazy/opravné příkazy>“
#:ref:`Vyplatit opravený produkt zákazníkovi <repairs/repair_orders/return-customer>`

... opravy, opravné příkazy a vrácení zboží:

Vrácení zboží
============

Vrácení zboží může být zpracováno v Odoo prostřednictvím obratu, který je vytvořen přímo ze zakázky prodeje (SO).
Jednou, když byla zboží dodána zákazníkovi.

Vytvořit vrácení zboží, přejděte do aplikace „Prodej“ a klikněte na SO, ze kterého chcete vrátit zboží.
produkt se vrátí zpět. Pak z formuláře SO klikněte na tlačítko „Dodání“ chytrého rozhraní.
Tím se otevře objednávka na dodání (DO).

Z této formy klikněte na „Vrácení“. To otevře okno „Obrat zpět“.

.. obrázek: opravy/opravy-vratky.png
:align:center
:alt:Okno pro přepnutí zpět na objednávku zásilky.

Tento okno zobrazuje produkt, který je součástí objednávky, a množství dodané.
zákazníkovi a jednotce měření produktu.

Klikněte na hodnotu v poli „Množství“ a změňte množství produktu, který chcete
v případě potřeby zpět.

Klikněte na ikonu „🗑️“ (směs odpadků) v pravém dolním rohu produktu, abyste jej odebrali z
pokud je třeba.

Jakmile je hotovo, klikněte na tlačítko „Vrácení“ pro potvrzení vrácení. To vytvoří nový doklad o
vrácené zboží.

Jakmile je zboží vráceno do skladu, lze registrovat přijetí vráceného zboží.
databázi kliknutím na tlačítko „Převést zpět“ z přenosového formuláře.

..tip:
Jakmile je ověřena zpětná platba pro vrácení zboží, hodnota ve sloupci „Doručeno“
na původní |SO| aktualizace, aby odrážely rozdíl mezi původním :guilabel:`Množství`.
a objednané množství, které zákazník zadává.

.... obrázek: opravy/opraveno-kolik-dodano.png
:synchronizace: střed
:alt:Dodací a množství sloupce na objednávkách po vrácení.

.. opravy /opravné práce/oprava:

Vytvořit opravný příkaz
===================

Jakmile jsou produkty vráceny, jejich opravy lze sledovat vytvořením požadavku na opravu (RO).

Pro vytvoření nového |RO| přejděte do aplikace „Opravy“ pomocí klávesové zkratky :menuselection:„Repairs app“, a klikněte na :guilabel:„New“.
otevře prázdný formulář RO.

... obrázek: opravy/oprava-vlevo-formulář.png
:align:center
:alt:Formulář pro opravu prázdné stránky z levé strany.

Na tomto formuláři začněte vybíráním zákazníka. Zákazník, který jste si vybrali, by měl být pro koho
objednávka bude fakturována a dodána.

V poli „Produkt k opravě“ vyberte možnost z rozevírací nabídky.
potřebuje opravit. Pokud je třeba, klikněte na „Vyhledat více…“ a otevřete „Vyhledat produkt“.
Otevřete okno pro opravu a procházejte všechny produkty v databázi.

Jakmile je vybráno zboží k opravě, objeví se nové pole „Množství“
pod ní. V poli pro množství zadejte počet kusů produktu, který vyžaduje
opravit.

Vpravo od této hodnoty klikněte na seznam sestupně a vyberte jednotku měření (Jm).
produkt.

V poli „Návrat“ klikněte na rozbalovací nabídku a vyberte návratový doklad z něhož
z jaké země pochází opravovaný výrobek.

Zatrhněte políčko „Pod zárukou“, pokud je opravovaný produkt kryt zárukou.
záruka. Pokud je zaškrtnuto, nebude zákazník účtován za všechny použité náhradní díly
pořádku.

V poli „Datum“ klikněte na datum, abyste zobrazili okno kalendáře.
V kalendáři vyberte datum opravy, klikněte na tlačítko „Použít“ (viz obrázek).

.. obrázek:opravy/vyplneny-formular-na-ukoncenou-opravu.png
:align:center
:alt:Formulář pro opravu prázdného řádku vlevo.

V poli „Odpovědný“ klikněte na seznam a vyberte uživatele, který by měl být
odpovědný za opravu.

V poli „Společnost“ zvolte společnost, pro kterou je tento |RO|
patřících do skupiny.

V poli „Štítky“ klikněte na rozbalovací nabídku a vyberte, které štítky se mají aplikovat
tohoto |RO|.

Tabulka dílů
---------

Přidejte, odeberte nebo znovu použijte části v záložce „Součástky“. Chcete-li tak učinit, klikněte na „Přidat řádek“
v dolní části formuláře.

V sloupci „Typ“ klikněte na políčko a zobrazí se tři možnosti, ze kterých si můžete vybrat:
„Přidat“, „Odebrat“ a „Znovu použít“.

.. obrázek: repair_orders/repair-orders-type-column.png
:align:center
:alt: Zadejte možnosti sloupce nebo novou část pod záložkou Parts.

Vybráním položky „Přidat“ přidáte tuto část do seznamu |RO|. Seznam komponentů pro použití v
opravit. Pokud jsou komponenty použité, může uživatel, který opravu dokončil, zaznamenat, že byly použity.
nebyly použity, uživatel může také uvést, že ano, a komponenty se dají uložit pro jiný
používání.

Volbou guilabel:Odstranit odstraníte tento díl z |RO|. Odstraňování částí seznamuje komponenty,
během opravy odstranit z výrobku, který se opravuje. Pokud jsou
odstraněny, uživatel provádějící opravu může uvést, že byly odstraněny.

Vybráním položky „Recyklace“ se tato část z |RO| označí pro pozdější použití nebo jako
použity v jiném skladu.

V sloupci „Produkt“ vyberte, který produkt (součást) má být přidán, odstraněn nebo
znovu použít. V sloupci „Požadavek“ změňte množství, pokud je třeba, abyste uvedli, kolik
Tento díl by měl být použit při opravě.

V sloupci „Dokončeno“ změňte hodnotu (ve formátu 0,00) po dokončení části
úspěšně přidán, odstraněn nebo znovu použit.

V sloupci „Jednotka měření“ vyberte |UoM| pro díl.

V poslední kolonce „Použito“ zaškrtněte políčko jednou, když se díl použije při opravě.
proces.

Pokud chcete přidat další sloupce do řádku, klikněte na ikonu :guilabel:`(volitelné sloupce)“.
pravicový pruh hlavičky. Vyberte požadované možnosti a přidejte je do řádku.

.. obrázek: opravy/opravy-další-možnosti.png
:align:center
:alt:Doplňkové volitelné možnosti, které lze přidat k nové části.

Karty Oprava a Různé
-----------------------------------

Klikněte na záložku „Poznámky k opravám“ a přidejte vnitřní poznámky o tomto konkrétním |RO|.
Může být potřeba, aby o tom věděl uživatel provádějící opravu.

Klikněte na prázdné pole pro psaní poznámek.

Klikněte na záložku „Různé“ a zobrazí se typ operace pro tuto opravu.
Výchozí hodnotou je „Oprava“ (viz guilabel:„Vaše společnost: Opravy“), což ukazuje, že se jedná o opravu.
operace.

Jakmile jsou na formuláři |RO| provedeny všechny požadované konfigurace, klikněte na tlačítko „Potvrdit opravu“.
Toto pohybuje |RO| do fáze „Potvrzeno“ a rezervuje potřebné komponenty.
Na opravu.

V seznamu produktů pod záložkou „Díly“ se objeví nová sloupec s názvem „Predikované“.
zobrazení dostupnosti všech komponent potřebných k opravě.

Jakmile je připravena oprava, klikněte na tlačítko „Zahájit opravu“. To přesune |RO| do stavu „Ve fázi opravy“
stupeň (v pravém horním rohu). Pokud má být zrušeno opravy, klikněte na:guilabel:`Zrušit opravu“.

Jakmile jsou všechny produkty úspěšně opraveny, je |RO| dokončeno.
databáze, klikněte na tlačítko „Ukončit opravu“.

.. poznámka::
Pokud nebyly všechny části přidružené k |RO| použity, kliknutím na tlačítko :guilabel:`End Repair`
:guilabel:`Nedokončený pohyb (y)“ okno se zobrazí.

.... obrázek: opravy/opravy-neukončené-přemisťování.png
:synchronizace: střed
:alt:Pop-up okno pro nevyužitá místa.

Pop-up okno upozorňuje uživatele na rozdíl mezi počátečním požadavkem a
skutečné množství použité pro objednávku.

Pokud chcete změnit množství „Used“, klikněte na „Smazat“ nebo zavřete okno.
Okno. Pokud má být objednávka potvrzena, klikněte na tlačítko „Potvrdit“.

Toto přesouvá |RO| do fáze „Opraveno“. Tlačítko „Pohyb produktu“ také
Připomíná, že je nutné vyplnit všechny položky formuláře.

Klikněte na tlačítko „Historie pohybu“ chytrého panelu, abyste zobrazili historii pohybu produktu během a
Po opravě.

.. obrázek: opravy/oprava-zboží-pohyb.png
:align:center
:alt:Přesune historii produktu zahrnutého v opravném příkazu.

... opravy, objednávky na opravu a zákazníci se vracejí:

Vrácení zboží zákazníkovi
--------------------------

Na výrobek se vztahuje záruka
~~~~~~~~~~~~~~~~~~~~~~~~~

Jakmile je produkt úspěšně opravený, může být vrácen zákazníkovi.

Zboží není v záruce
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pokud není produkt pod zárukou nebo by měl zákazník nést náklady na opravu, klikněte sem
:guilabel:Vytvořit nabídku. To otevře nové okno |SO|, které je předvyplněné částmi použitými v
V případě poškození vozidla je nutné vyčíslit celkovou cenu opravy.

.. obrázek: opravy/oprava-nová-nabídka.png
:align:center
:alt:Předvyplněná nová cenová nabídka na náhradní díly obsažené v opravném příkazu.

Pokud by mělo být tento doklad zasláno zákazníkovi, klikněte na „Potvrdit“ a pokračujte v fakturaci.
zákazník pro opravu.

..tip:
Pokud zákazníkovi má být účtována oprava, může se vytvořit produkt typu služba.
přičteno k částce za opravený výrobek.

Pro vrácení produktu zákazníkovi přejděte do aplikace „Prodej“ a vyberte
původní |SO|, ze kterého byla zpracována první vrácená zásilka. Pak klikněte na položku „Dodání“.
chytrý tlačítko.

Z výsledného seznamu operací pak klikněte na tlačítko „Obrat“, které je označené
„Zdrojový dokument“, který by měl číst „Vrácení zboží WH/OUT/XXXXX“.

Tím se otevře formulář pro vrácení zboží. Na horní části tohoto formuláře je nyní tlačítko s inteligentním textem „Opravné příkazy“.
se objevuje a odkazuje na návrat do dokončeného |RO|.

Klikněte na „Vrácení“ v horní části formuláře, což otevře okno „Obrat“.
okno.

.. obrázek: opravy/opravy-vratky.png
:align:center
:alt:Okno pro přepnutí zpět na objednávku zásilky.

Tento okno zobrazuje produkt, který je součástí objednávky, a množství dodané.
zákazníkovi a jednotce měření produktu.

Klikněte na hodnotu v poli „Množství“ a změňte množství produktu, který chcete
v případě potřeby zpět.

Klikněte na ikonu „🗑️“ (směs odpadků) v pravém dolním rohu produktu, abyste jej odebrali z
pokud je třeba.

Jakmile je připraveno, klikněte na tlačítko „Vrácení“ pro potvrzení vrácení. To vytvoří novou dodávku pro
vrácené zboží.

Když je objednávka zpracována a zboží vráceno zákazníkovi, klikněte
:guilabel:`Doručit“ k ověření doručení.

.. viz též:
:doc:`../prodej/prodej/produkty a ceny/vrácení zboží“
