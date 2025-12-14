import json

with open('blog/posts/manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

print(f"Total posts in manifest: {len(manifest['posts'])}")
print("\nPost filenames:")
for i, post in enumerate(manifest['posts'], 1):
    print(f"{i}. {post['filename']}")

