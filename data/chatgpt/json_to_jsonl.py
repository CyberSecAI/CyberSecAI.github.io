#JSON to JSONL Converter

import json

def json_to_jsonl(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    with open(output_file, 'w') as f:
        for weakness in data.get('Weaknesses', []):
            json.dump(weakness, f)
            f.write('\n')

# Usage
input_file = 'cwe_trimmed.json'
output_file = 'cwe_trimmed.jsonl'
json_to_jsonl(input_file, output_file)

print(f"Conversion complete. JSONL file saved as {output_file}")