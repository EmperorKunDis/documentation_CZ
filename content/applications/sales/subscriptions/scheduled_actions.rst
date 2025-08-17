=================
Plánované akce
=================

„Předem naplánované akce“ jsou předdefinované procesy, které umožňují uživatelům automatizovat určité úkoly v
databáze na základě určeného harmonogramu nebo počtu výskytů. Tyto úkoly mohou zahrnovat zasílání
e-maily, vystavování faktur, čištění dat a mnoho dalšího.

V Odoo jsou některé plánované akce aktivní vždy, aby bylo zajištěno, že určité funkce
Aktivovány jsou automaticky, ale existuje také mnoho možností plánovaných akcí, které se zobrazují v
databáze, které nejsou aktivní v základním nastavení.

V Odoo *Předplatné* jsou dvě plánované akce, které spouští proces fakturace.
aktivní opakující se předplatné a také kdy by měla platba skončit z důvodu vypršení předplatného.

Jejich zapnutí je vždy povoleno a lze je kdykoliv zrušit pro správu předplatného.
ručně.

Přístup k plánovaným akcím
========================

.. důležité:
Při přístupu k plánovaným akcím je nutné mít zapnutý režim vývojáře.
aktivovány.

S aktivovaným vývojářským režimem přejděte do aplikace „Nastavení“ --> „Technické“ --> „Plánování“.
Akce.

.. obrázek: scheduled_actions/scheduled-actions-technical-settings-page.png
:align:center
:alt:Možnost plánovaných akcí v sekci Technické nastavení aplikace Nastavení Odoo.

Takto se zobrazí panel „Zaslání e-mailu“. Na této stránce je
kompletní seznam plánovaných akcí pro celou databázi.

Zde zadejte do vyhledávacího pole „Předplatné“. Tímto způsobem se objeví tři předplatná.
výsledky. Následující dokumentace se zaměřuje na poslední dva výsledky v seznamu:

- :guilabel:`Prodejní předplatné: vytváření opakujících se faktur a plateb“
- :guilabel:`Prodej s předplatným: vypršení předplatného“

.. obrázek: scheduled_actions/scheduled-actions-page-subscription-results.png
:align:center
:alt: Výsledky související s předplatným na stránce plánovaných akcí v nastavení Odoo.

Zjistěte, zda je plánovaná akce aktivní, podle sloupce „Aktivní“ v
odpovídající řádek na panelu „Plánované akce“ (viz guilabel:Scheduled Actions), pokud je zaškrtnuté políčko.
zaškrtávací políčko je zelené s vyznačeným křížkem, plánovaná akce je aktivní.

Pokud chcete aktivovat plánovanou akci, klikněte na požadovanou plánovanou akci v seznamu.

.. obrázek:: scheduled_actions/scheduled-action-form.png
:alt: Formulář plánované akce v aplikaci Nastavení Odoo.

Poté přepněte v poli „Aktivní“ přepínač ve schváleném akčním formuláři na
Ano. To udělá přepínač zelený a ukazuje, že plánované akce jsou nyní „aktivní“.

Schopnost nastavit, jak často se má akce spouštět, je k dispozici i u plánované akce.
formulář v poli „Vykonat každý“.

.. důležité:
Pokud je doba provedení menší než pět, tak se plánovaná akce **nefunguje správně**.
minut, což je obecný pravidlo pro všechny plánované akce.

Pro více informací si přečtěte článek :doc:`Často kladené technické otázky


Vytvářejte opakující se faktury a platby
========================================

Aby generoval opakující se faktury a platby podle plánu
akce na správné vytváření opakujících se faktur a plateb za předplatné, *Odložené náklady*.
a účty „Pozdržená faktura“ musí být nastaveny, aby Odoo mohl zpracovávat různé faktury.
a platby související s předplatným.

Pro vytvoření účtů „Záloha na výdaje“ a „Záloha na příjmy“ přejděte do nabídky:menuselection:Účetnictví
app --> Konfigurace --> Nastavení. Oba účty lze nastavit v:guilabel:`Výchozím
Součást „Účty“.

.. obrázek: scheduled_actions/deferred-settings-accounting.png
:align:center
:alt:Nastavení nezbytných odložených účtů v nastavení aplikace Odoo Účetnictví.

Jakmile jsou správné účty zadány v poli „Záloha“ a „Záloha na dlouhodobý majetek“,
V poli „Příjem“ klikněte na tlačítko „Uložit“ v pravém horním rohu.

Vytvořit fakturu
--------------

Elementy související s:guilabel:`Předplatné prodeje: vytváření opakujících se faktur a plateb“
plánované akce lze najít na potvrzených objednávkách s předpokládaným prodejem.

Pro zkoumání těchto prvků otevřete potvrzenou objednávku v aplikaci *Předplatné*.
ukázat objednávkový formulář pro předplatné.

Na potvrzené objednávce předplatného se zaměřte na položku „Opakující se plán“
:guilabel:`Datum další faktury“ políčko.

.. obrázek:scheduled_actions/confirmed-subscription-sales-order-fields.png
:align:center
:alt:Potvrzená objednávka předplatného v aplikaci Odoo Subscriptions.

Plánovaná akce vytváří fakturu, pokud je dnešní datum stejné jako datum:guilabel:`Datum
Další faktura“.

Odoo používá informace z pole „Opakující se plán“ k aktualizaci data příští faktury.
Podle toho.

.. varování:
Pokud je nastavená politika fakturace produktů na základě dodaného množství (ručně), a
Pokud je dodané množství nulové, Odoo nevystaví fakturu a zákazníkovi nebude účtována žádná částka.

Výsledkem je, že předplatné se zpracovává jako bezplatný opakovaný produkt a zobrazuje se takto.
*šumění* objednávky předplatného.

Pokud k tomu dojde, zobrazí se následující zpráva: „Aktivace automatické obnovy byla úspěšná. Zdarma.
Další faktura: [datum]. E-mail nebyl odeslán.

Jakmile je vystaven faktura za předplatné objednávku, lze ji zobrazit kliknutím na
tlačítko „Faktury“ v chytrém panelu, které se zobrazí na vrcholu objednávky prodeje předplatného.

Zákazníkovi je zaslána e-mailová zpráva o pravidelném poplatku za předplatné, pokud existuje.
Na účtu je zadán token pro platbu.

Zkontrolovat, zda existuje „Token platby“, otevřete kartu „Další informace“ a podívejte se na
v poli „Platební token“ v sekci „Předplatné“.

.. obrázek: scheduled_actions/payment-token-field.png
:align:center
:alt: pole Platba v záložce Jiná informace na objednávkovém formuláři pro předplatné.

Pokud neexistuje žádný token platby, vystaví se faktura a bude odeslána zákazníkovi.
V tomto případě je nutné platbu manuálně zadat.

Uzavírání faktur
----------------

Akce „Vytvořit pravidelné faktury a platby“ z plánovače akcí :guilabel:`Prodej s předplatným: Generovat opakující se faktury a platby`:
Má schopnost uzavřít předplatné, pokud jsou splněny následující podmínky:

- Pokud předplatné nemá žádný token platby, vytvořte a zveřejněte fakturu.
- Pokud předplatné obsahuje pole „Platební token“, zkuste provést platbu.

    - Pokud je platba úspěšná, vytvořte a zveřejněte fakturu.
    - Pokud se platba nezdaří, pošlete upomínky občas.

        - Zrušte předplatné, pokud bude nadále selhávat déle než čtrnáct dní.

Vypršení předplatného
========================

Akce :guilabel:`Sale Subscription: expiry of subscription` zkontroluje všechny ostatní
podmínky, které mohou vést k automatickému uzavření předplatného. Pokud jsou splněny určité podmínky,
Plánovaná akce uzavře tuto předplatnou.

Nejprve se spustí akce s názvem „Sale Subscription: expiration of subscriptions“, která zkontroluje, jestli
datum ukončení předplatného již uplynulo a je nastaveno v objednávce na prodej předplatného.

.. obrázek: scheduled_actions/subscription-expiration-date.png
:align:center
:alt:Datum vypršení platnosti objednávky na předplatné v Odoo Subscription.

Poté se spustí akce „Sale Subscription: expiration of subscriptions“, která zkontroluje, jestli
faktura nebyla uhrazena v termínu splatnosti.

Chcete-li zobrazit faktury připojené k předplatnému, otevřete objednávku pro předplatné
produkt a klikněte na chytrý tlačítko „Faktury“. Pak se podívejte na „Datum fakturace“
sloupce.

.. obrázek: scheduled_actions/invoices-invoice-date-column.png
:align:center
:alt:Datum faktury v sekci Faktura na stránce s předplatným aplikace Odoo Subscriptions.

Nedoplatky s datem faktury, které jsou starší než stanovený počet dní.
V poli „Automatické uzavření“ v záložce „Opakující se plán“ jsou automaticky uzavřeny
akci „Vypršení předplatného“ z rozpisu akcí.

.. obrázek:scheduled_actions/automatic-closing-field.png
:align:center
:alt:Pole automatického uzavření v podobě formuláře opakujícího se plánu v Odoo Subscription.

Příkladem je například příští datum faktury 1. července a nastavení automatického uzavření na
„30 dní“, akce, která byla naplánována na 1. srpna, by měla ukončit předplatné.

.. viz též:
   - :doc:`../předplatné`
   - :doc:`automatické upozornění“
