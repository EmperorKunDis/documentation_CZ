================
Soutěž na dodavatele
================

... nakupovat/spravovat smlouvy/alternativní poptávky:

.. |PO| nahradit za: abbr: PO (objednávka)
.. |POs| nahradit za: zkratka: `POs (Purchase Orders)`
.. |RfQ| nahradit za: zkratku `RfQ (požadavek na nabídku)`
.. |RfQs| nahradit za: :abbr:`RfQs (žádosti o nabídku)“

Občas se může stát, že společnosti budou chtít pozvat dodavatele k podání nabídek na podobné zboží nebo služby.
hned. To pomáhá společnostem při výběru nejlevnějších a nejrychlejších dodavatelů pro jejich konkrétní podnikání
potřeby.

V Odoo lze tento postup provést vytvořením alternativních požadavků na nabídku (RfQ).
dodavatelé. Jakmile je od každého dodavatele obdržená odpověď, mohou být produktové řady z každého |RfQ|
a na základě porovnání může být učiněno rozhodnutí o tom, z jakých dodavatelů si máte zakoupit které produkty.

.. poznámka::
Někdy nazývané jako „výzva k podání nabídky“, tento proces je primárně využíván organizacemi
veřejný sektor, který je zákonem povinen jej používat při nákupu.
Firmy mohou také využít alternativní |RfQ|, aby efektivně utrácely peníze.

Konfigurace
=============

Pro vytvoření alternativních nabídek RfQ musí být funkce Purchase Agreements povolena v
Nastavení aplikace Purchase. Chcete-li tuto funkci zapnout, přejděte do sekce:
Konfigurace --> Nastavení. V části „Objednávky“ klikněte na zaškrtávací políčko
:guilabel:`Kupní smlouvy“.

Poté klikněte na tlačítko „Uložit“ a změna se aplikuje.

.. obrázek: zadávací řízení/zadávací řízení povoleno nastavením.png
:align:center
:alt:Povolení smluv o nákupu v nastavení aplikace Nákup.

... nakupovat/spravovat obchody/vytvářet poptávky:

Vytvořte RfQ.
===============

Vytvoření nového |RfQ| podle pokynů v dokumentaci :doc:`rfq`.

.. viz též:
„Tutoriál Odoo: základy nákupu a první poptávka


... nakupovat/spravovat obchody/vytvářet alternativy:

Vytvořte alternativní RfQ
=========================

Jakmile je vytvořen požadavek na nabídku (PO) a odeslán dodavateli, mohou být vytvořeny další
prodejce porovnat ceny, dodací lhůty a další faktory, aby jim pomohli při rozhodování o objednávce.

Pro vytvoření alternativního RFQ z původního klikněte na záložku „Alternativa“. Poté klikněte
:guilabel:Vytvořit alternativu“. Kliknutím se zobrazí okno „Vytvořit alternativu“
se objevuje.

.. obrázek: zadávací řízení/zadávací řízení vytvořit alternativu.png
:align:center
:alt:Vyskakují výzvy k podání nabídek, které vytváří alternativní citaci.

Vyberte si z nabídky alternativního dodavatele v rozevíracím seznamu vedle
:guilabel:„Dodavatel“ pole, k němuž je přidělená alternativní nabídka.

Nedaleko odtud je zaškrtávací políčko „Kopírovat produkty“, které je výchozím nastavením vybrané.
vybrané, produktové množství původního RfQ je zkopírováno do alternativy.
První alternativní nabídka, zaškrtněte políčko a klikněte na tlačítko „Vytvořit
Alternativní“. Otevře se nová tabulka „RfQ“.

Jelikož byla zaškrtnuta možnost „Vytvořit alternativu“, nový formulář je již
obsahující stejné výrobky, množství a další detaily jako původní |RfQ|.

.. poznámka::
Pokud je zaškrtnuto pole „Kopírovat produkty“ při vytváření alternativní nabídky,
Pokud nechcete, nemusíte přidávat žádné další produkty.

V případě, že je vybraný dodavatel uveden v sloupci „Dodavatel“ pod konkrétním produktem
v příloze objednávky jsou přeneseny hodnoty zadané na formuláři produktu.
musí být změněny ručně, pokud je třeba.

Jakmile je připravena druhá alternativní nabídka, klikněte na záložku „Alternativy“.
a poté: `Vytvořit alternativu`.

Otevře se okno „Vytvořit alternativu“. Zvolte jiného dodavatele
z roletky vedle pole :guilabel:`Dodavatel“. Pro tento konkrétní |RfQ| však *nezaškrtněte*.
zaškrtnutí položky „Kopie produktů“. Tím se odstraní všechny produkty na nové alternativě |RfQ|
nechat prázdné. Konkrétní produkty, které má být objednány od tohoto dodavatele, lze
přidány, jak je potřeba.

Když je připravená, klikněte na tlačítko „Vytvořit alternativu“.

..tip:
Pokud by měla být z odkazu „Alternativy“ odstraněna alternativní citační citace, může se to stát takto:
jednotlivě odstranit kliknutím na ikonu „X“ (odstranit) v konci řádku.

Tím vznikne třetí nový RfQ. Ale protože objem produkce původního RfQ byl
Není přenesená, produktové řady jsou prázdné a nové produkty lze přidat podle potřeby
kliknutím na tlačítko „Přidat produkt“ a výběrem požadovaných produktů z roletky.

Jakmile jsou přidány požadované množství konkrétních produktů, klikněte na tlačítko „Odeslat e-mailem“.

.. obrázek: zadávací řízení/zadávací řízení - prázdný formulář.png
:align:center
:alt: Prázdná alternativní citace s alternativami v navigačním panelu.

Otevře okno „Sestavit e-mail“, kde lze zprávu dodavateli napsat.
můžete si ji upravit a přidat přílohy, pokud je potřebujete. Jakmile bude hotová, klikněte na tlačítko „Odeslat“.

Z nové podoby klikněte na záložku „Alternativy“. Pod touto záložkou jsou všechny tři |RfQs|
být viditelné v sloupci Reference. Dodavatelé jsou také uvedeni pod
sloupci „Dodavatel“ a pořadí „Celkem“ (a „Stav“) objednávek.
Jsou v řadách také.

Datum v sloupci „Očekávaný příjezd“ je pro každého dodavatele vypočítáno na základě jakýchkoli
přednastavené dodací lhůty pro dodavatele a produkty.

... nakupovat/spravovat obchody/propojit poptávku:

Odkaz nové nabídky na stávající nabídku
=====================================

I když se citační vzor nezíská přímo z karty Alternativy jiného |RfQ|,
Ještě je možné ho propojit s již existujícími |RfQs|.

Pro to začněte vytvářet novou |RfQ|. Přejděte na: „Nákupní aplikace – Nový“. Vyplňte
podle předchozích pokynů <nákup/správa obchodních případů/vytvoření RFQ>.

Poté klikněte na záložku „Alternativy“. Od té doby, co byl vytvořen nový RfQ
Samostatně zatím nejsou propojeny žádné další objednávky.

Aby se však tento |RfQ| propojil s existujícími alternativami, klikněte na
první řádek v sloupci Výrobce.

.. obrázek: oznameni-o-vyhlaseni-zakazky/oznameni-o-vyhlaseni-zakazky-odkaz-rfq-popup.png
:align:center
:alt:Pop-up, který spojí novou nabídku s již existujícími poptávkami.

Otevře se okno s názvem „Přidat alternativní PO“. Vyberte požadovaný již vytvořený
Klikněte na „Vybrat“ a všechny tyto objednávky jsou nyní kopií této objednávky.
je k dispozici v záložce „Alternativy“.

..tip:
Pokud je zpracováváno velké množství |POs| a předchozí |POs| nelze najít, klikněte
ikonu „fa-chevron-down“ vedle vyhledávací lišty nahoře
z okna s nápovědou.

Pak v sekci „Skupina“ klikněte na „Dodavatel“. Dodavatelé jsou zobrazeni
vlastní seznamy rozbalovacích nabídek a každý dodavatelský seznam lze rozšířit pro zobrazení otevřených |POs|.
ten dodavatel.

... nakupovat, spravovat obchody, porovnávat produktové řady:

Srovnejte produktové řady
=====================

Alternativní nabídky lze porovnat vedle sebe, aby bylo možné určit, která firma nabízí nejlepší
smlouvy o dodávkách zboží, které jsou součástí objednávek.

Chcete-li porovnat alternativní nabídky, přejděte do aplikace „Nákup“ a vyberte jednu z
dříve vytvořených poptávek.

Klikněte na záložku „Alternativy“ a zobrazí se všechny spojené poptávky.
Vyberte možnost „Vytvořit alternativu“ a klikněte na „Srovnání produktových řad“. To vás přesměruje do
stránce „Srovnání objednávek“.

.. obrázek: zadávací řízení/srovnání produktů.png
:align:center
:alt:Stránka s porovnáním produktových řad pro alternativní poptávky.

Stránka „Srovnání objednávek“ (výchozí) se větví podle „Produktu“. Každá položka
je zobrazena vlastní podskupina rozbalovacího seznamu a obsahuje všechny
V sloupci Reference zadejte čísla PO.

.. poznámka::
Chcete-li odstranit řádky produktů z stránky „Srovnání objednávek“, klikněte na tlačítko
v řadě výrobků na pravici.

Tímto způsobem se tento konkrétní produkt odstraní jako volitelná možnost z stránky a změní se
:guilabel:`Celková cena“ produktu na stránce nastavte na „0“.

Dále je v objednávkovém formuláři RfQ, kde je tento produkt zahrnutý, uvedena i požadovaná
změněno na „0“.

Jakmile jsou vybrány nejlepší nabídky, jednotlivé produkty lze vybírat kliknutím na
Tlačítko „Vybrat“ na konci každé odpovídající řádky.

Jakmile jsou vybrány všechny požadované produkty, klikněte na tlačítko „Poptávka“.
kousky chleba (v horní části stránky), abyste se mohli vrátit na přehled všech |RfQs|.

... nakupovat/spravovat obchody/zrušit/ponechat alternativy:

Zrušit (nebo ponechat) alternativy
=============================

Jakmile si vyberete požadované produkty na stránce „Srovnání objednávkových linií“,
Zbývající poptávky (RfQ) bez vybraných produktů lze zrušit.

Cena v sloupci „Celkem“ pro každý produkt, který nebyl vybrán, je automaticky nastavena na
„0“, které je uvedeno na konci každé odpovídající řádky.

Ačkoliv zatím nebyly zrušeny, ukazuje to, že každý z těchto objednávek může být zrušen.
bez vlivu na ostatní živé objednávky, jakmile budou tyto objednávky potvrzeny.

.. obrázek: výzvy_k_podání_nabídek/výzva_k_podání_nabídky_nula_celkem.png
:align:center
:alt:Zrušené citační údaje v přehledu nákupní aplikace.

Potvrďte požadavek na nabídku (RfQ) pro výrobky vybrané v požadavku na nabídku (RfQ), klikněte do požadavku na nabídku (RfQ) a potom
:guilabel:`Potvrdit objednávku“.

To způsobuje okno s dotazem „Co když poptávky?“.
vystoupit.

Pro zobrazení podrobného formuláře jednoho ze seznamu nabídek klikněte na řádkovou položku pro tuto nabídku.
otevře okno „Alternativní PO“ s detaily daného konkrétního
Zadání lze prohlédnout zde.

Jakmile je hotovo, klikněte na tlačítko „Zavřít“ v okně s upozorněním.

V okně „Co se týče alternativních požadavků na nabídky“ jsou dvě možnosti
jsou prezentovány: „Zrušit alternativy“ a „Ponechat alternativy“.

Pokud by tento |PO| nebyl potvrzen, klikněte na tlačítko :guilabel:`Odmítnout`.

Vybráním možnosti „Zrušit alternativní nabídky“ se automaticky zruší všechny alternativní nabídky |RfQs|.
:guilabel:`Keep Alternatives“ udrží alternativní nabídky otevřené, takže je stále lze přistupovat, pokud
Pokud je třeba objednat další množství produktů, musí se to udělat později.

Jakmile jsou objednány všechny produkty, vyberte z nabídky „Zrušit alternativy“
je otevřena v té době.

.. obrázek: výzvy_k_podání_nabídek/vyzvy_k_podani_nabidek_uzavirat_nebo_rušit.png
:align:center
:alt: Zrušit nebo zachovat okno pro alternativní nabídky.

Konečně pomocí kousků chleba nahoře na stránce klikněte na „Požadavky na cenovou nabídku“
Navigujte zpět na přehled všech RfQs.

Zrušené objednávky jsou viditelné šedě a uvedeny s :guilabel:`Zrušeno“ stavem pod
sloupci „Stav“ na konci jejich příslušných řádků.

Nyní, když byly objednány všechny požadované množství výrobků, lze proces nákupu dokončit a
mohou být přijaty do skladu.

.. viz též:
:doc:`objednávky na oblečení“
