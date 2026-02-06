# ================================
# PASSWORD GENERATOR APPLICATION
# ================================
# This program allows the user to:
# 1. Specify password length
# 2. Generate a random password
# 3. Display the password

import random
import string

print("\n--- PASSWORD GENERATOR ---")
length = int(input("Enter password length: "))

# Characters include letters, digits, and symbols
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = "".join(random.choice(characters) for i in range(length))

print("Generated Password:", password)