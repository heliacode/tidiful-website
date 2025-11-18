#!/usr/bin/env python3
"""Check which blog posts have excerpts"""

import re
from pathlib import Path

posts_dir = Path("blog/posts")
html_files = list(posts_dir.glob("*.html"))

print(f"Total blog posts: {len(html_files)}\n")

posts_with_excerpt = []
posts_without_excerpt = []

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if re.search(r'<meta\s+name=["\']excerpt["\']', content, re.IGNORECASE):
        posts_with_excerpt.append(html_file.name)
    else:
        posts_without_excerpt.append(html_file.name)

print(f"Posts WITH excerpts: {len(posts_with_excerpt)}")
print(f"Posts WITHOUT excerpts: {len(posts_without_excerpt)}\n")

if posts_without_excerpt:
    print("Posts missing excerpts:")
    for post in posts_without_excerpt:
        print(f"  - {post}")
else:
    print("[SUCCESS] All blog posts have excerpts!")

