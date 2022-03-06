import bcrypt


def generate(rounds):
    password = input("Enter a master password: ").encode()

    with open("key.dat", "wb") as file:
        hashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds=rounds))
        file.write(hashed)

    return hashed
