
# def mod_inverse(a, m):
#     a = a % m
#     for x in range(1, m):
#         if (a * x) % m == 1:
#             return x
#     return None

def matrix_inverse_2x2(key):
    a, b = key[0]
    c, d = key[1]

    det = (a*d - b*c) % 26
    det_inv = pow(det, -1, 26)
    # det_inv = mod_inverse(det, 26)

    inv = [
        [( d * det_inv) % 26, (-b * det_inv) % 26],
        [(-c * det_inv) % 26, ( a * det_inv) % 26]
    ]
    return inv


def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"

    result = ""

    for i in range(0, len(text), 2):
        x1 = ord(text[i]) - 65
        x2 = ord(text[i+1]) - 65

        c1 = (key[0][0]*x1 + key[0][1]*x2) % 26
        c2 = (key[1][0]*x1 + key[1][1]*x2) % 26

        result += chr(c1 + 65) + chr(c2 + 65)

    return result


def hill_decrypt(cipher, key):
    inv_key = matrix_inverse_2x2(key)
    return hill_encrypt(cipher, inv_key)


# ===== INPUT =====
print("Enter key matrix values:")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

key = [[a, b], [c, d]]

text = input("Enter message: ")

encrypted = hill_encrypt(text, key)
print("Encrypted:", encrypted)

decrypted = hill_decrypt(encrypted, key)
print("Decrypted:", decrypted)