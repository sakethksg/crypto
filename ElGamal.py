import random
import math

def main():
    p = int(input("Enter prime (p): "))
    g = int(input("Enter alpha (g): "))
    x = int(input("Enter private key (x): "))
    m = int(input("Message: "))

    # Public key
    y = pow(g, x, p)

    # Random k (1 <= k <= p-2 and gcd(k, p-1) = 1)
    while True:
        k = random.randint(1, p - 2)
        if math.gcd(k, p - 1) == 1:
            break

    print("Random k used:", k)

    # Encryption
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p

    print("Public Key (y):", y)
    print("Ciphertext (c1):", c1)
    print("Ciphertext (c2):", c2)

    # Decryption
    s = pow(c1, x, p)
    s_inv = pow(s, -1, p)   # Modular inverse (Python 3.8+)
    decrypted_m = (c2 * s_inv) % p

    print("Decrypted Message:", decrypted_m)

if __name__ == "__main__":
    main()