=====
Formy
=====

Formuláře v Odoo jsou velmi silné. Jsou přímo integrovány s dalšími aplikacemi a lze je
má mnoho různých využití.

V této kapitole se dozvíte, jak:

- Přidejte formulář do vlastního šablonového tématu.
- Změnit akci formuláře.
- Stylování formulářů díky proměnným Bootstrapu.

... /webové šablony/formuláře/výchozí formulář:

Výchozí tvar
============

Pokud chcete přidat formulář na stránku, vložte do ní kód generovaný Webovým tvůrcem.

Mělo by vypadat nějak takto.

... blok kódu::xml

<form
akce="/webová stránka/formulář/" metoda="POST"
enctype="multipart/form-data"
označené jako povinné.
data-mark="*" data-pre-fill="true">
data-success-mode="redirect"
data-success-page="/"
model_jméno="mail.mail">
<div třída="s_webové_formuláře_řádky" třída="s_bezbarvých_zadání">

<!--Formulářové pole-->
</div>
</div>


... /webové-šablony/formuláře/akce/:

Akce
=======

V značce formuláře je atribut data-model_name, který vám umožní definovat různé akce pro vaše
forma.

Odeslat e-mail (tato akce je používána výchozí hodnotou).

... blok kódu::xml

<form data-model_name="mail.mail">

Přihlásit se na pracovní pozici.

... blok kódu::xml

<form data-model_name="hr.uchazeč">

Vytvořte zákazníka.

... blok kódu::xml

<form data-model_name="res.partner">

Vytvořte si lístek.

... blok kódu::xml

<form data-model_name="helpdesk.ticket">

Vytvořit příležitost.

... blok kódu::xml

<form data-model_name="crm.lead">

Vytvořte úkol.

... blok kódu::xml

<form data-model_name="projekt.úkol">

.. poznámka::

Výchozí akcí je „Odeslat e-mail“, ale pokud jsou na databázi nainstalovány nějaké aplikace, pak
další možnosti jsou například: Přihlásit se k práci, vytvořit zákazníka, vytvořit lístek, vytvořit požadavek.
příležitost, atd.

Prosím, zkontrolujte si, že některé z těchto akcí vyžadují specifické požadované pole.
funkční. Abychom nezapomněli na některé požadavky, doporučujeme přednastavit formulářový kousek
Webového tvůrce a vložte do něj zdrojový kód, který byl vygenerován.

.. /webové šablony/formuláře/úspěch:

Úspěch
=======

Definujte, co se stane po odeslání formuláře pomocí atributu data-success-mode.

Přesměrujte uživatele na stránku definovanou v atributu data-success-page.

... blok kódu::xml

<form data-success-mode="redirect" data-success-page="/kontaktujte-nás-děkujeme/">

Zobrazit zprávu (na stejné stránce).

... blok kódu::xml

<form data-success-mode="message">

Přidejte zprávu o úspěchu přímo pod značku formuláře. Vždy přidejte třídu d-none, aby
že úspěšné vyplnění formuláře je skryté, pokud není odesláno.

... blok kódu::xml

<div class="s_website_form_end_message d-none">
<div třída="oe_struktura">
<část třídy „s_text_block“ s výškou 64px a odsazením 64px>
<div class="container">



</div>

