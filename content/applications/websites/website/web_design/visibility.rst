==========
Viditelnost
==========

Můžete si vybrat, zda budou bloky budov zobrazeny nebo skryty podle návštěvníkova:

- druh zařízení (mobil nebo počítač).
- země (geolokace na základě IP adresy)
- jazyk webu
- :parametry UTM v odkazu na sledování (viz. report/link_tracker).
- Stav přihlášení.

... webu/viditelnosti/mobilních a počítačových zařízeních:

Mobilní/počítačová
===============

.. role:: neupravený HTML (neupravený)
:formát:html

.. |desktop icon| replace:: :raw-html:`<svg viewBox="0 0 465 462" xmlns="http://www.w3.org/2000/svg" width="18" height="18"><path d="M456.969 9.84743L454.026 6.90425C444.956 -2.16512 429.098 -1.01124 418.605 9.48152L10.8984 417.188C0.405681 427.681 -0.748186 443.539 8.32118 452.609L454.392 45.2678C464.884 34.775 466.038 18.9168 456.969 9.84743Z"></path><path d="M346.673 26.269H39.1908C17.8303 26.269 0.5 43.6036 0.5 64.9695V322.973C0.5 336.409 7.35309 348.251 17.752 355.19L114.47 258.472H62.9696C56.9597 258.472 52.0878 253.601 52.0878 247.591V141.602L464.79 90.0139V322.973C464.79 344.339 447.46 361.674 426.099 361.674H271.336L284.233 400.375H342.269C352.949 400.375 361.614 409.042 361.614 419.725C361.614 430.408 352.949 439.075 342.269 439.075H123.021C120.837 439.075 118.734 438.708 116.771 438.033L154.429 400.375H181.057L193.954 361.674H193.13L226.244 328.56C228.268 329.181 230.417 329.516 232.645 329.516C244.665 329.516 254.409 319.772 254.409 307.753L296.331 258.472Z"></path></svg>`

.. |mobile icon| replace:: :raw-html:`<svg viewBox="0 0 566.93 566.93" xmlns="http://www.w3.org/2000/svg" width="18" height="18"><rect transform="translate(283.46 -117.41) rotate(45)" x="255.56" y="-16.93" width="55.81" height="600.8" rx="25.61"></rect><path d="m395.46 399.46a12 12 0 0 1-12 12h-128.4l-115.68 115.69a47.8 47.8 0 0 0 32.08 12.31h224a48 48 0 0 0 48-48v-268.4l-48 48zm-112 108a32 32 0 1 1 32-32 32 32 0 0 1-32 32z"></path><path d="m171.46 87.46a12 12 0 0 1 12-12h200a11.89 11.89 0 0 1 6.48 1.93l37.61-37.61a47.82 47.82 0 0 0-32.09-12.32h-224a48 48 0 0 0-48 48v268.41l48-48z"></path></svg>`

Pro přepínání viditelnosti bloku na základě typu zařízení návštěvníka:

- Otevřete editor webové stránky a vyberte blok.
- V záložce „Nastavení“ pod možnostmi přizpůsobení bloku hledejte
:label:`Dostupnost`.

  - Klikněte na tlačítko |desktop ikona| (:guilabel:`Zobrazit/skrýt na ploše`) pro skrytí
blok pro uživatele, kteří navštěvují vaše webové stránky z počítače.
  - Klikněte na tlačítko „Zobrazit / skrýt v mobilním zařízení“ (:guilabel:`Mobile Icon`):
pro uživatele, kteří navštěvují vaše webové stránky z mobilního zařízení.

- Klikněte na tlačítko „Uložit“ pro aplikaci změn.

Je také možné skrýt prvky uvnitř bloků, což se často používá k skrytí specifických
elementy uvnitř bloků, které mohou být příliš široké na správné zobrazení v mobilních zařízeních.
volba je k dispozici, vyberte prvek v bloku a hledejte „Zobrazit“.
volba v nastavení prvku.

Příklad:
Vybraný obrázek se na mobilních zařízeních skrývá.

.. obrázek:: visibility/element-visibility.png
:alt: Příklad skrytého prvku sloupce na mobilních zařízeních

.. webové stránky / viditelnost / podmínky:

Podmínky
==========

Pro přístup k zemi, jazyku webu, parametry UTM a stav přihlášení:

- Otevřete editor webu a vyberte blok.
- V záložce „Přizpůsobit“ hledejte „Zobrazit“.
- Klikněte na „Žádné podmínky“ a vyberte místo toho „Podmíněně“.
různé možnosti:

  - :guilabel:`Země“: země, ze které pochází návštěvníkův IP adresa.
  - :guilabel:`Jazyky“: používaný jazyk webu návštěvníkem.

.. poznámka::
Tato možnost je k dispozici pouze v případě, že je nainstalováno více než jedno jazykové prostředí.
<../konfigurace/přeložit>.

  - :label:kampaň UTM: vybraná kampaň.
  - :guilabel:`UTM Medium“: vybraný kanál pro jakoukoliv kampaň.
  - :guilabel:`Zdroj UTM“: vybraný zdroj jakékoli kampaně.
  - :guilabel:`Uživatelé“: vyberte, zda se návštěvník má přihlásit nebo
:guilabel:`Vylogován“ k zobrazení bloku. Výchozím nastavením je možnost „Zobrazit
pro všechny“.

- Vyberte jednu nebo více z prvních pěti možností a poté vyberte, jestli blok bude viditelný pro
nebo:guilabel:`Skryté pro“, pak klikněte na „Vybrat záznam…“ a vyberte jej.

..tip:
   - Pro každou možnost můžete vybrat více záznamů klepnutím na tlačítko „Vyberte záznam…“
znovu.
   - Klikněte na tlačítko „Odebrat“ (ikona „fa-minus“).

Klikněte na tlačítko „Uložit“ pro aplikaci změn.

Příklad:
Blok s následující konfigurací se zobrazí pouze uživatelům s belgickou IP adresou
adresa, na kterou je webová stránka zobrazená v francouzštině, pokud nebudou navštěvovat stránku pomocí
Kampaň „Prodej“ sledovala URL.

.. obrázek: viditelnost/viditelnost-podmínky.png
:alt: Příklad bloku s více viditelnostními podmínkami

..._web/viditelnost/neviditelné prvky:

Neviditelné prvky
==================

Bloky a prvky s vlastními nastavení viditelnosti jsou uvedeny na konci webového editoru.
příslušné liště. Chcete-li si prohlédnout, jak stránka vypadá, klikněte na ikonku :icon:`fa-eye`.
:guilabel:`viditelný“ tlačítko pro skrytí bloku nebo prvku, nebo ikonu „fa-eye-slash“
(:guilabel:'skrytý') pro zobrazení v editoru webu.

.. obrázek: viditelné/neviditelné prvky.png
:alt: Bloky a prvky s vlastními nastaveními viditelnosti zobrazené na dně editoru
