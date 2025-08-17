=======================
Fakturace přepravních nákladů
=======================

Fakturace zákazníků za dopravu po dodání zajišťuje přesné účtování podle skutečných nákladů na dopravu v reálném čase.
faktory jako vzdálenost, hmotnost a metoda.

V Odoo lze přepravní náklady fakturovat dvěma způsoby:

#S klientem se dohodnout na pevné ceně a zahrnout ji do objednávky prodeje.
<Inventar/Versand/Rechnung-So>

#Přepravu faktury k zákazníkovi po dodání
<Inventář/dodání/faktura – dodání>, což odráží skutečné náklady, které podnik vynaložil.

Konfigurace
=============

Pro nastavení cen dopravních metod přejděte na:
Nastavení“. V sekci „Doručení“ zapněte funkci „Metody doručení“.
Poté klikněte na tlačítko „Uložit“.

.. obrázek: fakturace/povolení dodání.png
:align:center
:alt:Zapněte funkci „Metody doručení“ v Nastavení.

Přidejte způsob dopravy
===================

Dále nastavte cenu každé přepravní metody kliknutím na:
Konfigurace --> Možnosti dopravy“ a klikněte na tlačítko „Vytvořit“. To způsobí, že se otevře formulář
poskytnout podrobnosti o přepravci, včetně:

- :guilabel:`Dopravní metoda“ (*povinné pole*), název způsobu dopravy (např. „sazba za zásilku“)
„doručení na dobírku“, „dodání v den objednávky“ atp.
- :guilabel:`Dodavatel“ (*povinné*) - vyberte přepravní službu, jako je FedEx, pokud používáte
třetí strana přepravce Zajistěte, aby integrace s dopravcem byla správně nainstalována.
Vyberte poskytovatele ze seznamu.

......viz také:
:doc:`../nastavení/třetí strana dopravce

- :guilabel:`Společnost“: pokud by měla být doprava určena konkrétní společnosti, vyberte ji z
vyberte ze seznamu. Nechte pole prázdné, pokud chcete metodu aplikovat na všechny společnosti.

- :guilabel:`Webová stránka“: Konfigurace způsobu dopravy pro elektronickou obchodní stránku. Vyberte příslušný
Webovou stránku vyberte ze seznamu nebo nechte pole prázdné a metoda bude aplikována na všechny webové stránky.

- :guilabel:`Dodací produkt“ (*povinné*) - produkt uvedený na řádku objednávky
„<Inventar/Versand/Rechnung auf so>“ jako přepravní poplatek.
- Zdarma při objednávce nad: zaškrtnutím políčka se zobrazí možnost bezplatné dopravy, pokud je hodnota objednávky vyšší než
spořil více, než bylo uvedeno.

... inventarizační, expediční a fakturační:

Daňový doklad na prodejní objednávce
===========================

Pokud chcete na prodejní objednávce vyúčtovat náklady na dopravu před dodáním zboží, přejděte do
Vyberte v nabídce „Prodejní aplikace“ požadovanou objednávku.

V objednávce prodeje klikněte na tlačítko „Přidat dopravu“ v pravém dolním rohu.

.. obrázek: fakturace/doprava.png
:align:center
:alt:Klikněte na tlačítko „Přidat dopravu“ v dolní pravé části stránky, poblíž celkové ceny.

V okně „Přidat způsob dopravy“ zvolte v roletce
Pole „Dopravní metoda“.

Poté klikněte na tlačítko „Získat sazbu“ a zobrazí se vám cena dopravy podle aktuálního kurzu.
Odoo přepravní údaje pro integraci dopravce.

Kalkulace nákladů na dopravu se provádí automaticky podle hmotnosti objednaného zboží.
Konečně klikněte na tlačítko :guilabel:`Přidat`, abyste okno zavřeli.

.. obrázek: fakturace/dodací metoda.png
:align:center
:alt: Vypočítat poštovné vybráním způsobu dopravy.

... inventarizační záznam, faktura na dodání zboží:

Na prodejním příkazu se zboží objeví v záložce „Dodací řádek“ s
:guilabel:`Cena za jednotku“ nastavit jako náklady na dopravu, které byly vypočítány v „Přidat způsob dopravy“.
pop-up okno.

.. obrázek: fakturace_dodani_produktu.png
:align:center
:alt:Zobrazit dodací produkt na řádku prodejní objednávky.

Konečně po dodání produktu klikněte na tlačítko „Vytvořit fakturu“ a vytvořte fakturu.
je vytvořen, který zahrnuje náklady na dopravu, které byly dříve přidány.

.. obrázek: fakturace/vytvorit-fakturu.png
:align:center
:alt:Zobrazit tlačítko „Vytvořit fakturu“.

Poté klikněte na tlačítko „Vytvořit a zobrazit fakturu“ a vytvoří se návrh faktury s
poštovné zahrnuté v záložce „Fakturační řádky“.

.. obrázek: fakturace/faktura-zadani.png
:align:center
:alt:Zobrazit dodací produkt v řádku faktury.

... inventář/dodací list/faktura dodání:

Faktura skutečných nákladů na dopravu
===========================

Změnit fakturu tak, aby odrážela skutečnou cenu dopravy, postupujte podle kroků uvedených výše.
Vytvořit fakturu s dodací položkou, která má jednotku:
Nula jako cena.

Poté upravte v návrhu faktury položku „Jednotková cena“ tak, aby odrážela skutečnou cenu dopravy.
Poté konečně fakturujte zákazníkovi upravenou cenu dopravy klepnutím na tlačítko „Potvrdit“.

.. obrázek: fakturace/faktura-náklady.png
:align:center
:alt:Zobrazit dodací produkt na řádku faktury.

.. viz také:
   - :doc:`../setup_configuration/third_party_shipper`
   - :doc:`../setup_configuration/labels`
