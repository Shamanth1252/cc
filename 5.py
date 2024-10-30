def generate_pubic_key(prime,base,private_key):
    return pow(base,private_key,prime)
def generate_shared_secret(public_key,private_key,prime):
    return pow(public_key,private_key,prime)
prime=int(input("enter the large prime number(recommanded>2048 bits)"))
base=int(input("enter the large prime number(recommanded>2048 bits)"))

aliceprivate=int(input("aliceenter your private key(a random interger less than the prime)"))
alice_public=generate_public_key(prime,base,alice_private)
print("Alice public key %d",alice_public)

bobprivate=int(input("aliceenter your private key(a random interger less than the prime)"))
bob_public=generate_public_key(prime,base,alice_private)
print("Alice public key %d",alice_public)

private("bobs publickey:",bob_public)

alice_shared_secret=generate_shared_secret(bob_public,aliceprivate,prime)
bob_shared_secret=generate_shared_secret(alice_public,bobprivate,prime)

print("Alice Shared secrte:",alice_shared_secret)
print("Bob shared secret",bob_shared_secret)

if alice_shared_secret== bob_shared_secret:
    print("Sucess the secret key is",alice_shared_secret)
else:
    print("Error :shared secret do not matched")

