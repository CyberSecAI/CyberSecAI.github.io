#usage python3 ./trim_json.py

import json


def remove_content_history(data):
    if isinstance(data, dict):
        if 'ContentHistory' in data:
            del data['ContentHistory']
        for value in data.values():
            remove_content_history(value)
    elif isinstance(data, list):
        for item in data:
            remove_content_history(item)

# Read the JSON data from the file
with open('cwe.json', 'r') as file:
    json_data = json.load(file)

# Remove ContentHistory
remove_content_history(json_data)

# Write the modified data back to a file
with open('cwe_trimmed.json', 'w') as file:
    json.dump(json_data, file, indent=2)

print("ContentHistory has been removed and the result has been saved to output.json")