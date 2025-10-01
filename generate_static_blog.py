# Blog SEO Solution - Static Generation Script

# This script generates static HTML files for each blog post
# Run this whenever you add new posts to ensure SEO compatibility

import os
import re
from datetime import datetime
from pathlib import Path

def generate_static_blog_posts():
    """Generate static HTML files for each blog post for SEO"""
    
    posts_dir = Path("blog/posts")
    output_dir = Path("blog/static")
    output_dir.mkdir(exist_ok=True)
    
    # Get all HTML files in posts directory
    post_files = list(posts_dir.glob("*.html"))
    
    for post_file in post_files:
        # Read the post content
        with open(post_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract metadata
        title_match = re.search(r'<title>(.*?)</title>', content)
        date_match = re.search(r'<meta name="date" content="(.*?)">', content)
        excerpt_match = re.search(r'<meta name="excerpt" content="(.*?)">', content)
        
        title = title_match.group(1) if title_match else "Untitled"
        date = date_match.group(1) if date_match else datetime.now().strftime("%Y-%m-%d")
        excerpt = excerpt_match.group(1) if excerpt_match else "No excerpt available"
        
        # Generate static HTML with proper SEO meta tags
        static_html = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - TidiFul Blog</title>
    <meta name="description" content="{excerpt}">
    <meta name="date" content="{date}">
    <meta name="excerpt" content="{excerpt}">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{excerpt}">
    <meta property="og:url" content="https://tidiful.com/blog/static/{post_file.stem}.html">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:title" content="{title}">
    <meta property="twitter:description" content="{excerpt}">
    
    <link rel="icon" type="image/png" href="../../assets/images/leaf_png_128x128.png">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/feather-icons/dist/feather.min.js"></script>
    <script src="https://unpkg.com/feather-icons"></script>
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
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{ background: #161616; }}
        .prose {{ color: #e5e7eb; }}
        .prose h1, .prose h2, .prose h3 {{ color: #10b981; }}
        .prose a {{ color: #10b981; }}
        .prose code {{ background: #374151; padding: 2px 6px; border-radius: 4px; }}
    </style>
</head>
<body class="min-h-screen text-gray-100 antialiased">
    <!-- Navigation -->
    <nav class="border-b border-gray-700 bg-gray-900 backdrop-blur-sm">
        <div class="container mx-auto px-4 py-4">
            <div class="flex items-center justify-between">
                <div class="flex items-center space-x-2">
                    <img src="../../assets/images/leaf_png_128x128.png" alt="TidiFul" class="w-8 h-8">
                    <span class="text-xl font-bold text-gray-100">TidiFul</span>
                </div>
                <div class="hidden md:flex items-center space-x-8">
                    <a href="../../index.html" class="text-gray-300 hover:text-emerald-400 transition-colors">Home</a>
                    <a href="#" class="text-gray-300 hover:text-emerald-400 transition-colors">Features</a>
                    <a href="../../pricing.html" class="text-gray-300 hover:text-emerald-400 transition-colors">Pricing</a>
                    <a href="../blogs.html" class="text-emerald-400 font-medium">Blog</a>
                    <a href="#" class="text-gray-300 hover:text-emerald-400 transition-colors">Contact</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Blog Post Content -->
    <article class="py-16 bg-gray-900">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto">
                <div class="bg-gray-800 rounded-2xl p-8 md:p-12">
                    <div class="mb-8">
                        <div class="flex items-center mb-4">
                            <div class="w-10 h-10 rounded-full bg-emerald-500 flex items-center justify-center mr-4">
                                <i data-feather="calendar" class="w-5 h-5 text-white"></i>
                            </div>
                            <div>
                                <p class="text-sm text-gray-400">{datetime.strptime(date, "%Y-%m-%d").strftime("%B %d, %Y")}</p>
                                <h1 class="text-3xl md:text-4xl font-bold text-gray-100">{title}</h1>
                            </div>
                        </div>
                    </div>
                    
                    <div class="prose prose-lg max-w-none">
                        {content}
                    </div>
                    
                    <div class="mt-12 pt-8 border-t border-gray-700">
                        <a href="../blogs.html" class="inline-flex items-center text-emerald-400 hover:text-emerald-300 transition-colors">
                            <i data-feather="arrow-left" class="w-4 h-4 mr-2"></i>
                            Back to Blog
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </article>

    <script>
        feather.replace();
    </script>
</body>
</html>"""
        
        # Write static file
        output_file = output_dir / f"{post_file.stem}.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(static_html)
        
        print(f"Generated static file: {output_file}")

if __name__ == "__main__":
    generate_static_blog_posts()
