=========
Funkce
=========

**Odoo Tabulka** podporuje vzorce a funkce, které najdete ve většině tabulkových řešení. Tato stránka
Zobrazuje dostupné funkce podle kategorií. Funkce specifické pro Odoo jsou zahrnuty jak v
relevantní kategorii a v kategorii určené pro funkci Odoo:

- :ref:`Výčet <spreadsheet/functions/array>“
- :ref:`Databáze <rozsah funkcí/databáze>`
- :ref:`Datum <spreadsheet/functions/date>`
- :ref:`Inženýrství <spreadsheet/functions/engineering>`
- :ref:`Filtr <rozsah/funkce/filtr>`
- :ref:`Finanční <spreadsheet/functions/financial>`
- :ref:`Informace <spreadsheet/functions/info>`
- :ref:`Logické <spreadsheet/functions/logical>`
- :ref:`Vyhledávání <spreadsheet/functions/lookup>`
- :ref:`Matematika <rozšířené funkce/matematika>`
- :ref:`Prováděcí programy <spreadsheet/functions/operators>`
- :ref:`Parsér <spreadsheet/functions/parser>`
- :ref:`Statistické <spreadsheet/functions/statistical>“
- :ref:`Text <spreadsheet/functions/text>`
- :ref:`Web <spreadsheet/functions/web>`
- :ref:`Funkce specifické pro Odoo <spreadsheet/functions/odoo>`

.. poznámka::
Formule obsahující funkce, které nejsou kompatibilní s aplikací Excel, jsou nahrazeny jejich vyhodnocenými
výsledek při exportu tabulky.

.. _tabulka/funkce/výčet:

Array
=====

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * – VÝBĚR(vstupní rozsah, řádky, sloupce)
     - Vrací výsledný seznam omezený na konkrétní šířku a výšku (není kompatibilní s aplikací Excel).
   * – VYBERTEKOLY (složka, číslo sloupce, [číslo sloupce 2, …])
     - „Článek o funkci CHOOSECOLS na webu Microsoftu <https://support.microsoft.com/office/choosecols-function-bf117976-2722-4466-9b9a-1c01ed9aebff>“
   * – VYBRAT(složka, řádek, [řádek2, …])
     - „Článek o funkci Chooserows <https://support.microsoft.com/office/chooserows-function-51ace882-9bab-4a44-9625-7274ef7507a3>“
   * – Rozšířit (složený výraz, řádky, [sloupce], [přidat mezery])
     - „Rozšíření článku v aplikaci Excel <https://support.microsoft.com/office/expand-function-7433fba5-4ad1-41da-a904-d5d95808bc38>“
   * – snížit (rozsah, [rozsah2, ...])
     - Všechny hodnoty z jedné nebo více rozsahů sloučí do jednoho sloupce (není kompatibilní s Excel)
   * -FREKVENCE(datum, třídy)
     - „Článek o funkci Frekvence na webu podpory Microsoftu <https://support.microsoft.com/office/frequency-function-44e3be2b-eca0-42cd-a3f7-fd9ea898fdb9>“
   * -HSTACK(range1, [range2, ...])
     - „Článek o funkci HSTACK na webu Microsoftu <https://support.microsoft.com/office/hstack-function-98c4ab76-10fe-4b4f-8d5f-af1c125fe8c2>“
   * - MDETERM(čtvercová matice)
     - „Funkce MDETERM v článku <https://support.microsoft.com/office/mdeterm-function-e7bfa857-3834-422b-b871-0ffd03717020>“
   * -MINVERSE(čtvercová matice)
     - „Článek o funkci MINVERSE <https://support.microsoft.com/office/minverse-function-11f55086-adde-4c9f-8eb9-59da2d72efc6>“
   * - M*MULT(matrix1, matrix2)
     - „Článek o funkci MMULT (<https://support.microsoft.com/office/mmult-function-40593ed7-a3cd-4b6b-b9a3-e4ad3c7245eb>).“
   * -SUMPRODUKT(range1, [range2, ...])
     - „Funkce SUMPRODUCT - článek <https://support.microsoft.com/office/sumproduct-function-16753e75-9f68-4874-94ac-4d2145a2fd2e>“
   * –SUMX2MY2(složka_x, složka_y)
     - „Článek o funkci SUMX2MY2 <https://support.microsoft.com/office/sumx2my2-function-9e599cc5-5399-48e9-a5e0-e37812dfa3e9>“
   * –SUMX2PY2(složka_x, složka_y)
     - „Článek o funkci SUMX2PY2 <https://support.microsoft.com/office/sumx2py2-function-826b60b4-0aa2-4e5e-81d2-be704d3d786f>“
   * -SUMXMY2(složka_x, složka_y)
     - „Funkce SUMXMY2 - článek <https://support.microsoft.com/office/sumxmy2-function-9d144ac1-4d79-43de-b524-e2ecee23b299>“
   * –TOCOL (složený výraz, [ignorovat], [skenování sloupcem])
     - „Funkce TOCOL v článku o Excelu <https://support.microsoft.com/office/tocol-function-22839d9b-0b55-4fc1-b4e6-2761f8f122ed>“
   * – TOROW (array, [ignorovat], [skenovat sloupcem])
     - „Funkce TOROW v článku <https://support.microsoft.com/office/torow-function-b90d0964-a7d9-44b7-816b-ffa5c2fe2289>“
   * -TRANSPOZICE (rozsah)
     - „Převod funkce“ (článek <https://support.microsoft.com/office/transpose-function-ed039415-ed8a-4a81-93e9-4b6dfac76027>).
   * VSTACK(rozsah1, [rozsah2, ...])
     - „Článek o funkci VSTACK <https://support.microsoft.com/office/vstack-function-a4b86897-be0f-48fc-adca-fcc10d795a9c>“
   * -WRAPCOLS (rozsah, počet obalů, [přidat mezery])
     - „Článek o funkci WRAPCOLS v Excelu <https://support.microsoft.com/office/wrapcols-function-d038b05a-57b7-4ee0-be94-ded0792511e2>“
   * - WRAPROWS (rozsah, počet zobrazení, [zaplnit])
     - „Funkce WRAPROWS v článku <https://support.microsoft.com/office/wraprows-function-796825f3-975a-4cee-9c84-1bbddf60ade0>“

.._excelové tabulky, funkce a databáze:

Databáze
========

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * -DAVERAGE(databáze, pole, kritéria)
     - „Článek o funkci DAVERAGE <https://support.microsoft.com/office/daverage-function-a6a2d5ac-4b4b-48cd-a1d8-7b37834e5aee>“
   * -DCOUNT(databáze, pole, kritéria)
     - „Článek o funkci DCOUNT na webu Microsoftu <https://support.microsoft.com/office/dcount-function-c1fc7b93-fb0d-4d8d-97db-8d5f076eaeb1>“
   * DCOUNTA(databáze, pole, kritéria)
     - `Excel DCOUNTA článek <https://support.microsoft.com/office/dcounta-function-00232a6d-5a66-4a01-a25b-c1653fda1244>`_
   * DGET(databáze, pole, kritéria)
     - „Článek o funkci DGET na webu Microsoftu <https://support.microsoft.com/office/dget-function-455568bf-4eef-45f7-90f0-ec250d00892e>“
   * DMAX (tabulka, pole, kritéria)
     - „Článek o funkci DMAX na webu Microsoftu <https://support.microsoft.com/office/dmax-function-f4e8209d-8958-4c3d-a1ee-6351665d41c2>“
   * DMIN(databáze, pole, kritéria)
     - „Funkce DMIN v článku Excelu <https://support.microsoft.com/office/dmin-function-4ae6f1d9-1f26-40f1-a783-6dc3680192a3>“
   * – DPRODUKT(databáze, pole, kritéria)
     - „Funkce DPRODUCT <https://support.microsoft.com/office/dproduct-function-4f96b13e-d49c-47a7-b769-22f6d017cb31>“
   * -DSTDEV(databáze, pole, kritéria)
     - „Článek o funkci DSTDEV <https://support.microsoft.com/office/dstdev-function-026b8c73-616d-4b5e-b072-241871c4ab96>“
   * - DSTDEVP(databáze, pole, kritéria)
     - „Článek o funkci DSTDEVP na webu podpory Microsoftu <https://support.microsoft.com/office/dstdevp-function-04b78995-da03-4813-bbd9-d74fd0f5d94b>“
   * -DSUM(databáze, pole, kritéria)
     - „Článek o funkci DSUM v Excelu <https://support.microsoft.com/office/dsum-function-53181285-0c4b-4f5a-aaa3-529a322be41b>“
   * DVAR(tabulka, pole, kritéria)
     - „Článek o funkci DVAR v Excelu <https://support.microsoft.com/office/dvar-function-d6747ca9-99c7-48bb-996e-9d7af00f3ed1>“
   * DVÁRP (tabulka, pole, kritéria)
     - „Článek o funkci DVARP na webu Microsoftu <https://support.microsoft.com/office/dvarp-function-eb0ba387-9cb7-45c8-81e9-0394912502fc>“

.._spreadsheet/funkce/datum:

Datum
====

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * - DATUM(rok, měsíc, den)
     - „Článek o funkci DATE na webu Microsoftu <https://support.microsoft.com/office/date-function-e36c0c8c-4104-49da-ab83-82328b832349>“
   * - DATEDIF(start_date, end_date, jednotka)
     - „Článek o funkci DATEDIF <https://support.microsoft.com/office/datedif-function-25dba1a4-2812-480b-84dd-8b32a451b35c>“
   * - DATEVALUE(datový řetězec)
     - „Excel DATEVALUE článek <https://support.microsoft.com/office/datevalue-function-df8b07d4-7761-4a93-bc33-b7471bbff252>“
   * - DEN(datum)
     - „Článek o funkci DAY na webu Microsoftu <https://support.microsoft.com/office/day-function-8a7d1cbb-6c7d-4ba1-8aea-25c134d03101>“
   * - DNY(konec, začátek)
     - „Článek o funkci DAYS na webu Microsoftu <https://support.microsoft.com/office/days-function-57740535-d549-4395-8728-0f07bff0b9df>“
   * – DAYS360 (datum začátku, datum konce, metoda)
     - „Článek o funkci DAYS360 <https://support.microsoft.com/office/days360-function-b9a509fd-49ef-407e-94df-0cbda5718c2a>“
   * - EDATE(start_date, měsíců)
     - „Článek o funkci EDATE na webu Microsoftu <https://support.microsoft.com/office/edate-function-3c920eb2-6e66-44e7-a1f5-753ae47ee4f5>“
   * -EOMONTH(start_date, měsíců)
     - „Článek o funkci EOMONTH na webu podpory Microsoftu <https://support.microsoft.com/office/eomonth-function-7314ffa1-2bc9-4005-9d66-f49db127d628>“
   * -HODINA
     - „Článek o funkci HOUR <https://support.microsoft.com/office/hour-function-a3afa879-86cb-4339-b1b5-2dd2d7310ac7>“
   * -ISOWEEKNUM(datum)
     - „Článek o funkci ISOWEEKNUM <https://support.microsoft.com/office/isoweeknum-function-1c2d0afe-d25b-4ab1-8894-8d0520e90e0e>“
   * -MINUTA
     - „Minutová funkce“ (<https://support.microsoft.com/office/minute-function-af728df0-05c4-4b07-9eed-a84801a60589>).
   * -MĚSÍC(datum)
     - „Článek o funkci MONTH (<https://support.microsoft.com/office/month-function-579a2881-199b-48b2-ab90-ddba0eba86e8>).“
   * - MĚSÍC.KONEC(datum)
     - Poslední den v měsíci následující po datu (není kompatibilní s Excel)
   * - MĚSÍC.ZAČÁTEK(datum)
     - První den v měsíci před datem (nekompatibilní s Excel)
   * -NETWORKDAYS(start_date, end_date, [svátky])
     - „Článek o funkci NETWORKDAYS <https://support.microsoft.com/office/networkdays-function-48e717bf-a7a3-495f-969e-5005e3eb18e7>“
   * -NETWORKDAYS.INTL(start_date, end_date, [weekend], [holidays])
     - „Článek o funkci NETWORKDAYS.INTL <https://support.microsoft.com/office/networkdays-intl-function-a9b26239-4f20-46a1-9ab8-4e925bfd5e28>“
   * - NOW()
     - „Článek o funkci NOW <https://support.microsoft.com/office/now-function-3337fd29-145a-4347-b2e6-20c904739c46>“
   * -ČTVRTLETÍ (datum)
     - Čtvrtina roku, ve které spadá konkrétní datum (není kompatibilní s Excelem)
   * - ČTVRTLETÍ KONEC (datum)
     - Poslední den čtvrtletí je v daném roce konkrétním dnem (není kompatibilní s Excel)
   * -ČTVRTINA.ZAČÍTKOVAT(datum)
     - První den čtvrtletí v daném roce je specifický (není kompatibilní s Excel)
   * - DVOJKA
     - „Druhá funkce článku <https://support.microsoft.com/office/second-function-740d1cfc-553c-4099-b668-80eaa24e8af1>“
   * - ČAS (hodina, minuta, sekunda)
     - „Článek o funkci TIME na webu Microsoftu <https://support.microsoft.com/office/time-function-9a5aff99-8f7d-4611-845e-747d0b8d5457>“
   * - TIMEVALUE(časová řada)
     - „Článek o funkci TIMEVALUE na webu Microsoftu <https://support.microsoft.com/office/timevalue-function-0b615c12-33d8-4431-bf3d-f3eb6d186645>“
   * - DNES()
     - „Článek Excelu Today <https://support.microsoft.com/office/today-function-5eb3078d-a82c-4736-8930-2f51a028fdd9>“
   * - PONDĚLÍ (datum, [typ])
     - „Článek o funkci WEEKDAY v Excelu <https://support.microsoft.com/office/weekday-function-60e44483-2ed1-439f-8bd0-e404c190949a>“
   * -WEEKNUM(datum, [typ])
     - „Článek o funkci WEEKNUM <https://support.microsoft.com/office/weeknum-function-e5c43a03-b4ab-426c-b411-b18c13c75340>“
   * - DNYPRACOVNI (datum_zahájení, počet_dní, [svátky])
     - „Článek o funkci WORKDAY v Excelu <https://support.microsoft.com/office/workday-function-f764a5b7-05fc-4494-9486-60d494efbf33>“
   * - WORKDAY.INTL(start_datum, počet dní, [víkend], [svátky])
     - „Článek o funkci WORKDAY.INTL <https://support.microsoft.com/office/workday-intl-function-a378391c-9ba7-4678-8a39-39611a9bf81d>“
   * - ROK(datum)
     - „Funkce YEAR - článek <https://support.microsoft.com/office/year-function-c64f017a-1354-490d-981f-578e8ec8d3b9>“
   * - KONEČNÉ DATUM
     - Poslední den v roce je specifický den (není kompatibilní s Excel)
   * - ROK.ZAČÁTEK(datum)
     - První den v roce je specifický datum (není kompatibilní s Excel)
   * - ROKFRAK (datum začátku, datum ukončení, [způsob počítání dnů])
     - Přesná délka mezi dvěma daty (není kompatibilní s Excel)

.._rozsáhlé tabulky, funkce a inženýrské výpočty.

Inženýrství
===========

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * – DELTA(číslo1, [číslo2])
     - „Článek o funkci DELTA <https://support.microsoft.com/office/delta-function-2f763672-c959-4e07-ac33-fe03220ba432>“

..._spreadsheet/functions/filter:

Filtr
======

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * -FILTER(rozsah, podmínka1, [podmínka2, …])
     - „Příspěvek k filtru v Excelu <https://support.microsoft.com/office/filter-function-f4f7cb66-82eb-4767-8f7c-4877ad80c759>“
   * - ODOO.FILTER.VALUE(název filtru)
     - Vrací aktuální hodnotu filtru v tabulce (není kompatibilní s aplikací Excel).
   * – SORT(rozsah, [sloupec_seřazení, ...], [je_vzestupně, ...])
     - „Článek o funkci SORT <https://support.microsoft.com/en-us/office/sort-function-22f63bd0-ccc8-492f-953d-c20e8e44b86c>“
   * -UNIKÁTNÍ (rozsah, [podle sloupce], [přesně jednou])
     - „Funkce Unikátní článek“ (https://support.microsoft.com/office/unique-function-c5ab87fd-30a3-4ce9-9d1a-40204fb85e1e)

.._excel/funkce/finance:

Finanční
=========

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * - ACCRINTM(vydání, splatnost, sazba, zpětný odkup, [denní konvence])
     - „Excel ACCRINTM článek <https://support.microsoft.com/office/accrintm-function-f62f01f9-5754-4cc4-805b-0e70199328a7>“
   * - AMORLINC (cena, nákupní datum, první konec období, rezerva, období, sazba, [denní konvence])
     - `Excel AMORLINC funkce <https://support.microsoft.com/office/amorlinc-function-7d417b45-f7f5-4dba-a0a5-3451a81079a8>`_
   * -COUPDAYS(splatnost, dozrání, frekvence, [denní konvence])
     - „Funkce COUPDAYBS - <https://support.microsoft.com/office/coupdaybs-function-eb9a8dfb-2fb2-4c61-8e5d-690b320cf872>“
   * - DNY SPLATNOSTI (termín splatnosti, četnost úročení, [denní metoda počítání úroků])
     - „Článek o funkci COUPDAYS na webu Microsoft Support <https://support.microsoft.com/office/coupdays-function-cc64380b-315b-4e7b-950c-b30b0a76f671>“
   * -COUPDAYSNC(splatnost, dozrání, frekvence, [denní konvence])
     - „Článek o funkci COUPDAYSNC <https://support.microsoft.com/office/coupdaysnc-function-5ab3f0b2-029f-4a8b-bb65-47d525eea547>“
   * -COUPNCD(splatnost, doba splatnosti, frekvence, denní konvence)
     - „Funkce COUPNCD <https://support.microsoft.com/office/coupncd-function-fd962fef-506b-4d9d-8590-16df5393691f>“
   * - COUPNUM(splatnost, doba splatnosti, frekvence, [denní konvence])
     - `Funkce COUPNUM v článku <https://support.microsoft.com/office/coupnum-function-a90af57b-de53-4969-9c99-dd6139db2522>
   * -COUPPCD(splatnost, doba splatnosti, frekvence, denní konvence)
     - „Funkce COUPPCD v článku <https://support.microsoft.com/office/couppcd-function-2eb50473-6ee9-4052-a206-77a9a385d5b3>“
   * - CUMIPMT(sazba, počet období, současná hodnota, první období, poslední období, [konec nebo začátek])
     - „Článek o funkci CUMIPMT na webu Microsoftu <https://support.microsoft.com/office/cumipmt-function-61067bb0-9016-427d-b95b-1a752af0e606>“
   * - CUMPRINC(sazba, počet období, současná hodnota, první období, poslední období, [konec nebo začátek])
     - `Excel CUMPRINC článek <https://support.microsoft.com/office/cumprinc-function-94a4516d-bd65-41a1-bc16-053a6af4c04d>`_
   * - DB(náklady, záchrana, život, období, měsíc)
     - „Článek o funkci Excelu <https://support.microsoft.com/office/db-function-354e7d28-5f93-4ff1-8a52-eb4ee549d9d7>“
   * – DDB (náklady, vyproštění, život, doba, faktor)
     - „Článek o funkci DDB <https://support.microsoft.com/office/ddb-function-519a7a37-8772-4c96-85c0-ed2c209717a5>“
   * -DISC(splatnost, dozrání, cena, zpětný odkup, denní konvence)
     - „Článek o funkci DISC <https://support.microsoft.com/office/disc-function-71fce9f3-3f05-4acf-a5a3-eac6ef4daa53>“
   * –DOLARDE(částka, jednotka)
     - „Dollared funkce <https://support.microsoft.com/office/dollarde-function-db85aab0-1677-428a-9dfd-a38476693427>“
   * –DOLARFR(desetinná cena, jednotka)
     - `Excel DOLLARFR funkce <https://support.microsoft.com/office/dollarfr-function-0835d163-3023-4a33-9824-3042c5d4f495>`_
   * –DÉLKA (splatnost, dozrání, sazba, výnos, frekvence, [denní konvence])
     - „Článek o funkci DURATION <https://support.microsoft.com/office/duration-function-b254ea57-eadc-4602-a86a-c8e369334038>“
   * -EFEKT (nominální sazba, počet období za rok)
     - „Článek o funkci Excel EFFECT <https://support.microsoft.com/office/effect-function-910d4e4c-79e2-4009-95e6-507e04f11bc4>“
   * FV(sazba, počet období, výše splátky, [předpokládaná hodnota], [konec nebo začátek])
     - „Funkce Excelu <https://support.microsoft.com/office/fv-funkce-2eef9f44-a084-4c61-bdd8-4fe4bb1b71b3>“
   * -FVSPROGRAM(hlavní, sazebník)
     - „Článek o funkci FVSCHEDULE <https://support.microsoft.com/office/fvschedule-function-bec29522-bd87-4082-bab9-a241f3fb251d>“
   * - INTRATE (datum vypořádání, datum splatnosti, investiční, výplatní, [denní konvence])
     - „Funkce Intrate v článku Microsoftu <https://support.microsoft.com/office/intrate-function-5cb34dde-a221-4cb6-b3eb-0b9e55e1316f>“
   * -IPMT(sazba, období, počet období, současná hodnota, [budoucí hodnota], [konec nebo začátek])
     - „Článek o funkci IPMT na webu Excelu <https://support.microsoft.com/office/ipmt-function-5cce0ad6-8402-4a41-8d29-61a0b054cb6f>“
   * -IRR(příjmy, [odhadovaná míra inflace])
     - „Článek o funkci IRR na webu Microsoftu <https://support.microsoft.com/office/irr-function-64925eaa-9988-495b-b290-3ad0c163c1bc>“
   * -ISPMT(sazba, období, počet období, současná hodnota)
     - „Článek o funkci ISPMT na webu Microsoftu <https://support.microsoft.com/office/ispmt-function-fa58adb6-9d39-4ce0-8f43-75399cea56cc>“
   * -MDURATION(datum splatnosti, datum dozrání, úroková sazba, výnos, frekvence, [denní konvence])
     - „Článek o funkci MDURATION na webu Microsoftu <https://support.microsoft.com/office/mduration-function-b3786a69-4f20-469a-94ad-33e5b90a763c>“
   * -MIRR (příjmy z hotovosti, úroková sazba, návratnost investic)
     - „Článek o funkci MIRR na webu Microsoftu <https://support.microsoft.com/office/mirr-function-b020f038-7492-4fb4-93c1-35c345b53524>“
   * -NOMINÁL(účinná sazba, počet období za rok)
     - „Článek o funkci NOMINAL <https://support.microsoft.com/office/nominal-function-7f1ae29b-6b92-435e-b950-ad8b190ddd2b>“
   * - NPER(sazba, platba, současná hodnota, [budoucí hodnota], [konec nebo začátek])
     - „Článek o funkci NPER na webu Microsoftu <https://support.microsoft.com/office/nper-function-240535b5-6653-4d2d-bfcf-b6a38151d815>“
   * -NPV(sleva, příjem v hotovosti 1, [příjem v hotovosti 2, ...])
     - „Článek o funkci NPV na webu Microsoftu <https://support.microsoft.com/office/npv-function-8672cb67-2576-4d07-b67b-ac28acf2a568>“
   * – ODOO.ACCOUNT.GROUP(typ)
     - Vrátí ID účtu skupiny (není kompatibilní s Excel)
   * - ODOO.KREDIT(účetní kódy, datový rozsah, [offest], [ID společnosti], [zahrnout nezaúčtované položky])
     - Získat celkový kredit na uvedených účtech a v daném období (není kompatibilní s Excel)
   * - ODOO.CURRENCY.RATE(měna_od, měna_do, [datum])
     - Tato funkce přijímá jako argumenty dva měnové kódy a vrací směnný kurz z prvního měnové jednotky na druhou jako desetinné číslo (není kompatibilní s aplikací Excel).
   * - ODOO.DEBIT(účetní kódy, datový rozsah, [odstup], [ID společnosti], [zahrnout neevidované transakce])
     - Získat celkový zůstatek na účtu a období (nekompatibilní s aplikací Excel).
   * – ODOO.BALANCE (účetní kódy, datový rozsah, [offest], [ID firmy], [zahrnout nezaúčtované položky])
     - Získat součet zůstatku na účtu a období (není kompatibilní s aplikací Excel).
   * - ODOO.FISCALYEAR.END(den, [firma_id])
     - Vrací datum konce účetního období, které zahrnuje poskytnuté datum (není kompatibilní s Excel).
   * - ODOO.FISCALYEAR.START(den, [firma_id])
     - Vrací datum začátku fiskálního roku, který zahrnuje poskytnuté datum (není kompatibilní s aplikací Excel).
   * – DLOUHOTRVÁLOST (sazba, současná hodnota, budoucí hodnota)
     - „Článek o funkci PDURATION na webu podpory Microsoftu <https://support.microsoft.com/office/pduration-function-44f33460-5be5-4c90-b857-22308892adaf>“
   * – Pmt(sazba, počet období, současná hodnota, [budoucí hodnota], [konec nebo začátek])
     - „Článek o funkci PMT <https://support.microsoft.com/office/pmt-function-0214da64-9a63-4996-bc20-214433fa6441>“
   * – PPMT (sazba, období, počet období, současná hodnota, [budoucí hodnota], [konec nebo začátek])
     - „Článek o funkci PPMT na webu Microsoftu <https://support.microsoft.com/office/ppmt-function-c370d9e3-7749-4ca4-beea-b06c6ac95e1b>“
   * - CENA (splatnost, dozrání, sazba, výnos, zpětný odkup, frekvence, denní konvence)
     - „Funkce Excelu CENA <https://support.microsoft.com/office/price-function-3ea9deac-8dfa-436f-a7c8-17ea02c21b0a>“
   * -PRICEDISC(datum splatnosti, datum splatnosti, sazba, způsob odkupu, [denní konvence])
     - „Článek o funkci PRICEDISC na webu Microsoftu <https://support.microsoft.com/office/pricedisc-function-d06ad7c1-380e-4be7-9fd9-75e3079acfd3>“
   * -PRICEMAT(splatnost, dozrání, emise, úroková sazba, výnos, [denní konvence])
     - „Funkce Excelu PriceMat <https://support.microsoft.com/office/pricemat-function-52c3b4da-bc7e-476a-989f-a95f675cae77>“
   * – PV(sazba, počet období, výše splátky, [budoucí hodnota], [konec nebo začátek])
     - „Článek o funkci PV v Excelu <https://support.microsoft.com/office/pv-function-23879d31-0e02-4321-be01-da16e8168cbd>“
   * - RATE (počet období, platba za jedno období, současná hodnota, [budoucí hodnota], [začátek nebo konec], [hodnota úroku])
     - „Článek o funkci RATE na webu Microsoftu <https://support.microsoft.com/office/rate-function-9f665657-4a7e-4bb7-a030-83fc59e748ce>“
   * - PŘIJATO (splatnost, dozrání, investice, slevy, [denní konvence])
     - „Excel obdržel článek <https://support.microsoft.com/office/received-function-7a3f8b93-6611-4f81-8576-828312c9b5e5>“
   * - RRV (počet období, současná hodnota, budoucí hodnota)
     - „Článek o funkci RRI na webu Microsoftu <https://support.microsoft.com/office/rri-function-6f5822d8-7ef1-4233-944c-79e8172930f4>“
   * - SLN (náklady, záchrana, život)
     - „Článek podpory Microsoftu <https://support.microsoft.com/office/sln-function-cdb666e5-c1c6-40a7-806a-e695edc2f1c8>“
   * -SYD (náklady, záchrana, život, doba)
     - `Funkce SYD <https://support.microsoft.com/office/syd-function-069f8106-b60b-4ca2-98e0-2a0f206bdb27>“
   * TBILLEQ (termín splatnosti, doba fixace, sazba)
     - „Tbilleq funkce <https://support.microsoft.com/office/tbilleq-function-2ab72d90-9b4d-4efe-9fc2-0f81f2c19c8c>“
   * -TBILLPRICE(splatnost, doba splatnosti, slevy)
     - „Článek o funkci TBILLPRICE <https://support.microsoft.com/office/tbillprice-function-eacca992-c29d-425a-9eb8-0513fe6035a2>“
   * -TBILLYIELD(usazení, splatnost, cena)
     - „Článek o funkci TBILLYIELD <https://support.microsoft.com/office/tbillyield-function-6d381232-f4b0-4cd5-8e97-45b9c03468ba>“
   * – VDB (cena, záchrana, život, start, konec, [faktor], [bez přepínače])
     - „Článek o funkci VDB <https://support.microsoft.com/office/vdb-function-dde4e207-f3fa-488d-91d2-66d55e861d73>“
   * -XIRR(čistý příjem, datum čistého příjmu, odhadovaná sazba)
     - „Článek o funkci XIRR <https://support.microsoft.com/office/xirr-function-de1242ec-6477-445b-b11b-a303ad9adc9d>“
   * -XNPV(sleva, částky příjmů, datum příjmu)
     - „Článek o funkci XNPV <https://support.microsoft.com/office/xnpv-function-1b42bbf6-370f-4532-a0eb-d67c16b664b7>“
   * - VÝNOS (datum vypořádání, datum splatnosti, úroková sazba, cena, způsob vyrovnání, frekvence, [denní metoda výpočtu výnosu])
     - „Článek o funkci YIELD“ (https://support.microsoft.com/office/yield-function-f5f5ca43-c4bd-434f-8bd2-ed3c9727a4fe)
   * -YIELDDISC(splatnost, dozrání, cena, zpětný odkup, [denní konvence])
     - „Článek o funkci YIELDDISC na webu podpory Microsoftu <https://support.microsoft.com/office/yielddisc-function-a9dbdbae-7dae-46de-b995-615faffaaed7>“
   * -YIELDMAT (splatnost, doba splatnosti, emise, úroková sazba, cena, denní konvence)
     - „Funkce YIELDMAT v článku <https://support.microsoft.com/office/yieldmat-function-ba7d1809-0d33-4bcb-96c7-6c56ec62ef6f>“

... _tabulka/funkce/informace:

Info
====

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * -CELL(info_type, reference)
     - „Článek o funkci CELL na webu Microsoftu <https://support.microsoft.com/office/cell-function-51bd39a5-f338-4dbe-a33f-955d67c2b2cf>“
   * -ISNULL(hodnota)
     - „Funkce IS v článku na webu podpory Microsoftu <https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665>“
   * -ISERR(hodnota)
     - „Funkce IS v článku na webu podpory Microsoftu <https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665>“
   * -ISERROR(hodnota)
     - „Funkce IS v článku na webu podpory Microsoftu <https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665>“
   * -ISLOGICKÉ(value)
     - „Funkce IS v článku na webu podpory Microsoftu <https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665>“
   * -ISNA(hodnota)
     - „Funkce IS v článku na webu podpory Microsoftu <https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665>“
   * -ISNONTEXT(value)
     - „Funkce IS v článku na webu podpory Microsoftu <https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665>“
   * -ISNUMBER(hodnota)
     - „Funkce IS v článku na webu podpory Microsoftu <https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665>“
   * -IstText(value)
     - „Funkce IS v článku na webu podpory Microsoftu <https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665>“
   * - NE()
     - „Excel - funkce NA“ (<https://support.microsoft.com/office/na-function-5469c2d1-a90c-4fb5-9bbc-64bd9bb6b47c>).

.._spreadsheet/functions/logical:

Logické
=======

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * - A NEBO (logické vyjádření1, logické vyjádření2 atd.)
     - „Excel a funkce AND <https://support.microsoft.com/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9>“
   * - NEPRAVDĚLNOST
     - „Pravdivost článku Excel <https://support.microsoft.com/office/false-function-2d58dfa5-9c03-4259-bf8f-f0ae14346904>“
   * -Pokud je logická výraznost pravdivá, pak hodnota
     - „Příspěvek o funkci IF <https://support.microsoft.com/office/if-function-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2>“
   * - pokud je hodnota nulová, pak se použije výchozí hodnota
     - „Článek o funkci IFERROR <https://support.microsoft.com/office/iferror-function-c526fd07-caeb-47b8-8bb6-63f3e417f611>“
   * - IFNA(hodnota, [hodnota_při_chybě])
     - „Funkce IFNA v článku Microsoftu <https://support.microsoft.com/office/ifna-function-6626c961-a569-42fc-a49d-79b4951fd461>“
   * - IFS(podmínka1, hodnota1, [podmínka2, ...], [hodnota2, ...])
     - „Článek o funkci IFS <https://support.microsoft.com/office/ifs-function-36329a26-37b2-467c-972b-4a39bd951d45>“
   * -NE(logická_výraz)
     - `Excel - funkce NE článku <https://support.microsoft.com/office/not-function-9cfc6011-a054-40c7-a140-cd4ba2d87d77>`
   * -OR(logické výrazy1, [logické výrazy2, ...])
     - `OR funkce <https://support.microsoft.com/office/or-function-7d17ad14-8700-4281-b308-00b131e22af0>`
   * -PRAVDA
     - „Pravdivý článek“ (<https://support.microsoft.com/office/true-function-7652c6e3-8987-48d0-97cd-ef223246b3fb>).
   * - XOR(logická_výraz1, [logická_výraz2, ...])
     - „Článek o funkci XOR <https://support.microsoft.com/office/xor-function-1548d4c2-5e47-4f77-9a92-0533bba14f37>“

.._spreadsheet/functions/výběr:

Překlad
======

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * -ADRESA (řádek, sloupec, [absolutní/relační režim], [používat notaci A1], [list])
     - „Příspěvek Excel ADDRESS <https://support.microsoft.com/office/address-function-d0c26c0d-3991-446b-8de4-ab46431d4f89>“
   * - PŘEDLOŽENÍ(CELL(odkaz))
     - „Funkce sloupce“ (<https://support.microsoft.com/office/column-function-44e8c754-711c-4df3-9da4-47a55042554b>).
   * - Sloupce (rozsah)
     - „Článek o funkci sloupců <https://support.microsoft.com/office/columns-function-4e8e7b4e-e603-43e8-b177-956088fa48ca>“
   * -HLOOKUP(hledaný klíč, rozsah, index, [je řazený])
     - „Článek o funkci HLOOKUP <https://support.microsoft.com/office/hlookup-function-a3034eec-b719-4ba3-bb65-e1ad662ed95f>“
   * -INDEX(odkaz, řádek, sloupec)
     - „Článek o funkci INDEX v Excelu <https://support.microsoft.com/office/index-function-a5dcf0dd-996d-40a4-a822-b56b061328bd>“
   * - NEPŘÍMÉ (odkaz, [použít označení A1])
     - `Excel INDIRECT článek <https://support.microsoft.com/office/indirect-function-474b3a3a-8a26-4f44-b491-92b6306fa261>`_
   * – VYHLEDAT (hledaný klíč, hledaná pole, [rozsah výstupu]).
     - „Výukový článek o funkci LOOKUP <https://support.microsoft.com/office/lookup-function-446d94af-663b-451d-8251-369d5e3864cb>“
   * - MATCH(hledané klíčové slovo, rozsah, [hledání typu])
     - „Článek o funkci MATCH <https://support.microsoft.com/office/match-function-e8dffd45-c762-47d6-bf89-533f4a37673a>“
   * – OFFSET(odkaz, řádky, sloupce, výška, šířka)
     - „Článek o funkci OFFSET <https://support.microsoft.com/en-us/office/offset-function-c8de19ae-dd79-4b9b-a14e-b4d906d11b66>“
   * -PIVOT (pivot_id, [řádků], [zahrnout celkový součet], [zahrnout nadpisy sloupců], [počet sloupců])
     - Vytvořte tabulku s otáčivými sloupci (nekompatibilní s Excelem)
   * - PIVOT.HEADER(pivot_id, [doménové pole jméno, ...], [doménový hodnota, ...])
     - Získat hlavičku tabulky s výsledky (není kompatibilní se softwarem Excel)
   * -PIVOT.VALUE(pivot_id, měřitelný název, pole doménového pole, doménová hodnota, ...)
     - Získat hodnotu z tabulky s agregací (nekompatibilní s Excel)
   * - VYBRAT(CELL([celé_odkazování]),)
     - „Funkce řádku“ (<https://support.microsoft.com/office/row-function-3a63b74a-c4d0-4093-b49a-e76eb49a6d8d>).
   * - ROW(rozsah)
     - „Článek o funkci řádků <https://support.microsoft.com/office/rows-function-b592593e-3fc2-47f2-bec1-bda493811597>“
   * -VLOŽKA (hledaný klíč, rozsah, index, [je řazeno])
     - „Výukový článek o funkci VLOOKUP <https://support.microsoft.com/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1>“
   * -XLOOKUP(hledaný klíč, rozsah pro vyhledávání, rozsah pro návrat, [pokud nenalezeno], [režim shody], [režim vyhledávání])
     - „Článek o funkci XLOOKUP <https://support.microsoft.com/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929>“

.._excel/funkce/matematika:

Matematika
====

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * ABS(hodnota)
     - „Článek o funkci ABS na webu podpory Microsoftu <https://support.microsoft.com/office/abs-function-3420200f-5628-4e8c-99da-c99d7c87713c>“
   * -ACOS(hodnota)
     - „Funkce ACOS v článku Microsoftu <https://support.microsoft.com/office/acos-function-cb73173f-d089-4582-afa1-76e5524b5d5b>“
   * -ACOSH(hodnota)
     - „Článek o funkci ACOSH <https://support.microsoft.com/office/acosh-function-e3992cc1-103f-4e72-9f04-624b9ef5ebfe>“
   * - ACOT(hodnota)
     - „Funkce ACOT v článku na podporu Microsoft Office <https://support.microsoft.com/office/acot-function-dc7e5008-fe6b-402e-bdd6-2eea8383d905>“
   * - ACOTH(hodnota)
     - „Článek o funkci ACOTH <https://support.microsoft.com/office/acoth-function-cc49480f-f684-4171-9fc5-73e4e852300f>“
   * -ASIN(hodnota)
     - „Funkce ASIN v článku o Excelu <https://support.microsoft.com/office/asin-function-81fb95e5-6d6f-48c4-bc45-58f955c6d347>“
   * - ASINH(hodnota)
     - „Článek o funkci ASINH <https://support.microsoft.com/office/asinh-function-4e00475a-067a-43cf-926a-765b0249717c>“
   * - ATAN(hodnota)
     - „Článek o funkci ATAN na webu Microsoftu <https://support.microsoft.com/office/atan-function-50746fa8-630a-406b-81d0-4a2aed395543>“
   * - ATAN2(x, y)
     - „Článek o funkci ATAN2 <https://support.microsoft.com/office/atan2-function-c04592ab-b9e3-4908-b428-c96b3a565033>“
   * - ATANH(hodnota)
     - „Článek o funkci ATANH <https://support.microsoft.com/office/atanh-function-3cd65768-0de7-4f1d-b312-d01c8c930d90>“
   * - STŘECHA (hodnota, faktor)
     - „Článek o funkci CEILING na webu Microsoftu <https://support.microsoft.com/office/ceiling-function-0a5cd7c8-0720-4f0a-bd2c-c943e510899f>“
   * -STROP.MAT(číslo, [důležitost], [způsob])
     - „Článek o funkci CEILING.MATH na webu Microsoftu <https://support.microsoft.com/office/ceiling-math-function-80f95d2f-b499-4eee-9f16-f795a8e306c8>“
   * -CEILING.PRECISE(číslo, [důležitost])
     - „Článek o funkci CEILING.PRECISE <https://support.microsoft.com/office/ceiling-precise-function-f366a774-527a-4c92-ba49-af0a196e66cb>“
   * -COS(úhel)
     - „Funkce COS v článku Excelu“ <https://support.microsoft.com/office/cos-function-0fb808a5-95d6-4553-8148-22aebdce5f05>
   * -COSH(hodnota)
     - „Článek o funkci COSH <https://support.microsoft.com/office/cosh-function-e460d426-c471-43e8-9540-a57ff3b70555>“
   * – úhel COT
     - „Funkce COT v článku o aplikaci Excel <https://support.microsoft.com/office/cot-function-c446f34d-6fe4-40dc-84f8-cf59e5f5e31a>“
   * - COTH(hodnota)
     - „Funkce COTH v článku na podporu Microsoft Office <https://support.microsoft.com/office/coth-function-2e0b4cb6-0ba0-403e-aed4-deaa71b49df5>“
   * - COUNTBLANK(hodnota1, [hodnota2, ...])
     - „Excel - počet prázdných buněk v článku <https://support.microsoft.com/office/countblank-function-6a92d772-675c-4bee-b346-24af6bd3ac22>“
   * -COUNTIF(rozsah, kritérium)
     - „Článek o funkci COUNTIF <https://support.microsoft.com/office/countif-function-e0de10c6-f885-4e71-abb4-1f464816df34>“
   * -COUNTIFS(criteria_range1; criterion1; [criteria_range2, ...]; [criterion2, ...])
     - „Článek o funkci COUNTIFS <https://support.microsoft.com/office/countifs-function-dda3dc6e-f74e-4aee-88bc-aa8c2a866842>“
   * – CSC
     - „Článek o funkci CSC <https://support.microsoft.com/office/csc-function-07379361-219a-4398-8675-07ddc4f135c1>“
   * -CSCH(hodnota)
     - „Funkce CSch v článku Microsoftu <https://support.microsoft.com/office/csch-function-f58f2c22-eb75-4dd6-84f4-a503527f8eeb>“
   * -DECIMAL(hodnota, základ)
     - „Článek o funkci DECIMAL na webu Microsoftu“
   * -STUPNĚ (úhel)
     - „Článek o funkci stupně Excelu <https://support.microsoft.com/office/degrees-function-4d6ec4db-e694-4b94-ace0-1cc3f61f9ba1>“
   * -EXP(hodnota)
     - „EXP funkce“ (<https://support.microsoft.com/office/exp-function-c578f034-2c45-4c37-bc8c-329660a63abe>).
   * – PODLAHOVÁ HODNOTA (hodnota, [faktor])
     - „Článek o funkci Excel FLOOR <https://support.microsoft.com/office/floor-function-14bb497c-24f2-4e04-b327-b0b4de5a8886>“
   * - PODLAHA.MAT(číslo, [důležitost], [způsob])
     - „Článek o funkci FLOOR.MATH na webu podpory Microsoftu <https://support.microsoft.com/office/floor-math-function-c302b599-fbdb-4177-ba19-2c2b1249a2f5>“
   * – PRECISE(číslo, [důležitost]).
     - „Článek o funkci FLOOR.PRECISE na webu podpory Microsoftu <https://support.microsoft.com/office/floor-precise-function-f769b468-1452-4617-8dc3-02f842a0702e>“
   * -INT(value)
     - „Článek o funkci INT na webu Microsoftu <https://support.microsoft.com/office/int-function-a6c4af9e-356d-4369-ab6a-cb1fd9d343ef>“
   * -ISEVEN(hodnota)
     - „Článek o funkci ISEVEN <https://support.microsoft.com/office/iseven-function-aa15929a-d77b-4fbb-92f4-2f479af55356>“
   * -ISO.STROP(číslo, [důležitost])
     - „Článek o funkci ISO.CEILING na webu podpory Microsoftu <https://support.microsoft.com/office/iso-ceiling-function-e587bb73-6cc2-4113-b664-ff5b09859a83>“
   * -ISODD(hodnota)
     - `Excel - funkce ISDOD <https://support.microsoft.com/office/isodd-function-1208a56d-4f10-4f44-a5fc-648cafd6c07a>`
   * LN(hodnota)
     - „Článek v LN <https://support.microsoft.com/office/ln-function-81fe1ed7-dac9-4acd-ba1d-07a142c6118f>“
   * -LOG(hodnota, [základ])
     - Získat odmocninu z čísla pro danou základnu (nekompatibilní s Excel)
   * -MOD(dividenda, čitatel)
     - „Článek o funkci Excelu <https://support.microsoft.com/office/mod-function-9b6cd169-b6ee-406a-a97b-edf2a9dc24f3>“
   * – MUNIT (rozměr)
     - „Článek o funkci MUNIT <https://support.microsoft.com/office/munit-function-c9fe916a-dc26-4105-997d-ba22799853a3>“
   * – ODD(hodnota)
     - „Funkce ODD (<https://support.microsoft.com/office/odd-function-deae64eb-e08a-4c88-8b40-6d0b42575c98>).“
   * -PI()
     - „Článek o funkci PI v Excelu <https://support.microsoft.com/office/pi-function-264199d0-a3ba-46b8-975a-c4a04608989b>“
   * -POWER(základ, exponent)
     - „Článek o funkci Power v Excelu <https://support.microsoft.com/office/power-function-d3f2908b-56f4-4c3f-895a-07fb519c362a>“
   * - VÝROBEK (faktor1, [faktor2, ...])
     - „Článek o funkci produktu“ <https://support.microsoft.com/office/product-function-8e6b5b24-90ee-4650-aeec-80982a0512ce>
   * - RAND()
     - „Článek o funkci RAND na webu Microsoftu <https://support.microsoft.com/office/rand-function-4cbfa695-8869-4788-8d90-021ea9f5be73>“
   * - RANDARRAY(řádků, sloupců, minimální hodnoty, maximální hodnoty, celé číslo)
     - „Článek o funkci RANDARRAY <https://support.microsoft.com/office/randarray-function-21261e55-3bec-4885-86a6-8b0a47fd4d33>“
   * -RANDOM BETWEEN (low, high)
     - „RAND BETWEEN článek <https://support.microsoft.com/office/randbetween-function-4cc7f0d1-87dc-4eb7-987f-a469ab381685>“
   * - ROUND(hodnota, [místo])
     - „Rovná funkce v Excelu <https://support.microsoft.com/office/round-function-c018c5d8-40fb-4053-90b1-b3e7f61a213c>“
   * - ROUNDDOWN(hodnota, [místo])
     - „Článek o funkci ROUNDDOWN <https://support.microsoft.com/office/rounddown-function-2ec94c73-241f-4b01-8c6f-17e6d7968f53>“
   * - ROZHOVOR (hodnota, [místa])
     - „Článek o funkci ROUNDUP <https://support.microsoft.com/office/roundup-function-f8bc9b23-e795-47db-8703-db171d0c42a7>“
   * SEC (úhel)
     - „Článek o funkci SEC v Excelu <https://support.microsoft.com/office/sec-function-ff224717-9c87-4170-9b58-d069ced6d5f7>“
   * - SECH(hodnota)
     - „Funkce SECH v článku o Excelu <https://support.microsoft.com/office/sech-function-e05a789f-5ff7-4d7f-984a-5edb9b09556f>“
   * -SEKVENCE(řádků, [sloupců], [začátek], [krok])
     - `Excel funkce SEQUENCE <https://support.microsoft.com/en-us/office/sequence-function-57467a98-57e0-4817-9f14-2eb78519ca90>`_
   * SIN(úhel)
     - „Funkce SIN v článku o Excelu <https://support.microsoft.com/office/sin-function-cf0e3432-8b9e-483c-bc55-a76651c95602>“
   * -SINH(hodnota)
     - „Excelová funkce SINH <https://support.microsoft.com/office/sinh-function-1e4e8b9f-2b65-43fc-ab8a-0a37f4081fa7>“
   * -SQR(hodnota)
     - „Článek o funkci SQRT <https://support.microsoft.com/office/sqrt-function-654975c2-05c4-4831-9a24-2c65e4040fdf>“
   * -SUM(hodnota1, [hodnota2, ...])
     - „Funkce SUM v článku Excelu <https://support.microsoft.com/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89>“
   * -SUMIF(criteria_range, kritérium, [sum_range])
     - `Funkce SUMIF - článek <https://support.microsoft.com/office/sumif-function-169b8c99-c05c-4483-a712-1697a653039b>`
   * -SUMIFS(součetní rozsah, kritéria rozsahu 1, kritérium 1, [kritéria rozsahu 2, …], [kritérium 2, …])
     - „Článek o funkci SUMIFS <https://support.microsoft.com/office/sumifs-function-c9e748f5-7ea7-455d-9406-611cebce642b>“
   * TAN(úhel)
     - „Článek o funkci TAN <https://support.microsoft.com/office/tan-function-08851a40-179f-4052-b789-d7f699447401>“
   * – TANH(hodnota)
     - „Článek o funkci TANH <https://support.microsoft.com/office/tanh-function-017222f0-a0c3-4f69-9787-b3202295dc6c>“
   * -TRUNC(hodnota, [místo])
     - „Funkce TRUNC - článek <https://support.microsoft.com/office/trunc-function-8b86a64c-3127-43db-ba14-aa5ceb292721>“

..._spreadsheet/functions/operators:

Operátoři
=========

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * - PŘIDAT(hodnota1, hodnota2)
     - Součet dvou čísel (nekompatibilní s Excel)
   * - CONCAT(value1, value2)
     - „Příspěvek o funkci CONCAT <https://support.microsoft.com/office/concat-function-9b1a9a3f-94ff-41af-9736-694cbd6b4ca2>“
   * -DĚLENÍ (dividenda, děleno)
     - Jedna čísla dělená druhou (nekompatibilní s Excel)
   * - EQ (hodnota1, hodnota2)
     - Rovný (nekompatibilní s Excel)
   * – GT(hodnota1, hodnota2)
     - Strictně větší než (nekompatibilní s Excel)
   * - GTE (hodnota1, hodnota2)
     - Větší nebo rovno (není kompatibilní s Excel)
   * -LT(hodnota1, hodnota2)
     - Méně než (nekompatibilní s Excel)
   * - LTE(value1, value2)
     - Menší nebo rovno (nekompatibilní s Excel)
   * - MINUS(value1, value2)
     - Rozdíl dvou čísel (nekompatibilní s Excel)
   * -MULTIPLY(faktor1, faktor2)
     - Produkt dvou čísel (nekompatibilní s Excel)
   * - NE(hodnota1, hodnota2)
     - Není kompatibilní s Excel
   * - POW(základ, exponent)
     - Číslo vynásobené číslem (není kompatibilní s Excel)
   * -UMINUS(hodnota)
     - Číslo s obráceným znaménkem (není kompatibilní se softwarem Excel)
   * -UNÁRNÍ.PROCENTO(procento)
     - Hodnota vyjádřená procentem (není kompatibilní s Excel)
   * + (hodnota)
     - Uvedený počet, nezměněný (není kompatibilní s Excel)

..._spreadsheet/funkce/parsování:

Parsér
======

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * - PŘEVOD(číslo, z_jednotky, na_jednotku)
     - „Příspěvek o funkci CONVERT na webu podpory Microsoftu <https://support.microsoft.com/en-us/office/convert-function-d785bef1-808e-4aac-bdcd-666c810f9af2>“

.._excel/funkce/statistické:

Statistické
===========

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * - AVEDEV(hodnota1, [hodnota2, ...])
     - „Funkce AVEDEV <https://support.microsoft.com/office/avedev-function-58fe8d65-2a84-4dc7-8052-f3f87b5c6639>“
   * -PRŮMĚR(hodnota1, [hodnota2, ...])
     - „Průměrný článek Excelu“ <https://support.microsoft.com/office/average-function-047bac88-d466-426c-a32b-8f33eb960cf6>
   * -PRŮMĚR(hodnota1, [hodnota2, ...])
     - „Průměrná hodnota v aplikaci Excel <https://support.microsoft.com/office/averagea-function-f5f84098-d453-4f4c-bbba-3d2c66356091>“
   * - Průměr podle kritéria (criteria_range, criterion, [average_range])
     - „Průměr funkce AVERAGEIF“ <https://support.microsoft.com/office/averageif-function-faec8e2e-0dec-4308-af69-f5576d8ac642>
   * -PRŮMĚRNÍ HODNOTA (průměrná hodnota, kritéria rozsahu 1, kritérium 1, [kritéria rozsahu 2, ...], [kritéria 2, ...])
     - „Článek o funkci AVERAGEIFS <https://support.microsoft.com/office/averageifs-function-48910c45-1fc0-4389-a028-f7c5c3001690>“
   * -PRŮMĚRNÁ HODNOTA (hodnoty, váhy, [další hodnoty, ...], [další váhy, ...])
     - Vážený průměr (součástí Excelu není).
   * - CORREL(data_y, data_x)
     - „Článek o funkci CORREL <https://support.microsoft.com/office/correl-function-995dcef7-0c0a-4bed-a3fb-239d7b68ca92>“
   * - POČET(hodnota1, [hodnota2, ...])
     - „Článek o funkci COUNT v Excelu <https://support.microsoft.com/office/count-function-a59cd7fc-b623-4d93-87a4-d23bf411294c>“
   * - COUNT(hodnota1,[hodnota2, ...])
     - „Funkce COUNT v článku o Excelu <https://support.microsoft.com/office/counta-function-7dc98875-d5c1-46f1-9a82-53f3219e2509>“
   * -COVAR(data_y, data_x)
     - „Článek o funkci COVAR na webu Microsoftu <https://support.microsoft.com/office/covar-function-50479552-2c03-4daf-bd71-a5ab88b2db03>“
   * -KOVARIANTA.P(data_y, data_x)
     - „Článek o funkci COVARIANCE.P <https://support.microsoft.com/office/covariance-p-function-6f0e1e6d-956d-4e4b-9943-cfef0bf9edfc>“
   * -KOVARIANTA.S(data_y, data_x)
     - „Článek o funkci COVARIANCE.S <https://support.microsoft.com/office/covariance-s-function-0a539b74-7371-42aa-a18f-1f5320314977>“
   * – PŘEDPOVĚĎ (x, y, x)
     - „Článek o předpovědi v Excelu <https://support.microsoft.com/office/forecast-and-forecast-linear-functions-50ca49c9-7b40-4892-94e4-7ad38bbeda99>“
   * - RŮST (známá data y, známá data x, nová data x, b)
     - Fit se shoduje s exponenciálními růstovými trendy (nekompatibilní s aplikací Excel)
   * - INTERCEPT(datum_y, datum_x)
     - „Článek o funkci INTERCEPT <https://support.microsoft.com/office/intercept-function-2a9b74e2-9d47-4772-b663-3bca70bf63ef>“
   * - VELKÉ(data, n)
     - „Funkce Excelu LARGE <https://support.microsoft.com/office/large-function-3af0af19-1190-42bb-bb8b-01672ec00a64>“
   * – LINEST(data_y, [data_x], [vypočítat_b], [podrobný])
     - „Článek o funkci LINEST <https://support.microsoft.com/office/linest-function-84d7d0d9-6e50-4101-977a-fa7abf772b6d>“
   * – LOGIST(data_y, [data_x], [vypočítat_b], [podrobné])
     - „Článek o funkci LOGEST v Excelu <https://support.microsoft.com/office/logest-function-f27462d8-3657-4030-866b-a272c1d18b4b>“
   * -MATTHEWS(data_x, data_y)
     - Vypočítejte korelační koeficient Matthewa pro datovou sadu (nekompatibilní s Excel)
   * -MAX(hodnota1, [hodnota2, ...])
     - „Maximální funkce článku Excel <https://support.microsoft.com/office/max-function-e0012414-9ac8-4b34-9a47-73e662c08098>“
   * - MAXA(hodnota1, [hodnota2, ...])
     - „Maximální hodnota funkce v článku o Excelu <https://support.microsoft.com/office/maxa-function-814bda1e-3840-4bff-9365-2f59ac2ee62d>“
   * -MAXIFS(rozsah, kritéria_rozsah1, kritérium1, [kritéria_rozsah2, ...], [kritérium2, ...])
     - „Maxifunkce v článku o funkci MAXIFS <https://support.microsoft.com/office/maxifs-function-dfd611e6-da2c-488a-919b-9b6376b28883>“
   * -MEDIAN(hodnota1, [hodnota2, ...])
     - „Článek o funkci MEDIAN na webu Excel <https://support.microsoft.com/office/median-function-d0916313-4753-414c-8537-ce85bdd967d2>“
   * - MIN(hodnota1, [hodnota2, ...])
     - „Minimální funkce“ (<https://support.microsoft.com/office/min-function-61635d12-920f-4ce2-a70f-96f202dcc152>).
   * - MINA (hodnota1, [hodnota2, ...])
     - „Článek o funkci MINA na webu Microsoftu <https://support.microsoft.com/office/mina-function-245a6f46-7ca5-4dc7-ab49-805341bc31d3>“
   * - MINIFS(rozsah, kritéria_rozsah1, kritérium1, [kritéria_rozsah2, ...], [kritérium2, ...])
     - „Článek o funkci MINIFS <https://support.microsoft.com/office/minifs-function-6ca1ddaa-079b-4e74-80cc-72eef32e6599>“
   * - PEARSON(datum_y, datum_x)
     - „Příspěvek PEARSON v Excelu <https://support.microsoft.com/office/pearson-function-0c3e30fc-e5af-49c4-808a-3ef66e034c18>“
   * -PERCENTILE(datum; procentil)
     - „Článek o funkci PERCENTILE v aplikaci Excel <https://support.microsoft.com/office/percentile-exc-function-bbaa7204-e9e1-4010-85bf-c31dc5dce4ba>“
   * -PERCENTILE.EXC(data, percentil)
     - „Excel PERCENTILE.EXC článek <https://support.microsoft.com/office/percentrank-exc-function-d8afee96-b7e2-4a2f-8c01-8fcdedaa6314>“
   * -PERCENTILE.INC(data, percentil)
     - „Článek o funkci PERCENTILE.INC <https://support.microsoft.com/office/percentile-inc-function-680f9539-45eb-410b-9a5e-c1355e5fe2ed>“
   * -POLYFIT.COEFFS(datum_y, datum_x, pořadí, [přerušení])
     - Vypočítejte koeficienty polynomické regrese datové sady (nekompatibilní s Excel)
   * -POLYFIT.FORECAST(x, data_y, data_x, řád, [přerušení])
     - Vypočtěte hodnotu předpovědi pomocí polynomické regrese datové sady (nekompatibilní s aplikací Excel).
   * -QUARTILE(data, číslo kvartilu)
     - „Článek o funkci QUARTILE na webu podpory Microsoftu <https://support.microsoft.com/office/quartile-function-93cf8f62-60cd-4fdb-8a92-8451041e1a2a>“
   * -QUARTILE.EXC(data, číslo kvartilu)
     - „Excel QUARTILE.EXC článek <https://support.microsoft.com/office/quartile-exc-function-5a355b7a-840b-4a01-b0f1-f538c2864cad>“
   * -QUARTILE.INC(data, číslo kvartilu)
     - „Článek o funkci QUARTILE.INC na webu Microsoftu <https://support.microsoft.com/office/quartile-inc-function-1bbacc80-5075-42f1-aed6-47d735c4819d>“
   * – RANK(hodnota, datum, [je_vzestupně]
     - „Funkce RANK v článku „<https://support.microsoft.com/office/rank-function-6a2fc49d-1831-4a03-9d8c-c279cf99f723>“
   * RSQ(data_y, data_x)
     - „Článek o funkci RSQ <https://support.microsoft.com/office/rsq-function-d7161715-250d-4a01-b80d-a8364f2be08f>“
   * - SLOPE(data_y, data_x)
     - „Článek o funkci SLOPE <https://support.microsoft.com/office/slope-function-11fb8f97-3117-4813-98aa-61d7e01276b9>“
   * - MALÉ (DATA, N)
     - „Malá funkce v Excelu“ <https://support.microsoft.com/office/small-function-17da8222-7c82-42b2-961b-14c45384df07>
   * -SPEARMAN(data_y, data_x)
     - Vypočítejte korelační koeficient Spearmana pro sadu dat (nekompatibilní se systémem Excel).
   * -STDEV(hodnota1,[hodnota2,...])
     - „Článek o funkci STDEV <https://support.microsoft.com/office/stdev-function-51fecaaa-231e-4bbb-9230-33650a72c9b0>“
   * -STDEVP(hodnota1, [hodnota2, ...])
     - „Excel STDEV.P článek <https://support.microsoft.com/office/stdev-p-function-6e917c05-31a0-496f-ade7-4f4e7462f285>“
   * -STD.V(hodnota1, [hodnota2, ...])
     - „Článek o funkci STDEV.S <https://support.microsoft.com/office/stdev-s-function-7d69cf97-0c1f-4acf-be27-f3e83904cc23>“
   * - STDEVA (hodnota1, [hodnota2, …])
     - „Článek o funkci STDEVA na webu podpory Microsoftu <https://support.microsoft.com/office/stdeva-function-5ff38888-7ea5-48de-9a6d-11ed73b29e9d>“
   * -STDEV(hodnota1, [hodnota2, ...])
     - „Článek o funkci STDEVP <https://support.microsoft.com/office/stdevp-function-1f7c1c88-1bec-4422-8242-e9f7dc8bb195>“
   * -STDEVPÁ(hodnota1, [hodnota2, …])
     - „Článek o funkci STDEVPA na webu Microsoftu <https://support.microsoft.com/office/stdevpa-function-5578d4d6-455a-4308-9991-d405afe2c28c>“
   * STEYX(datum_y, datum_x)
     - „Článek o funkci STEYX <https://support.microsoft.com/office/steyx-function-6ce74b2c-449d-4a6e-b9ac-f9cef5ba48ab>“
   * - TREND(známá data y, [známá data x], [nová data x], [b])
     - Fit ukazuje bodovou křivku, která je odvozena pomocí nejmenších čtverců (není kompatibilní s Excel).
   * - VAR(hodnota1, [hodnota2, ...])
     - „Příspěvek k funkci VAR <https://support.microsoft.com/office/var-function-1f2b7ab2-954d-4e17-ba2c-9e58b15a7da2>“
   * - VAR.P(hodnota1, [hodnota2, ...])
     - „Excel VAR.P funkce <https://support.microsoft.com/office/var-p-function-73d1285c-108c-4843-ba5d-a51f90656f3a>“
   * - VAR.S(hodnota1, [hodnota2, ...])
     - „Článek o funkci VAR.S na webu Microsoftu <https://support.microsoft.com/office/var-s-function-913633de-136b-449d-813e-65a00b2b990b>“
   * - VARA(hodnota1, [hodnota2, ...])
     - „Funkce VARA v článku na webu Microsoftu <https://support.microsoft.com/office/vara-function-3de77469-fa3a-47b4-85fd-81758a1e1d07>“
   * - VARP(value1, [value2, ...])
     - „Výukový článek o funkci VARP <https://support.microsoft.com/office/varp-function-26a541c4-ecee-464d-a731-bd4c575b1a6b>“
   * - VARPA(hodnota1, [hodnota2, ...])
     - „Článek o funkci VARPA na webu Microsoftu <https://support.microsoft.com/office/varpa-function-59a62635-4e89-4fad-88ac-ce4dc0513b96>“

..._spreadsheet/funkce/text:

Text
====

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * - CHAR(tabulka_číslo)
     - `Funkce CHAR v článku <https://support.microsoft.com/office/char-function-bbd249c8-b36e-4a91-8017-1c133f9b837a>“
   * -ČISTÉ (text)
     - „Článek o funkci CLEAN <https://support.microsoft.com/office/clean-function-26f3d7c5-475f-4a9c-90e5-4b8ba987ba41>“
   * - CONCATENATE(string1, [string2, ...])
     - `Excel CONCATENATE článek <https://support.microsoft.com/office/concatenate-function-8f8ae884-2ca8-4f7a-b093-75d702bea31d>`_
   * -EXACT(string1, string2)
     - „Exaktní funkce“ (<https://support.microsoft.com/office/exact-function-d3087698-fc15-4a15-9631-12575cf29926>).
   * -FIND(hledaný výraz, hledaný text, od)
     - „Excel - funkce FIND <https://support.microsoft.com/office/find-findb-functions-c7912941-af2a-4bdf-a553-d0d89b0a0628>“
   * - PŘIDAT (oddělovač, hodnota nebo pole1, [hodnota nebo pole2, ...])
     - Sloučí prvky polí s oddělovačem (není kompatibilní s Excel)
   * -LEFT(text, [počet znaků])
     - „Excel - funkce LEFT <https://support.microsoft.com/office/left-leftb-functions-9203d2d2-7960-479b-84c6-1ea52b99640c>“
   * -LEN(text)
     - „Excelová funkce LEN (<https://support.microsoft.com/office/len-lenb-functions-29236f94-cedc-429d-affd-b5e33d2c67cb>).“
   * - NÍŽE
     - `Funkce nižšího řádu v aplikaci Excel <https://support.microsoft.com/office/lower-function-3f21df02-a80c-44b2-afaf-81358f9fdeb4>`_
   * - MID(text, začátek, délka výstupu)
     - „Článek o funkci MID v Excelu <https://support.microsoft.com/office/mid-midb-functions-d5f9e25c-d7d6-472e-b568-4ecb12433028>“
   * -PROPER(text_k_započtení)
     - „Funkce Excelu „Proper“ <https://support.microsoft.com/office/proper-function-52a5a283-e8b2-49be-8506-b2887b889f94>“
   * - REPLACE(text, pozice, délka, nový_text)
     - „Excel REPLACE funkce <https://support.microsoft.com/office/replace-replaceb-functions-8d799074-2425-4a8a-84bc-82472868878a>“
   * – PRAVÉ (text, [počet znaků])
     - „Pravá funkce v Excelu <https://support.microsoft.com/office/right-rightb-functions-240267ee-9afa-4639-a02b-f19e1786cf2f>“
   * - HLEDAT(hledané slovo, hledaný text, od začátku)
     - „Excel Search Article <https://support.microsoft.com/office/search-searchb-functions-9ab04538-0e55-4719-a72e-b6f54513b495>“
   * - ROZDĚLIT (text, oddělovač, [rozdělit_každý], [odstranit_prázdné_texty])
     - „Článek o funkci TEXTSPLIT na webu podpory Microsoftu <https://support.microsoft.com/office/textsplit-function-b1ca414e-4c21-4ca0-b1b7-bdecace8a6e7>“
   * -SUBSTITUJ(hledaný_text, hledáno, nahradit, [počet_náhrad])
     - „Vzorec SUBSTITUTE“ <https://support.microsoft.com/office/substitute-function-6434944e-a904-4336-a9b0-1e58df3bc332>
   * -TEXT(číslo, formát)
     - „Excel - funkce TEXT <https://support.microsoft.com/office/text-function-20d5ac4d-7b94-49fd-bb38-93d29371225c>“
   * -TEXTJOIN(oddělovač, ignoruj prázdné, text1, [text2, …])
     - „Excel funkce TEXTJOIN <https://support.microsoft.com/office/textjoin-function-357b449a-ec91-49d0-80c3-0e8fc845691c>“
   * - TRIM(text)
     - „Článek o funkci TRIM <https://support.microsoft.com/office/trim-function-410388fa-c5df-49c6-b16c-9e5630b479f9>“
   * -UPPER(text)
     - „Funkce horního indexu <https://support.microsoft.com/office/upper-function-c11f29b3-d1a3-4537-8df6-04d0049963d6>“
   * - HODNOTA(text)
     - „Excelová funkce VALUE <https://support.microsoft.com/en-us/office/value-function-257d0108-07dc-437d-ae1c-bc2d3953d8c2>“

.. _tabulkový procesor/funkce/web:

Web
===

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * -HYPERLINK(url, [link_label])
     - „Excel HYPERLINK článek <https://support.microsoft.com/office/hyperlink-function-333c7ce6-c5ae-4164-9c47-7de9b76f577f>“

.. _spreadsheet/functions/odoo:

Funkce specifické pro Odoo
=======================

Tato část obsahuje funkce, které přímo komunikují s databází vašeho Odoo.

Array
-----

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * – VÝBĚR(vstupní rozsah, řádky, sloupce)
     - Vrací výsledný seznam omezený na konkrétní šířku a výšku (není kompatibilní s aplikací Excel).
   * – snížit (rozsah, [rozsah2, ...])
     - Všechny hodnoty z jedné nebo více rozsahů sloučí do jednoho sloupce (není kompatibilní s Excel)

Datum
----

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * - MĚSÍC.KONEC(datum)
     - Poslední den v měsíci následující po datu (není kompatibilní s Excel)
   * - MĚSÍC.ZAČÁTEK(datum)
     - První den v měsíci před datem (nekompatibilní s Excel)
   * -ČTVRTLETÍ (datum)
     - Čtvrtina roku, ve které spadá konkrétní datum (není kompatibilní s Excelem)
   * - ČTVRTLETÍ KONEC (datum)
     - Poslední den čtvrtletí je v daném roce konkrétním dnem (není kompatibilní s Excel)
   * -ČTVRTINA.ZAČÍTKOVAT(datum)
     - První den čtvrtletí v daném roce je specifický (není kompatibilní s Excel)
   * - KONEČNÉ DATUM
     - Poslední den v roce je specifický den (není kompatibilní s Excel)
   * - ROK.ZAČÁTEK(datum)
     - První den v roce je specifický datum (není kompatibilní s Excel)
   * - ROKFRAK (datum začátku, datum ukončení, [způsob počítání dnů])
     - Přesná délka mezi dvěma daty (není kompatibilní s Excel)

Finanční
---------

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * – ODOO.ACCOUNT.GROUP(typ)
     - Vrátí ID účtu skupiny (není kompatibilní s Excel)
   * - ODOO.KREDIT(účetní kódy, datový rozsah, [offest], [ID společnosti], [zahrnout nezaúčtované položky])
     - Získat celkový kredit na uvedených účtech a v daném období (není kompatibilní s Excel)
   * - ODOO.CURRENCY.RATE(měna_od, měna_do, [datum])
     - Tato funkce přijímá jako argumenty dva měnové kódy a vrací směnný kurz z první měny na druhou jako desetinné číslo (není kompatibilní s aplikací Excel).
   * - ODOO.DEBIT(účetní kódy, datový rozsah, [odstup], [ID společnosti], [zahrnout neevidované transakce])
     - Získat celkový zůstatek na účtu a období (nekompatibilní s aplikací Excel).
   * – ODOO.BALANCE (účetní kódy, datový rozsah, [offest], [ID firmy], [zahrnout nezaúčtované položky])
     - Získat součet zůstatku na účtu a období (není kompatibilní s aplikací Excel).
   * - ODOO.FISCALYEAR.START(den, [firma_id])
     - Vrací datum začátku fiskálního roku, který zahrnuje poskytnuté datum (není kompatibilní s aplikací Excel).
   * - ODOO.FISCALYEAR.END(den, [firma_id])
     - Vrací datum konce účetního období, které zahrnuje poskytnuté datum (není kompatibilní s Excel).
   * - ODOO.PARTNER.BALANCE(partner_ids, [account_codes], [date_range], [offset], [company_id], [include_unposted])
     - Získat vyváženost účtu pro zadané období a účty (není kompatibilní s Excel)
   * – ODOO.RESIDUAL([účetní kódy], [datový rozsah], [odstupňování], [identifikátor společnosti], [zahrnout nezaúčtované položky])
     - Získat zůstatek na konkrétním účtu a v daném období (není kompatibilní s Excel)

Překlad
------

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * -PIVOT (pivot_id, [řádků], [zahrnout celkový součet], [zahrnout nadpisy sloupců], [počet sloupců])
     - Vytvořte tabulku s otáčivými sloupci (nekompatibilní s Excelem)
   * - PIVOT.HEADER(pivot_id, [doménové pole jméno, ...], [doménový hodnota, ...])
     - Získat hlavičku tabulky s výsledky (není kompatibilní se softwarem Excel)
   * -PIVOT.VALUE(pivot_id, měřitelný název, pole doménového pole, doménová hodnota, ...)
     - Získat hodnotu z tabulky s agregací (nekompatibilní s Excel)

Matematika
----

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * - COUNTUNIQUE(hodnota1, [hodnota2, ...])
     - Počítá počet jedinečných hodnot v rozsahu (není kompatibilní s Excel)
   * -COUNTUNIQUEIFS(rozsah, kritéria_rozsah1, kritérium1, [kritéria_rozsah2, ...], [kritérium2, ...])
     - Počítá počet jedinečných hodnot v rozsahu, filtrovaných podle kritérií (není kompatibilní s Excel)

Miscellaneous
----

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * -FORMÁT.VELKÉ.ČÍSLO(hodnota, [jednotka])
     - Použijte velký formát čísla (není kompatibilní s Excel)
   * - ODOO.LIST(list_id, index, field_name)
     - Získat hodnotu ze seznamu (nekompatibilní s Excelem)
   * - ODOO.LIST.HEADER(list_id, pole_jméno)
     - Získat hlavičku seznamu (nekompatibilní s Excelem)

Operátoři
---------

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * - PŘIDAT(hodnota1, hodnota2)
     - Součet dvou čísel (nekompatibilní s Excel)
   * -DĚLENÍ (dividenda, děleno)
     - Jedna čísla dělená druhou (nekompatibilní s Excel)
   * - EQ (hodnota1, hodnota2)
     - Rovný (nekompatibilní s Excel)
   * – GT(hodnota1, hodnota2)
     - Strictně větší než (nekompatibilní s Excel)
   * - GTE (hodnota1, hodnota2)
     - Větší nebo rovno (není kompatibilní s Excel)
   * -LT(hodnota1, hodnota2)
     - Méně než (nekompatibilní s Excel)
   * - LTE(value1, value2)
     - Menší nebo rovno (nekompatibilní s Excel)
   * - MINUS(value1, value2)
     - Rozdíl dvou čísel (nekompatibilní s Excel)
   * -MULTIPLY(faktor1, faktor2)
     - Produkt dvou čísel (nekompatibilní s Excel)
   * - NE(hodnota1, hodnota2)
     - Není kompatibilní s Excel
   * - POW(základ, exponent)
     - Číslo vynásobené číslem (není kompatibilní s Excel)
   * -UMINUS(hodnota)
     - Číslo s obráceným znaménkem (není kompatibilní se softwarem Excel)
   * -UNÁRNÍ.PROCENTO(procento)
     - Hodnota vyjádřená procentem (není kompatibilní s Excel)
   * + (hodnota)
     - Uvedený počet, nezměněný (není kompatibilní s Excel)

Statistické
-----------

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * -PRŮMĚRNÁ HODNOTA (hodnoty, váhy, [další hodnoty, ...], [další váhy, ...])
     - Vážený průměr (součástí Excelu není).
   * - RŮST (známá data y, známá data x, nová data x, b)
     - Fit se shoduje s exponenciálními růstovými trendy (nekompatibilní s aplikací Excel)
   * -MATTHEWS(data_x, data_y)
     - Vypočítejte korelační koeficient Matthewa pro datovou sadu (nekompatibilní s Excel)
   * -POLYFIT.COEFFS(datum_y, datum_x, pořadí, [přerušení])
     - Vypočítejte koeficienty polynomické regrese datové sady (nekompatibilní s Excel)
   * -POLYFIT.FORECAST(x, data_y, data_x, řád, [přerušení])
     - Vypočtěte hodnotu předpovědi pomocí polynomické regrese datové sady (nekompatibilní s aplikací Excel).
   * -SPEARMAN(data_y, data_x)
     - Vypočítejte korelační koeficient Spearmana pro sadu dat (nekompatibilní se systémem Excel).
   * - TREND(známá data y, [známá data x], [nová data x], [b])
     - Fit ukazuje bodovou křivku, která je odvozena pomocí nejmenších čtverců (není kompatibilní s Excel).

Text
----

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1

   * – Jméno a argumenty
     - Popis nebo odkaz
   * - PŘIDAT (oddělovač, hodnota nebo pole1, [hodnota nebo pole2, ...])
     - Sloučí prvky polí s oddělovačem (není kompatibilní s Excel)
