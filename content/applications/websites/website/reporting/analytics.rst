=================
Analýza webu
=================

Analýza webových stránek pomáhá majitelům webových stránek sledovat, jak lidé používají jejich webové stránky. Poskytuje údaje o
demografii návštěvníků, jejich chování a interakce, což pomáhá zlepšovat webové stránky a marketingové strategie.

Můžete sledovat návštěvnost svého webu na Odoo pomocí analytiky :ref:`analytics/plausible`.
:ref:`analytics/google-analytics`. Doporučujeme používat plausible.io, protože je to bezpečné řešení.
lehký a snadno použitelný.

Dashboard společnosti Plausible Analytics je také integrován do systému Odoo a lze jej přistupovat
přes menu „Webová stránka“ -> „Zprávy“ -> „Analýza“.

.. _analytics/plausible:

Plausible.io
============

Odoo provozuje vlastní server plausible.io a poskytuje zdarma připravený plausible.io
řešení pro databáze **Odoo Online**, které používají doménu odoo.com. Odoo automaticky vytváří a
založí váš účet. Začněte s ním pracovat přes:
Analýza“.

.. poznámka::
   - Pokud používáte vlastní doménu, například „example.com“ (viz dokumentaci o doménách),
musíte si vytvořit svůj vlastní účet a předplatné na Plausible.io.
   - Pokud již máte účet na Plausible.io, můžete jej propojit s Odoo Online.
databáze musíte vytvořit dvě proměnné ir.config.parameters, které budou používat servery služby Plausible.io.
zapnout režim vývojáře a přejít do sekce „Obecné nastavení“
Technické --> Systémové parametry. Klikněte na „Nový“ a vyplňte následující
:guilabel:`Klíč“ a :guilabel:`Hodnota“ pole:

...... seznamová tabulka::
:hlavičky: 1

        * – Klíč
          - Hodnota
        * - „webová stránka.Plausible skript“
          - „https://plausible.io/js/plausible.js“
        * – „webová stránka.Plausible Server“
          - „https://plausible.io“

Pak postupujte podle níže uvedených kroků a připojte svůj stávající účet na serverech Plausible.io.

.... upozornění::
Deaktivace bezplatného účtu Plausible.io propojeného s vaší databází **Odoo Online**
Také zruší všechny stávající klíče, čímž je způsobí nefunkčnost. Výsledkem bude tedy nutnost vytvoření nových
budou vytvořeny nové klíče a všechna historická data spojená s původními klíči se ztratí. Pokud
Pokud plánujete účet deaktivovat, doporučuje se předem zálohovat svá data na místním disku.

Pokud je vaše databáze hostována na Odoo.sh nebo On-premise, nebo pokud chcete používat vlastní
Účet u Plausible.io postupujte takto:

#Vytvořte nebo se přihlaste do účtu Plausible.io pomocí následujícího odkazu: <https://plausible.io/register>.
#Pokud vytváříte nový účet, postupujte podle kroků registrace a aktivace.
Na stránce „Přidat informace o webu“ přidejte doménu svého webu bez
včetně „www“ (např. „example.odoo.com“) a změňte časové pásmo v poli „Časový posun“.
Pokud je třeba, klikněte na tlačítko „Instalace Plausible“. Poté pokračujte přes další krok.
:guilabel:`Návod na ruční instalaci“ a klikněte na :guilabel:`Začněte sbírat data“.
#Jakmile je vše hotovo, klikněte na loga služby Plausible.io v pravém horním rohu stránky a přejděte do seznamu
webové stránky <https://plausible.io/sites> a pak klikněte na ikonu :icon:`fa-ellipsis-v`.
vedle webové stránky a vyberte ikony „Nastavení“
z nabídky.

.... obrázek: analytics/plausible-gear-icon-settings.png
:alt: Klikněte na ikonu ozubeného kola v seznamu webů.

#V bočním panelu vyberte možnost „Zobrazitelnost“, pak klikněte na „Přidat sdílený odkaz“.
#Zadejte do pole „Jméno“:guilabel:„Název“, nechte prázdné pole „Heslo (volitelně)“, protože služba
Analytické panel v Odoo nepodporuje tento typ integrace, pak klikněte na:guilabel:`Vytvořit
sdílený odkaz.

#Zkopírujte sdílený odkaz.

.. obrázek:: analytics/plausible-copy-shared-link.png
:alt:Kopírujte sdílenou odkazovou adresu z Plausible.io

#V Odoo přejděte na: „Webové stránky -> Konfigurace -> Nastavení“.
#V sekci „SEO“ zapněte „Plausible Analytics“, pak vložte
:guilabel:`Sdílený odkaz“ a klikněte na „Uložit“.

..tip:
Pokud máte více webových stránek, přidejte své weby do seznamu
Plausibilní účet přesunutím na adresu <https://plausible.io/sites> a kliknutím na tlačítko :guilabel:`+ Add
Webové stránky. V Odoo v nastavení webových stránek se ujistěte, že je vybrána ta správná webová stránka.
:guilabel:`Nastavení webu“ pole v horní části stránky před vložením
:guilabel:`Sdílený odkaz“.

.. poznámka::
Odoo automaticky přidává dvě vlastní cíle: „Získání nových zákazníků“ a „Obchod“.

.. viz též:
„Dokumentace Plausible Analytics <https://plausible.io/docs>“

.. _analytics/google-analytics:

Google Analytics
================

Sledovat návštěvnost svého webu Odoo pomocí Google Analytics:

#Vytvořte nebo se přihlaste do účtu Google pomocí následujícího odkazu: <https://analytics.google.com>.
#- Pokud nastavujete Google Analytics poprvé, klikněte na tlačítko „Začít měřit“.
a postupujte podle kroku vytváření účtu.
   - Pokud již máte účet v Google Analytics, přihlaste se a klikněte na ikonu „fa-cog“
v levém dolním rohu stránky a přejděte na stránku **Administrace**. Pak klikněte
:guilabel:`+ Vytvořit“ a vyberte „Vlastnost“ z rozevírací nabídky.

#Dokončete další kroky: „Vytvoření vlastnosti <https://support.google.com/analytics/answer/9304153?hl=en/&visit_id=638278591144564289-3612494643&rd=2#property>“
podnikatelské údaje a obchodní cíle.
#Když dosáhnete kroku „Sběr dat“, vyberte platformu Web.

.... obrázek: analytics/GA-platform.png
:alt:Vyberte platformu pro vlastní Google Analytics.

#Založte svůj datový proud: Zadejte svou „URL webu“ a „Název proudu“, pak
klikněte na tlačítko „Vytvořit a pokračovat“.
#Zkopírujte měřicí identifikaci:guilabel:`Measurement ID`.

.... obrázek: analytics/GA-measurement-id.png
:alt: ID měření v Google Analytics.

#V Odoo přejděte na: „Webové stránky -> Konfigurace -> Nastavení“.
#V sekci SEO zapněte Google Analytics a pak do textového pole vložte
:guilabel:`ID měření“ a klikněte na „Uložit“.

..tip:
Pokud máte více webových stránek s různými doménami, pak je vhodné mít pro každou z nich samostatný soubor configuration.
Je doporučeno vytvořit jednu vlastnost <https://support.google.com/analytics/answer/9304153?hl=en/&visit_id=638278591144564289-3612494643&rd=2#property>.
na doménu. V Odoo v nastavení webu se ujistěte, že je vybrána správná doména.
:guilabel:`Nastavení webu“ pole v horní části stránky před vložením
:guilabel:`ID měření“.

.. viz též:
„Dokumentace Google k nastavení Analytics pro webové stránky


.._analytics/google-tag-manager:

Google Tag Manager
==================

Google Tag Manager je systém pro správu značek, který vám umožní snadno aktualizovat
měřicí kódy a související fragmenty kódu, které jsou známé jako tagy na vašem webu nebo mobilním zařízení.
aplikace přímo přes kódový injektor.

.. poznámka::
:abbr:`GTM (Google Tag Manager)` není analytickým nástrojem a neposkytuje funkce reportingu;
je používána k sběru dat a pracuje s nástrojem Google Analytics, aby poskytla podrobnější informace.
poznatků. Pro správné používání GTM je doporučeno také nastavit Google Analytics.

Pro více informací se podívejte na dokumentaci o propojení služby Google Analytics a
Google Tag Manager <https://support.google.com/tagmanager/answer/9442095?hl=cs>.

.. varování:
   - Některé GTM tagy používají data (např. pokročilá sledování nákupů) k získání
proměnné a odeslat je do služby Google Analytics. V současnosti se datové vrstvy v Odoo nezpracovávají.
   - Google Tag Manager nemusí být v souladu s místními předpisy o ochraně osobních údajů.

Pro konfiguraci GTM postupujte takto:

#Vytvořte nebo se přihlaste ke svému účtu Google, kliknutím na odkaz https://tagmanager.google.com/.

#V záložce „Účty“ klikněte na „Vytvořit účet“.

#Zadejte „Název účtu“ a vyberte zemi, ke které se váš účet vztahuje.

#Zadejte adresu svého webu do pole „Název kontejneru“ a vyberte cílový server.
platforma.

#Klikněte na tlačítko „Vytvořit“ a souhlaste s podmínkami služby.

#Zkopírujte kód hlavičky a těla z okna s upozorněním. Pak přejděte na svůj web, klikněte
:guilabel:`Upravit“, přejděte na záložku „Téma“ a posuňte se dolů k
V sekci „Pokročilé“ klikněte na položku „Hlavička“ a „Tělo“.
:guilabel:`Vložení kódu“ pro vkládání kódů.

.. obrázek:: analytics/gtm-codes.png
:alt:Instalace Google Tag Manager

.. poznámka::
Data jsou shromažďována v nástrojích používaných pro sledování webu (např. Google Analytics,
Plausibilní (Facebook pixel), ne v Odoo.

.. viz též:
„Nastavení spouštěčů pro kliknutí na Googlu
<https://support.google.com/tagmanager/answer/7679320?hl=cs&ref_topic=7679108&sjid=17684856364781654579-EU>
