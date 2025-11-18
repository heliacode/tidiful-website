#!/usr/bin/env python3
"""Comprehensive check of all blog files"""

import json
import re
from pathlib import Path

print("=" * 70)
print("COMPREHENSIVE BLOG SYSTEM CHECK")
print("=" * 70)

# 1. Check manifest
manifest_path = Path("blog/posts/manifest.json")
with open(manifest_path, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

manifest_filenames = {post['filename'] for post in manifest['posts']}

# 2. Check actual files in blog/posts
posts_dir = Path("blog/posts")
actual_post_files = {f.name for f in posts_dir.glob("*.html") if f.name != "manifest.json"}

# 3. Check static files
static_dir = Path("blog/static")
actual_static_files = {f.name for f in static_dir.glob("*.html")}

# 4. Check sitemap
sitemap_path = Path("sitemap.xml")
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

sitemap_post_urls = set(re.findall(r'<loc>https://tidiful\.com/blog/posts/([^<]+)</loc>', sitemap_content))
sitemap_static_urls = set(re.findall(r'<loc>https://tidiful\.com/blog/static/([^<]+)</loc>', sitemap_content))

print("\n[FILE INTEGRITY CHECK]")
print(f"   Manifest posts: {len(manifest_filenames)}")
print(f"   Actual post files: {len(actual_post_files)}")
print(f"   Actual static files: {len(actual_static_files)}")
print(f"   Sitemap post URLs: {len(sitemap_post_urls)}")
print(f"   Sitemap static URLs: {len(sitemap_static_urls)}")

# Find discrepancies
issues = []

# Posts in manifest but not in filesystem
missing_posts = manifest_filenames - actual_post_files
if missing_posts:
    issues.append("MISSING POST FILES")
    for post in missing_posts:
        print(f"   [ERROR] Post in manifest but file missing: {post}")

# Posts in filesystem but not in manifest
orphaned_posts = actual_post_files - manifest_filenames
if orphaned_posts:
    issues.append("ORPHANED POST FILES")
    for post in orphaned_posts:
        print(f"   [WARNING] Post file not in manifest: {post}")

# Static files not in sitemap
orphaned_static = actual_static_files - sitemap_static_urls
if orphaned_static:
    issues.append("ORPHANED STATIC FILES")
    for static in orphaned_static:
        print(f"   [WARNING] Static file not in sitemap: {static}")

# Posts in manifest but not in sitemap
missing_in_sitemap = manifest_filenames - sitemap_post_urls
if missing_in_sitemap:
    issues.append("POSTS MISSING FROM SITEMAP")
    for post in missing_in_sitemap:
        print(f"   [ERROR] Post in manifest but not in sitemap: {post}")

# Check excerpts in HTML files
print("\n[EXCERPT CHECK IN HTML FILES]")
posts_missing_excerpts = []
for post_file in actual_post_files:
    file_path = posts_dir / post_file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if not re.search(r'<meta\s+name=["\']excerpt["\']', content, re.IGNORECASE):
        posts_missing_excerpts.append(post_file)
        print(f"   [ERROR] Missing excerpt meta tag: {post_file}")

if not posts_missing_excerpts:
    print("   [OK] All post files have excerpt meta tags")

# Check JSON validity
print("\n[JSON VALIDITY CHECK]")
try:
    json.loads(manifest_path.read_text(encoding='utf-8'))
    print("   [OK] Manifest JSON is valid")
except json.JSONDecodeError as e:
    issues.append("INVALID JSON")
    print(f"   [ERROR] Manifest JSON is invalid: {e}")

# Summary
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

if not issues and not posts_missing_excerpts:
    print("[SUCCESS] Everything is correct!")
    print(f"   - All {len(manifest_filenames)} posts accounted for")
    print(f"   - All files exist")
    print(f"   - All excerpts present")
    print(f"   - Sitemap synchronized")
else:
    print("[ISSUES FOUND]")
    for issue in set(issues):
        print(f"   - {issue}")
    if posts_missing_excerpts:
        print(f"   - {len(posts_missing_excerpts)} posts missing excerpt meta tags")

print("=" * 70)

