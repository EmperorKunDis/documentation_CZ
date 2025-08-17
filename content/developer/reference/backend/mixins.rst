
.._odkaz/směs:

=========================
Mixiny a užitečné třídy
=========================

Odoo implementuje několik užitečných tříd a rozšíření, které vám usnadní přidání
často používané chování na vašich objektech. Tento průvodce popíše většinu z nich s
příklady a použití.

.. odkaz/směsi/e-mail:

Messengerové funkce
==================

.._odkaz/směsice/pošta/chat:

Správa zpráv
---------------------

Základní systém zasílání zpráv
~~~~~~~~~~~~~~~~~~~~~~

Přidání funkcí pro zasílání zpráv do vašeho modelu je velmi snadné. Jednoduše dědění
mixinu „mail.thread“ a přidání do vašeho formuláře prvek „<chatter/>“.
Výhled vám rychle pomůže nastartovat. Chatovací prvek podporuje
možnosti ovládání chování formuláře:

* „otevřít přílohy“: Zobrazuje sekce „Přílohy“ rozbalená.
* „reload_on_attachment“: Obnoví pohled na formulář, když jsou přidány nebo odstraněny přílohy
* „reload_on_follower“: Obnoví formulář, když jsou aktualizovány sledované stránky
* „reload_on_post“: Znovu načítá formulář, když jsou nové zprávy publikovány

Příklad:

Vytvořme jednoduchý model, který bude představovat služební cestu. Organizace
Tento typ cesty obvykle zahrnuje hodně lidí a mnoho diskusí, takže
přidat podporu pro výměnu zpráv na modelu.

.. kódový blok:: python

class BusinessTrip(models.Model):
_name = 'podnikání.cesta
dědí se z mail.thread
_popis = 'Obchodní cesta'

jméno = fields.String()
partner_id = fields.many2one('res.partner','Zodpovědný')
hosté = pole.MnohoNaMnoho('res.partner', 'Hosté')

V podobě formuláře:

... kódový blok :: XML

<zaznamenání id="cestovní formulář pro obchodní cesty" model="ir.ui.view">
<položka jméno>business.trip.form</položka>
<field name="model">business.trip</field>
<položka jméno="arch" typ="xml">
<form string="Obchodní cesta">
<!-- Váš obvyklý pohled na formulář zde
                    ...
Pak přichází integrace chatu s možnostmi, které si můžete nastavit -->


</položka>


Jakmile přidáte podporu chatovacího rozhraní do svého modelu, uživatelé mohou snadno přidat zprávy
nebo poznámky uvnitř jakéhokoliv záznamu vašeho modelu; každá z nich bude odesílat
upozornění (pro všechny uživatele zprávy, pro zaměstnance (*base.group_user*))
uživatelé pro interní poznámky). Pokud je vaše e-mailová brána a adresa pro zachycení správně
pokud je tato konfigurace nastavena, budou tyto upozornění odeslána na e-mail a lze na ně přímo reagovat.
z vašeho poštovního klienta. Automatický směrovací systém odpověď odešle na
správná vlákna.

Serverová strana obsahuje několik funkcí, které vám pomohou snadno odesílat zprávy.
spravovat své fanoušky na profilu:

...rubrika: Vkládání příspěvků

... metoda: post_message(self, tělo = '', předmět = None, typ zprávy = 'notification', podtyp = None, rodičovské ID = False, přílohy = None, **klauzule)

Vložte nový příspěvek do stávající diskuze a vrátí se vám nová
ID zprávy v poštovním serveru.

:param str | Značkový tělo: Tělo zprávy. Bude v případě použití proměnné „str“ uvedeno ve značkách.
objekt třídy Markup pro obsah HTML.
:param str typ_zprávy: viz pole zprávy.message_type
:param int parent_id: odpověď na předchozí zprávu přidáním
partnerovi rodičů v případě soukromé diskuse
:param list(rozsah(pár(str, str))) attachments: seznam příloh v podobě párů ve tvaru
„(název, obsah)“, kde obsah není kódován v Base64
:parametrem bool body_is_html: určuje, zda se má tělo považovat za HTML i v případě, že je to řetězec.
:param \*\*args: přidané klíčové slovo bude použito jako výchozí hodnota sloupce
nový záznam pro zprávu
:vrací: ID nově vytvořené zprávy
:rtype: int

... metoda: post_message_with_view(views_or_xmlid, **kwargs)

Metoda, která pomáhá odeslat e-mail nebo zprávu pomocí ID pohledu.
vykreslovat pomocí motoru ir.qweb. Tento způsob je samostatný, protože
v šabloně a kompozitní vrstvě není nic, co by umožňovalo zpracování
zobrazovat stránky v sekvencích. Tato metoda pravděpodobně zmizí, když budou používat šablony
zobrazovat v uživatelském rozhraní.

:param str nebo „ir.ui.view“: vnější ID nebo záznam pohledu
by měl být zaslán

... metoda: post_message_with_template(šablona_id, **parametry)

:Metoda, která pomáhá odeslat e-mail s šablonou

:param template_id: ID šablony, kterou chcete použít k vytvoření těla zprávy


..rubrice: Přijímání zpráv

Tyto metody se volají při zpracování nové zprávy na poštovním serveru.
E-maily mohou být buď nová vlákna (pokud dorazí přes :ref:`alias <reference/mixins/mail/alias>`)
nebo prostě odpovědi z již existujícího vlákna. Přebírání jim umožňuje nastavit hodnoty
záznamu vlákna podle některých hodnot z e-mailu samotného (tj. aktualizace
datum nebo e-mailovou adresu, přidat jako sledované osoby adresy CC atd.

... metoda: message_new(msg_dict, custom_values = None)

Voláno funkcí „message_process“ při příjmu nové zprávy
pro daný model vlákna, pokud zpráva nepatřila do
existující vlákno.

Výchozí chování je vytvoření nového záznamu odpovídajícího
model (na základě několika velmi základních informací získaných ze zprávy).
Případné další chování lze implementovat přepsáním této metody.

:param dict msg_dict: mapa obsahující podrobnosti o e-mailu
přílohy. Podrobnosti naleznete v metodě „message_process“ a „mail.message.parse“.
:parametrem je volitelný seznam hodnot, které lze přidat
hodnoty pole, které mají být předány metodě create(), když vytváří nový záznam o vlákně.
buďte opatrní, tyto hodnoty mohou přebít jakékoliv jiné hodnoty
zpráva
:rtype: int
:vrací: ID nově vytvořeného objektu vlákna

... metoda: message_update(msg_dict, update_vals=None)

Voláno funkcí „message_process“ při příjmu nové zprávy
pro existující vlákno. Výchozí chování je aktualizace záznamu
s hodnotami „update_vals“ z e-mailu, který přišel.

Pokud chcete implementovat další chování, můžete tento článek
metoda.

:param dict msg_dict: mapa obsahující podrobnosti o e-mailu a přílohy;
viz „message_process“ a „mail.message.parse()“, kde najdete podrobnosti.
:parametrem update_vals: Dikta obsahující hodnoty, které mají být aktualizovány u zadaných záznamů
jejich identifikátory; pokud je seznam prázdný nebo neexistuje, žádná operace zápisu není provedena.
:výstup: True

..rubrika: Správa fanoušků

... metoda: message_subscribe(partner_ids = None, channel_ids = None, subtype_ids = None, force = True)

Přidejte do záznamů sledujících partnery.

:param list(int) partner_ids: IDy partnerů, které se budou odběratelům zobrazovat
do rekordu
:param seznam(int) channel_ids: ID kanálů, které budou odběratelům přidány
do rekordu
:param list(int) subtype_ids: ID podtypů, které kanály/partnery
bude přiřazena (výchozí hodnota je výchozí podtyp, pokud je „None“).
:param force: pokud je True, smažte stávající sledující před vytvořením nového
používáním podtypu, který je uveden v parametrech
:výstup: Úspěch/Neúspěch
:rtype: bool


... metoda: message_unsubscribe(partner_ids=None, channel_ids=None)

Odeberte partnera z seznamu fanoušků alba.

:param list(int) partner_ids: IDy partnerů, které se budou odběratelům zobrazovat
do rekordu
:param seznam(int) channel_ids: ID kanálů, které budou odběratelům přidány
do rekordu
:výstup: True
:rtype: bool


... metoda: message_unsubscribe_users(user_ids = None)

Záložka na zprávy o přihlášení uživatelů.

:param seznam(int) uživatelských ID: ID uživatelů, kteří budou odhlášeni
do databáze; pokud je hodnota None, odhlásí se aktuální uživatel.
:výstup: True
:rtype: bool

Záznam změn
~~~~~~~~~~~~~~~

Modul „pošta“ přidává silný systém sledování políček, který vám umožní
zaznamenávat změny v konkrétních polích záznamu.
na pole, jednoduše nastavte atribut sledování na hodnotu True.

Příklad:

Změňme si název a odpovědnost za naše obchodní cesty:

.. kódový blok:: python

class BusinessTrip(models.Model):
_name = 'podnikání.cesta
dědí se z mail.thread
_popis = 'Obchodní cesta'

name = fields.Char(tracking=True)
partner_id = fields.many2one('res.partner','Zodpovědný',
tracking=True)
hosté = pole.MnohoNaMnoho('res.partner', 'Hosté')

Od teď se každá změna jména nebo odpovědné osoby zaznamenává do poznámky.
Ve zprávě se pak objeví pole „jméno“ s uvedeným jménem.
aby poskytla více kontextu k oznámení (i když jméno nebylo
změna).

Podtypy
~~~~~~~~

Podtypy vám poskytují více detailů při kontrole zpráv. Podtypy fungují jako třídění
systém oznámení, který umožňuje odběratelům dokumentu přizpůsobit si
podtyp oznámení, které si přejí dostávat.

Podtypy vytváříte jako data ve vašem modulu; model má následující pole:

„jméno“ (povinné pole) – :třída: `~odoo.fields.Char`
název podtypů bude zobrazen v nastavení oznámení.
popup
„popis“ – :třída: „odoo.pole.Char“
popis, který bude přidán do zprávy spojené s touto
podtyp. Pokud je prázdný, bude přidán místo názvu
„interní“ – :třída:`~odoo.fields.Boolean
zprávy s vnitřními podtypy budou viditelné pouze zaměstnancům.
členové skupiny „uživatelé základní skupiny“
„parent_id“ – :třída:`~odoo.fields.Many2one
přidružené typy odkazů pro automatické přihlášení, například podtyp projektu.
úkolu, je automaticky přiřazen k podtypům úkolů prostřednictvím této
projektu se přiřadí ke všem úkolům tohoto projektu.
podtypy, které byly nalezeny pomocí rodičovského podtypu
„vztahové pole“ – :třída: „~odoo.pole.Char“
například při propojování typů projektu a úkolů.
pole je položka projektu v úlohách
„res_model“ – :třída: „~odoo.fields.Char“
podtyp se vztahuje na určitý model; pokud je hodnota False, tento podtyp se vztahuje na všechny modely
„výchozí“ – :třída:`~odoo.fields.Boolean
jestli je podtyp aktivován automaticky při přihlášení
„sled“ – :třída: „~odoo.pole.integer“
slouží k uspořádání podtypů v nastavení oznámení.
„skrytý“ – :třída: `odoo.fields.Boolean`
zda je podtyp skrytý v nastavení oznámení.


Přiřazení podtypů sledovaným polím umožňuje přihlásit se k různým typům
upozornění podle toho, co by mohlo uživatele zajímat. K tomu používá
může přehrát funkci „_track_subtype()“:

... metoda: _track_subtype(hodnoty vstupu)

Řešením je dát podtyp vyvolaný změnou v záznamu
hodnotám, které byly aktualizovány.

:parametrem seznamu inicializačních hodnot: původní hodnoty záznamu; pouze změněné pole
Jejich přítomnost je v slovníku
:návratová hodnota: plná externí identifikace podtypů nebo False, pokud není spuštěn žádný podtyp


Příklad:

Přidejme do našeho příkladového třídy pole „stát“ a vyvoláme notifikaci
s konkrétním podtypem, pokud se hodnota pole změní.

Nejprve definujme podtyp:

... kódový blok :: XML

<záznam id="změna stavu" typu "mail.message.subtype">
<pole název="jméno">Potvrzená cesta</pole>
<položka název="res_model">business.trip</položka>
<vlastnost jméno="default" hodnota="True"/>
<položka jméno="popis">Potvrzení obchodní cesty!</položka>



Pak je potřeba přepsat funkci „track_subtype()“. Tato funkce
je vyvolán sledovacím systémem, aby věděl, který podtyp se má použít v závislosti
na současnou změnu. V našem případě chceme využít nový lesklý
podtyp, když pole „stav“ změní hodnotu z *návrh* na *potvrzeno*:

.. kódový blok:: python

class BusinessTrip(models.Model):
_name = 'podnikání.cesta
dědí se z mail.thread
_popis = 'Obchodní cesta'

name = fields.Char(tracking=True)
partner_id = fields.many2one('res.partner','Zodpovědný',
tracking=True)
hosté = pole.MnohoNaMnoho('res.partner', 'Hosté')
stav = pole.Výběr([('návrh', 'Nový'), ('potvrzeno', 'Potvrzené')])
tracking=True)

def _track_subtype(self, inicializační hodnoty):
                # init_values obsahuje hodnoty polí před změnami.
                #
                # Aplikované hodnoty lze získat na záznamu, protože jsou již připravené.
                # v mezipaměti
self.ensure_one()
pokud je v hodnotách inicializace pole state a stav se rovná confirmed:
vrací sebe sama
návrat super(BusinessTrip, self)._track_subtype(init_values)

Přizpůsobení oznámení
~~~~~~~~~~~~~~~~~~~~~~~~~

Při odesílání oznámení uživatelům se může hodit přidat tlačítka
šablonu, která umožňuje provádět rychlé akce přímo z e-mailu. I jednoduchá tlačítka
Přímé propojení na formulář záznamu může být užitečné, ale většinou
nechcete, aby se tlačítka zobrazovala uživatelům portálu.

Systém oznámení umožňuje přizpůsobit šablony oznámení následujícím způsobem
způsoby:

- Zobrazit tlačítka přístupu: tyto tlačítka jsou vidět na horní části notifikace.
e-mailem a umožnit příjemci přímý přístup k formuláři záznamu.
- Zobrazení tlačítka Follow: Toto tlačítko umožňuje příjemci
přímé rychlé předplatné z rekordu
- Zobrazit tlačítka „Odhlásit se“: tyto tlačítka umožňují příjemci
: přímo rychle odhlásit z rejstříku
- Zobrazit *Vlastní akční tlačítka*: tyto tlačítka jsou voláním konkrétních tras
a umožní vám provádět některé užitečné akce přímo z e-mailu (např.
přeměna vedení na příležitost, ověření výdajového listu
Expense Manager, apod.

Tato nastavení tlačítka můžete aplikovat na různé skupiny, které si můžete definovat.
sám tím, že převezmete funkci „_notify_get_groups“.

... metoda: _notify_get_groups(zpráva, skupiny)

Řešením je dát podtyp vyvolaný změnou v záznamu
hodnotám, které byly aktualizovány.

:param „zpráva“: „mail.message“ zprávu, která je v tuto chvíli odesílána
:param seznam(soubor) skupin: seznam tuplů ve tvaru (skupina, funkce skupiny, data skupiny), kde:

skupina
je identifikátor, který se používá jen proto, aby bylo možné jej přehrát a upravit.
skupiny. Výchozí skupinou je „uživatel“ (adresáti spojení s uživatelem zaměstnance).
„portál“ (adresáti propojení s uživatelem portálu) a „zákazník“ (adresáti, kteří nejsou
(např. uživatelské skupiny) nebo přidat další uživatele.
spojené s rezervační skupinou, jako jsou HR manažeři, aby bylo možné nastavit specifické tlačítka akcí
jim.
skupinová funkce
je funkční ukazatel, který jako parametr přijímá záznam partnera.
Metoda bude aplikována na příjemce, aby se zjistilo, patří-li k dané skupině.
skupině nebo ne. Pouze první shodný výraz je uchován. Hodnotící pořadí je
pořadí v seznamu.
skupinová data
je toto pole obsahem seznamu parametrů pro e-mail s upozorněním, který má následující
možné klíče - hodnoty:

          - má přístup k tlačítku
zda se v e-mailu zobrazí dokument Access. Pravda je výchozím nastavením
nové skupiny, False pro portál/zákazníka.
          - tlačítko
seznam s URL a titulem tlačítka
          - has_button_follow
zobrazit možnost Sledovat e-mail (pokud adresát není aktuálně přihlášený).
nových skupin, True pro staré.
portál / zákazník.
          - button_follow
seznam s URL a titulem tlačítka
          - has_button_odhlásit
zda zobrazit možnost Odhlásit se v e-mailu (pokud adresát aktuálně sleduje vlákno).
Pravda výchozí pro nové skupiny, nepravda pro portál/klienta.
          - tlačítko Odhlásit se
seznam s URL a titulem tlačítka
          - akce
seznam akčních tlačítek, které mají být zobrazeny v e-mailové notifikaci.
Každá akce je diktát, který obsahuje URL a název tlačítka.

:návratová hodnota: plná externí identifikace podtypů nebo False, pokud není spuštěn žádný podtyp


URL v seznamu akcí může být automaticky vygenerován voláním
Funkce "_notify_get_action_link()":


... metoda: _notify_get_action_link(self, link_type, **kwargs)

Vytvořit odkaz pro daný typ na aktuální záznam (nebo na konkrétní)
zaznamenat, pokud jsou nastaveny argumenty „model“ a „res_id“.

:param str typ_odkazu: typ odkazu, který má být vytvořen; může být libovolným z těchto hodnot:

„výhled“
odkaz na zobrazení záznamu
„přidělit“
přiřadit uživatele, který se zaregistroval, do pole „user_id“
pokud existuje,
„sledovat“
sám o sobě vysvětlitelný
„odhlásit se“
sám o sobě vysvětlitelný
„metoda“
:volat metodu na záznamu, název metody by měl být
Prováděno jako metoda kwargu „metoda“.
„nový“
otevřít prázdný formulář pro nový záznam, můžete také specifikovat
Specifickou akci poskytnutím jejího ID (ID v databázi nebo plně vyřešené).
externí ID (v argumentu action_id

:vrací: odkaz typu vybraného pro záznam
:rtype: str

Příklad:

Přidejme si do notifikace o změně stavu cesty na služební cestu vlastní tlačítko.
Tlačítko tento stav obnoví na Návrh a bude viditelný pouze pro členy
z (fiktivní) skupiny Cestovní manažer („business.group_trip_manager“).

.. kódový blok:: python

class BusinessTrip(models.Model):
_name = 'podnikání.cesta
dědí se z mail.thread a mail.alias.mixin
_popis = 'Obchodní cesta'

            # Předchozí kód zde

def action_cancel(self):
self.write({'state': 'návrh'})

def _notify_get_groups(self, zpráva, skupiny):
"Zpracujte příjemce služby Trip Manager, kteří mohou zrušit cestu na poslední chvíli.
Ve skutečnosti, pokud se vám podaří získat nějaké peníze, můžete si je užívat, ale ne na úkor zábavy.
groups = super(BusinessTrip, self)._notify_get_groups(zpráva, skupiny)

self.ensure_one()
pokud se stav objektu rovná „potvrzený“:
app_akce = sebevražedný odkaz na metodu
metoda="action_cancel")
trip_actions = [{'url': app_action, 'title': _('Zrušit')}]

nová_skupina = (
'správce zájezdu',
lambda partner: některý z
user.sudo().has_group('business.group_trip_manager')
for uživatel v partner.user_ids
                    ),
{'akce': cestovní akce}
                )

vrací seznam skupin, do kterého je přidána nová skupina


Pozor, že bych mohl definovat svou funkci hodnocení mimo tento kód.
metoda a definovat globální funkci k tomu namísto lambdy.
z důvodu, aby byly tyto dokumentační soubory stručnější a méně složité
že je někdy nudná, volím raději tu první než tu druhou.

Převzetí výchozích hodnot
~~~~~~~~~~~~~~~~~~~

Existuje několik způsobů, jak upravit chování modelu „mail.thread“.
včetně, ale nejen:

„_mail_post_access“ – atribut třídy „~odoo.models.Model“
požadované oprávnění k vkládání zpráv do modelu.
výchozí je „write“ a lze nastavit i na „read“.

Kontextové klíče:
Tyto kontextové klíče lze použít k určitému ovládání funkcí „mail.thread“.
jako automatické přihlášení nebo sledování pole během volání metody „vytvořit()“
„write()“ (nebo jiný metod, kde se může hodit).

    - „mail_create_nosubscribe“: při vytváření nebo odesílání zprávy se nezaregistruj
současného uživatele do vlákna záznamu
    - „mail_create_nolog“: při vytváření nezaznamenávejte automatické „<Document>
„Vytvořeno“
    - „mail_notrack“: při vytváření a psaní neprovádějte sledování hodnot
vytváření zpráv
    - „tracking_disable“: při vytváření a psaní nevykonávejte žádné funkce MailThread
(automatické předplatné, sledování, pošta, ...).
    - „mail_auto_delete“: automatické odstranění oznámení e-mailu; Pravda výchozím nastavením
    - „mail_notify_force_send“: pokud bude méně než 50 e-mailových upozornění k odeslání
je odesílá přímo, namísto použití fronty; Pravda výchozí hodnotou
    - „mail_notify_user_signature“: přidat podpis aktuálního uživatele
e-mailové notifikace; jsou pravdivé


.. odkaz/směsice/pošta/přezdívka:

Alias e-mailu
----------

Alias je konfigurovatelná e-mailová adresa, která je spojena s určitým záznamem.
(která obvykle dědí „mail.alias.mixin“), která vytváří nové záznamy při
Kontaktujte nás na emailu. Jsou snadným způsobem, jak získat přístup k systému
venku, takže uživatelé nebo zákazníci mohou rychle vytvářet záznamy ve vašem
databáze bez nutnosti přímého připojení k Odoo.

Aliasy versus příchozí poštovní brána
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Někteří lidé používají příchozí poštovní bránu pro stejný účel. I tak je třeba
Pokud je správně nakonfigurovaný e-mailový server, může používat i aliasy.
univerzální doména bude dostačující, protože všechny směrování budou prováděna uvnitř Odoo.
Aliasové adresy mají několik výhod oproti Mail Gateway:

* Snadněji konfigurovatelný
    * Jediný vstupní brána může být použita mnoha přezdívkami, což zabraňuje tomu, aby
nastavit více e-mailových adres na doméně (vše je nastaveno
uvnitř Odoo
    * Není potřeba mít přístup do systému, abyste si mohli nastavit alias
* Větší soudržnost
    * Konfigurovatelné na příslušném záznamu, nikoli v podnabídce Nastavení
* Náročnější je přehrát serverovou část
    * Model mixinu je navržen tak, aby se dal rozšiřovat od začátku, což vám umožní
získávat užitečná data z příchozích e-mailů snadněji než s poštou
brána.


Podpora aliasů pro integraci
~~~~~~~~~~~~~~~~~~~~~~~~~

Aliasy se obvykle nastavují na základním modelu, který pak vytvoří konkrétní
zaznamenávat při kontaktování e-mailem. Například projekt má aliasy pro vytváření úkolů
nebo problémy, prodejní tým má přezdívky, které generují leady.

.. poznámka: Model, který bude vytvořen pod aliasem **musí být dědičný od
„model mail_thread“.

Podpora aliasů je přidána dědičením „mail.alias.mixin“; tento mixin bude
generovat nový záznam „mail.alias“ pro každý záznam rodičovské třídy,
je vytvořen (například každý záznam „projekt.projekt“ má svůj „mail.alias“
zaznamenaná při vytváření záznamu).

.. poznámka: Aliasy lze vytvářet i ručně a podporovat je jednoduchým
:klasu: `odoo.fields.Many2one`. Tento průvodce předpokládá, že chcete mít
více kompletní integrace s automatickým vytvářením aliasu a záznamem specifického
výchozí hodnoty, atd.

Oproti dědičnosti „mail.thread“ je „mail.alias.mixin“ **vyžadován**
specifické přesměrování, aby fungovalo správně. Tyto přesměrování budou specifikovat hodnoty
vytvořeného pseudonymu a o typu záznamu, který musí vytvořit.
Některé výchozí hodnoty, které tyto záznamy mohou mít v závislosti na rodičovském objektu:

.. metoda: _get_alias_model_name(vstupy)

Vrátí název modelu pro přezdívku. Při příchozích e-mailech, které nejsou
Odpovědi na existující záznamy způsobí vytvoření nového záznamu
Tento aliasový model má hodnotu, která závisí na „vals“, což je slovník
hodnoty předané metodě „create“ při vytváření záznamu tohoto modelu.

:param vals: hodnoty nově vytvořeného záznamu, ve kterém budou uloženy
přezdívka
:vrácená hodnota: název modelu
:rtype: str

... metoda: get_alias_values

Vracené hodnoty vytvářejí alias nebo píší na něj po jeho vytvoření.
vytvoření. I když není úplně povinné, je obvykle vyžadováno k tomu, aby
že nově vytvořené záznamy budou spojeny s rodičem aliasu (tj.
(vytváření úkolů v správném projektu) nastavením slovníku
v poli „alias_defaults“ výchozí hodnoty v příkazu alias.

:vrací: slovník hodnot, které se zapsaly do nové vlastní proměnné
:rtype: slovník

Přesměrování „_get_alias_values()“ je zvláště zajímavé, protože umožňuje
upravit chování svých aliasů snadno. Mezi pole, která lze nastavit
Zájem je především o tyto pseudonymy:

„alias_name“ – :třída:`~odoo.fields.Char`
jméno aliasu e-mailové adresy, například „práce“ pokud chcete zachytit e-maily s tématem práce
<jobs@example.odoo.com>
„alias_user_id“ - :třída: „~odoo.fields.Many2one“ („res.users“)
vlastník záznamů vytvořených při přijímání e-mailů na tuto adresu.
pokud tento prvek není nastaven, systém se pokusí najít vlastníka
na základě odesílacího (z)adresy nebo použije účet správce.
pokud se pro danou adresu nenajde žádný uživatel systému
„alias_defaults“ – :třída: „~odoo.fields.Text“
Pythonová slovníkové hodnota, která bude vyhodnocena k poskytnutí
výchozí hodnoty při vytváření nových záznamů pro tento alias
„alias_force_thread_id“ – :třída: „~odoo.fields.Integer“
volitelné ID vlákna (záznamu), ke kterému budou směřovány všechny příchozí zprávy.
Pokud je nastaveno, tato funkce deaktivuje odpověď na přílohu.
vytváření nových rekordů.
„alias_contact“ – :třída: „~odoo.fields.Selection“
Zásady pro odeslání zprávy na dokument pomocí poštovního brány

    - *každý*: každý může přispívat
    - *partner*: pouze ověření partneři
    - *sledovatelé*: pouze sledovatelé souvisejícího dokumentu nebo členové následujících kanálů

Poznámka: Aliasy využívají dědičnost delegace (viz reference/orm/inheritance).
Tedy že se jméno uloží do jiné tabulky a
přístup k těmto polím přímo z vašeho rodičovského objektu. To umožňuje
aby jste si svůj přezdívku mohli snadno nastavit z pohledu formuláře.

Příklad:

Přidejme do naší třídy pro podnikání aliasy, abychom mohli vytvářet výdaje na cestách.
e-mailová adresa.

.. kódový blok:: python

class BusinessTrip(models.Model):
_name = 'podnikání.cesta
dědí se z mail.thread a mail.alias.mixin
_popis = 'Obchodní cesta'

name = fields.Char(tracking=True)
partner_id = fields.many2one('res.partner','Zodpovědný',
tracking=True)
hosté = pole.MnohoNaMnoho('res.partner', 'Hosté')
stav = pole.Výběr([('návrh', 'Nový'), ('potvrzeno', 'Potvrzené')])
tracking=True)
expense_ids = pole.One2many('business.expense', 'trip_id', 'Náklady')
alias_id = fields.many2one('mail.alias', 'Alias', 'ondelete="restrict"',
required=True)

def _get_alias_model_name(self, vals):
"Specifikujte model, který bude vytvořen při přijetí zprávy na alias."
vrací hodnotu business.expense

def _get_alias_values(self):
"Uveďte nějaké výchozí hodnoty, které budou nastaveny v aliasu při jeho vytvoření."
hodnoty = super(BusinessTrip, self)._get_alias_values()
                # alias_defaults obsahuje slovník, který bude napsán
                # všechny záznamy vytvořené tímto uživatelským jménem
                #
                # v tomto případě chceme všechny záznamy o výdajích odeslat na e-mailovou adresu aliasu cesty.
                # být spojen s příslušnou pracovní cestou
hodnoty['alias_defaults'] = {'trip_id': self.id}
                # chceme, aby jen ti, kteří se na výpravě účastní, mohli utrácet
                # Výchozí
hodnota['alias_kontakt'] = 'sledovatelé'
Vracené hodnoty

třída BusinessExpense(model.Model):
_name = 'podnikání.náklady'
dědí se z mail.thread
_popis = 'Náklady na podnikání'

jméno = fields.String()
částka = fields.Float('Částka')
trip_id = fields.many2one('business.trip', 'Business Trip')
partner_id = fields.many2one('res.partner','Vytvořeno uživatelem')

Chtěli bychom, aby se náš alias dal snadno konfigurovat z pohledu formuláře.
pracovní cesty, tak k našemu pohledu přidáme následující:

... kódový blok :: XML

<stránka typu="Emaily">
<skupina jméno="skupinové_alias">

<div name="alias_def">

zatímco je v režimu úpravy -->

string="E-mailová adresa aliasu" required="0"/>



                        @




string="Přijímat e-maily od uživatelů" />
</skupina>


Nyní můžeme přímo z pohledu formuláře změnit aliasovou adresu.
kdo může posílat e-maily na tuto adresu.

Pak můžeme přepsat metodu „message_new()“ našich nákladových modelů, abychom získali hodnoty
z našeho e-mailu, kdy bude výdaj vytvořen:

.. kódový blok:: python

třída BusinessExpense(model.Model):
            # Dřívější kód zde
            # ...

def message_new(self, zpráva, vlastní hodnoty = None):
""" Přesměrování pro nastavení hodnot podle e-mailu.

V tomto jednoduchém příkladu používáme jako jméno e-mailového účtu název e-mailové zprávy.
zkuste najít partnera s tímto e-mailem.
„Vyhledat expenzi pomocí regulárního výrazu.“
jméno = msg_dict.get('subject', 'Nová položka výdajů')
                # Spojte poslední plovoucí číslo v řetězci
                # Příklad: „50,3 bar 34,5“ se stává „34,5“. To může být cena.
                # kódovat na úkor. Pokud ne, vezměte si 1.0 místo
částka_vzor = „(číslo + (desetinné číslo)*?| desetinné číslo)“
expense_price = re.findall(složenec, jméno)
cena = výdajová cena a nebo 1,0
                # hledat partnera podle e-mailové adresy
partner = self.env['res.partner'].search([('email', 'ilike', email_address)],
limit=1)
defaulty = {
'name': name,
'cena': cena
'partner_id': partner.id
                }
defaulty.aktualizovat(předdefinované hodnoty nebo {}).
res = super(BusinessExpense, self).message_new(msg, default_values=defaults)
vrací se hodnota res

.._odkaz/směsi/pošta/aktivity:

Sledování aktivit
-------------------

Aktivita je akce, kterou musí uživatel na dokumentu provést, jako například zavolat.
nebo organizování schůzky. Akce jsou součástí poštovního modulu, protože
integrované do Chatter, ale nejsou součástí mail.thread.aktivity.
jsou záznamy třídy „mail.activity“, které mají typ („mail.activity.type“).
jméno, popis, plánovaný čas (a další). Čekající aktivity jsou viditelné
nad historií zpráv v chatovacím widgetu.

Můžete integrovat aktivity pomocí třídy „mail.activity.mixin“ na vašem objektu
a konkrétní widgety, které je zobrazí (přes pole „activity_ids“).
zobrazení pošty a zobrazení kanbanu vašich záznamů („mail_activity“ a „kanban_activity“)
widgety, resp.).

Příklad:

Organizace pracovního cestování je zdlouhavý proces, který vyžaduje sledování potřebných činností
jako je objednání letenek nebo taxi na letiště mohou být užitečné.
přidáme metodu mixinu na náš model a zobrazíme další plánované aktivity
v historii zpráv naší cesty.

.. kódový blok:: python

class BusinessTrip(models.Model):
_name = 'podnikání.cesta
_dědí z ['mail.thread', 'mail.activity.mixin']
_popis = 'Obchodní cesta'

jméno = fields.String()
            # [...]

Upravujeme pohled na formulář cesty, aby zobrazoval její další aktivity:

... kódový blok :: XML

<zaznamenání id="cestovní formulář pro obchodní cesty" model="ir.ui.view">
<položka jméno>business.trip.form</položka>
<field name="model">business.trip</field>
<položka jméno="arch" typ="xml">
<form string="Obchodní cesta">
<!-- Vaše obvyklá forma zobrazení zde -->


<field name="activity_ids" widget="mail_activity"/>



</položka>


Konkrétní příklady integrace najdete v následujících modelech:

* „crm.lead“ v aplikaci CRM (CRM)
* „prodej.objednávka“ v aplikaci „Prodeje“ (*sales*)
* „úkol projektu“ v aplikaci „Projekt“ (*projekt*)


.. odkaz/směsice/webová stránka:

Funkce webu
================

... odkaz/směsice/webová stránka/utm:

Sledování návštěvníků
----------------

Třída „utm.mixin“ může být použita k sledování online marketingu/komunikace
kampaně prostřednictvím argumentů v odkazech na určené zdroje. Mixin přidává
3 pole pro vaši šablonu:

* „campaign_id“: pole typu „many2one“ pro „utm.campaign“
objekt (tj. Vánoční speciál, Podzimní kolekce atd.)
* „source_id“: pole typu „many2one“ pro „utm.source“
předmět (tj. vyhledávač, seznamka, apod.)
* „medium_id“: pole typu „many2one“ na hodnotu „utm.medium“
objekt (tj. poštovní zásilka, elektronická pošta, aktualizace sociální sítě atd.)

Tyto modely mají pouze jedno pole „jméno“ (tzn., že jsou tam jen proto, aby
kampaně, ale nemají žádné konkrétní chování).

Jakmile se zákazník na vašich stránkách objeví s těmito parametry v adrese URL
(tj. https://www.odoo.com/?campaign_id=mixin_talk&source_id=www.odoo.com&medium_id=webové stránky)
Pro tyto parametry návštěvníkovi webu nastaví tři soubory cookie.
Jednou, když je objekt, který dědí z utm.mixinu vytvořen ze stránky (tj.
formulář, žádost o práci apod.), spustí se kód mixinu utm a získá hodnoty
od cookies k jejich nastavení do nového rekordu. Poté můžete
použijte pole kampaně, zdroje a média jako jakékoli jiné pole při definování zpráv
a pohledy (skupina, atd.).

Tento způsob chování lze rozšířit přidáním vztahového pole do jednoduché třídy (
Model by měl podporovat rychlé vytvoření (tj. volání metody „create()“ s jediným parametrem).
„název“ a rozšířit funkci „sledování polí“):

... kódový blok:: python

třída UtmMyTrack(model.Model):
_name = 'my_modul.my_track'
_description = 'Můj sledovací objekt'

jméno = pole.Char(string='Jméno', povinné=True)


class MyModel(models.Models):
_name = "my_module.my_model"
_dědí z mixinu utm
_description = „Sledovaný objekt“

my_field = fields.many2one('my_modul.my_track','Můj pole')

@ApiModel
def tracking_fields(self):
výsledek = super(MyModel, self).tracking_fields()
výsledky.append([
            # ("parametr URLu", "název pole mixinu", "název v cookies")
('my_field','my_field','odoo_utm_my_field')
            ])
vrátí výsledek

Toto mu řekne, aby vytvořil soubor cookie s názvem *odoo_utm_my_field* se
hodnota nalezená v parametru URL my_field; nový záznam tohoto modelu
vytvořené pomocí volání z webové stránky, přehozením metody „create()“
Metoda „utm.mixin“ získá výchozí hodnoty pro tento prvek ze
cookie a záznam „my_module.my_track“ bude vytvořen na lince, pokud
neexistuje.

Konkrétní příklady integrace najdete v následujících modelech:

* „crm.lead“ v aplikaci CRM (CRM)
* „hr. uchazeč“ v procesu náboru (aplikace „hr_recruitment“)
* „helpdesk.ticket“ v aplikaci Helpdesk (Enterprise Edition only)

.. odkaz/směsice/webová stránka/zveřejněno:

Viditelnost webu
------------------

Můžete snadno přidat viditelnost webové stránky na jakýkoliv záznam.
tento mixin je poměrně snadno ručně implementovatelný a je nejčastěji používaným po
„mail.thread“ dědění, což je důkaz jeho užitečnosti. Typické použití
případ pro tuto metodu je každý objekt, který má přední stránku; schopnost řídit
viditelnost stránky vám umožňuje pracovat na editaci stránky bez časového tlaku
a zveřejnit ji, až budete spokojeni.

Pro zahrnutí funkčnosti je potřeba pouze dědit mixin „website.published.mixin“:

... kódový blok:: python

class BlogPost(models.Model):
name="blog.post"
_description = „Příspěvek na blog“
_dědí z mixinu 'webové stránky.zveřejněné.mixin'

Toto mixinu přidává do vaší třídy 2 pole:

* „webová stránka zveřejněna“: pole typu „pravda/nepravda“, které reprezentuje
status publikace
* „webová adresa“: pole typu „char“, které reprezentuje
URL, kterým se objekt přistupuje

Všimněte si, že poslední pole je počítané pole a musí být implementováno pro vaši třídu:

... kódový blok:: python

def _vypočítat_webovou_adresu(self):
for blog_post v sebe:
blog_post.web_url = "/blog/%s" % (log_post.blog_id)

Jakmile je mechanismus vytvořený, stačí upravit vaše front-end a back-end.
přidat tlačítko do tlačítkového panelu v zadní části aplikace.
Obvykle je tento postup správný:

... blok kódu::xml

<button třída="oe_stat_button" jméno="webové stránky_tlačítko_vydání"
typ="objekt" ikonou="fa-globus">



V předním panelu je potřeba několik bezpečnostních kontrol, aby se nedostalo na „Upravování“.
tlačítka pro návštěvníky webu:

... blok kódu::xml

<div id="website_published_button" class="float-right">
<!-- nebo jakýkoliv jiný významný soubor -->

<t t-set="objekt" t-value="blog_post"/>
<t t-set="publish_edit" t-value="true"/>
<t t-set="akce" t-value="'blog.blog_post_akce'"/>
</t>


Pozor, že musíte předat svůj objekt jako proměnnou „objekt“ do šablony.
V tomto příkladu byl záznam „blog.post“ předán jako proměnná „blog_post“.
„qweb“ renderovacímu motoru je nutné tuto informaci zadat do publika
šablona správy. Proměnná „publish_edit“ umožňuje v přední části
tlačítko pro přepínání mezi předním a zadním uživatelským rozhraním.
a naopak snadno) a pokud je nastaveno, musíte uvést celé externí ID akce.
chcete volat zadní část v proměnné „akce“ (poznámka: při pohledu na formulář)
musí existovat pro daný model).

Akce „website_publish_button“ je definována v mixinu a přizpůsobuje se
chování k vašemu objektu: pokud třída má funkci pro výpočet „webové adresy“,
uživatel je přesměrován na front-end, když klikne na tlačítko.
Poté může stránku publikovat přímo z přední části webu, což zajišťuje
že žádné online vydání nemůže být náhodné. Pokud není funkce počítání,
Pouze se spustí „webová stránka zveřejněná“.

.. odkaz/směsice/webová stránka/SEO:

Metadat webu
----------------

Toto jednoduché rozšíření vám umožňuje snadno dostat metadata do vašeho frontendu.
stránky.

... kódový blok:: python

class BlogPost(models.Model):
name="blog.post"
_description = „Příspěvek na blog“
_dědí z ['webové stránky.SEO.metadat', 'webové stránky.zveřejněno.směs']

Toto mixinu přidává na vašem modelu 3 pole:

* „webová stránka_meta_název“: pole typu „text“ umožňující nastavit
přidat další titulek na stránku
* „webová meta popis“: pole typu „char“, které obsahuje
krátký popis stránky (často používaný v výsledcích vyhledávání).
* „webová metatitulek“: pole typu „char“, které obsahuje nějaké
klíčová slova, která pomohou vyhledávačům přesněji zařadit stránku.
„Rozšířit“ nástroj vám pomůže snadno vybrat klíčová slova související s výrazem

Tyto pole lze v administraci upravovat pomocí nástroje „Zvýraznit“ z editoru.
Nástrojová lišta. Zadáním těchto polí můžete pomoci vyhledávačům lépe indexovat vaše stránky.
Pozor, vyhledávače nevyhodnocují výsledky pouze na základě těchto metadat.
Nejlepší praxe v oblasti optimalizace pro vyhledávače stále spočívá ve získání odkazů na důvěryhodných zdrojích.

.._odkaz/směsi/různé:

Ostatní
======

.._odkaz/směsi/různé/hodnocení:

Hodnocení zákazníků
---------------

Hodnotící mixin umožňuje odeslat e-mail s žádostí o hodnocení zákazníka a automaticky
přechodem na kanban procesy a agregací statistik o vašich hodnoceních.

Přidání hodnocení na vaši model
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Přidání podpory hodnocení je velmi jednoduché - prostě dědíte „rating.mixin“ model:

... kódový blok:: python

class MyModel(models.Models):
_name = "my_module.my_model"
_dědí z mixinu rating a mail thread

user_id = fields.many2one('res.users', 'Odpovědná osoba')
partner_id = fields.many2one('res.partner', 'Zákazník')

Chování mixinu se přizpůsobí vašemu modelu:

* Záznam „rating.rating“ bude propojen s položkou „partner_id“ vašeho
model (pokud pole existuje).

  - Toto chování lze přehlušit funkcí „rating_get_partner_id()“.
pokud použijete jiné pole než „partner_id“

* Záznam „rating.rating“ bude propojen s partnerem uživatele „user_id“.
pole vašeho modelu (pokud pole existuje) (tj. partner, který je hodnocen).

  - Toto chování lze přehlušit funkcí „rating_get_rated_partner_id()“.
pokud použijete jiné pole než „user_id“ (pozorně si přečtěte, že funkce musí
„res.partner“, systém automaticky vyhledá partnera podle „user_id“
uživatele (včetně IP adresy)

* Historie chatu zobrazí hodnocení události (pokud váš model dědí od
„mail.thread“

Požadavky na hodnocení zasílejte e-mailem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pokud chcete poslat e-maily s žádostí o hodnocení, jednoduše vytvořte e-mail s
odkaz na hodnocený objekt. Základní e-mailová šablona by mohla vypadat takto:

... blok kódu::xml


<pole název="název">Můj model: žádost o hodnocení</pole>

<pole název="předmět">Žádost o hodnocení služeb</pole>
<field name="model_id" ref="my_module.model_my_model"/>
<field name="partner_to">${objekt.rating_get_partner_id().id}</field>
<field name="auto_delete" eval="True"/>

%set access_token = objekt.rating_get_access_token()
<p>Ahoj,</p>
Jak spokojeni jste?
<ul>
<li><a href="/rate/${access_token}/5">Spokojený</a></li>
<li><a href="/rate/${access_token}/3">Okay</a></li>
<li><a href="/rate/${access_token}/1">Nespokojený</a></li>


</záznam>

Vaše zákaznice pak obdrží e-mail s odkazy na jednoduchou webovou stránku, kde
poskytnout zpětnou vazbu na jejich interakci s vašimi uživateli (včetně volného textu)
zpětná vazba).

Poté můžete snadno integrovat své hodnocení s vaším pohledem na formu definováním
akce pro hodnocení:

... blok kódu::xml

<záznam id="hodnocení - hodnocení - akce - můj vzor" model="ir.actions.act_window">
<pole název="name">Hodnocení zákazníků</pole>
<field name="res_model">rating.rating</field>
<field name="view_mode">kanban,pivot,graf</field>

</záznam>


<políčko name="název">my_modul.my_model.view.form.dědictví.hodnocení</políčko>
<položka modelu>my_module.my_model</položka>
<položka jméno="dědičná_id" odkaz="my_modul.my_model_view_form"/>
<položka jméno="arch" typ="xml">
<xpath expr="//div[@name='button_box']" position="inside">
<tlačítko jméno="%(hodnocení_hodnocení_akce_můj_vzorec)" typ="akce"
class="oe_stat_button" icon="fa-smile-o">


</xpath>
</p>
</záznam>

Poznámka: Pro hodnocení existují výchozí pohledy (kanban, pivot, graf), které umožňují
Vám se rychle zobrazí pohled na hodnocení vašich zákazníků.

Konkrétní příklady integrace najdete v následujících modelech:

* „úkol projektu“ v aplikaci Projekt (*hodnocení projektu*)
* „helpdesk.ticket“ v aplikaci Helpdesk (Enterprise Edition only)
