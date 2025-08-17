=========
Salt Edge
=========

Salt Edge je třetí stranou, která shromažďuje informace o bankovnictví.
z vašich účtů. Podporuje ~5000 institucí ve více než 50 zemích.
země.

Odoo může synchronizovat přímo s vaší bankou a dostat všechny výpisy z účtu importované.
automaticky do vaší databáze.

.. viz též:
   - :doc:`/bankovní synchronizace``
   - :doc:`../transakce`

Konfigurace
=============

Propojte své bankovní účty s Odoo
---------------------------------

#Začněte synchronizaci kliknutím na:menuselection:`Účetnictví --> Konfigurace
--> Přidat bankovní účet.
#Vyberte instituci, se kterou chcete synchronizovat. Můžete vidět, zda je
třetí stranou, která poskytuje instituci služby.
#Po zadání telefonního čísla se vám zeptá na e-mailovou adresu. Tato e-mailová
Adresa je použita k vytvoření účtu u společnosti Salt Edge. Ujistěte se, že zadáváte správnou adresu.
platná e-mailová adresa, jinak se nebudete moci dostat k hranici soli.
účet.

.... obrázek:: saltedge/saltedge-contact-email.png
:alt:E-mailovou adresu, kterou poskytnete společnosti Salt Edge pro vytvoření vašeho účtu.

#Po zadání e-mailové adresy vás přesměruje na stránky společnosti Salt Edge, kde můžete pokračovat.
synchronizační proces.

.... obrázek: saltedge/saltedge-login-page.png
:alt:Přihlášení do aplikace Salt Edge.

#Ujistěte se, že souhlasíte zaškrtnutím políčka pro udělení souhlasu.

.... obrázek: saltedge/saltedge-give-consent.png
:alt:Souhlasová stránka společnosti Salt Edge.

#Dokončete synchronizaci podle následujících kroků.


Aktualizujte své přihlašovací údaje
-----------------------

Aby jste aktualizovali přihlašovací údaje nebo změnili nastavení synchronizace, aktivujte
Vývojářský režim (viz developer mode), přejděte do sekce „Účetnictví“ – „Konfigurace“
Online synchronizace“ a vyberte instituci, u které chcete aktualizovat přihlašovací údaje. Klikněte
Klikněte na „Aktualizovat přihlašovací údaje“ a postupujte podle pokynů.

Nezapomeňte zaškrtnout souhlas s podmínkami. Jinak nemusí být možné přístup k Odoo
Vaše informace.

Vygenerovat nové účty
------------------

Přidat nové online účty do vaší sítě, aktivujte režim vývojáře
Přejděte do sekce „Účetnictví“ -> „Konfigurace“ -> „Online synchronizace“, vyberte
instituci, aby získala nové účty. Klikněte na tlačítko „Získat účty“ a
Postupujte podle pokynů.

.. poznámka::
Nezapomeňte zaškrtnout souhlas s podmínkami používání. Jinak nemusí být schopna aplikace Odoo přistupovat k vašim datům.
informace.

Často kladené otázky
===

Při pokusu o smazání synchronizace v Odoo se mi zobrazí chybová hláška
-------------------------------------------------------------------

Odoo nemůže trvale smazat připojení, které jste vytvořili se svou bankovní institucí.
Může odvolat souhlas, který jste dali, takže Odoo už nebude moci přistupovat k vašemu účtu.
chyba, kterou vidíte, je pravděpodobně zpráva o tom, že souhlas byl odvolán, ale záznam
nemůže být smazán, protože stále existuje v hranici soli. Pokud chcete odstranit připojení
plně prosím připojte se k vašemu účtu „Salt Edge <https://www.saltedge.com/dashboard>“.
a ručně smazat vaši synchronizaci. Jakmile je to hotové, můžete se vrátit do Odoo a smazat
rekord.

Mám chybu, že už jsem tento účet synchronizoval.
--------------------------------------------------------------------

Synchronizace vašeho účtu s Salt Edgem je pravděpodobně již provedena. Prosím zkontrolujte
„přístrojová deska <https://www.saltedge.com/dashboard>“ (kterou nemáte již zaregistrovanou)
stejné přihlašovací údaje.

Pokud již máte synchronizaci s týmiž přihlašovacími údaji, které jsou na vašem zařízení Salt Edge
přístrojovou desku a tato synchronizace nebyla vytvořena s Odoo, odstraňte ji a vytvořte ji znovu z vašeho
Odoo databáze.

Pokud již máte připojení s týmiž přihlašovacími údaji, které jsou na vaší stránce Salt Edge.
a tato synchronizace byla vytvořena s Odoo, aktivujte:ref:`vývojáře
režim vývojáře (developer-mode)“, přejděte na „:menu-selection:Účetnictví -> Konfigurace -> Online“
Synchronizace“ a klikněte na „Aktualizovat přihlašovací údaje“, abyste znovu aktivovali spojení.
