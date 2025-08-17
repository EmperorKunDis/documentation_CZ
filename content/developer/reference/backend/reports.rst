
..zvýrazněno::xml

.. odkaz/výpisy:

.. odkaz/zprávy/zpráva:

============
QWeb Reports
============

Zprávy jsou psány v HTML/QWeb, jako webové stránky v Odoo. Můžete použít
obvyklé nástroje pro řízení toku kontrol QWeb (viz reference/qweb). Pro zobrazení PDF používá
Sama o sobě je prováděna pomocí wkhtmltopdf.

Hlášení se vyhlašují pomocí akce :ref:`report <reference/actions/report>`.
a odkaz na „referenci/zprávy/šablony“ pro akci, kterou chcete použít.

Pokud je to užitečné nebo nutné, lze specifikovat
:ref:`report/reports/paper_formats“ pro zprávu o výzkumu.

... odkaz/reporty/šablony:

Šablona hlášení
===============

Šablony reportů vždy obsahují následující proměnné:

„čas“
odkaz na modul python:time ze standardní knihovny Python
„uživatel“
„uživatel“ v záznamu „res.user“ pro uživatele, který tiskl zprávu
„res_company“
rekord pro aktuální „uživatelovu“ společnost
„webová stránka“
aktuální objekt webové stránky (toto pole může být přítomno, ale nemusí být)
„web_base_url“
URL adresa pro webový server
„context_timestamp“
funkce, která přijímá :class:`python:datetime.datetime` v UTC\ [#unzoned]_
převodem na časové pásmo uživatele, který tiskl zprávu

Minimální funkční šablona
-----------------------

Minimální šablona by mohla vypadat takto:

<šablona id="faktura-report">

<t t-foreach="dokumenty" t-as="o">

<div class="page">
<h2>Název zprávy</h2>
Toto objektu se říká <p><span t-field="o.name"/></p>

</t>

</t>


Přidání „external_layout“ zobrazí standardní hlavičku a patičku.
report. Tělo PDF bude obsahovat „<div
„“. ID šablony musí být jméno specifikované v
hlášení o výkazu; například „účet.report_faktura“ pro výše uvedený případ
report. Protože se jedná o šablonu QWeb, můžete přistupovat k všem polím
Objekty „doc“ přijaté šablonou.

Výchozí zobrazovací kontext bude také obsahovat následující položky:

„dokumenty“
záznamy pro současnou zprávu
„doc_ids“
seznam id pro „dokumenty“
„doc_model“
vzor pro záznamy „dokument“

Pokud chcete přistupovat k dalším záznamům/vzorcům v šabloně, budete potřebovat
„vlastní zpráva“ (viz. reference/reports/custom_reports), nicméně v tomto případě
Tyto věci budete muset poskytnout, pokud je potřebujete.

Překladatelné šablony
----------------------

Pokud chcete překládat zprávy (například do jazyka partnera),
Pro vytvoření dvou šablon je potřeba:

* Hlavní šablona hlášení
* Přeložitelný dokument

Poté můžete volat přeložitelný dokument z hlavního šablonu s atributem
„t-lang“ nastaven na kód jazyka (například „fr“ nebo „en_US“) nebo na pole záznamu.
Pokud používáte, budete muset znovu procházet související záznamy s vhodným kontextem.
položky přeložitelné (jako zeměpisné názvy, prodejní podmínky atd.).

.. varování:

Pokud váš šablonový formulář nevyužívá přeložitelné záznamové pole, při opětovném procházení záznamu
v jiném jazyce není nutné a ovlivní výkon.

Pojďme se podívat na výkaz prodejních objednávek z modulu Prodej:

<!-- Hlavní šablona -->
<šablona id="report_saleorder">

<t t-foreach="dokumenty" t-as="dokument">


</t>


<!-- Překladatelný šablonový komentář -->
<template id="report_saleorder_dokument">

<t t-set="doc" t-value="doc.s kontextem (jazyk = partner_id.jazyk)" />
<t t-call="web.externí_layout">
<div třída="stránka">

<div class="row">
<div class="col-6">
<strong t-if="doc.partner_shipping_id == doc.partner_invoice_id">Faktura a adresa pro zaslání:</strong>
<strong t-if="doc.partner_shipping_id != doc.partner_invoice_id">Adresa faktury:</strong>

                    <...>

</div>
</t>



Hlavní šablona volá přeložitelnou šablonu s „doc.partner_id.lang“ jako
„t-lang“ parametru, takže se zobrazí v jazyce partnera.
Každá objednávka prodeje bude vytisknuta v jazyce odpovídajícím zákazníkovi. Pokud chcete
přeložit pouze tělo dokumentu, ale ponechat hlavičku a patu v výchozím nastavení
jazyka bychom mohli tento vnější formát zprávy nazvat takto:

<t t-call="web.external_layout" t-lang="cs_CZ">

..tip:

Prosím vás, abyste si všimli, že to funguje pouze při volání externích šablon.
schopnost překládat část dokumentu nastavením atributu „t-lang“ na jiném XML uzlu
než „t-volání“. Pokud chcete přeložit část šablony, můžete vytvořit externí
šablonu s touto částečnou šablonou a volat ji z hlavní šablony pomocí „t-lang“
atribut.


Čárové kódy
--------

Čárové kódy jsou obrázky vrácené kontrolerem, které lze snadno vložit
díky syntaxi QWebu (např. viz :ref:`reference/qweb/attributes`):

.. kódový blok:: html



Můžete přidat další parametry jako řetězec dotazu

.. kódový blok:: html

<img t-att-src="'/report/barcode/?
barcode_type='QR'&amp;value='text'&amp;width=200&amp;height=200" />


Užitečné poznámky
--------------

* Můžete používat třídy Twitter Bootstrap a FontAwesome ve svém výkazu
šablona
* Místní CSS lze vložit přímo do šablony
* Globální CSS lze vložit do hlavního formátu zprávy dědičným způsobem.
šablonu a vložit svůj CSS:

<šablona id="report_saleorder_style" dědí_id="report.style">
<xpath expr=".">

.example-css-class {
pozadí: červená;
          }
</t>



* Pokud se zdá, že chybí styly ve vašem PDF hlášení, zkontrolujte


.. odkaz/zprávy/papírové formáty:

Formát papíru
============

Formáty papíru jsou záznamy „report.paperformat“ a mohou obsahovat
sledujícími atributy:

„jméno“ (povinné)
jen jako pomůcka při hledání zprávy, nikoliv jako popis zprávy
v nějakém seznamu
„Popis“
malý popis formátu
„formát“
buď předdefinovaný formát (A0 až A9, B0 až B10, Legal, Letter,
Tabloid, ...) nebo „vlastní“; výchozí velikost je A4. Nemůžete používat nezadané
formát, pokud definujete rozměry stránky.
„dpi“
výstupní DPI; 90 v základním nastavení
„margintop“, „marginbottom“, „marginleft“, „marginright“
velikost okrajů v mm
„výška stránky“, „šířka stránky“
rozměry stránky v mm
„orientace“
Portrét nebo krajina
„hlavička“
pravda/nepravda pro zobrazení hlavičkové řádky
„header_spacing“
mezera mezi hlavičkami v mm

Příklad:

<záznam id="formát_papíru_francouzská kontrola" typu="report.paperformat">
<políčko jméno="název">Francouzský bankovní šek</políčko>
<field name="default" eval="True"/>
<položka název="formát">vlastní</položka>
<vlastnost jméno="page_height">80</vlastnost>
<vlastnost jméno="page_width">175</vlastnost>
<položka name="orientace">portrét</položka>
<field name="margin_top">3</field>
<vlastnost jméno="margin-bottom">3</vlastnost>
<vlastnost jméno="margin-left">3</vlastnost>
<pole name="margin_right">3</pole>
<pole název="hlavička" hodnota="false"/>
<vlastnost name="hlavičkové rozestupy">3</vlastnost>
<vlastnost jméno="dpi">80</vlastnost>
</záznam>

.. _odkaz/zprávy/vlastní zprávy:

Přizpůsobené zprávy
==============

Základní reportovací systém vytváří hodnoty renderingu na základě cíle
Model specifikovaný pomocí pole „model“.

První bude hledat modelku jménem
:samp:`report.{modul.nazev_reportu}` a zavolat tento model.
„_get_report_values(doc_ids, data)“ pro přípravu dat pro zobrazení.
šablona.

Toto lze použít k zahrnutí libovolných položek, které chceme používat nebo zobrazovat při renderování.
šablona, například z dat dalších modelů:

... kódový blok:: python

od odoo importovat api, modely

třída ParticularReport(model.AbstractModel):
_name = 'report.module.report_name'

def _get_report_values(self, docids, data=None):
            # Zpět zprávu akce, budeme ji potřebovat pro její data.
report = self.env['ir.actions.report']._get_report_from_name('modul.report_jméno')
            # získat vybraná data pro tuto verzi zprávy
obj = self.env[report.model].prohlížet(docidy)
            # vrátit vlastní kontext renderování
return {
'řádky': docids.get_lines()
            }

.. varování:

Při použití vlastního reportu se zobrazí „Výchozí“ položky související s dokumentem.
(„doc_id“, „doc_model“ a „dokumenty“) nebudou zahrnuty. Pokud chcete
Pokud je chcete, musíte je do textu vložit sami.

V následujícím příkladu bude kontext renderování obsahovat hodnoty „globální“.
a také „řádky“, které do nich vložíme, ale nic jiného.

.. _reference/reporty/vlastní písmo:

Vlastní písmo
============

Pokud chcete používat vlastní písmo, budete potřebovat přidat své vlastní písmo a související méně/CSS do balíčku „web.reports_assets_common“.
Pokud přidáte svůj vlastní font do „web.assets_common“ nebo „web.assets_backend“, nebude k dispozici pro zprávy QWeb.

Příklad:

<šablona id="report_assets_common_custom_fonts" jméno="QWeb Custom Fonts" dědí od "web.report_assets_common">
<xpath expr="." pozice="uvnitř"
<link href="/vašemodul/statické/src/less/fonty.less" rel="styl" typu="text/less"/>
</xpath>


Budete muset definovat „@font-face“ v tomto souboru, i když jste jej použili v jiném balíčku aktiv (kromě „web.reports_assets_common“).

Příklad:

@font-face {
font-family: 'MonixBold';
src: 'MonixBold', 'MonixBold', url('/modul/statické_fonty/MonixBold-Regular.otf') format('opentype');
    }

h1.title-big {
font-family: MonixBold;
velikost písma: 60px;
barva: #3399cc;
    }

Po přidání třídy do balíčku aktiv můžete použít třídu – v tomto příkladu „h1-title-big“ – ve svém vlastním QWeb reportu.

Zprávy jsou webové stránky.
=====================

Hlášení jsou dynamicky generována moduly hlášení a lze je zobrazit
přes přímo uvedený odkaz:

Příkladem je přístup k zprávě o prodejní objednávce v režimu HTML.
http://<server-address>/report/html/sale.report_saleorder/38

Případně si můžete stáhnout PDF verzi zde
http://<server-address>/report/pdf/sale.report_saleorder/38

… [#unzoned] nezáleží na časovém pásmu, ve kterém je datum a čas.
objekt je ve skutečnosti v (včetně časového pásma), jeho časové pásmo bude
nepodmíněně nastavit na UTC před upravením podle
uživatelů

..._wkhtmltopdf: https://wkhtmltopdf.org
