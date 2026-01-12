from encryption import shift_lower, shift_upper

def decrypt_text(text, shift1, shift2):
    # A new string is built to avoid modifying the encrypted input directly
    result = ""
    for c in text:
        # Reversing the shift restores the original lowercase characters
        if 'a' <= c <= 'z':
            result += shift_lower(c, -shift1) 
            
            # Reversing the shift restores the original uppercase characters
        elif 'A' <= c <= 'Z':
            result += shift_upper(c, -shift2)  
        else:
            # Non-alphabet characters must remain unchanged for accurate recovery
            result += c
    return result
