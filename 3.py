def generate_public_key(prime, base, private_key):
    return pow(base, private_key, prime)

def generate_shared_secrete(public_key, private_key, prime):
    return pow(public_key, private_key, prime)

prime = int(input("enter a large prime number (recommended 2048 bits)"))
base = int(input("enter a base (primitive root modulo of prime)"))

alice_private = int(input("enter your private key (a random integer less than prime)"))
alice_public = generate_public_key(prime, base, alice_private)
print("Alice public key", alice_public)

bobs_private = int(input("enter your private key (a random integer less than prime)"))
bobs_public = generate_public_key(prime, base, bobs_private)
print("Bobs public key", bobs_public)

alice_shared = generate_shared_secrete(bobs_public, alice_private, prime)
bobs_shared = generate_shared_secrete(alice_public, bobs_private, prime)

print("Alice shared key", alice_shared)
print("Bobs shared key", bobs_shared)

if alice_shared == bobs_shared:
    print("Success the shared key is", alice_shared)
else:
    print("Error: shared key doesn't match")
