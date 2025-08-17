
.._odkaz/kontroly:

===============
Webové kontroly
===============

Kontroloři
===========

Kontroler musí poskytovat rozšiřitelnost, podobně jako
Třída Model, ale nemůže použít stejný mechanismus jako
Předpoklady (databáze s naloženými moduly) nemusí být ještě k dispozici (např.
nebyla vytvořena žádná databáze nebo nebyla vybrána žádná databáze.

Takže kontroloři poskytují vlastní mechanismus pro rozšíření, který je oddělen od
modelky:

Kontroloři jsou vytvářeni dědičností od třídy „odoo.http.Controller“.
Způsoby jsou definovány metodami ozdobenými:

class MyController(odoo.http.Controller):
@route('/nějaká_adresa', autentizace='veřejná')
def handler(self):
vrací seznam

Pro převzetí kontroly nad třídou, která dědí od této třídy, použijte :ref:`dědičnost <python:tut-inheritance>`.
třída a přetížit příslušné metody, pokud je potřeba znovu vystavit

třída Extension(MůjKontroler):
@route()
def handler(self):
do_před()
vrací se zpět do metody Extension.handler()

* Použití funkce :func:`~odoo.http.route` je nutné, aby se metoda
(a trasa): pokud metoda není dekorována, je viditelná.
bude „nepublikován“.
* Všechny metody dekorátorů jsou kombinovány, pokud je převažující metoda
dekorátor nemá žádný argument, všechny předchozí budou zachovány, jakékoliv poskytnuté
argument bude přednostně použit, např.:

třída Restrict(Můj Controller):
@route(auth='user')
def handler(self):
return super(Restrict, self).handler()

„/nějaká_URL“ změní z veřejného ověření na uživatele (vyžaduje


API
===

.. odkaz/http/routing:

Routování
-------

.. autodekorátor: odoo.http.route

.. odkaz/http/požadavek:

Žádost
-------

Žádostní objekt je automaticky nastaven na :data:`odoo.http.request`.
začátek požadavku.

... třída autoclass:odoo.http.Request
:členové:
:člen-pořadí: podle zdroje

... autoklasifikace: odoo.http.JsonRPCDispatcher
:členové:
:člen-pořadí: podle zdroje
... autoklasifikace: odoo.http.HttpDispatcher
:členové:
:člen-pořadí: podle zdroje

Odpověď
--------

... autoklasifikace: odoo.http.Response
:členové:
:člen-pořadí: podle zdroje

.... možná bychom tento parametr nastavili tak, aby dokumentoval všechny tyto jemné metody na odpovědi Werkzeugu.
objekt? (funguje)
:dědičné členy:
