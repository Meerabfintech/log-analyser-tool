#!/bin/bash
# Bash script to run the log analyzer
# Shows bash scripting skills from Course 2

echo "==================================="
echo "LOG ANALYZER TOOL - BASH LAUNCHER"
echo "==================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo " Python3 is not installed. Please install it first."
    exit 1
fi

# Check if log file exists
LOG_FILE="sample.log"
if [ ! -f "$LOG_FILE" ]; then
    echo " Log file $LOG_FILE not found!"
    echo "Creating a sample log file..."
    python3 -c "
with open('$LOG_FILE', 'w') as f:
    f.write('2024-03-12 INFO Server started\n')
    f.write('2024-03-12 ERROR Connection failed\n')
    f.write('2024-03-12 WARNING High memory\n')
"
    echo " Sample log file created."
fi

# Run tests first
echo -e "\n RUNNING TESTS..."
python3 -m unittest test_analyzer.py -v

# Ask if user wants to run main analysis
echo -e "\n"
read -p "Run main analysis? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo -e "\n RUNNING LOG ANALYSIS..."
    python3 log_analyzer.py
fi

echo -e "\n Analysis complete!"
echo "Check analysis_report.txt for results."
chmod +x run_analysis.sh
