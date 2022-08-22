import bcrypt, getpass


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