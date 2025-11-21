import subprocess
import sys

# Define the command to execute (using ip a, common on modern Linux)
COMMAND = "ip a" 
OUTPUT_LOG = "log_stage5_utilities.txt"

def run_network_audit(cmd):
    print(f"[*] Starting Network Interface Audit by running: {cmd}")

    try:
        # Execute the command
        result = subprocess.run(
            cmd, 
            shell=True,
            check=True, 
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = result.stdout.strip()

        print("[SUCCESS] Command executed.")
        print("\n--- Network Audit Output ---")
        print(output)
        print("--- End Audit ---")

        # Note: We will log this output to the final log file manually

    except subprocess.CalledProcessError as e:
        # Handle failure, like command not found or permission denied
        print(f"[ERROR] Command failed with exit code {e.returncode}.")
        print(f"  Error message: {e.stderr.strip()}")

    except Exception as e:
        print(f"[CRITICAL ERROR] An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_network_audit(COMMAND)
