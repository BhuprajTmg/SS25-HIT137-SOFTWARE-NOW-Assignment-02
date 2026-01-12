def verify(original_text, decrypted_text):
    if original_text == decrypted_text:
        print("Decryption successful! Text matches original.")
    else:
        print("Decryption failed! Text does not match original.")