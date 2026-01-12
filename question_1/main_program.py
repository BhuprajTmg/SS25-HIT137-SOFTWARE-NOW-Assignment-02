from encryption import encrypt_text
from decryption import decrypt_text

def verify(original_text, decrypted_text):
    # Normalising whitespace ensures minor formatting differences do not affect comparison
    original_norm = ' '.join(original_text.split())
    decrypted_norm = ' '.join(decrypted_text.split())
    
    # This confirms whether the encryption and decryption process was mathematically correct
    if original_norm == decrypted_norm:
        print("Decryption worked, it matches the original text.")
    else:
        print("Decryption failed! Text does not match original.")
        
# Reading the raw file provides a real-world input source for encryption
with open("raw_text.txt", "r") as f:
    raw_text = f.read().replace('\r', '')
    
# User supplied shift values allow the encryption key to be changed each time
shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))

# Encrypting the text before saving prevents the original data from being stored in plain form
encrypted_text = encrypt_text(raw_text, shift1, shift2)
with open("encrypted_text.txt", "w") as f:
    f.write(encrypted_text)
print("Encryption done. Check 'encrypted_text.txt'.")

# Decrypting verifies that the algorithm can correctly reverse the encryption
decrypted_text = decrypt_text(encrypted_text, shift1, shift2)
with open("decrypted_text.txt", "w") as f:
    f.write(decrypted_text)
print("Decryption done. Check 'decrypted_text.txt'.")

# Final verification confirms whether the system preserved the original data correctly
verify(raw_text, decrypted_text)
