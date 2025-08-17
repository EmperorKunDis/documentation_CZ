================
Konferenční hovory
================

Konferenční hovory pomáhají zaměstnancům rychle a efektivně spojit se, takže mohou problémy projednávat.
otevřené fórum. Účastníci mohou být omezeni pomocí kódu přihlášení. Tímto způsobem se zajistí důvěrnost
zůstat soukromé.

Tento dokument popisuje konfiguraci konferenčních hovorů v Axivoxu pro použití s Odoo VoIP.

Přidejte virtuální konferenci
========================

Chcete-li přidat virtuální konferenční místnost, přejděte na Axivox Management Console.
<https://manage.axivox.com>`. Po přihlášení klikněte na položku „Konference“ v nabídce.
vlevo.

Dále klikněte na zelené tlačítko s nápisem „Přidat konferenci“ a poté na „Nová konference“.
vzniká forma.

.. obrázek: konference_hovory/nove_konference.png
:align:center
:alt: Nová konferenční forma na Axivoxu.

Zde vyplňte pole „Jméno“ a nastavte „Vnitřní rozšíření“.

Vnitřní rozšíření je to, co používá každý v síti k rychlému připojení do konference.
volat místo psaní celého telefonního čísla.

..tip:
Vyberte si číslo mezi třemi až pěti číslicemi, které bude snadno zapamatovatelné a navolitelné.

Dále nastavte přístupový kód (heslo), pokud je potřeba konferenční místnost zabezpečit.
zúčastnit se konference, jakmile je vytočené prodloužení konference.
Při zadávání přípony se digitální recepční zeptá na heslo.

V poli „Rozšíření správce“ klikněte na vykřičník a z rozevírací nabídky vyberte uživatele.
rozšíření, které spravuje hovor.

Konečně v poli „Čekat na spuštění konference“ klikněte na
klikněte na rozbalovací nabídku a vyberte možnost „Ano“ nebo „Ne“.

Pokud by výběr byl „ano“, pak nikdo nemůže využívat virtuální konferenci
do doby, než se administrátor připojí a přihlásí na konferenční hovor.

Pokud jsou vyplněny všechna pole, ujistěte se, že konfiguraci uložíte pomocí tlačítka „Uložit“. Pak klikněte
V horním pravém rohu klikněte na „Použít změny“.

Po provedení této akce se konference přidá a správce Axivox má možnost
:guilabel:`Smazat“ nebo „Upravit“ konferenci z hlavního okna Axivoxu
přístrojová deska.

Pro pozvání uživatele Axivoxu na konkrétní hovor klikněte na tlačítko „Pozvat“ vedle
požadovanou konferenci a pokračujte v zadávání telefonního čísla nebo rozšíření pozvané osoby.
okno, které se objeví.

Jakmile je do pole „Prosím zadejte telefonní číslo“ přidán přípona nebo číslo,
textové poli „Osoba, kterou chcete pozvat“ klikněte na zelené tlačítko „Pozvat“, a obdrží
hned po příchodu dostanou telefonát, který je automaticky propojí s konferencí.

.. obrázek: konferenční hovory/pozvánka na konferenci.png
:align:center
:alt: Nová konferenční forma na Axivoxu.

Příchozí hovory
================

Pro otevření konference širšímu publiku lze konferenci propojit s čísly **Příchozí hovory**.

Pro to se přihlaste na „Axivox management console <https://manage.axivox.com>“ a klikněte
V levém menu zvolte položku „Příchozí hovory“.

Na panelu „Příchozí hovory“ klikněte na tlačítko „Upravit“, které je umístěno v pravém horním rohu.
:guilabel:`Číslo“ konference, ke které se má připojit.

Poté klikněte na první pole s názvem „Typ cílového zařízení pro hlasovou hovor“, které je označeno
nabídce a vyberte:guilabel:'Konference'.

Dále v poli Konference klikněte na vyhledávací pole a zvolte konkrétní
konference, která se k tomuto příchozímu číslu připojuje.

Nyní, pokud se volá na tuto číslo, je hovor připojen do konference, pokud ne
Je vyžadován přístupový kód. Pokud je vyžadován přístupový kód, volající
je pak vyzván k zadání přístupového kódu, který se používá k vstupu do konference.

Začátek hovoru v Odoo
==================

Kdekoli v databázi Odoo otevřete widget VoIP kliknutím na ikonu :guilabel:`☎️ (telefon)“.
v pravém horním rohu. Poté zavolejte konkrétní číslo pro konferenci a
klikněte na ikonu :guilabel:`☎️ (telefon)`.

.. obrázek: konference/telefonní widget.png
:align:center
:alt:Připojení k konferenční lince pomocí widgetu VoIP v Odoo.

Jakmile se digitální recepční ozve, zadejte přístupový kód (:guilabel:Přístupový kód) a stiskněte
:guilabel:`# (libra)“ ikonu/klávesnici.
