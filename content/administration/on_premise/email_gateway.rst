=============
Emailový brána
=============

Odoo Mail Gateway vám umožňuje zasílat všechny e-maily přímo do Odoo.

Jeho princip je jednoduchý: váš SMTP server spouští skript „mailgate“ pro každé nové
příchozí e-mail.

Skript se postará o připojení k databázi Odoo prostřednictvím XML-RPC a odeslání e-mailů.
funkce „MailThread.message_process()“.

Předpoklady
-------------

- Administrátorská přístupová práva k databázi Odoo.
- Vlastní poštovní server, například Postfix nebo Exim.
- Technické znalosti o tom, jak konfigurovat e-mailový server.

Pro Postfix
-----------

Ve vašem aliasovém souboru (:file:`/etc/aliases`):

... blok kódu:: text

email@adresa: „|/odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <název databáze> -u <uživatelské jméno> -p <heslo>“

.. poznámka::
Zdroje

   - „Postfix <http://www.postfix.org/documentation.html>“
   - „Aliasy v Postfixu <http://www.postfix.org/aliases.5.html>“
   - „Virtuální poštovní server <http://www.postfix.org/virtual.8.html>“

Pro Exim
--------

... blok kódu:: text

*: /odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <název databáze> -u <uživatelské jméno> -p <heslo>

.. poznámka::
Zdroje

   - „Exim <http://www.exim.org/docs.html>“

.. tip::
Pokud nemáte přístup nebo nezvládáte správu svého e-mailového serveru, použijte :ref:`server
<email-inbound-custom-domain-incoming-server>
