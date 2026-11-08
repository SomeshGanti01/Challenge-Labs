
import hashlib
import itertools
import string
import time

targets = {
    "security": "fafa4483874ec051989d53e1e432ba3a6c6b9143",
    "Tomtom": "06f6fe0f73c6e197ee43eff4e5f7d10fb9e438b2",
}

salts = [
    "www.exploringsecurity.com"
]

def sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()

start = time.time()

for salt in salts:
    print("\nTesting salt:", salt)

    for username, target in targets.items():
        found = False

        for length in range(5, 8):
            for digits in itertools.product("0123456789", repeat=length):
                password = "".join(digits)

                candidates = [
                    salt + password,
                    password + salt
                ]

                for candidate in candidates:
                    if sha1(candidate) == target:
                        print("FOUND:", username, password)
                        found = True
                        break

                if found:
                    break

                if found:
                    break


        if not found:
            print("Not found:", username)

print("\nTime:", round(time.time() - start, 2), "seconds")
