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
