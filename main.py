#!/usr/bin/env python3

from key.getkey import load_key, dump_key, generate_key
from key.login import prompt_login


KEY_ROUNDS = 14  # increase for complexity


if __name__ == "__main__":
    try:
        key = load_key()  # load key from 'key.dat' file

    except:
        key = generate_key(KEY_ROUNDS)  # prompt for new password
        dump_key(key)  # write key to file

    master_password = prompt_login(key)

    if not master_password:
        exit()

#     option = input(
#         """
# 1. List a password
# 2. Create a password
# > """
#     ).strip()

#     if option == "1":
#         passwords = decrypt_passwords(master_password)
#         print(passwords)
