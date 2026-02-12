# Diffie-Hellman with a and b derived from user input

roll = input("Enter your roll number: ")
name = input("Enter your name: ")

# a = last 4 digits of roll number
a = int(roll[-4:])

# b = number of letters in name (ignoring spaces)
b = len(name.replace(" ", ""))

p = int(input("Enter a prime number (P): "))
g = int(input("Enter a primitive root (G): "))

# Public keys
# A = g^a mod p
A = pow(g, a, p)

# B = g^b mod p
B = pow(g, b, p)

print("\nAlice private key (a):", a)
print("Bob private key (b):", b)

print("Alice sends to Bob:", A)
print("Bob sends to Alice:", B)

# Shared Secret
# K = B^a mod p = A^b mod p
keyA = pow(B, a, p)
keyB = pow(A, b, p)

print("\nShared Secrets:")
print("Alice's Secret Key:", keyA)
print("Bob's Secret Key:", keyB)