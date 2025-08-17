(function ($) {

    document.addEventListener('DOMContentLoaded', () => {
        // Zapněte záložní URL pro nefunkční přesměrování z přepínače verze nebo jazyka.
        _prepareSwitchersFallbacks();
    });

    /**
     * Přidat posluchače událostí na odkazy v přepínači verze a jazyka.
     *
     * Pokud je odkaz kliknutý, uživatel je přesměrován na nejbližší záložní URL (včetně
     * URL původního cílového odkazu, pokud je k dispozici.
     */
    const _prepareSwitchersFallbacks = () => {
        document.querySelectorAll('a.o_switcher_item').forEach(element => {
            element.addEventListener('click', async event => {
                if (element.hasAttribute('href')) {
                    const targetUrl = element.getAttribute('href');
                    if (!targetUrl.startsWith('/')) {  // Pokud je v adrese localhost, nezkoušejte platné URL.
                        event.preventDefault();
                        const fallbackUrls = await _generateFallbackUrls(targetUrl);
                        const fallbackUrl = await _getFirstValidUrl(fallbackUrls) ?? targetUrl;
                        window.location.href = fallbackUrl;
                    }
                }
            });
        });
    };

})();
