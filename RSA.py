def main():
    print("Enter first prime number (p): ", end="")
    p = int(input())

    print("Enter second prime number (q): ", end="")
    q = int(input())

    n = p * q
    phi = (p - 1) * (q - 1)

    print("Enter public exponent (e) [must be coprime to phi]: ", end="")
    e = int(input())
    d = pow(e, -1, phi)

    print(f"Public Key: {{e={e}, n={n}}}")
    print(f"Private Key: {{d={d}, n={n}}}")

    print("\nEnter a numeric message to encrypt: ", end="")
    message = int(input())

    encrypted = pow(message, e, n)
    print("Encrypted Message:", encrypted)

    decrypted = pow(encrypted, d, n)
    print("Decrypted Message:", decrypted)

if __name__ == "__main__":
    main()