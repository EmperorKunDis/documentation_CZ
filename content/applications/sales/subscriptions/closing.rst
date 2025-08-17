===================
Připojení k odběru
===================

Odoo Subscription poskytuje podnikům flexibilitu při rozhodování, zda zákazníci mohou sami spravovat své předplatné.
jejich předplatné nebo omezit tuto schopnost úplně.

Konfigurace
=============

Začněte tím, že se přesunete na: „Aplikace pro předplatné“ → „Konfigurace“ → „Opakující se plány“.
Zde buď vytvořte nový plán kliknutím na tlačítko „Nový“ nebo vyberte existující plán pro úpravy.
it.

Jakmile se dostanete na formulář „Opakující se plány“, zapněte možnost „Zavřené“ v
:guilabel:'Samoobslužný' sekce, aby zákazníci mohli zavřít své vlastní předplatné pomocí
Klientský portál.

.. obrázek: uzavření/opakované plány - možnost zavřít.png
:align:center
:alt:Volba Zrušit na formuláři opakovaného plánu v Odoo Subscription.


Zrušit předplatné
====================

Pohled správce
------------------

Po potvrzení cenové nabídky na předplatné se objednávka stává prodejním příkazem.
Stav předplatného se změní na:guilabel:`Ve výrobě“.

V tomto bodě se zobrazí možnost ukončení předplatného pomocí tlačítka „Uzavřít“.
tlačítko v horní části objednávky předplatného poblíž řádku obsahujícího :guilabel:`Ve výrobě`.
dalších fázích. Tato možnost je dostupná i po vystavení daňového dokladu a zaplacení objednávky.
byly zaregistrovány.

.. obrázek: uzavření/zrušení předplatného správcem.png
:align:center
:alt: Zrušit předplatné z administrativního hlediska pomocí Odoo Subscription.

Kliknutím na tlačítko „Zavřít“ se zobrazí okno s názvem „Důvod ukončení“.
umožňuje správcům zadat důvod pro uzavření předplatného nebo vybrat ze
rozbalovací nabídka možností v poli „Důvod“.

.. obrázek: uzavření/důvod ukončení pop-up okno.png
:align:center
:alt:Pop-up okno s důvodem zrušení při kliknutí na tlačítko Zavřít v Odoo Subscriptions.

Když je zadána požadovaná hodnota „Důvod“, klikněte na tlačítko „Odeslat“.

Kliknutím na tlačítko „Odeslat“ v okně „Důvod zrušení“ se aktualizuje předplatné.
objednávka na prodej by měla zobrazit stavový štítek „Zrušeno“, spolu s uvedeným štítkem „Uzavřeno“.
Důvod.“

.. obrázek: uzavření/zrušená objednávka.png
:align:center
:alt:Zrušená objednávka pro uzavřenou smlouvu v Odoo Subscriptions.

Ten samý důvod lze nalézt i v poznámce k prodejnímu příkazu.

.. obrázek: uzavření/prodejní objednávka chatter.png
:align:center
:alt:Hovor o zadané objednávce pro uzavřenou smlouvu v Odoo Subscription.

Zákaznický pohled
-------------

.. poznámka::
Jako administrátor máte možnost vidět, co vidí zákazníci při správě svých
předplatné je přístupné prostřednictvím tlačítka „Náhled“ umístěného v horní části stránky.
objednávka na prodej předplatného.

Z pohledu zákazníka v zákaznickém portálu tlačítko „Ukončit předplatné“
je umístěn v levém sloupci objednávky.

.. obrázek: uzavření/zrušení předplatného z pohledu zákazníka.png
:align:center
:alt:Tlačítko pro ukončení předplatného na zákaznickém pohledu objednávky v Odoo Subscription.

Když zákazník klikne na tlačítko „Zrušit předplatné“, zobrazí se mu okno s názvem „Zrušit předplatné“.
Zobrazí se okno s výběrem důvodu, proč zákazník nemá zájem o službu.
Vybírají si uzavření předplatného.

.. obrázek: uzavření/ukončení předplatného zákazníka pov.png
:align:center
:alt:Okno s upozorněním, které se objeví při zavření předplatného.

.. poznámka::
Zákazníci mohou zvolit pouze přednastavený důvod, proč je předplatné ukončeno.
*nevkládat vlastní důvod z portálu zákazníků. Tyto volby lze upravit prostřednictvím
navigace na: „Zasílání -> Konfigurace -> Důvody k uzavření“.

Jakmile si zákazník vybere důvod pro zavření účtu, kliknou na tlačítko „Odeslat“
Pop-up okno.

Při zavření je objednávka předplatného v zákaznickém portálu označena štítkem :guilabel:`Zavřeno`.

Dále se zadaný důvod ukončení objevuje v objednávce předplatného.
Aplikace „Předplatné“ v administračním rozhraní.

.. viz též:
   - :doc:`../předplatné`
