import json

def read_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line:  # Skip empty lines
                try:
                    data.append(json.loads(stripped_line))
                except json.JSONDecodeError as e:
                    print(f"Skipping invalid line: {line}")
                    print(f"Error: {e}")
    return data

# Example usage:
file_path = 'reddit_davinci.jsonl'
jsonl_data = read_jsonl(file_path)

human_text_data = []
machine_text_data = []
for item in jsonl_data:
    human_text_data.append(item['human_text'])
    machine_text_data.append(item['machine_text'])

data = {"human_writen":human_text_data,
        "machine_generated":machine_text_data}

import pandas as pd
# Prepare the data for DataFrame
df_data = []

for label, texts in data.items():
    for text in texts:
        df_data.append({"text": text, "label": label})

# Convert to DataFrame
df = pd.DataFrame(df_data)

df.to_csv("reddit_human_davinci.csv")