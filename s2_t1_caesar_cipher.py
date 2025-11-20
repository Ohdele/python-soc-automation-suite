def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the base (A or a)
            start = ord('A') if char.isupper() else ord('a')
            # Apply shift and wrap around (mod 26)
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    # Decrypting is simply encrypting with the negative shift
    return caesar_encrypt(text, -shift)

# Example: Encrypting a simple security message with a shift of 3
plaintext = "ALERT: Malicious traffic detected"
key = 3

ciphertext = caesar_encrypt(plaintext, key)
decrypted_text = caesar_decrypt(ciphertext, key)

print(f"Original Text: {plaintext}")
print(f"Key (Shift): {key}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")

