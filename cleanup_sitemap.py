#!/usr/bin/env python3
"""Clean up sitemap.xml by removing excessive empty lines"""

from pathlib import Path

def cleanup_sitemap():
    sitemap_file = Path("sitemap.xml")
    
    with open(sitemap_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Remove excessive empty lines (keep max 1 empty line between sections)
    cleaned_lines = []
    prev_empty = False
    for line in lines:
        if line.strip():  # Non-empty line
            cleaned_lines.append(line)
            prev_empty = False
        elif not prev_empty:  # First empty line, keep it
            cleaned_lines.append(line)
            prev_empty = True
        # Skip subsequent empty lines
    
    with open(sitemap_file, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)
    
    print(f"[OK] Cleaned up sitemap.xml (removed excessive empty lines)")

if __name__ == "__main__":
    cleanup_sitemap()

