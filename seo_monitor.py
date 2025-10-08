#!/usr/bin/env python3
"""
SEO Monitoring Script for TidiFul Website
Checks basic SEO elements and generates reports
"""

import os
import json
import requests
from datetime import datetime
from urllib.parse import urljoin

class SEOMonitor:
    def __init__(self, base_url="https://tidiful.com"):
        self.base_url = base_url
        self.pages = [
            "/",
            "/pricing.html", 
            "/blog/blogs.html",
            "/blog/posts/image-to-excel-complete-guide.html",
            "/blog/posts/invoice-to-excel-complete-guide.html",
            "/blog/posts/pdf-to-csv-complete-guide.html",
            "/blog/posts/what-is-pdf-to-csv-conversion.html",
            "/blog/posts/how-to-scan-pdf-documents-like-a-pro-a-complete-guide-for-business-professionals.html"
        ]
        self.languages = ["en-US", "fr-FR", "de-DE", "es-ES", "el-GR"]
        
    def check_page_seo(self, page_path, lang="en-US"):
        """Check SEO elements for a specific page"""
        url = f"{self.base_url}{page_path}"
        if lang != "en-US":
            url += f"?lang={lang}"
            
        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                return {"error": f"HTTP {response.status_code}"}
                
            content = response.text
            
            # Check for essential SEO elements
            seo_checks = {
                "title": self.extract_title(content),
                "meta_description": self.extract_meta_description(content),
                "h1_tags": self.extract_h1_tags(content),
                "hreflang_tags": self.extract_hreflang_tags(content),
                "canonical_url": self.extract_canonical(content),
                "structured_data": self.extract_structured_data(content),
                "internal_links": self.extract_internal_links(content),
                "images_with_alt": self.check_image_alt_tags(content),
                "page_size": len(content),
                "load_time": response.elapsed.total_seconds()
            }
            
            return seo_checks
            
        except Exception as e:
            return {"error": str(e)}
    
    def extract_title(self, content):
        """Extract page title"""
        import re
        match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        return match.group(1) if match else None
    
    def extract_meta_description(self, content):
        """Extract meta description"""
        import re
        match = re.search(r'<meta name="description" content="(.*?)"', content, re.IGNORECASE)
        return match.group(1) if match else None
    
    def extract_h1_tags(self, content):
        """Extract all H1 tags"""
        import re
        matches = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
        return [match.strip() for match in matches]
    
    def extract_hreflang_tags(self, content):
        """Extract hreflang tags"""
        import re
        matches = re.findall(r'<link[^>]*hreflang="([^"]*)"[^>]*href="([^"]*)"', content, re.IGNORECASE)
        return matches
    
    def extract_canonical(self, content):
        """Extract canonical URL"""
        import re
        match = re.search(r'<link[^>]*rel="canonical"[^>]*href="([^"]*)"', content, re.IGNORECASE)
        return match.group(1) if match else None
    
    def extract_structured_data(self, content):
        """Extract structured data (JSON-LD)"""
        import re
        matches = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.IGNORECASE | re.DOTALL)
        return len(matches)
    
    def extract_internal_links(self, content):
        """Extract internal links"""
        import re
        matches = re.findall(r'<a[^>]*href="([^"]*)"', content, re.IGNORECASE)
        internal_links = [link for link in matches if link.startswith('/') or 'tidiful.com' in link]
        return len(internal_links)
    
    def check_image_alt_tags(self, content):
        """Check images with alt tags"""
        import re
        img_tags = re.findall(r'<img[^>]*>', content, re.IGNORECASE)
        images_with_alt = [img for img in img_tags if 'alt=' in img]
        return len(images_with_alt)
    
    def generate_report(self):
        """Generate comprehensive SEO report"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "base_url": self.base_url,
            "pages_checked": len(self.pages),
            "languages_checked": len(self.languages),
            "results": {}
        }
        
        for page in self.pages:
            report["results"][page] = {}
            for lang in self.languages:
                print(f"Checking {page} ({lang})...")
                seo_data = self.check_page_seo(page, lang)
                report["results"][page][lang] = seo_data
        
        return report
    
    def save_report(self, report, filename="seo_report.json"):
        """Save report to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"Report saved to {filename}")
    
    def print_summary(self, report):
        """Print summary of SEO findings"""
        print("\n" + "="*60)
        print("TIDIFUL SEO MONITORING SUMMARY")
        print("="*60)
        
        total_pages = len(report["results"])
        total_checks = sum(len(langs) for langs in report["results"].values())
        
        print(f"Pages checked: {total_pages}")
        print(f"Total checks: {total_checks}")
        print(f"Languages: {', '.join(self.languages)}")
        
        # Check for common issues
        issues = []
        for page, langs in report["results"].items():
            for lang, data in langs.items():
                if "error" in data:
                    issues.append(f"{page} ({lang}): {data['error']}")
                else:
                    if not data.get("title"):
                        issues.append(f"{page} ({lang}): Missing title")
                    if not data.get("meta_description"):
                        issues.append(f"{page} ({lang}): Missing meta description")
                    if not data.get("h1_tags"):
                        issues.append(f"{page} ({lang}): Missing H1 tags")
                    if not data.get("hreflang_tags"):
                        issues.append(f"{page} ({lang}): Missing hreflang tags")
        
        if issues:
            print(f"\nIssues found: {len(issues)}")
            for issue in issues[:10]:  # Show first 10 issues
                print(f"  - {issue}")
            if len(issues) > 10:
                print(f"  ... and {len(issues) - 10} more issues")
        else:
            print("\n✅ No major SEO issues found!")
        
        print("\n" + "="*60)

def main():
    """Main function to run SEO monitoring"""
    monitor = SEOMonitor()
    
    print("Starting TidiFul SEO monitoring...")
    report = monitor.generate_report()
    
    # Save detailed report
    monitor.save_report(report)
    
    # Print summary
    monitor.print_summary(report)
    
    # Save summary to text file
    with open("seo_summary.txt", "w") as f:
        f.write(f"TidiFul SEO Monitoring Summary\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Pages checked: {len(report['results'])}\n")
        f.write(f"Languages: {', '.join(monitor.languages)}\n")
        f.write("\nFor detailed results, see seo_report.json\n")

if __name__ == "__main__":
    main()
