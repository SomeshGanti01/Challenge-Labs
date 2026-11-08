
import hashlib
import itertools
import string

salt = "www.exploringsecurity.com"

targets = {
    "Sparky": "2834da08d58330d8dafbb2ac1c0f85f6b3b135ef",
    "JillC": "f44f3b09df53c1c11273def13cacd8922a86d48c",
}

def hash_password(password):
    return hashlib.sha1(
        (salt + password).encode()
    ).hexdigest()

words = [
    "sparky", "Sparky", "SPARKY",
    "jillc", "JillC", "JILLC",
    "jill", "Jill", "password",
    "qwerty", "welcome", "admin",
    "dragon", "monkey", "secret",
]

candidates = set(words)

# Generate common numeric suffixes and prefixes
for word in words:
    for number in range(10000):
        n = str(number)

        for password in (word + n, n + word):
            if 5 <= len(password) <= 7:
                candidates.add(password)

print("Total candidates:", len(candidates))

for username, target in targets.items():
    found = False

    for password in candidates:
        if hash_password(password) == target:
            print("FOUND:", username, "=", password)
            found = True
            break

    if not found:
        print("Not found yet:", username)
