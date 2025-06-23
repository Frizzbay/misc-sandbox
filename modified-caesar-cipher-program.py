# Get the text to encrypt from user
text_to_encrypt = input("Enter text to encrypt: ")

# Get shift value with validation loop
while True:
    try:
        # Ask user for shift value
        shift = int(input("Enter shift value (1-25): "))
        
        # Check if shift is in valid range
        if 1 <= shift <= 25:
            break  # Exit loop if valid
        else:
            print("Shift must be between 1 and 25. Try again.")
    except ValueError:
        # Handle case where user enters non-integer
        print("Please enter a valid integer.")

# Initialize empty string to store encrypted result
encrypted_text = ""

# Iterate through each character in the input text
for char in text_to_encrypt:
    # Check if character is a letter
    if char.isalpha():
        # Handle lowercase letters
        if char.islower():
            # Convert lowercase letter to position (a=0, b=1, ..., z=25)
            char_position = ord(char) - ord('a')
            # Apply shift and wrap around using modulus
            new_position = (char_position + shift) % 26
            # Convert back to lowercase letter
            encrypted_char = chr(new_position + ord('a'))
        
        # Handle uppercase letters
        else:  # char.isupper()
            # Convert uppercase letter to position (A=0, B=1, ..., Z=25)
            char_position = ord(char) - ord('A')
            # Apply shift and wrap around using modulus
            new_position = (char_position + shift) % 26
            # Convert back to uppercase letter
            encrypted_char = chr(new_position + ord('A'))
        
        # Add the shifted character to result
        encrypted_text += encrypted_char
    
    else:
        # Non-alphabetical characters remain unchanged
        encrypted_text += char

# Print the final encrypted text
print("Encrypted text:", encrypted_text)