let tocEntryListId = 0; // Slouží k generování identifikátorů seznamu vstupů pro oba seznamy obsahu - pro menu a stránku.

/**
 * Aktualizujte poskytnutý seznam obsahu, aby bylo možné skládat jeho položky pomocí Bootstrapu.
 *
 * Typická struktura nabídky TOC je následující:
 * 
 *     
 *         <a name="nadpis_bez_deti" href="něco.html">Něco</a>.
 *     </li>
 *     
 *         <a name="neaktivní nadpis s dětskými odkazy" href="#">Něco</a>
 *         <ul>...</ul>
 *     </li>
 *     
 *         <a name="klikací nadpis s dětskými odkazy" href="něco.html">Něco</a>
 *         <ul>...</ul>
 *     </li>
 * 
 *
 * Od <ul> je vždy předcházeno <a>, takže změna se týká pouze <a>.
 * pokud následuje element <ul>, jednoduše se vracíme na všechny prvky DOM.
 * které je třeba upravit.
 *
 * Konečná struktura by měla vypadat takto:
 * 
 *     <!--Unchanged-->
 *     
 *         <a name="nadpis_bez_deti" href="něco.html">Něco</a>.
 *     </li>
 *     Vytvořte div. Přidejte i a a nastavte cíl na a a i. Nastavte id pro ul.
 *     
 *         
 *             <i class="i-chevron-right" data-bs-target="#o_target_123" data-bs-toggle="collapse"/>
 *             <a name="neaktivní nadpis s dětskými položkami" href="#" data-bs-target="#o_target_123>" data-bs-toggle="collapse">Něco</a>
 *         </div>
 *         <ul id="o_target_123" class="collapse">...</ul>
 *     </li>
 *     Vytvořte div. Přidejte i a a. Nastavte cíl BS pouze na i, aby se odkaz přesměroval. Nastavte ID pro ul.
 *     
 *         
 *             <i class="i-chevron-right" data-bs-target="#o_target_456" data-bs-toggle="collapse"/>
 *             <a name="klikací nadpis s dětskými odkazy" href="něco.html">Něco</a>
 *         </div>
 *         <ul id="o_target_456" class="collapse">...</ul>
 *     </li>
 *
 *
 * @param {HTMLElement} tocElement - Element obsahující seznam obsahu.
 */
const _prepareAccordion = (tocElement) => {
    // Začněte na druhé seznamu položek obsahu (<ul>), abyste zabránili zhroucení celého obsahu.
    const tocRoot = tocElement.querySelector('ul');
    tocRoot.querySelectorAll('ul').forEach(tocEntryList => {
        // Upravte tag <ul>.
        tocEntryList.id = `o_target_${tocEntryListId++}`;
        tocEntryList.classList.add('collapse');

        // Pokud se v tagu a nevyskytuje žádný odkaz, pak jej upravte, jinak dojde k přesměrování.
        const relatedHeadingRef = tocEntryList.previousSibling;
        if (relatedHeadingRef.getAttribute('href') === '#') {
            relatedHeadingRef.setAttribute('data-bs-target', `#${tocEntryList.id}`);
            relatedHeadingRef.setAttribute('data-bs-toggle', 'collapse');
        }

        // Vytvořte a nakonfigurujte prvek <div>.
        const tocEntryWrapper = document.createElement('DIV');
        tocEntryWrapper.classList.add('o_toc_entry_wrapper');
        tocEntryList.parentElement.insertBefore(tocEntryWrapper, tocEntryList);

        // Vytvořte a nakonfigurujte prvek .
        const arrowButton = document.createElement('I');
        arrowButton.setAttribute('data-bs-target', `#${tocEntryList.id}`);
        arrowButton.setAttribute('data-bs-toggle', 'collapse');
        arrowButton.classList.add('i-chevron-right');

        // Vložte prvky <i> a <a> do elementu <div>.
        tocEntryWrapper.append(arrowButton, relatedHeadingRef);
    });
};

/**
 * Vytvořte seznam náhradních adres URL od nejbližší po nejvzdálenější cílové URL.
 * vrátit první, který odkazuje na existující zdroj.
 *
 * Generace začíná od cílové adresy a chodí zpět k kořenovému adresáři
 * dokumentace se střídá mezi tím, že zahrnuje původní jazyk nebo ne, pokud je
 * zahrnuté v původním URL. Poslední záložní URL je kořen dokumentace s
 * verze bez obsahu, která odkazuje uživatele na index verze výchozí.
 *
 * Příklad:
 * 1. .../dokumentace/13.0/přispívání/dokumentace.html
 * 2. .../dokumentace/13.0/přispívání.html
 * 3. .../dokumentace/13.0
 * 4. .../dokumentace/
 *
 * Příklad:
 * 1. .../dokumentace/15.0/cs/správa/instalace.html
 * 2. .../dokumentace/15.0/správa/instalace.html
 * 3. .../dokumentace/15.0/cs/administrace.html
 * 4.../dokumentace/15.0/administrace.html
 * 5. .../dokumentace/15.0/cs/
 * 6. .../dokumentace/15.0/
 * 7. .../dokumentace/
 */
const _generateFallbackUrls = async (targetUrl) => {

    const _deconstructUrl = (urlObject) => {
        let urlBase = urlObject.origin;
        let version = '';
        let language = '';
        const originalPathParts = [];
        for (let fragment of urlObject.pathname.split('/').reverse()) {
            if (fragment.length > 0) {
                if (fragment.match(/^(?:saas-)?\d{2}\.\d$|^master$/)) {
                    // Pokuste se najít verzi, která odpovídá předchozí části cesty.
                    version = fragment;
                } else if (fragment.match(/^[a-z]{2}(?:_[A-Z]{2})?$/)) {
                    // Snažte se shodovat jazyk před zvážením části cesty.
                    language = fragment;
                } else if (version || language) {
                    // Tento fragment je součástí základní adresy URL, ale již není její součástí.
                    urlBase += `/${fragment}`;
                } else {
                    // Tento úsek je součástí původní trasy.
                    originalPathParts.unshift(fragment);
                }
            }
        }
        return [urlBase, version, language, originalPathParts];
    };

    const targetUrlObject = new URL(targetUrl);
    const [urlBase, version, language, originalPathParts] = _deconstructUrl(targetUrlObject);

    // Vytvořte záložní URL adresy.
    const fallbackUrls = [targetUrl]; // Začněte s původním URL, pokud ho přestavíme špatně.
    for (let i = originalPathParts.length; i >= 0; i--) {
        const fallbackPathParts = originalPathParts.slice(0, i);

        // Pokud chybí přípona .html, přidejte ji na konec poslední části cesty a pokud se nejedná o kořenovou složku.
        if (
            fallbackPathParts.length > 0
            && !fallbackPathParts[fallbackPathParts.length - 1].endsWith('.html')
        ) {
            fallbackPathParts[fallbackPathParts.length - 1] += '.html';
        }

        // Vytvořte záložní adresu URL z částí verze, jazyka a cesty.
        if (version && language) {
            fallbackUrls.push(
                `${urlBase}/${version}/${language}/${fallbackPathParts.join('/')}`,
                `${urlBase}/${version}/${fallbackPathParts.join('/')}`,
            );
        } else if (version && !language) {
            fallbackUrls.push(`${urlBase}/${version}/${fallbackPathParts.join('/')}`);
        } else if (!version && language) {
            fallbackUrls.push(
                `${urlBase}/${language}/${fallbackPathParts.join('/')}`,
                `${urlBase}/${fallbackPathParts.join('/')}`,
            );
        } else if (!version && !language) {
            fallbackUrls.push(`${urlBase}/${fallbackPathParts.join('/')}`);
        }
    }
    fallbackUrls.push(`${urlBase}/`);
    return fallbackUrls;
};

/**
 * Projděte seznam URL a vraťte první odkazující na platný zdroj, pokud existuje.
 *
 * URL nemá protokol, takže se nedají stáhnout při sestavování dokumentace lokálně
 * bez příkazů „CORE“ a „JE-LI VZDÁLENÝ BUDOVY“, URL adresy bez protokolu
 * Není testováno, zda je v adrese uvedeno „http“ nebo „https“.
 */
const _getFirstValidUrl = async (urls) => {
    for (let url of urls) {
        if (url.startsWith('http')) {
            const response = await fetch(url);
            if (response.ok) {
                return url;
            }
        }
    }
    return null; // Nenalezeno platný odkaz.
};
