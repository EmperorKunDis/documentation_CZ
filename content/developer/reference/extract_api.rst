===========
Extrakt API
===========

.. |IAP| nahradit za: zkratka: `IAP (In-app purchases)`
.. |OCR| nahradit za: abbr: `OCR (Optical Character Recognition)`

Odoo poskytuje službu automatizace zpracování dokumentů typu faktura, výpis z bankovního účtu
Náklady nebo životopisy.

Služba dokumenty skenuje pomocí OCR motoru a poté
Používá algoritmy založené na umělé inteligenci (AI) k extrahování polí zájmu, jako jsou
celková částka, splatnost nebo řádky faktury pro *faktury*, počáteční a konečný zůstatek, datum
*bankovní výpisy*, celkovou částku, datum pro *výdaje*, nebo jméno, e-mail a telefonní číslo pro *životopisy*.

Tato služba je zpoplatněná. Každé zpracování dokumentu vám bude odečten jeden kredit ze
digitální dokumenty |IAP| účet. Více informací o účtech IAP naleznete
:doc:`tady </aplikace/základní/v_aplikaci_nákupy>“.

Tuto službu můžete používat přímo v aplikaci pro účetnictví, výdaje nebo nábor zaměstnanců nebo prostřednictvím
API. Detailní informace o Extract API jsou uvedeny v následujícím oddílu.
služby přímo do svých vlastních projektů.


Přehled
========

Extrakt API používá protokol JSON-RPC2, jeho koncové body jsou umístěny na
„https://extrakce.apio.odoo.com“.

... _extrakce_api/verze:

Verze
-------

Specifikace verze Extract API je uvedena v trase.

Poslední verze jsou:
    - faktury: 123
    - bankovní výpisy: 100
    - Náklady: 132
    - žadatelé: 102

Proud
----

Průtok je stejný pro každý typ dokumentu.

#|Vyvolání metody:ref:`/parse <extract_api/parse>`, abyste mohli odeslat své dokumenty (každý volání pro jeden
dokumentu (v případě úspěchu obdržíte v odpovědi token pro daný dokument).
#Pak musíte pravidelně zjišťovat výsledky pomocí :ref:`/get_result <extract_api/get_result>`.
stav zpracování dokumentu.
| Nebo můžete v době volání poskytnout webovou adresu pomocí parametru webhook_url.
:ref:`/parse <extract_api/parse>` a budete informováni (pomocí požadavku na POST) o tom, kdy byla
Výsledek je připraven.

Pro všechny z nich by měl být použit metod HTTP POST. Pythonová implementace celého proudu
faktury se nacházejí: stáhnout zde <extrakce_api/implementace.py> a token pro integraci
testování je poskytováno v
:ref:`integrační testování část <latestextract_api/integration_testing>“.


Parsing
=====

Požádejte o digitalizaci dokumentu. Cesta vrátí token „dokument“, který můžete použít
Vyhledat výsledek vaší žádosti.

... _extrakce_api/parse:

Trasy
------

    - /api/extract/invoice/2/parse
    - /api/extract/bank_statement/1/parse
    - /api/extract/expense/2/parse
    - /api/extract/applicant/2/parse

Žádost
-------

.. první třídy: o definice

„jsonrpc“ (nutné)
viz JSON-RPC 2
„metoda“ (povinné)
viz JSON-RPC 2
„id“ (povinné)
viz JSON-RPC 2
„params“
... první třídy :: o definici seznamu

„token účtu“ (povinné)
Token účtu IAP:
Při každém úspěšném volání bude stržen jeden kredit.
„verze“ (povinné)
Verze určí formát vašich požadavků a formát odpovědi serveru.
Měli byste používat nejnovější verzi dostupnou na odkazu :ref:`<extract_api/version>`.
„dokumenty“ (povinné)
Dokument musí být poskytnut jako řetězec Base64 v kódování ASCII.
Seznam by měl obsahovat pouze jeden dokument. Toto pole je seznam jen kvůli zpětné kompatibilitě.
Podporované formáty jsou *.pdf, *.png a *.jpg.
„dbuuid“ (volitelné)
Jedinečný identifikátor databáze Odoo.
„webhook_url“ (volitelné)
Může být zadán odkaz na webhooka. Na webhook bude odeslána prázdná požadavek
„webhook_url/document_token“, když je výsledek připravený.
„user_infos“ (volitelné)
Informace o osobě, která dokument posílá do výpisového centra.
buď klient, nebo dodavatel (podle „pohledu“). Tato informace není
Provoz služby je bez něj možný, ale výsledek se velmi zhoršuje.

... první třídy: o definice seznamu

„user_company_vat“ (volitelné)
Daňové identifikační číslo uživatele.
„uživatelské jméno společnosti“ (volitelné)
Název uživatelské společnosti.
„uživatelské_firmy_země_kód“ (volitelné)
Kód země uživatele. Formát:
„ISO 3166 alfa-2 <https://www.iban.com/country-codes>“.
„user_lang“ (volitelné)
Jazyk uživatele. Formát: *jazykový kód + _ + lokalita* (např. fr_FR, en_US).
„user_email“ (volitelné)
E-mail uživatele.
„nákupní objednávka“
Regex pro identifikaci nákupních objednávek. Výchozí formát je požadován, pokud nebyl zadán.
„perspektiva“ (volitelné)
... první třídy :: o definici seznamu

Může být „klient“ nebo „dodavatel“. Toto pole je užitečné pouze pro faktury.
„klient“ znamená, že informace o uživateli poskytnuté jsou spojeny s klientem daného subjektu.
faktura.
„Dodavatel“ znamená, že je spojen s dodavatelem.
Pokud není k dispozici, bude použit klient.

... kódový blok::js

    {
„jsonrpc“: „2.0“,
„metoda“: „volání“,
„params“: {
„token účtu“: řetězec
„verze“: integer
„dokumenty“:[„string“]
„dbuuid“: řetězec
„webhook_url“: „string“,
"user_infos": {
„user_company_vat“: str
"název společnosti uživatele": řetězec
„uživatelská společnost země kódu“: řetězec
"user_lang": string
"uživatelské e-mailové adresy": řetězec
„purchase_order_regex“: „string“,
„perspektiva“: řetězec
            },
        },
„id“: řetězec
    }

.. poznámka::
Parametr „user_infos“ je nepovinný, ale výrazně zlepšuje kvalitu výsledku.
Výhodou je zejména pro faktury. Čím více informací můžete poskytnout, tím lépe.

Odpověď
--------

.. první třídy: o definice

„jsonrpc“
viz JSON-RPC 2
„id“
viz JSON-RPC 2
„výsledek“
... první třídy :: o definici seznamu

„stav“
Kód, který ukazuje stav požadavku. Podívejte se na tabulku níže.
„status_msg“
Stručný popis stavu požadavku.
„token dokumentu“
Pouze v případě úspěšného požadavku.

===========================  ==============================================================
stav                            stav_msg
===========================  ==============================================================
`úspěch`                         Úspěch
„chyba_nepodporovaná_verze“ Nepodporovaná verze
„interní chyba“           Došlo k interní chybě
Chyba - nedostatek kreditu
`chyba_nepodporovaný_souborový_formát`   Nepodporovaný souborový formát
`chyba_údržby`                     Server je v současné době ve fázi údržby. Zkuste prosím později znovu.
===========================  ==============================================================

... kódový blok::js

    {
„jsonrpc“: „2.0“,
„id“: řetězec
"výsledek": {
„status“: řetězec
„status_msg“: řetězec
„token dokumentu“: řetězec
        }
    }

.. poznámka::
Ve skutečnosti však API nepoužívá schéma chyb JSON-RPC, ale má své vlastní.
schéma zabalené do úspěšného výsledku JSON-RPC.

Dosáhnout výsledků
===========

... _extrakce_api/získat výsledek:

Trasy
------

    - /api/extract/invoice/2/get_result
    - /api/extract/bank_statement/1/get_result
    - /api/extract/expense/2/get_result
    - /api/extract/applicant/2/get_result

Žádost
-------

.. první třídy: o definice

„jsonrpc“ (nutné)
viz JSON-RPC 2
„metoda“ (povinné)
viz JSON-RPC 2
„id“ (povinné)
viz JSON-RPC 2
„params“
... první třídy :: o definici seznamu

„verze“ (povinné)
Verze by měla odpovídat verzi, kterou bylo předáno v požadavku na :ref:`/parse <extract_api/parse>`.
„token dokumentu“ (povinné)
Token „dokumentu“, pro který chcete získat aktuální stav analýzy.
„token účtu“ (povinné)
Token účtu |IAP|, který byl použit k odeslání dokumentu.

... kódový blok::js

    {
„jsonrpc“: „2.0“,
„metoda“: „volání“,
„params“: {
„verze“: integer
„dokumentový token“: integer
„token účtu“: řetězec
        },
„id“: řetězec
    }

Odpověď
--------

Při získávání výsledků z analýzy se detekované pole liší podle typu
dokumentu. Každá odpověď je seznam slovníků, jeden pro každý dokument. Klíče slovníku
je název pole a hodnota je hodnota pole.

.. první třídy: o definice

„jsonrpc“
viz JSON-RPC 2
„id“
viz JSON-RPC 2
„výsledek“
... první třídy :: o definici seznamu

„stav“
Kód, který ukazuje stav požadavku. Podívejte se na tabulku níže.
„status_msg“
Stručný popis stavu požadavku.
„výsledky“
Pouze v případě úspěšného požadavku.

... první třídy: o definice seznamu

„full_text_annotation“
Obsahuje neupravený celkový výsledek z OCR pro dokument.

================================  =============================================================
stav                              stav_zpráva
================================  =============================================================
„úspěch“                             „úspěch“
`chyba_nepodporovaná_verze`         Nepodporovaná verze
„interní chyba“                      Došlo k chybě
`server_v_servisu`                      Server je v současné době ve výluce, zkuste to prosím později
`chyba_dokumentu_nebyl_nalezen`     Dokument nenalezen
`chyba_nepodporovaná_velikost`         Dokument byl odmítnut, protože je příliš malý
„chyba_nepřítomnost_počtu_stránek“     Nelze získat počet stránek v PDF souboru
„Chyba při převodu PDF na obrázky“ Převod PDF na obrázky se nepodařil
„chyba_heslo_ochrana“           Soubor PDF je chráněn heslem
„chyba_příliš_mnoho_stránek“           Dokument obsahuje příliš mnoho stránek
================================  =============================================================

... kódový blok::js

    {
„jsonrpc“: „2.0“,
„id“: řetězec
"výsledek": {
„status“: řetězec
„status_msg“: řetězec
„výsledky“: [
                {
„full_text_annotation“: „string“,
"feature_1_name": feature_1_result,
"feature_2_name": feature_2_result
                    ...
                },
                ...
            ]
        }
    }

Společná pole
~~~~~~~~~~~~~

... _nejnovější extrakt API/získat výsledek/výsledky funkce:

„feature_result“
******************

Každý zájem, který chceme z dokumentu extrahovat, jako například celkovou částku nebo datum splatnosti,
také nazývané funkce. Exhaustivní seznam všech extrahovaných funkcí spojených s určitým typem
Dokument naleznete v sekcích níže.

Pro každou vlastnost se vracíme seznam kandidátů a vyznačujeme kandidáta, kterého naše modely předpovídají.
aby byl nejlepší pro danou funkci.

.. první třídy: o definice

„selected_value“ (volitelné)
Nejlepším kandidátem na tuto funkci.
„vybrané hodnoty“ (volitelně)
Nejlepší kandidáti na tuto funkci.
„kandidáti“ (volitelné)
Seznam všech kandidátů pro tuto funkci, seřazených podle sestupného skóre důvěryhodnosti.

... kódový blok::js

„název vlastnosti“:
"vybraná hodnota": kandidát_12
„kandidáti“: [kandidát 12, kandidát 3, kandidát 4, …]
   }

kandidát
*********

Každému kandidátovi přidělíme jeho zástupce a pozici v dokumentu. Kandidáti jsou seřazeni
podle sestupného pořadí vhodnosti.

.. první třídy: o definice

„obsah“
Prezentace kandidáta.
„koordinace“
... první třídy :: o definici seznamu

„[centrální x, centrální y, šířka, výška, úhel otáčení]“.
vzhledem k velikosti stránky a jsou tedy mezi 0 a 1.
Úhel je pravotočivá rotaci měřená v stupních.
„stránka“
Číslo stránky originálního dokumentu, na kterém je kandidát umístěn (začíná na 0).

... kódový blok::js

„kandidát“: [
        {
„obsah“: řetězec nebo číslo
„koordinace“: [float, float, float, float, float]
"stránka": int
        },
        ...
    ]


Faktury
~~~~~~~~

Faktury jsou složité a mohou obsahovat mnoho různých polí. Následující tabulka je kompletní
seznam všech polí, ze kterých lze z faktury extrahovat data.

+-------------------------+------------------------------------------------------------------------+
|Název funkce           | Specifika                                                                         |
+=========================+========================================================================+
|„SWIFT_code“|„Content“ je slovníkový obsah kódu, který byl převeden na řetězec.
|                         |                                                                        |
|                             |Obsahuje informace o detekovaném kódu SWIFT.
|                          |(nebo „BIC <https://www.iso9362.org/isobic/overview.html>“_.)             |
|                         |                                                                        |
|                            | Klíče:                                                                   |
|                         |                                                                        |
|...............................| ...... první třídy: o definice seznamu .....................................|
|                         |                                                                        |
|                            | „bic“
|                            |  detekovaný BIC (řetězec).                                               |
|                              | „jméno“ (volitelné)|
|                            |    název banky (řetězec).                                                   |
|                            | „kód země“
|                          |    ISO 3166 alfa-2 kód země banky (řetězec).                       |
|                            | „město“ (volitelné)|
|                             |město banky (řetězec)                                                       |
|                            | „ověřený BIC“
|                            |    Pravda, pokud byl kód BIC nalezen v naší databázi (logická hodnota).
|                         |                                                                        |
|                             |Jméno a město jsou přítomné pouze v případě, že je true verifed_bic.           |
+-------------------------+------------------------------------------------------------------------+
|„IBAN“|„Content“ je řetězec
+-------------------------+------------------------------------------------------------------------+
|„aba“|„obsah“ je řetězec
+-------------------------+------------------------------------------------------------------------+
|„DIČ“|„content“ je řetězec
|                         |                                                                        |
|V závislosti na hodnotě perspektivy v uživatelských informacích bude tento výraz|
|                              |Daňové identifikační číslo dodavatele nebo klienta. Pokud se jedná o perspektivní obchod, pak
|                            | klienta bude DPH dodavatele. Pokud je to dodavatel, pak je to jeho DPH.
|                             | daňové identifikační číslo klienta.                                          |
+-------------------------+------------------------------------------------------------------------+
|„QR faktura“              | „Content“ je řetězec
+-------------------------+------------------------------------------------------------------------+
|„platební referenční číslo“ | „obsah“ je řetězec
+-------------------------+------------------------------------------------------------------------+
|„objednávka“| „content“ je řetězec
|                         |                                                                        |
|                          |Používá „selected_values“ místo „selected_value“                       |
+-------------------------+------------------------------------------------------------------------+
|„země“|„obsah“ je řetězec
+-------------------------+------------------------------------------------------------------------+
|„měna“                   | „obsah“ je řetězec
+-------------------------+------------------------------------------------------------------------+
|„datum“               | „obsah“ je řetězec
|                         |                                                                        |
|                             |Formát: *YYYY-MM-DD*                                                       |
+-------------------------+------------------------------------------------------------------------+
|„datum splatnosti“|Součástí „datumu“
+-------------------------+------------------------------------------------------------------------+
|„celková daň“|„content“ je desetinné číslo
+-------------------------+------------------------------------------------------------------------+
|„fakturační_id“         | „obsah“ je řetězec                                                            |
+-------------------------+------------------------------------------------------------------------+
|„součet“           | „obsah“ je desetinné číslo
+-------------------------+------------------------------------------------------------------------+
|„celkem“| „obsah“ je číslo s desetinnou čárkou
+-------------------------+------------------------------------------------------------------------+
|„dodavatel“             | „obsah“ je řetězec                                                          |
+-------------------------+------------------------------------------------------------------------+
|„klient“               | „obsah“ je řetězec                                                            |
+-------------------------+------------------------------------------------------------------------+
|„e-mail“              | „obsah“ je řetězec
+-------------------------+------------------------------------------------------------------------+
|„webová stránka“|„obsah“ je řetězec
+-------------------------+------------------------------------------------------------------------+


„funkce invoice_lines“
*************************

Je vrácena jako seznam slovníků, kde každý slovník představuje řádek faktury.

... kódový blok::js

„fakturační řádky“:
        {
„popis“: řetězec
„množství“: plovoucí číslo
„celková cena“: plovoucí číslo
„celkem“: plovoucí číslo
„daně“: seznam[float]
„celkem“: plovoucí číslo
"cena_za_jednotku": float
        },
        ...
    ]

Bankovní výpisy
~~~~~~~~~~~~~~~

Následující tabulka obsahuje seznam všech polí, která jsou extrahována z výpisů z bankovního účtu.

+-------------------------+------------------------------------------------------------------------+
|Název funkce           | Specifika                                                                         |
+=========================+========================================================================+
|"balance_start""         | "content" je desetinné číslo
+-------------------------+------------------------------------------------------------------------+
|„balance_end“|„content“ je číslo ve formátu desetinného čísla
+-------------------------+------------------------------------------------------------------------+
|„datum“               | „obsah“ je řetězec
+-------------------------+------------------------------------------------------------------------+

„bankovní výpisy“
********************************

Je vrácena jako seznam slovníků, kde každý slovník představuje řádek výpisu z účtu.

... kódový blok::js

„bankovní výpisy“:
        {
„cena“:  „float“,
„popis“: řetězec
„datum“: „string“,
        },
        ...
    ]

Náklady
~~~~~~~

Náklady jsou méně komplikované než faktury. Následující tabulka obsahuje všechny
polí, která lze z výkazu o nákladech extrahovat.

+-------------------------+------------------------------------------------------------------------+
|Název funkce           | Specifika                                                                         |
+=========================+========================================================================+
|„Popis“|„Obsah“ je řetězec
+-------------------------+------------------------------------------------------------------------+
|„země“|„obsah“ je řetězec
+-------------------------+------------------------------------------------------------------------+
|„datum“               | „obsah“ je řetězec
+-------------------------+------------------------------------------------------------------------+
|„celkem“| „obsah“ je číslo s desetinnou čárkou
+-------------------------+------------------------------------------------------------------------+
|„měna“                   | „obsah“ je řetězec
+-------------------------+------------------------------------------------------------------------+

Uchazeč
~~~~~~~~~

Třetí typ dokumentu je určen pro zpracování životopisů. Následující tabulka obsahuje kompletní
seznam všech polí, ze kterých můžeme extrahovat informace z životopisu.

+-------------------------+------------------------------------------------------------------------+
|Název funkce           | Specifika                                                                         |
+=========================+========================================================================+
|název|obsah je řetězec
+-------------------------+------------------------------------------------------------------------+
|„e-mail“              | „obsah“ je řetězec
+-------------------------+------------------------------------------------------------------------+
|„telefon“| „obsah“ je řetězec
+-------------------------+------------------------------------------------------------------------+
|„mobilní“|„obsah“ je řetězec
+-------------------------+------------------------------------------------------------------------+

..._nejnovější výstup_API:

Testování integrace
===================

Můžete svou integraci otestovat tak, že použijete „*integration_token*“ jako „account_token“ v
:ref:`/parse <extract_api/parse>“ požadavku.

Použitím tohoto tokenu se dostanete do režimu testování a můžete si simulovat celý průběh bez skutečného
parsování dokumentu bez účtování jednoho kreditu za každé úspěšné **parsování dokumentu**.

Technicky je v testovacím režimu jenom rozdíl, že dokument, který odesíláte, se neparsuje.
systému a odpověď, kterou získáte.
:ref:`/get_result <extrakt_api/get_result>` je pevně nastavená.

Implementace celého proudu pro faktury v Pythonu je k dispozici
:stáhnout: zde <extrakce_api/implementace.py>.

..._JSON-RPC2: https://www.jsonrpc.org/specification

.. |ss| neupravený:: html



.. |se| neupraveným HTML


