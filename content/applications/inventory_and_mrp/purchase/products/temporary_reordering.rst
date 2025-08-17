==========================
Přechodné pravidlo pro přeskupení
==========================

Některé podniky vyžadují, aby určité produkty byly vždy skladem ve stanoveném minimálním množství.
dostatečně dlouhou dobu. Firmy mohou vytvořit *nákupní režim
v Odoo pravidla pro automatizaci nákupních objednávek na konkrétní produkty.

Pravidla přeskupování udržují předpovězené zásoby nad určitou hranicí, aniž by překročily
určená horní hranice nebo maximální částka. Když produkt s pravidlem opakovaného nákupu klesne pod
určené množství, Odoo vytvoří objednávku pomocí určeného způsobu (např. „Koupit“ nebo
*Výroba*) doplnit zásoby.

V některých případech se mohou podniky rozhodnout pro „dodatečné pravidlo o přeřazení“ v okamžiku, kdy nechtějí
konkrétní produkty, které se budou automaticky doplňovat.

V Odoo se vytvoří pravidlo „přechodného“ doplňování ve výrobní tabulce, když je produkt:

#je konfigurován s trasou „Koupit“
#Není konfigurováno žádné pravidlo pro přeskupování.
#Máme skladem 0 kusů.
#Je součástí prodejního příkazu (PO).

Tato pravidla se smazají po potvrzení nákupního příkazu (PO) vytvořeného pro produkt.

.. viz též:
   - :doc:`../../skladovani/dodavky/pravidla-pro-doplnění/pravidla-pro-naskladnění
   - :doc:`../../nákup/produkty/dodání`

Konfigurace
=============

Chcete-li nakonfigurovat produkt, který spouští dočasná pravidla pro znovuobjednávání při dosažení zásoby „0“, začněte
Přejděte na záložku „Produkty“ a klikněte na tlačítko „Nový“.

.. poznámka::
Stejné konfigurace lze provést i na již existujícím produktu, a to přechodem do
:menu „Aplikace inventáře --> Zboží --> Zboží“ a výběrem existujícího produktu.

V poli produktu zadejte název produktu a ujistěte se, že je zaškrtnuto pole „Může být prodáno“.
Možnost „Může být zakoupen“ je aktivní a nachází se pod názvem produktu.
pole.

Poté nastavte :guilabel:`Produktový typ“ na „Skladovatelný produkt“ a pod :guilabel:`Obecné
Tabulka „Informace“.

Dále klikněte na záložku „Nákup“ a v sekci „Dodavatel“ vyberte možnost „Přidat řádek“.
Vybrat dodavatele ze seznamu. Poté nastavit cenu podle položky „Cena“.

.. důležité:
Pro fungování dočasných pravidel pro objednávání je nutné nastavit dodavatele. Při :abbr:`PO (nákupní
(v případě, že ještě není vyčerpán).
:guilabel:`Dashboard doplňování zásob“ v aplikaci „Sklad“ vyvolává varování, že je třeba přidat dodavatele.
výrobní forma.

.... obrázek: dočasné přeskupení/varování o dočasném přeskupení.png
:synchronizace: střed
:alt:Pop-up varování při kliknutí na doplnění produktu bez nastaveného dodavatele.

Před vytvořením prodejního příkazu (SO) na produkt zkontrolujte stav skladu pomocí chytrého filtru „Na skladě“.
Tlačítko na produktovém formuláři zobrazuje „0.00 jednotek“. Pak ujistěte se, že jsou nastaveny pravidla opakovaných objednávek
Tlačítko s nápisem „0“ ukazuje, že na tento produkt se žádné předpisy nevztahují.

.. obrázek: dočasné přeskupení/dočasné přeskupení chytrých tlačítek.png
:align:center
:alt:Produkt ve tvaru chytré řady tlačítek s pravidly pro přeskupování a tlačítky na dosah ruky.

Aktivovat dočasné pravidlo pro přeskupení
=================================

Aby se spustil dočasný pravidlo pro přeskupení objednávek, vytvořte novou objednávku na produkt pomocí navigace
:menu-vyber->Prodej aplikace--> Nová.

Poté přidejte zákazníka do pole „Zákazník“ a klikněte na „Přidat produkt“ pod
sloupec „Produkt“ v záložce „Dodací řádky“. Poté vyberte požadovaný produkt
z rozevírací nabídky. Nakonec potvrďte „SO (prodejní objednávka)“.

.. obrázek: dočasné přeskupení/dočasné přeskupení prodejních objednávek.png
:align:center
:alt: Objednávka pro produkt bez nastavených pravidel opakované objednávky.

.. nákup/dodání zásob:

Zpráva o doplnění zásob
==========================

Zobrazit dočasné pravidlo pro přeskupení, které bylo vytvořeno pro produkt, který je vyprodaný.
Vyberte si položku „Skladové aplikace“ - „Provoz“ - „Dodávky“.
příkazovém řádku „Doplnění“.

Na tomto panelu najděte produkt pro který byla vytvořena pravidla dočasného přeobjednávání.
produktová řada, její množství „Na skladě“, záporné množství „Předpověď“ a „Koupit“.
„Trasa“ a „Počet kusů na objednávku“, které mohou být vidět.

Dále jsou k dispozici dvě možnosti doplnění vpravo od řádku: guilabel:„Objednávka
Jednou je to „Jednorázový“ a jednou „Automat“.

.. obrázek: dočasné přeskupení/dočasné přeskupení zásobovacího panelu.png
:align:center
:alt: Zpráva o doplňování, která zobrazuje dočasné pravidlo pro doplňování a možnosti.

Pro použití pravidla jednorázového dočasného přeřazení klikněte na tlačítko „Pouze jednou“. Toto akce spustí
okno s potvrzením v pravém horním rohu, které zobrazuje text:guilabel:`Další doplnění
byla vygenerována nová objednávka,“ řekl.

..tip:
Jakmile je objednávka vytvořena po kliknutí na „Objednat jednou“, obnovte
Stránka. Dočasné přeřazení produktu již nezobrazuje
:guilabel:`Doplnění zásob“ panelu.

Úplná objednávka
=======================

Pro zobrazení objednávky vytvořené z panelu „Dodavatelské zásoby“ přejděte na
Vyberte možnost „Koupit aplikaci“ a vyberte vytvořený PO (objednávku na nákup).
Přehled poptávek.

Zde klikněte na „Potvrdit objednávku“, pak na „Dostat produkty“ a nakonec na
Klikněte na tlačítko „Potvrdit“ pro dokončení objednávky.

.. obrázek: dočasné přeskupení/dočasné přeskupení nákupního příkazu.png
:align:center
:alt:Příkaz k nákupu produktu, který byl objednán s pravidlem dočasného opětovného objednání.

Nyní lze původní objednávku dodat a fakturovat.

.. poznámka::
Jakmile je objednávka dodána a fakturována, ujistěte se, že neexistují žádné pravidla pro opětovné objednání.
na výrobku.

Přejděte do sekce „Aplikace Inventura --> Zboží --> Zboží“, vyberte produkt a potvrďte
že tlačítko „Chytré nastavení“ s názvem „Přeskupení pravidel“ zobrazuje hodnotu 0.
