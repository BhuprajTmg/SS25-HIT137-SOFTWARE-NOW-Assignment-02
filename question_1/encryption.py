def shift_lower(c, shift):
    pos = ord(c) - ord('a')
    pos = (pos + shift) % 26
    return chr(pos + ord('a'))

def shift_upper(c, shift):
    pos = ord(c) - ord('A')
    pos = (pos + shift) % 26
    return chr(pos + ord('A'))

def encrypt_text(text, shift1, shift2):
    result = ""
    for c in text:
        if 'a' <= c <= 'z':
            result += shift_lower(c, shift1)  # always forward
        elif 'A' <= c <= 'Z':
            result += shift_upper(c, shift2)  # always forward
        else:
            result += c
    return result
