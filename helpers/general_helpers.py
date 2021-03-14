import random
from string import ascii_lowercase, digits


def generate_string(symbols_count: int):
    gstring = ''.join(random.choices(ascii_lowercase + digits, k=symbols_count))
    return gstring
