====================
Prodávejte předplatné
====================

Předplatné je opakující se a trvá neomezeně dlouho. Časem si zákazníci mohou přát změnit
Proto je důležité mít možnost upravit ceny nebo změnit kvantitu.
aby vyhovovaly všem potřebám. Právě zde se může objevit příležitost k prodeji předplatného.

Upselling může být prospěšné následujícím typům zákazníků:

#. |*Věrní zákazníci*
|Jedná se o zákazníky, kteří už důvěřují společnosti/značce a protože si již vytvořili
vzorec platby za produkty/služby a je zde více důvěry při pokusu prodat.
jim dražší produkt nebo službu.
#. | *Noví zákazníci*
|Pro nové zákazníky neznalé společnosti/značky je nutné zvolit novou, atraktivní taktiku.
zaměřené na přesvědčení zákazníka k nákupu dražšího produktu nebo služby.

V těchto případech mohou být slevy užitečné. Obvykle končí předplatné po určité době
času.

Takže pokud jsou tyto dražší produkty/služby nabízeny novým zákazníkům se slevou, pak
Někdy může vést k prodeji a vytváří mezi zákazníkem a obchodníkem silný pocit důvěry.
Společnost/značka. V důsledku toho může dojít ke zvýšení míry udržení zákazníků, protože se budou cítit více pohodlně
a důvěryhodný v průběhu času.

Slevová konfigurace
----------------------

Aby měli schopnost nabídnout novému zákazníkovi předplatné s využitím slevy.
Funkce Slevy musí být aktivována.

Pro aktivaci funkce Slevy přejděte do části: „Aplikace pro prodej –> Konfigurace“.
Nastavení“, přejděte do sekce „Cena“ a zaškrtněte políčko vedle
Vyberte „Slevy“ a poté klikněte na „Uložit“.

.. obrázek: upselling/configuration-to-upsell-a-subscription.png
:align:center
:alt:Aktivace slevového kupónu v Odoo Sales.

S tímto nastaveným bude možné poskytnout slevu na řádcích prodejních objednávek.

Prodávejte předplatné
====================

Před přechodem na předplatné zkontrolujte dokumentaci o tom, jak vytvořit cenovou nabídku.
Používáním produktů s předplatným.

Když je potvrzená citace s předplatným, stává se oficiálně objednávkou na prodej a vytvoří nový
Předplatné vytvoříte v aplikaci Odoo *Subscriptions*.

.. poznámka::
Před prodejem produktů s vyšší hodnotou musí být vystaven faktura za předplatné.

Při otevření objednávky na předplatné buď v aplikaci „Prodej“ nebo „Předplatné“,
možnost prodeje předplatného je k dispozici prostřednictvím tlačítka „Upsell“ v horní části stránky.
z objednávky na prodej.

.. obrázek: upselling/upsell-your-subscription.png
:align:center
:alt:Tlačítko pro upselling s objednávkami předplatného v Odoo Subscription.

Když je kliknut na tlačítko „Upsell“, objeví se nová objednávka s
:guilabel:`Upsell“ stavový banner v pravém horním rohu.
už v záložce „Objednávkové řádky“.

Uživateli je také připomenuto, že opakující se produkty jsou slevněné.
Část času v poměru k počátečnímu předplatnému, které je umístěno pod
:guilabel:„Řádky objednávek“ kartě.

.. důležité:
Proražená částka se vztahuje pouze na produkty typu „Služba“ a ne na produkty typu „Zboží“.
Produkty typu „spotřební“ nebo „skladovatelný“, i když se zpráva objeví.

Do nového formuláře pro nabídku upgrade přidejte nové produkty předplatného v poli :guilabel:`Objednávky`
tabu kliknutím na tlačítko „Přidat produkt“ a výběrem požadovaného předplatného.

.. obrázek: upselling/použití tlačítka pro upselling v Odoo Sales.png
:align:center
:alt:Přidávání produktů do předplatného pomocí možnosti upsell v Odoo Subscriptions

Jakmile jsou přidány požadované produkty pro zvýšení tržeb, může být odesláno zákazníkovi.
kliknutím na tlačítko „Odeslat e-mailem“.

.. důležité:
Při potvrzení cenové nabídky zákazníkem jsou k původnímu produktu přidány navrhované doplňkové produkty.
předplatné. Ceny citací se pak přepočítají na zbývající dobu aktuálního účtování
období.

.. poznámka::
Před odesláním nové nabídky zákazníkovi lze cenu za jednotku, daně i slevu změnit.
byla aplikována.

Jakmile zákazník schválí nabídku, klikněte na tlačítko „Potvrdit“ v nabídce, čímž ji proměníte ve smlouvu.
objednávky. Když na ni kliknete, objeví se tlačítko „Historie prodejů“, které zobrazuje počet
K tomuto prvotnímu objednávce jsou připojeny prodejní objednávky.

Když je kliknutá tlačítko „Prodejní historie“, Odoo zobrazí samostatnou stránku obsahující
seznam souvisejících objednávek s jasným zobrazením jejich individuálních :guilabel:`Předplatné
Status`.

.. obrázek: upselling/sales-history-smartbutton.png
:align:center
:alt:Příbuzný prodej v rámci předplatného, který je viditelný z tlačítka „Historie prodeje“ v aplikaci Odoo Subscription.

.. viz též:
   - :doc:`../předplatné`
