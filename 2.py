def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def generate_key(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    while gcd(e, phi) != 1:
        e += 1
    d = modinv(e, phi)
    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

if __name__ == '__main__':
    p = int(input("Enter prime p: "))
    q = int(input("Enter prime q: "))
    public_key, private_key = generate_key(p, q)
    print(f"Public key: {public_key}")
    print(f"Private key: {private_key}")
    message = input("Enter message: ")
    encrypted_message = encrypt(public_key, message)
    print(f"Encrypted message: {encrypted_message}")
    decrypted_message = decrypt(private_key, encrypted_message)
    print(f"Decrypted message: {decrypted_message}")
