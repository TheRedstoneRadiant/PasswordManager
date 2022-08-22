#!/usr/bin/env python3

from key.getkey import getkey
from passwords.passwords import decrypt_passwords

if __name__ == "__main__":
    master_password = getkey()

    if master_password is None:
        exit()

    option = input(
        """
1. List a password
2. Create a password
> """
    ).strip()

    if option == "1":
        passwords = decrypt_passwords(master_password)
        print(passwords)
