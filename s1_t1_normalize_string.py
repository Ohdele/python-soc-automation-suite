import re

def normalize_string(input_str):
    # Replace non-alphanumeric characters (including spaces) with an underscore
    normalized = re.sub(r'[^a-zA-Z0-9_]', '_', input_str)
    # Convert to lowercase
    return normalized.lower()

test_input = "Admin User #1 (Server)"
print(f"Original: {test_input}")
print(f"Normalized: {normalize_string(test_input)}")
