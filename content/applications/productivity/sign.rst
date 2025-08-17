====
Znamení
====

Služba **Odoo Sign** umožňuje odesílat, podepisovat a schvalovat dokumenty online pomocí elektronických podpisů.

Elektronická **podpisová značka** ukazuje souhlas s obsahem dokumentu.
ručně psaný podpis, elektronický pak závazek vázáním na obsah podepsaného
dokument.

S aplikací Sign můžete nahrát jakýkoliv PDF soubor a přidat do něj pole. Tyto pole lze automaticky
Vyplněné údaji uživatele, které jsou v databázi.

.. viz též:
   - „Odoo Sign: stránka produktu <https://www.odoo.com/app/sign>“
   - „Tutoriály Odoo: Podepsání [video] <https://www.odoo.com/slides/sign-61>“

Platnost elektronických podpisů
=================================

Dokumenty podepsané v aplikaci Sign jsou platné elektronické podpisy v Evropské unii a
Spojené státy americké, které splňují požadavky na elektronickou značku většiny
zemích. Právní platnost elektronických podpisů vygenerovaných pomocí Odoo závisí na zemi, ve které žijete.
legislativy. Firmy působící v zahraničí by měly brát v potaz i elektronickou
podpisové zákony.

.. důležité:
Níže uvedené informace nemají právní platnost, slouží pouze k obecnému informování.
Jakmile se rychle mění zákony o elektronických podpisech, nemůžeme zaručit, že všechny informace
je aktuální. Pro právní poradenství týkající se elektronických komunikací doporučujeme kontaktovat místního advokáta.
podpisové shody a platnosti.

Evropská unie
--------------

„Nařízení eIDAS <http://data.europa.eu/eli/reg/2014/910/oj>“ stanoví rámec pro
elektronické podpisy v členských státech Evropské unie.
<https://europa.eu/european-union/about-eu/countries_en>“. Rozlišuje tři typy
elektronické podpisy:

#Jednoduché elektronické podpisy
#Advanced Electronic Signatures
#Kvalifikované elektronické podpisy

Odoo vytváří první typ, **jednoduché elektronické podpisy**; tyto podpisy jsou právně platné.
v rámci EU, jak je uvedeno v nařízení eIDAS.

Elektronické podpisy nemusí být automaticky uznány jako platné. Možná budete muset přinést
dodatečné důkazy o platnosti podpisu. Aplikace Sign nabízí jednoduchý elektronický
podpisu se automaticky shromažďuje nějaké důkazní břemeno během procesu podpisu.
jako:

#E-mailová a SMS ověření (pokud je povoleno).
#. Silná identifikace pomocí aplikace itsme® (k dispozici v Belgii a Nizozemsku)
#Časové razítko, IP adresa a geograficky sledovatelné přístupové protokoly k dokumentům a jejich asociovaným
podpisy
#Dokumentovatelnost a nezměnitelnost (jakákoliv změna podepsaného dokumentu je detekována
Odoo s využitím kryptografických důkazů

.. poznámka::
:doc:`Dokumentace pro Německo <sign/germany>`

Spojené státy americké
------------------------

Zákon o elektronických podpisů v globálním a národním obchodu (Electronic Signatures in Global and National Commerce Act)
<https://www.fdic.gov/regulations/compliance/manual/10/X-3.1.pdf>`, na mezistátní a
mezinárodní úrovni a „UETA (Úmluva o jednotném elektronickém obchodním styku)
<https://www.uniformlaws.org/committees/community-home/librarydocuments?communitykey=2c04b76c-2b7d-4399-977e-d5876ba7e034&tab=librarydocuments>
Na státní úrovni poskytnout právní rámec pro elektronické podpisy. Poznámka: Illinois
<http://www.ilga.gov/legislation/ilcs/ilcs5.asp?ActID=89&> a „New
<https://www.its.ny.gov/electronic-signatures-and-records-act-esra> nebyl přijat, ale
podobného charakteru.

Všeobecně platí, že elektronické podpisy musí splňovat pět kritérií, aby byly uznány za platné:

#Podpis musí být zřetelný a podepsaný s úmyslem podepsat. Například použitím myši k nakreslení podpisu
Musí být možné prokázat úmysl, a podepisující osoba musí mít také možnost se z elektronického dokumentu odhlásit.
#Podepsaný musí nejprve vyjádřit nebo naznačit svůj souhlas s elektronickým obchodováním.
#**Podpis musí být jasně připojen**. V Odoo jsou metadata, jako je adresa IP uživatele,
Je přidána podpisová doložka, která může být použita jako důkaz.
#**Podpis musí být spojen s podepisovaným dokumentem**, například uchováním záznamu
podrobně popisuje, jak byla podpisová stopa zachycena.
#Elektronicky podepsané dokumenty musí být uchovávány a archivovány všemi zúčastněnými stranami.
například poskytnutím podepisujícímu buď úplně vyhotovenou kopii nebo možnost stáhnout si ji.
kopie.

Jiné země
---------------

- :doc:`Alžírsko <sign/algeria>`
- :doc:`Angola <sign/angola>`
- :doc:`Argentina <sign/argentina>`
- :doc:`Austrálie <sign/australia>`
- :doc:`Ázerbajdžán <sign/azerbajdžán>“
- :doc:`Bangladéš <sign/bangladesch>`
- :doc:`Brazílie <sign/brazilie>`
- :doc:`Kanada <sign/canada>`
- :doc:`Chile <sign/chile>`
- :doc:`Čína <sign/china>`
- :doc:`Kolumbie <sign/colombia>`
- :doc:`Dominikánská republika <sign/dominican_republic>`
- :doc:`Ekvádor <sign/ekvador>“
- :doc:`Egypt <sign/egypt>“
- :doc:`Etiopie <sign/ethiopia>`
- :doc:`Guatemala <sign/guatemala>`
- :doc:`Hongkong <sign/hong_kong>`
- :doc:`Indie <sign/indie>`
- :doc:`Indonésie <sign/indonésie>`
- :doc:`Írán <sign/iran>“
- :doc:`Irák <sign/irak>`
- :doc:`Izrael <sign/izrael>“
- :doc:`Japonsko <sign/japan>`
- :doc:`Kazachstán <sign/kazachstán>“
- :doc:`Keňa <sign/kenya>`
- :doc:`Kuvajt <sign/kuwait>`
- :doc:`Malajsie <sign/malajsie>`
- :doc:`Mexiko <sign/mexiko>`
- :doc:`Maroko <sign/maroko>`
- :doc:`Nový Zéland <sign/new_zealand>`
- :doc:`Nigérie <sign/nigeria>`
- :doc:`Norsko <sign/norsko>`
- :doc:`Omán <sign/oman>“
- :doc:`Pákistán <sign/pakistan>`
- :doc:`Peru <sign/peru>`
- :doc:`Filipíny <sign/filipiny>`
- :doc:`Katar <sign/katar>“
- :doc:`Rusko <sign/rusko>`
- :doc:`Saúdská Arábie <sign/saudska_araba>`
- :doc:`Singapur <sign/singapore>`
- :doc:`Jižní Afrika <sign/south_africa>`
- :doc:`Jižní Korea <sign/south_korea>`
- :doc:`Švýcarsko <sign/switzerland>`
- :doc:`Thajsko <sign/thailand>`
- :doc:`Turecko <sign/turkey>`
- :doc:`Ukrajina <sign/ukrajina>`
- :doc:`Spojené arabské emiráty <sign/spojene-arabske-emiraty>`
- :doc:`Spojené království <sign/spojene_kralovstvi>`
- :doc:`Uzbekistán <sign/uzbekistan>`
- :doc:`Vietnam <sign/vietnam>`

Přiložit dokument k podpisu
=======================

Odrazový podpis
------------------

Klikněte na „Nahrát PDF k podpisu“ z vašeho Dashboardu pro jednorázový podpis. Vyberte
Váš dokument otevřete a do něj vložte požadované pole:
Můžete změnit přiřazenou roli pole kliknutím na něj a výběrem
Ten, který chcete.

Po dokončení klikněte na tlačítko „Odeslat“ a vyplňte požadované pole. Jakmile je dokument odeslán,
zůstává k dispozici. Přejděte na: Menu „Dokumenty“ – „Všechny dokumenty“, abyste si mohli prohlédnout své dokumenty.
a stav podpisů.

.. obrázek: sign/signature-status.png
:alt:Stav podpisu

Platnost a upozornění
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Můžete nastavit **datum platnosti** pro dokumenty omezené doby trvání nebo odeslat **automatické e-maily
připomínky k podpisům včas. Z vašeho panelu klikněte na tlačítko „Odeslat“ u
dokument. Na nové stránce přejděte do sekce „Možnosti“ a vyplňte
Zadejte do pole „Platnost“ hodnotu, přepněte vypínač „Poznámka“ a klikněte na hodnotu pro editaci.
Výchozí počet dní mezi připomínkami.

.. obrázek: značka/připomínka.png
:alt:Nastavte počet dní mezi upomínkami

Šablony
---------

Můžete vytvářet šablony dokumentů, když musíte několikrát za sebou odeslat stejný dokument.
pracovní ploše, klikněte na tlačítko „Nahrát šablonu PDF“. Vyberte dokument a přidejte požadované
:ref:`pole <sign/fields>“. Můžete změnit :ref:`povinnost <sign/role>` pole kliknutím na něj
a vybrat si ten, který chcete.

Klikněte na tlačítko „Vlastnosti šablony“ pro přidání „Štítků“ do vaší šablony, definujte
„Pracovní prostor podepsaných dokumentů“, přidejte „Štítky podepsaných dokumentů“ a nastavte
:guilabel:`Přesměrování odkazu“ bude k dispozici v potvrzovacím e-mailu s podpisem.
Po podpisu nebo definujte:guilabel:`Oprávnění uživatelé`, pokud chcete omezit použití vašeho
šablonu pro konkrétní autorizované uživatele nebo skupiny.

Vaše šablony jsou viditelné ve výchozím nastavení na vašem panelu nástrojů. Kliknutím na tlačítko „Odeslat“ můžete rychle
Odeslat šablonu dokumentu příjemci nebo „Sign Now“ v okamžiku, kdy jste připraveni podepsat svůj dokument
Ihned.

..tip:
Vytvořit šablonu z dokumentu, který byl již dříve odeslán, můžete tak, že přejdete na
:menuvyber:"Dokumenty --> Všechny dokumenty". Na dokument, který chcete získat, klikněte na
poté klikněte na vertikální elipsu (:guilabel:`⋮`) a následně na Template.
(:guilabel:'⋮') znovu a pak zvolte „Obnovit“. Dokument se nyní objeví na vašem panelu.
do vašich ostatních šablon.

.. podpis/postava:

Role
=====

Každý prvek v dokumentu Sign je spojen s rolí odpovídající konkrétní osobě. Když
dokument se podepisuje, osoba přidělená do role musí vyplnit své přiřazené pole.
Podepište ho.

Role je k dispozici po přechodu na: menu: „Sign“ → „Konfigurace“ → „Rolí“.

Existující role lze aktualizovat nebo vytvořit nové kliknutím na tlačítko „Nový“.
Vyberte „Název role“ a přidejte další krok ověření, který potvrdí
identitu podepisující osoby a zda lze dokument přidělit jinému kontaktu.
:guilabel:Změnit oprávnění“ pro roli. Můžete také vybrat barvu pro roli.
Tato barva může pomoci pochopit, které role jsou zodpovědné za konfiguraci pole.
šablona.

Zabezpečená identifikace
----------------------

Jako majitel dokumentu můžete požádat o :guilabel:`Extra Authentication Step`,
:ref:`Ověření SMS <sign/sms>` nebo prostřednictvím :ref:`Itsme® <sign/itsme>“ (k dispozici v Belgii a
Nizozemsko). Oba způsoby autentizace vyžadují :ref:`kredity <iap/buying_credits>“. Pokud nemáte
zůstane kredit na účtu, pak se přeskočí ověřovací kroky.

.. viz též:
   - :doc:`Nákup v aplikaci (IAP) <../essentials/in_app_purchase>`
   - :doc:`Ceník SMS a často kladené otázky <../marketing/sms_marketing/cenik_a_faq>`

.._podpis/SMS:

SMS ověření
~~~~~~~~~~~~~~~~

Přejděte na :menuselection:`Sign --> Konfigurace --> Roly“. Klikněte v :guilabel:`Dalších
Sloupec „Kontrola identity“ pro roli a vyberte možnost „Jedinečný kód prostřednictvím SMS“.

.. poznámka::
Před odesláním textových zpráv je nutné své telefonní číslo registrovat. Pro provedení této akce přejděte na
a klikněte na „Koupit kredity“ pod
:guilabel:`Přihlašování pomocí SMS“.

Přejděte k dokumentu, který chcete podepsat, přidejte pole, pro které je potřeba ověření pomocí SMS, například
V poli „Podpis“ a klikněte na „Odeslat“. Na nové stránce vyberte
Vyberte „Zákazník“ a klikněte na „Odeslat“.

Osoba podepisující dokument vyplní pole „Podpis“ a pak stiskne tlačítko „Podepsat“.
klikněte na tlačítko „Ověřit a odeslat dokončený dokument“. Otevře se stránka „Konečné ověření“
kde přidat své telefonní číslo. Jednorázové kódy jsou zasílány formou SMS zprávy.

.. obrázek: sign/sms-verification.png
:alt:Přidejte do dokumentu haš

.. poznámka::
   - Tato funkce je zapnuta výchozím nastavením.
   - Jakmile se k role přiřadí krok ověření, tento krok je
požadované pro jakékoliv pole přiřazené této roli.

.._podpis/jájsem:

Itsme®
~~~~~~

Autorizace pomocí Itsme® může být použita k tomu, aby podepisující osoby poskytovaly svou identitu prostřednictvím Itsme®.
tato funkce je dostupná pouze v Belgii a Nizozemsku.

Tuto funkci lze zapnout v nastavení podpisu a aplikuje se automaticky na
:guilabel:`Zákazník (identifikovaný pomocí služby itsme®)` a pro ostatní role přejděte na
Vyberte položku „Sign > Konfigurace > Hlídání“. Klikněte na položku „Další ověření
Klikněte na tlačítko „Přidat“ a vyberte „Via itsme®“.

Přejděte do dokumentu, který má být podepsán a přidejte pole „Podpis“. Přepněte na
role nakonfigurované k používání této funkce a klikněte na tlačítko „Přezkoumat“ a „Odeslat“.

.. obrázek: sign/itsme-identification.png
:alt: vyberte zákazníka, který je identifikován pomocí služby itsme

Po podpisu dokumentu uživatel vyplní pole „Podpis“ a pokračuje
kliknutím na tlačítko „Zkontrolovat a odeslat dokončený dokument“, což spustí
Stránka „Konečné ověření“, kde je vyžadováno ověření přes svůj účet u společnosti It´s me.

Podpisový haš
==============

Každý podpis dokumentu vytváří **haš - jedinečnou digitální stopu operace.
generované za účelem zajištění stoprocentní kontroly a nezměnitelnosti. Tento proces zaručuje, že každý
změny provedené po přiložení podpisu jsou snadno detekovatelné, což zajišťuje integritu dokumentu.
autenticitu a bezpečnost po celou dobu svého života.

Do podpisů je přidán vizuální bezpečnostní rámec, který zobrazuje začátek hašovací funkce.
uživatelé mohou skrýt nebo zobrazit jej pomocí možnosti „Rám“ při podepisování
dokument.

.. obrázek: sign/sign-hash.png
:alt:Přidání vizuálního bezpečnostního rámečku k podpisu.

..._podpisy/typ-údajů:

Štítky
====

Štítky lze použít k zařazení a uspořádání dokumentů, což uživatelům umožňuje rychle vyhledávat.
filtrovat dokumenty podle specifických kritérií.

Můžete spravovat štítky kliknutím na: menu „Nastavení“ -> „Štítky“. Chcete-li vytvořit štítek, klikněte
:guilabel:`Nový“. Na nové řádce přidejte :guilabel:`Název štítku“ a vyberte :guilabel:`Index barvy“.
pro váš štítek.

Pro přidání štítku do dokumentu použijte seznam dostupný ve vašem dokumentu.

.. poznámka::
Můžete upravit značky podepsaného dokumentu přechodem na: „Dokumenty“ → „Všechny“.
Dokumenty, kliknutím na vertikální elipsu (:guilabel: „⋮“) u dokumentu a poté
:guilabel:`Podrobnosti“ a upravit si :guilabel:`Štítky“.

Udělejte si znamení
==========

Pokud je dokument podepisován různými stranami, můžete si pomocí nastavení pořadí podpisu ověřit,
pořadí, v jakém vaši příjemci podepisují.

Po nahrání PDF s alespoň dvěma poli pro podpisy s různými rolemi a kliknutí
:guilabel:`Odeslat“, přepněte na :guilabel:`Určit pořadí podpisu“ a vyhledejte podepsaného.
jméno nebo e-mailovou adresu, kterou chcete přidat. Můžete si zvolit pořadí podpisu pomocí znaků **1** a **2**
v první sloupcovce.

.. obrázek: podepisovací pořadí/podepsání v pořadí.png
:alt:Přepněte přepínač, abyste určili pořadí podpisu.

Každému příjemci je zaslána pouze jedna výzva k podpisu, a to až poté, co byl podepsán předchozím příjemcem.
Dokončili své činy.

.._podpisy/pole:

Typy polí
===========

Pole jsou v dokumentu použita k označení informací, které musí podepsaný uvést.
Přidat pole do dokumentu jednoduše tahem a pložením z levého sloupce.
dokument.

K podpisu dokumentů lze použít různé typy polí (umístění, doplnění atd.).
přizpůsobení vlastních typů polí (známých také jako typy polí pro podpis), může být
i pro vaše zákazníky, partnery a zaměstnance.

Pro vytvoření a úpravu typů polí přejděte do sekce „Sign --> Konfigurace --> Nastavení -->
Upravit typy polí.

Můžete vybrat existující pole kliknutím na něj nebo vytvořit nové pomocí tlačítka „Vytvořit“. Nejdříve
Upravte pole „Název pole“ a poté vyberte typ pole:

- :guilabel:`Podpis“: uživatelé jsou požádáni o zadání podpisu buď kresbou nebo generováním
automatická podle jména nebo nahraná místní soubor (obvykle obrázek).
Každé další pole typu „Podpis“ pak používá data zadaná do prvního pole.
- :guilabel:„Začátek“: uživatelé jsou požádání o zadání počátečních písmen svého jména, podobně jako
:guilabel:`Podpis“ pole.
- :label:Text: uživatelé zadávají text na jediné řádce.
- :guilabel:`Multiline Text“: uživatelé zadávají text na více řádcích.
- :guilabel:`Záložka“: uživatelé mohou vybrat položku (např. k označení schválení nebo souhlasu).
- :guilabel:`Výběr“: uživatelé si vybírají jednu možnost z různých možností.

Nastavení „Automatické vyplnění partnerového pole“ se používá k automatickému vyplnění pole během
podpisový proces. Ten používá hodnotu jednoho z polí v kontaktním modelu („res.partner“).
osoba podepisující dokument. Pro tento účel zadejte technické jméno pole kontaktního modelu.

..tip:
Pro zjištění technického názvu pole zapněte vývojářský režim a myší přejeďte nad otázku
označit pole.

.. poznámka::
Předvyplněné hodnoty jsou pouze návrhy a lze je upravit podle potřeby osoby, která dokument podepisuje.
dokument.

Velikost polí můžete také změnit pomocí editaci „Default Width“.
:guilabel:`Výchozí výška“. Oba rozměry jsou definovány jako procento celé stránky vyjádřené
desetinné, kde 1 rovná se plné šířce nebo výšce stránky. Výchozí šířka nových polí
Velikost objektu Create je nastavena na 15 % (0,150) šířky celé stránky, zatímco jejich výška je nastavena na 1,5 % (0,015)
výšky celé stránky.

Následně napište :guilabel:`Tip`. Tipy se zobrazují uvnitř šipek na levé straně profilu uživatele.
obrazovka během podpisového procesu, aby pochopili, co krok obnáší (např. „Podepište zde“
nebo „Vyplňte datum narození“). Můžete také použít text :guilabel:`Zástupný symbol`, který se zobrazí uvnitř
Před dokončením pole.

.. obrázek: sign/tip-placeholder.png
:alt: Příklad tipu a vzoru pro Odoo Sign
