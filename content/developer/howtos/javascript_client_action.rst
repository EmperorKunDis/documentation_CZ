
...jakto/javascript-klientska-akce:

======================
Vytvořte akci klienta
======================

Akce klienta vyvolá akci, která je zcela implementována na straně klienta.
Jedním z výhod používání klientské akce je schopnost vytvářet velmi přizpůsobitelné rozhraní.
s lehkostí. Klientské akce jsou obvykle definovány komponentou OWL; můžeme také používat web
výchozího rámce a používání služeb, jádra, háčků, ...

#Vytvořte akci klienta:ref:`<reference/actions/client>`, nezapomeňte
zpřístupnit ho.

... kódový blok :: XML

<záznam modelu "ir.actions.client" s ID "my_client_action">
<pole název="název">Můj klientský postup</pole>
<položka jméno="tag">my_module.MyClientAction</položka>
</záznam>

#Vytvořte komponentu, která reprezentuje klientské akce.

... kódový blok::js
:předpis: :soubor: `my_client_action.js`

import { registry } z "@web/core/registry";

import { Komponenta } z "@odoo/owl";

class MyClientAction extends Component {
statická šablona = "my_module.clientaction";
      }

      // remember the tag name we put in the first step
registry.category("akce").add("my_modul.MyClientAction", MyClientAction);

... kódový blok :: XML



<šablony xml:space="preserve">
<t t-name="supertriko.akceklienta">
Ahoj, svět


