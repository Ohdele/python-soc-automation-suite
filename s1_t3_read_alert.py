def read_and_alert(filename):
    severity = "Unknown"
    try:
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith("Severity:"):
                    # Extract the value after ': ' and strip whitespace
                    severity = line.split(': ')[1].strip()
                    break

        if severity == "High":
            print(f"!!! CRITICAL ALERT: High Severity Incident Detected !!!")
        elif severity != "Unknown":
            print(f"INFO: Incident has Severity: {severity}")
        else:
            print("WARNING: Could not determine incident severity.")

    except FileNotFoundError:
        print(f"Error: Report file not found: {filename}")

read_and_alert("incident_report.txt")
