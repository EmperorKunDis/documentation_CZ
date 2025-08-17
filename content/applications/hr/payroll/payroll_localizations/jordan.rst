======
Jordánsko
======

Balíček pro lokální úpravu programu **Payroll** společnosti Jordan nabízí komplexní řešení pro správu mezd.
splnění jordánských pracovních zákonů. Podporuje výpočet daně z příjmu pomocí progresivního zdanění
základní mzda, sociální pojištění zaměstnavatele i zaměstnance a zdravotní pojištění.
včetně náhrad za bydlení a dopravu.

Konfigurace
=============

Instalujte následující moduly, abyste získali všechny funkce Jordanu.
Lokalizace systému pro mzdy a personalistiku:

.. seznam tabulkový::
:hlavičkové řádky: 1

   * Jméno
     - Technické označení
     - Popis
   * --:guilabel:Jordánsko - platová účtárna
     - „l10n_jo_hr_mzdy“
     - Mzdy - základní výpočet, srážková daň, národní příspěvek
daň z příjmu a sociální pojištění
   * – :guilabel:Jordan – Mzdy a účetnictví
     - „l10n_jo_hr_mzdy“
     - Mostový modul mezi **Personalistika** a **Účetnictví**

.. viz též:
:doc:`Dokumentace k daňovému místu Jordánsko <../../../finance/fiscal_localizations/jordan>`

Základní výpočty
==================

Balíček lokální verze Odoo Payroll pro Jordánsko poskytuje základní nástroje pro správu mzdy
Splňují jordánské pracovní zákony a předpisy. Mezi klíčové funkce patří:

- **Základní výpočet mzdy**: Odoo podporuje výpočet mezd zaměstnanců na základě
předdefinované mzdové struktury, které zajišťují přesné zpracování mezd.
- Přispívá na sociální zabezpečení: Zpracovává odvody na sociální zabezpečení za zaměstnance.
přispívání zaměstnavatele, které se řídí místními předpisy.
- Podpora daně z příjmu: Systém je konfigurován tak, aby vypočítal daň z příjmu v Jordánsku.
včetně slev založených na progresivních daňových pásmech, jak je vyžaduje jordánská pracovní a daňová legislativa
zákony.
- **Vlastní slevy a výdaje**: Lokální verze podporuje další slevy a výdaje.
nebo přesčas jako součást výpočtu mzdy.

Tyto funkce zajišťují, že podniky mohou efektivně spravovat výplaty a dodržovat jordánské specifické
právních požadavků. Pro zvýšení funkčnosti mohou podniky využít pružnost Odoa k
upravit pracovní postupy pro mzdy.

Sociální zabezpečení
===============

Balíček pro lokální úpravu programu **Payroll** v Odoo usnadňuje správu sociálního zabezpečení
automatizovat výpočty pro zaměstnance i zaměstnavatele. Výše příspěvku je stanovena v procentech z
je základní mzda zaměstnance s maximální hranicí pojistného platu v souladu s jordánským sociálním
Zákony o bezpečnosti společnosti SSC.

Příspěvky zaměstnance
----------------------

Odoo vypočítává odvod na sociální zabezpečení zaměstnance ve výši 7,5 % jeho základní mzdy, a to do
maximální výši pojistného platu ve výši 3 000 JOD. Pokud je mzda zaměstnance vyšší než tato částka, bude se z ní odvádět
na částku, která je omezena. Tím se zajistí dodržování :abbr:`SSC (jordánského systému sociálního zabezpečení).
Požadavky společnosti) a odráží přesně na výplatní pásce zaměstnance.

Přispívání zaměstnavatele
----------------------

Pro zaměstnavatele vypočítává Odoo sociální pojištění ve výši 14,25 % z základního platu zaměstnance.
Také omezena na 3 000 JOD. Stejně jako příspěvky zaměstnance, pokud plat přesahuje tuto hranici,
Příspěvek zaměstnavatele se vypočítává z maximální částky. Do příspěvku patří
penze, pojištění pracovních úrazů a další povinné výhody.

Hlavní vlastnosti
------------

- Přispívání s omezeným limitem: Systém zajišťuje, že příspěvky zaměstnance i zaměstnavatele jsou
společně s pojistným limitem stanoveným SSC.
- **Automatické výpočty**: Příspěvky se automaticky vypočítají a započtou do mzdy.
snížení chyb a administrativní práce.
- **Splnění předpisů**: Konfigurace Odoo zajišťuje plné splnění jordánských předpisů
zákony o sociálním zabezpečení, které odrážejí správné sazby a limity pro obě strany.

Daň z příjmu
======================

Balíček pro lokální úpravu programu **Payroll** automaticky vypočítává daň z příjmu pomocí pokročilé sazby
zajišťují dodržování jordánských pracovních zákonů. Systém aplikuje sazby daně z příjmu
Na hrubé mzdu zaměstnance, s vyššími pásmy se zvyšujícím procentem.
Výpočet se dělí na šest sloupců a příslušná daň se strhává měsíčně.

Daňové pásmo
------------

- Pásmo s 5 % daně: Použijte pro roční hrubý příjem do výše 5 000 dinárů. Odoo vypočítává 5 % z
příjmy v tomto rozmezí. Pokud hrubý příjem nepřesáhne 5 000 jordánských dinárů, celý obnos je zdaněn
  5%.
- **10% daňový pás**: Použitelný pro roční hrubé příjmy mezi 5 001 a 10 000 JOD. Platí pouze část
Daň z příjmu nad 5 000 JOD činí 10 %. Například pokud je hrubý příjem 7 000 JOD, daň bude činit
2 000 JOD se zdaní 10 %.
- **15% daňový pás**: Vztahuje se na roční hrubý příjem mezi 10 001 a 15 000 JOD.
Příjem nad 10 000 JOD do 15 000 JOD je zdaněn sazbou 15 %. Například pokud čistý příjem dosahuje
12.000 JOD, pouze 2.000 JOD je zdaněno sazbou 15 %.
- Sazba 20 %: Aplikovatelná na roční hrubý příjem mezi 15 001 a 20 000 dinárů.
Tato částka je zdaněna sazbou 20 % a odpočty jsou automaticky upraveny systémem Odoo.
- **25% daňový pás**: Použitelný pro roční hrubé příjmy mezi 20 001 a 1 000 000 JOD.
Do výše 20 000 JOD a do výše 1 milionu JOD je zdaněno 25 %. Pro vyšší příjmy zajišťuje Odoo přesné
výpočet s použitím této hodnoty.
- **30% daňový pás**: Aplikovatelné na roční hrubý příjem převyšující 1 milion dinárů. Všechny příjmy nad touto hranicí
Výše daně činí 30 %, systém zajišťuje přesné měsíční srážky pro vysokopříjmové osoby.
příjmových skupinách.

Automatizovaný proces
-----------------

Odoo určí příslušnou daňovou sazbu pro každého zaměstnance na základě jeho hrubé roční mzdy.
aplikuje odpovídající sazby. Tyto odečty jsou přepočítávány a odečítány měsíčně, což usnadňuje
správu mezd a zajištění souladu.

Hlavní vlastnosti
------------

- **Progresivní daňový systém**: Vypočítává daně pro každou část příjmu zvlášť a zajišťuje spravedlnost
a přesnost.
- **Automatické odpočty**: Zajišťuje hladký průběh výplaty s přesnými měsíčními daněmi
slevy.
- Soulad s jordánskými předpisy: Plně vyhovuje jordánským daňovým zákonům a minimalizuje
ruční zásahy a chyby.
