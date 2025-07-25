import pandas as pd

def detect_anomalies(input_path="processed/logs_cleaned.csv", output_path="processed/anomalies.csv"):
    df = pd.read_csv(input_path, parse_dates=["timestamp"])
    ip_counts = df["source_ip"].value_counts()
    threshold = ip_counts.mean() + 3 * ip_counts.std()  # Adjust threshold as needed
    suspicious_ips = ip_counts[ip_counts > threshold].index.tolist()
    anomalies = df[df["source_ip"].isin(suspicious_ips)]
    anomalies.to_csv(output_path, index=False)
    return anomalies

if __name__ == "__main__":
    anomalies = detect_anomalies()
    print(f"Found {len(anomalies)} suspicious events. Saved to processed/anomalies.csv")
