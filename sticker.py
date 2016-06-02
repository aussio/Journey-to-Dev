"""
Problem Statement:

You have a sticker machine that can only print stickers with the word "wpengine". Write a function to calculate how many "wpengine" stickers would need to be printed to spell a given other word out of the letters on the sticker. For example, it would take 2 stickers to get the word "winning" from "wpengine" stickers (need 2 i's and 3 n's).
"""
from collections import Counter


def sticker_machine(input_word, sticker_word='wpengine'):
    input_letter_counter = Counter(input_word)
    sticker_letter_counter = Counter(sticker_word)
    count = 0

    if not is_possible_to_print(input_word, sticker_word):
        return -1

    while has_letters_remaining(input_letter_counter):
        count += 1
        input_letter_counter.subtract(sticker_letter_counter)

    return count

def has_letters_remaining(counter):
    for value in counter.values():
        if value > 0:
            return True
    else:
        return False

def is_possible_to_print(input_word, sticker_word):
    for letter in input_word:
        if letter not in sticker_word:
            return False
    else:
        return True
