========================
Dodání na objednávku (MTO)
========================

.. |SO| nahradit za: :abbr:`SO (objednávka na prodej)`
.. |SOs| nahradí za: :abbr:`SOs (objednávky na prodej)`
.. |MO| nahradit za: zkratka: `MO (manufacturing order)`
.. |PO| nahradit za: :abbr:`PO (objednávka na nákup)`
.. |MTO| nahradit za: zkratka: `MTO (make to order)`
.. |RFQ| nahradit za: zkratku: RFQ (žádost o nabídku)
.. |BOM| nahradit::: zkratka: BOM (seznam materiálů)

*Dodávka na objednávku*, známá také jako *MTO* (výroba na objednávku), je strategie doplňování zásob, která vytváří
návrh objednávky na produkt, pokaždé když je nutné vyplnit prodejní objednávku (SO) nebo když
potřebný jako součást výrobního příkazu (VŘ).

Pro produkty, které jsou zakoupeny od dodavatele, je vytvořena žádost o nabídku (RFQ), aby byly do zásob
produktu, zatímco |RFQ| je vytvářen pro výrobky. Vytvoření |RFQ|
nebo |MO| se vyskytuje pokaždé, když je potvrzeno |SO| nebo |MO| požadující produkt, bez ohledu na
Aktuální stav skladových zásob produktů objednaných zákazníkem.

.. důležité::
Pro použití trasy |MTO| je nutné zapnout funkci :guilabel:`Multistep Routes`.
takže přejděte na: „Inventářová aplikace --> Konfigurace --> Nastavení“ a zaškrtněte
zaškrtávací políčko vedle :guilabel:`Dlouhé trasy“, pod nadpisem :guilabel:`Sklad“.

Nakonec klikněte na tlačítko :guilabel:`Uložit`, abyste změnu uložili.

.. inventář/sklady/úložiště/archivace MTO:

Obnovit trasu MTO
===================

Výchozí nastavení Odoo je „archivované“. To proto, že MTO je trochu specifické.
workflow, který využívá jen několik firem. Ale snadno se archivovaná trasa může znovu otevřít
pár jednoduchých kroků.

Pro to začněte procházet seznamem: „Nastavení aplikace Inventář --> Trasy“.
Stránka „Trasy“, klikněte na ikonu „svislý šipky“ (svislá šipka) vpravo
okraji vyhledávacího pole a klikněte na filtr „Archivované“ pro jeho zapnutí.

.. obrázek: mto/archivní filtr.png
:align:center
:alt:Archivní filtr na stránce s trasami.

Po zapnutí filtru „Archiv“ se na stránce „Trasy“ zobrazí všechny trasy,
a jsou nyní archivovány. Zaškrtněte políčko vedle :guilabel:`Dodání na objednávku (MTO)` a klikněte
tlačítko „Akce“ (ikonka:fa-cog) k zobrazení rozbalovací nabídky. Z rozbalovací nabídky
vyberte: guilabel:"Obnovit".

.. obrázek: mto/unarchive-button.png
:align:center
:alt:Akce odebrání archivace na stránce s trasami.

Nakonec odstraňte filtr „Archiv“ z vyhledávací lišty. Stránka „Trasy“ je nyní
ukazuje všechny nearchivované trasy včetně „Dodání na objednávku (MTO)“, která je vybíratelná
kartě „Sklad“ každé produktové stránky.

Nastavit produkt pro MTO
=========================

S archivací trasy MTO mohou produkty nyní správně konfigurovat pro doplňování na objednávku.
Chcete-li tak učinit, začněte v sekci „Nástroje“ -> „Výrobky“ -> „Výrobky“. Pak vyberte
existující produkt nebo klikněte na „Nový“ pro konfiguraci nového.

Na stránce produktu vyberte záložku „Sklad“ a zapněte „Dodat zboží“.
Dopravní trasu (MTO) v sekci „Trasy“ spolu s „Koupit“ nebo
:guilabel:`Výroba“ trasa.

.. důležité::
Pokud není vybrána jiná trasa, funkce „Dodání na objednávku“ (**MTO**) nefunguje.
stejně tak. Odoo potřebuje vědět, jak doplnit produkt při zadání objednávky
pro něj (koupit nebo vyrobit jej).

.. obrázek: mto/select-routes.png
:align:center
:alt: Vyberte trasu MTO a druhou cestu na záložce Inventář.

Pokud je produkt zakoupen od dodavatele pro splnění požadavku |SOs|, povolte :guilabel:`Může být zakoupen`.
zaškrtávací políčko pod názvem produktu. Tím se objeví záložka „Nákup“ vedle
další záložky níže.

Klikněte na záložku „Nákup“ a specifikujte dodavatele a cenu.
prodávat za.

.. důležité::
Specifikace dodavatele je pro tento postup zásadní, protože Odoo nemůže vytvořit |RFQ| bez specifikace dodavatele.
vědět, od koho je produkt zakoupený.

Pokud je produkt vyráběn, ujistěte se, že má k dispozici seznam komponent (BOM).
takže klikněte na tlačítko „Seznam součástí“ v horní části obrazovky a pak klikněte
Vyberte možnost „Nový“ na stránce „Seznam materiálů“ pro konfiguraci nového seznamu materiálů pro produkt.

.. viz také:
Pro kompletní přehled o vytváření BOM se podívejte na dokumentaci k tématu :doc:`billů materiálu
<../../../výroba/základní nastavení/fakturační konfigurace>.

Doplňte pomocí MTO
===================

Po konfiguraci produktu pro použití trasy |MTO| je vytvořena objednávka na doplnění zásob každých
Čas doručení zboží v pracovní dny (Po - Pá) nebo o víkendu (So - Ne) je potvrzen. Druh objednávky závisí na
druhou trasu navíc k MTO.

Pokud je například Buy druhou volbou, pak při potvrzení objednávky vytvoříte
SO.

.. důležité::
Když je pro produkt povolená trasa MTO, vždy se při každé objednávce vytvoří příkaz na doplnění zásob.
potvrzení o |SO| nebo |MO|. I když je dostatek zásob zboží
na skladě k uspokojení poptávky bez nutnosti zakoupit nebo vyrobit další jednotky.

Zatímco trasa MTO může být použita společně s trasou Buy nebo Manufacture, trasa Buy
je použita jako příklad pro tento postup. Začněte přechodem do aplikace „Prodej“.
Poté klikněte na tlačítko „Nový“, které otevře prázdnou objednávkovou formu.

Do prázdného citačního formuláře přidejte „Zákazník“ a pak klikněte na „Přidat produkt“.
kartě „Řádky objednávek“ a vložte produkt nakonfigurovaný pro použití tras *MTO* a *Koupit*.
Klikněte na tlačítko „Potvrdit“ a citát se změní na |SO|.

Na stránce se nyní objevuje tlačítko „Koupit“ s ikonou štítku. Po kliknutí na něj se zobrazí formulář pro poptávku.
spojené s |SO|.

Klikněte na tlačítko „Potvrdit objednávku“ k potvrzení RFQ a přeměnění jej na PO. Po kliknutí se zobrazí modrá
Tlačítko „Přijmout produkty“ se nyní zobrazuje nad |PO|. Jakmile jsou produkty přijaty,
Klikněte na tlačítko „Přijmout produkty“ a otevře se objednávka přijetí. Klikněte na „Zkontrolovat“,
Zařadit produkty do zásob.

Vraťte se na SO kliknutím na „breadcrumb“ SO nebo přejděte na
:menuselection:`Prodejní aplikace --> Objednávky --> Objednávky“, a poté vyberte SO.

Konečně klikněte na tlačítko „Dodání“ v horní části objednávky a otevřete tak dodací okno.
objednávku. Jakmile jsou produkty odeslány zákazníkovi, klikněte na tlačítko „Potvrdit“
Dodání.

.. viz také:
Informace o průběhu prací, které zahrnují trasu MTO, naleznete v následující dokumentaci:

   - :doc:`dodavatelské sklady“
   - :doc:`../../../vyrábění/dodavatelé/dodavatele_základní“
   - :doc:`/manufacturing/advanced_configuration/sub_assemblies`
