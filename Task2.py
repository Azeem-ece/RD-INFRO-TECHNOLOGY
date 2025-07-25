import pandas as pd
import os
import json

csv_file = "data.csv"
json_file = "data.json"

# Confirm the CSV file is present
if os.path.isfile(csv_file):
    # Load the CSV data into a DataFrame
    table = pd.read_csv(csv_file)
    print("Contents of CSV file:")
    print(table)

    # Save the DataFrame to a JSON file
    table.to_json(json_file, orient="records", indent=4)
    print(f"\nData successfully written to '{json_file}'.")

    # Optionally, display the JSON data
    with open(json_file, "r") as reader:
        json_output = json.load(reader)
        print("\nPreview of JSON data:")
        print(json.dumps(json_output, indent=4))
else:
    print(f"'{csv_file}' not found in the current directory.")