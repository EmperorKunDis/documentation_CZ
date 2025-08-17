================================
Digitální dokumenty s umělou inteligencí
================================

Digitální fakturace je proces převodu papírových dokumentů na dodavatelskou fakturu a zákaznický účet.
faktury v účetnictví.

Odoo využívá technologii optického rozpoznávání znaků a umělé inteligence k
poznat obsah dokumentů. Formuláře dodavatelské faktury a zákaznické faktury se automaticky
vytvářené a obyvatelné na základě skenovaných faktur.

.. viz též:
   - „Ověřte si digitální zpracování faktur od společnosti Odoo“
   - „Návody k Odoo: Digitalizace faktur od dodavatelů
<https://www.odoo.com/slides/slide/vendor-bill-digitization-7065>

Konfigurace
=============

V poli „Účetnictví“ -> „Konfigurace“ -> „Nastavení“ -> „Digitální podpisy“ zaškrtněte pole
„Digitální dokumenty“ a zvolte, jestli „Faktury dodavatelů“ nebo
:guilabel:„Faktury zákazníkům“ (včetně kreditních faktur) by měly být zpracovány
automaticky nebo na vyžádání.

Pokud zapnete možnost „Jedna daňová řádka na faktuře“, vytvoří se pouze jedna daňová řádka za danou sazbu.
V novém zákoně nezáleží na počtu řádků faktury.

Nahrání faktury
==============

Nahrát faktury ručně
------------------------

V sekci „Účetní přehled“ klikněte na tlačítko „Nahrát“ vašeho dodavatele.
Sbírka zákonů.
Alternativně přejděte na: „Účetnictví“ -> „Zákazníci“ -> „Faktury“.
:menu-vyberte „Účetnictví“ -> „Dodavatelé“ -> „Faktury“ a vyberte „Nahrát“.

..._fakturaci/e-mailovou adresu:

Nahrávejte faktury pomocí e-mailové adresy
------------------------------------

Můžete si nakonfigurovat své propojené skeneru, aby odesílal skenované dokumenty na e-mailovou adresu aliasu. Emaily zaslané na
Tyto přezdívky jsou převedeny do nových návrhů faktur pro zákazníky nebo dodavatele.

Můžete změnit e-mailovou adresu odkazující na časopis. Chcete-li tak učinit, přejděte do aplikace „Nastavení“. Pod
:guilabel:`Obecné nastavení: Diskuse“, zapněte „Vlastní e-mailové servery“ a přidejte
:guilabel:„Název domény“ a :guilabel:„Uložit“.

Emailová adresa je nyní dostupná v záložce „Pokročilé nastavení“ v záznamu o příspěvku.
Doručený e-mail se automaticky převede na novou fakturu nebo účetní doklad.

.. poznámka::
Pokud používáte aplikaci „Dokumenty“ (viz dokumentace: Dokumenty ), můžete automaticky
Odesílejte své faktury do pracovního prostoru Finance (např.
„(příklad@odoo.com)“.

Výchozí e-mailové aliasy „faktury dodavatelů“ a „faktury odběratelů“, které následují
Název domény, který jste nastavili, se automaticky vytvoří pro faktury od dodavatele.
:guilabel:`Faktury zákazníkům“ a „E-maily odeslané na tyto adresy jsou převedeny
automaticky do nových faktur nebo účtů.

Chcete-li změnit výchozí e-mailovou adresu, přejděte na
Vyberte položku „Účetnictví“ -> „Konfigurace“ -> „Účetnictví: Knihy“. Vyberte knihu, kterou chcete
klikněte na záložku „Pokročilé nastavení“ a upravte položku „E-mailová přezdívka“.

Digitalizace faktur
====================

Podle vašich nastavení se dokument buď zpracuje automaticky, nebo budete muset kliknout na
Klikněte na „Odeslat k digitalizaci“ a provádějte ji ručně.

Jakmile jsou data z PDF extrahována, můžete je opravit, pokud je třeba, kliknutím na
odpovídající štítky (k dispozici v režimu „Upravit“).

Počítačové vidění s umělou inteligencí
========================

Je nezbytné zkontrolovat a opravit (pokud je třeba) informace, které byly během digitalizace nahrány.
Poté musíte dokument nahrát kliknutím na tlačítko „Potvrdit“. Tímto způsobem umělá inteligence
se učí a systém identifikuje správná data pro budoucí digitalizace.

Ceny
=======

Digitální fakturace je služba In-App Purchase (IAP), která vyžaduje předplacené kredity.
práce. Digitalizace jednoho dokumentu spotřebuje jeden kredit.

Pro nákup kreditu přejděte do sekce „Účetnictví“ -> „Konfigurace“ -> „Nastavení“ -> „Digitální fotoaparát“.
a klikněte na „Koupit kredity“, nebo přejděte do „Nastavení“ -> „Odoo IAP“ a klikněte na
:guilabel:`Zobrazit moje služby“.

.. poznámka::
Uživatelé podnikové verze Odoo s platnou předplatitelskou licencí získají bezplatné kredity, které mohou využít ke testování funkcí IAP.
rozhodnout se o koupi dalších kreditů pro databázi. To zahrnuje i demoverze a tréninkové databáze
vzdělávací databáze a jednoduché databáze bez aplikace.

.. viz též:
   - „Naše politika soukromí“
   - :doc:`/aplikace/základní/nákupy-v-aplikaci`
