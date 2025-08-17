================
Kancelářské odpovědi
================

*Kancelářské odpovědi* jsou vlastní vstupy, kde zkratka klávesnice vyplňuje delší odpověď.
uživatel zadá klíčové slovo, které je poté automaticky nahrazeno rozšířenou náhradou.
odpověď. Používání předdefinovaných odpovědí ušetří čas, protože umožňují uživatelům používat zkratky k vyplnění delších textů.
zprávy. To také omezuje možnost chyb při psaní delších zpráv, protože
Jsou předdefinované zprávy, které zajišťují konzistentní chování v průběhu interakce s klientem.

Kancelářské odpovědi se skládají ze dvou hlavních částí: zkratky a náhrady. Zkratka
Je to klíčové slovo nebo fráze, která má být nahrazena. Substituce je delší zpráva
nahrazuje zkratku.

... obrázek: canned_responses/canned-response-sample.png
:alt:Živý chat s použitím předpřipravených odpovědí.

K dispozici jsou předpřipravené odpovědi:ref: použít v konverzacích v sekci „Živý chat“
Aplikace **Diskuse** a kompozér *Chat*. To zahrnuje soukromé konverzace i kanály
konverzace a zprávy v aplikaci WhatsApp.

..._diskutovat/vytvořené odpovědi:

Vytváření předpřipravených odpovědí
=========================

Připravené odpovědi jsou spravovány v aplikaci **Discuss**. Chcete-li vytvořit novou připravenou odpověď,
nebo spravovat seznam existujících odpovědí, přejděte na:menu: „Diskuse aplikace --> Konfigurace
--> Připravené odpovědi“.

Pak klikněte na tlačítko „Nový“ v horním levém rohu seznamu.
odhaluje novou prázdnou řádku v seznamu.

Kancelářské odpovědi se skládají ze dvou hlavních komponent - zkratky, kterou uživatel zadává, a
*náhradní zkratka*, která nahrazuje zkrácení.

.. obrázek:: canned_responses/shortcut-substitution.png
:alt: Seznam předpřipravených odpovědí, které zdůrazňují zkratky a položky pro nahrazení.

Do pole „Zkratka“ zadejte příkazovou zkratku. Poté klikněte na
:guilabel: pole „Výměna“ a zadejte text, který nahradí zkratku.

..tip:
Zkuste spojit zkratku s tématem výměny. To vám usnadní orientaci.
aby bylo možné používat odpovědi, zabraňuje tomu, aby se seznam odpovědí stal neuspořádaným.
převládající.

Do pole :guilabel:`Popis` zadejte jakoukoliv informaci, která poskytuje kontext pro tuto odpověď.
například pokyny, kdy by se mělo a nemělo používat.

V poli :guilabel:`Vytvořeno uživatelem` se automaticky zobrazí jméno uživatele, který vytváří
nový odpovědní formulář. Tento pole nelze upravit.

Chcete-li odpověď sdílet s dalšími uživateli, vyberte jeden nebo více
Skupiny, které by měly mít přístup, a uveďte je do pole „Autorizovaná skupina“.

.. varování:
Pokud pole „Autorizovaná skupina“ nebude vyplněno, odpověď může být použita jen a pouze
uživatel, který ji vytvořil.

Automaticky jsou kreditovány jako vytvořené uživatelem *OdooBot*.
musí být přiřazeny k autorizované skupině, než je může používat jakákoliv osoba. Chcete-li zobrazit
odpovědi vytvořené robotem Odoo, přejděte na: „Diskuse aplikace --> Konfigurace -->
„Kancelářské odpovědi“. Vyhledejte v poli „Hledat“ a odstraňte všechny filtry.

Poslední pole „Poslední použití“ uchovává datum a čas každé odpovědi, která byla nejčastěji používána.
ještě nedávno použité. Toto pole nelze upravit.

..._diskuse/sdílení odpovědí:

Sdílejte odpovědi
===============

Kancelářské odpovědi jsou v základním nastavení k dispozici pouze uživateli, který je vytvořil.
Odpověď musí být sdílena s ostatními.

.. poznámka::
Uživatelé s oprávněním *Administrátor* mohou zobrazit a upravovat předpřipravené odpovědi vytvořené jinými
Uživatelé mohou používat aplikaci **Discuss**, ale jsou schopni ji používat jen v případě, že
zahrnut do autorizované skupiny, která byla přiřazena na řádku položky předpřipravených odpovědí.
na stránce „Připravené odpovědi“.

Přístup k společným odpovědím je udělován na úrovni skupin :ref:`<access-rights/groups>`.

Pro zobrazení skupin, do kterých je uživatel členem, nejprve zapněte režim vývojáře:
Pak přejděte na:menu-selection:Nastavení aplikace --> Uživatelé a společnosti --> Uživatelé“. Vyberte uživatele
seznam a klikněte na otevření jejich „Záznam uživatele“. Poté klikněte na „Skupiny“ chytrý odkaz.
tlačítko v horní části stránky.

..tip:
Pro zobrazení seznamu uživatelů v konkrétní skupině nejprve zapněte :doc:`Rozvojový režim.
</>generální/rozvojářský režim>. Následně přejděte do sekce „Nastavení aplikace“ --> „Uživatelé a
Společnosti --> Skupiny. Vyberte skupinu z seznamu, pak klikněte na tlačítko pro otevření :guilabel:Skupina
Záznamy. Seznam uživatelů je zahrnut na záložce :guilabel:`Uživatelé`.

Po určení skupin, které mají mít přístup k odpovědi, musí být tyto skupiny **přidány
„Diskuse“ a „Vytvořené odpovědi“ do pole „Autorizované skupiny“ pro každou předdefinovanou
Odpověď.

.. poznámka::
Uživatel, který odpověď vytvořil, ji může používat i když není členem jedné ze skupin.
*Autorizované skupiny*.

..._diskutovat o případových studiích:

Použijte předpřipravený odpověď
=====================

Kancelářské odpovědi lze použít v aplikaci **Discuss**, v konverzaci **Live Chat** nebo na jakémkoli
záznam obsahující kompozici *Chatter*. To zahrnuje soukromé konverzace i kanály
konverzace a zprávy v aplikaci WhatsApp.

Pro použití předpřipravené odpovědi zadejte do kompozéru nebo okna chatu lomítko ( : ), následované
zkratku. Pak stiskněte klávesovou zkratku :kbd:`Enter`, což nahradí zkratku náhradou, ale
Odpověď lze ještě upravit před odesláním.

..tip:
Vložením znaku „:“ do pole pro psaní v aplikaci Chatter nebo okně chatu se vygeneruje seznam
dostupných odpovědí v podobě hotových textů. Odpověď lze vybrat z nabídky, nebo ji lze použít
zkratky.

Pro prohledávání dostupných odpovědí zadejte :, následované prvními písmeny vaší otázky.
zkratka.

.... obrázek: canned_responses/canned-responses-using.png
:alt:Okno živého chatu s seznamem všech dostupných předpřipravených odpovědí.

.. viz též:
   - :doc:`Hovor <chatter>`
   - :doc:`Diskuse <../discuss>`
   - :ref:`Komandy a přednastavené odpovědi <live-chat/canned-responses>“
