def caesar_cipher(text, shift, mode):
    result = ""

    # Loop through each character in the text
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26
            if mode == 'decrypt':
                shift_amount = -shift_amount
            
            # Shift the character and handle wrapping around the alphabet
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')
                
            shifted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            result += shifted_char
        else:
            result += char  # Non-alphabetic characters are added unchanged

    return result

# Get input from the user
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))
mode = input("Choose mode (encrypt/decrypt): ").lower()

# Perform encryption or decryption
output = caesar_cipher(text, shift, mode)
print(f"Output: {output}")
