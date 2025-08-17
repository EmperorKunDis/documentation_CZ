... faktury pro zákazníky/poštou:

=========
Snailmail
=========

Posílání přímé pošty může být efektivní strategií pro zaujmutí pozornosti lidí, zejména když
jejich e-mailové schránky jsou přeplněné. S Odoo máte možnost vystavovat faktury a vést po nich sledování
připojte se k nám a získejte přístup ke všem svým reportům poštou ze všech zemí světa.

Konfigurace
=============

Přejděte do sekce „Účetnictví > Konfigurace > Nastavení > Faktury zákazníkům“.
Aktivovat: guilabel:"Poštovní zásilka".

Chcete-li tuto funkci nastavit jako výchozí, vyberte možnost „Odeslat poštou“ v nabídce „Výchozí způsob odeslání“.
Oddíl „Možnosti“.

.. obrázek: snailmail/setup-snailmail.png
:align:center
:alt:V nastavení zapněte funkci poštovní schránky v účetnictví Odoo

Faktury poštou
=====================

Otevřete fakturu, klikněte na „Odeslat a tisknout“ a vyberte možnost „Poslat poštou“. Ujistěte se
adresa vašeho zákazníka je správně nastavena včetně země před odesláním dopisu.

.. důležité::
Vaše dokumenty musí splňovat následující pravidla, aby mohly být odeslány a projít kontrolou:

   - Okraje musí být **5 mm** po všech stranách. Odoo je nutí vytvořit okrajové pásy vyplněním
bílá před odesláním pošty dopisem, může vést k tomu, že uživatel přijde o své zvyky.
do okrajů. Chcete-li zkontrolovat okraje, zapněte režim vývojáře
<developer-mode>`, přejděte na: „Všeobecné nastavení“ --> „Technické“ --> „Hlášení
sekci: Formát papíru.
   - V levém dolním rohu musí zůstat volný čtverec o rozměrech 15 mm na 15 mm.
   - Při odesílání pošty musí být prostor volný (ke stažení: stáhnout šablonu pro tisk v PDF).
(více informací najdete v souboru snailmail/snailmail-template.pdf).
   - Pingen (poskytovatel služby Odoo Snailmail) skenuje oblast pro zpracování adresy, takže pokud se něco změní
Pokud je adresa napsaná mimo oblast, nebude počítána jako součást adresy.

Ceny
=======

Snailmail je služba /applications/essentials/in_app_purchase, která vyžaduje předplatné známky.
(=poštovné) za práci. Za odeslání jednoho dokumentu se platí jedna známka.

Pro nákup známek přejděte do sekce „Účetnictví“ -> „Konfigurace“ -> „Nastavení“ -> „Zákazník“.
faktury: „Snailmail“, klikněte na „Koupit kredity“ nebo přejděte do sekce „Nastavení > Aplikace“.
Nákupy: Odoo IAP, a klikněte na „Zobrazit mé služby“.

.. viz též:
„Zásady ochrany soukromí společnosti Odoo“
