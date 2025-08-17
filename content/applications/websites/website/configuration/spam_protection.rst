=====================
Formy ochrany před spamem
=====================

:ref:`Cloudflare Turnstile <cloudflare-turnstile>` a :ref:`Google reCAPTCHA v3 <google-recaptcha>“
ochránit formuláře na webu, stránky pro přihlášení a stránky pro obnovení hesla před spamem a zneužíváním.
pokus o rozlišení lidských a robotických příspěvků pomocí neinteraktivních výzev založených na
telemetrie a chování návštěvníků.

.. důležité:
Doporučujeme používat Cloudflare Turnstile, protože třetí verze reCAPTCHA nemusí být v souladu s místními předpisy
ochranných předpisů.

.. poznámka::
Všechny stránky používající :guilabel:`Formulář`, :guilabel:`Blok novinek`, :guilabel:`Pop-up okno s novinkami
části a formulář Extra krok při placení chrání oba.
Nástroje. **Stránky pro přihlášení na web a stránky pro obnovení hesla** jsou také chráněny.

.. viz též:
   - „Dokumentace Cloudflare Turnstile“ <https://developers.cloudflare.com/turnstile/>
   - „Návod k použití Google reCAPTCHA v3 <https://developers.google.com/recaptcha/docs/v3>“

.. _cloudflare-turnstile:

Konfigurace Cloudflare Turnstile
==================================

Na Cloudflare
-------------

- Vytvořte účet na Cloudflare nebo použijte stávající a
„Přihlásit se na adrese <https://dash.cloudflare.com/login>.
- V navigačním panelu na přístrojové desce klikněte na :guilabel:`Turnstile“.
- Na stránce „Turnstile Sites“ klikněte na „Přidat web“.
- Přidejte :guilabel:Název webu, abyste jej snadno identifikovali.
- Zadejte nebo vyberte doménu webu, například „*example.com*“ nebo „*subdomain.example.com*“.
- Vyberte režim widgetu:

  - Režim „Spravované“ je **doporučený**, protože návštěvníci mohou být vyzváni k zaškrtnutí políčka
potvrzující, že jsou lidmi, pokud je to považováno za nutné Turnstilem.

.... obrázek:spam_protection/turnstile-human.png
:alt: Widget ověření lidské přítomnosti Cloudflare

  - Pro režim „Nepřítomný“ a „Skrytý“ návštěvníci nikdy
Provokovat uživatele k interakci. V režimu „Neprompt“ může být zobrazena nabídka načítání, aby
varovat návštěvníky, že Turnstile chrání formulář, avšak widget nepodporuje Odoo.

.. poznámka::
Pokud kontrola turniketu selže, návštěvník nebude moci formulář odeslat a následující
Při chybě se zobrazí chybová hláška.

.. obrázek:: spam_protection/turnstile-error.png
:alt:Chybová zpráva ověření Cloudflare Turnstile

- Klikněte na tlačítko „Vytvořit“.

.. obrázek:spam_protection/turnstile-configuration.png
:alt:Přidání webu do Cloudflare Turnstile

Vytvořené klíče jsou pak zobrazeny. Stránku nechte otevřenou pro pohodlí, protože kopírování klíčů
Další požadavek je na Odoo.

Odoo
-------

- Ve svém účtu klikněte na záložku „Nastavení“ a v části „Spojení“ zapněte
:guilabel:`Cloudflare Turnstile“ a klikněte na „Uložit“.
- Otevřete stránku Cloudflare Turnstile, zkopírujte Site Key a vložte ho do
:guilabel:`Klíč webové stránky CF“ pole v Odoo.
- Otevřete stránku Cloudflare Turnstile, zkopírujte klíč „Secret“ a vložte jej do
:guilabel:`Tajný klíč CF“ pole v Odoo.
- Klikněte na tlačítko „Uložit“.

..tip:
Přejděte na turniket ve svém účtu Cloudflare, abyste viděli řešení a získali přístup k dalším
nastavení.

.._google-recaptcha:

Konfigurace reCAPTCHA 3
==========================

.. varování:
reCAPTCHA verze 3 nemusí být v souladu s místními předpisy o ochraně osobních údajů.

Na Googlu
---------

Otevřete stránku registrace služby reCAPTCHA na adrese https://www.google.com/recaptcha/admin/create/. Přihlásit
nebo vytvořit účet Google, pokud je třeba.

Na registrační stránce webu:

- Webu přidejte štítek :guilabel:.
- Zanechte typ reCAPTCHA na Score based (v3).
- Zadejte jednu nebo více domén, například „*example.com*“ nebo „*subdomain.example.com*“.
- Pokud uživatel vybral projekt v poli „Google Cloud Platform“, bude automaticky zvolen.
Vytvořené s přihlášeným účtem na Googlu. Pokud ne, je vám automaticky vytvořen. Klikněte
:guilabel:`Google Cloud Platform“ si vybrat projekt sám nebo přejmenovat automaticky vytvořený.
projektu.
- Souhlasit s podmínkami služby.
- Klikněte na tlačítko „Odeslat“.

.. obrázek: spam_protection/recaptcha-google-configuration.png
:alt: Příklad registrace na webu reCAPTCHA

Následně se zobrazí nová stránka s vygenerovanými klíči. Nechte ji otevřenou pro pohodlné použití, protože
Další klíč k Odoo je potřeba.

Odoo
-------

- Ve svém účtu klikněte na záložku „Nastavení“ a v části „Spojení“ zapněte
:guilabel:`reCAPTCHA“ v případě potřeby.

.. varování::
Nebuďte bezbranní vůči útokům spamových robotů. Neodstraňujte funkci :guilabel:`reCAPTCHA` nebo neinstalujte
modul integrace, stejně jako mnoho dalších by bylo také odstraněno.

- Otevřete stránku služby Google reCAPTCHA, zkopírujte klíč webu (:guilabel:`Site key`) a vložte jej do
:guilabel:`Hlavní klíč“ pole v Odoo.
- Otevřete stránku služby Google reCAPTCHA, zkopírujte klíč „Secret“ a vložte ho do
:guilabel:`Tajný klíč“ pole v Odoo.
- Změňte výchozí hodnotu :guilabel:`Minimální skóre“ („0,70“) v případě potřeby na nějakou hodnotu mezi „1,00“.
a „0.00“. Čím vyšší je prahová hodnota, tím obtížnější je projít reCAPTCHA a naopak.
Ve hře je celkem 11 úrovní a z nich jsou dostupné pouze následující čtyři:
„0,1“, „0,3“, „0,7“ a „0,9“.
- Klikněte na tlačítko „Uložit“.

.. viz též:
„Hodnocení služby reCAPTCHA - Dokumentace Google <https://cloud.google.com/recaptcha/docs/interpret-assessment-website#interpret_scores>“

Můžete návštěvníkům sdělit, že reCAPTCHA chrání formulář. K tomu otevřete webový editor a
Přejděte na formulář a klikněte někam dovnitř formuláře. Poté se v pravém sloupci objeví
Kartě „Nastavení“, kde je tlačítko „Zobrazit zásady reCAPTCHA“ pod „Formulář“.
část.

.. obrázek: spam_protection/recaptcha-policy.png
:alt: zobrazení politické zprávy o reCAPTCHA na formuláři

.. poznámka::
Pokud ověření reCAPTCHA selže, zobrazí se následující chybová hláška:

.... obrázek:spam_protection/recaptcha-error.png
:alt:Chybová zpráva ověření služby Google reCAPTCHA

..tip:
Analytika a další nastavení jsou k dispozici na stránce „Administrace služby Google reCAPTCHA“
<https://www.google.com/recaptcha/admin/>_). Například můžete dostávat e-mailové upozornění, pokud Google
detekuje podezřelý provoz na vašem webu nebo zobrazuje procento podezřelých požadavků.
Mohlo by vám pomoci určit správnou minimální skóre.
