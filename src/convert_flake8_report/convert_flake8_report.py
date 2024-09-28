import xml.etree.ElementTree as ET
import hashlib
import json
import argparse
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def generate_fingerprint(issue_type, file_path, line_number):
    # Create a unique fingerprint using hashing
    fingerprint = f"{issue_type}-{file_path}-{line_number}"
    return hashlib.md5(fingerprint.encode("utf-8")).hexdigest()


def parse_xml_to_json(xml_string):
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError as e:
        logging.error(f"Error parsing XML: {e}")
        return []

    report = []

    for testcase in root.findall("testcase"):
        # Skip test cases without failures
        failure = testcase.find("failure")
        if failure is None:
            continue  # No failure in this testcase, so skip it

        try:
            # Extract issue details
            issue_type = testcase.attrib["name"].split(" ")[
                0
            ]  # This contains the error code (e.g., F401)
            file_path = testcase.attrib["name"].split("(")[1].split(":")[0]
            line_number = testcase.attrib["name"].split(":")[1]
            failure_message = failure.attrib["message"].split("&#10;")[
                0
            ]  # First line of the message

            # Prepare the JSON structure for each issue, formatted according to the example
            issue = {
                "description": f"({issue_type}) {failure_message}",
                "fingerprint": generate_fingerprint(issue_type, file_path, line_number),
                "location": {
                    "lines": {
                        "begin": int(line_number),
                        "end": int(line_number),  # Same start and end for this format
                    },
                    "path": file_path,
                },
                "severity": "major",  # Set severity as major
            }

            report.append(issue)
        except (IndexError, ValueError) as e:
            logging.error(f"Error processing testcase: {e}")
            continue

    return report


def main():
    # Set up argument parser to allow file path input from terminal
    parser = argparse.ArgumentParser(
        description="Convert XML lint report to GitLab Code Quality JSON"
    )
    parser.add_argument(
        "xml_file", help="Path to the XML lint report file created with ament_flake8"
    )
    parser.add_argument("output_file", help="Path to the output JSON file")

    args = parser.parse_args()

    # Validate input file path
    if not os.path.isfile(args.xml_file):
        logging.error(f"Error: The file '{args.xml_file}' does not exist.")
        return

    # Read the XML file
    try:
        with open(args.xml_file, "r") as file:
            xml_content = file.read()
    except Exception as e:
        logging.error(f"Error reading XML file: {e}")
        return

    # Parse the XML content and generate the JSON report
    json_report = parse_xml_to_json(xml_content)

    # Write the JSON report to the output file
    try:
        with open(args.output_file, "w") as json_file:
            json.dump(json_report, json_file, indent=2)
        logging.info(f"Code quality report has been generated and saved to {args.output_file}")
    except Exception as e:
        logging.error(f"Error writing JSON file: {e}")


if __name__ == "__main__":
    main()
