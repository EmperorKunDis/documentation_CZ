=====================
Plánování trasy
=====================

Výchozí nastavení aplikace Odoo Field Service zobrazuje statickou mapu s umístěním všech úkolů na daný den.
připnutý. Pro uživatele terénních služeb je možné zobrazit trasu
na mapě pomocí MapBoxu. Pro tento účel zapněte následující funkci **Map Routes**:

#Vytvořte nebo se přihlaste do účtu MapBox pomocí následujícího odkazu: <https://www.mapbox.com/>.
#Vytvořte token <https://docs.mapbox.com/help/getting-started/access-tokens/#adding-url-restrictions-to-access-tokens>.
#Přejděte na stránku „Přístupové tokeny“ v Mapboxu <https://account.mapbox.com/access-tokens/>_ a zkopírujte
vašeho tokenu.
#V Odoo přejděte do aplikace „Nastavení“ a posuňte se dolů k „Integraci“.
sekci. Vložte svůj přístupový token do pole :guilabel:`Token` v části
:guilabel:`Uložit trasu“ a klikněte na :guilabel:`Zobrazit trasy“.

Zobrazení trasy na mapě
==================================

.. důležité:
Pro zobrazení úkolu v terénním plánu je nutné poskytnout platnou adresu.
zákazník.

Pro zobrazení úkolů na mapě přejděte do položky „Správa služeb“ - „Moje úkoly“ - „Mapa“.
Vaše cestovní plán, Odoo se postará o vaši servisní práci podle jejího data:guilabel:
ukázat cestu z jednoho místa na druhé.

Chcete-li otevřít svou trasu na webových stránkách nebo v aplikaci Google Maps, klikněte na tlačítko „Zobrazit v Google Maps“.
Google Maps zahrnuje vaši aktuální polohu jako výchozí bod trasy.

..tip:
   - Výchozí mapa zobrazuje úkoly dnešní doby. Odstraňte filtr „Dnes“ v poli vyhledávání
zobrazit všechny úkoly. Vaše úkoly jsou pak seřazeny podle data v levém sloupci.
   - Klikněte na úkol v levém sloupci nebo na špendlík na mapě, abyste zobrazili podrobnosti o úkolu.
můžete otevřít úkol nebo kliknout na „Navigovat“ a získat trasu.
vaši aktuální polohu k místu, kde se tato konkrétní úloha nachází.
