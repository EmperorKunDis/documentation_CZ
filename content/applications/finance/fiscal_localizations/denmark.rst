=======
Dánsko
=======

Splnění požadavků dánského účetnictví: uchovávání a integrita dat
=============================================================================

Tato stránka popisuje, jak Odoo splňuje požadavky dánského účetního zákona.
Specificky se týká skladování a integritních záznamů o finančních transakcích a příjmech.
Odoo si uvědomuje důležitost dodržování dánských předpisů a implementovala pevná
opatření k zajištění bezpečnosti a souladu s předpisy u zákaznických dat.

.. důležité::
Registraci Odoo jako digitální účetní systém potvrdil Dánský obchodní úřad.
Autorizované osoby pod registračními čísly „fob585505“ a „fob441967“. Klienti musí splňovat určité
Podmínky pro využití výhod, které jsou uvedeny níže.


Základní požadavky dánského účetního zákona
----------------------------------------------

Dánský účetní zákon (DBA) definuje „požadavky na digitální systémy pro vedení účetnictví“.
<https://www.erhvervsstyrelsen.dk/krav-til-digital-bogfaring/>

- **Uchovávejte transakční data a faktury:** Uchovejte všechna zaznamenaná transakční data a faktury
a) jsou po dobu nejméně pěti let od konce účetního období, ke kterému se vztahují, pokryta ustanovením § 3.

- Zajistit integritu dat: zabránit zákazníkovi v úpravě, zpětného datování nebo odstranění zaznamenaných transakcí.

- **Udržujte přístupnost dat:** Uchovávejte všechny zaznamenané transakce v strukturovaném a strojově čitelném formátu
ať už je zákazník v dobrém nebo špatném stavu, bankrotu či likvidaci.

- **Poskytnout schopnost dešifrování:** Zajistit, aby byly šifrované účetní záznamy a faktury rozšifrovány
do strukturovaného a čitelného formátu.

Odoo Compliance
---------------

Registrace systému Odoo jako digitálního standardu účetních systémů u Dánského obchodního úřadu
potvrzuje, že Odoo splňuje platná kritéria pro digitální účetní systém v Dánsku.
v souladu s požadavky zákona o účetnictví DBA.

Aby však mohli využívat všechny požadované záruky pro digitální účetní systém v Dánsku,
Klient musí splnit několik podmínek.

Podmínky plného souladu s DBA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Zákazník používá účetnictví Odoo na platformě Odoo SaaS (Odoo Online).
- Zákazník má aktivní předplatné Odoo (např. Standard nebo Custom Plan) a jeho databáze je
spravované oficiálně registrovanou firmou „Odoo Accounting Firm <https://www.odoo.com/accounting-firms>“;
- Zákazník se zdrží jakýchkoliv úprav nebo akcí směřujících k narušení neměnnosti systému.
sledovatelnost nebo bezpečnostní kontroly.

.. poznámka::
Uživatelé produktů Odoo mimo tyto podmínky jsou zodpovědní za zajištění vlastních
splnění Dohody o zamezení dvojího zdanění.

Pokud jsou splněny výše uvedené podmínky, požadavky smlouvy o zamezení dvojího zdanění jsou splněny prostřednictvím
Popisované procesy v následujících částech.

Nepřenosné záznamy transakcí
-----------------------------

- Jakmile jsou transakce zaznamenány, nelze je smazat prostřednictvím uživatelského rozhraní.
- Všechny změny jsou zaznamenány a poskytují tak úplný záznam o všech provedených změnách.
- Historicky datované záznamy mohou být vytvořeny, Odoo zaznamenává datum a čas vzniku záznamu.

Bezpečné uložení dokumentů
-----------------------

- Pokladní doklady a digitální poukázky jsou uloženy jako přílohy a integrovány do databáze, což zajišťuje jejich
Jsou zahrnuty do záloh.
- Uložené dokumenty nelze smazat.
- Zcela podporujeme ukládání povinných digitálních poukázek, jak je definováno dánskými předpisy.

Dostupnost kontinuálních dat
----------------------------

- Klienti s aktivními předplatnými mohou všechny transakce a digitální poukázky zobrazit prostřednictvím Odoo.
- Ať už jde o krach, likvidaci nebo převod obchodu, Odoo může poskytnout přístup ke všem transakcím.
a digitální dárkové kupony pro bývalé klienty po dobu šesti let (viz:ref:`lokalizace/dánsko/životní cyklus dat`).

Automatické vývozy dat a bezpečné uložení
----------------------------------------

- Odoo Accounting neimplementuje automatické mazání nebo archivace zaznamenaných transakcí, takže pokud má zákazník
Už šest let eviduje transakce, a tak ve skladbě účetnictví Odoo zůstává zachována celých šest let historie.
- Jak je uvedeno v „SLA Odoo Cloud Hosting <https://www.odoo.com/cloud-sla>“
„Politika ochrany osobních údajů společnosti Odoo“ (<https://www.odoo.com/privacy>), na které je Odoo Cloud založena, používá denní snímky
zálohy, které nelze individuálně měnit nebo smazat ani na žádost zákazníka, a zajišťují tak jejich integritu.
- Všechny dokumenty a faktury uložené v databázi zálohy jsou k dispozici jako standardní archiv ZIP, který je přiložen
dump SQL.

.._lokalizace/dánsko/životní cyklus dat:

Řízení životního cyklu dat
-------------------------

- Konfigurace zálohování databáze Odoo je k dispozici v běžném formátu SQL a zahrnuje všechny nahrávky.
transakcí.
- Smlouva o údržbě cloudu „Odoo Cloud Hosting SLA <https://www.odoo.com/cloud-sla>“ zaručuje tři měsíce zálohovaných dat pro všechny
aktivních zákazníků. Jako zvláštní záruka pro dánské zákazníky podléhající DBA a splňující podmínky
vyznačené výše, poslední záloha v cloudu bude uchovávána po dobu šesti let, jakmile se rozhodnou
zrušit své předplatné na Odoo Cloud, aby splnili požadavky přílohy číslo 1, číslo 4 vyhlášky číslo 97.

Dešifrování
----------

Data zákazníků aplikace Odoo Accounting v cloudu jsou uložena vždy zašifrovaně (zašifrování při odpočinku).
úrovně zálohování). Když jsou zálohy obnoveny, jsou automaticky dešifrovány a poskytnuty v dešifrované podobě.
standardní formáty pro uživatele: exporty do SQLu + archiv všech připojených dokumentů (úložiště souborů).
