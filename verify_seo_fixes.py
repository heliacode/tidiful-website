#!/usr/bin/env python3
import os

posts = [f for f in os.listdir('blog/posts') if f.endswith('.html')]
print(f'Total posts: {len(posts)}')

breadcrumb = sum(1 for p in posts if 'BreadcrumbList' in open(f'blog/posts/{p}', encoding='utf-8').read())
hreflang = sum(1 for p in posts if 'hreflang' in open(f'blog/posts/{p}', encoding='utf-8').read())
faq = sum(1 for p in posts if 'FAQPage' in open(f'blog/posts/{p}', encoding='utf-8').read())
inlang = sum(1 for p in posts if '"inLanguage"' in open(f'blog/posts/{p}', encoding='utf-8').read())
wordcount = sum(1 for p in posts if '"wordCount"' in open(f'blog/posts/{p}', encoding='utf-8').read())
modified = sum(1 for p in posts if 'article:modified_time' in open(f'blog/posts/{p}', encoding='utf-8').read())

print(f'BreadcrumbList: {breadcrumb}/{len(posts)}')
print(f'Hreflang tags: {hreflang}/{len(posts)}')
print(f'FAQ schema: {faq}/{len(posts)}')
print(f'inLanguage: {inlang}/{len(posts)}')
print(f'wordCount: {wordcount}/{len(posts)}')
print(f'article:modified_time: {modified}/{len(posts)}')

