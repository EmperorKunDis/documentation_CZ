=====
Forum
=====

**Fórum Odoo** je otázka-odpověď fórem, které bylo navrženo s myšlenkou na poskytování zákaznického servisu.
Přidáním fóra na webovou stránku získáte komunitu, povzbudíte zapojení uživatelů a budete sdílet
znalosti.

..._forum/create:

Vytvořit fórum
==============

Pro vytvoření nebo úpravu fóra přejděte na: „Webová stránka --> Konfigurace --> Fórum: Fóra“. Klikněte
:guilabel:`Nový“ nebo vyberte existující fórum a nakonfigurujte následující prvky.

:guilabel:`Název fóra“: přidejte název fóra.

:guilabel:`Režim“: vyberte „Otázky“, abyste mohli označit odpověď jako nejlepší.
Poté se otázka zobrazí jako „vyřešená“ nebo „:guilabel:Diskuse“, pokud není potřeba.

.. poznámka::
I v případě zvoleného režimu je možné odpovědět pouze jednou na jeden příspěvek.
Komentovat lze vícekrát, ale...

:guilabel:`Výchozí řazení“: vyberte, jaké otázky budou vypadat výchozím způsobem.

  - :guilabel:`Nejnovější“: podle data poslední odpovědi
  - :guilabel:`Poslední aktualizace“: datem posledního vkládání příspěvků (odpovědi a komentáře zahrnuty)
  - :guilabel:'Nejvíce hlasů': podle počtu hlasů
  - :guilabel:`Důležitost“: dle relevančního hodnocení (výpočet podle vzorce)
  - :guilabel:`Odpovězeno“: podle pravděpodobnosti odpovědi (určeno vzorcem)

.. poznámka::
Uživatelé mají několik možností třídění (celkový počet odpovědí, celkový počet zobrazení, poslední aktivita).
přední část.

Vyberte možnost „Otevřené“ pro zobrazení fóra všem uživatelům nebo „Přihlášení“ pro zobrazení pouze přihlášeným.
aby bylo viditelné pouze pro přihlášené uživatele nebo „Některým uživatelům“ aby bylo viditelné jen pro ně.
specifickou skupinu uživatelů vybráním jedné z následujících:

Poté nastavte zisky karmy a práva související s karmu.
<forum/prava-související-s-karma>.

..._forum/karma:

Body karmy
------------

Body karmy mohou být uděleny uživatelům na základě různých interakcí v fóru. Mohou být použity k
určit, které funkce fóra uživatelé mohou používat, od hlasování v příspěvcích po
mají práva moderátora. Jsou také používány k nastavení hodností uživatelů:

.. důležité:
   - Body kreditu uživatele jsou sdíleny mezi všemi fóry, kurzy atd. jednoho webu OpenERP.
   - Uživatelé e-learningu mohou získat body za různé interakce s kurzem.
a také :ref:`úkoly <elearning/task> a testy <elearning/quiz>.

..._forum/karma-gains:

Karma získává
~~~~~~~~~~~

Několik interakcí na fóru může přidat nebo odebrat body kreditu.

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Interakce
     - Popis
     - Normální zisk kreditu
   * --:guilabel:Zadání otázky
     - Zveřejníte otázku.
     - 2
   * – :guilabel:`Otázka označena jako upravená“
     - Další uživatel hlasuje pro otázku, kterou jste položili.
     - 5
   * -- :guilabel:`Dotaz snížený o hodnocení“
     - Další uživatel hlasuje proti otázce, kterou jste položili.
     - -2
   * :-:guilabel:`Odpověď s hlasy“
     - Další uživatel hlasuje pro odpověď, kterou jste zveřejnili.
     - 10
   * -- :guilabel:`Odpověď s hlasem dolů“
     - Další uživatel hlasuje proti odpovědi, kterou jste zveřejnili.
     - -2
   * Přijetí odpovědi
     - Označíte odpověď jiného uživatele jako nejlepší.
     - 2
   * Odpověď přijata
     - Další uživatel označí odpověď, kterou jste zveřejnili, jako nejlepší.
     - 15
   * – :guilabel:`Odpověď označena jako spam“
     - Vaše otázka nebo odpověď je označena jako „urážlivé“ (<forum/moderation>).
     - -100

.. poznámka::
Noví uživatelé získávají **tři body** po ověření své e-mailové adresy.

Pro změnu výchozích hodnot přejděte na: „Webové stránky - Konfigurace - Fórum: Diskusní fóra“.
Vyberte fórum a přejděte na záložku „Zisk karmy“. Vyberte hodnotu, kterou chcete upravit.

Pokud je hodnota kladná (např. „5“), bude každý bod přičten ke skóre uživatele
Čas interakce na vybraném fóru. Naopak pokud je hodnota záporná (např.
(-5), bude počet bodů odečten. Použijte hodnotu 0, pokud interakce nemá na uživatele vliv
také.

.._forum/prava-související-s-karmu:

Pravidla související s karma
~~~~~~~~~~~~~~~~~~~~

Konfigurace počtu potřebných bodů karmy pro přístup k různým funkcím fóra najdete
Vyberte webové stránky --> Konfigurace --> Fórum: Fóra“, vyberte fórum a přejděte na
Karta „Související práva karmy“. Vyberte hodnotu, kterou chcete upravit.

.. varování:
Některé funkce, například „Upravit všechny příspěvky“, „Zavřít všechny příspěvky“
:guilabel:`Smazat všechny příspěvky“, :guilabel:`Upravit příspěvky“ a :guilabel:`Odpojit všechny komentáře“.
Jsou poměrně citlivé. Ujistěte se, že chápete důsledky udělení jakékoli oprávnění uživateli, který dosáhne
nastavit požadavky na karmu pro přístup k takovým funkcím.

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Funkčnost
     - Popis
     - Požadavek na karmické body
   * – :guilabel:`Zeptejte se“
     - Položte otázky.
     - 3
   * Odpovězte na otázky
     - Odpovídejte na otázky.
     - 3
   * –:guilabel:`Hlasovat pro“
     - Hlasujte pro otázky nebo odpovědi.
     - 5
   * :-:downvote
     - Hlasovat proti otázkám nebo odpovědím.
     - 50
   * – :guilabel:`Upravit vlastní příspěvky“
     - Upravujte otázky nebo odpovědi, které jste zveřejnili.
     - 1
   * – :guilabel:`Upravit všechny příspěvky“
     - Upravte jakoukoliv otázku nebo odpověď.
     - 300
   * – :guilabel:`Zavřít vlastní příspěvky“
     - Zavřete otázky nebo odpovědi, které jste zveřejnili.
     - 100
   * Zavřít všechny příspěvky
     - Zavřít jakoukoliv otázku nebo odpověď.
     - 500
   * – :guilabel:`Smazat vlastní příspěvky“
     - Smazat otázky nebo odpovědi, které jste zveřejnili.
     - 500
   * --:guilabel:`Smazat všechny příspěvky“
     - Odeberte jakoukoliv otázku nebo odpověď.
     - 1,000
   * :- guilabel:Nofollow odkazy
     - Pokud jste pod hranicí karmy, atribut *nofollow* vyzývá vyhledávače k ignorování
odkazy, které sdílíte.
     - 500
   * Přijmout odpověď na vlastní otázku
     - Označte odpověď jako nejlepší na otázky, které jste položili.
     - 20
   * –:guilabel:`Přijmout odpověď na všechny otázky“
     - Označte odpověď jako nejlepší na jakékoliv otázce.
     - 500
   * -:guilabel:`Vlastnosti editoru: obrázky a odkazy“
     - Přidejte odkazy a obrázky do svých příspěvků.
     - 30
   * --:guilabel:`Komentovat vlastní příspěvky“
     - Přidávejte komentáře pod otázky nebo odpovědi, které jste vytvořili.
     - 1
   * -- :guilabel:`Komentuj všechny příspěvky“
     - Přidávejte komentáře pod jakoukoliv otázku nebo odpověď.
     - 1
   * -- :guilabel:`Převádět vlastní odpovědi na komentáře a naopak“
     - Převádějte své komentáře na odpovědi.
     - 50
   * -- :guilabel:`Převést všechny odpovědi na komentáře a naopak“
     - Převádějte komentáře na odpovědi.
     - 500
   * --:guilabel:Odpojit vlastní komentáře
     - Smazat komentáře, které jste zveřejnili.
     - 50
   * – Odpojit všechny komentáře
     - Smazat jakýkoliv komentář.
     - 500
   * – :guilabel:`Kladně vyjádřené otázky bez ověření“
     - Otázky, které zadáte, nemusí být předem „ověřeny“ podle pokynů v článku Moderace.
     - 100
   * – Označit příspěvek jako nevhodný
     - Značte otázku nebo odpověď jako nevhodné.
     - 500
   * -- :guilabel:`Střední příspěvky“
     - Přejděte do sekce „Moderace“ a klikněte na tlačítko „Upravit“.
     - 1,000
   * – :guilabel:`Změnit otázku“
     - Změňte „tagy“ otázek, které jsou vložené do fóra.
     - 75
   * Vytvořit nové štítky
     - Vytvářejte nové tagy při vkládání otázek.
     - 30
   * Zobrazit podrobné informace o uživateli
     - Když uživatel přejede myší nad vaším avatarem nebo uživatelským jménem, objeví se vpravo od nich malé okno.
bodů karmy, životopisu a počtu :ref:`známek <forum/badges>“ na každém stupni.
     - 750

..tip:
Sledovat všechny aktivity týkající se karmy a ručně přidávat nebo odebírat karmu pomocí:
režimu vývojáře (developer-mode) a přejít na: „Nastavení“ --> „Gamifikační nástroje“ --> „Karma“.
„Sledování“.

..._forum/gamifikace:

Gamifikace
------------

Hodnost a odznaky mohou být použity k podpoře účasti. Hodnosti jsou založené na celkovém :ref:`karma
body <forum/karma>“, zatímco odznaky mohou být uděleny ručně nebo automaticky po dokončení
výzvy.

..._forum/ranky:

Hodnost
~~~~~

Pro vytvoření nových nebo změnu výchozích hodnot jděte do: „Webové stránky“ - „Konfigurace“
Fórum: Hodnost a kliknutí: guilabel: Nový nebo vyberte existující hodnost.

Přidejte pole „Hodnost jméno“, „Požadované body karmy“ a „Dosažená hodnost“.
:guilabel:Popis, zprávu motivující uživatele k dosažení cíle a
obrázek.

.. obrázek:forum/hody.png
:alt: Hodnost fóra

.._forum/známky:

Náramky
~~~~~~

Pro vytvoření nových štítků nebo pro úpravu výchozích štítků přejděte na:
Fórum: Štítky a kliknutí na štítek „Nový“ nebo vyberte existující štítek.

Zadejte název a popis odznaku, přidejte obrázek a nakonfigurujte jej.

Přidělit ručně
***************

Pokud má být odznak udělen ručně, vyberte uživatele, kteří jej mohou udělit, z
následujících možností:

- :guilabel:Všichni uživatelé, kteří nejsou portálem (protože odznaky uděluje zadní část).
- :guilabel:`Seznam vybraných uživatelů“: uživatelé vybraní pod :guilabel:`Oprávnění uživatelé“.
- :guilabel:`Lidé s nějakými štítky“: uživatelé, kteří byli označeni štítky vybranými pod
:guilabel:`Požadované odznaky“.

Můžete omezit, kolikrát za měsíc může uživatel udělit odznak tím, že zapnete
„Omezená měsíční zásilka“ a vložte „Počet omezených zásilek“.

Přiřadit automaticky
********************

Pokud by mělo být ocenění uděleno automaticky při splnění určitých podmínek, vyberte
„Nikdo, kdo byl přidělen na základě výzev“ pod „Povolení udělit“.

Dále určete, jak bude udělován odznak kliknutím na tlačítko „Přidat“ pod
sekci Odměny za výzvy. Vyberte výzvu, kterou chcete přidat nebo vytvořit novou kliknutím
:guilabel:`Nový“.

..tip:
Je možné udělit štítku hodnost „Forum Badge Level“ („Bronz“,
:gui-label:"Stříbrný", :gui-label:"Zlatý") pro zvýraznění nebo zeslabení důležitosti.

.. obrázek:forum/badges.png
:alt:Národní státní vlajka

..._forum/tagy:

Štítky
----

Uživatelé mohou používat tagy k filtrování příspěvků na fóru.

Pro správu štítků přejděte na: „Webová stránka --> Konfigurace --> Fórum: Štítky“. Klikněte
:guilabel:`New“ vytvořit štítek a vybrat příslušný „Forum“.

..tip:
   - V sekci „Štítky“ na liště fóra můžete filtrovat všechny otázky přiřazené k
vybraný štítek. Klikněte na tlačítko „Zobrazit všechny“ pro zobrazení všech štítků.
   - Nové tagy lze vytvářet při psaní nového příspěvku, pokud uživatel má dostatek „karmy“
bodů v sekci „Karma a práva“

..._forum/pouziti:

Použijte fórum
===========

.. poznámka::
Přístup k mnoha funkcím závisí na počtu karma bodů uživatele.
<forum/práva související s karma>.

.._forum/post:

Položte otázky
--------------

Pro vytvoření nového příspěvku přejděte do přední části fóra, klikněte na „Nový příspěvek“ a vyplňte
následující:

- :guilabel:`Název tématu`: přidejte otázku nebo téma příspěvku.
- :guilabel:`Popis otázky“: přidejte popis k otázce.
- :guilabel:`Štítky“: přidejte až pět :ref:`štítků <forum/tags>“.

Klikněte na tlačítko „Zveřejněte svůj dotaz“.

..._forum/interact:

Interagujte s příspěvky
-------------------

K příspěvku lze provádět různé akce.

- Označte otázku jako oblíbenou kliknutím na tlačítko hvězdičky (:guilabel:„☆“).
- Sledujte příspěvek a získejte oznámení (e-mailem nebo v rámci Odoo) při jeho odpovědi kliknutím na
tlačítko zvonku (:guilabel:`🔔`).
- Hlasovat pro nebo proti otázce
Odpověď.
- Označte odpověď jako **nejlepší** kliknutím na tlačítko s vykřičníkem (:guilabel:`❌`). Tato možnost je
je k dispozici, pokud je nastaven režim „Fórum“ na „Otázky“.
- Odpovědět na otázku.
- Komentář k otázce nebo odpovědi přidáte klepnutím na tlačítko s mluvícím bublinou (:guilabel:`💬`).
- Položku sdílejte na Facebooku, Twitteru nebo LinkedInu kliknutím na tlačítko „Sdílet“.

Klikněte na tlačítko s elipsou (:guilabel:`...`):

  - :guilabel:`Upravit otázku nebo odpověď.“
  - :guilabel:`Zavřít“ otázku.
  - Odpověď nebo otázku smazat. Je možné odpověď nebo otázku také „obnovit“.
otázky později.
  - Označit otázku nebo odpověď jako urážlivé.
  - Komentář převést na odpověď.
  - :guilabel:`Zobrazit“ příslušný „Pomocník“ (viz „Tiket pomocníka“).

.. obrázek: forum/post-actions.png
:alt: Akce u příspěvku

.. poznámka::
Výchozí hodnota je 150 bodů karmy pro zobrazení profilu jiného uživatele. Tato hodnota může být
je nastaven při vytváření nové webové stránky.

.._fórum/moderace:

Moderovat fórum
================

Na předním konci fóra je v sekci „Nástroje pro moderátory“ shromážděno to nejpodstatnější.
moderátorské funkce.

.. obrázek:forum/moderacni-nastroje.png
:alt: Nástroje pro moderování na bočním panelu fóra

:validace: přístup k otázkám a odpovědím, které čekají na schválení
zobrazované uživatelům, kteří nejsou moderátory.

.. obrázek:forum/validace.png
:alt:Dotaz k ověření

.. poznámka::
Pokud uživatel nemá potřebný kredit, je otázka otevřená. Uživatel není schopen vložit příspěvek
otázky nebo odpovědi, zatímco čeká na schválení. Každému uživateli je povoleno pouze jedna nevyřízená otázka.
fórum.

:guilabel:`Označené“: zobrazte všechny otázky a odpovědi, které byly označeny jako nevhodné. Klikněte
:guilabel:„Přijmout“ k odstranění urážlivé vlajky nebo „Urážlivá“ pro potvrzení. Pak vyberte
důvod a klikněte na „Označit jako urážlivé“. Příspěvek je pak skryt před uživateli bez
právo moderátora a odpočet 100 bodů z hodnocení uživatele, který se provinil.

.. obrázek:forum/ofenzivni-duvod.png
:alt: Výběr osoby s agresivním chováním

:guilabel:`Zavřeno“: přístup k všem otázkám, které byly zavřeny. Je možné :guilabel:`Smazat“
nebo:reopen: otázku. Zavřít otázku znamená otevřít ji, kliknout na tlačítko s tečkami
(:guilabel:'...'), pak :guilabel:'Zavřít', vyberte důvod zavření, a klikněte
:guilabel:`Uzavřít příspěvek“. Příspěvek je pak skryt před uživateli bez práv k moderování.

.. poznámka::
Vyberte možnost „Spam nebo reklama“ nebo „Obsahuje vulgární nebo urážlivý obsah“.
„poznámky“ jako důvod, odečte se z účtu uživatele 100 bodů karmy.

..tip:
   - Vytvořte a upravte důvody pro uzavírání témat přes:
Zavřít důvody. Vyberte „Základní“ jako „Typ důvodu“, pokud se má důvod zobrazit
používá se při uzavírání otázky a :guilabel:`Ostrý` pro příspěvky s označením.
   - Veškeré příspěvky spravujte přes: „Webové stránky --> Konfigurace --> Fórum: Fóra“.
Vyberte fórum a klikněte na tlačítko „Příspěvky“. Po kliknutí se zobrazí
tlačítko „Akce“, je možné provést export, archivování.
:guilabel:`Obnovit“ nebo „Smazat“ jeden nebo více příspěvků.
