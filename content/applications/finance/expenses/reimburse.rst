===================
Zaměstnance odškodnit
===================

Po zveřejnění výkazu o nákladech je :doc:`výkaz o nákladech <../expenses/post_expenses>
Dalším krokem je vrácení peněz zaměstnanci. Stejně jako schválení a zveřejnění výdajů mohou být zaměstnanci
a v hotovosti nebo šekem.
<náklady/vracet jednotlivě> nebo :ref:`ve velkém <náklady/vracet ve velkém>), nebo :ref:`vrácené
Příkaz pro vystavení mezd.

Nastavení
========

Vrácení peněz lze provést výplatou, šekem, hotově nebo převodem na účet.
Nejprve nastavte různé možnosti přes:
Konfigurace --> Nastavení.

Vracet zaměstnancům náklady:ref:`v jejich výplatních páskách <expenses/reimburse-paystub>`, zaškrtněte
zaškrtávací políčko vedle možnosti „Vrácení v daňovém dokladu“ v sekci „Náklady“.

Dále nastavte způsob platby v sekci „Účetnictví“ a klikněte na rozbalovací nabídku
pod položkou „Způsoby platby“ a vyberte požadovaný způsob platby. Výchozí možnosti zahrnují
platba pomocí :guilabel:`Manuální (Hotovost), :guilabel:`Šeky (Banka), :guilabel:`NACHA (Banka)
jiných. Nevyplněním pole umožňuje použití všech dostupných způsobů platby.

Když jsou všechny požadované konfigurace dokončeny, klikněte na tlačítko „Uložit“, abyste aktivovali nastavení.

... výdaje/výplata jednotlivých zaměstnanců:

Vracet individuálně
======================

Pro vrácení individuální faktury za výdaje přejděte na:
Zprávy o výdajích. Všechny zprávy o výdajích jsou představeny v základním pohledu na seznamu. Klikněte na výdaje
Zprávu o výdaji lze zobrazit, pokud je vyplněna a uhrazena.

.. důležité::
*Výdajové faktury s stavem „Přijato“ lze vyúčtovat pouze v případě, že mají tento stav.

Klikněte na tlačítko „Registrace platby“ v levém horním rohu faktury a
Otevře se okno „Registrace platby“. Do tohoto okna zadejte následující informace
okno:

- :guilabel:`Kniha účetních záznamů“: Vyberte účetní knihu, do které chcete přidat platbu pomocí rolovací nabídky
menu. Výchozí možnosti jsou: „Banka“ nebo „Hotovost“.
- Vyberte způsob platby z nabídky. Pokud
Pokud je zvolen „Cash“ pro „Journal“, jediná dostupná možnost je
:guilabel:`Návod“. Pokud je vybrána volba :guilabel:`Banka“ pro :guilabel:`Deník“, výchozí
Možnosti jsou: „Manuální“ nebo „Kontroly“.
- :guilabel:`Účet příjemce“: Vyberte účet zaměstnance, na který je platba odeslána
Pokud zaměstnanec má uvedený bankovní účet v záložce „Soukromé informace“
v sekci „Soukromé informace“ svého formuláře pro zaměstnance v aplikaci **Zaměstnanci**.
populuje pole výchozí hodnotou.
- :guilabel:`Částka“: Toto pole se automaticky vyplní celkovou částkou vrácené.
měna, která je umístěna vpravo od pole, může být upravena pomocí vyskakovacího seznamu.
- :guilabel:`Datum platby“: Zadejte datum, kdy jsou peníze vyplaceny do tohoto pole.
populuje pole výchozí hodnotou.
- :guilabel:`Memo“: Text, který je zadán v :doc:`Souhrnu výdajů
Toto pole se automaticky vyplní z políčka „Expense Report“ v záložce „Náklady“.

.. obrázek:vratka.png
:align:center
:alt:Pop-up okno pro registraci platebního příkazu vyplněné pro individuální fakturu
náhrada.

Když jsou pole v okně doplněna, klikněte na tlačítko „Vytvořit platbu“.
Zapíšou platbu a zaměstnanci vrátí peníze.

... výdajů/výplata hromadně:

Velkoobchodně vracet
=================

Pro vrácení více výdajových zpráv najednou přejděte na: „Aplikace pro výdaje --> Výdaje
Zobrazit všechny výdajové zprávy v seznamovém pohledu. Poté upravte filtry „Stav“ podle
vlevo pouze nákladové faktury s stavem „Přijato“.

.. tip::
Upravit filtry „Stav“ tak, aby zobrazovaly pouze faktury za služby s „Vystaveno“, není
Je nutné, ale odstraňuje krok výběru každého jednotlivého hlášení v seznamu.

Zaškrtněte políčko vedle názvu sloupce „Zaměstnanec“ a vyberte všechny zprávy v
seznam. Po zaškrtnutí se v horní části stránky zobrazí počet vybraných faktur.
(:guilabel:'(#) Vybráno'). Dále se také objeví tlačítko pro registraci platby (:guilabel:'Registrace platby').
v horním levém rohu.

.. obrázek: vyrovnat se/více zpráv.png
:align:center
:alt:Výdajové faktury filtrované podle stavu Odesláno, což umožňuje zobrazit tlačítko Registrace platby.

Klikněte na tlačítko „Registrace platby“ a v okně „Registrace platby“
Zobrazí se okno s následujícími informacemi:

- :guilabel:`Kniha účetních záznamů“: Vyberte účetní knihu, do které se má platba zaevidovat, pomocí
nabídce. Výchozí možnosti jsou „Banka“ nebo „Hotovost“.
- Vyberte způsob platby z nabídky. Pokud
Pokud je zvolen „Cash“ pro „Journal“, jediná dostupná možnost je
:guilabel:`Návod“. Pokud je vybrána volba :guilabel:`Banka“ pro :guilabel:`Deník“, výchozí
Možnosti jsou: „Manuální“ nebo „Kontroly“.
- :guilabel:`Souhrnné platby“: Když je pro stejného zaměstnance vybráno více výdajových hlášení,
se zobrazí možnost. Zaškrtněte políčko pro jednorázovou platbu namísto vydání více plateb.
platby stejnému zaměstnanci.
- :guilabel:`Datum platby“: Zadejte datum, kdy jsou peníze vyplaceny.
pole, pokud není uvedeno jinak.

.. obrázek: vracet-registrovat.png
:align:center
:alt:V okně Poplatek zaplacený se vyplnilo.

Když jsou pole v okně s připnutou lištou vyplněna, klikněte na tlačítko Vytvořit platby.
zaregistrovat platby a zaměstnance vyplatit.

... výdaje/výplatní pásky:

Informace v příštím výplatním lístku
======================

Pokud je aktivována možnost „Vrácení v výplatní pásce“ na stránce Nastavení, mohou být platby přidány do
jejich další výplatní pásku namísto ručního vystavení.

.. důležité::
Zaúčtování výdajů na mzdových listech lze provádět pouze individuálně, v případě cestovních náhrad na
*Schválený* stav. Jakmile bude mít výkaz nákladů stav *Zveřejněno*, nebude možné jej znovu vyplatit.
Výplatní páska se nenachází v následujícím výpisu.

Přejděte na:menu:„Aplikace pro výdaje --> Zprávy o výdajích“ a klikněte na jednotlivý výdaj.
zaplaceno na následující výplatní pásku. Klikněte na „Zaplatí se v příštím výplatním termínu“.
tlačítko chytré, a náklady se přičítají k další výplatní pásce vystavené pro daného zaměstnance. Dále
v chatu je zaznamenáno sdělení, že výdaj bude přičten k následujícímu výplatnímu listu.

.. obrázek: vracet/platit prostřednictvím výplatního lístku.png
:align:center
:alt:Tlačítko Přehled v příštím výplatním listu je viditelné pouze s stavem schváleného přehledu.

Stav faktury zůstává:guilabel:„Schváleno“. Stav se mění pouze na
„Vyplatit“ (a pak „Hotovo“) při zpracování výplaty.

.. viz též:
Více informací o výplatních páskách naleznete v dokumentaci :doc:`Výplatní pásky <../../hr/payroll/payslips>`.
zpracování výplatních pásek.
