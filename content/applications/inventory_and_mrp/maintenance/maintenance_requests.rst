====================
Požadavky na údržbu
====================

.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`

Pro zachování funkčnosti strojů a pracovišť je často nutné provádět
údržbu na nich. To může zahrnovat i preventivní údržbu, která má za cíl zabránit poškození zařízení
opravné údržby, které se používají k opravě zařízení, která jsou poškozená nebo jinak
nepoužitelné.

V Odoo *Údržba* mohou uživatelé vytvářet požadavky na údržbu a sledovat jejich plánování a průběh.
výbavu a údržbu pracovišť.

Vytvořit požadavek na údržbu
==========================

Pro vytvoření nové žádosti o údržbu přejděte na: „Údržba aplikace --> Údržba -->
Zadání požadavku na údržbu“, a klikněte na „Nový“.

Začněte vyplňovat formulář zadáním popisného názvu do pole „Žádost“ (např.:
„Nástroj nefunguje“.

V poli „Vytvořeno“ se automaticky vyplní uživatel, který požadavek vytváří.
uživatele lze vybrat kliknutím na rozbalovací nabídku.

V rozevíracím seznamu „Pro“ vyberte „Zařízení“, pokud je požadavek na údržbu
vytvářený pro určité zařízení nebo: `Work Center`, pokud je vytvářen pro práci
centrum.

Podle volby v poli „Pro“ se název dalšího pole buď mění na
Vyberte buď „Zařízení“ nebo „Středisko“. Vyberte z roletkového seznamu
zařízení nebo pracoviště.

Pokud je nastavení „Vlastní údržbové listy“ zapnuté v nastavení aplikace „Údržba“,
Pole „Šablona listu“ se objeví pod poli „Zařízení“ nebo „Práce“.
Zadejte pole „Center“ a pokud je třeba, použijte toto pole k výběru listu, který má být vyplněn zaměstnancem.
Prováděním údržby.

Další pole se nazývá „Datum žádosti“ a je nastaveno výchozím datem, v němž byla
je vytvořen požadavek na údržbu. Tato data nelze změnit uživatelem.

V poli „Typ údržby“ vyberte možnost „Opravná“.
je určen k opravě již existujícího problému nebo možnost „Preventivní“ při požadavku
aby se podobné problémy v budoucnu neopakovaly.

Pokud je požadavek vytvářen k řešení problému, který se vyskytl během konkrétní výrobní objednávky
(MO), vyberte ji v poli „Výrobní objednávka“.

Pokud byl v poli „Výrobní objednávka“ vybrán |MO|, zobrazí se pole „Dodavatelská objednávka“.
je pod ním. Pokud se problém objevil v rámci konkrétního pracovního úkolu, uveďte jej do tohoto pole.

V poli „Tým“ vyberte tým údržby, který je zodpovědný za správu
žádost. Pokud je za konkrétní člen týmu zodpovědný někdo konkrétní, vyberte ho v poli „Odpovědná osoba“ .

Pole „Datum plánované údržby“ se používá k určení data, kdy by měla být provedena údržba.
místo a čas začátku. Vyberte datum kliknutím na pole pro otevření kalendáře
okno, vyberte den v kalendáři, zadejte hodinu a minutu do dvou polí
pod kalendářem a klikněte na tlačítko „Použít“ pro uložení data a času.

Pole :guilabel:`Doba trvání“ se používá k určení doby, po kterou je nutné provést údržbu.
Vyžádejte si čas. Použijte pole pro vstup textu k zadání času ve formátu „00:00“.

Pokud byl v poli „Pro“ vybrán „Středisko práce“, zobrazí se „Blokové středisko práce“.
za políčkem „Doba“ se objeví zaškrtávací políčko. Zapněte jej, abyste zabránili vydání pracovních příkazů nebo
další údržba, která je naplánovaná na určité pracoviště, zatímco požadavek na údržbu
je zpracovávána.

Komunikuje důležitost (nebo naléhavost) údržby pomocí pole :guilabel:`Priority`.
požadavek. Přiřaďte požadavku prioritu mezi nula a tři:
na požadované hvězdné číslo. Příkazy s vyšší prioritou se zobrazují nad ty s nižší
prioritou na kanbanovém tabuli používaném k sledování postupu požadavků na údržbu.

V dolní části formuláře v záložce „Poznámky“ zadejte všechny podstatné informace o
žádost o údržbu (proč k údržbě došlo, kdy k ní došlo atd.)

Karta Instrukce se používá k zahrnutí pokynů pro údržbu.
Provedena. Vyberte jednu ze tří možností a poté zahrňte pokyny podrobněji popsané níže:

- :guilabel:`PDF“: klikněte na tlačítko „Nahrát soubor“ a otevřete správce souborů zařízení.
a pak vyberte soubor ke stažení.
- :guilabel:`Google Slide“: Zadejte odkaz na :guilabel:`Google Slide“ do pole pro zadávání textu.
Přiblíží se po výběru možnosti.
- :guilabel:`Text`: zadejte pokyny do pole pro vkládání textu, které se objeví po výběru možnosti
vybrána.

.. obrázek: maintenance_requests/request-form.png
:align:center
:alt:Formulář požadavku na údržbu pro určité zařízení.

Žádost o údržbu procesu
===========================

Jakmile je vytvořen požadavek na údržbu, objeví se ve fázi „Nový požadavek“.
Stránku „Žádosti o údržbu“, kterou lze zobrazit kliknutím na:
--> Údržba --> Požadavky na údržbu.

Nároky na údržbu lze přesouvat mezi různými fázemi tahem a pložením.
po kliknutí na požadavek otevřít v nové záložce a poté vybrat požadovanou fázi
z ukazatele na pódiu, který je umístěn nad pravým horním rohem formuláře požadavku.

Úspěšné požadavky na údržbu by měly být přesunuty do fáze „Opraveno“, což znamená, že
Opravuje se konkrétní kus stroje nebo pracovního centra.

Nedokončené požadavky na údržbu by měly být přesunuty do fáze „Skartace“ s uvedením specifikovaného
Nemohla být opravena a musela být vyřazena z provozu.
