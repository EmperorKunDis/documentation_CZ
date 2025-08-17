=========================
Dvoufaktorová autentizace
=========================

.. |2fa| nahradit za :: abbr: 2FA (dvoufaktorové ověření)
.. |QR| nahradit za :: abbr: QR (Quick Response) kód

*Dvoufázové ověření (2FA)* je způsob, jak zvýšit bezpečnost a zabránit neoprávněným osobám
z přístupu k uživatelským účtům.

Prakticky řečeno, |2fa| znamená uložení tajného klíče v *autentizátoru* obvykle na mobilním telefonu.
Vyměňování kódu z autentizátoru při pokusu o přihlášení.

To znamená, že neautorizovaný uživatel by musel odhadnout heslo účtu a mít přístup k
autentizátor, který je obtížnější.

Požadavky
============

.. důležité::
Tyto seznamy jsou pouze příklady. Neslouží jako doporučení konkrétního softwaru.

Telefonem založené autentizátory jsou nejjednodušší a nejběžnější. Příklady zahrnují:

- „Authy“
- „FreeOTP <https://freeotp.github.io/>“
- „Google Authenticator <https://support.google.com/accounts/answer/1066447?hl=cs>“
- „Poslední heslo autentizátor <https://lastpass.com/auth/>“
- Microsoft Authenticator


Další možností jsou správci hesel. Mezi nejčastější patří:

- „1Password <https://support.1password.com/one-time-passwords/>“
- „Bitwarden <https://bitwarden.com/help/article/authenticator-keys/>“

.. poznámka::
Zbytek dokumentu používá jako příklad aplikaci Google Authenticator, protože je jednou z nejpoužívanějších.
Je to běžně používaný produkt, což není žádné doporučení.

Nastavení dvoufázového ověření
===============================

Po výběru autentizátoru se přihlaste do Odoa a pak klikněte na profilový obrázek v pravém horním rohu.
rohu a vyberte položku „Můj profil“ z rozbalovací nabídky.

Klikněte na záložku „Bezpečnost účtu“, poté posuňte „Dvoufázové ověření“.
přepnout na aktivní.

.. obrázek: 2fa/account-security.png
:align:center

Tím se zobrazí okno „Zabezpečení“ s požadavkem na potvrzení hesla.
Pokračujte v zadávání hesla, pak klikněte na „Potvrzení hesla“. Následně se objeví
Otevře se okno s názvem „Aktivace dvoufaktorového ověření“, ve kterém je QR kód.


.. obrázek: 2fa/qr-code.png
:align:center

Použijte požadovanou aplikaci pro ověřování a naskenujte QR kód, když vás na to vyzvou.

.. tip::
Pokud není možné skenovat obrazovku (např. nastavení probíhá na stejném zařízení jako
aplikace autentizátoru, kliknutím na odkaz „Nemůžu skenovat?“, který je poskytnutý, nebo
Pokud chcete zadat heslo ručně, můžete použít alternativu - kopírovat tajné heslo.

.. obrázek:: 2fa/secret-visible.png
:align:center

.. obrázek: 2fa/input-secret.png
:align:center

Následně by měl autentizátor zobrazit ověřovací kód.

.. obrázek:: 2fa/authenticator.png
:align:center

Zadejte kód do pole „Kontrolní kód“ a pak klikněte na „Aktivovat“.

.. obrázek: 2fa/2fa-enabled.png
:align:center

Přihlášení
==========

Chcete-li potvrdit dokončení nastavení dvoufaktorového ověřování, odhlaste se z aplikace Odoo.

V poli pro přihlašovací jméno a heslo zadejte své přihlašovací údaje, pak klikněte na tlačítko „Přihlásit se“.
Stránce „Dvoufázové ověření“ zadejte kód, který vám byl poskytnutý autentizátorem, který jste si vybrali.
Pole „Kód autentizace“, pak klikněte na „Přihlásit“.

.. obrázek: 2fa/2fa-login.png
:align:center
:alt:Přihlášení s povolenou dvoufaktorovou autentizací.

.. nebezpečí::
Pokud uživatel ztratí přístup ke svému autentizátoru, musí administrátor **musí** deaktivovat dvoufázové ověření.
účet před přihlášením uživatele.

Zavedení dvoufázového ověření
=================================

Pro uživatele povinné použití dvoufaktorového ověření, nejprve přejděte na hlavní panel Odoo:
Odeberte filtr aplikací z pole „Hledat…“ a pak vyhledejte 2FA.
e-mailem.

Klikněte na tlačítko „Instalovat“ v kartě pro modul „Dvoufázové ověření e-mailem“.

.. obrázek: 2fa/2FA-e-mailem.png
:align:center
:alt:Modul dvoufázového ověření e-mailem v adresáři aplikací.

Po dokončení instalace přejděte na: guilabel:Nastavení aplikace: Povolení. Zatrhněte políčko
Označte „Zapnout dvoufaktorovou autentizaci“. Poté vyberte možnost
zda se tento parametr vztahuje na :guilabel:`Pouze zaměstnance“ nebo :guilabel:`Všechny uživatele“.

.. poznámka::
Vybráním „Všichni uživatelé“ se nastavení aplikuje na portálové uživatele navíc k zaměstnancům.

.. obrázek: 2fa/enforce-settings.png
:align:center
:alt:Zapněte dvoufaktorové ověřování v aplikaci Nastavení.

Klikněte na tlačítko „Uložit“ pro uložení neuložených změn.
