=============
Opravy kódu
=============

Občas potřebujeme upravit způsob, jakým pracuje uživatelské rozhraní.
pokryté nějakou podporovanou API. Například všechny registry jsou dobré rozšíření
bodů: pole umožňuje přidávat a odstraňovat specializované komponenty pole.
nebo hlavní registr komponent umožňuje přidávat komponenty, které se mají zobrazit.
pořád.

V některých případech ale nestačí.
může potřebovat upravit objekt nebo třídu přímo na místě. K tomu slouží
poskytuje funkci „patch“. Je užitečná hlavně k přehrávání / aktualizaci
chování nějaké jiné složky/kusu kódu, který neovládáme.

Popis
===========

Funkce patch se nachází v adresáři @web/core/utils/patch:

.. funkce:patch(objekt k opravě, rozšíření)

:parametrem je objekt, který má být opraven
:param objekt extension: objekt, který každému klíči přiřazuje rozšíření
:vrací: funkci pro odstranění opravy

Funkce patch() upravuje v místě objekt objToPatch (nebo třídu).
aplikuje všechny klíč/hodnotu popsané v objektu extension.
Pokud se funkce vrátí, může být použita k odstranění opravy v případě potřeby.

Většina opravných operací poskytuje přístup k hodnotě rodičovské složky pomocí
původní klíčové slovo super (viz příklady níže).

Oprava jednoduchého objektu
========================

Tady je jednoduchý příklad, jakým způsobem se může objekt opravit:

... kódový blok: JavaScript

import { patch } z "@web/core/utils/patch";

const objekt = {
pole: „pole“,
fn() {
      // do something
    },
  };

patch(objekt, {
fn() {
      // do things
    },
  });


Při opravách funkcí chceme obvykle mít přístup k „rodiči“
Funkci lze jednoduše zavolat pomocí nativního klíčového slova „super“:

... kódový blok: JavaScript

patch(objekt, {
fn() {
super.fn(...argumenty);
      // do other things
    },
  });

.. varování:

„super“ lze použít jen v metodě, nikoli funkci. To znamená, že
Následující konstrukty jsou pro JavaScript neplatné.

... kódový blok :: JavaScript

const obj = {
a: funkce () {
          // Throws: "Uncaught SyntaxError: 'super' keyword unexpected here"
super.a();
        },
b: () => {
          // Throws: "Uncaught SyntaxError: 'super' keyword unexpected here"
super.b();
        },
      };

Podpora getterů a setterů je také součástí:

... kódový blok: JavaScript

patch(objekt, {
getNumber():
return super.number / 2;
      },
set číslo (hodnota) {
super.číslo = hodnota;
      },
    });

.. _frontend/patching_class:

Oprava třídy JavaScriptu
===========================

Funkce „patch“ je navržená tak, aby fungovala s jakýmkoliv objektem nebo třídou ES6.

Javascriptové třídy však pracují s prototypovým dědičením a
chceme opravit standardní metodu třídy, pak skutečně potřebujeme
prototyp:

... kódový blok: JavaScript

třída MyClass {
static myStaticFn() {...}
myPrototypeFn() {...}
  }

  // this will patch static properties!!!
patch(MyClass, {
static void myStaticFn() {...}
  });

  // this is probably the usual case: patching a class method
patch(MyClass.prototype, {
myPrototypeFn() {...}
  });


Dále JavaScript zpracovává konstruktor vlastním speciálním nativním způsobem, což dělá
nelze opravit. Jediným řešením je volání metody v původním
konstruktor a metodu místo toho přepíšete:

... kódový blok: JavaScript

třída MyClass {
constructor() {
tento.nastavit();
    }
setup() {
tento.číslo = 1;
    }
  }

patch(MyClass.prototype, {
setup() {
super.setup(...argumenty);
tento.dvojitýČíslo = tento.číslo * 2;
    },
  });

.. varování:

Nelze přímo opravit konstruktor třídy!

Oprava komponenty
====================

Komponenty jsou definovány pomocí javascriptových tříd, takže všechny informace výše stále
drží. Proto by komponenty Owl měly používat metodu setup, aby se
je také snadno opravitelný (viz část o „nejlepších postupech“).

... kódový blok: JavaScript

patch(MyComponent.prototype, {
setup() {
použijMůjHák();
    },
  });

Odstranění náplasti
================

Funkce patch vrací svůj protějšek. To je především užitečné pro
testovacích účelů, když na začátku testu něco opravíme.
Nechte ho nakonec neopravený.

... kódový blok: JavaScript

const neopravený = opravit (objekt, {...});
    // test stuff here
unpatch();

Použití stejného opravného náplasti na více objektů
===========================================

Může se stát, že chcete aplikovat stejný náplast na více objektů.
Protože se v jazyce „super“ používá klíčové slovo, může být použito pouze
jednou a nelze je kopírovat („podívejte se na dokumentaci klíčového slova <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#description>“).
Funkce, která vrací objekt použitý k opravě, může být použita k jeho jedinečnému označení.

... kódový blok: JavaScript

const obj1 = {
metoda() {
doSomething();
      },
    };

const obj2 = {
metoda() {
dovednostní věci();
      },
    };

funkce vytvoření objektu pro rozšíření
return {
metoda() {
super.metoda();
doObecnýchVeci();
        },
      };
    }

patch(obj1, vytvořit rozšíření objektu);
patch(obj2, vytvořit rozšíření objektu);

.. varování:

Pokud je „rozšíření“ založeno na jiném, pak by měly být obě rozšíření
je možné aplikovat samostatně. Nesnažte se kopírovat nebo klonovat rozšíření.

...... kódový blok:: javascript

const objekt = {
metoda1() {
doSomething();
        },
method2() {
jinouSekvenci();
        },
      };

const ext1 = {
metoda1() {
super.metoda1();
doThings();
        },
      };

const invalid_ext2 = {
...ext1, // toto nebude fungovat: super se bude v metodách z ext1 odkazovat na špatný objekt
method2() {
super.metoda2();
jinak();
        },
      };

patch(objekt, neplatný_ext2);
objekt.metoda1(); // vyvolává chybu: Neočekávaný typ: (přechodná hodnota).metoda1 není funkcí

const valid_ext2 = {
method2() {
super.metoda2();
jinak();
        },
      };

patch(objekt, ext1); // první patch základní rozšíření
patch(objekt, valid_ext2); // pak nový
metoda1(objekt); // funguje, jak by měla
