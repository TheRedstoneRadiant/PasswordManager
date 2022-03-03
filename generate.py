#!/usr/bin/env python3

import bcrypt

password = input("Master password: ").encode()
rounds = 14  # set higher for better security

with open("key.dat", "wb") as file:
    file.write(bcrypt.hashpw(password, bcrypt.gensalt(rounds=rounds)))

# https://www.delftstack.com/howto/python/python-aes-encryption/#the-aes-256-using-pycrypto-in-python
