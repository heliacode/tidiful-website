#!/usr/bin/env python3
"""
Comprehensive SEO and AI-SEO validation for blog posts
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple

class BlogSEOValidator:
    def __init__(self, blog_file: str):
        self.blog_file = Path(blog_file)
        self.issues = []
        self.warnings = []
        self.passed = []
        
    def validate(self) -> Tuple[bool, Dict]:
        """Run all SEO validations"""
        if not self.blog_file.exists():
            self.issues.append(f"Blog file not found: {self.blog_file}")
            return False, self.get_results()
        
        with open(self.blog_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Run all validations
        self.check_meta_tags(content)
        self.check_open_graph(content)
        self.check_twitter_cards(content)
        self.check_structured_data(content)
        self.check_canonical_url(content)
        self.check_title_tag(content)
        self.check_description(content)
        self.check_keywords(content)
        self.check_ai_seo_elements(content)
        self.check_internal_links(content)
        self.check_headings(content)
        self.check_images(content)
        
        success = len(self.issues) == 0
        return success, self.get_results()
    
    def check_meta_tags(self, content: str):
        """Check required meta tags"""
        required_meta = {
            'charset': r'<meta\s+charset=["\']UTF-8["\']',
            'viewport': r'<meta\s+name=["\']viewport["\']',
            'description': r'<meta\s+name=["\']description["\']',
            'keywords': r'<meta\s+name=["\']keywords["\']',
            'author': r'<meta\s+name=["\']author["\']',
            'robots': r'<meta\s+name=["\']robots["\']',
            'date': r'<meta\s+name=["\']date["\']',
            'excerpt': r'<meta\s+name=["\']excerpt["\']'
        }
        
        for tag, pattern in required_meta.items():
            if re.search(pattern, content, re.IGNORECASE):
                self.passed.append(f"Meta tag '{tag}' found")
            else:
                self.issues.append(f"Missing required meta tag: {tag}")
    
    def check_open_graph(self, content: str):
        """Check Open Graph tags"""
        og_tags = {
            'og:type': r'<meta\s+property=["\']og:type["\']',
            'og:title': r'<meta\s+property=["\']og:title["\']',
            'og:description': r'<meta\s+property=["\']og:description["\']',
            'og:url': r'<meta\s+property=["\']og:url["\']',
            'og:image': r'<meta\s+property=["\']og:image["\']',
            'og:site_name': r'<meta\s+property=["\']og:site_name["\']',
            'article:published_time': r'<meta\s+property=["\']article:published_time["\']'
        }
        
        for tag, pattern in og_tags.items():
            if re.search(pattern, content, re.IGNORECASE):
                self.passed.append(f"Open Graph tag '{tag}' found")
            else:
                self.warnings.append(f"Missing Open Graph tag: {tag}")
    
    def check_twitter_cards(self, content: str):
        """Check Twitter Card tags"""
        twitter_tags = {
            'twitter:card': r'<meta\s+property=["\']twitter:card["\']',
            'twitter:title': r'<meta\s+property=["\']twitter:title["\']',
            'twitter:description': r'<meta\s+property=["\']twitter:description["\']',
            'twitter:image': r'<meta\s+property=["\']twitter:image["\']'
        }
        
        for tag, pattern in twitter_tags.items():
            if re.search(pattern, content, re.IGNORECASE):
                self.passed.append(f"Twitter Card tag '{tag}' found")
            else:
                self.warnings.append(f"Missing Twitter Card tag: {tag}")
    
    def check_structured_data(self, content: str):
        """Check structured data (Schema.org)"""
        # Check for JSON-LD
        if re.search(r'<script\s+type=["\']application/ld\+json["\']', content, re.IGNORECASE):
            self.passed.append("JSON-LD structured data found")
            
            # Check for BlogPosting schema
            if '"@type":\s*"BlogPosting"' in content or '"@type":"BlogPosting"' in content:
                self.passed.append("BlogPosting schema found")
            else:
                self.issues.append("Missing BlogPosting schema type")
            
            # Check for Organization schema
            if '"@type":\s*"Organization"' in content or '"@type":"Organization"' in content:
                self.passed.append("Organization schema found")
            else:
                self.warnings.append("Missing Organization schema")
        else:
            self.issues.append("Missing JSON-LD structured data")
        
        # Check for FAQ schema (important for AI-SEO)
        if '"@type":\s*"FAQPage"' in content or '"@type":"FAQPage"' in content:
            self.passed.append("FAQPage schema found (excellent for AI-SEO)")
        else:
            self.warnings.append("Missing FAQPage schema (recommended for AI-SEO)")
        
        # Check for HowTo schema (good for step-by-step guides)
        if '"@type":\s*"HowTo"' in content or '"@type":"HowTo"' in content:
            self.passed.append("HowTo schema found (excellent for AI-SEO)")
        else:
            self.warnings.append("Missing HowTo schema (recommended for step-by-step guides)")
    
    def check_canonical_url(self, content: str):
        """Check canonical URL"""
        if re.search(r'<link\s+rel=["\']canonical["\']', content, re.IGNORECASE):
            self.passed.append("Canonical URL found")
        else:
            self.issues.append("Missing canonical URL")
    
    def check_title_tag(self, content: str):
        """Check title tag"""
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        if title_match:
            title = title_match.group(1).strip()
            if len(title) > 0:
                if len(title) <= 60:
                    self.passed.append(f"Title tag found: '{title[:50]}...' (good length)")
                else:
                    self.warnings.append(f"Title tag may be too long ({len(title)} chars, recommended: 60)")
                
                if 'TidiFul' in title or 'Tidiful' in title:
                    self.passed.append("Title includes brand name")
                else:
                    self.warnings.append("Title doesn't include brand name")
            else:
                self.issues.append("Title tag is empty")
        else:
            self.issues.append("Missing title tag")
    
    def check_description(self, content: str):
        """Check meta description"""
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', content, re.IGNORECASE)
        if desc_match:
            desc = desc_match.group(1)
            length = len(desc)
            if 150 <= length <= 160:
                self.passed.append(f"Meta description length is optimal ({length} chars)")
            elif length < 150:
                self.warnings.append(f"Meta description may be too short ({length} chars, recommended: 150-160)")
            else:
                self.warnings.append(f"Meta description may be too long ({length} chars, recommended: 150-160)")
        else:
            self.issues.append("Could not extract meta description")
    
    def check_keywords(self, content: str):
        """Check keywords meta tag"""
        keywords_match = re.search(r'<meta\s+name=["\']keywords["\']\s+content=["\']([^"\']+)["\']', content, re.IGNORECASE)
        if keywords_match:
            keywords = keywords_match.group(1)
            keyword_count = len([k.strip() for k in keywords.split(',') if k.strip()])
            if keyword_count >= 5:
                self.passed.append(f"Keywords found ({keyword_count} keywords)")
            else:
                self.warnings.append(f"Few keywords found ({keyword_count}, recommended: 5+)")
        else:
            self.warnings.append("Keywords meta tag not found")
    
    def check_ai_seo_elements(self, content: str):
        """Check AI-SEO specific elements"""
        # Check for question-based headings (good for AI assistants)
        question_headings = re.findall(r'<h[2-4][^>]*>.*\?.*</h[2-4]>', content, re.IGNORECASE)
        if len(question_headings) >= 3:
            self.passed.append(f"Found {len(question_headings)} question-based headings (excellent for AI-SEO)")
        elif len(question_headings) > 0:
            self.warnings.append(f"Found only {len(question_headings)} question-based headings (recommended: 3+)")
        else:
            self.warnings.append("No question-based headings found (recommended for AI-SEO)")
        
        # Check for step-by-step content
        step_patterns = [
            r'step\s+\d+',
            r'step-by-step',
            r'how\s+to',
            r'guide',
            r'tutorial'
        ]
        step_count = sum(1 for pattern in step_patterns if re.search(pattern, content, re.IGNORECASE))
        if step_count >= 2:
            self.passed.append("Step-by-step content found (good for AI-SEO)")
        else:
            self.warnings.append("Limited step-by-step content (recommended for AI-SEO)")
        
        # Check for FAQ sections
        faq_indicators = ['FAQ', 'frequently asked', 'common questions', 'Q&A']
        faq_count = sum(1 for indicator in faq_indicators if re.search(indicator, content, re.IGNORECASE))
        if faq_count > 0:
            self.passed.append("FAQ content found (excellent for AI-SEO)")
        else:
            self.warnings.append("No FAQ content found (highly recommended for AI-SEO)")
    
    def check_internal_links(self, content: str):
        """Check for internal links"""
        internal_links = re.findall(r'<a[^>]+href=["\'](?:\.\./|\./|/|https?://tidiful\.com)[^"\']+["\']', content, re.IGNORECASE)
        if len(internal_links) >= 3:
            self.passed.append(f"Found {len(internal_links)} internal links (good for SEO)")
        elif len(internal_links) > 0:
            self.warnings.append(f"Found only {len(internal_links)} internal links (recommended: 3+)")
        else:
            self.warnings.append("No internal links found (recommended for SEO)")
    
    def check_headings(self, content: str):
        """Check heading structure"""
        h1_count = len(re.findall(r'<h1[^>]*>', content, re.IGNORECASE))
        h2_count = len(re.findall(r'<h2[^>]*>', content, re.IGNORECASE))
        h3_count = len(re.findall(r'<h3[^>]*>', content, re.IGNORECASE))
        
        if h1_count == 1:
            self.passed.append("Single H1 tag found (correct)")
        elif h1_count == 0:
            self.issues.append("No H1 tag found")
        else:
            self.warnings.append(f"Multiple H1 tags found ({h1_count}, recommended: 1)")
        
        if h2_count >= 3:
            self.passed.append(f"Found {h2_count} H2 tags (good structure)")
        else:
            self.warnings.append(f"Found only {h2_count} H2 tags (recommended: 3+)")
    
    def check_images(self, content: str):
        """Check image alt text"""
        images = re.findall(r'<img[^>]+>', content, re.IGNORECASE)
        images_with_alt = re.findall(r'<img[^>]+alt=["\'][^"\']+["\']', content, re.IGNORECASE)
        
        if len(images) > 0:
            if len(images_with_alt) == len(images):
                self.passed.append(f"All {len(images)} images have alt text")
            else:
                self.warnings.append(f"{len(images) - len(images_with_alt)} images missing alt text")
        else:
            self.warnings.append("No images found (images can improve engagement)")
    
    def get_results(self) -> Dict:
        """Get validation results"""
        return {
            'file': str(self.blog_file),
            'passed': len(self.passed),
            'warnings': len(self.warnings),
            'issues': len(self.issues),
            'details': {
                'passed': self.passed,
                'warnings': self.warnings,
                'issues': self.issues
            },
            'score': self.calculate_score()
        }
    
    def calculate_score(self) -> int:
        """Calculate SEO score (0-100)"""
        total_checks = len(self.passed) + len(self.warnings) + len(self.issues)
        if total_checks == 0:
            return 0
        
        # Passed = 100%, Warnings = 50%, Issues = 0%
        score = (len(self.passed) * 100 + len(self.warnings) * 50) / total_checks
        return int(score)

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python validate_blog_seo.py <blog_file.html>")
        sys.exit(1)
    
    blog_file = sys.argv[1]
    validator = BlogSEOValidator(blog_file)
    success, results = validator.validate()
    
    print(f"\n{'='*60}")
    print(f"SEO Validation Report: {results['file']}")
    print(f"{'='*60}\n")
    
    print(f"SEO Score: {results['score']}/100\n")
    
    if results['details']['passed']:
        print(f"[PASSED] ({results['passed']}):")
        for item in results['details']['passed']:
            print(f"   + {item}")
        print()
    
    if results['details']['warnings']:
        print(f"[WARNINGS] ({results['warnings']}):")
        for item in results['details']['warnings']:
            print(f"   ! {item}")
        print()
    
    if results['details']['issues']:
        print(f"[ISSUES] ({results['issues']}):")
        for item in results['details']['issues']:
            print(f"   - {item}")
        print()
    
    print(f"{'='*60}")
    if success:
        print("[SUCCESS] SEO validation PASSED")
    else:
        print("[FAILED] SEO validation FAILED - Please fix issues above")
    print(f"{'='*60}\n")
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()

