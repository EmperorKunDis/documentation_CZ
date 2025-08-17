/* global_připravit-akordeon */ //see utils.js
(function ($) {

    document.addEventListener('DOMContentLoaded', () => {
        const navigationMenu = document.getElementById('o_main_toctree');

        // Povolit automatické skládání a rozkládání položek obsahu
        _prepareAccordion(navigationMenu);

        // Dovolit odpovídajícím způsobem zvýraznit a rozšířit vstupy do seznamu obsahu a jejich příslušné vstupy do seznamu obsahu
        // seznam, který je zobrazen na stránce.
        const deepestActiveTocEntries = _flagActiveTocEntriesAndLists(navigationMenu);

        // Rozbalte položky hlavního menu.
        _expandTopMenus(navigationMenu);

        // Zobrazit skrytý menu, pokud jsou správně definovány CSS třídy
        navigationMenu.removeAttribute('hidden');

        // Posouvejte nabídku na nejhlubší aktivní položku obsahu.
        _scrollToDeepestActiveTocEntry(deepestActiveTocEntries);
    });

    /**
     * Přidejte příslušné třídy na záhlaví stránek (a seznamy) zobrazených stránky.
     *
     * Vstupy TOC (element <li>) na cestě zobrazené stránky obdrží
     * třídě „o_active_toc_entry“ a jejich související (rodičské) seznamy položek obsahu (elementy <ul>)
     * třída show (Bootstrap). Dále také nejhlubší aktivní položky obsahu v dané větev
     * obdrží třídu o_deepest_active_toc_entry a jejich děti TOC vstupy do seznamu obdrží
     * Třída Show.
     *
     * @param {HTMLElement} navigační menu - Navigační menu.
     * @vrácení {Složený typ} – Nejhlubší aktivní záznamy v sekvenci.
     */
    const _flagActiveTocEntriesAndLists = navigationMenu => {
        const regexLayer = /\btoctree-l(?<layer>\d+)\b/;
        let lastLayer = undefined;
        let lastTocEntry = undefined;
        const deepestActiveTocEntries = [];
        navigationMenu.querySelectorAll('.current').forEach(element => {
            if (element.tagName === 'UL') {
                element.classList.add('show'); // Rozbalte všechny související seznamy.
            } else if (element.tagName === 'LI') {
                element.classList.add('o_active_toc_entry'); // Vyznačte všechny aktivní <li>.
                let match = regexLayer.exec(element.className);
                let currentLayer = parseInt(match.groups.layer, 10);
                if (lastLayer && currentLayer <= lastLayer) { // Seznamy jsou otevřené.
                    // Zaškrtněte poslední aktivní záznam v seznamu TOC jako nejhlubší větve před přesunem na
                    // další aktivní větev.
                    deepestActiveTocEntries.push(lastTocEntry);
                }
                lastLayer = currentLayer;
                lastTocEntry = element;
            }
        });
        if (lastTocEntry) {
            // Poslední aktivní vstup TOC je nejhlubším větvím.
            deepestActiveTocEntries.push(lastTocEntry);
        }
        deepestActiveTocEntries.forEach(deepestTocEntry => {
            const childTocEntryList = deepestTocEntry.querySelector('ul');
            if (childTocEntryList) {  // TOC vstup má spojený seznam TOC vstupů.
                childTocEntryList.classList.add('show');
            }
            deepestTocEntry.classList.add('o_deepest_active_toc_entry');
        });
        return deepestActiveTocEntries;
    };

    /**
     * Přidejte třídu show na hlavní menu.
     *
     * @param {HTMLElement} navigační menu - Navigační menu.
     */
    const _expandTopMenus = navigationMenu => {
        navigationMenu.querySelectorAll('.toctree-l1').forEach(tocEntry => {
            const childTocEntryList = tocEntry.querySelector('ul');
            if (childTocEntryList) {  // TOC vstup má spojený seznam TOC vstupů.
                childTocEntryList.classList.add('show'); // Rozbalte hlavní menu.
            }
        });
    };

    /**
     * Přejděte na aktivní záhlaví obsahu.
     *
     * Poznámka: tato metoda musí být volána po metodě _expandTopMenus a zobrazení menu.
     *
     * @param {Array} nejhlubší aktivní vstupy do obsahu - Nejhlubší aktivní vstupy do obsahu jejich příslušných
     *                                          pobočka.
     */
    const _scrollToDeepestActiveTocEntry = deepestActiveTocEntries => {
        if (deepestActiveTocEntries.length > 0) {
            deepestActiveTocEntries[0].scrollIntoView({block: 'center'});
        }
    };

     document.addEventListener('scroll', () => {
         // Povolit skrýt vyhledávací lištu při posouvání stránky na mobilním zařízení.
         _flagHeaderWithScrollPosition();
     });

    /**
     * Přidejte nebo odeberte třídu „o_header_scrolled“ podle pozice posunu.
     */
     const _flagHeaderWithScrollPosition = () => {
         const header = document.querySelector('.o_main_header');
         if (this.scrollY > 0) {
             header.classList.add('o_header_scrolled');
         } else {
             header.classList.remove('o_header_scrolled');
         }
     };

})();
