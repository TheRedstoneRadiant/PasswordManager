#!/usr/bin/env python3

from key.getkey import load_key

if __name__ == "__main__":
    try:
        key = load_key()

    except (FileNotFoundError, LoadKeyError):
        key = generate_key(KEY_ROUNDS)

    if not key:
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
