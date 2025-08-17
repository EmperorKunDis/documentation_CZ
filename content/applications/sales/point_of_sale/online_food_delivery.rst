====================
Doručování jídla online
====================

UrbanPiper je systém pro správu objednávek, který integruje s více platformami pro doručování jídla.
Sloučí objednávky ze všech propojených platforem do jediného rozhraní a zjednoduší
doručovací proces.

Podporované poskytovatele:

- „Careem <https://www.careem.com>“
- „Cari“
- „ChowNow <https://www.chownow.com>“
- „Deliveroo <https://deliveroo.co.uk/>“
- „DoorDash <https://www.doordash.com>“
- „EatEasy“
- „Glovo <https://glovoapp.com>“
- „Grubhub <https://www.grubhub.com>“
- „HungryPanda <https://www.hungrypanda.co>“
- „HungerStation <https://hungerstation.com>“
- „Jahez <https://www.jahez.net/>“
- „Just Eat“
- „Mrsool <https://mrsool.co>“
- „Ninja“
- „Noon Food <https://www.noon.com>“
- „Postmates <https://www.postmates.com>“
- „Rafeeq“
- „SkipTheDishes <https://www.skipthedishes.com/>“
- „Swiggy“
- „Talabat <https://www.talabat.com>“
- „UberEats <https://www.ubereats.com>“
- „Zomato <https://www.zomato.com>“

Konfigurace
=============

Předpoklady
-------------

Pokud chcete používat integraci UrbanPiper v produkčním prostředí, zkontrolujte následující
požadavky jsou splněny:

- Předplatné UrbanPiper: Předplatné UrbanPiper je nezbytné.

...... poznámka::
Pro jakékoliv obavy nebo dotazy týkající se vašeho předplatného UrbanPiper prosím kontaktujte nás.
odpovídající účetní spojený s vaší databází Odoo.

- **Požadavky na Odoo:**

  - **Předplatné Odoo:** Aktivní předplatné Odoo Enterprise je nutné. Předplatné Odoo Community nestačí
tuto integraci nepodporuje.
  - **Verze Odoo:** Odoo Enterprise verze 18.0 nebo vyšší.
  - Platforem Odoo: Všechny platfomy Odoo jsou podporovány, včetně Odoo Online, Odoo.sh a
Instalace on-premises.

- **Účet pro prodejce doručovací platformy:** Pro každou zemi je nutný registrovaný účet prodejce.
přepravní platformu (například Uber Eats, DoorDash, Careem, Deliveroo, Zomato).

... _online_potravinový_dodavatel/přístupové údaje:

Kreditní karta UrbanPiper
----------------------

#Získejte své údaje o uživateli Atlasu:

   #Přejděte do nastavení POS:ref:`<configuration/settings>`.
   #Přejděte dolů do sekce „Konfigurace pro doručovací služby“.
   #Klikněte na tlačítko „Vyplňte tento formulář a získáte uživatelské jméno a klíč API“ a vyplňte dotazník.
#„Přejděte do svého účtu Atlasu <https://atlas.urbanpiper.com>“ a získávejte klíč API a uživatelské jméno
kliknutím na:menu-selection:Nastavení --> Přístup k API.

.. obrázek: online_food_delivery/urban-piper-api.png
:alt: Přístup k aplikaci Atlas

Místo prodeje
-------------

#Zapněte nastavení „Urban Piper“:

   #Přejděte do nastavení POS:ref:`<configuration/settings>`.
   #Přejděte dolů do sekce „Konfigurace pro doručovací služby“.
   #Zkontrolujte nastavení „Městský piper“.

#Založil UrbanPiper.

   #Vyplňte pole „Uživatelské jméno“ a „API klíč“ svým uživatelským jménem a API klíčem UrbanPiper.
kreditní údaje <online_food_delivery/credentials>.
   #Vyberte požadované dodavatele v poli „Platforma pro doručování jídla“ pod
sekci „Místo Urban Piper“ (tj. Zomato, Uber Eats).
#Uložte nastavení.
#Klikněte na tlačítko „+ Vytvořit obchod“. To vytvoří novou lokaci na UrbanPiper
Atlasová platforma.

.. poznámka::
   - V polích „Ceník“ a „Daňová pozice“ je výchozí hodnota automaticky vybraná.
po uložení.
   - Pokud je vytvoření obchodu úspěšné, zobrazí se oznámení.
   - Vytváření obchodu může trvat 2-3 minuty, než se změny zobrazí v atlasu UrbanPiper.
platforma.
   - Obchod je automaticky pojmenován podle názvu vašeho prodejního místa.

.. obrázek: online_food_delivery/create-store.png
:alt:Nastavení připojení pro doručování jídla

Produkty
--------

Prodávat produkty jednotlivě.

#Přejděte na: „Prodejní místo“ - „Produkty“ - „Produkty“.
#Vyberte si produkt, abyste otevřeli jeho formulář.
#Přejděte do záložky „Prodejní místo“.
#Dokončete sekci „Městský pištěl“:

   - Do pole „Dostupné na rozvozu“ zadejte požadovaný POS.
   - Pokud chcete, nastavte pole „Druh jídla“ a zapněte „Je doporučené“.
a tlačítka „Je alkoholik“.

.. obrázek: online_food_delivery/produkt.png
:alt: kde je možné jednotlivý produkt nabídnout k dodání

Prodávat více produktů najednou pro doručování jídla.

#Přejděte na: „Prodejní místo“ - „Produkty“ - „Produkty“.
#Klikněte na ikonu seznamu (:icon:`oi-view-list`), abyste přepnuli do zobrazení seznamu.
#Vyberte produkty.
#Zadejte požadované místo prodeje do sloupce „Dostupné na rozvoz jídla“.

.. obrázek: online_food_delivery/produkty.png
:alt: Seznam produktů

.. poznámka::
   - Současná verze UrbanPiper nepodporuje kombinované produkty.
   - Jako obcházení problému vytvořte produkt a definujte varianty jako: doc: Attributes & Variants
<../prodej/produkty-cena/produkty/varianty>.

Synchronizace
---------------

Pro umožnit produkty na platformách pro doručování jídla, synchronizujte se svým účtem UrbanPiper:

#Přejděte do nastavení POS:ref:`<configuration/settings>`.
#Přejděte dolů do sekce „Dodavatel jídla“.
#Klikněte na tlačítko „Synchronizace menu“.

   - Datum posledního synchronizování pod tlačítkem „Vytvořit obchod“ a „Synchronizovat“
Aktualizace tlačítek menu.

.. poznámka::
   - Úspěšná synchronizace vyvolá oznámení.
   - Synchronizační proces může trvat 2–3 minuty, než se změny zobrazí v Atlasu UrbanPiper.
platforma.

Spustit web
-------

#Přejděte na záložku „Lokace“ („Locations“) ve vašem účtu Atlasu.
#Vyberte umístění pro aktivování a pak klikněte na „Požádat o spuštění“.

....... obrázek: online_food_delivery/go-live.png
:alt:Žádost o spuštění v záložce „Místa“ účtu Atlas

#V okně s upozorněním:

   #Vyberte platformu, kterou chcete aktivovat a klikněte na tlačítko „Další“.
   #Zadejte do příslušných polí hodnoty „ID platformy“ a „URL platformy“.
zprovoznit spojení mezi platformou a UrbanPiperem.
   #Klikněte na tlačítko „Žádost o spuštění“.

....... obrázek: online_food_delivery/go-live-parameters.png
:alt:Parametry pro spuštění

....... poznámka::
Chcete-li najít umístění a jeho :guilabel:`Platform ID` a :guilabel:`Platform URL`,

      #Klikněte na umístění, abyste otevřeli jeho nastavení.
      #Vlastnosti umístění jsou dostupné v záložce HUB.
#Zkontrolujte, zda je vaše poloha aktivní:

   #Přejděte na záložku „Lokace“ („Locations“) ve vašem účtu Atlasu.
   #Vyberte si poskytovatele v sloupci „Společnost“ a zkontrolujte stav tohoto
pro tuto lokalitu.

Průtok objednávek
==========

Objednávka zadaná přes konfigurovanou dodací platformu vyvolá upozornění. Tyto
objednávky, zobrazit seznam objednávek:

#Klikněte na tlačítko „Zobrazit objednávky“ v okně upozornění.
#Klikněte na ikonu tašky pro objednávky přes internet a poté na „New“.

.... obrázek:: online_food_delivery/cart-button.png
:alt:Tlačítko Kup teď

....... poznámka::
      - Kliknutím na tento ikonu zobrazíte počet objednávek v každé fázi: :guilabel:`New`.
:guilabel:`Průběžně“ a :guilabel:`Dokončeno“.
      - Tlačítko „Nový“ označuje nově vytvořené objednávky a tlačítko „Ve výrobě“ je pro
přijaté objednávky a „Dokončeno“ je pro objednávky připravené k dodání.

Pak

#Vyberte požadované pořadí.
#Klikněte na tlačítko „Přijmout“.
#Když je objednávka přijata, její stav se změní z „Objednáno“ na
:guilabel:'Přiznáno' a je automaticky zobrazeno na přípravě.

Když je objednávka připravena,

#Otevřete seznam objednávek.
#Vyberte objednávku.
#Klikněte na tlačítko „Připraveno k odeslání“. Stav objednávky se změní z
:guilabel:`Přiznání“ k :guilabel:`Jídlo připraveno“, a jeho :guilabel:`Stav“ se změní na
:guilabel:`Pokračující“ na :guilabel:`Zaplacené“.

Odmítnutí objednávky
---------------

Občas se může stát, že obchod nebo restaurace nebude chtít objednávku přijmout. V takovém případě otevřete
listového zobrazení

#Vyberte požadované pořadí.
#Klikněte na tlačítko „Odmítnout“.
#Vyberte jeden z důvodů ve vyskakovacím okně.

.. obrázek: online_food_delivery/reject-order.png
:alt:Odmítnout objednávku

.. důležité:
Objednávky služby **Swiggy** nelze odmítnout přímo. Při pokusu o jejich odmítnutí se zákazníkovi zobrazí
podporu kontaktovat restauraci. Podobně jako Deliveroo, Just Eat a Hunger Station
neumožňuje odmítnutí objednávky. Vždy postupujte podle pokynů příslušného poskytovatele
takových případů.
