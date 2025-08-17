========
Unsplash
========

**Unsplash** je uznávaná knihovna obrázků, která je integrována s Odoo.

Pokud je vaše databáze hostována na Odoo Online, můžete si prohlížet obrázky z Unsplash bez
konfigurace.

Pokud je vaše databáze hostována na Odoo.sh nebo v prostředí on premise, postupujte takto:

#Chcete-li vytvořit klíč přístupu do Unsplash, založte nebo se přihlaste k účtu Unsplash.
<https://unsplash.com>.

#Přejděte na stránku „Dashboard aplikací“ („Applications dashboard“) a klikněte
:guilabel:`Nová aplikace“, zaškrtněte všechny políčka a klikněte na „Přijmout podmínky“.

#V okně vložte své:guilabel:`Jméno aplikace`, začínající
předpona „Odoo:“ (např. „Odoo: Připojení“), takže Unsplash rozpozná, že jde o instanci Odoo. Pak
Přidejte popis a klikněte na tlačítko „Vytvořit aplikaci“.

#Na stránce s podrobnostmi o aplikaci se přesuňte dolů do části „Klíče“ a zkopírujte
:guilabel:`Přístupový klíč“ a :guilabel:"ID aplikace".

#V Odoo přejděte do sekce „Obecné nastavení“ a zapněte „Obrázek Unsplash“.
Vyberte možnost „Knihovna“ a pak zadejte klíč „Přístupu“ a „ID aplikace“.

.. varování:
Jako uživatel Odoo Online máte omezený klíč s maximálně 50 požadavky na Unsplash.
za hodinu.
