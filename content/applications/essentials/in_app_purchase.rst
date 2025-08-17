======================
Nákupy v aplikaci (IAP)
======================

.. |Nákupy v aplikaci| nahradit za: zkratku: `Nákupy v aplikaci`

Nákupy v aplikaci (IAP) jsou dobrovolné služby, které rozšiřují databáze Odoo. Každá služba nabízí
své vlastní specifické funkce a možnosti. Seznam služeb je k dispozici na webu Odoo IAP
Katalog <https://iap.odoo.com/iap/all-in-app-services>

.. obrázek: in_app_purchase/iap.png
:alt: Katalog služeb IAP dostupných na adrese IAP.Odoo.com.

.. příklad::
Služba :guilabel:`SMS` posílá textové zprávy přímo kontaktům ze záznamů v databázi.
:guilabel:`Digitální dokumenty“ služba digitalizuje skenované nebo PDF faktury dodavatelů, výdaje a
pokračuje s optickým rozpoznáváním znaků a umělou inteligencí.

Služby IAP nepotřebují konfigurovat nebo nastavit před použitím. Uživatelé Odoo mohou kliknout na
službu v aplikaci a aktivovat ji. Každá služba však vyžaduje své vlastní předplacené kredity a
Pokud uživatelé vyčerpají svůj kredit, musí si zakoupit další kredity, aby mohli aplikaci dál používat.

.. poznámka::
Uživatelé podnikové verze Odoo s platnou předplatitelskou licencí získají bezplatné kredity, které mohou využít ke testování funkcí IAP.
rozhodnout se o koupi dalších kreditů pro databázi. To zahrnuje i demoverze a tréninkové databáze
vzdělávací databáze a jednoduché databáze bez aplikace.

.. _in_app_purchase/portal:

Služby IAP
============

Služby IAP poskytuje společnost Odoo i třetí strany a mají široké využití.

Následující služby nabízí Odoo v rámci systému IAP:

- :guilabel:`Digitální dokumenty“: digitalizuje skenované nebo PDF faktury dodavatelů, výdaje a životopisy
s OCR a umělou inteligencí.
- :guilabel:`Autocomplete partnerů“: automaticky doplňuje kontaktní záznamy o firemní údaje.
- :guilabel:`SMS“: odesílá SMS zprávy přímo ze seznamu kontaktů.
- :guilabel:`Výroba kontaktů“: generuje kontakty na základě předem stanovených kritérií a převádí návštěvníky webu
do kvalitních kontaktů a příležitostí.
- :guilabel:`Poštovní zásilka`: zasílá zákazníkům faktury a sledovací zprávy poštou, celosvětově.
- Zajistěte identifikaci podepisujících se službou itsme®:
Odoo Sign umožňuje ověření identity prostřednictvím platformy pro identitu *itsme* :icon:`fa-registered`.
která je v Belgii a Nizozemsku k dispozici.

Pro více informací o všech službách, které jsou nyní k dispozici (poskytovaných vývojáři jinými než Odoo)
navštivte katalog „Odoo IAP <https://iap.odoo.com/iap/all-in-app-services>“.

Používejte služby IAP
----------------

Služby IAP jsou automaticky integrovány s Odoo a nevyžadují od uživatelů žádné konfigurace.
Nastavení. Chcete-li využít službu, interagujte s ní vždy tam, kde se objevuje ve výpisu databáze.

.. příklad::
Následující průtok se soustředí na SMS službu IAP používanou z kontaktu.

To lze provést kliknutím na ikonu „SMS“ v databázi.

....... obrázek:: in_app_purchase/sms-icon.png
:alt:Ikona SMS na obvyklé kontaktní informační stránce, která je součástí databáze Odoo.

Jedním z možných způsobů využití služby SMS |IAP| s Odoo je následující postup:

Nejprve přejděte do aplikace Kontakty pomocí příkazu :menuselection:`Kontakty` a klikněte na kontakt.
mobilní telefonní číslo zadané do pole :guilabel:`Telefon´ nebo :guilabel:`Mobil´
kontaktní formulář.

Poté najděte ikonu „SMS“ vedle ikony „Mobilní telefon“
:guilabel:`Telefon“ nebo :guilabel:`Mobil“ pole. Klikněte na ikonku :icon:`fa-mobile` :guilabel:`SMS“.
a objeví se okno „Odeslat textovou zprávu“.

Do pole „Zpráva“ v okně přetahujte myší text zprávy. Pak klikněte na
:tlačítko „Odeslat SMS“. Odoo poté zprávu odesílá prostřednictvím SMS kontaktu a zároveň eviduje, že byla
Bylo odesláno v chatu kontaktního formuláře.

Při odeslání SMS zprávy jsou automaticky odečteny kredity předplacené služby *SMS* |IAP|.
Odoo se pokusí odečíst z již existujících kreditů. Pokud nebudou dostatek kreditů na odeslání zprávy,
Přiměje uživatele k nákupu dalších produktů.

.. viz též:
Pro více informací o tom, jak používat různé služby |IAP| a pro podrobnější pokyny
vztahující se k funkci SMS v Odoo, přečtěte si níže uvedenou dokumentaci:

   - :doc:`Těžba kontaktů <../sales/crm/acquire_leads/lead_mining>`
   - :doc:`Zvýšte svou databázi kontaktů pomocí funkce Autocomplete Partner

   - :doc:`Marketing SMS <../marketing/sms_marketing>`

... _in_app_purchase/kredity:

Kredity IAP
===========

Každé použití služby IAP spotřebovává předplacenou kreditní částku za tuto službu. Odoo vyzývá
nákup dalších kreditů, když už nezbývá dost kreditů na pokračování v používání služby.
Můžete si také nastavit e-mailové upozornění, když jsou kredity nízké (<in_app_purchase/low-credits>).

Kredity se kupují v balíčcích z katalogu Odoo IAP.
<http://iap.odoo.com/iap/all-in-app-services>_ a cena je specifická pro každou službu.

.. příklad::
Služba „SMS“ má k dispozici čtyři balíčky, viz
nominály:

   - :guilabel:`Startovací balíček“: 10 kreditů
   - :guilabel:`Standardní balení“: 100 kreditů
   - :guilabel:`Pokročilé balení“: 500 kreditů
   - :guilabel:`Expertní balíček“: 1 000 kreditů

.... obrázek: in_app_purchase/packs.png
:alt:Čtyři různé balíčky kreditů pro službu SMS IAP.

Počet kreditů spotřebovaných závisí na délce zprávy a cílové zemi.

Více informací najdete v sekci :doc:`Ceník SMS a často kladené otázky.
viz dokumentace na adrese <../marketing/sms_marketing/cena_a_otazky_a_odpovedi>.

.. _iap/nákup kreditů:

Kupte si kredity
-----------

Pokud není dostatek kreditů na provedení úkolu, databáze automaticky vyzve uživatele k jeho zakoupení.
více kreditů.

Uživatelé si mohou zkontrolovat aktuální stav kreditů pro každý službu a ručně zakoupit další kredity.
Navigujte do aplikace „Nastavení“ --> „Kontakty“ a pod nimi
Klikněte na „Zobrazit služby“.

Tím se zobrazí stránka služby IAP s různými |IAP| službami.
databáze. Zde klikněte na službu IAP a otevřete její stránku „Informace o účtu“, kde
Další kredity lze zakoupit.

Kredity zakoupit manuálně
~~~~~~~~~~~~~~~~~~~~

Chcete-li nakupovat kredity v Odoo ručně, postupujte takto:

Nejprve přejděte do aplikace Nastavení a zadejte do vyhledávacího pole IAP.
Alternativně uživatelé mohou procházet dolů do sekce „Kontakty“.
sekci „Kontakty“, kde je uvedeno „Odoo IAP“ a klikněte na „Zobrazit moje“.
Služby.

.. obrázek: in_app_purchase/view-services.png
:alt:Aplikace Nastavení zobrazující hlavní panel Odoo IAP a tlačítko Zobrazit moje služby.

Provedením takového kroku se zobrazí stránka „IAP Account“, na které jsou uvedeny různé služby IAP.
databáze. Zde klikněte na službu IAP a otevřete její stránku „Informace o účtu“, kde
Další kredity lze zakoupit.

Na stránce „Informace o účtu“ klikněte na tlačítko „Koupit kredity“. To spustí
Stránku „Koupit kredity pro (IAP účet)“ v novém okně. Zde klikněte na „Koupit“.
Požadovaný balíček kreditů. Pak postupujte podle pokynů a zadejte platební údaje a potvrďte
pořádku.

.. obrázek: in_app_purchase/koupit-balíček.png
:alt:Stránka služby SMS na IAP.Odoo.com s čtyřmi balíčky kreditů k prodeji.

Jakmile je transakce dokončena, kredity jsou dostupné pro použití v databázi.

..._v_aplikaci_s_nízkým_kreditem:

Oznámení o nízké úvěrové historii
~~~~~~~~~~~~~~~~~~~~~~~

Je možné si nechat zasílat upozornění, když kreditní limit dosáhne určité hodnoty, abyste se vyhnuli tomu, že vám dojdou peníze.
Použijte službu IAP. Postupujte podle následujících kroků:

Přejděte do aplikace „Nastavení“ a zadejte „IAP“ do vyhledávacího pole.
Pod sekcí „Kontakty“ v části „Odoo IAP“, kde je uvedeno „Zobrazit mé“, klikněte.
Služby.

K dispozici jsou účty IAP v seznamovém zobrazení na stránce „Účet IAP“. Zde lze
Klikněte na požadovaný účet IAP, abyste zobrazili stránku „Informace o účtu“ služby.

Nastavte hodnotu :guilabel:`Email Alert Threshold` na částku kreditu, která by měla spustit upozornění.
upozornit na případný pokles zůstatku pod tuto hodnotu. Následně vyberte uživatele, kteří by měli e-mail obdržet.
upozornění pomocí pole :guilabel:`E-mailové adresy příjemců upozornění`.
