from encryption import shift_lower, shift_upper

def decrypt_text(text, shift1, shift2):
    result = ""
    for c in text:
        if 'a' <= c <= 'z':
            result += shift_lower(c, -shift1)  # always backward
        elif 'A' <= c <= 'Z':
            result += shift_upper(c, -shift2)  # always backward
        else:
            result += c
    return result
