import bcrypt, getpass


KEY_ROUNDS = 14  # increase for complexity
KEY_FILENAME = "key.dat"


def dump_key(key: bytes):
    with open(KEY_FILENAME, "wb") as file:
        file.write(key)


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


def login(key):
    for _ in range(3):
        master_password = getpass.getpass("Master password: ").encode()

        if bcrypt.checkpw(master_password, key):
            return master_password

        print("Sorry, try again.")

    print("3 incorrect password attempts.")


def load_key():
    try:
        with open(KEY_FILENAME, "rb") as file:
            key = file.read().strip()
            if not key:
                raise Exception("Empty 'key.dat' file")

    except:
        key = generate_key(KEY_ROUNDS)
        dump_key(key)  # write key to file

    return login(key)
