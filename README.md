
---
## 1. RSA

**Aim:** 
To implement RSA public-key cryptosystem for secure data transmission.

**Objective:**
- Generate public and private key pairs using large prime numbers
- Perform encryption of plaintext using public key
- Perform decryption of ciphertext using private key
- Understand the mathematical foundations of trapdoor functions

**Algorithm:**

**Key Generation:**
1. Select two large prime numbers $p$ and $q$.
2. Compute $n = p \times q$.
3. Compute Euler's totient function $\phi(n) = (p-1)(q-1)$.
4. Choose public exponent $e$ such that $1 < e < \phi(n)$ and $\gcd(e, \phi(n)) = 1$.
5. Compute private key $d$ where $d \equiv e^{-1} \pmod{\phi(n)}$ using Extended Euclidean Algorithm.
6. Public Key: $(e, n)$, Private Key: $(d, n)$.

**Encryption:**
1. Convert plaintext message $m$ to integer such that $0 \leq m < n$.
2. Compute ciphertext $c = m^e \mod n$.

**Decryption:**
1. Compute plaintext $m = c^d \mod n$.
2. Convert integer $m$ back to plaintext.

---

## 2. ElGamal

**Aim:** 
To implement ElGamal public-key cryptosystem based on Discrete Logarithm Problem.

**Objective:**
- Generate key pairs using cyclic groups
- Understand the probabilistic nature of encryption
- Perform encryption and decryption operations
- Analyze security based on discrete logarithm hardness

**Algorithm:**

**Key Generation:**
1. Select a large prime number $p$.
2. Choose a generator $g$ of the multiplicative group $\mathbb{Z}_p^*$.
3. Select private key $x$ such that $1 < x < p-1$.
4. Compute public key $y = g^x \mod p$.
5. Public Key: $(p, g, y)$, Private Key: $x$.

**Encryption:**
1. Choose random ephemeral key $k$ such that $1 < k < p-1$.
2. Compute $c_1 = g^k \mod p$.
3. Compute $c_2 = m \cdot y^k \mod p$ (where $m$ is plaintext integer).
4. Ciphertext: $(c_1, c_2)$.

**Decryption:**
1. Compute shared secret $s = c_1^x \mod p$.
2. Compute modular inverse $s^{-1} \mod p$.
3. Recover plaintext $m = c_2 \cdot s^{-1} \mod p$.

---

## 3. Diffie-Hellman Key Exchange (2-Party)

**Aim:** 
To establish a shared secret key over an insecure channel between two parties.

**Objective:**
- Enable two parties to agree on a common secret key without pre-sharing
- Prevent eavesdroppers from deriving the shared secret
- Understand the Discrete Logarithm Problem
- Provide foundation for many modern key exchange protocols

**Algorithm:**

**Setup (Public Parameters):**
1. Agree on a large prime number $p$.
2. Agree on a generator $g$ of $\mathbb{Z}_p^*$.

**Key Exchange:**
1. **Alice:** 
   - Choose private key $a$ randomly where $1 < a < p-1$.
   - Compute public value $A = g^a \mod p$.
   - Send $A$ to Bob.

2. **Bob:**
   - Choose private key $b$ randomly where $1 < b < p-1$.
   - Compute public value $B = g^b \mod p$.
   - Send $B$ to Alice.

3. **Alice computes shared secret:** $s = B^a \mod p = (g^b)^a = g^{ab} \mod p$.

4. **Bob computes shared secret:** $s = A^b \mod p = (g^a)^b = g^{ab} \mod p$.

**Shared Secret:**
$$K = g^{ab} \mod p$$

---

## 4. Diffie-Hellman Key Exchange (3-Party)

**Aim:** 
To establish a shared secret key among three parties over an insecure channel.

**Objective:**
- Extend 2-party Diffie-Hellman to three participants
- Enable all three parties to compute the same shared secret
- Minimize number of communication rounds
- Maintain security against eavesdroppers

**Algorithm:**

**Setup (Public Parameters):**
1. Agree on a large prime number $p$.
2. Agree on a generator $g$ of $\mathbb{Z}_p^*$.

**Round 1 (Broadcast):**
1. **Alice:** Choose private $a$, compute $A = g^a \mod p$, send $A$ to Bob.
2. **Bob:** Choose private $b$, compute $B = g^b \mod p$, send $B$ to Carol.
3. **Carol:** Choose private $c$, compute $C = g^c \mod p$, send $C$ to Alice.

**Round 2 (Compute and Forward):**
1. **Alice:** Compute $A' = C^a = g^{ac} \mod p$, send $A'$ to Bob.
2. **Bob:** Compute $B' = A^b = g^{ab} \mod p$, send $B'$ to Carol.
3. **Carol:** Compute $C' = B^c = g^{bc} \mod p$, send $C'$ to Alice.

**Round 3 (Final Computation):**
1. **Alice:** Compute $K = (C')^a = (g^{bc})^a = g^{abc} \mod p$.
2. **Bob:** Compute $K = (A')^b = (g^{ac})^b = g^{abc} \mod p$.
3. **Carol:** Compute $K = (B')^c = (g^{ab})^c = g^{abc} \mod p$.

**Shared Secret:**
$$K = g^{abc} \mod p$$

---

## 5. Extended Euclidean Algorithm

**Aim:** 
To find the greatest common divisor (GCD) of two integers and express it as a linear combination.

**Objective:**
- Compute $\gcd(a, b)$ efficiently
- Find integer coefficients $x$ and $y$ satisfying $ax + by = \gcd(a, b)$
- Compute modular multiplicative inverses for RSA and other cryptosystems
- Solve linear Diophantine equations

**Algorithm:**

**Extended Euclidean Algorithm:**
```
Input: Integers a, b with a ≥ b ≥ 0
Output: (g, x, y) such that g = gcd(a, b) and ax + by = g

function egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (g, x₁, y₁) = egcd(b, a mod b)
        x = y₁
        y = x₁ - floor(a/b) * y₁
        return (g, x, y)
```

**Modular Inverse Algorithm:**
```
Input: Integer a, modulus n (where gcd(a, n) = 1)
Output: a⁻¹ mod n

1. (g, x, y) = egcd(a, n)
2. If g ≠ 1, inverse does not exist
3. Return x mod n
```

**Example Application:**
For RSA: $d \equiv e^{-1} \pmod{\phi(n)}$ computed using Extended Euclidean Algorithm.

---

## 6. Hill Cipher

**Aim:** 
To implement a polygraphic substitution cipher using linear algebra.

**Objective:**
- Encrypt blocks of plaintext simultaneously
- Understand the role of matrix invertibility in cryptography
- Perform encryption and decryption using matrix operations modulo 26
- Analyze security based on key matrix size

**Algorithm:**

**Key Generation:**
1. Choose an $n \times n$ invertible matrix $K$ modulo 26.
2. Verify that $\det(K)$ is coprime with 26 (to ensure invertibility).
3. Compute $K^{-1} \mod 26$ using matrix inversion with modular arithmetic.

**Encryption:**
1. Convert plaintext letters to numbers (A=0, B=1, ..., Z=25).
2. Group plaintext into vectors $P$ of length $n$ (pad if necessary).
3. For each plaintext vector $P$, compute ciphertext vector:
   $$C = K \cdot P \mod 26$$
4. Convert numbers back to letters.

**Decryption:**
1. Convert ciphertext letters to numbers.
2. Group into vectors $C$ of length $n$.
3. For each ciphertext vector $C$, compute plaintext vector:
   $$P = K^{-1} \cdot C \mod 26$$
4. Convert numbers back to letters.

**Matrix Inversion Modulo 26:**
1. Compute determinant $d = \det(K)$.
2. Find $d^{-1} \mod 26$ using Extended Euclidean Algorithm.
3. Compute adjugate matrix $\text{adj}(K)$.
4. Compute $K^{-1} = (d^{-1} \cdot \text{adj}(K)) \mod 26$.

---

## 7. Vigenère Cipher

**Aim:** 
To implement a polyalphabetic substitution cipher using a keyword.

**Objective:**
- Overcome frequency analysis weakness of monoalphabetic ciphers
- Encrypt plaintext using Caesar shift with varying key values
- Understand the role of key length in cryptographic strength
- Perform encryption and decryption using modular arithmetic

**Algorithm:**

**Key Setup:**
1. Choose keyword $K$ of length $m$.
2. Convert keyword letters to numerical values $(k_0, k_1, ..., k_{m-1})$ where A=0, B=1, ..., Z=25.

**Encryption:**
1. Convert plaintext $P$ to numerical values $(p_0, p_1, ..., p_{n-1})$.
2. For each position $i$ from 0 to $n-1$:
   $$c_i = (p_i + k_{i \mod m}) \mod 26$$
3. Convert ciphertext values back to letters.

**Decryption:**
1. Convert ciphertext $C$ to numerical values $(c_0, c_1, ..., c_{n-1})$.
2. For each position $i$ from 0 to $n-1$:
   $$p_i = (c_i - k_{i \mod m}) \mod 26$$
3. Convert plaintext values back to letters.

**Variant - Beaufort Cipher:**
$$c_i = (k_{i \mod m} - p_i) \mod 26$$
$$p_i = (k_{i \mod m} - c_i) \mod 26$$

---
## 8. Playfair Cipher

**Aim:** 
To implement a digraph substitution cipher that encrypts pairs of letters using a 5×5 matrix key.

**Objective:**
- Encrypt plaintext in pairs (digraphs) rather than single letters
- Generate a 5×5 key matrix from a keyword
- Understand how Playfair cipher improves security over simple substitution
- Apply specific encryption rules for digraph processing
- Perform decryption by reversing the encryption rules

**Algorithm:**

**Key Matrix Generation:**
1. Choose a keyword (remove duplicate letters).
2. Fill the 5×5 matrix row-wise with keyword letters.
3. Fill remaining positions with rest of alphabet (I and J combined in single cell).
4. Result: 5×5 grid of 25 letters.

**Preprocessing Plaintext:**
1. Convert to uppercase, replace J with I.
2. Split into digraphs (pairs of letters):
   - If both letters in a digraph are same, insert 'X' between them
   - If odd number of letters, append 'X' at the end
3. Examples: HE LL O → HE LX LO; BALLOON → BA LX LO ON

**Encryption Rules (for digraph (a, b)):**

Let (row₁, col₁) = position of a in matrix
Let (row₂, col₂) = position of b in matrix

**Rule 1 - Same row:**
Shift both letters right by 1 (wrap around)
- a' = matrix[row₁][(col₁ + 1) mod 5]
- b' = matrix[row₂][(col₂ + 1) mod 5]

**Rule 2 - Same column:**
Shift both letters down by 1 (wrap around)
- a' = matrix[(row₁ + 1) mod 5][col₁]
- b' = matrix[(row₂ + 1) mod 5][col₂]

**Rule 3 - Different row and column:**
Swap columns (rectangle rule)
- a' = matrix[row₁][col₂]
- b' = matrix[row₂][col₁]

**Decryption Rules:**

**Rule 1 - Same row:**
Shift both letters left by 1 (wrap around)
- a = matrix[row₁][(col₁ - 1) mod 5]
- b = matrix[row₂][(col₂ - 1) mod 5]

**Rule 2 - Same column:**
Shift both letters up by 1 (wrap around)
- a = matrix[(row₁ - 1) mod 5][col₁]
- b = matrix[(row₂ - 1) mod 5][col₂]

**Rule 3 - Different row and column:**
Swap columns (rectangle rule - same as encryption)
- a = matrix[row₁][col₂]
- b = matrix[row₂][col₁]

**Postprocessing:**
1. Remove inserted 'X' characters that were added:
   - Remove X if it appears between identical letters
   - Remove trailing X added for padding
2. Replace I with appropriate J if needed

---