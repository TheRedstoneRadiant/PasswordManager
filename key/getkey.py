import bcrypt, getpass
from key.generate import generate


def getkey():
    try:
        with open("key.dat", "rb") as file:
            key = file.read()
            if not key.strip():
                raise FileNotFoundError
    except FileNotFoundError:
        rounds = 14  # set higher for increased security
        key = generate(rounds)  # prompt user for new master password

    master_password = getpass.getpass("Master password: ").encode()
    remaining_attempts = 2

    while not bcrypt.checkpw(master_password, key):
        if not remaining_attempts:
            print("3 incorrect password attempts.")
            return

        print("Sorry, try again.")
        remaining_attempts -= 1
        master_password = getpass.getpass("Master password: ").encode()

    return master_password
