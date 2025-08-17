=========================================
Zkuste doplnit kontakty pomocí partnera
=========================================

*Doplňte partnera* doplní databázi kontaktů firemními údaji. V kterémkoliv modulu zadejte
nový název společnosti do pole „Zákazník“ („technické pole partner_id“) a vyberte jeden
z firem, které jsou v nabídce rozbalovacího seznamu. Hned získáte cenné informace o firmách plné
těžko dostupné informace o poptávané společnosti.

.. důležité:
Společnost **nemůže být** ručně zadána do aplikace *Kontakty* před obohacením
je s daty.

Informace poskytnuté partnerem doplňování adres mohou zahrnovat obecné informace o podniku.
(včetně celého názvu a loga), sociálních médií, :guilabel:`Typ společnosti`,
Informace o založení, informace o sektorech a počet
:guilabel:`Zaměstnanci“, :guilabel:`Odhadovaný obrat“, :guilabel:`Telefonní číslo“
:guilabel:`Časová zóna“ a „Použité technologie“.

.. důležité:
Při shánění kontaktů na firmu se ujistěte, že jste si osvojili nejnovější evropské předpisy.
Více informací o nařízení GDPR naleznete v: „Odoo GDPR
<http://odoo.com/gdpr>. V Odoo nelze vyhledávat kontaktní informace jednotlivých osob.
funkce doplňování výrazů, která vyhledává podobná slova.

Konfigurace
=============

Přejděte do aplikace „Nastavení“ –> „Kontakty“. Pak aktivujte „Partnera“.
Funkci „Doplňování“ zaškrtnutím políčka vedle ní a kliknutím na tlačítko „Uložit“.

.. obrázek: partner_autocomplete/settings-partner-autocomplete.png
:align:center
:alt: Pohled na nastavení stránky a aktivace funkce v Odoo.

Zaplňte kontakty firemními daty
===================================

Od jakéhokoliv modulu, když uživatel zadává jméno nového kontaktu společnosti, Odoo odhalí velké
nabídka možných shod. Pokud některé z nich vyberete, kontakt se pak doplní
s firemními daty souvisejícími s tímto konkrétním výběrem.

Příkladem může být následující informace po zadání „Odoo“:

.. obrázek: partner_autocomplete/odoo-autocomplete.png
:align:center
:alt: Vytvoření nového kontaktu v Odoo

V chatovací části se pak objevují informace o společnosti po kliknutí na vybranou
předvyplněný kontakt:

.. obrázek: partner_autocomplete/odoo-info-autocomplete.png
:align:center
:alt: Pohled na informace, které se zobrazují při psaní slova odoo s možností automatického doplňování

..tip:
Partner Autocomplete funguje i v případě, kdy je do pole zadána místo IČO číslo DPH.
název společnosti.

Ceny
=======

Služba Partner Autocomplete je službou In-App Purchase (IAP), která vyžaduje předplacené kredity.
užité. Každá žádost spotřebuje jeden kredit.

Chcete-li koupit kredity, přejděte do aplikace „Nastavení“ - „Kontakty“. Pak najděte buď
Vlastnosti „Autocomplete“ a klikněte na „Koupit kredity“, nebo najděte
Vyberte funkci „Odoo IAP“ a klikněte na „Zobrazit služby“. Na výsledné stránce vyberte
Žádaný balíček.

.. poznámka::
Pokud databáze vyčerpá kredity, bude se při kliknutí na
Společnost, která se doporučí, bude odkaz na webové stránky a loga.

Dozvíte se více o našich zásadách ochrany osobních údajů „Zásady ochrany osobních údajů“ <https://iap.odoo.com/privacy>.

.. poznámka::
Uživatelé podnikového řešení Odoo s platnou licencí získají bezplatné kredity na testování:abbr:`IAP (In-App
Před rozhodnutím o koupi dalších kreditů pro databázi se ujistěte, že jste si přečetli popis funkce „Koupit“. To zahrnuje
demonstrační databáze, vzdělávací databáze a databáze bez aplikace.

.. viz též:
:doc:`../../../základy/nákupy_v_aplikaci“
