import getpass, bcrypt

def prompt_login(key):
    for _ in range(3):
        master_password = getpass.getpass("Master password: ").encode()

        if bcrypt.checkpw(master_password, key):
            return master_password

        print("Sorry, try again.")

    print("3 incorrect password attempts.")