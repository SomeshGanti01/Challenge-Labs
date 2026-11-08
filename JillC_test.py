import hashlib
import itertools

SALT = "www.exploringsecurity.com"
TARGET = "f44f3b09df53c1c11273def13cacd8922a86d48c"

leet = {
    "a": "a4@",
    "e": "e3",
    "i": "i1!",
    "o": "o0",
    "s": "s5$",
    "t": "t7"
}

def check(password):
    if 5 <= len(password) <= 7:
        hashed = hashlib.sha1(
            (SALT + password).encode()
        ).hexdigest()

        if hashed == TARGET:
            print("\nPASSWORD FOUND:", password)
            return True
    return False

with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
    for count, line in enumerate(f, 1):
        word = line.strip()

        if not word:
            continue

        variants = {
            word.lower(),
            word.upper(),
            word.capitalize(),
            word.title(),
            word[::-1]
        }

        for candidate in variants:
            if check(candidate):
                raise SystemExit

        if len(word) <= 7:
            choices = [
                leet.get(c, c)
                for c in word.lower()
            ]

            for combo in itertools.product(*choices):
                if check("".join(combo)):
                    raise SystemExit

        if count % 10000 == 0:
            print("Processed:", count, "lines", flush=True)

print("\nNo match found in this search.")