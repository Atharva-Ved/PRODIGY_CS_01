def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char) + shift_amount - 65) % 26 + 65) if char.isupper() else chr((ord(char) + shift_amount - 97) % 26 + 97)
            encrypted_message += new_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char) - shift_amount - 65) % 26 + 65) if char.isupper() else chr((ord(char) - shift_amount - 97) % 26 + 97)
            decrypted_message += new_char
        else:
            decrypted_message += char
    return decrypted_message

def main():
    print("Welcome to the Caesar Cipher program!")
    print("You can encrypt or decrypt messages using a shift value with caesar cipher algorithm.")
    print("Please follow the prompts to enter your message and shift value.")
    
    while True:
        choice = input("Enter '0' to encrypt a message, '1' to decrypt a message, or '2' to exit: ").strip()
        
        if choice == '2':
            print("Exiting the program. Goodbye!")
            break
        
        message = input("Enter your message: ")
        
        while True:
            try:
                shift = int(input("Enter the shift value (0-25): "))
                if 0 <= shift <= 25:
                    break
                else:
                    print("Shift value must be between 0 and 25. Please try again.")
            except ValueError:
                print("Invalid input. Please enter an integer between 0 and 25.")

        if choice == '0':
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        elif choice == '1':
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")
        else:
            print("Invalid choice. Please enter '0' for encrypt, '1' for decrypt, or '2' to exit.")

if __name__ == "__main__":
    main()
