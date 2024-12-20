def generate_public_key(prime, base, private_key):
    return pow(base, private_key, prime)

def generate_shared_secret(public_key, private_key, prime):
    return pow(public_key, private_key, prime)

# Input prime and base
prime = int(input("Enter a large prime number (recommended > 2048 bits): "))
base = int(input("Enter a base (recommended < prime): "))

# Alice's private key
alice_private = int(input("Alice, enter your private key (a random integer less than the prime): "))
alice_public = generate_public_key(prime, base, alice_private)
print("Alice's public key:", alice_public)

# Bob's private key
bob_private = int(input("Bob, enter your private key (a random integer less than the prime): "))
bob_public = generate_public_key(prime, base, bob_private)
print("Bob's public key:", bob_public)

# Generate shared secrets
alice_shared_secret = generate_shared_secret(bob_public, alice_private, prime)
bob_shared_secret = generate_shared_secret(alice_public, bob_private, prime)

print("Alice's shared secret:", alice_shared_secret)
print("Bob's shared secret:", bob_shared_secret)

# Verify if the shared secrets match
if alice_shared_secret == bob_shared_secret:
    print("Success! The shared secret key is:", alice_shared_secret)
else:
    print("Error: shared secrets do not match.")
