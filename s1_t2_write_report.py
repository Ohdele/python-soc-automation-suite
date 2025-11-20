def create_report(filename, incident_data):
    try:
        with open(filename, 'w') as f:
            f.write("--- Incident Report ---\n")
            for key, value in incident_data.items():
                f.write(f"{key}: {value}\n")
        print(f"Report successfully saved to {filename}")
    except IOError:
        print(f"Error: Could not write to file {filename}")

incident_details = {
    "Incident ID": "INC-2025-0042",
    "Severity": "High",
    "Timestamp": "2025-11-20 11:30:00",
    "Source IP": "192.168.1.105",
    "Status": "Pending Review"
}

create_report("incident_report.txt", incident_details)
