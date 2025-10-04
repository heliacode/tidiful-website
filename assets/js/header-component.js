// Header Component for TidiFul Website
class HeaderComponent {
    constructor() {
        this.headerHTML = `
            <nav class="border-b border-gray-700 bg-gray-900 backdrop-blur-sm">
                <div class="container mx-auto px-4 py-4">
                    <div class="flex items-center justify-between">
                        <a href="{{HOME_PATH}}" class="flex items-center space-x-2 hover:opacity-80 transition-opacity">
                            <img src="{{LOGO_PATH}}" alt="TidiFul" class="h-8 w-auto">
                            <span class="text-xl font-bold text-gray-100">TidiFul</span>
                        </a>
                        
                        <!-- Desktop Navigation -->
                        <div class="hidden lg:flex items-center space-x-8">
                            <a href="{{HOME_PATH}}" class="text-gray-300 hover:text-emerald-400 transition-colors">Home</a>
                            <a href="#" class="text-gray-300 hover:text-emerald-400 transition-colors">Features</a>
                            <a href="{{PRICING_PATH}}" class="text-gray-300 hover:text-emerald-400 transition-colors">Pricing</a>
                            <a href="{{BLOG_PATH}}" class="{{BLOG_ACTIVE}}">Blog</a>
                            <a href="{{ABOUT_PATH}}" class="text-gray-300 hover:text-emerald-400 transition-colors">About</a>
                            <a href="#" class="text-gray-300 hover:text-emerald-400 transition-colors">Contact</a>
                        </div>
                        
                        <!-- Desktop Actions -->
                        <div class="hidden lg:flex items-center space-x-4">
                            <select id="language-switcher" class="bg-gray-800 text-gray-300 border border-gray-700 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500">
                                <option value="en-US">🇺🇸 English</option>
                                <option value="fr-FR">🇫🇷 Français</option>
                                <option value="de-DE">🇩🇪 Deutsch</option>
                                <option value="es-ES">🇪🇸 Español</option>
                                <option value="el-GR">🇬🇷 Ελληνικά</option>
                            </select>
                                <a href="{{LOGIN_PATH}}" class="px-4 py-2 rounded-lg border border-emerald-500 text-emerald-400 hover:bg-emerald-900 transition-colors" data-i18n="nav.createAccountLogin">
                                    Create Account / Login
                                </a>
                        </div>
                        
                        <!-- Mobile Menu Button -->
                        <button id="mobile-menu-button" class="lg:hidden p-2 rounded-lg text-gray-300 hover:text-emerald-400 hover:bg-gray-800 transition-colors">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                            </svg>
                        </button>
                    </div>
                </div>
            </nav>
            
            <!-- Mobile Menu Overlay - Compact height -->
            <div id="mobile-menu" class="lg:hidden hidden fixed inset-x-0 top-0 z-50 bg-gray-800 border-b border-gray-600">
                <div class="flex flex-col w-full">
                    <!-- Mobile Menu Header -->
                    <div class="flex items-center justify-between p-4 border-b border-gray-700">
                        <a href="{{HOME_PATH}}" class="flex items-center space-x-2 hover:opacity-80 transition-opacity">
                            <img src="{{LOGO_PATH}}" alt="TidiFul" class="h-8 w-auto">
                            <span class="text-xl font-bold text-gray-100">TidiFul</span>
                        </a>
                        <button id="mobile-menu-close" class="p-2 rounded-lg text-gray-300 hover:text-emerald-400 hover:bg-gray-800 transition-colors">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                            </svg>
                        </button>
                    </div>
                    
                    <!-- Mobile Navigation Links -->
                    <div class="px-4 py-2">
                        <nav class="space-y-2">
                            <a href="{{HOME_PATH}}" class="block px-4 py-2 text-lg text-gray-300 hover:text-emerald-400 hover:bg-gray-800 rounded-lg transition-colors">Home</a>
                            <a href="#" class="block px-4 py-2 text-lg text-gray-300 hover:text-emerald-400 hover:bg-gray-800 rounded-lg transition-colors">Features</a>
                            <a href="{{PRICING_PATH}}" class="block px-4 py-2 text-lg text-gray-300 hover:text-emerald-400 hover:bg-gray-800 rounded-lg transition-colors">Pricing</a>
                            <a href="{{BLOG_PATH}}" class="block px-4 py-2 text-lg {{BLOG_ACTIVE_MOBILE}} hover:bg-gray-800 rounded-lg transition-colors">Blog</a>
                            <a href="{{ABOUT_PATH}}" class="block px-4 py-2 text-lg text-gray-300 hover:text-emerald-400 hover:bg-gray-800 rounded-lg transition-colors">About</a>
                            <a href="#" class="block px-4 py-2 text-lg text-gray-300 hover:text-emerald-400 hover:bg-gray-800 rounded-lg transition-colors">Contact</a>
                        </nav>
                    </div>
                    
                    <!-- Mobile Actions -->
                    <div class="px-4 py-2 border-t border-gray-700 space-y-2">
                        <select id="mobile-language-switcher" class="w-full bg-gray-800 text-gray-300 border border-gray-700 rounded-lg px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500">
                            <option value="en-US">🇺🇸 English</option>
                            <option value="fr-FR">🇫🇷 Français</option>
                            <option value="de-DE">🇩🇪 Deutsch</option>
                            <option value="es-ES">🇪🇸 Español</option>
                            <option value="el-GR">🇬🇷 Ελληνικά</option>
                        </select>
                            <a href="{{LOGIN_PATH}}" class="block w-full text-center px-4 py-2 rounded-lg border border-emerald-500 text-emerald-400 hover:bg-emerald-900 transition-colors" data-i18n="nav.createAccountLogin">
                                Create Account / Login
                            </a>
                    </div>
                </div>
            </div>
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
        html = html.replace('{{ABOUT_PATH}}', paths.aboutPath);
        html = html.replace('{{LOGIN_PATH}}', paths.loginPath);
        html = html.replace('{{BLOG_ACTIVE}}', currentPage === 'blog' ? 'text-emerald-400 font-medium' : 'text-gray-300 hover:text-emerald-400 transition-colors');
        html = html.replace('{{BLOG_ACTIVE_MOBILE}}', currentPage === 'blog' ? 'text-emerald-400 font-medium' : 'text-gray-300 hover:text-emerald-400');

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
            aboutPath: `${depth}about.html`,
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
            
            // Initialize mobile language switcher
            const mobileSwitcher = document.getElementById('mobile-language-switcher');
            if (mobileSwitcher && !mobileSwitcher.hasAttribute('data-initialized')) {
                mobileSwitcher.setAttribute('data-initialized', 'true');
                mobileSwitcher.addEventListener('change', function() {
                    existingI18n.changeLanguage(this.value);
                });
            }
        }
        
        // Initialize mobile menu
        this.initializeMobileMenu();
    }
    
    // Initialize mobile menu functionality
    initializeMobileMenu() {
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        const mobileMenu = document.getElementById('mobile-menu');
        const mobileMenuClose = document.getElementById('mobile-menu-close');
        
        if (mobileMenuButton && mobileMenu && mobileMenuClose) {
            // Open mobile menu
            mobileMenuButton.addEventListener('click', () => {
                mobileMenu.classList.remove('hidden');
                document.body.style.overflow = 'hidden'; // Prevent background scrolling
            });
            
            // Close mobile menu
            const closeMenu = () => {
                mobileMenu.classList.add('hidden');
                document.body.style.overflow = ''; // Restore scrolling
            };
            
            mobileMenuClose.addEventListener('click', closeMenu);
            
            // Close menu when clicking on overlay
            mobileMenu.addEventListener('click', (e) => {
                if (e.target === mobileMenu) {
                    closeMenu();
                }
            });
            
            // Close menu when pressing Escape key
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && !mobileMenu.classList.contains('hidden')) {
                    closeMenu();
                }
            });
            
            // Close menu when clicking on navigation links
            const mobileNavLinks = mobileMenu.querySelectorAll('nav a');
            mobileNavLinks.forEach(link => {
                link.addEventListener('click', closeMenu);
            });
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
