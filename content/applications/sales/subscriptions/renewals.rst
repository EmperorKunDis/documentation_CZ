===================
Obnovit předplatné
===================

Základem každého předplatného je opakované platby. To znamená, že zákazníci
zaručeně platit pravidelnou částku v určitém časovém intervalu, za přístup k předplatnému.
produkt nebo služba.

Obnovení předplatného je proces, kterým zákazníci procházejí, když se rozhodnou pokračovat ve sledování obsahu.
účast na a zaplacení předplatného produktu nebo služby.

Uživatelé procházejí obnovovacím procesem v různých intervalech – týdně, měsíčně, ročně atd.
– v závislosti na délce sjednané doby trvání.

Většina společností, které nabízí předplatné, se snaží automatizovat proces obnovení pro zákazníky.
Plně automatické obnovení předplatného se ale v některých případech nepoužívá.

Aplikace Odoo **Subscriptions** umožňuje společnostem spravovat všechny své předplatné na jednom místě.
místo. Obnovení může být automatické nebo manuální, zahrnovat další produkty nebo doplňkové služby
na základě každé obnovy a filtrovat v agregovaných pohledech pro rychlé vyhledání zákazníků, kteří potřebují obnovit
jejich předplatné.

Obnovení předplatného
=====================

Aby se obnovila předplatná, je nutné potvrdit cenovou nabídku s předplatným produktem.
s nastaveným opakujícím se plánem.

Pro otevření cenové nabídky přejděte na: „Aplikace pro předplatné --> Předplatné“.
--> Citáty“ a vyberte požadovanou citát z seznamu nebo vytvořte nový kliknutím
:guilabel:`Nový“ pro otevření nového citačního formuláře.

.. poznámka::
  - Je potřeba pouze jediný produkt.
  - Předplatné je považováno za produkt, protože se jedná o opakující se produkt.

Předplatitelské ceny musí být potvrzeny a platba od zákazníka za
Prvotní předplatné musí být fakturováno a zaregistrováno, aby se úspěšně otevřel *Obnovení
Citace*

.. viz též:
Více informací o výše uvedeném procesu potvrzení cenových nabídek a fakturace plateb naleznete zde.
viz:
   - :doc:`../sales/sales_quotations/create_quotations`
   - :doc:`../sales/sales_quotations/get_paid_to_validate`

Jakmile je potvrzena platba z předplatného, nabídka se stává prodejnou.
objednávku. Na prodejní objednávkový formulář se aplikuje štítek „Ve výrobě“ a sada tlačítek
objeví se také v hlavičce prodejního příkazu, včetně tlačítka „Obnovit“.

.. obrázek:obnovení/tlačítko pro obnovu.png

:alt:Tlačítko pro obnovení objednávky předplatného s Odoo Subscription.

Když je kliknut na tlačítko „Obnovit“, Odoo okamžitě předloží novou nabídku obnovení.
s tagem „Přepočet ceny“.

.. obrázek:obnovení/cenová nabídka.png

:alt:Obnovení cenové nabídky v aplikaci Odoo Předplatné.

Zde se může objevit běžný prodejní proces k potvrzení cenové nabídky. Obvykle začíná
kliknutím na tlačítko „Odeslat e-mailem“, které odesílá kopii nabídky zákazníkovi.
e-mailovou adresu, aby ji mohli potvrdit a nakonec zaplatit.

.. poznámka::
V chatu s citačním štítkem „Obnovení ceny“ je zmíněno, že tento předplatitelský účet
obnovení předplatného z původní objednávky.

Jakmile je potvrzena cenová nabídka na obnovu, stává se z ní objednávka a
V horní části stránky se zobrazí tlačítko „Historie prodeje“.

.. obrázek:renovace/tlačítko-prodejní-historie-chytré-krabičky.png

Sales history smart button in the Odoo Subscriptions application.

Když je kliknutá tlačítko „Historie prodeje“, Odoo zobrazí samostatnou stránku.
ukázat různé prodejní objednávky spojené s tímto předplatným a jejich individuální
:label:Stav předplatného.

.. obrázek:obnovení/stránka s historií prodeje.png

:alt:Obnovení cenové nabídky v aplikaci Odoo Předplatné.

Dále je potřeba potvrdit „Obnovení cenové nabídky“ a pak stisknout tlačítko „MRR“.
je také viditelný na vrcholu objednávky prodeje.

.. obrázek:renovace/tlacitko-chytre-kliceni.png

:alt: Tlačítko MRR Smart v aplikaci Odoo Subscriptions.

Po kliknutí se zobrazí stránka „Analýza MRR“, která podrobně popisuje měsíční opakující se příjmy.
s tímto konkrétním předplatným.

.. důležité:
Ve výjimečných případech může automatické platby selhat, což způsobí štítek *Nepodařilo se provést platbu*.
v pravém horním rohu objednávky, pokud došlo k chybě při způsobu platby.

To se dělá proto, aby systém neúčtoval zákazníkovi další poplatky při příští plánované platbě.
akci spustí. Protože stav platby není známý, požádá Odoo o ruční provedení operace.
zjistit, zda byla platba provedena, než bude možné ji používat znovu.

Pro zobrazení cenové nabídky přejděte na: „Aplikace pro správu předplatného --> Správa předplatného --> Ceník“.
Vyberte požadovanou předplatnou a zkontrolujte Chatter, abyste zjistili, zda byla platba provedena.

Pokud platba nebyla provedena, nejprve vstupte do režimu ladění podle návodu :doc:`Ladění (debugging) <../../general/developer_mode>
Poté klikněte na záložku „Další informace“ a označte políčko vedle „Smlouva“.
v případě výjimky. Obnovte objednávku a štítek „Neplacení“ zmizí.

Pokud platba **byla** provedena, musí být vystavena nová faktura a ručně zadána do systému. To se děje automaticky
aktualizuje datum příští faktury předplatného. Jakmile je vytvořen, zadejte:
<../../obecne/rozvojovy-mod>“ a přejděte na novou objednávku. Klikněte na „Další
záložce „Info“ a zaškrtněte políčko vedle „Smlouva v případě výjimky“.
Obnovte objednávku prodeje a štítek „Neplacení“ zmizí.

.. obrázek::obnovení/smlouva-v-vyjímce.png
:synchronizace: střed
:alt:Vybraná možnost „smlouva v mimořádné situaci“ s vyznačeným štítkem „neplatba“.

Volba „smlouva v případě výjimky“ zvolená s volbou „neúspěšná platba“.
zobrazení štítku.

V obou případech se jedná o situaci, kdy je již nevybraná možnost „Smlouva v mimořádných případech“.
automaticky obnoví. Pokud zůstane předplatné v režimu „neúspěšná platba“,
do té doby, než bude objednávka uzavřena.

.. viz též:
   - :doc:`../předplatné`
