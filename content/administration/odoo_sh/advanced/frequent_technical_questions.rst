
.. _odoosh-advanced-frequent_technical_questions:

============================
Časté technické dotazy
============================

„Nepravidelně spouštěné úlohy neběží přesně v čase, kdy byly očekávány“
-------------------------------------------------------------------

Na platformě Odoo.sh nemůžeme garantovat přesný čas spouštění plánovaných akcí.

To je způsobeno tím, že na jednom serveru mohou být klienti více, a proto musíme zaručit každému zákazníkovi spravedlivý podíl ze serveru. Proto jsou plánované akce implementovány trochu jinak než na běžném Odoo serveru a prováděny na *nejlepší snahu* principu.

.. varování::
Nepočítejte s tím, že by se nějaká plánovaná akce spouštěla častěji než každých pět minut.

Existují „nejlepší postupy“ pro plánované akce?
-------------------------------------------------------

**Odoo.sh vždy omezuje dobu provádění plánovaných akcí (**také známých jako crony**).
Proto musíte při vývoji vlastních cronů brát tento faktor na zřetel.

Doporučujeme:

- Vaše plánované akce by měly pracovat s malými soubory dat.
- Vaše plánované akce by měly být spuštěny po zpracování každého balíčku.
Takže pokud je časový limit překročen, není třeba začínat znovu.
- Vaše plánované akce by měly být
„idemponentní“: musí být nezávislé
mohou způsobit nežádoucí účinky, pokud jsou užívána častěji, než se očekávalo.

.._změna-ip-adresy

Jak mohu automatizovat úkoly při změně IP adresy?
----------------------------------------------------------

Administrátoři projektu jsou o změnách IP adres informováni prostřednictvím služby Odoo.sh.
Dále je provedeno požadavku typu HTTP GET, když se mění IP adresa produkčního instanci.
cestu /_odoo.sh/ip-change s novou IP adresou jako parametrem dotazu
(„nový“), spolu s předchozím IP adresou jako další parametrem („starý“).

Toto zařízení umožňuje aplikovat vlastní akce na základě změny IP adresy.
(např. odeslání e-mailu, kontaktování aplikace firewallu, konfigurace objektů databáze atd.)

Pro bezpečnostní důvody je cesta do adresáře / _odoo.sh/ip-change přístupná pouze interně na platformě
sám sebe a v případě přístupu jiným způsobem vrátí odpověď „403“.

Příklad falešné implementace:

... kódový blok: Python

třída IPChangeController(http.Controller):

@http.route('/_odoo.sh/ip-change', autentizace='veřejná')
def ip_change(self, staré=None, nové=None):
_logger.info("IP adresa se změnila z %s na %s", stará, nová)
            # Pak proveďte požadovanou akci pro vaši konkrétní situaci, například aktualizujte
            # ir.config_parameter, poslat e-mail, kontaktovat externí službu firewallu prostřednictvím jejího API atd.
vrací hodnotu ok
