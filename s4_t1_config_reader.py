import configparser
import os

CONFIG_FILE = 'target_config.ini'
OUTPUT_FILE = 'sanitized_summary.log'

def process_config():
    config = configparser.ConfigParser()

    # 1. Read the configuration file
    if not os.path.exists(CONFIG_FILE):
        print(f"[ERROR] Configuration file '{CONFIG_FILE}' not found.")
        return

    config.read(CONFIG_FILE)

    # 2. Extract data (including sensitive)
    target_ip = config.get('Target_Host', 'Target_IP', fallback='N/A')
    username = config.get('Credentials', 'User', fallback='N/A')
    password = config.get('Credentials', 'Password', fallback='N/A')
    api_key = config.get('Credentials', 'API_Key', fallback='N/A')

    # 3. Define sanitized output
    sanitized_content = (
        "--- Configuration Summary ---\n"
        f"Target IP: {target_ip}\n"
        f"Username: {username}\n"
        "Password: [REDACTED]\n"
        "API Key: [REDACTED]\n"
        "--- End Summary ---\n"
    )

    # 4. Write sanitized output to a log file
    try:
        with open(OUTPUT_FILE, 'w') as f:
            f.write(sanitized_content)
        print(f"[SUCCESS] Configuration read and sanitized output written to '{OUTPUT_FILE}'.")

        # Print the sensitive data verification to the terminal ONLY (not the log)
        print(f"[VERIFY] Original Password: {password}")
        print(f"[VERIFY] Original API Key: {api_key}")

    except IOError as e:
        print(f"[ERROR] Could not write to output file: {e}")

if __name__ == "__main__":
    process_config()
