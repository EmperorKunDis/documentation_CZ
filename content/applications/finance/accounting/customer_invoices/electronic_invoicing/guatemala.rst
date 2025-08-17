:sirotčinec:

======================================
Elektronické fakturace v Guatemale
======================================

Aplikace Odoo **Fakturace** a **Účetnictví** nabízejí právně vyhovující řešení elektronického fakturování.
Vyhovující požadavkům guatemalské legislativy včetně těch stanovených zákonem
„Úřad pro správu daní (SAT) <https://portal.sat.gob.gt/>“

Právní rámec pro elektronické faktury v Guatemale
============================================

Guatemala zavedla povinné elektronické faktury pod názvem „FEL (Factura Electrónica en Línea)“
systém, který se vztahuje na většinu podniků a zlepšuje daňovou kontrolu a modernizuje správu daní.
Zásadní prvky zahrnují:

- **Elektronická fakturace v síti (FEL)**: Povinný systém elektronické fakturace pro obchodníky a spotřebitele
:abbr:`B2G“ transakce, které upravuje :abbr:`SAT (Superintendencia
„Úřad pro správu daní“. Každý autorizovaný dokument musí být podepsán elektronicky a obsahovat
jedinečný certifikační kód.
- **Součástí SAT**: Všechny elektronické dokumenty musí být vydány prostřednictvím ověřeného certifikačního orgánu
„(Dodavatel certifikace)“ a ověřené SATem („Nadřízeným orgánem pro správu
Tributaria) před dodáním zákazníkovi. Jakmile je ověřeno, dokument obdrží
datum certifikace a jedinečný identifikátor UUID.
- **Formát XML**: Guatemala vyžaduje použití formátu XML pro elektronické dokumenty, které jsou v souladu s požadavky SAT
oficiální schéma XSD pro zajištění sledovatelnosti a kompatibility.
- **Časový harmonogram přijetí FEL**: Přechod na FEL byl proveden postupně v rámci ekonomické činnosti
a profil daňového poplatníka, ale je nyní povinné pro většinu obchodních odvětví v zemi.

Splnění guatemalských předpisů o elektronických fakturách
==================================================

Odoo Fakturace usnadňuje splnění požadavků na elektronické faktury v Guatemale tím, že nabízí nativní
Funkce pro integraci a automatizaci FEL:

- **Podporované formáty**: Odoo podporuje většinu povinných typů dokumentů FEL ve formátu XML v souladu se SAT.
včetně faktur (zkratka FACT), kreditních poznámek (zkratka NCRE) a debetních poznámek (zkratka NDEB).
Každý dokument je automaticky předán k ověření ověřovateli (Infile), podepsán elektronickým podpisem a
ověřené v reálném čase společností SAT.
- **Zabezpečené ukládání a vyhledávání**: V souladu s guatemalskými předpisy poskytuje Odoo
centrální a bezpečné uložení ověřených dokumentů včetně jejich grafických XML a PDF verzí
reprezentace s plným přístupem pro kontrolní a auditní procesy.
- **Automatické výpočty a hlášení daně z přidané hodnoty**: Odoo automaticky vypočítává DPH (IVA) a příslušnou daň
výpočty, zajištění souladu s místními daněmi, výjimkami a strukturou hlášení
jak je definováno v SAT.

.. viz též:
:doc:`Dokumentace k guatemalské daňové lokalizaci <../../../fiscal_localizations/guatemala>`

.. varování: Vyloučení odpovědnosti

Tato stránka poskytuje obecný přehled o guatemalských předpisech týkajících se elektronických faktur a jak Odoo podporuje
Splnění požadavků SAT. Není určeno k poskytování právních nebo daňových rad. Doporučujeme
předem se poradit s daňovým poradcem nebo právníkem, který je obeznámený s elektronickou fakturací v Guatemale.
pravidla, která zajistí plné dodržování předpisů přizpůsobená vašim konkrétním podnikatelským potřebám.
