===================================
Nepohyblivé aktiva a dlouhodobý majetek
===================================

**Nepohyblivé aktiva**, také známá jako **dlouhodobá aktiva**, jsou investice, které se očekává, že budou
realizovány během jednoho roku. Jsou kapitalizovány a neúčtují se, ale objevují se na účtech společnosti
výkazu zisku a ztráty. Podle své povahy mohou podléhat **odpisům**.

Veškeré nemovité věci jsou součástí nehmotných aktiv.
produktivní složky, jako jsou budovy, dopravní prostředky, zařízení, pozemky a software.

Příklad: Kupujeme auto za 27 tisíc dolarů. Plánujeme ho rozpočítat na pět let a
Poté ho prodá za 7 000 $. Použije metodu lineární nebo rovnoměrné amortizace
Každý rok se utratí 4 000 dolarů za **odpisy**. Po pěti letech je to celkem **nashromážděných
Zaúčtovaná hodnota odepisovaného majetku je 20 000 $, což nám zůstane 7 000 $.
Nepočítá se do odpisů, nebo Hodnota po likvidaci.

Odoo Accounting automaticky vytváří všechny účetní záznamy o odpisu v režimu „návrh“
módu. Pak jsou zveřejňovány v intervalech.

Odoo podporuje následující metody **odpisu**:

- Přímá linka
- Klesající
- Klesající rovnice s přímkou

.. poznámka::
Server kontroluje jednou denně, zda je potřeba nějaký příspěvek publikovat. Může se tedy stát, že bude trvat až 24 hodin, než
zobrazí se změna z „návrhu“ na „publikované“.

Předpoklady
=============

Takové transakce musí být zveřejněny na účtu „Aktiv“ místo výchozího
Pokladna.

Nastavte účet aktiv
---------------------------

Konfiguraci účtu v **Nástrojích pro rozpočet a fakturace** proveďte takto:
Konfigurace --> Nastavení účetnictví, klikněte na tlačítko *Vytvořit* a vyplňte formulář.

.. obrázek: assets/assets01.png
:align:center
:alt: Konfigurace účtu majetku v Odoo Accounting

.. poznámka::
Tento účet musí být buďto typu *Pevné investice* nebo *Nepohyblivé investice*.

Přidejte výdaj na správný účet
------------------------------------

Vyberte účet na návrh zákona
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V návrhu zákona vyberte správný účet pro všechny aktiva, která kupujete.

.. obrázek: /assets/assets02.png
:align:center
:alt:Výběr účtu aktiv na návrhu faktury v Odoo účetnictví

.._produktové aktiva účtu:

Vyberte jiný účet pro výdaje pro konkrétní produkty
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Začněte upravovat produkt, přejděte na záložku Účetnictví, vyberte správný účet pro výdaje a
Ušetřit.

.. obrázek: assets/assets03.png
:align:center
:alt:Změna účtu aktiv pro produkt v Odoo

.. tip::
Je možné automatizovat vytváření záznamů aktiv :ref:`<automatizace vytváření záznamů aktiv>`.
produkty.

..._aktiva-účtu-novin:

Změnit účet za zveřejněný příspěvek
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pro toto otevřete Knihu nákupů přechodem na: „Účetnictví“ - „Účetnictví“.
Nákupy“, vyberte položku účetního záznamu, který chcete upravit, klikněte na účet a zvolte správný
jedna.

.. obrázek: assets/assets04.png
:align:center
:alt:Úprava položky účetní knihy v Odoo

Vstupy aktiv
==============

... vytvořit položku s aktivy

Vytvořte nový záznam
------------------

Při vstupu aktiv se automaticky generují všechny účetní záznamy ve stavu návrhu. Ty jsou pak zveřejněny
Jeden po druhém v pravý čas.

Pro vytvoření nové položky přejděte na: „Účetnictví“ - „Účetnictví“ - „Majetek“, klikněte na
Vytvořte a vyplňte formulář.

Klikněte na položku „vybrat související nákupy“ a spojte existující záznam s novým vstupem.
Pole jsou pak automaticky vyplněna a záznam je nyní uveden pod položkou **Související.
Koupit**

.. obrázek: assets/assets05.png
:align:center
:alt:Vstup aktiv v účetnictví Odoo

Jakmile je vše hotovo, klikněte na tlačítko „Vypočítat odpis“ (vedle tlačítka „Potvrdit“) a vygenerujete všechny
hodnoty **Odepsaní**. Tato tabulka zobrazuje všechny položky, které Odoo vytvoří.
jakým způsobem ocení váš majetek a kdy.

.. obrázek: assets/assets06.png
:align:center
:alt:Odhadová komise v účetnictví Odoo

Co znamená „Prorata Temporis“?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Funkce Prorata Temporis je užitečná pro odpisování vašich aktiv co nejprecizněji.

S touto funkcí se vypočítává první záznam v Účetnictví odpisů podle zbývajícího času.
mezi datem Prorata a prvním dnem oslabení namísto výchozí doby
mezi oslabováním.

Příkladem je například Depreciační rada s první devalvací v hodnotě 241,10 $.
a ne 4 000 USD. Proto je poslední záznam také nižší a má hodnotu 3758,90 USD.

Jaké jsou různé metody odepisování
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Metoda **liniové depreciace** rozděluje počáteční hodnotu odpisů na počet
plánované odpisy. Všechny položky s odpisem mají stejnou hodnotu.

Metoda postupného odepisování vynásobí hodnotu odpisovatelného majetku faktorem postupného odepisování.
za každý záznam. Každá položka odepisování má nižší částku než předchozí položka. Poslední
Účet odpisů nepoužívá klesající koeficient, ale částku odpovídající
zůstatek ocenitelné hodnoty tak, aby dosáhl nuly na konci stanoveného období.

Metoda **Odpočtu v klesající linii** používá metodu Odpočtu, ale s
minimální odepisování rovnoměrně, což zajišťuje rychlé odepisování.
Začíná se na nízké úrovni, později je konstantní.

Pohledávky z Knihy nákupů
---------------------------------

Můžete vytvořit záznam o aktivu z konkrétního položky v knize nákupních dokladů.

Pro toto otevřete Knihu nákupů přechodem na: „Účetnictví“ - „Účetnictví“.
Nákupy“ a vyberte položku z knihy, kterou chcete uvést jako aktivum. Ujistěte se, že je vedená
v správném účtu (viz:ref:`účet s aktivy`)

Poté klikněte na položku *Akce* a zvolte možnost *Vytvořit aktivum*. Vyplňte formulář stejně jako v případě
:ref:`vytvořit nový záznam <create-assets-entry>“.

.. obrázek: assets/assets07.png
:align:center
:alt:Vytvořit záznam o aktivu z položky v účetnictví Odoo

Modifikace aktiv
========================

Můžete měnit hodnotu aktiv, aby se zvýšila nebo snížila jejich hodnota.

Pro provedení změny otevřete aktivum, které chcete upravit, a klikněte na položku „Upravit odpisy“. Poté vyplňte
formulář s novými hodnotami odpisu a klikněte na tlačítko *Upravit*

Při poklesu hodnoty se vytvoří nový záznam v deníku pro „Snížení hodnoty“ a všechny
budoucí *nepublikované* záznamy v deníku, které jsou uvedeny na účet odpisu.

Zvýšení hodnoty vyžaduje vyplnění dalších polí, která se týkají pohybů na účtu.
a vytvoří novou položku majetku s hodnotou **Zvýšení hodnoty**. Hodnota majetku může být
přístupný pomocí tlačítka Smart Button.

.. obrázek: /assets/assets08.png
:align:center
:alt: Chytrý tlačítko pro zvýšení v účetnictví Odoo

Odpis fixního majetku
========================

Prodat aktivum nebo se ho zbavit znamená, že musí být vyřazeno z rozvahy.

Pro toto provedení otevřete aktivum, které chcete prodat nebo zlikvidovat, klikněte na „Prodat nebo zlikvidovat“ a vyplňte formulář.

.. obrázek: assets/assets09.png
:align:center
:alt: Řízení aktiv v účetnictví Odoo

Odoo Accounting pak vytvoří všechny potřebné účetní záznamy k likvidaci majetku, včetně
zisk nebo ztráta při prodeji, která je vypočítána na základě rozdílu mezi hodnotou v účetnictví
čas prodeje a za kolik je prodáno.

.. poznámka::
Pro zaznamenání prodeje aktiv musíte nejprve vystavit fakturu zákazníkovi a poté ji spojit s příslušnou položkou.
s ním spojené prodeje aktiv.

.._aktiva/aktivní model:

Modelové aktiva
=============

Můžete vytvořit **Assets Modely**, abyste mohli rychleji vkládat své aktivní položky. Je to zvláště užitečné, pokud
Kupujete stejné typy aktiv.

Pro vytvoření modelu přejděte na: „Účetnictví -> Konfigurace -> Model aktiva“, klikněte na
Vytvořte nový záznam a vyplňte jej stejně, jako byste vytvářeli novou položku.

.. tip::
Můžete také převést potvrzenou položku aktiv do modelu otevřením.
:menu „Účetnictví“ -> „Účetnictví“ -> „Vybavení“ a poté kliknutím na tlačítko „Uložit“.
Modelka.

Použijte model aktiv na nový vstup
-----------------------------------

Při vytváření nového záznamu o aktivu vyplňte položku **Zásoby** správným majetkem.
účet.

Nové tlačítka s odkazy na všechny modely spojené s daným účtem se zobrazí v horní části formuláře. Po kliknutí
Tlačítko s modelem vyplní formulář podle zadaného modelu.

.. obrázek: assets/assets10.png
:align:center
:alt:Tlačítko pro modelování aktiv v účetnictví Odoo

.._aktiva-automatizace:

Automatizujte aktiva
===================

Když vytváříte nebo upravujete účet, jehož typ je buď *Nepřevoditelné aktiva* nebo *Pevná aktiva*,
Vlastními aktivy* můžete nastavit, aby vytvářely aktiva pro výdaje, které jsou na něm přičítány.
automaticky.

Máte tři možnosti pro pole „Automatizace aktiv“:

#**Ne:** tento výchozí stav nevyvolá žádnou akci.
#**Vytvořit v návrhu:** pokaždé, když je transakce připsána na účet, vytvoří se návrh *Příjmu aktiv*
je vytvořen, ale neověřen. Nejprve musíte vyplnit formulář v sekci „Účetnictví“ ->
Účetnictví --> Aktiva.
#**Vytvořte a ověřte:** musíte také vybrat model aktiv (viz: `Model aktiva`).
Při zadání transakce se na účet připíše položka „Aktiva“ a okamžitě ověřená.

.. obrázek:: assets/assets11.png
:align:center
:alt:Automatizace aktiv na účtu v Odoo Accounting

.. tip::
Můžete například vybrat tento účet jako výchozí účet **Náklady na produkt**.
Zcela automatizovat nákup. (viz: :ref:`produktové aktiva účet`)

.. viz též:
  * :doc:`../začínáme/účetní kniha`
