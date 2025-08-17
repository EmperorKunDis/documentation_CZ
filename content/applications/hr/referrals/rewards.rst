=======
Odměny
=======

Po úspěšném získání odměných bodů mohou zaměstnanci vyměnit své body za
nákup odměn v aplikaci **Referrals** v Odoo. Odměny **musí být**:
konfigurovat „vytvořit odkaz“ předtím, než zaměstnanci mohou body uplatnit na odměny.
<odkazy/využít>.

..._referraly/vytvorit:

Vytvořte odměny
==============

Odměny jsou jedinými konfiguracemi, které je třeba nastavit při instalaci aplikace **Referrals**.

Vytvářet nebo upravovat nabídky mohou pouze uživatelé s právy „Administrátor“ aplikace **Nabídka práce**.
změnit odměny.

.. viz též:
:doc:`../obecne/uzivatele/prava_pristupu`

Chcete-li přidat odměny, přejděte na: „Referral app → Konfigurace → Odměny“. Klikněte
„Nový“ a načtěte si formulář, kde zadáte následující informace:

- Název produktu: zadejte název, jak by měl vypadat pro odměnu. Tento údaj je
je nutné.
- :guilabel:`Náklady“: zadejte počet bodů, které je třeba nasbírat k využití odměny.
- :guilabel:Společnost: Vyberte společnost pro kterou je nastavená odměna z nabídky. Pokud
a odměna je k dispozici pro více společností, každá společnost **musí** nakonfigurovat odměnu pro své
konkrétní společnosti. Toto pole se objevuje pouze v prostředí více společností; pokud je tento údaj
Pokud se objeví, je nutné ji použít.

...... příklad::
Společnost s třemi různými společnostmi nabízí dárkovou kartu jako odměnu. V databázi
jsou tři samostatné odměny za dárkovou kartu, jedna pro každou ze tří společností.

- :guilabel:`Odpovědná osoba za dárek“: vyberte z roletky osobu odpovědnou za
získání a doručení odměny příjemci. Tato osoba je upozorněna, když je odměna
Kupované v aplikaci **Referrals**, takže vědí, kdy odměnu doručit příjemci.
- :guilabel:Foto: přidejte fotografii odměny, která se zobrazí na stránce s odměnami.
obrázek v pravém horním rohu (čtverec s fotoaparátem a plusem uvnitř).
:ikonka: „fa-pencil“ :guilabel:„(pencil)“ ikona se objeví. Klikněte na :ikonku: „fa-pencil“
:guilabel:`(tužka)` ikonu pro výběr a přidání fotografie do formuláře odměny. Jakmile je fotografie vybrána,
Při přejetí nad obrázkem se zobrazí dvě ikony namísto jedné: :icon:`fa-pencil` :guilabel:`(pencil)`
ikonu a ikonku „odpadkový koš“ (trash can). Klikněte na ikonku „odpadkový koš“
:guilabel:`(koš)` ikonu pro odstranění aktuálně vybraného obrázku.
- :guilabel:`Popis odměny“: zadejte popis odměny, který je viditelný na odměně
kartu pod nadpisem. Toto pole je povinné.

.. obrázek: odměny/odměny.png
:alt:Vyplněná a podepsaná smlouva o odměně se všemi podrobnostmi.

.. důležité::
Je doporučeno zadat „Náklady“ a přidat „Fotku“. Pokud není uvedená cena,
výchozí cena je uvedena jako nula, což by znamenalo, že odměna bude zdarma v obchodě s odměnami.
Pokud fotografie nebyla vybrána, na stránce s odměnami se zobrazí ikonka náhradního obrázku.

.._přesměrování / využití:

Vyměňte odměny
==============

Chcete-li uplatnit odměnu, musíte si vydělat body. Tyto body pak můžete použít k nákupu
odměna.

Pro nákup odměny klikněte na tlačítko „Odměny“ v hlavním menu „Přátelé“.
dashboard. Všechny nastavené odměny jsou uvedeny v samostatných kartách s odměnami.

Požadovaný počet bodů potřebný k nákupu odměny je uveden v pravém horním rohu karty.

Pokud uživatel má dostatek bodů na nákup odměny, zobrazí se ikona „nákupní košík“ s tlačítkem „Koupit“.
Tlačítko se objeví na dně karty odměn. Pokud nemají dost bodů pro odměnu,
karta s odměnami zobrazuje: „Potřebujete dalších (x) bodů k nákupu“, místo
:icon:`fa-shopping-basket` tlačítko „Koupit“.

Klikněte na tlačítko „Koupit“ vedle odměny, kterou chcete zakoupit.
V okně „Potvrzení“ se objeví dotaz, zda uživatel skutečně chce produkt zakoupit.
odměnu. Kliknutím na tlačítko „OK“ zakoupíte předmět nebo kliknutím na „Zrušit“ zavřete okno.
zrušit nákup.

Po kliknutí na tlačítko „OK“ se okno zavře a body použité k nákupu
body jsou odečteny od dostupných bodů uživatele. Nyní byly aktualizovány odměny
odrážet aktuální dostupné body.

.. obrázek: odměny/využít-odměnu.png
:alt:Tlačítko Koupit se objevuje pod hrníčkem a batohem jako odměnou, zatímco kolo uvádí, jak
je potřeba mnohem více bodů, aby se mohl využít.
