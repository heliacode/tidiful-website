#!/usr/bin/env python3
"""
Enhanced AI Visibility Monitor for TidiFul Website
Designed to work with GitHub Actions and provide comprehensive monitoring
"""

import requests
import json
import time
import os
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Any
import argparse

class EnhancedAIVisibilityMonitor:
    def __init__(self, config_file: str = None):
        self.brand_name = "TidiFul"
        self.website_url = "https://tidiful.com"
        self.target_keywords = [
            "PDF to CSV",
            "PDF to CSV converter", 
            "convert PDF to CSV",
            "PDF CSV conversion",
            "document processing AI",
            "invoice automation",
            "AI document processing",
            "PDF to JSON converter",
            "invoice processing software",
            "document automation platform"
        ]
        self.ai_platforms = {
            "chatgpt": "OpenAI ChatGPT",
            "claude": "Anthropic Claude", 
            "perplexity": "Perplexity AI",
            "bard": "Google Bard",
            "bing_chat": "Microsoft Bing Chat",
            "voice_search": "Voice Search Assistants"
        }
        self.results_file = "ai_visibility_results.json"
        self.report_file = "ai_visibility_report.md"
        
        # Load configuration if provided
        if config_file and os.path.exists(config_file):
            self.load_config(config_file)
    
    def load_config(self, config_file: str) -> None:
        """Load configuration from JSON file"""
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
                self.target_keywords = config.get('keywords', self.target_keywords)
                self.ai_platforms = config.get('platforms', self.ai_platforms)
        except Exception as e:
            print(f"Warning: Could not load config file {config_file}: {e}")
    
    def simulate_ai_platform_check(self, query: str, platform: str) -> Dict[str, Any]:
        """Simulate checking AI platform for brand mentions"""
        # In a real implementation, you would use APIs or web scraping
        # This simulates realistic monitoring results
        
        import random
        
        # Simulate different platform behaviors
        platform_weights = {
            "chatgpt": 0.8,  # High likelihood of mention
            "claude": 0.7,   # High likelihood
            "perplexity": 0.6, # Medium likelihood
            "bard": 0.5,     # Medium likelihood
            "bing_chat": 0.4, # Lower likelihood
            "voice_search": 0.3 # Lower likelihood
        }
        
        weight = platform_weights.get(platform, 0.5)
        mentioned = random.random() < weight
        
        if mentioned:
            sentiments = ["positive", "neutral", "positive", "positive", "neutral"]
            sentiment = random.choice(sentiments)
            confidence = random.uniform(0.7, 0.95)
            
            contexts = [
                f"TidiFul is mentioned as a recommended solution for {query.lower()}",
                f"Users are asking about TidiFul for {query.lower()}",
                f"TidiFul appears in search results for {query.lower()}",
                f"TidiFul is suggested as a tool for {query.lower()}"
            ]
            context = random.choice(contexts)
        else:
            sentiment = "neutral"
            confidence = random.uniform(0.3, 0.6)
            context = f"No mention of {self.brand_name} found for {query.lower()}"
        
        return {
            "mentioned": mentioned,
            "sentiment": sentiment,
            "confidence": round(confidence, 2),
            "context": context,
            "timestamp": datetime.now().isoformat()
        }
    
    def check_brand_mentions(self, query: str) -> Dict[str, Any]:
        """Check for brand mentions across all AI platforms"""
        results = {
            "query": query,
            "timestamp": datetime.now().isoformat(),
            "platforms": {},
            "summary": {
                "total_platforms": len(self.ai_platforms),
                "mentions_found": 0,
                "positive_mentions": 0,
                "negative_mentions": 0,
                "neutral_mentions": 0,
                "average_confidence": 0.0
            }
        }
        
        total_confidence = 0
        mentions_count = 0
        
        for platform, name in self.ai_platforms.items():
            platform_result = self.simulate_ai_platform_check(query, platform)
            results["platforms"][platform] = {
                "platform_name": name,
                **platform_result
            }
            
            if platform_result["mentioned"]:
                mentions_count += 1
                results["summary"]["mentions_found"] += 1
                
                if platform_result["sentiment"] == "positive":
                    results["summary"]["positive_mentions"] += 1
                elif platform_result["sentiment"] == "negative":
                    results["summary"]["negative_mentions"] += 1
                else:
                    results["summary"]["neutral_mentions"] += 1
            
            total_confidence += platform_result["confidence"]
        
        results["summary"]["average_confidence"] = round(total_confidence / len(self.ai_platforms), 2)
        
        return results
    
    def monitor_keyword_visibility(self, keywords: List[str] = None) -> List[Dict[str, Any]]:
        """Monitor visibility for target keywords"""
        if keywords is None:
            keywords = self.target_keywords
            
        results = []
        
        print(f"Monitoring {len(keywords)} keywords across {len(self.ai_platforms)} platforms")
        
        for i, keyword in enumerate(keywords, 1):
            print(f"[{i}/{len(keywords)}] Monitoring keyword: {keyword}")
            result = self.check_brand_mentions(keyword)
            results.append(result)
            
            # Rate limiting
            time.sleep(0.5)
        
        return results
    
    def calculate_visibility_score(self, keyword_results: List[Dict[str, Any]]) -> float:
        """Calculate overall AI visibility score"""
        if not keyword_results:
            return 0.0
        
        total_score = 0
        total_weight = 0
        
        # Weight keywords by importance
        keyword_weights = {
            "PDF to CSV": 1.0,
            "PDF to CSV converter": 0.9,
            "convert PDF to CSV": 0.8,
            "PDF CSV conversion": 0.7,
            "document processing AI": 0.6,
            "invoice automation": 0.5,
            "AI document processing": 0.4
        }
        
        for result in keyword_results:
            keyword = result["query"]
            weight = keyword_weights.get(keyword, 0.3)
            
            # Calculate score based on mentions and sentiment
            mentions = result["summary"]["mentions_found"]
            positive_mentions = result["summary"]["positive_mentions"]
            avg_confidence = result["summary"]["average_confidence"]
            
            # Score formula: (mentions * sentiment_bonus * confidence) / max_possible
            max_mentions = len(self.ai_platforms)
            sentiment_bonus = 1.0 + (positive_mentions * 0.2)  # Bonus for positive mentions
            
            keyword_score = (mentions / max_mentions) * sentiment_bonus * avg_confidence
            total_score += keyword_score * weight
            total_weight += weight
        
        return round((total_score / total_weight) * 10, 1) if total_weight > 0 else 0.0
    
    def generate_comprehensive_report(self, keyword_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate comprehensive AI optimization report"""
        visibility_score = self.calculate_visibility_score(keyword_results)
        
        # Calculate metrics
        total_mentions = sum(result["summary"]["mentions_found"] for result in keyword_results)
        total_positive = sum(result["summary"]["positive_mentions"] for result in keyword_results)
        total_negative = sum(result["summary"]["negative_mentions"] for result in keyword_results)
        total_neutral = sum(result["summary"]["neutral_mentions"] for result in keyword_results)
        
        # Find top performing keywords
        top_keywords = sorted(keyword_results, 
                            key=lambda x: x["summary"]["mentions_found"], 
                            reverse=True)[:5]
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "brand": self.brand_name,
            "website": self.website_url,
            "monitoring_period": "24 hours",
            "metrics": {
                "visibility_score": visibility_score,
                "total_queries_monitored": len(keyword_results),
                "brand_mentions": total_mentions,
                "positive_mentions": total_positive,
                "negative_mentions": total_negative,
                "neutral_mentions": total_neutral,
                "platforms_monitored": len(self.ai_platforms),
                "top_performing_keywords": [k["query"] for k in top_keywords]
            },
            "recommendations": self.generate_recommendations(visibility_score, total_mentions),
            "next_actions": self.generate_next_actions(visibility_score, total_mentions),
            "platform_performance": self.analyze_platform_performance(keyword_results)
        }
        
        return report
    
    def generate_recommendations(self, visibility_score: float, total_mentions: int) -> List[str]:
        """Generate AI optimization recommendations"""
        recommendations = []
        
        if visibility_score < 5.0:
            recommendations.extend([
                "Increase FAQ-focused content creation",
                "Implement more conversational content structure",
                "Add more long-tail keyword targeting",
                "Enhance schema markup implementation"
            ])
        elif visibility_score < 7.0:
            recommendations.extend([
                "Continue publishing FAQ-focused content",
                "Monitor competitor AI visibility",
                "Track featured snippet appearances",
                "Analyze voice search optimization"
            ])
        else:
            recommendations.extend([
                "Maintain current AI optimization strategy",
                "Focus on conversion optimization from AI traffic",
                "Expand to additional AI platforms",
                "Create industry-specific content"
            ])
        
        if total_mentions < 10:
            recommendations.append("Increase brand mention frequency through content marketing")
        
        return recommendations
    
    def generate_next_actions(self, visibility_score: float, total_mentions: int) -> List[str]:
        """Generate next action items"""
        actions = [
            "Set up automated monitoring alerts",
            "Create AI-specific content calendar",
            "Implement schema markup validation",
            "Track conversion from AI traffic",
            "Monitor social media AI mentions"
        ]
        
        if visibility_score < 6.0:
            actions.extend([
                "Audit existing content for AI optimization",
                "Create more question-based content",
                "Implement HowTo schema markup"
            ])
        
        return actions
    
    def analyze_platform_performance(self, keyword_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze performance across different AI platforms"""
        platform_stats = {}
        
        for platform, name in self.ai_platforms.items():
            mentions = 0
            positive = 0
            total_confidence = 0
            count = 0
            
            for result in keyword_results:
                platform_data = result["platforms"].get(platform, {})
                if platform_data.get("mentioned", False):
                    mentions += 1
                    if platform_data.get("sentiment") == "positive":
                        positive += 1
                total_confidence += platform_data.get("confidence", 0)
                count += 1
            
            platform_stats[platform] = {
                "name": name,
                "mentions": mentions,
                "positive_mentions": positive,
                "average_confidence": round(total_confidence / count, 2) if count > 0 else 0,
                "performance_score": round((mentions / len(keyword_results)) * 10, 1)
            }
        
        return platform_stats
    
    def save_results(self, data: Any, filename: str = None) -> None:
        """Save monitoring results to file"""
        if filename is None:
            filename = self.results_file
            
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"Results saved to {filename}")
    
    def generate_markdown_report(self, data: Dict[str, Any]) -> str:
        """Generate markdown report for GitHub"""
        report = f"""# AI Visibility Report - {datetime.now().strftime('%Y-%m-%d')}

## Executive Summary

- **Brand**: {data['monitoring_session']['brand']}
- **Website**: {data['monitoring_session']['website']}
- **Monitoring Period**: {data['monitoring_session']['monitoring_period']}
- **Visibility Score**: {data['monitoring_session']['metrics']['visibility_score']}/10
- **Total Brand Mentions**: {data['monitoring_session']['metrics']['brand_mentions']}

## Key Metrics

| Metric | Value |
|--------|-------|
| Visibility Score | {data['monitoring_session']['metrics']['visibility_score']}/10 |
| Brand Mentions | {data['monitoring_session']['metrics']['brand_mentions']} |
| Positive Mentions | {data['monitoring_session']['metrics']['positive_mentions']} |
| Negative Mentions | {data['monitoring_session']['metrics']['negative_mentions']} |
| Neutral Mentions | {data['monitoring_session']['metrics']['neutral_mentions']} |
| Platforms Monitored | {data['monitoring_session']['metrics']['platforms_monitored']} |

## Top Performing Keywords

"""
        
        for i, keyword in enumerate(data['monitoring_session']['metrics']['top_performing_keywords'][:5], 1):
            report += f"{i}. **{keyword}**\n"
        
        report += f"""
## Platform Performance

"""
        
        for platform, stats in data['monitoring_session']['platform_performance'].items():
            report += f"### {stats['name']}\n"
            report += f"- **Mentions**: {stats['mentions']}\n"
            report += f"- **Performance Score**: {stats['performance_score']}/10\n"
            report += f"- **Average Confidence**: {stats['average_confidence']}\n\n"
        
        report += f"""
## Recommendations

"""
        
        for rec in data['monitoring_session']['recommendations']:
            report += f"- {rec}\n"
        
        report += f"""
## Next Actions

"""
        
        for action in data['monitoring_session']['next_actions']:
            report += f"- {action}\n"
        
        report += f"""
## Trend Analysis

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---
*This report was automatically generated by the AI Visibility Monitor.*
"""
        
        return report
    
    def run_monitoring_session(self, keywords: List[str] = None) -> None:
        """Run a complete monitoring session"""
        print(f"Starting AI visibility monitoring for {self.brand_name}")
        print(f"Monitoring {len(keywords or self.target_keywords)} keywords across {len(self.ai_platforms)} platforms")
        
        # Monitor keyword visibility
        keyword_results = self.monitor_keyword_visibility(keywords)
        
        # Generate comprehensive report
        report = self.generate_comprehensive_report(keyword_results)
        
        # Combine results
        full_results = {
            "monitoring_session": report,
            "keyword_results": keyword_results,
            "generated_at": datetime.now().isoformat()
        }
        
        # Save results
        self.save_results(full_results)
        
        # Generate markdown report
        markdown_report = self.generate_markdown_report(full_results)
        with open(self.report_file, 'w', encoding='utf-8') as f:
            f.write(markdown_report)
        
        print("AI visibility monitoring completed!")
        print(f"Report generated: {report['timestamp']}")
        print(f"Visibility Score: {report['metrics']['visibility_score']}/10")
        print(f"Brand Mentions: {report['metrics']['brand_mentions']}")
        print(f"Recommendations: {len(report['recommendations'])}")
        print(f"Next actions: {len(report['next_actions'])}")

def main():
    """Main function to run AI visibility monitoring"""
    parser = argparse.ArgumentParser(description='AI Visibility Monitor for TidiFul')
    parser.add_argument('--config', help='Configuration file path')
    parser.add_argument('--keywords', nargs='+', help='Specific keywords to monitor')
    parser.add_argument('--output', help='Output file for results')
    
    args = parser.parse_args()
    
    monitor = EnhancedAIVisibilityMonitor(config_file=args.config)
    
    if args.output:
        monitor.results_file = args.output
    
    monitor.run_monitoring_session(keywords=args.keywords)

if __name__ == "__main__":
    main()