import random
import math

def main():
    p = int(input("Enter prime (p): "))
    g = int(input("Enter alpha (g): "))
    x = int(input("Enter private key (x): "))

    y = pow(g, x, p)

    while True:
        k = random.randint(1, p - 2)
        if math.gcd(k, p - 1) == 1:
            break

    print("Random k used:", k)
    print("Public Key (y):", y)

    # =====(NUMERIC MESSAGE) =====
    # m = int(input("Message: "))
    # c1 = pow(g, k, p)
    # c2 = (m * pow(y, k, p)) % p
    #
    # print("Ciphertext (c1):", c1)
    # print("Ciphertext (c2):", c2)
    #
    # s = pow(c1, x, p)
    # s_inv = pow(s, -1, p)
    # decrypted_m = (c2 * s_inv) % p
    #
    # print("Decrypted Message:", decrypted_m)


    # ===== (STRING MESSAGE) =====
    message = input("Message: ")
    encrypted = []

    for ch in message:
        m = ord(ch)
        c1 = pow(g, k, p)
        c2 = (m * pow(y, k, p)) % p
        encrypted.append((c1, c2))

    print("Ciphertext:", encrypted)

    decrypted_message = ""

    for c1, c2 in encrypted:
        s = pow(c1, x, p)
        s_inv = pow(s, -1, p)
        decrypted_m = (c2 * s_inv) % p
        decrypted_message += chr(decrypted_m)

    print("Decrypted Message:", decrypted_message)


if __name__ == "__main__":
    main()