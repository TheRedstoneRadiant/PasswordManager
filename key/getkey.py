import bcrypt, getpass


KEY_FILENAME = "key.dat"


def dump_key(key: bytes):
    with open(KEY_FILENAME, "wb") as file:
        file.write(key)


def load_key():
    with open(KEY_FILENAME, "rb") as file:
        key = file.read().strip()
        if not key:
            raise Exception("Empty 'key.dat' file")

    return key


def prompt_password():
    password = getpass.getpass("Enter a new master password: ")
    confirmation = getpass.getpass("Confirm master password: ")

    while password != confirmation:
        print("Passwords do not match. Try again.")
        return prompt_password()

    return password


def generate_key(rounds):
    password = prompt_password()
    salt = bcrypt.gensalt(rounds=rounds)

    return bcrypt.hashpw(password, salt)