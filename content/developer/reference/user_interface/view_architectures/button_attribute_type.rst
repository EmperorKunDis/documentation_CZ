.. atribut: typ
:noindex:

Typ tlačítka, které určuje jeho chování. Může mít dvě různé hodnoty:

...... atribut:: objekt


Zavolejte metodu na modelu pohledu. Tlačítko „název“ je metoda, která se volá s
aktuální identifikátor záznamu a současný „kontext“.

...... atribut:: akce


Nahrát a spustit záznam akce z tabulky ir.actions. Tlačítko má vlastnost name, která je ID XML
akce načítání. V kontextu je přidána modelová vrstva (jako aktivní model) a
aktuální rekord (jako aktivní ID).

...... příklad::
... kódový blok::xml

<tlačítko typu "objekt" jméno="akce_vytvorit_novy" string="Vytvořit dokument"/>
<tlačítko typu "akce" jméno="addon.action_create_view" string="Vytvořit a upravit"/>

:požadavek: Povinné, pokud je atribut special nastaven na hodnotu false
:typ: str
