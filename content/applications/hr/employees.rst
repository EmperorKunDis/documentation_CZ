Zobrazit obsah

=========
Zaměstnanci
=========

Odoo **Zaměstnanci** centralizuje :doc:`soubory o zaměstnancích <employees/new_employee>“, pracovní smlouvy
:doc:`smlouvy <plat/smlouvy>“ a „organizační struktury <zamestnanci/organizace>“ v
jednoho systému. Přesné nastavení parametrů zajistí, že na panelu se zobrazují aktuální informace o každém zaměstnanci.
přítomnost a pracovní místo – data, která řídí přesnost výplaty, plánování kapacity a dodržování předpisů
reportér.

.. karty:

......karta: Noví zaměstnanci
:target: zaměstnanci/nový zaměstnanec

Vytvořit nové záznamy zaměstnanců

...... karta: Oddělení
:target: zaměstnanci/oddělení

Vytvářet a spravovat oddělení, do kterých patří zaměstnanci.

......karta:Certifikace
:cíl: zaměstnanci/certifikace

Certifikujte zaměstnance jako odborníky v oboru s certifikacemi.

... karta: Štítky
:target: zaměstnanci/odznaky

Udělovat zaměstnancům odznaky za výkony a dosažené úspěchy.

....... karta: Vybavení
:cíl: zaměstnanci/zařízení

Spravovat a sledovat vybavení zaměstnanců.

...... karta: Odchod
:target: zaměstnanci/odchod

Dbejte na správu záznamů o zaměstnancích po skončení spolupráce.

......karta: Zpráva o udržení zaměstnanců
:target: zaměstnanci/zpráva o udržení

Získat přehled o míře udržení zaměstnanců v dané firmě.

.._zaměstnanci/prostředí:

Nastavení
========

Pro zobrazení a konfiguraci dostupných nastavení přejděte na:
Konfigurace --> Nastavení.

Zaměstnanci
---------

- :guilabel:`Zobrazení přítomnosti“: vyberte, jakým způsobem se počítá dostupnost zaměstnance.

  - :guilabel:`Podle počtu účastníků“: označen dostupný při :ref:`zadání do systému <attendances/check-in>“
aplikace **Přítomnosti**.
  - Založeno na uživatelském stavu v systému“: dostupné, pokud se zaměstnanec přihlásí do
Odoo <přítomnosti/check_in_check_out>.

- :guilabel:'Pokročilá kontrola přítomnosti': pokud je zapnuto, lze zjistit stav přítomnosti podle
spíše operační signály než přihlášení nebo přihlášení:

  - :guilabel:`Na základě počtu odeslaných e-mailů“: zaměstnanec je označen jako přítomný, pokud poslal alespoň
    # počet e-mailů za hodinu; jinak jsou označeni jako nepřítomní. Zadejte minimální počet e-mailů
musí být zaslána do pole :guilabel:`Odeslané e-maily“.
  - „Založeno na IP adrese“: zaměstnanec je označen jako přítomný pouze v případě, že se připojí z jedné
zadané firemní IP adresy. Zadejte IP adresu do pole :guilabel:`IP Adresa`.
pole oddělující jednotlivé adresy čárkou.

- :guilabel:`Správa dovedností“: zapněte tuto možnost, aby se zobrazila karta :ref:`Životopis <employees/resume>“.
na profilu zaměstnance, což umožňuje zobrazit:ref:`pracovní zkušenosti <employees/cv>`.
:ref:`dovednosti <zaměstnanci/dovednosti>“ a „certifikace <zaměstnanci/certifikace>“.
- :guilabel:'Práce na dálku': zapněte tuto možnost, abyste mohli zobrazit podrobný rozvrh.
formulář zaměstnance, v záložce :ref:`Informace o práci <employees/work-info-tab>`.
Specifická lokalita může být pro každý pracovní den nastavena pro zaměstnance. Pro odpovídající ikonu
zobrazené v pravém horním rohu karty zaměstnance, které ukazují jejich umístění ikonou.
status barevně.

...... příklad::
Zelená ikonka „domov“ značí, že zaměstnanec pracuje z domova
Tento den. Ikona „budova“ značí, že zaměstnanec má v plánu
práce v kanceláři.

Barva ikony ukazuje stav zaměstnance, zelená značí přítomnost, žlutá
značí nepřítomnost a šedá barva znamená, že je mimo pracovní dobu zaměstnance.

.. obrázek:: zaměstnanci/přítomnost.png
:alt:Dvě karty kanban zaměstnanců, které zobrazují jejich pracovní pozici a stav.

Organizace práce
-----------------

Vyberte z roletky výchozí hodiny společnosti. Výchozí možnosti
:guilabel:`Standardní pracovní doba 40 hodin týdně“, „Předvolená zdrojová kalendář“
:guilabel:`Standardní úvazek 32 hodin týdně (4 pracovní dny, pátek volno).“

Dostupná pracovní doba je stejná jako konfigurovaná:ref:`směna
„Mzdy/směny“ v aplikaci „Mzdy“. Směny lze vytvářet a upravovat z obou
aplikace **Mzdy a zaměstnanci**.

Práva zaměstnance na aktualizaci
----------------------

Zapněte možnost „Editace zaměstnance“ a umožněte zaměstnancům upravovat svá vlastní data.
evidenci zaměstnanců.

..toctree::


zaměstnanci/nový zaměstnanec
zaměstnanci/přijetí
zaměstnanci/oddělení
zaměstnanci/certifikace
zaměstnanci/známky
zaměstnanci/zařízení
zaměstnanci/odchod
zaměstnanci/zpráva o udržení
