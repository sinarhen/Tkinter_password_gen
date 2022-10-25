from random import choice
from string import ascii_letters, digits


def generate():
    symbols = ascii_letters + digits
    passw = ''
    for i in range(15):
        passw += choice(symbols)
    return passw
