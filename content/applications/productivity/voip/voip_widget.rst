============
VoIP akce
============

.. |VOIP| nahradit za: zkratku: `VoIP (hlasová služba přes internetový protokol)`

VoIP widget je doplněk, který je k dispozici uživatelům Odoo po instalaci modulu VoIP.
správy mobilních zařízení pro každého obchodníka a hledání správných přepojení hovorů pro rozčilené zákazníky
Klienti nebo ti, kteří potřebují místnost pro konferenční hovor, využívají tlačítko VoIP.
vyřešit žádnou z těchto obchodních potřeb.

Nastavte widget VoIP
========================

Ve widgetu VOIP je tři záložky: „Poslední“, „Další aktivity“ a
„Kontakty“, které se používají pro správu hovorů a denních aktivit v Odoo.
vyhledávací lištu pro rychlejší vyhledání kontaktů.

.. obrázek:: voip_widget/voip-tabs.png
:alt:Kliknutelné tabulky VoIP.

Poslední záložka
----------

Pod záložkou „Poslední“ v widgetu VOIP je k dispozici historie hovorů uživatele.
To zahrnuje příchozí i odchozí hovory. Kliknutím na jakýkoli telefonní číslo můžete začít hovor.

Další karta s aktivitami
-------------------

Pod záložkou „Další aktivity“ v widgetu |VOIP| uživatel vidí všechny hovory přidělené
a které mají být dokončeny v průběhu dne.

Klikněte na aktivitu z této záložky a vyberte jednu z následujících akcí, abyste se připravili a dokončili.
pod nadpisem „Dokumenty“):

- Ikona „poštovní schránka“ :guilabel:„Poštovní schránka“: poslat e-mail kontaktu (např. kolegům nebo
klientů (zákazníků)
- :icon:`fa-user` :guilabel:`(uživatel)`: zobrazuje kontaktní informace pro tento kontakt
- :icon:`fa-file-text-o` :guilabel:`(dokumenty)`: zobrazuje připojený záznam v Odoo (např. prodej
(objednávky)
- :icon:`fa-clock-o` :guilabel:`(Aktivita)`: naplánovat aktivitu

Při prohlížení aktivity může uživatel také spravovat podrobnosti a stav aktivity:

- :icon:`fa-check` :guilabel:`(check)`: označuje aktivitu jako dokončenou
- :icon:`fa-pencil` :guilabel:`(edit)`: upravuje aktivitu (např. termín splatnosti)
- :icon:`oi-close` :guilabel:`(zavřít)`: zruší aktivitu

Pro zavolání zákazníka souvisejícího s plánovanou aktivitou klikněte na ikonu :icon:`fa-phone` :guilabel:`(telefon)`
ikonu. Klikněte na ikonu „fa-keyboard-o“ a zadejte jiný telefonní číslo.

Přidejte hovor
~~~~~~~~~~

Na domovské stránce databáze klikněte na :menuselection:`CRM aplikaci“. Na záložce :guilabel:`Pipeline“
je otevřený pro zobrazení Kanbanu. Následně klikněte na ikonu „oi-voip“ vpravo nahoře obrazovky.
ikona VoIP a ujistěte se, že widget VOIP je otevřen na kartě Další aktivity.
tabulku. Poté přejeďte myší nad příležitostí, která má mít hovor, a klikněte na ikonu:
:guilabel:`(telefon)` s malým zeleným :icon:`fa-plus` :guilabel:`plus“ ikonou.

.. obrázek: voip_widget/add-call.png
:alt:Prodejní příležitost s možností přidání hovoru do widgetu VoIP.

Chcete-li odstranit hovor z karty „Další aktivity“, přejeďte myší nad příležitostí, která má
schůzku naplánovali a klikněte na červený ikonu „telefon“ s popiskem „(telefon)“, který se objeví vedle
:icon:`fa-minus` :guilabel:`(-)`

.. obrázek: voip_widget/remove-call.png
:alt:Možnost prodeje s možností odstranit hovor z widgetu VoIP.

Karta Kontakty
------------

Pod záložkou „Kontakty“ v widgetu |VOIP| se uživatel dostane k kontaktu
Aplikace **Kontakty**.

Každý kontakt s uloženým telefonním číslem lze zavolat kliknutím na kontakt v |VOIP|
kartě „Kontakty“ v widgetu.

V horní části widgetu je také k dispozici vyhledávací funkce, která je znázorněna ikonou :icon:`fa-search`.
:guilabel:`(hledání)` ikona. Tento nástroj použijte k vyhledání konkrétního kontaktu. Plánované aktivity nebudou
zobrazit se jako výsledky vyhledávání.

Zavolejte přes VoIP
===========================

Jedním z hlavních účelů VoIP je umožnit telefonování bez potřeby telefonu. Zde jsou
tři způsoby, jak uskutečnit telefonní hovor v databázi Odoo. Prvním krokem je kliknutí na ikonu :icon:`oi-voip`.
ikona „Hlasové hovory“ (VoIP) v pravém horním rohu navigačního panelu.

- Zadejte telefonní číslo, které chcete zavolat kliknutím na ikonu „fa-keyboard-o“ :guilabel:„(klávesnice)“.
ikonu a poté telefonní číslo.
- Klikněte na ikonu „Telefon“ (telefon) a zavoláte poslední kontakt, který jste vytočili.
- Hledejte konkrétní kontakt podle jména nebo přejděte na záložku :guilabel:`Kontakty`. Pak vyberte
Kontaktujte nás a klikněte na ikonu :icon:`fa-phone` :guilabel:`(telefon)` .

Při přijímání hovorů v Odoo zazvoní |VOIP| widget a zobrazí se notifikace.
widgetu, klikněte na ikonu „OI-Close“ v horním pravém rohu widgetu.
obrazovka.

.. poznámka::
VoIP číslo je to, které poskytuje Axivox. Můžete se k němu dostat přes
„https://manage.axivox.com/<https://manage.axivox.com/>“_. Po přihlášení do portálu přejděte na
:menu_selecetion:`Uživatelé --> Odchozí číslo“ (sloupec)

Přenést hovor
---------------------

Přenos hovoru ručně lze provést pouze v době, kdy je aktivní hovor. Přenos hovoru uvnitř |VoIP|
widget, nejprve odpovězte na hovor pomocí ikony „Telefon“ (telefon).

Jakmile je hovor přijat, klikněte na ikonu „fa-arrows-h“ a zvolte „(levá/pravá šipka)“.
ikonu. Pak zadejte příponu uživatele, na kterého se má hovor přesměrovat. Nakonec klikněte
:guilabel:`Přeposlat“ hovor na tuto telefonní číslo.

..tip:
Pro zjištění rozšíření uživatele se obraťte na administrátora VoIP. Pokud má uživatel
:guilabel:`Administrace“ přístupová práva nastavená na „Nastavení“, pro vyhledání rozšíření přejděte do
Vyberte aplikaci „Nastavení“ a klikněte na ikonu „Pravítko“
tlačítko. Vyberte uživatele a přejděte na záložku VoIP. To je jejich telefonní číslo.
:guilabel:`Jméno VoIP“.

Pokud uživatel nezvedne hovor nebo je zaneprázdněn jiným hovorem, pak mohou být automaticky
přenesena. Toto se nastavuje u poskytovatele služby VoIP.

Přeposlat telefonní hovor
--------------------

Přeposlat hovor prostřednictvím widgetu |VOIP| je možné nejprve zvednout telefonickou linku pomocí ikony „Telefon“
:guilabel:`(telefon)` ikonu.

Poté klikněte na ikonu „směry nahoru a dolů“ (levá a pravá šipka). Zadejte plný telefon
číslo uživatele, na kterého by měl hovor být přeposlán. Nakonec klikněte na tlačítko „Přenést“ a zvolte
zavolat na tuto telefonní číslo.

Odeslat e-mail prostřednictvím VoIP widgetu
=====================================

Emaily můžete také odesílat přes widget |VoIP|, což je užitečné pro zasílání e-mailových zpráv s pokračováním
účastníci hovoru, kteří posílají svému kolegovi e-mail s dotazem nebo připomínají dodavateli, aby jim zaslali nějaké
komponenty během telefonického přepisu.

Pro odeslání e-mailu prostřednictvím widgetu VoIP klikněte na ikonku :icon:`oi-voip` :guilabel:`(VoIP)`
v horní liště nabídky. Po kliknutí se zobrazí
v levém dolním rohu stránky. Pak vyhledejte kontakt na e-mail nebo je najděte v
Kontakty“ v záložce widgetu „VoIP“.

Dále klikněte na ikonu :icon:`fa-envelope-o` :guilabel:`(envelope)` a poté vyberte e-mail.
přijímatelé, zadejte předmět e-mailu a napište e-mail. Když je připravený k odeslání, klikněte
:guilabel:`Odeslat“. K odeslání e-mailu později klikněte na ikonku „fa-caret-down“
Ikona „Odeslat později“ vedle ikony „Odeslat“, kliknutím na ni zvolte
v plánovaný čas a klikněte na tlačítko „Zařadit do rozvrhu“.

... _voip/voip_widget/troubleshooting_voip:

Řešení problémů s VoIP widgetem
===============================

Každá část níže popisuje běžné problémy s widgetem |VOIP| a jak je vyřešit.

Chybějící parametr
-----------------

Pokud se objeví chybová zpráva „chybějící parametr“, obnovte okno a zkuste to znovu.
znovu.

Chybný číslo
----------------

Pokud se zobrazí chybová hláška „Nesprávné číslo“, ujistěte se, že používáte
mezinárodní formát s ikonou „plus“ a následně
mezinárodní kód země (např. +1 650 691 3277, kde „+1“ je mezinárodní předvolba pro
Spojené státy).


Připojení k serveru přes WebSocket bylo ztraceno
------------------------------------------------------

Pokud dojde k chybě *WebSocket spojení s serverem bylo ztraceno. Zkuste stránku aktualizovat.*
zpráva se zobrazí v widgetu VoIP, pak stránku obnovte a zavřete ostatní záložky prohlížeče.

Tento problém způsobuje návrat do databáze po delší době nečinnosti, například během oběda.
je příliš mnoho otevřených záložek v prohlížeči.

Nepodařilo se spustit uživatelský agregát
------------------------------

Pokud se nezdařilo spustit uživatelské agenty. URL websocketu může být špatné. Prosím,
Administrátor ověří adresu websocket serveru v obecných nastaveních. V tomto případě se zobrazí chybová hláška
widget VOIP, pak aktualizujte prohlížeč a počítač.

Tento problém způsobuje prohlížeč nebo počítač, který není aktuální (a může také vést k problémům s
mikrofonu).

Změkčený widget pro hlasové služby
----------------------

Pokud je widget VoIP úplně šedý a nelze s ním interagovat, aktualizujte prohlížeč.
a počítač a odstranit rozšíření prohlížeče Google Chrome způsobující problém.

Nelze se připojit na VoIP telefonní číslo
---------------------------------------

Pokud uživatel nemůže připojit se na své VoIP číslo, pak v jeho profilu chybí
:guilabel:`Tajná VoIP“. K přidání klikněte na uživatelské avatary a poté na „Můj profil“.
Zde klikněte na záložku VoIP a pak zadejte tajný klíč uživatele Voip.
je heslo uživatele k jeho účtu u poskytovatele služeb VoIP.
