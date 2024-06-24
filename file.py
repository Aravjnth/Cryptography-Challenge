from cryptography.fernet import Fernet

def generate_key():
    """
    Generate a secret key for encryption and decryption.
    """
    key = Fernet.generate_key()
    return key

def encrypt_message(key, message):
    """
    Encrypt a message using the given key.
    """
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(message.encode())
    return cipher_text

def decrypt_message(key, cipher_text):
    """
    Decrypt a cipher text using the given key.
    """
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text)
    return plain_text.decode()

def main():
    # Generate a secret key
    key = generate_key()
    print("Secret Key:", key.decode())

    # Input message to encrypt
    message = input("Enter a message to encrypt: ")

    # Encrypt the message
    cipher_text = encrypt_message(key, message)
    print("Encrypted Message:", cipher_text.decode())

    # Decrypt the cipher text
    plain_text = decrypt_message(key, cipher_text)
    print("Decrypted Message:", plain_text)

if __name__ == "__main__":
    main()
