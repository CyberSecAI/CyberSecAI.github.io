#usage python3 ./split_cwe.py


import json
import os

def split_json_by_id(input_file, output_dir, ids_per_file=200):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Read the JSON data
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Extract the list of items (assuming it's the first key in the JSON)
    items = list(data.values())[0]

    # Sort items by ID
    sorted_items = sorted(items, key=lambda x: int(x['ID']))

    # Split items into chunks
    chunks = [sorted_items[i:i + ids_per_file] for i in range(0, len(sorted_items), ids_per_file)]

    # Write each chunk to a separate file
    for i, chunk in enumerate(chunks):
        output_file = os.path.join(output_dir, f'split_{i+1}.json')
        with open(output_file, 'w') as file:
            json.dump({list(data.keys())[0]: chunk}, file, indent=2)

    print(f"Split complete. {len(chunks)} files created in {output_dir}")

# Usage
input_file = 'cwe_trimmed.json'  # The file created by the previous script
output_dir = 'split'
ids_per_file = 200

split_json_by_id(input_file, output_dir, ids_per_file)