=========
Nehody
=========

Když řídíte flotilu vozidel, nehody jsou nevyhnutelné. Sledování nehod je důležité pro pochopení
údržba vozidel a identifikace bezpečných řidičů.

Aplikace Fleet společnosti Odoo nabízí několik způsobů sledování nehod. Podívejte se na následující kroky
Jedna z možných metod pro sledování nehod a nákladů na opravy.

Struktura
=========

Pro tento případ použití přejděte na: „Aplikace pro flotily -> Flotila -> Služby“. Na odkazu:
tvaru <flotila/služba-tvar>, vytvoří se dvě služby typů <flotila/nový-typ>: „Nehoda“
Vina řidiče“ a „Nehoda – žádná vina“.

Tento systém eviduje opravy spojené s nehodami a třídí je podle příčiny.

Při nehodě vzniká servisní záznam. Konkrétně potřebné opravy pro nehodu
jsou uvedeny v poli Popis služby a podrobnosti o nehodě jsou zaznamenány
v části poznámky.

S touto organizační strukturou je možné zobrazit všechny nehody uspořádané podle viníka, vozu a
Řidič nebo náklady.

.. poznámka::
Pro správu nehod je **povinné** vedení servisních záznamů.

Podrobné pokyny pro vytváření služebních záznamů naleznete na stránce :doc:`service`.
v aplikaci Fleet společnosti Odoo.

Záznamy o nehodách a opravách
=========================

Pro zaznamenání nehody a spuštění procesu opravy je první krok vytvoření :ref:`služby
záznam, který popisuje konkrétní opravy, které jsou potřeba.

.. poznámka::
Některé nehody vyžadují více oprav s různými dodavateli. Pro tyto scénáře je vhodné používat
Pro každého dodavatele provádějícího opravy je nutný samostatný záznam služby. Pro uspořádání záznamů
Je doporučeno udržet pole poznámky stejné a připojit stejně důležitý
dokumentace, například zpráva o dopravní nehodě.

Přejděte na:menu:fleetapp-->fleet-->services, abyste viděli hlavní služby.
přístrojová deska. Klikněte na tlačítko „Nový“ v levém horním rohu a načtou se prázdné služby.

Do formuláře zadejte následující informace:

- :guilabel:`Popis opravy“: zadejte popis oprav potřebných k úplnému opravení vozidla, například
„Oprava karoserie“, „Výměna čelního skla“ nebo „Výměna prahů, pneumatik a oken“.
- :guilabel:`Typ služby“: pro tento příklad vyberte buď „Nehoda – vinou řidiče“ nebo „Nehoda
  - Bez viny“, podle situace.

Při prvním vstupu do jedné ze dvou služeb typu :guilabel:`Service Type` zadejte nové
výběr typu služby a poté klikněte na tlačítko „Vytvořit nový typ služby“. Potom klikněte na tlačítko „Vytvořit nový typ služby“
objeví se okno s novým typem služby a v poli „Jméno“ se objeví název.
:guilabel:`Kategorie“ pole, vyberte :guilabel:`Služba“ z roletky a poté klikněte na
:guilabel:`Uložit a zavřít“ tlačítko.

Jakmile je do databáze přidán typ služby po nehodě, je k dispozici pro výběr v
rozbalovací nabídka v poli „Typ služby“.
- :guilabel:`Datum“: vyberte datum nehody pomocí okna kalendáře.
Najděte požadovaný měsíc pomocí tlačítka „Předchozí“ a „Další“.
:guilabel:`(šipka)` ikony a klikněte na datum pro jeho výběr.
- :guilabel:`Náklady na opravu“: nechte pole prázdné, protože není známá konečná cena opravy.
- :guilabel:`Dodavatel“: vyberte dodavatele, který provádí opravy pomocí rolovací nabídky. Pokud
Pokud dodavatel již v systému nebyl zadán, zadejte název dodavatele a klikněte na buď
:guilabel:`Vytvořit“ pro jejich přidání nebo „Vytvořit a upravit…“ pro :ref:`přidání a konfiguraci
Výrobce <flotila/nový výrobce>.
- :guilabel:`Vozidlo“: vyberte vozidlo, které bylo v nehodě, z roletky.
Když je vybrán vůz, pole „Řidič“ se zaplní a jednotka měření pro
:guilabel:`Hodnota tachometru“ pole se objeví.
- „Řidič“: pole obsahuje jméno řidiče pro vybrané vozidlo, které je zobrazeno v seznamu aktuálních řidičů.
Vyberte pole „Vozidlo“. Pokud jiný řidič vozidlo řídil v době, kdy došlo k nehodě, vyberte
Pokud k nehodě došlo, vyberte správného řidiče z roletky.
- :guilabel:`Hodnota tachometru“: zadejte hodnotu tachometru při nehodě. Jednotky
měřítko je buď v kilometrech (:guilabel:'km'), nebo mílích (:guilabel:'mi'), podle toho, jak
Vybrané vozidlo bylo nakonfigurováno.
- :guilabel:`POZNÁMKY“: zadejte konkrétní podrobnosti o nehodě na spodní části formuláře služby.
například „Srazil jelena“ nebo „Zadní náraz na křižovatce při zastavení“.

Odoo poskytuje možnost připojit jakýkoliv důležitý dokument, například odhad nákladů na opravu a policejní zprávy.
zprávy, ke služebnímu záznamu. Klikněte na ikonku „papír“
ikona umístěná v chatu formuláře a okno prohlížeče souborů se objeví. Vyberte
požadovaný rekord a klikněte na tlačítko „Otevřít“ pro nahrání souboru.

.. poznámka::
Jakmile je soubor přidán do záznamu služby, objeví se v chatu sekce „Soubory“.
Chcete-li připojit další záznamy, klikněte na ikonu „+“ vedle tlačítka „Připojit soubor“
dokumenty.

.. obrázek: nehody/formulář služby.png
:alt: Zadejte informace o opravě nehody.

Servisní fáze
==============

V aplikaci Fleet společnosti Odoo je čtyři základní fáze servisu:

.. záložky::

.. tab:: Nový

Výchozí stav při vytváření služebního záznamu. Služba byla požadována, ale
opravy nezačaly, pole „Náklady“ pro tuto fázi zůstává nulové.

...... záložka Běh

Oprava je v procesu, ale není ještě dokončena. Odhad na opravy je uveden v
:guilabel:`Cena“ pole.

....... tab:: Dokončeno

Všechny opravy uvedené na servisním formuláři byly dokončeny. V poli „Náklady“ je
aktualizovány tak, aby odrážely konečnou celkovou cenu za opravy.

...... tab::Zrušené

Požadavek na službu byl zrušen.

Při opravě změňte stav služby tak, aby odrážel aktuální stav vozidla.
z dvou možností: na individuální :ref:`záznam služby <fleet/service_record>`, nebo v :ref:`Kanban
Zobrazení služby (<fleet/Kanban>).

...flotila/záznam služby:

Sloužil v letech 1980-2004.
--------------

Otevřete hlavní panel služeb, přejděte na:menuselection:„Aplikace pro flotily –> Flotila“
Služby“. Následně klikněte na záznam služby pro otevření podrobného formuláře služby. Klikněte
požadované kroky v pravém horním rohu nad formulářem služby pro změnu stavu.

.. obrázek: nehody/běhání.png
:alt: Stáje v pohledu ze servisního tvaru.

…_flotila/kanban:

Kanbanový pohled
-----------

Otevřete hlavní panel služeb, přejděte na:menuselection:„Aplikace pro flotily –> Flotila“
Služby. Nejprve klikněte na ikonu „OI View Kanban“ v pravém horním rohu
displej, který organizuje všechny opravy vozidel.

Poté odstraňte výchozí filtr „Typ služby“ v hledání. Po provedení této akce se zobrazí všechny
služby se zobrazují v kanbanovém pohledu uspořádané podle jejich :guilabel:`Stavu`.

Přetáhněte služební záznam na požadovanou etapu.

.. obrázek: nehody/přetahování a pádu.png
:alt: Pohled na fáze kanbanu s přesouváním karty do fáze „Ve výrobě“.

Hlášení nehod
==================

Jedním z hlavních důvodů, proč se sledovat dopravní nehody pomocí metod popsaných v tomto dokumentu, je schopnost
zobrazit celkové náklady na nehodu, určit nejbezpečnější řidiče a vypočítat skutečné celkové náklady.
pro konkrétní vozidla.

Hlavní panel „Dashboard služeb“ zobrazuje všechny různé nehody
informace, zatímco:ref:`Panel s výstupy <fleet/reporting_dashboard>` zobrazuje celkový
pro konkrétní vozidla.

... _flotilovou/služební přehledovou tabulku:

Dashboard služeb
------------------

Přejděte na:menu:app:fleet --> fleet --> services, abyste zobrazili služby.
přístrojová deska. Všechny záznamy o službách jsou zobrazeny v :icon:`oi-view-list` :guilabel:`(Seznam)`
Seřazené abecedně podle služby.

V seznamu se objevují dvě služby pro sledování nehod: :guilabel:`Nehoda – Řidič
Vina a odpovědnost za nehodu – žádná vina.“

Každá skupina zobrazuje počet záznamů v každém typu a seznam jednotlivých záznamů.
pod nadpisem každé skupiny.

.. příklad::
V tomto případě se jedná o tři nehody, kde viníkem byl řidič a jednu nehodu, která byla zaviněna.
Ta nehoda není vinou řidiče. Tento panel také zobrazuje odhadované celkové náklady na opravu :guilabel:`Cost`.
všechny nehody v každé skupině.

Odhadované náklady na opravu vozidla po nehodě způsobené řidičem činí 3 284 dolarů.
Při nehodě se žádné náklady nevyskytly, protože oprava nebyla dokončena a nebylo vydáno odhadem.
zatím neexistuje.

.... obrázek: nehody/skupinové-nehody.png
:alt:Hasičské záchranné služby s celkovými náklady zvýrazněnými.

.. poznámka::
Celkový výpočet nákladů zahrnuje všechny náklady na opravu včetně odhadovaných.
náklady na opravu a náklady na konečnou opravu. Tato čísla nemusí být přesná, pokud dojde k nějakým opravám
Ve fázi „běžící“ a konečná faktura zatím nebyla vypočítána.

... _flotila/přehledová ploška:

Dashboard s přehledem o výkonu
-------------------

Přejděte na položku menu „Flotilní aplikace -> Zprávy -> Náklady“ a zobrazte si položku „Náklady“.
Analýza. Tato zpráva obsahuje graf :icon:`fa-bar-chart` :guilabel:`(Bar Chart)` všech
Smluvní a servisní náklady za aktuální rok, rozdělené podle měsíců
(:guilabel:'Datum: (rok)'), výchozí hodnotou. :guilabel:'Součet', reprezentovaný šedou čárkovanou linií, je
Celková částka obou smluv o dodávce a službě.

Pro zobrazení celkových nákladů na vozidlo klikněte na ikonu „fa-caret-down“ a poté na „(Zobrazit vyhledávací lištu)“.
ikonu vpravo od vyhledávací lišty, která zobrazí nabídku. Klikněte na položku :guilabel:`Vozidlo`.
Sloupce „Skupina“ (viz ikona :icon:`oi-group`) a data jsou uspořádána podle vozidla.

Tato cena zahrnuje skutečné náklady na každé vozidlo včetně smluvních nákladů (např. měsíční splátky).
náklady na pronájem vozidla) a všechny náklady spojené s poskytováním služeb včetně všech nehod. Na každou sloupcovou hodnotu se můžete podívat kliknutím myší.
okno s datovým přebalem, které zobrazuje název vozidla a celkovou cenu. To umožňuje
kompletní pohled na náklady spojené s provozem vozidla.

.. obrázek: nehody/celkové-náklady.png
:alt:Zpráva o nákladech na vozidlo zobrazující celkové náklady na vozidlo.

Pro zobrazení podrobností o nákladech na smlouvu a opravy klikněte na
:ikonka „Obrázek v převrácené orientaci“ (Pivot) v pravém horním rohu ikony „Náklady
Analytická lišta. Zobrazuje každé vozidlo na samostatné řádce a zobrazuje
Smluvní a servisní cena a celková cena.

.. obrázek: nehody/flotila-pivota.png
:alt: Zpráva o nákladech na smlouvu a služby, která zobrazuje náklady na smlouvu a službu zvlášť.
celkem.

.. poznámka::
Zobrazení „Pivot“ (výchozí) zobrazuje data podle vozidla.
Protože se v tomto případě nejedná o skupinu dat, není potřeba filtrovat podle pole „Vozidlo“.
aktivován, neovlivňuje prezentovaná data.

Řízení oprav po nehodě
=======================

Pro společnosti s více zaměstnanci, které spravují velké množství vozidel, je zobrazení pouze služby
Záznamy v etapách „Nový“ a „V provozu“ mohou být užitečné, pokud je
velké množství záznamů v přehledu služeb.

Přejděte na: „Flotila - aplikace -> Flotila – služby“, kde jsou uvedeny všechny požadavky na služby.
organizované službou typu. Pak klikněte na ikonku „fa-caret-down“ a zvolte
Ikona „Panel pro vyhledávání“ vpravo od vyhledávací lišty zobrazí nabídku. Klikněte na „Přidat
Vlastní filtr“ v sloupci „Filtry“ a „Přidat vlastní filtr“.
Zobrazí se okno „Filtr“.

Na vyskakovacím okně je potřeba nastavit tři rozbalovací pole.

V prvním poli přejděte dolů a vyberte: „Stage“.

Zatímco druhé pole nechte nastavené na hodnotě :guilabel:`=`.

V posledním poli vyberte možnost „Běží“.

Poté klikněte na ikonu „+“ vedle posledního pole a
identický pravidlo se nachází pod aktuálním pravidlem.

Poté změňte třetí pole druhé pravidlo na „Nový“ a nechte
další pole beze změn.

Klikněte na tlačítko „Přidat“ v dolní části, abyste přidali nový filtr.

.. obrázek: nehody/vlastní filtry.png
:alt:Filtr, který se má přidat pouze pro zobrazení nových a běžících služeb.

Tato mírná úprava zobrazuje pouze služby v položkách :guilabel:`Nový“ a :guilabel:`Běží“.
fáze, což je užitečný dokument pro společnost, která spravuje velké množství oprav v daném čase.

Mít tento výstup zobrazen jako výchozí výstup při otevření panelu „Služby“
klikněte na ikonu „fa-caret-down“ (Zobrazit vyhledávací panel) vpravo nahoře.
vyhledávací lištu. Následně klikněte na „Uložit aktuální vyhledávání“ pod ikonou „Hvězda“.
Sloupec „Oblíbené“, který odhaluje další sloupec s možnostmi pod ním. Zaškrtněte políčko
Kromě filtru „Výchozí“ klikněte na „Uložit“. Pak si můžete vytvořit
Pokud se zobrazí panel „Služby“, je vždy aktivní.
přístupný.
