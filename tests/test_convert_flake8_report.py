import unittest
import json
import os
import sys

# Ensure that the src directory is in the path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from convert_flake8_report.convert_flake8_report import parse_xml_to_json  # Adjust this import based on your actual function

class TestConvertLintReport(unittest.TestCase):

    def setUp(self):
        self.test_data_dir = os.path.join(os.path.dirname(__file__), 'test_data')

    def read_file(self, file_name):
        file_path = os.path.join(self.test_data_dir, file_name)
        with open(file_path, 'r') as file:
            return file.read()

    def test_no_errors(self):
        # Load the sample XML input
        xml_content = self.read_file('sample_lint_report_no_erros.xml')
        
        # Expected output
        expected_output = json.loads(self.read_file('sample_lint_report_no_erros.json'))

        # Parse the XML and get the actual output
        actual_output = parse_xml_to_json(xml_content)

        # Compare the actual output to the expected output
        self.assertEqual(actual_output, expected_output)
    
    def test_with_errors(self):
        # Load the sample XML input
        xml_content = self.read_file('sample_lint_report_with_errors.xml')
        
        # Expected output
        expected_output = json.loads(self.read_file('sample_lint_report_with_errors.json'))

        # Parse the XML and get the actual output
        actual_output = parse_xml_to_json(xml_content)

        # Compare the actual output to the expected output
        self.assertEqual(actual_output, expected_output)
    
    def test_invalid_xml(self):
        # Load the sample XML input
        xml_content = "<testsuite><testcase></testsuite>"
        
        # Expected output
        expected_output = []

        # Parse the XML and get the actual output
        actual_output = parse_xml_to_json(xml_content)

        # Compare the actual output to the expected output
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
