from flask import Flask, render_template, request
app = Flask(__name__)

# Function to perform Caesar Cipher encryption
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Handle alphabetic characters (both upper and lowercase)
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        elif char.isdigit():  # Handle numeric characters (0-9)
            encrypted_text += chr((ord(char) - 48 + shift) % 10 + 48)
        else:
            encrypted_text += char  # Non-alphabetic, non-numeric characters are unchanged
    return encrypted_text

# Function to perform Caesar Cipher decryption
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the form data
        message = request.form["message"]
        shift = int(request.form["shift"])
        action = request.form["action"]
        
        # Encrypt or decrypt based on the user's choice
        if action == "encrypt":
            result = caesar_encrypt(message, shift)
        else:
            result = caesar_decrypt(message, shift)
        
        return render_template("index.html", result=result, message=message, shift=shift, action=action)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
