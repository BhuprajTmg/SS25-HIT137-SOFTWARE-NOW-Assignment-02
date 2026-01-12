def shift_lower(c, shift):
    # Converts a lowercase letter into a numerical position (0–25) so it can be shifted mathematically
    pos = ord(c) - ord('a')
    # Modulo 26 ensures the alphabet wraps correctly when the shift exceeds 'z'
    pos = (pos + shift) % 26
    return chr(pos + ord('a')) # Converts the shifted numeric position back into a character

def shift_upper(c, shift):
    # Converts an uppercase letter into a number so it can be shifted using arithmetic
    pos = ord(c) - ord('A')
    # Using modulo prevents overflow past 'Z' and keeps results inside the alphabet
    pos = (pos + shift) % 26
     # Converts the final position back into an uppercase character
    return chr(pos + ord('A'))

def encrypt_text(text, shift1, shift2):
     # The result string is built character-by-character to preserve spaces and punctuation
    result = ""
    for c in text:
         # Lowercase and uppercase letters use different shifts to increase encryption strength
        if 'a' <= c <= 'z':
            result += shift_lower(c, shift1)  # always forward
        elif 'A' <= c <= 'Z':
            result += shift_upper(c, shift2)  # always forward
        else:
            # Non-alphabet characters are left unchanged so formatting is preserved
            result += c
    return result
