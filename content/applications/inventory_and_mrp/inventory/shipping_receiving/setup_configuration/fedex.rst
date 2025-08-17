=================
Spojení s FedEx
=================

Propojení účtu FedEx s aplikací Inventář v Odoo umožňuje :doc:`vypočítat
dodací sazby <../setup_configuration>, a také vytváření dodacích štítků <labels> v rámci systému Odoo.
Toho je dosaženo zapnutím modulu pro přepravu FedEx, pak alespoň jednou konfigurací
*metoda dopravy*.

.. poznámka::
Tato dokumentace obsahuje konfigurační detaily specifické pro integraci FedEx. Podrobnosti naleznete v
dokumentace k tématu :doc:`třetích dopravců <third_party_shipper> pro obecného dopravce
pokyny k integraci.

Povolit připojení k dopravci
=========================

Pro zapnutí připojení pro FedEx přejděte do:
Konfigurace --> Nastavení. Vyhledejte sekci „Připojení k dopravcům“ a zaškrtněte
zaškrtávací políčko vedle :guilabel:`FedEx Connector`.

Konečně klikněte na tlačítko „Uložit“ pro uložení změn. Poté se zobrazí ikona „pravý úhel“.
Tlačítko „Metody přepravy FedEx“ se zobrazí pod tlačítkem „FedEx Connector“.

.. obrázek: fedex/fsm-button.png
:alt:Tlačítko níže pro způsoby přepravy společnosti FedEx.

Zvolte způsob dodání
=========================

Jakmile je zapnutý přepravce FedEx, musí být alespoň jedna dodací adresa nakonfigurována.
metoda. Po provedení takových úprav lze způsob doručení zahrnout do prodejních objednávek (SO) a použít k
vypočítat náklady na dopravu a vytisknout štítek s adresou.

Pro povolení způsobu dodání přejděte do: „Skladová aplikace - Konfigurace“.
Nastavení“ a klikněte na tlačítko „Dopravní metody FedEx“ pod tlačítkem „Dopravní metody FedEx“.
Zatrhněte políčko „Connector“ a otevře se stránka, která zobrazuje všechny dostupné způsoby doručení společnosti FedEx.

.. poznámka::
Pro zobrazení všech způsobů doručení pro každého dopravce s aktivním konektorem přejděte na
:menu:„Aplikace skladu --> Konfigurace --> Způsoby dodání“.

Vyberte způsob dodání, abyste otevřeli jeho formulář. Můžete také kliknout na tlačítko „Nový“ pro otevření prázdného
a vytvořit nový způsob dodání.

.. obrázek: fedex/fedex-form.png
:alt:Formulář pro způsob doručení společnosti FedEx.

.. důležité::
Povolení připojení k dopravci FedEx automaticky vytvoří dvě výchozí metody doručování:
:guilabel:`FedEx USA“ a :guilabel:"FedEx mezinárodní“. Každý z těchto způsobů je
jsou přednastaveny testovacími přihlašovacími údaji, které lze použít k testování.

Než se může používat metoda k vytvoření skutečných dodávek, musí být zadané testovací přihlašovací údaje.
nahrazena kreditními údaji z platného účtu FedEx.

Základní informace
-------------------

Na samém vrcholu formuláře pro způsob doručení jsou pole, která se používají k nastavení způsobu fungování metody
v Odoo. V poli „Dodavatel“ vyberte z roletky „FedEx“, pokud je
nebyl vybrán.

Ostatní položky v této sekci jsou obecné pro všechny poskytovatele dodávek. Pro podrobnosti o tom, jak
vyplňte je a podívejte se na dokumentaci k tématu „dodavatelé třetích stran“ (viz :doc:`third-party shippers <third_party_shipper>`).

Karta Konfigurace
-----------------------

Možnosti v záložce „Konfigurace FedEx“ v dialogovém okně pro nastavení způsobu doručení FedEx se používají k
připojit metodu k účtu FedEx, a nakonfigurovat detaily doručení spojené s metodou
(případně balíčkový typ).

Pro získání potřebných informací k vyplnění polí je nutné mít účet vývojáře společnosti FedEx.
toto tlačítko. Chcete-li vytvořit nový účet, přejděte na stránku FedExu Open Account
Stránku „Otevření účtu“ najdete na adrese https://www.fedex.com/en-us/open-account.html. Na této stránce klikněte na tlačítko „Vytvořit účet“.
Postupujte podle pokynů.

Vytvořit projekt API
~~~~~~~~~~~~~~~~~~

Po vytvoření účtu „Developer“ (<https://developer.fedex.com/api/en-us/home.html>) přejděte na
kartě „Moje projekty“ a klikněte na „Vytvořit projekt API“.

V okně „Povídejte si o svých potřebách v oblasti API“ vyberte možnost „Dodávky s FedEx a potřebuje
integrovat API společnosti FedEx do svého systému v poli „Pracuji pro společnost“ vyskakovacího okna.

.. obrázek: fedex/fed-ex-api-needs.png
:alt:Pop-up na webu společnosti FedEx pro výběr API.

Poté, co se vám zobrazí výzva k „Vybrat služby API pro váš projekt“, ujistěte se, že zapnete následující služby API:

 - :guilabel:`Lodě, sazby a další API“
 - :guilabel:`API pro ověřování adresy“
 - :guilabel:`Sazby a časy přepravy API“
 - :guilabel:`Lodní API“
 - :guilabel:`Nahrávání obchodních dokumentů“

.. obrázek:: fedex/select-apis.png
:alt:Stránka na webu společnosti FedEx, kde uživatelé vybírají API potřebné pro projekt.

Zadejte název projektu, pak vyberte země, kam budou balíčky zaslány.
osvobozen od.

.. obrázek: fedex/country-selector.png
:alt:Stránka na webu společnosti FedEx, kde uživatelé vybírají země, do kterých a ze kterých budou balíčky zasílat.

Chcete-li projekt přesunout do produkce, klikněte na záložku „Klíč pro výrobu“. Odtud můžete
:guilabel:`Účet pro zasílání“. Zkopírujte „Klíč API“, „Tajný klíč“ a číslo účtu, pak je vložte
Do příslušných políček na formuláři „Způsoby doručení“.

Certifikační proces
~~~~~~~~~~~~~~~~~~~~~

Pro vytvoření štítku pro odeslání přepravní společnosti FedEx musí být API ověřeno. V nabídce na levé straně
FedEx „Developer Portal“ <https://developer.fedex.com/api/en-us/home.html> klikněte
„Certifikace API“ a postupujte podle pokynů.

.. poznámka::
Tyto certifikáty často vyžadují kontaktování týmu podpory FedEx e-mailem.

Číslo účtu
~~~~~~~~~~~~~~~~~~~~~

Číslo účtu je jedinečné číslo, které bylo každému účtu FedEx přiděleno.

Abychom našli číslo účtu FedEx, musíme se přihlásit do svého účtu na webu www.fedex.com. Klikněte na
Jméno účtu v pravém horním rohu obrazovky a vyberte možnost „Můj profil“.
z rozbalovací nabídky.

Na stránce profilu klikněte na položku „Správa účtu“ v levém rohu obrazovky.
Na obrazovce se zobrazuje číslo účtu.

Jakmile jsou zjištěny heslo a číslo účtu, vepište je do pole „Heslo“ a
:guilabel:Číslo účtu“ na kartě „Konfigurace FedEx“ v sekci „Způsob doručení“.
forma.

Dodací podmínky
~~~~~~~~~~~~~~~~

Hlavní část záložky „Konfigurace FedEx“ zahrnuje několik dalších polí.
slouží k poskytnutí informací o způsobu doručení:

- :guilabel:`Typ služby FedEx“: Služba FedEx použitá k odeslání balíčku.
- :guilabel:`Metoda předání balíku do rukou společnosti FedEx“: Metoda, jak se dostane balík do rukou společnosti FedEx.
- :guilabel:`Typ balíku FedEx“: Druh použitého balíčku pro způsob doručení.
- :guilabel:`Hmotnost balíku v jednotkách hmotnosti“: Jednotka, kterou se váží balíky.
- :label:Délka balíku: Jednotka měření, která se používá k určení rozměrů balíků.
- :label_type:Typ dodací etikety: Typ dodací etikety používané pro balíčky.
- :label_format:Formát souboru používaný společností Odoo pro vytváření dodacích štítků.
- :guilabel:`Typ faktury“: Rozměry a typ papíru použitého k tisku faktur.

.. důležité::
Vyberte možnosti, které byste měli zvolit na kartě „Konfigurace FedEx“ v okně pro odeslání.
metoda závisí na vyjednaných dodacích službách spojeného účtu FedEx.
služby k dispozici pro účet FedEx, navštivte stránku *Správa účtu* po přihlášení.
FedEx webové stránky nebo mluvte s pracovníkem zákaznického servisu.

Možnosti
~~~~~~~~~~~~~~~

Karta „Nastavení“ v sekci „Konfigurace FedEx“ obsahuje několik dalších
možnosti dalšího nastavení způsobu doručení:

- :guilabel:Doručení v sobotu“: Zatrhněte políčko, pokud chcete umožnit doručování balíků s dodáním v sobotu
metoda, která by měla být dodána v sobotu.
- :guilabel:`Vytvořit štítek pro vrácení zboží“: Zaškrtněte políčko, pokud chcete automaticky generovat štítek pro vrácení zboží při
potvrzení dodacího listu.
- :guilabel:`Daň zaplacená“: Vyberte z roletky, zda se mají daňové poplatky platit
odesílatel nebo příjemce.

Aktivujte způsob doručení
========================

Výchozí nastavení v Odoo je takové, že se metody doručení vytváří ve vývojovém prostředí. To znamená, že
sloužit pouze k testovacím účelům a nemohou vytvářet skutečné objednávky na dodání.

Abychom aktivovali způsob dodání v produkčním prostředí, klikněte na ikonu „fa-stop“
tlačítko „Testovací prostředí“ v horní části formuláře pro způsob doručení.
Chytré tlačítko se změní na čtverec s ikonou „fa-play“ a textem „Produkční prostředí“.

Při zapnutém výrobním prostředí lze ověřit dodací příkaz pomocí metody dodání
Vytvoří skutečnou dodací etiketu s FedEx.

Klikněte na tlačítko „Spustit“ a vrátí se vám dodávka.
Metoda pro testovací prostředí.

.. varování::
**Nepovolujte** produkční prostředí pro metodu doručení, dokud není připravené k použití
pro skutečné dodací objednávky. Takové jednání může vést k vytvoření nechtěných poplatků s FedEx.
