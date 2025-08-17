====================
Servis po prodeji
====================

Po prodeji poskytované služby lze v aplikaci Helpdesk nakonfigurovat pro jednotlivá oddělení.
Pokud je funkce povolena, uživatelé mohou :ref:`vydávat náhrady <pomoci/nahrady>`, :ref:`generovat slevové kupony
<helpdesk/coupons>`, „proces vrací“ <helpdesk/returns>, a „plánuje opravy“ <helpdesk/scheduled>.
<helpdesk/opravy> nebo :ref:`servisní zásahy přímo ze zakázky <helpdesk/field>“.

Zřídit pozáruční servis
===========================

Začněte tím, že zapnete pozáruční servis na konkrétním **týmu Helpdesku**, přejděte do
:menuselection:`Pomocná aplikace -> Konfigurace -> Týmy pomocné aplikace“ a klikněte na tým
služby by měly být aplikovány. Pak přejděte do sekce „Po prodeji“ na týmu
Nastavení stránky a vyberte, která z následujících možností chcete povolit:

- :guilabel:`Vrácení peněz“: vystavuje kreditní faktury pro vrácení peněz zákazníkovi nebo upravuje zbývající částku dlužnou.
- :guilabel:`Slevové kupony“: nabízí slevy a zboží za zvýhodněné ceny prostřednictvím stávajícího systému slevových kuponů.
- :guilabel:`Vracení zboží“: iniciuje vrácení zboží od zákazníka prostřednictvím obrácené přepravy.
- :guilabel:`Opravy“: vytváří opravárenské objednávky pro poškozené nebo nefunkční produkty.
- :guilabel:`Servisní služba“: plánování terénních zásahů prostřednictvím aplikace **Servisní služby**.

.. obrázek: pozáruční/pozáručně-zapnuto.png
:alt:Možnosti pozáručního servisu, které jsou na pracovišti podpory k dispozici.

Služby, které jsou povoleny, se mohou lišit v závislosti na typu podpory týmu.

.. nebezpečí::
Protože všechny pozáruční služby v Odoo vyžadují integraci s jinými aplikacemi, umožňuje
Jeden z nich může vést k instalaci dalších modulů nebo aplikací. Instalace
nová aplikace na databázi One-App-Free spouští 15denní zkušební dobu. Na konci zkušební doby, pokud
Pokud nebude placená předplatná přidána do databáze, již nebude dostupná.

.. _helpdesk/vrácení peněz:

Vystavit dobropis
=============================

Kreditní poznámka je dokument vystavený zákazníkovi, který ho informuje o tom, že mu byla připsána
určité částky peněz. Mohou být použity k poskytnutí plného vrácení peněz zákazníkovi nebo ke snížení
zůstatková pohledávka. Většinou vznikají prostřednictvím účetnictví nebo fakturace
je možné vytvořit i prostřednictvím Helpdesku.

.. důležité:
Faktury musí být zadány před tím, než bude vystaven kreditní doklad.

Vytvořit kreditní poznámku lze v aplikaci Helpdesk na záložce „Tiket“ kliknutím na
Tlačítko „Vrácení peněz“ v pravém horním rohu lístku. To otevře okno „Vrácení peněz“.
Pop-up okno.

.. obrázek: pozáruční/pozáruční vrácení peněz
:alt:Výhled na stránku pro vytvoření reklamace.

Vyplňte potřebné údaje do políček:

 - :guilabel:Objednávka na prodej: pokud byla původní vstupenka odkazována na objednávku na prodej, automaticky
populace v tomto oboru.
 - :guilabel:`Produkt“: produkt, který je na lístku uvedený. Pokud se v tomto poli vybere nějaký výrobek, zobrazí se pouze
Vybírat lze objednávky, dodání a faktury obsahující tento produkt.
 - „Číslo šarže“: tento prvek je **pouze** viditelný, pokud byl vybrán „Produkt“.
Má spojené číslo nebo sériové číslo.
 - „Faktury k vrácení“: tento údaj je **povinný**. Pokud nejsou dostupné žádné faktury,
rozbalovací nabídce se zobrazí informace o tom, že tento zákazník nemá v současné době vyexpedované faktury.
:guilabel:`Produkt“ nemá žádné související faktury.
 - :guilabel:`Důvod zobrazený na faktuře“: Tento prázdný pole se automaticky vyplní s tiketem
číslo, ale lze ho upravit s dalšími informacemi.
 - :guilabel:'Účetní deník': účetní deník, kam se kreditka zaeviduje. Po
Při výběru faktury se tento pole automaticky nastaví na účetní knihu uvedenou na původní faktuře, i když
Může být změněn, pokud je třeba.
 - :guilabel:`Datum obratu“: když na tento odkaz kliknete, použijte kalendář, který se zobrazí.
Vyberte datum faktury kreditní poznámky. Toto pole je **povinné**.

Po vyplnění nezbytných polí klikněte na tlačítko „Zpět“ nebo „Zpět a vytvořit“.
Faktura.

:guilabel:`Zpětná faktura“ vytvoří kreditní fakturu ve stavu návrhu, který lze upravovat předtím, než bude odeslána.
Tato možnost může být použita k poskytnutí částečného vrácení peněz.

:guilabel:`Zpětná faktura“ vytvoří kreditní fakturu, která je automaticky zadána do účetnictví.
faktura ve stavu návrhu. Faktura obsahuje stejné informace jako původní faktura
Tato informace však může být upravena.

Jakmile je faktura odepsána, přidá se tlačítko „Faktury“ do
Tiket Helpdesku.

... obrázek: after_sales/after-sales-credit-note-smart-button.png
:alt: Pohled na chytré tlačítko vstupenky se zaměřením na tlačítko kreditní poznámky.

.. viz též:
:doc:`/účetnictví/fakturace/dodací listy/přepravní doklady“

... pomocí helpdesku / kuponů:

Vytvořit kupón z lístku
==============================

Slevové kupony lze použít na změnu ceny produktů nebo objednávek. Podmínky definují způsob použití
omezení kuponu. Programy „Kupón“ jsou konfigurovány v sekci **Prodej**, **Pokladna** nebo
Aplikace pro webové stránky.

.. důležité:
Modul e-commerce **musí být nainstalován**, aby se mohly vytvářet slevové kódy z webu.

Chcete-li vytvořit slevový kupon, otevřete lístek na **Helpdesku** a klikněte na tlačítko :guilabel:`Sleva`.
v levém horním rohu. Vyberte možnost z nabídky „Program slev“ v
Pop-up okno „Vytvořit slevový kód“ se objeví.

... obrázek: after_sales/after-sales-generate-coupon.png
:alt:Výhled na okno pro vytváření slevových kuponů.

.. poznámka::
Vytvořit nový „Program slev“, přejděte na „Prodejní aplikace --> Zboží“.
--> Slevy a věrnostní program" a klikněte na "Nový". Chcete-li umožnit sdílení programu
Klienti HelpDesku musí mít nastavený programový typ na „Slevové kupony“.
generuje jednorázové kupóny, které umožňují okamžitý přístup ke slevám a odměnám.

Slevové kupony lze vytvářet také v aplikaci POS nebo Webová aplikace. Podívejte se na
:dokumentu: „Slevy a věrnostní programy <../../../prodej/prodej/produkty-a-ceny/slevy-a-vernostni-programy>“
více informací.

Klikněte na pole „Platnost do“ a použijte kalendář pro výběr data vypršení platnosti.
pro tento kód slevového kupónu. Pokud je pole nevyplněné, kód není platný.

Klikněte na „Odeslat e-mailem“ a vytvořte e-mail, který pošlete zákazníkovi s kódem slevy.

Klikněte na tlačítko „Získat odkaz“ a vygenerujete odkaz, který můžete poslat přímo zákazníkovi.
Okno „Sdílejte slevové kódy“. Klikněte na tlačítko „Kopírovat“ vedle
V poli „Sdílet odkaz“ zkopírujte výsledky a vložte je do jakékoliv komunikace s klientem.
Když zákazník používá odkaz, kód se automaticky aplikuje na jeho košík.

Po vytvoření slevového kódu se přidá tlačítko „Slevové kupóny“
nejvyšší část lístku; klikněte na chytrý tlačítko pro zobrazení slevového kódu, data vypršení platnosti a
Další informace.

... obrázek: after_sales/after-sales-coupon-smart-button.png
:alt:Výhled na chytré tlačítko na lístku se zaměřením na tlačítko slevového kuponu.

.. viz též:
   - „Slevové kupony“
   - :doc:`../../../sales/sales/products_prices/loyalty_discount`

... pomocí formuláře pro vrácení zboží.

Vrácené zboží
===============

Vrácení zboží probíhá prostřednictvím „obrácených převodů“, které generují nové skladové operace pro
vrácení produktů. Klikněte na tlačítko „Vrácení“ v horní části lístku, abyste otevřeli
Pop-up okno „Návrat“.

.. obrázek: pozáruční servis/tlačítko pro vrácení zboží po záruce.png
:alt:Zobrazení požadavku na podporu s vyznačeným tlačítkem pro návrat.

.. důležité:
Tlačítko „Vrácení“ se objeví pouze na lístku, pokud je zákazník zaregistrován.
doručení do databáze.

Vyberte si prodejní objednávku nebo dodání na vrácení, abyste identifikovali produkty.
musí být vráceny.

Výchozí množství odpovídá ověřenému množství z objednávky na dodání. Aktualizujte
Pokud je potřeba, vyplňte pole „Množství“. Odstranit řádek lze kliknutím na ikonu „Odpadkový koš“
:guilabel:„Odpad“ ikonu.

Vyberte položku „Návratová adresa“ pro zadání místa, kam se mají věci po vrácení zaslat.
Dokončeno.

.. obrázek: pozáruční servis/pozáruční servis - reverzní transfer.png
:alt: Pohled na stránku pro vytváření zpětného převodu.

Pro potvrzení vrácení zboží klikněte na „Vrácení“. Tímto se vygeneruje nová skladová operace pro
vracené zboží.

Pro výměnu přijatého zboží za nové klikněte na „Výměna“.
generuje skladovou operaci v Odoo, která dodá náhradní produkt.

Použijte ozubená kolečka k návratu na požadavek na pomoc. Nový tlačítko „Návrat“ s inteligentním popisem
Je k dispozici na vrchní části lístku.

.. obrázek: after_sales/after-sales-return-smart-button.png
:alt: Pohled na tlačítko „Zpět“ v žádosti o technickou podporu.

.. viz též:
:doc:`/sales/sales/products_prices/returns`

... pomocná služba/opravy:

Odeslat zboží k opravě přes lístek
======================================

Pokud se tiket týká problému s poškozeným nebo nefunkčním produktem, může být vytvořen
vytvořené z helpdeskového lístku a spravované v aplikaci „Opravy“.

Pro vytvoření nové opravy otevřete lístek pomocí volby „Helpdesk“ a klikněte na
Tlačítko „Oprava“ v pravém horním rohu, které otevře formulář „Příručka pro opravy“.

.. obrázek: after_sales/after-sales-repair-reference.png
:alt:Pohled na stránku s odkazy na opravy.

Vyplňte potřebné údaje do políček:

 - :guilabel:`Zákazník“: pole přebírá hodnotu z lístku, nový kontakt však může být
vybrat z roletky.
 - Pokud byl produkt specifikován v poli „Produkt“ na
pokud ano, tak se do tohoto pole automaticky přidává tento produkt. Pokud ne, klikněte do pole pro výběr produktu
z nabídky.
 - :guilabel:`Číslo/sériové číslo“: tento prvek je **pouze** viditelný, pokud se opravují produkty
sledovány podle čísla nebo sériového čísla.
 - :guilabel:`Vrácení zboží“: vracený produkt pochází z objednávky.
 - :guilabel:`Na záruku“: pokud je tato políčka zaškrtnutá, prodejní cena všech produktů z
se nastaví na nulu.
 - :guilabel:`Datum plánovaného termínu“: tento položkový seznam má výchozí hodnotu aktuální datum. Chcete-li vybrat nové datum, klikněte
do pole a vyberte datum pomocí kalendáře s křížovým výběrem.
 - :guilabel:`Zodpovědný“: přiřaďte uživatele z roletky, který bude mít na starosti opravu.
 - :guilabel:`Štítky“: klikněte do pole pro přidání existující štítkové nebo vytvoření nové.
lze přiřadit tagy.

Pokud jsou potřeba díly pro opravu, mohou být přidány v záložce „Díly“.
informace pro vnitřní opravárenský tým lze přidat do záložky „Poznámky k opravě“.

Jakmile je formulář vyplněný, klikněte na tlačítko „Potvrdit opravu“.
Tento opravu, klikněte na tlačítko: guilabel:"Vytvořit nabídku".

Poté se k lístku přidá chytrý tlačítko „Opravy“, které odkazuje na objednávku opravy.

.. obrázek: after_sales/after-sales-repair-smart-button.png
:alt:Zobrazení chytrých tlačítek s důrazem na tlačítko opravit.

..tip:
Jakmile uživatel vytvoří opravný příkaz z helpdeskového lístku, může se k němu dostat prostřednictvím
tlačítko „Oprava“ na lístku nebo odkazu v chatu, i když nemají
přístupová práva k aplikaci **Oprava**.

.. pomocí helpdesku/pole:

Vytvořit úkol z požadavku
=======================================

Na místě provedené zásahy lze naplánovat na základě požadavku a spravovat prostřednictvím aplikace **Servisní tým**.
aplikace. Klienti s přístupem do portálu mají možnost sledovat
postup řešení úkolu v terénu stejně jako by šlo o řešení problému na zákaznické lince.

..tip:
Pro změnu výchozího projektu **Služby v terénu** pro tým přejděte na:
--> Konfigurace --> Tým podpory -> vybrat tým. Vyberte tým pomocí
V sekci „Po prodeji“ vyberte projekt pod sekcí „Servisní služby“.

Pro vytvoření nové úlohy služby v terénu přejděte do lístku typu „Pomoc“. Klikněte
„Plán intervence“ k otevření okna „Vytvořit úkol pro terénní službu“.

.. obrázek: pozáruční servis/pozáruční servis - vytvoření pole služeb.png
:alt: Příklad vytváření úkolu pro terénní službu.

Potvrďte nebo aktualizujte úkol: guilabel:Název.

V poli „Projekt“ v okně „Vytvořit úkol pro servisní zásah“ je výchozí hodnota
stejnému projektu „Služba v terénu“, který byl identifikován na stránce nastavení týmu. Chcete-li změnit
pro tento konkrétní úkol, vyberte jeden z políčka „Projekt“.

Pokud je to možné, vyberte si šablonu listu z rozevírací nabídky.

.. poznámka::
*Pracovní listy pro terénní služby* jsou zprávy, které popisují práci provedenou během úkolu na místě.
Po dokončení práce se pracovní listy podepisují zákazníkem k potvrzení, že práce byla provedena.
Zákazník je spokojený.

Pokud je projekt **Field Service** přiřazený týmu **Helpdesk** a má povoleny pracovní listy,
Má přiřazené výchozí šablony, tyto šablony se automaticky zobrazují v poli „List“.
políčko s výběrem šablony. I tak se ale pole dá upravit a můžete do něj vložit jinou šablonu.
vybrána.

Pokud projekt **Služby v terénu** nemá povolené listy, pak se zobrazí :guilabel:`List
V okně „Vytvořit úkol pro servis“ se pole „Šablona“ nezobrazuje.

Klikněte na tlačítko „Vytvořit úkol“ nebo „Vytvořit a zobrazit úkol“.

Po vytvoření úkolu je k lístku přidána chytrá tlačítka „Úkoly“, která odkazují na
Úkol „Servisní služba“ do zakázky.

.. obrázek: after_sales/after-sales-field-service-smart-button.png
:alt:Zobrazení tlačítka s chytrými funkcemi, které se zaměřují na úkol.

.. viz též:
„Služby v terénu“
