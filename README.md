# Automated-Security-Log-Analytics-Dashboard-


import pandas as pd
import re
from datetime import datetime
import os

def parse_log_line(line):
    # Example: Parse a syslog or firewall log line
    # Adjust regex based on your log format
    pattern = r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<host>\S+) (?P<process>\S+)\[(?P<pid>\d+)\]: (?P<message>.*)'
    match = re.match(pattern, line)
    if match:
        return match.groupdict()
    return None

def process_log_file(input_path, output_path):
    logs = []
    with open(input_path, 'r') as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                logs.append(parsed)
    df = pd.DataFrame(logs)
    df.to_csv(output_path, index=False)

# Example usage:
process_log_file('firewall.log', 'processed_logs.csv')




import pandas as pd

def detect_anomalies(df):
    # Simple example: Flag IPs with unusually high connection counts
    ip_counts = df['source_ip'].value_counts()
    threshold = ip_counts.mean() + 2 * ip_counts.std()  # Adjust as needed
    anomalies = ip_counts[ip_counts > threshold].index.tolist()
    return anomalies

df = pd.read_csv('processed_logs.csv')
anomalies = detect_anomalies(df)
print("Anomalous IPs:", anomalies)
