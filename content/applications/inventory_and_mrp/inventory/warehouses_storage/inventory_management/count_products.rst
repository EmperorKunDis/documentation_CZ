=====================
Změny v inventáři
=====================

.. |Ia| nahradit:: Změny v inventáři
.. nahradí se za inventarizační rozdíly

Ve skladovém systému jsou zaznamenány zásoby v databázi, ale nemusí být vždy přesné.
odpovídat skutečným zásobám v skladu. Rozdíl mezi záznamy může být způsoben
poškození, lidský faktor, krádež nebo jiné faktory. Proto musí být provedeny úpravy zásob
vyrovnat rozdíly a zajistit, aby záznamy v databázi odpovídaly skutečnosti.
sečetla v skladu.

Stránka Změny zásob
==========================

Pro zobrazení stránky „Změny zásob“ přejděte na:
Operace --> Fyzická inventura“.

.. obrázek: počet_produktů/stránka_úpravy zásob.png
:alt:Na stránce Změny skladových zásob jsou uvedeny produkty, které jsou momentálně na skladě.

Stránka „Úpravy zásob“ zobrazuje všechny produkty, které jsou nyní skladem.

.. poznámka::
Na seznamu je pouze zboží s množstvím větším než nula.
Stránka „Nastavení“. Chcete-li zobrazit produktové řady s aktuálním množstvím nulovým, přejděte na
:menu_selektor:„Skladové zásoby –> Zprávy –> Sklad“.

Pro každou produktovou řadu je uveden následující seznam informací:

- :guilabel:`Lokalita“: konkrétní místo v skladu, kde je produkt uložen.
Tato sloupec je viditelný pouze v případě, že jsou zapnuté :doc:`Skladovací místa <use_locations>`.
- :guilabel:`Oblíbené“: označuje produkty, které byly oblíbené.
- :guilabel:`Produkt“: produkt, který je uveden na řádku upravování zásob.
- :guilabel:„Číslo šarže / sériové číslo“: identifikátor, který je přiřazen konkrétnímu produktu uvedenému v seznamu.
Mohou obsahovat písmena, číslice nebo kombinace obojího.

.. poznámka::
Pokud má konkrétní produkt v zásobě více než 1,00 kusů a více než jeden sériový číslo,
číslo nebo číslo šarže, které mu bylo přiděleno, každý jedinečně identifikovaný produkt je zobrazen samostatně.
produktová řada s vlastním číslem šarže/sériového čísla zobrazená pod :guilabel:`Číslo šarže/Sériové číslo
sloupec.

- :guilabel:`Datum vypršení platnosti“: datum, do kterého jsou zboží s touto sériovou číslem
vypršet.
- :guilabel:`Poslední datum sčítání“: poslední datum, kdy byla kvantita aktualizována.
- :guilabel:`Soubor“: soubor, který obsahuje množství uvedené v poli.
- :guilabel:`Množství na skladě“: množství produktu, které je nyní zaznamenáno v databázi.
- :guilabel:`Jednotka měření`: jednotka, ve které je produkt měřen. Pokud není uvedeno jinak
specifikované (např. v :guilabel:`Librech“ nebo :guilabel:`Uncích“), výchozí :abbr:`Jednotka měření
Mezi jednotkami je vztah.
- :guilabel:`Početní množství“: skutečný počet, který byl spočítán při inventarizaci. Tento prvek
zadána výchozí hodnota, ale lze ji změnit v závislosti na tom, zda odpovídá :guilabel:`Na skladě
Ať už je to kvantita nebo ne.
- :guilabel:Rozdíl: rozdíl mezi :guilabel:Skladovou zásobou a
:guilabel:`Počet“, když se provede úprava zásob. Rozdíl je
je automaticky vypočítávána po každé inventarizaci.
- :guilabel:`Datum plánovaného sčítání“: datum, ke kterému má být provedeno sčítání. Pokud není uvedeno jinak,
Tento datum se automaticky nastaví na 31. prosince aktuálního roku.
- :guilabel:`Uživatel“: osoba přiřazená k počtu v databázi. To může být buď
fyzicky sečíst zásoby nebo aplikovat počet v databázi.

..tip:
Později skryté sloupce jsou skryty v základním nastavení. Chcete-li tyto sloupce zobrazit, klikněte na
:ikona:"nastavení" (adjust) do pravého dolního rohu formuláře.
Zobrazíte požadovanou sloupec zaškrtnutím políčka vedle této možnosti.

... inventarizaci / vytvoření úpravy:

Vytvořte inventurní opravu
------------------------------

Chcete-li vytvořit novou inventární úpravu z stránky „Inventární úpravy“, klikněte na
:guilabel:'Nový'. To vytvoří novou řádek pro úpravu zásob na konci stránky.

..tip:
|Ia| lze vytvořit také na základě předpovědního reportu na úrovni jednotlivce.
produktový záznam. Chcete-li otevřít zprávu, přejděte na produktový záznam a klikněte
:guilabel:`Předpověď“ chytrý tlačítko. Poté v horní části stránky klikněte na :guilabel:`Aktualizovat
„Množství“, pak „Nový“.

.... obrázek:: count_products/forecast-report.png
:alt:Tlačítko Aktualizovat množství na výkazu pro předpověď v aplikaci Sklad.

Na prázdné řádce pro úpravu zásobního listu klikněte na rozbalovací nabídku pod položkou „Produkt“
sloupci a vyberte produkt. Pokud je sledovaný pomocí číslovek nebo sériových čísel
číslo, které je požadováno, musí být vybráno z rozbalovací nabídky pod
Sloupec „Číslo šarže“.

..tip:
Příkaz Inventarizace lze použít také k vytvoření nebo zaznamenání sériových čísel a šarží.

Poté nastavte hodnotu v sloupci „Počítaná kvantita“ na množství zjištěné pro tento
v průběhu inventarizace.

Vpravo od sloupce „Počet“ je sloupec „Datum plánované dodávky“ a
Kromě změny pomocí tlačítka „Uživatel“ lze také provést přes příslušné nabídky.
:guilabel:`Datum plánovaného zpracování“ změní datum, ke kterému by měla být inventarizace prováděna.
a přiřazením uživatele k konkrétnímu inventarizačnímu příkazu.
Pro účely dohledatelnosti.

Jakmile provedete všechny změny na nové lince úpravy zásob, klikněte mimo ni.
Tím se přizpůsobení odstraní a čára bude na začátku stránky.

Pokud je počet zboží v zásobě vyšší než počet zboží, které je k dispozici, hodnota
v sloupci „Rozdíl“ je zelená barva. Pokud je počítané množství menší než
„Množství na skladě“, hodnota v sloupci „Rozdíl“ je červená. Pokud je
množství odpovídá a nebylo vůbec změněno. V poli Diferenci se nic nezobrazuje
sloupek.

.. obrázek: count_products/difference-column.png
:alt:Rozdílová sloupec na stránce pro úpravy zásob.

V této fázi se eviduje inventurní úprava, ale ještě nebyla aplikována. To znamená
Že před upravením nebyla aktualizována skutečná množství na skladě.
počítaná hodnota.

... inventarizaci a aplikaci úpravy:

Použijte upravený počet
--------------------

„Ia“ lze dokončit několika způsoby. První možností je kliknout na
Druhou možností je zaškrtnout políčko „Použít“ na konci řádku vpravo.
zaškrtávací políčko na začátku řádku. To zobrazí nové možnosti tlačítka nahoře na stránce.
Jedním z nich je tlačítko „Použít“, které místo toho vyvolá
zobrazí se okno „Změna zásob“.

Z této nabídky lze ke skladovému pohybu přiřadit odkaz nebo důvod.
výchozím nastavení je pole „Důvod inventury“ předvyplněno dnešním datem, tedy datem, kdy
je možné upravit tak, aby odrážela jakýkoli referenční bod nebo důvod, který je požadován.

Jakmile bude připraveno, klikněte na tlačítko „Použít“ pro aplikaci inventární úpravy.

.. poznámka::
Při aplikaci inventurní korekce vzniká zároveň :doc:`záznam o pohybu skladových zásob (ZPS).
v hlášení „Historie přesunů“ (*Moves History*) pro sledovatelnost.

.. obrázek: počet_produktů/použít_účtování_skladových změn.png
:alt:Použití všech možností aplikuje inventarizační úpravu pouze jednou, pokud je uveden důvod.

Přesunout produkty
=================

„Ia“ lze také použít k přesunu produktů na různá skladová místa nebo
Různé balíčky. Chcete-li přesunout produkt, zaškrtněte políčko vpravo na konci řádku pro
žádaný produkt. V horní části stránky klikněte na tlačítko „Přesunout“. Kliknutím na něj se otevře
pop-up.

.. obrázek: počet_produktů/přesunout_panel.png
:alt:Produkty Relocate se zobrazují v okně Změna zásob.

V následném okně zadejte tyto informace:

- :guilabel:Toto umístění: nové místo pro produkty.
- :guilabel:`Toto balení“: nové balení produktů.
- :guilabel:`Důvod přemístění“: důvod stěhování.

.. důležité::
Přesun produktů funguje pouze na interních lokalitách. Produkty nelze přesouvat mezi
společnosti.

Pouze uživatelé s právy *Administrátor* mohou provádět přesun produktů.

Nastaveno na nulu
===========

Klepnutím na „Ia“ lze také vymazat zásoby tím, že se k nim přičte nula.
zaškrtnutí položky v levém sloupci řádku s požadovaným produktem. V horní části stránky klikněte na
Klikněte na tlačítko „Akce“ (ikona „nástroje“) a z rozevírací nabídky vyberte možnost „Nastavit na 0“.
Jakmile je tento proces dokončen, použijte upravený počet pomocí příkazu :ref:`apply <inventory/apply-adjustment>`.

Sčítat produkty
==============

Sčítání produktů je častou aktivitou v skladu. Po dokončení sčítání se přesuňte na
Vyberte položku „Aplikace inventáře“ > „Provoz“ > „Fyzická inventarizace“.
Sloupec „Počet zboží“.

Na každé produktové lince identifikujte, zda je hodnota v sloupci „Množství na skladě“
v databázi odpovídají nově spočítané hodnoty. Pokud je zaznamenaná hodnota a počítaná hodnota
klikněte na ikonu „fa-bullseye“ vpravo dole u produktů.

Tím se kopíruje hodnota z sloupce „Množství na skladě“ do
sloupci „Počet“ a nastaví hodnotu sloupce „Rozdíl“ na
„0,00“. Následně po aplikaci se zobrazí inventární pohyb s „0,00“:
Zaznamenané v historii úprav zásob výrobku.

.. obrázek: count_products/zero-move.png
:alt: Přesun při nulovém počtu záznamů v inventáři.

Pokud nově spočítaná hodnota pro daný produkt nebude odpovídat hodnotě v poli :guilabel:`On
Klikněte na ikonu „fa-bullseye“ a zvolte možnost „Záznamy“.
ikonu, která zaznamená skutečnou hodnotu v poli „Počet“ ve sloupci „Zaznamenaný počet“.

Pro toto klikněte na pole v sloupci „Počet“ v konkrétní zásobovací položce.
řádku pro nastavení produktu, jehož počet se mění. To automaticky přiřadí
:guilabel:`Počet“ na hodnotě „0,00“.

Chcete-li změnit tuto hodnotu, zadejte novou hodnotu odpovídající skutečné, právě spočítané hodnotě a klikněte
od linie. Tím se šetří nastavení a hodnota se automaticky upraví na
Sloupec „Rozdíl“.

Pokud je počet zboží v zásobě vyšší než počet zboží, které je k dispozici, hodnota
v sloupci „Rozdíl“ je zelená barva. Pokud je počítané množství menší než
„Množství na skladě“, hodnota v sloupci „Rozdíl“ je červená. Pokud je
množství odpovídá a nebylo vůbec změněno. V poli Diferenci se nic nezobrazuje
sloupek.

Poté, co byla aplikována, se pohyb s rozdílem mezi :guilabel:`Quantity On Hand` a
Počet kusů je zaznamenán v historii úprav zásob produktu.

.. obrázek: count_products/history-inventory-adjustments.png
:alt:Dashboard s historií inventárních úprav, který zobrazuje seznam předchozích pohybů produktu.

Vyvolá se nabídka „Akce“ při výběru jednoho nebo více produktů zaškrtnutím jejich políček.
V nabídce „Akce“ je možnost „Nastavit na množství skladem“, která nastaví
vybrané položky z „Počet kusů“ na „Skladové množství“.
„Nastavit na 0“, což nastaví počet vybraných produktů na nulu.

.. obrázek: počet_produktů/úprava zásob - akce.png
:alt:Nápověda k položce Změny inventáře v nabídce Akce.

.. důležité::
Sčítání se někdy stane, ale nemůže být ihned aplikováno v databázi. V této době
Při skutečném počtu a aplikaci úpravy zásob dochází k pohybu produktů. V tom případě
Množství na skladě v databázi se může změnit a již nemusí být v souladu s počítaným
množství. Pro další bezpečnostní opatření požaduje Odoo potvrzení před aplikací zásob
přizpůsobení.

Zrušit úpravu zásob
==============================

Pro obnovení změn provedených v inventáři přejděte na:
Hlášení --> Historie pohybů.

Zaškrtněte políčko vpravo od řádku s požadovaným produktem. V horní části stránky klikněte
Tlačítko ikonky „fa-gear“ s textem „Akce“, které otevře nabídku, a klikněte na „Zpět
Vyrovnání zásob.

.. poznámka::
Po zrušení inventárního úpravy není linka ze seznamu :guilabel:`Moves
Historie reportu. Namísto toho je přidána další řádka, tentokrát s slovem „[reverted]“
do sloupce „Zdroj“.

...... obrázek:: count_products/vrazeni-pravidelneho-nastaveni.png
:alt: Odkaz na pole referenčních údajů v přehledu historie pohybů v aplikaci Inventář.

Změna frekvence inventarizace
================================

Výchozí datum pro |ia| je vždy stanoveno na 31. prosince
v aktuálním roce. Pro některé společnosti je však důležité mít přesný počet skladových zásob.
vždy. V takovém případě lze změnit termín splatnosti dluhu.

Pro změnu výchozího termínu vyberte v menu volbu „Skladové aplikace - Konfigurace“.
Nastavení“. Pak v sekci „Provádění“ najděte „Den inventarizace za rok
a měsíců, který obsahuje seznam s výchozím nastavením na 31. prosince.

.. obrázek: počet_produktů/roční inventura.png
:alt: Upravte datum příští inventury pomocí nastavení ročního dne a měsíce.

Pro změnu dne klikněte na „31“, zadejte číslo od 1 do 31 podle požadovaného měsíce
rok.

Pak klikněte na tlačítko „Prosinec“ a zobrazí se nabídka. Vyberte
žádaný měsíc.

Jakmile provedete všechny požadované změny, klikněte na tlačítko „Uložit“ pro uložení všech změn.

...Inventarizační plán počtu:

Připravte velké zásoby
-------------------------

Pro plánování velkých inventur, jako je například úplný seznam všech položek skladem, nejprve přejděte
:menu:Skladové zásoby --> Provoz --> Fyzická inventura

Pak vyberte požadované produkty k počítání zaškrtnutím políčka na nejlepravém konci každého.
produktová řada.

..tip:
Chcete-li požádat o počet všech produktů skladem, zaškrtněte políčko v horní části stránky.
tabulce v hlavičkové řádce vedle štítku „Lokalita“. Toto vybere všechny produkty
řádky.

.. obrázek: count_products/count-popup.png
:alt:Požádejte o počítadlo na stránce pro úpravy zásob.

Jakmile si vyberete všechny požadované produkty, klikněte na tlačítko „Požádat o počet“ v
Na horní část stránky. To otevře okno s názvem „Požádat o počet“, kde je uvedeno
do formuláře lze zadat:

- :guilabel:`Datum inventury“: plánovaný termín sčítání.
- :guilabel:`Uživatel“: uživatel, který je zodpovědný za počítání.
- :guilabel:`Datum účtování“: datum, ke kterému se provede ocenění zásob.
- :guilabel:`Počet kusů na skladě`: zanechat prázdné pole pro počet položek v každé řadě produktu, vyberte
:guilabel:`Zanechat prázdné“. Předvyplnit skladovou zásobu každé produktové řady aktuální
hodnota zaznamenaná v databázi, vyberte možnost „Změnit aktuální hodnotu“.

.. poznámka::
Možnost Leave Empty vyžaduje, aby zaměstnanec provádějící audit ručně zadal
počet, který spočítali, zatímco možnost „Nastavit aktuální hodnotu“ vyžaduje pouze
zaměstnanci, aby zkontrolovala počítaný počet a kliknula na „Použít“.

Poté klikněte na tlačítko „Přijmout“ a požádejte o počet.

.. obrázek: count_products/count-popup.png
:alt:Požádejte o zobrazení počtu na stránce s úpravami zásob.

.. důležité::
V aplikaci Odoo **Barcode** mohou uživatelé zobrazit pouze zásoby přidělené jim.
a jsou naplánovány na dnešek nebo dříve.

Sčítání se někdy stane, ale nemůže být ihned aplikováno v databázi. V této době
Při skutečném počtu a aplikaci úpravy zásob dochází k pohybu produktů. V tom případě
Množství na skladě v databázi se může změnit a již nemusí být v souladu s počítaným
množství. Pro další bezpečnostní opatření požaduje Odoo potvrzení před aplikací zásob
přizpůsobení.

Historie přizpůsobování
==================

Podrobnosti o inventarizaci lze zobrazit kliknutím na ikonu „fa-history“
:guilabel:`Historie“ ikonu.

Uživatel, který počítal hlasy, je uveden v závorkách v poli „Odkaz“.
uživatel, který aplikaci počítal, je uveden v poli :guilabel:`Done By`.

.. obrázek: počet_produktů/úpravy_historie.png
:alt:Historie úpravy zásob.

Inventarizační kontrola
---------------

Audit záznamu lze zobrazit na stránce „Úprava záznamů“. Tento audit
zahrnuje záznamy o inventáři před i po dokončení sečtení, aby bylo možné sledovat, co se změnilo.

Na stránce „Úprava zásob“ zaškrtněte políčko v horním levém rohu stránky.
Vyberte všechny řádky. Pak klikněte na tlačítko „Požádat o počet“. V okně nastavte
Vyberte „Počet“ a poté „Nastavit aktuální hodnotu“. Poté klikněte na „Potvrdit“.

Po návratu na stránku „Upravení zásob“ vyberte všechny řádky znovu a klikněte
:menuvolba:Tisk --> Počítat listy. Tlačítko „Počítat listy“ exportuje do formátu PDF.

.. viz také:
:doc:`počet cyklů“
