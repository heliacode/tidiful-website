#!/bin/bash
# Test script for AI Visibility Monitor
# Simulates GitHub Action environment

echo "Testing AI Visibility Monitor..."

# Check if Python is available
if ! command -v python &> /dev/null; then
    echo "Error: Python is not installed or not in PATH"
    exit 1
fi

# Check if required files exist
required_files=("ai_visibility_monitor.py" "ai_monitoring_config.json")
for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "Error: Required file $file not found"
        exit 1
    fi
done

echo "All required files found"

# Run the monitoring script
echo "Running AI visibility monitoring..."
python ai_visibility_monitor.py --config ai_monitoring_config.json

# Check if results were generated
if [ -f "ai_visibility_results.json" ]; then
    echo "✅ Results file generated successfully"
else
    echo "❌ Results file not generated"
    exit 1
fi

if [ -f "ai_visibility_report.md" ]; then
    echo "✅ Report file generated successfully"
else
    echo "❌ Report file not generated"
    exit 1
fi

# Display summary
echo ""
echo "=== MONITORING SUMMARY ==="
if command -v jq &> /dev/null; then
    echo "Visibility Score: $(jq -r '.monitoring_session.metrics.visibility_score' ai_visibility_results.json)/10"
    echo "Brand Mentions: $(jq -r '.monitoring_session.metrics.brand_mentions' ai_visibility_results.json)"
    echo "Keywords Monitored: $(jq -r '.monitoring_session.metrics.total_queries_monitored' ai_visibility_results.json)"
else
    echo "Install 'jq' for detailed JSON parsing"
fi

echo ""
echo "✅ AI Visibility Monitor test completed successfully!"
echo "Check ai_visibility_results.json and ai_visibility_report.md for details"
