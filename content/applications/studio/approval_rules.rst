==============
Pravidla schválení
==============

Pravidla schválení se používají k automatizaci procesů schvalování akcí. Umožňují definovat
kritéria, podle kterých je potřeba získat schválení předtím, než lze akci provést pomocí tlačítka.

Konfigurace
=============

Pokud chcete přidat schválení pravidel pomocí Studio, postupujte takto:

#:ref:`Otevřené studio <studio/access>` a přepněte na požadovaný :doc:`pohled <views>“.
#Vyberte tlačítko, na které se pravidlo má aplikovat.
#Klikněte na ikonu „+“ a zvolte možnost „Přidat kroky schválení“.
:guilabel:`Vlastnosti“ záložka.
#Uveďte, kdo je zodpovědný za schválení akce pomocí jednoho z následujících polí.
nebo obojí:

    - :guilabel:`Schvalovací uživatelé“ a zadat jednoho nebo více uživatelů.
    - :guilabel:`Skupina schvalovatelů“ pro určení jedné uživatelské skupiny.

.. poznámka::
Pro všechny uživatele nastavené jako :guilabel:`Approver“ se vytvoří aktivita, pokud jejich schválení
požadovány.

#* (volitelné)* Vyberte uživatele, kteří mají být upozorněni na akci prostřednictvím interní poznámky.
je buď schválen nebo zamítnut.
#(*volitelné*) Přidejte :guilabel:`Popis`, který se zobrazí na tlačítku.

..tip:
Můžete si vybrat, za jakých podmínek se má krok schválení použít, kliknutím na
:ikonka:`fa-filter` (ikona vedle pole :ikony:`Approvers`).

Chcete-li přidat další krok schválení, klikněte na ikonu „+“ a poté na „Přidat krok schválení“.
Každý krok může být:

- Povolte možnost „Exkluzivní schválení“ na jakémkoli kroku, aby uživatel, který schválil krok, nemohl
schválit další krok pro stejný záznam.
- Změňte „Příkaz k schválení“ kroků vybráním čísla, 1 je první.
krok, „2“ druhý krok atd. Uživatel odpovědný za vyšší krok může schválit/odmítnout
předchozí kroky, pokud není vybrána možnost „Exkluzivní schválení“.

Klikněte na ikonu „koš“ („trash“) vedle pole „Schvalovatelé“.
odstranit schválení.

..tip:
Můžete vytvořit speciální skupiny uživatelů pro schválení: vizte :ref:`skupiny uživatelů <přístupová práva/skupiny>`.

... schválení pravidel použití:

Užívání
===

Jakmile je definována schvalovací pravidla pro tlačítko, uvede se vedle něj ikona
popisek tlačítka pro každý krok schválení. Kliknutím na ikonu se zobrazí příslušný krok (počet kroků závisí na typu schvalovacího procesu).

.. obrázek:: schválení/tlačítko schválení.png
:alt:Tlačítko pro potvrzení s dvěma kroky

.. poznámka::
Pokud klikne na tlačítko neoprávněný uživatel, zobrazí se chybová hláška a aktivita se zastaví.
vytvořen pro uživatele specifikované v poli :guilabel:`Approvers`, pokud je nějaké.

Autorizovaní uživatelé mohou:

- Akci vykonajte přímo kliknutím na tlačítko, pokud je to poslední nebo jediný schvalovací krok.
- Schválit akci a nechat ji provést jiným uživatelem – nebo přesunout na další krok schválení – pomocí
kliknutím na ikonu uživatelského avatara vedle tlačítka a poté kliknout na :icon:`fa-check`.
(:guilabel:'schválit').
- Akci zamítněte kliknutím na ikonu uživatelského avatara vedle tlačítka a poté
:icon:`fa-times` tlačítko (zrušit).
- (pouze pro uživatele vybrané pod položkou :guilabel:`Approvers`) Přesunout jejich práva schválení
jeden nebo více uživatelů pro všechny záznamy vytvořené:

  - Kliknutím na ikonu „OI View Kanban“ (ikona „Výhled kanban“) a poté
:guilabel:`Delegát“.
  - Vybrat jednoho nebo více:guilabel:`Approverů`, :guilabel:`Do kdy` budou mít schválení
právo (na věčnost pokud je prázdné) a volitelně uživatelé, kteří mají být upozorněni pomocí
vnitřní poznámku pomocí pole :guilabel:`Notify to`.

.. obrázek:: schvalovací pravidla/delegátní dialog.png
:alt:Delegát do dialogu

..tip:
   - Uživatel, který schválil nebo zamítl akci, může své rozhodnutí zrušit kliknutím na **avatar uživatele**.
ikona vedle tlačítka s popisem a poté tlačítko s ikonou `fa-undo` (popisek `revoke`).
Může také zrušit rozhodnutí ostatních uživatelů pro kroky s nižší hodnotou „Priorita schválení“.
pokud není povolena výhradní schválení.
   - Schválení je sledováno v chatovací části záznamu. Každé schválení také vytvoří nový záznam
když se provede akce související s přístupem do schválení. Chcete-li zobrazit záznamy o schválení,
vývojářský režim </applications/generální/developer_mode> a přejděte na: „Nastavení“ -->
Technické --> Schválení vstupů do studia.
