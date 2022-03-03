#!/usr/bin/env python3

import bcrypt, getpass

with open("key.dat", "rb") as file:
    key = file.read()

remaining_attempts = 2
master_password = getpass.getpass("Master password: ").encode()

while not bcrypt.checkpw(master_password, key):
    if not remaining_attempts:
        print("3 incorrect password attempts.")
        exit()

    print("Sorry, try again.")
    remaining_attempts -= 1
    master_password = getpass.getpass("Master password: ").encode()


print(master_password)
