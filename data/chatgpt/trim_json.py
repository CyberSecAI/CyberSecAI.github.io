#usage python3 ./trim_json.py

import json
import jsonlines

def remove_content_history(data):
    if isinstance(data, dict):
        if 'ContentHistory' in data:
            del data['ContentHistory']
        for value in data.values():
            remove_content_history(value)
    elif isinstance(data, list):
        for item in data:
            remove_content_history(item)

def remove_views(data):
    if isinstance(data, dict):
        if 'Views' in data:
            del data['Views']
        for value in data.values():
            remove_views(value)
    elif isinstance(data, list):
        for item in data:
            remove_views(item)

def remove_categories(data):
    if isinstance(data, dict):
        if 'Categories' in data:
            del data['Categories']
        for value in data.values():
            remove_categories(value)
    elif isinstance(data, list):
        for item in data:
            remove_categories(item)



# Read the JSON data from the file
with open('cwe.json', 'r') as file:
    json_data = json.load(file)

# Remove ContentHistory
remove_content_history(json_data)
remove_views(json_data)
remove_categories(json_data)

# Write the modified data back to a file
with open('cwe_trimmed.json', 'w') as file:
    json.dump(json_data, file, indent=2)

print("ContentHistory and Views have been removed and the result has been saved to output.json")