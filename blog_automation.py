#!/usr/bin/env python3
"""
Automated Blog Post Management System
Handles blog post discovery, manifest generation, static file creation, and sitemap updates
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path
import argparse

class BlogAutomation:
    def __init__(self):
        self.posts_dir = Path("blog/posts")
        self.static_dir = Path("blog/static")
        self.manifest_file = self.posts_dir / "manifest.json"
        self.blogs_html = Path("blog/blogs.html")
        self.sitemap_file = Path("sitemap.xml")
        
    def discover_blog_posts(self):
        """Automatically discover all blog posts in the posts directory"""
        if not self.posts_dir.exists():
            print(f"[ERROR] Posts directory not found: {self.posts_dir}")
            return []
        
        posts = []
        for html_file in self.posts_dir.glob("*.html"):
            if html_file.name == "template.html":  # Skip template files
                continue
                
            post_info = self.extract_post_metadata(html_file)
            if post_info:
                posts.append(post_info)
        
        # Sort by date (newest first)
        posts.sort(key=lambda x: x['date'], reverse=True)
        return posts
    
    def extract_post_metadata(self, html_file):
        """Extract metadata from HTML file"""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract title
            title_match = re.search(r'<title>(.*?)</title>', content)
            title = title_match.group(1) if title_match else "Untitled"
            title = title.replace(' - TidiFul Blog', '').replace(' | TidiFul', '')
            
            # Extract date
            date_match = re.search(r'<meta property="article:published_time" content="(.*?)"', content)
            if not date_match:
                date_match = re.search(r'<meta name="date" content="(.*?)"', content)
            if not date_match:
                date_match = re.search(r'"datePublished": "(.*?)"', content)
            
            date = date_match.group(1)[:10] if date_match else datetime.now().strftime("%Y-%m-%d")
            
            # Extract excerpt
            excerpt_match = re.search(r'<meta name="description" content="(.*?)"', content)
            excerpt = excerpt_match.group(1) if excerpt_match else "No excerpt available"
            
            # Extract URL
            url_match = re.search(r'<link rel="canonical" href="(.*?)"', content)
            url = url_match.group(1) if url_match else f"posts/{html_file.name}"
            
            return {
                'filename': html_file.name,
                'title': title,
                'date': date,
                'excerpt': excerpt,
                'url': url.replace('https://tidiful.com/', '')
            }
        except Exception as e:
            print(f"[ERROR] Could not extract metadata from {html_file.name}: {e}")
            return None
    
    def generate_manifest(self, posts):
        """Generate or update the manifest.json file"""
        manifest = {
            "posts": posts,
            "lastUpdated": datetime.now().isoformat(),
            "totalPosts": len(posts)
        }
        
        try:
            with open(self.manifest_file, 'w', encoding='utf-8') as f:
                json.dump(manifest, f, indent=2, ensure_ascii=False)
            print(f"[OK] Generated manifest with {len(posts)} posts")
            return True
        except Exception as e:
            print(f"[ERROR] Could not generate manifest: {e}")
            return False
    
    def generate_static_posts(self, posts):
        """Generate static versions of blog posts"""
        if not self.static_dir.exists():
            self.static_dir.mkdir(parents=True)
        
        generated_count = 0
        for post in posts:
            if self.generate_single_static_post(post):
                generated_count += 1
        
        print(f"[OK] Generated {generated_count} static posts")
        return generated_count > 0
    
    def generate_single_static_post(self, post):
        """Generate static version of a single post"""
        try:
            post_file = self.posts_dir / post['filename']
            with open(post_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract just the article content (between <main> tags or similar)
            article_match = re.search(r'<main[^>]*>(.*?)</main>', content, re.DOTALL)
            if not article_match:
                article_match = re.search(r'<article[^>]*>(.*?)</article>', content, re.DOTALL)
            
            article_content = article_match.group(1) if article_match else content
            
            # Generate static HTML
            static_html = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{post['title']} - TidiFul Blog</title>
    <meta name="description" content="{post['excerpt']}">
    <meta name="date" content="{post['date']}">
    <meta name="excerpt" content="{post['excerpt']}">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="{post['title']}">
    <meta property="og:description" content="{post['excerpt']}">
    <meta property="og:url" content="https://tidiful.com/blog/static/{post['filename']}">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:title" content="{post['title']}">
    <meta property="twitter:description" content="{post['excerpt']}">
    
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
                    <a href="../../features.html" class="text-gray-300 hover:text-emerald-400 transition-colors">Features</a>
                    <a href="../../pricing.html" class="text-gray-300 hover:text-emerald-400 transition-colors">Pricing</a>
                    <a href="../blogs.html" class="text-emerald-400 font-medium">Blog</a>
                    <a href="../../about.html" class="text-gray-300 hover:text-emerald-400 transition-colors">About</a>
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
                                <p class="text-sm text-gray-400">{datetime.strptime(post['date'], "%Y-%m-%d").strftime("%B %d, %Y")}</p>
                                <h1 class="text-3xl md:text-4xl font-bold text-gray-100">{post['title']}</h1>
                            </div>
                        </div>
                    </div>
                    
                    <div class="prose prose-lg max-w-none">
                        {article_content}
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
            static_file = self.static_dir / post['filename']
            with open(static_file, 'w', encoding='utf-8') as f:
                f.write(static_html)
            
            return True
        except Exception as e:
            print(f"[ERROR] Could not generate static post {post['filename']}: {e}")
            return False
    
    def update_blogs_html(self, posts):
        """Update the blogs.html file with current post list"""
        if not self.blogs_html.exists():
            print(f"[ERROR] blogs.html not found: {self.blogs_html}")
            return False
        
        try:
            with open(self.blogs_html, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract filenames for JavaScript
            filenames = [post['filename'] for post in posts]
            
            # Update the commonPosts array
            old_pattern = r'const commonPosts = \[(.*?)\];'
            new_posts = ',\n                '.join([f"'{filename}'" for filename in filenames])
            new_content = f'const commonPosts = [\n                {new_posts}\n                // Add new post filenames here when you create them\n            ];'
            
            updated_content = re.sub(old_pattern, new_content, content, flags=re.DOTALL)
            
            if updated_content != content:
                with open(self.blogs_html, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"[OK] Updated blogs.html with {len(filenames)} posts")
                return True
            else:
                print("[INFO] blogs.html already up to date")
                return True
        except Exception as e:
            print(f"[ERROR] Could not update blogs.html: {e}")
            return False
    
    def update_sitemap(self, posts):
        """Update sitemap.xml with blog posts"""
        if not self.sitemap_file.exists():
            print(f"[ERROR] sitemap.xml not found: {self.sitemap_file}")
            return False
        
        try:
            with open(self.sitemap_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find the end of existing blog posts section
            blog_posts_end = content.find('</urlset>')
            if blog_posts_end == -1:
                print("[ERROR] Could not find </urlset> tag in sitemap")
                return False
            
            # Generate new sitemap entries
            new_entries = []
            
            # Add main blog posts
            for post in posts:
                url = post['url'].replace('posts/', 'https://tidiful.com/blog/posts/')
                static_url = url.replace('/posts/', '/static/')
                
                # Main post entry
                new_entries.append(f'''  <!-- {post['title']} Blog Post - English -->
  <url>
    <loc>{url}</loc>
    <lastmod>{post['date']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
    <xhtml:link rel="alternate" hreflang="en-US" href="{url}?lang=en-US"/>
    <xhtml:link rel="alternate" hreflang="fr-FR" href="{url}?lang=fr-FR"/>
    <xhtml:link rel="alternate" hreflang="de-DE" href="{url}?lang=de-DE"/>
    <xhtml:link rel="alternate" hreflang="es-ES" href="{url}?lang=es-ES"/>
    <xhtml:link rel="alternate" hreflang="el-GR" href="{url}?lang=el-GR"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{url}"/>
  </url>

  <!-- {post['title']} Static - English -->
  <url>
    <loc>{static_url}</loc>
    <lastmod>{post['date']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
    <xhtml:link rel="alternate" hreflang="en-US" href="{static_url}?lang=en-US"/>
    <xhtml:link rel="alternate" hreflang="fr-FR" href="{static_url}?lang=fr-FR"/>
    <xhtml:link rel="alternate" hreflang="de-DE" href="{static_url}?lang=de-DE"/>
    <xhtml:link rel="alternate" hreflang="es-ES" href="{static_url}?lang=es-ES"/>
    <xhtml:link rel="alternate" hreflang="el-GR" href="{static_url}?lang=el-GR"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{static_url}"/>
  </url>''')
            
            # Remove old blog post entries and add new ones
            # Find the start of blog posts section
            blog_start = content.find('<!-- Blog Posts -->')
            if blog_start != -1:
                # Remove everything from blog posts to end of urlset
                content = content[:blog_start] + '</urlset>'
            
            # Insert new entries before </urlset>
            new_content = content.replace('</urlset>', '\n  <!-- Blog Posts -->\n\n' + '\n'.join(new_entries) + '\n\n</urlset>')
            
            with open(self.sitemap_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"[OK] Updated sitemap.xml with {len(posts)} blog posts")
            return True
        except Exception as e:
            print(f"[ERROR] Could not update sitemap: {e}")
            return False
    
    def run_full_automation(self):
        """Run the complete blog automation process"""
        print("Starting automated blog post management...")
        
        # Step 1: Discover posts
        posts = self.discover_blog_posts()
        if not posts:
            print("[WARNING] No blog posts found")
            return False
        
        print(f"[INFO] Discovered {len(posts)} blog posts")
        
        # Step 2: Generate manifest
        if not self.generate_manifest(posts):
            return False
        
        # Step 3: Generate static posts
        if not self.generate_static_posts(posts):
            return False
        
        # Step 4: Update blogs.html
        if not self.update_blogs_html(posts):
            return False
        
        # Step 5: Update sitemap
        if not self.update_sitemap(posts):
            return False
        
        print("[SUCCESS] Blog automation completed successfully!")
        return True

def main():
    parser = argparse.ArgumentParser(description='Automated Blog Post Management')
    parser.add_argument('--action', choices=['full', 'manifest', 'static', 'update', 'discover'], 
                       default='full', help='Action to perform')
    
    args = parser.parse_args()
    
    automation = BlogAutomation()
    
    if args.action == 'full':
        success = automation.run_full_automation()
    elif args.action == 'discover':
        posts = automation.discover_blog_posts()
        print(f"Discovered {len(posts)} posts:")
        for post in posts:
            print(f"  - {post['filename']}: {post['title']}")
        success = True
    elif args.action == 'manifest':
        posts = automation.discover_blog_posts()
        success = automation.generate_manifest(posts)
    elif args.action == 'static':
        posts = automation.discover_blog_posts()
        success = automation.generate_static_posts(posts)
    elif args.action == 'update':
        posts = automation.discover_blog_posts()
        success = automation.update_blogs_html(posts) and automation.update_sitemap(posts)
    
    exit(0 if success else 1)

if __name__ == "__main__":
    main()
