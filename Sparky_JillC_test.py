
import hashlib
import itertools

salt = "www.exploringsecurity.com"
wordlist = "rockyou.txt"

targets = {
    "Sparky": "2834da08d58330d8dafbb2ac1c0f85f6b3b135ef",
    "JillC": "f44f3b09df53c1c11273def13cacd8922a86d48c",
}

def check(password):
    digest = hashlib.sha1(
        (salt + password).encode("utf-8")
    ).hexdigest()

    for username, target in targets.items():
        if digest == target:
            return username

    return None

found = set()
tested = set()

def test(password):
    if not 5 <= len(password) <= 7:
        return

    if password in tested:
        return

    tested.add(password)
    username = check(password)

    if username and username not in found:
        print("FOUND:", username, "=", password)
        found.add(username)

print("Starting variation search...")

with open(wordlist, "r", encoding="utf-8", errors="ignore") as file:
    for line_number, line in enumerate(file, 1):
        word = line.strip()

        if not word.isalnum() or not 3 <= len(word) <= 7:
            continue

        variants = {
            word.lower(),
            word.upper(),
            word.capitalize()
        }

        for base in variants:
            test(base)

            for number in range(100):
                digits = str(number)

                test(base + digits)
                test(digits + base)

        if line_number % 100000 == 0:
            print("Lines processed:", line_number,
                  "| Candidates tested:", len(tested),
                  "| Recovered:", len(found))

        if len(found) == len(targets):
            break

print("\nSearch finished.")
print("Total candidates tested:", len(tested))

for username in targets:
    if username not in found:
        print("Not recovered:", username)
