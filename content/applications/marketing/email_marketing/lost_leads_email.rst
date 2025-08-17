=============================
E-mailová zpráva o obnovení neaktivních kontaktů
=============================

V Odoo jsou ztracené kontakty odstraněny ze stávajícího CRM kanálu, ale lze je stále cílit.
Aplikace pro e-mailový marketing k použití v rámci strategických kampaní, například na obnovu ztracených kontaktů.

E-mail o znovuaktivaci ztracených kontaktů se zaměřuje na kontakty, které byly ztraceny v určitém časovém období.
a používá vlastní filtry a důvody pro vyřazení nežádoucích kontaktů z poštovního seznamu.

Jakmile je dokončena e-mailová zpráva o obnovení sledování, může být odeslána tak, jak je, nebo upravena a odeslána.
různé skupiny pro testování A/B nebo jako šablona pro pozdější použití.

Příklad:
Sklad má zbytky zboží ze série limitovaných předmětů loňského roku, aby pomohl vyčistit
vyřadit přebytečné zásoby, skladník vytváří e-mail s názvem „ztráta kontaktu“, aby se spojil
informovat o příležitostech, které byly ztraceny, a upozornit na skladové zásoby.

Ve schránce pro ztracené objednávky používá následující filtry:

   - :guilabel:`Černá listina“ je „nepovolený“
   - :guilabel:`Vytvořeno od` *>=* `01.01.2024 00:00:01`
   - :guilabel:`Stage“ není v „New“, „Qualified“ nebo „Won“
   - :guilabel:`Ztracený důvod“ je v „Nedostatek zásob“
   - a buďto:guilabel:Active je nastaveno nebo není

.... obrázek: lost_leads_email/příklad.png
:synchronizace: střed
:alt:Filtr pro obnovení ztracených kontaktů, který vylučuje důvody jako „Příliš drahé“.

..tip:
Při přidávání a odstraňování filtrů se soustřeďte na hodnotu „# záznamů“ pod názvem filtru.
filtrační sekce. Toto číslo ukazuje celkový počet záznamů, které odpovídají aktuálnímu
kritérií.

K zobrazení seznamu všech shodných záznamů klikněte na text „# záznam(y)“.

....... obrázek::lost_leads_email/records.png
:synchronizace: střed
:alt: Text záznamu # je níže pod seznamem filtrů příjemců.

Minimální požadavky
====================

Chcete-li vytvořit a doručit kampaň na obnovení ztracených kontaktů e-mailem, použijte nástroje CRM a e-mail.
Marketingové aplikace* musí být nainstalovány a nakonfigurovány.*

Tady jsou minimální potřebné filtry, které se týkají kampaně na obnovení ztracených kontaktů:

- Záložka „Příjemci“ (**musí být nastavena na**)
Model *Zákazník/Příležitost*.
- Filtr „Černá listina“ (viz email_marketing/blacklist_filter) k vyloučení odběratelů, kteří se odhlásili z odběru.
- Vytvořeno na <email_marketing/created_on_filter> pro cílení na ztracené leady,
určité časové období.
- filtrů „Stadium“ (viz email_marketing/stage_filter), které vyloučí kontakty, které byly již získány.
Stále jsou aktivní v nových fázích prodejního kanálu (tedy například „New“, „Qualified“ atd.). Tyto hodnoty
bude se lišit podle organizace; je však minimálně životaschopné vyloučit všechny kontakty.
**Vyhraná etapa**
- Jeden nebo více filtrů „Ztracený důvod“ (<email_marketing/lost_reason_filter>) k vyloučení nežádoucích
jako duplicitní záznamy, spamy nebo neaktuální záznamy.
- Dva filtry typu :ref:`Active <email_marketing/active_filter>`, které cílí na obě skupiny aktivních
neaktivní kontakty.

Přidejte potřebné filtry
=========================

Nejprve přejděte do aplikace „E-mailový marketing“ a na stránce „Kampaně“
klikněte na tlačítko „Nový“ v pravém horním rohu.

.. _e-mailový marketing/pole příjemce:

V novém formuláři „Pošta“ zadejte vhodný název pro e-mail
odpovídající pole. Poté v poli „Příjemci“ vyberte
Vyberte z roletky „Lead/Opportunity“ model.

.._email_marketing/blacklist_filter:

V části pravidel pod pole „Příjemci“ klikněte na modifikovat filtr.
:guilabel:`▶ (trojúhelník směřující doprava)` ikona pro rozšíření filtrů pravidel. Ponechte výchozí
Pravidlo „černé listiny“.

.. e-mailový marketing/vytvořeno:

Vytvořeno
----------

Začněte kliknutím na „Nová pravidla“ pod výchozími „Pravidly pro černou listinu“. Pak klikněte
první pole nového pravidla, které se objeví, a vyberte parametr
rozbalovací nabídka. Po zadání konkrétního časového období během kterého byly cílené kontakty
ztráta může být označena například jako 30 dní předem, 90 dní předem, minulý rok atd.

V druhém poli vyberte: „menší nebo rovno“ („<=“) a „větší nebo rovno“ („>=“).
nebo rovno“ nebo „je mezi“ jako datový operátor, aby bylo možné zadat čas
výběr zvolen v třetím poli.

V třetím poli použijte okno kalendáře pro výběr dat a klikněte na tlačítko „Použít“.
Zamknout časový rozsah.

.. obrázek:lost_leads_email/created-on.png
:align:center
:alt:Nastavení vlastního filtru, které určuje časový úsek jako cokoliv před dnešním datem.

.. důležité:
Pokud se aplikují více pravidel, ujistěte se, že je na začátku prohlášení.
:guilabel:`Příjemci“ filtru seznamu čte: :guilabel:`Všechny následující pravidla splňují“. Pokud
neklikejte na výrok a z rozevírací nabídky vyberte „všechny“ (oproti
:guilabel:"kohokoliv").

.... obrázek::lost_leads_email/match-all.png
:synchronizace: střed
:alt:Výrok na začátku seznamu filtrů s otevřeným roletkovým menu.

.. _email_marketing/stupen_filtru:

Stage
-----

Nyní přidejte filtr „Stage“ s hodnotou „New“, „Qualified“ a „Won“.
fáze prodejního procesu.

.. poznámka::
Tento krok předpokládá, že v obchodním procesu CRM existují tři fáze: „Nový“, „Kvalifikovaný“ a „Získaný“.
Nicméně jména na jevišti se mohou lišit podnik od podniku. Podívejte se do skutečné databáze.
jména v aplikaci CRM pro tento krok.

Začněte znovu kliknutím na „Nový pravidlo“ a vyberte „Stadium“ z prvního pole.
položky nabídky. Ve druhé položce vyberte operátor „neobsahuje“, a ve třetí
Vyberte pole „Nový“, „Kvalifikovaný“ a „Získaný“ a definujte tak fáze
parametry pravidla.

Při přidání pravidla takto se logika v třetím poli zobrazí jako :code:`OR` („|“).
prohlášení.

.. obrázek:lost_leads_email/stage-is-in.png
:align:center
:alt:Ve filtračním pravidle zahrňte více fází, použijte operátor „je v“.

..tip:
Další způsob, jak přidat pravidla pro *Stage*, je použít jedno pravidlo na řádek pomocí
:guilabel:`obsahuje“ nebo „neobsahuje“ operátory a ručně zadávat výraz.
definující znaky v každém názvu fáze. Tento způsob však umožňuje pouze jednu volbu.
čas, který může být užitečný pro rychlé zapínání a vypínání filtrů na liště :guilabel:`Hledat...`.

.... obrázek::lost_leads_email/stages.png
:synchronizace: střed
:alt:Tři filtrační pravidla vyžadující, aby Stage neobsahovaly nové, kvalifikované nebo vyhrané.

.. _email_marketing/ztráta důvodu filtr:

Ztracený rozum
-----------

Poté přidejte jednu nebo více pravidel „Ztracený důvod“ (anglicky:Lost Reason), abyste vyloučili kontakty, které by neměly být cílem.
pro konkrétní případ: důvody ztráty zakázky viz. „ztráta příležitosti“ v sekci „Prodej / CRM / Pipeline“.

Pro to udělejte další :guilabel:`New Rule`, a opět v prvním poli vyberte
Vyberte z rozevírací nabídky „Ztracený důvod“. Pro operátora vyberte buď „není
nebo:guilabel: neobsahuje z nabídky. S volbou buďto nebo použijte třetí
pole pro zadání důvodu ztráty (nebo více důvodů, v závislosti na volbě operátora).
zahrnout do pravidel.

Pokud zvolíte operátor „neobsahuje“, opakujte předchozí kroky a přidejte další
ztrácejí důvody, které jsou potřebné, kde každý ztracený důvod obsazuje jeden řádek pravidel po druhém.

Více informací najdete v části níže popisující, jak :ref:`vybrat vhodný ztracený
důvodů <email_marketing/select_lost_reasons>.

.. obrázek: lost_leads_email/reasons.png
:align:center
:alt: Seznam filtračních pravidel, které vylučují všechny důvody ztráty kromě požadovaného důvodu.

.._email_marketing/aktivní filtr:

Aktivní
------

Nakonec přidejte dva filtry :guilabel:`Active`, abyste zahrnuli jak aktivní, tak i neaktivní kontakty.
kampaň.

.. důležité:
Přidání obou aktivních i neaktivních záznamů je nutné, aby bylo možné získat celkový rozsah ztracených
je v databázi na prvním místě. Dělání jednoho bez druhého výrazně ovlivňuje počet cílových
záznamy o e-mailové kampani, nezahrnuje ani úplné nebo přesné ztracené kontakty
diváci.

Nejprve klikněte na ikonu „Přidat větví“ u nejnověji vytvořeného pravidla (například
„Ztracený důvod“), která je uprostřed tří ikon, které se nacházejí vpravo od řádku pravidel.
Takto se přidá dvojice pravidel :guilabel:`jakékoliv z`. Poté v prvním poli horního pravidla
nově vytvořené pobočce vyberte parametr „Aktivní“ z roletky. Potom
automaticky vyplňuje číst: guilabel:'Aktivní' je 'povoleno'.

V prvním poli spodního pravidla větve vyberte z roletky :guilabel:`Aktivní`
menu znovu. Tentokrát ale vyberte z nabídky operátorů „není“.
druhé pole. Pravidlo by pak mělo znít: :guilabel:`Aktivní` není „povoleno“.

.. obrázek: lost_leads_email/active.png
:align:center
:alt:Dva filtrační pravidla typu „Match Any Of“, která zahrnují jak aktivní, tak i neaktivní kontakty.

Přidejte obsah
================

Nyní je třeba vytvořit obsah těla e-mailu.
použít některý z předdefinovaných stylizovaných šablon nebo si vybrat mezi „Plain Text“ a
Možnosti „Začít od nuly“ pro přesnější kontrolu. Další informace najdete v
*E-mailový marketing*:ref:`dokumentace o tom, jak vytvořit e-mail <email_marketing/create_email>“.

..tip:
Chcete-li si sadu filtrů uložit pro pozdější použití, klikněte na tlačítko :guilabel:`Uložit jako oblíbený
disk) a zadejte název (např. „Ztracené kontakty“), pak klikněte na tlačítko :guilabel:„Přidat“.

.... obrázek::lost_leads_email/favorite-filter.png
:synchronizace: střed
:alt:Pop-up okno pro uložení filtru „Uložit jako oblíbené“ může zachránit kritéria ztracených kontaktů na později.

Odeslat nebo naplánovat
================

Jakmile jsou všechny součásti e-mailové kampaně hotovy, buď:

- Klikněte na modrou tlačítko „Odeslat“ v pravém horním rohu formuláře, abyste okamžitě odeslali
e-mailová adresa; nebo
- klikněte na šedé tlačítko „Rozvrh“, které se nachází napravo od tlačítka „Odeslat“.
aby e-mail byl odeslán v budoucnu na určité datum a čas.

..tip:
Zvažte použití metody A/B testování, která by měla poslat alternativní verzi e-mailu určitému procentu
cílové skupiny. To může pomoci určit, které předměty a obsah těla produkují nejlepší výsledky.
kliknutí na odkaz, než bude finální verze zaslána zbylým kontaktům.

Pro toto otevřete záložku „Testování A/B“ v e-mailovém formuláři a zaškrtněte políčko vedle
:guilabel:`Povolit testování A/B“. Pak upravte parametry podle potřeby a klikněte na :guilabel:`Vytvořit
Alternativní verze.

.... obrázek:lost_leads_email/ab-testing.png
:synchronizace: střed
:alt:Karta A/B testy s zaškrtnutou položkou umožňující A/B testování vytvoří alternativní verzi.

..._email_marketing/vyberte_důvod_pro_ztrátu:

Vyberte vhodný důvod ztráty
===============================

Když je kontakt označen jako ztracený, Odoo doporučuje vybrat důvod proč byl kontakt ztracen.
tato příležitost nevedla k prodeji. Udělat tak však udržuje organizaci vedení obchodu a reportování dat
přesná a generuje potenciál k následnému oslovení v budoucnu.

Pokud existující důvod ztráty není vhodný, uživatelé s potřebnými oprávněními mohou vytvořit nový.
Jedná se o ztracené důvody v databázi, které se mohou lišit podle organizace.
z plynovodu do plynovodu.

Více informací o *Ztracených důvodech* včetně jejich vzniku najdete na
:doc:`../../sales/crm/pipeline/lost_opportunities`.

Výchozí nastavení Odoo zahrnuje několik běžných důvodů „Ztracené věci“, například:

- *Příliš drahé*
- *Nemáme lidi, nemáme dovednosti.*
- *Nedostatek zásob*

Při určování důvodů pro zahrnutí do e-mailu na obnovení ztracených kontaktů se zaměřte na
E-mail je reklama, která má za cíl vyhledat jeden nebo více důvodů ztráty. Pak přidejte pravidlo s tímto obsahem:
:guilabel:„Ztracený důvod“ neobsahuje „______“ pro každý důvod v databázi, s výjimkou
relevantní.

Příklad:
Pokud e-mail propaguje výběr zboží, které bylo dříve nedostupné, ale je nyní opět skladem.
Je tedy logické cílit na ztracené důvody: „Nedostatek zásob“.

....... obrázek::lost_leads_email/out-of-stock.png
:synchronizace: střed
:alt: Seznam filtračních pravidel, které vylučují všechny důvody ztráty kromě nedostupnosti.

Pokud e-mail reklamuje slevu, je vhodné cílit na leady s důvodem ztráty:
*příliš drahé*.

.... obrázek:lost_leads_email/too-expensive.png
:synchronizace: střed
:alt: Seznam filtračních pravidel, které vylučují všechny důvody ztráty kromě příliš drahé.

Analyzujte výsledky
===================

Po odeslání e-mailu s aktivací ztracených kontaktů mohou marketingové týmy používat chytré tlačítka vedle
emailu a analyzovat výsledky, abyste mohli určit další kroky.

Kliknutím na kteroukoli z chytrých tlačítek se otevře seznam záznamů, které odpovídají konkrétnímu tlačítku.
kriteria.

.. obrázek:lost_leads_email/smart-buttons.png
:align:center
:alt:Stránka s e-mailem, který byl odeslán, na které jsou vidět chytré tlačítka po celé šířce stránky.

Chytré tlačítka obsahují:

- :guilabel:`Počet odeslaných e-mailů“: celkový počet odeslaných e-mailů.
- :guilabel:`Otevřeno“: procento příjemců, kteří otevřeli e-mail.
- :guilabel:`Odpověděl/a“: procento příjemců, kteří odpověděli na e-mail.
- :guilabel:`Kliknutí“: procento příjemců, kteří na odkaz v e-mailu klikli.
- :guilabel:`Vedení/Příležitosti“: počet vytvořených leadů (nebo příležitostí).
*Pipeline CRM*, jako důsledek e-mailové kampaně.
- :guilabel:`Citace“: počet citací vytvořených v aplikaci *Prodej*.
výsledkem e-mailu.
- :guilabel:`Fakturované“: celkový obrat vzniklý jako výsledek e-mailové kampaně na základě faktur
zasílané zákazníkům a zaplacené zákazníky. Tyto hodnoty jsou zaznamenány buď v poli „Faktura“ nebo
Aplikace pro účetnictví se liší podle aplikace, která je nainstalována v databázi.
- :guilabel:`Přijaté“: procento příjemců, kteří e-mail obdrželi.
- :guilabel:`Odpověď nebyla doručena“: procento e-mailů, které se nedoručily.
- :guilabel:`Zapomenuté“: počet příjemců e-mailu, kteří ho obdrželi, ale neinteragovali s ním.
s ním v nějakém významném smyslu (tj. otevřený, kliknutý atd.).

E-mailová péče
===============

*Emailový marketing* (někdy nazývaný také jako *proces vedení zákazníků*) je proces zasílání sérií
včasné a relevantní „nudge“ e-maily pro kontaktování potenciálního zákazníka, vytvoření hlubšího vztahu a
Nakonec přeměnit vedení na prodej.

Účelem udržování kontaktu je udržet e-mailovou kampaň „viditelnou“ nebo na vrcholu seznamu příchozích zpráv.
až do chvíle, kdy budou připraveni nakoupit.

Efektivní péče o zákazníky je možné provádět mnoha způsoby, ale často zahrnuje:

- Odeslání prvního e-mailu (například e-mail k obnovení ztracených kontaktů).
- Posílat každý týden (nebo na základě konkrétních podnětů) následný e-mail po dobu trvání
kampaň.
- Kontinuálně analyzovat výsledky, abychom se mohli učit o tom, co fungovalo a přineslo nám prodeje.
- Přizpůsobovat se tak, aby zůstal „viditelný“ na vrcholu schránky pro odesílané e-maily.
Případně doufat v odpověď z hlavy.

Jak se kampaň rozvíjí, může tým marketingu poslat různé emaily s následováním podle toho, jak
Odpověděl na něj minulý týden.

Příklad:
Marketingový tým chce reklamovat obnovení omezeného sortimentu všem kontaktům.
ztratili důvod, proč nemají dostatek zásob. Vytváří tři týdny trvající vedení zákazníků.
kampaň.

   - **Týden 1:** Marketingový tým odesílá první e-mail s předmětem: „Omezená edice“.
Zboží je opět skladem! Neváhejte!“
   - **Týden 2:** tým pro marketing posílá dva různé e-maily podle toho, jak se lead odpověděl.

     - Pokud zákazník ignoroval e-mail z týdne 1: „Skladníky už nezbývá mnoho, jste si objednal?“
     - Pokud klikl na e-mail z týdne 1: „Máte ještě čas přidat do své sbírky“

   - Týden 3: Marketingový tým odesílá poslední e-mail všem kontaktům, kteří nebyli převedeni.
s tímto textem: „Sleva 20 %, nepropásněte poslední šanci si tyhle věci koupit předtím, než zmizí!“

V průběhu celé kampaně se tým marketingu neustále odvolává na chytré tlačítka po celém
nahoře na stránce s e-mailovou kampaní a zjistěte, jaké procento kontaktů otevírá, kliká nebo ignoruje
e-maily. Dále také pravidelně analyzují zprávy o počtu příležitostí, nabídek a
V rámci kampaně vznikly faktury.

.. viz též:
   - :doc:`/email_marketing`
   - :doc:`odhlášení odběru“
   - :doc:`/marketing_automation``
