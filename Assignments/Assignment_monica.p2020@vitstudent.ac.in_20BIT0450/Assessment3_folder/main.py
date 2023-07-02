from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generate a random 256-bit encryption key
key = get_random_bytes(32)

# Initialize AES cipher with the generated key and AES.MODE_ECB mode (electronic codebook)
cipher = AES.new(key, AES.MODE_ECB)

# Padding function to ensure the input data is a multiple of 16 bytes (AES block size)
def pad_data(data):
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len] * pad_len)

# Encryption function
def encrypt(plain_text):
    padded_text = pad_data(plain_text)
    encrypted_data = cipher.encrypt(padded_text)
    return encrypted_data

# Decryption function
def decrypt(cipher_text):
    decrypted_data = cipher.decrypt(cipher_text)
    pad_len = decrypted_data[-1]
    return decrypted_data[:-pad_len]

# Test encryption and decryption
message = b"Hello, AES!"
encrypted_message = encrypt(message)
decrypted_message = decrypt(encrypted_message)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
