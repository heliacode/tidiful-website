#!/usr/bin/env python3
"""
Quick Blog Post Creator
Creates a new blog post template and runs automation
"""

import os
import sys
from datetime import datetime
from pathlib import Path

def create_blog_post():
    """Create a new blog post template"""
    
    if len(sys.argv) < 2:
        print("Usage: python create_blog_post.py 'Post Title'")
        print("Example: python create_blog_post.py 'How to Use AI for Document Processing'")
        return False
    
    title = sys.argv[1]
    
    # Create filename from title
    filename = title.lower()
    filename = filename.replace(' ', '-')
    filename = filename.replace('?', '')
    filename = filename.replace('!', '')
    filename = filename.replace(',', '')
    filename = filename.replace('.', '')
    filename = filename.replace(':', '')
    filename = filename.replace('(', '')
    filename = filename.replace(')', '')
    filename = filename.replace("'", '')
    filename = filename.replace('"', '')
    filename += '.html'
    
    posts_dir = Path("blog/posts")
    if not posts_dir.exists():
        posts_dir.mkdir(parents=True)
    
    post_file = posts_dir / filename
    
    if post_file.exists():
        print(f"[ERROR] Blog post already exists: {filename}")
        return False
    
    # Create blog post template
    template = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-838XD1M1EQ"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-838XD1M1EQ');
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | TidiFul</title>
    <meta name="description" content="Learn about {title.lower()} with TidiFul's comprehensive guide. Discover best practices, tools, and methods for efficient document processing.">
    <meta name="keywords" content="{title.lower()}, document processing, AI, automation, TidiFul">
    <meta name="author" content="TidiFul Team">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://tidiful.com/blog/posts/{filename}">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="Learn about {title.lower()} with TidiFul's comprehensive guide. Discover best practices, tools, and methods for efficient document processing.">
    <meta property="og:url" content="https://tidiful.com/blog/posts/{filename}">
    <meta property="og:site_name" content="TidiFul">
    <meta property="og:image" content="https://tidiful.com/assets/images/tidiful_logo.png">
    <meta property="og:image:alt" content="TidiFul {title} Guide">
    <meta property="og:locale" content="en_US">
    <meta property="article:published_time" content="{datetime.now().isoformat()}">
    <meta property="article:author" content="TidiFul Team">
    <meta property="article:section" content="Document Processing">
    <meta property="article:tag" content="{title.split()[0]}">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:title" content="{title}">
    <meta property="twitter:description" content="Learn about {title.lower()} with TidiFul's comprehensive guide. Discover best practices, tools, and methods for efficient document processing.">
    <meta property="twitter:image" content="https://tidiful.com/assets/images/tidiful_logo.png">
    <meta property="twitter:image:alt" content="TidiFul {title} Guide">
    
    <!-- Structured Data -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{title}",
        "description": "Learn about {title.lower()} with TidiFul's comprehensive guide. Discover best practices, tools, and methods for efficient document processing.",
        "image": "https://tidiful.com/assets/images/tidiful_logo.png",
        "author": {{
            "@type": "Organization",
            "name": "TidiFul Team"
        }},
        "publisher": {{
            "@type": "Organization",
            "name": "TidiFul",
            "logo": {{
                "@type": "ImageObject",
                "url": "https://tidiful.com/assets/images/tidiful_logo.png"
            }}
        }},
        "datePublished": "{datetime.now().isoformat()}",
        "dateModified": "{datetime.now().isoformat()}",
        "mainEntityOfPage": {{
            "@type": "WebPage",
            "@id": "https://tidiful.com/blog/posts/{filename}"
        }},
        "articleSection": "Document Processing",
        "keywords": "{title.lower()}, document processing, AI, automation"
    }}
    </script>
    
    <!-- FAQ Structured Data -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {{
                "@type": "Question",
                "name": "What is {title.split()[0]}?",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "This is a placeholder FAQ. Please update with relevant content about {title.lower()}."
                }}
            }},
            {{
                "@type": "Question",
                "name": "How does {title.split()[0]} work with TidiFul?",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "TidiFul provides advanced tools and methods for {title.lower()}. Please update with specific details."
                }}
            }}
        ]
    }}
    </script>
    
    <link rel="icon" type="image/png" href="../../assets/images/leaf_png_128x128.png">
    <link rel="apple-touch-icon" href="../../assets/images/leaf_png_256x256.png">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/feather-icons/dist/feather-icons.min.js"></script>
    <script src="https://unpkg.com/feather-icons"></script>
    <script src="../../assets/js/i18n.js"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        primary: {{
                            50: '#ecfdf5',
                            100: '#d1fae5',
                            200: '#a7f3d0',
                            300: '#6ee7b7',
                            400: '#34d399',
                            500: '#10b981',
                            600: '#059669',
                            700: '#047857',
                            800: '#065f46',
                            900: '#064e3b',
                        }},
                        secondary: {{
                            50: '#ecfeff',
                            100: '#cffafe',
                            200: '#a5f3fc',
                            300: '#67e8f9',
                            400: '#22d3ee',
                            500: '#06b6d4',
                            600: '#0891b2',
                            700: '#0e7490',
                            800: '#155e75',
                            900: '#164e63',
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        .text-gradient {{
            background: linear-gradient(135deg, #10b981, #06b6d4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .card-hover {{
            transition: all 0.3s ease;
        }}
        .card-hover:hover {{
            transform: translateY(-4px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }}
        .prose {{
            max-width: none;
        }}
        .prose h2 {{
            color: #f3f4f6;
            font-size: 1.875rem;
            font-weight: 700;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }}
        .prose h3 {{
            color: #e5e7eb;
            font-size: 1.5rem;
            font-weight: 600;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
        }}
        .prose p {{
            color: #d1d5db;
            line-height: 1.75;
            margin-bottom: 1rem;
        }}
        .prose ul, .prose ol {{
            color: #d1d5db;
            margin-bottom: 1rem;
        }}
        .prose li {{
            margin-bottom: 0.5rem;
        }}
        .prose strong {{
            color: #f3f4f6;
            font-weight: 600;
        }}
        .prose a {{
            color: #10b981;
            text-decoration: none;
        }}
        .prose a:hover {{
            color: #34d399;
            text-decoration: underline;
        }}
    </style>
</head>
<body class="min-h-screen text-gray-100 antialiased">
    <!-- Navigation -->
    <nav class="border-b border-gray-700 bg-gray-900 backdrop-blur-sm relative z-10">
        <div class="container mx-auto px-4 py-4">
            <div class="flex items-center justify-between">
                <a href="../../index.html" class="flex items-center space-x-2 hover:opacity-80 transition-opacity">
                    <img src="../../assets/images/leaf_png_128x128.png" alt="TidiFul" class="h-8 w-auto">
                    <span class="text-xl font-bold text-gray-100">TidiFul</span>
                </a>
                
                <!-- Desktop Navigation -->
                <div class="hidden lg:flex items-center space-x-8">
                    <a href="../../index.html" class="text-gray-300 hover:text-emerald-400 transition-colors" data-i18n="nav.home">Home</a>
                    <a href="../../features.html" class="text-gray-300 hover:text-emerald-400 transition-colors" data-i18n="nav.features">Features</a>
                    <a href="../../pricing.html" class="text-gray-300 hover:text-emerald-400 transition-colors" data-i18n="nav.pricing">Pricing</a>
                    <a href="../blogs.html" class="text-emerald-400 font-medium" data-i18n="nav.blog">Blog</a>
                    <a href="../../about.html" class="text-gray-300 hover:text-emerald-400 transition-colors">About</a>
                    <a href="#" class="text-gray-300 hover:text-emerald-400 transition-colors" data-i18n="nav.contact">Contact</a>
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
                    <a href="https://app.tidiful.com" class="px-4 py-2 rounded-lg border border-emerald-500 text-emerald-400 hover:bg-emerald-900 transition-colors" data-i18n="nav.createAccountLogin">
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
        
        <!-- Mobile Menu Overlay -->
        <div id="mobile-menu" class="lg:hidden hidden fixed inset-x-0 top-0 z-[100] bg-gray-800 border-b border-gray-600">
            <div class="flex flex-col w-full">
                <!-- Mobile Menu Header -->
                <div class="flex items-center justify-between p-4 border-b border-gray-700">
                    <a href="../../index.html" class="flex items-center space-x-2 hover:opacity-80 transition-opacity">
                        <img src="../../assets/images/leaf_png_128x128.png" alt="TidiFul" class="h-8 w-auto">
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
                        <a href="../../index.html" class="block px-4 py-2 text-lg text-gray-300 hover:text-emerald-400 hover:bg-gray-800 rounded-lg transition-colors" data-i18n="nav.home">Home</a>
                        <a href="../../features.html" class="block px-4 py-2 text-lg text-gray-300 hover:text-emerald-400 hover:bg-gray-800 rounded-lg transition-colors" data-i18n="nav.features">Features</a>
                        <a href="../../pricing.html" class="block px-4 py-2 text-lg text-gray-300 hover:text-emerald-400 hover:bg-gray-800 rounded-lg transition-colors" data-i18n="nav.pricing">Pricing</a>
                        <a href="../blogs.html" class="block px-4 py-2 text-lg text-emerald-400 font-medium hover:bg-gray-800 rounded-lg transition-colors" data-i18n="nav.blog">Blog</a>
                        <a href="../../about.html" class="block px-4 py-2 text-lg text-gray-300 hover:text-emerald-400 hover:bg-gray-800 rounded-lg transition-colors">About</a>
                        <a href="#" class="block px-4 py-2 text-lg text-gray-300 hover:text-emerald-400 hover:bg-gray-800 rounded-lg transition-colors" data-i18n="nav.contact">Contact</a>
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
                    <a href="https://app.tidiful.com" class="block w-full text-center px-4 py-2 rounded-lg border border-emerald-500 text-emerald-400 hover:bg-emerald-900 transition-colors" data-i18n="nav.createAccountLogin">
                        Create Account / Login
                    </a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Blog Post Content -->
    <main class="py-8 md:py-16 bg-gray-900">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto">
                <!-- Breadcrumb -->
                <nav class="mb-8">
                    <ol class="flex items-center space-x-2 text-sm text-gray-400">
                        <li><a href="../../index.html" class="hover:text-emerald-400 transition-colors">Home</a></li>
                        <li><span class="mx-2">/</span></li>
                        <li><a href="../blogs.html" class="hover:text-emerald-400 transition-colors">Blog</a></li>
                        <li><span class="mx-2">/</span></li>
                        <li class="text-gray-300">{title}</li>
                    </ol>
                </nav>

                <!-- Article Header -->
                <header class="mb-12">
                    <h1 class="text-4xl md:text-5xl font-bold mb-6 text-gray-100">
                        {title}
                    </h1>
                    <div class="flex items-center space-x-4 text-gray-400 mb-6">
                        <span class="flex items-center">
                            <i data-feather="calendar" class="w-4 h-4 mr-2"></i>
                            {datetime.now().strftime('%B %d, %Y')}
                        </span>
                        <span class="flex items-center">
                            <i data-feather="clock" class="w-4 h-4 mr-2"></i>
                            5 min read
                        </span>
                        <span class="flex items-center">
                            <i data-feather="user" class="w-4 h-4 mr-2"></i>
                            TidiFul Team
                        </span>
                    </div>
                    <p class="text-xl text-gray-300 leading-relaxed">
                        Learn about {title.lower()} with TidiFul's comprehensive guide. Discover best practices, tools, and methods for efficient document processing.
                    </p>
                </header>

                <!-- Article Content -->
                <article class="prose prose-lg">
                    <h2>Introduction</h2>
                    <p>This is a template blog post about <strong>{title}</strong>. Please replace this content with your actual article content.</p>
                    
                    <h2>What You'll Learn</h2>
                    <ul>
                        <li>Understanding {title.split()[0]}</li>
                        <li>Best practices and methods</li>
                        <li>How TidiFul can help</li>
                        <li>Real-world applications</li>
                    </ul>
                    
                    <h2>Getting Started</h2>
                    <p>Add your content here. This template includes:</p>
                    <ul>
                        <li>Proper SEO meta tags</li>
                        <li>Structured data (Article and FAQ schema)</li>
                        <li>Responsive design</li>
                        <li>Mobile-friendly navigation</li>
                        <li>Google Analytics integration</li>
                    </ul>
                    
                    <h2>Conclusion</h2>
                    <p>Replace this conclusion with your actual content about {title.lower()}.</p>
                    
                    <div class="bg-emerald-900/20 border border-emerald-500/30 rounded-lg p-6 my-8">
                        <h3 class="text-emerald-400 font-semibold mb-3">Ready to Get Started?</h3>
                        <p class="text-gray-300 mb-4">Experience the power of TidiFul's document processing capabilities.</p>
                        <a href="../../index.html" class="inline-block px-6 py-3 bg-emerald-600 hover:bg-emerald-500 text-white font-medium rounded-lg transition-colors">
                            Try TidiFul Free
                        </a>
                    </div>
                </article>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-gray-800 py-12">
        <div class="container mx-auto px-4">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
                <div class="md:col-span-2">
                    <div class="flex items-center space-x-2 mb-4">
                        <img src="../../assets/images/leaf_png_128x128.png" alt="TidiFul" class="h-8 w-auto">
                        <span class="text-xl font-bold text-gray-100">TidiFul</span>
                    </div>
                    <p class="text-gray-400" data-i18n="footer.tagline">Transforming documents into structured data with AI-powered precision.</p>
                </div>
                
                <div>
                    <h4 class="text-lg font-semibold mb-4" data-i18n="footer.product">Product</h4>
                    <ul class="space-y-2">
                        <li><a href="../../features.html" class="text-gray-400 hover:text-emerald-400 transition-colors" data-i18n="nav.features">Features</a></li>
                        <li><a href="../../pricing.html" class="text-gray-400 hover:text-emerald-400 transition-colors" data-i18n="nav.pricing">Pricing</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="text-lg font-semibold mb-4" data-i18n="footer.resources">Resources</h4>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-gray-400 hover:text-emerald-400 transition-colors" data-i18n="footer.documentation">Documentation</a></li>
                        <li><a href="../blogs.html" class="text-gray-400 hover:text-emerald-400 transition-colors" data-i18n="nav.blog">Blog</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-emerald-400 transition-colors" data-i18n="footer.caseStudies">Case Studies</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-emerald-400 transition-colors" data-i18n="footer.support">Support</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="border-t border-gray-700 mt-8 pt-8 text-center">
                <p class="text-gray-500" data-i18n="footer.copyright">© 2023 TidiFul. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script>
        // Initialize mobile menu
        function initializeMobileMenu() {{
            const mobileMenuButton = document.getElementById('mobile-menu-button');
            const mobileMenu = document.getElementById('mobile-menu');
            const mobileMenuClose = document.getElementById('mobile-menu-close');
            const body = document.body;

            function openMobileMenu() {{
                mobileMenu.classList.remove('hidden');
                body.style.overflow = 'hidden';
            }}

            function closeMobileMenu() {{
                mobileMenu.classList.add('hidden');
                body.style.overflow = '';
            }}

            mobileMenuButton.addEventListener('click', openMobileMenu);
            mobileMenuClose.addEventListener('click', closeMobileMenu);

            // Close menu when clicking on links
            const mobileLinks = mobileMenu.querySelectorAll('a');
            mobileLinks.forEach(link => {{
                link.addEventListener('click', closeMobileMenu);
            }});

            // Close menu when pressing Escape
            document.addEventListener('keydown', (e) => {{
                if (e.key === 'Escape' && !mobileMenu.classList.contains('hidden')) {{
                    closeMobileMenu();
                }}
            }});

            // Close menu when clicking outside
            mobileMenu.addEventListener('click', (e) => {{
                if (e.target === mobileMenu) {{
                    closeMobileMenu();
                }}
            }});
        }}

        // Initialize language switcher
        function initializeLanguageSwitcher() {{
            const desktopSwitcher = document.getElementById('language-switcher');
            const mobileSwitcher = document.getElementById('mobile-language-switcher');

            function switchLanguage(language) {{
                // Update URL with language parameter
                const url = new URL(window.location);
                url.searchParams.set('lang', language);
                window.location.href = url.toString();
            }}

            if (desktopSwitcher) {{
                desktopSwitcher.addEventListener('change', (e) => {{
                    switchLanguage(e.target.value);
                }});
            }}

            if (mobileSwitcher) {{
                mobileSwitcher.addEventListener('change', (e) => {{
                    switchLanguage(e.target.value);
                }});
            }}
        }}

        // Initialize everything when DOM is loaded
        document.addEventListener('DOMContentLoaded', function() {{
            initializeMobileMenu();
            initializeLanguageSwitcher();
            
            // Initialize Feather icons
            if (typeof feather !== 'undefined') {{
                feather.replace();
            }}
        }});
    </script>
</body>
</html>"""
    
    # Write the file
    with open(post_file, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"[SUCCESS] Created blog post: {filename}")
    print(f"[INFO] File location: {post_file}")
    print(f"[INFO] Title: {title}")
    
    # Run automation
    print("\n[INFO] Running blog automation...")
    os.system("python blog_automation.py --action full")
    
    return True

if __name__ == "__main__":
    create_blog_post()
