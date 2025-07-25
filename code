import os
import pandas as pd
from datetime import datetime

def process_log_file(filepath):
    logs = []
    with open(filepath, 'r') as f:
        for line in f:
            try:
                time_str = line.split()[0]  # Adjust for your log's timestamp format
                # Example for ISO format: "2024-01-01T12:00:00 ..."
                timestamp = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                timestamp = datetime.now()
            logs.append({
                "timestamp": timestamp,
                "raw_message": line.strip(),
                "source_ip": None,  # Will be parsed in clean.py
                "severity": None,    # Will be parsed in clean.py
            })
    return logs

def process_log_directory(input_dir="data", output_path="processed/logs_combined.csv"):
    all_logs = []
    for filename in os.listdir(input_dir):
        if filename.endswith(".log"):
            logs = process_log_file(os.path.join(input_dir, filename))
            all_logs.extend(logs)
    df = pd.DataFrame(all_logs)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    return df

if __name__ == "__main__":
    df = process_log_directory()
    print("Logs processed and saved to processed/logs_combined.csv")
