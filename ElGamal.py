def main():
    print("Enter prime (p): ")
    p = int(input())

    print("Enter alpha: ")
    g = int(input())

    print("Enter private key (x): ")
    x = int(input())

    print("Enter random k: ")
    k = int(input())

    print("Message: ")
    m = int(input())

    # Public key
    y = pow(g, x, p)

    # Encryption
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p

    print("Public Key (y):", y)
    print("Ciphertext (c1):", c1)
    print("Ciphertext (c2):", c2)

    # Decryption
    s = pow(c1, x, p)
    s_inv = pow(s, -1, p)
    decrypted_m = (c2 * s_inv) % p

    print("Decrypted Message:", decrypted_m)


if __name__ == "__main__":
    main()