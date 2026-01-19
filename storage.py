def save_password(service, password):
    with open("data/passwords.txt", "a", encoding="utf-8") as f:
        f.write(f"{service}: {password}\n")