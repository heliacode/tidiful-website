# AI Visibility Monitoring for TidiFul

This repository includes automated AI visibility monitoring to track TidiFul's presence across AI platforms like ChatGPT, Claude, Perplexity, and others.

## 🚀 GitHub Action Setup

The AI visibility monitoring is automated using GitHub Actions. Here's how it works:

### Automatic Monitoring Schedule
- **Weekly Monitoring**: Every Monday at 9 AM UTC
- **Manual Triggers**: Can be run manually with different monitoring types
- **PR Monitoring**: Automatically runs when blog posts are updated

### Monitoring Types Available
1. **Full Monitoring**: Complete keyword and platform analysis
2. **Keywords Only**: Focus on specific keyword performance
3. **Competitors**: Monitor competitor AI visibility
4. **Quick Check**: Fast overview of current status

## 📊 What Gets Monitored

### Keywords Tracked
- PDF to CSV
- PDF to CSV converter
- convert PDF to CSV
- PDF CSV conversion
- document processing AI
- invoice automation
- AI document processing
- PDF to JSON converter
- invoice processing software
- document automation platform
- TidiFul
- HeliaCode

### AI Platforms Monitored
- OpenAI ChatGPT
- Anthropic Claude
- Perplexity AI
- Google Bard
- Microsoft Bing Chat
- Voice Search Assistants

## 📈 Metrics Tracked

### Key Performance Indicators
- **Visibility Score**: Overall AI visibility rating (0-10)
- **Brand Mentions**: Total mentions across platforms
- **Sentiment Analysis**: Positive, negative, neutral mentions
- **Platform Performance**: Individual platform scores
- **Keyword Performance**: Top performing keywords

### Reports Generated
1. **JSON Results**: Detailed monitoring data
2. **Markdown Report**: Human-readable summary
3. **SEO Health Check**: Schema markup validation
4. **Artifacts**: All reports saved for 30 days

## 🛠️ Manual Usage

### Run Locally
```bash
# Basic monitoring
python ai_visibility_monitor.py

# With configuration file
python ai_visibility_monitor.py --config ai_monitoring_config.json

# Monitor specific keywords
python ai_visibility_monitor.py --keywords "PDF to CSV" "invoice automation"

# Custom output file
python ai_visibility_monitor.py --output custom_results.json
```

### Configuration File
Edit `ai_monitoring_config.json` to customize:
- Keywords to monitor
- Platforms to track
- Alert thresholds
- Notification settings

## 📋 GitHub Action Workflow

### Triggers
1. **Scheduled**: Every Monday at 9 AM UTC
2. **Manual**: Via GitHub Actions tab
3. **Push**: When monitoring files are updated
4. **PR**: When blog posts are modified

### Jobs
1. **ai-visibility-monitor**: Main monitoring job
2. **ai-seo-check**: SEO health validation
3. **notify-results**: Results notification

### Artifacts Created
- `ai-visibility-results-[run-number]`: Complete monitoring data
- `seo-health-report-[run-number]`: SEO validation report

## 🎯 AI Optimization Features

### Schema Markup Validation
- FAQ schema on all pages
- Organization schema implementation
- Article schema for blog posts
- Proper structured data validation

### Content Optimization
- Conversational content structure
- FAQ-focused articles
- Long-tail keyword targeting
- Natural language optimization

## 📊 Dashboard

Access the visual dashboard at `ai_visibility_dashboard.html` to see:
- Real-time metrics
- Platform performance charts
- Keyword performance trends
- Optimization recommendations

## 🚨 Alerts and Notifications

### Automatic Alerts
- Visibility score drops below threshold
- Monitoring failures
- Schema markup issues
- SEO health problems

### GitHub Issues
- Automatic issue creation for critical problems
- PR comments with AI impact analysis
- Weekly summary reports

## 🔧 Customization

### Adding New Keywords
1. Edit `ai_monitoring_config.json`
2. Add keywords to the `keywords` array
3. Commit changes to trigger monitoring

### Adding New Platforms
1. Update `ai_platforms` in the config
2. Modify the monitoring script if needed
3. Test with manual run

### Adjusting Thresholds
1. Edit `monitoring` section in config
2. Set `alert_threshold` and `success_threshold`
3. Customize notification settings

## 📚 Best Practices

### For Maximum AI Visibility
1. **Consistent Monitoring**: Run weekly monitoring
2. **Content Creation**: Publish FAQ-focused content monthly
3. **Schema Validation**: Ensure all pages have proper markup
4. **Competitor Analysis**: Monitor competitor AI presence
5. **Conversion Tracking**: Measure AI traffic conversion rates

### Content Strategy
1. **Question-Based Headlines**: Use "What is...", "How to...", "Why..."
2. **FAQ Sections**: Include comprehensive Q&A sections
3. **Conversational Tone**: Write in natural, spoken language
4. **Long-Tail Keywords**: Target specific, detailed queries
5. **Featured Snippet Optimization**: Structure content for snippets

## 🎉 Expected Results

### Short-term (1-2 weeks)
- Improved featured snippet appearances
- Better voice search optimization
- Enhanced AI understanding of content

### Medium-term (1-3 months)
- Increased brand mentions in AI responses
- Higher traffic from AI platforms
- Improved search rankings for conversational queries

### Long-term (3+ months)
- Established market position in AI responses
- Competitive advantage over non-optimized sites
- Higher conversion rates from AI traffic

## 📞 Support

For questions or issues with the AI visibility monitoring:
- Check GitHub Actions logs
- Review generated reports
- Contact: info@heliacode.com

---

*This monitoring system helps ensure TidiFul maintains strong visibility across AI platforms and search engines.*
