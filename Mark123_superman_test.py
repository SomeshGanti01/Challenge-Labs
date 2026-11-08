
import hashlib

salt = "www.exploringsecurity.com"

targets = {
    "Sparky": "2834da08d58330d8dafbb2ac1c0f85f6b3b135ef",
    "Mark123": "92e54f10103a3c511853c7098c04141f114719c1",
    "superman": "437fbc6892b38db6ac5bdbe2eab3f7bc924527d9",
    "JillC": "f44f3b09df53c1c11273def13cacd8922a86d48c",
}

# Initial candidate passwords to test
candidates = [
    "password", "Password", "password123",
    "admin", "admin123", "123456",
    "superman", "Superman", "sparky",
    "Sparky", "mark123", "Mark123",
    "security", "Security", "tomtom",
    "Tomtom", "jillc", "JillC",
    "qwerty", "welcome", "letmein",
]

for username, target in targets.items():
    found = False

    for password in candidates:
        if not 5 <= len(password) <= 7:
            continue

        calculated = hashlib.sha1(
            (salt + password).encode()
        ).hexdigest()

        if calculated == target:
            print(f"FOUND: {username} = {password}")
            found = True
            break

    if not found:
        print(f"Not found in initial candidates: {username}")
