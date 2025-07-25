import pandas as pd
import re

def clean_logs(input_path="processed/logs_combined.csv", output_path="processed/logs_cleaned.csv"):
    df = pd.read_csv(input_path, parse_dates=["timestamp"])
    # Extract source IP from raw_message (adjust regex for your log format)
    df["source_ip"] = df["raw_message"].apply(
        lambda x: re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", x)[0] 
        if re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", x) else None
    )
    # Add basic severity parsing (adjust as needed)
    df["severity"] = df["raw_message"].apply(
        lambda x: "ERROR" if "error" in x.lower() else "INFO" if "info" in x.lower() else "UNKNOWN"
    )
    df.to_csv(output_path, index=False)
    return df

if __name__ == "__main__":
    df = clean_logs()
    print("Logs cleaned and enriched. Output: processed/logs_cleaned.csv")
