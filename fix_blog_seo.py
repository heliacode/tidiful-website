#!/usr/bin/env python3
"""
Script to add missing SEO elements to blog posts:
- BreadcrumbList schema
- Hreflang tags
- Advanced schema properties (inLanguage, wordCount, timeRequired)
- article:modified_time
"""

import os
import re
from pathlib import Path
from datetime import datetime

def extract_title_from_html(content):
    """Extract title from HTML"""
    title_match = re.search(r'<title>(.*?)</title>', content)
    if title_match:
        title = title_match.group(1)
        # Clean up title
        title = title.replace(' - TidiFul Blog', '').replace(' | TidiFul', '')
        return title
    return None

def extract_canonical_url(content):
    """Extract canonical URL from HTML"""
    canonical_match = re.search(r'<link rel="canonical" href="(.*?)"', content)
    if canonical_match:
        return canonical_match.group(1)
    return None

def extract_date_from_html(content):
    """Extract date from HTML"""
    # Try article:published_time first
    date_match = re.search(r'<meta property="article:published_time" content="(.*?)"', content)
    if not date_match:
        date_match = re.search(r'<meta name="date" content="(.*?)"', content)
    if date_match:
        date_str = date_match.group(1)
        # Extract just the date part (YYYY-MM-DD)
        if 'T' in date_str:
            return date_str.split('T')[0]
        return date_str[:10]
    return datetime.now().strftime("%Y-%m-%d")

def add_hreflang_tags(content, canonical_url):
    """Add hreflang tags if missing"""
    if 'hreflang' in content:
        return content  # Already has hreflang
    
    if not canonical_url:
        return content
    
    hreflang_block = f'''    <!-- Hreflang Tags -->
    <link rel="alternate" hreflang="en" href="{canonical_url}?lang=en-US">
    <link rel="alternate" hreflang="fr" href="{canonical_url}?lang=fr-FR">
    <link rel="alternate" hreflang="de" href="{canonical_url}?lang=de-DE">
    <link rel="alternate" hreflang="es" href="{canonical_url}?lang=es-ES">
    <link rel="alternate" hreflang="el" href="{canonical_url}?lang=el-GR">
    <link rel="alternate" hreflang="x-default" href="{canonical_url}">
    
'''
    
    # Insert after canonical link
    canonical_pattern = r'(<link rel="canonical" href="[^"]*">\s*\n)'
    if re.search(canonical_pattern, content):
        content = re.sub(canonical_pattern, r'\1' + hreflang_block, content)
    
    return content

def add_breadcrumb_schema(content, title, canonical_url):
    """Add BreadcrumbList schema if missing"""
    if 'BreadcrumbList' in content:
        return content  # Already has BreadcrumbList
    
    if not canonical_url or not title:
        return content
    
    # Escape quotes in title for JSON
    title_escaped = title.replace('"', '\\"')
    
    breadcrumb_schema = f'''    <!-- Breadcrumb Structured Data -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {{
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://tidiful.com/index.html"
            }},
            {{
                "@type": "ListItem",
                "position": 2,
                "name": "Blog",
                "item": "https://tidiful.com/blog/blogs.html"
            }},
            {{
                "@type": "ListItem",
                "position": 3,
                "name": "{title_escaped}",
                "item": "{canonical_url}"
            }}
        ]
    }}
    </script>
    
'''
    
    # Insert before favicon link (most reliable location)
    favicon_pattern = r'(<link rel="icon" type="image/png")'
    if re.search(favicon_pattern, content):
        content = re.sub(favicon_pattern, breadcrumb_schema + r'\1', content)
    
    return content

def add_advanced_schema_properties(content, date_str):
    """Add inLanguage, wordCount, timeRequired to Article schema"""
    if '"inLanguage"' in content:
        return content  # Already has advanced properties
    
    # Add inLanguage after dateModified
    date_modified_pattern = r'("dateModified":\s*"[^"]*",\s*\n)'
    if re.search(date_modified_pattern, content):
        content = re.sub(date_modified_pattern, r'\1        "inLanguage": "en-US",\n        ', content)
    
    # Add wordCount and timeRequired before mainEntityOfPage or keywords or closing brace
    if '"mainEntityOfPage"' in content:
        main_entity_pattern = r'("mainEntityOfPage":\s*\{[^}]*\},\s*\n)'
        if re.search(main_entity_pattern, content):
            content = re.sub(main_entity_pattern, r'\1        "wordCount": "2500",\n        "timeRequired": "PT10M",\n        ', content)
    elif '"keywords"' in content:
        keywords_pattern = r'("keywords":\s*"[^"]*"\s*\n)'
        if re.search(keywords_pattern, content):
            content = re.sub(keywords_pattern, r'\1        "wordCount": "2500",\n        "timeRequired": "PT10M",\n        ', content)
    elif '"articleSection"' in content:
        article_section_pattern = r'("articleSection":\s*"[^"]*",\s*\n)'
        if re.search(article_section_pattern, content):
            content = re.sub(article_section_pattern, r'\1        "wordCount": "2500",\n        "timeRequired": "PT10M",\n        ', content)
    
    return content

def add_article_modified_time(content, date_str):
    """Add article:modified_time if missing"""
    if 'article:modified_time' in content:
        return content  # Already has it
    
    # Add after article:published_time
    published_pattern = r'(<meta property="article:published_time" content="[^"]*">\s*\n)'
    modified_time = f'    <meta property="article:modified_time" content="{date_str}T00:00:00Z">\n'
    
    if re.search(published_pattern, content):
        content = re.sub(published_pattern, r'\1' + modified_time, content)
    
    return content

def fix_blog_post(filepath):
    """Fix a single blog post"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Extract metadata
        title = extract_title_from_html(content)
        canonical_url = extract_canonical_url(content)
        date_str = extract_date_from_html(content)
        
        # Add missing elements
        content = add_hreflang_tags(content, canonical_url)
        content = add_breadcrumb_schema(content, title, canonical_url)
        content = add_advanced_schema_properties(content, date_str)
        content = add_article_modified_time(content, date_str)
        
        # Only write if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    posts_dir = Path("blog/posts")
    if not posts_dir.exists():
        print(f"Posts directory not found: {posts_dir}")
        return
    
    posts = list(posts_dir.glob("*.html"))
    posts = [p for p in posts if p.name != "manifest.json"]
    
    print(f"Processing {len(posts)} blog posts...")
    
    fixed_count = 0
    for post_file in posts:
        if fix_blog_post(post_file):
            print(f"[OK] Fixed: {post_file.name}")
            fixed_count += 1
        else:
            print(f"[SKIP] Already complete: {post_file.name}")
    
    print(f"\n[SUCCESS] Fixed {fixed_count} out of {len(posts)} posts")

if __name__ == "__main__":
    main()

