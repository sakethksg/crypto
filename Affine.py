def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def affine_encrypt(text, a, b):
    text = text.upper()
    result = ""

    for ch in text:
        if ch.isalpha():
            x = ord(ch) - 65
            e = (a * x + b) % 26
            result += chr(e + 65)
        else:
            result += ch

    return result


def affine_decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)
    # a_inv = pow(a, -1, 26)  Using built-in function for modular inverse

    if a_inv is None:
        raise ValueError("Invalid key! 'a' must be coprime with 26.")

    for ch in cipher:
        if ch.isalpha():
            y = ord(ch) - 65
            d = (a_inv * (y - b)) % 26
            result += chr(d + 65)
        else:
            result += ch

    return result


a = int(input("Enter multiplicative key (a): "))
b = int(input("Enter additive key (b): "))
text = input("Enter message: ")

if mod_inverse(a, 26) is None:
    print("Invalid key! Choose 'a' coprime with 26.")
else:
    encrypted = affine_encrypt(text, a, b)
    print("Encrypted:", encrypted)

    decrypted = affine_decrypt(encrypted, a, b)
    print("Decrypted:", decrypted)