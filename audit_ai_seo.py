#!/usr/bin/env python3
"""
Audit all blog posts for AI-SEO optimization
Identifies missing schema markup, FAQs, and optimization opportunities
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List

class AISEOAuditor:
    def __init__(self):
        self.posts_dir = Path("blog/posts")
        self.results = []
        
    def audit_all_posts(self):
        """Audit all blog posts"""
        if not self.posts_dir.exists():
            print(f"Posts directory not found: {self.posts_dir}")
            return
        
        html_files = list(self.posts_dir.glob("*.html"))
        print(f"Found {len(html_files)} blog posts to audit\n")
        
        for html_file in html_files:
            result = self.audit_post(html_file)
            self.results.append(result)
        
        self.print_summary()
        self.save_report()
    
    def audit_post(self, html_file: Path) -> Dict:
        """Audit a single blog post"""
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        result = {
            'filename': html_file.name,
            'issues': [],
            'warnings': [],
            'passed': [],
            'score': 0
        }
        
        # Check for FAQPage schema
        if '"@type":\s*"FAQPage"' in content or '"@type":"FAQPage"' in content:
            result['passed'].append('FAQPage schema found')
        else:
            result['issues'].append('Missing FAQPage schema')
        
        # Check for HowTo schema
        if '"@type":\s*"HowTo"' in content or '"@type":"HowTo"' in content:
            result['passed'].append('HowTo schema found')
        else:
            # Check if it's a tutorial/guide post
            if any(word in content.lower() for word in ['how to', 'step', 'guide', 'tutorial']):
                result['warnings'].append('Missing HowTo schema (recommended for guides)')
        
        # Check for FAQ section in content
        faq_indicators = ['FAQ', 'frequently asked', 'common questions', 'Q&A']
        has_faq_content = any(re.search(indicator, content, re.IGNORECASE) for indicator in faq_indicators)
        if has_faq_content:
            result['passed'].append('FAQ content found')
        else:
            result['warnings'].append('No FAQ section in content')
        
        # Check for question-based headings
        question_headings = re.findall(r'<h[2-4][^>]*>.*\?.*</h[2-4]>', content, re.IGNORECASE)
        if len(question_headings) >= 3:
            result['passed'].append(f'Found {len(question_headings)} question-based headings')
        elif len(question_headings) > 0:
            result['warnings'].append(f'Only {len(question_headings)} question-based headings (recommended: 3+)')
        else:
            result['warnings'].append('No question-based headings found')
        
        # Check for BlogPosting schema
        if '"@type":\s*"BlogPosting"' in content or '"@type":"BlogPosting"' in content:
            result['passed'].append('BlogPosting schema found')
        else:
            result['issues'].append('Missing BlogPosting schema')
        
        # Check for Organization schema
        if '"@type":\s*"Organization"' in content or '"@type":"Organization"' in content:
            result['passed'].append('Organization schema found')
        else:
            result['warnings'].append('Missing Organization schema')
        
        # Check meta description length
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', content, re.IGNORECASE)
        if desc_match:
            desc_length = len(desc_match.group(1))
            if 150 <= desc_length <= 160:
                result['passed'].append(f'Meta description length optimal ({desc_length} chars)')
            else:
                result['warnings'].append(f'Meta description length: {desc_length} chars (recommended: 150-160)')
        
        # Check for conversational keywords
        conversational_keywords = ['how to', 'what is', 'why', 'when', 'where', 'can i', 'should i']
        conversational_count = sum(1 for keyword in conversational_keywords if re.search(keyword, content, re.IGNORECASE))
        if conversational_count >= 3:
            result['passed'].append('Conversational language found')
        else:
            result['warnings'].append('Limited conversational keywords')
        
        # Calculate score
        total_checks = len(result['passed']) + len(result['warnings']) + len(result['issues'])
        if total_checks > 0:
            result['score'] = int((len(result['passed']) * 100 + len(result['warnings']) * 50) / total_checks)
        
        return result
    
    def print_summary(self):
        """Print audit summary"""
        print("=" * 70)
        print("AI-SEO AUDIT SUMMARY")
        print("=" * 70)
        print()
        
        # Sort by score (lowest first)
        sorted_results = sorted(self.results, key=lambda x: x['score'])
        
        print("POSTS NEEDING IMMEDIATE ATTENTION (Score < 60):")
        print("-" * 70)
        critical = [r for r in sorted_results if r['score'] < 60]
        if critical:
            for result in critical:
                print(f"\n{result['filename']} (Score: {result['score']}/100)")
                if result['issues']:
                    print("  ISSUES:")
                    for issue in result['issues']:
                        print(f"    - {issue}")
        else:
            print("  None! Great job!")
        print()
        
        print("POSTS WITH WARNINGS (Score 60-80):")
        print("-" * 70)
        warnings = [r for r in sorted_results if 60 <= r['score'] < 80]
        if warnings:
            for result in warnings:
                print(f"\n{result['filename']} (Score: {result['score']}/100)")
                if result['warnings']:
                    for warning in result['warnings'][:3]:  # Show top 3
                        print(f"    ! {warning}")
        else:
            print("  None!")
        print()
        
        print("OVERALL STATISTICS:")
        print("-" * 70)
        total_posts = len(self.results)
        avg_score = sum(r['score'] for r in self.results) / total_posts if total_posts > 0 else 0
        posts_with_faq_schema = sum(1 for r in self.results if 'FAQPage schema found' in r['passed'])
        posts_with_howto_schema = sum(1 for r in self.results if 'HowTo schema found' in r['passed'])
        posts_with_faq_content = sum(1 for r in self.results if 'FAQ content found' in r['passed'])
        
        print(f"Total Posts Audited: {total_posts}")
        print(f"Average Score: {avg_score:.1f}/100")
        print(f"Posts with FAQ Schema: {posts_with_faq_schema}/{total_posts} ({posts_with_faq_schema*100//total_posts}%)")
        print(f"Posts with HowTo Schema: {posts_with_howto_schema}/{total_posts} ({posts_with_howto_schema*100//total_posts}%)")
        print(f"Posts with FAQ Content: {posts_with_faq_content}/{total_posts} ({posts_with_faq_content*100//total_posts}%)")
        print()
        
        print("TOP PRIORITY ACTIONS:")
        print("-" * 70)
        missing_faq_schema = [r for r in self.results if 'Missing FAQPage schema' in r['issues']]
        missing_faq_content = [r for r in self.results if 'No FAQ section in content' in r['warnings']]
        
        if missing_faq_schema:
            print(f"\n1. Add FAQPage schema to {len(missing_faq_schema)} posts:")
            for result in missing_faq_schema[:5]:
                print(f"   - {result['filename']}")
        
        if missing_faq_content:
            print(f"\n2. Add FAQ sections to {len(missing_faq_content)} posts:")
            for result in missing_faq_content[:5]:
                print(f"   - {result['filename']}")
        
        print()
        print("=" * 70)
    
    def save_report(self):
        """Save detailed report to file"""
        report_file = Path("ai_seo_audit_report.json")
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump({
                'audit_date': str(Path().cwd()),
                'total_posts': len(self.results),
                'average_score': sum(r['score'] for r in self.results) / len(self.results) if self.results else 0,
                'results': self.results
            }, f, indent=2)
        
        print(f"\nDetailed report saved to: {report_file}")

def main():
    auditor = AISEOAuditor()
    auditor.audit_all_posts()

if __name__ == "__main__":
    main()

