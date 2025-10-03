// Header Component for TidiFul Website
class HeaderComponent {
    constructor() {
        this.headerHTML = `
            <nav class="border-b border-gray-700 bg-gray-900 backdrop-blur-sm">
                <div class="container mx-auto px-4 py-4">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-2">
                            <img src="{{LOGO_PATH}}" alt="TidiFul" class="w-8 h-8">
                            <span class="text-xl font-bold text-gray-100">TidiFul</span>
                        </div>
                        <div class="hidden md:flex items-center space-x-8">
                            <a href="{{HOME_PATH}}" class="text-gray-300 hover:text-emerald-400 transition-colors">Home</a>
                            <a href="#" class="text-gray-300 hover:text-emerald-400 transition-colors">Features</a>
                            <a href="{{PRICING_PATH}}" class="text-gray-300 hover:text-emerald-400 transition-colors">Pricing</a>
                            <a href="{{BLOG_PATH}}" class="{{BLOG_ACTIVE}}">Blog</a>
                            <a href="#" class="text-gray-300 hover:text-emerald-400 transition-colors">Contact</a>
                        </div>
                        <div class="flex items-center space-x-4">
                            <select id="language-switcher" class="bg-gray-800 text-gray-300 border border-gray-700 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500">
                                <option value="en-US">🇺🇸 English</option>
                                <option value="fr-FR">🇫🇷 Français</option>
                                <option value="de-DE">🇩🇪 Deutsch</option>
                                <option value="es-ES">🇪🇸 Español</option>
                                <option value="el-GR">🇬🇷 Ελληνικά</option>
                            </select>
                            <a href="{{LOGIN_PATH}}" class="px-4 py-2 rounded-lg border border-emerald-500 text-emerald-400 hover:bg-emerald-900 transition-colors">
                                Create Account / Login
                            </a>
                        </div>
                    </div>
                </div>
            </nav>
        `;
    }

    // Generate header HTML based on current page context
    generateHeader(currentPage = 'home') {
        const paths = this.getPaths(currentPage);
        let html = this.headerHTML;

        // Replace placeholders
        html = html.replace('{{LOGO_PATH}}', paths.logoPath);
        html = html.replace('{{HOME_PATH}}', paths.homePath);
        html = html.replace('{{PRICING_PATH}}', paths.pricingPath);
        html = html.replace('{{BLOG_PATH}}', paths.blogPath);
        html = html.replace('{{LOGIN_PATH}}', paths.loginPath);
        html = html.replace('{{BLOG_ACTIVE}}', currentPage === 'blog' ? 'text-emerald-400 font-medium' : 'text-gray-300 hover:text-emerald-400 transition-colors');

        return html;
    }

    // Get relative paths based on current page depth
    getPaths(currentPage) {
        const depth = this.getCurrentDepth();
        
        return {
            logoPath: `${depth}assets/images/leaf_png_128x128.png`,
            homePath: `${depth}index.html`,
            pricingPath: `${depth}pricing.html`,
            blogPath: `${depth}blog/blogs.html`,
            loginPath: `${depth}login.html`
        };
    }

    // Determine current page depth based on URL
    getCurrentDepth() {
        const path = window.location.pathname;
        if (path.includes('/blog/posts/')) {
            return '../../';
        } else if (path.includes('/blog/')) {
            return '../';
        } else {
            return '';
        }
    }

    // Insert header into page
    insertHeader(selector = '#header-container') {
        const container = document.querySelector(selector);
        if (container) {
            const currentPage = this.getCurrentPageType();
            container.innerHTML = this.generateHeader(currentPage);
            this.initializeComponents();
        }
    }

    // Determine current page type
    getCurrentPageType() {
        const path = window.location.pathname;
        if (path.includes('blogs.html') || path.includes('blog') && path.includes('.html')) {
            return 'blog';
        }
        return 'home';
    }

    // Initialize interactive components
    initializeComponents() {
        // Initialize language switcher
        const existingI18n = window.i18n;
        if (existingI18n) {
            existingI18n.updateLanguageSwitcher();
            const switcher = document.getElementById('language-switcher');
            if (switcher && !switcher.hasAttribute('data-initialized')) {
                switcher.setAttribute('data-initialized', 'true');
                switcher.addEventListener('change', function() {
                    existingI18n.changeLanguage(this.value);
                });
            }
        }
    }
}

// Auto-initialize if DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    if (window.location.search.includes('auto-header=true')) {
        const headerComponent = new HeaderComponent();
        headerComponent.insertHeader();
    }
});

// Export for manual use
window.HeaderComponent = HeaderComponent;
