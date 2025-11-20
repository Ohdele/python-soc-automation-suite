from cryptography.fernet import Fernet

# 1. Key Generation (Needs to be done once and securely stored)
key = Fernet.generate_key()
f = Fernet(key)

# Example: Encrypting a sensitive log entry or config secret
sensitive_data = "Target_IP=10.0.2.15; User_Creds=admin:P@ssw0rd1"
encoded_data = sensitive_data.encode() # Fernet works on bytes

# 2. Encryption
encrypted_token = f.encrypt(encoded_data)

# 3. Decryption (Requires the exact same key 'key')
decrypted_data = f.decrypt(encrypted_token).decode()

print(f"Sensitive Data (Bytes): {encoded_data}")
print(f"Encryption Key (Base64): {key.decode()}")
print(f"Encrypted Token: {encrypted_token.decode()}")
print(f"Decrypted Data: {decrypted_data}")
