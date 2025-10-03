// i18n.js - Internationalization System for TidiFul
class I18n {
    constructor() {
        this.currentLanguage = this.detectLanguage();
        this.translations = {};
        // Don't load translations in constructor - wait for DOM
    }

    // Detect user's preferred language
    detectLanguage() {
        // Check URL parameter first
        const urlParams = new URLSearchParams(window.location.search);
        const urlLang = urlParams.get('lang');
        if (urlLang && this.isValidLanguage(urlLang)) {
            return urlLang;
        }

        // Check localStorage
        const storedLang = localStorage.getItem('tidiful-language');
        if (storedLang && this.isValidLanguage(storedLang)) {
            return storedLang;
        }

        // Check browser language
        const browserLang = navigator.language || navigator.userLanguage;
        const langCode = browserLang.split('-')[0];
        
        // Map browser language to supported languages
        const languageMap = {
            'en': 'en-US',
            'fr': 'fr-FR', 
            'de': 'de-DE',
            'es': 'es-ES',
            'el': 'el-GR'
        };

        return languageMap[langCode] || 'en-US';
    }

    // Validate if language is supported
    isValidLanguage(lang) {
        const supportedLanguages = ['en-US', 'fr-FR', 'de-DE', 'es-ES', 'el-GR'];
        return supportedLanguages.includes(lang);
    }

    // Load translation files
    async loadTranslations() {
        try {
            const response = await fetch(`assets/i18n/${this.currentLanguage}.json`);
            if (response.ok) {
                this.translations = await response.json();
                this.applyTranslations();
            } else {
                console.warn(`Translation file not found for ${this.currentLanguage}, falling back to English`);
                await this.loadFallbackTranslations();
            }
        } catch (error) {
            console.error('Error loading translations:', error);
            await this.loadFallbackTranslations();
        }
    }

    // Load English as fallback
    async loadFallbackTranslations() {
        try {
            const response = await fetch('assets/i18n/en-US.json');
            this.translations = await response.json();
            this.currentLanguage = 'en-US';
            this.applyTranslations();
        } catch (error) {
            console.error('Error loading fallback translations:', error);
        }
    }

    // Apply translations to the page
    applyTranslations() {
        // Update document language
        document.documentElement.lang = this.currentLanguage;

                // Translate elements with data-i18n attribute
                document.querySelectorAll('[data-i18n]').forEach(element => {
                    const key = element.getAttribute('data-i18n');
                    const translation = this.getTranslation(key);
                    if (translation) {
                        if (element.tagName === 'INPUT' && element.type === 'text') {
                            element.placeholder = translation;
                        } else if (element.tagName === 'TITLE') {
                            element.textContent = translation;
                        } else {
                            element.textContent = translation;
                        }
                    }
                });

                // Translate placeholder attributes
                document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
                    const key = element.getAttribute('data-i18n-placeholder');
                    const translation = this.getTranslation(key);
                    if (translation) {
                        element.placeholder = translation;
                    }
                });

        // Translate elements with data-i18n-html attribute (for HTML content)
        document.querySelectorAll('[data-i18n-html]').forEach(element => {
            const key = element.getAttribute('data-i18n-html');
            const translation = this.getTranslation(key);
            if (translation) {
                element.innerHTML = translation;
            }
        });

        // Update meta tags
        this.updateMetaTags();

        // Update language switcher
        this.updateLanguageSwitcher();
    }

    // Get translation by key
    getTranslation(key) {
        const keys = key.split('.');
        let translation = this.translations;
        
        for (const k of keys) {
            if (translation && typeof translation === 'object' && k in translation) {
                translation = translation[k];
            } else {
                console.warn(`Translation key not found: ${key}`);
                return key; // Return key as fallback
            }
        }
        
        return translation;
    }

    // Update meta tags for SEO
    updateMetaTags() {
        const title = this.getTranslation('meta.title');
        const description = this.getTranslation('meta.description');
        const keywords = this.getTranslation('meta.keywords');

        if (title) {
            document.title = title;
            document.querySelector('meta[property="og:title"]')?.setAttribute('content', title);
            document.querySelector('meta[name="twitter:title"]')?.setAttribute('content', title);
        }

        if (description) {
            document.querySelector('meta[name="description"]')?.setAttribute('content', description);
            document.querySelector('meta[property="og:description"]')?.setAttribute('content', description);
            document.querySelector('meta[name="twitter:description"]')?.setAttribute('content', description);
        }

        if (keywords) {
            document.querySelector('meta[name="keywords"]')?.setAttribute('content', keywords);
        }

        // Update hreflang tags
        this.updateHreflangTags();
    }

    // Update hreflang tags for multilingual SEO
    updateHreflangTags() {
        const currentUrl = window.location.href.split('?')[0]; // Remove existing params
        const supportedLanguages = this.getSupportedLanguages();
        
        // Remove existing hreflang tags
        document.querySelectorAll('link[hreflang]').forEach(link => link.remove());
        
        // Add hreflang tags for each language
        supportedLanguages.forEach(lang => {
            const hreflangLink = document.createElement('link');
            hreflangLink.rel = 'alternate';
            hreflangLink.hreflang = lang.code;
            hreflangLink.href = `${currentUrl}?lang=${lang.code}`;
            document.head.appendChild(hreflangLink);
        });
        
        // Add x-default hreflang
        const defaultLink = document.createElement('link');
        defaultLink.rel = 'alternate';
        defaultLink.hreflang = 'x-default';
        defaultLink.href = currentUrl;
        document.head.appendChild(defaultLink);
    }

    // Update language switcher
    updateLanguageSwitcher() {
        const switcher = document.getElementById('language-switcher');
        if (switcher) {
            const currentLang = this.currentLanguage;
            switcher.value = currentLang;
        }
    }

    // Change language
    async changeLanguage(newLang) {
        if (!this.isValidLanguage(newLang)) {
            console.error(`Unsupported language: ${newLang}`);
            return;
        }

        this.currentLanguage = newLang;
        localStorage.setItem('tidiful-language', newLang);
        
        // Update URL without reload
        const url = new URL(window.location);
        url.searchParams.set('lang', newLang);
        window.history.replaceState({}, '', url);

        await this.loadTranslations();
        // Apply translations after loading
        this.applyTranslations();
    }

    // Get current language
    getCurrentLanguage() {
        return this.currentLanguage;
    }

    // Get supported languages
    getSupportedLanguages() {
        return [
            { code: 'en-US', name: 'English', flag: '🇺🇸' },
            { code: 'fr-FR', name: 'Français', flag: '🇫🇷' },
            { code: 'de-DE', name: 'Deutsch', flag: '🇩🇪' },
            { code: 'es-ES', name: 'Español', flag: '🇪🇸' },
            { code: 'el-GR', name: 'Ελληνικά', flag: '🇬🇷' }
        ];
    }
}

// Initialize i18n when DOM is loaded
document.addEventListener('DOMContentLoaded', async function() {
    window.i18n = new I18n();
    
    // Load translations and apply them
    await window.i18n.loadTranslations();
    
    // Add language switcher event listener
    const switcher = document.getElementById('language-switcher');
    if (switcher) {
        switcher.addEventListener('change', function() {
            window.i18n.changeLanguage(this.value);
        });
    }
});
