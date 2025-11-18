#!/usr/bin/env python3
"""Verify manifest and sitemap are in sync"""

import json
import re
from pathlib import Path
from datetime import datetime

print("=" * 70)
print("MANIFEST & SITEMAP VERIFICATION REPORT")
print("=" * 70)

# Read manifest
manifest_path = Path("blog/posts/manifest.json")
with open(manifest_path, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

print(f"\n[MANIFEST SUMMARY]")
print(f"   Total Posts: {manifest['totalPosts']}")
print(f"   Last Updated: {manifest['lastUpdated']}")

# Read sitemap
sitemap_path = Path("sitemap.xml")
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

# Extract blog post URLs from sitemap
blog_post_urls = re.findall(r'<loc>https://tidiful\.com/blog/posts/([^<]+)</loc>', sitemap_content)
static_urls = re.findall(r'<loc>https://tidiful\.com/blog/static/([^<]+)</loc>', sitemap_content)

print(f"\n[SITEMAP SUMMARY]")
print(f"   Blog Post URLs: {len(blog_post_urls)}")
print(f"   Static URLs: {len(static_urls)}")

# Check manifest posts
print(f"\n[MANIFEST POSTS] ({len(manifest['posts'])})")
manifest_filenames = []
for i, post in enumerate(manifest['posts'], 1):
    filename = post['filename']
    manifest_filenames.append(filename)
    has_excerpt = bool(post.get('excerpt', '').strip())
    excerpt_status = "[OK]" if has_excerpt else "[MISSING]"
    print(f"   {i:2d}. {excerpt_status} {filename}")
    print(f"       Title: {post['title'][:60]}...")
    print(f"       Date: {post['date']}")

# Check sitemap coverage
print(f"\n[SITEMAP COVERAGE CHECK]")
missing_in_sitemap = []
for post in manifest['posts']:
    filename = post['filename']
    if filename not in blog_post_urls:
        missing_in_sitemap.append(filename)
        print(f"   [MISSING] {filename}")

if not missing_in_sitemap:
    print(f"   [OK] All manifest posts are in sitemap")

# Check for orphaned sitemap entries
print(f"\n[ORPHANED SITEMAP ENTRIES]")
orphaned = []
for url in blog_post_urls:
    if url not in manifest_filenames:
        orphaned.append(url)
        print(f"   [ORPHAN] {url}")

if not orphaned:
    print(f"   [OK] No orphaned entries in sitemap")

# Check excerpts
print(f"\n[EXCERPT STATUS]")
posts_with_excerpt = sum(1 for post in manifest['posts'] if post.get('excerpt', '').strip())
posts_without_excerpt = len(manifest['posts']) - posts_with_excerpt
print(f"   Posts with excerpts: {posts_with_excerpt}/{len(manifest['posts'])}")
if posts_without_excerpt > 0:
    print(f"   Posts missing excerpts: {posts_without_excerpt}")
    for post in manifest['posts']:
        if not post.get('excerpt', '').strip():
            print(f"      - {post['filename']}")
else:
    print(f"   [OK] All posts have excerpts!")

# Summary
print(f"\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
issues = []
if missing_in_sitemap:
    issues.append(f"❌ {len(missing_in_sitemap)} posts missing from sitemap")
if orphaned:
    issues.append(f"⚠️  {len(orphaned)} orphaned entries in sitemap")
if posts_without_excerpt:
    issues.append(f"❌ {posts_without_excerpt} posts missing excerpts")

if not issues:
    print("[SUCCESS] Everything is in sync!")
    print(f"   - All {manifest['totalPosts']} posts in manifest")
    print(f"   - All posts have excerpts")
    print(f"   - All posts in sitemap")
    print(f"   - No orphaned entries")
else:
    for issue in issues:
        print(f"   {issue}")

print("=" * 70)

