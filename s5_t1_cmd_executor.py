import subprocess
import sys

# Define the command to execute
# Using 'ls -l' to show file permissions and list files, common for auditing
COMMAND = "ls -l" 

def execute_command(cmd):
    print(f"[*] Executing command: {cmd}")
    try:
        # Use subprocess.run to execute the command and capture output
        result = subprocess.run(
            cmd, 
            shell=True,
            check=True,  # Raise an exception for non-zero exit codes
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True # Decode stdout and stderr as text
        )

        print("[SUCCESS] Command executed.")
        print("\n--- Command Output ---")
        print(result.stdout.strip())
        print("--- End Output ---")

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed with exit code {e.returncode}:")
        print(e.stderr.strip())
    except FileNotFoundError:
        print(f"[ERROR] Command not found: {cmd.split()[0]}")
    except Exception as e:
        print(f"[CRITICAL ERROR] An unexpected error occurred: {e}")

if __name__ == "__main__":
    execute_command(COMMAND)
