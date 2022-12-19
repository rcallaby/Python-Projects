
import random
import math

# Generate two prime numbers
prime1 = random.randint(100, 1000)
prime2 = random.randint(100, 1000)

# Calculate n and m
n = prime1 * prime2
m = (prime1-1) * (prime2-1)

# Generate a coprime of m
gcd = 0
while gcd != 1:
    e = random.randint(2, m)
    gcd = math.gcd(e, m)

# Calculate d
d = 0
while (e*d) % m != 1:
    d += 1

# Print out the public and private keys
print("Public key: (", e, ",", n, ")")
print("Private key: (", d, ",", n, ")")
