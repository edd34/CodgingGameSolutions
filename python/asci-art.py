# https://www.codingame.com/ide/puzzle/ascii-art

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ?")
def text_to_indexes(my_textes):
    for letter in t.upper():
        if letter in alphabet:
            yield (alphabet.index(letter) * l, alphabet.index(letter) * l + l )
        else:
            yield (alphabet.index("?") * l, alphabet.index("?") * l + l )
# print(text_to_indexes)
for i in range(h):
    res = ""
    row = input()
    for elem in text_to_indexes(row):
        res += row[elem[0]: elem[1]]
    print(res)