=================
Dodat nové vybavení
=================

...údržba/správa zařízení/přidat nové vybavení:

V Odoo se termínem „zařízení“ označuje jakýkoliv předmět používaný v běžných provozních činnostech, včetně
výroba produktů. To může znamenat kus stroje na výrobní lince nebo nástroj, který je
v různých lokalitách nebo počítač v kancelářských prostorách. Registrované vybavení v Odoo může být
mají společnost, která používá databázi Odoo, nebo třetí stranu, jako je dodavatel v případě
pronájmu zařízení.

S pomocí modulu Odoo Maintenance je možné sledovat jednotlivé kusy vybavení spolu s
informace o jejich údržbě. Chcete-li přidat nové zařízení, přejděte na
:guilabel:`Údržba“ modul, vyberte :menuselection:"Zařízení" --> "Stroje a nástroje" --> "Vytvořit",
a konfigurovat zařízení následovně:

- :guilabel:`Název zařízení“: název produktu daného zařízení
- :guilabel:`Kategorie vybavení“: kategorie vybavení, ke kterému patří zařízení; např.
počítače, stroje, nástroje atd. Nové kategorie lze vytvořit přesunem na
:menuselection:`Nastavení“ -> „Vybavení“ a kliknutím na tlačítko :guilabel:`Vytvořit“
- :guilabel:`Společnost“: společnost, která vlastní zařízení. Zde může jít o společnost, která využívá
Odoo databáze nebo třetí strana
- :guilabel:`Používáno“: specifikujte, jestli je zařízení používán konkrétním zaměstnancem, oddělením nebo obojím.
Vyberte možnost „Ostatní“ pro specifikaci pracovníka i oddělení.
- :guilabel:`Tým údržby“: tým odpovědný za servis zařízení; nové týmy mohou být
vytvořené přechodem na:menu: `Nastavení -> Údržbové týmy`.
výběrem možnosti „Vytvořit“; členy týmů lze také přiřadit z této stránky
- :guilabel:„Servisní technik“: osoba odpovědná za údržbu zařízení; tento termín může být použit pro
přiřadit konkrétní osobu v případě, že není přiřazen žádný tým údržby nebo pokud je přiřazen
Členem vybraného týmu by měl být vždy osoba odpovědná za vybavení, kterou lze kdykoli přidat.
Odoo jako uživatel může být přiřazen jako technik
- :guilabel:`Používá se v lokalitě“: místo, kde je zařízení použito; jedná se o prostý text
pole, které lze použít k určení míst, která nejsou pracovními centry, jako je například kancelář.
příklad
- Pokud se zařízení používá v pracovním centru, zadejte ho zde.
může být přiřazen do pracoviště také z menu „Údržba -> Stroje“.
„Zaměstnanecké centrum“, vyberte pracovní centrum nebo vytvořte nové pomocí tlačítka „Vytvořit“.
a kliknutím na záložku „Vybavení“ v dialogovém okně pracoviště

.. obrázek:add_new_equipment/new-equipment-form.png
:align:center
:alt: Příklad plně konfigurovaného nového vybavení.

Zahrňte další informace o produktu
--------------------------------------

Na stránce je také záložka „Informace o produktu“, kde lze poskytnout další informace.
podrobnosti o zařízení:

- :guilabel:`Dodavatel“: dodavatel, od kterého bylo zařízení zakoupeno
- :guilabel:`Referenční kód dodavatele“: kód přidělený dodavateli
- :guilabel:`Model“: konkrétní model zařízení
- :guilabel:`Sériové číslo“: jedinečné sériové číslo zařízení
- :guilabel:`Datum účinnosti“: datum, kdy se zařízení stalo použitelným; používá se k
vypočítat hodnotu MTBF (průměrný čas mezi poruchami)
- :guilabel:`Cena“: Cena zařízení
- :guilabel:`Datum vypršení záruky“: datum, kdy vyprší záruka na zařízení

.. obrázek:add_new_equipment/new-equipment-product-information.png
:align:center
:alt:Informace o produktu pro nový kus vybavení.

Přidejte podrobnosti o údržbě
-----------------------

Na spodní části stránky je k dispozici záložka „Údržba“, která poskytuje informace o závadě.
frekvence zařízení:

- :guilabel:`Očekávaný čas mezi poruchami“: průměrný počet dní, po které je zařízení
Je očekáváno, že bude fungovat mezi poruchami. Toto číslo lze nastavit ručně.
- :guilabel:„Průměrný čas mezi poruchami“: průměrný počet dní, po které zařízení funguje
neúspěchů. Toto číslo se vypočítává automaticky na základě předchozích neúspěchů a nelze jej
může být ručně konfigurován.
- :guilabel:`Odhadovaný termín dalšího selhání“: odhadované datum, kdy se zařízení může dočkat svého dalšího
neúspěch.
Tento datum se vypočítává automaticky na základě informací v poli :guilabel:`Průměrný čas mezi
Velikost pole „Porucha“ a „Nejnovější porucha“ nelze změnit ručně.
- :guilabel:Nejnovější selhání“: datum, kdy se zařízení zhroutilo. Toto datum je vypočítáno
na datum vytvoření poslední požadavku na údržbu zařízení a nelze ji konfigurovat
ručně.
- :guilabel:`Průměrný čas na opravu“: Průměrný počet dní potřebných k opravě zařízení.
Počet je automaticky vypočítán na základě doby trvání předchozích požadavků na údržbu.
Není možné je nastavit ručně.

.. obrázek:add_new_equipment/new-equipment-maintenance.png
:align:center
:alt:Karta údržby pro určité zařízení.

..tip:
Chcete-li zobrazit jakékoliv otevřené požadavky na údržbu pro konkrétní zařízení, přejděte na stránku s informacemi o tomto zařízení.
a klikněte na tlačítko „Údržba“ v horní části stránky.
