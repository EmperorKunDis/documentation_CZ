================================================================
Elektronické fakturace (:abbr:`EDI (elektronický výměnný formát dat)`)
================================================================

EDI, tedy elektronická výměna dat, je způsob komunikace mezi firmami prostřednictvím obchodních dokumentů.
jako objednávky a faktury v běžném formátu. Odesílání dokumentů podle EDI
standard zajišťuje, že stroj, který zprávu přijímá, informace správně interpretoval.
Existuje několik různých formátů souborů EDI a jsou k dispozici v závislosti na zemi vaší společnosti.

EDI funkce umožňuje automatizaci administrativy mezi firmami a může být také vyžadována
Některé vlády pro daňovou kontrolu nebo zjednodušení správy.

Elektronické fakturace vašich dokumentů jako jsou zákaznické faktury, kreditní dopisy nebo dodavatelské faktury je
jednou z aplikací EDI.

Odoo podporuje elektronické faktury v mnoha zemích. Podrobnější informace naleznete na stránce dané země:

- :doc:`Argentina <elektronické_fakturace/argentina>`
- :doc:`Rakousko <elektronické_fakturace/rakousko>`
- :doc:`Belgie <elektronické_fakturace/belgie>`
- :doc:`Brazílie <elektronické fakturace/brazílie>`
- :doc:`Chile <elektronické fakturace/chile>`
- :doc:`Kolumbie <elektronické_fakturace/kolumbie>“
- :doc:`Chorvatsko <elektronické_fakturace/chorvatsko>`
- :doc:`Ekvádor <elektronické_fakturace/ekvador>“
- :doc:`ESTONSKO <elektronické fakturace/estonsko>`
- :doc:`Finsko <elektronické_fakturace/finsko>`
- :doc:`Guatemala <elektronické_fakturace/guatemala>`
- :doc:`Maďarsko <elektronické_fakturace/maďarsko>`
- :doc:`Irsko <elektronické_fakturace/ireland>`
- :doc:`Itálie <elektronické_fakturace/italie>“
- :doc:`Lotyšsko <elektronické_fakturace/lotyšsko>`
- :doc:`Litva <elektronické_fakturace/litva>`
- :doc:`Lucembursko <elektronické_faktury/lucembursko>“
- :doc:`Mexiko <elektronická fakturace/mexiko>`
- :doc:`Nizozemsko <elektronické fakturace/nizozemsko>`
- :doc:`Norsko <elektronické_fakturace/norsko>“
- :doc:`Peru <elektronické_fakturace/peru>`
- :doc:`Rumunsko <elektronická fakturace/rumunsko>`
- :doc:`Španělsko <elektronické_fakturace/španělsko>`
- :doc:`Španělsko - Baskicko <elektronické_fakturace/baskicko>`
- :doc:`Uruguay <elektronické faktury/uruguay>“

.. viz též:
   - :doc:`Dokumentace k fiskálním lokalizacím <../../fiscal_localizations>`
   - „Zázračná tabulka – elektronické faktury v Odoo“ (PDF)


.._elektronické fakturace/konfigurace:

Konfigurace
=============

Výchozí formát dostupný v okně pro odeslání závisí na vašem
Země zákazníka.

Můžete definovat konkrétní formát faktury pro každého zákazníka. Pro toto nastavení přejděte na
Vyberte položku „Účetnictví“ -> „Zákazníci“ -> „Zákazník“, otevřete formulář zákazníka a přejděte na
Karta „Účetnictví“ a zvolte vhodný formát.

.. obrázek: elektronické_fakturace/zakaznický_formulář.png
:alt:Vyberte formát EDI pro konkrétního zákazníka

Národní elektronické fakturace
-----------------------------

Podle země vaší společnosti (např. „Itálie“:doc:`<../../fiscal_localizations/italy>`)
„Španělsko“ (doc: „Španělsko“), „Mexiko“
<../../fiscal_localizations/mexico> atd.) musíte vystavit daňový doklad s elektronickým účtenkováním.
konkrétní formát pro všechny faktury. V tomto případě můžete definovat výchozí formát elektronické fakturace
pro vaše prodejní deníky.

Pro toto klikněte na: „Účetnictví“ -> „Nastavení“ -> „Knihy“, otevřete si prodejní knihu.
Přejděte na záložku „Další nastavení“ a zapněte formáty, které potřebujete pro tento časopis.

...elektronické fakturace/vystavování:

Vytváření e-faktur
=====================

Klikněte na potvrzenou fakturu a zvolte možnost „Odeslat a tisknout“, abyste otevřeli okno pro odesílání. Zkontrolujte
možnost vytvářet a připojovat soubor elektronické faktury.

.. obrázek: elektronicka_fakturace/okno_zaslani.png
:alt:V poli Peppol je zaškrtnuto a k e-mailu je přiložen soubor faktury ve formátu XML.

...elektronické fakturace/Peppol:

Peppol
======

Síť „Peppol“ zajišťuje výměnu dokumentů a informací
mezi podniky a veřejnými institucemi. Hlavně se používá pro elektronické fakturace.
její přístupové body (konektory do sítě Peppol) umožňují firmám elektronicky
dokumenty.

Odoo je „vstupní branou“ a „SMP (Service Metadata Publisher)“, což umožňuje elektronické
Zadávání faktur bez nutnosti zasílat faktury a daňové doklady e-mailem nebo poštou.

Pokud ještě nebylo provedeno, nainstalujte modul Peppol („účet_peppol“): :guilabel:`ref <general/install>`, :guilabel:`account_peppol`.

.. důležité::
   - Registrace v Peppolu je zdarma a k dispozici v komunitě Odoo.
   - Můžete odesílat faktury pro zákazníky a daňové doklady a přijímat dodavatelské faktury.
**Vrácení peněz** přes Peppol.
   - Můžete odesílat a přijímat v jednom z následujících podporovaných formátů dokumentů:
**BIS Fakturace 3.0, XFaktura CIUS, NLCIUS**.
   - Následující země jsou oprávněné k registraci do systému Peppol v Odoo:
|Andorra, Albánie, Rakousko, Bosna a Hercegovina, Belgie, Bulharsko, Švýcarsko, Kypr
Česká republika, Německo, Dánsko, Estonsko, Španělsko, Finsko, Francie, Spojené království, Řecko
Chorvatsko, Maďarsko, Irsko, Island, Itálie, Lichtenštejnsko, Litva, Lucembursko,
Monako, Černá Hora, Severní Makedonie, Malta, Nizozemsko, Norsko, Polsko, Portugalsko, Rumunsko,
Srbsko, Švédsko, Slovinsko, Slovensko, San Marino, Turecko, Svatý stolec (Městský stát Vatikán)

..._elektronické fakturace/registrace Peppol:

Registrace
------------

Přejděte na „Účetnictví -> Konfigurace -> Nastavení“. Pokud nemáte
Modul Peppol nainstalován, nejprve zaškrtněte políčko „Zapnout PEPPOL“ a poté **ručně
Uložit**. Klikněte na tlačítko „Zahájit odesílání prostřednictvím Peppolu“ a otevřete registrační formulář.

.. poznámka::
Tento registrační formulář se také objeví, pokud zvolíte možnost :guilabel:`Odeslat a tisknout`.
fakturu přes Peppol bez dokončení registrace.

.. obrázek: elektronické_fakturace/registrace_do_peppolu.png
:alt:Tlačítko pro registraci do Peppolu

Můžete se zaregistrovat jako odesílatel nebo příjemce. Odesílatel může zasílat pouze faktury a kreditní doklady
Odoo přes Peppol bez registrace jako účastník Peppol na Odoo SMP. Pokud máte
existující registrace v jiné části Peppolu, kterou chcete zachovat, ale chcete odesílat faktury z
Odoo databáze a přijímat další dokumenty v jiném softwaru, registrovat se jako odesílatel.

.. tip::
   - Můžete se vždy nejprve zaregistrovat jako odesílatel a registraci pro přijímání dokumentů provést později.
   - Při registraci můžete zvolit i příjem dokumentů.

.. obrázek: elektronická_fakturace/registrace_do_peppolu.png
:alt:Formulář pro registraci do systému Peppol

Vyplňte následující informace:

- Zkontrolujte příjemce, pokud chcete registrovat na Odoo SMP. Pokud migrujete z jiného
poskytovatel služeb, vložte klíč migrace z předchozího poskytovatele (pole
se zobrazí po zaškrtnutí políčka (viz obrázek).
- :guilabel:`Schéma elektronické adresy“: obvykle závisí na vašem
země, ve které je společnost registrována. Odoo často vyplní tento údaj kódem EAS nejčastěji používaným ve vaší zemi.
Pro většinu belgických společností je tedy preferovaný kód EAS 0208.
- :guilabel:`Konecní bod`: obvykle se jedná o identifikační číslo z obchodního rejstříku nebo DIČ.
- :guilabel:`Telefonní číslo`: telefonní číslo včetně kódu země (např. +32 v Belgii).
- :guilabel:`E-mailová adresa“: Toto je e-mailová adresa, kterou může Odoo použít k kontaktování vás ohledně vašeho Peppolu.
registrace.

Pokud chcete prozkoumat nebo demonstrovat Peppol, můžete se přihlásit v režimu „Demo“.
V opačném případě vyberte možnost :guilabel:`Živé“.

.. tip::
   - Vybráním :guilabel:Demo se vše v Odoo simuluje. Není odesílání ani přijímání.
ověření partnera.
   - Pro pokročilé uživatele je možné spustit testy na testovacím systému Peppol. Server
umožňuje registraci na Peppol a odesílání/přijímání faktur do/od ostatních účastníků.
Pro to je nutné zapnout režim vývojáře, otevřít aplikaci Nastavení a přejít na
:menu „Technické -> Systémové parametry“ a vyhledejte „account_peppol.edi.mode“.
Klikněte na parametr a změňte hodnotu „Value“ na „test“. Návrat do nastavení Peppolu
v aplikaci **Nastavení**. Možnost :guilabel:`Test` je nyní k dispozici.

.. obrázek: elektronické_fakturace/parametr_systému_peppol.png
:alt:Parametr testovacího režimu Peppol

.. viz též:
   - „Peppol EAS – Evropská komise <https://ec.europa.eu/digital-building-blocks/wikis/display/DIGITAL/Code+lists/>“
   - „Peppol Endpoint - OpenPeppol eDEC Code Lists <https://docs.peppol.eu/edelivery/codelists/>“
(otevřete „Schémata identifikátorů účastníků“ jako stránku ve formátu HTML)

Při instalaci požádejte o zaslání ověřovacího kódu kliknutím na tlačítko „Odeslat
registrační kód formou SMS. Na telefonní číslo, které uživatel zadá, je zaslána textová zpráva s kódem.
Dokončit proces ověřování.

.. obrázek: elektronická_fakturace/peppol-telefonní-ověření.png
:alt: telefonní ověření

Jakmile zadáte kód a kliknete na tlačítko „Registrovat“, váš stav účastníka Peppolu je aktualizován.
Pokud jste si zvolili pouze odeslání dokumentů, pak se stav změní na „Může poslat, ale
neobdržet.
Pokud jste si zvolili zasílání dokumentů, stav se změní na „Mohu poslat, čeká se na schválení“.
registrace k přijímání“. V takovém případě by se měla aktivovat automaticky do 24 hodin.

Pak nastavte výchozí účetní knihu pro přijímání faktur od dodavatelů v poli :guilabel:`Incoming Invoices
Journal.

.. tip::
Chcete-li ručně spustit cron, který kontroluje stav registrace, povolte
:ref:`rozvojový režim“, pak přejděte do „Nastavení“ -> „Technické“ -> „Plánované akce“.
a hledejte akci „Aktualizace stavu účastníka PEPPOL“.

Stav vaší aplikace pro příjem by se měl změnit co nejdříve po registraci na Peppol.
síť.

.. obrázek: elektronická_fakturace/peppol_prijemce.png
:alt: aplikace přijímače

Všechny faktury a dodavatelské faktury lze nyní odeslat přímo prostřednictvím sítě Peppol.

.. důležité::
Chcete-li aktualizovat e-mailovou adresu, kterou může Odoo použít k kontaktování, změňte
:guilabel:`Aktualizovat kontaktní údaje“.

Konfigurace služeb Peppol
-------------------------

Jakmile se zaregistrujete do Odoo SMP, objeví se vám tlačítko „Nastavení služeb Peppol“
zobrazí se, abyste mohli povolit nebo zakázat formáty dokumentů, které používají ostatní účastníci.
Vám může poslat přes Peppol. Výchozí nastavení umožňuje všechny formáty dokumentů podporované Odoo (závislé
na namontovaných modulech).

Kontrola kontaktu
--------------------

Před odesláním faktury kontaktu pomocí sítě Peppol je nutné ověřit, zda
Jsou také zaregistrováni jako účastníci Peppolu.

Pro toto vyberte v menu: „Účetnictví“ - „Zákazníci“ - „Zákazníků“.
formulář, pak přejděte na záložku „Účetnictví“ – „Elektronické fakturace“, vyberte správnou
formátu a ujistěte se, že je vyplněn jejich kód Peppol EAS a „Endpunkt“.
Poté klikněte na tlačítko „Zkontrolovat“. Pokud kontakt existuje v síti, zobrazí se jeho platnost.
je nastaven na platné.

.. obrázek: elektronická_fakturace/peppol-kontakt-ověřit.png
:alt: ověřit registraci kontaktu

.. důležité::
Odoo automaticky vyplní oba kódy EAN a číslo koncového bodu na základě dostupných informací.
pokud chcete kontaktovat někoho, je lepší si tyto informace ověřit přímo u kontaktu.

Je možné zkontrolovat stav účasti na Peppolu několika zákazníků najednou.
Pro toto vyberte v menu „Účetnictví“ -> „Zákazníci“ -> „Zákazníci“ a přepněte na seznamový pohled.
Vyberte zákazníky, které chcete ověřit, a poté klikněte na tlačítko „Akce“ – „Ověření Peppolu“.

Pokud je účastník registrován na síti Peppol, ale nemůže přijímat formát, který jste vybrali
Pro ně se mění štítek „Konec bodu Peppol“ na „Nelze
přijmout tento formát.

.. obrázek: elektronicke_fakturace/peppol-ucastnikovy-formát.png
:alt: ověřit kontakt v ubl formátu

Vystavujte faktury
-------------

Jakmile je faktura připravena k odeslání prostřednictvím sítě Peppol, stačí na ní kliknout na tlačítko „Odeslat a vytisknout“.
fakturační formulář. Chcete-li zadat více faktur, vyberte je v seznamovém pohledu a klikněte
Akce - Odeslat a tisknout; budou odeslány později ve skupině.
Zatrhněte políčka „Fakturace BIS Billing 3.0“ a „Odeslat přes PEPPOL“.

.. obrázek: elektronické_fakturace/peppol-vytisknout-poslat.png
:alt:Odeslat fakturu Peppol

Vystavené faktury, které lze zaslat přes Peppol, jsou označeny jako :guilabel:`Peppol Ready“.
Zobrazit je můžete pomocí filtru „Připraveno na Peppol“ nebo přistupujte k účetnímu rozhraní.
Klikněte na položku „Připravené faktury Peppol“ v příslušném denním odpisu.

.. obrázek:: elektronicka_fakturace/peppol-pripravene-faktury.png
:alt:Filtr faktur připravených pro Peppol

Jakmile jsou faktury odeslány přes Peppol, stav se změní na „Ve zpracování“.
status se změní na „Dokončeno“, jakmile byly úspěšně doručeny kontaktnímu přístupu.
Takže ano, je to tak.

.. obrázek: elektronické_fakturace/peppol-zpracování_zprávy.png
:alt:Stav zprávy Peppol

.. tip::
Výchozí stav sloupce Status Peppol je skryt na seznamu Přijaté faktury. Můžete si zvolit, aby byl
Vybráním z volitelných sloupců, dostupných v pravém horním rohu.
Zobrazení faktur.

Kontrolu stavu těchto faktur provádí program Cron pravidelně. Stav lze zkontrolovat
před spuštěním cronu kliknutím na tlačítko „Stav faktury v systému Peppol“ ve správném
Prodejní deník na účetním přehledu.

.. obrázek: elektronická fakturace/peppol-získání-stavu-zprávy.png
:alt:Stav faktury Peppol

Přijímat faktury od dodavatelů
--------------------

Každý den se kontroluje, zda vám nebyly zaslány nové dokumenty prostřednictvím sítě Peppol.
Tyto dokumenty jsou importovány a automaticky vytvářeny faktury dodavatelů.
návrhy.

.. obrázek:: elektronická_fakturace/peppol-prijmout-faktury.png
:alt: přijímat faktury

Pokud chcete získat příchozí dokumenty Peppol předtím, než bude spuštěn cron, můžete tak učinit prostřednictvím
Účetní přehled na hlavním nákupním dokladu Peppol, který si nastavíte v Nastavení. Stačí kliknout
:guilabel:`Stáhnout z Peppolu“.

.. obrázek: elektronické_fakturace/peppol-vyhledat-faktury.png
:alt:Stáhnout faktury z Peppolu
