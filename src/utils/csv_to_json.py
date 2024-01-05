"""
Convert a CSV file to JSON format, with the option to split the output into multiple files based on a specified row limit. This function reads a CSV file, converts each row into a JSON object, and writes these objects into one or more JSON files. Each JSON file contains up to a specified number of rows from the CSV file, making it easier to handle large datasets.

This function is particularly useful for processing large CSV files that need to be converted into a more flexible data format like JSON. By splitting the output into smaller files, it helps in managing large datasets and ensures that each file remains of a manageable size.

# Parameters:
- csv_file_path (str): The file path to the input CSV file.
- json_file_base_path (str): The base file path for the output JSON files. The files are numbered sequentially.
- row_limit (int, optional): The maximum number of rows to be included in each JSON file. Defaults to 30,000.

# Example Usage:
csv_file_path = '/mnt/data/sample.csv'  # Replace with the actual CSV file path
json_file_base_path = '/mnt/data/output_json'  # Base path for output JSON files

# Convert the CSV to JSON and split into separate files every 30000 rows
csv_to_json(csv_file_path, json_file_base_path, row_limit=30000)
"""


import csv
import json


def csv_to_json(csv_file_path, json_file_base_path, row_limit=30000):
    """
    Convert a CSV file to JSON. The conversion will split the JSON output into separate files
    each containing a maximum of `row_limit` rows from the CSV.

    :param csv_file_path: Path to the input CSV file.
    :param json_file_base_path: Base path for the output JSON files.
    :param row_limit: Maximum number of rows to include in each JSON file.
    """
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        file_number = 1
        current_rows = []

        for row in reader:
            current_rows.append(row)

            if len(current_rows) == row_limit:
                output_file_path = f"{json_file_base_path}_{file_number}.json"
                with open(output_file_path, "w", encoding="utf-8") as jsonfile:
                    json.dump(current_rows, jsonfile, indent=4)

                file_number += 1
                current_rows = []

        # Dump remaining rows if any
        if current_rows:
            output_file_path = f"{json_file_base_path}_{file_number}.json"
            with open(output_file_path, "w", encoding="utf-8") as jsonfile:
                json.dump(current_rows, jsonfile, indent=4)
