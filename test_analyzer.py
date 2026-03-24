#!/usr/bin/env python3
"""
Test file for Log Analyzer
Shows understanding of testing concepts from Course 2
"""

import unittest
import tempfile
import os
from log_analyzer import LogAnalyzer

class TestLogAnalyzer(unittest.TestCase):
    
    def setUp(self):
        """Create a temporary log file for testing"""
        self.test_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        self.test_file.write("INFO Normal message\n")
        self.test_file.write("ERROR Test error message\n")
        self.test_file.write("WARNING Test warning\n")
        self.test_file.write("Connection from 192.168.1.1\n")
        self.test_file.close()
        self.analyzer = LogAnalyzer(self.test_file.name)
    
    def tearDown(self):
        """Clean up temporary file"""
        os.unlink(self.test_file.name)
    
    def test_read_log_file(self):
        """Test if file reading works"""
        result = self.analyzer.read_log_file()
        self.assertTrue(result)
        self.assertEqual(len(self.analyzer.lines), 4)
    
    def test_find_errors(self):
        """Test error finding with regex"""
        self.analyzer.read_log_file()
        errors = self.analyzer.find_errors()
        self.assertEqual(len(errors), 1)
        self.assertIn('ERROR', errors[0][1])
    
    def test_find_warnings(self):
        """Test warning finding with regex"""
        self.analyzer.read_log_file()
        warnings = self.analyzer.find_warnings()
        self.assertEqual(len(warnings), 1)
        self.assertIn('WARNING', warnings[0][1])
    
    def test_extract_ip_addresses(self):
        """Test IP address extraction with regex"""
        self.analyzer.read_log_file()
        ips = self.analyzer.extract_ip_addresses()
        self.assertEqual(len(ips), 1)
        self.assertEqual(ips[0], '192.168.1.1')
    
    def test_file_not_found(self):
        """Test handling of missing file"""
        analyzer = LogAnalyzer("nonexistent.log")
        result = analyzer.read_log_file()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
