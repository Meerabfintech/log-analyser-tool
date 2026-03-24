#!/usr/bin/env python3
"""Log Analyser Tool Google IT Automation Project uses: Regular Expressions, Error Finding, Testing Concepts"""

import re
import os
from collections import Counter
import datetime

class LogAnalyzer:
    """ Main class for analyzing log files"""
    def __init__(self, log_file):
        self.log_file = log_file
        self.lines = []
        self.errors = []
        self.warnings = []
        self.ip_addresses = []

    def read_log_files(self):
        """ Read the log file into memory"""
        try:
            with open(self.log_file, 'r') as file:
                self.lines = file.readlines()
            print(f"Read {len(self.lines)} lines from {self.log_file}")
            return True
        except FileNotFoundError:
            print(f"Error: File {self.log_file} not found")
            return False

    def find_errors(self):
        """Use regex To find error messages"""
        error_pattern = r'ERROR|error|Error|Failed|failed|Exception|exception'
        for i, line in enumerate(self.lines, 1):
            if re.search(error_pattern, line):
                self.errors.append((i, line.strip()))
        print(f"Found {len(self.errors)} errors")
        return self.errors

    def find_warnings(self):
        """Use regex to find warning messages"""
        warning_pattern = r'WARNING|Warning|warning|CAUTION|caution'
        for i, line in enumerate(self.lines, 1):
            if re.search(warning_pattern, line):
                self.warnings.append((i, line.strip()))
        print(f"Found {len(self.warnings)} warnings")
        return self.warnings

    def extract_ip_addresses(self):
        """Use regex to find all IP addresses"""
        ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        for line in self.lines:
            ips = re.findall(ip_pattern, line)
            self.ip_addresses.extend(ips)
        print(f"Found {len(self.ip_addresses)} IP addresses")
        return self.ip_addresses

    def count_error_types(self):
        """Count different types of errors"""
        error_types = []
        for _, line in self.errors:
            if 'timeout' in line.lower():
                error_types.append('Timeout')
            elif 'permission' in line.lower():
                error_types.append('Permission')
            elif 'connection' in line.lower():
                error_types.append('Connection')
            elif 'memory' in line.lower():
                error_types.append('Memory')
            else:
                error_types.append('Other')
        return Counter(error_types)

    def generate_report(self):
        """Generate a summary report"""
        print("\n" + "="*50)
        print("LOG ANALYSIS REPORT")
        print("="*50)
        print(f"File analysed: {self.log_file}")
        print(f"Total lines: {len(self.lines)}")
        print(f"Total errors: {len(self.errors)}")
        print(f"Total warnings: {len(self.warnings)}")
        print(f"Unique IPs: {len(set(self.ip_addresses))}")
        if self.errors:
            print("\nTOP 5 ERRORS:")
            for i, (line_num, error) in enumerate(self.errors[:5]):
                print(f"  {i+1}. Line {line_num}: {error[:50]}...")

            error_counts = self.count_error_types()
            if error_counts:
                print("\nERROR TYPES:")
                for error_type, count in error_counts.most_common():
                    print(f"  {error_type}: {count}")

        # Save report to file
        with open('analysis_report.txt', 'w') as report:
            report.write(f"Log Analysis Report for {self.log_file}\n")
            report.write(f"Date: {datetime.datetime.now()}\n")
            report.write(f"Total Errors: {len(self.errors)}\n")
            report.write(f"Total Warnings: {len(self.warnings)}\n")
            report.write(f"Unique IPs: {len(set(self.ip_addresses))}\n")
            report.write("\nTop Errors:\n")
            for i, (line_num, error) in enumerate(self.errors[:5], 1):
                report.write(f"{i}. Line {line_num}: {error}\n")
        print("\n Report saved to analysis_report.txt")
        print("="*50)

def main():
    """Main function to run the analyzer"""
    print("\n LOG FILE ANALYZER TOOL")
    print("Google IT Automation Course 2 Project\n")
    
    # Get log file from user
    log_file = input("Enter log file path (or use 'sample.log'): ").strip()
    if not log_file:
        log_file = "sample.log"
    
    # Create analyzer and run analysis
    analyzer = LogAnalyzer(log_file)
    if analyzer.read_log_files():
        analyzer.find_errors()
        analyzer.find_warnings()
        analyzer.extract_ip_addresses()
        analyzer.generate_report()

if __name__ == "__main__":
    main()
        
