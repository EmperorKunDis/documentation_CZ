/* global_připravit-akordeon */ //see utils.js
(function ($) {

    // Upravte stránku obsahu.
    document.addEventListener('DOMContentLoaded', () => {
        // Smyčka na všechno obsah stránky. Může být od 0 do 2 v závislosti na stránce.
        document.querySelectorAll('.o_page_toc').forEach(pageToc => {
            const headingRefs = pageToc.querySelectorAll('a'); // Všechny odkazy na nadpisy.

            // Pokud stránka obsahuje méně než dvě nadpisy, skryjte ji úplně.
            if (headingRefs.length <= 2) {
                _hidePageToc(pageToc);
                return;
            }

            // Povolit automatické skládání a rozkládání položek obsahu
            _prepareAccordion(pageToc);

            // Zvýrazněte vstupy do obsahu, jejichž sekce je zaměřená a rozšířte seznam vstupů do obsahu.
            _flagActiveTocEntriesAndLists(pageToc, headingRefs);

            // Povolit skrýt záznam obsahu v sekci hlaviček (<H1>)
            _flagFirstHeadingRef(headingRefs);

            // Zobrazit skrytý menu, pokud jsou správně definovány CSS třídy
            pageToc.removeAttribute('hidden');
        });
    });

    /**
     * Zcela skrýt místní strom obsahu.
     *
     * @param {HTMLElement} pageToc - Strom obsahu stránky.
     */
    const _hidePageToc = pageToc => pageToc.style.display = 'none';

    /**
     * Přidejte příslušné třídy do záhlaví (a seznamů) odkazujících na část, která je zaměřená.
     *
     * Vstupy do sekce, které jsou soustředěné (element <li>) získají třídu „o_active_toc_entry“
     * a jejich související seznamy položek (elementy <ul>) získají třídu „show“ (Bootstrap).
     *
     * @param {HTMLElement} pageToc - Strom obsahu stránky.
     * @param {NodeList} headingRefs - Odkaz na všechny nadpisy.
     */
    const _flagActiveTocEntriesAndLists = (pageToc, headingRefs) => {

        const _updateFlags = () => {
            const activeHeadingRef = clickedHeadingRef || _findActiveHeadingRef();
            if (
                lastActiveHeadingRef // „nepřiděleno“ při prvním updatu
                && activeHeadingRef.href === lastActiveHeadingRef.href
            ) {
                return; // Zaměření se nezměnilo
            }
            _unflagAll();
            _flagActiveHierarchy(activeHeadingRef);
            // Uložit obchod, aby se později nemuselo aktualizovat, pokud se nezmění soustředění
            lastActiveHeadingRef = activeHeadingRef;
        };

        const _findActiveHeadingRef = () => {
            let activeHeadingRef = headingRefs[0];
            headingRefs.forEach(headingRef => {
                const href = headingRef.getAttribute('href');
                if (href !== '#') {
                    const sectionId = href.replace('#', '');
                    // DOM se vyhledává pomocí metody querySelector, nikoliv getElementById, protože
                    // Automaticky dokumentované moduly vytvářejí identifikátory obsahující tečku, což by mohlo způsobit
                    // Nedopadlo to dobře.
                    const section = document.querySelector(`section[id="${sectionId}"]`);
                    if (window.pageYOffset >= section.offsetTop) {
                        // Zaměřená část je poslední s menším odsazením od horního okraje než
                        // současný posun uživatele při procházení.
                        activeHeadingRef = headingRef;
                    } else {
                        return activeHeadingRef; // Přestávka
                    }
                }
            });
            return activeHeadingRef;
        };

        const _unflagAll = () => {
            pageToc.querySelectorAll('li,ul').forEach(element => {
                element.classList.remove('o_active_toc_entry', 'show');
            });
            pageToc.querySelectorAll('i').forEach(element => {
                element.setAttribute('aria-expanded', false);
            });
        };

        const _flagActiveHierarchy = (headingRef) => {
            let tocEntry = headingRef.parentElement;
            while (tocEntry !== pageToc) {
                if (tocEntry.tagName === 'LI') {
                    // Vyznačte všechny <li> v aktivní hierarchii
                    tocEntry.classList.add('o_active_toc_entry');

                    // Aktualizujte atributy tagu .
                    const tocEntryWrapper = tocEntry.querySelector('.o_toc_entry_wrapper');
                    if (tocEntryWrapper) {
                        tocEntryWrapper.querySelector('i').setAttribute('aria-expanded', true);
                    }

                    // Rozbalte všechny související seznamy.
                    const relatedTocEntryList = tocEntry.querySelector('ul');
                    if (relatedTocEntryList) {
                        relatedTocEntryList.classList.add('show');
                    }
                }
                tocEntry = tocEntry.parentElement;
            }
        };

        let clickedHeadingRef = undefined;
        pageToc.addEventListener('click', ev => {
            clickedHeadingRef = ev.target.closest('a[href^="#"]'); // Vyznačte odkaz, na který jste kliknuli.
        });
        let timeoutId = undefined;
        document.addEventListener('scroll', () => {
            clearTimeout(timeoutId); // Pro každou událost smyčky zrušte předchozí časovač.
            timeoutId = setTimeout(() => {
                clickedHeadingRef = undefined; // Návrat k zvýraznění nadpisu
            }, 100);
            _updateFlags();
        });

        let lastActiveHeadingRef = undefined; // Začněte s hodnotou „undefined“, abyste mohli provést první aktualizaci
        _updateFlags(); // Nejprve aktivujte sekce, které jsou v prvním skenu.
    };

    /**
     * Přidejte třídu o_page_toc_title na první odkaz na nadpis.
     *
     * @param {NodeList} headingRefs - Odkaz na všechny nadpisy.
     */
    const _flagFirstHeadingRef = headingRefs => {
        headingRefs[0].parentNode.classList.add('o_page_toc_title');
    }

})();
