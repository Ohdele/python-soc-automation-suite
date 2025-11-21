import csv
import os

LOG_FILE = 'audit_log.csv'

def parse_log():
    if not os.path.exists(LOG_FILE):
        print(f"[ERROR] Log file '{LOG_FILE}' not found.")
        return

    success_login_count = 0

    try:
        with open(LOG_FILE, mode='r', newline='') as file:
            # Use csv.DictReader to read rows as dictionaries with header keys
            reader = csv.DictReader(file)

            print(f"[*] Starting analysis of '{LOG_FILE}'...")

            for row in reader:
                event = row.get('event_type')
                status = row.get('status')
                ip = row.get('source_ip')

                # Check for our target event: SUCCESSFUL LOGIN
                if event == 'login' and status == 'SUCCESS':
                    success_login_count += 1
                    print(f"  [FOUND] Success: {ip} logged in at {row.get('timestamp')}")

        print(f"[*] Analysis complete.")
        print(f"[RESULT] Total successful logins counted: {success_login_count}")

    except Exception as e:
        print(f"[ERROR] An error occurred during file parsing: {e}")

if __name__ == "__main__":
    parse_log()
