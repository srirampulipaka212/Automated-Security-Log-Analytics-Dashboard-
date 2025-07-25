# Automated Security Log Analytics Dashboard

## Project Overview

This project automates the collection, cleaning, analysis, and visualization of security logs from servers, networks, and firewalls. By building custom Python ETL pipelines, the system enables real-time monitoring, anomaly detection, and automated alerting—streamlining security operations and incident response.

## Features

- **Automated log ingestion** from multiple sources.
- **Data cleaning and enrichment** using Python scripts.
- **Anomaly detection** to highlight suspicious activity.
- **Structured output** for easy import into Splunk, Grafana, Tableau, or similar tools.

## Technologies Used

- **Python** (pandas, numpy, re, datetime, os)
- **Splunk, Grafana, or Tableau** (for visualization)
- **Git/GitHub** for version control

## Example Project Structure
## How to Run

1. **Clone this repository to your computer.**


2. **Install required dependencies.**


3. **Add your log files** (e.g., `sample.log`) to the `data/` folder.

4. **Run the processing scripts** in order:


Outputs will appear in the `processed/` folder.

5. **Import the output CSV files** into your dashboard tool (Splunk, Grafana, Tableau) to visualize and monitor security logs and anomalies.

---

