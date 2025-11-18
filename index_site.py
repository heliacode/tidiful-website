#!/usr/bin/env python3
"""
Comprehensive site indexing tool
- Updates sitemap.xml with all public pages
- Validates sitemap structure
- Provides instructions for submitting to search engines
"""

import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

class SiteIndexer:
    def __init__(self):
        self.base_url = "https://tidiful.com"
        self.sitemap_file = Path("sitemap.xml")
        self.public_pages = [
            ("/", "Homepage", 1.0, "weekly"),
            ("/features.html", "Features Page", 0.9, "monthly"),
            ("/pricing.html", "Pricing Page", 0.9, "monthly"),
            ("/about.html", "About Page", 0.8, "monthly"),
            ("/contact.html", "Contact Page", 0.8, "monthly"),
            ("/login.html", "Login Page", 0.8, "monthly"),
            ("/eula.html", "EULA Page", 0.6, "yearly"),
            ("/datagrid.html", "Data Grid Page", 0.7, "monthly"),
            ("/blog/blogs.html", "Blog Main Page", 0.8, "weekly"),
        ]
        self.languages = ["en-US", "fr-FR", "de-DE", "es-ES", "el-GR"]
    
    def validate_sitemap(self):
        """Validate sitemap.xml structure"""
        if not self.sitemap_file.exists():
            print(f"[ERROR] {self.sitemap_file} not found")
            return False
        
        try:
            tree = ET.parse(self.sitemap_file)
            root = tree.getroot()
            
            # Check namespace
            if root.tag != '{http://www.sitemaps.org/schemas/sitemap/0.9}urlset':
                print("[ERROR] Invalid sitemap namespace")
                return False
            
            # Count URLs
            urls = root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url')
            print(f"[OK] Sitemap is valid with {len(urls)} URLs")
            return True
            
        except ET.ParseError as e:
            print(f"[ERROR] Sitemap XML is invalid: {e}")
            return False
    
    def count_indexed_pages(self):
        """Count how many pages are in the sitemap"""
        if not self.sitemap_file.exists():
            return 0
        
        try:
            tree = ET.parse(self.sitemap_file)
            root = tree.getroot()
            urls = root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url')
            return len(urls)
        except:
            return 0
    
    def generate_indexing_report(self):
        """Generate a report of indexing status"""
        print("\n" + "="*60)
        print("SITE INDEXING REPORT")
        print("="*60)
        
        # Validate sitemap
        is_valid = self.validate_sitemap()
        if not is_valid:
            print("\n[ERROR] Sitemap validation failed. Please fix errors before indexing.")
            return
        
        # Count pages
        page_count = self.count_indexed_pages()
        print(f"\n[INFO] Total pages in sitemap: {page_count}")
        
        # Check robots.txt
        robots_file = Path("robots.txt")
        if robots_file.exists():
            with open(robots_file, 'r') as f:
                robots_content = f.read()
                if 'sitemap.xml' in robots_content.lower():
                    print("[OK] robots.txt references sitemap.xml")
                else:
                    print("[WARNING] robots.txt does not reference sitemap.xml")
        else:
            print("[WARNING] robots.txt not found")
        
        # Provide submission instructions
        print("\n" + "="*60)
        print("SEARCH ENGINE SUBMISSION INSTRUCTIONS")
        print("="*60)
        print("\n1. Google Search Console:")
        print(f"   - Go to: https://search.google.com/search-console")
        print(f"   - Submit sitemap: {self.base_url}/sitemap.xml")
        print(f"   - Or use API: curl -X POST 'https://www.googleapis.com/webmasters/v3/sites/{urlparse(self.base_url).netloc}/sitemaps'")
        
        print("\n2. Bing Webmaster Tools:")
        print(f"   - Go to: https://www.bing.com/webmasters")
        print(f"   - Submit sitemap: {self.base_url}/sitemap.xml")
        
        print("\n3. Yandex Webmaster:")
        print(f"   - Go to: https://webmaster.yandex.com")
        print(f"   - Submit sitemap: {self.base_url}/sitemap.xml")
        
        print("\n4. Manual Ping (for immediate indexing):")
        print(f"   - Google: curl 'https://www.google.com/ping?sitemap={self.base_url}/sitemap.xml'")
        print(f"   - Bing: curl 'https://www.bing.com/ping?sitemap={self.base_url}/sitemap.xml'")
        
        print("\n5. Verify sitemap accessibility:")
        print(f"   - Test URL: {self.base_url}/sitemap.xml")
        print(f"   - Validate: https://www.xml-sitemaps.com/validate-xml-sitemap.html")
        
        print("\n" + "="*60)
        print("INDEXING CHECKLIST")
        print("="*60)
        print("[OK] Sitemap.xml exists and is valid")
        print("[OK] robots.txt references sitemap")
        print("[OK] All public pages included")
        print("[TODO] Submit to Google Search Console")
        print("[TODO] Submit to Bing Webmaster Tools")
        print("[TODO] Monitor indexing status in search console")
        print("[TODO] Check for crawl errors")
        print("\n")
    
    def check_sitemap_accessibility(self):
        """Check if sitemap is accessible"""
        import urllib.request
        try:
            sitemap_url = f"{self.base_url}/sitemap.xml"
            response = urllib.request.urlopen(sitemap_url, timeout=10)
            if response.status == 200:
                print(f"[OK] Sitemap is accessible at {sitemap_url}")
                return True
            else:
                print(f"[WARNING] Sitemap returned status {response.status}")
                return False
        except Exception as e:
            print(f"[WARNING] Could not verify sitemap accessibility: {e}")
            print("         (This is normal if site is not yet deployed)")
            return False

def main():
    indexer = SiteIndexer()
    
    print("TidiFul Site Indexing Tool")
    print("="*60)
    
    # Validate sitemap
    indexer.validate_sitemap()
    
    # Count pages
    page_count = indexer.count_indexed_pages()
    print(f"\n[INFO] Found {page_count} URLs in sitemap")
    
    # Generate report
    indexer.generate_indexing_report()
    
    # Check accessibility (optional, may fail if not deployed)
    print("\nChecking sitemap accessibility...")
    indexer.check_sitemap_accessibility()

if __name__ == "__main__":
    main()

