======================
Modeláři a výrobci
======================

Aplikace Fleet společnosti Odoo zařazuje každé vozidlo do kategorie podle výrobce a modelu (například „BMW“, „X2“).
Předtím, než bude vozidlo přidáno do databáze Odoo, musí být zadán jeho výrobce.
A záznam modelu v databázi musí již existovat.

…flotil a výrobců:

Výrobci
=============

Aplikace Fleet společnosti Odoo je přednastavena pro 66 nejčastěji používaných značek automobilů a kol.
spolu s jejich logy. Pro zobrazení přednastavených výrobců přejděte na
:menuaplikace:„Flotilové aplikace“ --> „Nastavení“ --> „Výrobci“.

Výchozí filtr „S modelem“ zobrazuje pouze výrobce, kteří již mají vozidlo.
Výrobci. Odstraňte výchozí filtr, abyste viděli všechny výrobce.

Výrobci jsou seřazeni abecedně a každá karta ukazuje počet konkrétních modelů.
Pro každého výrobce jsou konfigurovány „flotily“ a „modely“.

.. obrázek: models/manufacturer.png
:alt:Karta výrobce s uvedeným počtem modelů.

...flotila/přidat výrobce:

Přidejte výrobce
------------------

Chcete-li přidat nového výrobce do databáze, klikněte na tlačítko „Nový“ v pravém horním rohu, abyste otevřeli
Vyplňte pole pro výrobce prázdných obalů. Do pole „Název“ zadejte název výrobce a
Vyberte obrázek, který chcete nahrát jako logo.

...flotilu/modely:

Modelky
======

Při přidávání vozidla do flotily zvolte typ vozu pro udržení aktuálních záznamů, které
sleduje konkrétní detaily, jako jsou plány údržby a kompatibilita dílů.

Oproti výrobcům (:ref:`<fleet/manufacturers>`) se modely **nepřipojují** k
Aplikace **Flotila**. Když se do flotily přidá nový typ vozidla, zobrazí se v aplikaci (a pokud je to nutné)
výrobce) *musí* být přidán do databáze <fleet/add-model>.

..flotila/přidat model:

Přidejte si vzor
-----------

Chcete-li přidat nový typ vozidla, přejděte na: „Aplikace pro flotilu --> Konfigurace --> Modely“.
Klikněte na „New“ v horním levém rohu a zadejte následující informace o nové položce
forma.

.. poznámka::
Záleží na nainstalovaném :doc:`lokalizaci <../../finance/fiscal_localizations>`, některé pole
nebo části nemusí být zobrazeny.

- :guilabel:`Název modelu“: Zadejte název modelu do pole.
- :guilabel:`Výrobce“: Vyberte výrobce z roletkového seznamu. Pokud není
konfigurováno, viz [fleet/add-manufacturers].
- :guilabel:`Typ vozidla“: Vyberte jeden z přednastavených typů vozidel pomocí vyhledávacího pole.
nebo :guilabel:`Auto“ nebo :guilabel:"Kolo".

.. důležité::
Přidat další typ vozidel nelze. Fleet je udržuje v pevnosti, aby zachoval svou
Součástí je integrace mzdy (payroll), kde vozidla lze považovat za zaměstnanecký benefit.

- :guilabel:`Kategorie“: Vyberte kategorii z :ref:`kategorií vozidel <fleet/categories>“.
buď vozidlo nebo vytvořit nové.

Informační panel
---------------

V záložce „Informace“ zadejte podrobnosti o typu vozu, například velikost auta.
počet cestujících, nastavení nákladů (pouze pro belgickou lokalizaci) a motor.
informace.

Model
~~~~~

- :guilabel:`Počet sedadel“: Zadejte, kolik cestujících může vozidlo přepravit.
- :guilabel:`Počet dveří“: Zadejte počet dveří, které má vozidlo.
- :guilabel:`Rok výroby“: Zadejte rok, ve kterém bylo vozidlo vyrobeno.
- :guilabel:`Závěs pro přívěsný vozík“: Zaškrtněte tuto políčko, pokud je na vozidle namontován závěs pro přívěsný vozík.

Mzda
~~~~~~

Sekce „Mzda“ se zobrazí pouze v případě, že společnost má nastavenou lokalizaci na
Belgie. Všechny hodnoty nákladů jsou uvedeny za měsíc, s výjimkou hodnoty katalogu (DPH)
Inc.)“.

- :guilabel:`Může být požadováno“: Zaškrtněte tuto políčko, pokud mohou zaměstnanci požádat o tento vzorový automobil.
Vozidlo je součástí pracovní smlouvy zaměstnance.
- :guilabel:`Hodnota v katalogu (včetně DPH)“: zadejte :abbr:`MSRP (Doporučená maloobchodní cena výrobce)
cena vozidla při jeho koupi nebo pronájmu.
- :guilabel:`Poplatek za emise CO2“: Znázorňuje poplatek za emise oxidu uhličitého, který je zaplacen belgické vládě.
Tato hodnota je automaticky vypočítána na základě belgických právních předpisů a **nemůže být**
upravena. Hodnota je založena na čísle, které bylo v poli „Emise CO2“ zadáno (viz
:guilabel:`Motor“ v části „Informace“ (viz obrázek).

.. důležité::
Upravením pole „Emise CO2“ upravíte hodnotu v poli „Poplatek za emise CO2“.

- :guilabel:`Náklady na vozidlo (odpisy)“: Zadejte měsíční náklady na vozidlo, které se objevují v platu.
konfigurátor pro budoucí zaměstnance. Tato hodnota ovlivňuje hrubou a čistou mzdu zaměstnance
je přidělen vozidlu a postupně se zmenšuje podle místních daňových zákonů.
:guilabel:`Náklady (Odhadované)“ neodepisuje automaticky na úrovni vozidla, ale
jen zohledňuje smlouvu spojenou s konkrétním vozidlem.
- :guilabel:`Celkové náklady (odpisy)“: Tato hodnota je kombinací :guilabel:`Nákladů
Ve výchozím nastavení je vypnutá a postupně se vyřazuje z provozu.

Motor
~~~~~~

- :guilabel:`Typ paliva“: Vyberte typ paliva, který používá vozidlo.
Výchozí možnosti jsou: „Diesel“, „Benzín“ a „Plug-in hybrid“.

:guilabel:`LPG“, :guilabel:`Vodík“ nebo :guilabel:`Elektrický“.
- :guilabel:`Dosah`: Zadejte vzdálenost, kterou může vozidlo ujet na jedno natankování paliva nebo jednu nabití baterie
dojezd v kilometrech.
- :guilabel:`CO2 emise“: Zadejte průměrné množství oxidu uhličitého, které vypouští vozidlo za
gramů na kilometr (g/km). Tyto informace poskytuje výrobce automobilu.
- :guilabel:`CO2 Standard“: Zadejte standardní množství oxidu uhličitého v gramů na kilometr
pro vozidlo podobné velikosti.
- :guilabel:`Přenosová rychlost“: Vyberte typ přenosu z roletkového seznamu.
:guilabel:`Manuální“ nebo :guilabel:`Automatický“.
- :guilabel:„Elektrický pohon“: Vyberte způsob měření výkonu vozidla z nabídky.
nebo v kilowatech nebo koňských silách.
- :guilabel:`Pohon‘: Pokud je vozidlo elektrické nebo hybridní, zadejte výkon, který používá
kilowatty (pouze pokud je vybrána jednotka kW).
:guilabel:`Převodní tabulka“ pole.
- :guilabel:Koní: Zadejte výkon vozidla do tohoto pole. Toto pole se zobrazí pouze v případě,
:guilabel:`Koně‘ je vybrán pro pole :guilabel:`Výkon‘.
- :guilabel:Daň z koňské síly“: Zadejte částku daně podle velikosti
motor vozidla. To se odvíjí od místních daní a předpisů a liší se podle
místo. Je vhodné se ujistit, že hodnota odpovídá účetnímu oddělení.
Je správné. Toto pole se zobrazí pouze v případě, že je vybráno pole „Koně“ pro pole „Výkon“.
pole.
- :guilabel:Daň z koníčků“: Zadejte daň podle motoru
specifikace. Počet závisí na místních daňových předpisech, proto je doporučeno
zajistit, aby do pole pro daňový výpočet byl zadán správný daňový výpočet.
pouze pokud pole :guilabel:`Power“ má hodnotu :guilabel:`Horsepower“.
- :guilabel:Daňová sazba: Procento, které lze odečíst z daní, je vypočítáno podle
je lokalizováno a nelze ho měnit. Toto pole se zobrazuje pouze pro určité lokalizace.

Tabulka dodavatelů
-----------

V této záložce specifikujte prodejce vozidel, ze kterých lze vůz zakoupit. S správným nastavením:
pro výběrová řízení <../../inventory_and_mrp/purchase/manage_deals/rfq> pro vozidla lze vytvořit
prostřednictvím aplikace Purchase v Odoo.

Chcete-li přidat dodavatele, klikněte na tlačítko „Přidat“ v horním levém rohu záložky „Dodavatelé“.
otevře okno s názvem „Přidat dodavatele“, které obsahuje seznam všech dodavatelů v současné době v
databáze. Přidejte dodavatele zaškrtnutím políčka vedle názvu dodavatele, pak klikněte
:selectlabel:„Vybrat“. Neexistují žádné omezení počtu dodavatelů, které lze přidat do seznamu.

Pokud se dodavatel v databázi ještě nevyskytuje, přidejte nového dodavatele kliknutím na tlačítko „Nový“
spodní části okna „Přidat dodavatele“. Ve formuláři „Vytvořit dodavatele“
která se objeví, zadejte potřebné informace a pak klikněte na tlačítko „Uložit a zavřít“, abyste
prodejce nebo klikněte na tlačítko „Uložit a nový“ pro přidání aktuálního prodejce a vytvoření dalšího nového prodejce.

.. obrázek: models/vendor.png
:alt:Formulář pro přidání nového dodavatele.

...flotila/kategorie:

Kategorie modelu
==============

Pro usnadnění organizačního procesu je doporučeno mít modely vozidel uložené pod konkrétním
kategorii. Modelové kategorie se nastavují na formuláři pro přidání vozidla:

Odoo nemá žádné přednastavené kategorie, všechny musíte přidat ručně.

Pro zobrazení všech kategorií v databázi přejděte na:
Konfigurace --> Kategorie“. Všechny kategorie jsou zobrazeny v seznamovém pohledu.

.._flotila/nová kategorie:

Přidejte novou kategorii modelu
------------------------

Pro přidání nové kategorie stiskněte tlačítko „Nový“ v pravém horním rohu.
:guilabel:`Kategorie“ panelu. Na konci seznamu se objeví nová řádka, do které zadejte
novou kategorii, pak buď klepněte na tlačítko „Uložit“, nebo na libovolné místo obrazovky, abyste uložili
vstup.

Pro přeorganizování kategorií v seznamu klepněte na ikonku .
:guilabel:`(přesouvatelný)` ikonu vedle libovolného názvu kategorie a přetáhnout čáru na
žádané pracovní místo.

Pořadí v seznamu nemá na databázi žádný vliv. Je však možné, že
zobrazit vozidla v určitém pořadí například podle velikosti nebo počtu cestujících
Nosnost vozidla.

.. poznámka::
Když se používá s aplikací Inventář, pak hodnota Max Weight a Max Volume
Políčka sledují kapacitu vozidla. To pomáhá řídit vnitropodnikové dodávky tím, že ukazuje, jak
máme ještě dost místa a hmotnosti pro naložení produktů
<../../Inventar a MRP/Inventar/Výdej a příjem/Nastavení konfigurace/Zaslání>.
