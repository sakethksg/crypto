def xor_strings(s1, s2):
    result = ""
    for i in range(len(s1)):
        result += chr(ord(s1[i]) ^ ord(s2[i]))
    return result

text = "HELLO"
key = "XMCKL"

cipher = xor_strings(text, key)
print("Encrypted:", cipher)

decrypted = xor_strings(cipher, key)
print("Decrypted:", decrypted)