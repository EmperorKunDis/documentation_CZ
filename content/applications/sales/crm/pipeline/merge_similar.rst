=====================================
Sloučit podobné kontakty a příležitosti
=====================================

Odoo automaticky detekuje podobné leady a příležitosti v aplikaci CRM.
Duplicitní záznamy umožňují jejich sloučení bez ztráty informací.
Tímto způsobem se nejen organizuje *trubní systém*, ale také zabraňuje zákazníkům v tom, aby
Kontaktováni více než jedním prodejcem.

.. poznámka::
Při slučování příležitostí se žádné informace neztratí. Data z druhé příležitosti jsou zaznamenaná
chaty a informační pole pro odkazování.

Identifikujte podobné kontakty a příležitosti
========================================

Podobné kontakty a příležitosti jsou identifikovány porovnáním e-mailové adresy a telefonního čísla.
spojeného kontaktu. Pokud je nalezen podobný vodič/příležitost, tlačítko „Podobné vodiče“
je uveden na začátku záznamu o příležitosti (nebo kontaktu).

.. obrázek: merge_similar/similar-smart-button.png
:align:center
:alt:Záznam o příležitosti s důrazem na tlačítko Smart Button Similar Leads.

Srovnání podobných příležitostí a kontaktů
-----------------------------------------

Pro porovnání podrobností podobných příležitostí přejděte na: „Aplikace CRM -->
Pipelines nebo menuselection: CRM aplikace --> Vedoucí. Otevřete vedoucího nebo příležitost a klikněte na
tlačítko „Podobné kontakty“. To otevře kartový pohled, který zobrazuje pouze podobné
leads/příležitosti. Klikněte na kartu pro zobrazení podrobností o leadu/příležitosti a potvrďte, že
Měly by se spojit.

Spojování podobných kontaktů a příležitostí
=======================================

.. důležité:
Při sloučení se Odoo zaměřuje na toho, kdo byl vytvořen jako první.
sloučit informace do prvního vytvořeného kontaktu/příležitosti. Pokud je však v databázi více
opportunity jsou sloučeny, vzniklá záznamová položka se označuje jako příležitost, ať už
z nichž byl vytvořen první záznam.

Po potvrzení, že kontakty a příležitosti by měly být sloučeny, se vraťte do kartového pohledu pomocí
kousky chleba, nebo klikněte na tlačítko „Podobné kontakty“ v rozbalovacím menu.
:ikonka: „zobrazit jako seznam“ :guilabel:„(seznam)“ ikona pro přepnutí na zobrazení v podobě seznamu.

Zatrhněte políčko na levé straně stránky pro sloučení kontaktů/příležitostí a pak klikněte na
Ikona „Akce“ v horní části stránky odhaluje rozbalovací nabídku.
Vyberte možnost „Spojit“ z rozbalovací nabídky.
vévodí.

Když je z nabídky „Akce“ vybrána možnost „Sloučit“,
Pop-up okno Merge se zobrazí. V tomto pop-up okně je pod položkou Assign
možnosti vybrat si „Prodejce“ a „Tým prodeje“.
Přiměřené rozbalovací nabídky.

Pod těmito poli jsou uvedeny příležitosti k propojení s příslušnými kontakty.
informace. Klikněte na tlačítko „Sloučit“.

.. obrázek:: select-merge.png
:align:center
:alt: Seznam podobných kontaktů a příležitostí vybraných pro sloučení v aplikaci CRM.

.. nebezpečí::
Spojení je nevratná akce. Nespojujte kontakty a příležitosti, pokud nejste naprosto jistí
Tyto dvě skupiny by měly být spojeny.

Kdy by neměly být sloučeny příležitosti
=============================================

Může se stát, že bude identifikován podobný vodič nebo příležitost, ale neměla by být
sloučeny. Tyto okolnosti se liší v závislosti na procesech prodejního týmu a organizace. Některé
Potenciální scénáře jsou uvedeny níže.

Ztracené příležitosti
----------

Pokud je příležitost označena jako ztracená, může být stále sloučena.
s aktivním kontaktem nebo příležitostí. Výsledný kontakt nebo příležitost je označen jako aktivní a přidán do
plynovod.

Různé kontakty uvnitř organizace
----------------------------------------

Leady/příležitosti ze stejné organizace, ale s různými kontakty, nemusí mít
stejné potřeby. V tomto případě je výhodnější nezrušit tyto záznamy a přidělit
Stejný prodejce nebo tým může zabránit opakování práce a komunikaci.

Existující duplicity s více než jedním prodejcem
--------------------------------------------------

Pokud existuje v databázi více než jeden kontakt/příležitost, může být danému obchodníkovi přiřazeno více prodejců.
těm, kteří aktivně pracují na nich samostatně. I když tyto příležitosti mohou potřebovat
je doporučeno označit prodejce, kteří jsou postiženi, v interním systému
poznámka pro lepší viditelnost.

Kontaktní údaje jsou podobné, ale nejsou přesné
--------------------------------------------

Podobné kontakty a příležitosti jsou identifikovány porovnáním e-mailových adres a telefonních čísel
související kontakty. Pokud je e-mailová adresa *podobná*, ale není *stejná* jako ta správná, mohou být
zůstat nezávislý.

Příklad:
Do trubky byly přidány tři různé větve a prodavačům byly přiřazeny různé obchodní příležitosti.
Byly identifikovány jako „Podobné kontakty“ kvůli e-mailovým adresám kontaktů.

Dva z těchto e-mailových adres vypadají, že pocházejí od stejné osoby „Robin“ a mají shodný e-mail.
adresy. Tyto kontakty by měly být sloučeny.

Třetí kontakt má stejnou doménu e-mailu, ale jinou adresu a jméno.
Toto vedení je pravděpodobně z téže organizace, ale od jiného kontaktu.
by se neměly spojovat.

.... obrázek::merge_similar/kontaktni-informace-pribeh.png
:synchronizace: střed
:alt: Seznam podobných případů s důrazem na kontaktní informace v aplikaci CRM.
