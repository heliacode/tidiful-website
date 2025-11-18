#!/usr/bin/env python3
"""
Update sitemap.xml to include all public pages and clean up formatting
"""

import re
from datetime import datetime
from pathlib import Path

def update_sitemap():
    sitemap_file = Path("sitemap.xml")
    
    if not sitemap_file.exists():
        print(f"[ERROR] sitemap.xml not found")
        return False
    
    # Read current sitemap
    with open(sitemap_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove empty lines (lines with only whitespace) - more aggressive
    lines = content.split('\n')
    cleaned_lines = []
    prev_empty = False
    for line in lines:
        if line.strip():  # Non-empty line
            cleaned_lines.append(line)
            prev_empty = False
        elif not prev_empty:  # First empty line, keep it
            cleaned_lines.append('')
            prev_empty = True
        # Skip subsequent empty lines
    content = '\n'.join(cleaned_lines)
    
    # Check if datagrid.html is already in sitemap
    if 'datagrid.html' not in content:
        # Find the position to insert (after blog main page, before blog posts)
        blog_posts_marker = '<!-- Blog Posts -->'
        if blog_posts_marker in content:
            datagrid_entry = '''  <!-- Data Grid Page - English -->
  <url>
    <loc>https://tidiful.com/datagrid.html</loc>
    <lastmod>2025-01-15</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
    <xhtml:link rel="alternate" hreflang="en-US" href="https://tidiful.com/datagrid.html?lang=en-US"/>
    <xhtml:link rel="alternate" hreflang="fr-FR" href="https://tidiful.com/datagrid.html?lang=fr-FR"/>
    <xhtml:link rel="alternate" hreflang="de-DE" href="https://tidiful.com/datagrid.html?lang=de-DE"/>
    <xhtml:link rel="alternate" hreflang="es-ES" href="https://tidiful.com/datagrid.html?lang=es-ES"/>
    <xhtml:link rel="alternate" hreflang="el-GR" href="https://tidiful.com/datagrid.html?lang=el-GR"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://tidiful.com/datagrid.html"/>
  </url>

'''
            content = content.replace(blog_posts_marker, datagrid_entry + blog_posts_marker)
            print("[OK] Added datagrid.html to sitemap")
        else:
            print("[WARNING] Could not find blog posts marker to insert datagrid.html")
    
    # Write updated sitemap
    with open(sitemap_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("[SUCCESS] Sitemap updated successfully!")
    return True

if __name__ == "__main__":
    update_sitemap()

