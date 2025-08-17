=============
Cloudové úložiště
=============

Součástí cloudu je integrace úložiště, které umožňuje ukládat chaty.
a přílohy v e-mailech na :ref:`Google Cloud <cloud-storage/google>` nebo :ref:`Microsoft Azure
platforma cloudového úložiště Microsoftu místo databázového serveru.

Modul lze použít k zabránění velkých souborů v přenosu do a z
server databáze nebo když je potřeba více úložného prostoru pro databázi.

.. poznámka::
   - Soubory vytvořené aplikací Odoo (například objednávky prodeje) a soubory aplikace Dokumenty/Podpis jsou uloženy
server databáze.
   - Omezení úložiště databáze závisí na řešení hostingu:

     - Odoo Online: 100 GB
     - Odoo.sh:

       - Sdílené hostování: 512 GB
       - Dedikovaný hosting: 4 TB

     - On premises: omezené infrastrukturou.

.._cloud-storage/google:

Google Cloud
============

Nejprve se zaregistrujte a přihlásíte do služby „Google Cloud“ na adrese https://cloud.google.com/.

..._cloud-storage/google/service:

Služební účet
---------------

#Otevřete navigační panel v konzoli Google Cloud a pak přejděte na: „IAM & Admin
--> Služby --> Vytvořit službu“.
#Definujte „Název služby“, klikněte na „Vytvořit a pokračovat“ a poté
:guilabel:`Dokončeno“.

...... obrázek:: cloud_storage/service-account.png
:alt:Vytvoření účtu služby Google Cloud

#Zapište si e-mailovou adresu služby, protože bude použita při :ref:`cloud
konfigurace úložiště „<cloud-storage/google/bucket>“.
#Klikněte na tlačítko „Akce“ (ikona „Ellipsis v“), poté vyberte možnost „Správa
klíčů.

.... obrázek:: cloud_storage/manage-keys.png
:alt: Přístup k akci „Správa klíčů“

#Přejděte na „Přidat klíč“ a vytvořte nový klíč. Vyberte „JSON“ jako „Klíč“.
typu, a klikněte na tlačítko „Vytvořit“. Uložte si stažený soubor JSON s klíčem v bezpečném místě.
Bude použito při konfiguraci Odoa:ref:`<cloud-storage/google/odoo>`.

.... obrázek::cloud_storage/create-key.png
:alt: Vytvoření klíče JSON služby Google Cloud

..._cloud-storage/google/bucket:

Koš cloudového úložiště
--------------------

#Otevřete navigační panel v konzole Google Cloud a pak přejděte na:menuselection:Cloud
Úložiště --> Koše --> Vytvořit.
#Vložte název kbelíku podle „pravidel pojmenování kbelíků <https://cloud.google.com/storage/docs/buckets?_gl=1*h4hwrv*_ga*MTcwNDM2NDE1Ny4xNzQzNzUxOTEy*_ga_WH2QY8WWF5*MTc0Mzc2NDMyOS4zLjEuMTc0Mzc2NDMyOS42MC4wLjA.#naming>“.
a poznamenat si ji, protože bude použita při konfiguraci Odoo:ref:`<cloud-storage/google/odoo>`.
#Nastavte kbelík podle svých představ a klikněte na tlačítko „Vytvořit“, jakmile budete hotovi.

.. obrázek:: cloud_storage/create-bucket.png
:alt: Vytvoření kbelíku

#Klikněte na tlačítko „Další akce“ (ikona ve tvaru oblouku nahoru) a poté vyberte možnost „Upravit“.
přístup.

.... obrázek:: cloud_storage/bucket-actions.png
:alt:Přístup k „Upravit přístup“ akci úložiště služby Google Cloud

#Klikněte na tlačítko „Přidat hlavní uživatel“ a vložte e-mailovou adresu služby.
hřiště školních dětí.
#Vyberte „Administrátor úložiště“ jako „Role“ pod záložkou „Úložiště“.
a klikněte na tlačítko „Uložit“.

.. obrázek:: cloud_storage/bucket-access.png
:alt:Přidání hlavního uživatele do úložiště služby Google Cloud

.._úložiště v cloudu/Google/Odoo:

Konfigurace Odoo
------------------

#:ref:`Nainstalujte modul Cloud Storage Google<general/install>“.
#Otevřete aplikaci „Nastavení“ a vyberte v navigačním panelu „Cloudové úložiště“.
#Vyberte Google Cloud Storage jako cloudového poskytovatele úložiště pro nové
přílohy.
#Zadejte název úložiště Google, který jste již nastavili (viz cloud-storage/google/bucket).
#Klikněte na „Nahrát soubor“ vedle „Služebního účtu Google“ a vyberte
:ref:`stáhnout soubor ve formátu JSON <cloud-storage/google/service>.
#Nastavte minimální velikost souboru (v bajtech) pro přílohy ukládané na Google Cloud.

.._cloud-storage/microsoft:

Microsoft Azure
===============

Nejprve se zaregistrujte a podepište jej pro „Microsoft Azure <https://azure.microsoft.com>“.

.._cloud-storage/microsoft/app:

Registrace aplikace
----------------

#Vyhledejte službu „Registrace aplikací“ na portálu Microsoft Azure a otevřete ji.
#Klikněte na „Nová registrace“, zadejte aplikaci „Jméno“ a vyberte
:guilabel:"Účty v jakémkoliv organizačním adresáři (jakýkoliv Microsoft Entra ID tenant -
„Multitenant“ pod položkou „Podporované účty“ a klikněte na „Registrovat“.

.... obrázek: cloud_storage/app-registration.png
:alt:Registrace aplikace Microsoftu Azure

#Zapište si :guilabel:`ID aplikace (klienta)` a :guilabel:`ID adresáře (nájemce)`
bude použito při konfiguraci Odoo:ref:`<cloud-storage/microsoft/odoo>`.
#Klikněte na „Přidat certifikát nebo tajný klíč“ vedle „Základních přihlašovacích údajů klienta“.
:guilabel:`Nové tajné heslo“, pak „Přidat“.

.... důležité::
Pro bezpečnostní důvody nechte pole :guilabel:`Expires“ nastavené na „180 dnů (6 měsíců)“ nebo zvolte
kratší doba platnosti. Před vypršením tajného klíče je možné přidat nový klientský
aktualizace nastavení :ref:`Odoo <cloud-storage/microsoft/odoo>`, kde je nová hodnota
nezbytné.

#Kopírujte tajný klíč klienta s hodnotou :guilabel:`Value` a uchovávejte jej v bezpečí. Bude použit při
:ref:`konfigurace Odoo <clouddrive/microsoft/odoo>“.

.. obrázek: cloud_storage/app-client-secret.png
:alt:Přidání tajného klíče do aplikace Microsoft Azure

.._cloud-storage/microsoft/storage:

Účet úložiště
---------------

#Hledejte službu „Účty úložiště“, otevřete ji a klikněte na „Vytvořit“.
#Klikněte na „Vytvořit nový“ pod políčkem „Skupina zdrojů“ a zadejte
:guilabel:`Jméno“ a klikněte na „OK“.
#Zadejte jedinečný název účtu služby Storage, který si poznamenejte, protože bude použit při
:ref:`konfigurace Odoo <clouddrive/microsoft/odoo>“.
#Nastavte účet úložiště podle svých představ a poté klikněte na tlačítko „Zkontrolovat a vytvořit“.
:guilabel:`Vytvořit“.

.... obrázek:: cloud_storage/storage-account.png
:alt: Vytvoření účtu služby Microsoft Azure Storage

.._úložiště v cloudu/Microsoft/kontejner:

Kontejner
~~~~~~~~~

#Otevřete zdroj úložiště například vyhledáním jeho názvu a vyberte
pod záložkou „Úložiště“ v navigačním panelu.
#Zadejte jméno, poznamenejte si ho, protože bude použit při konfiguraci Odoo.
<úložiště v cloudu/Microsoft/Odoo> a klikněte na tlačítko „Vytvořit“.

.... obrázek: cloud_storage/storage-account-container.png
:alt: Vytvoření úložiště Microsoft Azure

.._úložiště v cloudu/Microsoft/zdroj:

Sdílení zdrojů
~~~~~~~~~~~~~~~~

#Vyberte „Sdílení zdrojů (CORS)“ pod „Nastavení“ účtu úložiště.
navigační lišta.
#Vytvořte první pravidlo služby CORS pro bloky.

   - :guilabel:`Povolené původní země“: „*“
   - :guilabel:`Povolené metody“: „GET“
   - :guilabel:`Povolené hlavičky“: „Typ obsahu“
   - :guilabel:`Vystavené hlavičky“: „Typ obsahu“
   - guilabel:Maximální věk: 0

#Vytvořte druhou pravidla služby CORS a klikněte na tlačítko „Uložit“:

   - :guilabel:`Povolené původní země“: „*“
   - :guilabel:`Povolené metody“: „PUT“
   - :guilabel:`Povolené hlavičky“: „content-type, x-ms-blob-type“
   - :guilabel:`Vystavené hlavičky“: „Content-Type, X-MS-Blob-Type“
   - guilabel:Maximální věk: 0

.... obrázek::cloud_storage/resource-sharing.png
:alt: Vytváření pravidel CORS pro účet úložiště Microsoft Azure

.._cloud-storage/microsoft/role:

Přidělování rolí
~~~~~~~~~~~~~~~

#Vyberte v navigačním panelu účtu úložiště položku „Kontrola přístupu (IAM)“ a klikněte
:guilabel:`Přidat“ a vyberte „Přidit přiřazení role“.
#Vyhledejte „Data přispěvatele objektů blob“ a klikněte na „Další“.

.. poznámka::
Odebrat zbytečnou „delete“ oprávnění lze vytvořením:
místo toho vyhledejte název vlastního role.

#Klikněte na tlačítko „Vybrat členy“, zadejte název aplikace, kterou jste již dříve registrovali.
<cloud-storage/microsoft/app>`, vyberte ji a klikněte na tlačítko :guilabel:`Vybrat“.
#Klikněte na „Zkontrolovat a přidělit“ dvakrát.

.... obrázek: cloud_storage/storage-account-role.png
:alt:Přidání člena do kontejneru

.._cloud-storage/microsoft/custom:

Vlastní role
***********

.. poznámka::
Tento krok je **volitelný**. Odstranění oprávnění ke smazání by však zabránilo tomu, aby jej mohl provést kdokoli.
přístupem k účtu cloudového úložiště prostřednictvím mazání souborů.

#Otevřete zdroj předplatného například vyhledáním jeho názvu a zvolte Access
kontrolu (IAM) v navigačním panelu, klikněte na „Přidat“ a vyberte „Přidat vlastní
role.
#Vyberte záložku „JSON“ a klikněte na „Upravit“. Zkopírujte následující kód a přidejte jej do
„ID předplatného“ v poli „předplatitelné rozsahy“ a změňte „název role“ („Vlastní role“) podle potřeby.
přetáhněte ji sem a klikněte na tlačítko „Uložit“.

.. kódový blok: json

   {
„vlastnosti“:
„název role“: „Vlastní role“,
„popis“: „“,
„přidělovatelné rozsahy“]:
"/subscriptions/subscription-id"
           ],
„povolení“: [
               {
„akce“: [„Microsoft.Storage/storageAccounts/blobServices/generateUserDelegationKey/action“]
"neakce": []
"akceS daty": ["Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read", "Microsoft.Storage/storageAccounts/blobServices/containers/blobs/add/action"]
"nepovolené akce": []
               }
           ]
       }
   }

..._cloud-storage/microsoft/odoo:

Konfigurace Odoo
------------------

#:ref:`Nainstalujte modul Cloud Storage Azure“:guilabel:`
#Otevřete aplikaci „Nastavení“ a vyberte v navigačním panelu „Cloudové úložiště“.
#Vyberte „Azure Cloud Azure“ jako nového poskytovatele úložiště.
přílohy.
#Vložte:

   - :ref:`jméno účtu pro ukládání dat <cloud-storage/microsoft/storage> v :guilabel:`Azure
pole „Název účtu“;
   - :ref:`název kontejneru <cloud-storage/microsoft/container>“ v :guilabel:`Azure Container
pole "Jméno";
   - :ref:`adresář (nájemce) <cloud-storage/microsoft/app>“ v :guilabel:`Azure Tenant
pole „ID“
   - ID aplikace (klienta) v Azure Client ID.
pole „ID“
   - hodnotu tajného klíče klienta (viz cloud-storage/microsoft/app) v Azure Client
Secret pole.

#Nastavte minimální velikost souboru (v bajtech) pro přílohy ukládané na Microsoft Azure.
