#!/usr/bin/env python3
"""
Simple SEO health check script
"""

import os

def check_schema():
    pages = ['index.html', 'pricing.html', 'features.html', 'about.html']
    schema_issues = 0
    
    print("Running SEO health check for AI optimization...")
    
    for page in pages:
        if os.path.exists(page):
            with open(page, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'FAQPage' in content:
                    print(f"[OK] FAQ schema found on {page}")
                else:
                    print(f"[ERROR] Missing FAQ schema on {page}")
                    schema_issues += 1
        else:
            print(f"[ERROR] File not found: {page}")
            schema_issues += 1
    
    # Check Organization schema
    if os.path.exists('index.html'):
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
            if 'Organization' in content:
                print("[OK] Organization schema found")
            else:
                print("[ERROR] Missing Organization schema")
                schema_issues += 1
    
    # Count blog posts
    blog_dir = 'blog/posts'
    if os.path.exists(blog_dir):
        blog_posts = len([f for f in os.listdir(blog_dir) if f.endswith('.html')])
        print(f"[INFO] Found {blog_posts} blog posts")
    else:
        print("[INFO] Blog posts directory not found")
    
    if schema_issues == 0:
        print("[SUCCESS] All AI optimization checks passed!")
        return True
    else:
        print(f"[WARNING] Found {schema_issues} schema issues")
        return False

if __name__ == "__main__":
    success = check_schema()
    exit(0 if success else 1)
