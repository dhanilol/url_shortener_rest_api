from random import choice

from string import ascii_letters, digits

from environ import environ

env = environ.Env()

SIZE = env('MAXIMUM_URL_CHARS')
AVAIABLE_CHARS = ascii_letters + digits


def create_random_code(chars=AVAIABLE_CHARS):
    return "".join(
        [choice(chars) for _ in range(int(SIZE))]
    )
