from encryption import encrypt_text
from decryption import decrypt_text

def verify(original_text, decrypted_text):
    original_norm = ' '.join(original_text.split())
    decrypted_norm = ' '.join(decrypted_text.split())
    
    if original_norm == decrypted_norm:
        print("Yay! Decryption worked, it matches the original text.")
    else:
        print("Decryption failed! Text does not match original.")

with open("raw_text.txt", "r") as f:
    raw_text = f.read().replace('\r', '')

shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))

encrypted_text = encrypt_text(raw_text, shift1, shift2)
with open("encrypted_text.txt", "w") as f:
    f.write(encrypted_text)
print("Encryption done. Check 'encrypted_text.txt'.")

decrypted_text = decrypt_text(encrypted_text, shift1, shift2)
with open("decrypted_text.txt", "w") as f:
    f.write(decrypted_text)
print("Decryption done. Check 'decrypted_text.txt'.")

verify(raw_text, decrypted_text)
