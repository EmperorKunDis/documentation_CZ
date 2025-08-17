=========
Argentina
=========

Webináře
========

Níže najdete videa s obecným popisem lokalizace a její konfigurace.

- „Webinář - Lokace Argentiny <https://www.youtube.com/watch?v=_H1HbU-wKVg>“.
- „E-commerce – Lokace v Argentině“ (https://www.youtube.com/watch?v=5gUi2WWfRuI).

.. viz též:
   - „Chytrý návod – Lokace Argentiny
<https://www.odoo.com/slides/smart-tutorial-localizace-pro-Argentinu-130>
   - Dokumentace o zákonnosti a souladu s předpisy v Argentině


Konfigurace
=============

Instalace modulů
--------------------

:ref:`Instalujte následující moduly, abyste získali všechny funkce argentinského
lokalizace:

.. seznam tabulkový::
:hlavičkové řádky: 1
:šířky: 25 25 50

   * Jméno
     - Technické označení
     - Popis
   * Argentina - Účetnictví
     - „l10n_ar“
     - Výchozí:balík fiskálního umístění <fiscal_localizations/packages>, který reprezentuje
minimální konfigurace pro provoz v Argentině podle AFIP (Administración Federal de
Federálními směrnicemi a pokyny pro veřejné příjmy).
   * –:guilabel:„Argentinské účetní zprávy“
     - „l10n_ar_reports“
     - DPH Kniha faktur a DPH Souhrnné hlášení.
   * :- guilabel:Argentinské elektronické fakturace
     - l10n_ar_edi
     - Zahrnuje všechny technické a funkční požadavky pro vytváření elektronických faktur přes web
služba založená na předpisech AFIP.
   * – Argentina: elektronické fakturace v obchodě
     - „l10n_ar_website_sale“
     - (volitelné) Umožňuje uživateli zobrazit typ identifikace a odpovědnost za AFIP.
e-shopovou objednávku, aby vystavil elektronické faktury.
   * :-:ref:`Argentina - Zadržení plateb <l10n_ar/payment-withholdings>`
     - „l10n_ar_withholding“
     - Umožňuje zadat srážky při platbě faktury.

..._argentině/založte-si-firmu:

Nastavte svou společnost
----------------------

Jakmile jsou nainstalovány moduly pro lokalizaci, první krok je nastavení dat společnosti.
kromě základních informací je nutné vyplnit také pole s odpovědností AFIP.
Typ, který představuje daňovou povinnost a strukturu společnosti.

.. obrázek::argentina/select-responsibility-type.png
:align:center
:alt:Vyberte typ odpovědnosti AFIP.

Kontrolní účet
----------------

V účetnictví je k dispozici tři různé balíčky „Skladby účtů“.
Jsou založeny na typu odpovědnosti společnosti AFIP a vycházejí ze skutečnosti, že
firmy, které nepotřebují takové množství účtů jako firmy s komplexnějším daňovým systémem.
požadavky:

- Monotributista (227 účtů)
- IVA Exento (290 účtů).
- Zodpovědný za registraci (298 účtů).

.. obrázek:argentina/select-fiscal-package.png
:align:center
:alt:Vyberte daňovou lokalizaci.

Konfigurace hlavních dat
---------------------

Elektronické fakturační kreditní údaje
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Životní prostředí
***********

Infrastruktura AFIP je vytvořena ve dvou samostatných prostředích – **testovacím** a **produkčním**.

Testování je poskytováno tak, aby společnosti mohly své databáze otestovat až do chvíle, kdy budou připraveny k migraci
do prostředí **Produkce**. Tyto dvě prostředí jsou totiž zcela izolovaná od sebe
Jinak digitální certifikáty jedné instituce nejsou platné ve druhé.

Pro výběr databázového prostředí přejděte na:
Vyberte možnost „Lokalizace“ a zvolte buď „Prueba (Testing)“ nebo „Produccion (Production)“.

.. obrázek:argentina/select-environment.png
:align:center
:alt:Vyberte prostředí databáze AFIP: Testovací nebo produkční.

AFIP certifikáty
*****************

Elektronická faktura a další služby AFIP pracují s :guilabel:`Web Services (WS)` poskytovanými
AFIP.

Pro komunikaci s AFIP je třeba nejprve požádat o :guilabel:`Digitální
Certifikát, pokud ho ještě nemáte.

#:guilabel:`Vytvořit žádost o podepsání certifikátu (Odoo)“. Když je tato možnost vybrána, vytvoří se
.csr (žádost o podepsání certifikátu) je vytvořen k použití na portálu AFIP.
požádat o certifikát.

.. obrázek::argentina/zadat-vyhledavani.png
:alt:Žádost o certifikát.

#:guilabel:`Vytvořit certifikát (AFIP)“. Přihlaste se na portál AFIP a postupujte podle pokynů
popsané v tomto dokumentu <https://drive.google.com/file/d/17OKX2lNWd1bjUt3NxfqcCKBkBh-Xlpo-/>
>Pokud chcete získat certifikát, musíte se přihlásit na stránce <a href="https://www.google.com/intl/cs/policies/privacy/partners/" target="_blank">https://www.google.com/intl/cs/policies/privacy/partners/</a>.

#:guilabel:`Nahrát certifikát a soukromý klíč (Odoo)“. Jakmile je certifikát vygenerován, nahrajte
jej do Odoo pomocí ikony „Tužka“ vedle pole „Certifikát“ a vyberte
příslušný soubor.

.. obrázek::argentina/upload-certificate-private-key.png
:alt: Nahrát certifikát a soukromý klíč.

.. tip::
V případě potřeby konfigurace homologačního certifikátu se obraťte na oficiální webové stránky AFIP.
dokumentace: „Certifikát o homologaci
http://www.afip.gob.ar/ws/documentacion/certificados.asp>. Dále pak Odoo umožňuje uživateli
připravit si lokální testování elektronické fakturace bez homologačního listu. Následující zpráva
Bude se objevovat v chatu při testování lokálně:

....... obrázek:argentina/lokalni-testovani.png
:align:center
:alt:Faktura byla schválena lokálně, protože se nachází v testovacím prostředí bez testování
certifikát/klíč.

Partner
~~~~~~~

Druh identifikace a DPH
***************************

Argentinská lokalizace přinesla do systému nové typy dokumentů definované AFIP.
**Partner form**. Informace je pro většinu transakcí zásadní. Jsou šest
:guilabel:`Typy identifikace“ k dispozici výchozími hodnotami, stejně jako 32 neaktivních typů.

.. obrázek: argentinská identifikační karta
:align:center
:alt: Seznam typů dokumentů pro místní účetnictví v Odoo definovaných AFIP.

.. poznámka::
Kompletní seznam identifikačních typů definovaných AFIP je v Odoo.
Ale aktivní jsou jen ty běžné.

Odpovědnost typu AFIP
************************

V Argentině je dokument typu a příslušných transakcích spojených s klienty.
Dodavatelé jsou definováni typem odpovědnosti AFIP. Tento údaj by měl být uveden v poli **Partner
forma**.

.. obrázek:argentina/select-afip-responsibility-type.png
:align:center
:alt:Vyberte typ odpovědnosti AFIP.

Daně
~~~~~

Jako součást lokální části modulu jsou daně vytvářeny automaticky s jejich příslušnými
účetní a konfigurační údaje, například 73 daní pro:guilabel:Responsable Inscripto“.

.. obrázek:argentina/automaticka-konfigurace-dane.png
:align:center
:alt: Seznam místních daní z oblasti AR s finanční částkou a konfigurací v Odoo.

Druhy daní
***********

Argentina má několik druhů daní, nejčastější jsou:

- :guilabel:`DPH“: jedná se o běžnou DPH, jejíž procenta mohou být různá.
- :guilabel:„Zákazník“: předplatba daně, která se vztahuje na faktury
- :guilabel:`Zadržení“: předběžná platba daně, která se vztahuje na platby.

Speciální daně
*************

Některé argentinské daně nejsou běžně používané pro všechny společnosti a ty méně časté možnosti
je v Odoo označena jako neaktivní výchozí hodnotou. Před tvorbou nové daně se ujistěte, že daná daň
nebyly již zahrnuty jako neaktivní.

.. obrázek:argentina/special-inactive-taxes.png
:align:center
:alt: Seznam méně častých argentinských daňových možností, které jsou označeny jako neaktivní v Odoo
výchozí hodnotou.

..._druhy dokumentů:

Druhy dokumentů
~~~~~~~~~~~~~~

V některých latinskoamerických zemích, jako je například Argentina, jsou účetní transakce, jako faktury a
Faktury dodavatelů jsou zařazeny do typů dokumentů definovaných daňovými orgány státní správy.
Argentina, AFIP <https://www.afip.gob.ar/>__ je vládní daňovou autoritou
definuje takové transakce.

Dokumentový typ je klíčová informace, která by měla být jasně zobrazena
vytisknuté zprávy, faktury a záznamy v účetních knihách, které uvádějí pohyby na účtech.

Každý dokumentový typ může mít jedinečnou sekvenci pro každé časopisy, kde je přiřazen.
lokalizaci dokumentu, který zahrnuje typ dokumentu a zemi, pro kterou je dokument platný.
je vytvořen automaticky při instalaci modulu pro lokalizaci.

Informace potřebná pro typy dokumentů je zahrnuta automaticky, takže uživatel
na této stránce nemusíte nic vyplňovat:

.. obrázek:argentina/default-document-type-info.png
:align:center
:alt: Seznam dokumentů v Odoo.

.. poznámka::
Existuje několik typů dokumentů, které jsou vypnuté výchozí hodnotou, ale mohou být zapnuty.
aktivovány, pokud je potřeba.

Dopisy
*******

Pro Argentinu patří do kategorie „Dokumenty“ dopis, který pomáhá určit typ
transakce nebo operace. Například když se faktura vztahuje na:

- :guilabel:'Transakce B2B', musí být použit typ dokumentu :guilabel:'A'.
- :guilabel:'Transakce B2C', musí být použit typ dokumentu :guilabel:'B'.
- :guilabel:`Exportní transakce“, musí být použita dokumentová třída :guilabel:`E“.

Dokumenty již vložené do lokalizace mají správný písmeno přiřazené k každému.
:guilabel:`Typ dokumentu“, takže další konfigurace není nutná.

.. obrázek:argentina/dokumenty-seřazené-podle-abecedy.png
:align:center
:alt: dokumenty seřazené podle písmen.

Použití na fakturách
***************

Typ dokumentu na každé transakci bude určen následujícím způsobem:

- Účetní záznam související s fakturou (pokud účetní kniha používá dokumenty).
- Podmínky se aplikují podle typu emitenta a příjemce (např. typ daňového režimu
kupující a druh daňového režimu prodávajícího.

Časopisy
--------

V argentinské lokalizaci může mít časopis různý přístup v závislosti na jeho použití
a vnitřní typ. Pro konfiguraci účetních deníků přejděte na: „Účetnictví --> Konfigurace -->
Časopisy.

Pro prodejní a nákupní deník je možné aktivovat volbu „Používat dokumenty“.
který umožňuje seznam „Dokumentů“ (viz guilabel:Document Types), ke kterým lze přiřadit faktury a dodavatele.
fakturám. Pro podrobnější informace o fakturách se prosím obraťte na část :ref:`2.3 dokumenty
<druhy dokumentů>.

Pokud se v prodejních nebo nákupních denících neaktivuje možnost „Používat dokumenty“,
nebudou moci vystavovat faktury, což znamená, že jejich použití bude omezené na
monitorování pohybů na účtech souvisejících s interními kontrolními procesy.

Informace z AFIPu (dále jen AFIP PoS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Značka „AFIP POS Systém“ je viditelná pouze v případě, že se jedná o záznamy z knihy prodejů.
druh AFIP POS, který bude použit k řízení transakcí, pro které je deník vytvářen.

AFIP definuje následující:

#. sekvence dokumentů typu souvisejících s webovou službou;
#struktura a obsah elektronické faktury.

.. obrázek:argentina/sales-journal.png
:align:center
:alt: Položka v systému AFIP, která je k dispozici na prodejních fakturách v Odoo.

Webové služby
************

Služby na webu pomáhají vytvářet faktury pro různé účely. Níže jsou uvedeny některé z možností, které můžete vybrat


- :guilabel:`wsfev1: Elektronická faktura“ je nejběžnější služba, která se používá k vytvoření
faktury za dokumenty typu A, B, C, M bez podrobností na položku.
- :guilabel:`wsbfev1: Elektronická fiskální doložka`: je pro ty, kteří vystavují daňové doklady za kapitálové zboží a chtějí
mohou využít výhod elektronických daňových dluhopisů, které jim poskytne Ministerstvo průmyslu a obchodu.
podrobnosti najdete na: „Dluhopisy

- :guilabel:`wsfexv1: Elektronická vývozní faktura“: slouží k vytváření faktur pro
mezinárodní zákazníky a transakce s vývozem, dokumenty tohoto typu
V případě typu „E“ je toto spojení.

.. obrázek:argentina/web-services.png
:align:center
:alt:Webové služby.

Níže jsou uvedeny některé užitečné informace, které je třeba znát při práci s webovými službami:

- :guilabel:`Číslo označující operace v AFIP“: je číslo, které je v AFIP konfigurováno k identifikaci operací
vztahující se k tomuto AFIP POS;
- :guilabel:`AFIP POS Address“: je pole, které se týká komerční adresy registrované pro
POS, což je obvykle stejná adresa jako u společnosti. Například pokud má firma více
obchodů (daňových míst) pak bude po společnosti vyžadovat jedno zařízení AFIP POS na
místo. Toto místo bude tisknuto v daňovém dokladu;
- :guilabel:`Sjednocená kniha“: když je systém POS v AFIPu Preimpresa, pak dokumenty
Jestliže se v časopise objeví stejná písmena, budou mít stejnou sekvenci. Například:

  - Faktura: FA-A 0001-00000002
  - Kreditní poznámka: NC-A 0001-00000003
  - Debetní poznámka: ND-A 0001-00000004.

Sekvencery
~~~~~~~~~

Pro první fakturu automaticky synchronizuje Odoo s AFIP a zobrazí poslední řadu
použité.

.. poznámka::
Při vytváření záznamů o nákupu je možné definovat, zda se jedná o související záznamy.
dokumenty nebo ne. V případě, že by byla vybrána možnost použití dokumentů, byly by
není potřeba ručně spojovat dokumentové typy, protože je k dispozici číslo dokumentu
od dodavatele.

Použití a testování
=================

Faktura
-------

Informace níže se týká vytváření faktur po vytvoření partnerů a knih.
správně konfigurované.

Přiřazení typu dokumentu
~~~~~~~~~~~~~~~~~~~~~~~~~

Když je vybrán partner, pole „Druh dokumentu“ se zaplní automaticky
podle typu dokumentu AFIP:

- Faktura pro zákazníka s identifikačním číslem Iva Responsable Inscripto, předčíslím A je typ dokumentu, který ukazuje
vše v podrobnostech spolu s informacemi o zákazníkovi.

.... obrázek:argentina/přidat-fakturu-pro-zákazníka.png
:alt:Faktura pro zákazníka Iva Responsable Inscripto, předčíslí A.

- Faktura pro konečného spotřebitele s předčíslím B je typ dokumentu, který neobsahuje DPH.
Protože daně jsou již započítány v celkové částce.

.... obrázek:argentina/předpona-faktury-pro-konečného zákazníka.png
:alt:Faktura pro konečného zákazníka, předčíslí B.

- „Exportní faktura s předčíslím E“ je typ dokumentu používaný při vývozu zboží, který ukazuje
Incoterms.

.... obrázek:argentina/prefix-e-exportni-faktura.png
:alt:Exportní faktura, předčíslí E

I když některé faktury používají stejný účet, předpona a pořadí jsou dány
Pole „Dokument“.

Nejčastěji používané :guilabel:`Dokumentní typy` budou definovány automaticky pro různé
kombinace typu odpovědnosti AFIP, ale může být aktualizována ručně uživatelem před
Potvrzení faktury.

Elektronické fakturační prvky
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Při používání elektronické faktury se v případě správnosti všech údajů faktura odešle do
standardní způsob, pokud není chyba, která je třeba vyřešit. Když se objeví hlášky o chybě,
označit oba problémy spolu s navrženým řešením. Pokud chyba přetrvává
Faktura zůstává v režimu návrhu, dokud nebude vyřešena.

Jakmile je faktura zveřejněna, zobrazí se informace týkající se ověření a stavu AFIP.
v záložce AFIP včetně:

- :guilabel:`AFIP Autorisation“: CAE číslo
- :guilabel:`Datum splatnosti“: termín pro doručení faktury zákazníkům (obvykle 10 dní
při generování CAE (později).
- :guilabel:`Výsledek:“ ukazuje, zda je faktura „Přijatá v AFIP“.
:guilabel:`Přijato s výhradami“.

.. obrázek::argentina/afip-status.png
:align:center
:alt:Stav AFIP.

Daň z přijaté faktury
~~~~~~~~~~~~~

Podle typu odpovědnosti AFIP se může platit DPH na PDF jinak.
reportáž:

- :guilabel:`Daň zahrnuta“: v tomto případě musí být daň zahrnutá do ceny výrobku
reportu, pokud má zákazník následující typ odpovědnosti za AFIP
**Zodpovědný za přijetí přihlášky**

..... obrázek::argentina/dane-vylouceny.png
:alt: Daň zahrnuta.

- :guilabel:`Součástí daně z přidané hodnoty“: tento nápis znamená, že daň z přidané hodnoty je součástí
cena produktu, celková částka a součet. Tato podmínka se vztahuje na případ, kdy zákazník má následující
AFIP odpovědné typy:

  - IVA Subjekt osvobozený
  - Konečný spotřebitel
  - Zodpovědný za jednotný daňový systém
  - IVA osvobozeno.

.... obrázek:argentina/dane-v-cene.png
:synchronizace: střed
:alt: Daň je zahrnuta v ceně.

Speciální případy použití
~~~~~~~~~~~~~~~~~

Faktury za služby
*********************

Pro elektronické faktury, které obsahují služby, požaduje AFIP zprávu o službě.
datum zahájení a ukončení, tuto informaci lze vyplnit v záložce „Další info“.

.. obrázek:argentina/faktury-za-sluzby.png
:align:center
:alt:Faktury za služby.

Pokud nejsou data vybrána ručně před platnou fakturou, hodnoty budou automaticky vyplněny.
automaticky s prvním a posledním dnem měsíce faktury.

.. obrázek:argentina/sluzby-datumy.png
:align:center
:alt: Datum služby.

Exportní faktury
********************

Faktury související s exportními transakcemi vyžadují, aby účetní používali AFIP POS.
Systém Expo Voucher – Web Service, aby se s dokumenty mohly spárovat správné typy.

.. obrázek:argentina/expedicni-zpravodaj.png
:align:center
:alt: Výzkumná zpráva.

Když je v faktuře vybrán zákazník s typem odpovědnosti AFIP
„Zahraniční klient/dodavatel“ – „Zákon č. 19.640“, Odoo automaticky
přiděluje:

- Časopis související s exportem webových služeb.
- Druh exportního dokumentu
- Fiskální pozice: Nákupy a prodeje v zahraničí
- Koncept AFIP: Zboží/Definice vývozu zboží.
- Daň z přidané hodnoty osvobozena.

.. obrázek: exportní faktura.png
:align:center
:alt:Plnění polí faktury v Odoo.

.. poznámka::
Exportní dokumenty vyžadují zapnuté a nakonfigurované Incoterms, které lze nalézt v
:menu_vyber:"Další informace - Účetnictví".

.. obrázek:argentina/exportni-faktura-incoterm.png
:align:center
:alt:Exportní faktura - Incoterm.

Fiskální dluhopisy
***********

Klasický fiskální účet je určen pro ty, kteří vystavují faktury za zboží a chtějí
přístup k dani z přidané hodnoty, která je poskytnuta Ministerstvem průmyslu a obchodu.

Pro tyto transakce je důležité zvážit následující požadavky:

- Měna (dle parametrů tabulky) a cenová nabídka.
- Daně
- Zóna
- Popište každý kus.

  - Kód podle společného názvosloví MERCOSURu (NCM)
  - Úplná specifikace
  - Jednotková cena bez DPH.
  - Množství
  - Jednotka měření
  - Bonus
  - Sazba DPH.

Elektronická faktura Mipymes (FCE)
**************************************

Pro faktury malých a středních podniků existuje několik dokumentových typů, které jsou klasifikovány jako **MiPyME**, což znamená
také známý jako elektronický daňový doklad (nebo FCE ve španělštině). Tato klasifikace rozvíjí
mechanismus zlepšující podmínky financování malých a středních firem a umožňující
jejich produktivitu zvýšit prostřednictvím brzkého vybírání plateb a pohledávek vydaných
jejich klientům a dodavatelům.

Pro tento typ transakcí je důležité zvážit následující požadavky:

- konkrétní typy dokumentů (201, 202, 206 atd.);
- vydavatel musí být způsobilý k transakcím podle programu Mipymes.
- částka by měla být větší než 100 000 ARS.
- Pokud účet typu CBU není přiřazen emitentovi, nelze doklad ověřit.
s chybovou hláškou, například takovouto.

.. obrázek:argentina/bankovni-ucet-vztah-chyba.png
:align:center
:alt: Chyba vztahu k účtu.

Pro nastavení režimu přenosu se přihlaste do nastavení a vyberte buďto
:guilabel:`ADC“.

.. obrázek:argentina/režim přenosu.png
:align:center
:alt: Režim přenosu.

Chcete-li změnit režim přenosu pro konkrétní fakturu, přejděte na záložku „Další informace“.
tab a změňte ji před potvrzením.

.. poznámka::
Přepnutí režimu přenosu nezmění zvolený režim.
:guilabel:`Nastavení“.

.. obrázek:argentina/transmission-mode-on-invoice.png
:align:center
:alt:Režim přenosu na faktuře.

Při vytváření poznámky Credit/Debit související s dokumentem FCE:

- použít tlačítka „Poznámka k úhradě“ a „Poznámka k dluhu“, takže všechna data z faktury jsou
přenesena do nového pole „Poznámka k účtu“.
- dokument dopisu by měl být stejný jako dokument původce (A nebo B).
- Použít musí být stejná měna, jako je uvedena v originálním dokumentu.
rozdíl v kurzu, pokud je kurz měny jiný mezi dnem emise a datem splatnosti
datum. Je možné vytvořit poznámku k úhradě, která umožňuje snížit nebo zvýšit částku k zaplacení v ARS.

.. obrázek:argentina/kreditni-a-debetni-tlacitko.png
:align:center
:alt:Tlačítka pro úvěrové a debetní poznámky.

Když vytváříme „Dodací list“, můžeme mít dvě situace:

#FCE je odmítnuto, takže pole „Kreditní poznámka“ by mělo obsahovat pole „FCE, je
Zrušení?` jako *Pravda*; nebo
#. Kreditní poznámka je vytvořena k zrušení dokladu FCE, tedy pole
:guilabel:"FCE, je zrušeno?" musí být prázdné (pravda).

.. obrázek: argentinaproti.png
:align:center
:alt:FCE: Zrušení?

.._argentině/faktura-vytisknutá-zpráva:

Tisková zpráva
~~~~~~~~~~~~~~~~~~~~~~

Vztahující se k elektronickým fakturám, které byly ověřeny AFIP
obsahuje čárový kód na spodní straně formátu, který reprezentuje číslo CAE. Datum vypršení platnosti
Je také zobrazen, neboť je to zákonná povinnost.

.. obrázek:argentina/faktura-vytištěná-zpráva.png
:align:center
:alt:Tisková sestava faktury.

Řešení problémů a audit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pro účely kontroly a vyhledávání chyb lze získat podrobné informace o
číslo faktury, které bylo již dříve zasláno do AFIP.
Vývojářský režim („Vývojářský režim“), pak přejděte do nabídky „Účetnictví“ a klikněte na
tlačítko „Kontrola faktury“ v AFIPu.

.. obrázek:argentina/zadat-fakturu-v-afip.png
:align:center
:alt: Konzultujte fakturu v AFIP.

.. obrázek:argentina/faktura-v-afip-podrobnosti.png
:align:center
:alt: Podrobnosti faktury konzultovány v AFIP.

Je také možné získat poslední použitou číslici v AFIP pro konkrétní typ dokumentu a POS.
Číslo jako referenční údaj pro případné problémy s sekvencemi synchronizace mezi Odoo a
AFIP.

.. obrázek:argentina/consult-last-invoice-number.png
:align:center
:alt:Kontrolujte poslední číslo faktury.

Faktury dodavatelů
------------

Na základě vybraného nákupního deníku je pro fakturu dodavatele nově nastaven
požadované pole. Tato hodnota se automaticky vyplní podle typu odpovědnosti emitenta AFIP a
Klient, hodnota se ale může měnit podle potřeby.

.. obrázek:argentina/zmena-typ-dokumentu-noviny.png
:align:center
:alt: Změna typu periodika a dokumentu.

Pole „Číslo dokumentu“ je nutné zaregistrovat ručně a formát bude
ověřen automaticky. V případě neplatného formátu se zobrazí chyba uživatele
Uvádí správný formát, který je očekávaný.

.. obrázek:argentina/faktura-dodavatele-číslo-dokumentu.png
:align:center
:alt:Číslo faktury dodavatele.

Číslo faktury dodavatele je strukturováno stejně jako čísla faktur odběratele, s tím rozdílem, že
Sled dokumentů je zadán uživatelem následujícím způsobem: *Dokumentní prefix - písmeno -
Číslo dokumentu*.

Zkontrolovat číslo faktury dodavatele v AFIP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Většina společností má vlastní kontrolu, aby se ujistila, že faktura dodavatele souvisí s platnou fiskální normou.
dokumentu lze nastavit automatickou validaci v položce „Účetnictví“ - „Nastavení“ -
Argentinská lokalizace --> Zkontrolovat dokument v AFIP, přihlížející k následujícím úrovním:

- :guilabel:`Není k dispozici“; ověření nebylo provedeno (je to výchozí hodnota).
- :guilabel:`K dispozici:“ ověření je hotové. Pokud číslo není platné, zobrazí se
přesto umožňuje zaslat dodavateli fakturu.
- :guilabel:`Povinné:“ ověření je provedeno a neumožňuje uživateli vkládat dodavatele
účet, pokud je číslo dokumentu neplatné.

.. obrázek::argentina/verify-vendor-bills.png
:align:center
:alt:Zkontrolovat platnost faktur dodavatele v AFIP.

Zkontrolovat faktury dodavatelů v Odoo
*****************************

Při zapnutých nastaveních ověřování dodavatelů se na fakturách od dodavatele zobrazí nová tlačítka.
Odoo, označené jako „Zkontrolovat na AFIP“, které se nachází vedle „AFIP
Pole „autorizační kód“.

.. obrázek:argentina/verify-on-afip.png
:align:center
:alt: Zkontrolovat na AFIP.

V případě, že faktura dodavatele nelze ověřit v AFIP, bude hodnota :guilabel:`Zamítnuto`.
zobrazené na přístrojové desce a podrobnosti o zrušení budou doplněny do chatu.

.. obrázek:argentina/afip-auth-rejected.png
:align:center
:alt: Autorizace AFIP byla zamítnuta.

Speciální případy použití
~~~~~~~~~~~~~~~~~

Nezdaněné koncepty
****************

Existují některé transakce, které zahrnují položky, které nejsou součástí základu DPH, jako např.
účet za palivo a benzín.

Faktura od dodavatele bude evidována jedním položkovým dokladem za každý produkt, který je součástí DPH
částku a další položku k registraci výše osvobozeného konceptu.

.. obrázek:argentina/vat-exempt.png
:align:center
:alt: bez DPH.

Daň z vnímání
****************

Faktura od dodavatele bude evidována jedním položkovým dokladem za každý produkt, který je součástí DPH
sazba a daň z přijmu lze připočítat v jakémkoliv produktovém řetězci. Výsledkem je
Jedna daňová skupina pro DPH a druhá pro vnímání. Výchozí hodnota pro vnímání je
:guilabel:`0.10“.

Pro úpravu DPH a nastavení správné částky použijte ikonu „Tužka“
Ta je vedle položky „Vnímání“ a po jejím nastavení
Pak lze fakturu ověřit.

.. obrázek:argentina/enter-perception-amount.png
:align:center
:alt: Zadejte částku vnímání.

... _l10n_ar/platba-srážek:

Zadržování vedení
----------------------

Argentinský daňový modul již obsahuje potřebné srážky
záznamy, které lze zobrazit při procházení menu: „Účetní aplikace“ --> Konfigurace -->
Daň z přidané hodnoty a odstranění výchozího filtru „Prodej nebo nákup“.
Modul „Srážky ze mzdy“ („l10n_ar_withholding“) musí být nainstalován.
<generální/instalace>:

Journalové záznamy nejsou vytvářeny při zadávání plateb, pokud není vyřešená položka
Pro tuto funkci je nutné vytvořit účetní položku / bankovní účet / zůstatek.
důležité ověřit, že všechny platební metody v bankovních knihách mají nevyřízenou platbu.
a účet příjmu.

.. obrázek:argentina/l10n-ar-outstanding-payments.png
:alt: Musí být nastaven účet pro neuhrazené platby.

Tato konfigurace je pro správnou evidenci srážkových transakcí se zákazníky zásadní.
a dodavatelé.

.. poznámka::
V Argentině představují srážky zrušení konkrétní části celkového dluhu.
způsobené dluhem vůči dodavateli nebo snížením celkové částky, kterou je třeba vybrat od zákazníka.
Proto lze k jedné nebo více platbám přiřadit jeden či více srážek z daní.

Konfigurace
~~~~~~~~~~~~~

Odoo již vytváří většinu potřebných srážek ze mzdy uvnitř modulu „Dani“.
menu je v některých případech nutné aplikovat nebo upravit určité konfigurace, aby se správně
vypočítat srážkovou daň z platby dodavatelům. Následující typy srážek jsou k dispozici:

- :ref:`Zisky a srážkové daně <l10n_ar/earnings-withholdings>`
- :ref:`Výdělek <l10n_ar/earnings-scale-withholdings>`
- :ref:`IIBB Celkový výběr daně <l10n_ar/iib-total-amount-withholdings>`
- :ref:`IIBB nezdanitelné příjmy <l10n_ar/iib-non-taxable-income>`

... _l10n_ar/odvod-ze-mzdy

Zisk
********

Pro srážky ze mzdy je v Odoo již připravena evidence pro každou skupinu daňového režimu,
s uvedením názvu daně a kódu AFIP.

Každý z těchto záznamů je připraven k použití. Je dobrým zvykem, aby konfigurace byla dvojnásobná
Zkontrolovali, zda je konfigurace aktualizována a správně aplikována. Vyžaduje se ověření těchto polí:

- :guilabel:`Částka“: To je procento z celkové částky, která byla sražena.
- :guilabel:`Příjem nepodléhající zdanění“: Do této částky se srážková daň neuplatní.
- :guilabel:`Minimální srážková daň“: Pokud je vypočítaná částka sražené daně menší než tato hodnota
celková částka srážkové daně je nastavena na hodnotu 0,0.
- :guilabel:„Číslo srážkové daně“: Tento prvek pomáhá automatizovat získávání čísla srážkové daně.
pod platbou. Pokud je pole nevyplněné, číslo se ručně vybere při přidávání
zadržení platby.

.. obrázek:argentina/l10n-ar-earnings.png
:alt: Druh srážkové daně.

... _l10n_ar/earnings-scale-withholdings:

Výdělečný model
**************

V tomto případě procento nepotřebujete nastavit. Namísto toho je
vypočítané na základě hodnoty pole :guilabel:`Scale`.

Pro zobrazení, úpravu nebo vytvoření nových měřítek přejděte na: `Accounting app --> Configuration
--> Skalární výdělek“. Výchozí argentinská lokalizace je přednastavena dvěma hlavními měrnými systémy.
Skály by však měly být vytvářeny a aktualizovány podle potřeby dané společnosti.

.. poznámka::
Ziskové stupnice jsou kumulativní, což znamená, že Odoo sleduje různé záznamy.
Vytvořený pro fakturu, který automaticky vypočítá správnou částku srážkové daně.

... _l10n_ar/iiB_total_withholding:

IIBB Celková částka
*****************

V tomto případě je nutné vytvořit potřebná data související s aplikovatelnou provincií.
Zadržovaná částka se vypočítává na základě procenta, které je nastaveno v poli „Částka“ daňového přiznání.
konfigurace. Od doby, kdy Odoo automaticky nesynchronizuje procenta aplikovaná na každou
provincie, tato informace musí být ručně aktualizována.

V tomto případě je doporučeno vždy duplikovat a používat různé konfigurace
každý záznam chránit jakékoli technické konfigurace, které umožňují správné výpočty a
evidence srážkové daně.

... _l10n_ar/iib-non-tax-withholding:

IIBB Není zdaněno
************

Konfigurace srážek z nezdanitelné části základu daně je velmi podobná jako u srážky ze základu daně celkového.
srážková daň <l10n_ar/iib-total-withholdings>, tak procento :guilabel:`Sazba srážkové daně“ v
Každá z těchto záznamů musí být udržována. Odoo je však přednastaven s několika záznamy
které se vztahují na různé provincie. Rozdíl je ten, že není nutné
zavést nezdanitelnou částku nebo minimální srážkovou daň pro tento typ záznamu.

Partner, který se odmítá oženit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Jakmile je správná konfigurace nastavena pro každé možné srážkové daně pro partnery, aplikovatelná
Srážky musí být přiřazeny každému kontaktu. Pro otevření aplikace Kontakty klikněte na tlačítko
Vyberte požadovaného partnera. V záložce Účetnictví najděte položku Nákup
Tabulka srážek.

Použitím dalších políček „Od“ a „Do“ lze určit, kdy je daný
Výběry mohou být automatizovány přes různé období. V poli „ref“ je uveden
umožňuje přiřadit k každé srážce z příjmu interní kontrolní číslo, které je pouze pro vnitřní potřebu.
odkazu, takže se neprojeví na žádných transakcích a není vidět v nich.
je přístupný z nabídky „Nastavení“ (ikona „Nastavení“).

- :guilabel:`Od data“: začátek datového rozsahu srážkové daně.
- :guilabel:`Datum k dnešnímu dni“: datum konce termínu srážkové daně.
- :guilabel:'ref': Použijte interní kontrolní číslo pro každý řádek srážky, který je viditelný
Pro vnitřní odkaz a neovlivňuje žádné transakce.

Automatické výpočty a odvod srážkové daně z každého platby
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Při aplikaci nových plateb na faktury dodavatelů automaticky aplikuje a vypočítává správné
Zadržení částky na úhradu. V závislosti na konfiguraci záznamu může být nutné použít
číslo odkazu pro každou srážkovou linii.

Můžete přidat další srážky nebo upravit vypočítané srážky, pokud je to nutné.

.. obrázek:argentina/l10n-ar-payment.png
:alt:Platba srážkovou daní.

.. důležité::
Celková částka dluhu k proplacení je celkovou částkou splatné. Nicméně v případě Odoo
Stále zachycuje celkovou částku, tedy částku k vyrovnání s bankou, která bude
Jedná se o částku, která je vyjádřením zaplacené částky po provedení srážky.

.. obrázek::argentina/l10n-ar-payment-registered.png
:alt:Záznam o provedené platbě.

Kontrola řízení
----------------

Pro instalaci modulu *Třetí strany a odložené/elektronické kontroly* přejděte na
Vyberte položku „Aplikace“ a vyhledejte modul pod technickým názvem „l10n_latam_check“ a klikněte
tlačítko „Aktivovat“.

.. obrázek:argentina/l10n-latam-check-module.png
:align:center
:alt: modul l10n_latam_check.

Tento modul umožňuje požadovanou konfiguraci pro účetní knihy a platby:

- Vytvářejte, spravujte a kontrolujte různé typy šeků
- Optimalizujte řízení vlastních kontrol a třetích stran.
- Mějte snadný a efektivní způsob správy dat expirace vlastních i třetích stran

Jakmile jsou všechny konfigurace pro elektronické faktury v Argentině hotové, je také potřeba
pro dokončení konfigurací pro vlastní kontroly a třetí strany.

Vlastní kontroly
~~~~~~~~~~

Konfigurujte účetní knihu, která se používá k vytvoření vlastních šeků, přejděte na:
Konfigurace --> Záznamy“, vybrat bankovní záznam a otevřít „Odeslané“
Karta plateb.

- V nabídce „Zkontrolovat“ by měla být možnost „Způsob platby“. Pokud ne, klikněte

- Zapněte nastavení „Používat elektronické a odložené kontroly“.

.. poznámka::
Tato poslední konfigurace **vypne tisk**, ale umožňuje:

   - Zadávejte čísla šeků ručně
   - Přidá pole pro určení data splatnosti šeku

.. obrázek:argentina/bankovni-zpravodaj.png
:align:center
:alt: Konfigurace bankovních časopisů.

Správa vlastních kontrol
************************

Vlastní kontrola může být vytvořena přímo z faktury dodavatele. Pro tento proces klikněte na
tlačítko „Registrace platby“.

V okně registrace platby vyberte bankovní deník z něhož má být platba provedena.
Nastavte pole „Datum vkladu“ a „Částka“.

.. obrázek:argentina/payment-popup-vendorbill.png
:align:center
:alt:Pop-up okno pro platbu s vlastními možnostmi kontroly.

.. poznámka::
Pro správu současných kontrol musí být pole „Datum vložení šeku“ buď prázdné nebo vyplněné.
v současné datum. Pro správu odložených kontrol musí být nastaveno datum vstupu do systému (guilabel: Check Cash-In Date).
je zasazen do budoucnosti.

Pro správu stávajících vlastních kontrol přejděte na: „Účetnictví“ → „Dodavatelé“ → „Vlastní“.
Zkontrolovat. Toto okno zobrazuje kritické informace, jako například datum splatnosti šeků a
celkový počet šeků a celková částka zaplacená šeky.

.. obrázek:argentina/checks-menu-vendorbill.png
:align:center
:alt: Vlastní kontrola umístění menu.

Je důležité zdůraznit, že seznam je předfiltrován kontrolami, které jsou stále *nevyřešené*.
Bankovní výpis, který ještě nebyl stržen z účtu.
:guilabel:`Je spárováno s výpisem z bankovního účtu“ pole. Chcete-li vidět všechny své vlastní šeky
odstranit filtr „Nebankovní úvěr“ kliknutím na tlačítko „X“.

.. obrázek: argentinacheck-menu-list-vendorbill.png
:align:center
:alt: Vlastní filtrování a organizace nabídky.

Zrušit vlastní kontrolu
*******************

Zrušit vlastní kontrolu vytvořenou v Odoo, přejděte na:
Zkontrolujte a vyberte šek, který chcete zrušit, pak klikněte na tlačítko „Void Check“.
rozbije smír s fakturami dodavatelů a výpisy z účtu, nechá v
**zrušený stát**.

.. obrázek:argentina/prázdný_tlačítko.png
:align:center
:alt: Prázdný tlačítko pro zrušení vlastních kontrol

Kontroly třetích stran
~~~~~~~~~~~~~~~~~~

Pro registraci plateb pomocí šeků třetích stran je nutné dva konkrétní deníky nakonfigurovat.
Pro toto nastavení přejděte na: „Účetnictví“ -> „Konfigurace“ -> „Deníky“. Poté vytvořte dvě nová
časopisy:

- „Kontroly třetích stran“
- „Zrušené třetí strany“

.. poznámka::
Můžete ručně vytvořit další knihy, pokud máte více prodejních míst a potřebujete knihy pro každé z nich.
oni.

Pro vytvoření časopisu „Třetí strana“ klikněte na tlačítko „Nový“ a nakonfigurujte
následující:

- Do pole „Název časopisu“ zadejte „Třetí strana“.
- Vyberte „Hotovost“ jako typ
- V záložce „Účetní knihy“ nastavte položku „Hotovostní účet“ na „Šek 1.1.1.02.010“.
Vložte své vlastní „Krátký kód“ do políčka „Terceros“, vyberte si měnu.

.. obrázek:argentina/auto-cash-account.png
:align:center
:alt:Automaticky vytvořený účet kasu.

Přístupné platební metody jsou uvedeny v záložce *Platby*:

- Pro nové příchozí platby přejděte na záložku „Příchozí platby“ – „Přidat řádek“.
a vyberte možnost „Nové kontroly třetích stran“. Tento způsob se používá k vytvoření nových kontrol třetích stran.
kontrolách.
- Pro příchozí a odchozí platby existující třetí strany přejděte na záložku „Příchozí platby“.
--> Přidejte řádek a vyberte: guilabel:Existující třetí strany kontroly. Opakujte stejný krok pro
:guilabel:`Výstupní platby“ záložce. Tento způsob se používá k přijímání a/nebo úhradě faktur od dodavatelů.
i stávající kontroly a pro vnitrostátní převody.

.. tip::
Můžete smazat předchozí způsoby platby, které se objevují automaticky při konfiguraci třetí
kontroluje deníky.

.. obrázek: argentinská/automatické platební metody.png
:align:center
:alt:Platební metody vytvořené automaticky.

Kromě toho je také nutné vytvořit a nakonfigurovat deník *Zrušené třetí strany*.
slouží k řízení třetích stran, které byly odmítnuty, a může být použita k zaslání kontrol, které byly odmítnuty na
v okamžiku sběru nebo po návratu od dodavatelů, pokud je zboží odmítnuto.

Pro vytvoření záznamu *Zrušené třetí strany* klikněte na tlačítko „Nový“ a nakonfigurujte
Dále:

- Zadejte jako název časopisu „Odmítnuté třetí strany“
- Vyberte „Hotovost“ jako typ
- V záložce „Účetní knihy“ nastavte „Konto v hotovosti“ na „1.1.1.01.002 Odmítnutá platba“.
Třetí strana kontroluje`, zadejte libovolný kód „Krátké zprávy“ a vyberte
:guilabel:`Měna“

Použijte stejné způsoby platby jako časopis *Třetí strana*.

Nový třetí subjekt kontroly
**********************

Pro registraci nové platby třetí stranou pro fakturu zákazníka klikněte na „Registrovat platbu“.
tlačítko. V okně s nápovědou musíte vybrat „Třetí strana“ jako deník pro
registrace platby.

Vyberte možnost „Nová třetí strana“ jako „Způsob platby“ a vyplňte
:guilabel:Číslo šeku“, „Datum platby“ a „Banka šeku“. Volitelně můžete
ručně přidáte pole „Kontrola dodavatele DPH“, ale tento údaj se automaticky vyplní podle zákazníkova
Daňové identifikační číslo související s fakturou.

.. obrázek:argentina/tretí-strana-poplatku.png
:align:center
:alt:Okno s možnostmi platby s aktivovanými novými třetími stranami.

Existující třetí strany kontroly
***************************

Pro platbu faktury od dodavatele pomocí stávajícího šeku klikněte na tlačítko „Registrace platby“. V
Pokud chcete zobrazit okno s výzvou, musíte vybrat jako deník platby:guilabel:'Třetí strana'.
registrace.

Vyberte možnost „Zkontrolované třetí stranou“ jako „Metodu platby“ a vyberte šek.
z pole „Zkontrolovat“. V poli se zobrazují všechny **použitelné existující kontroly**, které lze použít jako
platba faktur dodavatelům.

.. obrázek: argentinapopup.png
:align:center
:alt:Okno pro platbu s možnostmi třetích stran, které jsou povoleny.

Při použití stávajícího třetího strany ověření můžete zkontrolovat operace související s ním.
Příkladem je například zjištění, že kontrola třetí strany provedená za účelem zaplacení faktury zákazníkovi byla později použita jako
existující třetí strana, která by mohla zaplatit fakturu dodavatele.

K tomu buď přejděte na: „Účetnictví –> Zákazníci –> Kontroly třetích stran“ nebo
V závislosti na případu vyberte položku „Účetnictví“ -> „Dodavatelé“ -> „Vlastní kontroly“ a klikněte na kontrolu.
V poli „Zkontrolovat současný deník“ klikněte na „Zkontrolovat operace“.
historii a pohyb šeku.

.. obrázek: argentinacheck-operations-menu-list.png
:align:center
:alt: Zkontrolujte nabídku operací.

Nabídka také zobrazuje kritické informace týkající se těchto operací, jako například:

- :guilabel:„Způsob platby“, který umožňuje třídit podle způsobu, jakým je platba odeslána dodavateli nebo
platba od zákazníka
- Časopis, ve kterém je nyní zapsána kontrola
- Partner spojený s operací (buď zákazník nebo dodavatel).

..._argentina/ecommerce-elektronické fakturace

Elektronické fakturace v e-commerce
------------------------------


Instalace modulu „Elektronický obchod v Argentině“ („l10n_ar_website_sale“)
umožňuje následující funkce a konfigurace:

- Zákazníci budou moci vytvářet online účty pro účely elektronického obchodování.
- Podpora požadovaných daňových polí v aplikaci elektronického obchodování.
- Přijímat platby za objednávky z internetu.
- Vytvářet elektronické dokumenty z e-commerce aplikace.

Konfigurace
~~~~~~~~~~~~~

Jakmile jsou všechny konfigurace pro argentinský elektronický fakturu
„Přizpůsobení vaší společnosti“ (<argentina/configure-your-company>), je nutné také provést některé konfigurace.
integrovat elektronický obchodní tok.

Registrace klientského účtu
***************************

Pro konfiguraci webu pro účty klientů postupujte podle pokynů v dokumentaci „checkout
Dokumentaci k nákupu na webu.

Automatická faktura
*****************

Nastavte svůj web, aby generoval elektronické dokumenty v prodejním procesu, kliknutím na
„Webová stránka“ -> „Konfigurace“ -> „Nastavení“ a aktivací „Automatické
V sekci „Fakturace“ v části „Fakturace“ lze automaticky vygenerovat požadované
elektronické dokumenty po potvrzení online platby.

.. obrázek:argentina/l10nar-automatické-fakturace-pro-e-shopy.png
:align:center
:alt:Aktivován prvek pro automatické vystavování faktur.

Pro funkci „Automatický fakturační doklad“ je třeba potvrdit platbu online.
generovat dokument, který je nutné konfigurovat pro
související webové stránky.

Produkty
********

Chcete-li umožnit fakturaci vašich produktů po potvrzení online platby, přejděte na požadovanou
produkt z webu: „Website --> E-commerce --> Produkty“. V obecných nastaveních
V záložce „Informace“ nastavte pole „Způsob fakturace“ na „Počet objednaných kusů“ a definujte
požadovaný:guilabel:Daň z přidané hodnoty.

Fakturační tok pro elektronický obchod
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Když jsou všechny zmíněné konfigurace nastaveny, klienti mohou dokončit následující požadované
kroky v procesu elektronického obchodování v Argentině, které umožňují zadat daňové údaje během nákupního procesu.

Daňová pole jsou k dispozici v procesu placení, jakmile je vyplněno pole „Země“.
zadejte „Argentina“. Zadáním fiskálních údajů dovolíte nákupu dokončit v odpovídající
elektronický dokument.

.. obrázek::argentina/l10nar-fiscal-fields-ar-ecommerce.png
:align:center
:alt:Povinné fiskální položky pro elektronické fakturace.

Když zákazník úspěšně nakoupí a zaplatí, vytvoří se potřebný daňový doklad s
odpovídající uspořádání a fiskální razítka uvedená v zprávě o tisku faktury.
<argentinská faktura tisknutá v reportu>.

.. viz též:
:doc:`Vytvoření účtu klienta <../../websites/ecommerce/checkout>`

Prodej produktů s vysokou likviditou
------------------------------

Produktem pro přímý prodej likvidity se prodávají produkty, které zahrnují třetí stranu.
Prodávající, dodavatel a vlastník zboží se mohou registrovat na odpovídající
Prodeje a nákupy.

.. poznámka::
:ref:`Nainstalujte modul Argentinské elektronické fakturace (l10n_ar_edi)` podle návodu v části
využít tuto funkci.

Konfigurace
~~~~~~~~~~~~~

Kniha nákupů
****************

Pro vytvoření elektronické faktury od dodavatele je nutný nákupní deník s dokumentovým typem *Likvidita
Produkt* Tento časopis musí být synchronizován s AFIP, protože bude použit k vytvoření
elektronický dokument o likviditě produktu.

Pro úpravu stávajícího nákupního deníku nebo vytvoření nového přejděte na:
Konfigurace -> Účetní deníky“. Pak vyberte existující nákupní deník nebo klikněte na
Tlačítko „Nový“ a vyplňte následující požadované informace:

- :guilabel:`Typ“: vyberte „Koupit“.
- :guilabel:`Použít dokumenty“: zaškrtněte tuto políčko, abyste mohli vybrat typ elektronického dokumentu.
- :guilabel:„AFIP je POS“: zaškrtněte tuto políčko, abyste mohli vytvářet elektronické dokumenty.
- :guilabel:`AFIP POS Systém“: vyberte „Elektronická faktura – webová služba“.
vybrat z nabídky a odeslat elektronický dokument do AFIP prostřednictvím webové služby.
- :guilabel:`Číslo označující operace v AFIP“: je číslo, které je v AFIP konfigurováno k identifikaci operací
spojené s touto pozicí AFIP.
- :guilabel:`AFIP POS Address“: je pole, které se týká komerční adresy registrované pro
POS, což je obvykle stejná adresa jako u společnosti. Například pokud má firma více
obchodů (daňových míst) pak bude po společnosti vyžadovat jedno zařízení AFIP POS na
místo. Toto místo bude uvedeno v daňovém dokladu.

.. obrázek:argentina/l10n-ar-purchase-journal.png
:align:center
:alt: Konfigurace nákupního deníku

Jednací deník
*************

Pro registraci faktury je potřeba vystavit prodejní deník, pokud se zboží prodává třetí osobě.
a pak stejný produkt znovu prodávat. Tento deník se nebude synchronizovat s AFIP, protože faktura nebude
elektronická.

Pro úpravu stávajícího prodejního deníku nebo vytvoření nového se přihlaste do
„Účetnictví“ -> „Konfigurace“ -> „Deníky“. Pak vyberte prodejní deník nebo
Klikněte na tlačítko „Nový“ a vyplňte následující povinné informace:

- :guilabel:`Typ“: vyberte „Prodej“.
- :guilabel:`Použít dokumenty“: zaškrtněte pole v deníku, abyste vybrali typ elektronického dokumentu
(v tomto případě elektronická faktura).

.. obrázek:argentina/l10n-ar-sales-journal.png
:align:center
:alt: Konfigurace prodejního deníku

Fakturační tok
~~~~~~~~~~~~~~

Jakmile jsou všechny konfigurace nastaveny, bude vygenerován faktura pro dodavatele produktů likvidity.
firma prodávající produkt na jinou stranu. Například distributor
Konkrétní produkt.

Zprávy
=======

Součástí lokální instalace je finanční report pro Argentinu.
Dashboard účetnictví. Chcete-li se dostat k těmto zprávám, přejděte na :menuselection:`Účetnictví
--> Zprávy --> Výroky Argentinců.

Pro přístup k DPH knize zpráv se přihlaste do: „Účetnictví -> Zprávy -> Daňová zpráva“, klikněte
ikonou „Kniha“ (:guilabel:"Book"), a vyberte „Argentinská kniha DPH (AR)“.

.. poznámka::
Záznam o DPH lze exportovat jako soubor s příponou .zip vybráním v roletce v nabídce
v horním levém rohu.

Shrnutí DPH
-----------

Tento přehledový výstup slouží k ověření měsíčních celkových částek DPH. Tento výstup je určen pouze pro vnitřní potřebu a
nebyly zaslány do AFIP.

IIBB – Prodej podle právního řádu
----------------------------

Tato tabulka umožňuje ověřit hrubý příjem v každé jurisdikci.
přiznání k příslušným daním, které však není předloženo správci daně AFIP.

.. obrázek:argentina/iibb-sales-jurisdiction.png
:alt:Prodej podle právního řádu.

IIBB - Nákupy podle právního řádu
--------------------------------

Tato tabulka umožňuje ověřit celkové nákupy v každém státě. Slouží jako
přiznání k příslušným daním, které však není předloženo správci daně AFIP.

.. obrázek:argentina/iibb-purchases-jurisdiction.png
:alt:IIBB Nákupy podle právního řádu.
