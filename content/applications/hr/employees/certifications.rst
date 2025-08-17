==============
Certifikace
==============

Když je pro práci potřeba konkrétní znalost, musí se sledovat certifikace zaměstnanců, aby se zajistilo
je k dispozici potřebné vzdělání a certifikace.

Když jsou požadovány konkrétní znalosti, sledujte certifikace zaměstnanců (např. kurzy, testy, semináře).
ověřit požadované dovednosti. Odoo přijímá jakýkoli typ certifikátu bez omezení.

.. důležité::
Chcete-li do profilu zaměstnance přidat certifikáty a zobrazit si hlášení *Certifikace zaměstnanců*,
Aplikace **Průzkumy** musí být nainstalována.

Zobrazit certifikáty
===================

Pro zobrazení celého seznamu všech certifikací zaměstnanců přejděte na:
Hlášení-->Certifikace.

Všechny certifikace se zobrazují v přehledu, řazené podle zaměstnance. Každý záznam o certifikaci zobrazuje
následující:

- :guilabel:`Zaměstnanec“: jméno zaměstnance spolu s jeho avatary.
- :guilabel:`Název“: název certifikátu.
- :guilabel:`Platnost od“: datum, kdy zaměstnanec obdržel certifikaci.
- :guilabel:`Platnost končí“: když vyprší platnost certifikátu.
- :guilabel:`Ověření“: odpovídající kurz v aplikaci „Průzkumy“, který absolvoval
pracovníkovi, pokud je to možné.

Přihlášky jsou také barevně označené. Platné certifikáty jsou černě,
Vypršené certifikáty jsou zobrazeny červeně a certifikáty, které vyprší do 90 dnů, jsou označeny žlutě.
Dny jsou oranžové.

.. obrázek: certifikace/certifikace.png
:alt: Seznam certifikací zaměstnanců.

.. důležité::
**Pouze** certifikační záznamy s nastaveným typem zobrazení na „Certifikace“
:ref:`Certifikační formulář <zaměstnanci/certifikace-formulář> se objeví na :guilabel:`Zaměstnanec
Zpráva o certifikacích. Ostatní certifikace se nachází v části životopisu.
:ref:`formulář zaměstnance <employees/cv>`.

Zobrazení certifikátů podle stavu platnosti
----------------------------------------

Při řízení velkého počtu zaměstnanců s různými certifikáty může být obtížné
určit, které zaměstnanci potřebují mít platné certifikáty v seznamu výchozího zobrazení.
Tento scénář je vhodné zobrazit s vyznačením platnosti certifikátu.

Pro toto vyberte v nabídce „Mzdy a personalistika“ -> „Zprávy“ -> „Certifikace“.
Ikona „fa-caret-down“ (Přepínání panelu vyhledávání) v liště hledání a klikněte
:guilabel:`Přidat vlastní skupinu“  :icon:`fa-caret-down“, což odhalí seznam. Klikněte
:guilabel:'Stav vypršení platnosti', pak klikněte mimo rozbalovací nabídku, abyste ji zavřeli.

Po provedení takového kroku jsou všechny certifikáty seřazeny podle stavu, začínajíc od:guilabel:`Vypršel platnost`.
certifikáty, pak certifikáty, které brzy vyprší (do 90 dnů).
a nakonec certifikáty, které jsou stále platné.

Filtrujte certifikáty podle jejich platnosti a zjistěte, které certifikáty brzy vyprší.
Zaměstnanci, kteří musí obnovit.

.. obrázek: certifikace/stavy.png
:alt: Seznam certifikací zaměstnanců, seřazený podle stavu.

..._zaměstnanci/certifikace-formulář:

Zaznamenat certifikaci
===================

Pro zaznamenání certifikace pro zaměstnance přejděte na: „Zaměstnanci aplikace -> Zprávy ->
Certifikáty“. Klikněte na „Nový“ a vložte následující
informace o formě:

- :guilabel:`Název certifikátu`: Zadejte krátký popis o certifikaci do tohoto pole.
- :guilabel:`Zaměstnanec“: Vyberte zaměstnance, který obdržel
certifikace.
- :guilabel:`Typ certifikátu“: Vyberte typ certifikátu z nabídky. Toto pole
určuje, kde na životopisu zaměstnance se certifikace objeví.
:guilabel:`Typ`, zadejte typ do pole a pak klikněte na :guilabel:`Vytvořit [typ]“.

Výchozí možnosti jsou:

  - :guilabel:Zkušenosti“: Vyberte tuto možnost, aby se certifikát zobrazoval v části „Zkušenosti“.
sekci záložky „Životopis“ v formuláři :doc:`nového zaměstnance <new_employee>“. Zkušenosti jsou
obvykle předchozí zaměstnání nebo stáže.
  - :guilabel:`Vzdělání“: Zvolte tuto možnost, abyste měli certifikát v sekci *Vzdělání*.
sekci záložky Resumé v novém formuláři zaměstnance.
  - :guilabel:`Sociální média“: Vyberte tuto možnost, pokud chcete, aby certifikát zobrazoval v sekci *Sociální média*.
Media* sekce záložky *Životopis* v záložce :doc:`nový zaměstnanec <new_employee>`. Sociální média
vstupy obvykle souvisí s certifikací v oblasti digitálního marketingu a sociálních médií
management a konkrétní školení od sociálních sítí.
  - Vyberte možnost „Interní certifikace“, pokud chcete, aby certifikaci bylo možné zobrazit v
*Interní certifikace* v sekci *Životopis* na kartě :doc:`zaměstnance <nový_zaměstnanec>`.
Vnitřní certifikační záznamy jsou spojeny s kurzy, školením nebo programem vytvořeným
společnost, která po dokončení bude mít k certifikaci připojenou.
  - :guilabel:`Dokončené vnitřní školení“: Vyberte tuto možnost, pokud chcete mít certifikaci zobrazenou
sekci *Dokončené vnitřní školení* na záložce *Životopis* v kartě zaměstnance.
<nový zaměstnanec>. Doplňky vzdělávání obvykle spadají do školení.
vytvořené společností pro specifické procesy této společnosti. Tyto nevedou k žádným
certifikáty, ale jsou uvedeny v profilu zaměstnance jako dokončené školení.

- V poli „Zobrazit typ“ vyberte, zda chcete certifikaci veřejně viditelnou nebo ne.
Možnosti jsou:

  - :guilabel:`Klasické“: Vyberte tuto možnost, pokud chcete mít certifikaci zobrazenou v sekci *Životopis*.
vzor zaměstnanecké žádosti a neobjevit se na výkazu *Zaměstnanecká certifikace*.
  - :guilabel:`Ověření“: vyberte tuto možnost, pokud chcete, aby se ověření zobrazilo v části „Životopis“.
:část formuláře zaměstnance, **a také** se objevit na výkazu „Certifikace zaměstnanců“.
Pokud je vybrán, objeví se pole „Certifikace“ pod poli „Zobrazovací typ“.
pole. Vyberte příslušného **Surveys** aplikaci certifikace z roletkového seznamu.
zaměstnance. Toto pole se zobrazí pouze v případě, že je nainstalována aplikace „Průzkumy“.
  - :guilabel:`Kurz“: Vyberte tuto možnost, abyste měli certifikaci zobrazenou v části „Životopis“.
zaměstnanecké formuláře a **ne** se objevit na výkazu *Certifikace zaměstnanců*.
Pokud je tato možnost vybrána, objeví se pod položkou „Zobrazovací typ“ pole „Kurz“.
pole. Vyberte příslušný kurz eLearning, který zaměstnanec absolvoval z roletky.
Toto pole se zobrazí pouze v případě, že je nainstalována aplikace eLearning.

- :guilabel:`Popis certifikátu“: Zadejte popis certifikátu do tohoto pole.
- Klikněte do pole Délka a zobrazí se kalendářové okno. Klikněte na
datum začátku a konce platnosti certifikátu.
Vyberte položku, klikněte na ikonu „fa-check“ a oba pole se zaplní.

.. obrázek: certifikace/kyberbezpečnost.png


.. poznámka::
Jakmile je pro zaměstnance zaznamenána certifikace, může být vytvořena nová certifikace stejného typu (tzn.
:guilabel:`Vzdělávání“ nebo „Interní certifikace“) lze přidat přímo z
formulář zaměstnance místo rozhraní „Certifikace zaměstnanců“.

V hlavním panelu aplikace **Správci zaměstnanců** klikněte na profil zaměstnance, abyste jej otevřeli.
formulář. V záložce „Životopis“ klikněte na tlačítko „Přidat“ v závěru formuláře.
odpovídající certifikační linka.

Tlačítko „Přidat“ se zobrazí pouze u profilů zaměstnanců, které již mají nějaké
certifikace.
