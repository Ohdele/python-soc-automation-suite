# Python SOC Automation Suite

End-to-end security automation toolkit for threat detection, network analysis, vulnerability assessment, and malware triage.  
Includes modules for packet capture, hashing, encryption, socket communication, intelligence lookups, and automated alerts.

## Features
- Threat detection & traffic profiling
- Vulnerability scanning & port analysis
- File integrity verification
- Malware inspection (static)
- Threat-intel enrichment (VirusTotal, Shodan)
- Consolidated logs and alert outputs

---

## Stage 1: Foundations (Python I/O & String Handling)

**Objective:** Develop foundational Python scripts for security tool prerequisites: cleaning and standardizing user input (String Normalization), and handling persistent data (File Read/Write) for reports and logs.

[View Commands and Outputs](log_stage1_foundations.txt)

---

## Stage 2: Cryptography (Cipher Implementation)

**Objective:** Developed scripts to implement both a classic cipher (Caesar) and a modern, secure cipher (Fernet/AES) to demonstrate secure data handling for sensitive information.

[View Commands and Outputs](log_stage2_cryptography.txt)

---

## Stage 3: Networking & Socket Programming

**Objective:** Built foundational network tools (TCP Client/Server) using Python's `socket` library to handle basic connections and data transfer, mimicking communication in a SOC environment.

[View Commands and Outputs](log_stage3_networking.txt)

---

## Stage 4: File System and Data Manipulation

**Objective:** Built scripts to automate file management, including reading structured configuration files, sanitizing sensitive data (REDACTION), and managing log outputs, crucial for professional SOC tooling.

[View Commands and Outputs](log_stage4_filesystem.txt)

---

---

## Stage 5: System Utilities and Automation

**Objective:** Built scripts to interact directly with the underlying operating system (OS), execute shell commands securely, and automate OS-level information gathering, crucial for environment auditing and security scanning.

* **Task 1 (Basic Command Execution):** Used the `subprocess` module to run a simple OS command (`ls -l`) and capture its standardized output.
* **Task 2 (Advanced Command/Network Audit):** Executed a more complex command (`ip a`) to retrieve detailed network interface information, demonstrating system audit capabilities.

[View Commands and Outputs](log_stage5_utilities.txt)
